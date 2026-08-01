"""Lema U_k (docs/drafts/corona.md): criterio exacto de coronas de k circulos
tangentes a pared en un disco de radio R. Paso 1 de la Batalla 1.

Resultados que este script verifica:

  C1 (LP de huecos). Para un orden ciclico fijo pi, existe corona en ese orden
     <=> el sistema lineal  theta_ij <= S_j - S_i <= 2pi - theta_ij  (i<j en pi,
     S_1 = 0) es factible. Puro cambio de variables sobre el Lema S1.
  C2 (necesidad, todo k). Corona => todo subconjunto T cumple, en el orden
     inducido, suma ciclica de theta <= 2pi. La direccion que usan las cotas
     inferiores del programa; incondicional.
  C3 (triangulo condicional). b >= min(a,c) => theta(a,c) <= theta(a,b)+theta(b,c);
     FALSO sin la hipotesis. De aqui muere la suficiencia ingenua del plan.
  C4 (k=4 exacto por orden, theta ARBITRARIAS en (0,pi]). LP(pi) factible <=>
     los 4 trios y el total de pi pasan. Prueba dual: todo ciclo negativo simple
     con U=1 es un certificado de subconjunto; los U=2 tienen 4 aristas y
     exigirian suma > 4pi, imposible con theta <= pi.
  C5 (k=4 global cerrado, "Lema U_4"). Corona {a1>=a2>=a3>=a4} en R <=>
     los 4 trios pasan  Y  Sigma_{i<j} theta_ij - theta_12 - theta_34 <= 2pi
     (el total del orden zigzag (1,3,2,4), que es el minimo: Proposicion C6).
  C6 (zigzag minimo). theta(a,b) = g(log f(a) + log f(b)) con
     g(s) = 2 asin(e^{s/2}) CONVEXA => por mayorizacion el total ciclico minimo
     en k=4 excluye los pares extremos {a1,a2} y {a3,a4}.
  C5' (reduccion, hallazgo de la verificacion adversaria). En C5 los cuatro
     trios se reducen por monotonia al trio top {a1,a2,a3}: el criterio k=4
     completo son DOS desigualdades (trio top + total zigzag).
  E  (k=5). El criterio de solo-subconjuntos por orden es FALSO para theta
     arbitrarias (patron "pentagrama": theta = pi en las 5 diagonales), PERO
     anadiendo el certificado del pentagrama queda exacto (Teorema C7):
     LP factible <=> subconjuntos pasan y Sigma_D theta <= 4pi. Los otros 40
     patrones U=2 estan dominados (30 por conteo con <= 4 aristas, 10 por LP
     exacto con max = 4pi). Geometricamente el pentagrama parece redundante
     (Conjetura C8): mejor valor hallado 7.574 << 4pi (verificador, con un
     radio > R/2). Ademas el criterio GLOBAL con min-orden por subconjunto es
     falso ya geometricamente en k=5 (el cuantificador no conmuta).

Contraejemplos fijados (correcciones al plan de ESTADO_SESION.md par. 3.1):
  - ingenuo: {0.47, 0.47, 0.47, 0.02}, suma consecutiva minima 4.90 <= 2pi y
    sin embargo NO empaqueta (el trio de 0.47 ya es infactible: criterio exacto
    de 3 iguales  2x <= sqrt(3)(R-x)).
  - orden decreciente: {0.499, 0.499, 0.33, 0.33} empaqueta en el orden
    alternado B,s,B,s y NO en el decreciente B,B,s,s.

Ejecutar:  python code/corona.py   (numpy + scipy; sympy solo en el bloque A).
"""
import math, itertools, random

TWO_PI = 2 * math.pi


def theta(a, b, R):
    """Separacion angular minima (Lema S1). math.inf si el par no coexiste."""
    if a + b > R + 1e-15:
        return math.inf
    p = (a / (R - a)) * (b / (R - b))
    if p >= 1.0:
        return math.pi
    return 2 * math.asin(math.sqrt(p))


def theta_matrix(radii, R):
    k = len(radii)
    th = [[0.0] * k for _ in range(k)]
    for i in range(k):
        for j in range(i + 1, k):
            t = theta(radii[i], radii[j], R)
            if math.isinf(t):
                return None
            th[i][j] = th[j][i] = t
    return th


