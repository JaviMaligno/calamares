import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Annulus

R, w = 15.0, 0.3
fig, axes = plt.subplots(1, 2, figsize=(12.5, 6.6))

def pan(ax):
    ax.add_patch(Circle((0,0), R, fc="#2b2b2b", ec="black", lw=3))
    ax.set_xlim(-R-1, R+1); ax.set_ylim(-R-1, R+1)
    ax.set_aspect("equal"); ax.axis("off")

# izquierda: best fit bloqueado
ax = axes[0]; pan(ax)
ax.add_patch(Annulus((-5,0), 10, w, fc="#e07b39", ec="k", lw=1))     # r1=10
ax.add_patch(Annulus((-5,0), 5, w, fc="#3a86c8", ec="k", lw=1))      # r2=5 anidado
ax.add_patch(Annulus((10.1,0), 4.9, w, fc="#57a05a", ec="k", lw=1))  # r3=4.9 en sarten
ax.add_patch(Annulus((12.5,-12.5), 4.8, w, fc="#888888", ec="k", lw=1, alpha=0.55))
ax.annotate("4.8 bloqueado", (12.5,-12.5), ha="center", va="center", fontsize=9, color="white")
ax.set_title("BEST FIT: anida el 5 y pierde el 4.8\n(coloca 3 aros)", fontsize=12)

# derecha: testigo (= worst fit)
ax = axes[1]; pan(ax)
ax.add_patch(Annulus((-5,0), 10, w, fc="#e07b39", ec="k", lw=1))
ax.add_patch(Annulus((10,0), 5, w, fc="#3a86c8", ec="k", lw=1))      # r2=5 en sarten, tangente
ax.add_patch(Annulus((-9.8,0), 4.9, w, fc="#57a05a", ec="k", lw=1))  # dentro del agujero del 10
ax.add_patch(Annulus((-0.1,0), 4.8, w, fc="#9b6ec8", ec="k", lw=1))
ax.set_title("TESTIGO (= worst fit): el 5 a la sartén,\nla pareja {4.9, 4.8} llena el agujero (4 aros)", fontsize=12)

fig.suptitle("Contraejemplo n=4 a la conjetura fuerte: R=15, w=0.3, radios {10, 5, 4.9, 4.8}", fontsize=13)
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/contraejemplo_n4.png", dpi=150, bbox_inches="tight")
print("ok")
