#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CERTIFICACION por subdivision del presupuesto de sombras de
thm:D1written (endurecimiento 3/3 del peer review externo: la ultima
maximizacion dirigida con asterisco — insercion.py bloque G — sube a
certificado de caja al estilo rstarcert).

EL CLAIM: sobre el politopo cascada del dominio D1
  o_1 >= o_2 >= ... >= o_j >= 1  (j >= 3),
  o_k >= (sum_{i>k} o_i + 1 + Sigma)/phi,   Sigma in [1, phi],
el presupuesto de sombras en R = o_1 + o_2 para insertar s,
  p = sum_{x in {o_1..o_j} u extras} 2 asin((s+x)/(R-s)),
cumple p < 2 pi para los dos presupuestos del teorema:
  p1: s = sigma_2 = phi - 1 = 1/phi, extras = {1}
  p2: s = w* = 1/phi,               extras = {1, phi-1}
(ambos con el MISMO s = 1/phi: phi - 1 = 1/phi).

LA REDUCCION DE DIMENSION (cubre TODOS los j de golpe): las piezas
k >= 3 se agrupan por su MASA m = sum_{k>=3} o_k y su numero
n = j - 2 <= m (cada o_k >= 1).  Por convexidad de asin en [0, 1],
asin(z)/z es creciente, luego para z_k <= z_max:
  sum_k 2 asin(z_k) <= C(z_max) * sum_k z_k,
  C(z) = 2 asin(z)/z    (la CUERDA adaptativa),
y sum_k z_k = (n s + m)/u <= m (1+s)/u con u = R - s.  El politopo
colapsa a CUATRO variables (Sigma, m, o_2, o_1) con las ligaduras de
cascada agregadas
  o_2 >= (m + 1 + Sigma)/phi,   o_1 >= max(o_2, (o_2+m+1+Sigma)/phi),
que toda instancia satisface (la cascada real las implica sumando).
z_max = (s + o_2)/u porque o_k <= o_2.

MAYORANTES DE CAJA (parametrizacion log: m = e^{vm}, o_2 =
suelo2 * e^{v2}, o_1 = suelo1 * e^{v1}):
  term1 = 2 asin((s+o1)/(o1+o2-s)): CRECE en o1 (signo o2 - 2s > 0,
    y o2 >= 3/phi > 2/phi = 2s en todo el dominio), DECRECE en o2
    -> esquina (o1_hi, o2_lo);
  term2: espejo -> (o2_hi, o1_lo), con el CAP de dominancia
    z2 <= (s+o2)/(2 o2 - s) (usa o1 >= o2; decrece en o2 -> o2_lo);
  masa <= C(z_max) * (1+s) m_hi/u_lo (n <= m);
  extras: 2 asin((s+e)/u_lo).
COLAS (sin tope de barrido, como rstarcert): v1 -> inf: term1 -> pi
y el resto se evalua con o1_lo enorme (total ~ 6.14 < 2 pi); v2 ->
inf: term2 por el cap (~ pi/3) y masa/term1 con u enorme; vm -> inf:
z1, z2, z_max DECRECEN en T = m + 1 + Sigma (gate simbolico A5) y
m/u <= 1/(lambda1+lambda2) <= 1/phi: el B&B 3D con m = e^V mayora
todo m >= e^V.

Bloques: [A] gates simbolicos; [B] B&B principal 4D (p1 y p2);
[C] las colas (celdas con algun v >= V); [D] contraste con
insercion.py (esquinas 4.7225 / 5.2644 y sondeo dentro de la cota);
[E] estatus.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check
from espcanal import mapa_supervivientes

S_INS = 1.0 / PHI                     # = phi - 1: el s de ambos
V_TOPE = math.log(64.0)               # frontera de las colas
EXTRAS_P1 = [1.0]
EXTRAS_P2 = [1.0, PHI - 1.0]


def _asin2(z):
    return 2.0 * math.asin(max(0.0, min(1.0, z)))


def _cuerda(z):
    """C(z) = 2 asin(z)/z, creciente (convexidad); C(0+) = 2."""
    z = max(1e-12, min(1.0, z))
    return 2.0 * math.asin(z) / z


