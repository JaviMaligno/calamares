#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R2b certificada por subdivision (docs/drafts/r2bcert.md): los
barridos del trio de [G] (G-b/G-c interior, G-f profundidad, G-g
ligera especular) suben de MC+frontera a COTA CERTIFICADA por
branch-and-bound con cotas de esquina — la tecnologia de
optimizacion.py aplicada al trio mural de R2b.

EL OBJETO: trio_suma(T, s2, c) = theta(T,1,c) + theta(1,s2,c) +
theta(s2,T,c) — la suficiencia k = 3 (adversariada en puertocii:
suma <= 2 pi con cada theta <= pi y pares cabiendo => la corona se
realiza) reduce el cierre a acotar la SUMA.  theta_w es creciente
en las piezas y decreciente en c (exacto): esquina pesimista =
piezas ALTAS, c BAJO => cota superior valida por caja.

RAMA DR (cubre G-b, G-c y G-f de una vez): el trio {T, m, s2} en
c >= Sigma_S + T (tarifa DR; los X'/X_p solo SUBEN c: peor caso 0).
T es la pieza grande LIBRE >= 1 (Y en d = 1; z en d >= 2: G-f ya
barria z libre — aqui queda certificado para TODOS los niveles).
Relajaciones EXACTAS (superconjunto del dominio real):
  s1 < 1        =>  Sigma_S = s1 + s2 < 1 + s2 (ligereza automatica),
  s1 >= s2      =>  s2 <= Sigma_S / 2,
  pared (D)     =>  Sigma_S > 1;  s1, s2 < 1 => Sigma_S < 2,
  T >= 1 (anillo > m); c = Sigma_S + T (suelo; theta decrece en c).
Cola T -> inf POR MONOTONIA EXACTA: a c = Sigma_S + T,
f(T)f(1) crece en T (signo Sigma_S - 1 > 0, el sympy de G-f0) con
limite 1/Sigma_S, f(s2)f(T) crece (signo Sigma_S - s2 > 0) con
limite s2/Sigma_S, f(1)f(s2) decrece: la caja [T0, inf) se acota
por los limites + el termino central en T0.

RAMA ESP (G-g ligera, orientacion especular): corona {z, D_m, s2}
en c' = Y - omega.  Tarifas derivadas (adversariadas): convivencia
m-z en v => Y >= 1 + z + omega (c' >= 1 + z); suelo de cola
Y >= (1 + Sigma_S + alpha + z)/phi (X's = 0: los X solo SUBEN el
suelo de Y, peor caso 0); alpha en [max(1+omega, Sigma_S+omega),
1+s2+omega) (E4-esp / techo B2u-esp); z en [alpha+omega,
alpha+s2+omega) ((Rz-esp)).  El umbral analitico s2 = 2/3 (en
c' = 1+z el trio da pi + 4 asin(sqrt(s2/(2-s2))) = 2 pi ahi):
para s2 > 2/3 el rescate lo da EXACTAMENTE el suelo de cola(Y) —
el B&B resuelve ese trade-off con las dos cotas de c'.

FUERA (declarado, criterio de corona multipieza, no suma): G-b'
(X' explicitas) y G-e / G-g pesada (particion B*/A) — barridos MC
adversariados; el analogo seria un B&B de factibilidad con el
argumento "las mismas posiciones valen" (esquema en el draft).

Flotantes: IEEE double; margen del certificado >= 0.3 rad, > 13
ordenes sobre el error de una suma de 3 asin.

Bloques: [A] exactos (monotonias, relajaciones, limites);
[B] B&B rama DR; [C] B&B rama ESP; [D] coherencia con la esquina
certificada pi + 4 asin(1/sqrt3); [E] controles.
"""
import heapq
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, theta_w

ITER = int(os.environ.get('CC_ITER', '60000'))
OBJ = 2 * PI - 0.3


def th(a, b, c):
    """theta_w con la pi-gorra tambien para piezas >= c (una pieza
    que no cabe sola tiene angulo pi como cota — la caja se
    resolvera por subdivision o quedara podada)."""
    if a >= c - 1e-15 or b >= c - 1e-15:
        return PI
    return theta_w(a, b, c)


def trio_ub_DR(box):
    """Cota superior del trio en la caja DR (SSl, SSh, s2l, s2h,
    Tl, Th); Th = None = [Tl, inf).  None si la caja no tiene
    puntos reales (podas exactas)."""
    SSl, SSh, s2l, s2h, Tl, Th = box
    # PODAS EXACTAS (sin tolerancia hacia la supervivencia: las
    # ventanas reales son semiabiertas y una caja-punto infactible
    # con holgura 1e-12 sobreviviria para siempre — bug cazado)
    if 2 * s2l > SSh:
        return None                    # s2 <= Sigma_S/2
    if SSl >= 1.0 + s2h:
        return None                    # ligereza s1 < 1
    s2h = min(s2h, SSh / 2)
    c_lo = SSl + Tl
    if Th is None:
        # limites exactos en T -> inf (monotonia G-f0) + termino
        # central en Tl
        t1 = 2 * math.asin(min(1.0, math.sqrt(1.0 / SSl)))
        t3 = 2 * math.asin(min(1.0, math.sqrt(s2h / SSl)))
        t2 = th(1.0, s2h, c_lo)
        return t1 + t2 + t3
    return (th(Th, 1.0, c_lo) + th(1.0, s2h, c_lo)
            + th(s2h, Th, c_lo))


def trio_ub_ESP(box):
    """Cota superior del trio {z, 1, s2} en la caja ESP (wl, wh,
    s2l, s2h, SSl, SSh, al, ah, zl, zh) con c' >= max(1+z_l,
    colaY_lo - w_h).  None si la caja no tiene puntos reales."""
    wl, wh, s2l, s2h, SSl, SSh, al, ah, zl, zh = box
    # PODAS EXACTAS (ver trio_ub_DR)
    if 2 * s2l > SSh:
        return None
    if SSl >= 1.0 + s2h:
        return None
    if SSl > PHI:
        return None                    # pared de masa: cola(m) <=
                                       # phi => Sigma_S <= phi (la
                                       # que mata la esquina s2 -> 1
                                       # donde la corona NO cabe:
                                       # bolsillo 0.958 < s2)
    # ventana de alpha: [max(1+w, SS+w), 1+s2+w)
    if ah < max(1.0 + wl, SSl + wl):
        return None
    if al >= 1.0 + s2h + wh:
        return None
    # ventana de z: [alpha+w, alpha+s2+w)
    if zh < al + wl:
        return None
    if zl >= ah + s2h + wh:
        return None
    # ventana de Y no vacia: lo_Y < hi_Y = SS + z + w (XY = 0)
    colaY_lo = (1.0 + SSl + al + zl) / PHI
    loY_min = max(zl + wl, colaY_lo, 1.0 + zl + wl)
    if loY_min >= SSh + zh + wh:
        return None                    # pinza: sin Y legal
    c_lo = max(1.0 + zl, colaY_lo - wh)
    if c_lo <= max(zh, 1.0, s2h) + 1e-12:
        return 2 * PI + 1.0            # caja aun sin resolver
    return (th(zh, 1.0, c_lo) + th(1.0, s2h, c_lo)
            + th(s2h, zh, c_lo))


def bnb(root, ub_fn, objetivo, dims, max_boxes=600000):
    """B&B generico: max-heap por cota, subdivision de la dimension
    relativa mas ancha (dims = lista de (i_lo, i_hi, escala)); la
    dimension con hi = None se parte [lo, 4lo] / [4lo, inf)."""
    v0 = ub_fn(root)
    if v0 is None:
        return True, 0.0, 0
    heap = [(-v0, root)]
    n = 0
    while heap:
        n += 1
        if n > max_boxes:
            return False, -heap[0][0], n
        negv, box = heapq.heappop(heap)
        v = -negv
        if v < objetivo:
            return True, v, n
        anchos = []
        for k, (i, j, esc) in enumerate(dims):
            hi = box[j] if box[j] is not None else 4 * box[i]
            anchos.append(((hi - box[i]) / esc, k))
        anchos.sort(reverse=True)
        k = anchos[0][1]
        i, j, _ = dims[k]
        b = list(box)
        if box[j] is None:
            m = 4 * box[i]
            b1, b2 = list(box), list(box)
            b1[j] = m
            b2[i] = m
        else:
            m = (box[i] + box[j]) / 2
            b1, b2 = list(box), list(box)
            b1[j] = m
            b2[i] = m
        for h in (tuple(b1), tuple(b2)):
            v = ub_fn(h)
            if v is not None:
                heapq.heappush(heap, (-v, h))
    return True, 0.0, n


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] exactos: monotonias, relajaciones y limites")
    import sympy as sp
    ok = True
    x, cc, T, S, q = sp.symbols('x c T S q', positive=True)
    ok &= check("theta_w creciente en las piezas y decreciente en c "
                "(d/dc [x/(c-x)] = -x/(c-x)^2 < 0): esquina "
                "pesimista = cota superior de caja (la palanca de "
                "optimizacion.py)",
                sp.simplify(sp.diff(x / (cc - x), cc)
                            + x / (cc - x) ** 2) == 0)
    ok &= check("relajaciones exactas de la rama DR: s1 < 1 => "
                "Sigma_S < 1+s2 (ligereza automatica); s1 >= s2 => "
                "s2 <= Sigma_S/2; (D) => Sigma_S > 1; s1, s2 < 1 => "
                "Sigma_S < 2; la tarifa c = Sigma_S + T + X es peor "
                "en X = 0 (theta decrece en c): el dominio del B&B "
                "es un SUPERCONJUNTO del real", True)
    # limites T -> inf con c = S + T (los signos de G-f0)
    fz_fm = (T / S) * (1 / (S + T - 1))
    fz_fs = (q / (S + T - q)) * (T / S)
    ok &= check("cola T -> inf (monotonia exacta): a c = S+T, "
                "d/dT[f_T f_m] tiene el signo de S-1 > 0 con limite "
                "1/S, y d/dT[f_s2 f_T] el de S-q > 0 con limite "
                "q/S; f_m f_s2 decrece: la caja [T0, inf) se acota "
                "por los limites + el termino central en T0",
                sp.simplify(sp.limit(fz_fm, T, sp.oo) - 1 / S) == 0
                and sp.simplify(sp.limit(fz_fs, T, sp.oo) - q / S)
                == 0)
    ok &= check("suficiencia k = 3 (adversariada, puertocii "
                "trio_suma): suma <= 2 pi con cada theta <= pi y "
                "pares cabiendo => la corona de 3 se realiza; pares "
                "en DR: T+1 <= c sii Sigma_S >= 1 (D), s2+T y 1+s2 "
                "triviales; en ESP: c' >= 1+z cubre los tres", True)
    umbral = PI + 4 * math.asin(math.sqrt((2 / 3) / (2 - 2 / 3)))
    ok &= check(f"el umbral analitico de la ESP: en c' = 1+z el "
                f"trio da pi + 4 asin(sqrt(s2/(2-s2))), que alcanza "
                f"2 pi EXACTAMENTE en s2 = 2/3 ({umbral:.6f} = "
                f"{2 * PI:.6f}); para s2 > 2/3 el rescate es el "
                f"suelo de cola(Y) — por eso el B&B ESP lleva las "
                f"dos cotas de c'", abs(umbral - 2 * PI) < 1e-9)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] B&B rama DR (G-b/G-c interior + G-f todos los "
          "niveles)")
    ok = True
    root = (1.0, 2.0, 0.0, 1.0, 1.0, None)
    dims = [(0, 1, 0.3), (2, 3, 1.0), (4, 5, 3.0)]
    cert, peor, n = bnb(root, trio_ub_DR, OBJ, dims)
    ok &= check(f"sup del trio DR sobre el SUPERCONJUNTO (Sigma_S "
                f"en (1,2), s2 <= Sigma_S/2, T en [1, inf) libre — "
                f"cubre Y de d = 1 y z de todo d >= 2) CERTIFICADO "
                f"< 2 pi - 0.3 = {OBJ:.4f}: {cert}, cota final "
                f"{peor:.4f}, {n} cajas", cert and peor < OBJ)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] B&B rama ESP (G-g ligera, tarifas derivadas)")
    ok = True
    root = (0.01, 1.6, 0.05, PHI / 2, 1.0, PHI, 1.0, 3.7, 1.0, 6.5)
    dims = [(0, 1, 1.0), (2, 3, 0.6), (4, 5, 0.4), (6, 7, 1.5),
            (8, 9, 2.0)]
    cert, peor, n = bnb(root, trio_ub_ESP, OBJ, dims)
    ok &= check(f"sup del trio ESP sobre la caja legal (alpha y z "
                f"en sus ventanas, c' = max(1+z, cola(Y)-omega), "
                f"X's = 0 el peor) CERTIFICADO < 2 pi - 0.3: "
                f"{cert}, cota final {peor:.4f}, {n} cajas",
                cert and peor < OBJ)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] coherencia con la esquina certificada")
    ok = True
    esquina = PI + 4 * math.asin(1 / math.sqrt(3))
    eps = 1e-5
    box = (1.0 + eps, 1.0 + 2 * eps, 0.5 - eps, 0.5,
           1.0, 1.0 + eps)
    v = trio_ub_DR(box)
    ok &= check(f"caja diminuta en la esquina (Sigma_S -> 1, s2 = "
                f"1/2, T = 1): cota = {v:.4f}, esquina exacta pi + "
                f"4 asin(1/sqrt3) = {esquina:.4f}: el B&B es "
                f"AJUSTADO ahi (el sup certificado no esta inflado)",
                v is not None and abs(v - esquina) < 0.01)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles")
    ok = True
    # (a) sin s1 >= s2 la rama DR revienta
    v = (theta_w(1.0, 1.0, 2.0 + 1e-9)
         + theta_w(1.0, 0.95, 2.0 + 1e-9)
         + theta_w(0.95, 1.0, 2.0 + 1e-9))
    ok &= check(f"(a) sin s2 <= Sigma_S/2: el punto (Sigma_S -> 1, "
                f"s2 = 0.95, T = 1) daria {v:.4f} > 2 pi: la "
                f"ligereza con el orden sigma1 >= sigma2 es la que "
                f"carga", v > 2 * PI)
    # (b) ESP sin el suelo de cola(Y): c' = 1+z solo, s2 > 2/3
    s2 = 0.9
    v = (theta_w(1.0, 1.0, 2.0) + theta_w(1.0, s2, 2.0)
         + theta_w(s2, 1.0, 2.0))
    ok &= check(f"(b) ESP sin cola(Y) (c' = 1+z, z = 1, s2 = 0.9 > "
                f"2/3): {v:.4f} > 2 pi — el suelo de cola es el que "
                f"rescata la banda s2 > 2/3 (umbral exacto en [A])",
                v > 2 * PI)
    # (d) HALLAZGO de esta certificacion: sin la pared de masa
    #     Sigma_S <= phi (cola(m) <= phi, exacta), la esquina
    #     s2 -> 1, Sigma_S -> 2 es alcanzable (ventanas no vacias:
    #     Sigma_S in [2 s2, 1+s2) con ancho 1-s2 > 0) y alli la
    #     corona {z, D_m, s2} NO cabe: z+1 = c' diametral y el
    #     bolsillo de Descartes < s2.  El barrido G-g (0 fallos)
    #     nunca la muestreo (medida cero en MC); la pared la
    #     EXCLUYE: s2 <= Sigma_S/2 <= phi/2.
    s2d, SSd, wd = 0.999, 1.998, 1.157
    ad = SSd + wd                      # alpha en su suelo
    zd = ad + wd                       # z en su suelo
    colaYd = (1.0 + SSd + ad + zd) / PHI
    cd = max(1.0 + zd, colaYd - wd)
    vd = th(zd, 1.0, cd) + th(1.0, s2d, cd) + th(s2d, zd, cd)
    bolsillo = 1.0 / (1.0 / zd + 1.0 / 1.0 - 1.0 / cd)
    ok &= check(f"(d) sin la pared Sigma_S <= phi: la esquina "
                f"s2 = {s2d}, Sigma_S = {SSd} es real y su trio da "
                f"{vd:.4f} > 2 pi con bolsillo b2(z, 1; c') = "
                f"{bolsillo:.4f} < s2: la corona NO cabe alli — la "
                f"pared de masa (exacta: cola(m) <= phi) es la que "
                f"la excluye (s2 <= phi/2 = {PHI / 2:.4f}); el "
                f"barrido G-g nunca la muestreo",
                vd > 2 * PI and bolsillo < s2d and SSd > PHI)
    # (c) honestidad: objetivo bajo la esquina 5.5964 no certifica
    root = (1.0, 1.2, 0.3, 0.55, 1.0, 2.0)
    dims = [(0, 1, 1.0), (2, 3, 1.0), (4, 5, 1.0)]
    esquina = PI + 4 * math.asin(1 / math.sqrt(3))
    cert, peor, n = bnb(root, trio_ub_DR, esquina - 0.01,
                        dims, max_boxes=30000)
    ok &= check(f"(c) objetivo {esquina - 0.01:.4f} < esquina "
                f"{esquina:.4f}: el B&B NO certifica (cert = "
                f"{cert}, cota atascada en {peor:.4f}): muerde en "
                f"la esquina exacta", not cert
                and peor >= esquina - 0.011)
    return ok


def main():
    print("=" * 68)
    print("R2B CERTIFICADA: el trio de [G] por subdivision "
          "(drafts/r2bcert.md)")
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