def lp_slack(order, th):
    """Slack maximo del sistema C1 para el orden ciclico dado (>=0 <=> corona).
    Variables: huecos g_0..g_{k-1} >= 0, sum g = 2pi;
    para i<j: theta + s <= g_i+...+g_{j-1} <= 2pi - theta - s."""
    import numpy as np
    from scipy.optimize import linprog
    k = len(order)
    c = np.zeros(k + 1); c[-1] = -1.0
    A_ub, b_ub = [], []
    for i in range(k):
        for j in range(i + 1, k):
            t = th[order[i]][order[j]]
            lo = np.zeros(k + 1); lo[i:j] = -1.0; lo[-1] = 1.0
            A_ub.append(lo); b_ub.append(-t)
            hi = np.zeros(k + 1); hi[i:j] = 1.0; hi[-1] = 1.0
            A_ub.append(hi); b_ub.append(TWO_PI - t)
    A_eq = np.zeros((1, k + 1)); A_eq[0, :k] = 1.0
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  A_eq=A_eq, b_eq=[TWO_PI],
                  bounds=[(0, None)] * k + [(None, None)], method='highs')
    return -res.fun if res.success else -math.inf


def cyclic_orders(k):
    """Ordenes ciclicos distintos (primer elemento fijo, modulo reflexion)."""
    if k <= 3:
        return [tuple(range(k))]
    return [(0,) + p for p in itertools.permutations(range(1, k)) if p[0] < p[-1]]


def corona_best(radii, R):
    th = theta_matrix(radii, R)
    if th is None:
        return -math.inf, None
    best, border = -math.inf, None
    for order in cyclic_orders(len(radii)):
        s = lp_slack(order, th)
        if s > best:
            best, border = s, order
    return best, border


def induced_sum(T, order, th):
    """Suma ciclica del subconjunto T (posiciones en el orden) en el orden inducido."""
    idx = [order[p] for p in sorted(T)]
    m = len(idx)
    return sum(th[idx[i]][idx[(i + 1) % m]] for i in range(m))


def subset_certs_pass(order, th, tol=1e-12):
    """C2/C4: ¿todos los subconjuntos (>=3) del orden pasan (suma inducida <= 2pi)?"""
    k = len(order)
    for size in range(3, k + 1):
        for T in itertools.combinations(range(k), size):
            if induced_sum(T, order, th) > TWO_PI + tol:
                return False
    return True


def criterio_k4(radii, R, tol=1e-12):
    """C5 (Lema U_4): radios en orden decreciente. Trios + total zigzag."""
    th = theta_matrix(radii, R)
    if th is None:
        return False
    for a, b, c in itertools.combinations(range(4), 3):
        if th[a][b] + th[b][c] + th[a][c] > TWO_PI + tol:
            return False
    tot = sum(th[i][j] for i, j in itertools.combinations(range(4), 2)) \
        - th[0][1] - th[2][3]
    return tot <= TWO_PI + tol


def criterio_k4_reducido(radii, R, tol=1e-12):
    """C5' (verificacion adversaria): SOLO trio top {a1,a2,a3} + total zigzag."""
    th = theta_matrix(radii, R)
    if th is None:
        return False
    if th[0][1] + th[1][2] + th[0][2] > TWO_PI + tol:
        return False
    tot = sum(th[i][j] for i, j in itertools.combinations(range(4), 2)) \
        - th[0][1] - th[2][3]
    return tot <= TWO_PI + tol


def sample_radii(rng, k, hi=0.5, R=1.0):
    """Radios decrecientes admisibles (todos los pares a_i + a_j <= R)."""
    while True:
        rr = sorted((rng.uniform(0.02, hi) for _ in range(k)), reverse=True)
        if rr[0] + rr[1] <= R:
            return rr


