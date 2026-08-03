"""Perfiles de tres aros: caracterizacion exacta y formula cerrada de rho*_3(omega).

Punto 3 de docs/reinsercion.md seccion 10. Analogo de la Proposicion 1 (par) para
k = 3: que perfiles {s1 >= s2 >= s3} en (0,1) NO son reinsertables en
N(1) (+) N(1-omega) con anidamiento, y el infimo rho*_3(omega) que eso impone.

Resultado (ver docs/drafts/perfil_tres.md, Proposicion 4). Con beta = 1 - omega,
S = {s1 >= s2 >= s3} NO es reinsertable si y solo si se da uno de:

  (i)   s2 > beta  y  s1 + s2 > 1                     (par en banda; s3 libre)
  (ii)  s2 > beta,  s1 + s2 <= 1,  s3 > beta  y el trio no cabe en el disco
        unidad (criterio angular; solo posible con omega > 1/2)
  (iii) s2 <= beta < s1:  s1 + s3 > 1,  s2 + s3 > beta,  s3 > s1 - omega
  (iv)  s1 <= beta:       s2 + s3 > 1,  s3 > s1 - omega

y el infimo resultante es (phi = razon aurea):

  rho*_3(omega) = max(1, min(2(1-omega), max(phi, 2/(1+2*omega))))

es decir, por tramos: 2/(1+2w) en (0, (sqrt5-2)/2], phi en [(sqrt5-2)/2, 1-phi/2],
2(1-w) en [1-phi/2, 1/2], 1 en [1/2, 1). Cruza T en omega_T = 1/T - 1/2 ~ 0.043689.

Este script valida cada pieza: (1) identidades algebraicas en sympy; (2) la
caracterizacion contra accepts() de reinserta.py (exacto para k=3: grupos de a lo
sumo 3 circulos, criterios cerrados, sin solver fisico); (3) familias testigo que
alcanzan la formula en el limite; (4) flips de frontera (relajar cada desigualdad
reactiva la reinsercion); (5) busqueda numerica del minimo sobre la region
bloqueada, como hace reinserta.py con el par.
"""
import math
import numpy as np
from reinserta import accepts, nests, rho_needed, feas3, TRIB, PHI

OM1 = (math.sqrt(5.0) - 2.0) / 2.0        # = 1/phi - 1/2 ~ 0.118034
OM2 = 1.0 - PHI / 2.0                     # ~ 0.190983
OMT = 1.0 / TRIB - 0.5                    # cruce con Tribonacci ~ 0.043689


# ---------------- caracterizacion y formula ----------------

def bloqueado(s1, s2, s3, om):
    """Proposicion 4: True si {s1>=s2>=s3} NO es reinsertable en N(1)(+)N(1-om)."""
    b = 1.0 - om
    if s2 > b:
        if s1 + s2 > 1.0:
            return True                                        # caso (i)
        return s3 > b and not feas3((s1, s2, s3), 1.0)         # caso (ii)
    if s1 > b:                                                 # caso (iii)
        return s1 + s3 > 1.0 and s2 + s3 > b and s3 > s1 - om
    return s2 + s3 > 1.0 and s3 > s1 - om                      # caso (iv)


def rho3_star(om):
    """Corolario 3: infimo de rho_needed sobre perfiles de 3 aros bloqueados."""
    return max(1.0, min(2.0 * (1.0 - om), max(PHI, 2.0 / (1.0 + 2.0 * om))))


def testigo(om, eps=1e-4):
    """Familia que aproxima el infimo en cada tramo (perfil bloqueado con
    rho_needed -> rho*_3 cuando eps -> 0)."""
    if om <= OM1:                                   # tramo 2/(1+2w): caso (iv)
        return [0.5 + om, 0.5 + eps, 0.5 + eps]
    if om <= OM2:                                   # meseta phi: caso (iv)
        return [1.0 / PHI, 0.5 + eps, 0.5 + eps]
    if om < 0.5:                                    # tramo 2(1-w): caso (i)
        return [1.0 - om + eps, 1.0 - om + eps, eps]
    return [0.5 + eps, 0.5 + eps, eps]              # tramo 1: caso (i)


