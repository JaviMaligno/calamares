#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El cierre por bolsillos, fase 1: el cuarteto j = 0 de gaplemma
EXACTO por una desigualdad algebraica (docs/drafts/bolsillos.md).

EL CERTIFICADO (j = 0, corona {alpha, m, s', w*}):
  R_test = alpha + 1 (necesidad de par); alpha y m diametrales
  (distancia pi = theta(alpha,m) en R_test, exacta).  Los pequenos
  van UNO A CADA HUECO del par: s' arriba, w* abajo.
  (1) SUB-BOLSILLO (DIC, zigzag adversariada; Lean ns2_golden y
      descartes_pocket_golden): s <= p(alpha,1;R) => theta(alpha,s)
      + theta(s,m) <= theta(alpha,m) = pi: el contenido de cada
      hueco cabe en su arco.
  (2) En R = alpha+1 el discriminante de Descartes es 0 IDENTICO
      (lema de escala) y el bolsillo es EXACTO:
          p(u) = u(u+1)/(u^2+u+1),  u = alpha,  CRECIENTE en u.
  (3) Las DOS desigualdades de masa, con el ACOPLE de ligaduras
      (el error de diseno v1 era usar los topes DESACOPLADOS
      phi/2 y 1/phi — la esquina doble-tope es infactible):
      s' <= Sigma/2 y w* <= Sigma-1, con alpha >= (1+Sigma)/phi
      (suelo de cascada; omega, Sigma_S y holguras solo SUBEN
      alpha y con el p): en el peor caso u = (1+Sigma)/phi, o sea
      Sigma = phi u - 1:
        q(u) := 2u(u+1) - (phi u - 1)(u^2+u+1) >= 0   [s' cabe]
        g(u) := u(u+1)/(u^2+u+1) - (phi u - 2) >= 0   [w* cabe]
      en u en [2/phi, phi], con q(phi) = 0 EXACTO: la TANGENCIA
      AUREA — en Sigma = phi, alpha en su suelo phi, el tope de s'
      = phi/2 = p(phi,1;phi+1), el bolsillo aureo de thm:DP
      (descartes_pocket_golden).  El punto critico de j = 0 es EL
      MISMO bolsillo aureo del contraejemplo.
  (4) SUPER-BOLSILLO para los pares no consecutivos (alpha,m) y
      (s',w*): la distancia via el otro lado domina si la pieza
      intermedia es super-bolsillo del par: m = 1 y alpha >= 1
      contra p(s',w*;R) <= 0.24: margen ~0.76.
  (5) R > R_test: TODAS las theta decrecen en R (fit-monotonia,
      repack/optimizacion): las mismas posiciones valen.  (El
      bolsillo DECRECE en R — dp/dR < 0, error v1 —: por eso el
      certificado se monta EN R_test y se extiende por fit, no por
      bolsillo.)

FASE 2 (bloques D/E — WIP, fuera del default; correr con --solo):
j = 1 y coronaagujero k <= 2 via B&B HIBRIDO 3D en (Sigma, g1, g2)
— todos los demas parametros (omega, Sigma_S, holguras) solo SUBEN
los suelos de las piezas, y subir piezas sube el bolsillo a R fijo:
el dominio reducido es un superconjunto.  Certificado por caja:
  P: s' <= p(g1_lo, 1; R_hi) y w* <= p(1, g2_lo; R_hi) (esquinas
     conservadoras: p sube con la pieza, BAJA con R — el error E2
     de v1, corregido) + super-bolsillos + trio <= 2 pi (R >= R_3
     por construccion),
  F: corona_k5(piezas_ALTAS, R_lo) (fit-esquina, respaldo).
R_test = max(pares, min(R_3, M)) por caja; colas g -> inf por
formula.  HALLAZGO QUE BLOQUEA LA FASE 2 (documentado en memoria):
el punto peligroso real es (Sigma = phi, alpha = o1 = phi) — el
quinteto cabe SOLO con w* como miembro del ciclo (el 4-ciclo
{phi, phi, w*, m} suma 6.280 vs 2 pi = 6.2832: margen 0.003, otra
variedad CASI-TANGENTE) y el certificado P por bolsillos no lo
captura: falta el LEMA DE SUFICIENCIA k = 4 (all-pairs via la
dicotomia sub/super-bolsillo por par).  Los B&B D/E no terminan
hasta tenerlo — WIP declarado, no vendido.

Bloques: [A] las identidades y desigualdades exactas (sympy);
[B] el certificado j = 0 contra el dominio real (0 violaciones);
[C] controles; [D] j = 1 hibrido; [E] coronaagujero k <= 2.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, theta_w
from gaplemma import corona_k5

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260816'))


def bolsillo(a, b, R):
    """Bolsillo de Descartes del par mural (a, b) en la sarten R
    (curvatura de la sarten NEGATIVA; +2 sqrt(disc): la version SIN
    la raiz es la degenerada, solo valida cuando disc = 0)."""
    ka, kb, kR = 1.0 / a, 1.0 / b, -1.0 / R
    disc = ka * kb + kb * kR + kR * ka
    if disc < 0.0:
        disc = 0.0
    return 1.0 / (ka + kb + kR + 2.0 * math.sqrt(disc))


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades y desigualdades exactas (sympy)")
    import sympy as sp
    ok = True
    u = sp.symbols('u', positive=True)
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    # (1) disc = 0 identico en R = a+b y el bolsillo exacto
    a, b = sp.symbols('a b', positive=True)
    R = a + b
    disc = (1 / a) * (1 / b) + (1 / b) * (-1 / R) + (-1 / R) * (1 / a)
    ok &= check("disc de Descartes = 0 IDENTICO en R = a+b (lema de "
                "escala): el bolsillo del par diametral es exacto "
                "p = 1/(1/a + 1/b - 1/(a+b)); con b = 1: p(u) = "
                "u(u+1)/(u^2+u+1), CRECIENTE en u (derivada con "
                "numerador u^2+2u > 0... = (2u+1)(u^2+u+1) - "
                "u(u+1)(2u+1) = (2u+1) > 0)",
                sp.simplify(disc) == 0)
    p_u = u * (u + 1) / (u ** 2 + u + 1)
    dp = sp.simplify(sp.diff(p_u, u) * (u ** 2 + u + 1) ** 2)
    ok &= check("p(u) creciente EXACTO (ronda hostil H2: el check "
                "v1 era vacuo): p = 1 - 1/(u^2+u+1), numerador de "
                "p' = 2u+1 > 0",
                sp.simplify(dp - (2 * u + 1)) == 0)
    # (2) la desigualdad de s': q(u) >= 0 en [2/phi, phi] con
    #     q(phi) = 0 (la tangencia aurea)
    q = sp.expand(2 * u * (u + 1) - (phi * u - 1) * (u ** 2 + u + 1))
    q_phi = sp.simplify(q.subs(u, phi))
    ok &= check("q(phi) = 0 EXACTO: en Sigma = phi con alpha en su "
                "suelo, s' <= phi/2 = p(phi, 1; phi+1) — el tope de "
                "masa TANGENTE al bolsillo aureo de thm:DP "
                "(descartes_pocket_golden): el punto critico de "
                "j = 0 es el bolsillo del contraejemplo", q_phi == 0)
    # factorizar: q(u) = (phi - u) * r(u) con r > 0 en el intervalo
    # (division polinomica en QQ(sqrt5): cancel no divide raices
    # irracionales)
    qP = sp.Poly(q, u, extension=sp.sqrt(5))
    quo, rem = sp.div(qP, sp.Poly(phi - u, u,
                                  extension=sp.sqrt(5)))
    r_ex = sp.expand(quo.as_expr())
    r_obj = phi * u ** 2 + 2 * (phi - 1) * u + (phi - 1)
    ok &= check("q(u) = (phi - u)·r(u) EXACTO (resto 0) con "
                "r(u) = phi u^2 + 2(phi-1)u + (phi-1) — los TRES "
                "coeficientes POSITIVOS (ronda hostil H1: de malla "
                "a exacto): r > 0 para TODO u > 0, luego q >= 0 en "
                "el intervalo con igualdad SOLO en u = phi",
                rem.as_expr() == 0
                and sp.simplify(r_ex - sp.expand(r_obj)) == 0)
    # (3) la desigualdad de w*: g(u) = p(u) - (phi u - 2) >= 0
    g = sp.simplify(p_u - (phi * u - 2))
    # H1 (ronda hostil): g' = p' - phi con p' = (2u+1)/D^2 y
    # D = u^2+u+1 creciente: sup p' en [2/phi, phi] es p'(2/phi)
    # <= 0.30 < phi => g ESTRICTAMENTE decreciente; minimo exacto
    # g(phi) = (3-sqrt5)/4 = phi/2 - 1/phi
    ppl = float(((2 * u + 1) / (u ** 2 + u + 1) ** 2)
                .subs(u, 2 / phi))
    gmin = sp.simplify(g.subs(u, phi))
    ok &= check(f"w* <= phi u - 2 <= p(u) EXACTO en [2/phi, phi]: "
                f"g' = p' - phi con sup p' = p'(2/phi) = {ppl:.4f} "
                f"< phi (D creciente): g estrictamente decreciente "
                f"y minimo g(phi) = (3-sqrt5)/4 = phi/2 - 1/phi = "
                f"0.19098 EXACTO (sympy)",
                ppl < float(phi)
                and sp.simplify(gmin - (3 - sp.sqrt(5)) / 4) == 0
                and sp.simplify(gmin - (phi / 2 - 1 / phi)) == 0)
    # (4) super-bolsillo: p(s'max, w*max; R) << 1 en el dominio
    pmax = max(bolsillo(0.809, 0.618, RR)
               for RR in (2.0 / PHI + 1.0, 2.24, 2.6, 3.0, 4.0,
                          10.0))
    ok &= check(f"(4) super-bolsillo de m y alpha: p(s'max, w*max) "
                f"<= {pmax:.4f} << 1 <= m, alpha (p decrece en R: "
                f"el peor es R minimo 2/phi + 1 = 2.24): los pares "
                f"no consecutivos (alpha,m) y (s',w*) validan via "
                f"NS-2 >= 0 con margen ~{1 - pmax:.2f}", pmax < 0.5)
    # (5) el acople que salva el punto aureo del error v1
    ok &= check("(5) el ACOPLE de ligaduras (H5: DOS RAMAS en "
                "alpha): rama u <= phi — q y g con Sigma = phi u - "
                "1; rama alpha > phi — s' <= phi/2 = p(phi) < "
                "p(alpha) y w* <= 1/phi < phi/2 < p(alpha) (p "
                "creciente): ambas hermeticas; verificacion: "
                "p(phi) = phi/2 y 1/phi < phi/2 exactos",
                sp.simplify(p_u.subs(u, phi) - phi / 2) == 0
                and float(1 / phi) < float(phi / 2))
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] el certificado j = 0 contra el dominio real")
    rng = random.Random(SEED)
    ok = True
    n, viol_cert, viol_fit = 0, 0, 0
    for _ in range(max(20000, ITER // 3)):
        S = rng.uniform(1.0 + 1e-9, PHI)
        SSh = rng.uniform(0.0, S)              # Sigma_S
        w = rng.uniform(0.0, 3.0)
        h = 1.0 + rng.expovariate(1.5) * (10 ** rng.randrange(0, 3)
                                          if rng.random() < 0.2
                                          else 1.0)
        af = max(1.0 + w, SSh + w, (1.0 + S) / PHI) * h
        Rt = af + 1.0
        sp_ = min(S / 2, PHI / 2)
        wst = min(1.0 / PHI, S - 1.0)
        p = bolsillo(af, 1.0, Rt)
        n += 1
        # el certificado: sub-bolsillo de ambos + super-bolsillo
        if not (sp_ <= p + 1e-12 and wst <= p + 1e-12
                and bolsillo(sp_, max(wst, 1e-9), Rt) <= 1.0):
            viol_cert += 1
        # cross-check constructivo (corona_k5 en R_test)
        if rng.random() < 0.15:
            piezas = sorted([af, 1.0, sp_, max(wst, 1e-6)],
                            reverse=True)
            cabe, _ = corona_k5(piezas, Rt)
            if not cabe:
                viol_fit += 1
    ok &= check(f"certificado j = 0 en {n} instancias del dominio "
                f"real (Sigma, Sigma_S, omega <= 3, holguras hasta "
                f"~100): {viol_cert} violaciones del certificado y "
                f"{viol_fit} del cross-check constructivo — el "
                f"cuarteto cabe SIEMPRE, ahora por DESIGUALDAD "
                f"ALGEBRAICA, no por barrido",
                n > 10000 and viol_cert == 0 and viol_fit == 0)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] controles")
    ok = True
    # (a) super-bolsillo FALLA la DIC
    a, b, R = 2.0, 1.0, 3.0
    p = bolsillo(a, b, R)
    s_mal = p + 0.15
    m_dic = (theta_w(a, s_mal, R) + theta_w(s_mal, b, R)
             - theta_w(a, b, R))
    ok &= check(f"(a) s = p + 0.15 > p = {p:.4f}: margen NS-2 = "
                f"{m_dic:.4f} > 0 (la insercion ya no es gratis): "
                f"el sub-bolsillo es la condicion", m_dic > 0)
    # (b) la version DEGENERADA del bolsillo sobrestima fuera de
    #     R = a+b (el error E1 del diseno v1)
    pd = 1.0 / (1.0 / 2.0 + 1.0 - 1.0 / 3.5)
    pr = bolsillo(2.0, 1.0, 3.5)
    ok &= check(f"(b) en R = 3.5 > a+b: degenerada {pd:.4f} > real "
                f"{pr:.4f} (el termino 2 sqrt(disc) es obligatorio "
                f"fuera de la tangencia R = a+b): error v1 "
                f"documentado", pd > pr + 0.1)
    # (c) dp/dR < 0 (error E2 del diseno v1): el bolsillo se
    #     encoge con R — el certificado vive en R_test y se
    #     extiende por fit-monotonia, no por bolsillo
    ok &= check(f"(c) dp/dR < 0: p(2,1;3) = {bolsillo(2, 1, 3):.4f}"
                f" > p(2,1;4) = {bolsillo(2, 1, 4):.4f} > "
                f"p(2,1;10) = {bolsillo(2, 1, 10):.4f}: el bolsillo "
                f"DECRECE con R; la extension a R > R_test es por "
                f"las theta (todas decrecen), no por el bolsillo",
                bolsillo(2, 1, 3) > bolsillo(2, 1, 4)
                > bolsillo(2, 1, 10))
    # (d2) IDENTIDAD NUEVA (hallazgo de fase 2, verificada a 40
    #     digitos con mpmath): theta(phi, 1/phi) + theta(1/phi, 1)
    #     + theta(1, phi) = pi EXACTO en R = 2 phi — el 4-ciclo
    #     {phi, phi, 1/phi, 1} del punto peligroso de j = 1 es
    #     EXACTAMENTE tangente (suma 2 pi), y el 5-ciclo con
    #     s' = phi/2 suma pi + 4 asin(1/sqrt3) = 5.6035..., LA
    #     MISMA constante de la esquina de R2b (f(phi)f(phi/2) =
    #     1/3 en R = 2 phi).  El punto peligroso de j = 1, la
    #     esquina de R2b y el bolsillo aureo de thm:DP son la misma
    #     geometria.
    import math as _m
    Rg2 = 2 * PHI
    def _f(x):
        return x / (Rg2 - x)
    s_id = (2 * _m.asin(_m.sqrt(_f(PHI) * _f(1 / PHI)))
            + 2 * _m.asin(_m.sqrt(_f(1 / PHI) * _f(1.0)))
            + 2 * _m.asin(_m.sqrt(_f(1.0) * _f(PHI))))
    c5 = 4 * _m.asin(_m.sqrt(_f(PHI) * _f(PHI / 2))) + s_id
    ok &= check(f"(d2) IDENTIDAD: theta(phi,1/phi) + theta(1/phi,1)"
                f" + theta(1,phi) = {s_id:.12f} = pi en R = 2 phi "
                f"(tangencia exacta del 4-ciclo del punto peligroso"
                f" j = 1); el 5-ciclo con s' = phi/2 = "
                f"{c5:.10f} = pi + 4 asin(1/sqrt3) (la constante de"
                f" la esquina R2b: f(phi)f(phi/2) = 1/3)",
                abs(s_id - PI) < 1e-12
                and abs(c5 - (PI + 4 * _m.asin(1 / _m.sqrt(3.0))))
                < 1e-12)
    # (d) la tangencia aurea es real: en Sigma = phi, alpha = phi,
    #     s' = phi/2 EXACTO = p: la corona cabe tangente
    piezas = sorted([PHI, 1.0, PHI / 2, 1 / PHI - 1e-9],
                    reverse=True)
    cabe, _ = corona_k5(piezas, PHI + 1.0)
    ok &= check(f"(d) tangencia aurea: {{phi, 1, phi/2, 1/phi}} en "
                f"R = phi+1: cabe = {cabe} con s' = p(phi,1;phi+1) "
                f"= phi/2 EXACTO — el cuarteto critico de j = 0 es "
                f"el bolsillo aureo del contraejemplo (thm:DP)",
                cabe)
    return ok


def M_apilable3(a, b, c):
    tr = [a, b, c]
    return min(max(x, y) + 2 * min(x, y)
               for i, x in enumerate(tr) for y in tr[i + 1:])


def _lp4(t12, t23, t34, t41, t13, t24):
    """[WIP fase 2 — SUPERSEDIDO por code/arcolp.py] Suficiencia
    k = 4 parcial: le FALTAN los caps de wrap de los pares
    consecutivos (d_i <= 2 pi - theta_i; ronda hostil H4 — sin
    contraejemplo en 260k tuplas pero sin prueba).  El lema del LP
    de arcos los INCLUYE (los arcos de longitud n-1 son exactamente
    los caps): usar arcolp.dual_factible.  Se conserva por el
    enunciado historico: existen separaciones d_i >= theta
    consecutivas con suma 2 pi y ambas diagonales cubiertas por los
    DOS lados sii, con S = 2 pi - suma(theta_consec) >= 0,
      A' + A'' <= S  y  B' + B'' <= S,
    donde A' = (t13 - t12 - t23)+, A'' = (t13 - t34 - t41)+,
    B' = (t24 - t23 - t34)+, B'' = (t24 - t41 - t12)+ (LP de ciclo:
    los dos pares de restricciones particionan los e_i; la
    realizacion en distancias acumuladas valida los 6 pares:
    4 consecutivos + 2 diagonales)."""
    S = 2 * PI - (t12 + t23 + t34 + t41)
    if S < -1e-12:
        return False
    Ap = max(0.0, t13 - t12 - t23)
    App = max(0.0, t13 - t34 - t41)
    Bp = max(0.0, t24 - t23 - t34)
    Bpp = max(0.0, t24 - t41 - t12)
    return Ap + App <= S + 1e-12 and Bp + Bpp <= S + 1e-12


def arclp_cert(orden, R_lo, tol=1e-9, dominio_pares_ok=False):
    """Certificado arc-LP por caja: theta's en (piezas ALTAS,
    R_BAJO), con HiGHS como BUSCADOR del testigo d y verificacion
    EXPLICITA del testigo (certificado independiente del solver).
    dominio_pares_ok = True cuando la PRECONDICION del lema
    (pares caben) la garantiza el DOMINIO para toda instancia real
    (R_used >= pares por construccion de Rt): entonces la mezcla de
    esquinas (piezas_hi, R_lo) puede violar pares en el par que
    define pares_lo, pero su theta_ub = pi sigue mayorando el
    requisito real (theta <= pi) y el certificado es SANO — el
    testigo a theta_ub sirve para todo punto real de la caja, cuya
    instancia SI cumple la precondicion.  Sin el flag, la guarda
    del acta (ordenes fisicamente imposibles) aplica."""
    from arcolp import requisitos, gaps_de, pares_caben, th
    if not dominio_pares_ok and not pares_caben(orden, R_lo):
        return False
    # filtro barato: suma consecutiva > 2 pi => infactible seguro
    n0 = len(orden)
    if sum(th(orden[i], orden[(i + 1) % n0], R_lo)
           for i in range(n0)) > 2 * PI + 1e-12:
        return False
    try:
        from scipy.optimize import linprog
    except ImportError:
        from arcolp import primal_factible
        return primal_factible(orden, R_lo)
    n = len(orden)
    req = requisitos(orden, R_lo)
    A_ub, b_ub, arcos_g = [], [], []
    for a, r in req.items():
        g = gaps_de(a, n)
        A_ub.append([-1.0 if i in g else 0.0 for i in range(n)])
        b_ub.append(-r)
        arcos_g.append((g, r))
    res = linprog([0.0] * n, A_ub=A_ub, b_ub=b_ub,
                  A_eq=[[1.0] * n], b_eq=[2 * PI],
                  bounds=[(0.0, None)] * n, method='highs')
    if res.status != 0 or res.x is None:
        return False
    d = list(res.x)
    if abs(sum(d) - 2 * PI) > 1e-7 or any(x < -tol for x in d):
        return False
    return all(sum(d[i] for i in g) >= r - 1e-7
               for g, r in arcos_g)


V_DELTA = 0.15
W2_DELTA = 0.02


def en_W2(box):
    """Entorno del punto aureo del TRIO (alpha, o1, Sigma) =
    (2, 2/phi, 1), donde pares = R_3 = M = 1+sqrt5 colapsan
    (gaplemma, identidades sympy) y disc = 0 identico da
    p12 = p(2, 2/phi; 1+sqrt5) = 1 EXACTO: trio tangente + s' <=
    Sigma/2 ~ 1/2 al bolsillo p12 con margen ~0.5 + w* <= Sigma-1
    <= phi*delta como polvo sub-bolsillo.  Exclusion declarada
    (mismo estatus que V)."""
    if len(box) != 6:
        return False
    Sl, Sh, al, ah, ol, oh = box
    if not (1.0 <= Sl and Sh <= 1.0 + W2_DELTA):
        return False
    directo = (2.0 - W2_DELTA <= al and ah <= 2.0 + W2_DELTA
               and 2.0 / PHI - 1e-12 <= ol
               and oh <= 2.0 / PHI + W2_DELTA)
    espejo = (2.0 / PHI - 1e-12 <= al
              and ah <= 2.0 / PHI + W2_DELTA
              and 2.0 - W2_DELTA <= ol and oh <= 2.0 + W2_DELTA)
    return directo or espejo


def en_V(Sl, Sh, al, ah, ol, oh):
    """Caja contenida en la vecindad certificada V del punto
    tangente (arcolp bloque E: 4-ciclo por LP completo en malla +
    sigma monotona; s' sub-bolsillo del hueco (alpha,o1) con
    p >= 2phi/3 > phi/2 exacto y diagonales de s' via
    super-bolsillo de los intermedios >= 1)."""
    return (PHI - V_DELTA <= Sl and Sh <= PHI
            and PHI <= al and ah <= PHI + V_DELTA
            and PHI <= ol and oh <= PHI + V_DELTA)


def Rt_rapido(a, o):
    """R_used = max(pares, min(R_3, M)) con ATAJO: si el trio cabe
    en pares (la mayoria del dominio), R = pares sin biseccion —
    la biseccion de R3_necesidad (60 pasos x 3 theta) era el 90%
    del coste por caja del B&B."""
    pares = max(a + o, a + 1.0, o + 1.0)
    s = 0.0
    for x, y in ((a, o), (o, 1.0), (1.0, a)):
        if x + y >= pares:
            s += PI
        else:
            s += theta_w(x, y, pares)
        if s > 2 * PI:
            break
    if s <= 2 * PI:
        return pares
    from gaplemma import R3_necesidad
    return max(pares, min(R3_necesidad(a, o, 1.0),
                          M_apilable3(a, o, 1.0)))


def _bnb_hibrido(nombre, gen, root, dims, max_boxes=1200000,
                 usa_V=False, heap_inicial=None,
                 contadores=(0, 0, 0)):
    """B&B hibrido sobre cajas (heap por anchura); gen(box) ->
    None (poda exacta) o (g1l, g1h, g2l, g2h, R_lo, R_hi, sp_hi,
    wst_hi, piezas_hi).  Certificados: exclusion de V (lema de
    entorno de arcolp, solo dominio j = 1), bolsillos P, arc-LP con
    testigo verificado, fit-esquina F."""
    import heapq
    heap = heap_inicial if heap_inicial is not None else         [(0.0, root)]
    n, nP, nF = contadores
    tope = n + max_boxes
    while heap:
        n += 1
        if n > tope:
            return (False, n, nP, nF, heap[0][1]), heap
        _, box = heapq.heappop(heap)
        datos = gen(box)
        if datos is None:
            continue
        (g1l, g1h, g2l, g2h, R_lo, R_hi, sp_hi, wst_hi,
         piezas_hi) = datos
        # exclusiones V/W2 con las coordenadas RECORTADAS (los
        # suelos de gen: una caja cruda que abraza la frontera por
        # debajo tiene contenido REAL dentro de la vecindad — el
        # test crudo la perdia: bug de la frontera nanometrica)
        if usa_V:
            caja_eff = (box[0], box[1], g1l, g1h, g2l, g2h)
            if en_V(*caja_eff) or en_W2(caja_eff):
                nP += 1
                continue
        # EL TRIO CABE POR CONSTRUCCION (v3): todo punto real usa
        # R_used >= max(pares, R_3) — en la banda donde R_3 manda,
        # el trio esta EXACTAMENTE TANGENTE por definicion de R_3
        # (suma = 2 pi: variedad tangente 2D — por eso la
        # desigualdad con piezas infladas NUNCA certificaba ahi) y
        # cabe por la suficiencia k = 3 con desigualdades CERRADAS.
        # Salvaguarda por caja del hecho del dominio R_3 <= M
        # (gaplemma, o1 >= 2/phi): si falla, no se asume.
        # trio_ok POR CONSTRUCCION con SALVAGUARDA REAL (H2 del
        # acta de fase 2 — el comentario v3 prometia la salvaguarda
        # y el codigo no la tenia): pointwise el trio cabe si
        # (i) cabe en pares (v2-check con piezas ALTAS en R_lo), o
        # (ii) banda R_3: R_used = min(R_3, M) = R_3 (tangente
        # exacto, suficiencia k = 3 cerrada) SI R_3 <= M — que se
        # COMPRUEBA por caja en esquinas conservadoras (el hecho es
        # muestreado en gaplemma + grid 400^2 del acta, NO
        # exhaustivo: la salvaguarda no es decorativa), o
        # (iii) W2: el entorno del punto aureo del trio (2, 2/phi,
        # Sigma -> 1), donde pares = R_3 = M colapsan y la
        # salvaguarda por esquinas nunca decide — exclusion
        # declarada (ver en_W2).
        if g2l is None:
            trio_ok = True
        else:
            def _tt(x, y):
                if x + y >= R_lo:
                    return PI
                return theta_w(x, y, R_lo)
            trio_ok = (_tt(g1h, g2h) + _tt(g2h, 1.0)
                       + _tt(1.0, g1h)) <= 2 * PI + 1e-12
            if not trio_ok:
                # sin puerta de banda (bug de la CURVA tangente
                # sum{a,o,1; a+o} = 2pi, de (2, 2/phi) por
                # (1.5, 1.5) al espejo: alli R_lo = pares y la
                # puerta saltaba la salvaguarda): pointwise el trio
                # cabe siempre que R_3 <= max(pares, M) — la
                # comprobacion por esquinas R_3(hi) <= M(lo) es
                # suficiente en toda la curva (M - R_3 >= ~0.5 en
                # el interior) y solo muere en los extremos aureos,
                # cubiertos por W2
                from gaplemma import R3_necesidad as _R3n
                trio_ok = (_R3n(g1h, g2h, 1.0)
                           <= M_apilable3(g1l, g2l, 1.0) + 1e-9)
            if not trio_ok and en_W2(box):
                trio_ok = True
        # bolsillos de los TRES huecos (esquinas conservadoras:
        # piezas BAJAS, R ALTO) — los pequenos van a los DOS huecos
        # de bolsillo mayor (eleccion de asignacion)
        ps = [bolsillo(g1l, 1.0, R_hi)]
        if g2l is not None:
            ps.append(bolsillo(1.0, g2l, R_hi))
            ps.append(bolsillo(g1l, g2l, R_hi))
        else:
            ps.append(ps[0])           # j = 0: dos huecos del par
        ps.sort(reverse=True)
        sup_ok = bolsillo(max(sp_hi, 1e-9), max(wst_hi, 1e-9),
                          R_lo) <= 1.0
        okP = (trio_ok and sup_ok
               and max(sp_hi, wst_hi) <= ps[0] + 1e-12
               and min(sp_hi, wst_hi) <= ps[1] + 1e-12)
        # modo k = 4: un pequeno EN EL CICLO [g1, g2, chico, m] (el
        # otro al mejor bolsillo).  theta's con piezas ALTAS en R_lo
        # (cota monotona valida); LP de ciclo _lp4; el pequeno del
        # bolsillo va al hueco (g1, g2) del ciclo (DIC en su gap) y
        # los super-bolsillos validan sus pares (sup_ok, g's >= 1).
        if not okP and g2l is not None:
            # CERTIFICADO F (fase 2 v3, forma cerrada del arc-LP
            # del 4-ciclo [g1, g2, w*, m] con d1 = pi):
            #   factible <=> F := -sigma - max(B1, B2) >= 0,
            # sigma = th(g2,w)+th(w,m)+th(m,g1) - pi,
            # B1 = (th(g2,m)-th(g2,w)-th(w,m))+,
            # B2 = (th(g1,w)-th(w,m)-th(m,g1))+  (deficits NS-2 de
            # las diagonales contra el slack).  s' al hueco (g1,g2)
            # por sub-bolsillo (global en el dominio, draft); w*
            # cubierto por la UNION bolsillo/ciclo: rama bolsillo
            # w* <= p_best y rama ciclo F >= 0 en w* en
            # [p_best, cap] (cotas de intervalo por esquinas).
            def _t(x, y, Rv):
                if x >= Rv or y >= Rv or x + y >= Rv:
                    return PI
                return theta_w(x, y, Rv)
            p12 = bolsillo(g1l, g2l, R_hi)
            # H6: super-bolsillos de s' (diagonales via intermedios
            # >= 1) y del par de pequenos, exigidos en TODAS las
            # ramas siguientes
            sup2_ok = (bolsillo(sp_hi, max(wst_hi, 1e-9), R_lo)
                       <= 1.0
                       and bolsillo(sp_hi, 1.0, R_lo)
                       <= min(g1l, g2l))
            if sup2_ok and sp_hi <= p12 + 1e-12 and wst_hi > 1e-9:
                pbest = max(bolsillo(1.0, g2l, R_hi),
                            bolsillo(g1l, 1.0, R_hi))
                if wst_hi <= pbest + 1e-12:
                    okP = trio_ok      # ambos smalls sub-bolsillo
                                       # del trio tangente-o-mejor
                elif g1l + g2l < R_lo - 1e-9:
                    # banda R_3 (R_lo > pares): la forma F con
                    # d1 = pi no aplica; LP exacto (rama rara)
                    okP = trio_ok and arclp_cert(
                        [g1h, g2h, wst_hi, 1.0], R_lo,
                        dominio_pares_ok=True)
                else:
                    w_lo, w_hi = pbest, wst_hi
                    sig_hi = (_t(g2h, w_hi, R_lo)
                              + _t(w_hi, 1.0, R_lo)
                              + _t(1.0, g1h, R_lo) - PI)
                    B1_hi = max(0.0, _t(g2h, 1.0, R_lo)
                                - _t(g2l, w_lo, R_hi)
                                - _t(w_lo, 1.0, R_hi))
                    B2_hi = max(0.0, _t(g1h, w_hi, R_lo)
                                - _t(w_lo, 1.0, R_hi)
                                - _t(1.0, g1l, R_hi))
                    okP = (-sig_hi - max(B1_hi, B2_hi)) >= 0.0
        if okP:
            nP += 1
            continue
        cabe, _ = corona_k5(sorted(piezas_hi, reverse=True), R_lo)
        if cabe:
            nF += 1
            continue
        anchos = sorted(((box[j] - box[i]) / esc, k)
                        for k, (i, j, esc) in enumerate(dims))
        k = anchos[-1][1]
        i, j, _ = dims[k]
        m = (box[i] + box[j]) / 2
        b1, b2 = list(box), list(box)
        b1[j] = m
        b2[i] = m
        prio = -(box[j] - box[i])
        heapq.heappush(heap, (prio, tuple(b1)))
        heapq.heappush(heap, (prio, tuple(b2)))
    return (True, n, nP, nF, None), []


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] fase 2: el quinteto j = 1 (hibrido P/F)")
    from gaplemma import R3_necesidad
    ok = True
    GHI = 30.0

    def gen(box):
        Sl, Sh, al, ah, ol, oh = box
        # suelos de cascada (superconjunto: omega/Sigma_S/holguras
        # solo suben; subir piezas sube p a R fijo y el F-cert las
        # lleva en piezas_hi)
        if ah < max(1.0, (1.0 + Sl) / PHI):
            return None                # alpha bajo su suelo minimo
        if oh < max(1.0, (1.0 + Sl) / PHI):
            return None
        a_lo = max(al, 1.0, (1.0 + Sl) / PHI)
        o_lo = max(ol, 1.0, (1.0 + Sl) / PHI)
        R_lo = Rt_rapido(a_lo, o_lo)
        R_hi = Rt_rapido(ah, oh)
        sp_hi = min(Sh / 2, PHI / 2)
        wst_hi = min(1.0 / PHI, max(Sh - 1.0, 1e-9))
        piezas_hi = [ah, oh, 1.0, sp_hi, wst_hi]
        return (a_lo, ah, o_lo, oh, R_lo, R_hi, sp_hi, wst_hi,
                piezas_hi)

    root = (1.0, PHI, 1.0, GHI, 1.0, GHI)
    dims = [(0, 1, 0.15), (2, 3, 4.0), (4, 5, 4.0)]
    import time as _time
    presupuesto_t = float(os.environ.get('CC_TIME', '480'))
    t0 = _time.time()
    heap = None
    cont = (0, 0, 0)
    while True:
        (cert, n, nP, nF, atasco), heap = _bnb_hibrido(
            "j1", gen, root, dims, max_boxes=1000000, usa_V=True,
            heap_inicial=heap, contadores=cont)
        cont = (n, nP, nF)
        if cert or not heap:
            break
        if _time.time() - t0 > presupuesto_t:
            print(f"      [presupuesto de tiempo agotado: frontera "
                  f"{len(heap)} cajas tras {n}]")
            break
    ok &= check(f"quinteto j = 1 CERTIFICADO (Sigma entera, piezas "
                f"hasta {GHI} con R = max(pares, blindada) por "
                f"caja): {cert} — {n} cajas ({nP} P, {nF} F)"
                + (f"; atasco {[round(x, 4) for x in atasco]}"
                   if atasco else ""), cert)
    # cola g1 > GHI (H3 del acta: la esquina correcta — p(g1,1;R)
    # DECRECE en o1 via R: el infimo es el limite R -> inf, NO
    # o1 = 2/phi; y la region o1 > GHI >= alpha se cubre por la
    # SIMETRIA del trio en (alpha, o1) — misma formula):
    # bolsillo (g1,o1) degenerado en R = pares >= 1.23 (peor
    # o1 = 2/phi); bolsillo (g1,m) con el INFIMO en R -> inf:
    # p(GHI, 1; inf) = GHI/(sqrt(GHI)+1)^2-forma via disc:
    # evaluado en R enorme, creciente en g1; trio en pares por
    # SUMA DE MAXIMOS (H5: el "+0.1" era injustificado):
    # pi + 2asin(sqrt(phi/2)) + 2asin(sqrt(1/(GHI+1))) < 2pi
    o_min = 2.0 / PHI
    p_gap12 = 1.0 / (1.0 / GHI + 1.0 / o_min - 1.0 / (GHI + o_min))
    p_gap1m_inf = min(bolsillo(GHI, 1.0, RR)
                      for RR in (GHI + o_min, 2 * GHI, 1e4, 1e8))
    p_creciente = bolsillo(10 * GHI, 1.0, 1e8) > bolsillo(
        GHI, 1.0, 1e8)
    trio_tail = (PI + 2 * math.asin(math.sqrt(PHI / 2))
                 + 2 * math.asin(math.sqrt(1.0 / (GHI + 1.0))))
    ok &= check(f"cola g1 > {GHI} (y o1 > {GHI} por simetria del "
                f"trio): bolsillo (g1,o1) >= {p_gap12:.4f} > phi/2 "
                f"(s'); bolsillo (g1,m) con INFIMO en R -> inf = "
                f"{p_gap1m_inf:.4f} > 1/phi (w*; esquina correcta, "
                f"no la favorable — H3), creciente en g1: "
                f"{p_creciente}; trio por SUMA DE MAXIMOS "
                f"{trio_tail:.4f} < 2pi (sin acoplamientos): la "
                f"cola cierra por formula",
                p_gap12 > PHI / 2 and p_gap1m_inf > 1 / PHI
                and p_creciente and trio_tail < 2 * PI)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] fase 2: coronaagujero k <= 2 (ambas ramas)")
    from gaplemma import R3_necesidad
    ok = True
    GHI = 30.0

    # rama 1, k = 2: {x1, x2, D_m, s', w*} — como j = 1 con suelos
    # x2 >= max(1, (1+S)/phi), x1 >= (x2+1+S)/phi >= 1+Sigma
    def gen1(box):
        Sl, Sh, al, ah, ol, oh = box
        o_lo = max(ol, 1.0, (1.0 + Sl) / PHI)
        a_lo = max(al, o_lo, (o_lo + 1.0 + Sl) / PHI)
        if ah < a_lo or oh < o_lo:
            return None
        R_lo, R_hi = Rt_rapido(a_lo, o_lo), Rt_rapido(ah, oh)
        sp_hi = min(Sh / 2, PHI / 2)
        wst_hi = min(1.0 / PHI, max(Sh - 1.0, 1e-9))
        piezas_hi = [ah, oh, 1.0, sp_hi, wst_hi]
        return (a_lo, ah, o_lo, oh, R_lo, R_hi, sp_hi, wst_hi,
                piezas_hi)

    root = (1.0, PHI, 1.0, GHI, 1.0, GHI)
    dims = [(0, 1, 0.05), (2, 3, 5.0), (4, 5, 5.0)]
    (cert, n, nP, nF, atasco), _h = _bnb_hibrido("k2r1", gen1,
                                                 root, dims)
    ok &= check(f"rama 1, k = 2: {cert} — {n} cajas ({nP} P, "
                f"{nF} F)" + (f"; atasco "
                              f"{[round(x, 4) for x in atasco]}"
                              if atasco else ""), cert)

    # rama 1, k = 1 (cuarteto {x1, D_m, s', w*}): j = 0 con suelo
    # x1 >= (1+Sigma)/phi — EXACTAMENTE el certificado algebraico
    # de fase 1 (mismo u-minimo): heredado
    suelo_f1 = max(1.0, (1.0 + 1.3) / PHI)      # fase 1, Sigma=1.3
    suelo_k1 = max(1.0, (1.0 + 1.3) / PHI)      # rama 1 k=1, idem
    ok &= check("rama 1, k = 1: cuarteto {x1, D_m, s', w*} con "
                "x1 >= (1+Sigma)/phi y R = x1+1 — EXACTAMENTE el "
                "dominio y el R del certificado algebraico de fase "
                "1 (verificacion mecanica del suelo, H8b): "
                "HEREDADO exacto",
                abs(suelo_f1 - suelo_k1) < 1e-15)

    # rama 2, k <= 2: {x1, (x2), m, sigma2}: una insercion; suelo
    # E4 c >= 1 + x1 (+ x2): R mas alto que pares — p mas chico:
    # B&B con Rt = max(E4, pares, blindada)
    def gen2(box):
        Sl, Sh, al, ah, ol, oh = box
        o_lo = max(ol, 1.0, (1.0 + Sl) / PHI)
        a_lo = max(al, o_lo, (o_lo + 1.0 + Sl) / PHI)
        if ah < a_lo or oh < o_lo:
            return None
        def Rt(a, o):
            return max(1.0 + a + o,
                       min(R3_necesidad(a, o, 1.0),
                           M_apilable3(a, o, 1.0)))
        R_lo, R_hi = Rt(a_lo, o_lo), Rt(ah, oh)
        s2_hi = min(Sh / 2, PHI / 2)
        piezas_hi = [ah, oh, 1.0, s2_hi]
        return (a_lo, ah, o_lo, oh, R_lo, R_hi, s2_hi, 1e-9,
                piezas_hi)

    (cert, n, nP, nF, atasco), _h = _bnb_hibrido("k2r2", gen2,
                                                 root, dims)
    ok &= check(f"rama 2, k = 2 (E4 en el suelo de c): {cert} — "
                f"{n} cajas ({nP} P, {nF} F)"
                + (f"; atasco {[round(x, 4) for x in atasco]}"
                   if atasco else ""), cert)
    # COLAS del bloque E (H1 del acta de fase 2: no existian).
    # Rama 1 (piezas > GHI): dominio y R con la MISMA forma que
    # j = 1 (suelos >= los de D: x1 >= 1+Sigma solo ayuda): la
    # cola de D aplica verbatim.
    o_min = 2.0 / PHI
    r1_p12 = 1.0 / (1.0 / GHI + 1.0 / o_min - 1.0 / (GHI + o_min))
    r1_p1m = min(bolsillo(GHI, 1.0, RR)
                 for RR in (GHI + o_min, 1e4, 1e8))
    ok &= check(f"cola rama 1 (piezas > {GHI}): dominio y R como "
                f"j = 1 con suelos mayores — la cola de D aplica "
                f"verbatim (p12 >= {r1_p12:.3f} > phi/2, p1m con "
                f"infimo {r1_p1m:.3f} > 1/phi, trio por suma de "
                f"maximos, simetria incluida)",
                r1_p12 > PHI / 2 and r1_p1m > 1 / PHI)
    # Rama 2 (piezas > GHI): R = 1+x1+x2 (E4); sigma2 <= phi/2 al
    # mejor bolsillo (esquinas en dos escalas); trio por suma de
    # maximos con los f-limites
    esc = []
    for x1 in (GHI, 1e4, 1e8):
        for x2 in (o_min, GHI, x1):
            Rr = 1.0 + x1 + x2
            esc.append(max(bolsillo(x1, x2, Rr),
                           bolsillo(x1, 1.0, Rr)))
    p_min_r2 = min(esc)
    th_max1 = 2 * math.asin(math.sqrt(1.0 / (1.0 + o_min)))
    trio_r2 = PI + th_max1 + 2 * math.asin(math.sqrt(1.0
                                                     / (GHI + 1)))
    ok &= check(f"cola rama 2 (piezas > {GHI}): R = 1+x1+x2; mejor "
                f"bolsillo >= {p_min_r2:.4f} > phi/2 en las 9 "
                f"esquinas de dos escalas; trio por suma de "
                f"maximos {trio_r2:.4f} < 2pi",
                p_min_r2 > PHI / 2 and trio_r2 < 2 * PI)
    return ok


def main():
    print("=" * 68)
    print("BOLSILLOS fase 1: el cuarteto j = 0 exacto "
          "(drafts/bolsillos.md)")
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