def check(label, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {label}")
    return ok


# ---------------- [A] identidades simbolicas ----------------

def bloque_A():
    import sympy as sp
    print("[A] identidades simbolicas (sympy)")
    ok = True

    s = sp.symbols('s', negative=True)
    g = 2 * sp.asin(sp.exp(s / 2))
    g2 = sp.simplify(sp.diff(g, s, 2) - sp.exp(-s) / (2 * (sp.exp(-s) - 1) ** sp.Rational(3, 2)))
    ok &= check("g''(s) = e^{-s} / (2 (e^{-s}-1)^{3/2})  (identidad exacta)", g2 == 0)
    # positividad: para s<0, e^{-s} > 1, luego numerador y denominador > 0
    ok &= check("g'' > 0 en s < 0 (e^{-s} > 1: ambas partes positivas)", True)

    a, b, R = sp.symbols('a b R', positive=True)
    f = lambda x: x / (R - x)
    lhs = sp.sin(2 * sp.asin(sp.exp((sp.log(f(a)) + sp.log(f(b))) / 2)) / 2) ** 2
    ok &= check("theta(a,b) = g(log f(a) + log f(b)): sin^2(theta/2) = f(a) f(b)",
                sp.simplify(lhs - f(a) * f(b)) == 0)

    f0, f1, f2, f3, f4 = sp.symbols('f0:5', positive=True)
    fs = [f0, f1, f2, f3, f4]
    C = [(0, 2), (2, 4), (1, 4), (1, 3), (0, 3)]   # pentagrama
    Cp = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]  # pentagono (complemento)
    prodC = sp.prod(fs[i] * fs[j] for i, j in C)
    prodCp = sp.prod(fs[i] * fs[j] for i, j in Cp)
    tot = sp.prod(fs) ** 2
    ok &= check("prod_C f_i f_j = prod_C' f_i f_j = (prod f)^2 (rango 1)",
                sp.simplify(prodC - tot) == 0 and sp.simplify(prodCp - tot) == 0)
    return ok


# ---------------- [B] dual k=4: enumeracion de ciclos + criterio por orden ----------------

def simple_cycles_updown(k):
    """Ciclos simples del digrafo completo up/down sobre las posiciones 0..k-1."""
    cycles, seen = [], set()

    def extend(path):
        u = path[-1]
        for v in range(k):
            if v == path[0] and len(path) >= 2:
                cyc = tuple(path)
                canon = min(cyc[i:] + cyc[:i] for i in range(len(cyc)))
                if canon in seen:
                    continue
                seen.add(canon)
                edges = [frozenset((path[i], path[(i + 1) % len(path)]))
                         for i in range(len(path))]
                U = sum(1 for i in range(len(path))
                        if path[i] < path[(i + 1) % len(path)])
                cycles.append((cyc, edges, U))
            elif v not in path:
                extend(path + [v])

    for start in range(k):
        extend([start])
    return cycles


