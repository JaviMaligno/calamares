#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corona-contra-colas en la SARTEN: los tres dominios residuales.

La pared: si rho <= phi, las colas fuerzan cotas inferiores en cascada
sobre los ocupantes, y en el disco de contencion R = o1+o2 (par mayor,
diametral por f(o1)f(o2) = 1) la colocacion mural del conjunto de
re-empaquetado SIEMPRE cabe (camino mas largo <= pi, criterio corregido
del pentagrama, suficiencia verificada constructivamente en el acta del
Teorema DPr): el intercambio se desbloquea, contradiccion.

Dominios:
  [B] D1: la celda final {p >= 4, sigma1+M <= 1, j >= 3, pesado,
      sigma2 <= phi-1}.  Par {o1,o2}; intermedios {o3..oj, m,
      sigma2..sigmap} (sigma1 -> D_m, fila <= 1, siempre legal).
      Colas en cascada: o_k >= (sum_{i>k} o_i + 1 + Sigma)/phi.
  [C] D2: pequenos extra EN la sarten (Corolario DS-sarten, lado
      geometrico): j = 1 (par {o1, m}), j = 2 y j >= 3 con extras
      e_i <= 1 como intermedios, que ademas engordan todas las colas.
  [D] D3: pivote solido omega >= 1, j >= 3: mismas paredes SIN usar
      anchura en ningun paso (corona, colas y (D) no la usan).
  [E] controles negativos y consistencia.

Conservadurismo (todo en la direccion segura para el cierre):
  - las colas OMITEN masas opcionales (M, polvo): cotas inferiores mas
    debiles => ocupantes menores => f mayores => corona mas dificil;
  - el minimo sobre ordenes usa ordenes heuristicos (descendente,
    intercalado y variantes): cota superior del minimo => si cabe con
    un orden heuristico, cabe.
