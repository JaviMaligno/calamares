"""Lema de reinsercion: umbral rho*(omega) del paso de intercambio.

Contexto (Teorema 2, seccion 5 de docs/resultados.md). El voraz F coloca m en el
contenedor u; el testigo P lo coloca en v. Para transformar P hasta hacerlo
coincidir con F hay que sacar de u el conjunto

    S = {aros de radio < r_m que P coloca en u}

y reinsertarlo. Bajo superincrecencia sum(S) < r_m y S entra en fila (Lema 0) en el
disco vacante que m deja en v. Sin superincrecencia sum(S) puede superar r_m y la
prueba se rompe: ese es exactamente el hueco de la conjetura del umbral de Tribonacci.

Recursos liberados por el intercambio (los unicos legales sin tocar nada mas):
  N(r_m)      D_m, el disco que m ocupaba en v; queda libre entero.
  N(r_m - w)  H_m, el agujero de m, que viaja con m hacia u y sigue siendo contenedor.
  anidamiento recursivo dentro del propio S.

Normalizando r_m = 1 y omega = w/r_m, el problema abstracto es:

  (R) toda secuencia rho-decreciente contenida en (0,1) con suma <= rho,
      es aceptada por N(1) (+) N(1-omega)?

donde "rho-decreciente" recoge lo unico que rho impone sobre los aros menores que
r_m: sum(X) <= rho*r_m y sum_{l>j} X_l <= rho*X_j para todo j. Toda S realizable en
una instancia con parametro rho cumple ambas, luego

    rho*(omega) := min { rho_needed(X) : X no aceptado }

es una cota inferior rigurosa del rho que necesita cualquier fallo del intercambio:
si rho < rho*(omega), la reinsercion existe sin recurrir a la geometria de v.

Este script calcula rho*(omega), lo contrasta con la formula cerrada del perfil de
dos aros y localiza el regimen donde hacen falta los bolsillos de Descartes.
"""
import itertools, math
import numpy as np
from sim import pack_feasible

TRIB = 1.839286755214161  # raiz real de x^3 = x^2 + x + 1
PHI = (1 + math.sqrt(5)) / 2

# Umbral del radio de k circulos iguales en el disco unidad (Graham-Lubachevsky
# et al.; k=2,3,4 exactos, k>=5 valores tabulados).
EQ = {1: 1.0, 2: 0.5, 3: 2*math.sqrt(3) - 3, 4: math.sqrt(2) - 1,
      5: 0.370191, 6: 1/3, 7: 1/3, 8: 0.302593, 9: 0.275932}

# ---------------- factibilidad de hermanos ----------------
CACHE = {}

def sep_angle(ri, rj, Rc):
    """Angulo minimo entre los centros de dos circulos tangentes a la pared de Rc.
    math.inf si ni siquiera caben los dos juntos."""
    di, dj = Rc - ri, Rc - rj
    if di <= 0 or dj <= 0:
        return math.inf if ri + rj > Rc else 0.0
    c = (di*di + dj*dj - (ri + rj)**2) / (2*di*dj)
    if c <= -1.0:
        return math.inf
    return math.acos(min(1.0, c))


def feas3(rs, Rc):
    """Criterio angular: exacto para tres circulos en un disco (los tres pueden
    suponerse tangentes a la pared), necesario para mas de tres."""
    a, b, c = rs
    s = sep_angle(a, b, Rc) + sep_angle(a, c, Rc) + sep_angle(b, c, Rc)
    return s <= 2*math.pi + 1e-12


def feas(rs, Rc, effort=1):
    """Circulos de radios rs, disjuntos, dentro de un disco de radio Rc.

    Resuelto por criterios cerrados siempre que se pueda; el solver fisico solo
    interviene en la franja que ninguno decide.
    """
    if not rs:
        return True
    if Rc <= 1e-12:
        return False
    srt = sorted(rs, reverse=True)
    if srt[0] > Rc + 1e-12:
        return False
    if sum(srt) <= Rc + 1e-12:
        return True                                    # Lema 0: fila sobre un diametro
    if len(srt) == 2:
        return False                                   # k=2: la suma es criterio exacto
    if len(srt) == 3:
        return feas3(srt, Rc)                          # k=3: criterio angular, exacto
    a = sum(r*r for r in srt)
    if a > Rc*Rc + 1e-12:
        return False                                   # cota de area
    if a <= Rc*Rc/2 + 1e-12:
        return True                                    # Fekete-Keldenich-Scheffer: densidad 1/2
    k = len(srt)
    if k in EQ and srt[-1] > EQ[k]*Rc + 1e-12:
        return False              # k circulos, todos por encima del umbral de k iguales
    for tri in itertools.combinations(srt, 3):
        if not feas3(sorted(tri, reverse=True), Rc):
            return False                               # un trio infactible basta
    key = (tuple(round(r/Rc, 5) for r in srt), effort)
    if key not in CACHE:
        rr, it = (10, 900) if effort == 1 else (40, 4000)
        CACHE[key] = pack_feasible([r/Rc for r in srt], 1.0, restarts=rr, iters=it)[0]
    return CACHE[key]


