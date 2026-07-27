"""Contraejemplo candidato a la conjetura fuerte (n=4):
R = 15, w = 0.3, radios {10, 5, 4.9, 4.8}.
Claves: pan {10,5} = 15 exacto; agujero del 10 (9.7) = {4.9+4.8} exacto;
{10, 4.9, 4.8} NO empaqueta en 15 (prueba rigurosa + solver).
Best fit anida el 5 -> bloquea el 4.8. Worst fit lo salva."""
import numpy as np, itertools, math
from sim import pack_feasible

R, w = 15.0, 0.3
radii = [10.0, 5.0, 4.9, 4.8]

# --- criterio angular exacto (tres circulos, todos tocando la pared) ---
def alpha(s, t, Rc):
    num = (Rc-s)**2 + (Rc-t)**2 - (s+t)**2
    den = 2*(Rc-s)*(Rc-t)
    return math.degrees(math.acos(max(-1, min(1, num/den))))

A, X, Y = 10.0, 4.9, 4.8
suma = alpha(A,X,R) + alpha(A,Y,R) + alpha(X,Y,R)
print(f"criterio angular {A},{X},{Y} en R={R}: suma = {suma:.1f} grados (>360 => no empaqueta)")

# --- cota rigurosa de |cX - cY| (prueba de infactibilidad) ---
# a = |c_A| en [4.8, 5]; c.u >= (D^2 - |c|^2 - a^2)/(2a) con |c| max
a = 5.0
cxu = (14.9**2 - 10.1**2 - a*a)/(2*a)
cyu = (14.8**2 - 10.2**2 - a*a)/(2*a)
cxv = math.sqrt(10.1**2 - cxu**2)
cyv = math.sqrt(10.2**2 - cyu**2)
d2max = 10.1**2 + 10.2**2 - 2*(cxu*cyu - cxv*cyv)
print(f"cota rigurosa: |cX-cY| <= {math.sqrt(d2max):.2f} < {X+Y} necesario => INFACTIBLE")

# --- solver fisico como contraste ---
print("solver {10,4.9,4.8} en 15:", pack_feasible([10,4.9,4.8], 15.0, restarts=80, iters=6000)[0])
print("solver {10,5} en 15:", pack_feasible([10,5], 15.0)[0])
print("solver {4.9,4.8} en 9.7:", pack_feasible([4.9,4.8], 9.7)[0])

# --- voraz con reglas + lex-max ---
CACHE = {}
def feasible(rs, Rc):
    if not rs: return True
    if sum(rs) <= Rc + 1e-9: return True
    srt = sorted(rs, reverse=True)
    if srt[0] > Rc + 1e-9: return False
    if len(srt) >= 2 and srt[0] + srt[1] > Rc + 1e-9: return False
    if len(srt) == 2: return True
    key = (tuple(sorted(round(r,4) for r in rs)), round(Rc,4))
    if key not in CACHE:
        CACHE[key] = pack_feasible(list(rs), Rc, restarts=60, iters=5000)[0]
    return CACHE[key]

def greedy(rule, rng=None):
    order = sorted(range(4), key=lambda i: -radii[i])
    containers = [{"cap": R, "occ": []}]
    placed = []
    for i in order:
        cands = [c for c in containers if radii[i] <= c["cap"] + 1e-9
                 and feasible([radii[j] for j in c["occ"]] + [radii[i]], c["cap"])]
        if cands:
            c = (min(cands, key=lambda c: c["cap"]) if rule == "best"
                 else max(cands, key=lambda c: c["cap"]))
            c["occ"].append(i); placed.append(i)
            if radii[i] - w > 1e-9:
                containers.append({"cap": radii[i] - w, "occ": []})
    return sorted(radii[i] for i in placed)

def set_feasible(sub):
    choices = [[-1] + [j for j in sub if j != i and radii[i] <= radii[j] - w + 1e-9]
               for i in sub]
    for parents in itertools.product(*choices):
        pmap = dict(zip(sub, parents))
        if not all(pmap[i] == -1 or radii[i] < radii[pmap[i]] for i in sub): continue
        groups = {}
        for i in sub: groups.setdefault(pmap[i], []).append(i)
        if all(feasible([radii[k] for k in kids], R if p == -1 else radii[p] - w)
               for p, kids in groups.items()):
            return True
    return False

L = []
for i in sorted(range(4), key=lambda i: -radii[i]):
    if set_feasible(L + [i]): L.append(i)
print("lex-max:", sorted(radii[i] for i in L))
print("best fit coloca :", greedy("best"))
print("worst fit coloca:", greedy("worst"))
rs = sorted(radii, reverse=True)
print("rho =", round(max(sum(rs[i+1:])/rs[i] for i in range(3)), 3))
