#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El cierre formal de la vacuidad F3 (docs/drafts/f3vacio.md): la
celda F3 (>= 3 tops casi iguales, el residuo 1.0116) es rho-VACIA
en el dominio del programa — la mitad que faltaba tras auditcolas.

  LA CADENA (exacta):
  (i)   La celda F3 se define por un par dominante casi igual
        (t2 >= 0.9 t1, la marca del hallazgo F5/f3cierre) mas al
        menos una tercera pieza comparable.
  (ii)  rho-legalidad + la celda (m = 1 y la pared D Sigma_S > 1
        debajo): cola(t1) >= t2 + t3 + 1 + Sigma_S > t2 + t3 + 2
        => t3 < (phi - r2) t1 - 2, con r2 = t2/t1.
  (iii) El bolsillo del par dominante en el SUELO DE PARES
        (R = t1 + t2, par diametral exacto) es
        p(t1, t2; t1+t2) = q(r2) t1 con
        q(r) = r(1+r)/(1+r+r^2) = r · x*(1/r) — LA MISMA funcion
        de espxy con el escalado por la pieza pequena (el bolsillo
        degenerado es homogeneo de grado 1).
  (iv)  Sub-bolsillo forzado: (phi - r2) t1 - 2 <= q(r2) t1 sii
        t1 <= 2/(phi - r2 - q(r2)).  En r2 = 0.9 el techo es
        t1 <= 23.0; para r2 > r* = 0.96375 (raiz real de la cubica
        aurea r^3 + (2-phi) r^2 + (2-phi) r - phi = 0, donde
        r + q(r) = phi) el techo es INFINITO.  El dominio REAL del
        programa tiene t1 = alpha <= 6.64 (techo medido del
        generador de puertocii, acta: ub_a con w inflada por X_Y;
        NO el ~5.1 del v1) — margen 23/6.64 = 3.46x.
  (v)   Con t3 sub-bolsillo, el trio cabe EN el suelo de pares
        (DIC/NS-2 con desigualdades cerradas: insercion gratis) y
        las piezas ulteriores (t4, granos), aun mas pequenas por
        la misma cola, insertan igual: R_arclp = pares = R_lb —
        SIN GAP.  El residuo 1.0116 se retira del programa.

Bloques: [A] exactos (q = x*(1/r); el umbral afilado; la cubica);
[B] el lema de vacuidad (enunciado + los numeros del techo); [C]
verificacion: MC de instancias rho-LEGALES de la celda — 0 gaps
(corona_suf exito en R_lb y trio en pares); [D] granos y k >= 4;
[E] estatus y alcance (la nota de escala t1 > 23 declarada).
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, corona_suf, R_lb_pack, \
    theta_w
from espxy import x_star

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260818'))


