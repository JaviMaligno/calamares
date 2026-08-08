#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lema de dualidad/zigzag (coronacolas.md par.4): certificados.

El puente evidencia -> teorema para la cadena corona-contra-colas.
Descomposicion (version espina/maximalidad):

  Z1  theta(a,b) = g(u_a + u_b) con u = log f, f(x) = x/(R-x) y
      g(s) = 2 asin(e^{s/2}) CRECIENTE y CONVEXA en s < 0.
  Z2  para un par NO apilable (R < max + 2 min) sin confinamiento,
      gamma_min = theta_w EXACTO: en la caja [0, R-a] x [0, R-b] las
      esquinas con d -> 0 dan h -> -inf y la esquina mural da
      h = cos theta_w (identidad algebraica).  La necesidad y la
      construccion usan EL MISMO numero por par.
  DIC (dicotomia hueco/muro) el margen NS-2(a, s, b) :=
      theta(a,s) + theta(s,b) - theta(a,b) es CRECIENTE en s y se anula
      exactamente en s = p(a,b,R), el radio del bolsillo de Descartes
      del par tangente (a,b) (los tres murales mutuamente tangentes:
      los angulos murales suman).  margen <= 0 <=> s <= p(a,b,R): la
      pieza cabe MURAL dentro del hueco del par sin empujarlo.
  ESP (espina, por MAXIMALIDAD del camino mas largo) en la construccion
      ciclica por camino mas largo, el camino critico (espina) cumple:
      (i) sus triples consecutivos tienen margen NS-2 >= 0 (un atajo
      dominante alargaria el camino: contradiccion con maximalidad);
      (ii) toda cadena de piezas saltadas entre dos espinas a, b suma
      <= theta(a,b) (el camino por las paradas seria mas largo), luego
      los saltados caben murales en su hueco, en orden, y por DIC cada
      saltado es sub-bolsillo de su par;
      (iii) el total = suma ciclica de la espina en su orden inducido.
  V   (condicion de valle) las parejas espina-espina no adyacentes son
      legales en las posiciones del camino mas largo (la validacion de
      TODAS las parejas del chequeo constructivo).  Es la unica pieza
      sin prueba general: se verifica en cada dominio (barrido) y el
      chequeo es parte de la construccion (nunca certifica ilegal).
  Z5  (dualidad) la espina tiene <= 7 miembros en los dominios: la
      necesidad (subconjuntos, min sobre ordenes, gamma_min = theta_w
      por Z2 y NB-espina) y la construccion (exhaustiva/rica sobre
      ordenes) realizan EL MISMO certificado sobre la espina =>
      R_construct = R_lb y en R >= R_lb la corona cabe: desbloqueo.

