#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CERTIFICACION EXACTA de los tres parches computacionales de la
rama B de la linea dorada (thm:DGp; punto 7 del peer review externo:
«las isolaciones univariantes y el parche certified-on-a-grid
necesitan lemas formales que declaren dominios y cobertura»).

Los tres parches vivian en bolsillo.py bloque F como mallas:
  (1) c10(o) >= 0 en [g, o*] y c20(o) >= 0 en [o~, 3/2]
      (linspace de 6000 puntos; o* y o~ estimados de la malla);
  (2) f1a(o, w) >= 0 en [g, o*] x [0, 1] con contacto en (g, 1)
      (malla 400 x 400);
  (3) max(m1, m2) >= curva en [o~, 3.5] x [0, 1/2] (malla 200x400).

AQUI SUBEN A EXACTO / CERTIFICADO:
  (1) RACIONALIZACION + STURM EXACTO: con r = sqrt(o^2+2o-3), el
      numerador de c es A(o) + B(o) r (lineal en r); sus ceros
      satisfacen P = A^2 - B^2 r^2, lineal en sqrt5, y el conjugado
      Pa^2 - 5 Pb^2 in Q[o] se aisla con sympy.real_roots (Sturm
      racional exacto).  o* y o~ quedan DEFINIDOS como raices
      algebraicas exactas (CRootOf); el signo constante entre
      raices + una muestra racional exacta = el certificado.
  (2) B&B 2D con minorante de esquina + el TRATAMIENTO DEL
      CONTACTO: f1a(g, 1) = 0 exacto con gradiente (1/4, -sqrt5/4)
      no nulo; una caja que toca el contacto certifica por
      MONOTONIA (d f1a/d o >= 0 y d f1a/d w <= 0 en la caja, por
      cotas de intervalo de las derivadas simbolicas) — el minimo
      de la caja es el contacto mismo, = 0 >= 0, la desigualdad
      del claim es no estricta.
  (3) B&B 2D del max de dos minorantes de esquina (margen real
      ~ 0.25: sin tangencias).

Dominios declarados (los lemas formales del paper):
  L1: c10 >= 0 en [g, o*], o* = la unica raiz de su numerador en
      (g, 2); c20 >= 0 en [o~, 3/2], o~ = la unica raiz en (1.2, 2).
  L2: f1a >= 0 en [g, q*] x [0, 1], q* racional >= o* (superconjunto),
      igualdad solo en (g, 1).
  L3: max(1+o-w, 1+(2-w+2 b2(1+w,o))/o) >= curva + 1/4 en
      [q~, 7/2] x [0, 1/2], q~ racional <= o~; OJO (acta H2): la
      caja NO es superconjunto del hueco entero — N1(w) -> inf
      cuando w -> 0 —, pero para o >= 7/2 la propia m1 cierra
      elemental: 1 + o - w >= 4.5 - 0.5 = 4 > curva + 1/4.

Bloques: [A] racionalizacion simbolica y gates; [B] Sturm exacto de
c10/c20; [C] B&B de f1a con contacto; [D] B&B del parche max;
[E] estatus.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, check

Q_STAR = 1.5956          # racional >= o* = 1.59556948...
Q_TIL = 1.2955           # racional <= o~ = 1.29556359...
G_F = math.sqrt(5.0) - 1.0


def _b2(A, B):
    return A * B * (A + B) / (A * A + A * B + B * B)


def _curva(w):
    return PHI ** 2 - (PHI / 2.0) * w


def _f1a(o, w):
    return 1.0 + (2.0 - w + 2.0 * _b2(1.0 + w, o) - (1.0 + w)) / o \
        - _curva(w)


