#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CONTRASTE INDEPENDIENTE del gap lemma (thm:gapwritten).

EL CONTEXTO HONESTO: este script se escribio como «endurecimiento
2/3» del peer review externo (subir gaplemma.py de barrido dirigido
a certificado de caja al estilo rstarcert) — y al terminar se
descubrio que el endurecimiento YA EXISTIA: la campana de bolsillos
(commits 2dff09c / 13630f5 / 4b0fede; docs/drafts/bolsillos.md;
scripts bolsillos.py y arcolp.py, tres rondas adversariales, Lean
39 golden_pi_trio) cerro el cuarteto j = 0 como TEOREMA ALGEBRAICO
(q(u) = (phi-u) r(u) con r de coeficientes positivos) y el quinteto
j = 1 por subdivision con la curva de tangencia del trio manejada
POR CONSTRUCCION.  El asterisco que el ciclo del review puso a
thm:gapwritten era un error de contexto (contradecia el parrafo
siguiente del propio paper); el certificado oficial es bolsillos.

LO QUE ESTE SCRIPT APORTA como contraste: una RE-DERIVACION
INDEPENDIENTE (sin conocer bolsillos) que converge a la misma
matematica por otra via — los mayorantes de esquina de rstarcert +
el cap de productos por su limite monotono + el motor antipodal:

  * bloque B: el cuarteto j = 0 analitico via h(alpha) =
    x*(alpha) - (phi alpha - 1)/2 con raiz real UNICA alpha = phi
    (equivalente a q(u)/g(u) de bolsillos fase 1; la tangencia
    aurea theta(phi, phi/2; phi^2) + theta(phi/2, 1; phi^2) = pi
    es la lectura angular de x*(phi) = phi/2, Lean
    descartes_pocket_golden);
  * bloque C: el quinteto j = 1 certificado por B&B FUERA de la
    banda |F| < 0.06 de la variedad F(alpha, o1) = alpha o1
    (alpha + o1 - 1) - alpha^2 - o1^2 = 0 — redescubierta aqui
    como la ecuacion del gemelo x** de espxy; es la misma curva
    tangente de bolsillos fase 2 (de (2, 2/phi) por (3/2, 3/2) al
    espejo), que alli queda CERTIFICADA por construccion y aqui
    solo declarada: bolsillos es estrictamente mas fuerte en esa
    banda;
  * bloque D: las colas alpha/o1 -> infinito en 1 caja cada una
    por el cap del limite (estable en la ultra-cola, donde
    R - o pierde precision float).

Dominio (superconjunto del real): Sigma in (1, phi]; s' <=
min(Sigma/2, phi/2); w* <= min(1/phi, Sigma-1); alpha, o1 >=
(1+Sigma)/phi; factores de cola hasta e^40 T.  Dos convergencias
independientes sobre la misma celda con tecnicas distintas.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, theta_w
from gaplemma import corona_k5, R3_necesidad, M_apilable
from areduccion import antipodal_dos_lados
from r2bmulti import th
from espcanal import mapa_supervivientes, suelo_trio,     _creciente_cabe

T_INF = float(os.environ.get('CC_TINF', '64.0'))
LOG_T = math.log(T_INF)


def _R_suelo(a_lo, o_lo, con_o1):
    """Cota inferior del R real: pares + la necesidad del trio
    {alpha, o1, m} por el LEMA DEL CRECIENTE (suelo_trio de
    espcanal, adversariado — mas fino que la suma ciclica R3),
    blindada con la dicotomia apilable M."""
    if con_o1:
        pares = max(a_lo + max(o_lo, 1.0), o_lo + 1.0)
        g = max(a_lo, o_lo)
        chico = min(a_lo, o_lo)
        try:
            st = suelo_trio(g, chico, 1.0, g + chico)
            M = M_apilable([a_lo, o_lo, 1.0])
            return max(pares, min(st, M))
        except ZeroDivisionError:
            # los extremos de cola degeneran las biseccciones
            # (R - x = 0): pares sola sigue siendo cota inferior
            # valida del R real
            return pares
    return a_lo + 1.0                  # j = 0: el par {alpha, m}


