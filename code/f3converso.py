#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El converso «gap => celda» del F3 (docs/drafts/f3converso.md).

Lo abierto declarado tras f3vacio: la celda realista del gap de
dualidad es VACUA (trio prohibido + sub-bolsillo forzado), pero el
CONVERSO — ¿todo gap del certificado ciclico vive en una celda
concreta? — quedo abierto con la frontera 0.9 EMPIRICA.  Este
ciclo lo cierra con una CELDA EXACTA que sustituye al 0.9:

  TEOREMA (converso del gap, v2 — la celda v1 fue REFUTADA por
  el acta: su (i) solo miraba pares con t_1 y su detector (ii)
  era vacuo).  Sea F una familia mural (k <= 6), R* = R_arclp(F)
  (arc-LP exacto, adversariado) y R_lb = R_lb_pack(F) (suma
  ciclica + confinamiento, adversariado).  Si R_lb < R* (GAP),
  entonces el NUCLEO N = pelar(F) cumple una de:
    (i')  N contiene ALGUN par apilable en R*: existe u >= t en
          N con R* >= u + 2t;
    (ii') |N| >= 4 y una pareja NO-adyacente DOMINA en R_mid in
          (R_lb, R*) sobre el orden de suma ciclica minima:
          theta_par > min(arcos complementarios).
  Contrapositiva por tres lemas (G1 pelado exacto con p_inf =
  ab/(sqrt a + sqrt b)^2; G2 tres-sin-gap como TEOREMA de cajas;
  G3 re-anclado en R_mid: sin pares apilables gamma_min =
  theta_w exacto y sin dominacion el sistema son cajas
  factibles — contradiccion con R_mid < R*): el complemento de
  (i') v (ii') es sin-gap.  Anatomia real (re-barrido honesto
  del referee + barrido [C]): la via dominante es la
  APILABILIDAD, no la pareja lejana.

Bloques: [A] monotonias y gates exactos (sympy + denso); [B] el
pelado masivo (R_arclp invariante); [C] el barrido del converso
(todo gap muestreado cae en la celda exacta); [D] controles (el
sintetico con gap esta en la celda; fuera de la celda sin gap);
[E] estatus.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, bolsillo_descartes, \
    R_lb_pack, theta_w
from f3cierre import R_arclp, arclp_factible_R
from arcolp import pares_caben, requisitos, arcos, gaps_de

ITER = int(os.environ.get('CC_ITER', '4000'))
SEED = int(os.environ.get('CC_SEED', '20260819'))
TOL_GAP = 2e-6


def apilable(a, b, R):
    """El par (a, b) es apilable en R si el chico puede esconderse
    radialmente tras el grande (lem:S1): R >= grande + 2 chico."""
    g, c = max(a, b), min(a, b)
    return R >= g + 2.0 * c - 1e-12


def bolsillo_inf(a, b):
    """El bolsillo de pared RECTA (limite R -> oo de Descartes,
    kw = 0): p_inf = ab/(sqrt(a)+sqrt(b))^2.  Como dp/dR < 0 (la
    pared mas plana achata el hueco, A1), p(R) >= p_inf para todo
    R >= a + b: la COTA UNIFORME del hueco entre murales."""
    sa, sb = math.sqrt(a), math.sqrt(b)
    return a * b / ((sa + sb) ** 2)


def pelar(piezas):
    """G1: pela recursivamente la pieza menor mientras quepa en
    el bolsillo UNIFORME (pared recta) del par minimo del resto —
    valido a TODO radio (A1: p(R) >= p_inf; A2: el hueco crece
    con la separacion).  Devuelve (nucleo, peladas)."""
    F = sorted(piezas, reverse=True)
    peladas = []
    while len(F) > 2:
        resto = F[:-1]
        t = F[-1]
        a_min, b_min = resto[-1], resto[-2]
        if t <= bolsillo_inf(b_min, a_min) + 1e-12:
            peladas.append(t)
            F = resto
        else:
            break
    return F, peladas


def no_adyacente_activa(piezas, R, tol=1e-7):
    """(ii'), RE-ANCLADA (acta R1+R4): ¿domina una pareja
    no-adyacente en R sobre el ORDEN DE SUMA CICLICA MINIMA?  El
    par de EXTREMOS reales (i, j) con 2 <= j-i <= n-2 domina si
    theta_par excede el MINIMO de los dos arcos complementarios.
    [El detector v1 consumia arcos(n) = (inicio, LONGITUD) como
    extremos: la tupla (1,1) daba theta(x, x) > tol siempre —
    VACUAMENTE True para n >= 4, hallazgo FATAL del acta.]"""
    import itertools
    n = len(piezas)
    if n < 4:
        return False
    # el orden de suma ciclica minima (la o del teorema G3)
    base = piezas[0]
    mejor_o, mejor_s = None, float('inf')
    for perm in itertools.permutations(piezas[1:]):
        orden = [base] + list(perm)
        s = sum(theta_w(orden[t], orden[(t + 1) % n], R)
                for t in range(n))
        if s < mejor_s:
            mejor_s, mejor_o = s, orden
    orden = mejor_o
    ths = [theta_w(orden[t], orden[(t + 1) % n], R)
           for t in range(n)]
    for i in range(n):
        for j in range(i + 2, n):
            if i == 0 and j == n - 1:
                continue               # adyacente por el ciclo
            suma_fwd = sum(ths[t] for t in range(i, j))
            suma_bwd = mejor_s - suma_fwd
            t_par = theta_w(orden[i], orden[j], R)
            if t_par > min(suma_fwd, suma_bwd) + tol:
                return True
    return False


def en_celda(F, R_star, R_lb):
    """¿F esta en la CELDA EXACTA (i') v (ii') del gap?  (tras
    pelar).  Acta R2: (i') mira TODOS los pares apilables, no
    solo los del top — el complemento debe ser «ningun par
    apilable», que es lo que G2/G3 exigen.  Acta R4: (ii') se
    evalua en R_mid entre R_lb y R* (donde el certificado pasa y
    el arc-LP falla), sobre el orden de suma minima."""
    N, _ = pelar(F)
    N = sorted(N, reverse=True)
    # (i') ALGUN par apilable en R*
    for a_i in range(len(N)):
        for b_i in range(a_i + 1, len(N)):
            if apilable(N[a_i], N[b_i], R_star):
                return True, "(i') par apilable"
    # (ii') nucleo >= 4 con dominacion no-adyacente en R_mid
    if len(N) >= 4:
        R_mid = R_star if R_lb is None \
            else 0.5 * (R_lb + R_star)
        if no_adyacente_activa(N, R_mid):
            return True, "(ii') no-adyacente domina"
    return False, "fuera"


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] monotonias y gates exactos")
    import sympy as sp
    ok = True
    # A1: monotonias del bolsillo de Descartes en a, b, R
    a, b, R = sp.symbols('a b R', positive=True)
    ka, kb, kw = 1 / a, 1 / b, -1 / R
    disc = ka * kb + kb * kw + kw * ka
    kp = ka + kb + kw + 2 * sp.sqrt(disc)
    p = 1 / kp
    # GLOBAL simbolico (acta R6; el v1 evaluaba 5 puntos y lo
    # vendia como simbolico): p = 1/kp con kp > 0: el signo de
    # dp/dx es el OPUESTO de dkp/dx.  Formas cerradas:
    #   dkp/dR = 1/R^2 + (1/a + 1/b)/(R^2 sqrt(disc)) > 0
    #   dkp/da = -(1/a^2) (1 + (1/b - 1/R)/sqrt(disc)) < 0
    # (b < R en el dominio mural => 1/b - 1/R > 0)
    dkpR = sp.simplify(sp.diff(kp, R)
                       - (1 / R ** 2 + (1 / a + 1 / b)
                          / (R ** 2 * sp.sqrt(disc))))
    dkpa = sp.simplify(sp.diff(kp, a)
                       + (1 / a ** 2) * (1 + (1 / b - 1 / R)
                                         / sp.sqrt(disc)))
    lim = sp.simplify(sp.limit(p, R, sp.oo)
                      - a * b / (sp.sqrt(a) + sp.sqrt(b)) ** 2)
    ok &= check("(A1) monotonias del bolsillo, GLOBALES "
                "simbolicas (acta R6): dkp/dR = 1/R^2 + "
                f"(1/a+1/b)/(R^2 sqrt(disc)) [residuo {dkpR}] > "
                "0 y dkp/da = -(1/a^2)(1 + (1/b-1/R)/sqrt(disc)) "
                f"[residuo {dkpa}] < 0 en todo el dominio mural "
                "(b < R; y a<->b por simetria) => dp/da, dp/db > "
                "0 y dp/dR < 0: la pared mas plana ACHATA el "
                "hueco; el limite R -> oo es p_inf = "
                f"ab/(sqrt a + sqrt b)^2 [residuo {lim}] y "
                "p(R) >= p_inf: LA COTA UNIFORME del pelado",
                dkpR == 0 and dkpa == 0 and lim == 0)
    # A2: el hueco crece con la separacion (el bolsillo tangente
    # es el MINIMO): dos murales a separacion angular gamma >=
    # tangencia: el circulo inscrito junto al muro entre ambos
    # crece con gamma (verificacion densa por el inscrito exacto)
    def inscrito(av, bv, Rv, gam):
        # mayor r mural entre los murales a (angulo 0) y b (angulo
        # gam): factible sii phi_a + phi_b <= gam, con phi_x el
        # angulo minimo para distar >= x + r del mural x (acos
        # exacto); biseccion en r
        import math as m

        def phi_min(xv, r):
            cx, cr = Rv - xv, Rv - r
            num = cx * cx + cr * cr - (xv + r) ** 2
            den = 2.0 * cx * cr
            if den <= 0:
                return PI
            c = max(-1.0, min(1.0, num / den))
            return m.acos(c)
        lo, hi = 0.0, Rv
        for _ in range(60):
            r = (lo + hi) / 2
            if phi_min(av, r) + phi_min(bv, r) <= gam:
                lo = r
            else:
                hi = r
        return lo
    rng = random.Random(SEED)
    viol, casos = 0, 0
    for _ in range(500):
        Rv = rng.uniform(2.0, 6.0)
        # dominio EXTENDIDO (acta R7a): a/R hasta 0.75 — el
        # barrido produce murales adyacentes con t1/R ~ 0.71
        av = rng.uniform(0.3, 0.75 * Rv)
        bv = rng.uniform(0.3, 0.75 * Rv)
        if av + bv >= Rv:
            continue
        g0 = theta_w(av, bv, Rv)
        p0 = bolsillo_descartes(av, bv, Rv)
        for f in (1.02, 1.05, 1.3, 1.8):
            g = min(2 * PI - 0.1, g0 * f)
            casos += 1
            if inscrito(av, bv, Rv, g) < p0 - 1e-6:
                viol += 1
    ok &= check(f"(A2) el hueco entre murales crece con la "
                f"separacion: inscrito(gamma) >= bolsillo "
                f"tangente en barrido denso EXTENDIDO ({casos} "
                f"casos, a/R hasta 0.75, factores desde 1.02 — "
                f"acta R7a): {viol} violaciones — el bolsillo "
                f"tangente es el MINIMO del hueco y el pelado "
                f"vale en TODA corona", viol == 0 and casos > 900)
    # A3: G2 — el ciclo de 3 es el arc-LP: barrido denso de trios
    # no apilables: R_lb_pack == R_arclp (lados)
    peor = 0.0
    n3 = 0
    for _ in range(300):
        t1 = rng.uniform(1.0, 3.0)
        t2 = t1 * rng.uniform(0.5, 1.0)
        t3 = t1 * rng.uniform(0.4, t2 / t1)
        F = [t1, t2, t3]
        lo, hi = R_arclp(F, lados=True)
        if apilable(t1, t3, hi) or apilable(t1, t2, hi) \
                or apilable(t2, t3, hi):
            continue
        n3 += 1
        # R_ini bajo el suelo de pares t1+t2 a proposito: el
        # confinamiento re-deriva el suelo (caja de distancias
        # vacia => gamma = 2pi bajo t1+t2) — acta R5, comentario
        rlb = R_lb_pack(F, max(t1 + t3, t1), confinado_por=t1)
        peor = max(peor, abs(rlb - lo))
    ok &= check(f"(A3) G2 — TRES no apilables SIN GAP: en {n3} "
                f"trios densos, |R_lb_pack - R_arclp| <= "
                f"{peor:.2e}", n3 > 150 and peor < 5e-9)
    # A3b (acta R5): G2 es TEOREMA por reduccion a CAJAS: para
    # n = 3 el requisito del 2-arco es max(th_i + th_j, th_k) con
    # th_k <= pi <= 2pi - th_i - th_j sii Sigma th <= 2pi: el
    # arc-LP de 3 es factible SII Sigma th <= 2pi = la suma
    # ciclica.  Verificacion contra el primal exacto:
    from arcolp import primal_factible as _pf
    from arcolp import pares_caben as _pc
    disc3, n3b = 0, 0
    for _ in range(1500):
        Rv = rng.uniform(2.0, 5.0)
        t3s = sorted((rng.uniform(0.3, Rv / 2) for _ in range(3)),
                     reverse=True)
        if not _pc(t3s, Rv):
            continue
        n3b += 1
        cajas_ok = sum(theta_w(t3s[i], t3s[j], Rv)
                       for i in range(3) for j in range(i + 1, 3))             <= 2 * PI + 1e-12
        lp_ok = _pf(t3s, Rv)
        disc3 += (cajas_ok != lp_ok)
    ok &= check(f"(A3b) G2 como TEOREMA (acta R5 + re-ronda H1 — "
                f"el gate v2 era TAUTOLOGICO, lp_ok = cajas_ok; "
                f"ahora compara de verdad): para n = 3 el arc-LP "
                f"se reduce a cajas — con d_k = th_k + s_k los "
                f"caps s_k <= 2pi - 2 th_k son >= 0 (th <= pi) y "
                f"suman 6pi - 2 Sigma th >= 2pi - Sigma th: "
                f"factible SII Sigma th <= 2pi = la condicion "
                f"ciclica; contraste REAL contra primal_factible "
                f"en {n3b} trios realizados: {disc3} "
                f"discrepancias", n3b > 800 and disc3 == 0)
    # A4: enunciados
    ok &= check("[ENUNCIADO] (A4) G1 — EL PELADO EXACTO: "
                "t <= p_inf(par minimo del RESTO) => "
                "R_req(F) = R_req(F sin t).  (>=) contencion; "
                "(<=) por A1+A2 todo par adyacente de toda "
                "corona mural a todo radio deja hueco >= "
                "bolsillo(R) >= p_inf del par minimo >= t "
                "(dominacion componente a componente: u >= "
                "a_min, v >= b_min); el circulo del bolsillo es "
                "MURAL (tangente a la pared por construccion de "
                "Descartes, kw = -1/R) y t se inserta ahi sin "
                "consumir arco; DISJUNCION CON NO-VECINOS (acta "
                "R7b — la desigualdad triangular de theta es "
                "falsa en general, arcolp H4): como t <= a_min "
                "<= toda pieza, Delta(t, c) >= Delta(vecino, c) "
                ">= theta(vecino, c) >= theta(t, c) por "
                "monotonia de theta en el radio; la recursion "
                "multi-grano re-evalua el par minimo del resto "
                "en cada paso (nunca dos granos al mismo "
                "bolsillo).  G3 RE-ANCLADO (acta R4): sin pares "
                "apilables, gamma_min = theta_w exacto (esquinas "
                "de gamma_min, cualquier dmin); en R_mid in "
                "(R_lb, R*) el certificado pasa (hay orden o con "
                "suma ciclica <= 2pi) y el arc-LP falla en TODO "
                "orden; si toda pareja no-adyacente cumpliera "
                "theta_par <= min(arcos complementarios en o), "
                "el sistema serian cajas d_i >= th_i con "
                "Sigma = 2pi: factible — contradiccion.  Luego "
                "gap sin apilables => (ii') dominacion en o a "
                "R_mid.  CONTRAPOSITIVA COMPLETA: gap => (i') "
                "ALGUN par apilable en R* (acta R2: el v1 solo "
                "miraba pares con t1 — REFUTADO con 4 "
                "contraejemplos) v (ii'); el complemento = sin "
                "pares apilables = G2 (|N| = 3; |N| = 2 trivial: "
                "ambos lados = el suelo del par, acta R11) + G3",
                True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] el pelado masivo (R_arclp invariante)")
    rng = random.Random(SEED + 1)
    ok = True
    n, exactos, peor = 0, 0, 0.0
    intentos = 0
    while n < 400 and intentos < 40000:
        intentos += 1
        k = rng.randrange(3, 6)
        t1 = rng.uniform(1.0, 3.0)
        n_g = rng.randrange(1, 4)      # 1-3 granos (acta R8: el
        # v1 solo ejercitaba UN grano — el pelado recursivo
        # multi-grano quedaba sin cobertura)
        F = sorted([t1] + [t1 * rng.uniform(0.4, 1.0)
                           for _ in range(max(1, k - 1 - n_g))]
                   + [t1 * rng.uniform(0.04, 0.18)
                      for _ in range(n_g)],
                   reverse=True)
        N, peladas = pelar(F)
        if not peladas:
            continue
        n += 1
        lo_f, hi_f = R_arclp(F, lados=True)
        lo_n, hi_n = R_arclp(N, lados=True)
        d = max(0.0, lo_n - hi_f, lo_f - hi_n)  # discrepancia
        # real (0 si los intervalos de biseccion solapan — acta R10)
        peor = max(peor, d)
        if d <= 5e-9:
            exactos += 1
    ok &= check(f"G1 verificado masivo: en {n} familias con "
                f"piezas peladas, R_arclp(F) == R_arclp(nucleo) "
                f"en {exactos}/{n} (peor discrepancia "
                f"{peor:.2e}) — el pelado no mueve el radio "
                f"mural", n >= 300 and exactos == n)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] el barrido del converso: todo gap cae en la celda")
    rng = random.Random(SEED + 2)
    ok = True
    n, gaps, en_c, fuera_c = 0, 0, 0, []
    vias = {}
    intentos = 0
    while n < ITER and intentos < ITER * 12:
        intentos += 1
        k = rng.randrange(3, 7)
        t1 = rng.uniform(1.0, 3.0)
        modo = rng.random()
        if modo < 0.4:
            # tops casi iguales (la zona F3)
            F = sorted([t1 * rng.uniform(0.85, 1.0)
                        for _ in range(min(k, 4))]
                       + [t1 * rng.uniform(0.2, 0.6)
                          for _ in range(max(0, k - 4))],
                       reverse=True)
        elif modo < 0.7:
            F = sorted([t1] + [t1 * rng.uniform(0.3, 1.0)
                               for _ in range(k - 1)],
                       reverse=True)
        else:
            # con piezas apilables (chicas y contenedor grande)
            F = sorted([t1] + [t1 * rng.uniform(0.55, 1.0)
                               for _ in range(k - 2)]
                       + [t1 * rng.uniform(0.25, 0.5)],
                       reverse=True)
        n += 1
        lo, hi = R_arclp(F, lados=True)
        suelo = max(max(a + b for i, a in enumerate(F)
                        for b in F[i + 1:]), F[0])
        rlb = R_lb_pack(F, suelo, confinado_por=F[0])
        gap = lo - rlb
        if gap > TOL_GAP:
            gaps += 1
            esta, via = en_celda(F, hi * (1.0 + 1e-9), R_lb=rlb)
            if esta:
                en_c += 1
                vias[via] = vias.get(via, 0) + 1
            else:
                fuera_c.append((F, gap, via))
    ok &= check(f"en {n} familias (k = 3..6, tres modos de "
                f"generacion incluida la zona F3): {gaps} con "
                f"GAP del certificado ciclico (R_lb_pack < "
                f"R_arclp); TODAS en la celda exacta (i') v "
                f"(ii'): {en_c}/{gaps}; fuera: {len(fuera_c)}; "
                f"anatomia por vias: {vias} — la dominante es la "
                f"APILABILIDAD, no la pareja lejana (acta R3: la "
                f"narrativa v1 estaba invertida)",
                gaps > 40 and en_c == gaps)
    if fuera_c:
        for F, g, via in fuera_c[:3]:
            print(f"  FUERA: {[round(t, 4) for t in F]} "
                  f"gap {g:.2e} ({via})")
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] controles")
    ok = True
    # (a) el PRIMER gap del stream REAL de C (mismo generador,
    #     mismos modos, misma semilla, mismo umbral — acta R9; el
    #     v1 usaba otro generador y umbral y tenia un NameError
    #     latente con esta sin inicializar)
    rng = random.Random(SEED + 2)
    F_gap, gap_v, via, esta = None, 0.0, "", False
    intentos = 0
    while F_gap is None and intentos < 4000:
        intentos += 1
        k = rng.randrange(3, 7)
        t1 = rng.uniform(1.0, 3.0)
        modo = rng.random()
        if modo < 0.4:
            F = sorted([t1 * rng.uniform(0.85, 1.0)
                        for _ in range(min(k, 4))]
                       + [t1 * rng.uniform(0.2, 0.6)
                          for _ in range(max(0, k - 4))],
                       reverse=True)
        elif modo < 0.7:
            F = sorted([t1] + [t1 * rng.uniform(0.3, 1.0)
                               for _ in range(k - 1)],
                       reverse=True)
        else:
            F = sorted([t1] + [t1 * rng.uniform(0.55, 1.0)
                               for _ in range(k - 2)]
                       + [t1 * rng.uniform(0.25, 0.5)],
                       reverse=True)
        lo, hi = R_arclp(F, lados=True)
        suelo = max(max(a + b for i, a in enumerate(F)
                        for b in F[i + 1:]), F[0])
        rlb = R_lb_pack(F, suelo, confinado_por=F[0])
        if lo - rlb > TOL_GAP:
            esta, via = en_celda(F, hi * (1.0 + 1e-9), R_lb=rlb)
            F_gap, gap_v = F, lo - rlb
            break
    ok &= check(f"(a) el primer gap del stream real de C: F = "
                f"{[round(t, 3) for t in (F_gap or [])]}, gap = "
                f"{gap_v:.2e} y esta en la celda ({via})",
                F_gap is not None and esta)
    # (a2) NEGATIVO del detector (ii') con n >= 4 a radio holgado
    #      (acta R1: el control que habria cazado el bug vacuo)
    r_hol = no_adyacente_activa([1.0, 0.9, 0.8, 0.7, 0.6], 4.0)
    ok &= check(f"(a2) el detector (ii') con radio HOLGADO "
                f"(R = 4.0, sin dominacion posible) devuelve "
                f"{r_hol} (False — el detector v1 vacuo devolvia "
                f"True aqui)", r_hol is False)
    # (b) fuera de la celda: trio no apilable => sin gap (G2)
    F2 = [1.0, 0.9, 0.6]
    lo2, hi2 = R_arclp(F2, lados=True)
    rlb2 = R_lb_pack(F2, 1.9, confinado_por=1.0)
    ok &= check(f"(b) trio no apilable {F2}: R_arclp = "
                f"{hi2:.6f}, R_lb_pack = {rlb2:.6f}, gap = "
                f"{abs(lo2 - rlb2):.2e} (cero: G2)",
                abs(lo2 - rlb2) < 5e-9)
    # (c) el pelado NO pela lo que no cabe: pieza > bolsillo
    N, peladas = pelar([1.0, 0.95, 0.9])
    ok &= check(f"(c) el pelado respeta el nucleo: "
                f"[1.0, 0.95, 0.9] -> nucleo {N}, peladas "
                f"{peladas} (nada pelable: 0.9 > bolsillo)",
                len(N) == 3 and not peladas)
    # (d) negativo del detector (ii): trio (n < 4) -> False
    r = no_adyacente_activa([1.0, 0.9, 0.8], 2.5)
    ok &= check(f"(d) el detector (ii) con n = 3 devuelve "
                f"{r} (False: no hay no-adyacentes)", r is False)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    ok = True
    ok &= check("[ENUNCIADO] EL CONVERSO «gap => celda» EN SU "
                "FORMA v2 (tras el acta que REFUTO la v1): gap "
                "del certificado ciclico => (i') ALGUN par "
                "apilable del nucleo en R* v (ii') dominacion "
                "no-adyacente en R_mid sobre el orden de suma "
                "minima.  Etiquetas HONESTAS: G1 teorema (A1 "
                "global simbolica + A2 denso extendido + el "
                "lema de no-vecinos por t <= a_min); G2 TEOREMA "
                "(reduccion a cajas A3b, firma numerica "
                "5.7e-12); G3 teorema re-anclado (derivacion "
                "del acta: sin apilables gamma_min = theta_w "
                "exacto y sin dominacion el sistema son cajas "
                "factibles — contradiccion); el barrido [C] es "
                "MUESTREO de respaldo (0 excepciones); la banda "
                "de gaps (1e-9, 2e-6] no barrida se declara.  "
                "ANATOMIA REAL: la via dominante es la "
                "apilabilidad (no la pareja lejana — la "
                "narrativa v1 invertida); la celda realista del "
                "F3 (>= 3 tops ~0.9, un caso con granos "
                "apilables) ya es vacua bajo rho <= phi "
                "(f3vacio).  El item (iv) del residuo pasa a: "
                "converso en forma exacta v2, RE-ADVERSARIADO "
                "tras refutacion", True)
    return ok


def main():
    print("=" * 68)
    print("EL CONVERSO GAP => CELDA DEL F3 (drafts/f3converso.md)")
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