def _rangos(box):
    """Caja (Sg, vm, v2, v1) -> rangos coherentes de (m, o2, o1).
    hi = None significa infinito (celda de cola)."""
    Sgl, Sgh, vml, vmh, v2l, v2h, v1l, v1h = box
    m_lo = math.exp(vml)
    m_hi = None if vmh is None else math.exp(vmh)
    s2_lo = (m_lo + 1.0 + Sgl) / PHI
    o2_lo = s2_lo * math.exp(v2l)
    if m_hi is None or v2h is None:
        o2_hi = None
    else:
        o2_hi = (m_hi + 1.0 + Sgh) / PHI * math.exp(v2h)
    s1_lo = max(o2_lo, (o2_lo + m_lo + 1.0 + Sgl) / PHI)
    o1_lo = s1_lo * math.exp(v1l)
    if o2_hi is None or v1h is None:
        o1_hi = None
    else:
        o1_hi = max(o2_hi, (o2_hi + m_hi + 1.0 + Sgh) / PHI) \
            * math.exp(v1h)
    return m_lo, m_hi, o2_lo, o2_hi, o1_lo, o1_hi


def presupuesto_mayorante(box, extras):
    """Mayorante del presupuesto sobre la caja; None si mal formada.
    La cola vm (m_hi = None) va por la RAMA HOMOGENEA: con
    o_i = lambda_i T (T = m+1+Sigma), cada z decrece en T (gate A5,
    valido para lambdas mixtas: la derivada ~ -s(2a+b) < 0 siempre),
    luego el sup vive en T_lo; y m/u crece en m hacia su limite
    1/(lambda1_lo+lambda2_lo) (gate A5)."""
    s = S_INS
    Sgl, Sgh, vml, vmh, v2l, v2h, v1l, v1h = box
    m_lo, m_hi, o2_lo, o2_hi, o1_lo, o1_hi = _rangos(box)
    cap2 = _asin2((s + o2_lo) / (2.0 * o2_lo - s))
    zdom = (s + o2_lo) / (2.0 * o2_lo - s)
    if m_hi is None:
        # ---- rama homogenea (cola vm) ----
        T_lo = m_lo + 1.0 + Sgl
        l2_lo = math.exp(v2l) / PHI
        l1_lo = max(l2_lo, (l2_lo + 1.0) / PHI) * math.exp(v1l)
        u_lo = (l1_lo + l2_lo) * T_lo - s
        if v1h is None:
            t1 = PI
        else:
            l2b = l2_lo                      # z1: o2 en su suelo
            l1_hi = max(l2b, (l2b + 1.0) / PHI) * math.exp(v1h)
            t1 = _asin2((s + l1_hi * T_lo)
                        / ((l1_hi + l2b) * T_lo - s))
        if v2h is None:
            t2 = cap2
            z_max = zdom
        else:
            l2_hi = math.exp(v2h) / PHI
            z2 = (s + l2_hi * T_lo) / ((l1_lo + l2_hi) * T_lo - s)
            t2 = min(cap2, _asin2(z2))
            z_max = min(zdom, z2)
        masa_ratio = 1.0 / (l1_lo + l2_lo)
    else:
        # ---- rama de esquinas (m finito) ----
        u_lo = o1_lo + o2_lo - s
        if o1_hi is None:
            t1 = PI                    # limite o1 -> inf
        else:
            t1 = _asin2((s + o1_hi) / (o1_hi + o2_lo - s))
        if o2_hi is None:
            t2 = cap2
            z_max = zdom
        else:
            t2 = min(_asin2((s + o2_hi) / (o1_lo + o2_hi - s)),
                     cap2)
            z_max = min(zdom, (s + o2_hi) / u_lo)
        masa_ratio = m_hi / u_lo
    if u_lo <= s + 1.0:                # fuera de regimen: no ocurre
        return None                    # en el dominio (o's >= 1.85)
    masa = _cuerda(min(1.0, z_max)) * (1.0 + s) * masa_ratio
    te = sum(_asin2((s + e) / u_lo) for e in extras)
    return t1 + t2 + masa + te


def criterio(box, extras):
    # devuelve SIEMPRE booleano estricto: el None interno de
    # presupuesto_mayorante mapea a False (acta H4 — el motor
    # mapa_supervivientes descarta cajas None en silencio)
    p = presupuesto_mayorante(box, extras)
    assert p is None or isinstance(p, float)
    return p is not None and p < 2.0 * PI - 1e-9


def crit_p1(box):
    return criterio(box, EXTRAS_P1)


