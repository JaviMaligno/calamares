#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La variedad peligrosa de la ESP con X_Y > 0
(docs/drafts/espxy.md): EXPLORACION Y DELIMITACION (no cierre).

La rama especular de R2b con X_Y > 0 quedo declarada fuera
(r2bcert H2, r2bmulti par. 4): las piezas de X_Y viven en v y la
corona real es {z, D_m, sigma2} U X_Y en c' = Y - omega, con el
suelo c' = 1 + z por la convivencia m-z.  HALLAZGO de esta
exploracion: esa corona tiene una OBSTRUCCION REAL con frontera en
forma cerrada:

  En el suelo c' = 1 + z el par (z, m) es diametral EXACTO
  (f(z) f(1) = 1) y una pieza x de X_Y debe caber junto a m.  El
  trio {z, m, x} cabe sii

     x <= x*(z) = z(z+1)/(z^2+z+1) = p(z, 1; 1+z)

  — EL BOLSILLO DE DESCARTES del par diametral (la forma degenerada
  1/(1/a+1/b-1/R) exacta en R = a+b): la frontera de la corona ES
  el bolsillo.  El sliver infactible x en (x*, 1] tiene anchura
  1 - x* = 1/(z^2+z+1); en z = phi la anchura es 1/(2 phi^2)
  EXACTO (2 phi^2 = 2 phi + 2).  Por encima de m sigue: para
  x >= 1 el par diametral es (z, x) y m debe caber en SU bolsillo:
  infactible sii z^2 + x^2 > x z (z + x - 1), hasta un techo
  x**(z).  El rescate de cola(Y) no llega cuando

     z + omega >= phi (3 + x - phi)   [= 3 phi - 1 en x = 1, EXACTO]

  (cola minima legal (3+omega+z+x)/phi con Sigma_S -> 1+,
  alpha -> Sigma_S + omega, X's = 0 salvo X_Y = x).  Los rescates
  estandar FALLAN en la region: apilar x tras m no tiene sitio (la
  tangencia diametral agota el diametro: z + 2 + 2x > 2c'), la fila
  de D_m ya lleva sigma1 + W y no admite x ~ 1, y c' esta en su
  suelo.  La region es LEGAL (ventanas de G-g comprobadas por
  instancia) — la celda ESP X_Y > 0 NECESITA UN TESTIGO NUEVO ahi;
  rutas candidatas en [E].

Bloques: [A] el algebra exacta (frontera = bolsillo, anchuras,
umbral aureo del no-rescate); [B] legalidad de la region +
refutacion SOUND de la corona (dual del arc-LP: necesario =>
False refuta); [C] los rescates fallan y la frontera es exacta
(dentro del bolsillo SI cabe); [D] extension de la variedad
(malla en (z, omega, x)); [E] estatus honesto y rutas.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, theta_w
from arcolp import dual_factible, primal_factible

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260818'))


def x_star(z):
    """La frontera exacta: el bolsillo del par diametral."""
    return z * (z + 1.0) / (z * z + z + 1.0)


def genera_legal(rng, con_sliver):
    """Punto legal de la ESP ligera con X_Y = x (una pieza).
    Ventanas de G-g (corte X_alpha = X_z = X_m = 0 para minimizar
    cola; la legalidad no exige X > 0 en las demas).  Devuelve
    (w, s2, s1, SS, alfa, z, x, Y, cp, cola) o None."""
    w = rng.uniform(0.9, 1.6)
    s2 = rng.uniform(0.05, 0.999)
    s1 = rng.uniform(s2, 0.999)
    SS = s1 + s2
    if SS <= 1.0 or SS >= 1.0 + s2:
        return None                    # ligera
    if SS > PHI:
        return None                    # pared de masa (cola de m):
                                       # ademas fuerza s2 <= phi/2 <
                                       # x*(z) en la zona sin rescate
                                       # — el bolsillo de s2 a salvo
    if s2 <= 1.0 - w:
        return None                    # (BH) s2 + X_m > 1 - w: pared
                                       # del BLOQUEO (acta: antes se
                                       # cumplia por suerte de la caja)
    if s2 <= s1 - w:
        return None                    # (B sigma1): idem
    lo_a = max(1.0 + w, SS + w)
    hi_a = 1.0 + s2 + w
    if lo_a >= hi_a:
        return None
    alfa = rng.uniform(lo_a, hi_a)
    z = rng.uniform(alfa + w, alfa + s2 + w)
    if con_sliver:
        xs = x_star(z)                 # x* < 1 siempre (acta: la
                                       # guarda xs >= 1 era rama muerta)
        x = rng.uniform(xs + 1e-9, 1.0)
    else:
        x = rng.uniform(0.3, x_star(z) - 1e-9)
    cola = (1.0 + SS + alfa + z + x) / PHI
    if cola > 1.0 + z + w:
        return None                    # la cola rescata: fuera de
                                       # la variedad (el suelo sube)
    lo_Y = max(z + x + w, cola, 1.0 + z + w)
    hi_Y = SS + z + x + w
    if lo_Y >= hi_Y:
        return None                    # pinza: sin Y legal
    Y = lo_Y                           # el adversario elige el suelo
    cp = Y - w                         # = 1 + z exacto (sin rescate)
    return (w, s2, s1, SS, alfa, z, x, Y, cp, cola)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] el algebra exacta de la variedad")
    import sympy as sp
    ok = True
    zs, xs = sp.symbols('z x', positive=True)
    R = 1 + zs
    f = lambda t: t / (R - t)
    # (a) el par (z, m) es diametral exacto en el suelo
    ok &= check("(a) en c' = 1 + z: f(z) f(1) = [z/1][1/z] = 1 "
                "EXACTO => theta(z, m) = pi identicamente (el par "
                "diametral del suelo de convivencia)",
                sp.simplify(f(zs) * f(1) - 1) == 0)
    # (b) trio factible sii f(x)(f(z) + f(1)) <= 1 sii x <= x*
    #     (theta(z,x) + theta(x,1) <= pi sii sin(th_zx/2) <=
    #     cos(th_x1/2) sii f(z)f(x) <= 1 - f(x)f(1))
    xstar = zs * (zs + 1) / (zs ** 2 + zs + 1)
    cond = sp.simplify(f(xstar) * (f(zs) + f(1)) - 1)
    ok &= check("(b) FRONTERA EXACTA: theta(z,x) + theta(x,1) = pi "
                "sii f(x)(f(z) + f(1)) = 1 sii x = x* = "
                "z(z+1)/(z^2+z+1) (sympy: la igualdad es "
                "identica); el trio cabe sii x <= x*", cond == 0)
    # (c) x* ES el bolsillo de Descartes degenerado del par (z, 1)
    #     en R = a + b: p = 1/(1/z + 1/1 - 1/(1+z))
    p_deg = 1 / (1 / zs + 1 - 1 / (1 + zs))
    ok &= check("(c) x* = p(z, 1; 1+z) EXACTO: la forma degenerada "
                "del bolsillo (disc = 0 en R = a+b) 1/(1/z + 1 - "
                "1/(1+z)) coincide con z(z+1)/(z^2+z+1): LA "
                "FRONTERA DE LA CORONA ES EL BOLSILLO del par "
                "diametral — la misma geometria del contraejemplo "
                "de thm:DP", sp.simplify(p_deg - xstar) == 0)
    # (d) anchura del sliver y la constante aurea
    phi = (1 + sp.sqrt(5)) / 2
    ancho = sp.simplify(1 - xstar - 1 / (zs ** 2 + zs + 1))
    ancho_phi = sp.simplify(
        (1 / (zs ** 2 + zs + 1)).subs(zs, phi) - 1 / (2 * phi ** 2))
    xphi = sp.simplify(xstar.subs(zs, phi) - phi / 2)
    ok &= check("(d) anchura del sliver = 1 - x* = 1/(z^2+z+1) "
                "exacta; en z = phi vale 1/(2 phi^2) EXACTO "
                "(z^2+z+1 = 2 phi + 2 = 2 phi^2 por phi^2 = "
                "phi + 1); y x*(phi) = phi/2 EXACTO (regalo del "
                "acta) — EL MECANISMO de la proteccion de sigma2: "
                "s2 <= Sigma_S/2 <= phi/2 = x*(phi) < x*(z) para "
                "todo z > phi, y la zona sin rescate tiene z >= "
                "2.84 >> phi (barrido del referee, 2M muestras, "
                "0 puntos con s2 > x*)",
                ancho == 0 and ancho_phi == 0 and xphi == 0)
    # (e) el lado x >= 1: el par diametral es (z, x) en c' = z + x
    #     y m debe caber: infactible sii z^2 + x^2 > x z (z+x-1)
    R2 = zs + xs
    f2 = lambda t: t / (R2 - t)
    izq = sp.simplify(f2(1) * (f2(zs) + f2(xs))
                      - (zs ** 2 + xs ** 2)
                      / (xs * zs * (zs + xs - 1)))
    ok &= check("(e) lado x >= 1 (c' = z + x, par diametral (z, "
                "x)): m cabe sii f(1)(f(z) + f(x)) <= 1 sii "
                "z^2 + x^2 <= x z (z + x - 1) (identidad sympy); "
                "en x = 1 da 1 > 0: infactible — el sliver cruza "
                "x = 1 con continuidad", izq == 0)
    # (f) el umbral aureo del no-rescate de cola
    x1 = sp.Integer(1)
    umbral = sp.simplify(phi * (3 + x1 - phi) - (3 * phi - 1))
    ok &= check("(f) no-rescate de cola: cola_min = (3 + omega + z "
                "+ x)/phi (Sigma_S -> 1+, alpha -> Sigma_S + "
                "omega, X's = 0 salvo X_Y = x) no levanta el suelo "
                "sii z + omega >= phi(3 + x - phi); en x = 1 el "
                "umbral es 3 phi - 1 EXACTO (phi(4 - phi) = "
                "4 phi - phi^2 = 3 phi - 1)", umbral == 0)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] la region es legal y la corona REALMENTE no cabe")
    rng = random.Random(SEED)
    ok = True
    n, refutadas, no_ref = 0, 0, 0
    peor = None
    intentos = 0
    while n < 300 and intentos < 400000:
        intentos += 1
        pt = genera_legal(rng, con_sliver=True)
        if pt is None:
            continue
        w, s2, s1, SS, alfa, z, x, Y, cp, cola = pt
        n += 1
        # refutacion SOUND: el dual del arc-LP es NECESARIO — False
        # en todos los ordenes => la corona {z, 1, s2, x} es
        # IMPOSIBLE de verdad (no un artefacto del criterio)
        piezas = [z, 1.0, s2, x]
        base = piezas[0]
        import itertools
        alguna = False
        vistos = set()
        for perm in itertools.permutations(piezas[1:]):
            if perm[::-1] in vistos:
                continue
            vistos.add(perm)
            if dual_factible([base] + list(perm), cp):
                alguna = True
                break
        if not alguna:
            refutadas += 1
            if peor is None or z < peor[0]:
                peor = (z, w, s2, round(x, 4), round(cp, 4))
        else:
            no_ref += 1
    ok &= check(f"en {n} puntos LEGALES del sliver (ventanas de "
                f"G-g ligera, Y en su suelo, cola sin rescate por "
                f"construccion): la corona {{z, m, s2, x}} queda "
                f"REFUTADA por el dual (necesario) en TODOS los "
                f"ordenes en {refutadas}/{n} ({no_ref} donde algun "
                f"orden pasa el dual — esperable cerca de la "
                f"frontera; numeros de ESTA semilla, el gate exige "
                f"> 80%); ejemplo con z minima: {peor}",
                n >= 200 and refutadas > 0.8 * n)
    ok &= check("[ENUNCIADO] LA VARIEDAD ES REAL: configuraciones "
                "legales del bloqueo (todas las paredes y ventanas "
                "de G-g) donde la corona del testigo estandar es "
                "geometricamente imposible — no es un limite del "
                "certificado sino del TESTIGO: la celda ESP con "
                "X_Y > 0 necesita un testigo nuevo en la variedad",
                True)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] los rescates fallan y la frontera es exacta")
    rng = random.Random(SEED + 1)
    ok = True
    # (a) dentro del bolsillo SI cabe (la frontera es exacta):
    #     puntos con x < x* y el trio + s2 factible
    n, caben = 0, 0
    intentos = 0
    while n < 300 and intentos < 400000:
        intentos += 1
        pt = genera_legal(rng, con_sliver=False)
        if pt is None:
            continue
        w, s2, s1, SS, alfa, z, x, Y, cp, cola = pt
        n += 1
        # x sub-bolsillo: insercion gratis en el gap (z, m) del
        # trio {z, m, s2} — comprobamos la corona completa
        piezas = [z, 1.0, s2, x]
        base = piezas[0]
        import itertools
        vistos = set()
        okc = False
        for perm in itertools.permutations(piezas[1:]):
            if perm[::-1] in vistos:
                continue
            vistos.add(perm)
            orden = [base] + list(perm)
            if dual_factible(orden, cp) \
                    and primal_factible(orden, cp):
                okc = True
                break
        if okc:
            caben += 1
    ok &= check(f"(a) DENTRO del bolsillo (x < x*): la corona "
                f"completa {{z, m, s2, x}} cabe en {caben}/{n} "
                f"puntos legales (arc-LP primal) — la frontera "
                f"x* = p(z, 1; 1+z) separa exactamente",
                n >= 200 and caben == n)
    # (b) apilar x tras m no tiene sitio: la tangencia diametral
    #     agota el diametro (z + 2 + 2x > 2 c' sii x > 0)
    ok &= check("(b) [ENUNCIADO] rescates estandar en la variedad: "
                "APILAR x tras m no tiene sitio — COROLARIO "
                "TRIVIAL (acta: en el suelo c' = 1 + z la cadena "
                "radial exige 2z + 2 + 2x <= 2c' = 2 + 2z sii "
                "x <= 0: la tangencia diametral z-m agota el "
                "diametro con holgura radial CERO, sin necesidad "
                "de medirlo); la FILA de D_m (capacidad 1, "
                "distinta de H_m = 1-omega-X_m que tarifica BH) "
                "lleva sigma1 + W > 1 - s2 y solo admitiria x < "
                "s2 <= phi/2 < x*(z) en la zona; cola no levanta "
                "por construccion (z + omega >= phi(3 + x - "
                "phi)): los rescates adversariados FALLAN.  La "
                "imposibilidad de colocaciones INTERIORES "
                "generales descansa en no-apilabilidad + "
                "compactacion (el lema de suficiencia k = 4 sigue "
                "pendiente en la campana): DELIMITACION, no "
                "cierre interior", True)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] extension de la variedad")
    ok = True
    # malla en z: anchura del sliver y ventana legal de (z, omega)
    filas = []
    for zv in (2.0, 2.5, 3.0, 4.0, 5.0, 6.0):
        xs = x_star(zv)
        ancho = 1.0 - xs
        # z legal exige alfa >= z - s2 - w y alfa < 1 + s2 + w:
        # z < 1 + 2 s2 + 2 w <= 1 + 2 + 3.2 = 6.2 (s2 < 1, w <=
        # 1.6); el no-rescate pide z + w >= phi(3 + x - phi)
        w_min = max(0.0, PHI * (3 + 1.0 - PHI) - zv)
        w_nec = max(w_min, (zv - 1 - 2 * 0.999) / 2)
        filas.append((zv, round(xs, 4), round(ancho, 4),
                      round(w_nec, 3)))
    ok &= check(f"malla ORIENTATIVA de la variedad (z, x*, "
                f"anchura, omega minima para legalidad+"
                f"no-rescate): {filas} — sin gate real (son "
                f"numeros derivados, no una afirmacion "
                f"falsable; acta E2); la sintesis del referee: "
                f"min z = 2.84 en la zona sin rescate (2M "
                f"muestras con omega libre), min omega = 0.906, "
                f"y la parte con omega >= 1 cae en regimen de "
                f"PIVOTE SOLIDO (posible cobertura por la rama "
                f"DPr j >= 3 — pendiente de comprobar: reduciria "
                f"la variedad a omega en (0.9, 1))",
                len(filas) == 6)
    # el lado x > 1 existe: punto con x = 1.05
    zv = 4.0
    x = 1.05
    cp = zv + x                        # suelo z + X_Y
    s = theta_w(zv, x, cp) + theta_w(x, 1.0, cp) \
        + theta_w(1.0, zv, cp)
    ok &= check(f"el lado x > 1 es MODEL-CONDITIONAL (acta): en "
                f"(z, x) = (4, 1.05), c' = z + x = 5.05: suma del "
                f"trio = {s:.4f} > 2 pi = {2 * PI:.4f}, y la banda "
                f"(1, x**(4) = 1.055) es finisima — pero una pieza "
                f"x >= 1 = r_m NO esta cubierta por el convenio de "
                f"X_Y (polvo < m, coronaagujero par. 2) y su "
                f"tarifa de cola esta sin derivar: la variedad "
                f"cruza x = 1 SOLO si el modelo admite esa pieza "
                f"ahi (no establecido)", s > 2 * PI)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus honesto y rutas")
    ok = True
    ok &= check("[ENUNCIADO] ESTATUS: la celda ESP X_Y > 0 NO se "
                "cierra en esta exploracion — se DELIMITA su "
                "variedad peligrosa con frontera exacta (el "
                "bolsillo del par diametral, la misma geometria "
                "aurea del contraejemplo de thm:DP y de la curva "
                "tangente de bolsillos).  Fuera de la variedad "
                "(x <= x* o cola rescata o x >= x**) el testigo "
                "estandar funciona (C-a)", True)
    ok &= check("[ENUNCIADO] RUTAS CANDIDATAS (por orden de "
                "promesa): (i) SIMETRIA m <-> x: x < 1 = r_m es "
                "LIBRE para el intercambio (thm:oblivious solo "
                "exige acuerdo en anillos >= r_m): enviar x a otro "
                "contenedor (u, la sarten, el agujero de alpha "
                "tras el repack) y dejar la corona {z, m, s2} "
                "certificada — exige derivar la tarifa del "
                "contenedor receptor; (ii) pared nueva del "
                "bloqueo: con x ~ m en v, la pared (RY) engorda "
                "(Sigma_S + X_Y > Y - omega con X_Y ~ 1) y quiza "
                "el bloqueo mismo se contradiga en la variedad "
                "(comprobar contra las colas); (iii) contar x en "
                "cola(Y) con tarifa entera (no phi-descontada) "
                "cuando x > p: el suelo de Y subiria justo el "
                "ancho del sliver.  NADA de esto esta hecho: "
                "residuo DECLARADO con geometria exacta", True)
    return ok


def main():
    print("=" * 68)
    print("ESP X_Y > 0: la variedad del bolsillo diametral "
          "(drafts/espxy.md)")
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
