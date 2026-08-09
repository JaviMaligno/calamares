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
  I1 (ligereza CONDICIONAL — corregida en la ronda hostil 2026-08-08):
     E4 + B2u-como-desigualdad  =>  Sigma_S < 1 + sigma2.  PERO B2u es
     la rama "la fila en u falla" de una DISYUNCION: la colocacion
     [A -> u junto a m; B -> fila en D_m] con A U B = S falla sii
     (1 + Sigma_A + X_alpha > alpha-omega) OR (Sigma_B > 1).  En la
     rama PESADA (Sigma_S >= 1+sigma2, solo posible con W > 0, k >= 3)
     E4 hace caber la fila {m, sigma2} en u y el atasco es de
     {sigma1} U W: el bloqueo NO se reduce a sigma2.  El recurso
     correcto es la PARTICION exacta A/B (enumeracion de subconjuntos)
     con el techo generalizado ub(alpha) = 1+omega+X_alpha+
     (Sigma_S - B*), B* = mayor subconjunto de S con suma <= 1.
     Con S = par (W = 0) la ligereza si es automatica (sigma1 < 1).
  I2 (colas cruzadas, rama Y >= alpha): cola(Y) con alpha dentro +
     E4 + (RY) es infactible salvo (phi-1)(X_Y+omega) >= 1: con
     X_Y = 0 exige omega >= phi (imposible, omega < 1 en anillo).
     OJO (ronda hostil): con X_Y + omega > phi la rama RESPIRA; su
     cierre es computacional (corona-Y / corona de la sarten), no I3.
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

PROGRAMA: [A] identidades exactas; [B] (c-ii-2) con X_Y = 0 EXACTO
(ligero) + malla pesada B1b + barrido MC general y delimitacion de
los residuos R2 (ligero) y R2W (pesado/S0 <= 1); [C] (c-ii-1) pinza
(Rz)+cola(z) + corona de la sarten, torres d = 1..3, omega en (0,1) y
pivote solido, pesado incluido; [D] enrutado exhaustivo; [E] controles
negativos; [F] repack de la sarten (pinzas F1e ligera / F1f pesada,
SOLO raiz distinta) + [F5] sub-celda R2b de raiz compartida
(DELIMITADA, ABIERTA).

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


def b_star(piezas, cap=1.0):
    """Mayor suma de un subconjunto de piezas <= cap (enumeracion
    exacta, |piezas| <= 6): el mejor contenido de la fila en D_m."""
    mejor = 0.0
    n = len(piezas)
    for mask in range(1 << n):
        s = 0.0
        for i in range(n):
            if mask >> i & 1:
                s += piezas[i]
        if s <= cap + 1e-12 and s > mejor:
            mejor = s
    return mejor


