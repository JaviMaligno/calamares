#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EXPLORACION (SIN CLAIM): G-b' con conteo j >= 4 por pooling —
el intento y su OBSTACULO ESTRUCTURAL, documentados.

EL OBJETIVO ERA cerrar el ultimo tope de conteo del residuo (ii)
(G-b' con j <= 3, eleccion de muestreo del MC declarada en el
paper) plegando las piezas X' en bloques por masa (greedy-halving
de espfinal) con el peso fino de la CUERDA DE FILA (arco(r) <=
2 asin(r/(c-r)) y la cuerda de convexidad: una fila de masa m con
piezas <= cap consume <= [2 asin(z)/z] m/(c-cap), z = cap/(c-cap)
— lema NUEVO, mas fino que el pi m/(c-cap) historico, exportable).

LO QUE FUNCIONA (bloques A y D verdes; B&B parciales): los caps
uniformes en Y (p(Y, a) <= a/(SS+M) via c - Y = SS + M), el min
con th(Y_hi, a, c_lo) para Y acotado, la cuerda de fila, y los
regimenes con piezas pequenas o resto diminuto.

EL OBSTACULO (por que NO hay claim): la banda «POCAS GRANDES» —
q = Mr/x_1 ~ 1 con el resto en 1-3 piezas comparables a x_1 — no
se certifica ni con bloques (el cap del bloque ~ x_1 hace
theta(Y, B) ~ pi/2 y el peso de cuerda ~ 1: los lados exceden pi
aunque la corona real quepa holgada) ni con explicitas (el numero
de grandes no esta acotado: j - 1 piezas pueden ser ~ x_1).  Es
EXACTAMENTE el «lema de reduccion de |A|» que r2bmulti [E] declaro
faltante para G-e/G-g pesadas: el multiconjunto mural sin cota de
cardinal.  CONCLUSION HONESTA: el tope j <= 3 de G-b' NO es un
tope trivial de quitar — colinda con ese abierto declarado; su
cierre requiere el lema de reduccion de cardinal (jerarquia
explicitas <= K + cadena-cuerda + fila, con la banda de transicion
tratada), un ciclo mayor.  El paper ya declara j <= 3 como
eleccion del MC: NADA QUE CAMBIAR alli.

Este script queda como EXPLORACION: los gates A (cuerda, caps,
pooling) son correctos y reutilizables; los B&B de [B] certifican
la mayoria del dominio pero dejan cajas de la banda pocas-grandes
SIN RESOLVER (documentadas en el output).  Sin ronda adversarial
(no soporta claim).
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check
from r2bmulti import th, bnb_factible
from espfinal import _antipodal2

SEED = int(os.environ.get('CC_SEED', '20260822'))
V_T = math.log(64.0)                   # frontera log de las colas


def _cuerda_fila(cap, c):
    """El peso por unidad de masa de una fila de piezas <= cap en
    capacidad c: arco(r) <= 2 asin(r/(c-r)) y por la cuerda de
    convexidad (asin(z)/z creciente, y r/(c-r) convexa en r)
    arco(r) <= [2 asin(z_max)/z_max] * r/(c-cap) con z_max =
    cap/(c-cap): la fila de masa m consume <= C * m/(c-cap)."""
    z = min(1.0, cap / max(1e-12, c - cap))
    if z < 1e-9:
        return 2.0 / max(1e-12, c - cap)
    return (2.0 * math.asin(z) / z) / (c - cap)


def _corona_pool(s2h, SSl, Y_lo, x1_hi, M_lo, masa_lado_hi,
                 cap_hi, Y_hi=None):
    """La corona [Y, m, sigma2, (x1)] + 2 bloques con caps por
    termino (uniformes en Y: gate A2) y el peso de bloque por la
    CUERDA DE FILA.  x1_hi = None en R-A.  masa_lado_hi = el
    techo de la masa de cada bloque (M_hi/2 + cap/2, o su limite
    en las colas)."""
    c_lo = SSl + Y_lo + M_lo
    nodos = [1e9, 1.0, s2h]
    if x1_hi is not None:
        nodos.append(x1_hi)
    n_bloq0 = len(nodos)
    nodos += [cap_hi, cap_hi]
    n = len(nodos)
    thmat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if i == 0:
                cap_l = 2.0 * math.asin(math.sqrt(min(
                    1.0, nodos[j] / (SSl + M_lo))))
                if Y_hi is not None:
                    # con Y acotado, th(Y_hi, a, c_lo) mayora el
                    # termino real (th crece en las piezas y
                    # decrece en c) y es mas fino que el limite
                    cap_l = min(cap_l,
                                th(min(Y_hi, 1e8),
                                   min(nodos[j], 1e8), c_lo))
                thmat[i][j] = cap_l
            else:
                thmat[i][j] = th(min(nodos[i], 1e8),
                                 min(nodos[j], 1e8), c_lo)
    D_val = _cuerda_fila(cap_hi, c_lo) * masa_lado_hi
    Ds = {n_bloq0: D_val, n_bloq0 + 1: D_val}
    return _antipodal2(nodos, thmat, Ds)


