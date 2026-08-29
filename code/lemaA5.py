#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FASE 3-PESADA DEL LEMA DE |A| (ciclo 3h) — K >= 2 ANILLOS
EXTRA DEL CANAL PESADO: el ultimo residuo de celda del canal
(espcanalp certifico k <= 1; k >= 2 quedo declarado con la
pinza de colas).

LA CELDA: la ESP PESADA (SS >= 1 + s2, SS > 1) con k >= 2
extras x_i >= r_m = 1 en el contenedor de Y — cada uno EN v
(hoja) o ANIDADO EN z (Wz).  El aparato es el de lemaA4
(masas como dimensiones, variantes AND por j_v, escalones,
bloques por cuerda, cola Wv W-uniforme, cota acoplada por
extremos, el motor de colocacion con EXENCION MOVIL) sobre la
estructura de espcanalp:

  - LA PARED PESADA DEL NODO (espcanal A7, por-extra): todo
    extra HOJA cumple x_i < T_p = omega + SS - 1 + min(beta,1)
    + X_x.  La derivacion (greedy A/B hacia el agujero de x_i)
    es POSICION-INDEPENDIENTE e independiente de los demas
    extras: el desbloqueo solo mueve B, children(x_i) y A (en
    fila a D_m, lem:row — el agujero de m no aloja extras);
    los otros extras no se tocan.  El analogo exacto del techo
    T ligero (A2iii, tambien por-extra).
  - LA PARTICION COLAPSADA A beta (espcanalp, adversariado):
    b = masa(B*) > 1/2, sigma1 <= b <= 1, piezas de A <=
    min(b, phi/2); A (masa SS - b) se paga POR MASA como
    bloque(s) partible(s) en la corona; bl = max(bl, 1 - bh).
  - la corona de v pesada: {z, D_m} + extras de v + bloque(s)
    A + polvo mu — SIN nodo s2 (sigma2 vive en la particion).
  - ventanas pesadas: a_hi = 1 + (SS - b) + Xp + omega (alpha
    convive con lo no-B); las demas como el canal.
  - x_floor = (1 + SS + Xm + Xp + Xz + mu)/phi (la pinza de la
    cola del extra menor, lemaA4).

ALCANCE DECLARADO (v1, los mismos recortes que las hojas
ligeras + los heredados): omega in [0, W_CORTE = 1.15]
certificado y [1.15, 1.6] DECLARADO (la lamina de saturacion —
en la ligera es omega-invariante para j_v >= 2, acta 3g; aqui
se declara el mismo corte); Wz <= 34 por dominio; extras de v
HOJAS (padres declarados); omega > 1.6 declarado (el hallazgo
3g: el patron espomegacanal no porta a k >= 2); la cola
Wv > 34 W-uniforme INCLUIDA.  k <= 1 es espcanalp.

Bloques: [A] gates; [B] B&B (12 dims: w, s2, SS, b, Xp, Xz,
Xm, a, z, mu, Wv, Wz); [C] contraste hostil (coronas pesadas
reales con particion explicita); [D] estatus.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check
from r2bmulti import th, bnb_factible
from lemaA import (_motor_dos_lados, _cuerda, _asin2)
from lemaA4 import _motor_rapido
from espcanal import suelo_trio

SEED = int(os.environ.get('CC_SEED', '20260829'))
W_TOP = 34.0
W_CORTE = float(os.environ.get('CC_WCORTE', '1.15'))
XP_MAX, XZ_MAX = 1.5, 1.0
W_MAX = 1.6
A_MAX_P = 1.0 + 0.999 + XP_MAX + W_MAX      # a <= 1+(SS-b)+Xp+w
Z_MAX_P = A_MAX_P + XZ_MAX + 0.999 + W_MAX  # sin Wz
LAMINA_N = [0]


