"""Busqueda del rho minimo de fallo en el modelo aditivo (exacto y rapido).
rho = max_i (suma de radios menores que r_i) / r_i. Superincreciente: rho < 1."""
import itertools
import numpy as np
from frontera import greedy_add, add_feasible

def lexmax_add(radii, w, R):
    order = sorted(range(len(radii)), key=lambda i: -radii[i])
    S = []
    def set_ok(sub):
        choices = [[-1] + [j for j in sub if j != i and radii[i] <= radii[j] - w + 1e-9]
                   for i in sub]
        for parents in itertools.product(*choices):
            pmap = dict(zip(sub, parents))
            if not all(pmap[i] == -1 or radii[i] < radii[pmap[i]] for i in sub):
                continue
            groups = {}
            for i in sub:
                groups.setdefault(pmap[i], []).append(i)
            if all(add_feasible([radii[k] for k in kids], R if p == -1 else radii[p] - w)
                   for p, kids in groups.items()):
                return True
        return False
    for i in order:
        if set_ok(S + [i]):
            S.append(i)
    return sorted(radii[i] for i in S)

def rho(radii):
    rs = sorted(radii, reverse=True)
    return max(sum(rs[i+1:]) / rs[i] for i in range(len(rs)-1))

rng = np.random.default_rng(3)
best_rho = None
R = 10.0
for t in range(4000):
    n = int(rng.integers(4, 7))
    radii = [round(float(x), 2) for x in rng.uniform(0.5, 9.0, n)]
    w = round(float(rng.uniform(0.3, 3.0)), 2)
    L = lexmax_add(radii, w, R)
    for rule in ("best", "worst"):
        S = greedy_add(radii, w, R, rule)
        if S != L:
            r = rho(radii)
            if best_rho is None or r < best_rho[0]:
                best_rho = (r, rule, radii, w, S, L)
print("instancia de fallo con rho minimo encontrada:")
if best_rho:
    r, rule, radii, w, S, L = best_rho
    print(f"  rho={r:.3f}  regla={rule}  w={w}  radios={sorted(radii, reverse=True)}")
    print(f"  coloca {S}  vs lex-max {L}")
else:
    print("  ninguna en 4000 instancias")
