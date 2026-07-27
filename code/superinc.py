"""Caso superincreciente: r_i > suma de todos los radios menores.
Funcion de area CORRECTA incluyendo discos (r <= w, sin agujero):
  a(r) = pi * (r^2 - max(0, r-w)^2)
Experimentos: voraz (best-fit) vs optimo exacto, metricas area y numero.
"""
import itertools, math
import numpy as np
from sim import pack_feasible

CACHE = {}
def feasible(radii, Rc):
    if not radii:
        return True
    if sum(radii) <= Rc + 1e-12:          # suficiente: empaquetado en fila sobre un diametro
        return True
    srt = sorted(radii, reverse=True)
    if srt[0] > Rc + 1e-12:               # necesario
        return False
    if len(srt) >= 2 and srt[0] + srt[1] > Rc + 1e-12:   # necesario (dos mayores)
        return False
    if sum(r*r for r in radii) > Rc*Rc + 1e-12:          # necesario (area)
        return False
    key = (tuple(sorted(round(r, 4) for r in radii)), round(Rc, 4))
    if key not in CACHE:
        CACHE[key] = pack_feasible(list(radii), Rc, restarts=12, iters=1200)[0]
    return CACHE[key]

def a(r, w):
    return math.pi * (r*r - max(0.0, r - w)**2)

def greedy(radii, w, R):
    order = sorted(range(len(radii)), key=lambda i: -radii[i])
    containers = [{"cap": R, "occ": []}]
    placed = []
    for i in order:
        r = radii[i]
        cands = [c for c in containers if r <= c["cap"] + 1e-12
                 and feasible([radii[j] for j in c["occ"]] + [r], c["cap"])]
        if not cands:
            continue
        best = min(cands, key=lambda c: c["cap"])
        best["occ"].append(i); placed.append(i)
        if r - w > 1e-9:
            containers.append({"cap": r - w, "occ": []})
    return len(placed), sum(a(radii[i], w) for i in placed), placed

def optimum(radii, w, R):
    n = len(radii)
    best_cnt, best_area = 0, 0.0
    for mask in range(1, 1 << n):
        sub = [i for i in range(n) if mask >> i & 1]
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
                best_cnt = max(best_cnt, len(sub))
                best_area = max(best_area, sum(a(radii[i], w) for i in sub))
                break
    return best_cnt, best_area

def random_superincreasing(rng, n, R):
    total, rs = 0.0, []
    for _ in range(n):
        r = total + rng.uniform(0.2, 1.5)
        rs.append(r); total += r
    rs = rs[::-1]
    s = rng.uniform(6.0, 9.9) / rs[0]
    return [round(r * s, 2) for r in rs]

if __name__ == "__main__":
    R = 10.0

    # contraejemplo analitico para NUMERO bajo superincrecientes
    w = 4.8
    radii = [9.95, 5.0, 4.3, 0.6]
    si = all(radii[i] > sum(radii[i+1:]) for i in range(len(radii)))
    g = greedy(radii, w, R); o = optimum(radii, w, R)
    print(f"Contraejemplo numero (superincreciente={si}), w={w}, radios={radii}:")
    print(f"  voraz : N={g[0]}, A={g[1]:.1f}")
    print(f"  optimo: N={o[0]}, A={o[1]:.1f}")

    # experimentos aleatorios superincrecientes
    rng = np.random.default_rng(11)
    trials = fail_area = fail_cnt = 0
    for t in range(120):
        n = int(rng.integers(4, 7))
        radii = random_superincreasing(rng, n, R)
        w = round(float(rng.uniform(0.4, 3.0)), 2)
        g = greedy(radii, w, R); o = optimum(radii, w, R)
        trials += 1
        if o[1] > g[1] + 1e-6:
            fail_area += 1
            print(f"  !! AREA falla: w={w} radios={radii} voraz={g[:2]} opt={o}")
        if o[0] > g[0]:
            fail_cnt += 1
    print(f"\n{trials} instancias superincrecientes aleatorias (n=4-6, w=U[0.4,3]):")
    print(f"  voraz suboptimo en AREA  : {fail_area}")
    print(f"  voraz suboptimo en NUMERO: {fail_cnt}")
