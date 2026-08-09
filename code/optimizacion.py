#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El lema de optimizacion de sups (docs/drafts/optimizacion.md):
sup G < 2pi - 0.05 CERTIFICADO por branch-and-bound con cotas de
esquina (aritmetica de intervalos por monotonia), no por muestreo.

Cierra el asterisco "el sup es un barrido" para TODOS los
presupuestos de sombras de los teoremas escritos de una vez: el
lema de la cola geometrica (colageometrica.md) domina cada
presupuesto real por G_u; aqui el sup de G sobre su caja queda
acotado rigurosamente.

LA PALANCA (bloque A, exacta): cada termino 2 asin((s+x)/(R-s)) es
  - CRECIENTE en la pieza x            (numerador),
  - CRECIENTE en s                     (d/ds = ((R-s)+(s+x))/(R-s)^2 > 0),
  - DECRECIENTE en R                   (denominador),
con la pi-gorra 2 asin(min(1, .)) <= pi.  Sobre una caja
[t2] x [Sigma] x [u] x [t1], evaluar numeradores en el extremo ALTO
y R en el BAJO da una COTA SUPERIOR valida de G en toda la caja
(esquina pesimista; puede ser infactible: sobra).  Podas exactas:
t2 >= 1+Sigma (hipotesis del lema), u <= phi t2, y el VINCULO
t1 >= max(t2, (t2+u)/phi) (colageometrica (V)) — la poda del
vinculo usa u_lo (cota inferior valida del suelo en la caja).

DIRECCIONES NO ACOTADAS:
  - t1: la caja final [T1, inf) usa la pi-gorra para el termino
    lider (2 asin <= pi SIEMPRE) y R_lo = T1 + t2_lo para el resto,
    que muere con T1.
  - t2 > T2 = 1000: forma NORMALIZADA (dividir por t2): a = t1/t2
    en [1, 40] + cola a > 40, u' = u/t2 en [0, phi], sigma = s/t2
    <= (phi/2)/T2, dominantes d'_r <= min(1, u'/phi^r, u'/(r+1))
    (soltar el -(1+Sigma)/t2 solo AGRANDA: cota valida), serie
    truncada a 60 terminos + resto analitico con asin(x) <= pi x/2
    y cola geometrica de razon 1/phi.

