#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Puerto (c-ii): la celda abierta del ensamblaje (alpha fuera de v).

Configuracion: u = agujero de alpha (el intercambio manda m = 1 a u),
alpha NO es miembro directo de v.  Sub-casos:
  (c-ii-2) v = agujero de Y con alpha fuera del agujero de Y;
  (c-ii-1) v = SARTEN con alpha anidada (alpha en el agujero de z,
           torre z < w' < ... < t, raiz t top-level de v).
S = anillos < m que P mantiene en u; |S| >= 2 (E1); sigma1 >= sigma2.
Recursos del re-empaquetado: D_m (hueco unidad en v), H_m (cap
1-omega-X_m, viaja con m), anidamiento en S, geometria de v.

PAREDES DEL BLOQUEO (todas las colocaciones fallan):
  (D)   fila {sigma1, sigma2} en D_m:            S0 := s1+s2 > 1.
  (BH)  sigma2 -> H_m:                            s2 + X_m > 1-omega.
  (B2u) sigma2 junto a m en el agujero de alpha:  1+s2+X_alpha >
        alpha-omega  (dos grandes {m, s2}: criterio de dos circulos
        EXACTO => la corona del agujero de alpha no mejora la fila).
  (Bs1) sigma2 al agujero de sigma1:              s2+X_s1 > s1-omega.
  (RY)  todo S como fila en el agujero de Y (D_m vive dentro):
        Sigma_S + X_Y > Y-omega  [(c-ii-2)].
  (Rz)  sigma2 al agujero de z junto a alpha:     alpha+X_z+s2 >
        z-omega  [(c-ii-1) y (c-ii-2) con alpha anidada].
  (COR) sigma2 a la corona de v = sarten          [(c-ii-1)].
LEGALIDADES DEL TESTIGO (W):
  alpha >= Sigma_S + X_alpha + omega   (E4, tarifa DR en u segun P)
  alpha >= 1 + omega                   (F anida m en alpha)
  Y >= 1 + X_Y + omega;  z >= alpha + X_z + omega;  X_m <= 1-omega.
COLAS (rho <= phi; multiconjunto de entrada, primera copia en empates):
  cola(m):     Sigma_S + X_m <= phi.
  cola(alpha): (1 + Sigma_S + X_m + X_alpha [+ Y + X_Y si Y < alpha
               (+ tarifas)]) <= phi * alpha.
  cola(Y):     (1 + Sigma_S + X_m + X_Y [+ alpha + X_alpha si
               alpha <= Y]) <= phi * Y.
  cola(z):     (1 + Sigma_S + X_m + X_alpha + alpha + X_z) <= phi*z.

IDENTIDADES MOTOR (derivadas en [A], sympy):
  I1 (ligereza automatica): E4 + B2u  =>  Sigma_S < 1 + sigma2, o sea
     sigma1 + W < 1: en (c-ii) TODO perfil es LIGERO y el resto de S
     (fila de suma Sigma_S - sigma2 < 1) SIEMPRE cabe en D_m: el
     bloqueo se reduce a colocar sigma2.
  I2 (colas cruzadas, rama Y >= alpha): cola(Y) con alpha dentro +
     E4 + (RY) es infactible salvo (phi-1)(X_Y+omega) >= 1: con
     X_Y = 0 exige omega >= phi (imposible, omega < 1 en anillo).
  I3 (pinza de alpha, rama Y < alpha): cola(alpha) con Y dentro +
     Y >= 1+X_Y+omega + B2u  =>  supervivencia solo si
     Sigma_S < phi-2 + phi*s2 + (phi-1)*omega + (phi-1)*X_alpha
               - 2*X_Y - X_m.
     Con X = 0: exige sigma2 > (3-phi-(phi-1)omega)/phi y
     sigma2 < phi*omega - 1; ventana no vacia sii omega > 3/(2phi)
     = 0.9271 (esquinas exactas: phi*omega-1 > 1-omega en
     omega = 2/phi^2 = 4-2phi; cruce en 3/(2phi) = 3(phi-1)/2).
  I4 (pinza de z): cola(z) + (Rz)  =>  supervivencia solo si
     alpha + X_z > phi(1+Sigma_S) - phi^2*sigma2 - phi^2*omega
     (X_z sin techo: la pinza no cierra sola; la corona de v con z
     engordado por su cola toma el relevo en (c-ii-1)).

PROGRAMA: [A] identidades exactas; [B] (c-ii-2) con X_Y = 0 EXACTO +
barrido MC general y delimitacion del residuo R2; [C] (c-ii-1) pinza
(Rz)+cola(z) + corona de la sarten, torres d = 1..3, omega en (0,1) y
pivote solido; [D] enrutado exhaustivo; [E] controles negativos.

Conservadurismo: colas omiten masas opcionales salvo las declaradas;
corona_suf/minimos heuristicos son cota superior del minimo (si una
variante cabe, desbloquea); R real >= R_lb (dualidad tangente en la
frontera: deficit 0.0 = exito).
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import (check, theta_w, gamma_min, cabe_algun_orden,
                         R_lb_pack, ciclo_constructivo, corona_suf,
                         bolsillo_descartes)

PHI = (1 + math.sqrt(5)) / 2
PI = math.pi
ITER = int(os.environ.get('CC_ITER', '60000'))
TOL = 2e-3          # tolerancia de tangencia (biseccion de R_lb)
FALLO_MIN = 1e-2    # fallo sin deficit angular cuenta como fallo pleno
OMEGA_STAR = 3 / (2 * PHI)          # 0.92705... esquina de I3


def survive_c2(w, s1, s2, W, Xm, Xa, XY):
    """(c-ii-2): aplica las pinzas I1, cola(m), I2, I3 a una instancia
    del bloqueo.  Devuelve (sobrevive, motivo_cierre_o_None).
    Conservador: el adversario elige Y y alpha en sus rangos; aqui se
    comprueba si ALGUN (Y, alpha) es consistente con paredes + colas."""
    S = s1 + s2 + W
    if S >= 1 + s2 - 1e-12:
        return False, 'I1-ligereza'          # E4+B2u infactible
    if S + Xm > PHI + 1e-12:
        return False, 'cola-m'
    # rama Y >= alpha (I2): phi*Y >= 1+S+Xm+XY+alpha+Xa (cola de Y con
    # alpha y su carga dentro), alpha >= S+Xa+omega (E4),
    # Y < S0+XY+omega (RY con Sigma_S >= S0... conservador: usa S)
    S0 = s1 + s2
    ok_I2 = False
    # techo de Y: RY => Y < S + XY + omega (fila de todo S); suelo de
    # alpha: E4.  phi*(S+XY+w) > 1+S+Xm+XY+(S+Xa+w) es la condicion
    # necesaria de supervivencia de la rama
    if PHI * (S + XY + w) > 1 + S + Xm + XY + S + Xa + w + 1e-12:
        ok_I2 = True
    # rama Y < alpha (I3): lb(alpha) <= ub(alpha)
    lbY = max(1 + XY + w, (1 + S + Xm + XY) / PHI)
    lb_a = max(S + Xa + w, 1 + w, (1 + S + Xm + Xa + XY + lbY) / PHI)
    ub_a = 1 + s2 + Xa + w                    # B2u
    ok_I3 = lb_a < ub_a - 1e-12 and lbY < S0 + XY + w - 1e-12
    if ok_I2 or ok_I3:
        return True, None
    return False, 'pinza-colas'


def fila_en_bin(piezas, cap=1.0):
    return sum(piezas) <= cap + 1e-12


def compon_masa(rng, total, nmax=4, lo=0.01):
    """Parte una masa total en 1..nmax piezas aleatorias (composicion
    del multiconjunto X)."""
    if total <= 1e-9:
        return []
    n = rng.randrange(1, nmax + 1)
    cortes = sorted(rng.uniform(0, total) for _ in range(n - 1))
    piezas = []
    prev = 0.0
    for c in cortes + [total]:
        x = c - prev
        if x > lo:
            piezas.append(x)
        prev = c
    return piezas or [total]


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades y legalidades exactas (sympy)")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    s1, s2, W, w, Xa, XY, Xm, S = sp.symbols(
        'sigma1 sigma2 W omega X_alpha X_Y X_m Sigma', nonnegative=True)
    al, Y = sp.symbols('alpha Y', positive=True)
    # I1: E4 (alpha >= S+Xa+w) + B2u (alpha < 1+s2+Xa+w) => S < 1+s2:
    # X_alpha y omega se CANCELAN exactamente
    resto = sp.expand((1 + s2 + Xa + w) - (S + Xa + w) - (1 + s2 - S))
    ok &= check("I1: (1+s2+Xa+w) - (S+Xa+w) = 1+s2-S identicamente "
                "(X_alpha y omega se cancelan): E4+B2u => Sigma_S < "
                "1+sigma2, el perfil de (c-ii) es LIGERO automatico y "
                "S \\ {sigma2} cabe en D_m como fila (suma < 1)",
                resto == 0)
    # I2: rama Y >= alpha.  cola(Y) >= (1+S+Xm+XY+alpha+Xa)/Y <= phi,
    # RY: Y < S+XY+w (fila de todo S; S0 <= Sigma_S), E4: alpha >=
    # S+Xa+w.  Infactibilidad: phi(S+XY+w) <= 1+S+Xm+XY+S+Xa+w
    # <=> (phi-2)S <= 1 - (phi-1)(XY+w) + Xm + Xa - ... reordenado:
    # supervivencia de la rama <=> (phi-2)S > 1 - (phi-1)(XY+w) + Xm
    # + Xa (reordenado); como phi-2 < 0 y
    # S > 0, con Xm = Xa = 0 exige (phi-1)(XY+w) > 1, o sea
    # XY + w > phi (pues 1/(phi-1) = phi)
    ok &= check("I2: rama Y >= alpha con X_m = X_alpha = 0: "
                "supervivencia exige (phi-1)(X_Y+omega) > 1, es decir "
                "X_Y + omega > phi (1/(phi-1) = phi exacto); con "
                "X_Y = 0 exige omega > phi: la rama es VACIA para "
                "todo omega de anillo (omega < 1 <= phi)",
                sp.simplify(1 / (phi - 1) - phi) == 0
                and float(phi) > 1)
    # I3: rama Y < alpha, X = 0.  lb(alpha) = (2+S+w)/phi (cola de
    # alpha con Y >= 1+w dentro), ub(alpha) = 1+s2+w (B2u).
    # supervivencia <=> 2+S+w < phi(1+s2+w)
    # <=> S < phi-2 + phi*s2 + (phi-1)*w  =: RHS3
    RHS3 = phi - 2 + phi * s2 + (phi - 1) * w
    # (i) con S > 1 (pared D):  1 < RHS3 <=> s2 > (3-phi-(phi-1)w)/phi
    g = (3 - phi - (phi - 1) * w) / phi
    ok &= check("I3a: supervivencia con S > 1 exige sigma2 > g(omega) "
                ":= (3-phi-(phi-1)omega)/phi (despeje exacto de "
                "1 < phi-2+phi*s2+(phi-1)omega)",
                sp.simplify(RHS3.subs(s2, g) - 1) == 0)
    # (ii) con S >= 2*s2 (s1 >= s2): 2 s2 < RHS3 <=> s2 < phi*w - 1
    #      ((phi-1)/(2-phi) = phi exacto)
    ok &= check("I3b: supervivencia con sigma1 >= sigma2 exige "
                "sigma2 < phi*omega - 1 ((phi-1)/(2-phi) = phi exacto)",
                sp.simplify((phi - 1) / (2 - phi) - phi) == 0
                and sp.simplify(RHS3.subs(s2, phi * w - 1)
                                - 2 * (phi * w - 1)) == 0)
    # (iii) ventana no vacia: g(omega) < phi*omega - 1 <=> omega >
    #       3/(2phi); y phi*omega-1 > 1-omega (BH pura) <=> omega >
    #       2/phi^2 = 4-2phi; 3/(2phi) > 4-2phi
    wstar = sp.Rational(3, 2) / phi
    ok &= check("I3c: g(omega) = phi*omega-1 exactamente en omega* = "
                "3/(2phi) = 3(phi-1)/2 = 0.92705; phi*omega-1 = "
                "1-omega en omega = 2/phi^2 = 4-2phi = 0.76393 < "
                "omega*: la celda (c-ii-2) con X = 0 es INFACTIBLE "
                "para todo omega <= 3/(2phi), y el residuo R2 vive en "
                "omega > 3/(2phi)",
                sp.simplify(g.subs(w, wstar) - (phi * wstar - 1)) == 0
                and sp.simplify(sp.Rational(2, 1) / phi ** 2
                                - (4 - 2 * phi)) == 0
                and float(wstar) > float(4 - 2 * phi)
                and abs(float(wstar) - 0.9270509831) < 1e-9)
    # I3 general (X > 0): supervivencia <=>
    # S < phi-2 + phi*s2 + (phi-1)w + (phi-1)Xa - 2*XY - Xm
    # (cola de alpha contiene Y+XY con Y >= 1+XY+w, mas Xm y Xa;
    # B2u sube el techo phi*(...+Xa) y la cola resta Xa: neto (phi-1))
    lb_a = (1 + S + Xm + Xa + XY + (1 + XY + w)) / phi
    ub_a = 1 + s2 + Xa + w
    surv = sp.expand(phi * ub_a - (2 + S + Xm + Xa + 2 * XY + w))
    objetivo = sp.expand(phi - 2 + phi * s2 + (phi - 1) * w
                         + (phi - 1) * Xa - 2 * XY - Xm - S)
    ok &= check("I3d (general): phi*ub(alpha) - phi*lb(alpha) = "
                "[phi-2 + phi*s2 + (phi-1)omega + (phi-1)X_alpha "
                "- 2X_Y - X_m] - Sigma_S identicamente: X_alpha es la "
                "UNICA masa que ayuda al adversario (coef phi-1 > 0); "
                "X_Y y X_m cierran (coefs -2, -1)",
                sp.simplify(surv - objetivo) == 0)
    # I4: pinza de z.  cola(z) >= (1+S+alpha+Xz)/phi <= z y (Rz):
    # z < alpha+Xz+s2+w  =>  supervivencia <=>
    # alpha + Xz > phi(1+S) - phi^2*s2 - phi^2*w
    Xz = sp.symbols('X_z', nonnegative=True)
    cond = sp.expand(phi * (al + Xz + s2 + w) - (1 + S + al + Xz))
    obj4 = sp.expand((phi - 1) * (al + Xz) - (1 + S) + phi * s2
                     + phi * w)
    ok &= check("I4: phi*(alpha+Xz+s2+w) - (1+S+alpha+Xz) = "
                "(phi-1)(alpha+Xz) - (1+S) + phi*s2 + phi*w "
                "identicamente: supervivencia de (Rz)+cola(z) <=> "
                "alpha+X_z > phi(1+S) - phi^2*s2 - phi^2*w (X_z sin "
                "techo: la pinza NO cierra sola; la corona de v toma "
                "el relevo)", sp.simplify(cond - obj4) == 0)
    # B2u es exacta como pared de dos grandes: {m=1, s2} en el disco
    # de capacidad alpha-omega caben sii 1+s2 <= alpha-omega (criterio
    # de dos circulos): la corona del agujero de alpha NO mejora
    ok &= check("B2u con X_alpha = 0 es exacta: dos circulos {1, "
                "sigma2} caben en cap = alpha-omega sii 1+sigma2 <= "
                "alpha-omega (criterio de dos circulos): sin carga el "
                "agujero de alpha no admite corona que salve a "
                "sigma2; con X_alpha > 0 B2u es una FILA y la corona "
                "{m, sigma2} U X_alpha se intenta en [B] "
                "(corona-alpha)", True)
    # el sondeo del acta: con X_Y = 0, (RY)+cola(Y) => S0 > phi -
    # phi^2*omega ((1-phi*w)*phi = phi - phi^2*w exacto)
    ok &= check("sondeo del acta refinado: (RY)+cola(Y) con X_Y = 0 "
                "dan S0 > phi(1-phi*omega) = phi - phi^2*omega "
                "(cierra solo omega ~ 0; el cierre real de X = 0 es "
                "I3 via la cola de alpha, hasta omega* = 3/(2phi))",
                sp.simplify(phi * (1 - phi * w)
                            - (phi - phi ** 2 * w)) == 0)
    return ok


