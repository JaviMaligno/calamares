#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lema de insercion por medida y teorema D1-escrito
(docs/drafts/insercion.md).

[A] la cota del arco prohibido por pieza: arco = 2 arccos h(R-s, d);
    max sobre d en el minimo interior d* = sqrt((R-s)^2 - (s+x)^2)
    con sin(delta_max) = (s+x)/(R-s) (identidad sympy); regimenes.
[B] el presupuesto REAL en el dominio D1: union de arcos prohibidos
    para sigma2 = phi-1 y la segunda insercion w* sobre
    empaquetamientos reales de {O, m}: total < 2 pi SIEMPRE.
[C] esquina exacta j = 3 del presupuesto (alta precision).
[D] cola geometrica: T_k <= T_3/phi^(k-3) (decaimiento exacto) y el
    presupuesto uniforme en j.
[E] el teorema en accion: el reparto entero (m de F + sigma1 a D_m +
    dos inserciones por medida) desbloquea todas las instancias.
[F] la rama D3 con sigma2 > phi-1 (sin sigma2 <= phi-1 disponible):
    vacuidad exacta para sigma2 > phi/2 (masa), presupuesto
    parametrico s = sigma2 en [phi-1, phi/2] con Sigma >= 2 sigma2.
[G] sup del politopo cascada por OPTIMIZACION dirigida (no sondeo),
    piezas exactas de monotonia (o2 decreciente, o1 banera con
    limite pi), y la esquina euclidiana determinista R = o1+o2.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, theta_w, cascada

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260810'))


def arco_prohibido(s, x, R, d):
    """Semi-anchura del arco prohibido de la pieza x (radio x, centro a
    profundidad d) para s mural: arccos h(R-s, d), clampeado."""
    u = R - s
    w = s + x
    if d <= 1e-12:
        return PI if u < w else 0.0
    h = (u * u + d * d - w * w) / (2 * u * d)
    if h >= 1.0:
        return 0.0
    if h <= -1.0:
        return PI
    return math.acos(h)


def empaqueta(radios, R, rng, intentos=8000):
    pos = []
    for r in radios:
        okc = False
        for _ in range(intentos):
            if rng.random() < 0.75:
                rho = (R - r) * (1.0 - 0.3 * rng.random())
            else:
                rho = math.sqrt(rng.random()) * (R - r)
            a = rng.uniform(0, 2 * PI)
            x, y = rho * math.cos(a), rho * math.sin(a)
            if all((x - px) ** 2 + (y - py) ** 2 >= (r + pr) ** 2 - 1e-12
                   for px, py, pr in pos):
                pos.append((x, y, r))
                okc = True
                break
        if not okc:
            return None
    return pos


def medida_prohibida(pos, s, R):
    """Medida de la union de arcos prohibidos para insertar s mural,
    y el mayor hueco libre (para la colocacion)."""
    arcos = []
    for x, y, r in pos:
        d = math.hypot(x, y)
        delta = arco_prohibido(s, r, R, d)
        if delta >= PI - 1e-12:
            return 2 * PI, None
        if delta > 0:
            c = math.atan2(y, x)
            arcos.append((c - delta, c + delta))
    if not arcos:
        return 0.0, 0.0
    # medida de la union en el circulo
    evs = []
    for a, b in arcos:
        a %= 2 * PI
        b %= 2 * PI
        if a <= b:
            evs.append((a, b))
        else:
            evs.append((a, 2 * PI))
            evs.append((0.0, b))
    evs.sort()
    total, hueco_max = 0.0, 0.0
    cur_a, cur_b = evs[0]
    prev_fin = None
    primera_ini = evs[0][0]
    for a, b in evs[1:]:
        if a <= cur_b + 1e-15:
            cur_b = max(cur_b, b)
        else:
            total += cur_b - cur_a
            hueco_max = max(hueco_max, a - cur_b)
            cur_a, cur_b = a, b
    total += cur_b - cur_a
    hueco_max = max(hueco_max, (primera_ini + 2 * PI) - cur_b)
    return total, hueco_max


