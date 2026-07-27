import numpy as np, math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Annulus
from sim import pack_feasible, contact_area, enumerate_configs

R, w = 10.0, 1.0
radii = [9.0, 4.2, 4.2, 4.2]
res = enumerate_configs(radii, w, R)
best_count = max(res, key=lambda t: (t[0], t[1]))
best_area  = max(res, key=lambda t: (t[1], t[0]))

def absolute_positions(pmap, placements):
    """Convierte posiciones relativas a cada contenedor en absolutas (la sarten en el origen)."""
    abs_pos = {}
    pending = dict()
    for parent, (kids, pos) in placements.items():
        for k, p in zip(kids, pos):
            pending[k] = (parent, np.array(p))
    def resolve(k):
        if k in abs_pos: return abs_pos[k]
        parent, rel = pending[k]
        base = np.zeros(2) if parent == -1 else resolve(parent)
        abs_pos[k] = base + rel
        return abs_pos[k]
    for k in pending: resolve(k)
    return abs_pos

fig, axes = plt.subplots(1, 2, figsize=(12, 6.4))
configs = [(best_area, "Máx. ÁREA"), (best_count, "Máx. NÚMERO")]
colors = ["#e07b39", "#3a86c8", "#57a05a", "#9b6ec8"]

for ax, (cfg, title) in zip(axes, configs):
    cnt, area, pmap, placements = cfg
    ax.add_patch(Circle((0, 0), R, fill=True, fc="#2b2b2b", ec="black", lw=3))
    pos = absolute_positions(pmap, placements)
    for ci, (k, p) in enumerate(sorted(pos.items())):
        r = radii[k]
        ax.add_patch(Annulus(tuple(p), r, w, fc=colors[ci % 4], ec="black", lw=1, alpha=0.95))
    ax.set_xlim(-R-0.5, R+0.5); ax.set_ylim(-R-0.5, R+0.5)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(f"{title}\nN = {cnt} aros,  A = {area:.1f} u²", fontsize=13)

fig.suptitle(f"Sartén R={R}, grosor w={w}, inventario de radios {radii}", fontsize=13)
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/divergencia_calamares.png", dpi=150, bbox_inches="tight")
print("guardado")
