"""Busqueda dirigida de fallos con rho < T en el regimen que el lema de
reinsercion NO cierra por via combinatoria.

reinserta.py establece que el paso de intercambio se resuelve sin mirar la
geometria de v mientras omega = w/r_m sea pequeno, y que a partir de
omega_c ~ 0.045 aparecen perfiles bloqueantes con rho por debajo de T. Ahi el
unico recurso que queda es el bolsillo de Descartes del contenedor v. La
conjetura del umbral de Tribonacci afirma que ese recurso basta hasta T.

Este script ataca esa ventana directamente. La busqueda aleatoria previa
(umbral.py) muestreaba radios y R uniformemente y por eso nunca visitaba la
region relevante: los fallos conocidos viven en tangencias exactas, de medida
nula. Aqui se construyen las instancias con la estructura del bloqueo:

  r_1 = alpha,  r_m = 1,  R = alpha + 1 (sarten rigida: {r_1, r_m} tangentes),
  sigma_1, sigma_2 en la banda (1 - omega, 1)   -> no caben en el agujero de m,
  pareja alojable en el agujero de r_1          -> el testigo coloca los cuatro.

alpha se barre alrededor de phi, que es donde la cota por bolsillos alcanza su
minimo (ver docs/reinsercion.md): si la conjetura fuese falsa, el contraejemplo
deberia aparecer cerca de ahi.
"""
import itertools, math
import numpy as np
from reinserta import feas, TRIB, PHI

def rho(radii):
    rs = sorted(radii, reverse=True)
    return max(sum(rs[i+1:]) / rs[i] for i in range(len(rs) - 1))


def greedy(radii, w, R, rule):
    """Voraz en orden decreciente; best fit = contenedor de menor capacidad."""
    order = sorted(range(len(radii)), key=lambda i: -radii[i])
    cont = [{"cap": R, "occ": []}]
    placed = []
    for i in order:
        cands = [c for c in cont if radii[i] <= c["cap"] + 1e-9
                 and feas([radii[j] for j in c["occ"]] + [radii[i]], c["cap"])]
        if cands:
            c = (min(cands, key=lambda c: c["cap"]) if rule == "best"
                 else max(cands, key=lambda c: c["cap"]))
            c["occ"].append(i)
            placed.append(i)
            if radii[i] - w > 1e-9:
                cont.append({"cap": radii[i] - w, "occ": []})
    return frozenset(placed)


def set_feasible(sub, radii, w, R):
    """Existe un bosque de anidamiento que aloje exactamente sub?"""
    ch = [[-1] + [j for j in sub if j != i and radii[i] <= radii[j] - w + 1e-9]
          for i in sub]
    for ps in itertools.product(*ch):
        pm = dict(zip(sub, ps))
        if not all(pm[i] == -1 or radii[i] < radii[pm[i]] for i in sub):
            continue
        g = {}
        for i in sub:
            g.setdefault(pm[i], []).append(i)
        if all(feas([radii[k] for k in kids], R if p == -1 else radii[p] - w)
               for p, kids in g.items()):
            return True
    return False


def lexmax(radii, w, R):
    L = []
    for i in sorted(range(len(radii)), key=lambda i: -radii[i]):
        if set_feasible(L + [i], radii, w, R):
            L.append(i)
    return frozenset(L)


def scan(alphas, omegas, grid, slack=(0.0,), verbose=True):
    """Barre la plantilla y devuelve (probadas, fallos, mejor_rho_de_fallo)."""
    tried = fails = 0
    best = None
    for alpha in alphas:
        for omega in omegas:
            lo = 1 - omega
            if lo <= 0 or alpha - omega < 1:      # m debe caber en el agujero de r_1
                continue
            for s1 in np.linspace(lo + 1e-4, 0.9999, grid):
                for s2 in np.linspace(lo + 1e-4, s1, grid):
                    if s1 + s2 > alpha - omega:   # la pareja debe caber en el agujero de r_1
                        continue
                    radii = [alpha, 1.0, float(s1), float(s2)]
                    r = rho(radii)
                    if r >= TRIB:
                        continue
                    for sl in slack:
                        R = alpha + 1.0 + sl
                        tried += 1
                        L = lexmax(radii, omega, R)
                        for rule in ("best", "worst"):
                            if greedy(radii, omega, R, rule) != L:
                                fails += 1
                                if best is None or r < best[0]:
                                    best = (r, alpha, omega, s1, s2, R, rule)
                                if verbose:
                                    print(f"  !! fallo rho={r:.4f} alpha={alpha:.3f} "
                                          f"omega={omega:.3f} sigma=({s1:.4f},{s2:.4f}) "
                                          f"R={R:.3f} regla={rule}")
    return tried, fails, best


if __name__ == "__main__":
    print(f"T = {TRIB:.6f}   phi = {PHI:.6f}\n")

    print("BARRIDO 1: alpha alrededor de phi, omega en el regimen critico", flush=True)
    alphas = [round(PHI + d, 4) for d in (-0.2, -0.1, 0.0, 0.1, 0.2, 0.5)]
    omegas = [0.06, 0.10, 0.16, 0.25, 0.35]
    t1, f1, b1 = scan(alphas, omegas, grid=9)
    print(f"  instancias con rho < T probadas: {t1}   fallos: {f1}", flush=True)

    print("\nBARRIDO 2: alpha amplio, con y sin holgura en R", flush=True)
    alphas = [1.3, 1.7, 2.0, 2.5, 3.0, 4.0]
    omegas = [0.08, 0.14, 0.22, 0.40]
    t2, f2, b2 = scan(alphas, omegas, grid=8, slack=(0.0, 0.03))
    print(f"  instancias con rho < T probadas: {t2}   fallos: {f2}", flush=True)

    print("\nCONTROL: la misma plantilla sin la restriccion rho < T debe dar fallos")
    ctl = 0
    for alpha, omega, s1, s2, R in ((2.0, 0.06, 0.98, 0.96, 3.0),
                                    (2.0, 0.101, 0.998, 0.90, 3.0),
                                    (2.0, 0.101, 0.952, 0.948, 3.0)):
        radii = [alpha, 1.0, s1, s2]
        L = lexmax(radii, omega, R)
        res = {rule: greedy(radii, omega, R, rule) for rule in ("best", "worst")}
        bad = [k for k, v in res.items() if v != L]
        ctl += len(bad)
        print(f"  alpha={alpha} omega={omega} sigma=({s1},{s2}) rho={rho(radii):.4f}: "
              f"lex-max={len(L)} aros, fallan {bad or 'ninguna'}")
    print(f"  fallos de control (con rho > T): {ctl}")

    total_fails = f1 + f2
    print(f"\nRESULTADO: {t1 + t2} instancias dirigidas con rho < T, {total_fails} fallos.")
    if total_fails == 0:
        print("  La conjetura del umbral de Tribonacci sobrevive a la busqueda dirigida:")
        print("  en la ventana que el argumento combinatorio no cierra, el bolsillo de v")
        print("  rescata en todos los casos probados.")
    else:
        print(f"  Mejor contraejemplo: {best if (best := b1 or b2) else '-'}")