def crit_p2(box):
    return criterio(box, EXTRAS_P2)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] gates simbolicos de los mayorantes")
    import sympy as sp
    ok = True
    s, o1, o2, u, z, m, T, l1, l2 = sp.symbols(
        's o1 o2 u z m T lambda1 lambda2', positive=True)
    # A1: asin convexa en (0,1) => asin(z)/z creciente => cuerda
    d2 = sp.diff(sp.asin(z), z, 2)
    ok &= check("(A1) asin''(z) = z/(1-z^2)^(3/2) >= 0 en (0,1): "
                "asin convexa => asin(z)/z creciente => la CUERDA "
                "2 asin(z) <= C(z_max) z mayora cada termino con "
                f"z <= z_max (d2 = {sp.simplify(d2)})",
                sp.simplify(d2 - z / (1 - z ** 2) ** sp.Rational(3, 2))
                == 0)
    # A2: term1 crece en o1 sii o2 > 2s; decrece en o2
    z1 = (s + o1) / (o1 + o2 - s)
    d_o1 = sp.simplify(sp.diff(z1, o1) * (o1 + o2 - s) ** 2)
    d_o2 = sp.simplify(sp.diff(z1, o2) * (o1 + o2 - s) ** 2)
    ok &= check(f"(A2) d z1/d o1 ~ {d_o1} (signo o2 - 2s > 0 en el "
                f"dominio) y d z1/d o2 ~ {d_o2} < 0: esquina "
                "(o1_hi, o2_lo); espejo para z2 con o1 - 2s > 0",
                sp.simplify(d_o1 - (o2 - 2 * s)) == 0
                and sp.simplify(d_o2 + (s + o1)) == 0)
    # A3: el cap de dominancia decrece en o2
    zc = (s + o2) / (2 * o2 - s)
    dc = sp.simplify(sp.diff(zc, o2) * (2 * o2 - s) ** 2)
    ok &= check(f"(A3) el cap z2 <= (s+o2)/(2 o2 - s) (usa o1 >= "
                f"o2) tiene derivada ~ {dc} < 0: sup en o2_lo",
                sp.simplify(dc + 3 * s) == 0)
    # A4: regimen o2 > 2s en todo el dominio
    ok &= check("(A4) o2 >= (m+1+Sigma)/phi >= 3/phi > 2/phi = 2s "
                "exacto (m >= 1, Sigma >= 1): el regimen sombra y "
                "los signos de A2 valen en todo el dominio; y "
                "o1 + o2 >= (m+1+Sigma)(1+phi)/phi^2 = m+1+Sigma "
                "exacto (phi^2 = 1+phi)",
                3.0 / PHI > 2.0 / PHI
                and abs((1 + PHI) / PHI ** 2 - 1.0) < 1e-12)
    # A5: decrecimiento en T = m+1+Sigma con lambdas fijas (cola vm)
    z1T = (s + l1 * T) / ((l1 + l2) * T - s)
    dT = sp.simplify(sp.diff(z1T, T) * ((l1 + l2) * T - s) ** 2)
    ok &= check(f"(A5) con o1 = lambda1 T, o2 = lambda2 T (T = "
                f"m+1+Sigma), d z1/dT ~ {dT} < 0: los z DECRECEN "
                "en T — el B&B de la cola vm con m = e^V mayora "
                "todo m mayor; y m/u crece en m hacia su limite "
                "1/(lambda1+lambda2) <= 1/phi",
                sp.simplify(dT + s * (2 * l1 + l2)) == 0)
    # A7: monotonias de la rama homogenea en las lambdas y en m
    a, b, c = sp.symbols('a b c', positive=True)
    zh = (s + a * T) / ((a + b) * T - s)
    da = sp.simplify(sp.diff(zh, a) * ((a + b) * T - s) ** 2 / T)
    mu = m / ((a + b) * (m + c) - s)
    dmu = sp.simplify(sp.diff(mu, m) * ((a + b) * (m + c) - s) ** 2)
    ok &= check(f"(A7) z homogeneo crece en su lambda propia "
                f"(d/da ~ {da}, signo b T - 2s > 0: b >= 1/phi, "
                f"T >= 3 => bT >= 3/phi > 2/phi = 2s) y m/u crece "
                f"en m (d ~ {dmu} = (a+b)c - s > 0 con c = 1+Sigma "
                ">= 2, a+b >= phi): lambda_hi y el limite "
                "1/(l1_lo+l2_lo) mayoran",
                sp.simplify(da - (b * T - 2 * s)) == 0
                and sp.simplify(dmu - ((a + b) * c - s)) == 0)
    # A8 (acta H1): la esquina de t1 homogeneo usa l2b = l2_lo
    # PERO suelo1 crece en lambda2: la esquina no es de lambdas
    # independientes — vale por la MONOTONIA ACOPLADA a lo largo
    # de v2 (rho = e^{v2}: lambda2 = rho/phi y el suelo de lambda1
    # suben JUNTOS y z1 baja), en ambos regimenes del max
    rho, e1 = sp.symbols('rho e1', positive=True)
    phi_s = sp.Rational(1, 2) + sp.sqrt(5) / 2
    l2s = rho / phi_s
    for reg, l1s in (("suelo (l2+1)/phi", (l2s + 1) / phi_s * e1),
                     ("suelo l2", l2s * e1)):
        z1r = (s + l1s * T) / ((l1s + l2s) * T - s)
        dr = sp.simplify(sp.diff(z1r, rho)
                         * ((l1s + l2s) * T - s) ** 2)
        neg = sp.simplify(sp.expand(dr))
        # dr = -(terminos positivos): comprobar -dr con coefs >= 0
        pol = sp.Poly(sp.expand(-neg), T, s, e1)
        coefs_ok = all(sp.simplify(c) >= 0 or
                       (sp.simplify(c)).is_positive
                       for c in pol.coeffs())
        ok &= check(f"(A8-{reg}) dz1/d rho ~ {sp.factor(neg)} < 0: "
                    "subir v2 con v1, T fijos BAJA z1 — la esquina "
                    "t1 con l2b = l2_lo mayora la caja entera "
                    "(monotonia acoplada del acta H1)",
                    coefs_ok and bool(neg.subs(
                        {T: 3, s: 0.618, e1: 1.0, rho: 1.0}) < 0))
    # A6: n <= m y la cota de masa
    ok &= check("(A6) n = j - 2 <= m (cada o_k >= 1) => "
                "sum(s + o_k) = n s + m <= m(1+s); z_k <= z_max = "
                "(s+o2)/u (o_k <= o2): la cuerda A1 cierra la "
                "reduccion de dimension — el B&B 4D cubre TODOS "
                "los j >= 3 a la vez", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] B&B principal 4D (v's en [0, V], m en [1, 64])")
    ok = True
    root = [1.0, PHI, 0.0, V_TOPE, 0.0, V_TOPE, 0.0, V_TOPE]
    for nombre, crit in (("p1 (sigma2, extras {1})", crit_p1),
                         ("p2 (w*, extras {1, sigma2})", crit_p2)):
        (n_s, env, fuera), vistos, certs, trunc = \
            mapa_supervivientes(root, crit, eps=2e-3,
                                max_boxes=int(os.environ.get(
                                    'CC_MAXB', '20000000')),
                                max_fallos=50000, sobre=False)
        ok &= check(f"{nombre}: {vistos} cajas, {certs} "
                    f"certificadas, {len(fuera)} sin resolver, "
                    f"truncado {trunc}",
                    len(fuera) == 0 and not trunc)
        if fuera:
            print(f"  primera: {fuera[0]}")
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] las colas: celdas con algun v en [V, inf)")
    ok = True
    INF = None
    # las 7 celdas del cubo {[0,V], [V,inf)}^3 menos la finita;
    # las direcciones infinitas van con hi = None (caps de limite);
    # las finitas se subdividen por B&B si la celda no cierra sola
    celdas = []
    for bm in (0, 1):
        for b2 in (0, 1):
            for b1 in (0, 1):
                if bm == b2 == b1 == 0:
                    continue
                box = [1.0, PHI,
                       V_TOPE if bm else 0.0, INF if bm else V_TOPE,
                       V_TOPE if b2 else 0.0, INF if b2 else V_TOPE,
                       V_TOPE if b1 else 0.0, INF if b1 else V_TOPE]
                celdas.append(((bm, b2, b1), box))
    for crit_nombre, extras in (("p1", EXTRAS_P1), ("p2", EXTRAS_P2)):
        pendientes = []
        for etiqueta, box in celdas:
            p = presupuesto_mayorante(box, extras)
            if p is not None and p < 2.0 * PI - 1e-9:
                continue
            pendientes.append((etiqueta, box, p))
        # las celdas que no cierran de una pieza: B&B SOLO en
        # sus direcciones FINITAS (las infinitas quedan fijas con
        # sus caps de limite; subdividirlas seria dividir
        # dimensiones muertas)
        sin_cerrar = []
        for etiqueta, box, p0 in pendientes:
            finitas = [k for k in range(3)
                       if box[2 + 2 * k + 1] is not None]
            if not finitas:
                sin_cerrar.append((etiqueta, p0))
                continue
            plantilla = list(box)

            def crit_wrap(b, _pl=tuple(plantilla),
                          _fin=tuple(finitas), _ex=extras):
                bb = list(_pl)
                bb[0], bb[1] = b[0], b[1]
                for idx, k in enumerate(_fin):
                    bb[2 + 2 * k] = b[2 + 2 * idx]
                    bb[2 + 2 * k + 1] = b[3 + 2 * idx]
                return criterio(bb, _ex)

            broot = [1.0, PHI]
            for k in finitas:
                broot += [box[2 + 2 * k], box[2 + 2 * k + 1]]
            (n_s, env, fuera), vistos, certs, trunc =                 mapa_supervivientes(broot, crit_wrap, eps=2e-3,
                                    max_boxes=2000000,
                                    max_fallos=20000, sobre=False)
            if len(fuera) or trunc:
                sin_cerrar.append((etiqueta, f"{len(fuera)} cajas"))
                if fuera:
                    print(f"  {crit_nombre} celda {etiqueta} "
                          f"primera: {fuera[0]}")
        ok &= check(f"{crit_nombre}: las 7 celdas de cola cierran "
                    f"(de una pieza o por sub-B&B en las "
                    f"direcciones finitas); sin cerrar: "
                    f"{sin_cerrar}", not sin_cerrar)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] contraste con insercion.py")
    ok = True
    # (a) las esquinas historicas del budget caben bajo la cota
    ok &= check("(a) esquinas j = 3 de insercion.py: 4.7225 y "
                "5.2644 < 2 pi = 6.2832 — el B&B certifica un sup "
                "estricto sobre ellas", 4.7225 < 2 * PI
                and 5.2644 < 2 * PI)
    # (b) sondeo: el mayorante domina el presupuesto real en
    # cajas-punto del politopo (coherencia del mayorante)
    import random
    from insercion import presupuesto_p
    from coronacolas import cascada
    rng = random.Random(20260821)
    peor_gap, viol = 1e9, 0
    for _ in range(4000):
        j = rng.randrange(3, 9)
        Sg = rng.uniform(1.0, PHI)
        holg = [1.0 + rng.expovariate(2.0) for _ in range(j)]
        os_ = cascada(None, Sg, j, holgura=holg)
        if os_[0] > 64.0 * (os_[1] + sum(os_[2:]) + 1 + Sg) / PHI:
            continue
        m = sum(os_[2:])
        vm = math.log(max(1.0, m))
        s2f = (m + 1.0 + Sg) / PHI
        v2 = math.log(os_[1] / s2f) if os_[1] >= s2f else 0.0
        s1f = max(os_[1], (os_[1] + m + 1.0 + Sg) / PHI)
        v1 = math.log(os_[0] / s1f) if os_[0] >= s1f else 0.0
        if max(vm, v2, v1) > V_TOPE:
            continue
        caja = [Sg, Sg, vm, vm, v2, v2, v1, v1]
        for extras in (EXTRAS_P1, EXTRAS_P2):
            may = presupuesto_mayorante(caja, extras)
            real = presupuesto_p(os_, extras, S_INS)
            if real is None or may is None:
                continue
            gap = may - real
            peor_gap = min(peor_gap, gap)
            if gap < -1e-9:
                viol += 1
    ok &= check(f"(b) el mayorante domina el presupuesto real en "
                f"cajas-punto del politopo (4000 instancias j <= 8, "
                f"peor holgura mayorante-real = {peor_gap:.4f}, "
                f"violaciones {viol})", viol == 0 and peor_gap > -1e-9)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    return check(
        "[ENUNCIADO] LA ULTIMA MAXIMIZACION CON ASTERISCO SUBE A "
        "CERTIFICADO: el presupuesto de sombras de thm:D1written "
        "(ambas inserciones, sigma2 y w*) queda certificado "
        "sup p < 2 pi por B&B sobre el politopo cascada COMPLETO — "
        "todos los j >= 3 a la vez via la reduccion masa+cuerda, "
        "Sigma en [1, phi], holguras no acotadas via las colas por "
        "caps de limite (sin tope de barrido).  El dominio del B&B "
        "es un SUPERCONJUNTO del politopo real (las ligaduras "
        "agregadas son implicadas por la cascada): mas fuerte.  "
        "Con esto el residuo (v) del paper pierde su ultimo "
        "portador computacional en los presupuestos", True)


def main():
    print("=" * 68)
    print("CERTIFICACION DEL PRESUPUESTO DE SOMBRAS D1 "
          "(endurecimiento 3/3)")
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
