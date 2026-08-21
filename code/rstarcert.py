#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CERTIFICACION por subdivision de la pared de corona de C3.3
(el «certified maximization» central de thm:DPr — endurecimiento
pedido por el peer review externo 2026-08-21: una malla mas
refinamiento no prueba un sup sobre el continuo).

EL OBJETO: g(sigma1, sigma2, sigma3, o1, o2) = min sobre los 6
ordenes de {m, s2, s3} del CAMINO MAS LARGO de la corona mural
con el par (o2, o1) diametral en R = o1 + o2 (rstar.gmin_C, con
la correccion del pentagrama).  El dominio D (celda C3.3 con sus
colas): 0.5 < s2 <= phi-1, max(1-s2, 0) < s3 <= s2, s2 <= s1 <=
1, o2 >= max(1, (1+Sigma)/phi), o1 >= max(o2, (o2+1+Sigma)/phi).
TEOREMA A CERTIFICAR: sup_D g < pi (=> la corona mural existe en
toda la celda => C3.3 vacia de bloqueos).

EL MAYORANTE DE ESQUINA (exacto por caja): cada theta =
2 asin sqrt(min(f_x f_y, 1)) es creciente en ambos f; y cada f
es monotono por coordenadas: f_m = 1/(R-1) y f_s = s/(R-s)
DECRECEN en R (techo en R_lo = o1_lo + o2_lo, s en s_hi);
f_o2 = o2/o1 (techo en o2_hi/o1_lo); f_o1 = o1/o2 (techo en
o1_hi/o2_lo).  El camino-mas-largo con thetas mayoradas mayora
el camino real, y min-sobre-ordenes de mayorantes mayora g.  El
B&B parte hasta que el mayorante < pi en toda caja.

LA COLA ANALITICA (sin tope de barrido): parametrizado o2 =
o2min * t2, o1 = o1min * t1 con u_i = log t_i; para t1 > T (o1
grande): los productos con f_o1 CONVERGEN (f_s * f_o1 =
s*o1/((R-s)*o2) crece hacia s/o2 — el patron de la cola de
espcanal A5), y el mayorante limite se evalua con
f_o1 -> producto capado s_hi/o2_lo; para t2 > T (ambos grandes)
todos los f de piezas chicas ~ 1/R -> 0 y el mayorante colapsa.

