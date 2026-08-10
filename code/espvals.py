#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La VACUIDAD de la variedad del bolsillo diametral
(docs/drafts/espvals.md, v2 tras acta REFUTADO): el «vals de las
bolas vacantes» v1 queda RETIRADO (no licenciado por F2: mezclaba
el recurso posicional y el certificado fresco en el MISMO
contenedor — en cada modo puro una pieza queda sin casa), y no
hace falta: la ronda hostil demostro que LA VARIEDAD ENTERA ES
ILEGAL bajo rho <= phi, por la pared que faltaba en los
generadores de espxy y espvals v1:

  COLA GLOBAL DE m: la cola de m = 1 incluye TODA pieza menor
  (definicion del paper: multiconjunto entero), en particular las
  X_Y: Sigma_S + X_m + Sigma_X_Y <= phi.  La variedad exigia
  Sigma_S > 1 (pared D, ligera) y x > x*(z) >= x*(1+2 omega) >
  0.91: Sigma_S + x > 1.91 > phi = 1.618 — INCOMPATIBLE.  Medido:
  100% de los puntos de espxy (300/300) y de espvals v1 (400/400 y
  250/250) violan cola(m).

  RIGIDEZ DEL SUELO (segundo derribo, independiente): en
  c' = 1 + z el par (z, m) es diametral tangente RIGIDO
  (|c_z - c_m| <= (c'-z) + (c'-1) = z + 1 con igualdad forzada) y
  el hueco maximo restante en v es EXACTAMENTE x* (el bolsillo):
  el propio P (pre-intercambio, con m y x en v) es infactible con
  x > x* — la obligacion «corona con x» era fantasma: si P existe,
  x no estaba mural en v.

  LA CONSECUENCIA POSITIVA: toda pieza legal de X_Y mide
  <= phi - Sigma_S < phi - 1 = 0.618 < x*(z) en todo el dominio
  (x*(z) > 0.618 sii z > 1.29, y z >= 1 + 2 omega): las X_Y son
  SIEMPRE sub-bolsillo del hueco diametral — la celda ESP X_Y > 0
  ligera se cierra por vacuidad del peligro + insercion
  sub-bolsillo (certificacion de la corona con k piezas pequenas:
  pendiente declarada, herramienta = motor de r2bmulti).