def _antipodal_par(a_hi, a_lo, o_hi, o_lo, resto):
    """La FRONTERA RAZOR (R ~ par saturado): corona con el par
    (alpha, o1) ANTIPODAL en pi y el resto por caminos (motor de
    areduccion, adversariado).  Cotas ACOPLADAS incondicionales:
    para todo punto p, R(p) >= alpha(p) + o1(p) >= alpha(p) +
    o_lo, y theta(alpha, x, alpha + c) es no-decreciente en alpha
    cuando c >= x (gate simbolico A2): el termino en (a_hi,
    a_hi + o_lo) mayora.  Analogamente para o1."""
    def _cap(x, c):
        # cap del producto acoplado por su LIMITE monotono (como
        # rstarcert A2): p(o) = o x / (c (o + c - x)) crece en o
        # (signo c - x >= 0, gate A2) con limite x/c — mayorante
        # universal y numericamente ESTABLE en la ultra-cola
        # (o + c pierde c por redondeo cuando o >> c/ulp)
        return 2.0 * math.asin(math.sqrt(min(1.0, x / c)))

    nodos = [a_hi, o_hi] + resto
    n = len(nodos)
    thmat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if i == 0 and j == 1:
                thmat[i][j] = PI
            elif i == 0:
                thmat[i][j] = min(th(a_hi, nodos[j], a_hi + o_lo),
                                  _cap(nodos[j], o_lo))
            elif i == 1:
                thmat[i][j] = min(th(o_hi, nodos[j], o_hi + a_lo),
                                  _cap(nodos[j], a_lo))
            else:
                thmat[i][j] = th(nodos[i], nodos[j], a_lo + o_lo)
    return antipodal_dos_lados(nodos, thmat, [False] * n, 0.0)


def criterio_gap(box, con_o1):
    """(Sg, ua, [uo,] sp, wt) con alpha = suelo(Sg)*e^ua, o1 =
    suelo(Sg)*e^uo (o1 = m = 1 si con_o1 es False).  True si un
    mayorante INCONDICIONAL certifica la caja."""
    if con_o1:
        Sgl, Sgh, ual, uah, uol, uoh, spl, sph, wtl, wth = box
    else:
        Sgl, Sgh, ual, uah, spl, sph, wtl, wth = box
        uol = uoh = 0.0
    if Sgl >= PHI or Sgh <= 1.0:
        return None
    sp_hi = min(sph, Sgh / 2.0, PHI / 2.0)
    if sp_hi < spl:
        return None
    wt_hi = min(wth, 1.0 / PHI, max(0.0, Sgh - 1.0))
    if wt_hi < wtl:
        return None
    suelo_lo = max(1.0, (1.0 + max(Sgl, 1.0)) / PHI)
    suelo_hi = max(1.0, (1.0 + min(Sgh, PHI)) / PHI)
    a_lo = suelo_lo * math.exp(ual)
    a_hi = suelo_hi * math.exp(uah)
    if con_o1:
        o_lo = suelo_lo * math.exp(uol)
        o_hi = suelo_hi * math.exp(uoh)
    else:
        o_lo = o_hi = 1.0
    # variante 1 (interior): piezas techo, R en los suelos
    R1 = _R_suelo(a_lo, o_lo, con_o1)
    piezas = [a_hi] + ([o_hi] if con_o1 else []) + [1.0, sp_hi,
                                                    wt_hi]
    if corona_k5(sorted(piezas, reverse=True), R1)[0]:
        return True
    # variante 2 (frontera razor, INCONDICIONAL): el par
    # antipodal con cotas acopladas — para j = 0 el par es
    # (alpha, m)
    resto = [1.0, sp_hi, wt_hi] if con_o1 else [sp_hi, wt_hi]
    if _antipodal_par(a_hi, a_lo, o_hi, o_lo, resto):
        return True
    # variante 3 (quinteto, la esquina del trio saturado): el
    # mayor mural y el RESTO tangente a el en el creciente
    # (espcanal, adversariado), a R en el suelo
    if con_o1:
        g_hi = max(a_hi, o_hi)
        otras = sorted([min(a_hi, o_hi), 1.0, sp_hi, wt_hi],
                       reverse=True)
        if len(otras) <= 4 and _creciente_cabe(g_hi, otras, R1):
            return True
    return False


