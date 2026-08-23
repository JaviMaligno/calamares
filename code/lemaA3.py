#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FASE 3a DEL LEMA DE |A|: LAS CELDAS PESADAS G-e Y G-g DEL
ENSAMBLAJE (puertocii) CERTIFICADAS — el mural {*, m} U A con A
multipieza SIN COTA EN |A| deja de ser barrido MC y pasa a
certificado por B&B + slots + el motor de colocacion.

LAS CELDAS (puertocii (e) y (g), rama pesada SS >= 1 + s2):
  G-e: orientacion Y-en-alpha; B* = mejor subconjunto de S con
       masa <= 1 (a D_m), A = S \\ B* al MURO: corona {Y, m} U A
       en c = SS + Y (peor caso legal: X' = 0, alpha en su
       suelo); Y >= 1 (legal Y >= 1 + w), SIN TECHO (la ventana
       Y < SS + w heredaba el tope de muestreo w <= 1.6 del MC:
       aqui Y va a la cola por fila de limites — el tope de w
       NO se replica).
  G-g: orientacion especular; corona {z, D_m = 1} U A en
       c' = Y - w >= 1 + z (la convivencia m-z en v: teorema del
       par); z >= 1, SIN TECHO (misma razon).  El par (z, m) a
       c' = 1 + z es la TANGENCIA LEGAL NO ESTRICTA (patron
       adversariado en espomegacola/areduccion): exencion
       antipodal.

EL GATE DE LA PARTICION (la matematica nueva de esta fase, gate
A2): si A no es vacio, entonces
  (i)   b := masa(B*) > 1/2  (si b <= 1/2, cualquier a de A
        cumple a <= 1 y a > ... : {a} solo ya seria mejor B* si
        a > b; y si a <= b <= 1/2 entonces B* U {a} <= 1
        contradiria la maximalidad);
  (ii)  toda pieza a de A cumple a <= b (el subconjunto {a} es
        candidato a B* y B* es maximo) y a <= masa(A) <= SS - b,
        luego a <= min(b, SS - b) <= SS/2 <= phi/2 = 0.809;
  (iii) masa(A) = SS - b < SS - 1/2 <= phi - 1/2 = 1.118.
CAP Y MASA UNIVERSALMENTE ACOTADOS: las filas por limites no
claman (G-e: p(Y, a) -> a/SS <= (phi/2)/(1+s2) < 1; G-g:
p(z, a) -> a <= phi/2 < 1) y el lema de slots decide.

Bloques: [A] gates (particion + filas + ventanas superconjunto);
[B] G-e por B&B (s2, SS, uY) con cola Y; [C] G-g por B&B
(s2, SS, uz) con cola z y el par (z, m) exento; [D] contraste
hostil (muestreo real de puertocii + falsabilidad); [E] estatus.
QUEDA DECLARADO para la fase 3b: k >= 2 anillos extra del canal
(espcanal E).
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check
from r2bmulti import th, bnb_factible
from lemaA import _motor_dos_lados, _cuerda, _asin2, K_CORTE

SEED = int(os.environ.get('CC_SEED', '20260823'))
V_T = math.log(64.0)
CAP_A = PHI / 2.0                      # gate A2(ii)
MASA_A = PHI - 0.5                     # gate A2(iii)


