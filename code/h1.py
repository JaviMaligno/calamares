"""H1 (docs/drafts/h1.md): pendiente de la frontera de bloqueo del trio.

Trio {alpha, s1, s2} tangente a la pared del disco R = alpha + 1; criterio angular
F(s1, s2) = theta(alpha,s1) + theta(alpha,s2) + theta(s1,s2) <= 2pi. La frontera
F = 2pi define s2 = h(alpha, s1) y H1 afirma kappa := -dh/ds1 >= 1.

Resultados demostrados en h1.md, verificados aqui:

  (i)  Forma cerrada de la frontera: con t(s) = sqrt((1-s)/s),

           F = 2pi  <=>  t(s1) + t(s2) = 1/sqrt(alpha(alpha+1)) = t(b(alpha)),

       con b(alpha) = alpha(alpha+1)/(alpha^2+alpha+1) el bolsillo de Descartes.
       Dominio: s1 in [s*, 1], s* = 4 alpha(alpha+1)/(2 alpha+1)^2 (diagonal).
  (ii) kappa = sqrt( g(s2) / g(s1) ),  g(s) = s^3 (1 - s): identidad cerrada
       INDEPENDIENTE de alpha (t es primitiva de -1/(2 sqrt(g))).
  (iii) kappa >= 1 en toda la frontera para TODO alpha > 1, igualdad solo en
       s1 = s2. Via G(t) := g(1/(1+t^2)) = t^2/(1+t^2)^4, con pico en
       t = 1/sqrt(3) (s = 3/4): si t(b) <= 1/sqrt(3) (alpha >= alpha0 =
       (sqrt(13)-1)/2) ambos t caen en el tramo creciente; si no, t1 <
       1/sqrt(2) - 1/sqrt(3) y kappa^2 >= G(1/sqrt2)/G(1/sqrt2 - 1/sqrt3) > 6.
  (iv) Corolario: min de s1 + s2 sobre los trios infactibles es 1 + b(alpha),
       alcanzado en (1, b(alpha)); y 1 + b(alpha) >= alpha sii alpha <= T
       (Tribonacci), luego para alpha <= T ningun trio infactible es compatible
       con la colocacion del testigo (W) s1 + s2 <= alpha - omega (estricto con
       omega > 0): el cierre del programa es Tribonacci, no aureo.

Bloques: [A] identidades simbolicas (sympy), [B] identidad de kappa contra
diferencias finitas en malla densa, [C] kappa >= 1 y frontera cerrada sobre
todo alpha, [D] monotonia de s1 + h y limite 1 + b(alpha), [E] cierre
Tribonacci y casos frontera.
"""
import math

TRIB = 1.839286755214161
PHI = (1 + math.sqrt(5)) / 2
ALPHA0 = (math.sqrt(13) - 1) / 2

TWO_PI = 2 * math.pi


def b_pocket(a):
    return a * (a + 1) / (a * a + a + 1)


def theta(a, b, R):
    p = (a / (R - a)) * (b / (R - b))
    if p >= 1.0:
        return math.pi if p <= 1.0 + 1e-12 else math.inf
    return 2 * math.asin(math.sqrt(p))


def Fsum(alpha, s1, s2):
    R = alpha + 1.0
    return theta(alpha, s1, R) + theta(alpha, s2, R) + theta(s1, s2, R)


def h_boundary(alpha, s1, iters=200):
    """s2 = h(alpha, s1): F = 2pi, biseccion (F creciente en s2). None si la
    frontera no corta la banda 0 < s2 <= s1."""
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


def kappa_closed(s1, s2):
    g = lambda s: s ** 3 * (1.0 - s)
    return math.sqrt(g(s2) / g(s1))


def kappa_fd(alpha, s1, s2, eps=1e-7):
    d1 = (Fsum(alpha, s1 + eps, s2) - Fsum(alpha, s1 - eps, s2)) / (2 * eps)
    d2 = (Fsum(alpha, s1, s2 + eps) - Fsum(alpha, s1, s2 - eps)) / (2 * eps)
    return d1 / d2


