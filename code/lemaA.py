#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BORRADOR REFUTADO-EN-REPARACION (SIN CLAIM): la fase 1 del
lema de reduccion de |A| fue REFUTADA en su ronda adversarial
(acta en VEREDICTOS, 2026-08-23) — NO usar corona_slots como
certificado.

EL VEREDICTO: el motor certifica coronas infeasibles.
Contraejemplo: corona_slots(P=[74.2, 0.1], M=51, cap=25.5, c=100)
= True con el A legal {25.5, 25.5} INFEASIBLE (prueba exacta de
ventana; LP de arcos infactible en todos los ordenes).  CAUSA:
_antipodal2 verifica caminos por lado y cubre los pares CRUZADOS
solo bajo la precondicion implicita «los polos mayoran en f a los
intermedios» — cierta en todos los usos historicos (polvo < m,
auditados) y VIOLADA por los slots (grandes con polo m = 1).
Segundo agujero: la pi-gorra tapa pares de P imposibles (falta el
gate f f < 1).  Tercero: el enunciado A1 (M < c) es falso como
teorema (M real hasta ~ pi c); el gate es conservador pero el
regimen M >= c queda fuera sin declarar.  Cuarto: los topes
M in [0.05, 13.2] de la aplicacion C(a) eran topes de barrido con
justificacion espuria.

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


def _corona_una(P, slots, M_p, cap_p, c_lo, par):
    """Una variante concreta: P + slots + 2 bloques(masa M_p) con
    la colocacion antipodal del par de indices `par` de los nodos
    no-bloque.  El RADIO del nodo-bloque es min(cap_p, M_p):
    ninguna pieza del bloque excede su masa (un bloque de masa
    diminuta no puede pesar como una pieza de radio cap)."""
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
    return _antipodal2(nodos, thmat, Ds)


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
    ok &= check("[ENUNCIADO] (A1) LA COTA UNIVERSAL DE CARDINAL: "
                "en una corona de capacidad c, la masa mural M "
                "cabe dentro del contenedor: M < c SIEMPRE "
                "(cada pieza r consume cuerda >= 2r sen(theta/2) "
                "> 0 del perimetro y la suma de radios de "
                "piezas interiores-disjuntas de un disco de "
                "radio c es < c... la forma usada: las piezas de "
                "una corona mural son disjuntas dentro del disco "
                "de radio c, luego la suma de sus radios a lo "
                "largo de un diametro es < c; el gate operativo: "
                "corona_slots RECHAZA M >= c).  Con el corte "
                "t = c/K: las piezas > t son a lo sumo "
                "floor(M/t) <= K - 1", True)
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
    # negativo: masa imposible
    r3 = corona_slots([2.0, 1.0], 3.4, 0.9, 3.2)
    ok &= check(f"(b) masa 3.4 >= c = 3.2: rechazado ({r3})",
                r3 is False)
    # negativo: corona apretada real
    r4 = corona_slots([2.0, 1.0, 0.95], 0.9, 0.9, 3.25)
    ok &= check(f"(c) {{2, 1, 0.95}} + A(masa 0.9, cap 0.9) en "
                f"c = 3.25 (el par 2+1 llena el diametro): "
                f"rechazado ({r4})", r4 is False)
    # contraste: slots vs corona real en instancias aleatorias
    import random
    from coronacolas import corona_suf
    rng = random.Random(SEED)
    n_p, viol = 0, 0
    for _ in range(4000):
        if n_p >= 300:
            break
        nP = rng.randrange(2, 4)
        P = sorted((rng.uniform(0.5, 3.0) for _ in range(nP)),
                   reverse=True)
        j = rng.randrange(1, 9)
        cap = rng.uniform(0.1, 2.0)
        xs = [rng.uniform(0.05, cap) for _ in range(j)]
        M = sum(xs)
        c = sum(P) + M + rng.uniform(1.0, 4.0)
        if not corona_slots(P, M, cap, c):
            continue                   # el lema no certifica esta
        n_p += 1
        piezas = sorted(P + xs, reverse=True)
        if not corona_suf(piezas, c + 1e-9)[0]:
            viol += 1
    ok &= check(f"(d) {n_p} coronas certificadas por el lema: la "
                f"corona real (corona_suf, con el A concreto) "
                f"cabe en TODAS (violaciones {viol}) — el lema "
                f"nunca certifica de mas", n_p >= 150 and viol == 0)
    return ok


