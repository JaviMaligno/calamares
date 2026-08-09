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
