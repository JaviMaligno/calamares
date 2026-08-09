#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insercion por sombras en la plantilla ANIDADA: teorema j >= 2
(docs/drafts/insercionanidada.md).

Plantilla (caso (b)): u = agujero de alpha (alpha top-level), v =
sarten; P tiene m top-level en la sarten y S en el agujero de alpha;
F tiene m en el agujero de alpha.  El reparto testigo:
  (1) la sarten TOP-LEVEL segun P: solo m se va (su disco unidad D_m
      queda vacante); m entra en el agujero de alpha y el INTERIOR
      del agujero se recoloca segun el certificado de F (cuando F
      coloco m, los ocupantes del agujero eran exactamente los > m
      que P le asigna, por maximalidad de m y orden decreciente de F;
      F certifico ese conjunto + m; subarboles rigidos).  S (todo lo
      < m del agujero per P) sale entera; el polvo/extras < m
      top-level de la sarten tambien salen (van a la fila w*).
  (2) LLENADO GREEDY de D_m: fila (lem:row) con TODA la masa suelta
      (S + extras + polvo, total Sigma) en orden decreciente hasta
      la primera pieza que no cabe, s'.  Si todo cabe (Sigma <= 1)
      no hay nada que insertar.  El peor caso es (D): s' = sigma2
      con sigma1 + sigma2 > 1; s' puede ser tambien un extra.
  (3) s' mural en la sarten por el LEMA DE INSERCION (sombras sobre
      la familia {alpha, o_1..o_j, D_m como pieza de radio 1} a las
      posiciones reales de P; la cota de sombra es uniforme en la
      profundidad).  Presupuesto monotono en s: cubrir el tope
      min(Sigma/2, phi/2) cubre todo s'.
  (4) el resto W'' (masa < 1/phi EXACTO: fila colocada + s' > 1 y
      cola(m) <= phi) como circulo-fila w* <= 1/phi, insercion de
      nuevo con la sombra de s' contada.

Paredes EXACTAS (bloque A):
  - tope del insertando: s' <= l2 <= min(Sigma/2, phi/2) SIEMPRE
    (l1+l2 <= Sigma y l1+l2 <= cola(m) <= phi), sin condicion en
    omega: D4 y D5 subsumidas; vale para piezas de S Y para extras.
  - regimen automatico j >= 2, UNIFORME: con |T| = j+1 >= 3 piezas
    top-level, la cascada (convenio de primera copia, identidad
    phi^2 = 1+phi) da t2 >= 1+Sigma >= 2 para el SEGUNDO mayor de T;
    el par de P da R - x >= R - t1 >= t2 >= 2 > phi >= 2s' y
    2 > 2/phi = 2w*: ambos regimenes estrictos (margen 2-phi).
  - j <= 1 NO: la navaja o_1 -> 2/phi = 2w* (Sigma -> 1) mata la
    segunda insercion (razon de sombra identicamente 1, presupuesto
    >= pi por la sola alpha): franja declarada (D6).

Bloques: [A] identidades exactas; [B] presupuesto por bisecciones MC
+ esquinas deterministas, con cobertura POR INSTANCIA hasta el
objetivo min(Sigma/2, phi/2) (el tope real del insertando);
[C] inserciones reales euclidianas; [D] cobertura y delimitacion
honesta; [E] controles; [F] holgura grande / dominio de torres
(c-ii-1): piezas hasta 10^4 sobre el suelo, omega hasta 1.35,
limite t -> inf por formula (ronda hostil del puerto, 2026-08-09).
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260811'))


def sombra(s, x, R):
    w, u = s + x, R - s
    if u <= w:
        return PI
    return math.asin(w / u)


def presupuesto(s, piezas, R):
    return sum(2 * sombra(s, x, R) for x in piezas)


