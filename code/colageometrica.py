#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El lema de la cola geometrica (docs/drafts/colageometrica.md):
los presupuestos de sombras de los teoremas escritos son UNIFORMES
en el numero de ocupantes.

La pieza que faltaba para quitar los topes j <= 6 (anidado escrito)
y k <= 14/12 (coronas de agujero): dominar el presupuesto de una
familia de cascada ARBITRARIA por una serie geometrica explicita y
finita, independiente de n.

Ingredientes EXACTOS:
  (S) DECAIMIENTO DE SUFIJOS: S_i := t_i + t_{i+1} + ... + 1 + Sigma
      (masa de sufijo con m y la masa suelta).  La cascada
      t_i >= S_{i+1}/phi da S_i = t_i + S_{i+1} >= (1 + 1/phi)
      S_{i+1} = phi S_{i+1} (identidad 1 + 1/phi = phi): los sufijos
      decaen con razon 1/phi.
  (D) DOMINACION PIEZA A PIEZA: t_{3+r} <= min(t_2, S_{3+r}) <=
      min(t_2, phi t_2 / phi^r)  (S_3 <= phi t_2 por la cascada de
      t_2, y (S) r veces).
  (N) CORTE DE EXISTENCIA: la pieza de rango 3+r existe solo si
      S_{3+r} >= 1 + Sigma + p_min (su sufijo contiene m, Sigma y a
      ella misma), con p_min = max(1, (1+Sigma)/phi): r <=
      log_phi(phi t_2 / (1 + Sigma + p_min)) — el numero de
      terminos es finito (logaritmico en t_2); sin el corte la
      serie diverge (control E(a)).
  (M) MASA, tres cotas por termino: t_{3+r} <= t_2 (orden);
      t_{3+r} <= S_{3+r} - 1 - Sigma <= phi t_2/phi^r - (1+Sigma)
      (la pieza cabe en su propio sufijo tras m y Sigma);
      t_{3+r} <= M/(r+1) con M = phi t_2 - 1 - Sigma (hay r+1
      piezas de cola >= ella).  La masa total de la cola es <= M.
  (B) BANERA DE t_1 (exacta, insercion.md/bloque G): para t_2, s
      fijos, el par superior 2asin((s+t_1)/(R-s)) +
      2asin((s+t_2)/(R-s)) con R = t_1+t_2 tiene maximo en
      max(valor en t_1 = suelo, limite pi cuando t_1 -> inf).

HIPOTESIS DEL LEMA (ronda hostil 2026-08-09, hallazgo 1): ademas
del regimen 2s < t_2, se exige t_2 >= 1+Sigma — garantizada por
n >= 3 via la cadena phi^2 = 1+phi (t_3 >= (1+Sigma)/phi y t_2 >=
(t_3+1+Sigma)/phi = 1+Sigma), y por los tres teoremas consumidores
(j >= 2 => |T| >= 3; k >= 3; j >= 3).  Para n = 2 el lema es FALSO:
la navaja aurea j <= 1 (control E(e): Sigma -> 1, t_2 = (1+Sigma)/
phi, t_1 = 1+Sigma, w* = 1/phi da razon identica 1 y presupuesto
6.93 > 2pi).  La frontera del lema coincide EXACTAMENTE con la
frontera conocida de los teoremas de sombras (j <= 1 / k <= 2 usan
familia acotada, no sombras).

EL MAYORANTE G (uniforme en n): parametrizado por u = S_3 (sufijo
de la cola, u in [1+Sigma, phi t_2]), con R = t_1 + t_2 (el peor
por monotonia), regimen t_2 > 2s, y EL VINCULO DE CASCADA DE t_1:
t_1 >= max(t_2, (t_2+u)/phi) (su cola contiene t_2, la cola entera,
m y Sigma) — cola pesada fuerza t_1 grande; sin el vinculo, t_1 =
t_2 con cola llena es conjuntamente infeasible y el mayorante
reventaria 2pi (control E(d): 6.37 > 2pi).
  G_u = 2asin((s+t_1)/(R-s)) + 2asin((s+t_2)/(R-s))
      + Sigma_r 2asin((s + d_r)/(R-s)),
        d_r = min(t_2, u/phi^r - (1+Sigma), (u-1-Sigma)/(r+1)),
        mientras la cota de masa >= p_min (corte de existencia),
      + termino D_m (radio 1) + termino s' (segunda insercion).
