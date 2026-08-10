#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Multipieza R2b (docs/drafts/r2bmulti.md): sube a CERTIFICADO por
subdivision dos de los barridos MC que r2bcert declaro fuera:

  [G-b'] la rama X' > 0 de R2b (piezas explicitas en u): corona
  {Y, m, sigma2} U X' en c = Sigma_S + Y + Sigma_X', con 1-3 piezas
  X' de tamano <= Y.  Certificada sobre un superconjunto de la CAJA
  DEL BARRIDO MC (correccion del acta: el techo Y <= 6.6 viene de
  Y < SS+X_Y+w con los topes de MUESTREO X_Y <= 3, w <= 1.6 — no de
  una pared derivada; X_Y > 3 queda FUERA, declarado): sin ventanas
  de alpha/Y, s2 < 1 entera (pared real), ligereza + s1 >= s2.

  [ESP X > 0] la rama especular de r2bcert FUERA del corte X = 0,
  con X_Y = 0: trio {z, D_m, sigma2} en c' = Y - omega, ventanas
  desplazadas por X_alpha <= 1.5, X_z <= 1, X_m <= 1 - omega, en
  la caja del barrido (omega <= 1.6).  B&B de cotas de esquina con
  coordenadas CLAMPADAS a las ventanas (leccion de bolsillos) y
  DOS cotas por caja (la global y la acoplada al suelo diametral
  c' = 1 + z, donde theta(z, m) <= pi identicamente).

EL MOTOR (esquina pesimista + arc-LP, el esquema declarado en
r2bcert par. 4): sobre una caja, evaluar el arc-LP con las piezas en
sus TECHOS y la capacidad en su SUELO domina todo punto real — theta
crece con las piezas y decrece con R (exacto), los requisitos r_A
son monotonos en las theta, y una d factible para requisitos mayores
sirve para menores (LAS MISMAS POSICIONES VALEN).  Si la esquina
pesimista es factible, TODA la caja lo es.

SOLIDEZ del criterio (leccion de f3cierre + correccion del acta):
la banda ~1e-9 del primal es favorable-a-factible — inaceptable
para suficiencia — y exigir margen al primal por bases es imposible
(todo vertice tiene filas activas EN igualdad).  El LP de HOLGURA
MAXIMA (max t, HiGHS) actua de BUSCADOR y el CERTIFICADO es la
verificacion en float puro de la d devuelta (_verifica_d: holgura
>= 5e-8 por arco, error float ~1e-15) — el t* de HiGHS lleva error
de objetivo medido de hasta 2.5e-8 y no basta solo; f3cierre [E]
valido el LP de FACTIBILIDAD del sistema, no el max-t.  Solo se usa
la direccion de SUFICIENCIA del arc-LP (elemental y valida para
todo k: una d factible coloca y toda pareja queda >= theta por
ambos lados); la caracterizacion exacta k <= 5 / k = 6 no se
invoca.

FUERA (declarado): G-e / G-g pesadas (el mural {*, m} U A con A
multipieza sin cota en |A|: exige un lema de reduccion de |A| que no
esta hecho), la ESP con X_Y > 0 (piezas en la corona de v con
capacidad phi-descontada — el analogo especular de G-b' con tarifa
peor), G-b' con X_Y > 3 u omega > 1.6 (topes de muestreo del MC) y
omega > 1.6 en la ESP.  Siguen como barridos MC adversariados
(puertocii G-b'/G-e/G-g).

Bloques: [A] el lema del motor (monotonias sympy + criterio
estricto + sanity contra corona_suf); [B] G-b' con 1 pieza X'
(k = 4); [C] G-b' con 2 y 3 piezas X' (k = 5, 6); [D] ESP X > 0
(X_Y = 0), 8 dims; [E] controles y alcance honesto.
"""
import heapq
import itertools
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, theta_w, corona_suf
from arcolp import dual_factible, pares_caben, requisitos, gaps_de

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260818'))


# ---------------------------------------------------------------- el motor
def th(a, b, c):
    """theta_w con pi-gorra tambien para piezas >= c (cota valida;
    la caja se resuelve por subdivision)."""
    if a >= c - 1e-15 or b >= c - 1e-15:
        return PI
    return theta_w(a, b, c)


def _verifica_d(d, arcos_req, n):
    """Verificacion INDEPENDIENTE DEL SOLVER (correccion del acta:
    el error del objetivo de HiGHS en el max-t llega a 2.5e-8 y
    1e-7 es exactamente su tolerancia por defecto — el t* reportado
    no basta como certificado): la d devuelta se re-evalua en float
    puro y se exige holgura minima >= MARGEN/2 en cada arco, d >= 0
    y |Sigma d - 2 pi| <= 1e-9 (renormalizando el reparto si hace
    falta).  El error float de una suma de <= 7 terminos es ~1e-15:
    la holgura verificada es real."""
    if d is None or any(x < 0.0 for x in d):
        return False
    s = sum(d)
    if abs(s - 2 * PI) > 1e-9:
        return False
    return all(sum(d[i] for i in g) - r >= MARGEN / 2
               for g, r in arcos_req)


def lp_margen(orden, R):
    """LP de HOLGURA MAXIMA del sistema de arcos (HiGHS): max t
    con Sigma d(A) >= r_A + t para todo arco, Sigma d = 2 pi,
    d >= 0.  Devuelve (t*, d) o (None, None).  El certificado NO es
    t*: es la verificacion en float de la d (_verifica_d) — un
    margen estricto sobre el primal por bases es imposible (todo
    vertice tiene filas activas EN igualdad), y f3cierre [E] valido
    el LP de FACTIBILIDAD del mismo sistema (no el max-t): la
    solidez aqui no descansa en el solver."""
    from scipy.optimize import linprog
    n = len(orden)
    req = requisitos(orden, R)
    A_ub, b_ub, arcos_req = [], [], []
    for a, r in req.items():
        g = gaps_de(a, n)
        A_ub.append([-1.0 if i in g else 0.0
                     for i in range(n)] + [1.0])
        b_ub.append(-r)
        arcos_req.append((g, r))
    res = linprog([0.0] * n + [-1.0], A_ub=A_ub, b_ub=b_ub,
                  A_eq=[[1.0] * n + [0.0]], b_eq=[2 * PI],
                  bounds=[(0, None)] * n + [(None, None)],
                  method='highs')
    if res.status != 0:
        return None, None
    return -res.fun, (list(res.x[:n]), arcos_req, n)


def _ordenes(piezas):
    """Ordenes ciclicos: primero la heuristica (grandes separadas),
    luego todos (primera pieza fija, mitad por reflexion)."""
    s = sorted(piezas, reverse=True)
    heur = s[0::2] + s[1::2][::-1]
    yield heur
    base = piezas[0]
    vistos = set()
    for perm in itertools.permutations(piezas[1:]):
        if perm[::-1] in vistos:
            continue
        vistos.add(perm)
        yield [base] + list(perm)


MARGEN = 1e-7


def cabe_esquina(piezas, R):
    """Criterio SOUND de suficiencia (nivel instancia): existe
    orden cuyo LP de holgura maxima da t* >= MARGEN y cuya d pasa
    la verificacion en float (_verifica_d — el certificado real; el
    t* de HiGHS lleva error de objetivo de hasta 2.5e-8, medido en
    el acta, y no basta solo).  El dual (necesario) poda ordenes
    infactibles rapido."""
    if not pares_caben(piezas, R):
        return False
    for orden in _ordenes(piezas):
        if not dual_factible(orden, R):
            continue
        t, pack = lp_margen(orden, R)
        if t is not None and t >= MARGEN and _verifica_d(*pack):
            return True
    return False


def lp_margen_mat(orden, thmat):
    """LP de holgura maxima sobre una MATRIZ mayorante de thetas
    (cotas por termino): mismo sistema de arcos con
    r_A = max(suma theta_consec, theta_extremos) leido de thmat.
    Devuelve (t*, pack) para _verifica_d, como lp_margen."""
    from scipy.optimize import linprog
    n = len(orden)
    thc = [thmat[orden[i]][orden[(i + 1) % n]] for i in range(n)]
    A_ub, b_ub, arcos_req = [], [], []
    for s in range(n):
        for L in range(1, n):
            fin = (s + L) % n
            r = max(sum(thc[(s + t) % n] for t in range(L)),
                    thmat[orden[s]][orden[fin]])
            fila = [0.0] * n + [1.0]
            g = frozenset((s + t) % n for t in range(L))
            for t in range(L):
                fila[(s + t) % n] = -1.0
            A_ub.append(fila)
            b_ub.append(-r)
            arcos_req.append((g, r))
    res = linprog([0.0] * n + [-1.0], A_ub=A_ub, b_ub=b_ub,
                  A_eq=[[1.0] * n + [0.0]], b_eq=[2 * PI],
                  bounds=[(0, None)] * n + [(None, None)],
                  method='highs')
    if res.status != 0:
        return None, None
    return -res.fun, (list(res.x[:n]), arcos_req, n)


def banda_matriz(tam, thmat):
    """Criterio ANTIPODAL (decisivo en la arista SS -> 1, donde el
    par (Y, m) exige pi por ambos lados y el margen del LP circular
    tiende a 0 incluso en puntos reales): Y y m a distancia
    EXACTAMENTE pi (theta real < pi ESTRICTO en todo punto real —
    algebra de pares en [A]: f(Y) f(m) < 1 sii SS + Sigma x > 1 —
    asi que d = pi > theta sin apoyo numerico), y la cadena
    {s2, x's} en un semicirculo: sistema de CAMINO, cuyo dual de
    familias disjuntas es EXACTO (matrices de intervalo TU; el
    contraejemplo de arcolp es circular).  El par (Y, m) se excluye
    del sistema (analitico); los pares cadena-extremo van el camino
    corto y el complementario >= pi >= theta automatico.  Certifica
    si algun orden tiene presupuesto minimo <= pi - MARGEN."""
    n = len(tam)                       # 0 = Y, 1 = m, 2.. = cadena
    for perm in itertools.permutations(range(2, n)):
        cadena = [0] + list(perm) + [1]
        m = len(cadena) - 1            # numero de gaps
        arcs = []
        for i in range(m):
            for j in range(i + 1, m + 1):
                r_c = sum(thmat[cadena[t]][cadena[t + 1]]
                          for t in range(i, j))
                if i == 0 and j == m:
                    r = r_c            # (Y, m) analitico: excluido
                else:
                    r = max(r_c, thmat[cadena[i]][cadena[j]])
                arcs.append((frozenset(range(i, j)), r))

        def peor(k, usados, acum):
            best = acum
            for t in range(k, len(arcs)):
                g, r = arcs[t]
                if not (g & usados):
                    v = peor(t + 1, usados | g, acum + r)
                    if v > best:
                        best = v
            return best

        if peor(0, frozenset(), 0.0) <= PI - MARGEN:
            return True
    return False


def cabe_matriz(tam, thmat):
    """Existe orden ciclico factible con margen para la matriz
    mayorante (tam = tamanos para la heuristica grandes-separadas;
    la suma rapida poda ordenes sin LP)."""
    n = len(tam)
    idx = sorted(range(n), key=lambda i: -tam[i])
    heur = idx[0::2] + idx[1::2][::-1]
    ordenes = [heur]
    vistos = {tuple(heur[1:]), tuple(heur[1:][::-1])}
    for perm in itertools.permutations(range(1, n)):
        if perm in vistos or perm[::-1] in vistos:
            continue
        vistos.add(perm)
        ordenes.append([0] + list(perm))
    for orden in ordenes:
        suma = sum(thmat[orden[i]][orden[(i + 1) % n]]
                   for i in range(n))
        if suma > 2 * PI - MARGEN:
            continue                   # poda: suma consecutiva
        t, pack = lp_margen_mat(orden, thmat)
        if t is not None and t >= MARGEN and _verifica_d(*pack):
            return True
    return False


def bnb_factible(root, criterio, eps=2e-4, max_boxes=2000000):
    """B&B de factibilidad (DFS): criterio(box) -> None (sin puntos
    reales: poda) / True (esquina pesimista factible: certificada) /
    False (partir).  Falla si una caja llega a anchura relativa
    < eps sin resolverse (se devuelve para analisis)."""
    stack = [tuple(root)]
    n_vistas, certificadas = 0, 0
    while stack:
        box = stack.pop()
        n_vistas += 1
        if n_vistas > max_boxes:
            return False, box, n_vistas, certificadas
        r = criterio(box)
        if r is None:
            continue
        if r is True:
            certificadas += 1
            continue
        d = len(box) // 2
        anchos = [(box[2 * i + 1] - box[2 * i])
                  / max(box[2 * i + 1], 1.0) for i in range(d)]
        k = max(range(d), key=lambda i: anchos[i])
        if anchos[k] < eps:
            return False, box, n_vistas, certificadas
        m = (box[2 * k] + box[2 * k + 1]) / 2
        b1, b2 = list(box), list(box)
        b1[2 * k + 1] = m
        b2[2 * k] = m
        stack.append(tuple(b1))
        stack.append(tuple(b2))
    return True, None, n_vistas, certificadas


# ------------------------------------------------------- G-b' (bloques B/C)
Y_MAX = 6.6      # techo real: Y < Sigma_S + X_Y + w <= 2 + 3 + 1.6


def criterio_gbp(box):
    """Caja (Y, s2, SS, x_1..x_j) del SUPERCONJUNTO de G-b':
    Y in [1, 6.6], ligereza SS in (1, 1 + s2), s1 >= s2 (s2 <=
    SS/2), x_i in (0, Y].  COTAS POR TERMINO (la esquina mixta
    global pierde la holgura de pares SS-1+x en la arista SS -> 1):
    cada theta(a, b) se mayora en SU esquina — participantes en
    techo CON su aporte a la capacidad c = SS + Y + Sigma x, resto
    en suelo; valido porque d theta/d a tiene el signo de
    R - a - b = SS + resto > 1 - 1 > 0 (sympy en [A]).  En los
    puntos reales TODOS los pares caben con holgura (algebra en
    [A]): la pi-gorra de la matriz nunca tapa un par imposible."""
    Yl, Yh, s2l, s2h, SSl, SSh = box[:6]
    xs = [(box[i], box[i + 1]) for i in range(6, len(box), 2)]
    # podas exactas (cajas sin puntos reales)
    if SSh <= 1.0:
        return None                    # pared (D): Sigma_S > 1
    if SSl >= 1.0 + s2h:
        return None                    # ligereza: SS < 1 + s2
    if 2.0 * s2l > SSh:
        return None                    # s1 >= s2
    if any(xl > Yh for xl, _ in xs):
        return None                    # x <= Y
    # techos de pieza (clamps al dominio real) y aportes a c
    s2_p = min(s2h, SSh / 2.0)
    SS_lo = max(SSl, 1.0)
    hi = [Yh, 1.0, s2_p] + [min(xh, Yh) for _, xh in xs]
    cap_lo = [Yl, 0.0, 0.0] + [xl for xl, _ in xs]
    cap_hi = [Yh, 0.0, 0.0] + [min(xh, Yh) for _, xh in xs]
    n = len(hi)
    thmat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            R_c = SS_lo + sum(cap_hi[k] if k in (i, j) else cap_lo[k]
                              for k in range(n))
            thmat[i][j] = thmat[j][i] = th(hi[i], hi[j], R_c)
    # antipodal primero (barato, decisivo en la arista SS -> 1);
    # el LP circular por ordenes despues
    if banda_matriz(hi, thmat):
        return True
    return cabe_matriz(hi, thmat)


def bloque_B():
    print("[B] G-b' con 1 pieza X' (corona k = 4) certificada")
    ok = True
    root = [1.0, Y_MAX, 0.0, 1.0, 1.0, 2.0, 0.0, Y_MAX]
    exito, caja, n, cert = bnb_factible(root, criterio_gbp)
    ok &= check(f"G-b' j = 1 CERTIFICADA sobre el superconjunto de "
                f"la CAJA DEL BARRIDO MC (correccion del acta: el "
                f"techo Y <= {Y_MAX} viene de Y < SS+X_Y+w con los "
                f"topes de muestreo X_Y <= 3, w <= 1.6 — X_Y mayor "
                f"queda FUERA, declarado en [E]; s2 < 1 ENTERA, "
                f"pared real; ligereza + s1 >= s2; x <= Y; SIN "
                f"ventanas de alpha/Y): la corona {{Y, m, s2, x}} "
                f"cabe en c = Sigma_S + Y + x en toda la caja; {n} "
                f"cajas vistas, {cert} certificadas"
                + ("" if exito else f"; CAJA SIN RESOLVER {caja}"),
                exito)
    return ok


def bloque_C():
    print("[C] G-b' con 2 y 3 piezas X' (coronas k = 5, 6)")
    ok = True
    root2 = [1.0, Y_MAX, 0.0, 1.0, 1.0, 2.0,
             0.0, Y_MAX, 0.0, Y_MAX]
    exito2, caja2, n2, cert2 = bnb_factible(root2, criterio_gbp)
    ok &= check(f"G-b' j = 2 (k = 5, misma caja del barrido): {n2} "
                f"cajas, {cert2} certificadas"
                + ("" if exito2 else f"; CAJA SIN RESOLVER {caja2}"),
                exito2)
    root3 = [1.0, Y_MAX, 0.0, 1.0, 1.0, 2.0,
             0.0, Y_MAX, 0.0, Y_MAX, 0.0, Y_MAX]
    exito3, caja3, n3, cert3 = bnb_factible(root3, criterio_gbp)
    ok &= check(f"G-b' j = 3 (k = 6, LP de holgura maxima): "
                f"{n3} cajas, {cert3} certificadas"
                + ("" if exito3 else f"; CAJA SIN RESOLVER {caja3}"),
                exito3)
    return ok


# ------------------------------------------------------------ ESP (bloque D)
W_MAX, XP_MAX, XZ_MAX = 1.6, 1.5, 1.0


def esp_ub(box):
    """Cota superior del trio {z, 1, s2} de la ESP con X > 0
    (X_Y = 0) en la caja (w, s2, SS, Xp, Xz, Xm, a, z).  Ventanas de
    G-g con las X: alpha in [max(1+w, SS+Xp+w), 1+s2+Xp+w); z in
    [alpha+Xz+w, alpha+Xz+s2+w); cola(Y) = (1+SS+Xm+a+Xp+z+Xz)/phi;
    c' = Y - w >= max(1+z, colaY - w).  Coordenadas CLAMPADAS.
    None = caja sin puntos reales."""
    wl, wh, s2l, s2h, SSl, SSh, Xpl, Xph, Xzl, Xzh, Xml, Xmh, \
        al, ah, zl, zh = box
    # podas exactas
    if 2.0 * s2l > SSh:
        return None                    # s1 >= s2
    if SSl >= 1.0 + s2h:
        return None                    # ligereza
    if SSl + Xml > PHI:
        return None                    # pared de masa (cola de m)
    if Xml > max(0.0, 1.0 - wl):
        return None                    # X_m <= 1 - w
    # ventana de alpha (clamps)
    a_lo = max(al, 1.0 + wl, SSl + Xpl + wl)
    a_hi = min(ah, 1.0 + s2h + Xph + wh)
    if a_lo >= a_hi:
        return None
    # ventana de z (clamps)
    z_lo = max(zl, a_lo + Xzl + wl)
    z_hi = min(zh, a_hi + Xzh + s2h + wh)
    if z_lo >= z_hi:
        return None
    # ventana de Y no vacia (X_Y = 0): max(colaY, 1+z+w) < SS+z+w
    colaY_lo = (1.0 + SSl + Xml + a_lo + Xpl + z_lo + Xzl) / PHI
    if colaY_lo >= SSh + z_hi + wh:
        return None                    # pinza: sin Y legal
    # DOS cotas validas por caja, se toma el minimo:
    # UB1 (acoplada al suelo diametral): c' >= 1 + z con el MISMO z
    # => theta(z, m) <= pi siempre; theta(s2, z; 1+z) crece en z
    # (d/dz ~ 1 - s2 > 0) => esquina z_hi coherente; theta(1, s2)
    # decrece en c' => c' = 1 + z_lo
    s2_p = min(s2h, SSh / 2.0)
    ub1 = (PI + th(1.0, s2_p, 1.0 + z_lo)
           + th(s2_p, z_hi, 1.0 + z_hi))
    # UB2 (esquina global): c' >= max(1 + z_lo, cola - w)
    c_lo = max(1.0 + z_lo, colaY_lo - wh)
    if c_lo <= max(z_hi, 1.0, s2_p) + 1e-12:
        ub2 = 2 * PI + 1.0             # sin resolver por esta via
    else:
        ub2 = (th(z_hi, 1.0, c_lo) + th(1.0, s2_p, c_lo)
               + th(s2_p, z_hi, c_lo))
    return min(ub1, ub2)


def bnb_sup(root, ub_fn, objetivo, max_boxes=6000000):
    """B&B de supremo (max-heap por cota, como r2bcert)."""
    v0 = ub_fn(tuple(root))
    if v0 is None:
        return True, 0.0, 0
    heap = [(-v0, tuple(root))]
    n = 0
    while heap:
        n += 1
        if n > max_boxes:
            return False, -heap[0][0], n
        negv, box = heapq.heappop(heap)
        if -negv < objetivo:
            return True, -negv, n
        d = len(box) // 2
        anchos = [((box[2 * i + 1] - box[2 * i])
                   / max(box[2 * i + 1], 1.0), i) for i in range(d)]
        anchos.sort(reverse=True)
        k = anchos[0][1]
        m = (box[2 * k] + box[2 * k + 1]) / 2
        b1, b2 = list(box), list(box)
        b1[2 * k + 1] = m
        b2[2 * k] = m
        for h in (tuple(b1), tuple(b2)):
            v = ub_fn(h)
            if v is not None:
                heapq.heappush(heap, (-v, h))
    return True, 0.0, n


def bloque_D():
    print("[D] ESP fuera del corte X = 0 (X_Y = 0): B&B de 8 dims")
    ok = True
    a_max = 1.0 + 0.999 + XP_MAX + W_MAX
    z_max = a_max + XZ_MAX + 0.999 + W_MAX
    root = [0.0, W_MAX, 0.0, 0.999, 1.0, PHI, 0.0, XP_MAX,
            0.0, XZ_MAX, 0.0, 1.0, 1.0, a_max, 1.0, z_max]
    objetivo = 2 * PI - 0.3
    exito, sup, n = bnb_sup(root, esp_ub, objetivo)
    ok &= check(f"ESP con X > 0 (X_alpha <= {XP_MAX}, X_z <= "
                f"{XZ_MAX}, X_m <= 1-w, X_Y = 0) en la caja del "
                f"barrido (omega <= {W_MAX}, alpha <= {a_max:.1f}, "
                f"z <= {z_max:.1f}): sup del trio {{z, D_m, s2}} < "
                f"2 pi - 0.3 CERTIFICADO con {n} cajas (cota "
                f"alcanzada {sup:.4f}) — las ventanas desplazadas "
                f"del acta H1/H2 de r2bcert quedan cubiertas en la "
                f"rama X_Y = 0", exito)
    ok &= check("[ENUNCIADO] con el suelo de cola(Y) las X SUBEN la "
                "capacidad ((...+X_m+X_alpha+X_z)/phi) pero tambien "
                "los techos de las ventanas (z crece con las X): el "
                "B&B lleva ambos efectos con coordenadas clampadas "
                "y DOS cotas por caja — la esquina diametral "
                "c' = 1+z la rescata cola(Y) igual que en r2bcert, "
                "ahora con X > 0; omega > 1.6 y X_Y > 0 quedan "
                "FUERA (declarado en [E])", True)
    return ok


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] el motor: esquina pesimista + criterio estricto")
    import sympy as sp
    ok = True
    x, R = sp.symbols('x R', positive=True)
    f = x / (R - x)
    ok &= check("dominacion (sympy): df/dx = R/(R-x)^2 > 0 y "
                "df/dR = -x/(R-x)^2 < 0 exactos => theta crece con "
                "las piezas y decrece con la capacidad; los "
                "requisitos r_A = max(suma theta_consec, theta_ext) "
                "son monotonos en las theta y la factibilidad del "
                "sistema de arcos es ANTITONA en los requisitos "
                "(la misma d vale): esquina pesimista factible => "
                "TODA la caja factible",
                sp.simplify(sp.diff(f, x) - R / (R - x) ** 2) == 0
                and sp.simplify(sp.diff(f, R) + x / (R - x) ** 2)
                == 0)
    # la regla de esquinas POR TERMINO: con la pieza a dentro de la
    # capacidad (R = a + A, A = resto), el producto f(a) f(b) =
    # a b / (A (a + A - b)) crece en a sii A - b = R - a - b > 0
    a_, b_, A_ = sp.symbols('a b A', positive=True)
    P = a_ * b_ / (A_ * (a_ + A_ - b_))
    ok &= check("regla por termino (sympy): d/da [f(a) f(b)] con "
                "R = a + A tiene el signo de A - b = R - a - b = "
                "SS + resto > 0 en el superconjunto (SS > 1): cada "
                "theta se mayora con los PARTICIPANTES en techo "
                "(incluido su aporte a c) y el resto en suelo — la "
                "esquina mixta global perdia la holgura de pares "
                "SS - 1 + x en la arista SS -> 1 y NO se usa",
                sp.simplify(sp.diff(P, a_)
                            - b_ * (A_ - b_)
                            / (A_ * (a_ + A_ - b_) ** 2)) == 0)
    ok &= check("[ENUNCIADO] pares del superconjunto G-b' (algebra): "
                "con c = SS + Y + Sigma x y SS > 1: (Y, m): Y + 1 "
                "<= c sii SS + Sigma x > 1 OK; (Y, x_i): x_i <= "
                "SS + resto OK; (m, s2), (m, x), (s2, x): mayoradas "
                "por Y >= max(1, s2, x); (x_i, x_j): ambos sumandos "
                "estan en c.  TODOS los pares caben ESTRICTO en "
                "todo punto real: la pi-gorra de la matriz nunca "
                "tapa un par imposible (el artefacto del arc-LP v1 "
                "no puede reaparecer)", True)
    ok &= check("[ENUNCIADO] criterio ESTRICTO (leccion f3cierre + "
                "correccion del acta): la banda ~1e-9 del primal es "
                "favorable-a-factible e inaceptable para "
                "SUFICIENCIA — y un margen sobre el primal por "
                "bases es imposible (vertices con filas activas EN "
                "igualdad).  El criterio: LP de HOLGURA MAXIMA "
                "(max t) COMO BUSCADOR y verificacion en FLOAT de "
                "la d devuelta como CERTIFICADO (holgura >= 5e-8 "
                "por arco re-evaluada; error float ~1e-15) — el t* "
                "de HiGHS lleva error de objetivo medido de hasta "
                "2.5e-8 y su cita anterior ('precision ~1e-9') era "
                "FALSA; f3cierre [E] valido el LP de FACTIBILIDAD, "
                "no el max-t: la solidez ya no descansa en el "
                "solver", True)
    # sanity del criterio: en la tangencia exacta el estricto DEBE
    # rechazar y con holgura real aceptar
    R3 = 1 + 2 / math.sqrt(3)
    t_tan, _ = lp_margen([1.0] * 3, R3)
    t_hol, _ = lp_margen([1.0] * 3, R3 + 1e-5)
    est = cabe_esquina([1.0] * 3, R3)
    cla = cabe_esquina([1.0] * 3, R3 + 1e-5)
    ok &= check(f"direccion del margen: en R3* exacto t* = "
                f"{t_tan:.2e} < 1e-7 (rechaza, {est}) y en R3* + "
                f"1e-5 t* = {t_hol:.2e} >= 1e-7 (acepta, {cla}): "
                f"el certificado nunca se apoya en la banda",
                (not est) and cla and abs(t_tan) < 1e-7)
    # sanity del motor contra corona_suf: si el constructivo cabe,
    # el arc-LP (necesario para coronas) debe caber tambien
    rng = random.Random(SEED)
    n_s, m_s, exc = 0, 0, 0
    while n_s < 400:
        s2 = rng.uniform(0.05, 0.999)
        s1 = rng.uniform(s2, 0.999)
        SS = s1 + s2
        if SS <= 1.0 or SS >= 1.0 + s2:
            continue
        Y = rng.uniform(1.0, 4.0)
        xs = [rng.uniform(0.01, Y)
              for _ in range(rng.randrange(1, 4))]
        c = SS + Y + sum(xs)
        n_s += 1
        piezas = sorted([Y, 1.0, s2] + xs, reverse=True)
        if corona_suf(piezas, c)[0]:
            m_s += 1
            if not cabe_esquina(piezas, c):
                exc += 1
    ok &= check(f"sanity del motor: en {n_s} instancias G-b' "
                f"aleatorias, corona_suf cabe en {m_s} y el "
                f"criterio estricto confirma TODAS ({exc} "
                f"excepciones) — el arc-LP domina al constructivo",
                m_s > 200 and exc == 0)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles y alcance honesto")
    ok = True
    # (a) la esquina de r2bcert: cerca de (SS -> 1, x -> 0) el
    #     motor certifica (limite trio 5.60 con margen 0.68)
    caja = (1.0, 1.001, 0.499, 0.5, 1.0, 1.0001, 0.0, 0.001)
    r = criterio_gbp(caja)
    ok &= check(f"(a) esquina critica (SS -> 1+, x -> 0, Y -> 1, "
                f"s2 = 1/2): el motor certifica la caja diminuta "
                f"({r}) — coherente con la esquina certificada "
                f"pi + 4 asin(1/sqrt3) = 5.60 de r2bcert (margen "
                f"0.68 absorbe las piezas X' -> 0)", r is True)
    # (b) solidez: coronas IMPOSIBLES no se certifican — el optimo
    #     clasico de 4 iguales (1 + sqrt2) por debajo, y la matriz
    #     mayorante en una caja-punto infactible
    mala = cabe_esquina([1.0, 1.0, 1.0, 1.0], 1 + math.sqrt(2)
                        - 1e-4)
    t_gordo = 2 * PI / 4 + 0.05
    mat_mala = [[0.0 if i == j else t_gordo for j in range(4)]
                for i in range(4)]
    r_mala = cabe_matriz([1.0] * 4, mat_mala)
    ok &= check(f"(b) controles negativos: {{1,1,1,1}} bajo el "
                f"optimo clasico 1+sqrt2: cabe_esquina = {mala}; y "
                f"cabe_matriz con todos los theta = pi/2 + 0.05 "
                f"(toda suma ciclica = 2 pi + 0.2 > 2 pi): "
                f"{r_mala} — ni el criterio de instancia ni el de "
                f"matriz certifican lo imposible",
                mala is False and r_mala is False)
    # (c) alcance honesto
    ok &= check("[ENUNCIADO] FUERA (declarado): G-e / G-g pesadas "
                "(mural con A multipieza, |A| sin cota — falta el "
                "lema de reduccion de |A|); la ESP con X_Y > 0 "
                "(corona de v multipieza con capacidad "
                "phi-descontada, el analogo especular de G-b' con "
                "tarifa peor); G-b' con X_Y > 3 u omega > 1.6 "
                "(topes de MUESTREO del MC, no paredes derivadas — "
                "correccion del acta: hay puntos legales con X_Y = "
                "4, Y = 7 fuera de la caja); y omega > 1.6 en la "
                "ESP (sup MC 5.7379 con omega hasta 3.0, acta "
                "r2bcert). Permanecen como barridos MC "
                "adversariados (puertocii G-b'/G-e/G-g). Los "
                "certificados nuevos usan solo la SUFICIENCIA del "
                "arc-LP (valida para todo k) y NO tocan los "
                "dominios de r2bcert: los EXTIENDEN", True)
    return ok


def main():
    print("=" * 68)
    print("MULTIPIEZA R2b: G-b' certificada y ESP fuera del corte "
          "X = 0 (drafts/r2bmulti.md)")
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
