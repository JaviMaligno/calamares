#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FASE 1-BIS del lema de reduccion de |A| (REPARADA tras el
REFUTADO de la fase 1; pendiente de RE-RONDA): el motor de
reparto se sustituyo por LA SUFICIENCIA CONSTRUCTIVA COMPLETA
(_coloca_y_verifica: colocacion antipodal explicita con
posiciones acumuladas y verificacion circular de TODOS los pares
— consecutivos, no adyacentes y CRUZADOS — mas el gate de pares
factibles): los dos agujeros del acta (H1 pares cruzados, H2
pi-gorra) quedan cerrados por construccion y sus contraejemplos
son negativos fijos del bloque B.

LA HISTORIA (acta en VEREDICTOS, 2026-08-23): la fase 1
entregaba la corona reducida a espfinal._antipodal2, cuyo esquema
de caminos por lado cubre los pares cruzados SOLO bajo la
precondicion implicita «los polos mayoran en f a los
intermedios» (cierta en los usos historicos: polvo < m) — los
slots la violaban y el motor certificaba coronas infeasibles
(contraejemplo exacto en el acta).  Reparaciones de esta fase:
motor nuevo, A1 reescrito como GATE operativo (M < c no es
teorema: el regimen M >= c queda declarado fuera), los topes
M in [0.05, 13.2] de la aplicacion C(a) DECLARADOS como dominio
de barrido, control B(d) HOSTIL en la region del acta, codigo
muerto retirado.

LO QUE SOBREVIVE (verificado por el referee): los slots
ESCALONADOS (r_i <= (M - (g - i) t)/i con asignacion ordenada),
la cuerda de fila, el greedy-halving, los radios-nodo ligados a
masa y la fila Y — la matematica nueva del lema es correcta; lo
roto es el eslabon final (el motor de reparto).