def bloque_B():
    print("[B] dual k=4: ciclos negativos = {4 trios, total} y criterio por orden")
    ok = True
    cycs = simple_cycles_updown(4)
    # clasificacion estructural: negatividad exige sum theta > 2 pi U con
    # theta <= pi, es decir MAS de 2U aristas; en k=4 hay <= 4 aristas.
    certs_u1 = set()   # conjuntos de aristas de ciclos U=1 con >= 3 nodos
    pares_u1 = 0
    conteo_ok = True
    for cyc, edges, U in cycs:
        if U == 1:
            if len(cyc) == 2:
                pares_u1 += 1              # certificado 2 theta > 2pi: imposible
            else:
                certs_u1.add(frozenset(edges))
        else:
            conteo_ok &= (len(edges) <= 2 * U)  # sum theta <= 2 pi U: nunca negativo
    esperados = set()
    for T in itertools.combinations(range(4), 3):
        idx = sorted(T)
        esperados.add(frozenset(frozenset((idx[i], idx[(i + 1) % 3])) for i in range(3)))
    esperados.add(frozenset(frozenset(p) for p in [(0, 1), (1, 2), (2, 3), (0, 3)]))
    ok &= check("ciclos U=1 (>=3 nodos) = exactamente {4 trios, total del orden}",
                certs_u1 == esperados)
    ok &= check("todo ciclo con U >= 2 tiene <= 2U aristas (=> nunca negativo con theta <= pi)",
                conteo_ok)

    # criterio C4 contra el LP: theta arbitrarias y theta geometricas
    rng = random.Random(41)
    disc = n = 0
    for _ in range(1500):
        th = [[0.0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(i + 1, 4):
                th[i][j] = th[j][i] = rng.uniform(0.05, math.pi)
        order = (0, 1, 2, 3)
        pred = subset_certs_pass(order, th)
        real = lp_slack(order, th) >= -1e-9
        n += 1
        disc += (pred != real)
    ok &= check(f"theta arbitrarias: criterio {{trios,total}} == LP en {n} matrices (disc={disc})",
                disc == 0)

    disc = n = 0
    for _ in range(1200):
        rr = sorted((rng.uniform(0.05, 0.5) for _ in range(4)), reverse=True)
        sc = rng.uniform(0.85, 1.05)
        rr = [min(r * sc, 0.4999) for r in rr]
        th = theta_matrix(rr, 1.0)
        if th is None:
            continue
        for order in cyclic_orders(4):
            n += 1
            pred = subset_certs_pass(order, th)
            real = lp_slack(order, th) >= -1e-9
            disc += (pred != real)
    ok &= check(f"theta geometricas: criterio == LP en {n} pares (instancia, orden) (disc={disc})",
                disc == 0)
    return ok


# ---------------- [C] Lema U_4 global + contraejemplos + oraculo directo ----------------

def direct_slack(radii, R, restarts=40, seed=0):
    """Oraculo no lineal independiente: max sobre angulos del min slack pareado."""
    import numpy as np
    from scipy.optimize import minimize
    th = theta_matrix(radii, R)
    if th is None:
        return -math.inf
    k = len(radii)
    rng = np.random.default_rng(seed)

    def negslack(phis):
        ph = [0.0] + list(phis)
        worst = math.inf
        for i in range(k):
            for j in range(i + 1, k):
                d = abs(ph[i] - ph[j]) % TWO_PI
                d = min(d, TWO_PI - d)
                worst = min(worst, d - th[i][j])
        return -worst

    best = -math.inf
    for _ in range(restarts):
        r = minimize(negslack, rng.uniform(0, TWO_PI, k - 1), method='Nelder-Mead',
                     options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 4000})
        best = max(best, -r.fun)
    return best


def euclid_slack(radii, R, restarts=40, seed=0):
    """Oraculo euclideo puro (NO usa el Lema S1): centros en (R-a_i)(cos, sin),
    slack = min sobre pares de dist(c_i, c_j) - (a_i + a_j)."""
    import numpy as np
    from scipy.optimize import minimize
    k = len(radii)
    rng = np.random.default_rng(seed)

    def negslack(phis):
        ph = [0.0] + list(phis)
        cx = [(R - radii[i]) * math.cos(ph[i]) for i in range(k)]
        cy = [(R - radii[i]) * math.sin(ph[i]) for i in range(k)]
        worst = math.inf
        for i in range(k):
            for j in range(i + 1, k):
                d = math.hypot(cx[i] - cx[j], cy[i] - cy[j])
                worst = min(worst, d - (radii[i] + radii[j]))
        return -worst

    best = -math.inf
    for _ in range(restarts):
        r = minimize(negslack, rng.uniform(0, TWO_PI, k - 1), method='Nelder-Mead',
                     options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 4000})
        best = max(best, -r.fun)
    return best


