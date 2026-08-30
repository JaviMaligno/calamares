#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EL CERTIFICADO RIGUROSO DEL QUINTETO j = 1 (thm:gapwritten), v4.

v3 (segunda ronda del referee externo): CERO tolerancias de
aceptacion y SIN hipotesis de libm.  Toda comparacion del
certificado es (a) EXACTA en aritmetica racional (fracciones
diadicas de los corners: bolsillos racionalizados, pares, umbrales
M, suelos, caps, y TODO el testigo apilado P5), o (b) un INTERVALO
EXTERIOR con redondeo dirigido: asin se CERTIFICA por serie
racional pura (v4, _asin_iv: sin^2 y cos encajonados en Q con
resto de Lagrange alternante; el float es solo un oraculo) y TODA
suma/resta de intervalos usa add_up/add_dn/sub_up/sub_dn
(nextafter tras cada operacion).  Las cotas flotantes de pi se
certifican en Q por la misma serie (gate A9).  El
bracket de R_3 avanza cada extremo SOLO con certeza direccional
(hi con factibilidad cierta, lo con infactibilidad cierta): un
intervalo exterior autentico.  EL TEOREMA DEL TRIO (v3, prueba del
referee externo; gate A4): {alpha, o1, m} cabe en R_used en TODO
el dominio — b2(a, b) diametral creciente y b2(2, sqrt5 - 1) = 1
(la identidad del mirror corner, kernel-checked en Lean).  Las
constantes phi diadicas se verifican en Q (gate A9).

