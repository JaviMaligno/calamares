"""Punto 1 de docs/reinsercion.md seccion 9: sustituir el bolsillo de Descartes por
la condicion completa "el trio {alpha, sigma1, sigma2} no empaqueta en v" y medir si
el infimo de rho sube de phi a T.

Configuracion rigida canonica, normalizada a r_m = 1: v es la sarten de radio
R = alpha + 1, ocupada por alpha y por m (tangentes). El intercambio saca a m,
coloca sigma1 en el disco vacante D_m y falla solo si sigma2 no cabe en ningun
sitio de v, es decir solo si el trio {alpha, sigma1, sigma2} es infactible en R.
(Esta es la condicion debil correcta: mas debil que "sigma2 no cabe en el bolsillo
de Descartes con sigma1 = 1", que da la cota phi de la Proposicion 2.)

Presiones sobre rho de una instancia que contenga ese bloqueo:
    cola de m:      rho >= sigma1 + sigma2            (los menores que m suman eso)
    cola de alpha:  rho >= (1 + sigma1 + sigma2)/alpha  (m y los sigma son < alpha)

Objetivo:  inf max(s1+s2, (1+s1+s2)/alpha)  sujeto a  trio infactible en alpha+1,
           0 < s2 <= s1 < 1.

La prediccion (resultados.md seccion 5quater) es que este infimo es exactamente la
constante de Tribonacci T, alcanzado en el limite tangente con s1 -> 1.
"""
import math
import numpy as np
from reinserta import feas3, TRIB, PHI


def infeasible_trio(alpha, s1, s2):
    return not feas3(sorted([alpha, s1, s2], reverse=True), alpha + 1.0)


def rho_of(alpha, s1, s2):
    t = s1 + s2
    return max(t, (1.0 + t) / alpha)


def witness_ok(alpha, s1, s2):
    """El testigo coloco S = {s1, s2} en u. En la plantilla canonica u es el
    agujero de alpha; para dos circulos la condicion exacta es la suma (limite
    omega -> 0: capacidad alpha)."""
    return s1 + s2 <= alpha + 1e-12


def min_s2_blocking(alpha, s1, tol=1e-12):
    """Menor sigma2 (<= s1) que hace infactible el trio, por biseccion.
    La infactibilidad es monotona creciente en s2. Devuelve None si ni s2 = s1
    bloquea."""
    if not infeasible_trio(alpha, s1, s1):
        return None
    lo, hi = 0.0, s1
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        if infeasible_trio(alpha, s1, mid):
            hi = mid
        else:
            lo = mid
    return hi


def best_rho(alpha, grid=2000, witness=False):
    """min sobre s1 de rho(alpha, s1, s2_min(s1)): en el optimo s2 esta en la
    frontera de infactibilidad (bajar s2 solo puede bajar rho). Con witness=True
    se exige ademas que S quepa en u (la colocacion del testigo)."""
    best = (math.inf, None, None)
    for s1 in np.linspace(0.25, 0.999999, grid):
        s2 = min_s2_blocking(alpha, float(s1))
        if s2 is None:
            continue
        if witness and not witness_ok(alpha, float(s1), s2):
            continue
        r = rho_of(alpha, float(s1), s2)
        if r < best[0]:
            best = (r, float(s1), s2)
    return best


if __name__ == "__main__":
    print(f"T = {TRIB:.9f}   phi = {PHI:.9f}\n")

    print("INFIMO DE rho CON LA CONDICION COMPLETA DEL TRIO (barrido en alpha)")
    print(f"  {'alpha':>8} {'rho_min':>12} {'s1*':>10} {'s2*':>10}")
    coarse = [1.3, 1.5, PHI, 1.7, 1.8, 1.839287, 1.9, 2.0, 2.2, 2.5, 3.0]
    results = []
    for a in coarse:
        r, s1, s2 = best_rho(a)
        results.append((r, a, s1, s2))
        mark = ""
        if s1 is not None and abs(r - TRIB) < 5e-3:
            mark = "   ~ T"
        print(f"  {a:>8.4f} {r:>12.6f} "
              + (f"{s1:>10.6f} {s2:>10.6f}" if s1 else f"{'-':>10} {'-':>10}") + mark)

    results = [t for t in results if t[2] is not None]
    r0, a0, _, _ = min(results)
    print(f"\n  minimo grueso en alpha = {a0:.4f}: rho = {r0:.6f}")

    print("\nREFINADO alrededor del minimo (biseccion sobre alpha, malla fina en s1)")
    lo, hi = a0 - 0.25, a0 + 0.25
    for _ in range(24):
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if best_rho(m1, grid=900)[0] < best_rho(m2, grid=900)[0]:
            hi = m2
        else:
            lo = m1
    a_star = 0.5 * (lo + hi)
    r_star, s1s, s2s = best_rho(a_star, grid=6000)
    print(f"  alpha* = {a_star:.6f}")
    print(f"  rho*   = {r_star:.6f}   (T = {TRIB:.6f}, diferencia {r_star - TRIB:+.2e})")
    print(f"  s1* = {s1s:.6f}  s2* = {s2s:.6f}  (limite tangente predicho: s1 -> 1)")

    # En el optimo sin restriccion s1+s2 > alpha: S no cabria en u, luego ese
    # bloqueo no es realizable por ningun testigo. La restriccion que falta es
    # la propia colocacion del testigo: S cabe en u.
    print(f"\n  en el optimo: s1+s2 = {s1s + s2s:.6f} vs alpha = {a_star:.6f} -> "
          f"{'S NO cabe en u' if s1s + s2s > a_star else 'S cabe en u'}")

    print("\nCON LA RESTRICCION DEL TESTIGO (S cabe en u): barrido en alpha")
    print(f"  {'alpha':>8} {'rho_min':>12} {'s1*':>10} {'s2*':>10}")
    resw = []
    for a in coarse:
        r, s1, s2 = best_rho(a, witness=True)
        if s1 is not None:
            resw.append((r, a, s1, s2))
        mark = "   ~ T" if s1 is not None and abs(r - TRIB) < 5e-3 else ""
        print(f"  {a:>8.4f} {r:>12.6f} "
              + (f"{s1:>10.6f} {s2:>10.6f}" if s1 else f"{'-':>10} {'-':>10}") + mark)
    rw, aw, _, _ = min(resw)
    lo, hi = aw - 0.12, aw + 0.12
    for _ in range(22):
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if best_rho(m1, grid=900, witness=True)[0] < best_rho(m2, grid=900, witness=True)[0]:
            hi = m2
        else:
            lo = m1
    aw_star = 0.5 * (lo + hi)
    rw_star, s1w, s2w = best_rho(aw_star, grid=6000, witness=True)
    print(f"\n  alpha* = {aw_star:.6f}   (T = {TRIB:.6f})")
    print(f"  rho*   = {rw_star:.6f}   (T = {TRIB:.6f}, diferencia {rw_star - TRIB:+.2e})")
    print(f"  s1* = {s1w:.6f}  s2* = {s2w:.6f}")

    verdict = abs(rw_star - TRIB) < 3e-3
    print("\nVEREDICTO:")
    print(f"  bolsillo solo                 -> phi  = {PHI:.4f}   (Proposicion 2)")
    print(f"  trio completo, u libre        -> {r_star:.4f}   (raiz de 2a^3 = a^2+2a+2)")
    print(f"  trio + colocacion del testigo -> {rw_star:.4f}"
          + (f"   = T: el infimo del intercambio en la plantilla canonica ES Tribonacci"
             if verdict else "   NO coincide con T - revisar"))