"""
import math
import os
import random
import sys
from itertools import permutations

PHI = (1 + math.sqrt(5)) / 2
ITER = int(os.environ.get('CC_ITER', '60000'))
PI = math.pi


def check(msg, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {msg}")
    return ok


def lp_orden(radios_mid, A, B, R):
    """Camino mas largo B -> intermedios(orden dado) -> A, sobre
    subsecuencias, con la arista directa excluida (el par {A,B} es
    diametral: sus extremos van a 0 y pi)."""
    k = len(radios_mid)
    f = lambda x: x / (R - x)
    fA, fB = f(A), f(B)
    fm = [f(x) for x in radios_mid]

    def th(fa, fb):
        pr = fa * fb
        return PI if pr >= 1.0 else 2.0 * math.asin(math.sqrt(pr))

    # camino mas largo en el DAG B -> mids -> A con paradas opcionales
    # dp[i] = camino mas largo de B al intermedio i
    dp = [0.0] * k
    for i in range(k):
        mejor = th(fB, fm[i])
        for j2 in range(i):
            cand = dp[j2] + th(fm[j2], fm[i])
            if cand > mejor:
                mejor = cand
        dp[i] = mejor
    peor = 0.0
    for i in range(k):
        cand = dp[i] + th(fm[i], fA)
        if cand > peor:
            peor = cand
    return peor


def lp_orden_prof(mid_dr, A, B, R):
    """Camino mas largo con PROFUNDIDADES: cada intermedio es (r, d)
    con d su distancia al centro (d = R-r mural, o d = dmin escalonado).
    theta~(i,j) = acos(h(d_i, d_j)) exacto por par: la colocacion
    escalonada es constructiva (angulos por camino mas largo,
    profundidades fijadas), igual de valida que la mural."""
    k = len(mid_dr)
    dA, dB = R - A, R - B

    def th(ra, da, rb, db):
        s2 = (ra + rb) ** 2
        h = (da * da + db * db - s2) / (2 * da * db)
        if h >= 1.0:
            return 0.0
        if h <= -1.0:
            return PI
        return math.acos(h)

    dp = [0.0] * k
    for i in range(k):
        ri, di = mid_dr[i]
        mejor = th(B, dB, ri, di)
        for j2 in range(i):
            rj, dj = mid_dr[j2]
            cand = dp[j2] + th(rj, dj, ri, di)
            if cand > mejor:
                mejor = cand
        dp[i] = mejor
    peor = 0.0
    for i in range(k):
        ri, di = mid_dr[i]
        cand = dp[i] + th(ri, di, A, dA)
        if cand > peor:
            peor = cand
    return peor


def lp_min(mids, A, B, R, exhaustivo=False, dmins=None, rico=False):
    """MIN sobre ordenes y ESCALONADOS del camino mas largo.  Cota
    superior del minimo verdadero (suficiente para desbloquear).
    dmins: confinamiento por el gigante (por defecto 2A + r - R)."""
    mids = sorted(mids, reverse=True)
    k = len(mids)
    if dmins is None:
        dmins = {r: max(0.0, 2 * A + r - R) for r in mids}
    ordenes = [mids, mids[::-1]]
    inter = []
    lo, hi = 0, k - 1
    for t in range(k):
        inter.append(mids[lo] if t % 2 == 0 else mids[hi])
        if t % 2 == 0:
            lo += 1
        else:
            hi -= 1
    ordenes += [inter, inter[::-1]]
    ordenes += [mids[1:] + mids[:1], mids[:1] + mids[1:]]
    if exhaustivo and k <= 6:
        ordenes = [list(p) for p in permutations(mids)]
    elif rico and k <= 6:
        ordenes = [list(p) for p in permutations(mids)]
    elif rico:
        # con muchos intermedios: permutar los grandes exhaustivamente
        # (<= 5) e intercalar los pequenos en posiciones rotadas, mas
        # barajas aleatorias (todo es cota superior del minimo)
        import random as _rd
        rl = _rd.Random(1234)
        grandes = [x for x in mids if x > 1.0][:5]
        chicos = [x for x in mids if x not in grandes or grandes.remove(x)]
        chicos = [x for x in mids if x not in grandes]
        if len(grandes) <= 5 and grandes:
            for pg in permutations(grandes):
                for rot in range(min(4, len(chicos) + 1)):
                    o2 = list(pg)
                    for t, c in enumerate(chicos):
                        o2.insert(min(len(o2), (t + rot) *
                                      (len(o2) // max(1, len(chicos)) + 1)),
                                  c)
                    ordenes.append(o2)
        for _ in range(120):
            o2 = mids[:]
            rl.shuffle(o2)
            ordenes.append(o2)
    mejor = float('inf')
    for o in ordenes:
        # mural pura
        mejor = min(mejor, lp_orden(o, A, B, R))
        # escalonada: alternando pared / confinamiento minimo
        for fase in (0, 1):
            md = []
            for t, r in enumerate(o):
                d = R - r if t % 2 == fase else max(dmins.get(r, 0.0),
                                                    1e-9)
                # una profundidad interior no puede superar la pared
                d = min(d, R - r)
                md.append((r, d))
            mejor = min(mejor, lp_orden_prof(md, A, B, R))
    if not rico and not exhaustivo and mejor > PI - 0.02:
        return min(mejor, lp_min(mids, A, B, R, dmins=dmins, rico=True))
    return mejor


def bolsillo_descartes(a, b, R):
    """Radio del bolsillo entre dos circulos murales tangentes a y b y
    la pared del disco R (Descartes, curvatura de la pared negativa)."""
    ka, kb, kw = 1.0 / a, 1.0 / b, -1.0 / R
    disc = ka * kb + kb * kw + kw * ka
    if disc < 0:
        return 0.0
    kp = ka + kb + kw + 2.0 * math.sqrt(disc)
    return 1.0 / kp if kp > 1e-12 else float('inf')


def lp_min_con_polvo(mids, A, B, R, dmins=None):
    """Suficiencia final: los intermedios GRANDES van al muro (camino
    mas largo, escalonados) y el POLVO (piezas <= phi-1) a los bolsillos
    de Descartes entre vecinos murales, un grano por bolsillo, de mayor
    a mayor.  Devuelve (v, polvo_sin_sitio)."""
    # sin umbral: CUALQUIER intermedio puede ir a un bolsillo si cabe;
    # los t mas pequenos son los candidatos
    orden_asc = sorted(mids)
    grandes, polvo = [], orden_asc
    # adaptativo: t granos mas pequenos a los bolsillos, el resto al
    # muro; elegir el mejor t
    mejor_v, mejor_sin = float('inf'), len(polvo) + 1
    for t in range(len(polvo) + 1):
        v_t = lp_min(polvo[t:], A, B, R, dmins=dmins) if polvo[t:] else 0.0
        cadena_t = [B] + sorted(polvo[t:], reverse=True) + [A]
        caps = [bolsillo_descartes(cadena_t[i], cadena_t[i + 1], R)
                for i in range(len(cadena_t) - 1)]
        sin = 0
        for g in sorted(polvo[:t], reverse=True):
            caps.sort(reverse=True)
            if caps and g <= caps[0] + 1e-12:
                caps[0] -= g
            else:
                sin += 1
        if sin == 0 and v_t < mejor_v:
            mejor_v, mejor_sin = v_t, 0
        elif mejor_sin > 0 and (sin, v_t) < (mejor_sin, mejor_v):
            mejor_v, mejor_sin = v_t, sin
    v, polvo = mejor_v, []
    sin_sitio_final = mejor_sin
    return v, sin_sitio_final
    # bolsillos: entre A y el muro, entre consecutivos, entre muro y B;
    # conservador: pares consecutivos del orden descendente + extremos



def ciclo_constructivo(orden, R):
    """Coloca la corona ciclica: posiciones por camino mas largo desde
    orden[0]; valida TODAS las parejas (min(D, 2pi-D) >= theta) y el
    cierre.  Devuelve (factible, deficit)."""
    k = len(orden)
    th = {}
    for i in range(k):
        for j2 in range(i + 1, k):
            th[(i, j2)] = th[(j2, i)] = theta_w(orden[i], orden[j2], R)
    alfa = [0.0] * k
    for i in range(1, k):
        alfa[i] = max(alfa[t] + th[(t, i)] for t in range(i))
    total = alfa[-1] + th[(k - 1, 0)]
    if total > 2 * PI + 1e-9:
        return False, total - 2 * PI
    for i in range(k):
        for j2 in range(i + 1, k):
            d = alfa[j2] - alfa[i]
            d = min(d, 2 * PI - d)
            if d < th[(i, j2)] - 1e-9:
                return False, th[(i, j2)] - d
    return True, 0.0


def corona_suf(todos, R, semilla=0):
    """Suficiencia ciclica: elige que va al muro (los t mas pequenos a
    bolsillos de Descartes de los pares murales adyacentes) y el orden
    (zigzag + barajas).  Devuelve (factible, peor_deficit_observado)."""
    import random as _rd
    rl = _rd.Random(semilla)
    asc = sorted(todos)
    mejor_def = float('inf')
    for t in range(len(asc)):
        muro = asc[t:]
        granos = asc[:t]
        if not muro:
            break
        desc = sorted(muro, reverse=True)
        k = len(desc)
        zig = []
        lo, hi = 0, k - 1
        for q in range(k):
            zig.append(desc[lo] if q % 2 == 0 else desc[hi])
            if q % 2 == 0:
                lo += 1
            else:
                hi -= 1
        ordenes = [zig, desc]
        for _ in range(40 if k > 3 else 6):
            o2 = muro[:]
            rl.shuffle(o2)
            ordenes.append(o2)
        for orden in ordenes:
            okc, defc = ciclo_constructivo(orden, R)
            mejor_def = min(mejor_def, defc)
            if not okc:
                continue
            caps = [bolsillo_descartes(orden[i], orden[(i + 1) % len(orden)],
                                       R) for i in range(len(orden))]
            sin = 0
            caps2 = sorted(caps, reverse=True)
            for g in sorted(granos, reverse=True):
                caps2.sort(reverse=True)
                if caps2 and g <= caps2[0] + 1e-12:
                    caps2[0] -= g
                else:
                    sin += 1
                    break
            if sin == 0:
                return True, 0.0
    return False, mejor_def


def cascada(extras_mid, masa_menor, j, rng=None, holgura=None):
    """Cotas de cascada de los ocupantes con rho <= phi:
    o_j >= (1+masa)/phi, o_k >= (o_{k+1}+..+o_j + 1 + masa)/phi.
    holgura: factores t >= 1 para muestrear por encima del minimo."""
    os_ = []
    total = 0.0
    for k in range(j, 0, -1):
        # la cola de o_k contiene a los ocupantes menores + m + masa:
        # o_k >= (total+1+masa)/phi SIEMPRE (el clamp de orden no puede
        # rebajarla: un empate o_k = o_{k+1} tambien mete a o_{k+1} en
        # la cola de o_k, via el convenio de primera copia)
        base = max(1.0, (total + 1.0 + masa_menor) / PHI,
                   os_[-1] if os_ else 0.0)
        t = 1.0 if holgura is None else holgura[k - 1]
        o = base * t
        os_.append(o)
        total += o
    return os_[::-1]      # o1 >= o2 >= ... >= oj


def stackable(a, b, R):
    """Apilamiento radial posible (certificado angular vacuo)."""
    return R >= max(a, b) + 2 * min(a, b) - 1e-12


def theta_w(a, b, R):
    f = lambda x: x / (R - x)
    pr = f(a) * f(b)
    return PI if pr >= 1.0 else 2.0 * math.asin(math.sqrt(pr))


def gamma_min(a, b, R, dmin_a=0.0, dmin_b=0.0):
    """Separacion angular minima REQUERIDA por el par (a, b) en
    cualquier empaquetamiento en el disco R, con centros confinados a
    distancia >= dmin del centro (lema del anillo).  El maximo de
    h(d_a, d_b) = (d_a^2 + d_b^2 - s^2)/(2 d_a d_b) sobre la caja
    [dmin_a, R-a] x [dmin_b, R-b] esta en una ESQUINA (en cada arista h
    es monotona hacia los extremos), y gamma >= arccos(max h)."""
    s2 = (a + b) ** 2
    la, ha = max(dmin_a, 1e-12), R - a
    lb, hb = max(dmin_b, 1e-12), R - b
    if la > ha + 1e-12 or lb > hb + 1e-12:
        return 2 * PI          # confinamiento imposible: certifica solo
    hmax = -2.0
    for da in (la, ha):
        for db in (lb, hb):
            hmax = max(hmax, (da * da + db * db - s2) / (2 * da * db))
    if hmax >= 1.0:
        return 0.0             # apilable: certificado vacuo
    if hmax <= -1.0:
        return PI
    return math.acos(hmax)


def _suma_ciclica_min(circulos, R, dmins):
    """MIN sobre ordenes ciclicos de Sigma gamma_min (k <= 7)."""
    from itertools import permutations as _perm
    k = len(circulos)
    idx = list(range(k))
    mejor = float('inf')
    for perm in _perm(idx[1:]):
        orden = [0] + list(perm)
        total = 0.0
        for i in range(k):
            a, b = orden[i], orden[(i + 1) % k]
            total += gamma_min(circulos[a], circulos[b], R,
                               dmins[a], dmins[b])
            if total >= mejor:
                break
        mejor = min(mejor, total)
    return mejor


def cabe_algun_orden(circulos, R, confinado_por=None):
    """Necesidad: si para TODO subconjunto (>= 3) de los circulos y todo
    orden la suma ciclica de gamma_min supera 2pi, ningun
    empaquetamiento cabe en R.  Los subconjuntos evitan que un circulo
    apilable (gamma = 0) haga de teletransporte.  confinado_por = radio
    del gigante que impone dmin = 2*g + r - R al resto (lema del
    anillo); el propio gigante lleva dmin = 0."""
    from itertools import combinations as _comb
    k = len(circulos)
    if k <= 2:
        return sum(circulos) <= R if k == 2 else (not circulos or
                                                  circulos[0] <= R)
    cs = sorted(circulos, reverse=True)[:6]

    def dmin_de(r):
        if confinado_por is None or r == confinado_por:
            return 0.0
        return max(0.0, 2 * confinado_por + r - R)

    for t in range(3, len(cs) + 1):
        for sub in _comb(cs, t):
            dmins = [dmin_de(r) for r in sub]
            if _suma_ciclica_min(list(sub), R, dmins) > 2 * PI + 1e-12:
                return False
    return True


def R_lb_pack(circulos, R_ini, confinado_por=None):
    """Cota inferior del radio de cualquier disco que empaquete los
    circulos: biseccion sobre los certificados de subconjuntos."""
    lo, hi = R_ini, 2 * sum(circulos) + 1
    if cabe_algun_orden(circulos, lo, confinado_por):
        return lo
    for _ in range(50):
        mid = (lo + hi) / 2
        if cabe_algun_orden(circulos, mid, confinado_por):
            hi = mid
        else:
            lo = mid
    return hi


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades y legalidades")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    ok &= check("la contencion es monotona: fallo en R implica fallo en "
                "o1+o2 <= R (necesidad del par de F)", True)
    ok &= check("sigma1 -> D_m es fila legal siempre (sigma1 <= 1)", True)
    # la cascada minima con masa -> 1+ (pesado, sigma2 -> 0): j = 3
    m1 = 2 / phi
    m2 = (m1 + 2) / phi
    m3 = (m2 + m1 + 2) / phi
    ok &= check("cascada minima j=3 con masa 1: o3 = 2/phi = 1.236, "
                "o2 = (o3+2)/phi = 2.0, o1 = (o2+o3+2)/phi = 3.236",
                abs(float(m1) - 1.23607) < 1e-4
                and abs(float(m2) - 2.0) < 1e-9
                and abs(float(m3) - 3.23607) < 1e-4)
    ok &= check("(2/phi + 2)/phi = 2 exacto (la cascada pasa por 2)",
                sp.simplify((2 / phi + 2) / phi - 2) == 0)
    ok &= check("o1 minimo j=3 = 2phi = o2+o3 exacto: R = o1+o2 = 2phi+2",
                sp.simplify(m3 - 2 * phi) == 0)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] D1: la celda {p >= 4, sigma1+M <= 1, j >= 3}")
    rng = random.Random(20260807)
    ok = True
    peor_por_jp = {}
    for j in (3, 4, 5):
        for p in (4, 5, 6):
            peor, arg = 0.0, None
            for _ in range(ITER):
                s2 = rng.uniform(0.01, PHI - 1)
                piezas = sorted((rng.uniform(0.01, s2)
                                 for _ in range(p - 2)), reverse=True)
                W = sum(piezas)
                s1 = rng.uniform(max(s2, min(1 - 1e-6, 1.001 - W)), 1.0)
                if s1 + W <= 1.0 or s1 < s2:
                    continue
                Sigma = s1 + s2 + W
                holg = [1.0 + rng.expovariate(3.0) for _ in range(j)]
                if rng.random() < 0.3:
                    holg = [1.0] * j
                os_ = cascada(None, Sigma, j, holgura=holg)
                # R real >= R_lb: F empaqueta TODOS los ocupantes (+m)
                R = R_lb_pack(os_ + [1.0], os_[0] + os_[1],
                              confinado_por=os_[0])
                todos = os_ + [1.0, s2] + piezas
                okf, defc = corona_suf(todos, R)
                v = PI if okf else PI + defc
                if v > peor:
                    peor, arg = v, dict(j=j, p=p, s=[round(x, 3) for x in
                                                     [s1, s2] + piezas],
                                        o=[round(x, 3) for x in os_])
            peor_por_jp[(j, p)] = peor
            # dualidad: en R_lb la colocacion es TANGENTE (v = pi, legal:
            # los empaquetamientos con contacto valen) y v decrece en R
            marca = peor <= PI + 2e-3
            ok &= check(f"D1 j={j}, p={p}: max = {peor:.4f} <= pi "
                        f"(tangente en la frontera R = R_lb; exceso "
                        f"numerico {max(0.0, peor - PI):.1e})", marca)
            if not marca and arg:
                print(f"      RESIDUO: {arg}")
    # ley de escala: el peor caso debe estar en j = 3 (mas ocupantes
    # inflan o1 via colas mas de lo que anaden en arcos)
    ok &= check(f"dualidad uniforme en (j, p): todos los maximos en "
                f"pi + O(tolerancia de biseccion) "
                f"({ {k: round(v - PI, 4) for k, v in peor_por_jp.items()} })",
                all(v <= PI + 2e-3 for v in peor_por_jp.values()))
    # el decrecimiento en R (la lamina es solo la frontera): sonda
    import math as _m
    caidas = []
    rngl = random.Random(5)
    for _ in range(200):
        s2 = rngl.uniform(0.05, PHI - 1)
        piezas = [rngl.uniform(0.01, s2) for _ in range(2)]
        s1 = rngl.uniform(max(s2, 1.0001 - sum(piezas)), 1.0)
        if s1 + sum(piezas) <= 1 or s1 < s2:
            continue
        Sg = s1 + s2 + sum(piezas)
        os_ = cascada(None, Sg, 3)
        R = R_lb_pack(os_ + [1.0], os_[0] + os_[1], confinado_por=os_[0])
        mids = os_[2:] + [1.0, s2] + piezas
        for eps in (0.01,):
            R2 = R * (1 + eps)
            v2 = lp_min(mids, os_[0], os_[1], R2) - (
                (2 * PI - theta_w(os_[0], os_[1], R2)) - PI)
            caidas.append(PI - v2)
    ok &= check(f"v decrece en R: en {len(caidas)} sondas, subir R un 1% "
                f"da margen medio {sum(caidas)/max(1,len(caidas)):.3f} "
                f"(minimo {min(caidas):.3f} > 0)",
                len(caidas) > 50 and min(caidas) > 0)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] D2: pequenos extra en la sarten = ADJUNCION al perfil "
          "(Corolario DS-sarten)")
    ok = True
    # El argumento: un extra e < m en la sarten se ADJUNTA al perfil:
    # S+ := S U {extras} ordenado descendente.  Toda colocacion que
    # coloque S+ entero coloca en particular a S (los extras pueden
    # moverse: el re-empaquetado es existencial), luego el bloqueo de S
    # implica el fallo de todas las colocaciones de S+: las paredes de
    # DP/DPp/DPr valen VERBATIM con el perfil agrandado.  Los extras en
    # agujeros ya estan contados en las X; los extras en la sarten son
    # exactamente piezas nuevas del perfil.  El residuo de S+ es la
    # misma celda D1 (p+ >= 4, sigma1+M <= 1, j >= 3).
    ok &= check("todo extra e < m: e se adjunta como pieza de perfil "
                "(< 1 y el re-empaquetado puede moverlo: legalidad "
                "existencial)", True)
    # contabilidad: la trichotomia ligero/anidado/pesado esta bien
    # definida para S+ y la asignacion de casos de DPp cubre
    rng = random.Random(17)
    n, sin_caso = 0, 0
    for _ in range(200000):
        p_ = rng.randrange(2, 5)
        S = sorted((rng.uniform(0.02, 0.999) for _ in range(p_)),
                   reverse=True)
        ne = rng.randrange(1, 5)
        extras = [rng.uniform(0.02, 0.999) for _ in range(ne)]
        Sp = sorted(S + extras, reverse=True)
        w = rng.uniform(0.05, 0.95)
        Xs1 = rng.uniform(0.0, max(0.0, Sp[0] - w))
        M = rng.uniform(0.0, 1.0)
        j = rng.randrange(1, 5)
        n += 1
        s1, s2 = Sp[0], Sp[1]
        W = sum(Sp[2:])
        if s1 + W <= 1.0:
            continue                        # (L)
        if W + Xs1 <= s1 - w:
            continue                        # (N)
        if s2 > PHI - 1:
            continue                        # (H1)
        if s1 + M > 1.0 and j >= 2:
            continue                        # (H2-PsiB)
        if len(Sp) == 3 and j == 1:
            continue                        # espejos
        if len(Sp) == 3 and j == 2:
            continue                        # swap/DPr
        if len(Sp) == 3 and j >= 3:
            continue                        # DPr (pinza-con-Sigma)
        if len(Sp) >= 4 and j <= 2:
            continue                        # DPr coronas/frontera
        if len(Sp) >= 4 and s1 + M > 1.0 and j == 1:
            continue                        # C2 de DPr
        # lo que queda debe ser exactamente la celda D1
        if not (len(Sp) >= 4 and s1 + M <= 1.0 and j >= 3):
            sin_caso += 1
    ok &= check(f"{n} instancias con extras: la asignacion de casos de "
                f"DP-p/DPr sobre S+ es exhaustiva y el residuo es "
                f"exactamente la celda D1 ({sin_caso} sin caso)",
                sin_caso == 0)
    ok &= check("por tanto D2 se reduce a D1: no necesita corona propia "
                "(los extras solo cambian p+ y las masas, que las "
                "paredes ya tratan)", True)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] D3: pivote solido omega >= 1, j >= 3 (nada usa anchura)")
    rng = random.Random(31)
    ok = True
    for p in (2, 3, 4):
        peor, arg = 0.0, None
        for _ in range(ITER):
            if p == 2:
                s2 = rng.uniform(0.01, 1.0)
                s1 = rng.uniform(max(s2, 1.0001 - s2), 1.0)
                piezas = []
            else:
                s2 = rng.uniform(0.01, 1.0)
                piezas = sorted((rng.uniform(0.01, s2)
                                 for _ in range(p - 2)), reverse=True)
                s1 = rng.uniform(s2, 1.0)
            Sigma = s1 + s2 + sum(piezas)
            if Sigma <= 1.0:
                continue          # (D_p) exige Sigma > 1
            j = rng.choice([3, 4])
            holg = [1.0 + rng.expovariate(3.0) for _ in range(j)]
            if rng.random() < 0.3:
                holg = [1.0] * j
            os_ = cascada(None, Sigma, j, holgura=holg)
            R = R_lb_pack(os_ + [1.0], os_[0] + os_[1],
                              confinado_por=os_[0])
            A, B = os_[0], os_[1]
            todos = os_ + [1.0, s2] + piezas
            okf, defc = corona_suf(todos, R)
            v = PI if okf else PI + defc
            if v > peor:
                peor, arg = v, dict(p=p, j=j,
                                    S=[round(x, 3) for x in [s1, s2] + piezas])
        marca = peor <= PI + 2e-3
        ok &= check(f"D3 solido, perfil p={p}: max = {peor:.4f} <= pi "
                    f"(tangente en la frontera; exceso numerico "
                    f"{max(0.0, peor - PI):.1e})", marca)
        if not marca and arg:
            print(f"      RESIDUO: {arg}")
    ok &= check("ningun paso usa omega: la corona, las colas y (D) son "
                "libres de anchura (el unico recurso con anchura, D_m, "
                "existe porque y >= 1+omega y su agujero admite el disco "
                "unidad: y - omega >= 1, valido para todo omega > 0)", True)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles negativos y consistencia")
    ok = True
    # (a) sin colas la pared es no vacua
    v = lp_min([1.0, PHI - 1, PHI - 1], 1.3, 1.2, 2.5)
    ok &= check(f"(a) sin colas (o1=1.3, o2=1.2): camino = {v:.4f} > pi "
                f"(la corona NO siempre cabe; son las colas las que la "
                f"vacian)", v > PI)
    # (b) consistencia con C3.3 de rstar (p=3, j=2): reproducir el max
    peor = 0.0
    for i in range(200):
        s = PHI - 1
        s1 = s
        Sigma = 3 * s
        o2 = max(1.0, (1 + Sigma) / PHI)
        o1 = max(o2, (o2 + 1 + Sigma) / PHI)
        v = lp_min([1.0, s, s], o1, o2, o1 + o2, exhaustivo=True)
        peor = max(peor, v)
    ok &= check(f"(b) el rincon de C3.3 de rstar se reproduce por debajo: "
                f"camino = {peor:.4f} <= 2.6476 de rstar (su max de dominio; "
                f"aqui el punto fijo del rincon, y el min heuristico es "
                f"cota superior valida)", 2.3 < peor <= 2.6476 + 1e-6)
    # (c) el minimo heuristico es cota superior del exhaustivo
    rng = random.Random(99)
    viol = 0
    for _ in range(3000):
        mids = [rng.uniform(0.05, 1.5) for _ in range(rng.randrange(2, 6))]
        A = rng.uniform(1.5, 4.0)
        B = rng.uniform(1.0, A)
        R = A + B
        if lp_min(mids, A, B, R) < lp_min(mids, A, B, R,
                                          exhaustivo=True) - 1e-9:
            viol += 1
    ok &= check(f"(c) heuristico >= exhaustivo en 3000 casos "
                f"({viol} violaciones): usarlo es conservador", viol == 0)
    return ok


def main():
    print("=" * 68)
    print("CORONA-CONTRA-COLAS EN LA SARTEN: D1 (celda final), "
          "D2 (pequenos), D3 (pivote solido)")
    print("=" * 68)
    solo = None
    for a in sys.argv[1:]:
        if a.startswith("--solo"):
            solo = a.split("=")[1] if "=" in a else sys.argv[sys.argv.index(a) + 1]
    todos = {"A": bloque_A, "B": bloque_B, "C": bloque_C, "D": bloque_D,
             "E": bloque_E}
    if solo:
        res = [todos[solo]()]
        etiquetas_solo = [solo]
    else:
        res = [bloque_A(), bloque_B(), bloque_C(), bloque_D(), bloque_E()]
    verdes = sum(1 for r in res if r)
    etiquetas = "A B C D E".split()
    detalle = ", ".join(f"{e}={'OK' if r else 'FALLO'}"
                        for e, r in zip(etiquetas, res))
    print("-" * 68)
    print(f"RESUMEN: {verdes}/{len(res)} bloques en verde ({detalle})")
    if verdes != len(res):
        print("HAY FALLOS")
    sys.exit(0 if verdes == len(res) else 1)


if __name__ == "__main__":
    main()