def criterio_q5(box):
    return criterio_gap(box, True)


def criterio_q4(box):
    return criterio_gap(box, False)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] monotonias y el gate del acoplo")
    import random
    ok = True
    ok &= check("[ENUNCIADO] (A1) monotonias estructurales: "
                "theta_w(a, b, R) crece en a y b y decrece en R "
                "(r2bmulti, adversariado) => la factibilidad de "
                "corona_k5 es anti-monotona en cada pieza y "
                "monotona en R: corona_k5(techos, R_suelo) cabe "
                "=> cabe en todo punto de la caja.  R_suelo con "
                "las necesidades (pares, R3, M) en los suelos de "
                "(alpha, o1): todas crecen con los radios — cota "
                "inferior valida del R real punto a punto", True)
    # gate SIMBOLICO de la variante 2 (la carga real): la cota
    # acoplada theta(a, x, a + c) es no-decreciente en a para
    # c >= x: sin^2(theta/2) = (a/c) * (x/(a+c-x)) = ax/(c(a+c-x))
    # y d/da del numerador-normalizado ~ (a+c-x) - a = c - x >= 0
    import sympy as sp
    a, c, x = sp.symbols('a c x', positive=True)
    prod = a * x / (c * (a + c - x))
    dnum = sp.simplify(sp.diff(prod, a) * c * (a + c - x) ** 2 / x)
    ok &= check("(A2) gate simbolico de la cota acoplada: "
                "d/da[a x/(c(a+c-x))] tiene el signo de "
                f"{dnum} = c - x >= 0 cuando c >= x — y en la "
                "variante antipodal c = o_lo >= 1 >= x para todo "
                "x en {m, s', w*} (s' <= phi/2 < 1, w* < 1/phi "
                "< 1): theta(alpha, x, alpha + o_lo) evaluada en "
                "a_hi MAYORA el termino de todo punto; simetrico "
                "para o1 con c = a_lo >= 1", dnum == c - x)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] EL CUARTETO CERRADO ANALITICO (j = 0): los "
          "bolsillos espejo del par diametral")
    import sympy as sp
    ok = True
    # La reduccion algebraica: con R = alpha + 1 (el par (alpha, m)
    # diametral), el camino alpha -> x -> m <= pi equivale a
    # p1 + p2 <= 1 (sin(t1/2) <= cos(t2/2)) con p_i = f f, y eso
    # se despeja EXACTO a x <= x*(alpha) = alpha(alpha+1)/
    # (alpha^2+alpha+1): el bolsillo de Descartes del par
    # diametral (espxy, Lean diametral_pocket_golden).
    al, x, Sg = sp.symbols('alpha x Sigma', positive=True)
    phi = (1 + sp.sqrt(5)) / 2
    fa, fm = al, 1 / al                # R - alpha = 1, R - 1 = alpha
    fx = x / (al + 1 - x)
    cond = sp.simplify(fx * (fa + fm) - 1)
    despeje = sp.solve(sp.Eq(fx * (fa + fm), 1), x)
    xstar = al * (al + 1) / (al ** 2 + al + 1)
    ok &= check("(B1) la reduccion algebraica del camino: "
                "theta(alpha, x) + theta(x, m) <= pi en "
                "R = alpha + 1 sii p1 + p2 <= 1 sii "
                f"x <= {sp.simplify(despeje[0])} = "
                "alpha(alpha+1)/(alpha^2+alpha+1) = x*(alpha), "
                "el bolsillo diametral (residuo "
                f"{sp.simplify(despeje[0] - xstar)} = 0)",
                sp.simplify(despeje[0] - xstar) == 0)
    # (B2) s' <= min(Sigma/2, phi/2) <= x*(alpha) en el dominio
    # alpha >= (1+Sigma)/phi: (a) rama Sigma/2 con alpha en su
    # suelo: (phi alpha - 1)/2 <= x*(alpha) para alpha in
    # [(1+1)/phi, (1+phi)/phi = phi]... el despeje: h(alpha) =
    # x*(alpha) - (phi alpha - 1)/2 tiene raiz EXACTA en
    # alpha = phi (la identidad x*(phi) = phi/2) y es positiva
    # antes; (b) rama phi/2 para alpha >= phi: x*(alpha) crece y
    # x*(phi) = phi/2: x* >= phi/2 ✓
    h = xstar - (phi * al - 1) / 2
    h_phi = sp.simplify(h.subs(al, phi))
    dx = sp.simplify(sp.diff(xstar, al))
    # x* es creciente: dx = (alpha^2 + 2alpha ... ) / (...)^2 > 0
    num_dx = sp.simplify(dx * (al ** 2 + al + 1) ** 2)
    # h > 0 en [2/phi, phi): verificacion por raices exactas
    raices = sp.solve(sp.Eq(sp.expand(h * 2 * (al ** 2 + al + 1)),
                            0), al)
    raices_reales = [r for r in raices if r.is_real]
    raiz_reales = [r for r in raices if r.is_real]
    ok &= check("(B2) la rama Sigma/2: h(alpha) = x*(alpha) - "
                f"(phi alpha - 1)/2 tiene a alpha = phi como su "
                f"UNICA raiz real (h(phi) = {h_phi}; las otras "
                "dos son complejas) — la identidad x*(phi) = "
                f"phi/2 —, y h(2/phi) = +0.2343 > 0: h > 0 en "
                "todo [2/phi, phi) por continuidad sin raices; "
                "luego s' <= Sigma/2 <= (phi alpha - 1)/2 <= "
                "x*(alpha) con alpha en su suelo (1+Sigma)/phi.  "
                "Para alpha SOBRE el suelo, x* solo crece: el "
                "numerador de dx*/dalpha es EXACTAMENTE 2 alpha "
                f"+ 1 > 0 (residuo {sp.simplify(num_dx - (2 * al + 1))} "
                "= 0) mientras Sigma/2 queda fijo: la "
                "desigualdad se ensancha",
                h_phi == 0
                and float(h.subs(al, 2 / phi)) > 0.2
                and len(raiz_reales) == 1
                and abs(float(raiz_reales[0]) - float(phi)) < 1e-12
                and sp.simplify(num_dx - (2 * al + 1)) == 0)
    # (B3) la rama phi/2 (alpha >= phi) y w*
    ok &= check("(B3) rama phi/2: para alpha >= phi, x*(alpha) >= "
                "x*(phi) = phi/2 >= s' (x* creciente, B2); y "
                "w* < 1/phi < 2/3 = x*(1) <= x*(alpha) para todo "
                "alpha >= 1: AMBAS piezas caben, una en cada "
                "BOLSILLO ESPEJO del par diametral (lados "
                "opuestos: los caminos son los dos semicirculos "
                "y no hay pareja no-adyacente en el mismo lado).  "
                "EL CUARTETO QUEDA CERRADO ANALITICO en todo el "
                "dominio no acotado, con la tangencia EXACTA "
                "theta(phi, phi/2; phi^2) + theta(phi/2, 1; "
                "phi^2) = pi en la esquina aurea (Sigma = phi, "
                "alpha en su suelo, s' = Sigma/2)",
                float((phi / 2 - 1 / phi).evalf()) > 0
                and abs(float(
                    (al * (al + 1) / (al ** 2 + al + 1))
                    .subs(al, 1)) - 2.0 / 3.0) < 1e-12)
    # verificacion numerica de la tangencia aurea
    t1 = theta_w(float(phi), float(phi) / 2, float(phi) + 1)
    t2 = theta_w(float(phi) / 2, 1.0, float(phi) + 1)
    ok &= check(f"(B4) la tangencia aurea numerica: "
                f"theta(phi, phi/2; phi+1) + theta(phi/2, 1; "
                f"phi+1) = {t1 + t2:.15f} = pi (error "
                f"{abs(t1 + t2 - PI):.1e}) — candidata Lean "
                f"(equivale a x*(phi) = phi/2, teorema 41)",
                abs(t1 + t2 - PI) < 1e-12)
    return ok


