"""Si el teorema nuevo es cierto, CUALQUIER regla de colocacion (best fit,
worst fit, aleatoria) da el mismo conjunto optimo bajo superincrecencia.
Prediccion fuerte: worst fit y aleatorio tampoco fallan nunca en area."""
import numpy as np
from superinc import feasible, a, optimum, random_superincreasing

def greedy_rule(radii, w, R, rule, rng=None):
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
    return len(placed), sum(a(radii[i], w) for i in placed)

rng = np.random.default_rng(23)
fails = {"best": 0, "worst": 0, "rand": 0}
trials = 100
for t in range(trials):
    n = int(rng.integers(4, 7))
    radii = random_superincreasing(rng, n, 10.0)
    w = round(float(rng.uniform(0.4, 3.0)), 2)
    o = optimum(radii, w, 10.0)
    for rule in fails:
        g = greedy_rule(radii, w, 10.0, rule, rng)
        if o[1] > g[1] + 1e-6:
            fails[rule] += 1
            print(f"  !! {rule} falla: w={w} radios={radii} g={g} opt={o}")
print(f"{trials} instancias superincrecientes, fallos de area por regla: {fails}")
