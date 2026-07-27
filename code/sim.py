"""
Calamares en la sarten: aros (radio exterior r, grosor w) en sarten circular de radio R.
- Anidamiento: un aro cabe dentro del agujero de otro si r_hijo <= r_padre - w.
- Hermanos (mismo contenedor) no se solapan: empaquetamiento de circulos en disco.
- Metricas: N = numero de aros colocados; A = suma de pi*w*(2r - w) (superficie de contacto).

Solver de factibilidad: relajacion fisica (empujar solapes, mantener dentro del contenedor),
con reinicios aleatorios.
"""
import numpy as np
import itertools, math, json
from dataclasses import dataclass

rng = np.random.default_rng(42)

def pack_feasible(radii, Rc, restarts=40, iters=4000, tol=1e-6):
    """Devuelve (factible, posiciones) para circulos de radios dados dentro de disco radio Rc."""
    radii = np.array(radii, float)
    n = len(radii)
    if n == 0:
        return True, np.zeros((0, 2))
    if radii.max() > Rc + 1e-12:
        return False, None
    if n == 1:
        return True, np.zeros((1, 2))
    if n == 2:  # condicion exacta
        if radii.sum() <= Rc + 1e-12:
            d = Rc - radii  # colocarlos opuestos
            pos = np.array([[-d[0], 0.0], [d[1], 0.0]])
            return True, pos
        return False, None
    if (radii**2).sum() > Rc**2 + 1e-12:  # cota de area
        return False, None
    for _ in range(restarts):
        pos = rng.uniform(-Rc/2, Rc/2, (n, 2))
        for it in range(iters):
            moved = 0.0
            # resolver solapes por pares
            for i in range(n):
                for j in range(i+1, n):
                    d = pos[j] - pos[i]
                    dist = np.hypot(*d)
                    need = radii[i] + radii[j]
                    if dist < need:
                        if dist < 1e-9:
                            d = rng.normal(size=2); dist = np.hypot(*d)
                        push = (need - dist) / 2 * d / dist
                        pos[i] -= push; pos[j] += push
                        moved += need - dist
            # mantener dentro del contenedor
            for i in range(n):
                dist = np.hypot(*pos[i])
                lim = Rc - radii[i]
                if dist > lim:
                    if dist < 1e-9:
                        pos[i] = 0.0
                    else:
                        pos[i] *= lim / dist
                    moved += dist - lim
            if moved < tol:
                return True, pos
        # comprobacion final por si acabo justo
        ok = True
        for i in range(n):
            if np.hypot(*pos[i]) > Rc - radii[i] + 1e-7: ok = False
            for j in range(i+1, n):
                if np.hypot(*(pos[j]-pos[i])) < radii[i]+radii[j] - 1e-7: ok = False
        if ok:
            return True, pos
    return False, None


def contact_area(r, w):
    return math.pi * w * (2*r - w)


def enumerate_configs(radii, w, R, max_report=10):
    """Enumera subconjuntos + asignaciones de padre (sarten=-1 o indice de otro aro).
    Devuelve lista de (count, area, parent_map, posiciones_por_contenedor)."""
    n = len(radii)
    results = []
    idxs = list(range(n))
    for subset_mask in range(1, 1 << n):
        subset = [i for i in idxs if subset_mask >> i & 1]
        # posibles padres para cada aro del subconjunto
        choices = []
        for i in subset:
            opts = [-1] + [j for j in subset if j != i and radii[i] <= radii[j] - w + 1e-9]
            choices.append(opts)
        for parents in itertools.product(*choices):
            pmap = dict(zip(subset, parents))
            # sin ciclos: el radio del hijo < radio del padre lo garantiza salvo empates exactos
            ok = all(pmap[i] == -1 or radii[i] < radii[pmap[i]] for i in subset)
            if not ok: continue
            # agrupar hijos por contenedor y comprobar factibilidad de cada empaquetado
            groups = {}
            for i in subset:
                groups.setdefault(pmap[i], []).append(i)
            placements, feas = {}, True
            for parent, kids in groups.items():
                Rc = R if parent == -1 else radii[parent] - w
                f, pos = pack_feasible([radii[k] for k in kids], Rc)
                if not f: feas = False; break
                placements[parent] = (kids, pos)
            if feas:
                cnt = len(subset)
                area = sum(contact_area(radii[i], w) for i in subset)
                results.append((cnt, area, pmap, placements))
    return results


if __name__ == "__main__":
    R, w = 10.0, 1.0
    radii = [9.0, 4.2, 4.2, 4.2]
    res = enumerate_configs(radii, w, R)
    best_count = max(res, key=lambda t: (t[0], t[1]))
    best_area  = max(res, key=lambda t: (t[1], t[0]))
    print(f"Instancia: R={R}, w={w}, radios={radii}")
    print(f"Config con MAX NUMERO : N={best_count[0]}, A={best_count[1]:.1f}, padres={best_count[2]}")
    print(f"Config con MAX AREA   : N={best_area[0]},  A={best_area[1]:.1f}, padres={best_area[2]}")
    # verificaciones puntuales
    print("¿Tres de r=4.2 caben en la sarten R=10?", pack_feasible([4.2]*3, 10.0)[0])
    print("¿Dos de r=4.2 caben en el agujero (R=8)?", pack_feasible([4.2]*2, 8.0)[0])
    print("¿9.0 + 4.2 juntos al nivel de la sarten?", pack_feasible([9.0, 4.2], 10.0)[0])
    json.dump({"R": R, "w": w, "radii": radii}, open("instance.json", "w"))
