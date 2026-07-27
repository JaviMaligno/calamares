"""Instancias gemelas con PREFIJO COMPARTIDO (R=15, r1=10, r2=5, w=0.505):
  I1 = {10, 5, 4.99, 4.50}: correcto en el paso 2 = SARTEN  (best fit falla)
  I2 = {10, 5, 4.76, 4.74}: correcto en el paso 2 = AGUJERO (worst fit falla)
En el paso 2 el estado (sarten con el 10; agujero vacio 9.495; aro entrante 5)
es IDENTICO: ninguna regla funcion-del-estado acierta en ambas."""
import math, itertools
from sim import pack_feasible

R, w = 15.0, 0.505
I1 = [10.0, 5.0, 4.99, 4.50]
I2 = [10.0, 5.0, 4.76, 4.74]

def asum(A, x, y):
    def al(s, t):
        num = (R-s)**2 + (R-t)**2 - (s+t)**2
        return math.degrees(math.acos(max(-1, min(1, num/(2*(R-s)*(R-t))))))
    return al(A,x) + al(A,y) + al(x,y)

print(f"h1 = {10-w}")
print(f"alpha {{10,4.99,4.50}}: {asum(10,4.99,4.50):.1f} (>360: no empaqueta)")
print(f"alpha {{10,4.76,4.74}}: {asum(10,4.76,4.74):.1f} (<360: empaqueta)")
print("solver {10,4.99,4.50} en 15:", pack_feasible([10,4.99,4.5], R, restarts=80, iters=6000)[0])
print("solver {10,4.76,4.74} en 15:", pack_feasible([10,4.76,4.74], R, restarts=80, iters=6000)[0])
print("solver {4.99,4.50} en 9.495:", pack_feasible([4.99,4.5], 10-w)[0])
print("solver {4.76,4.74} en 9.495:", pack_feasible([4.76,4.74], 10-w)[0], "(9.5 > 9.495: debe ser False)")

CACHE = {}
def feas(rs, Rc):
    if not rs: return True
    if sum(rs) <= Rc + 1e-9: return True
    srt = sorted(rs, reverse=True)
    if srt[0] > Rc + 1e-9 or (len(srt) > 1 and srt[0]+srt[1] > Rc + 1e-9): return False
    if len(srt) == 2: return True
    key = (tuple(sorted(round(r,4) for r in rs)), round(Rc,4))
    if key not in CACHE:
        CACHE[key] = pack_feasible(list(rs), Rc, restarts=60, iters=5000)[0]
    return CACHE[key]

def greedy(radii, rule):
    order = sorted(range(len(radii)), key=lambda i: -radii[i])
    containers = [{"cap": R, "occ": []}]
    placed = []
    for i in order:
        cands = [c for c in containers if radii[i] <= c["cap"] + 1e-9
                 and feas([radii[j] for j in c["occ"]] + [radii[i]], c["cap"])]
        if cands:
            c = min(cands, key=lambda c: c["cap"]) if rule == "best" else max(cands, key=lambda c: c["cap"])
            c["occ"].append(i); placed.append(i)
            if radii[i] - w > 1e-9:
                containers.append({"cap": radii[i] - w, "occ": []})
    return sorted(radii[i] for i in placed)

def lexmax(radii):
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
    return sorted(radii[i] for i in L)

for name, inst in (("I1 (correcto=sarten)", I1), ("I2 (correcto=agujero)", I2)):
    rs = sorted(inst, reverse=True)
    rho = max(sum(rs[i+1:])/rs[i] for i in range(3))
    print(f"\n{name}: {inst}  rho={rho:.3f}")
    print(f"  lex-max: {lexmax(inst)}")
    print(f"  best   : {greedy(inst,'best')}")
    print(f"  worst  : {greedy(inst,'worst')}")