# ---------------- validaciones ----------------

def check_simbolico():
    """Identidades exactas de la derivacion, en sympy."""
    import sympy as sp
    w, s = sp.symbols("w s", positive=True)
    phi = (1 + sp.sqrt(5)) / 2
    ok = True

    # cruce de tramos 1-2: 2/(1+2w) = 3/2 + w en w = (sqrt5-2)/2 = 1/phi - 1/2
    sols = sp.solve(sp.Eq(2 / (1 + 2 * w), sp.Rational(3, 2) + w), w)
    om1 = (sp.sqrt(5) - 2) / 2
    ok &= any(sp.simplify(r - om1) == 0 for r in sols)
    ok &= sp.simplify(om1 - (1 / phi - sp.Rational(1, 2))) == 0
    ok &= sp.simplify(2 / (1 + 2 * om1) - phi) == 0            # continuidad, vale phi

    # minimo de max(1+s, 1/s): cruce s^2 + s = 1 en s = 1/phi, valor phi
    s_star = sp.solve(sp.Eq(1 + s, 1 / s), s)
    ok &= any(sp.simplify(r - 1 / phi) == 0 for r in s_star)
    ok &= sp.simplify((1 + 1 / phi) - phi) == 0

    # cruce de tramos 2-3: 2(1-w) = phi en w = 1 - phi/2
    ok &= sp.simplify(2 * (1 - (1 - phi / 2)) - phi) == 0

    # frontera caso (iv) rama s1 = beta: (2-w)(1-w) = 1 en w = (3-sqrt5)/2 = 1-1/phi
    sols = sp.solve(sp.Eq((2 - w) * (1 - w), 1), w)
    ok &= any(sp.simplify(r - (3 - sp.sqrt(5)) / 2) == 0 for r in sols)
    ok &= sp.simplify((3 - sp.sqrt(5)) / 2 - (1 - 1 / phi)) == 0

    # cruce con Tribonacci: 2/(1+2w) = T en w = 1/T - 1/2 = T^2 - T - 3/2
    t = sp.symbols("t", positive=True)
    minpoly = t**3 - t**2 - t - 1
    expr = (1 / t - sp.Rational(1, 2)) - (t**2 - t - sp.Rational(3, 2))
    ok &= sp.simplify(sp.rem(sp.together(expr * t).as_numer_denom()[0],
                             minpoly, t)) == 0
    # y 2/(1+2w_T) - T = 0 modulo el polinomio minimo
    wT = 1 / t - sp.Rational(1, 2)
    expr2 = sp.together(2 / (1 + 2 * wT) - t)
    ok &= sp.simplify(sp.rem(sp.expand(expr2.as_numer_denom()[0]), minpoly, t)) == 0
    return bool(ok)


def check_caracterizacion(rng, oms, n_por_omega=900):
    """bloqueado() contra accepts() de reinserta.py. accepts es exacto para k=3
    (grupos <= 3: fila, suma del par, criterio angular; el solver no interviene).
    Muestreo mixto: uniforme + dirigido a las franjas criticas."""
    mal = tot = 0
    for om in oms:
        b = 1.0 - om
        focos = [0.5, b, 1.0 / PHI, 0.5 + om]
        for i in range(n_por_omega):
            if i % 3 == 0:
                X = rng.uniform(0.01, 0.999, 3)
            else:  # cerca de las fronteras activas de la caracterizacion
                X = np.clip([rng.choice(focos) + rng.normal(0, 0.03)
                             for _ in range(3)], 0.01, 0.999)
            X = sorted(float(x) for x in X)[::-1]
            tot += 1
            if bloqueado(*X, om) != (not accepts(list(X), nests(om), om)):
                mal += 1
                if mal <= 5:
                    print(f"    MISMATCH om={om} X={[round(x, 5) for x in X]}")
    return mal, tot