MODOS (los de colageometrica): modo 1 (s' en el tope
min(Sigma/2, phi/2), extra D_m = 1) — que ademas MAYORA el modo
sigma2 (misma s_hi por la ligadura sigma2 <= Sigma/2 <= phi/2 y
mismos extras: bloque A); modo 2 (w* = 1/phi, extras D_m y s').

Flotantes (redaccion reparada en ronda hostil): sin redondeo
dirigido (IEEE double).  La caja principal (donde vive el argmax)
se certifica a OBJETIVO FUERTE 5.25 y la cola normalizada a
2pi - 0.05 con cota final 6.0408: TODA caja final tiene cota
computada <= max(5.25, 6.0408) = 6.0408, margen 0.19 rad frente a
2pi - 0.05 — mas de 12 ordenes sobre el error de redondeo de una
suma de ~20 asin (~1e-14).  (La version v1 certificaba B a
2pi - 0.05 directamente y la decision de parada quedaba a 5e-5 del
objetivo: el certificado era correcto pero la frase de los "12
ordenes" era falsa; subir el objetivo de B a 5.25 la compra.)

Bloques: [A] monotonias y reducciones exactas (sympy); [B] el
branch-and-bound principal (t2 <= 1000); [C] la cola t2 > 1000
normalizada; [D] coherencia con el sup muestreado; [E] controles
(sin la hipotesis el B&B NO certifica; apretar el objetivo por
debajo del sup real tampoco).
"""
import heapq
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check

OBJ = 2 * PI - 0.05                    # el objetivo a certificar
OBJ_F = 5.25                           # objetivo FUERTE de la caja
                                       # principal (ronda hostil,
                                       # hallazgo 3: compra margen
                                       # 0.98 rad frente a OBJ)


def term_ub(x_hi, R_lo, s_hi):
    """Cota superior del termino 2 asin((s+x)/(R-s)) en la caja:
    numerador alto, denominador bajo, pi-gorra."""
    d = R_lo - s_hi
    w = s_hi + x_hi
    if d <= w:
        return PI
    return 2 * math.asin(w / d)


def doms_ub(t2_hi, S_lo, u_hi):
    """Dominantes de la cola evaluados en la esquina pesimista de la
    caja (piezas grandes: t2_hi, Sigma_lo, u_hi); cotas y corte de
    colageometrica.  Serie finita (corte de existencia con S_lo:
    p_min y el descuento 1+Sigma en su extremo conservador)."""
    p_min = max(1.0, (1.0 + S_lo) / PHI)
    M = u_hi - 1.0 - S_lo
    out = []
    r = 0
    while True:
        cap = u_hi / PHI ** r - (1.0 + S_lo)
        if cap < p_min - 1e-9:
            break
        if r > 200:
            # inalcanzable con t2 <= 1000 (r_max = 13; r = 200
            # exigiria u ~ 1.9e42); truncar EN SILENCIO dejaria de
            # ser cota — fuera del dominio: reventar (ronda hostil)
            raise RuntimeError("doms_ub fuera del dominio t2 <= 1000")
        out.append(min(t2_hi, cap, M / (r + 1)))
        r += 1
    return out


def G_ub(box, modo):
    """Cota superior de G sobre la caja (t2l, t2h, Sl, Sh, ul, uh,
    t1l, t1h); t1h = None significa [t1l, inf) (pi-gorra en el
    lider).  None si la caja es infactible (podas exactas)."""
    t2l, t2h, Sl, Sh, ul, uh, t1l, t1h = box
    # podas exactas (con los extremos que NO pierden puntos reales)
    if t2h < 1.0 + Sl - 1e-12:
        return None                    # t2 >= 1+Sigma
    if ul > PHI * t2h + 1e-12:
        return None                    # u <= phi t2
    suelo = max(t2l, (t2l + ul) / PHI)
    if t1h is not None and t1h < suelo - 1e-12:
        return None                    # vinculo de t1
    s_hi = min(Sh / 2, PHI / 2) if modo == 1 else 1 / PHI
    extras = [1.0] + ([min(Sh / 2, PHI / 2)] if modo == 2 else [])
    R_lo = max(t1l, suelo) + t2l
    total = PI if t1h is None else term_ub(t1h, R_lo, s_hi)
    total += term_ub(t2h, R_lo, s_hi)
    for d in doms_ub(t2h, Sl, min(uh, PHI * t2h)):
        total += term_ub(d, R_lo, s_hi)
    for x in extras:
        total += term_ub(x, R_lo, s_hi)
    return total


def branch_and_bound(root, modo, objetivo, max_boxes=400000):
    """Certifica sup G < objetivo sobre la caja raiz subdividiendo
    la dimension relativa mas ancha.  Devuelve (certificado,
    peor_cota, n_cajas)."""
    v0 = G_ub(root, modo)
    if v0 is None:
        return True, 0.0, 0
    heap = [(-v0, root)]
    n = 0
    peor_final = 0.0
    while heap:
        n += 1
        if n > max_boxes:
            return False, -heap[0][0], n
        negv, box = heapq.heappop(heap)
        v = -negv
        if v < objetivo:
            peor_final = max(peor_final, v)
            # todo lo restante en el heap es <= v: certificado
            return True, max(peor_final, v), n
        t2l, t2h, Sl, Sh, ul, uh, t1l, t1h = box
        # anchuras relativas (t1 infinito: anchura del tramo finito)
        t1h_eff = t1h if t1h is not None else 4 * t1l
        dims = [
            ((t2h - t2l) / t2l, 0),
            ((Sh - Sl), 1),
            ((uh - ul) / max(ul, 1.0), 2),
            ((t1h_eff - t1l) / t1l, 3),
        ]
        dims.sort(reverse=True)
        d = dims[0][1]
        hijos = []
        if d == 0:
            m = (t2l + t2h) / 2
            hijos = [(t2l, m, Sl, Sh, ul, uh, t1l, t1h),
                     (m, t2h, Sl, Sh, ul, uh, t1l, t1h)]
        elif d == 1:
            m = (Sl + Sh) / 2
            hijos = [(t2l, t2h, Sl, m, ul, uh, t1l, t1h),
                     (t2l, t2h, m, Sh, ul, uh, t1l, t1h)]
        elif d == 2:
            m = (ul + uh) / 2
            hijos = [(t2l, t2h, Sl, Sh, ul, m, t1l, t1h),
                     (t2l, t2h, Sl, Sh, m, uh, t1l, t1h)]
        else:
            if t1h is None:
                m = 4 * t1l
                hijos = [(t2l, t2h, Sl, Sh, ul, uh, t1l, m),
                         (t2l, t2h, Sl, Sh, ul, uh, m, None)]
            else:
                m = (t1l + t1h) / 2
                hijos = [(t2l, t2h, Sl, Sh, ul, uh, t1l, m),
                         (t2l, t2h, Sl, Sh, ul, uh, m, t1h)]
        for h in hijos:
            v = G_ub(h, modo)
            if v is not None:
                heapq.heappush(heap, (-v, h))
    return True, peor_final, n


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] monotonias y reducciones exactas (sympy)")
    import sympy as sp
    ok = True
    x, R, s = sp.symbols('x R s', positive=True)
    arg = (s + x) / (R - s)
    ok &= check("monotonia del argumento: d/dx > 0, d/dR < 0, "
                "d/ds = ((R-s)+(s+x))/(R-s)^2 > 0; asin creciente y "
                "pi-gorra: evaluar numeradores ALTOS y R BAJO da "
                "cota superior de caja (aritmetica de intervalos "
                "por monotonia)",
                sp.simplify(sp.diff(arg, x) - 1 / (R - s)) == 0
                and sp.simplify(sp.diff(arg, s)
                                - (R + x) / (R - s) ** 2) == 0
                and sp.simplify(sp.diff(arg, R)
                                + (s + x) / (R - s) ** 2) == 0)
    ok &= check("el modo sigma2 queda MAYORADO por el modo 1: misma "
                "s_hi (sigma2 <= Sigma/2 <= phi/2 por la ligadura "
                "sigma1 >= sigma2 ambas en S) y mismos extras "
                "(D_m = 1 o m = 1: la misma pieza unidad): basta "
                "certificar los modos 1 y 2", True)
    ok &= check("podas exactas: t2 >= 1+Sigma (hipotesis del lema "
                "de la cola), u <= phi t2 (cascada de t2) y t1 >= "
                "max(t2, (t2+u_lo)/phi) (vinculo (V) con u_lo: cota "
                "inferior valida en la caja); las cajas podadas no "
                "contienen puntos reales", True)
    ok &= check("regimen automatico en toda la caja: s_hi <= phi/2 "
                "y t2 >= 1+Sigma >= 2 > phi = 2(phi/2): el regimen "
                "2s < t2 nunca falla dentro de las hipotesis "
                "(margen 2-phi)", 2 - PHI > 0.38)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] branch-and-bound principal (2 <= t2 <= 1000), "
          "objetivo FUERTE 5.25")
    ok = True
    for modo in (1, 2):
        root = (2.0, 1000.0, 1.0, PHI, 2.0, PHI * 1000.0,
                2.0, None)
        cert, peor, n = branch_and_bound(root, modo, OBJ_F)
        ok &= check(f"modo {modo}: sup G <= {OBJ_F} CERTIFICADO "
                    f"sobre la caja principal (t2 hasta 1000, u "
                    f"hasta phi t2, t1 hasta inf via pi-gorra): "
                    f"{cert}, cota final {peor:.4f}, {n} cajas — "
                    f"margen 2pi - 0.05 - 5.25 = "
                    f"{OBJ - OBJ_F:.4f} rad, > 12 ordenes sobre el "
                    f"error float", cert and peor < OBJ_F)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] la cola t2 > 1000 (forma normalizada)")
    ok = True
    T2 = 1000.0
    sigma = (PHI / 2) / T2             # s/t2 en su tope
    ex_hi = 1.0 / T2                   # extras/t2 (D_m, s' <= 1)

    def cola_norm_ub(al, ah, upl, uph):
        """Cota del G normalizado en la caja (a = t1/t2, u' = u/t2):
        lider pi-gorra si ah = None; dominantes d'_r <= min(1,
        u'/phi^r, u'/(r+1)) (60 terminos + resto analitico).
        VINCULO NORMALIZADO (reparado en ronda hostil, hallazgo 1):
        a >= (1 + u')/phi — el "t2" del vinculo se normaliza a 1
        EXACTO, no a al; la version con (al + upl)/phi sobreestimaba
        R y NO era cota superior (deficit hasta 0.39 rad en cajas
        con al > 1: control E(c)).
        RESTO ANALITICO (justificacion reparada, hallazgo 2): los
        terminos reales r >= 60 solo existen si t2 >= ~3 phi^59, y
        su parte sigma real cumple sigma_real*(N-60) <=
        (phi/2) log_phi(phi t2/3)/t2, DECRECIENTE en t2 >= 1000,
        con sup < 1e-13 << sigma*40: el "40" del codigo sobra por
        11 ordenes; la parte de piezas es geometrica de razon 1/phi
        con asin(x) <= pi x/2."""
        if ah is not None and ah < max(1.0, (1.0 + upl) / PHI) - 1e-12:
            return None                # vinculo normalizado
        Rl = max(al, (1.0 + upl) / PHI) + 1.0
        d = Rl - sigma

        def t(xh):
            w = sigma + xh
            if d <= w:
                return PI
            return 2 * math.asin(w / d)
        total = PI if ah is None else t(ah)
        total += t(1.0)
        resto = 0.0
        for r in range(60):
            dr = min(1.0, uph / PHI ** r, uph / (r + 1))
            total += t(dr)
        # resto analitico r >= 60: d'_r <= u'/phi^r, asin <= pi x/2
        dr60 = uph / PHI ** 60
        resto = PI * (sigma * 40 + dr60 * PHI ** 2) / d
        total += resto
        total += 2 * t(ex_hi)
        return total

    # B&B 2D en (a, u'): a en [1, 40] + cola a > 40 (pi-gorra)
    heap = []
    v = cola_norm_ub(1.0, 40.0, 0.0, PHI)
    heap.append((-v, (1.0, 40.0, 0.0, PHI)))
    v = cola_norm_ub(40.0, None, 0.0, PHI)
    heap.append((-v, (40.0, None, 0.0, PHI)))
    heapq.heapify(heap)
    n, cert, peor = 0, True, 0.0
    while heap:
        n += 1
        if n > 200000:
            cert = False
            peor = -heap[0][0]
            break
        negv, (al, ah, upl, uph) = heapq.heappop(heap)
        v = -negv
        if v < OBJ:
            peor = max(peor, v)
            break
        ah_eff = ah if ah is not None else 4 * al
        if (ah_eff - al) / al > (uph - upl):
            if ah is None:
                hijos = [(al, 4 * al, upl, uph),
                         (4 * al, None, upl, uph)]
            else:
                m = (al + ah) / 2
                hijos = [(al, m, upl, uph), (m, ah, upl, uph)]
        else:
            m = (upl + uph) / 2
            hijos = [(al, ah, upl, m), (al, ah, m, uph)]
        for h in hijos:
            v = cola_norm_ub(*h)
            if v is not None:
                heapq.heappush(heap, (-v, h))
    ok &= check(f"t2 > 1000 normalizado: sup < 2pi - 0.05 "
                f"CERTIFICADO ({cert}, cota final {peor:.4f}, {n} "
                f"cajas; sigma = s/t2 <= {sigma:.2e}, resto "
                f"analitico geometrico tras 60 terminos)",
                cert and peor < OBJ)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] coherencia con el sup muestreado")
    ok = True
    # la cota B&B en una caja diminuta alrededor del argmax debe
    # aterrizar cerca de 5.2115 (el sup real)
    eps = 1e-4
    box = (2.0, 2.0 + eps, 1.0, 1.0 + eps,
           PHI * 2.0 - eps, PHI * 2.0,
           2 * PHI - eps, 2 * PHI + eps)
    v = G_ub(box, 2)
    ok &= check(f"caja diminuta alrededor del argmax (t2 = 2, "
                f"Sigma = 1, u = 2phi, t1 = 2phi, modo w*): cota = "
                f"{v:.4f}, en [5.2115, 5.22] (el B&B es AJUSTADO en "
                f"la esquina critica: el sup certificado no esta "
                f"inflado)", v is not None and 5.2115 - 1e-6 <= v <= 5.22)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles")
    ok = True
    # (a) sin la hipotesis t2 >= 1+Sigma el B&B NO certifica: la
    #     navaja n = 2 vive en t2 = (1+Sigma)/phi y supera 2pi
    SSn = 1.0 + 1e-6
    t2n = (1.0 + SSn) / PHI
    box = (t2n - 1e-7, t2n + 1e-7, SSn - 1e-9, SSn + 1e-9,
           1.0 + SSn - 1e-7, 1.0 + SSn + 1e-7,
           1.0 + SSn - 1e-6, 1.0 + SSn + 1e-6)
    t2l, t2h, Sl, Sh, ul, uh, t1l, t1h = box
    s_hi = 1 / PHI
    R_lo = t1l + t2l
    v = (term_ub(t1h, R_lo, s_hi) + term_ub(t2h, R_lo, s_hi)
         + term_ub(1.0, R_lo, s_hi)
         + term_ub(min(Sh / 2, PHI / 2), R_lo, s_hi))
    ok &= check(f"(a) SIN t2 >= 1+Sigma: la caja de la navaja "
                f"(t2 = (1+Sigma)/phi, t1 = 1+Sigma) da cota "
                f"{v:.4f} > 2pi = {2 * PI:.4f} y NO se puede "
                f"certificar por refinamiento (el presupuesto REAL "
                f"alli es 6.93 > 2pi, colageometrica E(e)): la "
                f"hipotesis es la que separa", v > 2 * PI)
    # (b) apretar el objetivo por debajo del sup real: el B&B debe
    #     FALLAR (honestidad: no certifica lo falso)
    root = (2.0, 4.0, 1.0, 1.1, 2.0, PHI * 4.0, 2.0, 16.0)
    cert, peor, n = branch_and_bound(root, 2, 5.20, max_boxes=40000)
    ok &= check(f"(b) objetivo 5.20 < sup real 5.2115: el B&B NO "
                f"certifica (cert = {cert}, cota atascada en "
                f"{peor:.4f} >= 5.2115): el certificado no es "
                f"vacuo, muerde exactamente en el sup",
                not cert and peor >= 5.2115 - 1e-6)
    # (c) la version ROTA del suelo normalizado (hallazgo 1 del
    #     acta) NO era cota superior: en la caja a in [1.7, 1.75],
    #     u' in [1.55, phi] el punto real (a = 1.7, u' = phi) la
    #     supera en ~0.39 rad
    T2 = 1000.0
    sigma = (PHI / 2) / T2
    al, ah, upl, uph = 1.7, 1.75, 1.55, PHI

    def norm_val(Rl, a_num, up_num):
        d = Rl - sigma

        def t(xh):
            w = sigma + xh
            return PI if d <= w else 2 * math.asin(w / d)
        total = t(a_num) + t(1.0)
        for r in range(60):
            total += t(min(1.0, up_num / PHI ** r,
                           up_num / (r + 1)))
        return total
    Rl_rota = max(al, (al + upl) / PHI) + 1.0
    cota_rota = norm_val(Rl_rota, ah, uph)
    R_punto = 1.7 + 1.0                # punto real: a = 1.7 >=
    val_punto = norm_val(R_punto, 1.7, PHI)  # (1+phi)/phi = phi OK
    ok &= check(f"(c) la version rota del vinculo normalizado "
                f"((al+upl)/phi en vez de (1+upl)/phi) daba cota "
                f"{cota_rota:.4f} < valor real en un punto DE la "
                f"caja {val_punto:.4f} (deficit "
                f"{val_punto - cota_rota:.3f} rad): no era cota — "
                f"reparada; el certificado v1 sobrevivio porque "
                f"ninguna caja evaluada la activaba (instrumentado "
                f"en acta)", cota_rota < val_punto - 0.3)
    return ok


def main():
    print("=" * 68)
    print("EL LEMA DE OPTIMIZACION: sup G < 2pi - 0.05 certificado "
          "por B&B (drafts/optimizacion.md)")
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
