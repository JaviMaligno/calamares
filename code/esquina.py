"""Esquina 13/7 (docs/drafts/esquina.md): curva exacta de T_can y el infimo global.

Con la frontera cerrada de H1 (docs/drafts/h1.md: infactible <=> t(s1) + t(s2)
<= t(b(alpha)), t(s) = sqrt((1-s)/s)), el programa de bloqueo con grosor de
grosor_positivo.md se resuelve en forma cerrada:

  (i)   T_can(omega) = 2(1-omega)                     en (0, omega_1],
        con omega_1 la raiz en (1/25, 1/14) de  4w^3 - 20w^2 + 25w - 1
        (juntura exacta s*(2-w) = 1-w, antes "sin forma cerrada");
  (ii)  T_can(omega) = alpha_m(omega) - omega         en [omega_1, 1/7],
        con alpha_m la raiz en (1, 2] de  t(a-1) + t(1-w) = t(b(a)),
        algebraica de grado 6: P(alpha, omega) = 0 (polinomio explicito);
  (iii) T_can(omega) = Phi(omega) = T_{1+omega} - omega  en [1/7, 0.30]
        (la rama del testigo de la Proposicion 4, sin cambios).

  TEOREMA (esquina): inf_{omega>0} T_can = 13/7, alcanzado (en el limite
  sigma_1 -> 1) solo en la esquina (omega, alpha, sigma_2) = (1/7, 2, 6/7).
  La cota inferior es universal; la familia de la esquina es GENUINA
  (Proposicion S5 + Lema S6a de suelo_rigido.md), asi que el infimo global
  no depende de la exactitud de feas3.

  ESTRUCTURA FINA (corrige grosor_positivo.md par. 4): la curva NO decrece en
  todo (0, 1/7]: omega_1 es un MINIMO local (valor 2(1-omega_1) ~ 1.9172860),
  V' (omega_1+) = c/(r'-c) > 0 EXACTO, y hay un maximo local en
  omega_peak ~ 0.0444700 (raiz de un polinomio de grado 8), altura +1.1e-4.
  El bump es invisible a la malla de grosor.py [D] (paso >= 0.005).

Motor de todas las monotonias: el G-lema de H1 (G(t) = t^2/(1+t^2)^4,
sigma'(x) = -2 sqrt(G(x))): sobre el segmento t1 + t2 = t(b), S = s1 + s2
decrece al mover t2 hacia arriba, y las ramas S^b(alpha) y B4 son crecientes
en alpha.

Bloques: [A] algebra exacta (sympy), [B] rama mixta contra P y contra la tabla
medida, [C] curva exacta contra fuerza bruta con el criterio angular (sin
coordenada t), [D] estructura fina (bump, dos minimos locales, esquina),
[E] familia genuina de la esquina.
"""
import math

TWO_PI = 2 * math.pi
TRIB = 1.839286755214161
CORNER = 13.0 / 7.0


# ---------------- primitivas (independientes de code/h1.py) ----------------

def b_pocket(a):
    return a * (a + 1) / (a * a + a + 1)


def s_diag(a):
    return 4 * a * (a + 1) / (2 * a + 1) ** 2


def t_of(s):
    return math.sqrt((1 - s) / s)


def s_of(t):
    return 1.0 / (1.0 + t * t)


def theta(a, b, R):
    p = (a / (R - a)) * (b / (R - b))
    if p >= 1.0:
        return math.pi if p <= 1.0 + 1e-12 else math.inf
    return 2 * math.asin(math.sqrt(p))


def Fsum(alpha, s1, s2):
    R = alpha + 1.0
    return theta(alpha, s1, R) + theta(alpha, s2, R) + theta(s1, s2, R)


def h_boundary(alpha, s1, iters=200):
    lo, hi = 1e-12, s1
    if Fsum(alpha, s1, hi) < TWO_PI or Fsum(alpha, s1, lo) > TWO_PI:
        return None
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if Fsum(alpha, s1, mid) > TWO_PI:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def omega_1():
    """Raiz de 4w^3 - 20w^2 + 25w - 1 en (1/25, 1/14), por biseccion."""
    p = lambda w: ((4 * w - 20) * w + 25) * w - 1
    lo, hi = 1 / 25, 1 / 14
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if p(mid) > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