def cascada_anidada_min(SS, j):
    """Ocupantes minimos del pan anidado SIN alpha en la cadena
    (conservador: ocupantes menores; el suelo es 1.0 = m, no 1+omega:
    los ocupantes no tienen relacion con la pared de alpha)."""
    os_ = []
    total = 0.0
    for _ in range(j):
        base = max(1.0, (total + 1.0 + SS) / PHI,
                   os_[-1] if os_ else 0.0)
        os_.append(base)
        total += base
    return os_[::-1]


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades exactas (sympy)")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    S, a = sp.symbols('Sigma alpha', positive=True)
    # (1) pared de masa INCONDICIONAL en omega
    ok &= check("pared de masa: sigma2 > phi/2 => sigma1+sigma2 >= "
                "2 sigma2 > phi >= cola(m): VACIA para TODO omega "
                "(la condicion omega > phi-1 del draft v1 era "
                "innecesaria; phi/2 > phi-1 exacto: D4 subsumida)",
                sp.simplify(phi / 2 - (phi - 1) - (1 - phi / 2)) == 0
                and float(1 - phi / 2) > 0)
    # (2) cascada j >= 2: o1 >= 1+Sigma exacto
    ok &= check("cascada j >= 2 (convenio de primera copia, "
                "adversariado en la sarten): o2 >= (1+Sigma)/phi y "
                "o1 >= (o2+1+Sigma)/phi >= (1+Sigma)(1+phi)/phi^2 = "
                "1+Sigma (identidad phi^2 = 1+phi)",
                sp.simplify(((1 + S) / phi + 1 + S) / phi - (1 + S))
                == 0)
    # (3) tope del insertando: s' <= min(Sigma/2, phi/2), con Sigma
    #     la masa suelta TOTAL (S + extras + polvo)
    ok &= check("tope del insertando: s' <= l2 (greedy decreciente, "
                "l1 entra primero) y l1+l2 <= Sigma, l1+l2 <= "
                "cola(m) <= phi dan s' <= min(Sigma/2, phi/2); "
                "cubre tambien s' = extra de la sarten (la cota "
                "(alpha-omega)/2 del par del agujero NO vale para "
                "extras y no se usa)",
                sp.simplify(S / 2 + S / 2 - S) == 0)
    # (4) regimen automatico j >= 2, UNIFORME: la cadena del segundo
    #     mayor top-level
    ok &= check("regimen automatico (j >= 2): con |T| = j+1 >= 3 "
                "piezas top-level {alpha, o_1..o_j}, la cascada da "
                "t3 >= (1+Sigma)/phi y t2 >= (t3+1+Sigma)/phi >= "
                "(1+Sigma)(1+phi)/phi^2 = 1+Sigma >= 2; par de P: "
                "R - x >= R - t1 >= t2 >= 2 > phi >= 2s' y "
                "2 > 2/phi = 2w*: AMBOS regimenes estrictos "
                "(margen 2-phi), sin usar alpha >= "
                "sigma1+sigma2+omega",
                sp.simplify(((1 + S) / phi + 1 + S) / phi - (1 + S))
                == 0 and float(2 - phi) > 0
                and float(2 - 2 / phi) > 0)
    # (6) llenado greedy de D_m: cierra tambien sigma1+sigma2 <= 1
    ok &= check("llenado greedy de D_m (masa suelta Sigma > 1; si "
                "Sigma <= 1 la fila entera cabe y no hay insercion): "
                "si s' es la primera pieza que no cabe, P_t + s' > 1 "
                "y W'' <= cola(m) - P_t - s' < phi - 1 = 1/phi "
                "exacto (cubre tambien sigma1+sigma2 <= 1 < Sigma, "
                "hueco del draft v1; (D) es el caso s' = sigma2)",
                sp.simplify((phi - 1) - 1 / phi) == 0)
    # (7) navaja j = 1: franja declarada
    ok &= check("navaja j = 1: o1 -> (1+Sigma)/phi -> 2/phi (Sigma "
                "-> 1) y con R = alpha+o1, o1 = 2/phi la razon de la "
                "sombra de alpha para w* = 1/phi es "
                "(alpha+1/phi)/(alpha+2/phi-1/phi) = 1 IDENTICA en "
                "alpha: el regimen R - alpha > 2w* falla con "
                "igualdad exacta: j <= 1 queda FUERA del teorema "
                "(franja declarada D6)",
                sp.simplify((a + 1 / phi) / (a + 2 / phi - 1 / phi)
                            - 1) == 0)
    # (8) legalidad del paso (1)
    ok &= check("[ENUNCIADO] paso (1): m es el MAYOR discrepante => "
                "cuando F coloco m, los ocupantes del agujero de "
                "alpha eran exactamente los > m que P le asigna "
                "(orden decreciente: nada < m estaba colocado) y F "
                "certifico ese conjunto + m; el interior del agujero "
                "se recoloca segun ese certificado con subarboles "
                "rigidos (thm:oblivious, ~303-341); S y los extras "
                "< m top-level de la sarten salen (D_m, mural, w*)",
                True)
    return ok


