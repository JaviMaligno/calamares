#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El lema de reduccion de |A| (docs/drafts/areduccion.md): las
ramas PESADAS de R2b (G-e directa y G-g especular), declaradas
fuera por r2bcert/r2bmulti porque el mural {*, m} U A tiene A
multipieza SIN COTA en |A|, se cierran con una dicotomia AUREA:

  LEMA DE REDUCCION 1/(4 phi).  Sea B* el mejor subconjunto de S
  con Sigma B* <= 1 (la particion adversariada de puertocii, B* en
  fila a D_m) y A = S \\ B*, con Sigma_S <= phi (pared de masa) y
  piezas < 1.  Entonces, con t0 = (phi-1)/4 = 1/(4 phi) y
  beta = Sigma B*:
    (i)  por maximalidad, a + beta > 1 para toda a en A, y
         beta >= sigma_1 >= max A (el subconjunto {sigma_1} es
         candidato); ademas beta > 1 - t0 o A entera > t0.
    (ii) |{a en A : a > t0}| <= 4 SIEMPRE: si beta <= (9-sqrt5)/8
         entonces |A| < (phi-beta)/(1-beta) <= 5 y toda A > t0;
         si beta > (9-sqrt5)/8, cinco piezas > t0 sumarian
         > 5(sqrt5-1)/8 = phi - (9-sqrt5)/8 >= phi - beta >=
         Sigma A — contradiccion.  La igualdad de umbrales
         5 t0 = phi - beta* es EXACTA en Q(sqrt5).
    (iii) el POLVO (piezas <= t0 de A) existe solo si
         beta > beta* = (9-sqrt5)/8 y su masa mu < 5 t0 = 0.7725;
         su coste angular como CADENA mural es de MASA, no de
         numero: theta(a,b) <= asin f(a) + asin f(b) (AM-GM +
         convexidad de asin, exactas) => la suma consecutiva
         interna de la cadena de polvo <= 2 Sigma asin f(d_i) <=
         pi mu / (R - t0), independiente del numero de piezas.

  Con (ii)+(iii) el mural pesado es {Y o z, m} + <= 4 piezas
  grandes + UN bloque de polvo agregado (mu, t0): coronas de <= 7
  nodos con el bloque atomico — certificables por el motor de
  r2bmulti (matriz mayorante por termino + criterio antipodal de
  DOS LADOS + verificacion float), con el par (Y|z, m) antipodal
  exacto y las cadenas como sistemas de CAMINO (TU, dual disjunto
  exacto).

Bloques: [A] el lema (algebra exacta en Q(sqrt5) + convexidad
sympy + fuzz de la particion); [B] el bloque de polvo (derivacion
+ fuzz 0 violaciones); [C] G-e pesada (DR) certificada por B&B;
[D] G-g pesada especular (corte X = 0) certificada por B&B; [E]
controles y alcance honesto.

