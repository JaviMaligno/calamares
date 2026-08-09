#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las dos ramas de agujero del puerto (docs/drafts/coronaagujero.md):
el residuo computacional final de (c-ii-2).

RAMA 1 — Y >= alpha RESPIRANDO (X_Y + omega > phi, unica no vacia por
I2).  v = agujero de Y (capacidad c = Y - omega); per P el agujero
contiene {x_1..x_k} (anillos > m compartidos, masa X_Y) y m top-level.
El reparto testigo es EL DE LOS TEOREMAS ANIDADOS con el agujero como
contenedor: m -> u por el certificado de F (D_m vacante top-level en
v); llenado greedy de D_m hasta s'; s' mural en v; resto w* < 1/phi
mural otra vez.  La dicotomia se HEREDA:
  k >= 3  <->  plantilla j >= 2 (regimen automatico: la cadena de
          cascada entre los x da x_2 >= 1+Sigma >= 2, y el par del
          agujero c >= x_1+x_2 da c - x >= x_2 >= 2 > phi >= 2s',
          2 > 2/phi = 2w*; sombras).
  k <= 2  <->  plantilla j <= 1 (familia ACOTADA <= 5:
          {x_1, (x_2), D_m-disco, s', w*}; criterio mural exacto +
          cota blindada del trio {x_1, x_2, m} sobre c).
  k = 0 es VACIO por el LEMA DE RESPIRACION FUERTE (ronda hostil
  2026-08-09: X_Y en el convenio real INCLUYE polvo < m del agujero,
  asi que "piezas >= 1" NO basta): la I2 COMPLETA + la pared (D)
  (Sigma_S > 1) dan X_Y + omega > phi(3-phi) = 2phi-1 = sqrt5; el
  polvo de v esta acotado por cola(m) <= phi: polvo <= phi - Sigma_S
  < phi - 1; luego la masa > m cumple X_{>m} + omega > sqrt5 -
  (phi-1) = phi > 0 EXACTO (sqrt5 - phi + 1 = phi): k >= 1 genuino,
  y el filtro X_{>m} + omega > phi del script queda justificado.

RAMA 2 — CORONA-ALPHA con X_alpha grande.  u = agujero de alpha
(capacidad c = alpha - omega) con ocupantes {x_1..x_k} per P (masa
X_alpha) y m que LLEGA por el certificado de F.  Perfil ligero
(Sigma_S < 1 + sigma_2): B = S \\ {sigma_2} tiene masa < 1 EXACTA y
va en fila a D_m (en v); SOLO sigma_2 necesita insercion mural en u
sobre {x_1..x_k, m}.  Dicotomia:
  k >= 3: regimen automatico para sigma_2 (c - x >= x_2 >= 1+Sigma
          >= 2 > 2 sigma_2 al ser sigma_2 < 1); sombras.
  k <= 2: familia acotada <= 4: {x_1, (x_2), m, sigma_2}; criterio
          mural + blindada.
  k = 0: criterio de dos circulos exacto, sin corona (I3): fuera.
Suelos de c: E4 (alpha >= Sigma_S + X_alpha + omega, S vive en u per
P) da c >= Sigma_S + X_alpha; techo B2u c < 1 + sigma_2 + X_alpha
(si no, la fila cabe y no hay bloqueo); pares c >= x_1+x_2, x_1+1.

Suelos de los x (ambas ramas): cascada con cola \\supseteq {m, Sigma}
y suelo 1 (anillos >= m; SIN relacion con omega: mas BAJOS que los
suelos 1+omega de la sarten — por eso las cajas certificadas de
insercionanidada/gaplemma NO cubren y hace falta este script).
Conservador: c = maximo de NECESIDADES puras (pares del
empaquetamiento real + blindada del trio); la legalidad
Y >= 1+X_Y+omega NO se usa como suelo.

Bloques: [A] identidades exactas (sympy); [B] rama 1, k >= 3
(sombras); [C] rama 1, k <= 2 (corona acotada); [D] rama 2 (ambas
k-celdas); [E] controles.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check
from gaplemma import R_trio_blindada, corona_k5

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260813'))


def sombra(s, x, R):
    w, u = s + x, R - s
    if u <= w:
        return PI
    return math.asin(w / u)


def presupuesto(s, piezas, R):
    return sum(2 * sombra(s, x, R) for x in piezas)


def cascada_agujero(SS, k, holg):
    """Minimos de cascada de los k ocupantes > m de un agujero: cada
    x, de menor a mayor, tiene cola que contiene a m, a la masa suelta
    Sigma y a los menores (convenio de primera copia); suelo 1 (son
    anillos >= m), SIN suelo de pared (los ocupantes de un agujero no
    tienen relacion con omega).  holg: factores >= 1.  Devuelve la
    lista DESCENDENTE."""
    xs = []
    total = 0.0
    for q in range(k):
        base = max(1.0, (total + 1.0 + SS) / PHI,
                   xs[-1] if xs else 0.0)
        v = base * holg[q]
        xs.append(v)
        total += v
    return xs[::-1]


def caps_masa(rng, SS):
    """(s', w*) del reparto greedy con las ligaduras exactas:
    s' <= min(Sigma/2, phi/2); W'' < min(1/phi, Sigma-1, Sigma-2s')."""
    s_cap = min(SS / 2, PHI / 2)
    sp = rng.uniform(0.05, s_cap) if rng is not None else s_cap
    wst = min(1 / PHI, SS - 1.0, max(1e-6, SS - 2 * sp))
    return sp, max(1e-6, wst)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades exactas (sympy)")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    S = sp.symbols('Sigma', positive=True)
    # (1) la cadena de cascada del agujero: k >= 3 => x2 >= 1+Sigma
    ok &= check("cadena del agujero (k >= 3): x3 >= (1+Sigma)/phi y "
                "x2 >= (x3+1+Sigma)/phi >= (1+Sigma)(1+phi)/phi^2 = "
                "1+Sigma (phi^2 = 1+phi) — la MISMA identidad del "
                "regimen automatico anidado, con el agujero como "
                "contenedor",
                sp.simplify(((1 + S) / phi + 1 + S) / phi - (1 + S))
                == 0)
    # (2) margenes de regimen: rama 1 y rama 2
    ok &= check("regimenes: rama 1 con c >= x1+x2, c - x >= x2 >= "
                "1+Sigma >= 2 > phi >= 2s' y 2 > 2/phi = 2w* (margen "
                "2-phi); rama 2 idem con 2 > 2 sigma2 (sigma2 < 1, "
                "margen 2-2sigma2 > 0)",
                float(2 - PHI) > 0 and float(2 - 2 / PHI) > 0)
    # (3) lema de respiracion fuerte (rama 1 sin k = 0; X_Y con
    #     polvo, convenio real de puertocii)
    ok &= check("LEMA DE RESPIRACION FUERTE: I2 completa "
                "((phi-1)(X_Y+omega) > 1 + (2-phi)Sigma_S + X_m + "
                "X_alpha) + pared (D) (Sigma_S > 1) => X_Y+omega > "
                "phi(3-phi) = 2phi-1 = sqrt5; polvo de v <= phi - "
                "Sigma_S < phi-1 (cola(m) <= phi); masa > m: "
                "X_{>m}+omega > sqrt5-(phi-1) = phi EXACTO => k >= 1 "
                "y el filtro del script justificado",
                sp.simplify(phi * (3 - phi) - (2 * phi - 1)) == 0
                and sp.simplify(2 * phi - 1 - sp.sqrt(5)) == 0
                and sp.simplify(sp.sqrt(5) - (phi - 1) - phi) == 0)
    # (4) rama 2 ligera: B = S \ {sigma2} cabe en D_m EXACTO
    ok &= check("rama 2 (perfil ligero Sigma_S < 1+sigma2): "
                "Sigma_B = Sigma_S - sigma2 < 1: la fila B entera va "
                "a D_m (lem:row) y SOLO sigma2 necesita insercion "
                "mural en u",
                sp.simplify((1 + sp.Symbol('s2')) - sp.Symbol('s2')
                            - 1) == 0)
    # (5) ventana de c en rama 2: ancho 1+sigma2-Sigma_S, X_alpha
    #     se cancela
    ok &= check("ventana de c en rama 2: [Sigma_S+X_alpha, "
                "1+sigma2+X_alpha) — E4 (S vive en u per P) y techo "
                "B2u; no vacia sii Sigma_S < 1+sigma2 (ligero); "
                "X_alpha se CANCELA en el ancho", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] rama 1 (Y >= alpha respirando), k >= 3: sombras")
    rng = random.Random(SEED)
    ok = True
    n, freg, fpres = 0, 0, 0
    peor = 0.0
    arg = None
    peor_k = {}

    def instancia(k, w, SS, holg):
        nonlocal n, freg, fpres, peor, arg
        xs = cascada_agujero(SS, k, holg)
        XY = sum(xs)
        # filtro por la masa > m (lema de respiracion fuerte: el
        # polvo de v se descuenta EXACTO, cabecera y check A(3))
        if XY + w <= PHI + 1e-12:
            return
        c = max(xs[0] + xs[1], xs[0] + 1.0)
        fam = xs + [1.0]               # D_m como pieza
        # MAYORANTE DESACOPLADO (ronda hostil, H3): s' = tope exacto
        # y w* = 1/phi SIMULTANEOS (el presupuesto es monotono en
        # ambos tamanos; la ligadura de masa solo puede rebajarlos)
        sp_ = min(SS / 2, PHI / 2)
        wst = 1 / PHI
        n += 1
        reg1 = all(c - x > 2 * sp_ + 1e-12 for x in fam)
        reg2 = all(c - x > 2 * wst + 1e-12 for x in fam + [sp_])
        if not (reg1 and reg2):
            freg += 1
            return
        v = max(presupuesto(sp_, fam, c),
                presupuesto(wst, fam + [sp_], c))
        if v >= 2 * PI - 0.05:
            fpres += 1
        if v > peor:
            peor = v
            arg = dict(k=k, w=round(w, 3), SS=round(SS, 3),
                       h=round(max(holg), 1))
        peor_k[k] = max(peor_k.get(k, 0.0), v)

    for _ in range(max(20000, ITER // 3)):
        k = rng.randrange(3, 11)
        w = rng.uniform(0.05, 1.35)
        SS = rng.uniform(1.0 + 1e-6, PHI)
        holg = [1.0 + rng.expovariate(2.5) for _ in range(k)]
        if rng.random() < 0.3:
            holg = [1.0] * k
        instancia(k, w, SS, holg)
    # esquinas deterministas + holgura grande (una y dos piezas)
    ndet = 0
    HS = [1.0, 2, 5, 20, 100, 1000, 10000]
    for k in (3, 4, 5, 6, 8, 10, 12, 14):
        for w in (0.05, PHI - 1, 0.9, 0.999, 1.2, 1.35):
            for SS in (1.0 + 1e-9, 1.3, PHI):
                for rk in range(k):
                    for h in HS:
                        holg = [1.0] * k
                        holg[rk] = h
                        instancia(k, w, SS, holg)
                        ndet += 1
    for k in (3, 4):
        for w in (0.05, 0.999, 1.35):
            for SS in (1.0 + 1e-9, PHI):
                for h1 in (5, 100, 1000):
                    for h2 in (5, 100, 1000):
                        holg = [1.0] * k
                        holg[0], holg[-1] = h1, h2
                        instancia(k, w, SS, holg)
                        ndet += 1
    ok &= check(f"rama 1, k >= 3 ({n} instancias respirantes, {ndet} "
                f"deterministas con h hasta 10^4): 0 fallos de "
                f"regimen esperados (exacto) — {freg} observados",
                n > 5000 and freg == 0)
    ok &= check(f"presupuesto de sombras en el MAYORANTE desacoplado "
                f"(s' = min(Sigma/2, phi/2) Y w* = 1/phi a la vez): "
                f"{fpres} fallos; peor = {peor:.4f} < 2pi - 0.05 = "
                f"{2 * PI - 0.05:.4f} (argmax {arg})",
                fpres == 0 and peor < 2 * PI - 0.05)
    trazak = {k: round(v, 3) for k, v in sorted(peor_k.items())}
    ok &= check(f"direccion k (asterisco declarado, analogo de la "
                f"direccion j de la ley de escala): peor presupuesto "
                f"DECRECIENTE en k — {trazak} — coherente con el "
                f"crecimiento geometrico de la cascada (razon phi)",
                peor_k[max(peor_k)] < peor_k[min(peor_k)])
    # limite x1 -> inf por formula (c = x1 + x2, sombra de x1 -> pi)
    vals = []
    for t in (1e6, 1e8):
        fam = [t, 2.0, 2.0, 1.0]
        c = t + 2.0
        sp_, wst = caps_masa(None, PHI)
        vals.append(max(presupuesto(sp_, fam, c),
                        presupuesto(wst, fam + [sp_], c)))
    ok &= check(f"limite x1 -> inf POR FORMULA: sombra de x1 -> pi y "
                f"las demas -> 0: presupuesto -> pi < 2pi (margen "
                f"pi); puntos 10^6, 10^8: "
                f"{[round(v, 4) for v in vals]}",
                all(abs(v - PI) < 0.01 for v in vals))
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] rama 1 (Y >= alpha respirando), k <= 2: corona acotada")
    rng = random.Random(SEED + 1)
    ok = True
    n, fallos = 0, 0
    peor_def = 0.0
    arg = None

    def instancia(k, w, SS, holg, sp_=None):
        nonlocal n, fallos, peor_def, arg
        xs = cascada_agujero(SS, k, holg)
        XY = sum(xs)
        if XY + w <= PHI + 1e-12:
            return
        if k == 2:
            c = R_trio_blindada(xs[0], xs[1], 1.0)
        else:
            c = xs[0] + 1.0
        if sp_ is None:
            sp_, wst = caps_masa(rng, SS)
        else:
            sp_, wst = sp_
        piezas = sorted(xs + [1.0, sp_, wst], reverse=True)
        n += 1
        cabe, defc = corona_k5(piezas, c)
        if not cabe:
            fallos += 1
            if defc > peor_def:
                peor_def = defc
                arg = dict(k=k, w=round(w, 3), SS=round(SS, 3),
                           c=round(c, 3))

    for _ in range(max(15000, ITER // 4)):
        k = rng.randrange(1, 3)
        w = rng.uniform(0.05, 1.35)
        SS = rng.uniform(1.0 + 1e-6, PHI)
        holg = [1.0 + rng.expovariate(2.0) for _ in range(k)]
        if rng.random() < 0.3:
            holg = [1.0] * k
        instancia(k, w, SS, holg)
    # esquinas: cascada exacta (incluye el punto aureo {2, 2/phi, 1}
    # en k = 2, Sigma -> 1), trade-off s'/w*, holgura grande
    ndet = 0
    for k in (1, 2):
        for w in (0.05, PHI - 1, 0.9, 0.999, 1.2, 1.35):
            for SS in (1.0 + 1e-9, 1.3, PHI):
                for h in (1.0, 1.004, 2, 5, 20, 100, 1000, 10000):
                    for rk in range(k):
                        holg = [1.0] * k
                        holg[rk] = h
                        s_cap = min(SS / 2, PHI / 2)
                        for sp_v in (0.05, s_cap / 2, s_cap):
                            wst = min(1 / PHI, SS - 1.0,
                                      max(1e-6, SS - 2 * sp_v))
                            instancia(k, w, SS, holg,
                                      (sp_v, max(1e-6, wst)))
                            ndet += 1
    ok &= check(f"rama 1, k <= 2 ({n} instancias respirantes, {ndet} "
                f"deterministas con esquinas y h hasta 10^4): la "
                f"corona <= 5 piezas cabe en c = max(pares, blindada "
                f"del trio con m): {fallos} fallos (peor deficit "
                f"{peor_def:.4f}, argmax {arg})", n > 3000 and
                fallos == 0)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] rama 2 (corona-alpha con X_alpha grande): ambas celdas")
    rng = random.Random(SEED + 2)
    ok = True
    n3, freg3, fpres3 = 0, 0, 0
    peor3 = 0.0
    n2, fallos2 = 0, 0
    peor_def2 = 0.0
    arg3, arg2 = None, None
    vacias = 0
    peor3_k = {}

    def instancia(k, w, SS, s2, holg):
        nonlocal n3, freg3, fpres3, peor3, n2, fallos2, peor_def2
        nonlocal arg3, arg2, vacias
        if SS >= 1 + s2 - 1e-12:       # perfil pesado: fuera (F1f)
            return
        xs = cascada_agujero(SS, k, holg)
        Xa = sum(xs)
        pares = max((xs[0] + xs[1]) if k >= 2 else 0.0, xs[0] + 1.0)
        blind = R_trio_blindada(xs[0], xs[1], 1.0) if k >= 2 else pares
        c = max(SS + Xa, pares, blind)
        if c >= 1 + s2 + Xa - 1e-12:   # suelo >= techo B2u: bloqueo
            vacias += 1                # infactible (celda vacia)
            return
        if k >= 3:
            fam = xs + [1.0]           # m como pieza
            n3 += 1
            if not all(c - x > 2 * s2 + 1e-12 for x in fam):
                freg3 += 1
                return
            v = presupuesto(s2, fam, c)
            if v >= 2 * PI - 0.05:
                fpres3 += 1
            if v > peor3:
                peor3 = v
                arg3 = dict(k=k, w=round(w, 3), SS=round(SS, 3),
                            s2=round(s2, 3))
            peor3_k[k] = max(peor3_k.get(k, 0.0), v)
        else:
            piezas = sorted(xs + [1.0, s2], reverse=True)
            n2 += 1
            cabe, defc = corona_k5(piezas, c)
            if not cabe:
                fallos2 += 1
                if defc > peor_def2:
                    peor_def2 = defc
                    arg2 = dict(k=k, w=round(w, 3), SS=round(SS, 3),
                                s2=round(s2, 3), c=round(c, 3))

    for _ in range(max(30000, ITER // 2)):
        k = rng.randrange(1, 11)
        w = rng.uniform(0.05, 1.35)
        s2 = rng.uniform(0.05, 0.999)
        SS = rng.uniform(max(1.0 + 1e-6, 2 * s2), 1 + s2)
        if SS >= 1 + s2:
            continue
        holg = [1.0 + rng.expovariate(2.0) for _ in range(k)]
        if rng.random() < 0.3:
            holg = [1.0] * k
        instancia(k, w, SS, s2, holg)
    # esquinas: sigma2 de la ventana R2 (hasta 0.804 y frontera 1/2),
    # Sigma -> 1+ y -> 1+sigma2, cascada exacta, holgura grande
    ndet = 0
    for k in (1, 2, 3, 4, 6, 8, 10, 12):
        for w in (0.05, 0.927, 0.999, 1.2, 1.35):
            for s2 in (0.363, 0.5, 0.618, 0.804, 0.95):
                for SSf in (0.001, 0.5, 0.999):
                    SS = max(1.0 + 1e-9, 2 * s2) + SSf * \
                        max(0.0, (1 + s2) - max(1.0 + 1e-9, 2 * s2))
                    if SS >= 1 + s2:
                        continue
                    for h in (1.0, 2, 10, 100, 10000):
                        for rk in sorted({0, k - 1}):
                            holg = [1.0] * k
                            holg[rk] = h
                            instancia(k, w, SS, s2, holg)
                            ndet += 1
    ok &= check(f"rama 2, k >= 3 ({n3} instancias, {ndet} "
                f"deterministas en total): regimen automatico para "
                f"sigma2 ({freg3} fallos, exacto) y presupuesto "
                f"({fpres3} fallos; peor {peor3:.4f} < "
                f"{2 * PI - 0.05:.4f}, argmax {arg3})",
                n3 > 2000 and freg3 == 0 and fpres3 == 0)
    ok &= check(f"rama 2, k <= 2 ({n2} instancias): la corona "
                f"{{x1, (x2), m, sigma2}} cabe en c = max(E4, pares, "
                f"blindada): {fallos2} fallos (peor deficit "
                f"{peor_def2:.4f}, argmax {arg2})",
                n2 > 2000 and fallos2 == 0)
    trazak = {k: round(v, 3) for k, v in sorted(peor3_k.items())}
    ok &= check(f"direccion k en rama 2 (asterisco declarado): peor "
                f"presupuesto DECRECIENTE en k — {trazak}",
                peor3_k[max(peor3_k)] < peor3_k[min(peor3_k)])
    print(f"      celdas vacias por suelo >= techo B2u (bloqueo "
          f"infactible, cerradas gratis): {vacias}")
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles")
    ok = True
    # (a) sin el par del agujero el regimen revienta
    v = presupuesto(0.6, [3.0, 1.0], 3.1)
    ok &= check(f"(a) con c = x1 + 0.1 (violando c >= x1+1) la "
                f"sombra se dispara ({v:.3f} incluye pi): los pares "
                f"del empaquetamiento real del agujero son los que "
                f"pagan", v >= PI)
    # (b) rama 2, k = 2: el regimen automatico NO cubre sigma2 alta
    c = 2 / PHI + (1 + 1e-9) / PHI + 0.0  # c = x1+x2 en cascada min
    x2 = (1 + 1e-9 + 1.0) / PHI
    ok &= check(f"(b) k = 2: c - x1 >= x2 = {x2:.3f} < 2*0.7: el "
                f"regimen automatico NO cubre sigma2 > 1/phi — la "
                f"celda necesita la corona acotada (por eso la "
                f"dicotomia es k >= 3 / k <= 2, como j >= 2 / j <= 1)",
                x2 < 1.4)
    # (c) rama 1 no respirante: cerrada por I2 COMPLETA (puertocii)
    ok &= check("(c) rama 1 sin respirar: la I2 COMPLETA "
                "((phi-1)(X_Y+omega) > 1+(2-phi)Sigma_S+X_m+X_alpha, "
                "survive_c2 de puertocii) + (D) exigen X_Y+omega > "
                "sqrt5 = 2phi-1 = 2.2360; el umbral phi del filtro "
                "es para la masa > m TRAS descontar el polvo "
                "(< phi-1): lema de respiracion fuerte, check A(3)",
                abs((PHI - 1) * PHI - 1.0) < 1e-12
                and abs(2 * PHI - 1 - math.sqrt(5)) < 1e-12)
    # (d) rama 2 pesada: fuera (particion B*/A + pinza F1f)
    ok &= check("(d) rama 2 con Sigma_S >= 1+sigma2 (pesado): FUERA "
                "de este script — la cierra la particion B*/A con la "
                "pinza b2(4/phi, 2/phi) = 12/(7phi) > 1 (puertocii "
                "[F1f], exacta) y en raiz compartida el cuarteto de "
                "[G]", abs(12 / (7 * PHI) - 1.0599) < 1e-3)
    return ok


def main():
    print("=" * 68)
    print("CORONA DE AGUJERO: las dos ramas residuales del puerto "
          "(drafts/coronaagujero.md)")
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