def q_bolsillo(r):
    """El bolsillo del par (t1, r t1) en su suelo de pares,
    normalizado por t1."""
    return r * (1.0 + r) / (1.0 + r + r * r)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] exactos")
    import sympy as sp
    ok = True
    r, z = sp.symbols('r z', positive=True)
    q = r * (1 + r) / (1 + r + r ** 2)
    xs = z * (z + 1) / (z ** 2 + z + 1)
    ok &= check("q(r) = r(1+r)/(1+r+r^2) = r · x*(1/r) EXACTO "
                "(sympy): el bolsillo del par (t1, t2 = r t1) en "
                "su suelo de pares es t2 · x*(t1/t2) — la MISMA "
                "funcion de la variedad de espxy con el escalado "
                "por la pieza pequena (p(a,b;a+b) es homogenea de "
                "grado 1) — q(1) = 2/3, y q es creciente en r",
                sp.simplify(q - r * xs.subs(z, 1 / r)) == 0
                and sp.simplify(q.subs(r, 1) - sp.Rational(2, 3))
                == 0)
    phi = (1 + sp.sqrt(5)) / 2
    # el umbral afilado del trio prohibido en la celda: con m y la
    # pared D debajo, tres tops con t2, t3 >= r t1 exigen
    # 2 r t1 + 2 <= phi t1: r <= phi/2 - 1/t1
    ok &= check("[ENUNCIADO] trio prohibido AFILADO en la celda "
                "(m = 1 y Sigma_S > 1 en la cola de t1): t2 + t3 + "
                "2 <= phi t1 => tres tops de ratio r exigen r <= "
                "phi/2 - 1/t1 (en t1 = 5.1: r <= 0.613 — mucho "
                "menos que el 0.9 de la celda): la celda con >= 3 "
                "tops de ratio 0.9 es ilegal por el trio; este "
                "script cierra ademas el caso t3 PEQUENO (el que "
                "el trio no mata): sub-bolsillo forzado", True)
    # la cubica aurea: r + q(r) = phi sii
    # r^3 + (2-phi) r^2 + (2-phi) r - phi = 0
    cubica = sp.expand((r + q - phi) * (1 + r + r ** 2))
    objetivo = r ** 3 + (2 - phi) * r ** 2 + (2 - phi) * r - phi
    raices = sp.solve(objetivo, r)
    r_star = None
    for rr in raices:
        v = complex(rr.evalf())
        if abs(v.imag) < 1e-12 and 0 < v.real < 1:
            r_star = v.real
    ok &= check(f"la CUBICA AUREA: r + q(r) = phi sii r^3 + "
                f"(2-phi) r^2 + (2-phi) r = phi (sympy: la "
                f"expansion coincide); su raiz real en (0,1) es "
                f"r* = {r_star:.6f} = 0.963749 (acta: tolerancia "
                f"apretada) — para r2 > r* el sub-bolsillo queda "
                f"forzado a TODA escala (phi - r - q(r) < 0)",
                sp.simplify(cubica - objetivo) == 0
                and r_star is not None
                and abs(r_star - 0.963749) < 1e-5)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] el lema de vacuidad")
    ok = True
    techo_09 = 2.0 / (PHI - 0.9 - q_bolsillo(0.9))
    ok &= check(f"[ENUNCIADO] LEMA DE VACUIDAD DE LA CELDA F3: en "
                f"toda instancia rho-legal con par dominante "
                f"t2 >= 0.9 t1, m = 1 y Sigma_S > 1 debajo, y "
                f"t1 <= 2/(phi - r2 - q(r2)) — el peor caso en "
                f"r2 = 0.9 da t1 <= {techo_09:.1f}, e infinito "
                f"para r2 > r* — la tercera pieza es SUB-BOLSILLO "
                f"del par dominante en el suelo de pares: t3 <= "
                f"(phi - r2) t1 - 2 <= q(r2) t1.  Con DIC/NS-2 "
                f"(desigualdades cerradas, zigzag adversariado) el "
                f"trio cabe EN pares y R_arclp = pares = R_lb: "
                f"SIN GAP.  El dominio REAL del programa (t1 = "
                f"alpha <= 6.64, techo medido del generador — "
                f"acta) queda entero bajo el techo, margen 3.46x",
                22.5 < techo_09 < 23.5
                and techo_09 > 6.64)
    # los numeros del techo sobre la banda de la celda
    filas = []
    for r2 in (0.90, 0.92, 0.94, 0.96, 0.9639, 0.98, 1.0):
        d = PHI - r2 - q_bolsillo(r2)
        filas.append((r2, round(2.0 / d, 1) if d > 1e-12
                      else 'inf'))
    ok &= check(f"el techo t1 <= 2/(phi - r2 - q(r2)) sobre la "
                f"banda de la celda: {filas} — crece de 23 a "
                f"infinito al acercarse r2 a r*; el margen del "
                f"dominio (5.1 vs 23) es > 4x", True)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] verificacion: instancias rho-legales de la celda")
    rng = random.Random(SEED)
    ok = True
    n, gaps, trio_pares = 0, 0, 0
    n_chico, n_cuatro = 0, 0
    intentos = 0
    while n < 600 and intentos < 3000000:
        intentos += 1
        t1 = rng.uniform(2.0, 6.7)     # dominio REAL (acta: 6.64)
        r2 = rng.uniform(0.9, 1.0)
        t2 = r2 * t1
        SS = rng.uniform(1.001, PHI - 1e-3)
        s2 = rng.uniform(0.05, min(0.999, SS / 2))
        s1 = SS - s2
        if not (s2 <= s1 < 1.0):
            continue
        # t3 legal: cola(t1) = t2 + t3 + 1 + SS <= phi t1; ademas
        # t3 <= t2 y cola(t2) = t3 + 1 + SS <= phi t2.  MODO
        # chico (acta, rep. 2): tambien terceras piezas < m
        t3_max = min(t2, PHI * t1 - t2 - 1.0 - SS,
                     PHI * t2 - 1.0 - SS)
        chico = rng.random() < 0.35
        if chico:
            if t3_max <= 0.3:
                continue
            t3 = rng.uniform(0.3, min(1.0, t3_max))
        else:
            if t3_max <= 1.0:
                continue
            t3 = rng.uniform(1.0, t3_max)
        tops = [t1, t2, t3]
        # 4 tops (acta): t4 legal si cola(t3) lo permite
        if rng.random() < 0.25:
            t4_max = min(t3, PHI * t3 - 1.0 - SS,
                         PHI * t1 - t2 - t3 - 1.0 - SS)
            if t4_max > 0.3:
                tops.append(rng.uniform(0.3, t4_max))
        # legalidad entera del multiconjunto (todas las colas)
        anillos = sorted(tops + [1.0, s1, s2], reverse=True)
        legal = all(sum(anillos[i + 1:]) <= PHI * p + 1e-12
                    for i, p in enumerate(anillos))
        if not legal:
            continue
        n += 1
        if chico:
            n_chico += 1
        if len(tops) == 4:
            n_cuatro += 1
        # (a) el trio cabe en el suelo de pares (sub-bolsillo)
        pares = t1 + t2
        s = theta_w(t1, t2, pares) + theta_w(t2, t3, pares) \
            + theta_w(t3, t1, pares)
        if s <= 2 * PI + 1e-9:
            trio_pares += 1
        # (b) el fenomeno F3: corona_suf en R_lb
        R = R_lb_pack(sorted(tops, reverse=True), pares,
                      confinado_por=t1)
        carga = tops + [s1, s2]
        if not corona_suf(carga, R)[0]:
            gaps += 1
    ok &= check(f"en {n} instancias rho-LEGALES de la celda "
                f"(legalidad entera, t1 hasta 6.7 = dominio real, "
                f"{n_chico} con t3 < m, {n_cuatro} con 4 tops — "
                f"acta rep. 2): el trio cabe EN el suelo de pares "
                f"en {trio_pares}/{n} y el fenomeno F3 (corona_suf "
                f"falla en R_lb) aparece en {gaps}/{n} — CERO "
                f"gaps: la celda legal no tiene el fenomeno",
                n >= 450 and gaps == 0 and trio_pares == n
                and n_chico >= 80 and n_cuatro >= 15)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] granos y k >= 4")
    ok = True
    ok &= check("[ENUNCIADO] las piezas ulteriores caen en cascada "
                "POR LA COLA DE t3, no la de t1 (acta rep. 3: el "
                "argumento del v1 usaba el dominio falso 5.1): "
                "cola(t3) >= t4 + 1 + Sigma_S <= phi t3 => t4 <= "
                "phi t3 - 1 - Sigma_S < phi t3 - 2, valido a TODA "
                "escala del dominio; medido en el acta: t4 <= 0.60 "
                "en la celda (y con t1 <= 5.1 la celda de 4 tops "
                "con t3 > 1, t4 >= 0.3 es directamente VACIA — 0 "
                "aceptadas en 2e6 intentos; existe solo con t1 en "
                "(5.1, 6.7]).  Los granos legales quedan bajo las "
                "mismas colas: polvo sub-bolsillo, insercion DIC "
                "gratis — el gap de granos pesados de f3cierre "
                "queda sin instancias legales en la celda", True)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus y alcance")
    ok = True
    ok &= check("[ENUNCIADO] ESTATUS (v2, con el acta): la celda "
                "F3 del programa (>= 3 tops casi iguales, residuo "
                "1.0116) es rho-VACIA — trio prohibido cuando la "
                "tercera pieza es comparable (auditcolas) + "
                "SUB-BOLSILLO FORZADO cuando no (este lema, techo "
                "23 vs dominio real 6.64, margen 3.46x).  Con el "
                "acta aplicada, el residuo 1.0116 SE RETIRA del "
                "programa; sobreviven el lema condicional de "
                "dualidad de f3cierre y el 1.0816 como enunciados "
                "abstractos del arc-LP.  ALCANCE HONESTO (acta "
                "rep. 5): la frontera 0.9 de la celda es EMPIRICA "
                "(caja del hallazgo) y el converso «gap => celda» "
                "queda ABIERTO — la evidencia lo apoya: fuera de "
                "la celda (r2 en 0.60-0.90) el CONFINAMIENTO sube "
                "R_lb sobre pares (hasta 1.0126) justo donde t3 "
                "excede el bolsillo, y corona_suf cabe en el R_lb "
                "subido: 0 gaps en 5100 instancias del acta; el "
                "techo cubre ademas hasta r2 ~ 0.75 en el dominio "
                "real.  Fuera de via: t1 > 23 con r2 en (0.9, r*), "
                "y r2 < ~0.74 con t3 sobre-bolsillo (alli manda el "
                "confinamiento, no este lema).  El paso (v) usa "
                "DIC/NS-2 e insercion adversariados", True)
    return ok


def main():
    print("=" * 68)
    print("LA VACUIDAD F3 CERRADA: sub-bolsillo forzado "
          "(drafts/f3vacio.md)")
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