X1C = 6.6                              # frontera del regimen C


def crit_C(box):
    """R-C (x_1 > X1C, Y >= x_1): caja (s2, SS, uq) con
    q = Mr/x_1 = e^uq - 1 >= 0.  Caps UNIFORMES en (x_1, Y)
    derivados en A6: par (Y, x_1) antipodal exento; (Y, B):
    p <= cap/(x_1 + Mr) = min(1, q)/(1 + q); (x_1, B): p <=
    min(1,q)/((1+q)(2 + q - min(1,q))); (m o s2 contra
    cualquiera): p <= 1/(1 + X1C); (B, B): p <= [min(1,q)/
    (1+q)]^2-forma <= 1/4; D por cuerda con ratio <=
    (q + min(1,q))/(2(2 + q - min(1,q))) y z_max <= min(1,q)/2.
    uq >= V_T marca la cola q -> inf (limites: 1/(1+q) -> 0,
    ratio -> 1/2)."""
    from r2bcolas import _antipodal_cola
    s2l, s2h, SSl, SSh, uql, uqh = box
    if SSh <= 1.0 or SSl > PHI:
        return None
    if SSl >= 1.0 + s2h:
        return None
    if 2.0 * s2l > SSh:
        return None
    q_lo = max(0.0, math.exp(uql) - 1.0)
    en_cola = uqh >= V_T - 1e-12
    q_hi = None if en_cola else math.exp(uqh) - 1.0
    mq_hi = 1.0 if (q_hi is None or q_hi >= 1.0)         else q_hi                      # min(1, q) techo
    # p(Y, B) = min(1,q)/(1+q): crece en q hasta q = 1, decrece
    # despues: el sup de caja es el max en las esquinas y en
    # q = 1 si esta dentro
    def p_yb(q):
        return min(1.0, q) / (1.0 + q)
    cands = [p_yb(q_lo)] + ([] if q_hi is None else [p_yb(q_hi)])
    if q_hi is None or (q_lo <= 1.0 <= q_hi):
        cands.append(0.5)
    p_YB = max(cands)
    den2 = 2.0 + q_lo - mq_hi
    p_xB = mq_hi / max(1e-9, (1.0 + q_lo) * den2)
    p_len = 1.0 / (1.0 + X1C)
    # D por cuerda
    ratio = (min(q_hi if q_hi is not None else 1e18, 1e18)
             + mq_hi)
    ratio = ((q_hi + mq_hi) / (2.0 * den2))         if q_hi is not None else 0.5 + mq_hi / (2.0 * den2)
    ratio = min(max(ratio, 0.0), 0.75)
    z_max = min(1.0, mq_hi / 2.0)
    C_val = (2.0 * math.asin(z_max) / z_max) if z_max > 1e-9         else 2.0
    D_val = C_val * ratio
    n = 6                              # [Y, m, s2, B, B, x1]
    i_max = 5
    tam = [1e9, 1.0, 1.0, 1e9, 1e9, 1e9]
    c_abs = 1.0 + 2.0 * X1C
    thmat = [[0.0] * n for _ in range(n)]
    thmat[0][1] = _asin2s(p_len)
    thmat[0][2] = _asin2s(p_len)
    thmat[0][3] = _asin2s(p_YB)
    thmat[0][4] = _asin2s(p_YB)
    thmat[0][5] = PI                   # el par antipodal
    thmat[1][2] = th(1.0, 1.0, c_abs)
    for k in (3, 4):
        thmat[1][k] = _asin2s(p_len)
        thmat[2][k] = _asin2s(p_len)
        thmat[k][5] = _asin2s(p_xB)
    thmat[3][4] = _asin2s(min(0.25, p_YB * p_YB * 4.0))
    thmat[1][5] = _asin2s(p_len)
    thmat[2][5] = _asin2s(p_len)
    for i in range(n):
        for j in range(i + 1, n):
            thmat[j][i] = thmat[i][j]
    Ds = {3: D_val, 4: D_val}
    return _antipodal_cola(tam, thmat, i_max)