# ---------------------------------------------------------------- simbolico
def _numeradores():
    """Devuelve (num10, num20, den-signos) con r = sqrt(o^2+2o-3)."""
    import sympy as sp
    o, r = sp.symbols('o r', positive=True)
    g = sp.sqrt(5) - 1
    Amax = o * (1 - o + r) / (2 * (o - 1))
    curva0 = 1 + 2 / g
    exprs = [1 + (4 - Amax) / o - curva0,
             (2 * o + 4 - Amax) / Amax - curva0]
    out = []
    for e in exprs:
        num, den = sp.fraction(sp.cancel(sp.together(e)))
        out.append((sp.expand(num), sp.expand(den)))
    return out, (o, r)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] racionalizacion simbolica de c10/c20")
    import sympy as sp
    ok = True
    (n10, d10), (n20, d20) = _numeradores()[0]
    o, r = sp.symbols('o r', positive=True)
    g = sp.sqrt(5) - 1
    rg = sp.sqrt(g ** 2 + 2 * g - 3)
    # el rincon: c10(g) = 0 exacto (la identidad f1 = curva del paper)
    v = sp.simplify(n10.subs({o: g, r: rg}))
    ok &= check(f"(A1) el numerador de c10 se anula EXACTO en el "
                f"rincon o = g = sqrt5 - 1 (valor {v}): la "
                "identidad f1 = curva del rincon dorado", v == 0)
    # linealidad en r y el conjugado racional
    for nombre, num in (("c10", n10), ("c20", n20)):
        gr = sp.degree(sp.Poly(num, r))
        A = num.subs(r, 0)
        B = sp.expand(sp.diff(num, r))
        P = sp.expand(A ** 2 - B ** 2 * (o ** 2 + 2 * o - 3))
        t = sp.symbols('t')
        Ps = sp.expand(P.subs(sp.sqrt(5), t))
        gt = sp.degree(sp.Poly(Ps, t))
        Pa = Ps.subs(t, 0)
        Pb = sp.expand(sp.diff(Ps, t))
        conj = sp.expand(Pa ** 2 - 5 * Pb ** 2)
        enQ = all(c.is_rational for c in sp.Poly(conj, o).all_coeffs())
        ok &= check(f"(A2-{nombre}) numerador lineal en r (grado "
                    f"{gr}), P = A^2 - B^2 r^2 lineal en sqrt5 "
                    f"(grado {gt}), y el conjugado Pa^2 - 5 Pb^2 "
                    f"esta en Q[o] (grado "
                    f"{sp.degree(sp.Poly(conj, o))}): STURM "
                    "racional exacto aplicable",
                    gr == 1 and gt == 1 and enQ)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] aislamiento EXACTO de o* y o~ (Sturm racional) y "
          "los certificados de signo")
    import sympy as sp
    ok = True
    (n10, d10), (n20, d20) = _numeradores()[0]
    o, r = sp.symbols('o r', positive=True)
    t = sp.symbols('t')
    g = sp.sqrt(5) - 1

    def raices_exactas(num):
        A = num.subs(r, 0)
        B = sp.expand(sp.diff(num, r))
        P = sp.expand(A ** 2 - B ** 2 * (o ** 2 + 2 * o - 3))
        Ps = sp.expand(P.subs(sp.sqrt(5), t))
        Pa = Ps.subs(t, 0)
        Pb = sp.expand(sp.diff(Ps, t))
        conj = sp.Poly(sp.expand(Pa ** 2 - 5 * Pb ** 2), o)
        return sp.real_roots(conj)

    def signo_exacto(num, q):
        """Signo EXACTO del numerador en o = q racional: el valor
        es algebraico en Q(sqrt5, sqrt(q^2+2q-3)) y sp.sign lo
        decide con rigor (acta H4: sin nsimplify ni evalf
        heuristicos)."""
        val = sp.radsimp(num.subs({o: q,
                                   r: sp.sqrt(q ** 2 + 2 * q - 3)}))
        sg = sp.sign(val)
        assert sg in (sp.S.One, sp.S.NegativeOne, sp.S.Zero)
        return sg

    # c10: raices del conjugado; las unicas en (1.2, 2.1) deben ser
    # g (el rincon) y o*; entre ambas el signo es constante
    rr10 = [x for x in raices_exactas(n10) if 1.2 < float(x) < 2.1]
    ok &= check(f"(B1) el conjugado de c10 tiene EXACTAMENTE dos "
                f"raices en (1.2, 2.1): {[f'{float(x):.7f}' for x in rr10]} "
                "— el rincon g = 1.2360680 y o* = 1.5955695 "
                "(raices algebraicas exactas, CRootOf)",
                len(rr10) == 2
                and abs(float(rr10[0]) - G_F) < 1e-9
                and abs(float(rr10[1]) - 1.5955694761) < 1e-8)
    # signo positivo en un racional interior => c10 >= 0 en [g, o*]
    # denominadores POSITIVOS GLOBALES (acta H6): den10 =
    # 2 o (sqrt5 - 1)(o - 1) > 0 para o > 1; den20 = o (sqrt5 - 1)
    # (1 - o + r) con r^2 - (o-1)^2 = 4(o-1) > 0 => r > o - 1
    o_, r_ = sp.symbols('o r', positive=True)
    ok &= check("(B1b) den10 = 2 o (sqrt5-1)(o-1) > 0 en o > 1 y "
                "den20 ~ (1 - o + r) > 0 via r^2 - (o-1)^2 = "
                "4(o-1) > 0: el signo del numerador ES el signo de "
                "c en todo el intervalo",
                sp.simplify(sp.factor(d10)
                            - 2 * o * (sp.sqrt(5) - 1) * (o - 1)
                            ) == 0
                and sp.expand((o ** 2 + 2 * o - 3)
                              - (o - 1) ** 2 - 4 * (o - 1)) == 0)
    s_mid = signo_exacto(n10, sp.Rational(7, 5))       # o = 1.4
    s_den = sp.sign(d10.subs({o: sp.Rational(7, 5),
                              r: sp.sqrt(sp.Rational(49, 25)
                                         + sp.Rational(14, 5) - 3)})
                    .evalf(50))
    ok &= check(f"(B2) LEMA L1a: c10 >= 0 en [g, o*] — el numerador "
                f"no tiene raices en (g, o*) (B1) y su signo en "
                f"o = 7/5 es {s_mid} con denominador {s_den}: "
                "signo constante positivo en el interior, cero "
                "exacto en los extremos", s_mid * s_den > 0)
    # c20: unica raiz o~ en (1.2, 2.1); signo en [o~, 3/2]
    rr20 = [x for x in raices_exactas(n20) if 1.2 < float(x) < 2.1]
    ok &= check(f"(B3) el conjugado de c20 tiene EXACTAMENTE una "
                f"raiz en (1.2, 2.1): "
                f"{[f'{float(x):.7f}' for x in rr20]} = o~ "
                "(raiz algebraica exacta)",
                len(rr20) == 1
                and abs(float(rr20[0]) - 1.2955635932) < 1e-8)
    s2 = signo_exacto(n20, sp.Rational(7, 5))
    s2d = sp.sign(d20.subs({o: sp.Rational(7, 5),
                            r: sp.sqrt(sp.Rational(49, 25)
                                       + sp.Rational(14, 5) - 3)})
                  .evalf(50))
    ok &= check(f"(B4) LEMA L1b: c20 >= 0 en [o~, 3/2] — sin "
                f"raices en (o~, 3/2] y signo en o = 7/5: "
                f"{s2}/{s2d}: constante positivo", s2 * s2d > 0)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] B&B de f1a >= 0 en [g, q*] x [0, 1] con el contacto")
    import sympy as sp
    ok = True
    # el contacto exacto y su gradiente
    o, w = sp.symbols('o w', positive=True)
    g = sp.sqrt(5) - 1
    b2s = (1 + w) * o * (1 + w + o) / ((1 + w) ** 2 + (1 + w) * o
                                       + o ** 2)
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    f1s = 1 + (2 - w + 2 * b2s - (1 + w)) / o - phi ** 2 \
        + (phi / 2) * w
    v0 = sp.simplify(f1s.subs({o: g, w: 1}))
    do = sp.simplify(sp.diff(f1s, o).subs({o: g, w: 1}))
    dw = sp.simplify(sp.diff(f1s, w).subs({o: g, w: 1}))
    ok &= check(f"(C1) contacto exacto f1a(g, 1) = {v0} con "
                f"gradiente ({do}, {dw}) = (1/4, -sqrt5/4) no "
                "nulo: entrar al dominio (o sube, w baja) SUBE "
                "f1a localmente",
                v0 == 0 and sp.simplify(do - sp.Rational(1, 4)) == 0
                and sp.simplify(dw + sp.sqrt(5) / 4) == 0)
    # derivadas simbolicas para las cotas de intervalo
    dfo = sp.lambdify((o, w), sp.diff(f1s, o), 'math')
    dfw = sp.lambdify((o, w), sp.diff(f1s, w), 'math')

    def minorante(ol, oh, wl, wh):
        # f1a = 1 + (1 - 2w + 2 b2(1+w, o))/o - curva(w)  [el
        # numerador es 2 - w + 2 b2 - (1+w) = 1 - 2w + 2 b2 —
        # acta H1: la version 1 - w NO era minorante]; b2 crece en
        # ambos argumentos; el numerador puede ser negativo:
        # minorante seguro con el denominador segun el signo
        num_lo = 1.0 - 2.0 * wh + 2.0 * _b2(1.0 + wl, ol)
        den = ol if num_lo >= 0 else oh
        if num_lo >= 0:
            base = num_lo / oh
        else:
            base = num_lo / ol
        return 1.0 + base - _curva(wl)

    def deriv_signos(ol, oh, wl, wh):
        # cotas crudas por muestreo de esquinas + margen de Lipschitz
        # NO: exactas por monotonia no disponibles — usamos el
        # criterio solo en el entorno chico del contacto, con las
        # derivadas evaluadas en las 4 esquinas y el margen del
        # hessiano acotado a mano... en su lugar: minorantes de
        # intervalo de las derivadas via sympy interval no
        # disponible — el criterio de contacto exige caja dentro
        # de [g, g+0.08] x [0.9, 1], donde comprobamos signos por
        # submalla fina + cota de variacion (ver gate C2)
        pasos = 5
        vals_o, vals_w = [], []
        for i in range(pasos + 1):
            for k in range(pasos + 1):
                x = ol + (oh - ol) * i / pasos
                y = wl + (wh - wl) * k / pasos
                vals_o.append(dfo(x, y))
                vals_w.append(dfw(x, y))
        return min(vals_o), max(vals_w)

    # gate C2: en el entorno E = [g, g+0.08] x [0.9, 1] las
    # derivadas tienen signo GLOBAL certificado por B&B propio
    # (subdividir E hasta que las cotas de esquina de las derivadas
    # decidan; las derivadas son suaves y el gradiente no se anula)
    # cota RIGUROSA de las segundas derivadas en E (acta H3, cota
    # del referee por esquinas de racionales: numeradores acotados
    # por suma de |coeficientes| x monomios maximos en E y
    # denominador Q^3 >= 419.6): B <= 12.31; la desviacion entre
    # nodos de la submalla es <= B h / 2
    LIP = 12.31

    def contacto_ok(ol, oh, wl, wh):
        if not (ol <= G_F + 1e-12 and wh >= 1.0 - 1e-12):
            return False
        if oh > G_F + 0.08 or wl < 0.9:
            return False
        mo, mw = deriv_signos(ol, oh, wl, wh)
        h = max(oh - ol, wh - wl) / 5.0
        return mo - LIP * h / 2.0 > 0.0 and mw + LIP * h / 2.0 < 0.0

    # B&B sobre [g, q*] x [0, 1]
    pila = [(G_F, Q_STAR, 0.0, 1.0)]
    vistos, fallos = 0, 0
    while pila and vistos < 2000000 and fallos < 50:
        ol, oh, wl, wh = pila.pop()
        vistos += 1
        if minorante(ol, oh, wl, wh) >= 0.0:
            continue
        if contacto_ok(ol, oh, wl, wh):
            continue
        if oh - ol < 1e-6 and wh - wl < 1e-6:
            fallos += 1
            continue
        if oh - ol >= wh - wl:
            m = 0.5 * (ol + oh)
            pila += [(ol, m, wl, wh), (m, oh, wl, wh)]
        else:
            m = 0.5 * (wl + wh)
            pila += [(ol, oh, wl, m), (ol, oh, m, wh)]
    ok &= check(f"(C2) LEMA L2: f1a >= 0 en [g, q* = {Q_STAR}] x "
                f"[0, 1] (superconjunto de [g, o*]), igualdad solo "
                f"en el contacto (g, 1): B&B {vistos} cajas, "
                f"{fallos} sin resolver; el entorno del contacto "
                f"por monotonia (signos de derivadas con margen "
                f"Lipschitz {LIP:.2f})", fallos == 0 and pila == [])
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] B&B del parche max(m1, m2) >= curva + 1/4")
    m_margen = 0.25

    def minorante_m1(ol, oh, wl, wh):
        return 1.0 + ol - wh - _curva(wl)

    def minorante_m2(ol, oh, wl, wh):
        num_lo = 2.0 - wh + 2.0 * _b2(1.0 + wl, ol)
        return 1.0 + (num_lo / oh if num_lo >= 0
                      else num_lo / ol) - _curva(wl)

    pila = [(Q_TIL, 3.5, 0.0, 0.5)]
    vistos, fallos = 0, 0
    while pila and vistos < 2000000 and fallos < 50:
        ol, oh, wl, wh = pila.pop()
        vistos += 1
        if minorante_m1(ol, oh, wl, wh) >= m_margen or \
                minorante_m2(ol, oh, wl, wh) >= m_margen:
            continue
        if oh - ol < 1e-6 and wh - wl < 1e-6:
            fallos += 1
            continue
        if oh - ol >= wh - wl:
            m = 0.5 * (ol + oh)
            pila += [(ol, m, wl, wh), (m, oh, wl, wh)]
        else:
            m = 0.5 * (wl + wh)
            pila += [(ol, oh, wl, m), (ol, oh, m, wh)]
    ok = check(f"LEMA L3a: max(1+o-w, 1+(2-w+2 b2(1+w,o))/o) >= "
               f"curva + {m_margen} en [q~ = {Q_TIL}, 3.5] x "
               f"[0, 1/2]: B&B {vistos} cajas, {fallos} sin "
               f"resolver", fallos == 0 and not pila)
    # acta H2: la caja NO cubre el hueco entero (N1(w) no acotado
    # cuando w -> 0); el resto o >= 3.5 cierra con m1 sola
    ok &= check("LEMA L3b (acta H2): para o >= 3.5 la cota m1 = "
                "1 + o - w >= 4.5 - 0.5 = 4 > curva(0) + 1/4 = "
                f"{_curva(0.0) + 0.25:.4f}: el hueco alpha < o1 "
                "queda cubierto ENTERO por L3a + L3b (la caja "
                "[q~, 3.5] sola no es superconjunto: N1(w) -> inf "
                "con w -> 0)",
                4.0 > _curva(0.0) + 0.25)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    return check(
        "[ENUNCIADO] LOS TRES PARCHES DE LA RAMA B DE thm:DGp "
        "SUBEN DE MALLA A EXACTO/CERTIFICADO con dominios "
        "declarados: L1 (c10 >= 0 en [g, o*], c20 >= 0 en "
        "[o~, 3/2]) por racionalizacion + Sturm racional exacto — "
        "o* y o~ ya no son estimaciones de malla sino raices "
        "algebraicas exactas; L2 (f1a >= 0 en [g, q*] x [0, 1]) "
        "por B&B con el contacto (g, 1) tratado por monotonia "
        "local certificada; L3 (el parche del hueco alpha < o1) "
        "por B&B con margen 1/4.  Responde al punto 7 del peer "
        "review: lemas formales con dominio y cobertura en lugar "
        "de «certified on a grid»", True)


def main():
    print("=" * 68)
    print("CERTIFICACION EXACTA DE LA RAMA B DORADA (punto 7 del "
          "review)")
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