W1 = omega_1()


def alpha_m(w, iters=200):
    """Raiz de Psi(a) = t(b(a)) - t(a-1) = t(1-w) en (1, 2] (Psi creciente)."""
    r = t_of(1 - w)
    f = lambda a: 1 / math.sqrt(a * (a + 1)) - t_of(a - 1) - r
    lo, hi = 1 + 1e-15, 2.0
    if f(hi) < 0:
        return None                      # w > 1/7: no hay raiz en (1, 2]
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def T_c(c):
    """Raiz positiva de a^3 = c(a^2 + a + 1), biseccion."""
    f = lambda a: a ** 3 - c * (a * a + a + 1)
    lo, hi = 1.0, 3.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def Phi(w):
    return T_c(1 + w) - w


def curva_exacta(w):
    """T_can(omega) segun la Proposicion 7."""
    if w <= W1:
        return 2 * (1 - w)
    if w <= 1 / 7:
        return alpha_m(w) - w
    return Phi(w)


def check(label, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {label}")
    return ok


# ---------------- [A] algebra exacta ----------------

def bloque_A():
    import sympy as sp
    a, w, x = sp.symbols('alpha omega x', positive=True)
    ok = True
    X2 = (2 - a) / (a - 1)          # t(alpha-1)^2
    Y2 = w / (1 - w)                # t(1-omega)^2
    Z2 = 1 / (a * (a + 1))          # t(b(alpha))^2
    # A1: P(alpha, omega) := numerador de (Z2-X2-Y2)^2 - 4 X2 Y2; grados (6, 2).
    #     P = 0 es NECESARIO para la ecuacion de la rama mixta X + Y = Z
    #     (doble cuadratura; el producto de las 4 ramas (Z±X±Y)).
    Pnum = sp.expand(sp.numer(sp.together((Z2 - X2 - Y2) ** 2 - 4 * X2 * Y2)))
    Pp = sp.Poly(Pnum, a, w)
    ok &= check(f"A1 P(alpha, omega) tiene grados (6, 2): {Pp.degree(a)}, {Pp.degree(w)}",
                Pp.degree(a) == 6 and Pp.degree(w) == 2)
    # A2: q(w) = P(13/7 + w, w) = 4(7w - 1) Q5(w) / 7^6 y Q5 NO tiene raices en
    #     [1/25, 1/7]: la rama mixta no cruza V = 13/7 antes de la esquina.
    q = sp.factor(sp.expand(Pnum.subs(a, sp.Rational(13, 7) + w)))
    Q5 = None
    for f, m in sp.factor_list(q)[1]:
        fp = sp.Poly(f, w)
        if fp.degree() == 5:
            Q5 = fp
    lin_ok = any(sp.simplify(f - (7 * w - 1)) == 0 for f, m in sp.factor_list(q)[1])
    ok &= check("A2a q(w) = P(13/7+w, w) tiene el factor lineal (7w - 1)", lin_ok)
    n_roots = Q5.count_roots(sp.Rational(1, 25), sp.Rational(1, 7))
    ok &= check(f"A2b el factor quintico no tiene raices en [1/25, 1/7] ({n_roots})",
                Q5 is not None and n_roots == 0)
    # A3: cubica de la juntura: s*(2-w) = 1-w  <=>  w(5-2w)^2 = 1, es decir
    #     4w^3 - 20w^2 + 25w - 1 = 0; creciente en (0, 5/6); 1/25 < w1 < 1/14.
    cub = 4 * w ** 3 - 20 * w ** 2 + 25 * w - 1
    lhs = (1 - w) - 4 * (2 - w) * (3 - w) / (2 * (2 - w) + 1) ** 2
    ok &= check("A3a s*(2-w) - (1-w) tiene numerador -(4w^3-20w^2+25w-1)",
                sp.simplify(sp.numer(sp.together(lhs)) + cub * sp.sign(1)) == 0
                or sp.simplify(sp.factor(sp.numer(sp.together(lhs))) + sp.factor(cub)) == 0)
    dcub = sp.expand(sp.diff(cub, w) - (5 - 2 * w) * (5 - 6 * w))
    ok &= check("A3b d/dw = (5-2w)(5-6w) > 0 en (0, 5/6)", dcub == 0)
    cp = sp.Poly(cub, w)
    ok &= check("A3c una unica raiz en (0, 1), en (1/25, 1/14)",
                cp.count_roots(0, 1) == 1
                and cp.count_roots(sp.Rational(1, 25), sp.Rational(1, 14)) == 1)
    # A4: V(w1) - 13/7 = 1/7 - 2 w1 > 0  (w1 < 1/14); V(1/7) = 13/7 exacto
    #     (alpha_m(1/7) = 2: t(1) = 0 y t(1 - 1/7) = t(6/7) = t(b(2))).
    ok &= check("A4a b(2) = 6/7 y t(6/7)^2 = 1/6 = 1/(2*3)",
                sp.Rational(2 * 3, 7) == sp.nsimplify(b_pocket(2))
                and sp.simplify((1 - sp.Rational(6, 7)) / sp.Rational(6, 7)
                                - sp.Rational(1, 6)) == 0)
    ok &= check("A4b P(2, 1/7) = 0 (la esquina esta en la curva)",
                sp.simplify(Pnum.subs({a: 2, w: sp.Rational(1, 7)})) == 0)
    # A5: V'(w1+) > 0 EXACTO: en la juntura alpha = 2 - w1 vale
    #     Psi'(alpha) = r'(w) - c(alpha) con el MISMO primer termino
    #     r'(w) = 1/(2 sqrt(w(1-w)^3)) y c = (2a+1)/(2(a^2+a)^{3/2}) > 0,
    #     luego V' = r'/Psi' - 1 = c/(r' - c) > 0.
    rp = 1 / (2 * sp.sqrt(w * (1 - w) ** 3))
    first = 1 / (2 * sp.sqrt((a - 1) ** 3 * (2 - a)))
    ok &= check("A5 primer termino de Psi' en alpha = 2-w es r'(w) exactamente",
                sp.simplify(first.subs(a, 2 - w) - rp) == 0)
    # A6: el polinomio de grado 8 de omega_peak (resultante de P y P_a + P_w)
    #     tiene UNA sola raiz en [1/25, 1/7]: el maximo local es unico.
    crit = sp.expand(sp.diff(Pnum, a) + sp.diff(Pnum, w))
    R = sp.resultant(sp.Poly(Pnum, a), sp.Poly(crit, a))
    R8 = None
    for f, m in sp.factor_list(sp.expand(R))[1]:
        fp = sp.Poly(f, w)
        if fp.degree() == 8:
            R8 = fp
    ok &= check("A6a el resultante tiene un factor de grado 8",
                R8 is not None)
    ok &= check(f"A6b R8 tiene exactamente 1 raiz en [1/25, 1/7]",
                R8.count_roots(sp.Rational(1, 25), sp.Rational(1, 7)) == 1)
    wpk = [r for r in sp.real_roots(R8)
           if sp.Rational(1, 25) < r < sp.Rational(1, 7)][0]
    print(f"     omega_peak = {sp.N(wpk, 20)}")
    # A7: motor de monotonia: sigma'(x) = -2x/(1+x^2)^2 y (sigma'/2)^2 = G(x)
    G = x ** 2 / (1 + x ** 2) ** 4
    sig = 1 / (1 + x ** 2)
    ok &= check("A7 sigma'(x) = -2x/(1+x^2)^2 y (sigma'/2)^2 = G",
                sp.simplify(sp.diff(sig, x) + 2 * x / (1 + x ** 2) ** 2) == 0
                and sp.simplify((sp.diff(sig, x) / 2) ** 2 - G) == 0)
    # A8: no bloqueo para alpha > 2 + omega: (B4) + banda dan
    #     S >= 2(alpha - omega - 1) > alpha - omega  <=>  alpha > 2 + omega.
    ok &= check("A8 2(alpha-omega-1) > alpha-omega  <=>  alpha > 2+omega",
                sp.simplify(2 * (a - w - 1) - (a - w) - (a - (2 + w))) == 0)
    # A9: Psi' > 0 en (1, 2]: al cuadrado, (a^2+a)^3 > (2a+1)^2 (a-1)^3 (2-a)
    #     (el LHS es >= 8 y el RHS <= 25*27/256 < 3 en el intervalo).
    p9 = sp.expand((a ** 2 + a) ** 3 - (2 * a + 1) ** 2 * (a - 1) ** 3 * (2 - a))
    ok &= check("A9 (a^2+a)^3 - (2a+1)^2(a-1)^3(2-a) > 0 en (1, 2] (Psi creciente)",
                sp.Poly(p9, a).count_roots(1, 2) == 0
                and bool(p9.subs(a, sp.Rational(3, 2)) > 0))
    return ok


# ---------------- [B] rama mixta contra P y la tabla ----------------

def bloque_B():
    import sympy as sp
    ok = True
    a, w = sp.symbols('alpha omega', positive=True)
    X2 = (2 - a) / (a - 1)
    Y2 = w / (1 - w)
    Z2 = 1 / (a * (a + 1))
    Pnum = sp.expand(sp.numer(sp.together((Z2 - X2 - Y2) ** 2 - 4 * X2 * Y2)))
    # B1: la raiz de la biseccion satisface P = 0 (residuo relativo ~ 0)
    worst = 0.0
    for wv in (0.05, 0.06, 0.08, 0.10, 0.12, 0.14):
        am = alpha_m(wv)
        res = float(Pnum.subs({a: am, w: wv}))
        worst = max(worst, abs(res))
    ok &= check(f"B1 P(alpha_m(w), w) = 0 (residuo max {worst:.2e})", worst < 1e-10)
    # B2: contra la tabla medida de grosor_positivo.md par. 4 (malla ~4e-4)
    tabla = [(0.06, 1.915080), (0.075431, 1.909131), (0.09, 1.901024),
             (0.11, 1.886743), (0.125, 1.874100)]
    dev = max(abs(alpha_m(wv) - wv - med) for wv, med in tabla)
    ok &= check(f"B2 rama mixta contra los 5 valores medidos (desvio max {dev:.1e},"
                " la malla)", dev < 4e-4)
    # B3: juntura: alpha_m(w1) = 2 - w1 y V(w1) = 2(1 - w1)
    ok &= check(f"B3 alpha_m(w1) = 2 - w1 (err {abs(alpha_m(W1) - (2 - W1)):.1e})",
                abs(alpha_m(W1) - (2 - W1)) < 1e-12)
    # B4: esquina: alpha_m(1/7) = 2 exacto y V = 13/7
    am7 = alpha_m(1 / 7)
    ok &= check(f"B4 alpha_m(1/7) = 2 (err {abs(am7 - 2):.1e}) y V = 13/7",
                abs(am7 - 2) < 1e-12 and abs(am7 - 1 / 7 - CORNER) < 1e-12)
    return ok


# ---------------- [C] curva exacta contra fuerza bruta ----------------

def smin_bruto(alpha, w, n1=240):
    """min de rho sobre bloqueos en alpha: solo el criterio angular (biseccion
    de Fsum, 80 iteraciones bastan aqui) y las paredes (B2), (B4), (W), banda.
    Sin coordenada t: contraste independiente de la forma cerrada."""
    c = max(1 - w, alpha - w - 1)
    if c >= 1:
        return None
    best = None
    for i in range(n1):
        s1 = c + (1 - 1e-9 - c) * i / (n1 - 1)
        h = h_boundary(alpha, s1, iters=80)
        s2 = max(c, h) if h is not None else (s1 if Fsum(alpha, s1, s1) >= TWO_PI else None)
        if s2 is None or s2 > s1:
            continue
        if Fsum(alpha, s1, s2) < TWO_PI - 1e-9:
            continue
        S = s1 + s2
        if S <= alpha - w + 1e-12:
            rho = max(S, (1 + S) / alpha)
            best = rho if best is None else min(best, rho)
    return best


def bloque_C():
    ok = True
    worst = 0.0
    detalles = []
    for w in (0.02, 0.035, W1, 0.045, 0.05, 0.06, 0.075, 0.09, 0.11, 0.125,
              1 / 7, 0.16, 0.20, 0.25):
        # barrido grueso en alpha + refinado alrededor del mejor
        best, best_a = None, None
        na = 120
        lo_a, hi_a = 1 + w + 1e-6, 2 + w
        for _ in range(3):
            for j in range(na):
                alpha = lo_a + (hi_a - lo_a) * j / (na - 1)
                v = smin_bruto(alpha, w)
                if v is not None and (best is None or v < best):
                    best, best_a = v, alpha
            paso = (hi_a - lo_a) / (na - 1)
            lo_a, hi_a = max(1 + w + 1e-6, best_a - 2 * paso), best_a + 2 * paso
        pred = curva_exacta(w)
        dev = abs(best - pred)
        worst = max(worst, dev)
        detalles.append((w, best, pred, dev))
    for w, best, pred, dev in detalles:
        print(f"     w={w:.6f}  bruto={best:.6f}  formula={pred:.6f}  d={dev:.1e}")
    ok &= check(f"C  curva exacta contra fuerza bruta angular, 14 valores de w "
                f"(desvio max {worst:.1e}, resolucion de malla)", worst < 1e-3)
    return ok


# ---------------- [D] estructura fina ----------------

def bloque_D():
    ok = True
    # D1: bump: V(w) > 2(1-w1) en (w1, ~0.0477), maximo cerca de 0.04447
    vals = {w: alpha_m(w) - w for w in (W1 + 1e-6, 0.0435, 0.04447, 0.0455, 0.048)}
    ok &= check(f"D1a V(w1 + 1e-6) > V(w1) = 2(1-w1)  "
                f"(delta {vals[W1 + 1e-6] - 2 * (1 - W1):+.1e})",
                vals[W1 + 1e-6] > 2 * (1 - W1))
    ok &= check(f"D1b bump: V(0.04447) - 2(1-w1) = "
                f"{vals[0.04447] - 2 * (1 - W1):+.2e} ~ +1.1e-4",
                1e-4 < vals[0.04447] - 2 * (1 - W1) < 1.2e-4)
    ok &= check("D1c V crece y luego decrece (w1, 0.0435, 0.04447, 0.0455, 0.048)",
                vals[W1 + 1e-6] < vals[0.0435] < vals[0.04447]
                and vals[0.04447] > vals[0.0455] > vals[0.048])
    # D2: w1 es minimo local de T_can: a la izquierda 2(1-w) decrece hacia
    #     2(1-w1); a la derecha V sube (D1a)
    ok &= check("D2 T_can(w1 - 1e-4) > T_can(w1) < T_can(w1 + 1e-4)",
                curva_exacta(W1 - 1e-4) > curva_exacta(W1) < curva_exacta(W1 + 1e-4))
    # D3: la esquina es el minimo global de la formula en (0, 0.30]
    grid = [k / 4000 for k in range(1, 1201)]
    tmin, wmin = min((curva_exacta(w), w) for w in grid)
    ok &= check(f"D3 min de la curva en malla de 1200 puntos = {tmin:.7f} en "
                f"w = {wmin:.5f} (esquina 13/7 = {CORNER:.7f})",
                abs(wmin - 1 / 7) < 1e-3 and tmin >= CORNER - 1e-9)
    # D4: T_can >= 13/7 con igualdad SOLO en 1/7 (margen minimo fuera de un
    #     entorno de la esquina)
    margen = min(curva_exacta(w) - CORNER for w in grid if abs(w - 1 / 7) > 0.01)
    ok &= check(f"D4 T_can - 13/7 >= {margen:.2e} > 0 fuera de |w - 1/7| <= 0.01",
                margen > 0)
    return ok


# ---------------- [E] familia genuina de la esquina ----------------

def bloque_E():
    ok = True
    # Familia genuina hacia la esquina, DESDE alpha = 2 + delta (en alpha = 2,
    # omega = 1/7 exactos no hay familia: kappa > 1 da s1 + h(2, s1) > 13/7
    # para todo s1 < 1 y (W) se viola; hay que abrir (B4) con delta > 0):
    #
    #   omega = 1/7,  alpha = 2 + delta,  eps = delta^2/4,
    #   sigma_1 = 1 - eps,  sigma_2 = (alpha - omega - 1) + eps/2.
    #
    # Anclaje S5: sigma_2 > b(alpha) estricto (Lema 1: alpha > T_{8/7} = 2), asi
    # que {alpha, 1, sigma_2} es GENUINAMENTE infactible (rigidez, disco
    # alpha + 1); el Lema S6a(3) propaga la infactibilidad a sigma_1 = 1 - eps.
    # eps = O(delta^2) porque el umbral de la frontera crece como sqrt(eps).
    # Aqui: paredes con holgura, margen sobre b(alpha), infactibilidad angular
    # en sigma_1 = 1 - eps, y rho -> 13/7.
    w = 1 / 7
    vals = []
    for delta in (1e-1, 1e-2, 1e-3, 1e-4):
        alpha = 2 + delta
        eps = delta * delta / 4
        s1 = 1 - eps
        s2 = (alpha - w - 1) + eps / 2
        margen_b = s2 - b_pocket(alpha)                # ancla S5
        okc = (s2 >= 1 - w - 1e-15 and s2 >= alpha - w - 1 - 1e-15
               and s1 + s2 <= alpha - w + 1e-15 and s2 <= s1 and margen_b > 0)
        infeas = Fsum(alpha, s1, s2) >= TWO_PI
        rho = max(s1 + s2, (1 + s1 + s2) / alpha)
        vals.append((delta, rho, okc, infeas))
    for delta, rho, okc, infeas in vals:
        print(f"     delta={delta:.0e}  rho={rho:.9f}  rho-13/7={rho - CORNER:+.2e}"
              f"  paredes={'OK' if okc else 'FALLO'}"
              f"  infactible={'SI' if infeas else 'NO'}")
    ok &= check("E1 paredes (B2), (B4), (W), banda y margen S5 en toda la familia",
                all(okc for _, _, okc, _ in vals))
    ok &= check("E2 infactibilidad angular tambien en sigma_1 = 1 - eps",
                all(infeas for _, _, _, infeas in vals))
    ok &= check(f"E3 rho decrece a 13/7 (ultimo: {vals[-1][1] - CORNER:+.1e})",
                all(v1[1] > v2[1] for v1, v2 in zip(vals, vals[1:]))
                and 0 < vals[-1][1] - CORNER < 1e-3)
    # E4: el ancla exacta: en sigma_1 = 1 el umbral es b(alpha) (S5/A4 de h1.py)
    ok &= check(f"E4 h(2, 1) = b(2) = 6/7 (err {abs(h_boundary(2.0, 1.0) - 6 / 7):.1e})",
                abs(h_boundary(2.0, 1.0) - 6 / 7) < 1e-7)
    return ok


if __name__ == "__main__":
    print(f"w1 = {W1:.15f}  (2(1-w1) = {2 * (1 - W1):.10f})")
    print(f"esquina: 13/7 = {CORNER:.10f}  T = {TRIB:.10f}  13/7 - T = {CORNER - TRIB:.7f}\n")
    res = []
    print("[A] algebra exacta (sympy)")
    res.append(bloque_A())
    print("\n[B] rama mixta contra P y la tabla medida")
    res.append(bloque_B())
    print("\n[C] curva exacta contra fuerza bruta angular")
    res.append(bloque_C())
    print("\n[D] estructura fina: bump, dos minimos locales, esquina global")
    res.append(bloque_D())
    print("\n[E] familia genuina de la esquina")
    res.append(bloque_E())
    print(f"\nRESULTADO: {sum(res)}/{len(res)} bloques OK"
          + ("" if all(res) else "  <-- REVISAR"))
