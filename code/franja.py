"""Diagrama de fases de la divergencia entre metricas.
Familia: sarten R=10, w=1, un aro grande b + pequenos ilimitados de radio rho.
Config A (con grande): grande centrado + n_hole pequenos en su agujero (h = b - w).
Config B (sin grande): n_pan pequenos en la sarten.
Umbrales exactos de n circulos iguales en disco unidad (optimos demostrados, n<=10):
 n=2..k en anillo: q_k = 1/(1 + 1/sin(pi/k)); n=7 igual que 6 (anillo+centro); n=10 especial.
"""
import numpy as np, math
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

R, w = 10.0, 1.0

def ring_ratio(k):
    return 1.0 / (1.0 + 1.0 / math.sin(math.pi / k))

# ratio maximo q_n = rho/Rc para que quepan n circulos iguales
Q = {1: 1.0, 2: 0.5}
for k in range(3, 7):
    Q[k] = ring_ratio(k)          # anillo de k
Q[7] = Q[6]                        # 6 en anillo + 1 centro, mismo ratio 1/3
Q[8] = ring_ratio(7)               # 7 en anillo + centro
Q[9] = ring_ratio(8)               # 8 en anillo + centro
Q[10] = 0.262258924                # empaquetamiento especial (valor conocido)

def maxfit(q):
    """max n circulos iguales de ratio q en disco unidad (n<=10; requiere q >= Q[10])."""
    best = 0
    for n in range(1, 11):
        if q <= Q[n] + 1e-12:
            best = n
    return best

def a(r):  # superficie de contacto de un aro
    return math.pi * w * (2*r - w)

rhos = np.arange(2.65, 5.201, 0.01)
bs   = np.arange(4.80, 9.801, 0.01)
grid = np.zeros((len(bs), len(rhos)), dtype=int)

for i, b in enumerate(bs):
    h = b - w
    for j, rho in enumerate(rhos):
        n_pan  = maxfit(rho / R)
        n_hole = maxfit(rho / h) if rho <= h else 0
        A_cnt, A_area = 1 + n_hole, a(b) + n_hole * a(rho)
        B_cnt, B_area = n_pan, n_pan * a(rho)
        if B_cnt > A_cnt and A_area > B_area:
            grid[i, j] = 2   # DIVERGENCIA: numero->sin grande, area->con grande
        elif A_cnt > B_cnt and B_area > A_area:
            grid[i, j] = 3   # divergencia inversa (esperamos vacio)
        elif A_area >= B_area and A_cnt >= B_cnt:
            grid[i, j] = 1   # coinciden: el grande domina
        else:
            grid[i, j] = 0   # coinciden: mejor sin el grande

vals, counts = np.unique(grid, return_counts=True)
print("celdas por clase:", dict(zip(vals.tolist(), counts.tolist())))
frac = (grid == 2).mean()
print(f"fraccion divergente del rectangulo explorado: {frac:.3f}")
# extremos de la franja
ii, jj = np.where(grid == 2)
if len(ii):
    print(f"rho en [{rhos[jj].min():.2f}, {rhos[jj].max():.2f}], b en [{bs[ii].min():.2f}, {bs[ii].max():.2f}]")

cmap = ListedColormap(["#c7d9ec", "#f2c9a1", "#c0392b", "#7d3c98"])
fig, ax = plt.subplots(figsize=(9, 7))
ax.imshow(grid, origin="lower", aspect="auto", cmap=cmap, vmin=0, vmax=3,
          extent=[rhos[0], rhos[-1], bs[0], bs[-1]])
ax.plot([4.2], [9.0], "k*", ms=16, mec="white")
ax.annotate("ejemplo anterior\n(9.0, 4.2)", (4.2, 9.0), textcoords="offset points",
            xytext=(12, -28), fontsize=10)
ax.set_xlabel("radio de los aros pequeños ρ", fontsize=12)
ax.set_ylabel("radio del aro grande b", fontsize=12)
ax.set_title(f"¿Divergen las métricas? Sartén R={R}, w={w}\n(grande b + pequeños ρ ilimitados)", fontsize=12)
legend = [Patch(fc="#c7d9ec", label="coinciden: mejor SIN el grande"),
          Patch(fc="#f2c9a1", label="coinciden: el grande domina"),
          Patch(fc="#c0392b", label="DIVERGEN: área→grande, número→sin grande"),
          Patch(fc="#7d3c98", label="divergencia inversa")]
ax.legend(handles=legend, loc="lower left", fontsize=9, framealpha=0.9)
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/franja_divergencia.png", dpi=150, bbox_inches="tight")
print("guardado")