# ---------------------------------------------------------------- bloque C
def _corona_slots_capY(s2_p, SSl, M_lo, M_hi, cap_hi, c_lo,
                       Y_hi=None):
    """corona_slots especializada para la corona {Y, m, sigma2} U
    A de G-b' con LA FILA Y POR CAPS DE LIMITE (r2bcolas A1: el
    producto contra Y crece en Y hacia a/(SS + M)): uniforme en Y
    — cubre la cola Y de golpe.  Y_hi (si finito) refina con
    th(Y_hi, a, c_lo)."""
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
        # SLOTS ESCALONADOS: la i-esima pieza mayor cumple
        # r_i <= (M - (g - i) t)/i (las i mayores pesan >= i r_i
        # y las g - i menores > t): cada slot mayora su pieza
        # por posicion (asignacion ordenada, monotonia)
        slots_g = [min(cap_hi, (M_hi - (g - i) * t) / i)
                   for i in range(1, g + 1)]
        cap_p = min(cap_p0, max(M_p, 1e-9))
        peso = _cuerda(cap_p, c_lo) * (M_p / 2.0 + cap_p / 2.0)
        # nodos: [Y(virtual), m, s2] + slots + [B, B]
        resto = [1.0, s2_p] + slots_g + [cap_p, cap_p]
        nb0 = 1 + len(resto) - 2
        nodos = [1e9] + resto
        n = len(nodos)
        thmat = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if i == 0:
                    thmat[i][j] = fila_Y(nodos[j])
                else:
                    thmat[i][j] = th(min(nodos[i], 1e8),
                                     min(nodos[j], 1e8), c_lo)
                thmat[j][i] = thmat[i][j]
        Ds = {nb0: peso, nb0 + 1: peso}
        if _antipodal2(nodos, thmat, Ds):
            continue
        if g >= 1:
            # colocacion alternativa: el par (Y, slot_1)
            # ANTIPODAL con exencion de tangencia (el requisito
            # th(Y, slot) <= pi siempre por el clamp y la
            # separacion colocada es pi exacto: legal no
            # estricto — el estandar adversariado de
            # espomegacola/r2bcolas); nodos reordenados para que
            # el par sea (0, 1) del motor y thmat[0][1] = 0
            nodos2 = [1e9, slots_g[0], 1.0, s2_p] \
                + slots_g[1:] + [cap_p, cap_p]
            n2 = len(nodos2)
            nb2 = n2 - 2
            th2 = [[0.0] * n2 for _ in range(n2)]
            for i in range(n2):
                for j in range(i + 1, n2):
                    if i == 0 and j == 1:
                        th2[i][j] = 0.0
                    elif i == 0:
                        th2[i][j] = fila_Y(nodos2[j])
                    else:
                        th2[i][j] = th(min(nodos2[i], 1e8),
                                       min(nodos2[j], 1e8),
                                       c_lo)
                    th2[j][i] = th2[i][j]
            Ds2 = {nb2: peso, nb2 + 1: peso}
            if _antipodal2(nodos2, th2, Ds2):
                continue
        return False
    return True


def bloque_C():
    print("[C] APLICACION 1: j >= 4 en G-b' (el hueco de "
          "r2bpool) — fila Y por caps, todo Y de golpe")
    ok = True
    V_T = math.log(64.0)
    Y1C = 6.6

    def crit_slots_YG(box):
        """Regimen Y >= Y1C: caja (s2, SS, uM); la fila Y por
        limites (uniforme en Y, cola Y incluida)."""
        s2l, s2h, SSl, SSh, uml, umh = box
        if SSh <= 1.0 or SSl > PHI:
            return None
        if SSl >= 1.0 + s2h:
            return None
        if 2.0 * s2l > SSh:
            return None
        s2_p = min(s2h, SSh / 2.0)
        M_lo, M_hi = math.exp(uml), math.exp(umh)
        cap = M_hi                     # x <= Y: cap <= min(M, Y)
        c_lo = max(SSl, 1.0) + Y1C + M_lo
        return _corona_slots_capY(s2_p, max(SSl, 1.0), M_lo,
                                  M_hi, cap, c_lo)

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
    ok &= check(f"(a) G-b' con Y in [1, {Y1C}] y CARDINAL LIBRE "
                f"(M <= 2 Y1C: x <= Y y M < c): {n2} cajas, "
                f"{cert2} certificadas — EXTIENDE r2bmulti (que "
                f"certificaba j <= 3) a todo j en su rango de Y"
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
        "[ENUNCIADO] FASE 1 DEL LEMA DE |A| CERRADA: el LEMA DE "
        "SLOTS (grandes <= K - 1 por la cota universal M < c, "
        "slots ESCALONADOS r_i <= (M - (g - i) t)/i por "
        "monotonia, pequenas por greedy-halving + cuerda de "
        "fila) elimina el cardinal con nodos fijos; el motor "
        "corona_slots es sound (negativos B(b)/B(c), que "
        "cazaron el cabe_matriz-sin-pesos y los bloques "
        "fantasma) y nunca certifica de mas (300 contrastes "
        "con corona_suf).  APLICACION CERTIFICADA: G-b' con "
        "cardinal LIBRE en Y in [1, 6.6] (extiende r2bmulti).  "
        "FASE 2 (declarada): Y > 6.6 y k >= 2 — el producto "
        "regimenes homogeneos x slots; G-e/G-g pesadas como "
        "destino final del lema", True)


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