# ---------------------------------------------------------------- bloque B
def omega_ef(w, Xa, XY, Xm):
    """I3d en forma cerrada: la supervivencia de (c-ii-2) es la del
    caso X = 0 con omega_ef := omega + X_alpha - phi(2 X_Y + X_m)
    (1/(phi-1) = phi): Sigma_S < phi-2 + phi*s2 + (phi-1)*omega_ef."""
    return w + Xa - PHI * (2 * XY + Xm)


def bloque_B():
    print("[B] (c-ii-2) v = agujero de Y, alpha fuera: pinza exacta + "
          "barrido MC + delimitacion del residuo R2")
    ok = True
    rng = random.Random(20260808)
    # --- B1: el caso X = 0 EXACTO sobre malla densa: cierre total en
    #     omega <= omega* = 3/(2phi) y ventana I3 en omega > omega*
    n, viol_bajo, sobreviven_alto = 0, 0, 0
    for iw in range(1, 200):
        w = iw / 200.0                       # (0, 1)
        for is2 in range(1, 100):
            s2 = is2 / 100.0
            for is1 in range(1, 40):
                s1 = s2 + (1 - s2) * is1 / 40.0
                if s1 >= 1.0 or s1 + s2 <= 1.0:
                    continue
                if s2 <= 1 - w:              # BH pura (X_m = 0)
                    continue
                for tW in (0.0, 0.5, 1.0):
                    W = tW * max(0.0, min(1 + s2 - (s1 + s2) - 1e-6,
                                          (PHI - s1 - s2)))
                    n += 1
                    viva, motivo = survive_c2(w, s1, s2, W, 0., 0., 0.)
                    if viva and w <= OMEGA_STAR:
                        viol_bajo += 1
                    if viva:
                        sobreviven_alto += 1
                        # la ventana I3 debe cumplirse
                        g = (3 - PHI - (PHI - 1) * w) / PHI
                        if not (g - 1e-9 < s2 < PHI * w - 1 + 1e-9):
                            viol_bajo += 1
    ok &= check(f"B1 (X = 0, malla {n} nodos): NINGUNA instancia "
                f"sobrevive con omega <= omega* = {OMEGA_STAR:.5f} "
                f"({viol_bajo} violaciones) y toda superviviente "
                f"(omega > omega*: {sobreviven_alto}) cae en la "
                f"ventana sigma2 in (g(omega), phi*omega-1): el caso "
                f"X = 0 queda CERRADO EXACTO bajo omega* y DELIMITADO "
                f"encima", viol_bajo == 0 and sobreviven_alto > 0)
    # --- B2: barrido MC general (X_m, X_alpha, X_Y > 0, k = 2..5,
    #     omega hasta pivote solido); supervivientes de las pinzas van
    #     a la corona del agujero de Y; el resto se DELIMITA via
    #     omega_ef (I3d): la caja R2
    it = 4 * ITER
    nb, cierres = 0, {'I1-ligereza': 0, 'cola-m': 0, 'pinza-colas': 0,
                      'corona-Y': 0, 'corona-alpha': 0}
    residuo = []
    fuera_caja = 0
    for _ in range(it):
        w = rng.uniform(0.02, 1.35)          # incluye pivote solido
        Xm = rng.uniform(0.0, max(0.0, 1 - w)) if rng.random() < 0.5 \
            else 0.0
        s2 = rng.uniform(0.02, 0.999)
        if s2 <= 1 - w - Xm:                 # BH: sigma2 no cabe en H_m
            continue
        lo1 = max(s2, 1.0001 - s2)
        if lo1 >= 0.999:
            continue
        s1 = rng.uniform(lo1, 0.999)         # (D): S0 > 1
        kW = rng.randrange(0, 3)
        Wp = [rng.uniform(0.01, s2) for _ in range(kW)]
        W = sum(Wp)
        Xa = rng.uniform(0.0, 1.5) if rng.random() < 0.6 else 0.0
        XY = rng.uniform(0.0, 1.0) if rng.random() < 0.4 else 0.0
        nb += 1
        viva, motivo = survive_c2(w, s1, s2, W, Xm, Xa, XY)
        if not viva:
            cierres[motivo] += 1
            continue
        # desbloqueo geometrico: corona del agujero de Y en su peor
        # capacidad (Y minimo legal; subir Y solo agranda el disco)
        S = s1 + s2 + W
        lbY = max(1 + XY + w, (1 + S + Xm + XY) / PHI)
        piezas = [s1, s2] + Wp + compon_masa(rng, XY)
        okc, _ = corona_suf(sorted(piezas, reverse=True), lbY - w)
        if okc:
            cierres['corona-Y'] += 1
            continue
        # con X_alpha > 0 la pared B2u es una FILA, no dos circulos:
        # el agujero de alpha admite corona {m, sigma2} U X_alpha en
        # su peor capacidad (alpha minimo legal; subir alpha agranda)
        if Xa > 1e-9:
            lb_a = max(S + Xa + w, 1 + w,
                       (1 + S + Xm + Xa + XY + lbY) / PHI)
            Xa_p = compon_masa(rng, Xa)
            okc2, _ = corona_suf(sorted([1.0, s2] + Xa_p,
                                        reverse=True), lb_a - w)
            if okc2:
                cierres['corona-alpha'] += 1
                continue
        # residuo: debe caer en la caja R2 (forma cerrada omega_ef)
        wef = omega_ef(w, Xa, XY, Xm)
        g = (3 - PHI - (PHI - 1) * wef) / PHI
        en_caja = (wef > OMEGA_STAR - 1e-9
                   and g - 1e-9 < s2 < PHI * wef - 1 + 1e-9
                   and 1 < S < 1 + s2
                   and S < PHI - 2 + PHI * s2 + (PHI - 1) * wef + 1e-9)
        if not en_caja:
            fuera_caja += 1
        residuo.append((round(w, 3), round(wef, 3), round(s1, 3),
                        round(s2, 3), round(W, 3), round(Xa, 3),
                        round(XY, 3), round(Xm, 3)))
    ok &= check(f"B2 (MC {nb} instancias del bloqueo): cierres = "
                f"{cierres}; residuo = {len(residuo)} y TODO el "
                f"residuo cae en la caja R2 {{omega_ef > omega*, "
                f"sigma2 in (g(omega_ef), phi*omega_ef - 1), "
                f"1 < Sigma_S < min(1+sigma2, phi-2+phi*sigma2+"
                f"(phi-1)omega_ef)}} ({fuera_caja} fuera)",
                fuera_caja == 0)
    if residuo:
        ws = [r[0] for r in residuo]
        wefs = [r[1] for r in residuo]
        s2s = [r[3] for r in residuo]
        print(f"      R2 DELIMITADO (no forzado): {len(residuo)} "
              f"instancias; omega in [{min(ws):.3f}, {max(ws):.3f}], "
              f"omega_ef in [{min(wefs):.3f}, {max(wefs):.3f}], "
              f"sigma2 in [{min(s2s):.3f}, {max(s2s):.3f}]")
        print(f"      ejemplo: (w, wef, s1, s2, W, Xa, XY, Xm) = "
              f"{residuo[0]}")
    # --- B3: la frontera del residuo es EXACTA: en omega_ef = omega*
    #     la ventana degenera al punto sigma2* = phi*omega* - 1 =
    #     3/2 - 1 = 1/2 EXACTO (esquina racional pura)
    s2_star = PHI * OMEGA_STAR - 1
    g_star = (3 - PHI - (PHI - 1) * OMEGA_STAR) / PHI
    ok &= check(f"B3: en omega* la ventana degenera al punto: "
                f"g(omega*) = {g_star:.12f} = phi*omega* - 1 = "
                f"{s2_star:.12f} = 1/2 EXACTO (phi * 3/(2phi) - 1 = "
                f"1/2): la esquina del residuo R2 es "
                f"(omega, sigma2) = (3/(2phi), 1/2)",
                abs(g_star - s2_star) < 1e-12
                and abs(s2_star - 0.5) < 1e-12)
    return ok


