"""Minimizar rho sobre la familia I1 de gadgets de 4 aros (best fit falla).
Estructura: r1=10; R = 10 + r2; best fit anida r2 en el agujero (10-w), r3 va a la
sarten, r4 queda bloqueado; testigo: sarten {10, r2}, agujero {r3, r4}.
Condiciones: r2 <= 10-w; r4 > r2-w; r3+r4 <= 10-w; r2+r4 > 10-w;
{10, r3, r4} no empaqueta en R (criterio angular > 360.5)."""
import math, itertools
import numpy as np
from sim import pack_feasible

def asum(A, x, y, R):
    def al(s, t):
        num = (R-s)**2 + (R-t)**2 - (s+t)**2
        return math.degrees(math.acos(max(-1, min(1, num/(2*(R-s)*(R-t))))))
    return al(A,x) + al(A,y) + al(x,y)

best = None
for r2 in np.arange(4.6, 5.5, 0.02):
    R = 10 + r2
    for w in np.arange(0.3, 2.5, 0.05):
        if r2 > 10 - w: continue
        h1 = 10 - w
        for r3 in np.arange(min(r2 - 0.01, h1), max(3.0, r2 - w), -0.02):
            r4lo = max(r2 - w, h1 - r2, 2.5) + 1e-6   # r4 > r2-w y r2+r4 > h1
            r4hi = min(r3 - 0.01, h1 - r3)            # r4 < r3 y r3+r4 <= h1
            if r4hi <= r4lo: continue
            for r4 in np.arange(r4lo, r4hi, 0.02):
                if asum(10, r3, r4, R) > 360.5:
                    rho = max((r2 + r3 + r4)/10, (r3 + r4)/r2)
                    if best is None or rho < best[0]:
                        best = (rho, round(r2,3), round(w,3), round(r3,3), round(r4,3), round(R,3))
if best:
    rho, r2, w, r3, r4, R = best
    print(f"mejor candidato: rho={rho:.3f}  R={R} w={w} radios={{10, {r2}, {r3}, {r4}}}")
    print(f"  cota teorica de la familia: 1 + (1+t)/(1+t+t^2) con t={r2/10:.3f} -> "
          f"{1 + (1+r2/10)/(1+r2/10+(r2/10)**2):.3f}")
    # verificacion completa con el solver
    radii = [10.0, r2, r3, r4]
    print("  solver {10,r3,r4} empaqueta:", pack_feasible([10, r3, r4], R, restarts=80, iters=6000)[0])
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
    def greedy(rule):
        order = sorted(range(4), key=lambda i: -radii[i])
        containers = [{"cap": R, "occ": []}]; placed = []
        for i in order:
            cands = [c for c in containers if radii[i] <= c["cap"] + 1e-9
                     and feas([radii[j] for j in c["occ"]] + [radii[i]], c["cap"])]
            if cands:
                c = min(cands, key=lambda c: c["cap"]) if rule == "best" else max(cands, key=lambda c: c["cap"])
                c["occ"].append(i); placed.append(i)
                if radii[i] - w > 1e-9:
                    containers.append({"cap": radii[i] - w, "occ": []})
        return sorted(radii[i] for i in placed)
    def lexmax():
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
        for i in sorted(range(4), key=lambda i: -radii[i]):
            if sf(L + [i]): L.append(i)
        return sorted(radii[i] for i in L)
    print("  lex-max:", lexmax())
    print("  best   :", greedy("best"))
    print("  worst  :", greedy("worst"))