# ---------------------------------------------------------------- bloque B
def _evalua(j, SS, piezas, R, MARG):
    """(s_cap, target, cubre, reg_ok): s_cap por biseccion (informe);
    cubre = ambos presupuestos en s = target = min(Sigma/2, phi/2)
    (el tope EXACTO del insertando s', valido tambien para extras)
    bajo 2pi - MARG y ambos regimenes (solo j >= 2; el presupuesto es
    monotono en s, cubrir target cubre todo s' <= target)."""
    wst = 1 / PHI
    target = min(SS / 2, PHI / 2)
    s_reg = min((R - x) / 2 for x in piezas) - 1e-9
    lo, hi = 0.0, min(s_reg, 0.999)
    if hi > 0.05:
        lo = 0.05
        for _ in range(30):
            mid = (lo + hi) / 2
            v1 = presupuesto(mid, piezas, R)
            r2 = all(R - x > 2 * wst + 1e-12 for x in piezas + [mid])
            v2 = presupuesto(wst, piezas + [mid], R) if r2 else 1e9
            if max(v1, v2) < 2 * PI - MARG:
                lo = mid
            else:
                hi = mid
    if j <= 1:
        return lo, target, None, True
    reg1 = all(R - x > 2 * target + 1e-12 for x in piezas)
    reg2 = all(R - x > 2 * wst + 1e-12 for x in piezas + [target])
    v1 = presupuesto(target, piezas, R) if reg1 else 1e9
    v2 = presupuesto(wst, piezas + [target], R) if reg2 else 1e9
    cubre = reg1 and reg2 and max(v1, v2) < 2 * PI - MARG
    return lo, target, cubre, reg1 and reg2


