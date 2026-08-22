#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LA TORRE PROFUNDA PESADA (la continuacion declarada de
esptorre): la banda media del canal ocupante a profundidad d >= 2
en el PERFIL PESADO (Sigma_S > 1 con la particion beta/A de
espcanalp), cerrada con la misma cirugia de torre sobre
criterio_pesada_z.

LA CELDA: x >= r_m anidado a profundidad d >= 2 en la torre de z,
perfil pesado (la corona de v es {z, D_m} + bloques por masa de la
particion beta/A; x y la torre viajan dentro de z).  espcanalp
cerro d = 1 (criterio_pesada_z, dominio entero); esptorre cerro el
perfil LIGERO a d >= 2 y declaro esta extension.

LA CIRUGIA (identica a esptorre, sobre la estructura pesada):
  (i)  la torre como MASA M_t >= x + omega SOLO en suelos
       favorables (cola de z, convivencia via t_1 >= x + omega,
       cola de Y en la pinza RY — el RHS de la pinza es el techo
       de la ventana de Y por children y NO cambia: la torre son
       descendientes de z);
  (ii) el TECHO de la ventana de z RETIRADO (a d >= 2 no es
       derivable: los children de t_1 no son polvo — la leccion
       de esptorre): z in [1, Z1] por B&B + la COLA z >= Z1 por
       caps de limite (th(z, pieza, c) <= 2 asin(sqrt pieza) via
       c >= 1 + z; las piezas de la corona pesada son D_m = 1 y
       bloques cap <= min(beta, phi/2) <= 1);
  (iii) la pared PESADA del nodo sobre x (x < omega + SS - 1 +
       beta + X_x, posicion-independiente, acta A7 de espcanalp)
       y la pinza de la cola de x, ambas sobre el x del FONDO
       (sus children si son polvo).

MODEL-CONDITIONAL como toda la celda.  Criterio de CAJAS (ventanas
con >= estricto): las sondas dan anchura +epsilon.

Bloques: [A] enunciado de la cirugia; [B] B&B (z finito) + cola z;
[C] contraste en-celda (generador con todas las pinzas respetadas,
None sobre punto legal = violacion); [D] negativos; [E] estatus.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check
from r2bmulti import th
from espfinal import _antipodal2
from espcanal import mapa_supervivientes
from puertocii import b_star_particion

SEED = int(os.environ.get('CC_SEED', '20260822'))
XCAP = PHI - 1.0
W_MAX, XP_MAX, XZ_MAX = 1.6, 1.5, 1.0
A_MAX = 1.0 + 0.999 + XP_MAX + W_MAX
X_TOP = 0.999 + W_MAX + XCAP + 0.01
Z1 = 40.0


def _asin2(z):
    return 2.0 * math.asin(max(0.0, min(1.0, z)))


