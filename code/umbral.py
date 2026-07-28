"""(1) Familia aditiva con rho -> 1+: parametro s = R - r1, w > s/2, 1.5s + w > r1.
    Instancias: r1=10, r2=s, pareja {r3,r4} con suma s+0.1, r4 > r2-w.
(2) Busqueda geometrica de fallos con rho < 1.8 (n=5), best/worst vs lex-max."""
import math, itertools
import numpy as np
from sim import pack_feasible

# ---------- (1) aditivo: rho -> 1 ----------
def add_feas(rs, Rc): return sum(rs) <= Rc + 1e-9

def greedy_add(radii, w, R, rule):
    order = sorted(range(len(radii)), key=lambda i: -radii[i])
    cont = [{"cap": R, "occ": []}]; placed = []
    for i in order:
        cands = [c for c in cont if add_feas([radii[j] for j in c["occ"]] + [radii[i]], c["cap"])
                 and radii[i] <= c["cap"] + 1e-9]
        if cands:
            c = min(cands, key=lambda c: c["cap"]) if rule == "best" else max(cands, key=lambda c: c["cap"])
            c["occ"].append(i); placed.append(i)
            if radii[i] - w > 1e-9: cont.append({"cap": radii[i] - w, "occ": []})
    return len(placed)

def rho(radii):
    rs = sorted(radii, reverse=True)
    return max(sum(rs[i+1:])/rs[i] for i in range(len(rs)-1))

# ---------- (2) geometrico: busqueda bajo Tribonacci ----------
CACHE = {}
def feas(rs, Rc):
    if not rs: return True
    if sum(rs) <= Rc + 1e-9: return True
    srt = sorted(rs, reverse=True)
    if srt[0] > Rc + 1e-9 or (len(srt) > 1 and srt[0]+srt[1] > Rc + 1e-9): return False
    if len(srt) == 2: return True
    key = (tuple(sorted(round(r,3) for r in rs)), round(Rc,3))
    if key not in CACHE:
        CACHE[key] = pack_feasible(list(rs), Rc, restarts=25, iters=2500)[0]
    return CACHE[key]

def greedy_geo(radii, w, R, rule):
    order = sorted(range(len(radii)), key=lambda i: -radii[i])
    cont = [{"cap": R, "occ": []}]; placed = []
    for i in order:
        cands = [c for c in cont if radii[i] <= c["cap"] + 1e-9
                 and feas([radii[j] for j in c["occ"]] + [radii[i]], c["cap"])]
        if cands:
            c = min(cands, key=lambda c: c["cap"]) if rule == "best" else max(cands, key=lambda c: c["cap"])
            c["occ"].append(i); placed.append(i)
            if radii[i] - w > 1e-9: cont.append({"cap": radii[i] - w, "occ": []})
    return frozenset(placed)

def lexmax_geo(radii, w, R):
    def sf(sub):
        ch = [[-1] + [j for j in sub if j != i and radii[i] <= radii[j] - w + 1e-9] for i in sub]
        for ps in itertools.product(*ch):
            pm = dict(zip(sub, ps))
            if not all(pm[i] == -1 or radii[i] < radii[pm[i]] for i in sub): continue
            g = {}
            for i in sub: g.setdefault(pm[i], []).append(i)
            if all(feas([radii[k] for k in kids], R if p == -1 else radii[p] - w)
                   for p, kids in g.items()):
                return True
        return False
    L = []
    for i in sorted(range(len(radii)), key=lambda i: -radii[i]):
        if sf(L + [i]): L.append(i)
    return frozenset(L)


if __name__ == "__main__":
    print("FAMILIA ADITIVA (r1=10): fallos con rho -> 1")
    for s, w in ((6.0, 3.5), (5.1, 2.6), (5.02, 2.52), (5.004, 2.503)):
        R = 10 + s
        r3 = round(s/2 + 0.06, 3); r4 = round(s/2 + 0.04, 3)
        radii = [10.0, s, r3, r4]
        ok = (r4 > s - w and r3 + r4 <= 10 - w and s + r4 > 10 - w and s <= 10 - w
              and 10 + r3 + r4 > R)
        nb = greedy_add(radii, w, R, "best")
        print(f"  s={s} w={w}: rho={rho(radii):.4f}  condiciones={ok}  "
              f"best coloca {nb}/4  (testigo coloca 4)")

    print("\nBUSQUEDA GEOMETRICA rho < 1.80 (n=5, 120 instancias estructuradas):")
    rng = np.random.default_rng(17)
    fails = 0; tried = 0
    while tried < 120:
        r1 = 10.0
        r2 = float(rng.uniform(3.5, 6.5))
        rest = sorted([float(rng.uniform(0.6, r2 - 0.05)) for _ in range(3)], reverse=True)
        radii = [r1, round(r2,2)] + [round(x,2) for x in rest]
        if rho(radii) >= 1.80: continue
        w = round(float(rng.uniform(0.3, 3.0)), 2)
        R = round(float(rng.uniform(10.4, r1 + r2 + 0.6)), 2)
        tried += 1
        L = lexmax_geo(radii, w, R)
        for rule in ("best", "worst"):
            S = greedy_geo(radii, w, R, rule)
            if S != L:
                fails += 1
                print(f"  !! fallo rho={rho(radii):.3f} w={w} R={R} radios={radii} regla={rule}")
    print(f"  fallos con rho < 1.80: {fails} de {tried} instancias x2 reglas")