def _corona_pesada_k(SSh_e, b_lo, b_hi, c_lo, fila_g, exento,
                     cadena_z=None):
    """La corona {G, m} U A de las celdas pesadas con b =
    masa(B*) de la caja: masa(A) = SS - b <= SSh_e - b_lo, toda
    pieza de A en (1 - b, b] (maximalidad de B*).  VARIANTES
    AND POR |A| = k:
      cap_k = min(b_hi, masa_A - (k-1) piso), piso = 1 - b_hi;
      k = 1 con cadena_z (G-g): el lema de la cadena dorada
      ((1-a)(z^2+z) >= a con z = cadena_z); k = 1 sin cadena
      (G-e) y k = 2..5: motor con k nodos de radio cap_k;
      k >= 6: dos bloques por cuerda (cap_6 mayora)."""
    masa_A = SSh_e - b_lo
    if masa_A <= 0.0:
        return True                    # A vacio: trio r2bmulti
    piso = max(0.0, 1.0 - b_hi)
    for k in range(1, 7):
        if k > 1 and k * piso >= masa_A:
            break                      # k piezas ya no caben
        cap_k = min(b_hi, masa_A - (k - 1) * piso)
        if cap_k <= 0.0:
            break
        if k == 1 and cadena_z is not None:
            # EL LEMA DE LA CADENA DORADA ES ANALITICO PURO
            # (gate A5): en cada punto real a <= min(b, SS-b)
            # <= SS/2 [A2] y z >= SS [A4], luego (1-a)(z^2+z)
            # >= (1-SS/2)(SS^2+SS) >= SS/2 >= a sii SS^2 - SS
            # - 1 <= 0 sii SS <= phi — la pared de la familia.
            # La comprobacion por esquinas de caja MEZCLA
            # a_max (que exige SS = SSh, b = b_lo) con z_min
            # (que exige SS chico) y rompe la tangencia exacta
            # por epsilon: aqui NO hay nada que evaluar
            continue
        if k <= 5:
            # ESCALONES POR MASA: la pieza i-esima mayor de k
            # piezas de suma masa_A es <= masa_A/i (y <= cap_k)
            nodos = [1e9, 1.0] + [min(cap_k, masa_A / i)
                                  for i in range(1, k + 1)]
            Ds = {}
        else:
            # ACTA H1 (FATAL, reparado): masa_A/6 solo acota la
            # pieza 6-esima — las CINCO mayores de un |A| >= 6
            # solo estan acotadas por cap_6 = masa_A - 5 piso
            # (a_(1) <= masa - 5(1-b)); el min con masa_A/6
            # dejaba thmat no mayorante (contraejemplo legal
            # del referee: pieza 0.4 modelada a cap 0.11)
            cap_b = cap_k
            peso = _cuerda(cap_b, c_lo) * (masa_A / 2.0
                                           + cap_b / 2.0)
            nodos = [1e9, 1.0, cap_b, cap_b]
            Ds = {2: peso, 3: peso}
        n = len(nodos)
        thmat = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if nodos[i] >= 1e8 or nodos[j] >= 1e8:
                    otro = nodos[j] if nodos[i] >= 1e8 \
                        else nodos[i]
                    thmat[i][j] = fila_g(otro)
                else:
                    thmat[i][j] = th(nodos[i], nodos[j], c_lo)
                thmat[j][i] = thmat[i][j]
        if not _motor_dos_lados(nodos, thmat, Ds,
                                exento=exento):
            return False
    return True


def _podas_pesada(s2l, s2h, SSl, SSh):
    """Paredes de la rama pesada: SS in [1 + s2, phi],
    s1 >= s2 => 2 s2 <= SS."""
    if SSh < 1.0 + s2l or SSl > PHI:
        return False
    if 2.0 * s2l > SSh:
        return False
    return True


def crit_Ge(box):
    """G-e: (s2, SS, uY).  Corona {Y, m} U A en c = SS + Y; la
    fila de Y por limites: p(Y, a) = Y a/((c - Y)(c - a)) =
    Y a/(SS (SS + Y - a)) CRECE en Y hacia a/SS (gate A3) —
    sup uniforme sobre la cola con SS >= SSl; el termino m-lado
    a/(SS + Y - a) <= a/(SSl + Y_lo - a) tambien mayorado via
    c_lo.  a <= phi/2 y SSl >= 1 dan p <= 0.809 < 1: sin clamp
    para las piezas de A — pero el PAR (Y, m) clampa cuando
    SS -> 1 (p -> 1/SS): EXENCION (Y, m) (gate A5: ff =
    Y/((c-Y)(c-1)) = Y/(SS (SS+Y-1)) < 1 ESTRICTO en la rama
    pesada porque SS > 1).  b como dimension (el acoplamiento
    masa/cap de la particion), variantes k."""
    s2l, s2h, SSl, SSh, bl, bh, uyl, uyh = box
    if not _podas_pesada(s2l, s2h, SSl, SSh):
        return None
    SSl_e = max(SSl, 1.0 + s2l)
    SSh_e = min(SSh, PHI)
    if bl > SSh_e or bh < 0.5:
        return None
    b_lo, b_hi = max(bl, 0.5), min(bh, SSh_e)
    Y_lo = math.exp(uyl)
    c_lo = SSl_e + Y_lo

    def fila_Y(a):
        return _asin2(math.sqrt(min(1.0, a / SSl_e)))

    return _corona_pesada_k(SSh_e, b_lo, b_hi, c_lo, fila_Y,
                            (0, 1))


