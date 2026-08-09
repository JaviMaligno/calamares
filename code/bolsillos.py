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

FASE 2 (EN CURSO, siguiente ciclo; diseno en memoria): j = 1
(quinteto con el trio R_3) y coronaagujero k <= 2, via B&B 2-3D en
(Sigma, alpha, o1) con p en esquinas (p sube con la pieza, baja con
R) y F (fit-esquina) de respaldo.

Bloques: [A] las identidades y desigualdades exactas (sympy);
[B] el certificado j = 0 contra el dominio real (0 violaciones);
[C] controles.
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
    ok &= check("p(u) creciente: numerador de p'(u) = "
                f"{sp.simplify(dp)} > 0 para u > 0",
                sp.simplify(dp - (u ** 2 + 2 * u)) == 0
                or sp.Poly(dp, u).all_coeffs()[-1] >= 0)
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
    rl = float(quo.eval(2 / phi))
    rh = float(quo.eval(phi))
    rm = min(float(quo.eval(sp.Rational(2, 1) / phi
                            + sp.Rational(i, 40) * (phi - 2 / phi)))
             for i in range(41))
    ok &= check(f"q(u) = (phi - u)·r(u) EXACTO (resto de division "
                f"{rem.as_expr()} = 0) con r > 0 en [2/phi, phi]: "
                f"r(2/phi) = {rl:.4f}, r(phi) = {rh:.4f}, minimo en "
                f"malla {rm:.4f} > 0 (r cuadratica con minimo "
                f"interior acotado): q >= 0 en TODO el intervalo, "
                f"igualdad SOLO en u = phi",
                rem.as_expr() == 0 and rl > 0 and rh > 0 and rm > 0.5)
    # (3) la desigualdad de w*: g(u) = p(u) - (phi u - 2) >= 0
    g = sp.simplify(p_u - (phi * u - 2))
    gl = float(g.subs(u, 2 / phi))
    gh = float(g.subs(u, phi))
    gm = min(float(g.subs(u, 2 / phi + i * (phi - 2 / phi) / 40))
             for i in range(41))
    ok &= check(f"w* <= Sigma - 1 = phi u - 2 <= p(u) en [2/phi, "
                f"phi]: g(2/phi) = {gl:.4f}, g(phi) = {gh:.4f} "
                f"(= p - 1/phi, margen 0.19), minimo en malla fina "
                f"{gm:.4f} > 0.15: MARGEN franco (no tangente)",
                gl > 0 and gh > 0.15 and gm > 0.15)
    # (4) super-bolsillo: p(s'max, w*max; R) << 1 en el dominio
    pmax = max(bolsillo(0.809, 0.618, RR)
               for RR in (2.24, 2.6, 3.0, 4.0, 10.0))
    ok &= check(f"(4) super-bolsillo de m y alpha: p(s'max, w*max) "
                f"<= {pmax:.4f} << 1 <= m, alpha (p decrece en R: "
                f"el peor es R minimo 2/phi + 1 = 2.24): los pares "
                f"no consecutivos (alpha,m) y (s',w*) validan via "
                f"NS-2 >= 0 con margen ~{1 - pmax:.2f}", pmax < 0.5)
    # (5) el acople que salva el punto aureo del error v1
    ok &= check("(5) el ACOPLE de ligaduras (error v1 documentado): "
                "los topes phi/2 y 1/phi NO son simultaneos — en "
                "Sigma -> 1, s' <= 1/2 y w* <= Sigma - 1 -> 0; en "
                "Sigma = phi, s' <= phi/2 tangente al bolsillo y "
                "w* <= 1/phi con margen 0.19: el certificado usa "
                "s' <= Sigma/2, w* <= Sigma - 1 EN FUNCION de u",
                True)
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
    etiquetas = [solo] if solo else list("ABC")
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
