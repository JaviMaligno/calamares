"""Busqueda de la condicion minima: ¿cuando importa la regla de colocacion?
Comparamos el CONJUNTO colocado por best/worst/random fit contra el conjunto
lex-maximo factible (el que logra el voraz de seleccion con oraculo).
Medimos la violacion de superincrecencia: rho = max_i (suma radios menores)/r_i.
rho <= 1: superincreciente (teorema: no puede fallar). Buscamos fallos y su rho.
"""
import itertools
import numpy as np
from superinc import feasible, a

def set_feasible(idx_sub, radii, w, R):
    sub = list(idx_sub)
    choices = [[-1] + [j for j in sub if j != i and radii[i] <= radii[j] - w + 1e-9]
               for i in sub]
    for parents in itertools.product(*choices):
        pmap = dict(zip(sub, parents))
        if not all(pmap[i] == -1 or radii[i] < radii[pmap[i]] for i in sub):
            continue
        groups = {}
        for i in sub:
            groups.setdefault(pmap[i], []).append(i)
        if all(feasible([radii[k] for k in kids], R if p == -1 else radii[p] - w)
               for p, kids in groups.items()):
            return True
    return False

def lexmax(radii, w, R):
    order = sorted(range(len(radii)), key=lambda i: -radii[i])
    S = []
    for i in order:
        if set_feasible(S + [i], radii, w, R):
            S.append(i)
    return frozenset(S)

def greedy_rule(radii, w, R, rule, rng):
    order = sorted(range(len(radii)), key=lambda i: -radii[i])
    containers = [{"cap": R, "occ": []}]
    placed = []
    for i in order:
        r = radii[i]
        cands = [c for c in containers if r <= c["cap"] + 1e-12
                 and feasible([radii[j] for j in c["occ"]] + [r], c["cap"])]
        if cands:
            if rule == "best":   c = min(cands, key=lambda c: c["cap"])
            elif rule == "worst": c = max(cands, key=lambda c: c["cap"])
            else:                 c = cands[rng.integers(len(cands))]
            c["occ"].append(i); placed.append(i)
            if r - w > 1e-9:
                containers.append({"cap": r - w, "occ": []})
    return frozenset(placed)

def rho_super(radii):
    rs = sorted(radii, reverse=True)
    return max(sum(rs[i+1:]) / rs[i] for i in range(len(rs)-1))

rng = np.random.default_rng(5)
R = 10.0
fails = []
for t in range(300):
    kind = t % 3
    if kind == 0:      # uniforme
        n = int(rng.integers(4, 7))
        radii = [round(float(x), 2) for x in rng.uniform(1.0, 9.0, n)]
        w = round(float(rng.uniform(0.5, 2.5)), 2)
    elif kind == 1:    # estructurado: 2-3 grandes comparables + mediano + pequenos
        nb = int(rng.integers(2, 4))
        bigs = [round(float(rng.uniform(3.8, 4.6)), 2) for _ in range(nb)]
        mid = round(float(rng.uniform(2.0, 3.6)), 2)
        smalls = [round(float(rng.uniform(1.0, 2.4)), 2) for _ in range(int(rng.integers(1, 3)))]
        radii = bigs + [mid] + smalls
        w = round(float(rng.uniform(0.5, 2.0)), 2)
    else:              # casi-superincreciente perturbado (rho ~ 1)
        n = int(rng.integers(4, 6))
        total, rs = 0.0, []
        for _ in range(n):
            r = total * float(rng.uniform(0.8, 1.3)) + float(rng.uniform(0.2, 1.0))
            rs.append(r); total += r
        s = rng.uniform(6.0, 9.9) / rs[-1]
        radii = [round(r * s, 2) for r in rs[::-1]]
        w = round(float(rng.uniform(0.4, 2.0)), 2)
    L = lexmax(radii, w, R)
    for rule in ("best", "worst", "rand"):
        S = greedy_rule(radii, w, R, rule, rng)
        if S != L:
            fails.append((rule, rho_super(radii), radii, w, sorted(radii[i] for i in S),
                          sorted(radii[i] for i in L)))

print(f"{len(fails)} fallos (regla != lex-max) en 300x3 ejecuciones")
if fails:
    fails.sort(key=lambda f: f[1])
    print("rho minimo entre fallos:", round(fails[0][1], 3))
    for f in fails[:8]:
        print(f"  {f[0]} rho={f[1]:.2f} w={f[3]} radios={f[2]}")
        print(f"      coloca {f[4]}  vs lex-max {f[5]}")