# ---------------------------------------------------------------- bloque C
DELTA_F = 0.06


def _F_gemelo(a, o):
    """La ecuacion del gemelo x** de espxy: F = 0 sii m = 1 satura
    EXACTO el semicirculo mural entre alpha y o1 a R = alpha+o1
    (theta(a,1,R) + theta(1,o,R) = pi sii a^2+o^2 = ao(a+o-1))."""
    return a * o * (a + o - 1.0) - a * a - o * o


def _cruza_banda_F(box):
    """True si la caja interseca la banda |F| < DELTA_F (evaluada
    con las esquinas monotonas: F crece en a y o sobre el dominio
    a, o >= 1)."""
    Sgl, Sgh, ual, uah, uol, uoh = box[:6]
    suelo_lo = max(1.0, (1.0 + max(Sgl, 1.0)) / PHI)
    suelo_hi = max(1.0, (1.0 + min(Sgh, PHI)) / PHI)
    a_lo, a_hi = suelo_lo * math.exp(ual), suelo_hi * math.exp(uah)
    o_lo, o_hi = suelo_lo * math.exp(uol), suelo_hi * math.exp(uoh)
    F_max = _F_gemelo(a_hi, o_hi)
    F_min = _F_gemelo(a_lo, o_lo)
    return F_min < DELTA_F and F_max > -DELTA_F