Alcance declarado: cajas del barrido MC (omega <= 1.6, Y < SS +
omega en G-e; X = 0 en G-g pesada); las X > 0 de las pesadas y
omega > 1.6 siguen como MC adversariado (puertocii G-e/G-g).
"""
import itertools
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, theta_w, corona_suf
from puertocii import b_star_particion
from r2bmulti import th, MARGEN, bnb_factible

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260818'))

T0 = (PHI - 1.0) / 4.0                 # = 1/(4 phi) = (sqrt5-1)/8
BSTAR = (9.0 - math.sqrt(5.0)) / 8.0   # beta* umbral de la dicotomia


def g_asin(x, R):
    """asin(f(x)) con guarda (f < 1 garantizado en los usos)."""
    fx = x / (R - x)
    if fx >= 1.0:
        return PI / 2
    return math.asin(fx)


def D_polvo(mu, R):
    """Cota del coste consecutivo interno de la cadena de polvo:
    2 Sigma asin f(d_i) <= pi Sigma d_i/(R - t0) = pi mu/(R - t0)
    (asin x <= pi x / 2, f(d) <= d/(R - t0))."""
    return PI * mu / (R - T0)


# ------------------------------------------------- caminos de dos lados
def _peor_camino(cadena, tam, thmat, es_polvo, D):
    """Presupuesto minimo del sistema de CAMINO [0] + cadena + [1]
    (dual de familias disjuntas, EXACTO por TU).  El nodo de polvo
    se expande en dos extremos virtuales t0 con arista interna D;
    el par (0, 1) antipodal queda excluido (analitico).
    REPARACION del acta: cadena vacia => presupuesto 0 — el lado
    degenerado ES el par excluido y no debe reintroducirlo via el
    arco completo (en la tangencia de G-g, theta(z, m) = pi
    identicamente y el requisito d = pi cerrado se satisface por
    construccion; antes el verde de D dependia del accidente de
    que la biseccion nunca anula un slot)."""
    if not cadena:
        return 0.0
    nodos = [0]
    for x in cadena:
        if es_polvo[x]:
            nodos.extend([('pL', x), ('pR', x)])
        else:
            nodos.append(x)
    nodos.append(1)
    # (codigo muerto talla() retirado — acta de espkp: llevaba T0
    # hardcodeado y era trampa latente para topes de polvo != t0;
    # las tallas de extremos entran SIEMPRE por thmat del llamador)

    def tth(u, v):
        if isinstance(u, tuple) and isinstance(v, tuple):
            return D                   # arista interna del polvo
        iu = u[1] if isinstance(u, tuple) else u
        iv = v[1] if isinstance(v, tuple) else v
        if iu == iv:
            return D
        return thmat[min(iu, iv)][max(iu, iv)] if not (
            isinstance(u, tuple) or isinstance(v, tuple)) else \
            thmat[min(iu, iv)][max(iu, iv)]

    m = len(nodos) - 1                 # gaps del camino
    arcs = []
    for i in range(m):
        for j in range(i + 1, m + 1):
            r_c = sum(tth(nodos[t], nodos[t + 1])
                      for t in range(i, j))
            if i == 0 and j == m:
                r = r_c                # (0,1) antipodal: excluido
            else:
                r = max(r_c, tth(nodos[i], nodos[j]))
            arcs.append((frozenset(range(i, j)), r))

    tope = PI - MARGEN

    def peor(k, usados, acum):
        if acum > tope:
            return acum                # corte: el lado ya es inviable
        best = acum
        for t in range(k, len(arcs)):
            g, r = arcs[t]
            if not (g & usados):
                v = peor(t + 1, usados | g, acum + r)
                if v > best:
                    best = v
                    if best > tope:
                        return best
        return best

    return peor(0, frozenset(), 0.0)


def antipodal_dos_lados(tam, thmat, es_polvo, D):
    """Nodos 0 y 1 (la pieza grande y m) a distancia EXACTA pi
    (theta(0,1) <= pi siempre; estricto en los puntos reales por
    holgura de pares).  El resto se reparte en DOS semicirculos;
    cada lado es un sistema de camino exacto con presupuesto
    pi - MARGEN.  Se prueban reparticiones y ordenes (k <= 5
    nodos repartibles: barato)."""
    resto = list(range(2, len(tam)))
    for mask in range(1 << len(resto)):
        lados = ([r for k, r in enumerate(resto) if mask >> k & 1],
                 [r for k, r in enumerate(resto)
                  if not mask >> k & 1])
        ok = True
        for lado in lados:
            ok_lado = False
            heur = [sorted(lado, key=lambda i: -tam[i]),
                    sorted(lado, key=lambda i: tam[i])]
            probados = set()
            for np_, perm in enumerate(
                    heur + list(itertools.permutations(lado))):
                if np_ >= 26:
                    break              # tope de ordenes: criterio de
                                       # SUFICIENCIA (menos ordenes =
                                       # mas conservador, nunca unsound)
                t = tuple(perm)
                if t in probados:
                    continue
                probados.add(t)
                if _peor_camino(list(perm), tam, thmat, es_polvo,
                                D) <= PI - MARGEN:
                    ok_lado = True
                    break
            if not ok_lado:
                ok = False
                break
        if ok:
            return True
    return False


# --------------------------------------------------------- criterios G-e
Y_MAX_E = PHI + 1.6                    # Y < SS + w (caja del barrido)


def criterio_ge(box):
    """Caja (Y, SS, beta, a1..a4, mu) de la rama pesada DR: mural
    {Y, m} U A_big U polvo en c = SS + Y = beta + Sigma a + mu + Y.
    Matriz por termino (participantes en techo CON su aporte a c;
    valido: R - a - b >= beta_lo > 0).  None = sin puntos reales."""
    Yl, Yh, SSl, SSh, bl, bh = box[:6]
    als = [(box[i], box[i + 1]) for i in range(6, 14, 2)]
    mul, muh = box[14], box[15]
    # podas exactas
    if SSh <= 1.0:
        return None                    # pesada: SS > 1
    if bh > min(1.0, SSh):
        bh = min(1.0, SSh)
        if bl > bh:
            return None
    if any(al > PHI / 2 for al, _ in als):
        return None                    # SS >= beta + a >= 2a <= phi
    if any(al > 0 and ah + bh <= 1.0 for al, ah in als):
        return None                    # maximalidad: a + beta > 1
    if mul > 0 and bh <= BSTAR:
        return None                    # polvo solo con beta > beta*
    if mul > 0 and sum(1 for al, _ in als if al > T0) >= 4:
        return None                    # refuerzo del acta: 4 t0 =
                                       # phi - 1 EXACTO => 4 grandes
                                       # y polvo incompatibles (mu <
                                       # 1 - beta < toda pieza polvo)
    # ligadura beta + Sigma a + mu = SS (interseccion no vacia)
    lo_t = bl + sum(al for al, _ in als) + mul
    hi_t = bh + sum(min(ah, 1.0) for _, ah in als) + muh
    if lo_t > SSh or hi_t < SSl:
        return None
    if any(bh < al for al, _ in als):
        return None                    # beta >= sigma1 >= a
    # nodos: 0 = Y, 1 = m, 2.. = A_big, ultimo = polvo (si muh > 0)
    hi = [Yh, 1.0] + [min(ah, PHI / 2) for _, ah in als if ah > 0]
    cap_hi = [Yh, 0.0] + [min(ah, PHI / 2)
                          for _, ah in als if ah > 0]
    cap_lo = [Yl, 0.0] + [al for al, ah in als if ah > 0]
    es_polvo = [False] * len(hi)
    if muh > 0:
        hi.append(T0)
        # el polvo NUNCA infla la capacidad como participante: su
        # aporte a c queda en el suelo mul (la pieza individual es
        # <= t0, no la masa del bloque)
        cap_hi.append(mul)
        cap_lo.append(mul)
        es_polvo.append(True)
    n = len(hi)
    base_lo = max(bl, T0)              # beta > t0 siempre
    R_glob_lo = base_lo + sum(cap_lo)
    thmat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            R_c = base_lo + sum(cap_hi[k] if k in (i, j)
                                else cap_lo[k] for k in range(n))
            thmat[i][j] = th(hi[i], hi[j], R_c)
    D = D_polvo(muh, R_glob_lo) if muh > 0 else 0.0
    return antipodal_dos_lados(hi, thmat, es_polvo, D)


# --------------------------------------------------------- criterios G-g
def criterio_gg(box):
    """Caja (w, s2, SS, beta, a1..a4, mu, alfa, z) de la G-g pesada
    en el corte X = 0: mural {z, m} U A_big U polvo en c' = Y - w
    >= max(1 + z, cola(Y) - w), cola = (1+SS+alfa+z)/phi.  La
    capacidad NO contiene las piezas: esquinas simples con clamps
    de ventana.  None = sin puntos reales."""
    wl, wh, s2l, s2h, SSl, SSh, bl, bh = box[:8]
    als = [(box[i], box[i + 1]) for i in range(8, 16, 2)]
    mul, muh = box[16], box[17]
    al_, ah_ = box[18], box[19]
    zl, zh = box[20], box[21]
    # podas exactas (dominio pesado + particion)
    if SSh <= 1.0 or SSl > PHI:
        return None
    if 2.0 * s2l > SSh:
        return None                    # s1 >= s2
    if any(a_l > PHI / 2 for a_l, _ in als):
        return None                    # SS >= beta + a >= 2a <= phi
    if any(a_l > 0 and a_h + bh <= 1.0 for a_l, a_h in als):
        return None
    if mul > 0 and bh <= BSTAR:
        return None
    if mul > 0 and sum(1 for a_l, _ in als if a_l > T0) >= 4:
        return None                    # refuerzo: big = 4 y polvo
                                       # incompatibles (4 t0 = phi-1)
    lo_t = bl + sum(a_l for a_l, _ in als) + mul
    hi_t = bh + sum(min(a_h, 1.0) for _, a_h in als) + muh
    if lo_t > SSh or hi_t < SSl:
        return None
    if any(bh < a_l for a_l, _ in als):
        return None
    # ventanas especulares (X = 0): alpha in [max(1+w, SS+w),
    # 1 + (SS - beta) + w); z in [alpha + w, alpha + s2 + w)
    a_lo = max(al_, 1.0 + wl, SSl + wl)
    a_hi = min(ah_, 1.0 + (SSh - bl) + wh)
    if a_lo >= a_hi:
        return None
    z_lo = max(zl, a_lo + wl)
    z_hi = min(zh, a_hi + s2h + wh)
    if z_lo >= z_hi:
        return None
    # ventana de Y no vacia: max(cola, 1+z+w) < SS + z + w
    cola_lo = (1.0 + SSl + a_lo + z_lo) / PHI
    if cola_lo >= SSh + z_hi + wh:
        return None
    c_lo = max(1.0 + z_lo, cola_lo - wh)
    # nodos: 0 = z, 1 = m, 2.. = A_big, ultimo = polvo.  TECHOS
    # CLAMPADOS POR LA LIGADURA (masa fantasma: la capacidad c' es
    # fija, y sin este clamp las cajas con Sigma techos > phi jamas
    # certifican): a_i <= SS - beta - resto - mu
    a_effs = []
    for k, (a_l, a_h) in enumerate(als):
        resto = bl + mul + sum(als[j][0] for j in range(4)
                               if j != k)
        a_effs.append(min(a_h, PHI / 2, SSh - resto))
    if any(e < a_l for e, (a_l, _) in zip(a_effs, als)):
        return None                    # ligadura por hueco
    mu_eff = min(muh, SSh - bl - sum(a_l for a_l, _ in als),
                 5 * T0)
    if mu_eff < mul:
        return None
    hi = [z_hi, 1.0] + [e for e, (_, a_h) in zip(a_effs, als)
                        if a_h > 0]
    es_polvo = [False] * len(hi)
    if mu_eff > 0 and muh > 0:
        hi.append(T0)
        es_polvo.append(True)
    n = len(hi)
    if c_lo <= max(hi[1:] + [1.0]) + 1e-12:
        return False                   # sin resolver: partir
    thmat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if i == 0:
                # pares con z: esquina ACOPLADA al suelo c' >= 1+z
                # (theta(z, x; 1+z) crece en z: d/dz ~ 1-x >= 0)
                # y tambien vale el suelo global: minimo de ambas
                t_ac = th(z_hi, hi[j], 1.0 + z_hi)
                t_gl = th(z_hi, hi[j], c_lo) if c_lo > z_hi + 1e-12 \
                    else PI
                thmat[i][j] = min(t_ac, t_gl)
            else:
                thmat[i][j] = th(hi[i], hi[j], c_lo)
    D = D_polvo(mu_eff, c_lo) if mu_eff > 0 and muh > 0 else 0.0
    return antipodal_dos_lados(hi, thmat, es_polvo, D)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] el lema de reduccion 1/(4 phi)")
    import sympy as sp
    ok = True
    # (a) algebra exacta en Q(sqrt5): t0 = (phi-1)/4 = 1/(4 phi);
    #     beta* = (9-sqrt5)/8; 5 t0 = phi - beta* EXACTO; y el caso
    #     beta <= beta*: (phi-beta)/(1-beta) <= 5 sii beta <= beta*
    s5 = sp.sqrt(5)
    phi = (1 + s5) / 2
    t0 = (phi - 1) / 4
    bstar = (9 - s5) / 8
    ok &= check("algebra exacta (Q(sqrt5)): t0 = (phi-1)/4 = "
                "1/(4 phi) (phi(phi-1) = 1); 5 t0 = 5(sqrt5-1)/8 = "
                "phi - beta* EXACTO con beta* = (9-sqrt5)/8; y "
                "(phi-beta)/(1-beta) <= 5 sii beta <= beta* "
                "(equivalencia lineal)",
                sp.simplify(t0 - 1 / (4 * phi)) == 0
                and sp.simplify(5 * t0 - (phi - bstar)) == 0
                and sp.simplify((phi - bstar) - 5 * (1 - bstar))
                == 0)
    ok &= check("[ENUNCIADO] LEMA: con B* = mejor subconjunto <= 1 "
                "(la particion adversariada de G-e) y Sigma_S <= "
                "phi, piezas < 1: (i) a + beta > 1 para toda a en "
                "A (maximalidad) y beta >= sigma_1 >= max A ({s1} "
                "es candidato); (ii) |{a en A: a > t0}| <= 4 "
                "SIEMPRE — beta <= beta*: |A| < (phi-beta)/"
                "(1-beta) <= 5 y toda a > 1-beta >= 1-beta* = t0; "
                "beta > beta*: cinco piezas > t0 sumarian > 5 t0 = "
                "phi - beta* >= phi - beta >= Sigma A, "
                "contradiccion; (iii) polvo (<= t0) solo si beta > "
                "beta*, con masa mu <= phi - beta < 5 t0 = 0.7725; "
                "(iv) REFUERZO (acta): 4 t0 = phi - 1 EXACTO => "
                "|A_big| = 4 y polvo son INCOMPATIBLES (con 4 "
                "grandes, mu < phi - beta - (phi-1) = 1 - beta < "
                "toda pieza de polvo): el mural real tiene <= 6 "
                "nodos y el modelo de 7 es superconjunto estricto",
                True)
    # (b) convexidad del asin y la cota por termino del polvo
    x = sp.symbols('x', positive=True)
    d2 = sp.diff(sp.asin(x), x, 2)
    ok &= check("convexidad (sympy): d2/dx2 asin(x) = "
                "x/(1-x^2)^(3/2) >= 0 en [0,1) => asin((u+v)/2) <= "
                "(asin u + asin v)/2; con AM-GM sqrt(uv) <= "
                "(u+v)/2 y asin creciente: theta(a,b) = "
                "2 asin(sqrt(f(a) f(b))) <= asin f(a) + asin f(b)",
                sp.simplify(d2 - x / (1 - x ** 2) ** sp.Rational(
                    3, 2)) == 0)
    # (c) fuzz de la particion: |A_big| <= 4 y las propiedades (i)
    rng = random.Random(SEED)
    n_f, peor_big = 0, 0
    viol = 0
    for _ in range(25000):
        p = rng.randrange(2, 12)
        t = rng.uniform(1.001, PHI)
        piezas = [rng.uniform(0.01, 0.999) for _ in range(p)]
        esc = t / sum(piezas)
        piezas = sorted((min(0.999, x * esc) for x in piezas),
                        reverse=True)
        SS = sum(piezas)
        if SS <= 1.0 or SS > PHI:
            continue
        beta, A = b_star_particion(piezas)
        n_f += 1
        big = [a for a in A if a > T0]
        peor_big = max(peor_big, len(big))
        if len(big) > 4 or any(a + beta <= 1.0 + 1e-12 for a in A) \
                or (A and beta + 1e-12 < max(A)) \
                or sum(a for a in A if a <= T0) >= 5 * T0:
            viol += 1
    ok &= check(f"fuzz de la particion ({n_f} perfiles legales, "
                f"2-11 piezas): |A_big| <= 4 en todos (max "
                f"observado {peor_big}), maximalidad y beta >= "
                f"max A y masa de polvo < 5 t0 sin excepciones "
                f"({viol} violaciones)", n_f > 2000 and viol == 0)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] el bloque de polvo: coste por masa")
    ok = True
    ok &= check("[ENUNCIADO] cadena de polvo (piezas d_i <= t0, "
                "masa mu, radio R): suma consecutiva interna <= "
                "Sigma (asin f(d_i) + asin f(d_i+1)) <= "
                "2 Sigma asin f(d_i) <= pi Sigma d_i/(R - t0) = "
                "pi mu/(R - t0) — INDEPENDIENTE del numero de "
                "piezas (asin x <= pi x/2 en [0,1]); los extremos "
                "del bloque se mayoran con talla t0 (theta "
                "monotona) y los arcos que ACABAN dentro del "
                "bloque quedan cubiertos por el arco al borde "
                "atomico (requisito mayorado por t0 + camino "
                "creciente)", True)
    # fuzz: cadenas de polvo aleatorias vs la cota
    rng = random.Random(SEED + 3)
    n_f, viol, peor_ratio = 0, 0, 0.0
    for _ in range(4000):
        R = rng.uniform(2.0, 8.0)
        r = rng.randrange(2, 30)
        ds = [rng.uniform(0.005, T0) for _ in range(r)]
        mu = sum(ds)
        suma = sum(theta_w(ds[i], ds[i + 1], R)
                   for i in range(r - 1))
        cota = D_polvo(mu, R)
        n_f += 1
        if suma > cota + 1e-12:
            viol += 1
        peor_ratio = max(peor_ratio, suma / cota)
    ok &= check(f"fuzz del bloque ({n_f} cadenas, 2-29 piezas): "
                f"suma consecutiva <= pi mu/(R - t0) en todas "
                f"({viol} violaciones; peor cociente "
                f"{peor_ratio:.3f})", viol == 0 and peor_ratio < 1)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] G-e pesada (DR) certificada")
    ok = True
    root = [1.0, Y_MAX_E, 1.0, PHI, T0, 1.0,
            0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0,
            0.0, 5 * T0]
    exito, caja, n, cert = bnb_factible(root, criterio_ge)
    ok &= check(f"G-e pesada CERTIFICADA (caja del barrido: Y <= "
                f"SS + 1.6 <= {Y_MAX_E:.2f}; piezas < 1; particion "
                f"B*): el mural {{Y, m}} U A_big(<= 4) U polvo cabe "
                f"en c = Sigma_S + Y en toda la caja — via el lema "
                f"de reduccion + antipodal de dos lados; {n} cajas "
                f"vistas, {cert} certificadas"
                + ("" if exito else f"; CAJA SIN RESOLVER {caja}"),
                exito)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] G-g pesada especular (corte X = 0) certificada")
    ok = True
    a_max = 1.0 + (PHI - T0) + 1.6
    z_max = a_max + 1.0 + 1.6
    root = [0.0, 1.6, 0.0, 1.0, 1.0, PHI, T0, 1.0,
            0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0,
            0.0, 5 * T0, 1.0, a_max, 1.0, z_max]
    exito, caja, n, cert = bnb_factible(root, criterio_gg)
    ok &= check(f"G-g pesada CERTIFICADA en el corte X = 0 (omega "
                f"<= 1.6, alpha <= {a_max:.2f}, z <= {z_max:.2f}): "
                f"el mural {{z, m}} U A_big U polvo cabe en c' = "
                f"Y - omega >= max(1 + z, cola(Y) - omega) en toda "
                f"la caja; {n} cajas vistas, {cert} certificadas"
                + ("" if exito else f"; CAJA SIN RESOLVER {caja}"),
                exito)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles y alcance honesto")
    ok = True
    # (a) sanity end-to-end: instancias aleatorias de G-e pesada
    #     con la particion real: el criterio de caja-punto coincide
    #     con corona_suf (que ya barria el MC)
    rng = random.Random(SEED + 5)
    n_s, viol = 0, 0
    while n_s < 200:
        p = rng.randrange(3, 10)
        piezas = sorted((rng.uniform(0.05, 0.98)
                         for _ in range(p)), reverse=True)
        SS = sum(piezas)
        s2 = piezas[1]
        if SS < 1.0 + s2 or SS > PHI:
            continue
        w = rng.uniform(0.01, 1.6)
        if 1.0 + w >= SS + w:
            continue
        Y = rng.uniform(1.0 + w, SS + w)
        beta, A = b_star_particion(piezas)
        big = sorted((a for a in A if a > T0), reverse=True)
        mu = sum(a for a in A if a <= T0)
        if len(big) > 4:
            continue
        n_s += 1
        eps = 1e-9
        caja = [Y, Y + eps, SS, SS + eps, beta, beta + eps]
        for k in range(4):
            v = big[k] if k < len(big) else 0.0
            caja += [v, v + (eps if v > 0 else 0.0)]
        caja += [mu, mu + (eps if mu > 0 else 0.0)]
        r = criterio_ge(tuple(caja))
        okc, _ = corona_suf(sorted([Y, 1.0] + A, reverse=True),
                            SS + Y)
        if okc and r is not True:
            viol += 1
    ok &= check(f"(a) sanity end-to-end ({n_s} instancias pesadas "
                f"reales): donde corona_suf cabe, el criterio de "
                f"caja-punto tambien certifica ({viol} "
                f"discrepancias) — el certificado no es mas debil "
                f"que el MC que sustituye", viol == 0)
    # (b) control negativo: el antipodal con un bloque de polvo de
    #     coste D > 2 pi no puede certificar por ningun reparto
    tam3 = [2.0, 1.0, T0]
    mat3 = [[0.0, 2.0, 0.3], [0.0, 0.0, 0.3], [0.0, 0.0, 0.0]]
    r_mala = antipodal_dos_lados(tam3, mat3, [False, False, True],
                                 D=10.0)
    ok &= check(f"(b) control negativo: bloque de polvo con coste "
                f"interno D = 10 > pi: antipodal_dos_lados = "
                f"{r_mala} — la cota de masa impide certificar lo "
                f"imposible", r_mala is False)
    ok &= check("[ENUNCIADO] alcance honesto: cajas del barrido MC "
                "(omega <= 1.6; Y < SS + omega en G-e; corte X = 0 "
                "en G-g pesada — sus X > 0 y omega > 1.6 siguen "
                "como MC adversariado, puertocii G-e/G-g).  El "
                "lema de reduccion es EXACTO (algebra); los "
                "cierres son certificados-por-subdivision.  Con "
                "esto, TODAS las ramas multipieza de R2b con "
                "tarifa derivada quedan certificadas salvo las "
                "X_Y > 0 / X > 0 declaradas", True)
    return ok


def main():
    print("=" * 68)
    print("REDUCCION DE |A|: las pesadas de R2b certificadas "
          "(drafts/areduccion.md)")
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