def criterio_torre_p(box):
    """Caja (w, s2, SS, beta, Xp, Xz, Xm, a, z, x) — como
    espcanalp.criterio_pesada_z con la cirugia de torre: masa
    M >= x + omega en suelos, convivencia con t_1, techo de z
    retirado; zh = None significa la cola z >= Z1."""
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
        return None                    # pared pesada del nodo (x
    a_lo = max(al_, 1.0 + wl, SSl + Xpl + wl)   # del fondo)
    a_hi = min(ah_, 1.0 + (SSh - bl) + Xph + wh)
    if a_lo >= a_hi:
        return None
    masa_A = max(0.0, SSh - bl)
    cap_A = min(bh, PHI / 2, masa_A) if masa_A > 0 else 0.0
    # LA MASA DE TORRE en su suelo
    M_lo = xl + wl

    def _certifica_z(z_hi_t, c_lo, masa, cap):
        """Corona {z, D_m} + bloque(s); z_hi_t = None -> cola z
        (caps de limite en la fila 0)."""
        variantes = [[masa], [masa / 2 + cap / 2,
                              masa / 2 + cap / 2]] \
            if masa > 0 else [[]]
        for bloques in variantes:
            nodos = [z_hi_t if z_hi_t is not None else 1e9,
                     1.0] + [cap] * len(bloques)
            if c_lo <= max(nodos[1:] + [1.0]) + 1e-12:
                continue
            n = len(nodos)
            thmat = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if i == 0:
                        if z_hi_t is None:
                            thmat[i][j] = _asin2(math.sqrt(
                                min(1.0, nodos[j])))
                        else:
                            t_ac = th(z_hi_t, nodos[j],
                                      1.0 + z_hi_t)
                            t_gl = th(z_hi_t, nodos[j], c_lo) \
                                if c_lo > z_hi_t + 1e-12 else PI
                            thmat[i][j] = min(t_ac, t_gl)
                    else:
                        thmat[i][j] = th(nodos[i], nodos[j],
                                         c_lo)
            Ds = {2 + k: PI * b / (c_lo - cap)
                  for k, b in enumerate(bloques)}
            if _antipodal2(nodos, thmat, Ds):
                return True
        return False

    KZ, K = 2, 4
    for k_z in range(KZ):
        x_lo_z = Xzl + (XCAP - Xzl) * k_z / KZ
        # ventanas de z con la TORRE: convivencia con t_1 >=
        # x + omega; cola de z con la masa M; SIN techo
        cola_z = (1.0 + SSl + Xml + a_lo + Xpl + x_lo_z
                  + xl + M_lo) / PHI
        z_lo = max(zl, a_lo + x_lo_z + (xl + wl) + wl, cola_z)
        if zh is not None and z_lo >= zh:
            continue
        z_hi = zh                      # None en la cola
        mu_y_max = max(0.0, PHI - max(SSl, 1.0) - Xml - Xpl
                       - x_lo_z)
        for k_seg in range(K):
            t_lo = mu_y_max * k_seg / K
            t_hi = mu_y_max * (k_seg + 1) / K
            cola_seg = (1.0 + SSl + Xml + a_lo + Xpl + z_lo
                        + x_lo_z + t_lo + xl + M_lo) / PHI
            if zh is not None and \
                    cola_seg >= SSh + z_hi + t_hi + wh:
                continue               # pinza RY (techo por
            c_lo = max(1.0 + z_lo,     # children, sin torre)
                       cola_seg - wh)
            masa = masa_A + t_hi
            cap = max(cap_A, t_hi)
            if not _certifica_z(z_hi, c_lo, masa, cap):
                return False
    return True


def crit_finito(box):
    return criterio_torre_p(list(box))