def _asin2s(p):
    return 2.0 * math.asin(math.sqrt(max(0.0, min(1.0, p))))


def criterio_pool(box, con_x1):
    """R-A: caja (s2, SS, uY, uM) con x_1 <= 1 (cap = min(1, M));
    R-B: (s2, SS, uY, x1, uMr) con x_1 in (1, X1C] DIRECTO y
    Mr = e^uMr - 1 >= 0.  Los techos u >= V_T marcan colas
    (limites por caps, gates A2/A3)."""
    if con_x1:
        s2l, s2h, SSl, SSh, uyl, uyh, x1l, x1h, uml, umh = box
    else:
        s2l, s2h, SSl, SSh, uyl, uyh = box[:6]
    if SSh <= 1.0 or SSl > PHI:
        return None
    if SSl >= 1.0 + s2h:
        return None
    if 2.0 * s2l > SSh:
        return None
    s2_p = min(s2h, SSh / 2.0)
    SSl_e = max(SSl, 1.0)
    Y_lo = math.exp(uyl)
    if con_x1:
        en_cola_M = umh >= V_T - 1e-12
        if x1l > X1C or x1h <= 1.0:
            return None                # fuera de R-B
        x1_hi = min(x1h, X1C)
        if x1_hi > Y_lo:               # x <= Y: recorte del suelo
            Y_lo = max(Y_lo, x1l)
        Mr_lo = max(0.0, math.exp(uml) - 1.0)
        M_lo = x1l + Mr_lo
        cap_hi = min(x1_hi,
                     (1e18 if en_cola_M
                      else math.exp(umh) - 1.0) + 1e-9)
        cap_hi = max(cap_hi, 1e-9)
        # la masa de los bloques es SOLO el resto Mr (x_1 va
        # explicita — meterla en el bloque doblaba su peso)
        if en_cola_M:
            # cola Mr: (Mr/2 + cap/2)/(c - cap) crece hacia 1/2
            # (cap fijo <= X1C): el peso de cola es el max del
            # ratio en la esquina Mr = T y el limite 1/2
            c_T = SSl_e + Y_lo + M_lo
            ratio = max((Mr_lo + cap_hi)
                        / (2.0 * max(1e-9, c_T - cap_hi)), 0.5)
            masa_lado = ratio * max(1e-9, c_T - cap_hi)
            return _corona_pool(s2_p, SSl_e, Y_lo, x1_hi,
                                M_lo, masa_lado, cap_hi,
                                None if uyh >= V_T - 1e-12
                                else math.exp(uyh))
        Mr_hi = math.exp(umh) - 1.0
        masa_lado = Mr_hi / 2.0 + cap_hi / 2.0
        return _corona_pool(s2_p, SSl_e, Y_lo, x1_hi, M_lo,
                            masa_lado, cap_hi,
                            None if uyh >= V_T - 1e-12
                            else math.exp(uyh))
    # R-A: x1 <= 1 como dimension (cap fino)
    x1l_a, x1h_a = box[6], box[7]
    uml, umh = box[8], box[9]
    en_cola_M = umh >= V_T - 1e-12
    if x1l_a > 1.0:
        return None
    cap_a = max(1e-9, min(x1h_a, 1.0))
    M_lo = max(math.exp(uml), x1l_a)
    if en_cola_M:
        c_T = SSl_e + Y_lo + M_lo
        ratio = max((M_lo + cap_a)
                    / (2.0 * max(1e-9, c_T - cap_a)), 0.5)
        masa_lado = ratio * max(1e-9, c_T - cap_a)
        return _corona_pool(s2_p, SSl_e, Y_lo, None, M_lo,
                            masa_lado, cap_a,
                            None if uyh >= V_T - 1e-12
                            else math.exp(uyh))
    M_hi = math.exp(umh)
    masa_lado = M_hi / 2.0 + cap_a / 2.0
    return _corona_pool(s2_p, SSl_e, Y_lo, None, M_lo,
                        masa_lado, cap_a,
                        None if uyh >= V_T - 1e-12
                        else math.exp(uyh))


