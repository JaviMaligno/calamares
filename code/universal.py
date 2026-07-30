"""Frontera universal (docs/drafts/universal.md): el toolkit del asalto a v generico.

Lema U: trio {A, x, y} tangente a la pared de un disco de radio R ARBITRARIO
(dominio interior: A+x, A+y, x+y < R). Con c := R - A y

    T_c(x) := sqrt((c - x)/x) ,      tau_R := c / sqrt(A R) ,

la infactibilidad angular es LINEAL:  F >= 2pi  <=>  T_c(x) + T_c(y) <= tau_R.

Casos particulares: A = 1, c = t reproduce psi/tau del Lema S3 (suelo_rigido);
A = alpha, c = 1 reproduce la frontera de h1.md. En x = c el bolsillo es

    b_R(A) = A R c / (A R + c^2)     (= AB(A+B)/(A^2+AB+B^2) si R = A + B),

la formula de Descartes de resultados.md par. 5bis, ahora para todo R. La
pendiente de la frontera es kappa = sqrt(g_c(y)/g_c(x)) con g_c(s) = s^3(c-s)
(la identidad de h1, uniforme en R), y el G_c-lema da el minimo de x + y sobre
la region infactible en la esquina x -> max.

Corolario (Teorema S con holgura): en la subfamilia rigida con R >= r1 + r2
(no solo =), bloqueado => rho > T. Monotonia: no empaquetable en R implica no
empaquetable en r1 + r2 <= R (un empaquetamiento en el disco menor lo es en el
mayor), y el Teorema S aplica tal cual con el disco 1 + t.

Bloques: [A] identidades simbolicas, [B] frontera lineal y kappa contra
biseccion angular en malla (A, R), [C] bolsillo general y casos particulares,
[D] Teorema S con holgura (monotonia numerica + familia con holgura), [E]
exploracion SIN ESTATUS: pan con tres ocupantes (proxy angular).
"""
import math

TWO_PI = 2 * math.pi
TRIB = 1.839286755214161


def theta(a, b, R):
    p = (a / (R - a)) * (b / (R - b))
    if p >= 1.0:
        return math.pi if p <= 1 + 1e-12 else math.inf
    return 2 * math.asin(math.sqrt(p))


def Fsum3(A, x, y, R):
    return theta(A, x, R) + theta(A, y, R) + theta(x, y, R)


def T_c(x, c):
    return math.sqrt((c - x) / x)


def tau_R(A, R):
    return (R - A) / math.sqrt(A * R)


def b_R(A, R):
    c = R - A
    return A * R * c / (A * R + c * c)


