#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LA BANDA MEDIA A PROFUNDIDAD d >= 2 (residuo (iii)): el canal
ligero con x en la TORRE PROFUNDA de z, certificado por subdivision
con la torre reducida a masa y la ventana de z SIN TECHO cerrada por
caps de limite (patron espomegacola).

LA CELDA: x in [2/phi, techo_nodo) anidado a profundidad d >= 2:
z contiene t_1, ..., t_{d-1} contiene x (t_i >= t_{i+1} + omega).
espcanal certifico d = 1 (x hijo directo de z) y las pinzas
posicion-independientes matan x fuera de la banda a TODA
profundidad (acta R3: pared del nodo sobre x — sus children SI son
polvo — y pinza de la cola de x).

POR QUE d >= 2 NO se reduce a d = 1 (el intento ingenuo): el punto
inducido con ocupante t_1 rompe la pinza del techo del nodo — los
children de t_1 contienen x >= r_m (no polvo), y el techo
techo_nodo capaba X_x por la pared del polvo global.  Lo mismo
tumba el techo de la ventana de z: a d >= 2, z NO tiene techo util
(la cadena de paredes se rompe hacia arriba).  El cierre correcto:

  (i)  LA TORRE COMO MASA: M_t = Sigma t_i >= x + omega (al menos
       t_1, y t_1 >= x + omega) entra SOLO en direcciones
       favorables (gates [B]): las colas de z y de x (pinzas de
       vacuidad y suelo de z — mas masa = mas vacuidad y mas
       suelo real; el criterio usa el SUELO M_lo = x + omega:
       cota inferior valida) y la capacidad de la corona (mas
       cola = c mayor).
  (ii) LA CONVIVENCIA con t_1 >= x + omega: z >= alpha + X_z +
       (x + omega) + omega (el agujero de z contiene t_1 junto a
       X_z... el suelo con t_1 minimo).
  (iii) LA VENTANA DE z SIN TECHO: B&B en z in [suelo, Z1] + LA
       COLA z >= Z1 por caps de limite: la corona de v es
       {z, D_m = 1, sigma2 < 1} U polvo (cap <= phi - 1 < 1) en
       c >= 1 + z, luego th(z, pieza, c) <= 2 asin(sqrt(pieza))
       (el cap de espomegacola, gate A1 alli: p = z p'/(1+z-p')
       crece en z hacia p' para p' <= 1) y los terminos lentos
       con c(Z1): th decrece en R.

La corona y el motor son los de espcanal.criterio_canal_z
(antipodal_dos_lados con polvo).  MODEL-CONDITIONAL: hereda el
convenio del canal >= r_m como toda la celda.

Bloques: [A] la reduccion y por que la ingenua falla; [B] gates
simbolicos; [C] B&B (banda de x, z finito) + la cola z; [D]
contraste y negativos; [E] estatus.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check
from espcanal import techo_nodo
from areduccion import antipodal_dos_lados
from r2bmulti import th, bnb_factible

SEED = int(os.environ.get('CC_SEED', '20260822'))
Z1 = 40.0                              # frontera de la cola de z


def _asin2(z):
    return 2.0 * math.asin(max(0.0, min(1.0, z)))