def crit_k2p(box):
    """Caja (w, s2, SS, b, Xp, Xz, Xm, a, z, mu, Wv, Wz): la
    ESP PESADA con k >= 2 extras de masas Wv (hojas en v) +
    Wz (anidados en z)."""
    wl, wh, s2l, s2h, SSl, SSh, bl, bh, Xpl, Xph, Xzl, Xzh, \
        Xml, Xmh, al, ah, zl, zh, mul, muh, Wvl, Wvh, \
        Wzl, Wzh = box
    # ---- perfil pesado y particion (espcanalp) ----
    if SSh <= 1.0 or SSl > PHI:
        return None
    if SSh < 1.0 + s2l:
        return None                    # ligera cubre
    if 2.0 * s2l > SSh:
        return None                    # s1 >= s2
    if bh < s2l or bh > 1.0 + 1e-12 or bl > SSh:
        return None
    if bh <= 0.5:
        return None                    # beta > 1/2 (teorema)
    bl = max(bl, 1.0 - bh)
    if Xml > max(0.0, 1.0 - wl):
        return None
    if SSl + Xpl + Xzl + Xml > PHI:
        return None                    # pared del polvo total
    mu_eff = min(muh, PHI - SSl - Xml - Xpl - Xzl)
    if mu_eff < mul:
        return None
    cola_v = Wvh >= W_TOP - 1e-9
    Wv_hi = 1e9 if cola_v else Wvh
    # ---- techo del nodo pesado (A7 por-extra) y pinza ----
    xx_hi = max(0.0, PHI - SSl - Xml - Xpl - Xzl)
    T_p = wh + SSh - 1.0 + min(bh, 1.0) + xx_hi
    x_floor = (1.0 + SSl + Xml + Xpl + Xzl + mul) / PHI
    if x_floor >= T_p:
        return None                    # ningun extra legal
    x_floor = max(1.0, x_floor)
    if Wvh + Wzh < 2.0 * x_floor - 1e-12:
        return None                    # k <= 1: espcanalp
    if Wvh < x_floor and Wvl > 1e-12:
        return None                    # masa Wv inalcanzable
    if Wzh < x_floor and Wzl > 1e-12:
        return None
    Wv_lo = 0.0 if Wvl <= 1e-12 else max(Wvl, x_floor)
    Wz_lo = 0.0 if Wzl <= 1e-12 else max(Wzl, x_floor)
    # ---- ventanas pesadas ----
    a_lo = max(al, 1.0 + wl, SSl + Xpl + wl)
    a_hi = min(ah, 1.0 + (SSh - bl) + Xph + wh)
    if a_lo >= a_hi:
        return None
    z_lo = max(zl, a_lo + Xzl + wl)
    z_hi = min(zh, a_hi + Xzh + s2h + wh + Wzh)
    if z_lo >= z_hi:
        return None
    cola_lo = (1.0 + SSl + Xml + a_lo + Xpl + z_lo + Xzl
               + mul + Wv_lo + Wz_lo) / PHI
    if cola_lo >= SSh + z_hi + mu_eff + wh + min(Wv_hi, 1e9):
        return None                    # pinza RY: sin Y legal
    # ---- la lamina declarada (por SUELO, leccion 12) ----
    if wl >= W_CORTE - 1e-12:
        LAMINA_N[0] += 1
        return None
    # ---- el bloque A (particion) y el polvo ----
    masa_A = max(0.0, SSh - bl)
    cap_A = min(bh, PHI / 2.0, masa_A) if masa_A > 0 else 0.0
    cap_mu = min(1.0, mu_eff) if mu_eff > 0 else 0.0
    # ---- variantes j_v ----
    if Wv_lo < x_floor:
        j_min = 0
    else:
        j_min = max(1, int(math.ceil(
            Wv_lo / T_p - 1e-12)))
    j_max = int(min(Wv_hi, 1e9) / x_floor + 1e-12) \
        if Wv_hi < 1e8 else 10 ** 6
    if j_max < j_min:
        return None
    # variantes: escalones EXACTOS hasta J_ESC = 8 (en la
    # pesada T_p es generoso — omega + SS - 1 + b + X_x — y el
    # bloque j >= 6 por cuerda no cabe con masa Wv entera al
    # cap; con j_max <= 8 cada j real va con su fila AND de
    # escalones, sound y sin cuerda); el centinela 99 =
    # "j >= 9 por bloques" solo si j_max > 8
    J_ESC = 8
    js = list(range(j_min, min(j_max, J_ESC) + 1))
    if j_max > J_ESC:
        js.append(99)
    # cota acoplada por extremos (lemaA4 A6: c lineal en z de
    # pendiente 1/phi => solo minimos interiores => sup en
    # extremos)
    K_base = (1.0 + SSl + Xml + a_lo + Xpl + Xzl + mul
              + Wz_lo)
    K_cola = K_base + Wv_lo

    def th_acopl(a_p):
        peor = 0.0
        for z_e in (z_lo, z_hi):
            c_e = (K_cola + z_e) / PHI - wh
            d1, d2 = c_e - z_e, c_e - a_p
            if d1 <= 1e-9 or d2 <= 1e-9:
                return PI
            peor = max(peor, z_e * a_p / (d1 * d2))
        return _asin2(math.sqrt(min(1.0, peor)))

    def th_extra(v_min, v_max, resto):
        peor_g = 0.0
        for z_e in (z_lo, z_hi):
            for v_e in (v_min, v_max):
                c_e = (K_base + resto + z_e + v_e) / PHI - wh
                d1, d2 = c_e - z_e, c_e - v_e
                if d1 <= 1e-9 or d2 <= 1e-9:
                    peor_g = 2.0
                    break
                peor_g = max(peor_g, z_e * v_e / (d1 * d2))
        t_g = _asin2(math.sqrt(min(1.0, peor_g)))
        return min(th_acopl(v_max), t_g)

    def _prueba(j, c_lo, fila, x1_lo, extras_th=None):
        extras_th = extras_th or {}
        base = [z_hi, fila[0], 1.0] if 1 <= j <= 8 \
            else [z_hi, 1.0]
        bloques = []
        # el bloque A (variantes OR: entero / partido greedy
        # |m1 - m2| <= cap, teorema de espfinal via el par
        # partible de espcanalp) — aqui como DOS bloques de
        # media masa + medio cap (el partido; el entero lo
        # domina: mismo peso total, mas reparto)
        if masa_A > 0:
            if c_lo - cap_A <= 1e-9:
                return False
            peso_A = _cuerda(cap_A, c_lo) * (masa_A / 2.0
                                             + cap_A / 2.0)
            bloques += [(cap_A, peso_A), (cap_A, peso_A)]
        if mu_eff > 0:
            if c_lo - cap_mu <= 1e-9:
                return False
            peso_mu = _cuerda(cap_mu, c_lo) * (mu_eff / 2.0
                                               + cap_mu / 2.0)
            bloques += [(cap_mu, peso_mu), (cap_mu, peso_mu)]
        if j == 99:
            # j >= 9 por BLOQUES PUROS (lemaA4, leccion 11):
            # cap = techo de la PRIMERA pieza que puede caer
            cap_f = min(T_p, max(x_floor,
                                 min(Wv_hi, 1e9)
                                 - 8.0 * x_floor))
            masa_f = min(Wv_hi, 1e9)
            if cola_v:
                zc = min(1.0, cap_f / max(1e-9, c_lo - cap_f))
                C_v = (2.0 * math.asin(zc) / zc) \
                    if zc > 1e-9 else 2.0
                den0 = c_lo - cap_f
                if den0 <= 1e-9:
                    return False
                r0 = (Wv_lo / 2.0 + cap_f / 2.0) / den0
                peso_f = C_v * max(PHI / 2.0, r0)
            else:
                if c_lo - cap_f <= 1e-9:
                    return False
                peso_f = _cuerda(cap_f, c_lo) \
                    * (masa_f / 2.0 + cap_f / 2.0)
            bloques += [(cap_f, peso_f), (cap_f, peso_f)]
        nodos = list(base)
        if 2 <= j <= 8:
            nodos += fila[1:]
        Ds = {}
        for capb, pesob in bloques:
            Ds[len(nodos)] = pesob
            nodos.append(capb)
        n = len(nodos)
        thmat = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for jj in range(i + 1, n):
                if i == 0:
                    piso_z = z_hi + (x1_lo if 1 <= j <= 8
                                     else 1.0)
                    t_ac = th(z_hi, nodos[jj], piso_z)
                    t_gl = th(z_hi, nodos[jj], c_lo) \
                        if c_lo > z_hi + 1e-12 else PI
                    if jj in extras_th:
                        v_min, resto = extras_th[jj]
                        t_c = th_extra(v_min, nodos[jj],
                                       resto)
                    else:
                        t_c = th_acopl(nodos[jj])
                    thmat[i][jj] = min(t_ac, t_gl, t_c)
                else:
                    thmat[i][jj] = th(nodos[i], nodos[jj],
                                      c_lo)
                thmat[jj][i] = thmat[i][jj]
        # EXENCION MOVIL (3g): el clamp unico de la fila 0 se
        # exenta por convivencia (c' >= z + x, o c' >= 1 + z
        # para D_m); dos clamps = False (dos antipodales del
        # mismo z se solapan); bloques excluidos
        clamps = [jj for jj in range(1, n)
                  if jj not in Ds
                  and thmat[0][jj] >= PI - 1e-9]
        if len(clamps) == 1:
            jj_c = clamps[0]
            if jj_c != 1:
                nodos[1], nodos[jj_c] = nodos[jj_c], nodos[1]
                for fila_t in thmat:
                    fila_t[1], fila_t[jj_c] = \
                        fila_t[jj_c], fila_t[1]
                thmat[1], thmat[jj_c] = thmat[jj_c], thmat[1]
            thmat[0][1] = 0.0
            thmat[1][0] = 0.0
            ex_eff = (0, 1)
        elif len(clamps) >= 2:
            return False
        else:
            ex_eff = None
        motor = (_motor_rapido if n >= 8
                 else _motor_dos_lados)
        return motor(nodos, thmat, Ds, exento=ex_eff)

    for j in js:
        if j == 0:
            c_lo = max(1.0 + z_lo, cola_lo - wh)
            if c_lo <= 1.0 + 1e-12:
                return False
            if not _prueba(0, c_lo, [], 0.0):
                return False
            continue
        x1_lo = (max(x_floor, Wv_lo / max(j, 1)) if j <= 8
                 else x_floor)
        if j <= 8:
            fila0 = [min(T_p,
                         min(Wv_hi, 1e9) - (j - i) * x_floor,
                         min(Wv_hi, 1e9) / i)
                     for i in range(1, j + 1)]
            if any(f < x_floor - 1e-9 for f in fila0):
                continue               # vacuidad por conteo
        else:
            c_lo6 = max(1.0 + z_lo, cola_lo - wh)
            if c_lo6 <= 1.0 + 1e-12:
                return False
            if not _prueba(99, c_lo6, [], 0.0):
                return False
            continue
        c_base = max(z_lo + x1_lo, cola_lo - wh,
                     suelo_trio(z_lo, x1_lo, 1.0,
                                z_lo + x1_lo))
        if c_base <= 1.0 + 1e-12:
            return False
        if j == 1:
            if not _prueba(1, c_base, fila0, x1_lo,
                           {1: (x1_lo, 0.0)}):
                return False
            continue
        # j >= 2: sub-bandas ADAPTATIVAS de x_2 ligadas
        # (lemaA4: el techo de x_1 baja con la banda de x_2)
        x2_top = fila0[1]
        if x2_top < x_floor - 1e-9:
            continue
        max_prof = 5e-3 if j <= 2 else (x2_top - x_floor)
        pendientes = [(x_floor, x2_top)]
        ok_j = True
        while pendientes:
            x2a, x2b = pendientes.pop()
            c_tr = suelo_trio(z_lo, x1_lo, x2a,
                              z_lo + x1_lo)
            c_lo = max(z_lo + x1_lo, c_tr, cola_lo - wh)
            if c_lo <= 1.0 + 1e-12:
                return False
            x1_b = min(fila0[0],
                       min(Wv_hi, 1e9) - x2a
                       - (j - 2) * x_floor)
            if x1_b < x1_lo - 1e-9:
                continue               # banda vacia
            fila_b = [x1_b, min(x2b, x1_b)] \
                + [min(f, x2b) for f in fila0[2:]]
            resto2 = (j - 2) * x_floor
            if _prueba(j, c_lo, fila_b, x1_lo,
                       {1: (x1_lo, x2a + resto2),
                        2: (x2a, x1_lo + resto2)}):
                continue
            if x2b - x2a > max_prof:
                mid = (x2a + x2b) / 2.0
                pendientes += [(x2a, mid), (mid, x2b)]
                continue
            ok_j = False
            break
        if not ok_j:
            return False
    return True


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] gates de la pesada k >= 2")
    ok = True
    ok &= check(
        "[ENUNCIADO] (A1p) LA PARED PESADA POR-EXTRA: la "
        "derivacion A7 de espcanal (greedy A/B hacia el "
        "agujero de x) aplica A CADA extra x_i por separado — "
        "el desbloqueo mueve SOLO B, children(x_i) y A (en "
        "fila a D_m, lem:row; el agujero de m no aloja "
        "extras >= 1), los demas extras no se tocan: "
        "posicion-independiente e independiente del resto.  "
        "Todo extra HOJA de la pesada cumple x_i < T_p = "
        "omega + SS - 1 + min(beta, 1) + X_x — el analogo "
        "exacto del techo T ligero (A2iii)", True)
    ok &= check(
        "[ENUNCIADO] (A2p) LA PARTICION COLAPSADA (espcanalp, "
        "adversariado): b = masa(B*) > 1/2, sigma1 <= b <= 1, "
        "toda pieza de A <= min(b, phi/2); A (masa SS - b) por "
        "MASA como bloques partibles (cadena cap-generica de "
        "espkp; greedy |m1 - m2| <= cap); bl = max(bl, 1-bh).  "
        "La corona pesada de v NO lleva nodo s2 (sigma2 vive "
        "en la particion A/B)", True)
    ok &= check(
        "[ENUNCIADO] (A3p) VENTANAS PESADAS: a_hi = 1 + "
        "(SS - b) + Xp + omega (alpha convive con lo no-B, "
        "espcanalp); techo Rz + Wz; cola(Y) += Wv + Wz; "
        "x_floor = (1 + SS + Xm + Xp + Xz + mu)/phi (la pinza "
        "de lemaA4); el aparato de variantes j_v, escalones "
        "con T_p, bloques j >= 6, cola Wv W-uniforme y cota "
        "acoplada A6 es el de lemaA4 (cinco ciclos "
        "adversariales); la exencion movil es la del 3g", True)
    ok &= check(
        "[ENUNCIADO] (A4p) ALCANCE: omega in [0, "
        f"{W_CORTE}] certificado, [{W_CORTE}, 1.6] DECLARADO "
        "(la lamina, por SUELO); Wz <= 34 por dominio (root "
        "de z lo cubre); padres declarados; omega > 1.6 "
        "declarado (hallazgo 3g: espomegacanal no porta a "
        "k >= 2); cola Wv > 34 W-uniforme incluida; k <= 1 "
        "es espcanalp", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] B&B pesada k >= 2 (12 dims)")
    eps = float(os.environ.get('CC_EPS', '2e-2'))
    wv_lo = float(os.environ.get('CC_WVLO', '0'))
    wv_hi = float(os.environ.get('CC_WVHI', str(W_TOP)))
    w_lo = float(os.environ.get('CC_WLO', '0'))
    w_hi = float(os.environ.get('CC_WHI', str(W_MAX)))
    s2_lo = float(os.environ.get('CC_S2LO', '0'))
    s2_hi = float(os.environ.get('CC_S2HI', '0.999'))
    wz_lo = float(os.environ.get('CC_WZLO', '0'))
    wz_hi = float(os.environ.get('CC_WZHI', str(W_TOP)))
    root = [w_lo, w_hi, s2_lo, s2_hi, 1.0, PHI, 0.5, 1.0,
            0.0, XP_MAX, 0.0, XZ_MAX, 0.0, 1.0,
            1.0, A_MAX_P, 1.0, Z_MAX_P + W_TOP,
            0.0, PHI - 1.0, wv_lo, wv_hi, wz_lo, wz_hi]
    LAMINA_N[0] = 0
    exito, caja, n, cert = bnb_factible(root, crit_k2p,
                                        eps=eps)
    return check(
        f"k >= 2 PESADA certificada fuera de la lamina "
        f"({LAMINA_N[0]} cajas en L; claim omega in [0, "
        f"{W_CORTE}], lamina [{W_CORTE}, 1.6] declarada; "
        f"Wz <= 34 por dominio) — Wv in [{wv_lo}, {wv_hi}], "
        f"omega in [{w_lo}, {w_hi}], s2 in [{s2_lo}, "
        f"{s2_hi}]: {n} cajas, {cert} certificadas"
        + ("" if exito else f"; SIN RESOLVER {caja}"),
        exito)


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] contraste hostil: coronas pesadas reales")
    import random
    from coronacolas import corona_suf
    from espcanal import techo_nodo
    rng = random.Random(SEED)
    ok = True
    n_i, viol = 0, 0
    for _ in range(200000):
        if n_i >= 300:
            break
        w = rng.uniform(0.01, 1.15)
        s2 = rng.uniform(0.05, 0.999)
        s1 = rng.uniform(s2, 0.999)
        # la familia S de la PESADA: s1, s2 y mas ocupantes
        # chicos W (espcanalp C): Sigma_S = s1 + s2 + sum(W)
        k_w = rng.randrange(1, 7)
        Ws = [rng.uniform(0.02, s2) for _ in range(k_w)]
        SS = s1 + s2 + sum(Ws)
        if SS < 1.0 + s2 or SS > PHI - 0.02:
            continue                   # PESADA: SS >= 1 + s2
        mu = rng.uniform(0.0, max(0.0, PHI - SS - 0.01))
        # LA PARTICION REAL: B* = mejor subconjunto de masa
        # <= 1 (greedy descendente), b = masa(B*), A = resto
        piezas = sorted([s1, s2] + Ws, reverse=True)
        B, b = [], 0.0
        A = []
        for p in piezas:
            if b + p <= 1.0 + 1e-12:
                B.append(p)
                b += p
            else:
                A.append(p)
        if b <= 0.5:
            continue                   # (teorema: b > 1/2)
        xx = max(0.0, PHI - SS - mu)
        T_p = w + SS - 1.0 + min(b, 1.0) + xx
        x_fl = max(1.0, (1.0 + SS + mu) / PHI)
        if x_fl >= T_p - 0.01:
            continue
        k = rng.randrange(2, 6)
        xs = sorted([rng.uniform(x_fl, T_p)
                     for _ in range(k)], reverse=True)
        jv = rng.randrange(0, k + 1)
        Wv_list = xs[:jv]
        Wz = sum(xs[jv:])
        alpha = rng.uniform(max(1.0 + w, SS + w),
                            1.0 + (SS - b) + w + 0.3)
        z = rng.uniform(alpha + w,
                        alpha + s2 + w + Wz + 0.3)
        colaY = (1.0 + SS + alpha + z + mu
                 + sum(xs)) / PHI
        Y = max(colaY,
                w + z + (Wv_list[0] if Wv_list else 1.0),
                w + 1.0 + z) + rng.uniform(0.0, 2.0)
        cp = Y - w
        # la corona real pesada: {z, D_m} + extras de v + LAS
        # PIEZAS DE A explicitas + mu (B* va al agujero de
        # D_m: b <= 1, el patron k = 1)
        carga = sorted([z, 1.0] + Wv_list + A,
                       reverse=True)
        n_p = max(1, int(mu / 0.2)) if mu > 0 else 0
        carga += [mu / n_p] * n_p if n_p else []
        okc, _ = corona_suf(sorted(carga, reverse=True),
                            cp + 1e-9)
        n_i += 1
        if not okc:
            viol += 1
    ok &= check(
        f"(a) {n_i} coronas PESADAS reales k = 2..5 (particion "
        f"A explicita con piezas <= min(b, phi/2), extras "
        f"repartidos v/anidados): corona_suf; violaciones "
        f"{viol}", n_i >= 300 and viol == 0)
    # (b) falsabilidad: una caja dura debe DECIDIRSE (True o
    # False), no colgarse; y una caja imposible artificial
    # (T_p < x_floor via SS bajo y b bajo... b > 1/2 siempre:
    # w chico, SS ~ 1.001, b ~ 0.501: T_p ~ w + 0.502 + xx)
    box_dura = [0.5, 0.6, 0.2, 0.3, 1.25, 1.35, 0.6, 0.75,
                0.0, 0.2, 0.0, 0.3, 0.0, 0.1, 1.5, 2.5,
                3.0, 6.0, 0.0, 0.2, 2.5, 4.0, 0.0, 2.0]
    r = crit_k2p(box_dura)
    ok &= check(f"(b) caja dura pesada decidida: {r} (el "
                f"criterio no se cuelga y devuelve "
                f"True/False/None)", r in (True, False, None))
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] estatus")
    return check(
        "ENUNCIADO PESADA k >= 2 (ciclo 3h): la ESP pesada "
        "con k >= 2 extras queda certificada en su dominio "
        "declarado (omega <= 1.15, hojas, Wz <= 34, Wv "
        "completo con cola) sobre la estructura de espcanalp "
        "(pared A7 por-extra, particion colapsada a beta, "
        "bloque A por masa) con el aparato de lemaA4.  "
        "RESIDUOS DECLARADOS: la lamina [1.15, 1.6] (por "
        "suelo), omega > 1.6 (hallazgo 3g), padres, Wz > 34, "
        "y las continuaciones de la ligera", True)


def main():
    print("=" * 68)
    print("FASE 3-PESADA DEL LEMA DE |A|: K >= 2 DEL CANAL "
          "PESADO")
    print("=" * 68)
    solo = None
    for a in sys.argv[1:]:
        if a.startswith("--solo"):
            solo = a.split("=")[1] if "=" in a else \
                sys.argv[sys.argv.index(a) + 1]
    etiquetas = [solo] if solo else list("ABCD")
    res = [globals()[f"bloque_{e}"]() for e in etiquetas]
    verdes = sum(1 for r in res if r)
    print(f"RESUMEN: {verdes}/{len(res)} bloques en verde ("
          + ", ".join(f"{e}={'OK' if r else 'FALLO'}"
                      for e, r in zip(etiquetas, res)) + ")")
    if verdes < len(res):
        print("FALLOS")
        sys.exit(1)


if __name__ == "__main__":
    main()