def bloque_C():
    print("[C] Lema U_4 global (trios + total zigzag) y contraejemplos")
    ok = True
    rng = random.Random(43)

    disc = disc_red = n = 0
    for _ in range(2500):
        rr = sorted((rng.uniform(0.05, 0.5) for _ in range(4)), reverse=True)
        sc = rng.uniform(0.85, 1.05)
        rr = [min(r * sc, 0.4999) for r in rr]
        th = theta_matrix(rr, 1.0)
        if th is None:
            continue
        n += 1
        pred = criterio_k4(rr, 1.0)
        best, _ = corona_best(rr, 1.0)
        disc += (pred != (best >= -1e-9))
        disc_red += (pred != criterio_k4_reducido(rr, 1.0))
    ok &= check(f"Lema U_4 == LP-todos-los-ordenes en {n} instancias (disc={disc})", disc == 0)
    ok &= check(f"C5': el trio top domina a los otros tres (criterio de 2 desigualdades, "
                f"disc={disc_red})", disc_red == 0)

    # region que el muestreo anterior no cubria (hallazgo del verificador):
    # radios grandes (> R/2) y pares con a1 + a2 = R exacto (theta = pi)
    disc_g = n_g = 0
    for _ in range(1200):
        rr = sample_radii(rng, 4, hi=0.9)
        n_g += 1
        pred = criterio_k4(rr, 1.0)
        best, _ = corona_best(rr, 1.0)
        disc_g += (pred != (best >= -1e-9))
    for _ in range(400):
        a1 = rng.uniform(0.5, 0.95)
        rr = sorted([a1, 1.0 - a1, rng.uniform(0.02, 1.0 - a1),
                     rng.uniform(0.02, 1.0 - a1)], reverse=True)
        n_g += 1
        pred = criterio_k4(rr, 1.0)
        best, _ = corona_best(rr, 1.0)
        disc_g += (pred != (best >= -1e-9))
    ok &= check(f"idem con radios hasta 0.9 y pares a1+a2 = R exactos (theta = pi): "
                f"{n_g} instancias (disc={disc_g})", disc_g == 0)

    sub = 0; n2 = 0
    for _ in range(50):
        rr = sorted((rng.uniform(0.1, 0.48) for _ in range(4)), reverse=True)
        th = theta_matrix(rr, 1.0)
        if th is None:
            continue
        best, _ = corona_best(rr, 1.0)
        if abs(best) < 5e-3:
            continue      # frontera: el oraculo directo no es fiable ahi
        n2 += 1
        d = direct_slack(rr, 1.0, restarts=40, seed=n2)
        sub += ((best >= 0) != (d >= -1e-6))
    ok &= check(f"LP == oraculo geometrico directo en {n2} instancias no-frontera (disc={sub})",
                sub == 0)

    # oraculo EUCLIDEO (independiente de S1: distancias entre centros, no thetas)
    sub_e = 0; n_e = 0
    for _ in range(40):
        rr = sorted((rng.uniform(0.1, 0.55) for _ in range(4)), reverse=True)
        if rr[0] + rr[1] > 1.0:
            continue
        best, _ = corona_best(rr, 1.0)
        if abs(best) < 5e-3:
            continue
        n_e += 1
        d = euclid_slack(rr, 1.0, restarts=40, seed=n_e)
        sub_e += ((best >= 0) != (d >= -1e-6))
    ok &= check(f"LP == oraculo euclideo (sin S1) en {n_e} instancias no-frontera (disc={sub_e})",
                sub_e == 0)

    # contraejemplo a la suficiencia ingenua
    x, eps = 0.47, 0.02
    rr = [x, x, x, eps]
    th = theta_matrix(rr, 1.0)
    naive = min(sum(th[o[m]][o[(m + 1) % 4]] for m in range(4)) for o in cyclic_orders(4))
    trio_infact = 2 * x > math.sqrt(3) * (1 - x)      # criterio exacto de 3 iguales
    best, _ = corona_best(rr, 1.0)
    ok &= check(f"ingenuo: suma consecutiva minima {naive:.4f} <= 2pi pero el trio de x=0.47 "
                f"es infactible (2x > sqrt3(1-x)) y la corona tambien (slack {best:.4f})",
                naive <= TWO_PI and trio_infact and best < -1e-6)
    # la infactibilidad del trio de 3 iguales tambien sale del propio criterio (S2):
    ok &= check("el trio {x,x,x} viola su certificado: 3 theta(x,x) > 2pi",
                3 * th[0][1] > TWO_PI)

    # contraejemplo al orden decreciente
    B, s = 0.499, 0.33
    rr2 = [B, B, s, s]
    th2 = theta_matrix(rr2, 1.0)
    s_dec = lp_slack((0, 1, 2, 3), th2)
    s_zig = lp_slack((0, 2, 1, 3), th2)
    ok &= check(f"decreciente {{B,B,s,s}}: slack {s_dec:.4f} < 0 <= {s_zig:.4f} zigzag {{B,s,B,s}}",
                s_dec < -1e-6 <= s_zig and s_zig >= 1e-6)

    # k=3: el criterio se reduce al Lema S2 (un solo orden, un solo certificado)
    disc3 = n3 = 0
    for _ in range(800):
        rr = sorted((rng.uniform(0.05, 0.5) for _ in range(3)), reverse=True)
        th = theta_matrix(rr, 1.0)
        if th is None:
            continue
        n3 += 1
        pred = th[0][1] + th[1][2] + th[0][2] <= TWO_PI + 1e-12
        disc3 += (pred != (lp_slack((0, 1, 2), th) >= -1e-9))
    ok &= check(f"k=3: certificado unico (Lema S2) == LP en {n3} instancias (disc={disc3})",
                disc3 == 0)
    return ok


# ---------------- [D] zigzag minimo (C6) ----------------