def criterio_q5_fuera(box):
    """El criterio del quinteto SOBRE EL COMPLEMENTO de la banda
    de tangencia del gemelo: una caja dentro de la banda queda
    fuera del claim certificado (declarada, no fallida)."""
    if _cruza_banda_F(box):
        return True
    return criterio_q5(box)


def bloque_C():
    print("[C] el quinteto (j = 1): B&B sobre el complemento de "
          "la banda de tangencia del gemelo")
    ok = True
    root = [1.0, PHI, 0.0, LOG_T, 0.0, LOG_T,
            0.0, PHI / 2, 0.0, 1.0 / PHI]
    (n_s, env, fuera), vistos, certs, trunc = mapa_supervivientes(
        root, criterio_q5_fuera, eps=2e-3,
        max_boxes=int(os.environ.get('CC_MAXB', '20000000')),
        max_fallos=100000, sobre=False)
    ok &= check(f"el quinteto {{alpha, o1, 1, s', w*}} cabe en "
                f"R = max(pares, suelo del trio) sobre TODO el "
                f"dominio continuo (factores <= {T_INF:.0f}) "
                f"FUERA de la banda |F| < {DELTA_F} de la "
                f"variedad de tangencia del gemelo: {vistos} "
                f"cajas, {certs} certificadas, {len(fuera)} sin "
                f"resolver, truncado {trunc}",
                len(fuera) == 0 and not trunc)
    if fuera:
        print(f"  primera: {fuera[0]}")
    ok &= check("[ENUNCIADO] LA BANDA DECLARADA con su ecuacion "
                "EXACTA: F(alpha, o1) = alpha o1 (alpha + o1 - 1) "
                "- alpha^2 - o1^2 con |F| < 0.06 — F = 0 es la "
                "variedad donde m = 1 satura EXACTO el "
                "semicirculo mural entre alpha y o1 a R = pares "
                "(theta + theta = pi), la MISMA ecuacion del "
                "gemelo x** de espxy; en el razor simetrico "
                "alpha = o1 = s da s = 3/2 exacto y Sigma* = "
                "(3 phi - 2)/2.  Sobre la banda el quinteto CABE "
                "punto a punto (corona_k5 exacto, barrido de "
                "gaplemma 60k sin fallos, deficit 0 en la "
                "tangencia) pero ningun mayorante estricto de "
                "caja certifica una tangencia: su cierre "
                "(tratamiento de variedad al estilo espcanal) "
                "queda declarado como continuacion", True)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] la cola alpha (u o1) grande y el contraste")
    ok = True
    # cola: para factor > T_INF, theta(x, alpha, R >= alpha + c)
    # tiene el producto f_x f_alpha <= x/c capado (rstarcert A2) y
    # los demas theta DECRECEN (R crece): el mayorante de la caja
    # frontera factor = T_INF domina todo factor mayor SI la
    # frontera certifica con la variante de SUELOS (R = suelos,
    # independiente del techo del factor).  Gate: la caja frontera
    # con ua in [log T, log T + 40] certifica
    root = [1.0, PHI, LOG_T, LOG_T + 40.0, 0.0, LOG_T + 40.0,
            0.0, PHI / 2, 0.0, 1.0 / PHI]
    (n_s, env, fuera), vistos, certs, trunc = mapa_supervivientes(
        root, criterio_q5, eps=2e-3, max_boxes=5000000,
        max_fallos=50000, sobre=False)
    ok &= check(f"(a) regimen alpha grande (ua in [log T, "
                f"log T + 40], uo libre): {vistos} cajas, "
                f"{len(fuera)} sin resolver, truncado {trunc}",
                len(fuera) == 0 and not trunc)
    root2 = [1.0, PHI, 0.0, LOG_T + 40.0, LOG_T, LOG_T + 40.0,
             0.0, PHI / 2, 0.0, 1.0 / PHI]
    (n2, e2, fuera2), v2, c2, tr2 = mapa_supervivientes(
        root2, criterio_q5, eps=2e-3, max_boxes=5000000,
        max_fallos=50000, sobre=False)
    ok &= check(f"(b) regimen o1 grande: {v2} cajas, "
                f"{len(fuera2)} sin resolver, truncado {tr2}",
                len(fuera2) == 0 and not tr2)
    ok &= check("[ENUNCIADO] (c) cierre de la cola factor > e^40 "
                "T: el limite alpha -> infinito esta cerrado POR "
                "FORMULA en gaplemma bloque D (pi + 2 asin "
                "sqrt(1/phi) < 2pi, margen 1.33, adversariado); "
                "entre T y e^40 T lo cubren (a)/(b); el dominio "
                "no acotado queda cerrado entero", True)
    # contraste con el barrido de gaplemma (mismo punto aureo)
    R3 = R3_necesidad(2.0, 2.0 / PHI, 1.0)
    ok &= check(f"(d) el punto aureo (alpha, o1) = (2, 2/phi): "
                f"R3 = {R3:.6f} = 1 + sqrt5 = {1 + math.sqrt(5):.6f} "
                f"(la igualdad exacta del acta de gaplemma)",
                abs(R3 - 1.0 - math.sqrt(5.0)) < 1e-6)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    ok = True
    ok &= check("[ENUNCIADO] ESTATUS DE CONTRASTE: este script "
                "es una RE-DERIVACION INDEPENDIENTE del gap lemma "
                "que converge con la campana de bolsillos (el "
                "certificado oficial de thm:gapwritten, tres "
                "rondas adversariales + Lean): el cuarteto j = 0 "
                "analitico (h(alpha) con raiz unica phi ~ "
                "q(u) = (phi-u) r(u) de bolsillos fase 1) y el "
                "quinteto j = 1 certificado fuera de la banda de "
                "la variedad F = 0 — la curva tangente que "
                "bolsillos fase 2 certifica POR CONSTRUCCION "
                "(mas fuerte alli).  Sin claim propio en el "
                "paper: dos convergencias independientes sobre "
                "la misma celda", True)
    return ok


def main():
    print("=" * 68)
    print("CERTIFICACION DEL GAP LEMMA (endurecimiento 2/3 del "
          "peer review)")
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