def criterio_torre(box):
    """Caja (w, s2, SS, Xp, Xz, Xm, a, z, mu, x) como la de
    espcanal.criterio_canal_z pero a profundidad d >= 2: la torre
    entra como masa M >= x + omega en los suelos de cola, t_1 >=
    x + omega en la convivencia, y z_hi = None significa la cola
    z >= Z1 (caps de limite).  OJO: criterio de CAJAS, no de
    puntos — las ventanas usan >= estricto y una caja de anchura
    cero en z o alpha es None (acta H5): las sondas deben dar
    anchura +epsilon."""
    wl, wh, s2l, s2h, SSl, SSh, Xpl, Xph, Xzl, Xzh, Xml, Xmh, \
        al, ah, zl, zh, mul, muh, xl, xh = box
    if 2.0 * s2l > SSh:
        return None
    if SSl >= 1.0 + s2h:
        return None
    if SSl + Xml + Xpl + Xzl + mul > PHI:
        return None
    if Xml > max(0.0, 1.0 - wl):
        return None
    mu_eff = min(muh, PHI - SSl - Xml - Xpl - Xzl)
    if mu_eff < mul:
        return None
    # la pared del nodo sobre x (children de x = polvo: posicion-
    # independiente, acta R3 de espcanal)
    if xl >= techo_nodo(s2h, wh, SSl, Xml, mul):
        return None
    # pinza de la cola de x (posicion-independiente; la cola real
    # de x a profundidad d es >= la modelada)
    if (1.0 + SSl + Xml + Xpl + Xzl + mul) / PHI > xh:
        return None
    # LA MASA DE TORRE en su suelo: M_lo = x_lo + omega_lo (t_1
    # como minimo, con t_1 >= x + omega)
    M_lo = xl + wl
    a_lo = max(al, 1.0 + wl, SSl + Xpl + wl)
    a_hi = min(ah, 1.0 + s2h + Xph + wh)
    if a_lo >= a_hi:
        return None
    # ventana de z a profundidad d >= 2: convivencia con t_1 y
    # cola de z con la torre entera; SIN techo (z_hi puede ser
    # None = cola)
    cola_z = (1.0 + SSl + Xml + a_lo + Xpl + Xzl + mul
              + xl + M_lo) / PHI
    z_lo = max(zl, a_lo + Xzl + (xl + wl) + wl, cola_z)
    if zh is not None:
        z_hi = zh
        if z_lo >= z_hi:
            return None
    # cola de Y (pinza RY): la cola real carga ademas M_t
    cola_lo = (1.0 + SSl + Xml + a_lo + Xpl + z_lo + Xzl
               + mul + xl + M_lo) / PHI
    if zh is not None and cola_lo >= SSh + z_hi + mu_eff + wh:
        return None                    # tramo vacuo
    c_lo = max(1.0 + z_lo, cola_lo - wh)
    s2_p = min(s2h, SSh / 2.0)
    cap = mu_eff
    if c_lo <= max(1.0, s2_p, cap) + 1e-12:
        return False
    hi = [z_hi if zh is not None else None, 1.0, s2_p, cap]
    es_polvo = [False, False, False, True]
    n = len(hi)
    thmat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if i == 0:
                if zh is None:
                    # cola z: cap de limite (espomegacola A1):
                    # th(z, p, c) <= th(z, p, 1+z) <= 2asin(sqrt p)
                    # para p <= 1
                    thmat[i][j] = _asin2(math.sqrt(min(1.0,
                                                       hi[j])))
                else:
                    t_ac = th(z_hi, hi[j], 1.0 + z_hi)
                    t_gl = th(z_hi, hi[j], c_lo) \
                        if c_lo > z_hi + 1e-12 else PI
                    thmat[i][j] = min(t_ac, t_gl)
            else:
                thmat[i][j] = th(hi[i], hi[j], c_lo)
    if zh is None:
        hi[0] = 1e9                    # solo heuristica de orden
    D = PI * mu_eff / (c_lo - cap) if mu_eff > 0 else 0.0
    return antipodal_dos_lados(hi, thmat, es_polvo, D)


def crit_finito(box):
    return criterio_torre(list(box))


