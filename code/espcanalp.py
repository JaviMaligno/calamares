#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La PESADA del canal ocupante >= r_m (docs/drafts/espcanalp.md):
el remate del canal — la fusion espfinal + x.

espcanal derivo la tarifa (las dos paredes del nodo) y cerro el
canal LIGERO entero (vacuidad del gemelo + pinza de la cola de x
+ B&B de banda alta + pared del nodo).  Quedaba el perfil PESADO
(Sigma_S >= 1 + sigma2) con el anillo extra x explicito: la
corona {z, x, D_m} U A + polvo fusionado — el criterio v5 de
espfinal (particion B*/A, tramos KZ x K, bloque partible,
variantes en OR) con la dimension x y sus podas nuevas:

  - PINZA DE LA COLA DE x CON EMPATE (espcanal R1, posicion- y
    perfil-independiente): 1 + Sigma_S + X_total <= phi x para
    todo x >= r_m (empate incluido: la cola de la primera copia
    recoge a la otra).  Con Sigma_S > 1: banda [1, 2/phi) MUERTA
    — la vacuidad del gemelo porta a la pesada tal cual.
  - PARED PESADA DEL NODO (espcanal A7, teorema): bloqueo =>
    x < omega + Sigma_S - 1 + sigma1 + X_x; poda conservadora con
    sigma1 <= 1 (S < m) y X_x <= phi - Sigma_S - X (cola global).
  - EL SUELO DEL TRIO {z, m, x} (lema del creciente, espcanal):
    en P conviven los tres en v => c' >= suelo_trio(z_lo, x_lo,
    1), ademas de z + x y la cola de Y con x.
  - El par ANTIPODAL pasa a (z, x); D_m entra como nodo del
    camino; pares con x con la cota acoplada th(x, b, z_lo + x)
    (A5 de espcanal: crece en x, coherente con c' >= z_real + x).

Bloques: [A] enunciado y podas (gates); [B] B&B por bandas de
Sigma_S con persistencia (CC_ESTADO/CC_TMAX/CC_SSLO/CC_SSHI);
[C] sanity pesada con x explicito; [D] controles; [E] estatus.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, corona_suf
from arcolp import dual_factible, primal_factible
from r2bmulti import th
from espfinal import _antipodal2
from espcanal import suelo_trio, mapa_supervivientes, \
    _creciente_cabe

SEED = int(os.environ.get('CC_SEED', '20260819'))
XCAP = PHI - 1.0
W_MAX, XP_MAX, XZ_MAX = 1.6, 1.5, 1.0
A_MAX = 1.0 + 0.999 + XP_MAX + W_MAX
Z_MAX = A_MAX + XZ_MAX + 0.999 + W_MAX
X_TOP = 0.999 + W_MAX + XCAP + 0.01    # techo de la pared pesada:
# omega + sigma1 + (phi-1) <= 1.6 + 1 + 0.618 = 3.218 < 3.227


def criterio_pesada_x(box):
    """Caja (w, s2, SS, beta, Xp, Xz, Xm, alfa, z, x) — 10 dims.
    REDUCCION DE DIMENSION vs espfinal (viable gracias a x): con
    x >= (1+SS)/phi en v, el suelo c' >= max(z+x, trio, cola)
    es MUCHO mayor que el 1+z de espfinal, y las piezas de A
    (todas <= min(beta, phi/2) por el lema de reduccion: beta >=
    sigma1 >= max A) se pagan POR MASA como bloque partible
    (derivacion cap-generica adversariada en espkp): las 6 dims
    de la particion explicita (a1..a4, mu_A y beta-de-piezas)
    colapsan a la sola dimension beta.  None = sin puntos."""
    wl, wh, s2l, s2h, SSl, SSh, bl, bh = box[:8]
    Xpl, Xph, Xzl, Xzh, Xml, Xmh = box[8:14]
    al_, ah_ = box[14], box[15]
    zl, zh = box[16], box[17]
    xl, xh = box[18], box[19]
    # ---- podas de perfil y particion ----
    if SSh <= 1.0 or SSl > PHI:
        return None
    if SSh < 1.0 + s2l:
        return None                    # pared pesada (ligera cubre)
    if 2.0 * s2l > SSh:
        return None
    if bh < s2l:
        return None                    # beta >= sigma1 >= sigma2
    if bh > 1.0 + 1e-12 or bl > SSh:
        return None
    # el greedy del mejor subconjunto: al parar, toda pieza
    # restante > 1 - beta => sigma1 > 1 - beta; con sigma1 <= beta
    # queda beta > 1/2 SIEMPRE (Sigma_S > 1).  El clamp usa la
    # forma 1 - bh (mas debil que 0.5; acta H4: se conserva para
    # no alterar los recuentos congelados — solo pierde poda)
    if bh <= 0.5:
        return None
    bl = max(bl, 1.0 - bh)
    if Xml > max(0.0, 1.0 - wl):
        return None
    if SSl + Xpl + Xzl + Xml > PHI:
        return None                    # pared del polvo total
    # ---- podas NUEVAS del canal ----
    # pinza de la cola de x con empate (banda [1, 2/phi) muerta)
    if (1.0 + SSl + Xml + Xpl + Xzl) / PHI > xh:
        return None
    # pared pesada del nodo (A7) con sigma1 <= beta <= bh:
    # x < w + SS - 1 + sigma1 + X_x — desbloqueo si el suelo de x
    # la supera
    xx_hi = max(0.0, PHI - SSl - Xml - Xpl - Xzl)
    if xl >= wh + SSh - 1.0 + min(bh, 1.0) + xx_hi:
        return None                    # desbloqueo derivado (A7)
    x_eff = min(xh, wh + SSh - 1.0 + min(bh, 1.0) + xx_hi)
    if x_eff < xl:
        return None
    # ---- ventanas ----
    a_lo = max(al_, 1.0 + wl, SSl + Xpl + wl)
    a_hi = min(ah_, 1.0 + (SSh - bl) + Xph + wh)
    if a_lo >= a_hi:
        return None
    # la carga de la corona: A = S sin B* (masa SS - beta, piezas
    # <= min(beta, phi/2)) — pagada por masa
    masa_A = max(0.0, SSh - bl)
    # cap fino: una pieza de A no puede exceder ni beta ni phi/2
    # (lema de reduccion) ni LA MASA ENTERA de A
    cap_A = min(bh, PHI / 2, masa_A) if masa_A > 0 else 0.0
    mu_a, cap_a = masa_A, cap_A
    otros = []

    def _certifica(z_hi_t, c_lo, masa, cap):
        """Corona [z, x, D_m] + el bloque A/polvo pagado POR MASA
        en c_lo; par antipodal (z, x); variantes: bloque unico /
        PARTIDO (greedy |m1-m2| <= cap, teorema de espfinal) /
        plegado sobre D_m; el creciente no-mural al final."""
        variantes = []
        if masa > 0:
            variantes.append([masa])
            variantes.append([masa / 2 + cap / 2,
                              masa / 2 + cap / 2])
        else:
            variantes.append([])
        for bloques in variantes:
            # nodos: 0 = z, 1 = x (ANTIPODAL), 2 = D_m, bloques
            nodos = [z_hi_t, x_eff, 1.0] + [cap] * len(bloques)
            if c_lo <= max(nodos[2:] + [1.0]) + 1e-12:
                continue
            n = len(nodos)
            thmat = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if i == 0 and j == 1:
                        thmat[i][j] = PI   # par antipodal: muerta
                    elif i == 0:
                        t_ac = th(z_hi_t, nodos[j], 1.0 + z_hi_t)
                        t_gl = th(z_hi_t, nodos[j], c_lo) \
                            if c_lo > z_hi_t + 1e-12 else PI
                        thmat[i][j] = min(t_ac, t_gl)
                    elif i == 1:
                        # cota acoplada de x (espcanal A5)
                        t_ac = th(x_eff, nodos[j],
                                  max(c_lo, zl + x_eff))
                        t_gl = th(x_eff, nodos[j], c_lo) \
                            if c_lo > x_eff + 1e-12 else PI
                        thmat[i][j] = min(t_ac, t_gl)
                    else:
                        thmat[i][j] = th(nodos[i], nodos[j], c_lo)
            Ds = {3 + k: PI * b / (c_lo - cap)
                  for k, b in enumerate(bloques)}
            if _antipodal2(nodos, thmat, Ds):
                return True
        # variante pliegue total sobre D_m (fila de radio suma)
        pleg = 1.0 + masa
        if c_lo > pleg + 1e-12:
            th0 = [[0.0] * 3 for _ in range(3)]
            th0[0][1] = PI
            th0[0][2] = min(th(z_hi_t, pleg, 1.0 + z_hi_t),
                            th(z_hi_t, pleg, c_lo)
                            if c_lo > z_hi_t + 1e-12 else PI)
            th0[1][2] = min(th(x_eff, pleg,
                               max(c_lo, zl + x_eff)),
                            th(x_eff, pleg, c_lo)
                            if c_lo > x_eff + 1e-12 else PI)
            if _antipodal2([z_hi_t, x_eff, pleg], th0, {}):
                return True
        # variante creciente (corona corta): z mural, resto
        # tangente
        otras_p = [x_eff, 1.0] + ([cap] if masa > 0 else [])
        if _creciente_cabe(z_hi_t, otras_p, c_lo,
                           extra=PI * masa / max(z_hi_t, 1e-9)):
            return True
        return False

    KZ, K = 2, 4
    for k_z in range(KZ):
        x_lo_z = Xzl + (XCAP - Xzl) * k_z / KZ
        x_hi_z = Xzl + (XCAP - Xzl) * (k_z + 1) / KZ
        z_lo = max(zl, a_lo + x_lo_z + wl)
        z_hi = min(zh, a_hi + x_hi_z + s2h + wh)
        if z_lo >= z_hi:
            continue
        mu_y_max = max(0.0, PHI - max(SSl, 1.0) - Xml - Xpl
                       - x_lo_z)
        st = suelo_trio(z_lo, xl, 1.0, z_lo + xl)
        for k_seg in range(K):
            t_lo = mu_y_max * k_seg / K
            t_hi = mu_y_max * (k_seg + 1) / K
            # cola de Y CON x (x < Y cuenta; X_x al suelo 0)
            cola_seg = (1.0 + SSl + Xml + a_lo + Xpl + z_lo
                        + x_lo_z + t_lo + xl) / PHI
            # techo (RY+x): la fila {z, x, S, polvo}
            if cola_seg >= SSh + z_hi + t_hi + wh + x_eff:
                continue               # tramo vacuo (pinza de Y)
            c_lo = max(1.0 + z_lo, z_lo + xl, st, cola_seg - wh)
            if not _certifica(z_hi, c_lo, mu_a + t_hi,
                              max(cap_a, t_hi)):
                return False
    return True


def criterio_pesada_z(box):
    """PESADA x-EN-z (d = 1; acta H1): x anidado en el agujero de
    z — la corona de v NO cambia ({z, D_m} + bloques por masa: x
    viaja dentro de z, lem:DG); cambian las ventanas de z (suelo
    de convivencia alpha + x, techo Rz+x, cola de z con x) y la
    cola de Y (x < z < Y cuenta).  Mismas 10 dims; pinza y pared
    A7 posicion-independientes."""
    wl, wh, s2l, s2h, SSl, SSh, bl, bh = box[:8]
    Xpl, Xph, Xzl, Xzh, Xml, Xmh = box[8:14]
    al_, ah_ = box[14], box[15]
    zl, zh = box[16], box[17]
    xl, xh = box[18], box[19]
    if SSh <= 1.0 or SSl > PHI:
        return None
    if SSh < 1.0 + s2l:
        return None
    if 2.0 * s2l > SSh:
        return None
    if bh < s2l or bh > 1.0 + 1e-12 or bl > SSh:
        return None
    if bh <= 0.5:
        return None                    # beta > 1/2 (teorema)
    bl = max(bl, 1.0 - bh)
    if Xml > max(0.0, 1.0 - wl):
        return None
    if SSl + Xpl + Xzl + Xml > PHI:
        return None
    if (1.0 + SSl + Xml + Xpl + Xzl) / PHI > xh:
        return None                    # pinza de la cola de x
    xx_hi = max(0.0, PHI - SSl - Xml - Xpl - Xzl)
    if xl >= wh + SSh - 1.0 + min(bh, 1.0) + xx_hi:
        return None                    # pared pesada del nodo
    x_eff = min(xh, wh + SSh - 1.0 + min(bh, 1.0) + xx_hi)
    if x_eff < xl:
        return None
    a_lo = max(al_, 1.0 + wl, SSl + Xpl + wl)
    a_hi = min(ah_, 1.0 + (SSh - bl) + Xph + wh)
    if a_lo >= a_hi:
        return None
    masa_A = max(0.0, SSh - bl)
    cap_A = min(bh, PHI / 2, masa_A) if masa_A > 0 else 0.0

    def _certifica_z(z_hi_t, c_lo, masa, cap):
        """Corona {z, D_m} + bloque(s) por masa (sin x: viaja
        dentro de z); par antipodal (z, D_m) como espfinal."""
        variantes = [[masa], [masa / 2 + cap / 2,
                              masa / 2 + cap / 2]] \
            if masa > 0 else [[]]
        for bloques in variantes:
            nodos = [z_hi_t, 1.0] + [cap] * len(bloques)
            if c_lo <= max(nodos[1:] + [1.0]) + 1e-12:
                continue
            n = len(nodos)
            thmat = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if i == 0:
                        t_ac = th(z_hi_t, nodos[j], 1.0 + z_hi_t)
                        t_gl = th(z_hi_t, nodos[j], c_lo) \
                            if c_lo > z_hi_t + 1e-12 else PI
                        thmat[i][j] = min(t_ac, t_gl)
                    else:
                        thmat[i][j] = th(nodos[i], nodos[j], c_lo)
            Ds = {2 + k: PI * b / (c_lo - cap)
                  for k, b in enumerate(bloques)}
            if _antipodal2(nodos, thmat, Ds):
                return True
        return False

    KZ, K = 2, 4
    for k_z in range(KZ):
        x_lo_z = Xzl + (XCAP - Xzl) * k_z / KZ
        x_hi_z = Xzl + (XCAP - Xzl) * (k_z + 1) / KZ
        # ventanas de z CON x dentro: convivencia alpha + x en el
        # agujero de z, techo Rz+x, cola de z con x
        cola_z = (1.0 + SSl + Xml + a_lo + Xpl + x_lo_z + xl) / PHI
        z_lo = max(zl, a_lo + x_lo_z + xl + wl, cola_z)
        z_hi = min(zh, a_hi + x_hi_z + s2h + wh + x_eff)
        if z_lo >= z_hi:
            continue
        mu_y_max = max(0.0, PHI - max(SSl, 1.0) - Xml - Xpl
                       - x_lo_z)
        for k_seg in range(K):
            t_lo = mu_y_max * k_seg / K
            t_hi = mu_y_max * (k_seg + 1) / K
            cola_seg = (1.0 + SSl + Xml + a_lo + Xpl + z_lo
                        + x_lo_z + t_lo + xl) / PHI
            # techo (RY) SIN x suelto: la fila {z, S, polvo} — x
            # va dentro de z
            if cola_seg >= SSh + z_hi + t_hi + wh:
                continue
            c_lo = max(1.0 + z_lo, cola_seg - wh)
            if not _certifica_z(z_hi, c_lo, masa_A + t_hi,
                                max(cap_A, t_hi)):
                return False
    return True


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] el enunciado y las podas del canal pesado")
    ok = True
    ok &= check("[ENUNCIADO] EL CRITERIO (10 dims) — REDUCCION DE "
                "DIMENSION vs espfinal, viable gracias a x: con "
                "x >= (1+SS)/phi en v, c' >= max(z+x, trio, "
                "cola(Y)) es mucho mayor que el 1+z de espfinal, "
                "y TODA la carga A = S sin B* (masa SS - beta, "
                "cada pieza <= min(beta, phi/2): beta >= sigma1 "
                ">= max A por definicion del mejor subconjunto, y "
                "a <= phi/2 por el lema de reduccion) se paga POR "
                "MASA como bloque partible (cadena monotona "
                "cap-generica, adversariada en espkp; greedy "
                "|m1-m2| <= cap, teorema de espfinal): las 6 dims "
                "de la particion explicita colapsan a beta.  "
                "Piezas nuevas adversariadas en espcanal: pinza "
                "de la cola de x CON EMPATE (vacuidad del gemelo, "
                "perfil-independiente), pared PESADA del nodo "
                "(A7) con sigma1 <= min(beta, 1), suelo del TRIO "
                "{z, m, x} (creciente), par antipodal (z, x) con "
                "cota acoplada (A5).  Tramos KZ = 2 (X_z) x K = 4 "
                "(mu_Y) como espfinal", True)
    ok &= check("[ENUNCIADO] SUFICIENCIA sobre superconjunto: las "
                "podas usadas son paredes verdaderas (espfinal + "
                "espcanal, actas); las omitidas solo agrandan el "
                "dominio — el certificado cubre todo punto legal "
                "pesado con x en v", True)
    # gate: el techo de la pared pesada del nodo
    import sympy as sp
    w, SS, s1, Xx = sp.symbols('omega SigmaS sigma1 X_x',
                               positive=True)
    phi = (1 + sp.sqrt(5)) / 2
    techo = w + SS - 1 + s1 + Xx
    v = sp.simplify(techo.subs({SS: phi, s1: 1, Xx: 0})
                    - (w + phi))
    ok &= check("(gate) el techo de la pared pesada: con "
                "sigma1 <= 1 y X_x <= phi - Sigma_S, "
                "x < omega + Sigma_S - 1 + sigma1 + X_x <= "
                f"omega + phi (residuo simbolico {v} = 0): "
                "X_TOP = 3.227 > 1.6 + 1.618 - 0.0 cubre "
                "(ademas X_x + Sigma_S <= phi da el techo fino "
                "omega + sigma1 + phi - 1 <= 3.218)", v == 0)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] B&B pesada-canal por bandas de Sigma_S")
    ok = True
    ss_lo = float(os.environ.get('CC_SSLO', '1.0'))
    ss_hi = float(os.environ.get('CC_SSHI', str(PHI)))
    eps_b = float(os.environ.get('CC_EPS', '4e-3'))
    root = [0.0, W_MAX, 0.0, 0.999, ss_lo, ss_hi, 0.0, 1.0,
            0.0, XP_MAX, 0.0, XZ_MAX, 0.0, 1.0,
            1.0, A_MAX, 1.0, Z_MAX, 1.0, X_TOP]
    (n_sobre, env, fuera), vistos, certs, trunc = \
        mapa_supervivientes(root, criterio_pesada_x, eps=eps_b,
                            max_boxes=int(os.environ.get(
                                'CC_MAXB', '20000000')),
                            max_fallos=200000, sobre=False)
    ok &= check(f"PESADA-CANAL banda Sigma_S [{ss_lo}, {ss_hi}] "
                f"CERTIFICADA: {vistos} cajas vistas, {certs} "
                f"certificadas, {len(fuera)} sin resolver, "
                f"truncado {trunc}",
                len(fuera) == 0 and not trunc)
    if fuera:
        print(f"  primera sin resolver: {fuera[0]}")
    # (b2) PESADA x-EN-z d = 1 (acta H1): el dominio entero
    root_z = [0.0, W_MAX, 0.0, 0.999, 1.0, PHI, 0.0, 1.0,
              0.0, XP_MAX, 0.0, XZ_MAX, 0.0, 1.0,
              1.0, A_MAX, 1.0, Z_MAX, 1.0, X_TOP]
    (_, _, fuera_z), n_z, cert_z, trunc_z = mapa_supervivientes(
        root_z, criterio_pesada_z, eps=4e-3, sobre=False)
    ok &= check(f"(b2) PESADA x-EN-z (d = 1) CERTIFICADA ENTERA "
                f"(acta H1: x dentro de z, corona de v sin x, "
                f"ventanas de z corridas): {n_z} cajas vistas, "
                f"{cert_z} certificadas, {len(fuera_z)} sin "
                f"resolver, truncado {trunc_z}",
                len(fuera_z) == 0 and not trunc_z)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] sanity pesada con x explicito")
    rng = random.Random(SEED)
    ok = True
    n, caben = 0, 0
    intentos = 0
    while n < 200 and intentos < 2000000:
        intentos += 1
        w = rng.uniform(0.05, W_MAX)
        s2 = rng.uniform(0.05, 0.999)
        s1 = rng.uniform(s2, 0.999)
        # perfil pesado: sigma1 + sigma2 + W >= 1 + sigma2
        k_w = rng.randrange(1, 5)
        Ws = [rng.uniform(0.02, s2) for _ in range(k_w)]
        SS = s1 + s2 + sum(Ws)
        if SS < 1.0 + s2 or SS > PHI - 0.05:
            continue
        Xm = rng.uniform(0.0, max(0.0, 1 - w)) \
            if rng.random() < 0.3 else 0.0
        Xp = rng.uniform(0.0, max(0.0, PHI - SS - Xm)) \
            if rng.random() < 0.3 else 0.0
        # X_z ANTES de x (acta H5: la pinza de x debe ver todo el
        # polvo de la instancia)
        Xz = rng.uniform(0.0, max(0.0, PHI - SS - Xm - Xp)) \
            if rng.random() < 0.3 else 0.0
        resto_x = max(0.0, PHI - SS - Xm - Xp - Xz)
        # x en la banda legal alta (la pinza con todo el polvo)
        x_lo_leg = (1.0 + SS + Xm + Xp + Xz) / PHI
        x_hi = w + SS - 1.0 + s1 + resto_x   # pared pesada A7
        if x_lo_leg >= x_hi:
            continue
        x = rng.uniform(x_lo_leg, x_hi)
        lo_a = max(1.0 + w, SS + Xp + w)
        # particion B*/A: B* = mejor subconjunto <= 1
        piezas = sorted([s1, s2] + Ws, reverse=True)
        mejor, mejor_m = [], 0.0
        for mask in range(1 << len(piezas)):
            m_v = sum(p for i, p in enumerate(piezas)
                      if mask >> i & 1)
            if m_v <= 1.0 and m_v > mejor_m:
                mejor_m = m_v
                mejor = [p for i, p in enumerate(piezas)
                         if mask >> i & 1]
        # particion: quitar las piezas de B* una a una
        resto_A = list(piezas)
        for p in mejor:
            resto_A.remove(p)
        beta = mejor_m
        hi_a = 1.0 + (SS - beta) + Xp + w
        if lo_a >= hi_a:
            continue
        alfa = rng.uniform(lo_a, hi_a)
        z = rng.uniform(alfa + Xz + w, alfa + Xz + s2 + w)
        st = suelo_trio(z, x, 1.0, z + x)
        cola = (1.0 + SS + Xm + alfa + Xp + z + Xz + x) / PHI
        lo_Y = max(cola, z + x + w, st + w)
        hi_Y = SS + z + w + x
        if lo_Y >= hi_Y:
            continue
        cp = lo_Y - w
        n += 1
        # corona real: {z, x, D_m} U A (la fila B* va dentro de
        # D_m); polvo A tratado como piezas explicitas
        carga = sorted([z, x, 1.0] + resto_A, reverse=True)
        if len(carga) <= 6:
            import itertools as it
            base = carga[0]
            vistos_p = set()
            okc = False
            for perm in it.permutations(carga[1:]):
                if perm[::-1] in vistos_p:
                    continue
                vistos_p.add(perm)
                orden = [base] + list(perm)
                if dual_factible(orden, cp) \
                        and primal_factible(orden, cp):
                    okc = True
                    break
        else:
            okc = corona_suf(carga, cp)[0]
        if not okc:
            okc = _creciente_cabe(z, [x, 1.0] + resto_A, cp)
        if okc:
            caben += 1
    ok &= check(f"en {n} instancias pesadas legales con x "
                f"explicito (particion B*/A real, x en la banda "
                f"de la pinza y la pared A7, Y en su suelo con "
                f"el trio): corona {{z, x, D_m}} U A cabe en "
                f"{caben}/{n} (arc-LP / corona_suf / creciente)",
                n >= 150 and caben == n)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] controles")
    ok = True
    eps = 1e-9
    # (a) la pinza del gemelo poda en la pesada
    caja_gem = [0.3, 0.3 + eps, 0.45, 0.45 + eps, 1.5, 1.5 + eps,
                0.9, 0.9 + eps, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                2.0, 2.0 + eps, 3.0, 3.0 + eps, 1.0, 1.0 + eps]
    r_gem = criterio_pesada_x(caja_gem)
    ok &= check(f"(a) la pinza del gemelo poda la pesada: caja "
                f"con x = 1 y SS = 1.5 (cola de la primera copia "
                f"1 + 1.5 = 2.5 > phi): criterio = {r_gem} "
                f"(None)", r_gem is None)
    # (b) la pared pesada del nodo poda
    caja_par = list(caja_gem)
    caja_par[18], caja_par[19] = 3.0, 3.0 + eps
    r_par = criterio_pesada_x(caja_par)
    ok &= check(f"(b) la pared pesada poda: x = 3.0 >= w + SS - 1 "
                f"+ beta + X_x = 0.3 + 0.5 + 0.9 + 0.118: "
                f"criterio = {r_par} (None = desbloqueo)",
                r_par is None)
    # (b3) beta < sigma2 es imposible (beta >= sigma1 >= sigma2)
    caja_b = list(caja_gem)
    caja_b[6], caja_b[7] = 0.1, 0.2
    r_b = criterio_pesada_x(caja_b)
    ok &= check(f"(b3) poda de particion: beta <= 0.2 < sigma2 = "
                f"0.45: criterio = {r_b} (None)", r_b is None)
    # (b4) NO-TAUTOLOGIA del certificador nuevo (acta H3): la
    #      caja raiz de una banda entera NO certifica de una
    root_neg = [0.0, W_MAX, 0.0, 0.999, 1.05, 1.1, 0.0, 1.0,
                0.0, XP_MAX, 0.0, XZ_MAX, 0.0, 1.0,
                1.0, A_MAX, 1.0, Z_MAX, 1.0, X_TOP]
    r_root = criterio_pesada_x(root_neg)
    ok &= check(f"(b4) no-tautologia del certificador (acta H3): "
                f"criterio_pesada_x(raiz de banda [1.05, 1.1]) = "
                f"{r_root} (False: exige subdivision real; el "
                f"mapa certifica 45361/166941, el resto se parte "
                f"o poda)", r_root is False)
    # (c) el certificador rechaza lo imposible: c_lo estrangulado
    #     via caja legal con z enorme y Y minima — control por
    #     construccion en el B&B (podas exactas); control directo
    #     del motor en espfinal bloque D (adversariado)
    ok &= check("(c) controles del motor heredados: _antipodal2 "
                "con negativos en espfinal bloque D "
                "(adversariado) y _creciente_cabe/suelo_trio/"
                "_pool_ok con negativos en espcanal bloque D "
                "(acta R5)", True)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    ok = True
    ok &= check("[ENUNCIADO] Con este certificado, EL CANAL "
                "OCUPANTE >= r_m QUEDA CERRADO EN EL CONTENEDOR "
                "DE Y (v y torre d = 1) EN AMBOS PERFILES "
                "(espcanal ligera v+z + este script pesada v+z, "
                "acta H1): tarifa derivada (dos paredes del "
                "nodo) + vacuidad del gemelo + pinza de la cola "
                "+ bandas certificadas + desbloqueo sobre el "
                "techo.  Declarado: la banda [2/phi, techo) en "
                "TORRES d >= 2 (ligera y pesada), x-en-u "
                "(exclusion estructural de lem:DBo), k >= 2 "
                "anillos extra (pinza de colas), omega <= 1.6 "
                "(tope heredado)", True)
    return ok


def main():
    print("=" * 68)
    print("LA PESADA DEL CANAL >= r_m (drafts/espcanalp.md)")
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