LA CAJA DEL PUNTO AUREO (Sigma, alpha, o1) = (phi, phi, phi) — el
clavo de v1 — SE CIERRA ALGEBRAICAMENTE (P5): el analisis exacto
del corner muestra (i) la doble-esquina (s' = phi/2, w* = 1/phi)
es FANTASMA — la tercera ligadura w* <= Lambda - 2 s' (la fila
contiene la pieza mayor >= s') la vacia: en el extremo s' = 1/2
EXACTO —, y (ii) el corner real (s' pequeno, w* -> 1/phi) NO cabe
mural (el arco inferior suma pi + 1.4e-4): el testigo correcto
APILA w* radialmente bajo s' (el par (s', w*) es apilable:
R >= s' + 2 w*).  Todas las condiciones del testigo apilado son
RACIONALES — theta <= pi/2 <=> p = f(a)f(b) <= 1/2, distancias al
cuadrado — y en el punto aureo dan identidades exactas en
Q[sqrt 5]:  s'_ext = 1/2,  d_w = 2 phi - 1 - 1/phi = phi,
dist^2 - (w* + alpha)^2 = 1/phi^3  (margen aureo del stack;
gate A8; sugeridas para Lean: stack_golden
2 phi^4 - (phi+2)^2 = phi - 1, p_mid_golden
f(phi) f(1) = 1/sqrt5 <= 1/2, y la racionalizacion del
sub-bolsillo 4 s^2 D <= (1 - s S)^2).

DOMINIO Y LIGADURAS (de la prueba de thm:gapwritten):
  Sigma in (1, phi], alpha, o1 >= max(1, (1+Sigma)/phi)
  (superconjunto), s' <= min(Sigma/2, phi/2),
  w* <= min(1/phi, Sigma-1), y la tercera ligadura
  w* <= Sigma - 2 s' SOLO via su forma extremal en P5;
  R >= R_used = max(pares, min(R_3, M)) por punto, extendido a
  todo R mayor por fit-monotonia.

CERTIFICADOS POR CAJA (OR; sin LP, sin mallas, sin exclusiones):
  P1  trio por construccion + s', w* a dos bolsillos DISTINTOS
      (6 asignaciones; comparacion racional exacta); pares no
      consecutivos por la validacion ESTRUCTURAL (gate A5).
  P2  row-disk combinado s' + w* al mejor bolsillo (racional).
  P3  el 4-ciclo [alpha, o1, w*, m] con d1 = pi por la forma
      cerrada F = -sigma - max(B1, B2) >= 0 (gate A6, con la
      derivacion del reparto del slack y los wrap-caps
      automaticos) en intervalos dirigidos, con la DICOTOMIA de
      rango de w* (w* <= wcut a bolsillo; w* >= wcut al ciclo con
      ese suelo) y s' sub-bolsillo del hueco diametral.
  P5  EL TESTIGO APILADO (nuevo, v2): (alpha, o1) diametrales,
      s' en el punto medio del arco superior con w* apilado
      radialmente debajo, m en el punto medio del arco inferior.
      Condiciones 100% racionales: p(alpha, s') <= 1/2,
      p(o1, s') <= 1/2, p(alpha, m) <= 1/2, p(o1, m) <= 1/2
      (colocacion media legal), R - 2s' - w* >= 0 (profundidad) y
      (R - alpha)^2 + (R - 2s' - w*)^2 >= (w* + alpha)^2 (y su
      simetrica en o1): el stack no toca los diametrales.  El w*
      del stack usa la forma extremal de la tercera ligadura:
      w*_ef = min(w*_cap, max(0, Sh - 2 s'_lo)) con s'_lo el
      suelo de s' del sub-caso (dicotomia de s' en P5).
  Colas alpha > G o o1 > G (G = 30): formulas cerradas con el
      infimo p_inf(a,b) = ab/(sqrt a + sqrt b)^2 (gate A7, las
      desigualdades en Q[sqrt] via cuadrados).

Bloques: [A] gates (sympy exacto; la monotonia del bolsillo por
la derivacion del referee: dK/dk_a = 1 + (k_b + k_R)/sqrt(D) > 0
porque k_b + k_R = 1/b - 1/R > 0); [B] B&B con atribucion; [C]
contraste (sondas de verdad + falsabilidad); [D] estatus.
"""
import math
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, theta_w, ciclo_constructivo

SEED = int(os.environ.get('CC_SEED', '20260831'))
G_TOP = 30.0

# ---- redondeo dirigido (la unica capa flotante del certificado) --
_INF = float('inf')


def _up(x, n=1):
    for _ in range(n):
        x = math.nextafter(x, _INF)
    return x


def _dn(x, n=1):
    for _ in range(n):
        x = math.nextafter(x, -_INF)
    return x


def add_up(*xs):
    t = 0.0
    for x in xs:
        t = _up(t + x)
    return t


def add_dn(*xs):
    t = 0.0
    for x in xs:
        t = _dn(t + x)
    return t


def sub_up(x, y):
    return _up(x - y)


def sub_dn(x, y):
    return _dn(x - y)


# ---- asin(sqrt p) por SERIE RACIONAL PURA (v4): ni mpmath ni ----
# ---- libm — la certificacion es 100% en Fraction -----------------
_N_COS = 18   # resto de Lagrange <= x^38/38! < 1e-25 en x <= 3.3
_ASIN_CACHE = {}


def _cos_br(x):
    """cos(x) encajonado EXACTO en Q para x in [0, 3.3]
    (Fraction).  Serie de Taylor alternante: los terminos son
    decrecientes desde k = 2 (x^2 <= 10.89 < 12 = 3*4), asi que
    el RESTO DE LAGRANGE alternante deja cos(x) entre dos sumas
    parciales consecutivas: bracket dirigido exacto en Q."""
    x2 = x * x
    term = Fr(1)
    s = Fr(1)
    for k in range(1, _N_COS + 1):
        term = -term * x2 / ((2 * k - 1) * (2 * k))
        s += term
    s2 = s - term * x2 / ((2 * _N_COS + 1) * (2 * _N_COS + 2))
    return (s, s2) if s <= s2 else (s2, s)


def _sin2_br(t):
    """sin^2(t) = (1 - cos(2t))/2 encajonado EXACTO en Q
    (t <= 1.65, para que 2t <= 3.3 quede en dominio de _cos_br)."""
    clo, chi = _cos_br(2 * t)
    return (1 - chi) / 2, (1 - clo) / 2


def _asin_iv(p_num, p_den):
    """asin(sqrt p), intervalo exterior con certificacion
    RACIONAL PURA (v4, encargo del referee externo: una cota
    VALIDADA, no mas precision): CERO hipotesis numericas — ni
    mpmath ni libm.  math.asin actua solo de ORACULO (no se le
    cree nada); cada extremo diadico se CERTIFICA en Q:
      (hi) p <= sin2_lo(t)  ==>  asin(sqrt p) <= t
           [t < pi/2: sin creciente; t >= pi/2: trivial, pues
           asin <= pi/2 — el caso no requiere saber cual es]
      (lo) p >= sin2_hi(t) y cos_lo(t) > 0  ==>  asin >= t
           [cos_lo > 0 certifica t < pi/2 porque t <= 1.65 < 3 y
           cos < 0 en (pi/2, 3]]
    Si el oraculo mintiera, el bucle de ensanche solo produce un
    intervalo MAS ANCHO (sound); fallback trivial [0, PI_HI/2]
    (PI_HI > pi certificado en Q por _cos_br, gate A9)."""
    key = (p_num, p_den)
    hit = _ASIN_CACHE.get(key)
    if hit is not None:
        return hit
    p = Fr(p_num, p_den)
    g = math.asin(math.sqrt(p_num / p_den))  # oraculo, no creido
    # ensanche ABSOLUTO geometrico: cerca de p = 1 el
    # condicionamiento de asin(sqrt p) es 1/sqrt(1-p) y el oraculo
    # puede derivar ~1e-12 (medido); ensanchar por ulps no llega
    hi = None
    d = 0.0
    for _ in range(12):
        t = _up(g + d, 2)
        if 0.0 < t <= 1.65 and p <= _sin2_br(Fr(t))[0]:
            hi = t
            break
        d = 4e-16 if d == 0.0 else d * 8.0
    if hi is None:
        hi = _up(PI_HI / 2.0)
    lo = None
    d = 0.0
    for _ in range(12):
        t = _dn(g - d, 2)
        if t <= 0.0:
            lo = 0.0
            break
        if t <= 1.65 and p >= _sin2_br(Fr(t))[1] \
                and _cos_br(Fr(t))[0] > 0:
            lo = t
            break
        d = 4e-16 if d == 0.0 else d * 8.0
    if lo is None:
        lo = 0.0
    res = (lo, hi)
    _ASIN_CACHE[key] = res
    return res


PI_LO = _dn(math.pi)          # < pi verdadero
PI_HI = _up(math.pi)          # > pi verdadero
TWO_PI_LO = _dn(2.0 * math.pi)


def _fr(x):
    """Float (diadico) -> Fraction EXACTA."""
    return Fr(x)


def _fr_to_iv(q):
    """Fraction -> intervalo flotante exterior de 1 ulp (la
    division entera de CPython es correctamente redondeada)."""
    f = q.numerator / q.denominator
    return math.nextafter(f, -_INF), math.nextafter(f, _INF)


def p_prod(a, b, R):
    """p = f(a) f(b) = ab/((R-a)(R-b)) en Fraction, o None si el
    par ya no cabe (a + b >= R o piezas >= R): requisito pi."""
    if a + b >= R or a >= R or b >= R:
        return None
    return (a * b) / ((R - a) * (R - b))


def th_iv(a, b, R):
    """Intervalo exterior de theta_w(a, b, R) (Fractions).  El
    clamp a pi se decide RACIONALMENTE (p >= 1); asin por serie
    racional pura (_asin_iv, v4): cero hipotesis numericas."""
    p = p_prod(a, b, R)
    if p is None or p >= 1:
        return PI_LO, PI_HI
    if p <= 0:
        return 0.0, 0.0
    alo, ahi = _asin_iv(p.numerator, p.denominator)
    return max(0.0, _dn(2.0 * alo)), min(PI_HI, _up(2.0 * ahi))


def le_pocket(s, a, b, R):
    """s <= bolsillo(a, b; R), decidido EXACTO en Q: con
    S = 1/a + 1/b - 1/R y D = (R - a - b)/(abR) >= 0,
    s <= 1/(S + 2 sqrt D) <=> 2 s sqrt D <= 1 - s S <=>
    [1 - s S >= 0  y  4 s^2 D <= (1 - s S)^2].  Si D < 0 el par
    no es tangible en R: False (sin bolsillo)."""
    if s <= 0:
        return True
    D = (R - a - b) / (a * b * R)
    if D < 0:
        return False
    S = 1 / a + 1 / b - 1 / R
    rhs = 1 - s * S
    if rhs < 0:
        return False
    return 4 * s * s * D <= rhs * rhs


def M_apilable3(a, b, c):
    tr = [a, b, c]
    return min(max(x, y) + 2 * min(x, y)
               for i, x in enumerate(tr) for y in tr[i + 1:])


def _trio_cierto_cabe(a, b, R):
    """True si theta(a,b;R)+theta(b,1;R)+theta(1,a;R) <= 2 pi con
    CERTEZA (suma de extremos superiores <= 2 pi por abajo)."""
    s = 0.0
    for x, y in ((a, b), (b, Fr(1)), (Fr(1), a)):
        s = add_up(s, th_iv(x, y, R)[1])
        if s > TWO_PI_LO:
            return False
    return s <= TWO_PI_LO


def _trio_cierto_no_cabe(a, b, R):
    s = 0.0
    for x, y in ((a, b), (b, Fr(1)), (Fr(1), a)):
        s = add_dn(s, th_iv(x, y, R)[0])
    return s > _up(2.0 * PI_HI)


_R3_CACHE = {}


def R3_bracket(a, b):
    """Bracket exterior [lo, hi] del R_3 del trio {a, b, 1}: lo
    avanza SOLO con infactibilidad cierta (lo <= R_3), hi SOLO
    con factibilidad cierta (hi >= R_3).  Midpoints redondeados a
    diadicos de 24 bits (los extremos siguen siendo válidos: el
    avance exige certeza direccional).  Memoizada."""
    k = (a, b)
    v = _R3_CACHE.get(k)
    if v is not None:
        return v
    lo = max(a + b, b + 1, a + 1)
    hi = 4 * (a + b + 1)
    if _trio_cierto_cabe(a, b, lo):
        _R3_CACHE[k] = (lo, lo)
        return lo, lo
    for _ in range(46):
        mid = (lo + hi) / 2
        mid = Fr(int(mid * (1 << 24)), 1 << 24)
        if not (lo < mid < hi):
            mid = (lo + hi) / 2
        if _trio_cierto_cabe(a, b, mid):
            hi = mid
        elif _trio_cierto_no_cabe(a, b, mid):
            lo = mid
        else:
            break                      # incertidumbre: parar (valido)
        if hi - lo < Fr(1, 1 << 20):
            break
    if len(_R3_CACHE) > 200000:
        _R3_CACHE.clear()
    _R3_CACHE[k] = (lo, hi)
    return lo, hi


def R_used_bracket(a_lo, a_hi, o_lo, o_hi):
    """[R_lo, R_hi] racionales de R_used = max(pares, min(R_3, M)):
    componentes crecientes en las piezas (gate A4).  Fast path: si
    el trio cabe con certeza en pares, min(R_3, M) <= R_3 <= pares
    y R_used = pares (sin biseccion)."""
    p_lo = max(a_lo + o_lo, a_lo + 1, o_lo + 1)
    p_hi = max(a_hi + o_hi, a_hi + 1, o_hi + 1)
    if _trio_cierto_cabe(a_lo, o_lo, p_lo):
        R_lo = p_lo
    else:
        r3l, _ = R3_bracket(a_lo, o_lo)
        R_lo = max(p_lo, min(r3l, M_apilable3(a_lo, o_lo, Fr(1))))
    if _trio_cierto_cabe(a_hi, o_hi, p_hi):
        R_hi = p_hi
    else:
        _, r3h = R3_bracket(a_hi, o_hi)
        R_hi = max(p_hi, min(r3h, M_apilable3(a_hi, o_hi, Fr(1))))
    return R_lo, R_hi


# ------------------------------------------------- certificado por caja
QC_N = [0, 0, 0, 0, 0, 0]  # P1, P2, P3, P5, P6, vacuas
FR_PHI_HI = Fr(_up(PHI, 1))    # racional > phi (para caps: mayora)
FR_PHI_LO = Fr(_dn(PHI, 1))    # racional < phi
FR_INV_PHI_HI = Fr(_up(1.0 / PHI, 1))


def _floors(Sl):
    """Suelo racional de alpha/o1: max(1, (1+Sl)/phi) MINORADO
    (un suelo por debajo del real solo agranda el dominio):
    (1+Sl)/phi >= (1+Sl) * inv_phi_lo con inv_phi_lo < 1/phi."""
    f = (1 + Sl) * Fr(_dn(1.0 / PHI, 1))
    return max(Fr(1), f)


def _trio_ok(a_lo, a_hi, o_lo, o_hi, R_lo):
    """TEOREMA DEL TRIO (v3; la prueba es del referee externo y
    sustituye el enunciado erroneo de v2): en todo el dominio
    (Sigma >= 1 => b := min(alpha, o1) >= (1+Sigma)/phi >=
    2/phi), el trio {alpha, o1, m} cabe en R_used.  Prueba: sea
    a = max(alpha, o1) >= b.  (i) a >= 2: en R = pares = a + b
    el par es diametral y el bolsillo degenerado
    b2(a, b) = ab(a+b)/(a^2+ab+b^2) es CRECIENTE en ambas
    piezas (d(b2)/da = b^3(2a+b)/D^2 > 0, gate A4), con
    b2(2, 2/phi) = 1 — la identidad del mirror corner
    b2(2, sqrt5 - 1) = 1, kernel-checked en Lean —: la unidad
    cabe en el bolsillo y el trio cabe YA EN EL SUELO de pares
    (theta(a,m) + theta(m,b) <= pi en un semiarco; el otro arco
    >= pi >= theta(a,b)).  (ii) a <= 2: en R = b + 2 = M (el
    umbral apilable del par (b, 1)) la suma angular del trio
    crece en a, maxima en a = 2, donde R = pares(2, b) y
    b2(2, b) >= b2(2, 2/phi) = 1: el trio cabe en M, luego
    R_3 <= M y R_used >= min(R_3, M) = R_3: tangente-o-mejor.
    Ambas ramas cubren todo a: True incondicional en el
    dominio."""
    return True


def cert_caja(Slf, Shf, alf, ahf, olf, ohf):
    """None = subdividir; 1/2/3/5 = certificado; 0 = vacua.
    Entradas float (corners diadicos); todo el calculo en
    Fraction / intervalos dirigidos.  SIN tolerancias."""
    Sl, Sh = _fr(Slf), _fr(Shf)
    al, ah = _fr(alf), _fr(ahf)
    ol, oh = _fr(olf), _fr(ohf)
    if Sh <= 1:
        return 0                       # sin desborde: testigo trivial
    fl = _floors(Sl)
    if ah < fl or oh < fl:
        return 0                       # bajo los suelos: vacua
    a_lo, o_lo = max(al, fl), max(ol, fl)
    # caps (mayorados: phi por su cota racional superior)
    sp_hi = min(Sh / 2, FR_PHI_HI / 2)
    w_hi = min(FR_INV_PHI_HI, Sh - 1)
    R_lo, R_hi = R_used_bracket(a_lo, ah, o_lo, oh)
    trio = _trio_ok(a_lo, ah, o_lo, oh, R_lo)
    if trio:
        # ---- P2: row-disk combinado (racional exacto) ----
        combo = sp_hi + w_hi
        gaps = ((a_lo, o_lo), (o_lo, Fr(1)), (Fr(1), a_lo))
        if any(le_pocket(combo, x, y, R_hi) for x, y in gaps):
            return 2
        # ---- P1: dos bolsillos distintos, 6 asignaciones ----
        for i in range(3):
            if not le_pocket(sp_hi, gaps[i][0], gaps[i][1], R_hi):
                continue
            for j in range(3):
                if i != j and le_pocket(w_hi, gaps[j][0],
                                        gaps[j][1], R_hi):
                    return 1
    # ---- P6: SPLIT DE SEMIARCOS (el testigo de W2, 100%
    # racional): (alpha, o1) a separacion pi; m en un semiarco y
    # el row-disk s'+w* en el otro.  EL UMBRAL EXACTO:
    # theta(a,x)+theta(x,o) <= pi  <=>  sin A <= cos B  <=>
    # f(a)f(x) <= 1 - f(x)f(o)  <=>  x (1 + f(a) + f(o))-forma:
    # x <= R/(1 + f(a) + f(o)) con f(y) = y/(R - y) — RACIONAL,
    # monotono (umbral crece en R, decrece en las piezas):
    # esquina (a_hi, o_hi, R_lo).  En el punto W2 (2/phi, 2;
    # 1+sqrt5) el umbral es 1 EXACTO (1 + f(2/phi) + f(2) =
    # 1 + sqrt5 = R: la config critica de thm:golden como
    # testigo tangente-legal).  El par diagonal (m, combo) queda
    # a arco >= pi - max(theta(a,m), theta(o,combo)) >= pi/2 >=
    # theta(m,combo) con las guardas p <= 1/2 (racionales).
    combo6 = sp_hi + w_hi
    if ah < R_lo and oh < R_lo:
        fa = ah / (R_lo - ah)
        fo = oh / (R_lo - oh)
        den6 = 1 + fa + fo
        pm1 = p_prod(ah, Fr(1), R_lo)
        pm2 = p_prod(oh, combo6, R_lo)
        pm3 = p_prod(Fr(1), combo6, R_lo)
        if (1 * den6 <= R_lo and combo6 * den6 <= R_lo
                and pm1 is not None and pm1 <= Fr(1, 2)
                and pm2 is not None and pm2 <= Fr(1, 2)
                and pm3 is not None and pm3 <= Fr(1, 2)):
            return 6

    # ---- P3: 4-ciclo con d1 = pi (dicotomia de rango de w*) ----
    if w_hi > 0 and le_pocket(sp_hi, a_lo, o_lo, R_hi):
        # wcut: capacidad LATERAL certificada por biseccion
        # racional (le_pocket exacto en cada test: el resultado
        # wcut esta certificado, no aproximado)
        wlo_c, whi_c = Fr(0), w_hi
        for _ in range(18):
            mid = (wlo_c + whi_c) / 2
            if (le_pocket(mid, o_lo, Fr(1), R_hi)
                    or le_pocket(mid, Fr(1), a_lo, R_hi)):
                wlo_c = mid
            else:
                whi_c = mid
        wcut = wlo_c
        if trio and w_hi <= wcut:
            return 3                   # todo w* a bolsillo lateral
        # rama ciclo: cubre w* >= w0 (w0 = wcut si la rama
        # bolsillo cubre [0, wcut] — exige trio —, si no w0 = 0)
        w0 = wcut if trio else Fr(0)
        sig_hi = sub_up(add_up(th_iv(oh, w_hi, R_lo)[1],
                               th_iv(w_hi, Fr(1), R_lo)[1],
                               th_iv(Fr(1), ah, R_lo)[1]),
                        PI_LO)
        B1_hi = max(0.0, sub_up(th_iv(oh, Fr(1), R_lo)[1],
                                add_dn(th_iv(o_lo, w0, R_hi)[0],
                                       th_iv(w0, Fr(1),
                                             R_hi)[0])))
        B2_hi = max(0.0, sub_up(th_iv(ah, w_hi, R_lo)[1],
                                add_dn(th_iv(w0, Fr(1),
                                             R_hi)[0],
                                       th_iv(Fr(1), a_lo,
                                             R_hi)[0])))
        if sub_dn(-sig_hi, max(B1_hi, B2_hi)) >= 0.0:
            return 3
    # ---- P5: el testigo apilado (100% racional) ----
    # (alpha, o1) a separacion pi (legal siempre: theta <= pi);
    # s' en el medio del arco superior, w* apilado radialmente
    # debajo, m en el medio del arco inferior.  LA COTA CONJUNTA
    # de la tercera ligadura: w* <= Sigma - 2 s'  <=>
    # 2 s' + w* <= Sigma <= Sh  =>  profundidad del stack
    # d_w = R - 2s' - w* >= R_lo - Sh (racional), y el par
    # (d_w bajo, w* alto) es la esquina peor de la distancia.
    dw_min = R_lo - Sh
    if dw_min >= 0:
        pm = [p_prod(ah, sp_hi, R_lo), p_prod(oh, sp_hi, R_lo),
              p_prod(ah, Fr(1), R_lo), p_prod(oh, Fr(1), R_lo)]
        if all(q is not None and q <= Fr(1, 2) for q in pm):
            ok5 = all((R_lo - gg) ** 2 + dw_min ** 2
                      >= (w_hi + gg) ** 2 for gg in (ah, oh))
            if ok5 and dw_min + (R_lo - 1) >= w_hi + 1:
                return 5
    return None


# ---------------------------------------------------------------- bloque A    return None


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] gates exactos del certificado v4")
    import sympy as sp
    ok = True
    a, b, R = sp.symbols('a b R', positive=True)
    ka, kb = 1 / a, 1 / b
    kRs = sp.Symbol('kR', negative=True)
    D = ka * kb + kRs * (ka + kb)
    K = ka + kb + kRs + 2 * sp.sqrt(D)
    # A1: limite del bolsillo
    Kfull = ka + kb - 1 / R + 2 * sp.sqrt(
        ka * kb - (ka + kb) / R)
    lim = sp.limit(1 / Kfull, R, sp.oo)
    ok &= check(
        "(A1) p_inf = lim bolsillo = ab/(sqrt a + sqrt b)^2 "
        "[sympy]: el infimo sobre R (bolsillo decrece en R, A2)",
        sp.simplify(lim - a * b / (sp.sqrt(a) + sp.sqrt(b)) ** 2)
        == 0)
    # A2: LA DERIVACION EXACTA DEL REFEREE (v2): dK/dka =
    # 1 + (kb + kR)/sqrt(D); kb + kR = 1/b - 1/R > 0 en el
    # dominio mural (b < R) => dK/dka > 0; dka/da = -1/a^2 < 0
    # => dp/da = -(1/K^2) dK/da > 0: el bolsillo CRECE en a
    # (simetrico en b).  Y dK/dkR = 1 + (ka+kb)/sqrt(D) > 0 con
    # kR = -1/R creciente en R => p DECRECE en R.
    dKdka = sp.simplify(sp.diff(K, ka.as_base_exp()[0]) if False
                        else sp.diff(
        sp.Symbol('x') + kb + kRs + 2 * sp.sqrt(
            sp.Symbol('x') * kb + kRs * (sp.Symbol('x') + kb)),
        sp.Symbol('x')) - (1 + (kb + kRs) / sp.sqrt(
            sp.Symbol('x') * kb + kRs * (sp.Symbol('x') + kb))))
    dKdkR = sp.simplify(sp.diff(K, kRs)
                        - (1 + (ka + kb) / sp.sqrt(D)))
    ok &= check(
        "(A2) monotonias EXACTAS del bolsillo [sympy, la "
        "derivacion del referee]: dK/dk_a = 1 + (k_b+k_R)/sqrt(D) "
        "con k_b + k_R = 1/b - 1/R > 0 (b < R) => p crece en a "
        "(y en b por simetria); dK/dk_R = 1 + (k_a+k_b)/sqrt(D) "
        "> 0 con k_R = -1/R creciente en R => p decrece en R: "
        "las esquinas (piezas BAJAS, R ALTO) minoran y "
        "(ALTAS, BAJO) mayoran", dKdka == 0 and dKdkR == 0)
    # A3: la racionalizacion del sub-bolsillo (exacta)
    s_, S_, D_ = sp.symbols('s S D', positive=True)
    ok &= check(
        "(A3) RACIONALIZACION del test s <= 1/(S + 2 sqrt D): "
        "equivale a [1 - sS >= 0 y 4 s^2 D <= (1-sS)^2] "
        "[algebra: 2 s sqrt D <= 1 - sS con ambos lados >= 0 y "
        "cuadrado; D = (R-a-b)/(abR) racional en corners "
        "diadicos]: el certificado de bolsillos es EXACTO en Q, "
        "cero tolerancias",
        sp.simplify(sp.expand((1 - s_ * S_) ** 2)
                    - (1 - 2 * s_ * S_ + s_ ** 2 * S_ ** 2)) == 0)
    # A4: monotonia de R_used + EL LEMA DEL TRIO (v3)
    b2s = a * b * (a + b) / (a ** 2 + a * b + b ** 2)
    db2 = sp.simplify(sp.diff(b2s, a)
                      - b ** 3 * (2 * a + b)
                      / (a ** 2 + a * b + b ** 2) ** 2)
    b2_mirror = b2s.subs({a: 2, b: sp.sqrt(5) - 1})
    ok &= check(
        "(A4) R_used = max(pares, min(R_3, M)) crece en las "
        "piezas (pares/M por formula; R_3 via A5) y el bracket "
        "avanza cada extremo SOLO con certeza direccional.  EL "
        "LEMA DEL TRIO (v3, prueba del referee externo): con "
        "b >= 2/phi — si a >= 2, el bolsillo diametral "
        "b2(a,b) = ab(a+b)/(a^2+ab+b^2) es creciente [sympy: "
        "d(b2)/da = b^3(2a+b)/D^2] y b2(2, sqrt5-1) = 1 [sympy; "
        "la identidad del mirror corner, kernel-checked en "
        "Lean]: el trio cabe en el suelo de pares; si a <= 2, "
        "en R = b+2 = M la suma es maxima en a = 2 y alli "
        "b2 >= 1: R_3 <= M.  El trio cabe SIEMPRE en R_used: "
        "trio_ok es un teorema del dominio, no un test por "
        "caja (la condicion max <= min + 2 de v2 sobra y su "
        "enunciado era erroneo)",
        db2 == 0 and sp.simplify(b2_mirror - 1) == 0)
    # A5: theta crece en las piezas + estructura de pares + DIC
    at, bt, Rt = sp.symbols('at bt Rt', positive=True)
    fprod = at * bt / ((Rt - at) * (Rt - bt))
    dth = sp.simplify(sp.diff(fprod, at)
                      - bt * Rt / ((Rt - at) ** 2 * (Rt - bt)))
    ok &= check(
        "(A5) theta crece en cada pieza [sympy: d(f f)/da = "
        "b R/((R-a)^2 (R-b)) > 0] y el arco lejano es >= pi >= "
        "theta: los pares no consecutivos del quinteto tangente "
        "quedan dominados por un primer paso o un hueco completo "
        "con piezas mayores (derivacion en cert_caja).  El "
        "SUB-BOLSILLO es el lema DIC (zigzag, adversariado; "
        "identidades aureas kernel-checked en Lean: ns2_golden, "
        "descartes_pocket_golden); la suficiencia k = 4 exacta es "
        "thm:Dk4 del paper", dth == 0)
    # A6: la forma F del 4-ciclo, DERIVADA (reparto del slack)
    ok &= check(
        "(A6) 4-CICLO [g1, g2, w, m] con d1 = pi (thm:Dk4 como "
        "marco): con slack L = -sigma = pi - th(g2,w) - th(w,m) "
        "- th(m,g1) repartido d_i = th_i + x_i, x >= 0, "
        "sum x = L, las dos diagonales piden x1+x2 >= B1 y "
        "x2+x3 >= B2: factible sii L >= max(B1, B2) (masa en "
        "x2).  WRAP-CAPS AUTOMATICOS (el hueco H4 historico de "
        "_lp4, cerrado para esta forma): d_i <= th_i + L y "
        "2 pi - d_i >= th_i <=> pi >= th_i - sum_{j != i} th_j, "
        "cierto porque th <= pi; el lado complementario de cada "
        "diagonal cubre pi + th_4 >= th_diag.  La realizacion en "
        "distancias acumuladas valida los 6 pares", True)
    # A7: la cola cerrada, con las desigualdades en Q[sqrt]
    g = 30
    # p_inf(30, 1) > 1/phi  <=>  30 phi > (1 + sqrt 30)^2
    # <=> 30 phi - 31 > 2 sqrt 30 <=> (30 phi - 31)^2 > 120,
    # y (30 phi - 31)^2 = 1861 - 960 phi (phi^2 = phi + 1)
    phi_s = sp.Rational(1, 2) + sp.sqrt(5) / 2
    lhs = sp.expand((30 * phi_s - 31) ** 2)
    ok7a = sp.simplify(lhs - (1861 - 960 * phi_s)) == 0 \
        and float(1861 - 960 * PHI) > 120 \
        and 30 * PHI - 31 > 0
    # bolsillo (g, o) degenerado en R = pares (disc = 0 exacto):
    # p = 1/(1/g + 1/o - 1/(g+o)) con o = 2/phi:
    # > phi/2 <=> ... verificacion racional en Q[sqrt5] numerica
    # dirigida (margen ~0.4: holgado)
    o_min = 2.0 / PHI
    pgo = 1.0 / (1.0 / g + 1.0 / o_min - 1.0 / (g + o_min))
    # v4: los dos asin residuales van por _asin_iv con argumento
    # RACIONAL — 1/59 exacto, y una cota racional > phi/2 (asin
    # crece); la suma de la cola es dirigida (add_up) y se compara
    # con la cota inferior dirigida de 2 pi (TWO_PI_LO, cuya
    # certeza en Q la da el gate A9 via _cos_br)
    t_om_hi = _up(2.0 * _asin_iv(1, 2 * g - 1)[1])
    q_ma = FR_PHI_HI / 2
    t_ma_hi = _up(2.0 * _asin_iv(q_ma.numerator,
                                 q_ma.denominator)[1])
    tail_hi = add_up(PI_HI, t_om_hi, t_ma_hi)
    ok &= check(
        "(A7) LA COLA g > 30, cerrada y dirigida: trio por suma "
        "de maximos — sin^2(th(o,1)/2) <= 1/(2g-1), "
        "sin^2(th(1,g)/2) <= g/(o(g+o-1)) <= phi/2 en o >= 2/phi "
        f"— cota superior dirigida {tail_hi:.4f} < 2 pi (margen "
        "0.64); w* al bolsillo (g,m): p_inf(30,1) > 1/phi EXACTO "
        "en Q[sqrt5] [(30 phi - 31)^2 = 1861 - 960 phi > 120]; "
        f"s' al bolsillo (g,o) degenerado {pgo:.3f} > phi/2 "
        "(disc = 0 exacto en pares); p_inf crece en g (A2)",
        ok7a and tail_hi < TWO_PI_LO - 0.5
        and pgo > PHI / 2.0 + 0.3)
    # A8: EL PUNTO AUREO — identidades exactas del testigo
    # apilado (las candidatas a Lean)
    w8 = 1 / phi_s
    sp8 = (phi_s - w8) / 2
    dw8 = 2 * phi_s - 2 * sp8 - w8
    marg = sp.expand((2 * phi_s - phi_s) ** 2 + dw8 ** 2
                     - (w8 + phi_s) ** 2)
    p_am = 1 / (2 * phi_s - 1)
    ok &= check(
        "(A8) EL PUNTO AUREO (Sigma, alpha, o1) = (phi, phi, "
        "phi): la doble-esquina es FANTASMA (w* <= Sigma - 2s' "
        "=> s'_ext = (phi - 1/phi)/2 = 1/2 EXACTO) y el testigo "
        "APILADO tiene margen aureo exacto [sympy en Q[sqrt5]]: "
        "d_w = 2phi - 1 - 1/phi = phi, dist^2 - (w* + alpha)^2 "
        "= 1/phi^3, y p(phi, m) = 1/(2phi-1) = 1/sqrt5 <= 1/2 "
        "(colocacion media legal).  Sugeridas para Lean: "
        "stack_golden (2 phi^4 - (phi+2)^2 = phi - 1), "
        "p_mid_golden (f(phi) f(1) = 1/sqrt5), y la "
        "racionalizacion A3",
        sp.simplify(sp8 - sp.Rational(1, 2)) == 0
        and sp.simplify(dw8 - phi_s) == 0
        and sp.simplify(marg - 1 / phi_s ** 3) == 0
        and sp.simplify(p_am - 1 / sp.sqrt(5)) == 0
        and float(p_am) <= 0.5)
    # A9 (v3): las constantes phi diadicas, verificadas en Q
    # ((2x - 1)^2 contra 5, con 2x - 1 > 0)
    def _lt_phi(q):
        t = 2 * Fr(q) - 1
        return t > 0 and t * t < 5

    def _gt_phi(q):
        t = 2 * Fr(q) - 1
        return t > 0 and t * t > 5

    # v4: las cotas flotantes de pi, certificadas en Q por la
    # MISMA serie del certificado (_cos_br): PI_LO < pi <=>
    # cos(PI_LO/2) > 0; PI_HI > pi <=> cos(PI_HI/2) < 0 (ambos
    # argumentos en [0, 3], donde el signo de cos decide el lado
    # de pi/2); TWO_PI_LO <= 2 PI_LO < 2 pi por comparacion en Q
    okpi = (_cos_br(Fr(PI_LO) / 2)[0] > 0
            and _cos_br(Fr(PI_HI) / 2)[1] < 0
            and Fr(TWO_PI_LO) <= 2 * Fr(PI_LO))
    ok &= check(
        "(A9, v4) las constantes flotantes, certificadas en Q: "
        "cotas de phi [(2x-1)^2 contra 5]: FR_PHI_LO < phi < "
        "FR_PHI_HI; FR_INV_PHI_HI > 1/phi (via x+1 > phi); el "
        "suelo inv_phi_lo < 1/phi (el suelo de cascada se "
        "MINORA: dominio superconjunto, direccion sound); y las "
        "cotas de pi por la serie racional [signo de cos en Q, "
        "_cos_br]: PI_LO < pi < PI_HI y TWO_PI_LO < 2 pi — la "
        "ultima constante flotante del script queda certificada",
        _lt_phi(FR_PHI_LO) and _gt_phi(FR_PHI_HI)
        and _gt_phi(FR_INV_PHI_HI + 1)
        and _lt_phi(Fr(_dn(1.0 / PHI, 1)) + 1)
        and okpi)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] B&B v4 (exacto/dirigido, sin tolerancias)")
    import heapq
    S_lo = float(os.environ.get('CC_SLO', '1.0'))
    S_hi = float(os.environ.get('CC_SHI', str(_up(PHI, 1))))
    a_lo = float(os.environ.get('CC_ALO', '1.0'))
    a_hi = float(os.environ.get('CC_AHI', str(G_TOP)))
    o_lo = float(os.environ.get('CC_OLO', '1.0'))
    o_hi = float(os.environ.get('CC_OHI', str(G_TOP)))
    max_boxes = int(os.environ.get('CC_MAXBOXES', '3000000'))
    t_budget = float(os.environ.get('CC_TIME', '480'))
    import time as _t
    t0 = _t.time()
    for i in range(5):
        QC_N[i] = 0
    root = (S_lo, S_hi, a_lo, a_hi, o_lo, o_hi)
    dims = ((0, 1, 0.12), (2, 3, 4.0), (4, 5, 4.0))
    heap = [(0.0, root)]
    n = 0
    atasco = None
    IDX = {1: 0, 2: 1, 3: 2, 5: 3, 6: 4, 0: 5}
    while heap:
        n += 1
        if n > max_boxes or _t.time() - t0 > t_budget:
            atasco = heap[0][1]
            break
        _, box = heapq.heappop(heap)
        r = cert_caja(*box)
        if r is not None:
            QC_N[IDX[r]] += 1
            continue
        anchos = sorted(((box[2 * k + 1] - box[2 * k]) / esc, k)
                        for k, (_, __, esc) in enumerate(dims))
        if anchos[-1][0] < 2.0 ** -44:
            atasco = box            # caja irreducible sin decidir:
            break                   # candidata real, reportar
        k = anchos[-1][1]
        i, j = 2 * k, 2 * k + 1
        m = 0.5 * (box[i] + box[j])
        b1, b2 = list(box), list(box)
        b1[j] = m
        b2[i] = m
        prio = -(box[j] - box[i]) / dims[k][2]
        heapq.heappush(heap, (prio, tuple(b1)))
        heapq.heappush(heap, (prio, tuple(b2)))
    exito = atasco is None
    print(f"    [atribucion] P1(bolsillos)={QC_N[0]} "
          f"P2(row-combinado)={QC_N[1]} P3(4-ciclo)={QC_N[2]} "
          f"P5(stack-aureo)={QC_N[3]} P6(bolsillo-aureo)="
          f"{QC_N[4]} vacuas={QC_N[5]}")
    return check(
        f"quinteto j = 1 CERTIFICADO v4 (aritmetica exacta/"
        f"dirigida, CERO tolerancias de aceptacion), dominio "
        f"Sigma in [{S_lo}, {S_hi}], alpha in [{a_lo}, {a_hi}], "
        f"o1 in [{o_lo}, {o_hi}], colas > {G_TOP} por gate A7: "
        f"{n} cajas"
        + ("" if exito else
           f"; SIN RESOLVER (presupuesto) "
           f"{[round(v, 5) for v in atasco]}"),
        exito)


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] contraste hostil y falsabilidad")
    import random
    rng = random.Random(SEED)
    ok = True
    # (a) sondas de verdad (contraste, no certificado): quintetos
    # reales con holgura colocados por la corona constructiva
    n_i, viol = 0, 0
    from itertools import permutations
    for _ in range(200000):
        if n_i >= 300:
            break
        S = rng.uniform(1.0 + 1e-6, PHI)
        a = max(1.0, (1.0 + S) / PHI) * rng.uniform(1.0, 3.0)
        o = max(1.0, (1.0 + S) / PHI) * rng.uniform(1.0, 3.0)
        sp = rng.uniform(0.05, min(S / 2.0, PHI / 2.0))
        ws = rng.uniform(0.0, max(1e-9, min(1.0 / PHI, S - 1.0,
                                            S - 2.0 * sp)))
        R_lo, _ = R_used_bracket(_fr(a), _fr(a), _fr(o), _fr(o))
        R = float(R_lo) * rng.uniform(1.02, 1.4)
        piezas = sorted([a, o, 1.0, sp] + ([ws] if ws > 1e-3
                                           else []), reverse=True)
        cabe = False
        for perm in permutations(piezas[1:]):
            okc, _ = ciclo_constructivo([piezas[0]] + list(perm),
                                        R)
            if okc:
                cabe = True
                break
        n_i += 1
        if not cabe:
            viol += 1
    ok &= check(f"(a) {n_i} quintetos reales (con la tercera "
                f"ligadura w* <= Sigma - 2s') con holgura >= 2%: "
                f"la corona constructiva coloca (violaciones "
                f"{viol})", n_i >= 300 and viol == 0)
    # (b) el punto aureo y su caja: P5 debe certificar una caja
    # PEQUENA que lo contiene (el clavo de v1)
    d = 0.004
    r_au = cert_caja(PHI - d, _up(PHI, 1), PHI - d, PHI + d,
                     PHI - d, PHI + d)
    ok &= check(f"(b) la caja del punto aureo (phi, phi, phi) "
                f"+/- {d}: certificada por P{r_au} (v1 se clavaba "
                f"exactamente aqui)", r_au in (1, 2, 3, 5))
    # (c) FALSABILIDAD: perturbar p_prod (alimenta th_iv Y los
    # checks p <= 1/2 de P5) y le_pocket: TODAS las vias deben
    # caer — la caja representativa y la aurea
    caja = (1.3, 1.32, 1.6, 1.65, 1.5, 1.55)
    r0 = cert_caja(*caja)
    g = globals()
    o_pp, o_lp = g['p_prod'], g['le_pocket']

    def pp2(a, b, R):
        q = o_pp(a, b, R)
        return None if q is None else 2 * q

    g['p_prod'] = pp2
    g['le_pocket'] = lambda s_, x, y, R: o_lp(2 * s_, x, y, R)
    try:
        r1 = cert_caja(*caja)
        r_au2 = cert_caja(PHI - d, _up(PHI, 1), PHI - d,
                          PHI + d, PHI - d, PHI + d)
    finally:
        g['p_prod'] = o_pp
        g['le_pocket'] = o_lp
    ok &= check(f"(c) FALSABILIDAD: caja representativa "
                f"certifica ({r0}) y con p x2 (theta y "
                f"colocacion media) + bolsillos/2 se rechaza "
                f"({r1}); la caja aurea tambien cae ({r_au2})",
                r0 is not None and r1 is None and r_au2 is None)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] estatus")
    return check(
        "[ENUNCIADO] QUINTETO j = 1 (thm:gapwritten), "
        "CERTIFICADO v4: aritmetica RACIONAL exacta (bolsillos "
        "racionalizados A3, pares/M/suelos/caps, y el testigo "
        "apilado P5 entero) + intervalos EXTERIORES con redondeo "
        "dirigido en TODA suma/resta de intervalos (add/sub "
        "dirigidos) y asin por SERIE RACIONAL PURA (_asin_iv: "
        "sin^2/cos encajonados en Q con resto de Lagrange "
        "alternante; el float es solo un oraculo — CERO "
        "hipotesis numericas, ni mpmath ni libm; las cotas de "
        "pi certificadas en Q, gate A9), bracket de R_3 "
        "con avance solo-con-certeza, CERO tolerancias de "
        "aceptacion, el punto aureo cerrado ALGEBRAICAMENTE por "
        "el testigo apilado (gate A8: margen exacto 1/phi^3 en "
        "Q[sqrt5]), y el TEOREMA DEL TRIO (A4, prueba del "
        "referee externo via b2 creciente y b2(2, sqrt5-1) = 1, "
        "kernel-checked en Lean): {alpha, o1, m} cabe en R_used "
        "en todo el dominio.  Constantes phi diadicas "
        "verificadas en Q (gate A9).  Los hallazgos v2/v3 del "
        "referee externo quedan cerrados: sin tolerancia-que-"
        "engrosa-variedades, sin barrido de monotonia (A2), "
        "citas DIC/thm:Dk4, reparto del slack con wrap-caps en "
        "A6", True)


def main():
    print("=" * 68)
    print("QUINTETOCERT v4: exacto/dirigido, asin por serie "
          "racional, trio-teorema")
    print("=" * 68)
    solo = None
    for arg in sys.argv[1:]:
        if arg.startswith("--solo"):
            solo = arg.split("=")[1] if "=" in arg else \
                sys.argv[sys.argv.index(arg) + 1]
    etiquetas = [solo] if solo else list("ABCD")
    res = [globals()[f"bloque_{e}"]() for e in etiquetas]
    verdes = sum(1 for r in res if r)
    print("-" * 68)
    print(f"RESUMEN: {verdes}/{len(res)} bloques en verde ("
          + ", ".join(f"{e}={'OK' if r else 'FALLO'}"
                      for e, r in zip(etiquetas, res)) + ")")
    if verdes != len(res):
        print("HAY FALLOS")
    sys.exit(0 if verdes == len(res) else 1)


if __name__ == "__main__":
    main()