def check(label, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {label}")
    return ok


def bloque_A():
    """Identidades simbolicas de la prueba (sympy)."""
    import sympy as sp
    a, b, x, y, s, al = sp.symbols('a b x y s alpha', positive=True)
    R = sp.Symbol('R', positive=True)
    ok = True
    # A1: (dtheta/db)^2 = (lam(b) tan(theta/2))^2, ambos miembros >= 0 en el dominio
    f = lambda t, Rr: t / (Rr - t)
    P = f(a, R) * f(b, R)
    th = 2 * sp.asin(sp.sqrt(P))
    lam = R / (b * (R - b))
    ok &= check("A1 dtheta/db = lam(b)*tan(theta/2)  (identidad al cuadrado)",
                sp.simplify(sp.together(sp.diff(th, b) ** 2 - lam ** 2 * P / (1 - P))) == 0)
    # A2: R = alpha+1  =>  f(alpha) = alpha  y  1 - alpha f(s) = R(1-s)/(R-s)
    Rv = al + 1
    ok &= check("A2a f(alpha) = alpha", sp.simplify(al / (Rv - al) - al) == 0)
    ok &= check("A2b 1 - alpha*f(s) = R(1-s)/(R-s)",
                sp.simplify(1 - al * s / (Rv - s) - Rv * (1 - s) / (Rv - s)) == 0)
    # A3: kappa^2 = (lam(x)/lam(y))^2 (sinB cosB / sinA cosA)^2 = g(y)/g(x)
    fx, fy = x / (Rv - x), y / (Rv - y)
    sA2, sB2 = al * fx, al * fy
    lamx, lamy = Rv / (x * (Rv - x)), Rv / (y * (Rv - y))
    k2 = (lamx / lamy) ** 2 * (sB2 * (1 - sB2)) / (sA2 * (1 - sA2))
    ok &= check("A3 kappa^2 = y^3(1-y)/(x^3(1-x))",
                sp.simplify(k2 - y ** 3 * (1 - y) / (x ** 3 * (1 - x))) == 0)
    # A4: h(alpha, 1) = b(alpha): f(s) = alpha/(1+alpha^2) <=> s = b(alpha)
    s_sol = sp.solve(sp.Eq(s / (Rv - s), al / (1 + al ** 2)), s)[0]
    bp = al * (al + 1) / (al ** 2 + al + 1)
    ok &= check("A4 h(alpha,1) = b(alpha)", sp.simplify(s_sol - bp) == 0)
    # A5: b(alpha) - 3/4 = (alpha^2+alpha-3)/(4(alpha^2+alpha+1)); raiz alpha0
    num = sp.factor(sp.numer(sp.together(bp - sp.Rational(3, 4))))
    ok &= check("A5a b - 3/4 tiene numerador alpha^2+alpha-3",
                num == sp.factor(al ** 2 + al - 3))
    a0 = (sp.sqrt(13) - 1) / 2
    ok &= check("A5b alpha0 = (sqrt(13)-1)/2 raiz, y 1/alpha0 = (1+sqrt(13))/6",
                sp.simplify(a0 ** 2 + a0 - 3) == 0
                and sp.simplify(1 / a0 - (1 + sp.sqrt(13)) / 6) == 0)
    # A6: 2b - alpha = -alpha(alpha^2-alpha-1)/(alpha^2+alpha+1)  (>= 0 sii alpha <= phi)
    ok &= check("A6 2b - alpha = -alpha(alpha^2-alpha-1)/(alpha^2+alpha+1)",
                sp.simplify(2 * bp - al + al * (al ** 2 - al - 1) / (al ** 2 + al + 1)) == 0)
    # A7: g'(s) = s^2 (3 - 4s) < 0 en s > 3/4
    ok &= check("A7 g'(s) = s^2(3-4s)",
                sp.simplify(sp.diff(s ** 3 * (1 - s), s) - s ** 2 * (3 - 4 * s)) == 0)
    # A8: frontera cerrada. Terminos cruzados de sin(A+B) = sinA cosB + cosA sinB:
    #     (sinA cosB)^2 = alpha R (1-y)/y * f(x)f(y)  (y el simetrico), de donde
    #     sin(A+B) = sqrt(alpha R) (t(x)+t(y)) sqrt(f(x)f(y)); como sin(th12/2) =
    #     sqrt(f(x)f(y)) != 0, F = 2pi (th12/2 = pi-A-B) da t(x)+t(y) = 1/sqrt(aR).
    cosA2 = Rv * (1 - x) / (Rv - x)
    cosB2 = Rv * (1 - y) / (Rv - y)
    ok &= check("A8 frontera cerrada: terminos cruzados de sin(A+B)",
                sp.simplify(al * fx * cosB2 - al * Rv * (1 - y) / y * fx * fy) == 0
                and sp.simplify(al * fy * cosA2 - al * Rv * (1 - x) / x * fx * fy) == 0)
    # A9: t(s) = sqrt((1-s)/s) es primitiva de -1/(2 sqrt(g))
    ok &= check("A9 t'(s) = -1/(2 sqrt(g(s)))",
                sp.simplify(sp.diff(sp.sqrt((1 - s) / s), s)
                            + 1 / (2 * sp.sqrt(s ** 3 * (1 - s)))) == 0)
    # A10: la constante de la frontera es t(b(alpha)): t(b)^2 = 1/(alpha(alpha+1))
    ok &= check("A10 t(b(alpha))^2 = 1/(alpha(alpha+1))",
                sp.simplify((1 - bp) / bp - 1 / (al * (al + 1))) == 0)
    # A11: extremo diagonal t(s*) = t(b)/2: s* = 4 alpha(alpha+1)/(2 alpha+1)^2
    sstar = 4 * al * (al + 1) / (2 * al + 1) ** 2
    ok &= check("A11 s* = 4a(a+1)/(2a+1)^2 (diagonal de la frontera)",
                sp.simplify((1 - sstar) / sstar - 1 / (4 * al * (al + 1))) == 0)
    # A12: G(t) := g(1/(1+t^2)) = t^2/(1+t^2)^4, G'(t) = 2t(1-3t^2)/(1+t^2)^5
    tt = sp.Symbol('t', positive=True)
    G = tt ** 2 / (1 + tt ** 2) ** 4
    ok &= check("A12 G = g(1/(1+t^2)) y G'(t) = 2t(1-3t^2)/(1+t^2)^5",
                sp.simplify(G - (s ** 3 * (1 - s)).subs(s, 1 / (1 + tt ** 2))) == 0
                and sp.simplify(sp.diff(G, tt)
                                - 2 * tt * (1 - 3 * tt ** 2) / (1 + tt ** 2) ** 5) == 0)
    # A13: constantes del caso t(b) > 1/sqrt(3): 6 G(1/sqrt2 - 1/sqrt3) < G(1/sqrt2)
    c1, c2 = 1 / sp.sqrt(2) - 1 / sp.sqrt(3), 1 / sp.sqrt(2)
    ok &= check("A13 6 G(1/sqrt2 - 1/sqrt3) < G(1/sqrt2)  (caso 2: kappa^2 > 6)",
                bool(sp.N(G.subs(tt, c2) - 6 * G.subs(tt, c1), 30) > 0))
    # A14: 1 + b - alpha = -(a^3 - a^2 - a - 1)/(a^2 + a + 1): cierre Tribonacci
    ok &= check("A14 1 + b - alpha = -(a^3-a^2-a-1)/(a^2+a+1)",
                sp.simplify(bp - (al - 1)
                            + (al ** 3 - al ** 2 - al - 1) / (al ** 2 + al + 1)) == 0)
    return ok


def s_diag(alpha):
    """Extremo diagonal de la frontera: F(s*, s*) = 2pi (t(s*) = t(b)/2)."""
    return 4 * alpha * (alpha + 1) / (2 * alpha + 1) ** 2


def malla_frontera(alphas, n_s1=120):
    """Genera puntos (alpha, s1, s2) de la frontera con s2 <= s1 <= 1."""
    pts = []
    for alpha in alphas:
        for i in range(n_s1):
            s1 = 0.55 + (0.999999 - 0.55) * i / (n_s1 - 1)
            s2 = h_boundary(alpha, s1)
            if s2 is not None:
                pts.append((alpha, s1, s2))
    return pts


def malla_frontera_full(alpha, n_s1=200, top=1 - 1e-8):
    """Frontera muestreada en TODO su dominio s1 in [s*, top] (cubre tambien
    alpha grande, donde la frontera vive pegada a s = 1)."""
    lo = s_diag(alpha)
    pts = []
    if lo >= top:
        return pts
    for i in range(n_s1):
        s1 = lo + (top - lo) * i / (n_s1 - 1)
        s2 = h_boundary(alpha, s1)
        if s2 is not None:
            pts.append((alpha, s1, s2))
    return pts


def bloque_B():
    """Identidad de kappa contra diferencias finitas, malla densa."""
    alphas = [1.05 + 0.05 * k for k in range(40)]          # 1.05 .. 3.00
    pts = malla_frontera(alphas)
    err = max(abs(kappa_fd(a, x, y) - kappa_closed(x, y)) /
              max(1.0, kappa_closed(x, y)) for a, x, y in pts if x < 0.9999)
    print(f"  puntos de frontera: {len(pts)}; error relativo maximo: {err:.2e}")
    return check("B  kappa_fd = sqrt(g(s2)/g(s1)) (err rel < 1e-5)", err < 1e-5)


def bloque_C():
    """kappa >= 1 sobre toda la frontera, para TODO alpha > 1 (Teorema H1),
    forma cerrada de la frontera y las dos ramas de la prueba."""
    ok = True
    t = lambda s: math.sqrt((1 - s) / s)
    alphas = [1.001 + 0.01 * k for k in range(270)] + [5.0, 10.0, 50.0, 100.0, 1000.0]
    pts = []
    for a in alphas:
        pts += malla_frontera_full(a)
    kmin = min(kappa_closed(x, y) for _, x, y in pts)
    front = max(abs(math.sqrt(a * (a + 1)) * (t(x) + t(y)) - 1.0) for a, x, y in pts)
    bmin = min(y - b_pocket(a) for a, _, y in pts)
    print(f"  alpha en (1, 3.7] U {{5, 10, 50, 100, 1000}}: {len(pts)} puntos de frontera")
    ok &= check(f"C1 kappa >= 1 en toda la frontera, TODO alpha (kappa_min = {kmin:.12f})",
                kmin >= 1.0 - 1e-8)
    ok &= check(f"C2 frontera cerrada t1 + t2 = t(b(alpha)) (desvio max {front:.2e})",
                front < 1e-6)
    ok &= check(f"C3 s2 >= b(alpha) en la frontera (min s2 - b = {bmin:+.2e})",
                bmin > -1e-9)
    # Caso 2 de la prueba (t(b) > 1/sqrt3, o sea alpha < alpha0 y s2 < 3/4):
    # ahi la desigualdad no es ajustada sino kappa^2 >= 6.
    caso2 = [(a, x, y) for a, x, y in pts if y < 0.75]
    k2min = min(kappa_closed(x, y) ** 2 for _, x, y in caso2) if caso2 else math.nan
    ok &= check(f"C4 caso s2 < 3/4: kappa^2 >= 6  ({len(caso2)} pts, min = {k2min:.3f})",
                bool(caso2) and k2min >= 6.0)
    return ok


def bloque_D():
    """s1 + h(alpha, s1) estrictamente decreciente; inf = 1 + b(alpha) en s1 -> 1.

    El limite se comprueba en s1 = 1 EXACTO (ahi theta(alpha, 1) = pi y h esta
    bien definida; A4 da h(alpha, 1) = b(alpha) simbolicamente). No sirve
    extrapolar desde s1 = 1 - d con tolerancia fija: kappa ~ 1/sqrt(1-s1)
    diverge (E3b), asi que h(1-d) - b = Theta(sqrt(d)) — con d = 1e-7 el
    desvio es ~2e-4 (constante 0.54-0.64 por sqrt(d)) y es TASA DE
    CONVERGENCIA, no error de biseccion. Esa tasa se verifica en D2b."""
    ok = True
    worst_mono = -math.inf
    worst_at_1 = 0.0
    rate_spread = 0.0
    for alpha in (1.5, PHI, 1.75, TRIB, 2.0, 2.2, 2.5):
        prev = None
        n = 400
        for i in range(n):
            s1 = 0.55 + (0.9999999 - 0.55) * i / (n - 1)
            s2 = h_boundary(alpha, s1)
            if s2 is None:
                continue
            cur = s1 + s2
            if prev is not None:
                worst_mono = max(worst_mono, cur - prev)   # debe ser < 0
            prev = cur
        # D2a: valor en s1 = 1. Ojo: theta(alpha, 1) es el caso tangente p = 1,
        # donde 2 asin(sqrt(p)) tiene error float O(sqrt(eps)) ~ 1e-8; esa es
        # la precision alcanzable aqui (la identidad exacta es A4, simbolica).
        worst_at_1 = max(worst_at_1, abs(h_boundary(alpha, 1.0) - b_pocket(alpha)))
        # D2b: tasa h(1-d) - b(alpha) = Theta(sqrt(d)) — cociente estable en d
        rs = [(h_boundary(alpha, 1.0 - d) - b_pocket(alpha)) / math.sqrt(d)
              for d in (1e-4, 1e-6, 1e-8, 1e-10)]
        rate_spread = max(rate_spread, max(rs) / min(rs))
    ok &= check(f"D1 s1 + h estrictamente decreciente (max incremento {worst_mono:+.2e})",
                worst_mono < 0.0)
    ok &= check(f"D2a h(alpha, 1) = b(alpha) en s1 = 1 (err max {worst_at_1:.2e})",
                worst_at_1 < 1e-7)
    ok &= check(f"D2b lim s1->1: h(1-d) - b = Theta(sqrt(d)) "
                f"(cociente max/min = {rate_spread:.4f})", rate_spread < 1.2)
    return ok


def bloque_E():
    """Cierre Tribonacci del programa y casos frontera."""
    ok = True
    # E1: cierre Tribonacci. El minimo de s1 + s2 sobre los trios infactibles es
    # 1 + b(alpha) (Corolario 1, valido para todo alpha > 1), y por A14
    # 1 + b(alpha) > alpha para alpha < T: ningun trio infactible es compatible
    # con (W) s1 + s2 <= alpha - omega si alpha <= T (estricto con omega > 0).
    # Sustituye al antiguo cierre aureo (2b >= alpha, solo alpha <= phi): la
    # cota fina 1 + b llega hasta T, coherente con la Proposicion 3.
    worst = min(1 + b_pocket(a) - a
                for a in (1.0001 + (TRIB - 1e-4 - 1.0001) * k / 399 for k in range(400)))
    ok &= check(f"E1 cierre Tribonacci: min (1 + b - alpha) en (1, T) = {worst:+.2e} > 0",
                worst > 0)
    eps = 1e-6
    ok &= check("E2 1 + b - alpha cambia de signo exactamente en alpha = T",
                1 + b_pocket(TRIB - eps) > TRIB - eps
                and 1 + b_pocket(TRIB + eps) < TRIB + eps)
    # E3: casos frontera: kappa(s1=s2) = 1 exacto; kappa -> inf cuando s1 -> 1.
    ok &= check("E3a kappa = 1 exacto en s1 = s2 (formula cerrada)",
                kappa_closed(0.9, 0.9) == 1.0)
    k_near_1 = kappa_closed(1 - 1e-10, b_pocket(2.0))
    ok &= check(f"E3b kappa -> inf en s1 -> 1 (kappa(1-1e-10) = {k_near_1:.1e})",
                k_near_1 > 1e4)
    # E4: identidades ancla: b(T) = T - 1 (Tribonacci) y b(phi) = phi/2 (aurea).
    ok &= check(f"E4 b(T) = T - 1 = {b_pocket(TRIB):.6f}  y  b(phi) = phi/2 = {b_pocket(PHI):.6f}",
                abs(b_pocket(TRIB) - (TRIB - 1)) < 1e-12
                and abs(b_pocket(PHI) - PHI / 2) < 1e-12)
    return ok


if __name__ == "__main__":
    print(f"T = {TRIB:.6f}  phi = {PHI:.6f}  alpha0 = (sqrt(13)-1)/2 = {ALPHA0:.9f}\n")
    res = []
    print("[A] identidades simbolicas (sympy)")
    res.append(bloque_A())
    print("\n[B] identidad cerrada de kappa contra diferencias finitas")
    res.append(bloque_B())
    print("\n[C] kappa >= 1 sobre la frontera")
    res.append(bloque_C())
    print("\n[D] monotonia de s1 + h y limite 1 + b(alpha)")
    res.append(bloque_D())
    print("\n[E] cobertura del programa y casos frontera")
    res.append(bloque_E())
    print(f"\nRESULTADO: {sum(res)}/{len(res)} bloques OK"
          + ("" if all(res) else "  <-- REVISAR"))