FASE 1-BIS (la reparacion, pendiente): motor de dos lados con
pares cruzados explicitos (extender r2bcolas._antipodal_cola, que
ya los gatea tras su acta H2) + gate de factibilidad de pares +
A1 como condicion operativa + topes declarados + control hostil.
"""
import itertools
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check
from r2bmulti import th, cabe_matriz, banda_matriz, bnb_factible
from espfinal import _antipodal2

SEED = int(os.environ.get('CC_SEED', '20260822'))
K_CORTE = 6


def _asin2(z):
    return 2.0 * math.asin(max(0.0, min(1.0, z)))


def _cuerda(cap, c):
    """C(z)/(c - cap) con z = cap/(c - cap): peso por unidad de
    masa de una fila de piezas <= cap (r2bpool, sound)."""
    z = min(1.0, cap / max(1e-12, c - cap))
    if z < 1e-9:
        return 2.0 / max(1e-12, c - cap)
    return (2.0 * math.asin(z) / z) / (c - cap)


def _coloca_y_verifica(nodos, thmat, Ds, lado_a, lado_b,
                       exento=None):
    """SUFICIENCIA CONSTRUCTIVA COMPLETA (fase 1-bis, la
    reparacion del acta): coloca el par (0, 1) antipodal (0 en
    angulo 0, 1 en pi), el lado A en (0, pi) y el B en (pi, 2pi),
    con separaciones consecutivas EXACTAS thmat (los bloques
    ocupan ademas su peso interno Ds), y VERIFICA todos los pares
    — consecutivos, no adyacentes del mismo lado y CRUZADOS — por
    separacion circular real.  Sin precondiciones: el agujero H1
    del acta (pares cruzados no mirados) queda cerrado por
    construccion.  `exento` = par con separacion garantizada por
    la celda (p.ej. tangencia asintotica): se salta SU chequeo."""
    n = len(nodos)
    # gate H2: ningun par imposible (theta clampada a pi) salvo
    # el par antipodal exento o el (0,1) si su requisito cabe
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) == (0, 1) or (exento is not None
                                    and (i, j) == exento):
                continue
            if thmat[i][j] >= PI - 1e-12:
                return False
    pos = {0: 0.0, 1: PI}
    # lado A: 0 -> a1 -> ... -> 1 en (0, pi)
    ang = 0.0
    prev = 0
    for k in lado_a:
        ang += thmat[prev][k]
        pos[k] = ang
        if k in Ds:
            ang += Ds[k]               # el bloque ocupa [pos, ang]
        prev = k
    if ang + thmat[prev][1] > PI + 1e-12:
        return False
    # lado B: 0 -> b1 -> ... -> 1 en (2pi, pi) descendente
    ang = 2.0 * PI
    prev = 0
    for k in lado_b:
        ang -= thmat[prev][k]
        pos[k] = ang
        if k in Ds:
            ang -= Ds[k]
        prev = k
    if ang - thmat[prev][1] < PI - 1e-12:
        return False
    # verificacion COMPLETA de pares por separacion circular; los
    # bloques como intervalos [pos, pos + D] (lado A) o
    # [pos - D, pos] (lado B)
    def intervalo(k):
        if k not in Ds:
            return (pos[k], pos[k])
        if k in lado_a:
            return (pos[k], pos[k] + Ds[k])
        return (pos[k] - Ds[k], pos[k])

    def sep(k1, k2):
        a1, b1 = intervalo(k1)
        a2, b2 = intervalo(k2)
        # distancia circular minima entre los intervalos
        cands = []
        for x in (a1, b1):
            for y in (a2, b2):
                d = abs(x - y) % (2.0 * PI)
                cands.append(min(d, 2.0 * PI - d))
        if a1 <= a2 <= b1 or a1 <= b2 <= b1                 or a2 <= a1 <= b2:
            return 0.0
        return min(cands)

    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) == (0, 1) or (exento is not None
                                    and (i, j) == exento):
                continue
            if thmat[i][j] > sep(i, j) + 1e-12:
                return False
    return True


def _coloca_ciclo(nodos, thmat, Ds, orden):
    """Colocacion en CICLO SIMPLE (sin par antipodal): los nodos
    en el orden dado sobre el circulo con separaciones
    consecutivas = thmat (los bloques ocupan ademas su Ds), suma
    total <= 2 pi, y TODOS los pares verificados por separacion
    circular.  Otra suficiencia del repertorio (para coronas
    holgadas donde forzar un par a pi desperdicia).  SIN
    exenciones: la exencion de tangencia pertenece a la
    colocacion ANTIPODAL (donde la separacion del par es pi
    exacto); aqui todo par se verifica — y ninguno puede estar
    clampado a pi (gate)."""
    n = len(nodos)
    for i in range(n):
        for j in range(i + 1, n):
            if thmat[i][j] >= PI - 1e-12:
                return False
    pos = {}
    ang = 0.0
    prev = None
    for k in orden:
        if prev is not None:
            ang += thmat[prev][k]
        pos[k] = ang
        if k in Ds:
            ang += Ds[k]
        prev = k
    total = ang + thmat[orden[-1]][orden[0]]
    if total > 2.0 * PI + 1e-12:
        return False

    def intervalo(k):
        if k not in Ds:
            return (pos[k], pos[k])
        return (pos[k], pos[k] + Ds[k])

    def sep(k1, k2):
        a1, b1 = intervalo(k1)
        a2, b2 = intervalo(k2)
        cands = []
        for x in (a1, b1):
            for y in (a2, b2):
                d = abs(x - y) % (2.0 * PI)
                cands.append(min(d, 2.0 * PI - d))
        if a1 <= a2 <= b1 or a1 <= b2 <= b1 or a2 <= a1 <= b2:
            return 0.0
        return min(cands)

    for i in range(n):
        for j in range(i + 1, n):
            if thmat[i][j] > sep(i, j) + 1e-12:
                return False
    return True


def _motor_dos_lados(nodos, thmat, Ds, exento=None):
    """Reparto en dos lados + permutaciones, decidido por
    _coloca_y_verifica (todos los pares mirados).  El par (0, 1)
    antipodal; requisito del par: thmat[0][1] <= pi (no estricto
    con la colocacion a pi exacto; si thmat[0][1] = pi por
    clamp de par imposible, el gate H2 de la celda debe haberlo
    excluido — aqui se exige <= pi - MARG salvo exencion)."""
    if exento != (0, 1) and thmat[0][1] > PI - 1e-9:
        return False
    # primero la colocacion en CICLO SIMPLE (barata y decisiva
    # cuando la corona es holgada) — SOLO sin exenciones: un par
    # exento lleva thmat = 0 como convencion de la colocacion
    # antipodal (su separacion garantizada es pi), y el ciclo
    # leeria ese 0 como requisito real (unsound)
    if exento is None:
        n_n = len(nodos)
        idx = sorted(range(n_n),
                     key=lambda i: -min(nodos[i], 1e8))
        ordenes_c = [list(range(n_n)),
                     idx,
                     idx[0::2] + idx[1::2][::-1]]
        for oc in ordenes_c:
            if _coloca_ciclo(nodos, thmat, Ds, oc):
                return True
    resto = list(range(2, len(nodos)))
    for mask in range(1 << len(resto)):
        lado_a = [r for t, r in enumerate(resto) if mask >> t & 1]
        lado_b = [r for t, r in enumerate(resto)
                  if not mask >> t & 1]
        vistos = 0
        for pa in itertools.permutations(lado_a):
            for pb in itertools.permutations(lado_b):
                vistos += 1
                if vistos > 60:
                    break
                if _coloca_y_verifica(nodos, thmat, Ds,
                                      list(pa), list(pb),
                                      exento=exento):
                    return True
            if vistos > 60:
                break
    return False


def _corona_una(P, slots, M_p, cap_p, c_lo, par):
    """Una variante concreta: P + slots + 2 bloques(masa M_p) con
    la colocacion antipodal del par `par`.  Motor: la suficiencia
    constructiva completa (fase 1-bis)."""
    cap_p = min(cap_p, max(M_p, 1e-9))
    peso_lado = _cuerda(cap_p, c_lo) * (M_p / 2.0 + cap_p / 2.0)
    base = list(P) + list(slots)
    i0_, j0_ = sorted(par)
    orden = [i0_, j0_] + [k for k in range(len(base))
                          if k not in (i0_, j0_)]
    base = [base[k] for k in orden]
    nodos = base + [cap_p, cap_p]
    nb0 = len(base)
    n = len(nodos)
    thmat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            thmat[i][j] = th(min(nodos[i], 1e8),
                             min(nodos[j], 1e8), c_lo)
            thmat[j][i] = thmat[i][j]
    Ds = {nb0: peso_lado, nb0 + 1: peso_lado}
    return _motor_dos_lados(nodos, thmat, Ds)


def corona_slots(P, M_hi, cap_hi, c_lo, K=K_CORTE,
                 par_antipodal=None):
    """EL MOTOR DEL LEMA: certifica la corona {P explicitas} U A
    para TODO multiconjunto A de piezas <= cap_hi con masa <= M_hi
    en capacidad >= c_lo.  VARIANTES por el numero g de piezas
    grandes (> t = c_lo/K): g in 0..n_g con n_g = floor(M_hi/t)
    <= K - 1; la variante g lleva g slots al techo cap y bloques
    con la masa restante <= M_hi - g t (cada grande pesa > t).
    TODAS las variantes deben certificar (cada A real tiene un g
    y su variante lo cubre: slots por monotonia, bloques por
    greedy + cuerda de fila).  Por variante, OR de colocaciones
    antipodales: (P0, P1) y, si hay slots, (P0, slot_1) — cada
    una es una suficiencia (el par colocado a pi exacto; el lado
    vacio exige th(par) <= pi - MARG, conservador).
    par_antipodal = (i, j) fija el par de la CELDA si existe
    (p.ej. exencion analitica): entonces solo esa colocacion,
    con th del par REAL (no pi ficticio: la exencion pertenece a
    la celda, no a este motor generico)."""
    if M_hi >= c_lo:
        return False                   # la masa no cabe: fuera
    t = c_lo / K
    n_g = int(M_hi / t) if cap_hi > t else 0
    cap_p = min(cap_hi, t)
    for g in range(n_g + 1):
        M_p = max(0.0, M_hi - g * t)
        # SLOTS ESCALONADOS (la masa liga las grandes): la
        # i-esima pieza mayor cumple r_i <= (M - (g - i) t)/i
        # (las i mayores pesan >= i r_i y las g - i menores
        # > t): cada slot mayora su pieza por posicion y la
        # asignacion ordenada respeta la monotonia
        slots = [min(cap_hi, (M_hi - (g - i) * t) / i)
                 for i in range(1, g + 1)]
        pares = [(0, 1)]
        if g >= 1:
            pares.append((0, len(P)))  # (P0, primer slot)
        if par_antipodal is not None:
            pares = [tuple(par_antipodal)]
        ok_g = False
        for par in pares:
            if _corona_una(P, slots, M_p, cap_p, c_lo, par):
                ok_g = True
                break
        if not ok_g:
            return False
    return True


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] el lema de slots y sus gates")
    import sympy as sp
    ok = True
    ok &= check("[ENUNCIADO] (A1) LA COTA DE CARDINAL, "
                "OPERATIVA (acta H3: «M < c en toda corona» es "
                "FALSO como teorema — M real puede llegar a "
                "~ pi c con muchas piezas diminutas): el lema "
                "opera BAJO EL GATE M_hi < c_lo (corona_slots "
                "rechaza el resto: el regimen M >= c queda FUERA "
                "del lema y DECLARADO); bajo el gate, las piezas "
                "> t = c/K son a lo sumo floor(M_hi/t) <= K - 1 "
                "(aritmetica, correcta)", True)
    # A2: los slots mayoran (monotonia)
    ok &= check("(A2) SLOTS AL TECHO: theta_w crece en las piezas "
                "(r2bmulti A, adversariado): una pieza real "
                "g <= cap en el lugar de un slot de tamano cap "
                "tiene TODOS sus theta <= los del slot; y un "
                "slot FANTASMA (sin pieza real) es un nodo extra "
                "que solo endurece el reparto (anadir nodos "
                "nunca facilita el antipodal/LP): conservador",
                True)
    # A3: la cuerda de fila (el lema de r2bpool, re-gateado aqui)
    z, a, b, c_s = sp.symbols('z a b c', positive=True)
    d2 = sp.diff(sp.asin(z), z, 2)
    fa = a / (c_s - a)
    ok &= check("(A3) LA CUERDA DE FILA: theta(a, b, c) <= "
                "asin(f_a) + asin(f_b) (semi-angulo: sqrt(f_a "
                "f_b) <= (f_a + f_b)/2 por AM-GM y asin convexa "
                f"(asin'' = {sp.simplify(d2)} >= 0) => asin de la "
                "media <= media de asin... la cadena de piezas "
                "<= t suma arco <= sum 2 asin(f_i) <= C(z_t) "
                "sum f_i <= C(z_t) M_p/(c - t) (asin(z)/z "
                "creciente por convexidad + f creciente en la "
                "pieza)", sp.simplify(
                    d2 - z / (1 - z ** 2) ** sp.Rational(3, 2))
                == 0)
    # A4: el greedy-halving
    ok &= check("(A4) GREEDY-HALVING (teorema de espfinal, "
                "adversariado): todo multiconjunto de piezas <= "
                "cap_p se parte en dos mitades con |m1 - m2| <= "
                "cap_p: cada lado recibe masa <= M_p/2 + cap_p/2 "
                "— el peso de lado del motor", True)
    # A5: la reduccion completa
    ok &= check("[ENUNCIADO] (A5) EL LEMA: si la corona reducida "
                "{P} U {cap x n_g} U {B, B} cabe en c_lo, "
                "entonces {P} U A cabe para TODO multiconjunto A "
                "con masa <= M_hi y piezas <= cap_hi — grandes a "
                "slots (A2), pequenas a bloques (A3 + A4), "
                "capacidad real >= c_lo (theta decrece en R).  "
                "Nodos <= |P| + K + 1: cardinal ELIMINADO", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] el motor corona_slots: positivos y negativos")
    ok = True
    # positivo: la banda POCAS-GRANDES de r2bpool (q ~ 1: Y, x1 y
    # el resto ~ x1) que los bloques-fila no certificaban
    Y, x1 = 20.0, 20.0
    SS, s2 = 1.4, 0.5
    M = 2.0 * x1                       # x1 + resto ~ x1
    c = SS + Y + M
    r = corona_slots([Y, 1.0, s2], M, x1, c)
    ok &= check(f"(a) LA BANDA POCAS-GRANDES (Y = x_1 = 20, "
                f"resto ~ x_1, la que tumbo r2bpool): "
                f"corona_slots certifica ({r})", r is True)
    # LOS CONTRAEJEMPLOS DEL ACTA como negativos fijos
    rH1 = corona_slots([74.2, 0.1], 51.0, 25.5, 100.0)
    rH1b = corona_slots([70.426, 1.360], 58.1, 29.046, 100.0)
    rH2 = corona_slots([2.0, 2.0], 0.5, 0.25, 3.9)
    ok &= check(f"(a2) LOS CONTRAEJEMPLOS DEL ACTA (H1: pares "
                f"cruzados; H1b: barrido hostil; H2: par "
                f"imposible bajo la pi-gorra) RECHAZADOS por el "
                f"motor de colocacion: {rH1}, {rH1b}, {rH2}",
                rH1 is False and rH1b is False and rH2 is False)
    # negativo: masa imposible
    r3 = corona_slots([2.0, 1.0], 3.4, 0.9, 3.2)
    ok &= check(f"(b) masa 3.4 >= c = 3.2: rechazado ({r3})",
                r3 is False)
    # negativo: corona GENUINAMENTE infeasible (la version
    # anterior {2, 1, 0.95} + A(0.9) en c = 3.25 resulto
    # FACTIBLE por ciclo simple — el motor viejo la rechazaba
    # por limitacion, no por infeasibilidad; el nuevo con
    # _coloca_ciclo la certifica correctamente): cuatro piezas
    # de 1.5 en c = 3.55 tienen suma ciclica 4 x 1.6416 = 6.57 >
    # 2 pi sin ningun par imposible — infeasible con prueba
    r4 = corona_slots([1.5, 1.5], 3.0, 1.5, 3.55)
    ok &= check(f"(c) {{1.5, 1.5}} + A(masa 3, cap 1.5) en "
                f"c = 3.55 (suma ciclica de 4 x th = 6.57 > "
                f"2 pi, infeasible probado): rechazado ({r4})",
                r4 is False)
    # contraste HOSTIL (acta H5: el control anterior no
    # muestreaba la region peligrosa): P0 dominante ~ 0.55-0.8 c,
    # cap grande 0.15-0.35 c — la region donde el motor viejo
    # certificaba infeasibles a razon ~1/60 —, mas los
    # multiconjuntos adversariales (pocas grandes al cap, g = n_g
    # exacto, piezas justo sobre t)
    import random
    from coronacolas import corona_suf
    rng = random.Random(777)
    n_p, viol = 0, 0
    for _ in range(20000):
        if n_p >= 300:
            break
        c = rng.uniform(10.0, 120.0)
        P0 = rng.uniform(0.55, 0.80) * c
        P1 = rng.uniform(0.05, 2.0)
        cap = rng.uniform(0.15, 0.35) * c
        M = rng.uniform(cap, min(0.95 * c, 3.0 * cap))
        if not corona_slots([P0, P1], M, cap, c):
            continue
        n_p += 1
        # multiconjuntos adversariales concretos bajo (M, cap)
        for xs in ([cap, cap] if 2 * cap <= M else [cap],
                   [cap] + [min(cap, M - cap)]
                   if M > cap else [M],
                   [M / 3.0] * 3):
            xs = [x for x in xs if x > 1e-9]
            if not xs or sum(xs) > M + 1e-9                     or max(xs) > cap + 1e-9:
                continue
            piezas = sorted([P0, P1] + xs, reverse=True)
            if not corona_suf(piezas, c + 1e-9)[0]:
                viol += 1
    ok &= check(f"(d) contraste HOSTIL (region del acta: P0 "
                f"dominante, cap grande): {n_p} coronas "
                f"certificadas x multiconjuntos adversariales; "
                f"violaciones {viol}", n_p >= 100 and viol == 0)
    return ok


# ---------------------------------------------------------------- bloque C
def _corona_slots_capY(s2_p, SSl, M_lo, M_hi, cap_hi, c_lo,
                       Y_hi=None):
    """corona_slots especializada para {Y, m, sigma2} U A de
    G-b' con LA FILA Y POR CAPS DE LIMITE (r2bcolas A1) — FASE
    1-BIS: decidida por el MOTOR DE COLOCACION (_motor_dos_lados;
    el acta de la re-ronda cazo que esta funcion seguia llamando
    a _antipodal2, el motor refutado — 5 cajas del B&B carecian
    de respaldo).  Dos colocaciones OR: par (Y, m) y par
    (Y, slot_1) con la exencion EN-CELDA (pr(Y, x1) < 1 estricto:
    x1 <= M y x1 <= Y — verificado en la primera acta)."""
    K = K_CORTE
    if M_hi >= c_lo:
        return False
    t = c_lo / K
    n_g = int(M_hi / t) if cap_hi > t else 0
    cap_p0 = min(cap_hi, t)

    def fila_Y(a):
        capL = _asin2(math.sqrt(min(1.0, a / (SSl + M_lo))))
        if Y_hi is not None:
            capL = min(capL, th(min(Y_hi, 1e8),
                                min(a, 1e8), c_lo))
        return capL

    for g in range(n_g + 1):
        M_p = max(0.0, M_hi - g * t)
        slots_g = [min(cap_hi, (M_hi - (g - i) * t) / i)
                   for i in range(1, g + 1)]
        cap_p = min(cap_p0, max(M_p, 1e-9))
        peso = _cuerda(cap_p, c_lo) * (M_p / 2.0 + cap_p / 2.0)

        def _prueba(orden_base, exento):
            # orden_base: nodos no-bloque con el par en (0, 1);
            # la fila del nodo Y (identificado como 1e9) va por
            # caps de limite
            nodos = list(orden_base) + [cap_p, cap_p]
            nb0 = len(orden_base)
            n = len(nodos)
            thmat = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if nodos[i] >= 1e8 or nodos[j] >= 1e8:
                        otro = nodos[j] if nodos[i] >= 1e8                             else nodos[i]
                        thmat[i][j] = fila_Y(otro)
                    else:
                        thmat[i][j] = th(nodos[i], nodos[j],
                                         c_lo)
                    thmat[j][i] = thmat[i][j]
            Ds = {nb0: peso, nb0 + 1: peso}
            return _motor_dos_lados(nodos, thmat, Ds,
                                    exento=exento)

        base1 = [1e9, 1.0, s2_p] + slots_g
        ok_g = _prueba(base1, None)
        if not ok_g and g >= 1:
            base2 = [1e9, slots_g[0], 1.0, s2_p] + slots_g[1:]
            ok_g = _prueba(base2, (0, 1))
        if not ok_g:
            return False
    return True


def bloque_C():
    print("[C] APLICACION 1: j >= 4 en G-b' (el hueco de "
          "r2bpool) — fila Y por caps, todo Y de golpe")
    ok = True
    V_T = math.log(64.0)
    Y1C = 6.6

    def crit_slots_Yc(box):
        """Regimen Y in [1, Y1C]: caja (s2, SS, uY, uM) compacta
        con la fila Y refinada por th(Y_hi)."""
        s2l, s2h, SSl, SSh, uyl, uyh, uml, umh = box
        if SSh <= 1.0 or SSl > PHI:
            return None
        if SSl >= 1.0 + s2h:
            return None
        if 2.0 * s2l > SSh:
            return None
        s2_p = min(s2h, SSh / 2.0)
        Y_lo, Y_hi = math.exp(uyl), math.exp(uyh)
        M_lo, M_hi = math.exp(uml), math.exp(umh)
        cap = min(M_hi, Y_hi)          # x <= Y
        c_lo = max(SSl, 1.0) + Y_lo + M_lo
        return _corona_slots_capY(s2_p, max(SSl, 1.0), M_lo,
                                  M_hi, cap, c_lo, Y_hi=Y_hi)

    root_c = [0.0, 1.0, 1.0, 2.0, 0.0, math.log(Y1C),
              math.log(0.05), math.log(2.0 * Y1C)]
    exito2, caja2, n2, cert2 = bnb_factible(root_c, crit_slots_Yc,
                                            eps=2e-3)
    ok &= check(f"(a) G-b' con Y in [1, {Y1C}] y cardinal libre "
                f"EN EL DOMINIO DECLARADO M in [0.05, 13.2] "
                f"(acta H4: AMBOS topes son de barrido, no "
                f"paredes — M no esta acotada por el modelo; el "
                f"claim COMPLEMENTA r2bmulti, que cubria j <= 3 "
                f"con M <= 3Y <= 19.8, sin contenerlo): {n2} "
                f"cajas, {cert2} certificadas"
                + ("" if exito2 else f"; SIN RESOLVER {caja2}"),
                exito2)
    ok &= check("[ENUNCIADO] (b) FASE 2 DECLARADA: Y > 6.6 con "
                "cardinal libre exige el producto de los "
                "regimenes homogeneos de r2bcolas (el acople "
                "x <= Y con ambos libres) con los slots — el "
                "regimen (a1) cap <= 6.6 y (a2) cap > 6.6 "
                "normalizado por Y; el intento con fila-limite "
                "plana dejo cajas M ~ 60 sin resolver "
                "(documentado).  r2bcolas cubre alli j <= 3; "
                "j >= 4 con Y > 6.6 queda declarado", True)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] APLICACION 2 (k >= 2): estado declarado")
    return check(
        "[ENUNCIADO] k >= 2 anillos extra del canal: el boceto "
        "con slots (par (z, extras) y masa de extras) dejo 0 "
        "certificadas — los dominios del criterio no estan "
        "cotejados con la celda real de espcanal (ventanas de "
        "z, cola de Y con los extras, techos por pieza) y el "
        "cap del slot roza el techo del nodo saturando contra "
        "z.  QUEDA DECLARADO PARA LA FASE 2 con el mismo "
        "producto regimenes x slots; la celda sigue declarada "
        "en espcanal E (la pinza de colas la acota pero no la "
        "cierra)", True)


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    return check(
        "[ENUNCIADO] FASE 1-BIS DEL LEMA DE |A|: el LEMA DE "
        "SLOTS (grandes <= K - 1 bajo el gate operativo M < c, "
        "slots ESCALONADOS r_i <= (M - (g - i) t)/i por "
        "monotonia, pequenas por greedy-halving + cuerda de "
        "fila) elimina el cardinal con nodos fijos; el motor es "
        "LA SUFICIENCIA CONSTRUCTIVA COMPLETA (_coloca_y_"
        "verifica: todos los pares mirados, cruzados incluidos, "
        "con gate de pares factibles — los contraejemplos de "
        "las dos actas son negativos fijos) y el control B(d) "
        "muestrea la region hostil.  APLICACION CERTIFICADA: "
        "G-b' con cardinal libre en Y in [1, 6.6], dominio "
        "declarado M in [0.05, 13.2] (COMPLEMENTA r2bmulti, sin "
        "contenerlo), decidida por el motor nuevo.  FASE 2 "
        "(declarada): Y > 6.6, k >= 2, M fuera de [0.05, 13.2] "
        "— el producto regimenes homogeneos x slots; G-e/G-g "
        "pesadas como destino final del lema", True)


def main():
    print("=" * 68)
    print("EL LEMA DE REDUCCION DE |A| (slots + cuerda de fila)")
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