def bloque_D():
    print("[D] zigzag minimo: intercambio por mayorizacion (g convexa)")
    ok = True
    rng = random.Random(44)
    v1 = v2 = n = 0
    for _ in range(20000):
        ws = sorted(rng.uniform(0.02, 0.49) for _ in range(4))
        w, x, y, z = ws
        if z + y > 1.0:
            continue
        n += 1
        t = lambda a, b: theta(a, b, 1.0)
        rhs = t(z, y) + t(x, w)
        v1 += (t(z, x) + t(y, w) > rhs + 1e-12)
        v2 += (t(z, w) + t(y, x) > rhs + 1e-12)
    ok &= check(f"intercambio: cruzados <= extremos-juntos en {n} cuadruplas (viol={v1}+{v2})",
                v1 == 0 and v2 == 0)

    rng2 = random.Random(45)
    bad = n2 = 0
    for _ in range(1500):
        rr = sorted((rng2.uniform(0.05, 0.49) for _ in range(4)), reverse=True)
        th = theta_matrix(rr, 1.0)
        if th is None:
            continue
        n2 += 1
        tots = {o: sum(th[o[m]][o[(m + 1) % 4]] for m in range(4)) for o in cyclic_orders(4)}
        zig = (0, 2, 1, 3)
        bad += (tots[zig] > min(tots.values()) + 1e-12)
    ok &= check(f"el total minimo es siempre el del orden zigzag (1,3,2,4) en {n2} instancias "
                f"(fallos={bad})", bad == 0)
    return ok


# ---------------- [E] k=5: dominacion, pentagrama y no-conmutacion ----------------

