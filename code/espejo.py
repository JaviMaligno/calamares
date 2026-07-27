"""(1) Instanciar la familia especular (worst fit falla, best fit acierta).
(2) Buscar un PREFIJO COMPARTIDO (R, r1, r2, w) que admita dos colas opuestas:
    cola I1 (pan-correcto: best falla) y cola I2 (agujero-correcto: worst falla).
    Si existe, ninguna regla funcion-del-estado puede acertar en ambas instancias."""
import math, itertools
import numpy as np
from sim import pack_feasible

def asum(A, x, y, R):
    def al(s, t):
        num = (R-s)**2 + (R-t)**2 - (s+t)**2
        den = 2*(R-s)*(R-t)
        return math.degrees(math.acos(max(-1, min(1, num/den))))
    return al(A,x) + al(A,y) + al(x,y)

# ---------- (1) familia especular ----------
r1, r4, w = 10.0, 4.9, 0.8
def xstar(R):
    lo, hi = r4, min(R - r1, r1)  # umbral de empaquetabilidad de {r1, x, r4} en R
    for _ in range(60):
        mid = (lo + hi) / 2
        if asum(r1, mid, r4, R) < 360: lo = mid
        else: hi = mid
    return lo

R = 15.7
xs = xstar(R)
r3, r2 = round(xs - 0.06, 3), round(xs + 0.06, 3)
print(f"ESPEJO: R={R}, w={w}, umbral x*={xs:.3f} -> radios {{{r1}, {r2}, {r3}, {r4}}}")
ok = (r2 <= R - r1 + 1e-9 and r2 <= r1 - w and w > r2 - r4 and r3 + r4 > r1 - w)
print("  condiciones laterales:", ok)
print("  solver {r1,r3,r4} empaqueta:", pack_feasible([r1,r3,r4], R, restarts=60, iters=5000)[0])
print("  solver {r1,r2,r4} empaqueta:", pack_feasible([r1,r2,r4], R, restarts=80, iters=6000)[0])

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

def greedy(radii, ww, RR, rule):
    order = sorted(range(len(radii)), key=lambda i: -radii[i])
    containers = [{"cap": RR, "occ": []}]
    placed = []
    for i in order:
        cands = [c for c in containers if radii[i] <= c["cap"] + 1e-9
                 and feas([radii[j] for j in c["occ"]] + [radii[i]], c["cap"])]
        if cands:
            c = min(cands, key=lambda c: c["cap"]) if rule == "best" else max(cands, key=lambda c: c["cap"])
            c["occ"].append(i); placed.append(i)
            if radii[i] - ww > 1e-9:
                containers.append({"cap": radii[i] - ww, "occ": []})
    return sorted(radii[i] for i in placed)

def lexmax(radii, ww, RR):
    def sf(sub):
        ch = [[-1] + [j for j in sub if j != i and radii[i] <= radii[j] - ww + 1e-9] for i in sub]
        for ps in itertools.product(*ch):
            pm = dict(zip(sub, ps))
            if not all(pm[i] == -1 or radii[i] < radii[pm[i]] for i in sub): continue
            g = {}
            for i in sub: g.setdefault(pm[i], []).append(i)
            if all(feas([radii[k] for k in kids], RR if p == -1 else radii[p] - ww)
                   for p, kids in g.items()):
                return True
        return False
    L = []
    for i in sorted(range(len(radii)), key=lambda i: -radii[i]):
        if sf(L + [i]): L.append(i)
    return sorted(radii[i] for i in L)

inst = [r1, r2, r3, r4]
print("  lex-max :", lexmax(inst, w, R))
print("  best fit:", greedy(inst, w, R, "best"))
print("  worst   :", greedy(inst, w, R, "worst"))
rs = sorted(inst, reverse=True)
print("  rho =", round(max(sum(rs[i+1:])/rs[i] for i in range(3)), 3))

# ---------- (2) prefijo compartido con colas opuestas ----------
print("\nBUSQUEDA DE PREFIJO COMPARTIDO (r1=10):")
found = None
for ww in (0.5, 0.8, 1.0, 1.2):
    h1 = 10 - ww
    for RR in np.arange(15.2, 16.61, 0.1):
        for rr2 in np.arange(5.0, min(RR - 10, 10 - ww) + 1e-9, 0.05):
            rr2 = round(rr2, 3)
            lo = rr2 - ww + 1e-6
            # cola I1: r4<r3<r2, r3+r4<=h1, r2+r4>h1, alpha(10,r3,r4)>360
            t1 = None
            for rr4 in np.arange(max(lo, 3.5), rr2, 0.05):
                if rr2 + rr4 <= h1: continue
                for rr3 in np.arange(rr4 + 0.03, rr2, 0.05):
                    if rr3 + rr4 > h1: break
                    if asum(10, rr3, rr4, RR) > 360.5:
                        t1 = (round(rr3,3), round(rr4,3)); break
                if t1: break
            if not t1: continue
            # cola I2: r3'+r4'>h1, alpha(10,r3',r4')<360, alpha(10,r2,r4')>360
            t2 = None
            for rr4 in np.arange(max(lo, 3.5), rr2, 0.05):
                if asum(10, rr2, rr4, RR) <= 360.5: continue
                for rr3 in np.arange(rr4 + 0.03, rr2, 0.05):
                    if rr3 + rr4 <= h1: continue
                    if asum(10, rr3, rr4, RR) < 359.5:
                        t2 = (round(rr3,3), round(rr4,3)); break
                if t2: break
            if t2:
                found = (ww, round(RR,2), rr2, t1, t2)
                break
        if found: break
    if found: break

if found:
    ww, RR, rr2, (a3, a4), (b3, b4) = found
    print(f"  PREFIJO: R={RR}, w={ww}, r1=10, r2={rr2}  (estado identico en el paso 2)")
    I1 = [10, rr2, a3, a4]; I2 = [10, rr2, b3, b4]
    print(f"  I1 (correcto=SARTEN): cola {{{a3},{a4}}}: best={greedy(I1,ww,RR,'best')} worst={greedy(I1,ww,RR,'worst')} lexmax={lexmax(I1,ww,RR)}")
    print(f"  I2 (correcto=AGUJERO): cola {{{b3},{b4}}}: best={greedy(I2,ww,RR,'best')} worst={greedy(I2,ww,RR,'worst')} lexmax={lexmax(I2,ww,RR)}")
else:
    print("  no encontrado en la rejilla explorada")