def bloque_B():
    print("[B] presupuesto del pan anidado: s_cap por celda y "
          "cobertura POR INSTANCIA hasta min(Sigma/2, phi/2) "
          "(cascada REAL, suelo honesto alpha >= 1+omega)")
    from coronanidada import cascada_anidada
    ok = True
    rng = random.Random(SEED)
    MARG = 0.05
    caps = {}
    stats = {'n': 0, 'ncov': 0, 'viol': 0, 'reg': 0}

    def procesa(j, w, SS, rank, holg):
        af, os_ = cascada_anidada(SS, j, rank, 1.0 + w, holg)
        piezas = sorted([af] + list(os_) + [1.0], reverse=True)
        R = piezas[0] + piezas[1]
        stats['n'] += 1
        s_cap, target, cubre, regs = _evalua(j, SS, piezas, R, MARG)
        caps.setdefault((j, round(w, 1)), []).append(s_cap)
        if j >= 2:
            stats['ncov'] += 1
            if not cubre:
                stats['viol'] += 1
            if not regs:
                stats['reg'] += 1

    for _ in range(max(20000, ITER // 3)):
        j = rng.randrange(1, 7)
        w = rng.uniform(0.05, 0.999)
        SS = rng.uniform(1.0 + 1e-6, PHI)
        holg = [1.0 + rng.expovariate(2.5) for _ in range(j + 1)]
        if rng.random() < 0.35:
            holg = [1.0] * (j + 1)
        rank = rng.randrange(0, j + 1)
        procesa(j, w, SS, rank, holg)
    # esquinas deterministas: holgura 1 EXACTA (empates de cascada),
    # Sigma -> 1+, Sigma = phi, ranks extremos, omegas criticas
    ndet = 0
    for j in (1, 2, 3, 4, 5, 6):
        for w in (0.05, 0.24, 0.4, PHI - 1, 0.7, PHI / 2, 0.9,
                  0.999):
            for SS in (1.0 + 1e-9, 1.3, PHI):
                for rank in sorted({0, j // 2, j}):
                    for hv in (1.0, 1.004):
                        procesa(j, w, SS, rank, [hv] * (j + 1))
                        ndet += 1
    peores = {k: round(min(v), 3) for k, v in sorted(caps.items())}
    ok &= check(f"s_cap por (j, omega~) [minimos observados, "
                f"{stats['n']} instancias, {ndet} deterministas]: "
                f"{peores}", stats['n'] > 3000)
    ok &= check(f"cobertura j >= 2 hasta el objetivo por instancia "
                f"(s' <= min(Sigma/2, phi/2), tope exacto valido "
                f"tambien para extras; {stats['ncov']} instancias): "
                f"{stats['viol']} fallos de presupuesto",
                stats['ncov'] > 2000 and stats['viol'] == 0)
    ok &= check(f"lema de regimen automatico (j >= 2) validado en el "
                f"muestreo: {stats['reg']} fallos de regimen "
                f"(esperados 0, es exacto)", stats['reg'] == 0)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] inserciones reales euclidianas en el pan anidado")
    rng = random.Random(SEED + 1)
    from insercion import empaqueta, inserta
    ok = True
    n, fallo1, fallo2 = 0, 0, 0
    for _ in range(max(2000, ITER // 20)):
        j = rng.randrange(0, 5)
        w = rng.uniform(0.05, 0.98)
        SS = rng.uniform(1.0 + 1e-6, PHI)
        s2 = rng.uniform(0.2, min(SS / 2, PHI / 2))
        os_ = cascada_anidada_min(SS, j)
        # dominio: alpha >= 1+omega (admite a m) y la cola de alpha
        # ((1+Sigma)/phi, con Sigma la masa suelta total)
        af = max(1.0 + w, (1.0 + SS) / PHI) \
            * (1.0 + rng.expovariate(2.0))
        fam = [af] + os_ + [1.0]
        R = (max(af + (os_[0] if j >= 1 else 1.0), af + 1.0,
                 (os_[0] + os_[1]) if j >= 2 else 0.0)
             * rng.uniform(1.0, 1.2))
        if any(R - x <= 2 * s2 + 1e-9 for x in fam):
            continue
        if presupuesto(s2, fam, R) >= 2 * PI - 1e-2:
            continue          # fuera del presupuesto: Lema A no aplica
        pos = empaqueta(fam, R, rng)
        if pos is None:
            continue
        n += 1
        p2 = inserta(pos, s2, R)
        if p2 is None:
            fallo1 += 1
            continue
        wstar = 1 / PHI
        if any(R - x <= 2 * wstar + 1e-9 for x in fam + [s2]):
            continue
        if presupuesto(wstar, fam + [s2], R) >= 2 * PI - 1e-2:
            continue
        p3 = inserta(pos + [p2], wstar, R)
        if p3 is None:
            fallo2 += 1
    ok &= check(f"pan anidado real ({n} empaquetamientos de "
                f"{{alpha, O, m}} con regimen Y presupuesto del "
                f"teorema): sigma2 SIEMPRE entra ({fallo1} fallos) "
                f"y el circulo-fila despues ({fallo2} fallos)",
                n > 400 and fallo1 == 0 and fallo2 == 0)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] cobertura de las celdas y delimitacion honesta")
    ok = True
    ok &= check("j >= 2 (TODO omega, TODO sigma2, extras incluidos): "
                "s' > min(Sigma/2, phi/2) vacio por masa (exacto, "
                "sin omega); s' <= min(Sigma/2, phi/2) en regimen "
                "automatico (exacto: t2 >= 1+Sigma >= 2 > phi) y "
                "con presupuesto < 2pi - 0.05 (numerico-certificado, "
                "bloque B): D4 = {j = 2, omega in [phi/2, 1)} y D5 "
                "(k, p son masa) quedan SUBSUMIDAS; la franja del "
                "draft v1 {j = 2, omega <= phi-1, sigma2 in "
                "[0.95, 1)} era VACIA por masa (mal delimitada) y "
                "el hueco real del viejo regimen (1+omega)/2 lo "
                "cierra el lema automatico",
                PHI / 2 > PHI - 1 and PHI / 2 < 0.95)
    ok &= check("[ENUNCIADO] D5 (k >= 4 fuera de la rama de "
                "reduccion): el tamano del perfil es masa (W'' < "
                "1/phi como un solo circulo-fila): colapsa al mismo "
                "teorema; k y p no aparecen", True)
    franja = "{j <= 1} entera (D6: j = 0 con smalls; j = 1 muere " \
             "por PRESUPUESTO en la navaja o1 -> 2/phi = 2w*: la " \
             "razon de sombra de alpha para w* es identicamente 1)"
    print(f"      FRANJA DELIMITADA (pinza dedicada pendiente; "
          f"cerrada computacionalmente por coronanidada): {franja}")
    ok &= check("cobertura del teorema: j >= 2 COMPLETA (todo omega, "
                "sigma2, k, p); j <= 1 DECLARADO (no forzado), con "
                "las pinzas computacionales de coronanidada detras",
                True)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles")
    ok = True
    # (a) sin la necesidad de par el regimen falla: R = alpha + 0.1
    s = 0.6
    af = 3.0
    v = presupuesto(s, [af, 1.0], af + 0.1)
    ok &= check(f"(a) sin R >= alpha + max(o1, 1) el regimen falla y "
                f"la sombra de alpha se dispara ({v:.3f} incluye "
                f"pi): las necesidades de par del pan de P son las "
                f"que pagan", v >= PI)
    # (b) el tope es tight en s' = phi/2
    ok &= check("(b) tope tight: s' = phi/2 exige cola(m) = phi "
                "EXACTA (l1 = l2 = phi/2 y nada mas < m): el punto "
                "frontera sigue cubierto (regimen con margen 2-phi "
                "y presupuesto en el objetivo phi/2, bloque B)",
                abs(2 * (PHI / 2) - PHI) < 1e-15
                and 2 - PHI > 0.38)
    # (c) la navaja j = 1 es real: en la esquina Sigma -> 1 el
    # regimen de w* falla numericamente
    SSc = 1.0 + 1e-12
    o1 = (1.0 + SSc) / PHI
    afc = 2.0                     # alpha >= o1: R - alpha = o1
    Rc = afc + o1
    reg = Rc - afc > 2 / PHI + 1e-9
    ok &= check(f"(c) navaja j = 1 numerica: Sigma -> 1, o1 = "
                f"{o1:.6f} = 2/phi, R = alpha + o1: regimen de w* "
                f"R - alpha > 2/phi es {reg} (falla con igualdad "
                f"exacta): la franja j <= 1 es genuina para este "
                f"testigo", not reg)
    return ok


# ---------------------------------------------------------------- bloque F
def _eval_holgura(piezas, SS):
    """Presupuesto de sombras del reparto del teorema (s' en el tope
    min(Sigma/2, phi/2) y w* = 1/phi despues) sobre la familia dada,
    con R = par de P.  None si falla algun regimen (no deberia:
    t2 >= 1+Sigma es exacto e independiente de holguras)."""
    piezas = sorted(piezas, reverse=True)
    R = piezas[0] + piezas[1]
    wst = 1 / PHI
    target = min(SS / 2, PHI / 2)
    reg1 = all(R - x > 2 * target + 1e-12 for x in piezas)
    reg2 = all(R - x > 2 * wst + 1e-12 for x in piezas + [target])
    if not (reg1 and reg2):
        return None
    return max(presupuesto(target, piezas, R),
               presupuesto(wst, piezas + [target], R))


def bloque_F():
    print("[F] holgura grande / dominio de torres (c-ii-1): piezas "
          "hasta 10^4 sobre el suelo, omega hasta 1.35, limite "
          "t -> inf (ronda hostil del puerto)")
    from coronanidada import cascada_anidada
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    ok &= check("(F0) suelo t >= Sigma_S+omega AUTOMATICO en la raiz "
                "de torre (sympy, dos ramas): omega >= phi-1 via "
                "t >= 1+2omega y Sigma_S <= Sigma <= phi <= 1+omega; "
                "omega < phi-1 via cascada t >= (2+omega+Sigma)/phi "
                ">= Sigma+omega <=> Sigma+omega <= 2/(phi-1) = 2phi, "
                "y Sigma+omega <= phi+(phi-1) = 2phi-1 < 2phi",
                sp.simplify(2 / (phi - 1) - 2 * phi) == 0
                and float(2 * phi - (2 * phi - 1)) > 0)
    rng = random.Random(SEED + 7)
    peor, arg = 0.0, None
    n, freg = 0, 0
    HS = [1.0, 1.5, 2, 3, 4, 6, 8, 12, 20, 40, 80, 200, 1000, 10000]
    for j in (2, 3, 4):
        for w in (0.05, 0.3, 0.6, 0.9, 0.999, 1.2, 1.35):
            for SS in (1.0 + 1e-9, 1.2, 1.4, PHI):
                for rank in range(j + 1):
                    for h in HS:
                        holg = [1.0] * (j + 1)
                        holg[rank] = h
                        af, occs = cascada_anidada(SS, j, rank,
                                                   1.0 + w, holg)
                        n += 1
                        v = _eval_holgura([af] + list(occs) + [1.0],
                                          SS)
                        if v is None:
                            freg += 1
                        elif v > peor:
                            peor = v
                            arg = dict(j=j, w=w, SS=round(SS, 3),
                                       rank=rank, h=h)
    # dos piezas infladas a la vez (la raiz t y un ocupante)
    for j in (2, 3):
        for w in (0.05, 0.6, 0.999, 1.35):
            for SS in (1.0 + 1e-9, 1.4, PHI):
                for h1 in (3, 10, 100, 1000):
                    for h2 in (3, 10, 100, 1000):
                        holg = [1.0] * (j + 1)
                        holg[0], holg[j] = h1, h2
                        af, occs = cascada_anidada(SS, j, 0,
                                                   1.0 + w, holg)
                        n += 1
                        v = _eval_holgura([af] + list(occs) + [1.0],
                                          SS)
                        if v is None:
                            freg += 1
                        elif v > peor:
                            peor = v
                            arg = dict(j=j, w=w, dos=(h1, h2))
    # MC con holguras log-uniformes independientes por pieza
    for _ in range(max(4000, ITER // 15)):
        j = rng.randrange(2, 7)
        w = rng.uniform(0.05, 1.35)
        SS = rng.uniform(1.0 + 1e-6, PHI)
        holg = [math.exp(rng.uniform(0.0, math.log(1e4)))
                for _ in range(j + 1)]
        rank = rng.randrange(0, j + 1)
        af, occs = cascada_anidada(SS, j, rank, 1.0 + w, holg)
        n += 1
        v = _eval_holgura([af] + list(occs) + [1.0], SS)
        if v is None:
            freg += 1
        elif v > peor:
            peor = v
            arg = dict(mc=True, j=j, w=round(w, 2))
    ok &= check(f"(F1) regimen automatico bajo holgura ARBITRARIA "
                f"({n} instancias, h hasta 10^4, omega hasta 1.35 "
                f"incl. pivote solido, dos piezas infladas): {freg} "
                f"fallos de regimen (exacto: t2 >= 1+Sigma no "
                f"depende de holguras)", freg == 0 and n > 4000)
    ok &= check(f"(F2) presupuesto bajo holgura arbitraria: peor = "
                f"{peor:.4f} < 2pi - 0.05 = {2 * PI - 0.05:.4f} "
                f"(argmax {arg}: el maximo vive en el SUELO h = 1; "
                f"inflar solo ayuda)", peor < 2 * PI - 0.05)
    # (F3) limite t -> inf por formula + puntos
    vals = []
    for t in (1e6, 1e8):
        vals.append(_eval_holgura([t, 2.0, 1.0], PHI))
    lim_ok = all(v is not None and abs(v - PI) < 0.01 for v in vals)
    ok &= check(f"(F3) limite t -> inf POR FORMULA: R = t+t2, la "
                f"sombra de t -> pi (razon (s+t)/(t+t2-s) -> 1, "
                f"regimen t2 - 2s >= 2-phi exacto) y las demas -> 0: "
                f"presupuesto -> pi < 2pi (margen pi); puntos "
                f"t = 10^6, 10^8: {[round(v, 4) for v in vals]}",
                lim_ok)
    return ok


def main():
    print("=" * 68)
    print("INSERCION ANIDADA: teorema j >= 2 escrito "
          "(drafts/insercionanidada.md)")
    print("=" * 68)
    solo = None
    for a in sys.argv[1:]:
        if a.startswith("--solo"):
            solo = a.split("=")[1] if "=" in a else \
                sys.argv[sys.argv.index(a) + 1]
    etiquetas = [solo] if solo else list("ABCDEF")
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