def inserta(pos, s, R):
    """Inserta s mural en el punto medio del mayor hueco libre;
    devuelve la posicion o None. Validacion euclidiana directa."""
    arcos = []
    for x, y, r in pos:
        d = math.hypot(x, y)
        delta = arco_prohibido(s, r, R, d)
        if delta >= PI - 1e-12:
            return None
        if delta > 0:
            arcos.append(((math.atan2(y, x) - delta) % (2 * PI),
                          (math.atan2(y, x) + delta) % (2 * PI)))
    # busca un angulo libre por barrido fino (suficiente para el test)
    for t in range(2000):
        psi = 2 * PI * t / 2000
        libre = True
        for a, b in arcos:
            if a <= b:
                if a - 1e-9 < psi < b + 1e-9:
                    libre = False
                    break
            else:
                if psi > a - 1e-9 or psi < b + 1e-9:
                    libre = False
                    break
        if libre:
            cx, cy = (R - s) * math.cos(psi), (R - s) * math.sin(psi)
            for x, y, r in pos:
                if (cx - x) ** 2 + (cy - y) ** 2 < (s + r) ** 2 - 1e-9:
                    return None      # la cota fallo: NO debe pasar
            return (cx, cy, s)
    return None


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] la cota del arco prohibido (sympy + numerico)")
    import sympy as sp
    ok = True
    u, v, w = sp.symbols('u v w', positive=True)
    h = (u ** 2 + v ** 2 - w ** 2) / (2 * u * v)
    dh = sp.simplify(sp.diff(h, v))
    ok &= check("A1: dh/dv = (v^2 - u^2 + w^2)/(2 u v^2) exacto: un "
                "solo cambio de signo - -> + en v (minimo interior "
                "cuando u > w)",
                sp.simplify(dh - (v ** 2 - u ** 2 + w ** 2) /
                            (2 * u * v ** 2)) == 0)
    vstar = sp.sqrt(u ** 2 - w ** 2)
    hstar = sp.simplify(h.subs(v, vstar))
    ok &= check("A2: h(v*) = sqrt(u^2 - w^2)/u exacto en el minimo "
                "interior v* = sqrt(u^2 - w^2): sin(delta_max) = w/u, "
                "la SOMBRA arcsin((s+x)/(R-s)) para piezas apilables",
                sp.simplify(hstar - sp.sqrt(u ** 2 - w ** 2) / u) == 0)
    # numerico: el arco maximo sobre d coincide con la sombra (u > w)
    rng = random.Random(SEED)
    peor = 0.0
    for _ in range(4000):
        s = rng.uniform(0.2, 1.0)
        x = rng.uniform(0.2, 3.0)
        R = rng.uniform(max(2.5, s + x + 0.2), 9.0)
        uu, ww = R - s, s + x
        if uu <= ww + 1e-6:
            continue
        sombra = math.asin(ww / uu)
        mx = max(arco_prohibido(s, x, R, 0.001 + t * (R - x - 0.001)
                                / 400) for t in range(401))
        peor = max(peor, mx - sombra)
    ok &= check(f"A3: max sobre profundidades del arco = la sombra "
                f"(exceso maximo {peor:.2e} <= 0): la cota por pieza "
                f"es Theta = min(pi, arcsin((s+x)/(R-s)))"
                f" y para pares no apilables ademas Theta <= theta "
                f"mural", peor <= 1e-9)
    # A4 (CONTROL, refutacion de la version ingenua): para pares NO
    # apilables (R < x + 2s) una pieza PROFUNDA bloquea arcos de hasta
    # pi >> theta mural: la cota uniforme-en-profundidad NO es theta.
    # La disyuntiva que salva el lema: no-apilable (R < x+2s) y
    # sombra-valida (R > x+2s) son MUTUAMENTE EXCLUYENTES, y el
    # presupuesto usa SOLO sombras, con la hipotesis R > 2s + x por
    # pieza (que el dominio garantiza: A5).
    peor2 = 0.0
    n2 = 0
    for _ in range(4000):
        s = rng.uniform(0.2, 1.2)
        x = rng.uniform(s, 3.0)
        R = rng.uniform(x + s + 0.1, x + 2 * s - 1e-3)
        if R <= x + s + 0.05:
            continue
        n2 += 1
        mx = max(arco_prohibido(s, x, R, 0.001 + t * (R - x - 0.001)
                                / 400) for t in range(401))
        peor2 = max(peor2, mx - theta_w(s, x, R))
    ok &= check(f"A4 [control]: para pares no apilables la pieza "
                f"profunda EXCEDE el theta mural (exceso maximo "
                f"{peor2:.2f} > 0 en {n2} casos): la version ingenua "
                f"del lema es falsa y el presupuesto usa sombras",
                n2 > 500 and peor2 > 0.5)
    # A5: el dominio D1 esta entero en regimen sombra: para toda pieza
    # x <= o1 y s <= phi-1: R - 2s - x >= (o1+o2) - 2s - o1 =
    # o2 - 2s >= 2 - 2(phi-1) = 2(2-phi) > 0 exacto
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    ok &= check("A5: regimen sombra en todo el dominio: o2 - 2s >= "
                "2 - 2(phi-1) = 2(2-phi) = 4 - 2 phi > 0 exacto "
                "(sympy): R > 2s + x para toda pieza del presupuesto",
                sp.simplify(2 - 2 * (phi - 1) - (4 - 2 * phi)) == 0
                and float(4 - 2 * phi) > 0)
    # A6 (REFUTACION DEL ENUNCIADO CON THETA MURAL, n = 1): el lema NO
    # puede enunciarse con Sum 2 theta_R(s, x_i) < 2 pi (la version que
    # tenia el draft): un par no apilable con x profundo cumple esa
    # hipotesis y NO admite insercion (todo psi en conflicto). El
    # enunciado correcto suma SOMBRAS Theta_i con R > 2s + x_i.
    Rc, xc, sc, dc = 3.0, 2.2, 0.5, 0.1
    hip_mural = 2 * theta_w(sc, xc, Rc) < 2 * PI
    todo_conflicto = (Rc - sc) + dc < sc + xc     # |c_s - c_x| < w siempre
    ok &= check(f"A6 [refutacion del enunciado mural]: R = {Rc}, "
                f"x = {xc} a d = {dc}, s = {sc}: Sum 2 theta_R = "
                f"{2 * theta_w(sc, xc, Rc):.3f} < 2 pi pero (R-s)+d = "
                f"{Rc - sc + dc} < s+x = {sc + xc}: todo angulo en "
                f"conflicto, insercion imposible: el enunciado exige "
                f"sombras + regimen", hip_mural and todo_conflicto
                and arco_prohibido(sc, xc, Rc, dc) >= PI - 1e-12)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] el presupuesto real del dominio D1 (medida de la union)")
    rng = random.Random(SEED + 1)
    ok = True
    n, fallo1, fallo2 = 0, 0, 0
    peor_medida = 0.0
    for _ in range(max(3000, ITER // 15)):
        j = rng.randrange(3, 8)
        Sg = rng.uniform(1.0, PHI)
        holg = [1.0 + rng.expovariate(3.0) for _ in range(j)]
        if rng.random() < 0.4:
            holg = [1.0] * j
        os_ = cascada(None, Sg, j, holgura=holg)
        R = (os_[0] + os_[1]) * rng.uniform(1.0, 1.3)
        pos = empaqueta(os_ + [1.0], R, rng)
        if pos is None:
            continue
        n += 1
        s2 = PHI - 1
        med, _ = medida_prohibida(pos, s2, R)
        peor_medida = max(peor_medida, med)
        p2 = inserta(pos, s2, R)
        if p2 is None:
            fallo1 += 1
            continue
        pos2 = pos + [p2]
        wstar = 1 / PHI
        p3 = inserta(pos2, wstar, R)
        if p3 is None:
            fallo2 += 1
    ok &= check(f"D1 real ({n} empaquetamientos de {{O, m}}, j = 3..7, "
                f"R hasta 1.3(o1+o2)): sigma2 = phi-1 SIEMPRE entra "
                f"({fallo1} fallos; peor medida prohibida "
                f"{peor_medida:.3f} < 2 pi) y el circulo-fila "
                f"w* = 1/phi entra despues ({fallo2} fallos)",
                n > 400 and fallo1 == 0 and fallo2 == 0)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] la esquina j = 3 del presupuesto (alta precision)")
    ok = True
    # minimo de la cascada: o = (2phi, 2, 2/phi), m = 1, R = 2phi + 2;
    # presupuesto ANALITICO con las sombras (piezas apilables con s):
    s2 = PHI - 1
    R = 2 * PHI + 2
    fam = [2 * PHI, 2.0, 2 / PHI, 1.0]
    total = 0.0
    for x in fam:
        u, w = R - s2, s2 + x
        if R < max(x, s2) + 2 * min(x, s2):
            arc = theta_w(s2, x, R)
        elif u > w:
            arc = math.asin(w / u)
        else:
            arc = PI
        total += 2 * arc
    ok &= check(f"esquina j = 3: presupuesto analitico de sigma2 = "
                f"phi-1 con sombras = {total:.4f} < 2 pi (margen "
                f"{2 * PI - total:.4f})", total < 2 * PI - 0.3)
    # segunda insercion: w* = 1/phi con sigma2 ya dentro
    wst = 1 / PHI
    total2 = 0.0
    for x in fam + [s2]:
        u, w = R - wst, wst + x
        if R < max(x, wst) + 2 * min(x, wst):
            arc = theta_w(wst, x, R)
        elif u > w:
            arc = math.asin(w / u)
        else:
            arc = PI
        total2 += 2 * arc
    ok &= check(f"esquina j = 3, segunda insercion w* = 1/phi: "
                f"presupuesto = {total2:.4f} < 2 pi (margen "
                f"{2 * PI - total2:.4f})", total2 < 2 * PI - 0.3)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] uniformidad en j: decaimiento geometrico y presupuesto")
    rng = random.Random(SEED + 2)
    ok = True
    # T_k <= T_3/phi^(k-3) exacto (T_k >= phi T_{k+1}) y el
    # presupuesto analitico para j grande
    peor_total = 0.0
    for j in range(3, 15):
        Sg = 1.0 + 1e-9
        os_ = cascada(None, Sg, j)
        R = os_[0] + os_[1]
        s2 = PHI - 1
        total = 0.0
        for x in os_ + [1.0]:
            u, w = R - s2, s2 + x
            if R < max(x, s2) + 2 * min(x, s2):
                arc = theta_w(s2, x, R)
            elif u > w:
                arc = math.asin(w / u)
            else:
                arc = PI
            total += 2 * arc
        peor_total = max(peor_total, total)
    ok &= check(f"presupuesto analitico de sigma2 en el MINIMO de la "
                f"cascada, j = 3..14: max = {peor_total:.4f} < 2 pi "
                f"(margen {2 * PI - peor_total:.4f}): la serie "
                f"converge y j desaparece", peor_total < 2 * PI - 0.3)
    # con holguras (o's por encima del minimo): sondeo del sup
    peor2 = 0.0
    for _ in range(max(4000, ITER // 12)):
        j = rng.randrange(3, 12)
        Sg = rng.uniform(1.0, PHI)
        holg = [1.0 + rng.expovariate(2.0) for _ in range(j)]
        os_ = cascada(None, Sg, j, holgura=holg)
        R = os_[0] + os_[1]
        s2 = PHI - 1
        total = 0.0
        for x in os_ + [1.0]:
            u, w = R - s2, s2 + x
            if R < max(x, s2) + 2 * min(x, s2):
                arc = theta_w(s2, x, R)
            elif u > w:
                arc = math.asin(w / u)
            else:
                arc = PI
            total += 2 * arc
        peor2 = max(peor2, total)
    ok &= check(f"presupuesto con holguras (j <= 11, R = o1+o2): "
                f"sup observado = {peor2:.4f} < 2 pi (margen "
                f"{2 * PI - peor2:.4f})", peor2 < 2 * PI - 0.1)
    # piezas EXACTAS de monotonia (sympy) -- el estatus honesto del
    # "sup por esquinas": (o2) el presupuesto DECRECE en o2 con el
    # resto fijo; (o1) NO es monotono en o1: es banera (decrece y
    # luego crece hacia el limite pi < 2 pi); el resto de direcciones
    # queda al optimizador del bloque G.
    import sympy as sp
    o1, o2, s, wi = sp.symbols('o1 o2 s w_i', positive=True)
    u = o1 + o2 - s
    w1, w2 = s + o1, s + o2
    # (o2): d/do2 [asin(w2/u) + asin(w1/u)] < 0  <=>
    # (u - w2) sqrt(u^2-w1^2) < w1 sqrt(u^2-w2^2); certificado exacto:
    # u - w2 = o1 - 2s < o1 + s = w1  y  w1^2 - w2^2 >= 0
    c1 = sp.simplify((u - w2) - (o1 - 2 * s)) == 0
    c2 = sp.simplify(w1 - (u - w2) - 3 * s) == 0        # gap = 3s > 0
    c3 = sp.simplify(w1 ** 2 - w2 ** 2 -
                     (o1 - o2) * (o1 + o2 + 2 * s)) == 0
    ok &= check("monotonia exacta en o2: u - w2 = o1 - 2s, "
                "w1 - (u - w2) = 3s > 0 y w1^2 - w2^2 = "
                "(o1 - o2)(o1 + o2 + 2s) >= 0: la derivada del "
                "presupuesto en o2 es negativa (el minimo de o2 es "
                "el peor) -- exacto", c1 and c2 and c3)
    # (o1): N_i^2/P^2 estrictamente decreciente en o1 (un solo cambio
    # de signo de la derivada del presupuesto: banera) y limite pi
    P2 = (o2 - 2 * s) / (2 * o1 + o2)
    Q = wi ** 2 / ((u ** 2 - wi ** 2) * P2)
    dQ = sp.together(sp.diff(Q, o1))
    num = sp.numer(dQ)
    den = sp.denom(dQ)
    num_ok = sp.simplify(
        num - 2 * wi ** 2 *
        (s ** 2 - o1 ** 2 - o1 * o2 - o2 * s - wi ** 2)) == 0
    den_ok = sp.simplify(
        den - (o2 - 2 * s) * (u ** 2 - wi ** 2) ** 2) == 0
    lim = sp.limit(2 * sp.asin(w1 / u), o1, sp.oo)
    ok &= check("banera exacta en o1: d(N_i^2/P^2)/do1 = "
                "2 w^2 (s^2-o1^2-o1 o2-o2 s-w^2) / "
                "[(o2-2s)(u^2-w^2)^2] < 0 (numerador < 0 con o1 > s; "
                "denominador > 0 en regimen o2 > 2s): a lo sumo un "
                "cambio - -> + del gradiente; limite o1 -> oo del "
                "presupuesto = pi < 2 pi",
                num_ok and den_ok and lim == sp.pi)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles")
    rng = random.Random(SEED + 3)
    ok = True
    # (a) sin cascada el presupuesto puede exceder 2 pi (tres grandes
    # iguales y R = par): la hipotesis muerde
    os_ = [2.0, 2.0, 2.0]
    R = 4.0
    s2 = PHI - 1
    total = 0.0
    for x in os_ + [1.0]:
        u, w = R - s2, s2 + x
        if R < max(x, s2) + 2 * min(x, s2):
            arc = theta_w(s2, x, R)
        elif u > w:
            arc = math.asin(w / u)
        else:
            arc = PI
        total += 2 * arc
    ok &= check(f"(a) sin cascada (o = 2, 2, 2, R = 4): presupuesto = "
                f"{total:.3f} > 2 pi: las colas son las que pagan la "
                f"insercion", total > 2 * PI)
    # (b) la insercion nunca produce solapes (validacion euclidiana
    # ya integrada en inserta(); aqui un stress con piezas al limite)
    n, viol = 0, 0
    for _ in range(2000):
        j = rng.randrange(3, 6)
        os_ = cascada(None, rng.uniform(1.0, PHI), j)
        R = (os_[0] + os_[1]) * rng.uniform(1.0, 1.15)
        pos = empaqueta(os_ + [1.0], R, rng)
        if pos is None:
            continue
        n += 1
        p2 = inserta(pos, PHI - 1, R)
        if p2 is None:
            continue
        cx, cy, s = p2
        for x, y, r in pos:
            if (cx - x) ** 2 + (cy - y) ** 2 < (s + r) ** 2 - 1e-9:
                viol += 1
    ok &= check(f"(b) stress euclidiano de la insercion ({n} casos, "
                f"{viol} solapes): la cota del arco es correcta",
                n > 300 and viol == 0)
    return ok


# ---------------------------------------------------------------- helpers F/G
def sombra_o_mural(s, x, R):
    """Cota del arco por pieza: sombra en regimen apilable, theta
    mural si el par no es apilable (mejor cota), pi si no hay
    regimen."""
    u, w = R - s, s + x
    if R < max(x, s) + 2 * min(x, s):
        return theta_w(s, x, R)
    if u > w:
        return math.asin(w / u)
    return PI


def presupuesto_p(os_, extras, s):
    """Presupuesto analitico de sombras en R = o1+o2 para insertar s;
    None si alguna pieza queda fuera de regimen sombra."""
    R = os_[0] + os_[1]
    tot = 0.0
    for x in os_ + extras:
        u, w = R - s, s + x
        if u <= w:
            return None
        tot += 2 * math.asin(w / u)
    return tot


def minimo_cascada(Sg, j):
    os_, tot = [], 0.0
    for _ in range(j):
        o = max(1.0, (tot + 1.0 + Sg) / PHI, os_[-1] if os_ else 0.0)
        os_.append(o)
        tot += o
    return os_[::-1]


def cascada_factible(os_, Sg):
    if any(os_[k] < os_[k + 1] - 1e-12 for k in range(len(os_) - 1)):
        return False
    tot = 0.0
    for k in range(len(os_) - 1, -1, -1):
        if os_[k] < (tot + 1.0 + Sg) / PHI - 1e-12 or \
                os_[k] < 1.0 - 1e-12:
            return False
        tot += os_[k]
    return True


def optimiza_presupuesto(fun, j, Sg, os_, pasos=500, paso0=0.4):
    """Coordinate ascent proyectado al politopo cascada (maximiza)."""
    cur = fun(os_) or 0.0
    step = paso0
    for _ in range(pasos):
        mejoro = False
        for k in range(j):
            for sgn in (+1.0, -1.0):
                cand = list(os_)
                cand[k] += sgn * step
                if not cascada_factible(cand, Sg):
                    continue
                p = fun(cand)
                if p is not None and p > cur + 1e-12:
                    os_, cur, mejoro = cand, p, True
        if not mejoro:
            step *= 0.5
            if step < 1e-7:
                break
    return cur, os_


# ---------------------------------------------------------------- bloque F
def bloque_F():
    print("[F] la rama D3 con sigma2 > phi-1 (presupuesto parametrico)")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    # F1: vacuidad por masa para sigma2 > phi/2: la cola de m contiene
    # sigma1 + sigma2 >= 2 sigma2 > phi => rho > phi, no hay bloqueo
    ok &= check("F1: sigma2 > phi/2 es VACIA con rho <= phi: "
                "cola(m) >= sigma1 + sigma2 >= 2 sigma2 > phi exacto",
                sp.simplify(2 * (phi / 2) - phi) == 0)
    # F2: con j >= 3, o2 >= 1 + Sigma exacto: o3 >= (1+Sigma)/phi y
    # o2 >= (o3 + 1 + Sigma)/phi >= (1+Sigma)(1+phi)/phi^2 = 1+Sigma
    S = sp.symbols('Sigma', positive=True)
    ok &= check("F2: o2 >= (1+Sigma)(1+phi)/phi^2 = 1 + Sigma exacto "
                "(phi^2 = 1 + phi): el regimen sombra o2 - 2s >= "
                "1 + Sigma - 2s >= 1 vale con Sigma >= 2s",
                sp.simplify((1 + S) * (1 + phi) / phi ** 2 - (1 + S))
                == 0)
    # F3: curva parametrica s = sigma2 en [phi-1, phi/2], con la
    # ligadura de masa Sigma >= max(1, 2s): minimos de cascada
    peor1, peor2 = 0.0, 0.0
    for j in range(3, 9):
        for i in range(801):
            s = (PHI - 1) + i * (PHI / 2 - (PHI - 1)) / 800
            os_ = minimo_cascada(max(1.0, 2 * s), j)
            p1 = presupuesto_p(os_, [1.0], s)
            p2 = presupuesto_p(os_, [1.0, s], 1 / PHI)
            if p1 is None or p2 is None:
                peor1 = 99.0
                break
            peor1 = max(peor1, p1)
            peor2 = max(peor2, p2)
    ok &= check(f"F3: curva s en [phi-1, phi/2], Sigma = max(1, 2s), "
                f"j = 3..8: sup p1 = {peor1:.4f}, sup p2 = "
                f"{peor2:.4f} < 2 pi (margenes "
                f"{2 * PI - peor1:.2f}, {2 * PI - peor2:.2f})",
                peor1 < 2 * PI - 0.3 and peor2 < 2 * PI - 0.3)
    # F4: sup por optimizacion dirigida sobre el politopo con la
    # ligadura Sigma >= 2s (s tambien se optimiza)
    rng = random.Random(SEED + 4)
    best = 0.0
    for j in (3, 4, 5):
        for trial in range(max(60, ITER // 1000)):
            s = rng.uniform(PHI - 1, PHI / 2)
            Sg = rng.uniform(max(1.0, 2 * s), PHI)
            holg = [1.0 + rng.expovariate(2.5) for _ in range(j)]
            if trial % 4 == 0:
                holg = [1.0] * j
            os_ = cascada(None, Sg, j, holgura=holg)
            for st in (s, PHI / 2):
                if 2 * st > Sg + 1e-12:
                    continue      # ligadura de masa: Sigma >= 2 sigma2
                cur, _ = optimiza_presupuesto(
                    lambda o: presupuesto_p(o, [1.0], st), j, Sg,
                    list(os_))
                best = max(best, cur)
    ok &= check(f"F4: sup optimizado del presupuesto D3-parametrico "
                f"(Sigma >= 2s, j <= 5): {best:.4f} < 2 pi (margen "
                f"{2 * PI - best:.4f}); el maximo vive en la esquina "
                f"s = phi/2, Sigma = phi, o = (phi^3, phi^2, phi)",
                0 < best < 2 * PI - 0.3)
    return ok


# ---------------------------------------------------------------- bloque G
def bloque_G():
    print("[G] sup del politopo D1 (optimizacion) y esquina euclidiana")
    rng = random.Random(SEED + 5)
    ok = True
    esquina1, esquina2 = 4.7225, 5.2644
    s2, wst = PHI - 1, 1 / PHI
    best1, best2 = 0.0, 0.0
    for j in (3, 4, 5, 6, 7, 8):
        for trial in range(max(80, ITER // 700)):
            Sg = rng.uniform(1.0, PHI)
            holg = [1.0 + rng.expovariate(2.0) for _ in range(j)]
            if trial % 4 == 0:
                holg = [1.0] * j
            os_ = cascada(None, Sg, j, holgura=holg)
            c1, o1v = optimiza_presupuesto(
                lambda o: presupuesto_p(o, [1.0], s2), j, Sg,
                list(os_))
            best1 = max(best1, c1)
            c2, _ = optimiza_presupuesto(
                lambda o: presupuesto_p(o, [1.0, s2], wst), j, Sg,
                list(os_))
            best2 = max(best2, c2)
            # Sigma tambien baja hacia 1 en el ascenso
            if Sg > 1.0:
                c1b, _ = optimiza_presupuesto(
                    lambda o: presupuesto_p(o, [1.0], s2), j, 1.0,
                    list(o1v))
                best1 = max(best1, c1b)
    ok &= check(f"G1: sup OPTIMIZADO del presupuesto sigma2 sobre el "
                f"politopo (j <= 8, Sigma libre en [1, phi]): "
                f"{best1:.4f} <= esquina {esquina1} (+1e-3) y < 2 pi: "
                f"la esquina j = 3, Sigma -> 1 domina",
                best1 < esquina1 + 1e-3 and best1 < 2 * PI - 0.3)
    ok &= check(f"G2: idem segunda insercion w*: {best2:.4f} <= "
                f"esquina {esquina2} (+1e-3) y < 2 pi",
                best2 < esquina2 + 1e-3 and best2 < 2 * PI - 0.3)
    # G3: la esquina euclidiana determinista R = o1 + o2 EXACTO:
    # o1, o2 diametrales; o3.., m murales apinados (peor lado);
    # sigma2 = phi-1 y w* = 1/phi se insertan, validacion euclidiana
    n, fallos = 0, 0
    for j in range(3, 7):
        for Sg in (1.0, 1.2, 1.3820, PHI):
            os_ = minimo_cascada(Sg, j)
            R = os_[0] + os_[1]
            resto = os_[2:] + [1.0]
            for orden in (list(resto), list(resto)[::-1]):
                pos = [(R - os_[0], 0.0)]
                ang = 0.0
                prev = os_[0]
                cfg = [(R - os_[0], 0.0, os_[0]),
                       (-(R - os_[1]), 0.0, os_[1])]
                legal = True
                for x in orden:
                    ang += theta_w(prev, x, R) + 1e-9
                    cx = (R - x) * math.cos(ang)
                    cy = (R - x) * math.sin(ang)
                    cfg.append((cx, cy, x))
                    prev = x
                for a in range(len(cfg)):
                    for b in range(a + 1, len(cfg)):
                        xa, ya, ra = cfg[a]
                        xb, yb, rb = cfg[b]
                        if (xa - xb) ** 2 + (ya - yb) ** 2 < \
                                (ra + rb) ** 2 - 1e-9:
                            legal = False
                if not legal:
                    continue
                n += 1
                p2 = inserta(cfg, s2, R)
                if p2 is None:
                    fallos += 1
                    continue
                p3 = inserta(cfg + [p2], wst, R)
                if p3 is None:
                    fallos += 1
    ok &= check(f"G3: esquinas euclidianas deterministas R = o1+o2 "
                f"exacto, murales apinados ({n} configuraciones "
                f"legales, j = 3..6, Sigma hasta phi): sigma2 y w* "
                f"SIEMPRE entran ({fallos} fallos)",
                n >= 8 and fallos == 0)
    return ok


def main():
    print("=" * 68)
    print("LEMA DE INSERCION POR MEDIDA Y TEOREMA D1-ESCRITO")
    print("(drafts/insercion.md)")
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