def check_testigos(oms, eps=1e-5, tol=5e-4):
    """El testigo esta bloqueado (segun accepts, no solo el predicado) y su
    rho_needed dista O(eps) de la formula."""
    todo_ok = True
    print(f"  {'omega':>7} {'rho*_3':>9} {'testigo':>9} {'dif':>9}  bloqueado")
    for om in oms:
        X = testigo(om, eps)
        blk = not accepts(list(X), nests(om), om)
        r = rho_needed(X)
        d = r - rho3_star(om)
        ok = blk and 0.0 <= d < tol
        todo_ok &= ok
        print(f"  {om:>7.4f} {rho3_star(om):>9.5f} {r:>9.5f} {d:>9.2e}  "
              f"{blk}{'' if ok else '  <-- FALLO'}")
    return todo_ok


def check_flips(eps=1e-4):
    """Relajar la desigualdad activa de cada caso debe reactivar la reinsercion."""
    casos = [
        # (omega, perfil aceptado tras el flip, descripcion)
        (0.06, [0.5 + 0.06, 0.5, 0.5 - eps], "iv: s2+s3 <= 1 -> P4"),
        (0.06, [0.5 + 0.06 + 2 * eps, 0.5 + eps, 0.5 + eps],
         "iv: s3 <= s1-om -> anida"),
        (0.15, [1 / PHI + 2 * eps, 0.5 + eps, 0.5 + eps],
         "meseta: s3 <= s1-om? no, sigue bloqueado", False),
        (0.25, [0.75 - eps, 0.74, 0.001], "i: s2 <= beta y s2+s3 <= ... -> acepta"),
        (0.06, [0.95, 0.9, 0.89 - eps], "iii: s3 <= s1-om -> anida"),
        (0.06, [0.95, 0.9, 0.05 - eps], "iii: s2+s3 <= beta -> par en B"),
    ]
    todo_ok = True
    for c in casos:
        om, X, desc = c[0], sorted(c[1], reverse=True), c[2]
        esperado = c[3] if len(c) > 3 else True
        acc = accepts(list(X), nests(om), om)
        ok = acc == esperado
        todo_ok &= ok
        print(f"  om={om:.2f} {desc:<45} accepts={acc}"
              f"{'' if ok else '  <-- FALLO'}")
    return todo_ok


def busca_minimo(om, rng, n_semillas=4000, n_descensos=12):
    """Minimo de rho_needed sobre la region bloqueada, con el predicado exacto
    (rapido) y descenso por coordenadas multi-arranque."""
    semillas = []
    b = 1.0 - om
    for i in range(n_semillas):
        if i % 2:
            X = sorted(rng.uniform(0.3, 0.999, 3), reverse=True)
        else:
            X = np.clip(sorted([rng.choice([0.5, b, 1 / PHI]) + rng.normal(0, 0.05)
                                for _ in range(3)], reverse=True), 0.01, 0.999)
        X = [float(x) for x in X]
        if bloqueado(*X, om):
            semillas.append((rho_needed(X), X))
    semillas.sort(key=lambda t: t[0])
    semillas = semillas[:n_descensos] + [(0.0, testigo(om, 1e-3))]
    best = math.inf
    for _, X0 in semillas:
        X, paso = list(X0), 0.02
        r = rho_needed(X)
        while paso > 1e-6:
            mejora = False
            for i in range(3):
                for s in (-paso, paso):
                    Y = sorted([X[j] + (s if j == i else 0.0) for j in range(3)],
                               reverse=True)
                    if not (0.0 < Y[2] and Y[0] < 1.0):
                        continue
                    rY = rho_needed(Y)
                    if rY < r - 1e-12 and bloqueado(*Y, om):
                        X, r, mejora = Y, rY, True
            if not mejora:
                paso /= 2
        best = min(best, r)
    return best