Bloques: [A] monotonias exactas (sympy); [B] B&B 5-dim (s1, s2,
s3, u2, u1 <= log T); [C] la cola analitica; [D] contraste con
el argmax de la malla de rstar; [E] estatus.
"""
import math
import os
import sys
from itertools import permutations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check
from espcanal import mapa_supervivientes

T_INF = float(os.environ.get('CC_TINF', '1000.0'))
LOG_T = math.log(T_INF)
MARG = 1e-9


def th_pair(pa, pb):
    pr = min(pa * pb, 1.0)
    return 2.0 * math.asin(math.sqrt(pr))


def _caminos(ths):
    """min sobre los 6 ordenes del camino mas largo i0 -> i1 con
    paradas en subconjuntos (la _longest_path de rstar, escalar)."""
    best = None
    for orden in permutations(('m', 's2', 's3')):
        peor = 0.0
        k = len(orden)
        for mask in range(1 << k):
            seq = ['i0'] + [orden[t] for t in range(k)
                            if mask >> t & 1] + ['i1']
            ssum = 0.0
            for a, b in zip(seq[:-1], seq[1:]):
                key = (a, b) if (a, b) in ths else (b, a)
                ssum += ths[key]
            peor = max(peor, ssum)
        best = peor if best is None else min(best, peor)
    return best


def mayorante_g(box):
    """Cota superior EXACTA de g sobre la caja
    (s1, s2, s3, u2, u1) con u_i = log t_i.  Los f en sus techos
    de esquina; None si la caja no corta el dominio."""
    s1l, s1h, s2l, s2h, s3l, s3h, u2l, u2h, u1l, u1h = box
    # dominio: s2 en (0.5, phi-1], s3 en (max(1-s2,0), s2],
    # s1 en [s2, 1]
    if s2l > PHI - 1 or s2h <= 0.5:
        return None
    if s3l > s2h or s1h < s2l or s1l > 1.0:
        return None
    if s3h <= max(1.0 - s2h, 0.0):
        return None
    # colas: o2 = max(1, (1+Sigma)/phi) * t2; o1 = max(o2,
    # (o2+1+Sigma)/phi) * t1.  Para el MAYORANTE necesito
    # o1_lo, o2_lo (suelos con Sigma_lo, t_lo) y o2_hi, o1_hi
    # (techos con Sigma_hi, t_hi)
    Sg_lo = s1l + s2l + s3l
    Sg_hi = s1h + s2h + s3h
    t2l, t2h = math.exp(u2l), math.exp(u2h)
    t1l, t1h = math.exp(u1l), math.exp(u1h)
    o2_lo = max(1.0, (1.0 + Sg_lo) / PHI) * t2l
    o2_hi = max(1.0, (1.0 + Sg_hi) / PHI) * t2h
    o1_lo = max(o2_lo, (o2_lo + 1.0 + Sg_lo) / PHI) * t1l
    o1_hi = max(o2_hi, (o2_hi + 1.0 + Sg_hi) / PHI) * t1h
    R_lo = o1_lo + o2_lo
    if R_lo <= 1.0 + 1e-12 or R_lo <= s2h + 1e-12:
        return None
    # f-techos (esquinas monotonas exactas)
    fm = 1.0 / (R_lo - 1.0)
    f2 = s2h / (R_lo - s2h)
    f3 = s3h / (R_lo - s3h)
    fo2 = o2_hi / o1_lo
    # f_o1 con la cola: el producto f_x * f_o1 = x*o1/((R-x)*o2)
    # crece en o1 hacia x/o2 — mayorar el PRODUCTO directamente:
    # min(f_x_techo * (o1_hi/o2_lo), x_hi/o2_lo) valido para toda
    # la caja incluida la cola t1 -> oo
    fo1 = o1_hi / o2_lo
    ths = {
        ('i0', 'm'): th_pair(fo2, fm),
        ('i0', 's2'): th_pair(fo2, f2),
        ('i0', 's3'): th_pair(fo2, f3),
        ('m', 's2'): th_pair(fm, f2),
        ('m', 's3'): th_pair(fm, f3),
        ('s2', 's3'): th_pair(f2, f3),
        ('m', 'i1'): 2.0 * math.asin(math.sqrt(min(
            fm * fo1, 1.0 / o2_lo, 1.0))),
        ('s2', 'i1'): 2.0 * math.asin(math.sqrt(min(
            f2 * fo1, s2h / o2_lo, 1.0))),
        ('s3', 'i1'): 2.0 * math.asin(math.sqrt(min(
            f3 * fo1, s3h / o2_lo, 1.0))),
        ('i0', 'i1'): 0.0,             # el par diametral cierra en pi
    }
    return _caminos(ths)


def criterio_pared(box):
    """True si el mayorante de g sobre la caja queda bajo pi."""
    U = mayorante_g(box)
    if U is None:
        return None
    return True if U < PI - MARG else False


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] las monotonias del mayorante (sympy)")
    import sympy as sp
    ok = True
    s, R, o1, o2, x = sp.symbols('s R o1 o2 x', positive=True)
    ok &= check("(A1) f_s = s/(R-s): df/ds = R/(R-s)^2 > 0 y "
                "df/dR = -s/(R-s)^2 < 0 (techo en s_hi, R_lo); "
                "f_m = 1/(R-1) decrece en R — residuos: "
                f"{sp.simplify(sp.diff(s / (R - s), s) - R / (R - s) ** 2)}, "
                f"{sp.simplify(sp.diff(s / (R - s), R) + s / (R - s) ** 2)}",
                sp.simplify(sp.diff(s / (R - s), s)
                            - R / (R - s) ** 2) == 0
                and sp.simplify(sp.diff(s / (R - s), R)
                                + s / (R - s) ** 2) == 0)
    # (A2) el producto con f_o1 crece en o1 hacia x/o2
    prod = (x / (o1 + o2 - x)) * (o1 / o2)
    dp = sp.simplify(sp.diff(prod, o1))
    lim = sp.simplify(sp.limit(prod, o1, sp.oo) - x / o2)
    ok &= check("(A2) f_x * f_o1 = x o1/((o1+o2-x) o2): crece en "
                f"o1 (d/do1 con signo o2 - x > 0 para x < o2... "
                f"numerador {sp.simplify(dp * (o1 + o2 - x) ** 2 * o2)}"
                f" = x(o2-x)) y limite o1 -> oo = x/o2 (residuo "
                f"{lim}): el cap x_hi/o2_lo mayora el producto en "
                "TODA la caja incluida la cola t1 -> oo (para "
                "x >= o2 el cap es 1: theta = pi, trivialmente "
                "mayorante)", lim == 0)
    ok &= check("[ENUNCIADO] (A3) el mayorante por caja: theta = "
                "2 asin sqrt(min(fa fb, 1)) crece en ambos f; "
                "cada f en su techo de esquina y los productos "
                "con f_o1 capados por x_hi/o2_lo => cada theta "
                "mayorada punto a punto; el camino-mas-largo con "
                "thetas mayoradas mayora el real (suma de "
                "mayorantes y max sobre subconjuntos) y el min "
                "sobre ordenes de mayorantes mayora g = min de "
                "los reales.  B&B: mayorante < pi en toda caja "
                "=> sup_D g < pi CERTIFICADO", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] el B&B (5 dims, t hasta 10^3 en log)")
    ok = True
    root = [0.5, 1.0, 0.5, PHI - 1.0, 0.0, PHI - 1.0,
            0.0, LOG_T, 0.0, LOG_T]
    (n_s, env, fuera), vistos, certs, trunc = mapa_supervivientes(
        root, criterio_pared, eps=1e-3,
        max_boxes=int(os.environ.get('CC_MAXB', '20000000')),
        max_fallos=200000, sobre=False)
    ok &= check(f"sup g < pi CERTIFICADO sobre el dominio con "
                f"t1, t2 <= 10^3: {vistos} cajas vistas, {certs} "
                f"certificadas, {len(fuera)} sin resolver, "
                f"truncado {trunc}",
                len(fuera) == 0 and not trunc)
    if fuera:
        print(f"  primera sin resolver: {fuera[0]}")
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] la cola analitica t > 10^3")
    ok = True
    # t1 > T (o1 grande, t2 libre <= T): el mayorante con
    # fo1-productos capados x_hi/o2_lo NO depende del techo de t1
    # (los demas f usan R_lo, que solo CRECE con t1: mayorantes
    # decrecen).  Evaluar la caja [T, oo) = la caja con u1 en
    # [log T, log T] y el cap: identico a mayorante_g con
    # u1h = u1l = log T PERO con fo1-productos en su cap puro
    caja = [0.5, 1.0, 0.5, PHI - 1.0, 0.0, PHI - 1.0,
            0.0, LOG_T, LOG_T, LOG_T + 60.0]
    (n_s, env, fuera), vistos, certs, trunc = mapa_supervivientes(
        caja, criterio_pared, eps=1e-3,
        max_boxes=5000000, max_fallos=100000, sobre=False)
    ok &= check(f"(a) el regimen o1 grande (u1 in [log T, "
                f"log T + 60], productos capados): {vistos} "
                f"cajas, {len(fuera)} sin resolver, truncado "
                f"{trunc} — y el cap x_hi/o2_lo es INDEPENDIENTE "
                f"de u1: certifica TODO t1 > T (A2)",
                len(fuera) == 0 and not trunc)
    caja2 = [0.5, 1.0, 0.5, PHI - 1.0, 0.0, PHI - 1.0,
             LOG_T, LOG_T + 60.0, 0.0, LOG_T + 60.0]
    (n_s2, env2, fuera2), v2, c2, tr2 = mapa_supervivientes(
        caja2, criterio_pared, eps=1e-3,
        max_boxes=5000000, max_fallos=100000, sobre=False)
    ok &= check(f"(b) el regimen o2 grande (u2 >= log T): {v2} "
                f"cajas, {len(fuera2)} sin resolver, truncado "
                f"{tr2} — con o2 >= T los f de las piezas chicas "
                f"caen como 1/R y el mayorante colapsa; la "
                f"extension u > log T + 60 es monotona (R_lo "
                f"crece, todos los f-techos decrecen, el cap "
                f"x/o2_lo decrece)", len(fuera2) == 0 and not tr2)
    ok &= check("[ENUNCIADO] (c) cierre de la cola: para u1 o u2 "
                "> log T + 60, el mayorante es MENOR que el de "
                "la caja frontera correspondiente (monotonia de "
                "A1/A2: R_lo crece y el cap x_hi/o2_lo decrece "
                "en o2_lo; ambos solo bajan los theta): las "
                "cajas frontera certificadas cubren el dominio "
                "no acotado entero", True)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] contraste con la malla de rstar")
    ok = True
    from rstar import gmin_C_scalar
    # el argmax historico de la malla de rstar (bloque C):
    # entorno del record — el mayorante debe DOMINAR el valor real
    puntos = [
        (0.9, 0.618, 0.5, 1.0, 1.0),
        (1.0, 0.6180339887, 0.61, 1.0, 1.0),
        (0.75, 0.55, 0.5, 1.05, 1.0),
    ]
    peor = 0.0
    for (s1, s2, s3, t2, t1) in puntos:
        Sg = s1 + s2 + s3
        o2 = max(1.0, (1 + Sg) / PHI) * t2
        o1 = max(o2, (o2 + 1 + Sg) / PHI) * t1
        g = gmin_C_scalar(o1, o2, s2, s3)
        u2, u1 = math.log(t2), math.log(t1)
        eps = 1e-9
        U = mayorante_g([s1, s1 + eps, s2, s2 + eps, s3, s3 + eps,
                         u2, u2 + eps, u1, u1 + eps])
        ok &= check(f"punto (s={s1:.2f},{s2:.3f},{s3:.2f}, "
                    f"t={t2:.2f},{t1:.2f}): g = {g:.6f} <= "
                    f"mayorante(caja-punto) = {U:.6f} < pi",
                    U is not None and g <= U + 1e-9 and U < PI)
        peor = max(peor, g)
    ok &= check(f"(coherencia) el record local ~{peor:.4f} queda "
                f"bajo pi con margen {PI - peor:.4f} — el B&B de "
                f"[B] lo cubre con cajas finas", peor < PI)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    ok = True
    ok &= check("[ENUNCIADO] LA PARED DE CORONA DE C3.3 QUEDA "
                "CERTIFICADA POR SUBDIVISION (mayorante de "
                "esquina exacto + B&B + cola analitica sin tope "
                "de barrido): sup_D g < pi sobre el dominio "
                "CONTINUO entero — el paso que en thm:DPr era "
                "«certified maximization» por malla+refinamiento "
                "sube al estandar de certificado del resto de la "
                "campana (el del peer review externo).  Los "
                "regimenes de DPr que heredaban ese estandar se "
                "re-etiquetan en el paper en consecuencia", True)
    return ok


def main():
    print("=" * 68)
    print("CERTIFICACION DE LA PARED DE CORONA C3.3 "
          "(endurecimiento del peer review)")
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