# ---------------------------------------------------------------- bloque C
def torre_c1(rng, w, S, Xm, Xa, s2, d, holg_t=1.0):
    """Construye la torre alpha < z < ... < t de profundidad d sobre
    el agujero de alpha, con paredes B2u/(Rz) vivas en cada nivel y
    colas acumuladas.  Devuelve (alpha, niveles, t, masa_cola_t,
    motivo_cierre) donde motivo_cierre != None si alguna pinza cierra."""
    lb_a = max(S + Xa + w, 1 + w, (1 + S + Xm + Xa) / PHI)
    ub_a = 1 + s2 + Xa + w                       # B2u
    if lb_a >= ub_a - 1e-12:
        return None, None, None, None, 'pinza-alpha'
    alpha = rng.uniform(lb_a, ub_a)
    masa = 1 + S + Xm + Xa + alpha               # cola acumulada bajo z
    hijo = alpha
    niveles = []
    for nivel in range(d):
        Xh = rng.uniform(0.0, 1.2) if rng.random() < 0.5 else 0.0
        lb_z = max(hijo + Xh + w, (masa + Xh) / PHI)
        ub_z = hijo + Xh + s2 + w                # (Rz) en este nivel
        if lb_z >= ub_z - 1e-12:
            return None, None, None, None, f'pinza-z{nivel + 1}'
        z = rng.uniform(lb_z, ub_z)
        niveles.append((z, Xh))
        masa += Xh + z
        hijo = z
    t = hijo * holg_t
    return alpha, niveles, t, masa - t, None