if __name__ == "__main__":
    rng = np.random.default_rng(20260729)
    print(f"T = {TRIB:.6f}  phi = {PHI:.6f}  om1 = {OM1:.6f}  om2 = {OM2:.6f}"
          f"  om_T = 1/T - 1/2 = {OMT:.6f}\n")

    print("1) IDENTIDADES SIMBOLICAS (sympy)")
    ok1 = check_simbolico()
    print(f"  todas las identidades: {'OK' if ok1 else 'FALLO'}\n")

    print("2) CARACTERIZACION (Prop. 4) CONTRA accepts() DE reinserta.py")
    oms = (0.02, 0.043689, 0.06, 0.09, 0.118, 0.15, 0.19, 0.25, 0.33,
           0.40, 0.48, 0.55, 0.70, 0.85)
    mal, tot = check_caracterizacion(rng, oms)
    ok2 = mal == 0
    print(f"  {tot} perfiles, {mal} desacuerdos: {'OK' if ok2 else 'FALLO'}\n")

    print("3) FAMILIAS TESTIGO: rho_needed -> rho*_3(omega) y bloqueadas")
    ok3 = check_testigos((0.01, 0.03, OMT, 0.05, 0.08, 0.10, OM1, 0.15,
                          0.18, OM2, 0.25, 0.35, 0.45, 0.55, 0.70))
    print(f"  {'OK' if ok3 else 'FALLO'}\n")

    print("4) FLIPS DE FRONTERA")
    ok4 = check_flips()
    print(f"  {'OK' if ok4 else 'FALLO'}\n")

    print("5) BUSQUEDA NUMERICA DEL MINIMO (predicado exacto + descenso)")
    print(f"  {'omega':>7} {'formula':>9} {'buscado':>9} {'dif':>9}")
    ok5 = True
    for om in (0.02, 0.05, 0.08, 0.118, 0.15, 0.19, 0.25, 0.35, 0.45, 0.60):
        r = busca_minimo(om, rng)
        d = r - rho3_star(om)
        # el infimo no se alcanza: la busqueda debe quedar por encima y cerca
        ok = -1e-9 <= d < 5e-3
        ok5 &= ok
        print(f"  {om:>7.4f} {rho3_star(om):>9.5f} {r:>9.5f} {d:>9.2e}"
              f"{'' if ok else '  <-- FALLO'}")
    print(f"  {'OK' if ok5 else 'FALLO'}\n")

    print("6) CONTRASTE CON LA TABLA DE reinsercion.md seccion 6 (columna k=3)")
    tabla = {0.03: 1.907, 0.04: 1.873, 0.05: 1.846, 0.06: 1.814, 0.08: 1.749,
             0.12: 1.618, 0.20: 1.601, 0.45: 1.100}
    print(f"  {'omega':>7} {'tabla':>7} {'formula':>9}   la tabla es cota superior")
    ok6 = True
    for om, v in tabla.items():
        f = rho3_star(om)
        ok6 &= f <= v + 2e-3
        print(f"  {om:>7.3f} {v:>7.3f} {f:>9.5f}   "
              + ("coincide" if abs(f - v) < 2e-3 else
                 f"la busqueda de reinserta.py quedo {v - f:+.3f} arriba (minimo local)"))
    print(f"  formula <= tabla en todo punto: {'OK' if ok6 else 'FALLO'}\n")

    print("VEREDICTO GLOBAL:",
          "TODO OK" if all((ok1, ok2, ok3, ok4, ok5, ok6)) else "HAY FALLOS")
    print(f"  rho*_3 cruza T en omega_T = 1/T - 1/2 = {OMT:.6f} "
          f"(antes se estimaba omega_c ~ 0.05)")

    import sys
    sys.exit(0 if all((ok1, ok2, ok3, ok4, ok5, ok6)) else 1)