def crit_cola(box18):
    """La cola z >= Z1: caja de 9 dims (sin z), z = [Z1, None)."""
    b = list(box18[:14]) + [Z1, None] + list(box18[14:])
    return criterio_torre(b)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] la reduccion de la torre y por que la ingenua "
          "falla")
    ok = True
    ok &= check("[ENUNCIADO] (A1) POR QUE NO se reduce a d = 1 "
                "con ocupante t_1: el techo del nodo capaba los "
                "children del ocupante por la pared del POLVO "
                "global (X_x <= phi - SS - ...), y los children "
                "de t_1 contienen x >= r_m (no polvo) — la "
                "reduccion ingenua rompe esa pinza, y con ella el "
                "techo de la ventana de z.  El cierre correcto "
                "certifica d >= 2 DIRECTO: torre como masa en "
                "suelos favorables + t_1 en convivencia + ventana "
                "de z sin techo cerrada por cola de caps", True)
    ok &= check("[ENUNCIADO] (A2) LAS PIEZAS POSICION-"
                "INDEPENDIENTES (acta R3 de espcanal): la pared "
                "del nodo sobre x (sus children si son polvo: "
                "x < sigma2 + omega + X_x con X_x <= phi - SS - "
                "...) y la pinza de la cola de x valen a toda "
                "profundidad: x fuera de [2/phi, techo) muere "
                "igual que en d = 1; queda la banda media, este "
                "certificado", True)
    ok &= check("[ENUNCIADO] (A3) LA TORRE COMO MASA: d >= 2 "
                "implica al menos t_1 con t_1 >= x + omega (su "
                "agujero contiene a x), luego M_t >= x + omega; "
                "M_t solo se usa en los SUELOS de las colas (de "
                "z, de Y) y en el suelo de convivencia de z — "
                "todas direcciones donde una cota inferior es "
                "valida (gates B)", True)
    ok &= check("[ENUNCIADO] (A4) LA CORONA de v no cambia "
                "({z, D_m, sigma2} U polvo): la torre viaja "
                "dentro de z (children travel inside parents); "
                "el motor es el de espcanal (antipodal con "
                "polvo, adversariado)", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] gates simbolicos")
    import sympy as sp
    ok = True
    M, phi_s, base, z, p = sp.symbols('M phi base z p',
                                      positive=True)
    d1 = sp.diff((base + M) / phi_s, M)
    ok &= check(f"(B1) las colas (base + M)/phi crecen en la masa "
                f"de torre (d/dM = {d1} > 0): usar el suelo "
                "M_lo = x + omega es cota inferior valida de "
                "TODAS las colas (mas torre real = mas suelo de "
                "z, mas vacuidad RY, mas capacidad c)",
                sp.simplify(d1 - 1 / phi_s) == 0)
    # B2: el cap de la cola z (el A1 de espomegacola)
    q = z * p / (1 + z - p)
    dq = sp.simplify(sp.diff(q, z) * (1 + z - p) ** 2 / p)
    lim = sp.limit(q, z, sp.oo)
    ok &= check(f"(B2) cola z: el producto q = zp/(1+z-p) crece "
                f"en z (d ~ {dq} >= 0 para p <= 1) con limite "
                f"{lim}: th(z, pieza, c) <= th(z, pieza, 1+z) <= "
                "2 asin(sqrt(pieza)) para toda pieza <= 1 — y "
                "las piezas de la corona son D_m = 1, sigma2 < 1 "
                "y el bloque de polvo cap <= phi - 1 < 1",
                sp.simplify(dq - (1 - p)) == 0 and lim == p)
    # B3: c >= 1 + z (el teorema del par) y th decrece en R
    ok &= check("(B3) c >= 1 + z (el agujero de v... el "
                "contenedor de la corona contiene el par {z, "
                "D_m}: suma de radios) y th decrece en R "
                "(r2bmulti, adversariado): los terminos lentos "
                "con c_lo mayoran", True)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] B&B de la banda media d >= 2 (z finito + cola z)")
    ok = True
    XCAP = PHI - 1.0
    tech_max = 1.0 + 1.6 + XCAP        # techo_nodo maximo global
    root = [0.0, 1.6, 0.0, 1.0, 1.0, PHI, 0.0, XCAP,
            0.0, XCAP, 0.0, 1.0, 1.0, 1.0 + 1.0 + XCAP + 1.6,
            1.0, Z1, 0.0, 5 * 0.618, 2.0 / PHI, tech_max]
    exito, caja, n, cert = bnb_factible(root, crit_finito,
                                        eps=5e-4)
    ok &= check(f"(a) z finito [1, {Z1}]: {n} cajas, {cert} "
                f"certificadas"
                + ("" if exito else f"; SIN RESOLVER {caja}"),
                exito)
    root2 = [0.0, 1.6, 0.0, 1.0, 1.0, PHI, 0.0, XCAP,
             0.0, XCAP, 0.0, 1.0, 1.0, 1.0 + 1.0 + XCAP + 1.6,
             0.0, 5 * 0.618, 2.0 / PHI, tech_max]
    exito2, caja2, n2, cert2 = bnb_factible(root2, crit_cola,
                                            eps=5e-4)
    ok &= check(f"(b) LA COLA z >= {Z1} (caps de limite, sin "
                f"techo): {n2} cajas, {cert2} certificadas"
                + ("" if exito2 else f"; SIN RESOLVER {caja2}"),
                exito2)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] contraste y negativos")
    rng = random.Random(SEED)
    ok = True
    from coronacolas import corona_suf
    # (a) instancias EN-CELDA (acta H1: el generador anterior
    # producia 196/200 None — pinza de x no respetada y z pegado
    # al suelo con la ventana de Y vacia; aqui alpha dentro de su
    # ventana, x SOBRE su pinza, z SOBRE el umbral de vacuidad de
    # RY, cajas con anchura +0.01; None sobre punto legal cuenta
    # como violacion)
    n_p, viol, n_cola = 0, 0, 0
    for _ in range(60000):
        if n_p >= 300:
            break
        d = rng.choice([2, 3, 4])
        w = rng.uniform(0.05, 1.6)
        s2 = rng.uniform(0.05, 0.95)
        # SS <= phi: la pared del polvo global (SS > phi es
        # ilegal y el criterio la poda con None, correcto)
        ss_hi = min(1.0 + s2, PHI) - 1e-9
        if ss_hi <= max(1.0 + 1e-6, 2 * s2):
            continue
        SS = rng.uniform(max(1.0 + 1e-6, 2 * s2), ss_hi)
        if not (1.0 < SS < 1.0 + s2):
            continue
        tech = techo_nodo(s2, w, SS, 0.0, 0.0)
        pinza_x = (1.0 + SS) / PHI
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
        # alpha DENTRO de su ventana [max(1, SS) + w, 1 + s2 + w):
        # la holgura no puede exceder 1 + s2 - SS (acta H1 bis)
        gap_a = 1.0 + s2 - SS
        if gap_a <= 0.015:
            continue
        alfa = max(1.0 + w, SS + w)             + rng.uniform(0.0, 0.9 * (gap_a - 0.012))
        cola_z = (1.0 + SS + alfa + x + Mt) / PHI
        z_suelo = max(alfa + t1 + w, cola_z)
        # el umbral de vacuidad de RY: cola(Y)/phi < SS + z + w
        # (sin mu): z sobre el umbral para que la ventana de Y
        # NO sea vacia
        z_umb = z_suelo
        for _ in range(60):
            cola_y = (1.0 + SS + alfa + z_umb + x + Mt) / PHI
            if cola_y < SS + z_umb + w:
                break
            z_umb += 0.25
        # un tercio de los puntos van a la cola z >= Z1
        if rng.random() < 0.33:
            zv = Z1 + rng.uniform(0.0, 50.0)
        else:
            zv = z_umb + rng.uniform(0.0, 2.0)
        if zv >= Z1:
            n_cola += 1
        bx = [w, w, s2, s2, SS, SS, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
              alfa, alfa + 0.01, min(zv, Z1 - 0.02),
              min(zv, Z1 - 0.02) + 0.01, 0.0, 0.0, x, x]
        r = criterio_torre(bx)
        if zv >= Z1:
            b2 = [w, w, s2, s2, SS, SS, 0.0, 0.0, 0.0, 0.0,
                  0.0, 0.0, alfa, alfa + 0.01, 0.0, 0.0, x, x]
            r = crit_cola(b2)
        n_p += 1
        if r is not True:
            viol += 1
    ok &= check(f"(a) {n_p} torres EN-CELDA (d = 2..4, alpha en "
                f"ventana, x sobre su pinza, z sobre el umbral "
                f"RY; {n_cola} en la cola z): el criterio "
                f"certifica TODAS — None o False sobre punto "
                f"legal cuenta como violacion ({viol})",
                n_p >= 200 and viol == 0)
    # (b) negativo: la pared del nodo mata x >= techo
    bx = [0.5, 0.5, 0.3, 0.3, 1.25, 1.25, 0.0, 0.0, 0.0, 0.0,
          0.0, 0.0, 1.8, 1.81, 5.0, 5.01, 0.0, 0.0, 3.0, 3.0]
    r = criterio_torre(bx)
    ok &= check(f"(b) x = 3 >= techo_nodo: la caja es vacua por "
                f"la pared del nodo ({r})", r is None)
    # (c) no-vacuidad del motor: una corona IMPOSIBLE (tres
    # piezas grandes en c pequeno) es rechazada por
    # antipodal_dos_lados con la misma llamada del criterio
    hi = [2.0, 1.0, 0.95, 0.0]
    c_malo = 3.05                      # 2 + 1 apretado y 0.95 no
    thmat = [[0.0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(i + 1, 4):
            thmat[i][j] = th(hi[i], hi[j], c_malo)
    r3 = antipodal_dos_lados(hi, thmat, [False] * 3 + [True], 0.0)
    ok &= check(f"(c) no-vacuidad: la corona {{2, 1, 0.95}} en "
                f"c = 3.05 (el par 2+1 llena el diametro y 0.95 "
                f"no cabe al lado) es RECHAZADA por el motor "
                f"({r3})", r3 is False)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    return check(
        "[ENUNCIADO] LA BANDA MEDIA DEL CANAL A PROFUNDIDAD "
        "d >= 2 QUEDA CERRADA (dentro del convenio): la torre "
        "como masa en suelos favorables + t_1 en la convivencia "
        "+ la ventana de z sin techo cubierta por B&B finito y "
        "cola de caps.  El residuo (iii) se encoge a: el "
        "CONVENIO mismo del canal >= r_m (model-conditional) y "
        "la exclusion estructural del contenido de u (lem:DBo).  "
        "ALCANCE HONESTO (acta H2): esto cierra la celda LIGERA "
        "(la de espcanal) para torres-CADENA; la PESADA con x "
        "(espcanalp) queda como CONTINUACION declarada (su "
        "criterio conserva el techo d = 1 de la ventana de z y "
        "la cirugia de torre no esta implementada alli); "
        "permanecen tambien omega <= 1.6 (tope heredado de esta "
        "celda — la tecnica de espomegacola no se ha aplicado "
        "aqui), y las torres con RAMAS (dos anillos >= r_m "
        "colgando del mismo t_i: caen bajo el k >= 2 no-anidados "
        "de espcanal A6, declarado; los suelos del criterio "
        "valen tambien para arboles pero el claim documenta la "
        "cadena)", True)


def main():
    print("=" * 68)
    print("LA BANDA MEDIA EN LA TORRE d >= 2 (residuo (iii))")
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