# ---------------- aceptacion por un juego de nidos ----------------
ACC = {}

def accepts(X, caps, w, effort=1):
    """X decreciente. caps: capacidades de los nidos raiz disponibles.

    Cada aro va a un nido raiz o al agujero de otro aro mayor, con anidamiento
    recursivo; los hermanos de cada contenedor deben empaquetarse como circulos.
    """
    n = len(X)
    if n == 0:
        return True
    if sum(X) <= caps[0] + 1e-12:
        return True                                    # fila en el nido grande
    key = (tuple(round(x, 6) for x in X), tuple(round(c, 6) for c in caps),
           round(w, 6), effort)
    if key in ACC:
        return ACC[key]
    choices = []
    for i in range(n):
        opts = [("R", k) for k, c in enumerate(caps) if X[i] <= c + 1e-12]
        opts += [("N", j) for j in range(i) if X[i] <= X[j] - w + 1e-12]
        if not opts:
            ACC[key] = False
            return False
        choices.append(opts)
    res = False
    for assign in itertools.product(*choices):
        groups = {}
        for i, a in enumerate(assign):
            groups.setdefault(a, []).append(i)
        if all(feas([X[i] for i in kids],
                    caps[a[1]] if a[0] == "R" else X[a[1]] - w, effort)
               for a, kids in groups.items()):
            res = True
            break
    ACC[key] = res
    return res


def nests(omega):
    """Los dos contenedores que libera el intercambio, normalizados a r_m = 1."""
    return (1.0, 1.0 - omega) if omega < 1.0 else (1.0,)


def rho_needed(X):
    """Minimo rho de una instancia que pueda contener a X por debajo de r_m = 1."""
    X = sorted(X, reverse=True)
    v = sum(X)                                          # X son aros menores que r_m
    for j in range(len(X) - 1):
        v = max(v, sum(X[j+1:]) / X[j])                 # cola de cada aro de X
    return v


# ---------------- busqueda del umbral ----------------
def descend(X, caps, w, step=0.04, tol=2e-4):
    """Coordinate descent sobre los radios, sin salir de la region no aceptada."""
    X = sorted((round(x, 6) for x in X), reverse=True)
    best = rho_needed(X)
    while step > tol:
        improved = False
        for i in range(len(X)):
            for s in (-step, step):
                Y = list(X)
                Y[i] = round(Y[i] + s, 6)
                if not (1e-3 < Y[i] < 1.0):
                    continue
                Y = sorted(Y, reverse=True)
                r = rho_needed(Y)
                if r >= best - 1e-12 or accepts(Y, caps, w):
                    continue
                best, X, improved = r, Y, True
        if not improved:
            step /= 2
    return best, X


def rho_star(omega, k, trials=200, seed=0):
    """min rho_needed(X) sobre perfiles X de k aros NO reinsertables.

    La mitad de las semillas se toma en la banda (1-omega, 1) y su entorno, que es
    donde vive el bloqueo: el muestreo uniforme casi nunca da con esa franja.
    """
    rng = np.random.default_rng(seed)
    caps, w = nests(omega), omega
    lo = max(0.05, 1 - omega - 0.12)
    seeds = []
    for t in range(trials):
        X = (sorted(rng.uniform(lo, 0.999, k), reverse=True) if t % 2
             else sorted(rng.uniform(0.05, 0.999, k), reverse=True))
        if not accepts(list(X), caps, w):
            seeds.append((rho_needed(X), list(X)))
    if not seeds:
        return math.inf, None
    seeds.sort(key=lambda t: t[0])
    best, arg = math.inf, None
    for _, X in seeds[:8]:                              # descenso solo sobre los mejores
        r, Y = descend(X, caps, w)
        if r < best:
            best, arg = r, Y
    return best, arg


