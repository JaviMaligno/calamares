"""Frontera de la irrelevancia de colocacion.
(1) Modelo ADITIVO (hermanos factibles sii suma <= capacidad): contraejemplo exacto.
(2) Modelo GEOMETRICO: gadget al filo (margenes ~0.01) con tres grandes ajustados.
"""
import numpy as np, itertools
from sim import pack_feasible

# ---------- modelo aditivo (aritmetica exacta, sin solver) ----------
def add_feasible(radii, Rc):
    return sum(radii) <= Rc + 1e-9

def greedy_add(radii, w, R, rule):
    order = sorted(range(len(radii)), key=lambda i: -radii[i])
    containers = [{"cap": R, "occ": []}]
    placed = []
    for i in order:
        cands = [c for c in containers
                 if add_feasible([radii[j] for j in c["occ"]] + [radii[i]], c["cap"])]
        if cands:
            c = min(cands, key=lambda c: c["cap"]) if rule == "best" else max(cands, key=lambda c: c["cap"])
            c["occ"].append(i); placed.append(i)
            if radii[i] - w > 1e-9:
                containers.append({"cap": radii[i] - w, "occ": []})
    return sorted(radii[i] for i in placed)

R, w = 13.5, 2.0
radii = [8.0, 5.5, 3.5, 2.8, 2.8]
print("ADITIVO, R=13.5, w=2, radios", radii)
for rule in ("best", "worst"):
    print(f"  {rule} fit coloca:", greedy_add(radii, w, R, rule))
print("  testigo manual: sarten {8, 5.5}=13.5; agujero de 8 (cap 6): {2.8, 2.8}=5.6;")
print("  agujero de 5.5 (cap 3.5): {3.5}. Coloca los CINCO.")
rho = max(sum(sorted(radii, reverse=True)[i+1:]) / sorted(radii, reverse=True)[i]
          for i in range(len(radii)-1))
print(f"  rho de superincrecencia = {rho:.2f}  (>1: no superincreciente)")

# ---------- gadget geometrico al filo ----------
CACHE = {}
def geo_feasible(radii, Rc):
    if not radii: return True
    if sum(radii) <= Rc + 1e-12: return True
    srt = sorted(radii, reverse=True)
    if srt[0] > Rc + 1e-12: return False
    if len(srt) >= 2 and srt[0] + srt[1] > Rc + 1e-12: return False
    key = (tuple(sorted(round(r, 4) for r in radii)), round(Rc, 4))
    if key not in CACHE:
        CACHE[key] = pack_feasible(list(radii), Rc, restarts=60, iters=6000)[0]
    return CACHE[key]

def greedy_geo(radii, w, R, rule):
    order = sorted(range(len(radii)), key=lambda i: -radii[i])
    containers = [{"cap": R, "occ": []}]
    placed = []
    for i in order:
        cands = [c for c in containers if radii[i] <= c["cap"] + 1e-12
                 and geo_feasible([radii[j] for j in c["occ"]] + [radii[i]], c["cap"])]
        if cands:
            c = min(cands, key=lambda c: c["cap"]) if rule == "best" else max(cands, key=lambda c: c["cap"])
            c["occ"].append(i); placed.append(i)
            if radii[i] - w > 1e-9:
                containers.append({"cap": radii[i] - w, "occ": []})
    return sorted(radii[i] for i in placed)

Rg, wg = 10.05, 0.1
gadget = [4.65, 4.635, 4.63, 2.3, 2.27, 2.27]
print(f"\nGEOMETRICO (gadget al filo), R={Rg}, w={wg}, radios {gadget}")
print("  ¿tres grandes caben en la sarten?", geo_feasible(gadget[:3], Rg))
print("  ¿sarten acepta ademas un 2.27 (bolsillo)?", geo_feasible(gadget[:3] + [2.27], Rg))
for rule in ("best", "worst"):
    print(f"  {rule} fit coloca:", greedy_geo(gadget, wg, Rg, rule))