def crit_cola(box18):
    """La cola z >= Z1: caja de 9 dims (sin z)."""
    b = list(box18[:16]) + [Z1, None] + list(box18[16:])
    return criterio_torre_p(b)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] la cirugia de torre sobre la pesada")
    ok = True
    ok &= check("[ENUNCIADO] (A1) la celda: x >= r_m a "
                "profundidad d >= 2 en la torre de z, perfil "
                "PESADO (particion beta/A de espcanalp; corona "
                "de v = {z, D_m} + bloques por masa).  La pared "
                "PESADA del nodo y la pinza de la cola actuan "
                "sobre el x del FONDO (children de x = polvo: "
                "posicion-independientes, actas A7/R3)", True)
    ok &= check("[ENUNCIADO] (A2) la cirugia identica a esptorre "
                "(alli adversariada): masa M >= x + omega en "
                "suelos favorables (las tres apariciones: cola "
                "de z, convivencia via t_1, cola de Y — el RHS "
                "de la pinza RY es el techo por children y no "
                "cambia con la torre), techo de la ventana de z "
                "RETIRADO (no derivable a d >= 2), cola z por "
                "caps de limite (gates B1/B2 de esptorre: "
                "(base+M)/phi crece en M; zp/(1+z-p) crece en z "
                "hacia p para p <= 1; c >= 1 + z por el par "
                "{z, D_m})", True)
    ok &= check("[ENUNCIADO] (A3) las piezas de la corona pesada "
                "en la cola z son D_m = 1 y bloques con cap = "
                "max(min(beta, phi/2, masa_A), t_hi) <= 1: los "
                "caps "
                "2 asin(sqrt pieza) aplican a todas", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] B&B de la pesada profunda (z finito + cola z)")
    ok = True
    root = [0.0, W_MAX, 0.0, 0.999, 1.0, PHI, 0.0, 1.0,
            0.0, XP_MAX, 0.0, XZ_MAX, 0.0, 1.0,
            1.0, A_MAX, 1.0, Z1, 1.0, X_TOP]
    (n_s, env, fuera), vistos, certs, trunc = \
        mapa_supervivientes(root, crit_finito, eps=4e-3,
                            max_boxes=int(os.environ.get(
                                'CC_MAXB', '20000000')),
                            max_fallos=100000, sobre=False)
    ok &= check(f"(a) z finito [1, {Z1}]: {vistos} cajas, "
                f"{certs} certificadas, {len(fuera)} sin "
                f"resolver, truncado {trunc}",
                len(fuera) == 0 and not trunc)
    if fuera:
        print(f"  primera: {fuera[0]}")
    root2 = [0.0, W_MAX, 0.0, 0.999, 1.0, PHI, 0.0, 1.0,
             0.0, XP_MAX, 0.0, XZ_MAX, 0.0, 1.0,
             1.0, A_MAX, 1.0, X_TOP]
    (n2, e2, fuera2), v2, c2, tr2 = \
        mapa_supervivientes(root2, crit_cola, eps=4e-3,
                            max_boxes=5000000,
                            max_fallos=100000, sobre=False)
    ok &= check(f"(b) LA COLA z >= {Z1} (caps, sin techo): {v2} "
                f"cajas, {c2} certificadas, {len(fuera2)} sin "
                f"resolver, truncado {tr2}",
                len(fuera2) == 0 and not tr2)
    if fuera2:
        print(f"  primera: {fuera2[0]}")
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] contraste en-celda")
    rng = random.Random(SEED)
    ok = True
    n_p, viol, n_cola = 0, 0, 0
    for _ in range(80000):
        if n_p >= 300:
            break
        d = rng.choice([2, 3, 4])
        w = rng.uniform(0.05, W_MAX)
        # S REAL (acta H1): multiconjunto con la particion beta/A
        # realizable via b_star_particion, como espcanalp C
        p_n = rng.randrange(3, 8)
        piezas = sorted((rng.uniform(0.05, 0.9)
                         for _ in range(p_n)), reverse=True)
        SS = sum(piezas)
        s2 = piezas[1]
        if not (1.0 + s2 <= SS <= PHI):
            continue
        beta, _A = b_star_particion(piezas)
        SS = beta + sum(_A)            # coherencia float
        if beta <= 0.51:
            continue
        # X's NO nulas (acta H2)
        resto_p = max(0.0, PHI - SS - 0.02)
        Xp = rng.uniform(0.0, resto_p / 3)
        Xz = rng.uniform(0.0, resto_p / 3)
        Xm = min(rng.uniform(0.0, resto_p / 3),
                 max(0.0, 1.0 - w) * 0.9)
        pinza_x = (1.0 + SS + Xm + Xp + Xz) / PHI
        tech = w + SS - 1.0 + min(beta, 1.0) + \
            max(0.0, PHI - SS - Xm - Xp - Xz)
        if tech <= max(2.0 / PHI, pinza_x) + 1e-6:
            continue
        x = rng.uniform(max(2.0 / PHI, pinza_x), tech - 1e-9)
        ts = []
        cur = x
        for _ in range(d - 1):
            cur = cur + w + rng.uniform(0.0, 0.2)
            ts.append(cur)
        t1 = ts[-1]
        Mt = sum(ts)
        # ventana de alpha pesada: a_hi = 1 + (SS - beta) + w
        # (bl = max(beta, 1 - beta) = beta con beta > 1/2), luego
        # la holgura sobre SS + w es < 1 - beta
        gap_a = 1.0 - beta
        if gap_a <= 0.015:
            continue
        alfa = max(1.0 + w, SS + Xp + w) \
            + rng.uniform(0.0, 0.9 * (gap_a - 0.012))
        if alfa + 0.011 >= 1.0 + (SS - beta) + Xp + w:
            continue
        cola_z = (1.0 + SS + Xm + alfa + Xp + Xz + x + Mt) / PHI
        z_suelo = max(alfa + Xz + t1 + w, cola_z)
        z_umb = z_suelo
        for _ in range(80):
            cola_y = (1.0 + SS + Xm + alfa + Xp + z_umb + Xz
                      + x + Mt) / PHI
            if cola_y < SS + z_umb + w:
                break
            z_umb += 0.25
        if rng.random() < 0.33:
            zv = Z1 + rng.uniform(0.0, 50.0)
        else:
            zv = z_umb + rng.uniform(0.0, 2.0)
        n_p += 1
        if zv >= Z1:
            n_cola += 1
            b2 = [w, w, s2, s2, SS, SS, beta, beta,
                  Xp, Xp, Xz, Xz, Xm, Xm,
                  alfa, alfa + 0.01, x, x]
            r = crit_cola(b2)
        else:
            bx = [w, w, s2, s2, SS, SS, beta, beta,
                  Xp, Xp, Xz, Xz, Xm, Xm,
                  alfa, alfa + 0.01,
                  min(zv, Z1 - 0.02), min(zv, Z1 - 0.02) + 0.01,
                  x, x]
            r = criterio_torre_p(bx)
        if r is not True:
            viol += 1
    ok &= check(f"(a) {n_p} torres pesadas EN-CELDA (d = 2..4, "
                f"perfil pesado SS >= 1 + s2, alpha en ventana, "
                f"x sobre su pinza, z sobre el umbral RY; "
                f"{n_cola} en la cola): None o False sobre punto "
                f"legal = violacion ({viol})",
                n_p >= 150 and viol == 0)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] negativos")
    ok = True
    # la corona pesada imposible: bloque de masa grande con c
    # pequeno es rechazada por el motor
    from espfinal import _antipodal2 as ap2
    nodos = [2.0, 1.0, 0.9, 0.9]
    c_malo = 3.05
    thmat = [[0.0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(i + 1, 4):
            thmat[i][j] = th(nodos[i], nodos[j], c_malo)
    Ds = {2: PI * 0.9 / (c_malo - 0.9), 3: PI * 0.9 / (c_malo - 0.9)}
    r = ap2(nodos, thmat, Ds)
    ok &= check(f"(a) no-vacuidad: corona {{2, 1}} + dos bloques "
                f"0.9 en c = 3.05: el motor la RECHAZA ({r})",
                r is False)
    # pared pesada: x enorme = vacuo
    bx = [0.5, 0.5, 0.3, 0.3, 1.35, 1.35, 0.9, 0.9,
          0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.9, 1.91,
          5.0, 5.01, 3.3, 3.3]
    r2 = criterio_torre_p(bx)
    ok &= check(f"(b) x = 3.3 sobre la pared pesada del nodo: "
                f"vacuo ({r2})", r2 is None)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    return check(
        "[ENUNCIADO] LA TORRE PROFUNDA PESADA CERRADA (dentro "
        "del convenio): con esptorre (ligera) y esto, la banda "
        "media del canal a d >= 2 queda cerrada EN AMBOS "
        "PERFILES para torres-cadena.  El residuo (iii) se "
        "encoge a: el convenio mismo, las torres con RAMAS "
        "(k >= 2 no-anidados, declarado) y la exclusion "
        "estructural de u.  Tope omega <= 1.6 heredado en ambas "
        "celdas del canal (declarado)", True)


def main():
    print("=" * 68)
    print("LA TORRE PROFUNDA PESADA (residuo (iii), ambos "
          "perfiles)")
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