def pair_formula(omega):
    """Perfil de dos aros: cerrado. Ver la proposicion en docs/reinsercion.md."""
    return max(1.0, 2.0 * (1.0 - omega))


def band_bound(k, omega):
    """Perfil de k aros todos en la banda (1-omega, 1): cota k*(1-omega), valida
    solo si k aros de ese tamano no caben en el disco unidad."""
    if k not in EQ or 1 - omega < EQ[k]:
        return math.inf
    return k * (1 - omega)


if __name__ == "__main__":
    print(f"T = {TRIB:.6f}   phi = {PHI:.6f}   omega_0 = 1 - T/2 = {1 - TRIB/2:.6f}\n")

    print("PERFIL DE DOS AROS: formula cerrada contra busqueda numerica")
    print(f"  {'omega':>7} {'max(1,2(1-w))':>14} {'buscado':>9}  perfil")
    for omega in (0.0, 0.04, 0.080357, 0.12, 0.20, 0.35, 0.50, 0.70):
        r, X = rho_star(omega, 2, trials=400, seed=1)
        prof = "-" if X is None else "{" + ", ".join(f"{x:.3f}" for x in X) + "}"
        print(f"  {omega:>7.4f} {pair_formula(omega):>14.4f} {r:>9.4f}  {prof}")

    print("\nCOTA DE BANDA k*(1-omega) (perfiles con los k aros en (1-omega,1))")
    print(f"  {'k':>3} {'umbral EQ[k]':>13} {'omega max':>10} {'cota minima k*EQ[k]':>21}")
    for k in range(2, 7):
        print(f"  {k:>3} {EQ[k]:>13.6f} {1-EQ[k]:>10.4f} {k*EQ[k]:>21.4f}"
              + ("   > T" if k*EQ[k] > TRIB else ""))

    print("\nUMBRAL rho*(omega) POR TAMANO DE PERFIL")
    print(f"  {'omega':>7} {'k=2':>8} {'k=3':>8} {'k=4':>8} {'min':>8}   veredicto")
    for omega in (0.0, 0.04, 0.080357, 0.12, 0.20, 0.30, 0.45, 0.60, 0.80):
        row = [rho_star(omega, k, trials=150, seed=7 + k)[0] for k in (2, 3, 4)]
        mn = min(row)
        verdict = ("reinsercion garantizada bajo T" if mn >= TRIB
                   else "hace falta la geometria de v")
        cells = " ".join(f"{x:>8.4f}" for x in row)
        print(f"  {omega:>7.4f} {cells} {mn:>8.4f}   {verdict}")

    print("\nLOCALIZACION DEL UMBRAL DE GROSOR omega_c (donde min_k rho*(omega) cruza T)")
    print(f"  {'omega':>7} {'k=2':>8} {'k=3':>8} {'k=4':>8} {'min':>8}  perfil minimo")
    for omega in (0.03, 0.04, 0.05, 0.055, 0.06, 0.065, 0.07, 0.08, 0.09):
        row = [rho_star(omega, k, trials=600, seed=11 + k) for k in (2, 3, 4)]
        mn, arg = min(row, key=lambda t: t[0])
        prof = "-" if arg is None else "{" + ", ".join(f"{x:.3f}" for x in arg) + "}"
        cells = " ".join(f"{r:>8.4f}" for r, _ in row)
        flag = "  <-- baja de T" if mn < TRIB else ""
        print(f"  {omega:>7.4f} {cells} {mn:>8.4f}  {prof}{flag}")

    print("\nINSTANCIAS CRITICAS CONOCIDAS (S en el paso de intercambio)")
    for name, r_m, w, S in (
            ("contraejemplo n=4 {10,5,4.9,4.8}  ", 5.0, 0.3, [4.9, 4.8]),
            ("gemelas I1        {10,5,4.99,4.50}", 5.0, 0.505, [4.99, 4.50]),
            ("gemelas I2        {10,5,4.76,4.74}", 5.0, 0.505, [4.76, 4.74])):
        omega = w / r_m
        X = sorted((s / r_m for s in S), reverse=True)
        ok = accepts(X, nests(omega), omega, effort=2)
        print(f"  {name} omega={omega:.4f} S/r_m={[round(x,4) for x in X]} "
              f"reinsertable={ok} cota_par={pair_formula(omega):.4f}")