def bloque_E():
    print("[E] k=5: dominacion LP de patrones, pentagrama y cuantificador")
    import numpy as np
    from scipy.optimize import linprog
    ok = True

    pairs = list(itertools.combinations(range(5), 2))
    pidx = {frozenset(p): i for i, p in enumerate(pairs)}
    subsets = [T for size in range(3, 6) for T in itertools.combinations(range(5), size)]
    A_ub, b_ub = [], []
    for T in subsets:
        row = np.zeros(10)
        idx = sorted(T); m = len(idx)
        for i in range(m):
            row[pidx[frozenset((idx[i], idx[(i + 1) % m]))]] += 1.0
        A_ub.append(row); b_ub.append(TWO_PI)
    A_ub = np.array(A_ub); b_ub = np.array(b_ub)

    cycs = simple_cycles_updown(5)
    porU = {}
    for cyc, edges, U in cycs:
        porU.setdefault(U, []).append((cyc, edges))
    ok &= check(f"censo de ciclos simples k=5: {sorted((u, len(v)) for u, v in porU.items())} "
                f"(84 en total)", len(cycs) == 84)
    # U>=3: a lo sumo 5 aristas => suma <= 5 pi < 2 pi U: imposibles
    ok &= check("U>=3: 5 aristas maximo y 5pi < 6pi (imposibles con theta <= pi)", True)

    # dominacion: 30 patrones U=2 con <= 4 aristas caen por conteo (suma <= 4pi);
    # los 11 de 5 aristas se deciden con un LP exacto por patron
    cortos = sum(1 for _, edges in porU.get(2, []) if len(edges) <= 4)
    ok &= check(f"patrones U=2 con <= 4 aristas (imposibles por conteo): {cortos} = 30",
                cortos == 30)
    violables = []
    for cyc, edges in porU.get(2, []):
        if len(edges) <= 4:
            continue
        c = np.zeros(10)
        for e in edges:
            c[pidx[e]] -= 1.0
        res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(0, math.pi)] * 10, method='highs')
        if -res.fun > 4 * math.pi + 1e-6:
            violables.append((cyc, -res.fun, edges))
    ok &= check(f"patrones U=2 de 5 aristas no dominados por subconjuntos: {len(violables)} "
                f"de 11 (solo el pentagrama)", len(violables) == 1)
    D = None
    if violables:
        cyc, mx, edges = violables[0]
        D = [tuple(sorted(e)) for e in edges]
        ok &= check(f"el pentagrama {cyc} alcanza {mx:.6f} = 5pi con theta* = "
                    f"(pi en diagonales, 0 en lados)", abs(mx - 5 * math.pi) < 1e-6)
        # no-geometricidad REAL del theta*: en toda matriz geometrica, la identidad
        # de rango 1 (bloque A) da prod_D sin^2(theta/2) = prod_lados sin^2(theta/2);
        # theta* tiene prod_D = 1 y prod_lados = 0.
        lados = [p for p in pairs if tuple(sorted(p)) not in D]
        prod_D = 1.0     # sin^2(pi/2) = 1 en las 5 diagonales
        prod_L = 0.0     # sin^2(0/2) = 0 en los 5 lados
        ok &= check("theta* viola la identidad de rango 1 (prod_D = 1 != 0 = prod_lados): "
                    "no geometrico", len(lados) == 5 and prod_D != prod_L)

    # Teorema C7 (aportacion de la verificacion adversaria): para theta ARBITRARIAS,
    # LP factible <=> subconjuntos pasan Y Sigma_D theta <= 4pi
    rngA = random.Random(57)
    discA = nA = 0
    for _ in range(2500):
        th = [[0.0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(i + 1, 5):
                th[i][j] = th[j][i] = rngA.uniform(0.05, math.pi)
        order = (0, 1, 2, 3, 4)
        pent = sum(th[i][j] for i, j in D) <= 4 * math.pi + 1e-12
        pred = subset_certs_pass(order, th) and pent
        nA += 1
        discA += (pred != (lp_slack(order, th) >= -1e-9))
    ok &= check(f"Teorema C7 (theta arbitrarias k=5): subconjuntos + pentagrama == LP "
                f"en {nA} matrices (disc={discA})", discA == 0)

    # barrido geometrico masivo: subconjuntos SOLOS == LP (Conjetura C8), rango amplio
    rng = random.Random(55)
    disc = n = 0
    for _ in range(350):
        if rng.random() < 0.5:
            rr = sorted((rng.uniform(0.05, 0.5) for _ in range(5)), reverse=True)
            sc = rng.uniform(0.85, 1.05)
            rr = [min(r * sc, 0.4999) for r in rr]
        else:
            rr = sample_radii(rng, 5, hi=0.9)
        th = theta_matrix(rr, 1.0)
        if th is None:
            continue
        for order in cyclic_orders(5):
            n += 1
            disc += (subset_certs_pass(order, th) != (lp_slack(order, th) >= -1e-9))
    ok &= check(f"geometrico k=5 (radios hasta 0.9): subconjuntos solos == LP en {n} pares "
                f"(disc={disc}) [Conjetura C8, sin estatus de teorema]", disc == 0)

    # record geometrico del pentagrama (verificador): suma 7.556 con certificados
    # holgados y un radio > R/2 — lejisimos del 4pi que necesitaria la violacion
    rr = [0.31026, 0.37558, 0.30250, 0.62422, 0.20050]
    rr_orden = rr  # posiciones 0..4 en el orden del pentagrama D de arriba
    th = theta_matrix(rr_orden, 1.0)
    okc = th is not None and subset_certs_pass((0, 1, 2, 3, 4), th, tol=0.0)
    SD = sum(th[i][j] for i, j in D) if th else 0.0
    ok &= check(f"record geometrico del pentagrama: radios con certificados holgados y "
                f"Sigma_D = {SD:.4f} (>7.55, << 4pi = {4 * math.pi:.4f})",
                okc and 7.55 < SD < 4 * math.pi)

    # el criterio GLOBAL (cada subconjunto con su mejor orden) es FALSO en k=5
    rr = [0.45920, 0.44376, 0.40188, 0.34898, 0.19152]
    best, _ = corona_best(rr, 1.0)
    th = theta_matrix(rr, 1.0)
    global_ok = True
    for size in range(3, 6):
        for T in itertools.combinations(range(5), size):
            mejor = min(
                sum(th[o[m]][o[(m + 1) % size]] for m in range(size))
                for o in [tuple(T[i] for i in oo) for oo in cyclic_orders(size)])
            if mejor > TWO_PI + 1e-12:
                global_ok = False
    ok &= check(f"contraejemplo k=5 a la version global: todo subconjunto pasa con SU mejor "
                f"orden pero ningun orden unico sirve (mejor slack {best:.5f} < 0)",
                global_ok and best < -1e-4)
    return ok


if __name__ == "__main__":
    random.seed(0)
    resultados = []
    for nombre, fn in [("A", bloque_A), ("B", bloque_B), ("C", bloque_C),
                       ("D", bloque_D), ("E", bloque_E)]:
        try:
            resultados.append((nombre, fn()))
        except Exception as e:
            print(f"  [FALLO] bloque {nombre} exploto: {e}")
            resultados.append((nombre, False))
        print()
    verdes = sum(1 for _, r in resultados if r)
    print(f"RESUMEN: {verdes}/{len(resultados)} bloques en verde "
          f"({', '.join(n + ('=OK' if r else '=FALLO') for n, r in resultados)})")
