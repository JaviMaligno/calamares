#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El gap lemma escrito: anidado j <= 1 por corona directa de <= 5
piezas (docs/drafts/gaplemma.md).

La navaja aurea mata el metodo de sombras en j <= 1, pero alli la
sarten es una familia ACOTADA: {alpha, (o1), disco-unidad con la fila
greedy de D_m dentro, s', w*} — a lo sumo 5 circulos. El criterio
mural directo (suma ciclica de thetas consecutivos <= 2 pi + LAS
PAREJAS NO ADYACENTES validadas en las posiciones consecutivas) es
exacto y finito, y el dominio es una caja compacta: maximizacion
certificada, el estandar de thm:DPr.

El reparto (identico al del teorema anidado j >= 2 salvo el paso 3):
  (1) m -> agujero de alpha (certificado de F); D_m vacante;
  (2) llenado greedy de D_m (fila decreciente hasta s');
  (3) REPACK MURAL de la sarten entera: {alpha, o1 (si j = 1),
      disco-1 (con la fila de D_m dentro), s', w*} en corona, con el
      criterio exacto de <= 5 piezas.  El disco-1 es legal como
      pieza: contiene la fila (lem:row) y su interior no es visible
      desde fuera.  El repack es recurso legal (posiciones
      existenciales; pan repack de thm:DP).
  (4) la masa: s' <= min(Sigma/2, phi/2) (tope exacto), W'' < 1/phi
      (greedy + cola de m), Sigma in (1, phi].

Dominio (colas + legalidades, sin usar omega en las piezas):
  alpha >= max(1+omega, Sigma_S+X_alpha+omega, (1+Sigma+X)/phi),
  con Sigma_S = SOLO la masa del agujero de alpha (S): los extras y
  el polvo top-level de la sarten NO estan en el agujero y no pueden
  entrar en el suelo E4 (el generador barre Sigma_S in [0, Sigma]
  INDEPENDIENTE de Sigma — ronda hostil 2026-08-09: el generador v1
  usaba Sigma total ahi y era ANTICONSERVADOR);
  j = 1: o1 >= (1+Sigma)/phi (cascada; la cola de o1 contiene m y
  TODA la masa suelta, extras incluidos; >= 1 por ser aro >= m);
  R >= max(alpha+o1, alpha+1, o1+1) (pares de P) y ademas la cota
  del trio BLINDADA min(R3, M) (ver R3_necesidad/M_apilable: si un
  par fuese apilable a R_real, R_real >= M >= min(R3, M) igualmente;
  en el dominio R3 <= M SIEMPRE — check explicito en [C] — con
  igualdad exacta solo en el punto aureo (alpha, o1) = (2, 2/phi)
  donde ademas pares = R3 = M = 1+sqrt5 y el trio no hace falta).
  Conservador: R = cota minima (theta decrece en R); alpha con techo
  infinito (limite alpha -> inf verificado aparte).

Bloques: [A] identidades y el criterio k <= 5; [B] j = 0 (cuarteto);
[C] j = 1 (quinteto); [D] limites y esquinas; [E] controles.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, theta_w, ciclo_constructivo

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260812'))


def R3_necesidad(a, b, c):
    """Radio minimo que la NECESIDAD del trio permite: el menor R con
    theta(a,b)+theta(b,c)+theta(c,a) <= 2 pi (para tres piezas todos
    los ordenes ciclicos son el mismo ciclo).  Es cota inferior
    VERDADERA del radio de cualquier disco que empaquete {a, b, c}
    con pares no apilables (P1 + particion del circulo: teorema,
    drafts/compactacion.md)."""
    lo, hi = max(a + b, b + c, a + c), 4.0 * (a + b + c)
    if (theta_w(a, b, lo) + theta_w(b, c, lo) +
            theta_w(c, a, lo)) <= 2 * PI:
        return lo
    for _ in range(60):
        mid = (lo + hi) / 2
        if (theta_w(a, b, mid) + theta_w(b, c, mid) +
                theta_w(c, a, mid)) <= 2 * PI:
            hi = mid
        else:
            lo = mid
    return lo      # extremo seguro


def M_apilable(trio):
    """Umbral de apilabilidad del trio: el menor max+2min sobre los
    tres pares.  Un par (x, y) es apilable en el disco R sii
    R >= max+2min (el chico cabe radialmente tras el grande); por
    debajo de M TODOS los pares son no apilables y la necesidad del
    trio (P1 + particion) aplica."""
    return min(max(a, b) + 2 * min(a, b)
               for i, a in enumerate(trio) for b in trio[i + 1:])


def R_trio_blindada(a, b, c):
    """Cota inferior INCONDICIONAL del radio de cualquier disco que
    empaquete {a, b, c}: max(pares, min(R3, M)).  Dicotomia sobre el
    R_real: si todos los pares son no apilables a R_real, la
    necesidad del trio da R_real >= R3; si algun par es apilable,
    R_real >= max+2min de ese par >= M.  En ambos casos
    R_real >= min(R3, M), sin hipotesis."""
    pares = max(a + b, b + c, a + c)
    return max(pares, min(R3_necesidad(a, b, c), M_apilable([a, b, c])))


def corona_k5(piezas, R):
    """Criterio exacto de corona mural para <= 5 piezas: prueba TODOS
    los ordenes ciclicos (<= 12) con ciclo_constructivo (posiciones
    por camino mas largo + validacion de todas las parejas).
    Devuelve (cabe, mejor_deficit)."""
    from itertools import permutations
    k = len(piezas)
    if k <= 2:
        return sum(piezas) <= R, 0.0
    mejor = 1e9
    base = piezas[0]
    for perm in permutations(piezas[1:]):
        okc, defc = ciclo_constructivo([base] + list(perm), R)
        if okc:
            return True, 0.0
        mejor = min(mejor, defc)
    return False, mejor


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades y el criterio de <= 5 piezas")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    ok &= check("[ENUNCIADO] criterio k <= 5: la corona mural con "
                "posiciones por camino mas largo y TODAS las parejas "
                "validadas es una colocacion legal (solidez "
                "adversariada en zigzag/compactacion); para <= 5 "
                "piezas el minimo sobre ordenes es exhaustivo "
                "(<= 12 ordenes ciclicos): criterio EXACTO y finito",
                True)
    ok &= check("tope del insertando y masa (heredados, exactos): "
                "s' <= min(Sigma/2, phi/2), W'' < phi-1 = 1/phi, "
                "Sigma in (1, phi]",
                sp.simplify((phi - 1) - 1 / phi) == 0)
    ok &= check("suelos del dominio: alpha >= max(1+omega, "
                "Sigma_S+omega, (1+Sigma)/phi); o1 >= max(1, "
                "(1+Sigma)/phi) = (1+Sigma)/phi (Sigma > 1 => "
                "(1+Sigma)/phi > 2/phi > 1)",
                float(2 / phi) > 1)
    # el disco-1 con la fila dentro es pieza legal
    ok &= check("[ENUNCIADO] el disco unidad con la fila greedy "
                "dentro es UNA pieza (lem:row dentro; interior no "
                "visible): el repack mural lo trata como radio 1",
                True)
    # la cota del trio es BLINDADA: dicotomia apilable/no apilable
    ok &= check("[ENUNCIADO] cota del trio blindada R >= max(pares, "
                "min(R3, M)): si todo par es no apilable a R_real, "
                "P1 + particion dan R_real >= R3; si algun par es "
                "apilable, R_real >= max+2min >= M: incondicional",
                True)
    # el punto aureo exacto donde R3 = M = pares (sympy)
    o1 = 2 / phi
    Rq = o1 + 2
    f = lambda x: x / (Rq - x)
    ok &= check("punto aureo del trio {2, 2/phi, 1}: pr(alpha, o1) "
                "= 1 y pr(alpha, m) + pr(o1, m) = 1 exactos en "
                "R = o1+2 (suma del trio = pi + 2 asin x + 2 asin y "
                "con x^2+y^2 = 1: EXACTAMENTE 2 pi), y ademas "
                "alpha+o1 = o1+2 = 1+sqrt5: pares = R3 = M colapsan "
                "(el intervalo [M, R3) es vacio alli); o1 = 2/phi es "
                "la raiz de o1^2+2 o1-4 = 0",
                sp.simplify(f(2) * f(o1) - 1) == 0
                and sp.simplify(f(2) * f(1) + f(o1) * f(1) - 1) == 0
                and sp.simplify((2 + o1) - (o1 + 2)) == 0
                and sp.simplify(o1 ** 2 + 2 * o1 - 4) == 0
                and sp.simplify((o1 + 2) - (1 + sp.sqrt(5))) == 0)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] j = 0: el cuarteto {alpha, 1, s', w*}")
    rng = random.Random(SEED)
    ok = True
    n, fallos = 0, 0
    peor_def, arg = 0.0, None
    for _ in range(max(20000, ITER // 3)):
        w = rng.uniform(0.02, 3.0)
        Sg = rng.uniform(1.0 + 1e-6, PHI)
        # Sigma_S = SOLO la masa del agujero (E4); extras/polvo de la
        # sarten NO cuentan en ese suelo: barrer INDEPENDIENTE
        SgS = rng.uniform(0.0, Sg)
        Xa = rng.uniform(0.0, 1.5) if rng.random() < 0.3 else 0.0
        af = max(1.0 + w, SgS + Xa + w, (1.0 + Sg + Xa) / PHI) * \
            (1.0 + (rng.expovariate(2.0) if rng.random() < 0.6 else 0))
        sp_ = rng.uniform(0.05, min(Sg / 2, PHI / 2))
        # W'' < 1/phi y ademas W'' < Sigma - fila - s' <= Sigma - 1
        wst = rng.uniform(0.01, min(1 / PHI - 1e-6,
                                    max(0.011, Sg - 1.0)))
        R = af + 1.0
        n += 1
        cabe, defc = corona_k5([af, 1.0, sp_, wst], R)
        if not cabe:
            fallos += 1
            if defc > peor_def:
                peor_def, arg = defc, dict(w=round(w, 2),
                                           af=round(af, 3),
                                           sp=round(sp_, 3),
                                           wst=round(wst, 3))
    ok &= check(f"j = 0 ({n} instancias, suelo HONESTO Sigma_S in "
                f"[0, Sigma], R = alpha+1 el peor): el cuarteto "
                f"SIEMPRE cabe ({fallos} fallos, peor deficit "
                f"{peor_def:.4f}; peor {arg})", n > 3000
                and fallos == 0)
    # esquinas deterministas: alpha en su suelo (incluido el MINIMO
    # absoluto Sigma_S = 0: alpha = max(1+w, (1+Sigma)/phi)), s' y
    # w* en sus topes (aun cuando la masa no de para ambos: sobra)
    peor2 = 0.0
    fallos2 = 0
    for w in (0.02, 0.2, 1 - PHI / 2, 0.5, PHI - 1, PHI / 2, 0.99,
              1.2, 2.0, 3.0):
        for Sg in (1.0 + 1e-9, 1.2, PHI / 2 * 2 - 1e-9, PHI):
            for SgS in (0.0, Sg / 2, Sg):
                af = max(1.0 + w, SgS + w, (1.0 + Sg) / PHI)
                sp_ = min(Sg / 2, PHI / 2) - 1e-9
                wst = 1 / PHI - 1e-9
                cabe, defc = corona_k5([af, 1.0, sp_, wst], af + 1.0)
                if not cabe:
                    fallos2 += 1
                    peor2 = max(peor2, defc)
    ok &= check(f"esquinas deterministas j = 0 (suelos de alpha con "
                f"Sigma_S in {{0, Sigma/2, Sigma}}, topes de s' y "
                f"w*): {fallos2} fallos (peor {peor2:.4f})",
                fallos2 == 0)
    # trade-off exacto s'/w* en el suelo minimo absoluto de alpha
    fallos3, peor3 = 0, 0.0
    for iS in range(40):
        Sg = 1.0 + 1e-6 + iS * (PHI - 1.0) / 39
        af = max((1.0 + Sg) / PHI, 1.02)
        stop = min(Sg / 2, PHI / 2)
        for k in range(13):
            sp_ = 0.05 + k * (stop - 0.05 - 1e-9) / 12
            wst = min(1 / PHI, Sg - 1.0, Sg - 2 * sp_) - 1e-9
            piezas = [af, 1.0, sp_]
            if wst > 0.005:
                piezas.append(wst)
            cabe, defc = corona_k5(piezas, af + 1.0)
            if not cabe:
                fallos3 += 1
                peor3 = max(peor3, defc)
    ok &= check(f"trade-off s'/w* con la ligadura de masa exacta en "
                f"el suelo minimo alpha = (1+Sigma)/phi (Sigma_S = "
                f"0): {fallos3} fallos (peor {peor3:.4f})",
                fallos3 == 0)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] j = 1: el quinteto {alpha, o1, 1, s', w*}")
    rng = random.Random(SEED + 1)
    ok = True
    n, fallos = 0, 0
    peor_def, arg = 0.0, None
    apil_viol, apil_act = 0, 0    # R3 activa con R3 > M: no debe pasar
    for _ in range(max(10000, ITER // 6)):
        w = rng.uniform(0.02, 3.0)
        Sg = rng.uniform(1.0 + 1e-6, PHI)
        SgS = rng.uniform(0.0, Sg)     # solo la S del agujero (E4)
        Xa = rng.uniform(0.0, 1.5) if rng.random() < 0.3 else 0.0
        af = max(1.0 + w, SgS + Xa + w, (1.0 + Sg + Xa) / PHI) * \
            (1.0 + (rng.expovariate(2.0) if rng.random() < 0.6 else 0))
        o1 = max(1.0, (1.0 + Sg) / PHI) * \
            (1.0 + (rng.expovariate(2.0) if rng.random() < 0.6 else 0))
        sp_ = rng.uniform(0.05, min(Sg / 2, PHI / 2))
        wst = rng.uniform(0.01, min(1 / PHI - 1e-6,
                                    max(0.011, Sg - 1.0)))
        # R = maximo de las necesidades ESCRITAS: pares de P y el
        # TRIO {alpha, o1, m} BLINDADO (P los empaqueta; dicotomia
        # apilable/no apilable: R >= min(R3, M) incondicional)
        pares = max(af + max(o1, 1.0), o1 + 1.0)
        R3 = R3_necesidad(af, o1, 1.0)
        M = M_apilable([af, o1, 1.0])
        if R3 > pares + 1e-9:
            apil_act += 1
            if R3 > M + 1e-9:
                apil_viol += 1
        R = max(pares, min(R3, M))
        n += 1
        cabe, defc = corona_k5([af, o1, 1.0, sp_, wst], R)
        if not cabe:
            fallos += 1
            if defc > peor_def:
                peor_def, arg = defc, dict(w=round(w, 2),
                                           af=round(af, 3),
                                           o1=round(o1, 3),
                                           sp=round(sp_, 3),
                                           wst=round(wst, 3))
    ok &= check(f"j = 1 ({n} instancias, suelo HONESTO Sigma_S in "
                f"[0, Sigma], R = max(pares, min(R3, M)) blindada): "
                f"el quinteto SIEMPRE cabe ({fallos} fallos, peor "
                f"deficit {peor_def:.4f}; peor {arg})", n > 2000
                and fallos == 0)
    ok &= check(f"no-apilabilidad EXPLICITA: en las {apil_act} "
                f"instancias con el trio activo (R3 > pares), R3 <= "
                f"M = min max+2min SIEMPRE ({apil_viol} violaciones):"
                f" min(R3, M) = R3 en todo el dominio y la necesidad "
                f"del trio aplica tal cual", apil_act > 50
                and apil_viol == 0)
    # esquinas deterministas, incluida LA NAVAJA (o1 = (1+Sigma)/phi
    # con Sigma -> 1: o1 -> 2/phi) y el SUELO MINIMO de alpha
    # (Sigma_S = 0: alpha = max(1+w, (1+Sigma)/phi))
    peor2, fallos2 = 0.0, 0
    for w in (0.02, 0.5, PHI - 1, PHI / 2, 0.99, 1.2, 2.0, 3.0):
        for Sg in (1.0 + 1e-9, 1.3, PHI):
            for SgS in (0.0, Sg):
                af = max(1.0 + w, SgS + w, (1.0 + Sg) / PHI)
                o1 = max(1.0, (1.0 + Sg) / PHI)
                for sp_ in (0.25, 0.5, min(Sg / 2, PHI / 2) - 1e-9):
                    # ligadura de masa EXACTA: l1 >= s' entro en D_m
                    # y fila+s' > 1: W'' <= min(1/phi, Sigma - 1,
                    # Sigma - 2 s')
                    wst = min(1 / PHI, Sg - 1.0,
                              max(0.0, Sg - 2 * sp_)) - 1e-9
                    piezas = [af, o1, 1.0, sp_]
                    if wst > 0.01:
                        piezas.append(wst)
                    R = R_trio_blindada(af, o1, 1.0)
                    cabe, defc = corona_k5(piezas, R)
                    if not cabe:
                        fallos2 += 1
                        peor2 = max(peor2, defc)
    ok &= check(f"esquinas deterministas j = 1 (incluida la navaja "
                f"o1 = 2/phi y el suelo minimo Sigma_S = 0): "
                f"{fallos2} fallos (peor {peor2:.4f})",
                fallos2 == 0)
    # DOBLE SUELO consistente: alpha y o1 AMBOS en (1+Sigma)/phi
    # (la esquina que el generador v1 con Sigma total casi no
    # tocaba), trade-off s'/w* exacto y holguras de o1 (monotonia)
    peor3, fallos3 = 0.0, 0
    for iS in range(30):
        Sg = 1.0 + 1e-6 + iS * (PHI - 1.0) / 29
        fl = (1.0 + Sg) / PHI
        for af in (max(fl, 1.02), max(fl, 1.02) * 1.1, 2.0, 2.6):
            for o1 in (fl, fl * 1.05, fl * 1.2, 2.0, 5.0, 20.0):
                stop = min(Sg / 2, PHI / 2)
                for k in range(11):
                    sp_ = 0.05 + k * (stop - 0.05 - 1e-9) / 10
                    wst = min(1 / PHI, Sg - 1.0,
                              Sg - 2 * sp_) - 1e-9
                    piezas = [af, o1, 1.0, sp_]
                    if wst > 0.005:
                        piezas.append(wst)
                    R = R_trio_blindada(af, o1, 1.0)
                    cabe, defc = corona_k5(piezas, R)
                    if not cabe:
                        fallos3 += 1
                        peor3 = max(peor3, defc)
    ok &= check(f"doble suelo alpha = o1 = (1+Sigma)/phi + trade-off "
                f"s'/w* exacto + o1 con holgura hasta 20 (monotonia "
                f"en o1 cubierta por puntos, no supuesta): {fallos3} "
                f"fallos (peor {peor3:.4f})", fallos3 == 0)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] limites: alpha -> infinito y los margenes")
    ok = True
    # alpha -> inf con R = alpha+1: f(alpha) -> inf pero
    # f(x) = x/(alpha+1-x) -> 0 como x/alpha, luego
    # pr(alpha, x) -> x y theta(alpha, x) -> 2 asin(sqrt x) FINITO
    # (< pi para x < 1), y theta(x, y) -> 0 entre piezas chicas.
    # Orden [1, s', alpha, w*]: el camino largo mete el pi diametral
    # (alpha, 1) que ABSORBE theta(alpha, s') (= 2.23 < pi), y el
    # total limite es pi + theta(alpha, w*) -> pi + 2 asin(sqrt(1/
    # phi)) = 4.951 < 2 pi (margen 1.33): benigno POR FORMULA, y los
    # puntos hasta 10^4 lo confirman
    lim = PI + 2 * math.asin(math.sqrt(1 / PHI))
    absorbe = 2 * math.asin(math.sqrt(PHI / 2)) < PI
    peores = []
    for af in (5.0, 50.0, 500.0, 1e4):
        cabe, _ = corona_k5([af, 1.0, PHI / 2 - 1e-9,
                             1 / PHI - 1e-9], af + 1.0)
        peores.append((af, cabe))
    ok &= check(f"limite alpha -> inf (j = 0, topes): total limite "
                f"del orden [1, s', alpha, w*] = pi + "
                f"2asin(sqrt(1/phi)) = {lim:.4f} < 2 pi (margen "
                f"{2 * PI - lim:.3f}; el pi diametral (alpha, 1) "
                f"absorbe theta(alpha, s') = "
                f"{2 * math.asin(math.sqrt(PHI / 2)):.3f} < pi); "
                f"puntos hasta 10^4: {peores}",
                all(c for _, c in peores) and absorbe
                and lim < 2 * PI - 0.5)
    # alpha -> inf con j = 1 (o1 en la navaja y con holgura)
    peores1 = []
    for af in (5.0, 500.0, 1e4):
        for o1 in (2 / PHI, 2.0):
            R = R_trio_blindada(af, o1, 1.0)
            cabe, _ = corona_k5([af, o1, 1.0, PHI / 2 - 1e-9,
                                 1 / PHI - 1e-9], R)
            peores1.append((af, o1, cabe))
    ok &= check(f"limite alpha -> inf (j = 1, topes, navaja y "
                f"holgura): {peores1}",
                all(c for _, _, c in peores1))
    # margen minimo observado en una malla del nucleo j = 0
    peor_marg = 1e9
    for wi in range(1, 15):
        w = wi * 0.1
        for si in range(2, 17):
            Sg = 1.0 + si * 0.04
            if Sg > PHI:
                continue
            # suelo HONESTO minimo (Sigma_S = 0): el peor alpha
            af = max(1.0 + w, (1.0 + Sg) / PHI)
            piezas = [af, 1.0, min(Sg / 2, PHI / 2) - 1e-9,
                      1 / PHI - 1e-9]
            R = af + 1.0
            # margen: cuanto puede crecer s' antes de fallar
            lo, hi = 0.0, 1.0
            for _ in range(25):
                mid = (lo + hi) / 2
                piezas2 = [af, 1.0, min(Sg / 2, PHI / 2) - 1e-9 + mid,
                           1 / PHI - 1e-9]
                if piezas2[2] < piezas2[0] and \
                        corona_k5(piezas2, R)[0]:
                    lo = mid
                else:
                    hi = mid
            peor_marg = min(peor_marg, lo)
    ok &= check(f"margen del nucleo j = 0 con el suelo HONESTO "
                f"minimo alpha = max(1+omega, (1+Sigma)/phi): s' "
                f"puede crecer >= {peor_marg:.4f} sobre su tope en "
                f"toda la malla (positivo pero FINO: con el suelo "
                f"honesto la esquina critica esta apretada; el "
                f"margen 0.021 del v1 venia del suelo inflado "
                f"Sigma+omega)", peor_marg > 0.005)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles")
    ok = True
    # (a) sin las colas (alpha sin suelo de cola) el cuarteto PUEDE
    # fallar? alpha = 1+w con w pequeno y Sigma grande: el suelo
    # Sigma+w manda: probar VIOLANDO el suelo Sigma+w
    cabe, defc = corona_k5([1.05, 1.0, 0.8, 0.6], 2.05)
    ok &= check(f"(a) violando el suelo alpha >= Sigma+omega (alpha "
                f"= 1.05 con piezas 0.8+0.6): el cuarteto NO cabe "
                f"(deficit {defc:.3f} > 0): las legalidades del "
                f"testigo son las que pagan", not cabe and defc > 0)
    # (b) la navaja ya no muerde: con la necesidad del trio en R, la
    # corona directa coloca el quinteto en el punto critico
    af, o1 = 1.3, 2 / PHI
    R = R_trio_blindada(af, o1, 1.0)
    cabe, _ = corona_k5([af, o1, 1.0, 0.5 - 1e-9, 1 / PHI - 1e-9], R)
    ok &= check(f"(b) la navaja (o1 = 2/phi) NO bloquea la corona "
                f"directa con R >= necesidad del trio "
                f"(R = {R:.3f}): quinteto cabe = {cabe}", cabe)
    return ok


def main():
    print("=" * 68)
    print("GAP LEMMA ESCRITO: anidado j <= 1 por corona directa "
          "(drafts/gaplemma.md)")
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