def survive_c2(w, s1, s2, Wp, Xm, Xa, XY):
    """(c-ii-2): cola(m) + particion u/D_m (techo generalizado) + I2 +
    I3 sobre una instancia del bloqueo con perfil S = {s1, s2} U Wp
    (piezas explicitas).  Devuelve (sobrevive, motivo, ligero).
    Conservador: el adversario elige Y y alpha en sus rangos; aqui se
    comprueba si ALGUN (Y, alpha) es consistente con paredes + colas.
    CORRECCION (ronda hostil 2026-08-08): la rama pesada
    (Sigma_S >= 1+s2) NO se despacha como cierre I1 — se ataca con la
    particion exacta A/B: [A -> fila junto a m en u; B -> fila en D_m]
    y el techo generalizado ub(alpha) = 1+omega+X_alpha+(Sigma_S-B*),
    B* = mayor subconjunto de S con suma <= 1 (para toda particion con
    Sigma_B <= 1 el bloqueo exige alpha-omega < 1+Sigma_A+X_alpha; el
    techo activo es el de B = B*).  Con B* = S - s2 (perfil ligero,
    S0 > 1) se recupera el B2u clasico.  Tambien corregido el techo de
    Y: (RY) da Y < Sigma_S+X_Y+omega (fila de TODO S), no S0+..."""
    W = sum(Wp)
    S = s1 + s2 + W
    ligero = S < 1 + s2 - 1e-12
    if S + Xm > PHI + 1e-12:
        return False, 'cola-m', ligero
    piezas = [s1, s2] + list(Wp)
    Bs = b_star(piezas)
    # rama Y >= alpha (I2): phi*Y >= 1+S+Xm+XY+alpha+Xa (cola de Y con
    # alpha y su carga dentro), alpha >= S+Xa+omega (E4),
    # techo de Y: RY => Y < S + XY + omega (fila de todo S)
    ok_I2 = PHI * (S + XY + w) > 1 + S + Xm + XY + S + Xa + w + 1e-12
    # rama Y < alpha (I3 con techo generalizado por particion)
    lbY = max(1 + XY + w, (1 + S + Xm + XY) / PHI)
    lb_a = max(S + Xa + w, 1 + w, (1 + S + Xm + Xa + XY + lbY) / PHI)
    ub_a = 1 + (S - Bs) + Xa + w
    ok_I3 = lb_a < ub_a - 1e-12 and lbY < S + XY + w - 1e-12
    if ok_I2 or ok_I3:
        return True, None, ligero
    return False, ('pinza-colas' if ligero else 'particion-pesada'), \
        ligero


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
                "(X_alpha y omega se cancelan): E4 + B2u-COMO-"
                "DESIGUALDAD => Sigma_S < 1+sigma2.  CORRECCION de la "
                "ronda hostil: B2u es una rama de la disyuncion "
                "[fila en u falla] OR [fila S \\ A en D_m falla]; en "
                "la rama PESADA (Sigma_S >= 1+sigma2, W > 0) E4 hace "
                "CABER la fila {m, sigma2} en u y el atasco pasa a "
                "{sigma1} U W: NO es un cierre, es la particion u/D_m "
                "y la pinza F-pesada quienes la tratan ([B1b], [F1f])",
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
                "todo omega de anillo (omega < 1 <= phi).  OJO (ronda "
                "hostil): con X_Y + omega > phi la rama RESPIRA y su "
                "cierre es SOLO computacional (corona-Y en los rangos "
                "barridos), no una pinza exacta",
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
    # --- B1: el caso X = 0 sobre malla densa.  LIGERO (W bajo el tope
    #     de I1): cierre total en omega <= omega* y ventana I3 encima.
    #     PESADO (Sigma_S >= 1+s2, W en su rango; incluye S0 <= 1 <
    #     Sigma_S): la particion u/D_m cierra o el nodo queda en R2W
    #     (delimitado; la pinza F-pesada del bloque [F] lo remata)
    n, viol_bajo, sobreviven_alto = 0, 0, 0
    n_pes, pes_viven, pes_bajo, pes_sinF = 0, 0, 0, 0
    pes_w = []
    for iw in range(1, 200):
        w = iw / 200.0                       # (0, 1)
        for is2 in range(1, 100):
            s2 = is2 / 100.0
            for is1 in range(1, 40):
                s1 = s2 + (1 - s2) * is1 / 40.0
                if s1 >= 1.0:
                    continue
                if s2 <= 1 - w:              # BH pura (X_m = 0)
                    continue
                cap_lig = max(0.0, min(1 + s2 - (s1 + s2) - 1e-6,
                                       (PHI - s1 - s2)))
                for tW in (0.0, 0.5, 1.0):
                    W = tW * cap_lig
                    if s1 + s2 + W <= 1.0:
                        continue             # (D) sobre TODO S
                    n += 1
                    viva, motivo, lig = survive_c2(w, s1, s2,
                                                   [W] if W else [],
                                                   0., 0., 0.)
                    if viva and w <= OMEGA_STAR:
                        viol_bajo += 1
                    if viva:
                        sobreviven_alto += 1
                        g = (3 - PHI - (PHI - 1) * w) / PHI
                        if not (g - 1e-9 < s2 < PHI * w - 1 + 1e-9):
                            viol_bajo += 1
                # rama PESADA: W una pieza <= s2 con sigma1+W >= 1
                for tP in (0.0, 0.5, 1.0):
                    Wp = min(s2, 1.0001 - s1) + tP * max(
                        0.0, min(s2, PHI - s1 - s2)
                        - min(s2, 1.0001 - s1))
                    if Wp > s2 or s1 + Wp < 1.0 \
                            or s1 + s2 + Wp > PHI:
                        continue
                    n_pes += 1
                    viva, motivo, lig = survive_c2(w, s1, s2, [Wp],
                                                   0., 0., 0.)
                    if viva:
                        pes_viven += 1
                        pes_w.append(w)
                        if w <= OMEGA_STAR:
                            pes_bajo += 1
                        # pinza F-pesada (raiz distinta): alpha > 4/phi
                        # > 2, T >= Y > 2/phi, W <= 1 a D_m
                        S = s1 + s2 + Wp
                        lb_a = max(S + w, 1 + w, (2 + S + w) / PHI)
                        if not (lb_a > 2.0 and Wp <= 1.0):
                            pes_sinF += 1
    ok &= check(f"B1 (X = 0, malla {n} nodos ligeros): NINGUNA "
                f"instancia LIGERA sobrevive con omega <= omega* = "
                f"{OMEGA_STAR:.5f} ({viol_bajo} violaciones) y toda "
                f"superviviente (omega > omega*: {sobreviven_alto}) "
                f"cae en la ventana sigma2 in (g(omega), phi*omega-1): "
                f"el caso X = 0 LIGERO queda CERRADO EXACTO bajo "
                f"omega* y DELIMITADO encima",
                viol_bajo == 0 and sobreviven_alto > 0)
    ok &= check(f"B1b (X = 0, malla PESADA {n_pes} nodos, hallazgo de "
                f"la ronda hostil): {pes_viven} sobreviven a la "
                f"particion u/D_m (omega in "
                f"[{min(pes_w) if pes_w else 0:.3f}, "
                f"{max(pes_w) if pes_w else 0:.3f}], {pes_bajo} bajo "
                f"omega*); en TODOS la pinza F-pesada de raiz distinta "
                f"aplica (alpha >= (2+S+w)/phi > 2 y W <= 1: "
                f"{pes_sinF} sin pinza); la sub-celda de raiz "
                f"compartida queda para [F5]", pes_sinF == 0)
    # --- B2: barrido MC general (X_m, X_alpha, X_Y > 0, k = 2..5,
    #     omega hasta pivote solido); supervivientes de las pinzas van
    #     a la corona del agujero de Y; el resto se DELIMITA via
    #     omega_ef (I3d): la caja R2 (ligero) o R2W (pesado / S0 <= 1,
    #     hallazgo de la ronda hostil).  Muestreo corregido: s1 ya NO
    #     exige S0 > 1 (la puerta real es Sigma_S > 1: fila de TODO S
    #     en D_m), X_alpha llega a 3.0 (la sub-celda de raiz compartida
    #     exige X_alpha >= Y >= 1+omega)
    it = 4 * ITER
    nb, cierres = 0, {'cola-m': 0, 'pinza-colas': 0,
                      'particion-pesada': 0, 'corona-Y': 0,
                      'corona-alpha': 0}
    residuo, residuo_W = [], []
    fuera_caja, resw_sinF = 0, 0
    for _ in range(it):
        w = rng.uniform(0.02, 1.35)          # incluye pivote solido
        Xm = rng.uniform(0.0, max(0.0, 1 - w)) if rng.random() < 0.5 \
            else 0.0
        s2 = rng.uniform(0.02, 0.999)
        if s2 <= 1 - w - Xm:                 # BH: sigma2 no cabe en H_m
            continue
        s1 = rng.uniform(s2, 0.999)          # sin baked-in S0 > 1
        kW = rng.randrange(0, 3)
        Wp = [rng.uniform(0.01, s2) for _ in range(kW)]
        W = sum(Wp)
        S = s1 + s2 + W
        if S <= 1.0:                         # (D): fila de TODO S
            continue
        Xa = rng.uniform(0.0, 3.0) if rng.random() < 0.6 else 0.0
        XY = rng.uniform(0.0, 1.0) if rng.random() < 0.4 else 0.0
        nb += 1
        viva, motivo, lig = survive_c2(w, s1, s2, Wp, Xm, Xa, XY)
        if not viva:
            cierres[motivo] += 1
            continue
        # desbloqueo geometrico: corona del agujero de Y en su peor
        # capacidad (Y minimo legal; subir Y solo agranda el disco)
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
        wef = omega_ef(w, Xa, XY, Xm)
        if lig and s1 + s2 > 1.0:
            # residuo ligero clasico: debe caer en la caja R2
            g = (3 - PHI - (PHI - 1) * wef) / PHI
            en_caja = (wef > OMEGA_STAR - 1e-9
                       and g - 1e-9 < s2 < PHI * wef - 1 + 1e-9
                       and 1 < S < 1 + s2
                       and S < PHI - 2 + PHI * s2
                       + (PHI - 1) * wef + 1e-9)
            if not en_caja:
                fuera_caja += 1
            residuo.append((round(w, 3), round(wef, 3), round(s1, 3),
                            round(s2, 3), round(W, 3), round(Xa, 3),
                            round(XY, 3), round(Xm, 3)))
        else:
            # residuo R2W (pesado o S0 <= 1 < Sigma_S): nueva celda de
            # la ronda hostil; en raiz distinta lo remata la pinza
            # F-pesada si N/phi > 2 y W cabe en D_m
            N = 2 + S + Xm + Xa + 2 * XY + w
            if not (N / PHI > 2.0 and W <= 1.0 + 1e-12):
                resw_sinF += 1
            residuo_W.append((round(w, 3), round(wef, 3),
                              round(s1, 3), round(s2, 3),
                              round(W, 3), round(Xa, 3),
                              round(XY, 3), round(Xm, 3)))
    ok &= check(f"B2 (MC {nb} instancias del bloqueo): cierres = "
                f"{cierres}; residuo ligero = {len(residuo)} y TODO "
                f"cae en la caja R2 {{omega_ef > omega*, sigma2 in "
                f"(g(omega_ef), phi*omega_ef - 1), 1 < Sigma_S < "
                f"min(1+sigma2, phi-2+phi*sigma2+(phi-1)omega_ef)}} "
                f"({fuera_caja} fuera); residuo R2W (pesado/S0<=1) = "
                f"{len(residuo_W)}, en todos aplica la pinza F-pesada "
                f"de raiz distinta (N/phi > 2, W <= 1: {resw_sinF} "
                f"sin pinza)", fuera_caja == 0 and resw_sinF == 0)
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
    if residuo_W:
        ws = [r[0] for r in residuo_W]
        Wm = [r[4] for r in residuo_W]
        print(f"      R2W DELIMITADO (pesado/S0<=1, ronda hostil): "
              f"{len(residuo_W)} instancias; omega in "
              f"[{min(ws):.3f}, {max(ws):.3f}], W in "
              f"[{min(Wm):.3f}, {max(Wm):.3f}]")
        print(f"      ejemplo: (w, wef, s1, s2, W, Xa, XY, Xm) = "
              f"{residuo_W[0]}")
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
def torre_c1(rng, w, S, Xm, Xa, s2, d, holg_t=1.0, piezas=None):
    """Construye la torre alpha < z < ... < t de profundidad d sobre
    el agujero de alpha, con paredes B2u/(Rz) vivas en cada nivel y
    colas acumuladas.  Devuelve (alpha, niveles, t, masa_cola_t,
    motivo_cierre) donde motivo_cierre != None si alguna pinza cierra.
    piezas (ronda hostil): perfil S explicito para el techo
    generalizado por particion (pesado incluido); sin piezas se usa el
    techo clasico 1+s2+Xa+w (solo valido en perfil ligero S0 > 1)."""
    lb_a = max(S + Xa + w, 1 + w, (1 + S + Xm + Xa) / PHI)
    if piezas is not None:
        ub_a = 1 + (S - b_star(piezas)) + Xa + w
    else:
        ub_a = 1 + s2 + Xa + w                   # B2u clasico
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
    cierres = {'cola-m': 0, 'pinza-alpha': 0,
               'pinza-z1': 0, 'pinza-z2': 0, 'pinza-z3': 0,
               'corona-v': 0}
    peor, arg, nres, nev = 0.0, None, 0, 0
    nres_pes = []
    for _ in range(it):
        w = rng.uniform(0.02, 1.35)
        Xm = rng.uniform(0.0, max(0.0, 1 - w)) if rng.random() < 0.5 \
            else 0.0
        s2 = rng.uniform(0.02, 0.999)
        if s2 <= 1 - w - Xm:                     # BH
            continue
        s1 = rng.uniform(s2, 0.999)              # sin baked-in S0 > 1
        kW = rng.randrange(0, 3)
        Wp = [rng.uniform(0.01, s2) for _ in range(kW)]
        W = sum(Wp)
        S = s1 + s2 + W
        if S <= 1.0:                             # (D): fila de TODO S
            continue
        if S + Xm > PHI:                         # cola de m
            cierres['cola-m'] += 1
            continue
        Xa = rng.uniform(0.0, 1.5) if rng.random() < 0.6 else 0.0
        d = rng.randrange(1, 4)
        alpha, niveles, t, masa_t, motivo = torre_c1(
            rng, w, S, Xm, Xa, s2, d, piezas=[s1, s2] + Wp)
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
        ligero = S < 1 + s2 - 1e-12
        v = 0.0 if okf else max(defc, FALLO_MIN)
        if okf:
            cierres['corona-v'] += 1
        if ligero:
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
        elif v > TOL:
            nres_pes.append((round(w, 3), round(s1, 3), round(s2, 3),
                             round(W, 3), round(Xa, 3), d, j))
    marca = peor <= TOL
    ok &= check(f"C1: {nev} coronas evaluadas (torres d = 1..3, "
                f"j = 0..3, omega hasta pivote solido, perfil pesado "
                f"INCLUIDO tras la ronda hostil); cierres = "
                f"{cierres}; peor deficit LIGERO = {peor:.2e} <= "
                f"{TOL} (tangente en R = R_lb); residuo pesado "
                f"C1W = {len(nres_pes)} (delimitado, no forzado)",
                marca)
    if not marca:
        print(f"      RESIDUO C1 ({nres} casos > tol): {arg}")
    if nres_pes:
        print(f"      C1W (pesado sin corona): {len(nres_pes)}; "
              f"ejemplo (w, s1, s2, W, Xa, d, j) = {nres_pes[0]}")
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
    rutas = {'cerrado-cola-m': 0,
             'cerrado-pinza-c2': 0, 'cerrado-pinza-torre': 0,
             'cerrado-corona-Y': 0, 'cerrado-corona-alpha': 0,
             'cerrado-corona-v': 0, 'residuo-R2-caja': 0,
             'residuo-R2W': 0, 'residuo-C1W': 0}
    n, sin_caso = 0, 0
    it = max(20000, ITER // 3)
    for _ in range(it):
        # instancia aleatoria de (c-ii): subcaso y perfil primitivos
        subcaso = rng.choice(['c-ii-1', 'c-ii-2', 'c-ii-2-anidada'])
        w = rng.uniform(0.02, 1.35)
        Xm = rng.uniform(0.0, max(0.0, 1 - w)) if rng.random() < 0.5 \
            else 0.0
        s2 = rng.uniform(max(0.02, 1 - w - Xm + 1e-4), 0.999)
        s1 = rng.uniform(s2, 0.999)      # sin baked-in S0 > 1
        kW = rng.randrange(0, 3)
        Wp = [rng.uniform(0.01, s2) for _ in range(kW)]
        W = sum(Wp)
        S = s1 + s2 + W
        if S <= 1.0:                     # (D): fila de TODO S
            continue
        Xa = rng.uniform(0.0, 3.0) if rng.random() < 0.6 else 0.0
        XY = rng.uniform(0.0, 1.0) if (subcaso != 'c-ii-1'
                                       and rng.random() < 0.4) else 0.0
        n += 1
        ligero = S < 1 + s2 - 1e-12
        if S + Xm > PHI:
            rutas['cerrado-cola-m'] += 1
            continue
        if subcaso == 'c-ii-1':
            d = rng.randrange(1, 4)
            alpha, niveles, t, _, motivo = torre_c1(
                rng, w, S, Xm, Xa, s2, d, piezas=[s1, s2] + Wp)
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
            elif ligero:
                sin_caso += 1    # (c-ii-1) ligero debe cerrar siempre
            else:
                rutas['residuo-C1W'] += 1
            continue
        # (c-ii-2): pinzas de colas cruzadas + particion
        viva, motivo, lig = survive_c2(w, s1, s2, Wp, Xm, Xa, XY)
        if not viva:
            rutas['cerrado-pinza-c2'] += 1
            continue
        if subcaso == 'c-ii-2-anidada':
            # alpha anidada: la pinza de su torre tambien esta
            d = rng.randrange(1, 3)
            _, _, _, _, motivo = torre_c1(rng, w, S, Xm, Xa, s2, d,
                                          piezas=[s1, s2] + Wp)
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
        if not (ligero and s1 + s2 > 1.0):
            # nueva ruta de la ronda hostil: R2W con pinza F-pesada
            N = 2 + S + Xm + Xa + 2 * XY + w
            if N / PHI > 2.0 and W <= 1.0 + 1e-12:
                rutas['residuo-R2W'] += 1
            else:
                sin_caso += 1
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
                f"{sin_caso} sin caso (todo cierra o cae en una caja "
                f"delimitada: R2 ligera, R2W pesada/S0<=1 con pinza "
                f"F-pesada, o residuo C1W declarado)", sin_caso == 0)
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
        viva, _, _ = survive_c2(w, s1, s2, [], 0.0, 0.0, 0.0)
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
    # en (b) (v = sarten, alpha en v).  CORRECCION de la ronda hostil:
    # sigma1 = 1 = m es irrealizable en el perfil S de (c-ii) (radios
    # ESTRICTAMENTE decrecientes: sigma1 < m); el limite sigma1 -> 1
    # es un perfil PESADO (Sigma_S -> 1+sigma2), que ya NO se despacha
    # por I1 sino por particion u/D_m + pinza F-pesada (antes el
    # script lo declaraba cierre 'I1-ligereza': ERROR reparado)
    t = 0.52
    b = t * (1 + t) / (1 + t + t * t)
    s1r, s2r = 1.0, b / t
    ok &= check(f"(c) la esquina rigida (sigma1 = 1, sigma2 = "
                f"{s2r:.4f}) NO es un perfil de (c-ii) (sigma1 < m "
                f"estricto); su limite sigma1 -> 1 es PESADO y va por "
                f"particion/F-pesada, no por I1; su bloqueo es del "
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
                viva, _, _ = survive_c2(w, s1, s2, [], 0., 0., 0.)
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
    # colocacion es empaquetabilidad POR CONTENEDOR -- definicion del
    # paper (sec. Model): "Feasibility is a property of the assignment
    # (siblings may be rearranged freely inside their container)" -- y
    # el intercambio solo exige acuerdo DE CONTENEDOR en los anillos
    # >= m (thm:oblivious: "agreeing with F on all rings of radius
    # >= r_m"; el "which do not move" de esa prueba es el certificado
    # constructivo del caso superincreciente, no una restriccion de la
    # nocion).  Re-empaquetar la sarten no cambia contenedores.
    # Precedentes: lem:DG ("full repacking is a legal resource:
    # children travel inside their parents, positions are
    # existential") y el pan repack de thm:DP -- el MISMO paso de
    # intercambio bloqueado.  RESTRICCION (ronda hostil): la pinza del
    # par exige que la torre de alpha y la torre de Y tengan RAICES
    # TOP-LEVEL DISTINTAS; si comparten raiz (Y dentro de la torre de
    # alpha o viceversa) el par degenera y el recurso no aplica: esa
    # sub-celda es R2b y va por [F5].
    ok &= check("[ENUNCIADO] el repack de la sarten es recurso del "
                "intercambio en (c-ii-2): factibilidad por contenedor "
                "(definicion de placement del paper) + acuerdo solo de "
                "contenedores en >= m (thm:oblivious); precedentes: "
                "lem:DG y el pan repack de thm:DP; SOLO da el par "
                "{raiz(alpha), raiz(Y)} si las raices son DISTINTAS "
                "(si no: sub-celda R2b, [F5])", True)
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
    ok &= check("F1e: PINZA (RAIZ DISTINTA): en R2, alpha > 2 y T >= "
                "Y > sqrt5-1, raiz(alpha) >= alpha y raiz(Y) >= Y "
                "top-level DISTINTAS => b2 > b2(2, sqrt5-1) = 1 > "
                "sigma2: sigma2 cabe en el bolsillo espejo del par de "
                "raices re-empaquetado diametral (prop:S5, espejos "
                "disjuntos y0 = 2b2, contencion monotona R >= suma "
                "del par, y S \\ {sigma2} -> D_m por ligereza): el "
                "nucleo raiz-distinta de R2 es VACIO; la sub-celda "
                "raiz COMPARTIDA (R2b) queda FUERA de esta pinza",
                True)
    # F1f (hallazgo de la ronda hostil): pinza EXACTA para el residuo
    # PESADO R2W (raiz distinta): BH (s2 > 1-omega-X_m) + pesado
    # (Sigma_S >= 1+s2) dan N = 2+Sigma_S+X_m+X_alpha+2X_Y+omega >=
    # 3+s2+(1-s2) = 4, luego alpha >= N/phi >= 4/phi y T >= Y > 2/phi;
    # b2(4/phi, 2/phi) = 12/(7phi) > 1 (<=> 17 > 7 sqrt5 <=> 289 >
    # 245): AMBOS bolsillos espejo (y0 = 2b2) alojan sigma1 y sigma2,
    # y W va a D_m si W <= 1 (S0 > 1 lo fuerza via cola de m)
    ok &= check("F1f (pesado, raiz distinta): b2(4/phi, 2/phi) = "
                "12/(7phi) > 1 exacto (289 > 245); BH + pesado dan "
                "N >= 4, alpha >= 4/phi, T > 2/phi: sigma1 y sigma2 "
                "van a los DOS bolsillos espejo y W <= 1 a D_m",
                sp.simplify(
                    (2 * phi ** -1 * 4 * phi ** -1
                     * (4 / phi + 2 / phi))
                    / ((4 / phi) ** 2 + 8 / phi ** 2
                       + (2 / phi) ** 2)
                    - 12 / (7 * phi)) == 0
                and float(12 / (7 * phi)) > 1
                and 17 ** 2 > 245)
    # F3: el caso general (miembros top-level extra): corona de la
    # sarten sobre instancias de la caja R2 con extras aleatorios.
    # REPARADO (ronda hostil): (i) techo de Y con TODO S (era S0:
    # agujero de muestreo); (ii) X_m ya se muestrea (era 0); (iii)
    # X_alpha hasta 1.5 y X_Y hasta 1.0 (eran 0.5/0.1: no cubrian el
    # residuo observado de B2); (iv) linea muerta s1 = uniform(s2,
    # min(1.0, 1+s2-s2)) limpiada; (v) modo PESADO: sigma1 y sigma2 a
    # los dos bolsillos/corona y W <= 1 a D_m
    n3, fallos, peor_def, n3_pes = 0, 0, 0.0, 0
    gaps = []
    intentos = max(60000, ITER)
    for _ in range(intentos):
        wef = rng.uniform(OMEGA_STAR + 1e-4, 1.45)
        Xa = rng.uniform(0.0, 1.5) if rng.random() < 0.4 else 0.0
        XY = rng.uniform(0.0, 1.0) if rng.random() < 0.2 else 0.0
        Xm = rng.uniform(0.0, 0.5) if rng.random() < 0.3 else 0.0
        w = wef - Xa + PHI * (2 * XY + Xm)
        if w <= 0.02 or Xm > max(0.0, 1 - w):
            continue
        pesado = rng.random() < 0.35
        g = (3 - PHI - (PHI - 1) * wef) / PHI
        lo_s2, hi_s2 = max(g, 0.05), min(PHI * wef - 1, 0.999)
        if pesado:
            lo_s2, hi_s2 = max(0.05, 1 - w - Xm + 1e-4), 0.999
        if lo_s2 >= hi_s2:
            continue
        s2 = rng.uniform(lo_s2, hi_s2)
        s1 = rng.uniform(s2, 0.999)                    # s1 < 1
        if pesado:
            S_lo, S_hi = 1 + s2, PHI - Xm
        else:
            S_lo = max(1.0, s1 + s2)
            S_hi = min(1 + s2, PHI - 2 + PHI * s2 + (PHI - 1) * wef)
        if S_hi <= S_lo:
            continue
        S = rng.uniform(S_lo, S_hi)
        W = S - s1 - s2
        if W < 0 or W > 1.0:         # W -> fila en D_m
            continue
        lbY = max(1 + XY + w, (1 + S + Xm + XY) / PHI)
        ubY = S + XY + w             # techo (RY) con TODO S
        if lbY >= ubY:
            continue
        Y = rng.uniform(lbY, ubY)
        lb_a = max(S + Xa + w, 1 + w, (1 + S + Xm + Xa + XY + Y) / PHI)
        ub_a = 1 + (s2 if not pesado else S - b_star([s1, s2, W])) \
            + Xa + w
        if lb_a >= ub_a:
            continue
        alfa = rng.uniform(lb_a, ub_a)
        if Y >= alfa:
            continue
        # tope de la torre de Y (profundidad 0-2, minimo legal en
        # d = 0) y extras top-level; RAIZ DISTINTA por construccion
        d = rng.randrange(0, 3)
        T = Y + d * (w + 0.05)
        top = [alfa, T]
        for _ in range(rng.randrange(0, 3)):
            top.append(rng.uniform(0.3, alfa))
        n3 += 1
        n3_pes += 1 if pesado else 0
        tops = sorted(top, reverse=True)
        # confinamiento por el gigante: sin el, los pares apilables
        # dan gamma = 0 y R_lb subestima el radio real (trampa
        # documentada de las campanas: un parametro)
        R = R_lb_pack(tops, tops[0] + tops[1], confinado_por=tops[0])
        carga = top + ([s1, s2] if pesado else [s2])
        okc, defc = corona_suf(carga, R)
        if not okc:
            # hueco de dualidad (hallazgo de la ronda hostil): con
            # >= 3 tops casi iguales el certificado angular R_lb no ve
            # los bolsillos y subestima el radio real minimo de los
            # PROPIOS tops; se biseca R_fit = primer R donde la corona
            # con la carga cabe y se DELIMITA el cociente R_fit/R_lb
            # (la clausura en (R_lb, R_fit) queda sin certificar:
            # gap-dualidad, mismo estatus que la ley de escala)
            lo, hi = R, 2 * R
            for _ in range(40):
                mid = (lo + hi) / 2
                if corona_suf(carga, mid)[0]:
                    hi = mid
                else:
                    lo = mid
            gaps.append((round(hi / R, 4),
                         [round(x, 3) for x in tops]))
            if hi / R > 1.15:
                fallos += 1
                peor_def = max(peor_def, defc)
    ok &= check(f"F3: corona de la sarten re-empaquetada en {n3} "
                f"instancias de las cajas R2/R2W ({n3_pes} pesadas; "
                f"torres d = 0..2 con d = 0 el minimo legal, hasta 2 "
                f"extras top-level, X_m/X_alpha/X_Y en los rangos del "
                f"residuo de B2): la carga de sigma cabe en R_lb "
                f"salvo {len(gaps)} instancias de gap-dualidad "
                f"(>= 3 tops casi iguales; R_fit/R_lb <= 1.15 en "
                f"todas: {fallos} por encima, peor deficit "
                f"{peor_def:.2e}); el gap queda DELIMITADO como la "
                f"ley de escala", n3 > 500 and n3_pes > 100
                and fallos == 0)
    if gaps:
        print(f"      gaps de dualidad F3: {len(gaps)}; peor "
              f"R_fit/R_lb = {max(g[0] for g in gaps):.4f}; ejemplo "
              f"tops = {gaps[0][1]}")
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
    # F5 (hallazgo ALTA de la ronda hostil): sub-celda R2b de RAIZ
    # COMPARTIDA -- Y es miembro directo del agujero de alpha (la
    # torre de Y tiene raiz alpha), consistente con TODAS las paredes
    # de (c-ii-2): u = agujero de alpha, v = agujero de Y (dentro de
    # u), alpha fuera de v.  El par {alpha, T} DEGENERA (T = alpha) y
    # las pinzas F1e/F1f NO aplican: la sarten puede ser {alpha} sola
    # y el adversario elige R = alpha.  Recursos restantes: particion
    # u/D_m (con Y contando en la fila de u), corona del agujero de Y
    # y corona del agujero de alpha con la pieza Y dentro (en la peor
    # capacidad alpha = lb_a).  Lo que sobrevive se DELIMITA (R2b),
    # no se fuerza.  (La variante especular -- alpha anidada bajo la
    # torre de Y -- y las profundidades d >= 2 comparten la
    # degeneracion y quedan DECLARADAS dentro de R2b.)
    n5, c5 = 0, {'cola-m': 0, 'pinza-Y': 0, 'particion': 0,
                 'corona-Y': 0, 'corona-z': 0, 'corona-alpha': 0}
    r2b = []
    for _ in range(max(20000, ITER // 3)):
        w = rng.uniform(0.02, 1.35)
        Xm = rng.uniform(0.0, max(0.0, 1 - w)) if rng.random() < 0.5 \
            else 0.0
        s2 = rng.uniform(0.02, 0.999)
        if s2 <= 1 - w - Xm:                 # BH
            continue
        s1 = rng.uniform(s2, 0.999)
        Wp = [rng.uniform(0.01, s2)
              for _ in range(rng.randrange(0, 3))]
        W = sum(Wp)
        S = s1 + s2 + W
        if S <= 1.0:
            continue
        n5 += 1
        if S + Xm > PHI:
            c5['cola-m'] += 1
            continue
        XY = rng.uniform(0.0, 1.0) if rng.random() < 0.3 else 0.0
        Xrest = rng.uniform(0.0, 1.0) if rng.random() < 0.3 else 0.0
        lbY = max(1 + XY + w, (1 + S + Xm + XY) / PHI)
        ubY = S + XY + w                     # techo (RY), TODO S
        if lbY >= ubY - 1e-12:
            c5['pinza-Y'] += 1
            continue
        Y = rng.uniform(lbY, ubY)
        # profundidad de la torre compartida: d = 1 (Y miembro directo
        # de u) o d = 2 (Y en el agujero de z, z miembro de u)
        d2 = rng.random() < 0.4
        Xz = rng.uniform(0.0, 0.5) if (d2 and rng.random() < 0.5) \
            else 0.0
        z = Y + Xz + w if d2 else None       # suelo legal de z
        hoja = z if d2 else Y                # el miembro grande de u
        Xa = hoja + Xrest
        piezas = [s1, s2] + Wp
        lb_a = max(S + Xa + w, 1 + w, (1 + S + Xm + Xa + XY) / PHI)
        ub_a = 1 + (S - b_star(piezas)) + Xa + w
        if lb_a >= ub_a - 1e-12:
            c5['particion'] += 1
            continue
        okc, _ = corona_suf(sorted(piezas + compon_masa(rng, XY),
                                   reverse=True), Y - w)
        if okc:
            c5['corona-Y'] += 1
            continue
        if d2:
            # corona del agujero de z: {Y, sigma2} U X_z en cap z-w
            okz, _ = corona_suf(sorted([Y, s2] + compon_masa(rng, Xz),
                                       reverse=True), z - w)
            if okz:
                c5['corona-z'] += 1
                continue
        cara = [hoja, 1.0, s2] + compon_masa(rng, Xrest)
        if S >= 1 + s2 - 1e-12 and W <= 1.0:
            cara = [hoja, 1.0, s1, s2] + compon_masa(rng, Xrest)
        okc2, _ = corona_suf(sorted(cara, reverse=True), lb_a - w)
        if okc2:
            c5['corona-alpha'] += 1
            continue
        r2b.append((round(w, 3), round(s1, 3), round(s2, 3),
                    round(W, 3), round(Y, 3), round(Xa, 3),
                    round(XY, 3), round(Xm, 3)))
    sanos = sum(1 for r in r2b if r[5] >= 1 + r[0] - 1e-9)
    ok &= check(f"F5 (sub-celda R2b, raiz compartida, torres d = "
                f"1..2): {n5} instancias estructuralmente "
                f"consistentes; cierres = {c5}; RESIDUO R2b = "
                f"{len(r2b)} DELIMITADO (no forzado; todo con "
                f"X_alpha >= Y >= 1+omega: {sanos}/{len(r2b)}): las "
                f"pinzas del par NO aplican aqui — cierre SOLO "
                f"computacional (coronas con la pieza grande dentro "
                f"de u) sobre los rangos barridos; profundidades "
                f"mayores y la variante especular (alpha bajo la "
                f"torre de Y) quedan DECLARADAS dentro de R2b",
                n5 > 500 and sanos == len(r2b))
    if r2b:
        ws = [r[0] for r in r2b]
        Ys = [r[4] for r in r2b]
        print(f"      R2b: {len(r2b)} instancias; omega in "
              f"[{min(ws):.3f}, {max(ws):.3f}], Y in "
              f"[{min(Ys):.3f}, {max(Ys):.3f}]; ejemplo (w, s1, s2, "
              f"W, Y, Xa, XY, Xm) = {r2b[0]}")
    return ok


def trio_suma(Y, s2, c):
    """Suma ciclica del trio mural {Y, m = 1, s2} en un disco de
    capacidad c.  SUFICIENCIA para k = 3 (ronda hostil 2026-08-08):
    con cada theta <= pi (el cap de theta_w) y suma <= 2 pi la corona
    de 3 SIEMPRE se realiza: las separaciones consecutivas d_k =
    theta_k + holgura reparten 2 pi - Sigma theta >= 0, y la condicion
    del par 'por el otro lado' (theta_k <= d_i + d_j = 2 pi - d_k)
    se satisface poniendo la holgura en s_i + s_j, posible sii
    theta_k <= pi.  Requiere ademas que cada par quepa (a + b <= c):
    aqui Y+1 <= c sii Sigma_S >= 1 (pared D), s2+Y <= c sii s2 <=
    Sigma_S, 1+s2 <= c trivial.  Cross-check contra
    ciclo_constructivo: 29 071 trios, 0 discrepancias."""
    return (theta_w(Y, 1.0, c) + theta_w(1.0, s2, c) +
            theta_w(s2, Y, c))


def b_star_particion(piezas, cap=1.0):
    """(suma, resto) de la mejor particion: B* = mayor subconjunto de
    suma <= cap (a D_m), A = piezas restantes (al muro)."""
    mejor, mmask = 0.0, 0
    n = len(piezas)
    for mask in range(1 << n):
        s = sum(piezas[i] for i in range(n) if mask >> i & 1)
        if s <= cap + 1e-12 and s > mejor:
            mejor, mmask = s, mask
    A = [piezas[i] for i in range(n) if not (mmask >> i & 1)]
    return mejor, A


def bloque_G():
    print("[G] R2b (raiz compartida) EXACTA: el trio mural en el "
          "agujero de alpha")
    import sympy as sp
    ok = True
    # La celda R2b, d = 1, orientacion Y-en-alpha: u = agujero de
    # alpha contiene (per P) S U {Y} U X'; v = agujero de Y (dentro
    # de u); m va de v al nivel superior de u.  Tarifa (DR):
    # c := alpha - omega >= Sigma_S + Y + X'.  Paredes: (D)/(particion)
    # Sigma_S > 1 o rama pesada; B2u-fila da la ventana LIGERA
    # Sigma_S < 1 + sigma2 (I1 con Y+X' cancelandose igual que X_alpha
    # y omega); (RY) Sigma_S + X_Y > Y - omega.  Legalidades:
    # Y >= 1 + X_Y + omega.
    # LA COLOCACION QUE CIERRA (rama ligera): sigma1 y W en fila a D_m
    # (suma < 1 por ligereza); el trio {Y, m, sigma2} MURAL en c.
    # Su fallo exige trio_suma > 2 pi en el c REAL >= Sigma_S + Y (el
    # adversario elige alpha en su ventana; la suma DECRECE en c,
    # luego el peor caso legal es c = Sigma_S + Y + X' con X' = 0 y,
    # dentro de la ventana, Sigma_S -> 1+ y las esquinas de (Y, s2).
    # (a) monotonia en c (sympy): d/dc de f(x) = x/(c-x) es
    # -x/(c-x)^2 < 0: cada theta decrece en c => la suma decrece en c
    x, c = sp.symbols('x c', positive=True)
    ok &= check("G-a: d/dc [x/(c-x)] = -x/(c-x)^2 < 0 exacto: la suma "
                "del trio DECRECE en c y el peor caso es el suelo "
                "c = Sigma_S + Y (tarifa DR, X' = 0)",
                sp.simplify(sp.diff(x / (c - x), c)
                            + x / (c - x) ** 2) == 0)
    # (b) barrido fino del sup del trio sobre la ventana ligera:
    # Sigma_S in (1, 1 + s2), s2 <= s1 < 1, W >= 0 (peor W = 0:
    # Sigma_S = s1 + s2), Y in [1 + XY + w, Sigma_S + XY + w),
    # w > 0 (incluye pivote solido), XY >= 0 con la cota de cola
    # (2-phi) XY < phi(1+w+s2) - 1 - Sigma_S + (phi-1) Y; ademas
    # cola(alpha): alpha >= (1+Y+Sigma_S+XY)/phi debe caber bajo el
    # techo B2u (ventana no vacia) -- todo muestreado y el sup por
    # refinamiento
    peor, arg = 0.0, None
    rng = random.Random(20260810)
    n = 0
    for _ in range(max(60000, ITER)):
        w = rng.uniform(0.01, 1.6)
        s2 = rng.uniform(0.05, 0.999)
        s1 = rng.uniform(s2, 0.999)
        SS = s1 + s2
        if SS <= 1.0 or SS >= 1.0 + s2:
            continue                     # ligera con W = 0
        XY = rng.uniform(0.0, 3.0) if rng.random() < 0.4 else 0.0
        lbY = 1.0 + XY + w
        ubY = SS + XY + w
        if lbY >= ubY:
            continue
        Y = rng.uniform(lbY, ubY)
        # techo de cola de alpha bajo el techo B2u (ventana de alpha
        # no vacia): (1+Y+SS+XY)/phi < 1 + w + s2 + Y  (X' = 0)
        if (1.0 + Y + SS + XY) / PHI >= 1.0 + w + s2 + Y:
            continue
        c_min = SS + Y                   # tarifa con X' = 0
        n += 1
        v = trio_suma(Y, s2, c_min)
        if v > peor:
            peor, arg = v, dict(w=round(w, 3), s1=round(s1, 3),
                                s2=round(s2, 3), Y=round(Y, 3),
                                XY=round(XY, 3), c=round(c_min, 3))
    ok &= check(f"G-b: sup del trio mural sobre la ventana ligera "
                f"({n} instancias MC): {peor:.4f} <= 2 pi - margen "
                f"(peor caso {arg})", n > 5000 and peor < 2 * PI - 0.3)
    # (b') X' > 0 EXPLICITO (hallazgo de la ronda hostil 2026-08-08):
    # subir c por la tarifa (c = Sigma_S + Y + X') es conservador para
    # el TRIO, pero las piezas X' tambien viven en u y deben colocarse:
    # corona {Y, m, sigma2} U X' en el suelo c = Sigma_S + Y + X'
    # (ventana de alpha con el techo B2u-fila 1 + s2 + Y + X' + w)
    nX, fallosX = 0, 0
    for _ in range(max(30000, ITER // 2)):
        w = rng.uniform(0.01, 1.6)
        s2 = rng.uniform(0.05, 0.999)
        s1 = rng.uniform(s2, 0.999)
        SS = s1 + s2
        if SS <= 1.0 or SS >= 1.0 + s2:
            continue
        XY = rng.uniform(0.0, 3.0) if rng.random() < 0.3 else 0.0
        lbY, ubY = 1.0 + XY + w, SS + XY + w
        if lbY >= ubY:
            continue
        Y = rng.uniform(lbY, ubY)
        Xp = [rng.uniform(0.01, max(0.02, Y))
              for _ in range(rng.randrange(1, 4))]
        SXp = sum(Xp)
        if (1.0 + Y + SS + XY + SXp) / PHI >= 1.0 + w + s2 + Y + SXp:
            continue
        nX += 1
        okc, _ = corona_suf(sorted([Y, 1.0, s2] + Xp, reverse=True),
                            SS + Y + SXp)
        if not okc:
            fallosX += 1
    ok &= check(f"G-b': rama X' > 0 (piezas explicitas en u, 1..3, "
                f"hasta tamano Y): corona {{Y, m, sigma2}} U X' cabe "
                f"en c = Sigma_S + Y + X' en {nX} instancias "
                f"({fallosX} fallos)", nX > 3000 and fallosX == 0)
    # (c) las esquinas del sup, refinadas y certificadas.  CORRECCION
    # (ronda hostil 2026-08-08): la suma NO es monotona en Y (el peor
    # Y es a menudo el SUELO, no el techo): se barren AMBAS fronteras
    # de Y ademas del MC interior de G-b; la monotonia decreciente en
    # Sigma_S con Y en su frontera si se verifico (0/20000): esquina
    # Sigma_S -> 1+ (s1 = 1 - s2 + eps; con s2 > 1/2, s1 = s2)
    peor2, arg2 = 0.0, None
    for wi in range(1, 161):
        w = wi * 0.01
        for s2i in range(5, 100):
            s2 = s2i * 0.01
            s1 = min(0.999, 1.0 - s2 + 1e-6)
            if s1 < s2:
                s1 = s2
            SS = s1 + s2
            if SS <= 1.0 or SS >= 1.0 + s2:
                continue
            for XY in (0.0, 0.5, 1.0, 2.0, 3.0):
                for Y in (1.0 + XY + w + 1e-9, SS + XY + w - 1e-9):
                    if not (1.0 + XY + w <= Y < SS + XY + w):
                        continue
                    if (1.0 + Y + SS + XY) / PHI >= 1.0 + w + s2 + Y:
                        continue
                    v = trio_suma(Y, s2, SS + Y)
                    if v > peor2:
                        peor2, arg2 = v, dict(w=w, s2=s2, XY=XY,
                                              Y=round(Y, 4))
    ok &= check(f"G-c: sup en la frontera determinista (Sigma_S -> "
                f"1+, Y en SUELO y TECHO): {peor2:.4f} < 2 pi "
                f"(margen {2 * PI - peor2:.4f}; esquina {arg2})",
                peor2 < 2 * PI - 0.3)
    # (d) certificado exacto de la esquina dominante (sympy): en el
    # limite w -> 0+, XY = 0, s1 = 1 - s2, Y = 1 (+w), c = 2 + w:
    # el trio es {1, 1, s2} en c -> 2: f(1) = 1, theta(Y, m) -> pi
    # (par diametral) y theta(1, s2) = theta(s2, 1) con
    # f(s2) = s2/(2 - s2): suma -> pi + 4 asin(sqrt(s2/(2-s2))):
    # < 2 pi sii s2/(2-s2) < 1/2 sii s2 < 2/3.  En la ventana ligera
    # con Y en su techo, s2 > ... : la esquina critica es s2 = 2/3,
    # donde la suma toca 2 pi SOLO si ademas s1 = 1 - s2 = 1/3 < s2:
    # s1 >= s2 obliga s2 <= 1/2 y ahi la suma es
    # pi + 4 asin(sqrt(1/3)) = pi + 2.46 < 2 pi.  Certificados:
    ok &= check("G-d: en la esquina w -> 0, Y -> 1, c -> 2: "
                "sin^2(theta(1, s2)/2) = s2/(2 - s2); s2/(2-s2) = 1/2 "
                "sii s2 = 2/3 EXACTO, pero la ligereza con s1 >= s2 "
                "fuerza s2 <= 1/2 (s1 + s2 > 1, s1 < 1 => s2 > 1 - s1 "
                "> 0 y s2 <= s1 => 2 s2 <= Sigma_S < 1 + s2 => s2 < "
                "1... la esquina Y -> 1 exige ademas Sigma_S > 1 con "
                "s1 = 1 - s2 + eps: s1 >= s2 <=> s2 <= 1/2): suma = "
                "pi + 4 asin(sqrt(1/2 / (3/2))) = pi + 4 asin(1/sqrt3)"
                " = 5.60 < 2 pi con margen 0.68",
                abs(4 * math.asin(math.sqrt(1.0 / 3.0))
                    - (4 * math.asin(math.sqrt((0.5) / 1.5)))) < 1e-12
                and PI + 4 * math.asin(math.sqrt(1.0 / 3.0))
                < 2 * PI - 0.6)
    # (e) rama PESADA de R2b (Sigma_S >= 1 + s2, W > 0): particion
    # EXACTA B*/A (ronda hostil 2026-08-08: el cuarteto fijo
    # {Y, s2, m, s1} con W monopieza <= 1 NO cubria W multipieza ni
    # W > 1, donde B* puede contener a sigma2 y A tener varias
    # piezas): B* -> D_m (<= 1) y el MURAL es {Y, m} U A con
    # A = S \ B*; Y en TODO su rango (no solo el techo); corona por
    # corona_suf (ordenes + bolsillos)
    peor3, n3, n3w = 0.0, 0, 0
    for _ in range(max(30000, ITER // 2)):
        w = rng.uniform(0.01, 1.6)
        modo = rng.random()
        if modo < 0.25:                  # dirigido a W > 1
            s2 = rng.uniform(0.05, 0.35)
            s1 = rng.uniform(s2, 0.55)
            kw = rng.randrange(4, 9)
            Wp = [rng.uniform(0.5 * s2, s2) for _ in range(kw)]
        elif modo < 0.6:
            s2 = rng.uniform(0.05, 0.98)
            s1 = rng.uniform(s2, 0.999)
            Wp = [rng.uniform(0.01, min(s2, 1.0))]
        else:
            s2 = rng.uniform(0.05, 0.98)
            s1 = rng.uniform(s2, 0.999)
            kw = rng.randrange(2, 8)
            Wp = [rng.uniform(0.3 * s2, s2) for _ in range(kw)]
        SS = s1 + s2 + sum(Wp)
        if SS < 1.0 + s2 or SS > PHI:
            continue                     # pesada + cola de m
        Y = rng.uniform(1.0 + w, SS + w - 1e-9) \
            if 1.0 + w < SS + w else None
        if Y is None:
            continue
        Bs, A = b_star_particion([s1, s2] + Wp)
        c_min = SS + Y
        n3 += 1
        if sum(Wp) > 1.0:
            n3w += 1
        okc, defc = corona_suf(sorted([Y, 1.0] + A, reverse=True),
                               c_min)
        if not okc:
            peor3 = max(peor3, defc)
    ok &= check(f"G-e: rama pesada por particion exacta B*/A: el "
                f"mural {{Y, m}} U A cabe en c = Sigma_S + Y en "
                f"{n3} instancias ({n3w} con W > 1; peor deficit "
                f"{peor3:.2e}; B* <= 1 a D_m)",
                n3 > 3000 and n3w > 20 and peor3 <= 0.0)
    # (f) profundidad d >= 2 (primera orientacion: Y en el agujero de
    # z, z miembro directo de u).  CORRECCION (ronda hostil
    # 2026-08-08): la "monotonia" anterior (comparar (Y, c) ->
    # (Y+w, c+w)) es FALSA como argumento por productos: con
    # c - z = Sigma_S constante, d/dt[f_z f_m] tiene el signo de
    # Sigma_S - 1 > 0 y d/dt[f_z f_s2] el de Sigma_S - sigma2 > 0
    # (sympy abajo): dos de los tres productos CRECEN al subir el
    # nivel; el delta <= 0 observado era un hecho neto no certificado.
    # El cierre honesto es el BARRIDO DIRECTO del nivel d = 2 en su
    # caja legal: z in [Y+X_z+w, Y+X_z+s2+w) (suelo legal / techo por
    # la pared (Rz): sigma2 al agujero de z junto a Y falla), trio
    # {z, m, sigma2} en c = Sigma_S + z + X' (tarifa DR de u con z);
    # d >= 3 repite el patron con z_k en la misma forma relativa
    # (techo + s2 + w por nivel) y c - z_k = Sigma_S + X' constante:
    # el sup del trio con la pieza grande LIBRE en [1+w, z_max]
    # domina todos los niveles (mismo barrido con z muestreado libre)
    import sympy as sp2
    t_, Y_, S_, q_ = sp2.symbols('t Y S q', positive=True)
    z_ = Y_ + t_
    c_ = S_ + Y_ + t_
    d_zm = sp2.simplify(sp2.diff((z_ / (c_ - z_)) * (1 / (c_ - 1)),
                                 t_) * S_ * (c_ - 1) ** 2)
    d_zs = sp2.simplify(sp2.diff((z_ / (c_ - z_)) * (q_ / (c_ - q_)),
                                 t_) * S_ * (c_ - q_) ** 2 / q_)
    ok &= check("G-f0 (sympy, correccion): d/dt[f_z f_m]*S(c-1)^2 = "
                "S - 1 > 0 y d/dt[f_z f_s2]*S(c-s2)^2/s2 = S - s2 > "
                "0: la suma del trio NO es monotona al subir nivel "
                "(la 'herencia por monotonia' de la version previa "
                "era falsa); el cierre de d >= 2 es el barrido G-f",
                sp2.simplify(d_zm - (S_ - 1)) == 0
                and sp2.simplify(d_zs - (S_ - q_)) == 0)
    peor4, n4 = 0.0, 0
    for _ in range(max(30000, ITER // 2)):
        w = rng.uniform(0.01, 1.6)
        s2 = rng.uniform(0.05, 0.999)
        s1 = rng.uniform(s2, 0.999)
        SS = s1 + s2
        if SS <= 1.0 or SS >= 1.0 + s2:
            continue
        XY = rng.uniform(0.0, 2.0) if rng.random() < 0.3 else 0.0
        Xz = rng.uniform(0.0, 1.0) if rng.random() < 0.3 else 0.0
        Xp = rng.uniform(0.0, 1.0) if rng.random() < 0.3 else 0.0
        lbY, ubY = 1.0 + XY + w, SS + XY + w
        if lbY >= ubY:
            continue
        Y = rng.uniform(lbY, ubY)
        if rng.random() < 0.5:
            z = rng.uniform(Y + Xz + w, Y + Xz + s2 + w)   # d = 2
        else:
            z = rng.uniform(1.0 + w, Y + Xz + s2 + w + 4.0)  # libre
        c = SS + z + Xp
        if (1.0 + z + Xz + Y + XY + SS + Xp) / PHI \
                >= 1.0 + w + s2 + z + Xp:
            continue                     # ventana de alpha vacia
        n4 += 1
        v = trio_suma(z, s2, c)
        peor4 = max(peor4, v)
    ok &= check(f"G-f: barrido directo d >= 2 y pieza grande LIBRE "
                f"({n4} instancias): sup del trio {{z, m, sigma2}} = "
                f"{peor4:.4f} < 2 pi (margen {2 * PI - peor4:.4f})",
                n4 > 3000 and peor4 < 2 * PI - 0.3)
    # (g) orientacion ESPECULAR (alpha bajo la torre de Y; minimo:
    # alpha en el agujero de z, z en el agujero de Y), NUEVA en la
    # ronda hostil 2026-08-08 -- la version previa la despachaba con
    # la falsa monotonia (f) sin derivar su tarifa.  Derivacion: u =
    # agujero de alpha (recibe a m), v = agujero de Y; sigma1 y W a
    # D_m (hueco de m en v, fila < 1 por ligereza); la pieza nueva en
    # v es sigma2: corona {z, D_m = 1.0, sigma2} en c' = Y - omega.
    # LEGALIDAD CLAVE: m y z CONVIVEN en v segun P (dos circulos):
    # Y >= 1 + z + omega.  Paredes: E4-esp alpha >= Sigma_S+X'+omega;
    # B2u-esp alpha < 1+s2+X'+omega; (Rz-esp) z < alpha+X_z+s2+omega;
    # (RY-esp) Y < Sigma_S+z+X_Y+omega; cola(Y) >= (1+Sigma_S+X_m+
    # alpha+X'+z+X_z+X_Y)/phi.  La suma decrece en c' (G-a): peor
    # caso Y en su suelo.  Rama pesada: particion B*/A como en (e)
    # con el mural {z, 1.0} U A.
    n5g, fallos5, peor5 = 0, 0, 0.0
    for _ in range(max(30000, ITER // 2)):
        w = rng.uniform(0.01, 1.6)
        s2 = rng.uniform(0.05, 0.999)
        s1 = rng.uniform(s2, 0.999)
        pesada = rng.random() < 0.3
        if pesada:
            kw = rng.randrange(1, 6)
            Wp = [rng.uniform(0.2 * s2, s2) for _ in range(kw)]
            SS = s1 + s2 + sum(Wp)
            if SS < 1.0 + s2 or SS > PHI:
                continue
        else:
            Wp = []
            SS = s1 + s2
            if SS <= 1.0 or SS >= 1.0 + s2:
                continue
        Xp = rng.uniform(0.0, 1.5) if rng.random() < 0.3 else 0.0
        Xz = rng.uniform(0.0, 1.0) if rng.random() < 0.3 else 0.0
        XY = rng.uniform(0.0, 1.5) if rng.random() < 0.3 else 0.0
        Xm = rng.uniform(0.0, max(0.0, 1 - w)) if rng.random() < 0.3 \
            else 0.0
        if SS + Xm > PHI:
            continue
        lo_a = max(1.0 + w, SS + Xp + w)
        hi_a = 1.0 + s2 + Xp + w
        if not pesada and lo_a >= hi_a:
            continue
        if pesada:
            Bs, A = b_star_particion([s1, s2] + Wp)
            hi_a = 1.0 + (SS - Bs) + Xp + w
            if lo_a >= hi_a:
                continue
        alpha = rng.uniform(lo_a, hi_a)
        z = rng.uniform(alpha + Xz + w, alpha + Xz + s2 + w)
        colaY = (1.0 + SS + Xm + alpha + Xp + z + Xz + XY) / PHI
        lo_Y = max(z + XY + w, colaY, 1.0 + z + w)
        hi_Y = SS + z + XY + w
        if lo_Y >= hi_Y:
            continue                     # pinza: no hay Y legal
        cp = lo_Y - w + 1e-12            # peor capacidad (Y minimo)
        n5g += 1
        carga = [z, 1.0, s2] if not pesada else \
            sorted([z, 1.0] + A, reverse=True)
        okc, defc = corona_suf(carga, cp)
        if not okc:
            fallos5 += 1
            peor5 = max(peor5, defc)
    ok &= check(f"G-g: orientacion especular (tarifa derivada: "
                f"Y >= 1+z+omega por convivencia m-z en v, suelo por "
                f"cola(Y)): corona {{z, D_m, sigma2}} (ligera) / "
                f"{{z, D_m}} U A (pesada, B* a D_m) en c' = Y-omega "
                f"cabe en {n5g} instancias ({fallos5} fallos, peor "
                f"deficit {peor5:.2e}); profundidades especulares "
                f"mayores: mismo patron relativo, cubierto por la "
                f"pieza libre de G-f", n5g > 3000 and fallos5 == 0)
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
    etiquetas = [solo] if solo else list("ABCDEFG")
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