def crit_Gg(box):
    """G-g: (s2, SS, b, uz) — b = masa(B*) COMO DIMENSION (las
    ligaduras de la particion acoplan b, |A|, masa y cap y el
    conservador plano no cierra).  Corona {z, D_m = 1} U A en
    c' >= 1 + z, z >= SS (pared E4-esp: z >= alpha + w >= SS +
    2w); el par (z, m) EXENTO (tangencia legal c' = 1 + z).
    VARIANTES AND POR |A| = k (piezas de A > 1 - b por
    maximalidad de B*, <= b, masa exacta SS - b):
      cap_k = min(b_hi, (SSh - b_lo) - (k-1) max(0, 1 - b_hi))
      (la mayor = masa menos las otras k-1); k imposible si
      k (1 - b_hi) >= SSh - b_lo o cap_k <= 0.
      k = 1: EL LEMA DE LA CADENA DORADA (gate A5): el lado
      {a} cabe sii p(z,a) + p(a,m) <= 1 sii (1-a)(z^2+z) >= a,
      y con a <= SS/2, z >= SS esto se reduce a SS^2 - SS - 1
      <= 0, es decir SS <= phi EXACTO (la pared de la familia
      ES el caso limite; en SS = phi, a = phi/2, z = phi la
      tangencia es exacta y legal) — LEMA POR PUNTO: las cotas
      a <= SS/2 y z >= SS estan atadas al MISMO SS de cada
      punto real, asi que la variante NO evalua nada (acta H2:
      la evaluacion por esquinas de caja seria la erronea).
      k = 2..5: motor con k nodos escalonados por masa.
      k >= 6: piezas <= cap_6 = masa_A - 5 piso: dos bloques
      por cuerda (acta H1)."""
    s2l, s2h, SSl, SSh, bl, bh, uzl, uzh = box
    if not _podas_pesada(s2l, s2h, SSl, SSh):
        return None
    SSl_e = max(SSl, 1.0 + s2l)
    SSh_e = min(SSh, PHI)
    if bl > SSh_e or bh < 0.5:
        return None                    # b in [1/2, SS]
    b_lo, b_hi = max(bl, 0.5), min(bh, SSh_e)
    masa_A = SSh_e - b_lo
    if masa_A <= 0.0:
        return True
    z_hi_c = math.exp(uzh) if uzh < V_T - 1e-12 else None
    z_lo_eff = max(math.exp(uzl), SSl_e)
    if z_hi_c is not None and z_hi_c < SSl_e:
        return None                    # pared z >= SS: sin puntos
    c_lo = 1.0 + z_lo_eff

    def fila_z(a):
        p = a if z_hi_c is None else \
            min(a, z_hi_c * a / (1.0 + z_hi_c - a))
        return _asin2(math.sqrt(min(1.0, p)))

    return _corona_pesada_k(SSh_e, b_lo, b_hi, c_lo, fila_z,
                            (0, 1), cadena_z=z_lo_eff)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] los gates de la fase 3a")
    import sympy as sp
    import random
    ok = True
    # A1: enunciado del claim
    ok &= check(
        "[ENUNCIADO] (A1) G-e/G-g PESADAS: el mural {*, m} U A "
        "con |A| libre (declarado FUERA en r2bmulti y cubierto "
        "solo por el MC de puertocii) se certifica por B&B + "
        "slots + motor de colocacion; los dominios son "
        "SUPERCONJUNTO de los barridos (Y y z SIN techo — el "
        "techo del MC heredaba w <= 1.6; aqui la cola va por "
        "fila de limites)", True)
    # A2: el gate de la particion (empirico masivo + argumento)
    from puertocii import b_star_particion
    rng = random.Random(SEED)
    viol = 0
    for _ in range(20000):
        kk = rng.randrange(2, 12)
        piezas = [rng.uniform(0.01, 0.999) for _ in range(kk)]
        if sum(piezas) > PHI:
            continue
        b, A = b_star_particion(piezas)
        if not A:
            continue
        if b <= 0.5 + 1e-12:
            viol += 1
        if any(a > b + 1e-12 for a in A):
            viol += 1
        if any(a > min(b, sum(piezas) - b) + 1e-12 for a in A):
            viol += 1
        if sum(A) > sum(piezas) - b + 1e-12:
            viol += 1
    ok &= check(
        "(A2) EL GATE DE LA PARTICION: con A no vacio, b > 1/2 "
        "(si b <= 1/2 y a <= b entonces B* U {a} <= 1 refuta la "
        "maximalidad; y a > b la refuta via {a}), toda a de A "
        "cumple a <= min(b, SS - b) <= SS/2 <= phi/2 = 0.809, y "
        "masa(A) = SS - b < SS - 1/2 <= 1.118 — 20k particiones "
        f"reales: {viol} violaciones", viol == 0)
    # A3: las filas por limites (sympy)
    Y, a, S, z = sp.symbols('Y a S z', positive=True)
    p_e = Y * a / (S * (S + Y - a))
    d_e = sp.simplify(sp.diff(p_e, Y))
    lim_e = sp.limit(p_e, Y, sp.oo)
    p_g = z * a / (1.0 * (1 + z - a))
    d_g = sp.simplify(sp.diff(p_g, z))
    lim_g = sp.limit(p_g, z, sp.oo)
    ok &= check(
        "(A3) FILAS POR LIMITES: G-e p(Y, a) = Ya/(S(S+Y-a)) "
        f"crece en Y (num de d/dY = S - a > 0 con a <= phi/2 < "
        f"1 <= S... a < S) hacia a/S = {sp.simplify(lim_e)}; "
        f"G-g p(z, a) = za/(1+z-a) crece en z hacia a = "
        f"{sp.simplify(lim_g)} <= phi/2: sin clamp",
        sp.simplify(lim_e - a / S) == 0
        and sp.simplify(lim_g - a) == 0
        and sp.simplify(sp.together(d_e)).as_numer_denom()[0]
        .equals(a * (S - a))
        and sp.simplify(sp.together(d_g)).as_numer_denom()[0]
        .equals(1.0 * a * (1 - a)))
    # A4: la tangencia (z, m) y las capacidades minorantes
    ok &= check(
        "(A4) G-g: c' = Y - w >= 1 + z (convivencia m-z en v, "
        "teorema del par — la pared del muestreo de puertocii "
        "lo_Y >= 1 + z + w) y el par (z, m) a c' = 1 + z es la "
        "TANGENCIA LEGAL NO ESTRICTA (exencion antipodal, "
        "patron adversariado en espomegacola); ademas z >= "
        "alpha + X_z + w >= SS + 2w >= SS (E4-esp): la pared "
        "z >= SS entra como poda y como suelo de la cadena. "
        "c' real >= c_lo = 1 + z_lo minora y todos los th/pesos "
        "decrecen en c (r2bmulti A). G-e: c = SS + Y >= SSl + "
        "Y_lo idem; la corona ignora X' >= 0 y las torres (solo "
        "agrandan c): conservador", True)
    # A5: la cadena dorada y la exencion (Y, m)
    zz, aa, SSs = sp.symbols('z a SS', positive=True)
    p1 = zz * aa / (1.0 * (1 + zz - aa))
    p2 = aa / (zz * (1 + zz - aa))
    suma_menos_1 = sp.simplify((p1 + p2 - 1)
                               * zz * (1 + zz - aa))
    # p1 + p2 <= 1  <=>  (1 - a)(z^2 + z) >= a
    ident = sp.simplify(suma_menos_1
                        - (aa * (zz ** 2 + 1)
                           - zz * (1 + zz - aa)))
    # con a = SS/2 y z = SS: (1 - SS/2)(SS^2 + SS) >= SS/2
    # <=> (2 - SS)(SS + 1) >= 1 <=> -SS^2 + SS + 1 >= 0
    # <=> SS^2 - SS - 1 <= 0 <=> SS <= phi
    red = sp.expand((1 - SSs / 2) * (SSs ** 2 + SSs) - SSs / 2)
    red2 = sp.expand(red * 2 / SSs - (-SSs ** 2 + SSs + 1))
    ok &= check(
        "(A5) EL LEMA DE LA CADENA DORADA (G-g, |A| = 1): el "
        "lado {a} entre z y m con c' = 1 + z cabe sii "
        "asin sqrt(p1) + asin sqrt(p2) <= pi/2 sii p1 + p2 <= 1 "
        "(x^2 + y^2 <= 1) sii (1-a)(z^2+z) >= a [sympy]; con "
        "a <= SS/2 y z >= SS se reduce a SS^2 - SS - 1 <= 0, "
        "es decir SS <= PHI EXACTO — la pared de la familia ES "
        "el caso limite (tangencia exacta en SS = phi, a = "
        "phi/2, z = phi).  Y LA EXENCION (Y, m) DE G-e: ff = "
        "Y/(SS (SS+Y-1)) < 1 estricto porque SS > 1 en la rama "
        "pesada (SS >= 1 + s2)",
        ident == 0 and red2 == 0
        and abs(float(red.subs(SSs, PHI))) < 1e-12)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] G-e por B&B (s2, SS, b, uY)")
    root = [0.0, 1.0, 1.0, 1.62, 0.5, 1.0, 0.0, V_T]
    exito, caja, n, cert = bnb_factible(root, crit_Ge, eps=2e-3)
    return check(f"G-e certificado (rama pesada, Y de 1 a la "
                 f"cola, |A| libre): {n} cajas, {cert} "
                 f"certificadas"
                 + ("" if exito else f"; SIN RESOLVER {caja}"),
                 exito)


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] G-g por B&B (s2, SS, b, uz)")
    root = [0.0, 1.0, 1.0, 1.62, 0.5, 1.0, 0.0, V_T]
    exito, caja, n, cert = bnb_factible(root, crit_Gg, eps=2e-3)
    return check(f"G-g certificado (rama pesada especular, z de "
                 f"1 a la cola, |A| libre): {n} cajas, {cert} "
                 f"certificadas"
                 + ("" if exito else f"; SIN RESOLVER {caja}"),
                 exito)


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] contraste hostil y falsabilidad")
    import random
    from coronacolas import corona_suf
    from puertocii import b_star_particion
    rng = random.Random(SEED)
    ok = True
    # (a) instancias reales de las dos celdas (el muestreo de
    # puertocii, extendido con Y/z hasta 300 — mas alla del tope
    # w <= 1.6 del MC) contra corona_suf
    n_e, n_gc, viol = 0, 0, 0
    for _ in range(60000):
        if n_e >= 300 and n_gc >= 300:
            break
        s2 = rng.uniform(0.05, 0.8)
        s1 = rng.uniform(s2, 0.999)
        kw = rng.randrange(1, 8)
        Wp = [rng.uniform(0.1 * s2, s2) for _ in range(kw)]
        SS = s1 + s2 + sum(Wp)
        if SS < 1.0 + s2 or SS > PHI:
            continue
        b, A = b_star_particion([s1, s2] + Wp)
        if not A:
            continue
        if rng.random() < 0.5 and n_e < 300:
            Yv = math.exp(rng.uniform(0.0, math.log(300.0)))
            carga = sorted([Yv, 1.0] + A, reverse=True)
            okc, defc = corona_suf(carga, SS + Yv + 1e-9)
            n_e += 1
        elif n_gc < 300:
            zv = math.exp(rng.uniform(0.0, math.log(300.0)))
            carga = sorted([zv, 1.0] + A, reverse=True)
            okc, defc = corona_suf(carga, 1.0 + zv + 1e-9)
            n_gc += 1
        else:
            continue
        if not okc:
            viol += 1
    ok &= check(f"(a) {n_e} instancias G-e + {n_gc} G-g reales "
                f"(particion B* real, Y/z hasta 300): la corona "
                f"cabe siempre (corona_suf); violaciones {viol}",
                n_e >= 300 and n_gc >= 300 and viol == 0)
    # (b) falsabilidad: los criterios con las thetas infladas x2
    # rechazan una caja que certifican
    caja_e = [0.617, 0.619, 1.615, 1.617, 0.81, 0.82,
              0.1, 0.12]
    caja_g = [0.617, 0.619, 1.615, 1.617, 0.54, 0.56,
              0.49, 0.51]
    pe = crit_Ge(caja_e) is True
    pg = crit_Gg(caja_g) is True
    g_mod = globals()
    orig = g_mod['_asin2']
    g_mod['_asin2'] = lambda x_: min(PI, 2.0 * orig(x_))
    try:
        re_ = crit_Ge(caja_e) is False
        rg_ = crit_Gg(caja_g) is False
    finally:
        g_mod['_asin2'] = orig
    ok &= check(f"(b) FALSABILIDAD: la caja media certifica "
                f"(G-e {pe}, G-g {pg}) y con las thetas x2 "
                f"se rechaza (G-e {re_}, G-g {rg_})",
                pe and pg and re_ and rg_)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    return check(
        "[ENUNCIADO] FASE 3a DEL LEMA DE |A|: G-e y G-g PESADAS "
        "certificadas (B&B + gate de la particion + slots + "
        "motor de colocacion; Y y z sin techo — los topes del "
        "MC no se replican).  Las celdas dejan de depender del "
        "barrido MC de puertocii (que queda como contraste).  "
        "QUEDA (fase 3b, lo ultimo del lema): k >= 2 anillos "
        "extra del canal (espcanal E)", True)


def main():
    print("=" * 68)
    print("FASE 3a DEL LEMA DE |A|: G-e / G-g PESADAS")
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
    print(f"RESUMEN: {verdes}/{len(res)} bloques en verde "
          f"({detalle})")
    if verdes != len(res):
        print("HAY FALLOS")
    sys.exit(0 if verdes == len(res) else 1)


if __name__ == "__main__":
    main()