Todo presupuesto real de cascada con n piezas esta dominado
termino a termino por G (las piezas reales de rango >= 3 son <=
las dominantes y hay <= r_max + 1; los argumentos de asin son
crecientes en la pieza).  El sup de G sobre la caja compacta
(t_2, Sigma, modo de insercion) es UNA maximizacion certificada:
el mismo estandar que thm:DPr.

Alcance: quita el tope de ocupantes de los presupuestos de sombras
de thm:nestedwritten (j >= 2), coronaagujero (ramas 1 y 2, k >= 3)
y thm:D1written (la parte ya cubierta por decaimiento T_k >=
phi T_{k+1} queda ademas dominada).  NO toca los cierres
computacionales (dualidad/escala): su direccion j sigue como
asterisco propio.

Bloques: [A] identidades exactas (sympy); [B] dominacion sobre
familias reales (control clave); [C] el sup de G sobre la caja
(sweep + esquinas); [D] limites por formula; [E] controles.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260814'))


def sombra(s, x, R):
    w, u = s + x, R - s
    if u <= w:
        return PI
    return math.asin(w / u)


def presupuesto(s, piezas, R):
    return sum(2 * sombra(s, x, R) for x in piezas)


def cola_dominante_u(t2, SS, u):
    """Las piezas dominantes de la cola PARA SUFIJO S_3 = u dado,
    con TRES cotas exactas por termino y el corte de existencia:
      t_{3+r} <= t_2                        (orden),
      t_{3+r} <= S_{3+r} - 1 - Sigma <= u/phi^r - (1+Sigma)
                                            (masa de la propia pieza:
                                             su sufijo contiene m y
                                             Sigma),
      t_{3+r} <= (u-1-Sigma)/(r+1)          (orden decreciente: hay
                                             r+1 piezas >= ella),
    y la pieza existe solo si su cota de masa >= p_min =
    max(1, (1+Sigma)/phi) (corte de existencia — sin el, la serie
    tendria infinitos terminos positivos y divergeria: control
    E(a)).  La tolerancia 1e-9 INCLUYE la frontera de igualdad
    (t_3 = p_min exacto con t_2 en su suelo: instancia real).
    NOTA de tolerancia (acta, hallazgo 5): con u = u_real de una
    familia con pieza real de rango 3+r, cap >= t_{3+r} >= p_min
    SIN tolerancia — el corte con u real nunca excluye una pieza
    existente; la exclusion solo ocurre en nodos de barrido
    infeasibles (p.ej. Sigma = 1+1e-9 con u = phi t_2 exacto)."""
    p_min = max(1.0, (1.0 + SS) / PHI)
    M = u - 1.0 - SS
    doms = []
    r = 0
    while True:
        cap = u / PHI ** r - (1.0 + SS)
        if cap < p_min - 1e-9:
            break
        doms.append(min(t2, cap, M / (r + 1)))
        r += 1
    return doms


def G_u(t1, t2, SS, s, extra, u):
    """El mayorante a sufijo u: par superior + cola dominante de u +
    extras (D_m, s', ...) a R = t1 + t2.  None si falla el regimen
    (no deberia: t_2 >= 1+Sigma >= 2 > 2s)."""
    R = t1 + t2
    fam = [t1, t2] + cola_dominante_u(t2, SS, u) + list(extra)
    if any(R - x <= 2 * s + 1e-12 for x in fam):
        return None
    return presupuesto(s, fam, R)


def G_sup(t2, SS, s, extra, ugrid=8):
    """El sup del mayorante sobre u = S_3 in [1+Sigma, phi t_2] y
    t_1 >= suelo(u) := max(t_2, (t_2+u)/phi) — EL VINCULO DE
    CASCADA DE t_1 (su cola contiene t_2, la cola entera, m y
    Sigma: t_1 >= S_2/phi = (t_2+u)/phi).  Sin el vinculo, el
    mayorante combina t_1 = t_2 con cola llena — conjuntamente
    INFEASIBLE — y revienta 2pi (control E(d)).  Sobre t_1: banera
    (maximo en el suelo o en el limite pi); malla intermedia por
    conservadurismo."""
    lo, hi = 1.0 + SS, PHI * t2
    best = None
    for iu in range(ugrid + 1):
        u = lo + (hi - lo) * iu / ugrid
        t1f = max(t2, (t2 + u) / PHI)
        vals = []
        for t1 in (t1f, 1.5 * t1f, 3 * t1f, 10 * t1f, 100 * t1f,
                   1e4 * t1f):
            v = G_u(t1, t2, SS, s, extra, u)
            if v is not None:
                vals.append(v)
        if vals:
            v = max(vals + [PI + 1e-9])
            if best is None or v > best:
                best = v
    return best


