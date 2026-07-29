"""H1 (docs/drafts/h1.md): pendiente de la frontera de bloqueo del trio.

Trio {alpha, s1, s2} tangente a la pared del disco R = alpha + 1; criterio angular
F(s1, s2) = theta(alpha,s1) + theta(alpha,s2) + theta(s1,s2) <= 2pi. La frontera
F = 2pi define s2 = h(alpha, s1) y H1 afirma kappa := -dh/ds1 >= 1.

Resultado demostrado en h1.md, verificado aqui:

    kappa = sqrt( g(s2) / g(s1) ),   g(s) = s^3 (1 - s),

identidad cerrada valida en toda la frontera, INDEPENDIENTE de alpha. De ahi
kappa >= 1 sii g(s2) >= g(s1); como en la frontera s2 >= b(alpha) (bolsillo de
Descartes) y g es decreciente en [3/4, 1], basta b(alpha) >= 3/4, es decir
alpha >= alpha0 = (sqrt(13)-1)/2 = 1.3027756... Para alpha <= phi el bloqueo es
imposible por la cota aurea 2 b(alpha) >= alpha, asi que el programa (que solo
necesita alpha > phi) queda cubierto sin hipotesis.

Bloques: [A] identidades simbolicas (sympy), [B] identidad de kappa contra
diferencias finitas en malla densa, [C] kappa >= 1 sobre la frontera,
[D] monotonia de s1 + h y limite 1 + b(alpha), [E] cobertura de la region usada
por grosor_positivo.md / trio.py y casos frontera.
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
    return ok


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


def bloque_B():
    """Identidad de kappa contra diferencias finitas, malla densa."""
    alphas = [1.05 + 0.05 * k for k in range(40)]          # 1.05 .. 3.00
    pts = malla_frontera(alphas)
    err = max(abs(kappa_fd(a, x, y) - kappa_closed(x, y)) /
              max(1.0, kappa_closed(x, y)) for a, x, y in pts if x < 0.9999)
    print(f"  puntos de frontera: {len(pts)}; error relativo maximo: {err:.2e}")
    return check("B  kappa_fd = sqrt(g(s2)/g(s1)) (err rel < 1e-5)", err < 1e-5)


def bloque_C():
    """kappa >= 1 sobre toda la frontera. Teorema: alpha >= alpha0.
    Observacion (solo numerica): tambien parece valer en (1, alpha0)."""
    ok = True
    pts = malla_frontera([ALPHA0 + 1e-9 + 0.02 * k for k in range(120)], n_s1=200)
    kmin = min(kappa_closed(x, y) for _, x, y in pts)
    s2min = min(y for a, _, y in pts if abs(y - b_pocket(a)) > -1)  # min global s2
    bmin = min(y - b_pocket(a) for a, _, y in pts)
    print(f"  alpha en [alpha0, 3.7]: {len(pts)} puntos, kappa_min = {kmin:.6f}")
    ok &= check("C1 kappa >= 1 en toda la frontera (alpha >= alpha0)", kmin >= 1.0 - 1e-12)
    ok &= check(f"C2 s2 >= b(alpha) en la frontera (min s2 - b = {bmin:+.2e})",
                bmin > -1e-9)
    ok &= check(f"C3 s2 >= 3/4 en la frontera si alpha >= alpha0 (min s2 = {s2min:.4f})",
                s2min >= 0.75 - 1e-9)
    pts_low = malla_frontera([1.02 + 0.02 * k for k in range(15)], n_s1=200)
    kmin_low = min(kappa_closed(x, y) for _, x, y in pts_low)
    print(f"  observacion numerica alpha in (1, alpha0): kappa_min = {kmin_low:.6f} "
          f"({len(pts_low)} puntos; sin prueba analitica ahi, no se usa)")
    return ok


def bloque_D():
    """s1 + h(alpha, s1) estrictamente decreciente; inf = 1 + b(alpha) en s1 -> 1."""
    ok = True
    worst_mono, worst_lim = 0.0, 0.0
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
        lim = 1.0 + b_pocket(alpha)
        worst_lim = max(worst_lim, abs(prev - lim))
    ok &= check(f"D1 s1 + h estrictamente decreciente (max incremento {worst_mono:+.2e})",
                worst_mono < 0.0)
    ok &= check(f"D2 lim s1->1 de s1 + h = 1 + b(alpha) (err max {worst_lim:.2e})",
                worst_lim < 1e-6)
    return ok


def bloque_E():
    """Cobertura de la region del programa y cierre aureo para alpha <= phi."""
    ok = True
    # E1: la region usada (grosor_positivo: alpha >= 2 - omega, omega <= 0.30;
    # trio.py: alpha en [1.5, 2.5] con optimos en alpha >= T) cae en alpha >= alpha0.
    ok &= check(f"E1 region usada alpha >= 2 - 0.30 = 1.70 > alpha0 = {ALPHA0:.6f}",
                2 - 0.30 > ALPHA0 and 1.5 > ALPHA0)
    # E2: cierre aureo: para alpha <= phi todo trio infactible tiene s1+s2 > alpha,
    # luego viola (W) s1+s2 <= alpha - omega. En la frontera: s1 + h > 2 b >= alpha.
    worst = math.inf
    for k in range(60):
        alpha = 1.05 + (PHI - 1.05) * k / 59
        for i in range(120):
            s1 = 0.55 + (0.9999999 - 0.55) * i / 119
            s2 = h_boundary(alpha, s1)
            if s2 is not None:
                worst = min(worst, s1 + s2 - alpha)
    ok &= check(f"E2 alpha <= phi: min (s1 + h - alpha) = {worst:+.4f} > 0", worst > 0)
    # E3: casos frontera: kappa(s1=s2) = 1 exacto; kappa -> inf cuando s1 -> 1.
    ok &= check("E3a kappa = 1 exacto en s1 = s2 (formula cerrada)",
                kappa_closed(0.9, 0.9) == 1.0)
    k_near_1 = kappa_closed(1 - 1e-10, b_pocket(2.0))
    ok &= check(f"E3b kappa -> inf en s1 -> 1 (kappa(1-1e-10) = {k_near_1:.1e})",
                k_near_1 > 1e4)
    # E4: b creciente => min de s2 en la frontera del programa es b(phi) > 3/4.
    ok &= check(f"E4 b(phi) = {b_pocket(PHI):.6f} > 3/4  y  b(T) = {b_pocket(TRIB):.6f}",
                b_pocket(PHI) > 0.75 and abs(b_pocket(TRIB) - (TRIB - 1)) < 1e-12)
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