def frontera_y(A, x, R, iters=100):
    lo, hi = 1e-15, min(x, R - A)      # x = c permitido (theta(A, c) = pi)
    if hi <= lo or Fsum3(A, x, hi, R) < TWO_PI:
        return None
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if Fsum3(A, x, mid, R) > TWO_PI:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def check(label, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {label}")
    return ok


# ---------------- [A] identidades simbolicas ----------------

def bloque_A():
    import sympy as sp
    A, x, y, R, s, B = sp.symbols('A x y R s B', positive=True)
    c = R - A
    f = lambda z: z / (R - z)
    ok = True
    # A1: termino cruzado general (la unica pieza que h1 hacia con R = alpha+1):
    #     f(A) f(x) (1 - f(A) f(y)) = (A R/(R-A)^2) * ((c-y)/y) * f(x) f(y)
    lhs = f(A) * f(x) * (1 - f(A) * f(y))
    rhs = (A * R / (R - A) ** 2) * ((c - y) / y) * f(x) * f(y)
    ok &= check("A1 termino cruzado general en R arbitrario",
                sp.simplify(lhs - rhs) == 0)
    # A2: bolsillo: T_c(y) = tau_R  =>  y = A R c/(A R + c^2); Descartes en R = A+B
    bol = sp.solve(sp.Eq((c - y) / y, c ** 2 / (A * R)), y)[0]
    ok &= check("A2a b_R(A) = A R (R-A)/(A R + (R-A)^2)",
                sp.simplify(bol - A * R * c / (A * R + c ** 2)) == 0)
    ok &= check("A2b en R = A + B es AB(A+B)/(A^2+AB+B^2) (Descartes, par. 5bis)",
                sp.simplify(bol.subs(R, A + B)
                            - A * B * (A + B) / (A ** 2 + A * B + B ** 2)) == 0)
    # A3: T_c es primitiva de -1/(2 sqrt(g_c)), g_c(s) = s^3 (c - s) escalado:
    #     T_c'(s) = -c/(2 sqrt(s^3 (c-s)))
    ok &= check("A3 T_c'(s) = -c/(2 sqrt(s^3(c-s)))",
                sp.simplify(sp.diff(sp.sqrt((c - s) / s), s)
                            + c / (2 * sp.sqrt(s ** 3 * (c - s)))) == 0)
    # A4: kappa = T_c'(x)/T_c'(y) = sqrt(g_c(y)/g_c(x)): el factor c se cancela
    ok &= check("A4 kappa = sqrt(g_c(y)/g_c(x)) sobre la frontera lineal",
                sp.simplify((c / (2 * sp.sqrt(x ** 3 * (c - x))))
                            / (c / (2 * sp.sqrt(y ** 3 * (c - y))))
                            - sp.sqrt(y ** 3 * (c - y)) / sp.sqrt(x ** 3 * (c - x))) == 0)
    # A5: condicion de concavidad/G_c (el (1+sqrt13)/6 de S4, ahora general):
    #     tau_R <= 1/sqrt(3)  <=>  3 c^2 <= A R  <=>  3(R-A)^2 <= A R.
    #     En A = 1, R = 1 + t: 3t^2 <= 1 + t <=> t <= (1+sqrt13)/6.
    t = sp.symbols('t', positive=True)
    cond = (3 * (R - A) ** 2 - A * R).subs({A: 1, R: 1 + t})
    r13 = sp.solve(sp.Eq(cond, 0), t)
    ok &= check("A5 3c^2 = AR en A=1, R=1+t da t = (1+sqrt(13))/6 (la cte de S4)",
                any(sp.simplify(rr - (1 + sp.sqrt(13)) / 6) == 0 for rr in r13))
    # A6: escala: todo es invariante por homotecia (T_c(lx; lc) = T_c(x; c),
    #     tau homogeneo de grado 0): basta normalizar A = 1.
    lam = sp.symbols('lambda', positive=True)
    ok &= check("A6 invariancia de escala de T y tau",
                sp.simplify(sp.sqrt((lam * c - lam * x) / (lam * x))
                            - sp.sqrt((c - x) / x)) == 0
                and sp.simplify((lam * R - lam * A) / sp.sqrt(lam * A * lam * R)
                                - (R - A) / sp.sqrt(A * R)) == 0)
    return ok


# ---------------- [B] frontera y kappa en malla ----------------

def bloque_B():
    ok = True
    worst_f, worst_k, npts = 0.0, 0.0, 0
    for A in (0.6, 1.0, 1.4, 1.7, 2.2, 3.0):
        for factor in (0.45, 0.55, 0.7, 0.8, 0.9, 1.0):
            for slack in (0.0, 0.03, 0.1, 0.2, 0.5, 0.8):
                R = A + factor * A + slack
                c = R - A
                tau = tau_R(A, R)
                for i in range(1, 22):
                    x = c * (0.55 + 0.44 * i / 22)
                    if x >= min(c, R - A):
                        continue
                    y = frontera_y(A, x, R)
                    if y is None or x + y >= R - 1e-9:
                        continue                    # rama del par, no angular
                    npts += 1
                    worst_f = max(worst_f, abs(T_c(x, c) + T_c(y, c) - tau))
                    if i % 3 == 0 and x + 1e-7 < c:
                        eps = 1e-7
                        y1, y2 = frontera_y(A, x + eps, R), frontera_y(A, x - eps, R)
                        if y1 is None or y2 is None:
                            continue
                        k_fd = -(y1 - y2) / (2 * eps)
                        g = lambda ss: ss ** 3 * (c - ss)
                        k_cl = math.sqrt(g(y) / g(x))
                        worst_k = max(worst_k, abs(k_fd - k_cl) / k_cl)
    print(f"     {npts} puntos de frontera en malla (A, R)")
    ok &= check(f"B1 frontera lineal T(x)+T(y) = tau_R (desvio max {worst_f:.1e})",
                worst_f < 1e-9 and npts > 300)
    ok &= check(f"B2 kappa = sqrt(g_c(y)/g_c(x)) (err rel max {worst_k:.1e})",
                worst_k < 1e-5)
    return ok


# ---------------- [C] bolsillo general ----------------

def bloque_C():
    ok = True
    worst = 0.0
    for A in (0.7, 1.0, 2.0, 3.5):
        for R in (A + 0.3, A + 0.8 * A, A + A, A + A + 0.5):
            c = R - A
            if c <= 0:
                continue
            y = frontera_y(A, c, R)     # x = c EXACTO (evita la tasa sqrt(eps))
            if y is None:
                continue
            worst = max(worst, abs(y - b_R(A, R)))
    ok &= check(f"C1 bolsillo bisecado en x = c = b_R(A) (err max {worst:.1e})",
                worst < 1e-7)
    # crecimiento en R: mas holgura, mas bolsillo (para el x maximo fijo NO —
    # aqui el bolsillo junto a x = c crece con R via c; lo relevante para la
    # monotonia del asalto es b_R(A) creciente en R con A fijo)
    ok &= check("C2 b_R(A) creciente en R (A = 1: R = 1.5, 1.8, 2.2, 3)",
                b_R(1, 1.5) < b_R(1, 1.8) < b_R(1, 2.2) < b_R(1, 3.0))
    return ok


# ---------------- [D] Teorema S con holgura ----------------

def pack3_wall(A, x, y, R):
    """Certificado constructivo (S2 general): F <= 2pi => empaqueta."""
    if A + x > R or A + y > R or x + y > R:
        return False
    return Fsum3(A, x, y, R) <= TWO_PI


def bloque_D():
    ok = True
    # D1: monotonia en R del certificado: si empaqueta en R' <= R, empaqueta en R
    #     (contencion); numericamente: F decreciente en R.
    worst = -math.inf
    for A, x, y in ((1, 0.5, 0.45), (1, 0.54, 0.4), (2, 0.9, 0.85)):
        prev = None
        for k in range(30):
            R = (1 + x / 10) * (A + x) + 0.02 * k   # barrido de R crecientes
            if x + y > R:
                continue
            Fv = Fsum3(A, x, y, R)
            if prev is not None:
                worst = max(worst, Fv - prev)
            prev = Fv
    ok &= check(f"D1 F decreciente en R (max incremento {worst:+.1e})", worst < 0)
    # D2: familia con holgura: instancias de F_hol (R > 1 + t) bloqueadas segun
    #     el criterio angular en el disco R; comprobar que el trio tampoco
    #     empaqueta en 1 + t y que rho > T (la cadena del corolario).
    fallos, n = 0, 0
    for t in (0.40, 0.43, 0.46, 0.49, 0.52, 0.54):
        for slackf in (0.003, 0.01, 0.03, 0.06):
            R = (1 + t) * (1 + slackf)
            # frontera angular en el disco R para el trio {1, u, v}, u = t - d
            for d in (0.0, 0.005, 0.015):
                u = t - d
                v = frontera_y(1.0, u, R)
                if v is None:
                    continue
                v = min(v * 1.0001 + 1e-9, u)       # estrictamente infactible en R
                if Fsum3(1.0, u, v, R) < TWO_PI:
                    continue
                if u + v > 1.0:                      # (F2) imposible: no instancia
                    continue
                n += 1
                # cadena: infactible en R => infactible en 1 + t
                if Fsum3(1.0, u, v, 1 + t) < TWO_PI:
                    fallos += 1
                # y rho > T
                rho = max((u + v) / t, t + u + v)
                if rho <= TRIB:
                    fallos += 1
    print(f"     instancias con holgura ensayadas: {n}")
    ok &= check(f"D2 cadena del corolario (infactible en R => en 1+t => rho > T): "
                f"{fallos} fallos", fallos == 0 and n >= 5)
    return ok


# ---------------- [E] exploracion: pan con tres ocupantes ----------------

def bloque_E():
    """SIN ESTATUS (exploracion para el asalto): v = sarten de radio R con
    ocupantes {A1, A2, m}; m sale; S = {u, v} debe reinsertarse junto a
    {A1, A2}. Proxy: infactibilidad angular de {A1, A2, u, v} en R (suma de
    los 4 arcos consecutivos en el orden optimo >= 2pi — para 4 circulos la
    tangencia a pared es solo un proxy, se declara como tal). Pregunta: ¿algun
    bloqueo con rho < 13/7? La plantilla canonica (A2 ausente) da inf = 13/7."""
    import itertools
    def ang4(circles, R):
        best = math.inf
        for perm in itertools.permutations(circles[1:]):
            order = [circles[0]] + list(perm)
            s = sum(theta(order[i], order[(i + 1) % 4], R) for i in range(4))
            best = min(best, s)
        return best

    best_rho, best_cfg = math.inf, None
    n_block = 0
    import random
    rnd = random.Random(2026)
    for _ in range(60000):
        alpha = rnd.uniform(1.3, 2.6)               # A1 (m = 1)
        gamma = rnd.uniform(1.0, alpha)             # A2
        omega = rnd.uniform(0.02, 0.25)
        # R minimo para {alpha, gamma, 1}: certificado angular
        lo, hi = alpha + gamma, alpha + gamma + 2.5
        for _ in range(40):
            mid = 0.5 * (lo + hi)
            if Fsum3(alpha, gamma, 1.0, mid) <= TWO_PI:
                hi = mid
            else:
                lo = mid
        R = hi * (1 + rnd.uniform(0, 0.04))         # holgura pequena
        # S = {u, v}: testigo en el agujero de alpha; paredes tipo (B2)/(B4)/(W)
        u = rnd.uniform(max(0.7, 1 - omega), 1.0)
        v = rnd.uniform(max(0.7, 1 - omega), u)
        if u + v > alpha - omega:
            continue
        # bloqueo proxy: {alpha, gamma, u, v} angularmente infactible en R
        if ang4([alpha, gamma, u, v], R) < TWO_PI:
            continue
        n_block += 1
        Sig = u + v
        # colas completas de la instancia {alpha, gamma, 1, u, v} (m = 1)
        rho = max((gamma + 1 + Sig) / alpha, (1 + Sig) / gamma, Sig / 1.0)
        if rho < best_rho:
            best_rho, best_cfg = rho, (alpha, gamma, omega, R, u, v)
    print(f"     bloqueos-proxy encontrados: {n_block}")
    if best_cfg:
        a_, g_, w_, R_, u_, v_ = best_cfg
        print(f"     mejor rho = {best_rho:.6f}  (alpha={a_:.4f}, gamma={g_:.4f}, "
              f"omega={w_:.4f}, R={R_:.4f}, u={u_:.4f}, v={v_:.4f})")
        print(f"     referencia: 13/7 = {13/7:.6f}, T = {TRIB:.6f}")
    return check("E  exploracion registrada (sin estatus; ver universal.md par. 5)",
                 True)


if __name__ == "__main__":
    print(f"T = {TRIB:.6f}\n")
    res = []
    print("[A] identidades simbolicas (sympy)")
    res.append(bloque_A())
    print("\n[B] frontera lineal y kappa en malla (A, R)")
    res.append(bloque_B())
    print("\n[C] bolsillo general b_R(A)")
    res.append(bloque_C())
    print("\n[D] Teorema S con holgura")
    res.append(bloque_D())
    print("\n[E] exploracion: tres ocupantes (proxy angular)")
    res.append(bloque_E())
    print(f"\nRESULTADO: {sum(res)}/{len(res)} bloques OK"
          + ("" if all(res) else "  <-- REVISAR"))