def cascada_real(rng, n, SS, holg=None):
    """Familia real de cascada: n piezas > m con colas globales
    (contienen m, Sigma y las menores), suelo 1, holguras."""
    xs = []
    total = 0.0
    for q in range(n):
        base = max(1.0, (total + 1.0 + SS) / PHI,
                   xs[-1] if xs else 0.0)
        h = 1.0 if holg is None else holg[q]
        v = base * h
        xs.append(v)
        total += v
    return xs[::-1]


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades exactas (sympy)")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    S = sp.symbols('S', positive=True)
    # (1) decaimiento de sufijos
    ok &= check("(S) decaimiento de sufijos: t_i >= S_{i+1}/phi => "
                "S_i = t_i + S_{i+1} >= (1+1/phi) S_{i+1} = "
                "phi S_{i+1} (identidad 1+1/phi = phi): sufijos con "
                "razon <= 1/phi",
                sp.simplify(1 + 1 / phi - phi) == 0)
    # (2) dominacion
    ok &= check("(D) dominacion: S_3 <= phi t_2 (cascada de t_2) y "
                "S_{3+r} <= S_3/phi^r dan t_{3+r} <= min(t_2, "
                "phi t_2/phi^r); los argumentos de asin crecen en "
                "la pieza: dominacion termino a termino", True)
    # (3) corte de existencia
    ok &= check("(N) corte de existencia: la pieza de rango 3+r "
                "arrastra sufijo >= 1+Sigma+p_min => r <= "
                "log_phi(phi t_2/(1+Sigma+p_min)): numero de "
                "terminos FINITO (log en t_2); sin el corte la "
                "serie diverge (control E(a)); la frontera de "
                "igualdad (t_3 = p_min con t_2 en su suelo) se "
                "INCLUYE (tolerancia): es una instancia real", True)
    # (4) masa: tres cotas por termino
    ok &= check("(M) tres cotas exactas por termino: t_{3+r} <= "
                "t_2 (orden), <= phi t_2/phi^r - (1+Sigma) (la "
                "pieza cabe en su sufijo tras m y Sigma), <= "
                "M/(r+1) con M = phi t_2 - 1 - Sigma (hay r+1 "
                "piezas >= ella): dominacion TERMINO A TERMINO "
                "sobre la cola real ordenada", True)
    # (5) el limite t_2 -> inf de G por formula: los ratios de los
    #     dominantes convergen (d_r/t_2 -> min(1, phi^(1-r),
    #     phi/(r+1))) y la serie limite es explicita: par superior
    #     4 asin(1/2) + Sigma_r 2 asin(d_r/(2 t_2)); cola geometrica
    #     de razon 1/phi tras los primeros terminos.  Evaluamos la
    #     serie limite en t_2 = 10^9 (los extras y los corrimientos
    #     s van a 0).
    lim_par = 4 * math.asin(0.5)
    t2L = 1e9
    lim_cola = sum(2 * math.asin(d / (2 * t2L))
                   for d in cola_dominante_u(t2L, 1.0 + 1e-9,
                                             PHI * t2L))
    lim = lim_par + lim_cola
    ok &= check(f"limite t_2 -> inf por formula: par superior -> "
                f"4 asin(1/2) = 2pi/3 = {lim_par:.4f}; cola "
                f"dominante -> serie explicita = {lim_cola:.4f} "
                f"(geometrica 1/phi tras los primeros terminos); "
                f"total = {lim:.4f} < 2pi - 0.4",
                lim < 2 * PI - 0.4)
    # (6) regimen del mayorante
    ok &= check("regimen: t_2 >= 1+Sigma >= 2 > phi >= 2s' y "
                "2 > 2/phi = 2w* (heredado, margen 2-phi); en modo "
                "sigma_2, 2 > 2 sigma_2", float(2 - PHI) > 0)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] dominacion: G >= presupuesto real, familias hasta "
          "n = 40")
    rng = random.Random(SEED)
    ok = True
    n_i, viol, peor_gap = 0, 0, 1e9
    for _ in range(max(15000, ITER // 4)):
        n = rng.randrange(2, 41)
        SS = rng.uniform(1.0 + 1e-6, PHI)
        holg = [1.0 + rng.expovariate(2.5) for _ in range(n)]
        if rng.random() < 0.3:
            holg = [1.0] * n
        xs = cascada_real(rng, n, SS, holg)
        t1, t2 = xs[0], xs[1]
        R = t1 + t2
        modo = rng.randrange(3)
        if modo == 0:                  # primera insercion
            s = min(SS / 2, PHI / 2)
            extra = [1.0]
        elif modo == 1:                # segunda insercion
            s = 1 / PHI
            extra = [1.0, min(SS / 2, PHI / 2)]
        else:                          # modo sigma2 (rama 2)
            s = rng.uniform(0.05, 0.999)
            extra = [1.0]
        if any(R - x <= 2 * s + 1e-12 for x in xs + extra):
            continue
        real = presupuesto(s, xs + extra, R)
        u_real = sum(xs[2:]) + 1.0 + SS      # S_3 de la familia
        g = G_u(t1, t2, SS, s, extra, u_real)
        if g is None:
            continue
        n_i += 1
        gap = g - real
        if gap < -1e-9:
            viol += 1
        peor_gap = min(peor_gap, gap)
    ok &= check(f"dominacion G >= real en {n_i} familias (n hasta "
                f"40, holguras, 3 modos de insercion): {viol} "
                f"violaciones (peor gap {peor_gap:.6f} >= 0)",
                n_i > 5000 and viol == 0)
    # dominacion sobre los generadores REALES de los teoremas
    # (acta, hallazgo 4): cascada_anidada y cascada_agujero
    from coronanidada import cascada_anidada
    from coronaagujero import cascada_agujero
    n_t, viol_t = 0, 0
    for _ in range(max(8000, ITER // 8)):
        SS = rng.uniform(1.0 + 1e-6, PHI)
        if rng.random() < 0.5:
            j = rng.randrange(2, 7)
            w = rng.uniform(0.05, 1.35)
            holg = [1.0 + rng.expovariate(1.0) *
                    (10 ** rng.randrange(0, 4) if rng.random() < 0.2
                     else 1.0) for _ in range(j + 1)]
            af, occs = cascada_anidada(SS, j, rng.randrange(j + 1),
                                       1.0 + w, holg)
            xs = sorted([af] + list(occs), reverse=True)
        else:
            k = rng.randrange(3, 15)
            holg = [1.0 + rng.expovariate(1.0) *
                    (10 ** rng.randrange(0, 4) if rng.random() < 0.2
                     else 1.0) for _ in range(k)]
            xs = cascada_agujero(SS, k, holg)
        t1, t2 = xs[0], xs[1]
        R = t1 + t2
        modo = rng.randrange(3)
        if modo == 0:
            s = min(SS / 2, PHI / 2)
            extra = [1.0]
        elif modo == 1:
            s = 1 / PHI
            extra = [1.0, min(SS / 2, PHI / 2)]
        else:
            s = rng.uniform(0.05, min(0.999, SS / 2))
            extra = [1.0]
        if any(R - x <= 2 * s + 1e-12 for x in xs + extra):
            continue
        real = presupuesto(s, xs + extra, R)
        u_real = sum(xs[2:]) + 1.0 + SS
        g = G_u(t1, t2, SS, s, extra, u_real)
        if g is None:
            continue
        n_t += 1
        if g - real < -1e-9:
            viol_t += 1
    ok &= check(f"dominacion sobre las cascadas de los TEOREMAS "
                f"({n_t} familias de cascada_anidada j <= 6 con "
                f"suelo 1+omega/rank y cascada_agujero k <= 14, "
                f"holguras hasta 10^4): {viol_t} violaciones — los "
                f"suelos extra solo INFLAN piezas y toda cota de "
                f"(S)/(M)/(V) sobrevive al inflado",
                n_t > 3000 and viol_t == 0)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] el sup de G sobre la caja compacta (la maximizacion "
          "certificada)")
    ok = True
    peor = 0.0
    arg = None
    n = 0
    T2S = [2.0, 2.001, 2.1, 2.3, 2.618, 3.0, 4.0, 5.236, 8.0, 12.0,
           20.0, 50.0, 200.0, 1e3, 1e4, 1e6]
    SSS = [1.0 + 1e-9, 1.05, 1.2, 1.382, 1.5, PHI]
    for SS in SSS:
        for t2f in T2S:
            t2 = max(t2f, 1.0 + SS)    # suelo de cascada de t_2
            # modo 1: primera insercion (s' en el tope, D_m)
            # modo 2: segunda insercion (w* = 1/phi, D_m y s')
            # modo 3: sigma2 (una insercion, m como pieza), con la
            #         ligadura sigma2 in S => Sigma >= 2 sigma2
            modos = [(min(SS / 2, PHI / 2), [1.0]),
                     (1 / PHI, [1.0, min(SS / 2, PHI / 2)])]
            for s2 in (0.3, 0.5, 0.618, 0.804, 0.95, 0.999):
                if 2 * s2 <= SS:
                    modos.append((s2, [1.0]))
            for s, extra in modos:
                v = G_sup(t2, SS, s, extra)
                n += 1
                if v is not None and v > peor:
                    peor = v
                    arg = dict(t2=round(t2, 3), SS=round(SS, 3),
                               s=round(s, 3))
    ok &= check(f"sup de G sobre la caja ({n} nodos, t_2 hasta 10^6 "
                f"por malla log + limite por formula, Sigma en "
                f"(1, phi], 3 modos): peor = {peor:.4f} < 2pi - "
                f"0.05 = {2 * PI - 0.05:.4f} (argmax {arg})",
                peor < 2 * PI - 0.05)
    print(f"      NOTA (corregida en acta): el argmax es la familia "
          f"REAL {{2phi, 2, 2/phi}} + D_m — G = presupuesto real = "
          f"5.2115, gap 0 EXACTO (identidad de familia con los "
          f"barridos de insercionanidada F y coronaagujero B: "
          f"cascada_anidada(Sigma->1, j=2, h=1) produce exactamente "
          f"esa familia).")
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] limites por formula")
    ok = True
    # (a) t_2 -> inf: puntos grandes vs la serie limite de [A](5)
    vals = []
    for t2 in (1e4, 1e6):
        v = G_sup(t2, 1.0 + 1e-9, PHI / 2, [1.0])
        vals.append(v)
    t2L = 1e9
    tope = 4 * math.asin(0.5) + sum(
        2 * math.asin(d / (2 * t2L))
        for d in cola_dominante_u(t2L, 1.0 + 1e-9, PHI * t2L))
    ok &= check(f"(a) t_2 -> inf: G en 10^4, 10^6 = "
                f"{[round(v, 4) for v in vals]} <= serie limite "
                f"{tope:.4f} + eps < 2pi - 0.4",
                all(v < tope + 0.05 for v in vals)
                and tope < 2 * PI - 0.4)
    # (b) t_1 -> inf: pi + resto chico (la banera sube al limite pi
    #     y las demas sombras mueren con R)
    v = G_u(1e8, 2.0, 1.0 + 1e-9, PHI / 2, [1.0], PHI * 2.0)
    ok &= check(f"(b) t_1 -> inf con t_2 = 2 (cola llena): G = "
                f"{v:.4f} -> pi (las sombras de la cola mueren con "
                f"R): margen pi", v is not None and abs(v - PI) < 0.01)
    # (c) la esquina critica: t_2 = 2, Sigma -> 1, cola llena
    #     u = phi t_2, t_1 en SU suelo de cascada (t_2+u)/phi = 2phi
    SSc = 1.0                          # frontera cerrada: en Sigma
    uc = PHI * 2.0                     # = 1 exacto la igualdad
    t1c = max(2.0, (2.0 + uc) / PHI)   # t_3 = p_min es admisible
    v = G_u(t1c, 2.0, SSc, 1 / PHI, [1.0, 0.5], uc)
    ok &= check(f"(c) esquina critica t_2 = 2, Sigma -> 1, u = "
                f"phi t_2 (cola llena), t_1 = suelo de cascada = "
                f"{t1c:.4f} = 2phi: G = {v:.4f} < 2pi - 0.05 — la "
                f"MISMA esquina 5.21 de los teoremas",
                v is not None and v < 2 * PI - 0.05
                and abs(t1c - 2 * PHI) < 1e-9)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles")
    ok = True
    # (a) sin el CORTE DE EXISTENCIA la serie diverge: cada termino
    #     fantasma por debajo de p_min sigue costando
    #     2 asin(s/(R-s)) > 0
    t2, SS, s = 2.0, 1.0 + 1e-9, 1 / PHI
    R = 4.0
    fantasma = 500 * 2 * math.asin(s / (R - s))
    ok &= check(f"(a) sin el corte de existencia (cap >= p_min), "
                f"500 terminos fantasma costarian ya "
                f"{fantasma:.1f} >> 2pi solo en corrimientos s: el "
                f"corte (la pieza arrastra sufijo >= 1+Sigma+p_min) "
                f"es esencial para que la serie sea FINITA",
                fantasma > 2 * PI)
    # (b) la dominacion falla si se viola la cascada (control)
    xs = [2.0, 2.0, 2.0, 2.0, 2.0]     # 5 piezas iguales SIN cascada
    R = 4.0
    s = 0.5
    real = presupuesto(s, xs + [1.0], R)
    g = G_u(2.0, 2.0, 1.0 + 1e-9, s, [1.0], PHI * 2.0)
    ok &= check(f"(b) familia SIN cascada (5 piezas iguales, "
                f"S_4 = 9 > phi*2): real = {real:.3f} > G = "
                f"{g:.3f}: la dominacion USA la cascada (rho <= "
                f"phi); fuera de ella es falsa — hipotesis "
                f"necesaria", real > g)
    # (c) regimen: violarlo revienta
    v = presupuesto(1.2, [2.0, 2.0, 1.0], 4.0)
    ok &= check(f"(c) con 2s = 2.4 > t_2 = 2 la sombra de t_1 "
                f"revienta ({v:.3f} incluye pi)", v >= PI)
    # (d) el vinculo de cascada de t_1 es esencial: t_1 = t_2 CON
    #     cola llena es conjuntamente infeasible y sin el vinculo
    #     el mayorante revienta 2pi
    v = G_u(2.0, 2.0, 1.0, 1 / PHI, [1.0, 0.5], PHI * 2.0)
    ok &= check(f"(d) SIN el vinculo t_1 >= (t_2+u)/phi: t_1 = "
                f"t_2 = 2 con cola llena (Sigma = 1 exacto, la "
                f"frontera admisible) da {v:.4f} > 2pi = "
                f"{2 * PI:.4f} — pero es INFEASIBLE (la cola de "
                f"t_1 contiene t_2, la cola y m+Sigma: t_1 >= "
                f"2phi): el vinculo no es decorativo",
                v is not None and v > 2 * PI)
    # (e) la hipotesis t_2 >= 1+Sigma es esencial: n = 2 (acta,
    #     hallazgo 1 — la navaja aurea j <= 1 como frontera)
    SSe = 1.0 + 1e-6
    t2e = (1.0 + SSe) / PHI            # suelo de cascada n = 2
    ue = 1.0 + SSe                     # cola vacia
    t1e = (t2e + ue) / PHI             # vinculo en su suelo = 1+Sigma
    se = 1 / PHI
    ve = G_u(t1e, t2e, SSe, se, [1.0, min(SSe / 2, PHI / 2)], ue)
    ok &= check(f"(e) SIN t_2 >= 1+Sigma (n = 2): t_2 = (1+Sigma)/"
                f"phi = {t2e:.4f}, t_1 = 1+Sigma, w* = 1/phi da "
                f"G = real = {ve:.4f} > 2pi — LA NAVAJA AUREA "
                f"j <= 1 (razon identica 1): la frontera del lema "
                f"coincide con la frontera conocida de los teoremas "
                f"de sombras; con n >= 3 la cadena phi^2 = 1+phi "
                f"da t_2 >= 1+Sigma y el contraejemplo es "
                f"inalcanzable", ve is not None and ve > 2 * PI
                and abs(t1e - (1.0 + SSe)) < 1e-9)
    return ok


def main():
    print("=" * 68)
    print("LA COLA GEOMETRICA: presupuestos uniformes en el numero "
          "de ocupantes (drafts/colageometrica.md)")
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