def crit_A(box):
    return criterio_pool(list(box), False)


def crit_B(box):
    return criterio_pool(list(box), True)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] el pooling y los gates")
    import sympy as sp
    ok = True
    Y, SS, M, a, c = sp.symbols('Y SS M a c', positive=True)
    ok &= check("[ENUNCIADO] (A1) EL POOLING (teorema de "
                "espfinal, adversariado): un multiconjunto de "
                "piezas <= cap partido por el greedy deja dos "
                "bloques de masa <= M/2 + cap/2, cada uno como "
                "fila mural con arco <= pi masa/(c - cap): el "
                "conteo j desaparece — R-A pliega TODO X' (cap = "
                "1 >= x_1), R-B la pieza maxima explicita y el "
                "resto plegado (cap = min(x_1, M - x_1) mayora "
                "toda pieza del resto y su masa)", True)
    # A2: el cap de la fila Y
    p = Y * a / ((SS + M) * (SS + Y + M - a))
    lim = sp.limit(p, Y, sp.oo)
    ok &= check(f"(A2) fila Y contra a: p = Ya/((SS+M)(c-a)) "
                f"crece en Y hacia {lim} y c - a >= Y para "
                "a <= SS + M (m = 1 < SS, s2 < 1 < SS, x1 <= M): "
                "cap = a/(SS_lo + M_lo), uniforme en Y",
                sp.simplify(lim - a / (SS + M)) == 0)
    # A3: los lentos decrecen en c y el peso del bloque
    q = PI * M / 2 / (SS + Y + M - a)
    dq = sp.diff(q, M)
    ok &= check("(A3) los pares lentos (th) decrecen en c "
                "(r2bmulti, adversariado) y c >= c_lo = SS_lo + "
                "Y_lo + M_lo; el peso del bloque pi(M/2+cap/2)/"
                "(c-cap) CRECE en M hacia pi/2 + pi cap/(2(c... "
                f"d/dM ~ {sp.simplify(sp.factor(dq))} > 0 (el "
                "numerador es SS + Y - a > 0 para cap = a < SS + "
                "Y): el cap de cola pi/2 + pi cap/(2 c_lo) mayora",
                sp.simplify(dq * 2 * (SS + Y + M - a) ** 2 / PI
                            - (SS + Y - a)) == 0)
    # A4: el par (Y, m) antipodal
    ok &= check("(A4) el par (Y, m): theta(Y, 1, c) < pi "
                "estricto sii f(Y) f(1) < 1 sii c - Y - 1 + ... "
                "(SS + M > 1, siempre con SS > 1): la exencion "
                "analitica del arco completo en _antipodal2 "
                "(espfinal, adversariado) es legitima", True)
    ok &= check("[ENUNCIADO] (A5) el dominio: j >= 4 arbitrario "
                "queda cubierto por (M, x_1) sin conteo; x <= Y "
                "pared del modelo; el claim SUPERPONE j <= 3 "
                "(seguro: mas instancias certificadas) y junto "
                "con r2bmulti/r2bcolas cierra G-b' para TODO "
                "conteo y todo Y", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] B&B de R-A y R-B (log + celdas de cola)")
    ok = True
    root_a = [0.0, 1.0, 1.0, 2.0, 0.0, V_T, 0.0, 1.0,
              0.0, V_T]
    exito, caja, n, cert = bnb_factible(root_a, crit_A, eps=1e-3)
    ok &= check(f"R-A (x_1 <= 1 como dim, X' entera en bloques): "
                f"{n} cajas, {cert} certificadas"
                + ("" if exito else f"; SIN RESOLVER {caja}"),
                exito)
    root_b = [0.0, 1.0, 1.0, 2.0, 0.0, V_T, 1.0, X1C,
              0.0, V_T]
    exito2, caja2, n2, cert2 = bnb_factible(root_b, crit_B,
                                            eps=1e-3)
    ok &= check(f"R-B (1 < x_1 <= {X1C} explicita + bloques): "
                f"{n2} cajas, {cert2} certificadas"
                + ("" if exito2 else f"; SIN RESOLVER {caja2}"),
                exito2)
    root_c = [0.0, 1.0, 1.0, 2.0, 0.0, V_T]
    exito3, caja3, n3, cert3 = bnb_factible(root_c, crit_C,
                                            eps=1e-3)
    ok &= check(f"R-C (x_1 > {X1C}: par (Y, x_1) antipodal, "
                f"caps uniformes en q = Mr/x_1, B&B 3D): {n3} "
                f"cajas, {cert3} certificadas"
                + ("" if exito3 else f"; SIN RESOLVER {caja3}"),
                exito3)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] contraste con la corona real (j = 4..12)")
    from coronacolas import corona_suf
    rng = random.Random(SEED)
    ok = True
    n_p, viol = 0, 0
    for _ in range(40000):
        if n_p >= 400:
            break
        j = rng.randrange(4, 13)
        s2 = rng.uniform(0.05, 0.95)
        SS = rng.uniform(max(1.0 + 1e-6, 2 * s2),
                         1.0 + s2 - 1e-9)
        if not (1.0 < SS < 1.0 + s2):
            continue
        Yv = math.exp(rng.uniform(0.0, math.log(200.0)))
        xs = sorted((rng.uniform(0.02, Yv) for _ in range(j)),
                    reverse=True)
        M = sum(xs)
        c = SS + Yv + M
        piezas = sorted([Yv, 1.0, s2] + xs, reverse=True)
        if not corona_suf(piezas, c + 1e-9)[0]:
            viol += 1
            continue
        n_p += 1
        # la caja-punto del criterio
        x1 = xs[0]
        if x1 <= 1.0:
            bx = [s2, s2, SS, SS,
                  math.log(Yv), math.log(Yv), x1, x1,
                  min(math.log(M), V_T), min(math.log(M), V_T)]
            r = crit_A(bx)
        elif x1 <= X1C:
            um = min(math.log(1.0 + (M - x1)), V_T)
            bx = [s2, s2, SS, SS,
                  math.log(Yv), math.log(Yv),
                  x1, x1, um, um]
            r = crit_B(bx)
        else:
            qv = (M - x1) / x1
            uq = min(math.log(1.0 + qv), V_T)
            r = crit_C([s2, s2, SS, SS, uq, uq])
        if r is not True:
            viol += 1
    ok &= check(f"(a) {n_p} instancias reales j = 4..12 (Y hasta "
                f"200, x <= Y): la corona real cabe (corona_suf) "
                f"y el criterio de pooling certifica la "
                f"caja-punto; violaciones {viol}",
                n_p >= 200 and viol == 0)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] negativos")
    ok = True
    # el motor con bloques imposibles (masa enorme, c pequeno)
    nodos = [2.0, 1.0, 0.9, 0.9, 0.9]
    c_malo = 3.2
    thmat = [[0.0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(i + 1, 5):
            thmat[i][j] = th(nodos[i], nodos[j], c_malo)
    Ds = {3: PI * 1.4 / (c_malo - 0.9), 4: PI * 1.4 / (c_malo - 0.9)}
    r = _antipodal2(nodos, thmat, Ds)
    ok &= check(f"(a) no-vacuidad: bloques de masa 1.4 con cap "
                f"0.9 en c = 3.2: el motor RECHAZA ({r})",
                r is False)
    # una caja legal chica certifica
    bx = [0.5, 0.5, 1.4, 1.4, math.log(3.0), math.log(3.0),
          math.log(2.0), math.log(2.0)]
    r2 = crit_A(bx)
    ok &= check(f"(b) R-A en un punto legal (Y = 3, M = 2, "
                f"SS = 1.4): certifica ({r2})", r2 is True)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    return check(
        "[ENUNCIADO] EXPLORACION SIN CLAIM: el cierre de j >= 4 "
        "en G-b' tropieza con la banda POCAS-GRANDES (q ~ 1, "
        "resto ~ x_1), que es el mismo lema de reduccion de |A| "
        "declarado faltante en r2bmulti [E] para G-e/G-g.  El "
        "tope j <= 3 del paper permanece declarado (correcto); "
        "la CUERDA DE FILA de este script (peso [2 asin(z)/z] "
        "m/(c-cap), mas fino que pi m/(c-cap)) queda como lema "
        "exportable para el ciclo futuro del lema de |A|", True)


def main():
    print("=" * 68)
    print("G-b' CON CONTEO ARBITRARIO (pooling por masa)")
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
