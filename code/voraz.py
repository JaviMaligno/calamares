"""Voraz: ordenar aros de mayor a menor; colocar cada uno en el contenedor factible
mas restrictivo (best fit). Comparar contra el optimo exacto (enumeracion) en las
dos metricas. Cache de factibilidad COMPARTIDA entre voraz y enumerador para que
el ruido numerico del solver no fabrique contraejemplos falsos.
"""
import itertools, math
import numpy as np
from sim import pack_feasible, contact_area

CACHE = {}
def feasible(radii, Rc):
    key = (tuple(sorted(round(r, 4) for r in radii)), round(Rc, 4))
    if key not in CACHE:
        CACHE[key] = pack_feasible(list(radii), Rc, restarts=15, iters=1500)[0]
    return CACHE[key]

def greedy(radii, w, R):
    order = sorted(range(len(radii)), key=lambda i: -radii[i])
    containers = [{"cap": R, "occ": []}]          # la sarten
    placed = []
    for i in order:
        r = radii[i]
        cands = [c for c in containers if r <= c["cap"] + 1e-12
                 and feasible([radii[j] for j in c["occ"]] + [r], c["cap"])]
        if not cands:
            continue
        best = min(cands, key=lambda c: c["cap"])  # el mas restrictivo
        best["occ"].append(i)
        placed.append(i)
        if r - w > 1e-9:
            containers.append({"cap": r - w, "occ": []})
    cnt = len(placed)
    area = sum(contact_area(radii[i], w) for i in placed)
    return cnt, area, placed

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
            ok = True
            for parent, kids in groups.items():
                Rc = R if parent == -1 else radii[parent] - w
                if not feasible([radii[k] for k in kids], Rc):
                    ok = False; break
            if ok:
                cnt = len(sub)
                area = sum(contact_area(radii[i], w) for i in sub)
                best_cnt = max(best_cnt, cnt)
                best_area = max(best_area, area)
                break  # este subconjunto ya es realizable: cnt y area solo dependen del subconjunto
    return best_cnt, best_area

if __name__ == "__main__":
    R, w = 10.0, 1.0

    # 1) contraejemplo analitico
    radii = [8.2, 4.6, 4.6, 4.6]
    g = greedy(radii, w, R)
    o = optimum(radii, w, R)
    print(f"Contraejemplo {radii}:")
    print(f"  voraz : N={g[0]}, A={g[1]:.1f}, coloca indices {sorted(g[2])}")
    print(f"  optimo: N={o[0]}, A={o[1]:.1f}")

    # 2) experimentos aleatorios
    rng = np.random.default_rng(7)
    fail_area = fail_cnt = trials = 0
    worst = None
    for t in range(80):
        n = rng.integers(4, 6)
        radii = [round(float(x), 1) for x in rng.uniform(1.5, 9.5, n)]
        g = greedy(radii, w, R)
        o = optimum(radii, w, R)
        trials += 1
        fa = o[1] > g[1] + 1e-6
        fc = o[0] > g[0]
        fail_area += fa; fail_cnt += fc
        if fa and (worst is None or o[1] - g[1] > worst[0]):
            worst = (o[1] - g[1], radii, g[:2], o)
    print(f"\n{trials} instancias aleatorias (n=4-5, radios U[1.5,9.5]):")
    print(f"  voraz suboptimo en AREA  : {fail_area} ({100*fail_area/trials:.0f}%)")
    print(f"  voraz suboptimo en NUMERO: {fail_cnt} ({100*fail_cnt/trials:.0f}%)")
    if worst:
        print(f"  peor brecha de area: {worst[0]:.1f} en radios={worst[1]}  "
              f"voraz(N,A)={worst[2]}  optimo(N,A)=({worst[3][0]},{worst[3][1]:.1f})")
