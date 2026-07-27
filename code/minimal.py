"""Condicion minima (n=3, a=10): mapa de rompibilidad del voraz sobre (b,c),
buscando para cada celda algun (R,w) donde falle en area. Version corregida:
contenedores con identidad por indice.
"""
import numpy as np
from superinc import feasible, a as area_fn, optimum

def greedy_runs(radii, w, R):
    order = sorted(range(len(radii)), key=lambda i: -radii[i])
    results = []
    def rec(k, caps, occs, placed, mode):
        if k == len(order):
            results.append(sum(area_fn(radii[i], w) for i in placed)); return
        i = order[k]; r = radii[i]
        cands = [ci for ci in range(len(caps)) if r <= caps[ci] + 1e-12
                 and feasible([radii[j] for j in occs[ci]] + [r], caps[ci])]
        if not cands:
            rec(k + 1, caps, occs, placed, mode); return
        if mode == "best":
            cands = [min(cands, key=lambda ci: caps[ci])]
        for ci in cands:
            new_occs = [o + [i] if x == ci else o for x, o in enumerate(occs)]
            new_caps = list(caps)
            if r - w > 1e-9:
                new_caps.append(r - w); new_occs.append([])
            rec(k + 1, new_caps, new_occs, placed + [i], mode)
    rec(0, [R], [[]], [], "best"); best = results[0]
    results = []
    rec(0, [R], [[]], [], "all"); worst = min(results)
    return best, worst

if __name__ == "__main__":
    grid = {}
    for b in np.arange(0.5, 10.01, 0.25):
        for c in np.arange(0.5, b + 1e-9, 0.25):
            radii = [10.0, round(float(b), 2), round(float(c), 2)]
            broken_sel = broken_pla = False
            for R in np.arange(10.0, 20.01, 0.5):
                for w in np.arange(0.25, 9.76, 0.25):
                    o = optimum(radii, w, R)[1]
                    gb, gw = greedy_runs(radii, w, R)
                    if o > gb + 1e-6: broken_sel = True
                    if o > gw + 1e-6: broken_pla = True
                    if broken_sel and broken_pla: break
                if broken_sel and broken_pla: break
            grid[(round(float(b),2), round(float(c),2))] = (broken_sel, broken_pla)

    mismatch_pred = mismatch_si = diff_sel_pla = 0
    disagr = []
    for (b, c), (bs_, bp_) in grid.items():
        pred = 30 < 2*b + 3*c
        si_viol = 10 < b + c
        if pred != bs_: mismatch_pred += 1; disagr.append((b, c, bs_, pred))
        if si_viol != bs_: mismatch_si += 1
        if bs_ != bp_: diff_sel_pla += 1
    print(f"{len(grid)} celdas.")
    print(f"desacuerdos con prediccion 3a<2b+3c : {mismatch_pred}")
    print(f"desacuerdos con superincrecencia    : {mismatch_si}")
    print(f"celdas donde la colocacion cambia la rompibilidad: {diff_sel_pla}")
    for b, c, bs_, pred in sorted(disagr)[:12]:
        print(f"  b={b}, c={c}: rompible={bs_}, prediccion={pred}")
    np.save("grid_minimal.npy", np.array([(b, c, int(s), int(p)) for (b,c),(s,p) in grid.items()]))