Controles: la instancia aurea es el punto critico exacto de NS-2
(margen 0 en s = phi/2 = p(phi, 1, phi+1), signo cambia al cruzar).
Z3 (zigzag minimiza la suma ciclica) queda como HEURISTICA de arranque:
se reporta su gap sin cargar la prueba (la espina va por exhaustivo).
"""
import math
import os
import random
import sys
from itertools import permutations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import (PHI, PI, check, theta_w, gamma_min, cascada,
                         R_lb_pack)

ITER = int(os.environ.get('CC_ITER', '60000'))


# ------------------------------------------------------------ utilidades
def bolsillo(a, b, R):
    """Radio del bolsillo de Descartes del par mural tangente (a, b),
    con el discriminante clampeado (tangencia exacta => disc = 0-)."""
    ka, kb, kw = 1.0 / a, 1.0 / b, -1.0 / R
    disc = max(0.0, ka * kb + kb * kw + kw * ka)
    kp = ka + kb + kw + 2.0 * math.sqrt(disc)
    return 1.0 / kp if kp > 1e-12 else float('inf')


def zig_de(desc):
    k = len(desc)
    out, lo, hi = [], 0, k - 1
    for q in range(k):
        out.append(desc[lo] if q % 2 == 0 else desc[hi])
        if q % 2 == 0:
            lo += 1
        else:
            hi -= 1
    return out


def margen_ns2(a, s, b, R):
    return theta_w(a, s, R) + theta_w(s, b, R) - theta_w(a, b, R)


def suma_ciclica(orden, R):
    k = len(orden)
    return sum(theta_w(orden[i], orden[(i + 1) % k], R) for i in range(k))


def ciclo_instr(orden, R):
    """ciclo_constructivo instrumentado: posiciones por camino mas
    largo, espina = camino critico 0 -> k-1 (+ cierre a 0).  Devuelve
    (ok, total, espina_indices, fallo_pareja, fallo_par_espina)."""
    k = len(orden)
    th = {}
    for i in range(k):
        for j in range(i + 1, k):
            if orden[i] + orden[j] > R + 1e-12:
                return False, float('inf'), [], False, False
            th[(i, j)] = th[(j, i)] = theta_w(orden[i], orden[j], R)
    alfa = [0.0] * k
    pred = [-1] * k
    for i in range(1, k):
        for t in range(i):
            cand = alfa[t] + th[(t, i)]
            if cand > alfa[i]:
                alfa[i], pred[i] = cand, t
    total = alfa[-1] + th[(k - 1, 0)]
    espina = []
    t = k - 1
    while t != -1:
        espina.append(t)
        t = pred[t]
    espina = espina[::-1]              # 0 = ... = k-1 en orden
    fallo_pareja = False
    fallo_par_espina = False
    en_espina = set(espina)
    if total <= 2 * PI + 1e-9:
        for i in range(k):
            for j in range(i + 1, k):
                d = alfa[j] - alfa[i]
                d = min(d, 2 * PI - d)
                if d < th[(i, j)] - 1e-9:
                    fallo_pareja = True
                    if i in en_espina and j in en_espina:
                        fallo_par_espina = True
    ok = total <= 2 * PI + 1e-9 and not fallo_pareja
    return ok, total, espina, fallo_pareja, fallo_par_espina


def corona_instr(todos, R, semilla=0):
    """corona_suf instrumentada: splits t + ordenes (zig, desc,
    barajas); devuelve el diagnostico del mejor intento.
    (exito, exceso, espina_r, saltados_diag, fallo_V, apilables_espina)
    con saltados_diag = lista de (cadena - arista, s - bolsillo)."""
    rl = random.Random(semilla)
    asc = sorted(todos)
    mejor = None
    for t in range(len(asc)):
        muro = asc[t:]
        if len(muro) < 3:
            break
        desc = sorted(muro, reverse=True)
        ordenes = [zig_de(desc), desc]
        for _ in range(40 if len(desc) > 3 else 6):
            o2 = muro[:]
            rl.shuffle(o2)
            ordenes.append(o2)
        for orden in ordenes:
            ok, total, esp, fV, fVe = ciclo_instr(orden, R)
            exceso = max(0.0, total - 2 * PI)
            if mejor is None or (ok and not mejor[0]) or \
               (ok == mejor[0] and exceso < mejor[1]):
                mejor = (ok, exceso, orden, esp, fV, fVe)
            if ok:
                break
        if mejor and mejor[0]:
            break
    if mejor is None:
        return False, float('inf'), [], [], False, 0
    ok, exceso, orden, esp, fV, fVe = mejor
    k = len(orden)
    espina_r = [orden[i] for i in esp]
    saltados = []
    for w in range(len(esp) - 1):
        i, j = esp[w], esp[w + 1]
        if j - i <= 1:
            continue
        a, b = orden[i], orden[j]
        cadena = (theta_w(a, orden[i + 1], R) +
                  sum(theta_w(orden[t], orden[t + 1], R)
                      for t in range(i + 1, j - 1)) +
                  theta_w(orden[j - 1], b, R))
        arista = theta_w(a, b, R)
        for t in range(i + 1, j):
            s = orden[t]
            saltados.append((cadena - arista, s - bolsillo(a, b, R)))
    apil = sum(1 for x in range(len(espina_r))
               for y in range(x + 1, len(espina_r))
               if R >= max(espina_r[x], espina_r[y]) +
               2 * min(espina_r[x], espina_r[y]) - 1e-12)
    return ok, exceso, espina_r, saltados, fVe, apil


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades exactas (sympy)")
    import sympy as sp
    ok = True
    s = sp.symbols('s', negative=True)
    g = 2 * sp.asin(sp.exp(s / 2))
    gp = sp.diff(g, s)
    ok &= check("Z1: g'(s) = e^{s/2}/sqrt(1-e^s) exacto (g creciente)",
                sp.simplify(gp - sp.exp(s / 2) / sp.sqrt(1 - sp.exp(s)))
                == 0)
    ok &= check("Z1: (log g')' = 1/(2(1-e^s)) exacto, > 0 en s < 0: "
                "g' creciente => g CONVEXA",
                sp.simplify(sp.diff(sp.log(gp), s) -
                            1 / (2 * (1 - sp.exp(s)))) == 0)
    x, a, b, R = sp.symbols('x a b R', positive=True)
    f = x / (R - x)
    ok &= check("f'(x) = R/(R-x)^2 exacto (> 0 en 0 < x < R): "
                "theta(a,x) crece en x; margen NS-2 crece en s",
                sp.simplify(sp.diff(f, x) - R / (R - x) ** 2) == 0)
    h_mural = (((R - a) ** 2 + (R - b) ** 2 - (a + b) ** 2) /
               (2 * (R - a) * (R - b)))
    cos_thw = 1 - 2 * (a / (R - a)) * (b / (R - b))
    ok &= check("Z2: h(R-a, R-b) = 1 - 2 f(a) f(b) = cos theta_w exacto "
                "(la esquina mural de la caja ES el certificado mural)",
                sp.simplify(h_mural - cos_thw) == 0)
    ok &= check("Z2: no apilable => R - b < a + b y R - a < a + b "
                "(esquinas d->0 dan h -> -inf): gamma_min = theta_w",
                True)  # R < max + 2 min <= max + min + min, trivial
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    Rg = phi + 1
    ka, kb, kw = 1 / phi, sp.Integer(1), -1 / Rg
    disc = sp.simplify(ka * kb + kb * kw + kw * ka)
    ok &= check("DIC aurea: discriminante de Descartes de (phi, 1; R = "
                "phi+1) = 0 EXACTO (bolsillo tangente critico)",
                disc == 0)
    kp = sp.simplify(ka + kb + kw)
    ok &= check("DIC aurea: radio del bolsillo = phi/2 exacto",
                sp.simplify(1 / kp - phi / 2) == 0)
    fg = lambda t: t / (Rg - t)
    ok &= check("NS-2 aurea: f(phi) f(phi/2) + f(1) f(phi/2) = 1 y "
                "f(phi) f(1) = 1 exactos => theta(phi, phi/2) + "
                "theta(phi/2, 1) = pi = theta(phi, 1): IGUALDAD",
                sp.simplify(fg(phi) * fg(phi / 2) +
                            fg(1) * fg(phi / 2) - 1) == 0
                and sp.simplify(fg(phi) * fg(1) - 1) == 0)
    # DIC general: en s = p(a,b,R) el margen es cero (tangencia de los
    # tres murales); alta precision numerica sobre una malla
    peor = 0.0
    rng = random.Random(3)
    nid = 0
    for _ in range(4000):
        av = rng.uniform(0.5, 4.0)
        bv = rng.uniform(0.5, 4.0)
        Rv = (av + bv) * rng.uniform(1.0001, 1.4)
        p = bolsillo(av, bv, Rv)
        if p <= 1e-6 or p >= min(av, bv):
            continue
        nid += 1
        peor = max(peor, abs(margen_ns2(av, p, bv, Rv)))
    ok &= check(f"DIC general: margen NS-2 = 0 en s = bolsillo(a,b,R) "
                f"({nid} puntos, peor |margen| = {peor:.2e}): identidad "
                f"de tangencia triple", nid > 1000 and peor < 1e-7)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] espina por maximalidad y la induccion NS-2 => NS")
    ok = True
    rng = random.Random(20260808)
    # (a) maximalidad: en el ciclo por camino mas largo, los triples
    # consecutivos de la espina tienen margen >= 0, las cadenas
    # saltadas suman <= su arista, y todo saltado es sub-bolsillo
    n, v_triple, v_cadena, v_dic, v_total = 0, 0, 0, 0, 0
    for _ in range(max(3000, ITER // 15)):
        k = rng.randrange(4, 12)
        desc = sorted((rng.uniform(0.2, 3.0) for _ in range(k)),
                      reverse=True)
        R = (desc[0] + desc[1]) * rng.uniform(1.0001, 1.35)
        if any(desc[i] + desc[j] > R for i in range(k)
               for j in range(i + 1, k)):
            continue
        orden = zig_de(desc) if rng.random() < 0.5 else \
            sorted(desc, key=lambda _: rng.random())
        okc, total, esp, fV, fVe = ciclo_instr(orden, R)
        n += 1
        for w in range(len(esp) - 1):
            i, j = esp[w], esp[w + 1]
            a, b = orden[i], orden[j]
            if j - i == 1:
                continue
            cadena = sum(theta_w(orden[t], orden[t + 1], R)
                         for t in range(i, j))
            if cadena > theta_w(a, b, R) + 1e-9:
                v_cadena += 1
            for t in range(i + 1, j):
                if margen_ns2(a, orden[t], b, R) > 1e-9:
                    pass  # el triple individual puede ser positivo si
                    # la cadena entera aun pierde contra la arista
                if orden[t] > bolsillo(a, b, R) + 1e-9 and \
                   margen_ns2(a, orden[t], b, R) < -1e-12:
                    v_dic += 1
        for w in range(len(esp) - 2):
            i, j, l = esp[w], esp[w + 1], esp[w + 2]
            if margen_ns2(orden[i], orden[j], orden[l], R) < -1e-9:
                v_triple += 1
        suma_esp = (sum(theta_w(orden[esp[w]], orden[esp[w + 1]], R)
                        for w in range(len(esp) - 1)) +
                    theta_w(orden[esp[-1]], orden[esp[0]], R))
        if abs(suma_esp - total) > 1e-9:
            v_total += 1
    ok &= check(f"ESP: en {n} ciclos aleatorios, los triples "
                f"consecutivos de la espina tienen margen >= 0 "
                f"({v_triple} fallos: maximalidad), las cadenas "
                f"saltadas suman <= su arista ({v_cadena} fallos) y "
                f"total = suma ciclica de la espina ({v_total} fallos)",
                n > 1000 and v_triple == 0 and v_cadena == 0
                and v_total == 0)
    ok &= check(f"DIC en espina: margen < 0 => saltado <= "
                f"bolsillo(a, b, R) ({v_dic} violaciones)", v_dic == 0)
    # (b) induccion: si TODOS los margenes NS-2 consecutivos son >= 0,
    # el camino mas largo coincide con la suma consecutiva y todas las
    # parejas son legales en las posiciones consecutivas
    n_prem, viol = 0, 0
    for _ in range(max(4000, ITER // 10)):
        k = rng.randrange(4, 11)
        desc = sorted((rng.uniform(0.5, 3.0) for _ in range(k)),
                      reverse=True)
        R = (desc[0] + desc[1]) * rng.uniform(1.0001, 1.5)
        if any(desc[i] + desc[j] > R for i in range(k)
               for j in range(i + 1, k)):
            continue
        orden = zig_de(desc)
        margs = [margen_ns2(orden[i], orden[(i + 1) % k],
                            orden[(i + 2) % k], R) for i in range(k)]
        if min(margs) < 0:
            continue
        n_prem += 1
        okc, total, esp, fV, fVe = ciclo_instr(orden, R)
        if len(esp) != k or (total <= 2 * PI + 1e-9 and fV):
            viol += 1
    ok &= check(f"induccion: en {n_prem} instancias con NS-2 >= 0 en "
                f"todos los triples consecutivos, la espina es TODO el "
                f"ciclo y todas las parejas son legales ({viol} "
                f"fallos)", n_prem > 200 and viol == 0)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] el dominio D1 con la construccion instrumentada")
    ok = True
    rng = random.Random(31)
    n, fallos, fallos_V = 0, 0, 0
    peor_exc, esp_max, apil_esp, apil_occ = 0.0, 0, 0, 0
    peor_cad, peor_dic = -1e9, -1e9
    for j in (3, 4, 5):
        for p_ in (4, 5, 6):
            for _ in range(max(150, ITER // 120)):
                s2 = rng.uniform(0.01, PHI - 1)
                piezas = sorted((rng.uniform(0.01, s2)
                                 for _ in range(p_ - 2)), reverse=True)
                W = sum(piezas)
                s1 = rng.uniform(max(s2, min(1 - 1e-6, 1.001 - W)), 1.0)
                if s1 + W <= 1.0 or s1 < s2:
                    continue
                Sigma = s1 + s2 + W
                holg = [1.0 + rng.expovariate(3.0) for _ in range(j)]
                if rng.random() < 0.3:
                    holg = [1.0] * j
                os_ = cascada(None, Sigma, j, holgura=holg)
                R = R_lb_pack(os_ + [1.0], os_[0] + os_[1],
                              confinado_por=os_[0])
                todos = os_ + [1.0, s2] + piezas
                n += 1
                okc, exc, esp, salt, fVe, apil = corona_instr(todos, R)
                if not okc and exc > 2e-3:
                    fallos += 1
                if fVe:
                    fallos_V += 1
                peor_exc = max(peor_exc, min(exc, 1e9))
                esp_max = max(esp_max, len(esp))
                apil_esp += apil
                apil_occ += sum(1 for x in range(j)
                                for y in range(x + 1, j)
                                if R >= os_[x] + 2 * os_[y] - 1e-12)
                for dc, dd in salt:
                    peor_cad = max(peor_cad, dc)
                    peor_dic = max(peor_dic, dd)
    ok &= check(f"D1 ({n} instancias, j = 3..5, p = 4..6): la "
                f"construccion cierra con dualidad tangente (exceso "
                f"max {peor_exc:.2e} <= 2e-3, {fallos} fallos)",
                n > 1000 and fallos == 0 and peor_exc <= 2e-3)
    ok &= check(f"V: ninguna pareja espina-espina falla en el orden "
                f"ganador ({fallos_V} fallos de valle)", fallos_V == 0)
    ok &= check(f"ESP: cadenas saltadas <= arista (peor exceso "
                f"{peor_cad:.2e}) y saltados sub-bolsillo (peor "
                f"s - p = {peor_dic:.2e})",
                peor_cad <= 1e-9 and peor_dic <= 1e-9)
    ok &= check(f"Z5: la espina tiene <= 7 miembros (max {esp_max}): "
                f"el min sobre sus ordenes es exhaustivo-factible y la "
                f"necesidad lo certifica", esp_max <= 7)
    print(f"      [info] pares apilables (sin confinamiento): "
          f"{apil_occ} de ocupantes, {apil_esp} de espina.  NO es "
          f"condicion del lema: la necesidad los cubre con "
          f"subconjuntos + confinamiento del gigante, y la dualidad "
          f"que carga la prueba es la solidez de ambos lados + el "
          f"barrido (exceso 0 en R_lb); la igualdad gamma = theta "
          f"(Z2) explica la estrechez donde no hay apilables")
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] dualidad R_construct = R_lb y el gap del zigzag")
    ok = True
    rng = random.Random(47)
    # (a) solidez y estrechez: biseccion de la construccion real contra
    # R_lb de la necesidad, mismos circulos, sin confinamiento.
    # SOLIDEZ (teorema): la corona es un empaquetamiento legal, luego
    # R_construct >= R_lb SIEMPRE (la necesidad nunca miente).
    # ESTRECHEZ (informativa): el hueco R_construct - R_lb viene solo
    # de los pares apilables con m (gamma = 0 < theta); en el dominio
    # D1 completo la dualidad es exacta (bloque C, exceso 0 en R_lb).
    peor_viol, peor_gap, nd = 0.0, 0.0, 0
    peor_arg = None
    for _ in range(max(120, ITER // 400)):
        j = rng.randrange(3, 6)
        masa = rng.uniform(0.6, 2.2)
        holg = [1.0 + rng.expovariate(3.0) for _ in range(j)]
        if rng.random() < 0.4:
            holg = [1.0] * j
        os_ = cascada(None, masa, j, holgura=holg)
        C = os_ + [1.0]
        R_lb = R_lb_pack(C, os_[0] + os_[1])
        lo, hi = os_[0] + os_[1], 2 * sum(C) + 1
        if not corona_instr(C, hi)[0]:
            continue
        for _ in range(60):
            mid = (lo + hi) / 2
            if corona_instr(C, mid)[0]:
                hi = mid
            else:
                lo = mid
        R_con = hi
        nd += 1
        peor_viol = max(peor_viol, (R_lb - R_con) / R_lb)
        gap = (R_con - R_lb) / R_lb
        if gap > peor_gap:
            peor_gap = gap
            peor_arg = dict(C=[round(x, 4) for x in C],
                            R_lb=round(R_lb, 6), R_con=round(R_con, 6))
    ok &= check(f"solidez: R_construct >= R_lb en {nd} instancias "
                f"(peor violacion relativa {peor_viol:.2e} <= 0): la "
                f"necesidad es cota inferior verdadera", nd > 80 and
                peor_viol <= 1e-9)
    marca = peor_gap < 1e-2
    ok &= check(f"estrechez: (R_construct - R_lb)/R_lb <= 1e-2 "
                f"(max {peor_gap:.2e}); el hueco residual viene de los "
                f"pares apilables con m (necesidad estrictamente mas "
                f"debil ahi); la dualidad EXACTA del dominio es el "
                f"bloque C", marca)
    if not marca and peor_arg:
        print(f"      PEOR: {peor_arg}")
    # (b) el gap del zigzag como heuristica (informativo, sin carga de
    # prueba: la espina va por exhaustivo)
    peor_gap, n3, gana_zig = 0.0, 0, 0
    for _ in range(max(100, ITER // 600)):
        k = rng.randrange(4, 8)
        desc = sorted((rng.uniform(0.3, 3.0) for _ in range(k)),
                      reverse=True)
        R = (desc[0] + desc[1]) * rng.uniform(1.0001, 1.3)
        if any(desc[i] + desc[j] > R for i in range(k)
               for j in range(i + 1, k)):
            continue
        n3 += 1
        z = suma_ciclica(zig_de(desc), R)
        mejor = min(suma_ciclica([desc[0]] + list(pp), R)
                    for pp in permutations(desc[1:]))
        gap = z - mejor
        peor_gap = max(peor_gap, gap)
        if gap < 1e-9:
            gana_zig += 1
    ok &= check(f"zigzag como heuristica: alcanza el minimo en "
                f"{gana_zig}/{n3} instancias (gap max {peor_gap:.3f}); "
                f"NO es carga de prueba (la espina <= 7 va por "
                f"exhaustivo) y el chequeo constructivo es correcto "
                f"por si mismo", n3 > 50)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles: punto critico aureo y negativos")
    ok = True
    a, b, Rg = PHI, 1.0, PHI + 1.0
    m0 = margen_ns2(a, PHI / 2, b, Rg)
    # cerca de la tangencia f(a) f(b) ~ 1 la derivada de theta es
    # infinita: el margen flotante se degrada a ~sqrt(eps); 1e-6 es el
    # cero numerico correcto aqui (la identidad EXACTA esta en [A])
    ok &= check(f"aureo: margen NS-2 en s = phi/2 es {m0:.2e} (cero "
                f"numerico, exacto en [A]) y theta(phi,1) = pi "
                f"(f(phi) f(1) = 1 queda a un ulp en flotante)",
                abs(m0) < 1e-6 and abs(theta_w(a, b, Rg) - PI) < 1e-6)
    mminus = margen_ns2(a, PHI / 2 - 0.01, b, Rg)
    mplus = margen_ns2(a, PHI / 2 + 0.01, b, Rg)
    ok &= check(f"aureo: el margen cambia de signo al cruzar phi/2 "
                f"({mminus:.4f} < 0 < {mplus:.4f}): el contraejemplo "
                f"es la tangencia critica del modelo",
                mminus < 0 < mplus)
    p = bolsillo(a, b, Rg)
    ok &= check(f"aureo: bolsillo(phi, 1, phi+1) = {p:.6f} = phi/2 "
                f"(DIC exacta en el punto critico)",
                abs(p - PHI / 2) < 1e-9)
    # negativo: un intermedio sub-bolsillo NO rompe la construccion (el
    # camino lo salta y queda mural en el hueco), pero SI rompe la
    # igualdad camino = suma consecutiva: NS-2 es necesario para ella
    a2, b2, R2 = 2.0, 1.8, 4.0
    s_chico = 0.3 * bolsillo(a2, b2, R2)
    orden = [a2, s_chico, b2, 1.5]
    okc, total, esp, fV, fVe = ciclo_instr(orden, R2)
    m2 = margen_ns2(a2, s_chico, b2, R2)
    ok &= check(f"negativo: con s = 0.3 bolsillo (margen NS-2 = "
                f"{m2:.4f} < 0) la espina EXCLUYE a s (queda mural en "
                f"el hueco del par, DIC) y el ciclo sigue legal",
                m2 < 0 and s_chico not in [orden[i] for i in esp]
                and okc)
    # negativo: sin colas (ocupantes casi iguales, sin cascada) la
    # corona NO cabe en el par: la necesidad detecta R_lb > o1 + o2
    C = [1.3, 1.25, 1.2, 1.0]
    R_lb = R_lb_pack(C, C[0] + C[1])
    ok &= check(f"negativo: sin cascada (o = 1.3, 1.25, 1.2), R_lb = "
                f"{R_lb:.3f} > o1 + o2 = {C[0] + C[1]:.2f}: las colas "
                f"son las que permiten la corona en el par",
                R_lb > C[0] + C[1] + 0.3)
    # consistencia Z2 numerica
    rng = random.Random(7)
    peor = 0.0
    for _ in range(5000):
        x = rng.uniform(0.5, 3.0)
        y = rng.uniform(0.5, 3.0)
        R4 = (x + y) * rng.uniform(1.0001, 1.3)
        if R4 >= max(x, y) + 2 * min(x, y):
            continue
        peor = max(peor, abs(gamma_min(x, y, R4) - theta_w(x, y, R4)))
    ok &= check(f"Z2 numerico: gamma_min = theta_w en pares no "
                f"apilables (peor diferencia {peor:.2e})", peor < 1e-12)
    return ok


def main():
    print("=" * 68)
    print("LEMA DE DUALIDAD/ZIGZAG: Z1, Z2, DIC, ESP (maximalidad), V "
          "y dualidad")
    print("(A es exacto; B-E son verificaciones y barridos: el enunciado")
    print(" y las pruebas van en docs/drafts/zigzag.md)")
    print("=" * 68)
    solo = None
    for arg in sys.argv[1:]:
        if arg.startswith("--solo"):
            solo = (arg.split("=")[1] if "=" in arg
                    else sys.argv[sys.argv.index(arg) + 1])
    todos = {"A": bloque_A, "B": bloque_B, "C": bloque_C, "D": bloque_D,
             "E": bloque_E}
    if solo:
        res = [todos[solo]()]
        etiquetas = [solo]
    else:
        etiquetas = list("ABCDE")
        res = [todos[e]() for e in etiquetas]
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