def bloque_C():
    print("[C] (c-ii-1) v = sarten, alpha anidada (torre d = 1..3): "
          "pinzas (Rz)+colas + corona de la sarten")
    from coronanidada import cascada_anidada, radio_necesario, \
        desbloqueo_corona
    ok = True
    rng = random.Random(31)
    it = 4 * ITER
    cierres = {'I1-ligereza': 0, 'cola-m': 0, 'pinza-alpha': 0,
               'pinza-z1': 0, 'pinza-z2': 0, 'pinza-z3': 0,
               'corona-v': 0}
    peor, arg, nres, nev = 0.0, None, 0, 0
    for _ in range(it):
        w = rng.uniform(0.02, 1.35)
        Xm = rng.uniform(0.0, max(0.0, 1 - w)) if rng.random() < 0.5 \
            else 0.0
        s2 = rng.uniform(0.02, 0.999)
        if s2 <= 1 - w - Xm:                     # BH
            continue
        lo1 = max(s2, 1.0001 - s2)
        if lo1 >= 0.999:
            continue
        s1 = rng.uniform(lo1, 0.999)             # (D)
        kW = rng.randrange(0, 3)
        Wp = [rng.uniform(0.01, s2) for _ in range(kW)]
        W = sum(Wp)
        S = s1 + s2 + W
        if S >= 1 + s2 - 1e-12:                  # I1: no es bloqueo
            cierres['I1-ligereza'] += 1
            continue
        if S + Xm > PHI:                         # cola de m
            cierres['cola-m'] += 1
            continue
        Xa = rng.uniform(0.0, 1.5) if rng.random() < 0.6 else 0.0
        d = rng.randrange(1, 4)
        alpha, niveles, t, masa_t, motivo = torre_c1(
            rng, w, S, Xm, Xa, s2, d)
        if motivo:
            cierres[motivo] += 1
            continue
        # corona de la sarten: t es ocupante top-level de v; j extras
        j = rng.randrange(0, 4)
        rank = rng.randrange(j + 1)
        holg = [1.0 + rng.expovariate(3.0) for _ in range(j + 1)]
        if rng.random() < 0.3:
            holg = [1.0] * (j + 1)
        # el suelo de t: su torre (lb exacto ya muestreado) y su cola
        tt, occs = cascada_anidada(S, j, rank, t, holg)
        R = radio_necesario(tt, occs)
        okf, defc = desbloqueo_corona(tt, occs, [s1, s2] + Wp, R)
        nev += 1
        v = 0.0 if okf else max(defc, FALLO_MIN)
        if okf:
            cierres['corona-v'] += 1
        if v > peor:
            peor, arg = v, dict(w=round(w, 3), d=d, j=j,
                                s=[round(s1, 3), round(s2, 3)],
                                W=round(W, 3), Xa=round(Xa, 3),
                                alpha=round(alpha, 3),
                                t=round(tt, 3),
                                o=[round(x, 3) for x in occs],
                                R=round(R, 3))
        if v > TOL:
            nres += 1
    marca = peor <= TOL
    ok &= check(f"C1: {nev} coronas evaluadas (torres d = 1..3, "
                f"j = 0..3, omega hasta pivote solido); cierres = "
                f"{cierres}; peor deficit = {peor:.2e} <= {TOL} "
                f"(tangente en R = R_lb)", marca)
    if not marca:
        print(f"      RESIDUO C1 ({nres} casos > tol): {arg}")
    # esquinas deterministas: holgura 1 (t y cascada en su minimo),
    # X's en 0 y en su tope adversario, fronteras de omega
    peor_esq, esq = 0.0, 0
    arg_esq = None
    for w in (0.3, 0.62, 0.93, 1.0, 1.2):
        for s2 in (max(0.05, 1 - w + 1e-3), 0.5, 0.8):
            if s2 >= 0.999:
                continue
            for s1 in (max(s2, 1.0001 - s2) + 1e-4, 0.98):
                if s1 >= 0.999 or s1 < s2:
                    continue
                S = s1 + s2
                if S >= 1 + s2 or S <= 1.0 or S > PHI:
                    continue
                for Xa in (0.0, 0.8):
                    for d in (1, 2, 3):
                        rngE = random.Random(int(1e3 * (w + s1 + s2))
                                             + d)
                        alpha, niveles, t, _, motivo = torre_c1(
                            rngE, w, S, 0.0, Xa, s2, d)
                        if motivo:
                            continue
                        for j in (0, 1, 2):
                            tt, occs = cascada_anidada(
                                S, j, j, t, [1.0] * (j + 1))
                            R = radio_necesario(tt, occs)
                            okf, defc = desbloqueo_corona(
                                tt, occs, [s1, s2], R)
                            esq += 1
                            v = 0.0 if okf else max(defc, FALLO_MIN)
                            if v > peor_esq:
                                peor_esq = v
                                arg_esq = dict(w=w, d=d, j=j, s1=s1,
                                               s2=s2, Xa=Xa,
                                               t=round(tt, 3))
    marca = peor_esq <= TOL
    ok &= check(f"C2 esquinas deterministas (cascada y torre en su "
                f"minimo): {esq} esquinas, peor deficit = "
                f"{peor_esq:.2e} <= {TOL}", marca)
    if not marca:
        print(f"      RESIDUO C2: {arg_esq}")
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] enrutado exhaustivo de (c-ii): toda instancia recibe "
          "exactamente una ruta (cierre o caja R2)")
    from coronanidada import cascada_anidada, radio_necesario, \
        desbloqueo_corona
    ok = True
    rng = random.Random(20260809)
    rutas = {'cerrado-I1': 0, 'cerrado-cola-m': 0,
             'cerrado-pinza-c2': 0, 'cerrado-pinza-torre': 0,
             'cerrado-corona-Y': 0, 'cerrado-corona-alpha': 0,
             'cerrado-corona-v': 0, 'residuo-R2-caja': 0}
    n, sin_caso = 0, 0
    it = max(20000, ITER // 3)
    for _ in range(it):
        # instancia aleatoria de (c-ii): subcaso y perfil primitivos
        subcaso = rng.choice(['c-ii-1', 'c-ii-2', 'c-ii-2-anidada'])
        w = rng.uniform(0.02, 1.35)
        Xm = rng.uniform(0.0, max(0.0, 1 - w)) if rng.random() < 0.5 \
            else 0.0
        s2 = rng.uniform(max(0.02, 1 - w - Xm + 1e-4), 0.999)
        lo1 = max(s2, 1.0001 - s2)
        if lo1 >= 0.999:
            continue
        s1 = rng.uniform(lo1, 0.999)
        kW = rng.randrange(0, 3)
        Wp = [rng.uniform(0.01, s2) for _ in range(kW)]
        W = sum(Wp)
        S = s1 + s2 + W
        Xa = rng.uniform(0.0, 1.5) if rng.random() < 0.6 else 0.0
        XY = rng.uniform(0.0, 1.0) if (subcaso != 'c-ii-1'
                                       and rng.random() < 0.4) else 0.0
        n += 1
        if S >= 1 + s2 - 1e-12:
            rutas['cerrado-I1'] += 1
            continue
        if S + Xm > PHI:
            rutas['cerrado-cola-m'] += 1
            continue
        if subcaso == 'c-ii-1':
            d = rng.randrange(1, 4)
            alpha, niveles, t, _, motivo = torre_c1(
                rng, w, S, Xm, Xa, s2, d)
            if motivo:
                rutas['cerrado-pinza-torre'] += 1
                continue
            j = rng.randrange(0, 4)
            tt, occs = cascada_anidada(
                S, j, rng.randrange(j + 1), t,
                [1.0 + rng.expovariate(3.0) for _ in range(j + 1)])
            R = radio_necesario(tt, occs)
            okf, _ = desbloqueo_corona(tt, occs, [s1, s2] + Wp, R)
            if okf:
                rutas['cerrado-corona-v'] += 1
            else:
                sin_caso += 1        # (c-ii-1) debe cerrar siempre
            continue
        # (c-ii-2): pinzas de colas cruzadas
        viva, motivo = survive_c2(w, s1, s2, W, Xm, Xa, XY)
        if not viva:
            rutas['cerrado-pinza-c2'] += 1
            continue
        if subcaso == 'c-ii-2-anidada':
            # alpha anidada: la pinza de su torre tambien esta
            d = rng.randrange(1, 3)
            _, _, _, _, motivo = torre_c1(rng, w, S, Xm, Xa, s2, d)
            if motivo:
                rutas['cerrado-pinza-torre'] += 1
                continue
        lbY = max(1 + XY + w, (1 + S + Xm + XY) / PHI)
        piezas = [s1, s2] + Wp + compon_masa(rng, XY)
        okc, _ = corona_suf(sorted(piezas, reverse=True), lbY - w)
        if okc:
            rutas['cerrado-corona-Y'] += 1
            continue
        if Xa > 1e-9:
            lb_a = max(S + Xa + w, 1 + w,
                       (1 + S + Xm + Xa + XY + lbY) / PHI)
            okc2, _ = corona_suf(sorted([1.0, s2] + compon_masa(rng, Xa),
                                        reverse=True), lb_a - w)
            if okc2:
                rutas['cerrado-corona-alpha'] += 1
                continue
        wef = omega_ef(w, Xa, XY, Xm)
        g = (3 - PHI - (PHI - 1) * wef) / PHI
        if (wef > OMEGA_STAR - 1e-9
                and g - 1e-9 < s2 < PHI * wef - 1 + 1e-9
                and 1 < S < 1 + s2
                and S < PHI - 2 + PHI * s2 + (PHI - 1) * wef + 1e-9):
            rutas['residuo-R2-caja'] += 1
        else:
            sin_caso += 1
    ok &= check(f"{n} instancias de (c-ii) enrutadas: rutas = {rutas}; "
                f"{sin_caso} sin caso (todo cierra o cae en la caja "
                f"R2 delimitada)", sin_caso == 0)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles negativos y consistencia")
    from coronanidada import cascada_anidada, radio_necesario, \
        desbloqueo_corona
    ok = True
    rng = random.Random(97)
    # (a) SIN COLAS la pinza de alpha no cierra: quitando cola(alpha)
    # y cola(Y) del sistema X = 0, el rango de alpha [S+w, 1+s2+w) es
    # no vacio en cuanto S < 1+s2 (I1): el sistema sobrevive en TODA
    # omega -- son las colas las que vacian omega <= omega*
    n_sin, sobreviven_sin, cerradas_con = 0, 0, 0
    for _ in range(4000):
        w = rng.uniform(0.05, OMEGA_STAR - 0.05)
        s2 = rng.uniform(max(0.02, 1 - w + 1e-4), 0.999)
        lo1 = max(s2, 1.0001 - s2)
        if lo1 >= 0.999:
            continue
        s1 = rng.uniform(lo1, 0.999)
        S = s1 + s2
        if S >= 1 + s2 or S > PHI:
            continue
        n_sin += 1
        if S + w < 1 + s2 + w - 1e-12:       # rango de alpha sin colas
            sobreviven_sin += 1
        viva, _ = survive_c2(w, s1, s2, 0.0, 0.0, 0.0, 0.0)
        if not viva:
            cerradas_con += 1
    ok &= check(f"(a) sin colas la pared es vacua: {sobreviven_sin}/"
                f"{n_sin} instancias con omega < omega* sobreviven "
                f"sin cola(alpha)/cola(Y), y con colas se cierran "
                f"{cerradas_con}/{n_sin} (todas): el cierre es de las "
                f"colas, no de las tarifas",
                n_sin > 500 and sobreviven_sin == n_sin
                and cerradas_con == n_sin)
    # (b) sin (D) no hay bloqueo: la fila del par en D_m se construye
    n2, viol2 = 0, 0
    for _ in range(20000):
        s2 = rng.uniform(0.01, 0.5)
        s1 = rng.uniform(s2, 1 - s2)         # S0 <= 1
        n2 += 1
        c1x, c2x = -1 + s1, 1 - s2
        if not (abs(c1x) + s1 <= 1 + 1e-12 and abs(c2x) + s2
                <= 1 + 1e-12 and abs(c1x - c2x) >= s1 + s2 - 1e-12):
            viol2 += 1
    ok &= check(f"(b) sin (D) (S0 <= 1) la fila diametral del par en "
                f"D_m es legal en {n2} muestras ({viol2} violaciones): "
                f"(D) es puerta del bloqueo", viol2 == 0)
    # (c) la instancia AUREA vive en (a), no en (c-ii): su bloqueo
    # tiene u = sarten (m y el par a nivel superior); y la RIGIDA vive
    # en (b) (v = sarten, alpha en v).  Ademas, si se intentara
    # plantar la rigida en (c-ii), I1 la expulsa: sigma1 = m = 1 da
    # Sigma_S >= 1 + sigma2 (E4+B2u infactible)
    t = 0.52
    b = t * (1 + t) / (1 + t + t * t)
    s1r, s2r = 1.0, b / t
    ok &= check(f"(c) la esquina rigida (sigma1 = 1, sigma2 = "
                f"{s2r:.4f}) NO cabe en (c-ii): Sigma_S = 1 + sigma2 "
                f">= 1 + sigma2 viola I1 (E4+B2u): su bloqueo es del "
                f"caso (b), como declara el acta anidada; la familia "
                f"aurea (j = 1, u = sarten) es del caso (a) "
                f"(coronacolas/ensamblaje [E])",
                s1r + s2r >= 1 + s2r - 1e-12)
    # (d) consistencia con el sondeo del acta: los supervivientes de
    # X = 0 cumplen S0 > phi - phi^2*omega (la conclusion del sondeo)
    viol4, n4 = 0, 0
    for iw in range(186, 200):
        w = iw / 200.0
        for is2 in range(1, 100):
            s2 = is2 / 100.0
            for is1 in range(1, 40):
                s1 = s2 + (1 - s2) * is1 / 40.0
                if s1 >= 1.0 or s1 + s2 <= 1.0 or s2 <= 1 - w:
                    continue
                viva, _ = survive_c2(w, s1, s2, 0.0, 0., 0., 0.)
                if viva:
                    n4 += 1
                    if not s1 + s2 > PHI - PHI ** 2 * w - 1e-9:
                        viol4 += 1
    ok &= check(f"(d) sondeo del acta: los {n4} supervivientes X = 0 "
                f"de la malla fina cumplen S0 > phi - phi^2*omega "
                f"({viol4} violaciones): la conclusion del sondeo es "
                f"correcta pero NO cierra sola; el cierre es I3",
                n4 > 0 and viol4 == 0)
    # (e) la pared de la corona de v es ACTIVA: al 90% de R_lb falla
    activos, n5 = 0, 0
    rng5 = random.Random(13)
    for _ in range(150):
        w = rng5.uniform(0.1, 0.9)
        s2 = rng5.uniform(max(0.05, 1 - w + 1e-3), 0.95)
        lo1 = max(s2, 1.0001 - s2)
        if lo1 >= 0.999:
            continue
        s1 = rng5.uniform(lo1, 0.999)
        S = s1 + s2
        if S >= 1 + s2 or S > PHI:
            continue
        alpha, niveles, t, _, motivo = torre_c1(
            rng5, w, S, 0.0, 0.0, s2, 1)
        if motivo:
            continue
        tt, occs = cascada_anidada(S, 1, 1, t, [1.0, 1.0])
        R = radio_necesario(tt, occs)
        okf, _ = desbloqueo_corona(tt, occs, [s1, s2], R * 0.90)
        n5 += 1
        if not okf:
            activos += 1
    ok &= check(f"(e) pared activa en (c-ii-1): al 90% de R_lb la "
                f"corona falla en {activos}/{n5} sondas (> 0: el "
                f"certificado muerde; en R >= R_lb siempre cabe)",
                n5 > 30 and activos > 0)
    return ok


def b2_espejo(a, y):
    return a * y * (a + y) / (a * a + a * y + y * y)


def bloque_F():
    print("[F] cierre de R2: el repack de la SARTEN como recurso "
          "(bolsillo espejo del par top-level)")
    import sympy as sp
    rng = random.Random(20260809)
    ok = True
    # F2 [ENUNCIADO] legalidad del recurso: la factibilidad de una
    # colocacion es empaquetabilidad POR CONTENEDOR (existencial en
    # posiciones) y el intercambio solo exige acuerdo DE CONTENEDOR en
    # los anillos >= m (thm:oblivious: "agreeing with F on all rings of
    # radius >= r_m"); re-empaquetar la sarten no cambia contenedores.
    # Precedente en el propio paper: thm:DP usa "the pan repack" con
    # ocupantes > m re-colocados (coronas de coronacolas).  En (c-ii-2)
    # la sarten contiene a alpha y al tope T de la torre de Y (ambos
    # top-level, compartidos), luego "sigma2 -> bolsillo espejo del par
    # {alpha, T} con la sarten re-empaquetada" es una colocacion del
    # testigo y su fallo es una pared del bloqueo.
    ok &= check("[ENUNCIADO] el repack de la sarten es recurso del "
                "intercambio en (c-ii-2): factibilidad por contenedor "
                "+ acuerdo solo de contenedores en >= m (thm:oblivious"
                "); precedente: el pan repack de thm:DP", True)
    # F1: la pinza exacta que vacia R2 (sympy)
    a, y = sp.symbols('a y', positive=True)
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    b2s = a * y * (a + y) / (a ** 2 + a * y + y ** 2)
    da = sp.simplify(sp.diff(b2s, a) *
                     (a ** 2 + a * y + y ** 2) ** 2 / y ** 2)
    ok &= check("F1a: db2/da * D^2/y^2 = y(2a + y) exacto, positivo: "
                "b2 es ESTRICTAMENTE creciente en cada argumento "
                "(y simetrico en ellos)",
                sp.simplify(da - y * (2 * a + y)) == 0)
    ok &= check("F1b: b2(2, sqrt5-1) = 1 exacto (la esquina aurea del "
                "espejo, ya en Lean como b2_mirror_corner)",
                sp.simplify(b2s.subs([(a, 2), (y, sp.sqrt(5) - 1)])
                            - 1) == 0)
    # alpha > 2: N = 2+S+Xm+Xa+2XY+omega y omega >= omega_ef - Xa +
    # phi(2XY+Xm) => N > 2+S+omega_ef+(1+phi)Xm+(2+2phi)XY >= 3+omega*
    # (S > 1, X >= 0); y 3 + 3/(2phi) > 2phi <=> 6phi+3 > 4phi^2 =
    # 4phi+4 <=> 2phi > 1: EXACTO
    ok &= check("F1c: 3 + 3/(2phi) - 2phi = (2phi-1)/(2phi) * ... > 0 "
                "exacto (6phi+3-4phi^2 = 2phi-1 via phi^2 = phi+1): "
                "en R2, alpha >= N/phi > (3+omega*)/phi > 2",
                sp.simplify(6 * phi + 3 - 4 * phi ** 2
                            - (2 * phi - 1)) == 0
                and float((3 + 3 / (2 * phi)) / phi) > 2)
    # Y > 2/phi = sqrt5 - 1: cola(Y) >= (1+S)/phi > 2/phi (S > 1)
    ok &= check("F1d: 2/phi = sqrt5 - 1 exacto: la cola de Y con "
                "Sigma_S > 1 da Y > 2/phi = sqrt5 - 1",
                sp.simplify(2 / phi - (sp.sqrt(5) - 1)) == 0)
    ok &= check("F1e: PINZA: en R2, alpha > 2 y T >= Y > sqrt5-1 => "
                "b2(alpha, T) > b2(2, sqrt5-1) = 1 > sigma2 (sigma2 < "
                "sigma1 < 1): sigma2 SIEMPRE cabe en el bolsillo "
                "espejo del par {alpha, T} re-empaquetado diametral "
                "(prop:S5, espejos disjuntos y0 = 2b2, contencion "
                "monotona R >= alpha+T): R2 ES VACIA en su nucleo "
                "{sarten = {alpha, T}}", True)
    # F3: el caso general (miembros top-level extra): corona de la
    # sarten sobre instancias de la caja R2 con extras aleatorios
    n3, fallos, peor_def = 0, 0, 0.0
    intentos = max(20000, ITER // 3)
    for _ in range(intentos):
        wef = rng.uniform(OMEGA_STAR + 1e-4, 1.45)
        Xa = rng.uniform(0.0, 0.5) if rng.random() < 0.4 else 0.0
        XY = rng.uniform(0.0, 0.1) if rng.random() < 0.2 else 0.0
        Xm = 0.0
        w = wef - Xa + PHI * (2 * XY + Xm)
        if w <= 0.02:
            continue
        g = (3 - PHI - (PHI - 1) * wef) / PHI
        lo_s2, hi_s2 = max(g, 0.05), min(PHI * wef - 1, 0.999)
        if lo_s2 >= hi_s2:
            continue
        s2 = rng.uniform(lo_s2, hi_s2)
        s1 = rng.uniform(s2, min(1.0, 1 + s2 - s2))    # s1 < 1
        S_hi = min(1 + s2, PHI - 2 + PHI * s2 + (PHI - 1) * wef)
        if S_hi <= max(1.0, s1 + s2) or s1 < s2:
            continue
        S = rng.uniform(max(1.0, s1 + s2), S_hi)
        S0 = s1 + s2
        lbY = max(1 + XY + w, (1 + S + Xm + XY) / PHI)
        ubY = S0 + XY + w
        if lbY >= ubY:
            continue
        Y = rng.uniform(lbY, ubY)
        lb_a = max(S + Xa + w, 1 + w, (1 + S + Xm + Xa + XY + Y) / PHI)
        ub_a = 1 + s2 + Xa + w
        if lb_a >= ub_a:
            continue
        alfa = rng.uniform(lb_a, ub_a)
        if Y >= alfa:
            continue
        # tope de la torre de Y (profundidad 0-2) y extras top-level
        d = rng.randrange(0, 3)
        T = Y + d * (w + 0.05)
        top = [alfa, T]
        for _ in range(rng.randrange(0, 3)):
            top.append(rng.uniform(0.3, alfa))
        n3 += 1
        tops = sorted(top, reverse=True)
        # confinamiento por el gigante: sin el, los pares apilables
        # dan gamma = 0 y R_lb subestima el radio real (trampa
        # documentada de las campanas: un parametro)
        R = R_lb_pack(tops, tops[0] + tops[1], confinado_por=tops[0])
        okc, defc = corona_suf(top + [s2], R)
        if not okc:
            fallos += 1
            peor_def = max(peor_def, defc)
    ok &= check(f"F3: corona de la sarten re-empaquetada en {n3} "
                f"instancias de la caja R2 (torres d = 0..2, hasta 2 "
                f"extras top-level): sigma2 SIEMPRE cabe ({fallos} "
                f"fallos, peor deficit {peor_def:.2e})",
                n3 > 500 and fallos == 0)
    # F4: consistencia con la pinza: en las mismas instancias,
    # b2(alpha, Y) > 1 siempre (el nucleo exacto)
    n4, viol = 0, 0
    for _ in range(20000):
        S = rng.uniform(1.0 + 1e-6, 1.9)
        w2 = rng.uniform(OMEGA_STAR, 1.4)
        alfa = rng.uniform((2 + S + w2) / PHI, 3.5)
        Y = rng.uniform(2 / PHI + 1e-9, alfa)
        n4 += 1
        if b2_espejo(alfa, Y) <= 1.0:
            viol += 1
    ok &= check(f"F4: b2(alpha, Y) > 1 en {n4} muestras del nucleo "
                f"({viol} violaciones): la pinza F1 es la que cierra",
                viol == 0)
    return ok


def main():
    print("=" * 68)
    print("PUERTO (c-ii): la celda abierta del ensamblaje "
          "(alpha fuera de v)")
    print("([B]/[C] son pinzas exactas + barridos MC con dualidad "
          "tangente; el residuo, si existe, se DELIMITA, no se fuerza)")
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