Bloques: [A] la pared que faltaba (algebra exacta de la
incompatibilidad); [B] la vacuidad medida (los generadores de
espxy re-ejecutados con cola(m): 0 supervivientes); [C] la rigidez
del suelo (exacta + numerica); [D] la consecuencia positiva
(sub-bolsillo universal de las X_Y legales); [E] estatus, el vals
retirado y las lecciones.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check
from espxy import x_star, genera_legal

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260818'))


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] la pared que faltaba: cola global de m")
    import sympy as sp
    ok = True
    ok &= check("[ENUNCIADO] cola GLOBAL de m (definicion del "
                "paper: tail(i) = suma de radios menores sobre "
                "TODA la instancia): Sigma_S + X_m + Sigma_X_Y <= "
                "phi.  Los generadores de espxy y espvals v1 solo "
                "imponian Sigma_S (+X_m) <= phi — la trampa: las "
                "paredes del prover pueden OMITIR masas opcionales "
                "(cotas inferiores validas), pero la LEGALIDAD del "
                "adversario exige la cola entera", True)
    z, w = sp.symbols('z w', positive=True)
    xs = z * (z + 1) / (z ** 2 + z + 1)
    phi = (1 + sp.sqrt(5)) / 2
    # x*(z) > phi - 1 sii z(z+1) > (phi-1)(z^2+z+1): en z = 1.29
    # ya se cumple; el dominio tiene z >= 1 + 2w > 1.29 para
    # w > 0.145 (y la variedad exigia w >= 0.9)
    v129 = sp.simplify(xs.subs(z, sp.Rational(129, 100))
                       - (phi - 1))
    ok &= check(f"INCOMPATIBILIDAD exacta: ligera Sigma_S > 1 "
                f"(pared D) y x > x*(z) con z >= 1 + 2 omega >= "
                f"2.8 (omega >= 0.9) => Sigma_S + x > 1 + "
                f"x*(2.8) = {1 + x_star(2.8):.4f} > phi = "
                f"{PHI:.4f}; y ya x*(1.29) > phi - 1 = 0.618 "
                f"(sympy: {sp.simplify(v129) > 0}): el sliver "
                f"y la ligera no caben juntos en rho <= phi",
                1 + x_star(2.8) > PHI and sp.simplify(v129) > 0)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] la vacuidad, medida sobre los generadores de espxy")
    rng = random.Random(SEED)
    ok = True
    n, violan = 0, 0
    peor = 9.9
    intentos = 0
    while n < 300 and intentos < 400000:
        intentos += 1
        pt = genera_legal(rng, con_sliver=True)
        if pt is None:
            continue
        w, s2, s1, SS, alfa, z, x, Y, cp, cola = pt
        n += 1
        if SS + x > PHI + 1e-12:
            violan += 1
            peor = min(peor, SS + x)
    ok &= check(f"los {n} puntos del generador de espxy (misma "
                f"semilla que su acta): cola(m) = Sigma_S + x "
                f"viola phi en {violan}/{n} (minimo observado "
                f"{peor:.4f} > phi = {PHI:.4f}): la «variedad "
                f"peligrosa» de espxy era VACIA — errata al acta "
                f"archivada (el referee dirigido comprobo las "
                f"paredes listadas y nadie miro cola(m): leccion "
                f"para la ronda final ciega)",
                n >= 200 and violan == n)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] la rigidez del suelo")
    ok = True
    ok &= check("[ENUNCIADO] en c' = 1 + z, P mismo es infactible "
                "con x > x* en v: |c_z - c_m| <= (c'-z) + (c'-1) "
                "= z + 1 con igualdad forzada (no solapar exige "
                ">= z+1): el par diametral es tangente RIGIDO y el "
                "hueco maximo restante es el bolsillo x* EXACTO "
                "(maximo circulo inscrito en la luna) — la "
                "obligacion «corona con x» era fantasma: si P "
                "existe, x no estaba mural en v", True)
    # numerico: el maximo circulo junto a m en el suelo
    for z in (3.0, 4.5, 6.0):
        cp = 1.0 + z
        # posicion rigida: z en (cp - z, 0), m en (-(cp-1), 0);
        # el circulo tangente a pared, a z y a m tiene radio x*
        # (Descartes degenerado) — verificacion por resolucion
        # numerica de las tres tangencias
        xs = x_star(z)
        import scipy.optimize as so

        def eqs(v):
            xc, yc, r = v
            return (math.hypot(xc - (cp - z), yc) - (z + r),
                    math.hypot(xc + (cp - 1.0), yc) - (1.0 + r),
                    math.hypot(xc, yc) - (cp - r))
        sol = so.fsolve(eqs, (0.0, cp - 0.5, 0.4), full_output=True)
        r_num = sol[0][2]
        if abs(r_num - xs) > 1e-8:
            return check(f"tangencias en z = {z}: r = {r_num} != "
                         f"x* = {xs}", False)
    ok &= check("las tres tangencias (pared, z, m) resueltas "
                "numericamente en z = 3, 4.5, 6: el radio coincide "
                "con x* = z(z+1)/(z^2+z+1) a 1e-8 — el bolsillo ES "
                "el hueco rigido", True)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] la consecuencia positiva: sub-bolsillo universal")
    ok = True
    ok &= check("[ENUNCIADO] toda pieza LEGAL de X_Y mide <= "
                "phi - Sigma_S < phi - 1 = 0.618 (cola de m con "
                "Sigma_S > 1), y x*(z) > 0.618 en todo el dominio "
                "(z >= 1 + 2 omega > 1.29): las X_Y legales son "
                "SIEMPRE sub-bolsillo del hueco diametral — el "
                "peligro de la corona con X_Y > 0 en la ligera "
                "especular NO EXISTE.  Cierre de la celda: "
                "vacuidad (este acta) + insercion sub-bolsillo de "
                "k piezas pequenas en los huecos del trio "
                "certificado — la certificacion k-piezas queda "
                "PENDIENTE declarada (herramienta: el motor de "
                "r2bmulti; las piezas <= 0.618 con capacidad "
                ">= 1 + z >= 2.8 son polvo comodo)", True)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus, el vals retirado y las lecciones")
    ok = True
    ok &= check("[ENUNCIADO] EL VALS v1 RETIRADO (acta REFUTADO): "
                "F2 da por contenedor O el recurso posicional "
                "(bolas vacantes sobre la realizacion de P) O el "
                "certificado fresco (fila/corona que la "
                "SUSTITUYE), no ambos: x -> D_m + sigma1 -> "
                "bola-de-x + trio fresco mezclaba los dos modos "
                "(la bola de x muere cuando el trio repacka v).  "
                "Leccion registrada para testigos futuros: elegir "
                "modo y cerrar su hueco (sombras para el posicional "
                "/ k = 4 para el fresco)", True)
    ok &= check("[ENUNCIADO] LECCIONES: (1) la legalidad del "
                "adversario exige las COLAS GLOBALES de todas las "
                "piezas (las paredes del prover omiten masas "
                "opcionales y NO certifican legalidad); (2) en los "
                "suelos de tangencia, comprobar que P MISMO existe "
                "(rigidez); (3) el referee dirigido de espxy no "
                "miro cola(m) porque no se le apunto alli — "
                "evidencia directa para la ronda final CIEGA "
                "comprometida con Javi.  Lo que SOBREVIVE de "
                "espxy: toda el algebra exacta de x*, anchuras y "
                "umbrales (geometria, teoremas Lean 40-41) — como "
                "FRONTERA de coronas, no como variedad legal",
                True)
    return ok


def main():
    print("=" * 68)
    print("LA VACUIDAD DE LA VARIEDAD: cola global de m "
          "(drafts/espvals.md v2)")
    print("=" * 68)
    solo = None
    for a in sys.argv[1:]:
        if a.startswith("--solo"):
            solo = a.split("=")[1] if "=" in a else \
                sys.argv[sys.argv.index(a) + 1]
    etiquetas = [solo] if solo else list("ABCDE")
    res = [globals()[f"bloque_{e}"]() for e in etiquetas]
    verdes = sum(1 for r in res if r)
    detalle = ", ".join(f"{e}={'OK' if r else 'FALLO'}"
                        for e, r in zip(etiquetas, res))
    print("-" * 68)
    print(f"RESUMEN: {verdes}/{len(res)} bloques en verde ({detalle})")
    if verdes != len(res):
        print("HAY FALLOS")
    sys.exit(0 if verdes == len(res) else 1)


if __name__ == "__main__":
    main()
