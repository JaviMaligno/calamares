"""PISTA D: la constante hermana de Tribonacci en la sarten CUADRADA.

Sarten cuadrada de lado s (= 2L). Los hermanos de la sarten se empaquetan como
circulos disjuntos dentro del cuadrado; los agujeros de los aros siguen siendo
discos, asi que la factibilidad dentro de agujeros no cambia (se reutilizan
reinserta.feas y sim.pack_feasible tal cual).

Hechos exactos del cuadrado (demostraciones en docs/drafts/cuadrado.md):

  PAR   {a, b} caben en el cuadrado sii max(a, b) <= s/2 y a + b <= (2-sqrt2) s.
        La distancia maxima entre centros admisibles es sqrt2 (s - a - b)
        (esquinas opuestas de las cajas de centros) y debe ser >= a + b.

  FILA DIAGONAL (Lema 0 cuadrado, suficiente): con los dos mayores en los
        extremos, la fila tangente sobre la diagonal cabe cuando
        2 sum(r) + (sqrt2 - 1)(r_1 + r_2) <= sqrt2 s   (r_1 >= r_2 >= resto);
        en particular basta sum(r) <= (2 - sqrt2) s.

  BOLSILLO DE ESQUINA: dado un circulo de radio a tangente a los dos lados de
        una esquina, el mayor circulo tangente a los dos lados de una esquina
        ADYACENTE que no lo corta tiene radio  x = (sqrt(s) - sqrt(a))^2.
        (En la esquina OPUESTA seria x = (2 - sqrt2) s - a.)

  CONFIG RIGIDA: {alpha, 1} con alpha + 1 = (2 - sqrt2) s solo caben en la
        diagonal exacta, cada uno clavado en su esquina. El mayor circulo
        insertable tras ellos es el bolsillo de esquina, que manda el circulo
        GRANDE (x decrece en a):
            b_sq(alpha) = (sqrt((1+alpha)/(2-sqrt2)) - sqrt(max(alpha, 1)))^2.
        Que el bolsillo sea el maximo insertable es evidencia numerica
        (seccion 3 del main); que es insertable, exacto por la formula.

SUELO de la familia de 4 aros (calco del algebra idealizada de resultados.md
5quater con el bolsillo de esquina en el papel del bolsillo de Descartes):
presiones  rho_2 >= 1 + P(t)/t  (trio infactible)  y  rho_2 <= 1/t  (pareja en
el agujero), con P(t) = (sqrt((1+t)/(2-sqrt2)) - 1)^2. Compatibles sii
P(t) <= 1 - t, y el infimo de rho es X = 1/t* en el cruce P(t*) = 1 - t*:

    t*:  (11 - 6 sqrt2) t^2 + (2 sqrt2 - 2) t - (7 - 4 sqrt2) = 0
    X = 1/t*:  (7 - 4 sqrt2) X^2 + (2 - 2 sqrt2) X - (11 - 6 sqrt2) = 0
    racional:  17 X^4 - 4 X^3 - 62 X^2 + 4 X + 49 = 0
    X = 1.7110185903...  (en el disco: T = 1.8392868, raiz de x^3 = x^2+x+1)

con la identidad exacta  b_sq(X) = X - 1  (calco de b(T) = T - 1). Ademas el
bolsillo rigido tiene minimo cerrado:  min_alpha b_sq = b_sq(sqrt2) = 1/sqrt2,
via la identidad  sqrt((4+3 sqrt2)/2) = 2^(1/4) + 2^(-1/4).

ESCALERA cuadrada EN LA REBANADA RIGIDA sigma1 = 1 (calco de reinsercion.md
secciones 7 y 9):
    bolsillo solo                 -> Phi_sq = 1.42167  (disco: phi = 1.61803)
    + infactibilidad del trio     -> 1.70849           (disco: 1.79906 exacto,
                                                        1.7997 medido)
    + colocacion del testigo      -> X = 1.71102       (disco: T = 1.83929)
Los cruces son raices de polinomios racionales de grado 8, 8 y 4:
    peldano 1: 4a^8 - 64a^6 + 80a^5 + 100a^4 - 128a^3 - 48a^2 + 8a + 49,
               raiz a1 = 1.7033992, Phi_sq = 1/(a1-1)
    peldano 2: a^8 + 16a^7 - 4a^6 - 208a^5 + 226a^4 + 400a^3 - 508a^2
               - 208a + 289, raiz a2 = 1.5853122, rho = 1/(a2-1)
    peldano 3: 17a^4 - 4a^3 - 62a^2 + 4a + 49, raiz a3 = X (rho = alpha = X).
En el disco el primer peldano es un punto fijo (minimo en alpha = phi con valor
phi); en el cuadrado esa coincidencia se rompe (valor 1.42167 en alpha
1.70340). El peldano final conserva el punto fijo en ambos: rho = alpha.

RUPTURA (hallazgo, sin analogo en el disco): en el cuadrado la rebanada rigida
NO es el optimo del relajado de 3 ingredientes. Deslizando el par (sigma1 en
una esquina, alpha empujado por la pared hasta la tangencia), el bolsillo de
esquina se abre mas despacio que en el disco y queda una ventana
M(alpha, sigma1) < sigma1 con bloqueos mas baratos; en el disco el criterio
angular exacto muestra que esa ventana no existe (bajar sigma1 encarece o
imposibilita el bloqueo). La familia deslizada realiza fallos de best fit con
rho < X (seccion 8): el umbral del cuadrado esta estrictamente por debajo del
suelo X de la familia rigida.
"""
import itertools, math
import numpy as np
from sim import pack_feasible          # agujeros: discos, tal cual
from reinserta import feas, TRIB, PHI  # factibilidad exacta/hibrida en discos

SQ2 = math.sqrt(2.0)
CPAR = 2.0 - SQ2                       # capacidad del par: a + b <= CPAR * s


def _raiz_quad(A, B, C):
    """Raiz positiva de A x^2 + B x + C = 0."""
    return (-B + math.sqrt(B * B - 4 * A * C)) / (2 * A)


XSQ = _raiz_quad(7 - 4 * SQ2, 2 - 2 * SQ2, -(11 - 6 * SQ2))   # 1.7110185903
TSTAR = 1.0 / XSQ                                             # 0.5844471858


def b_sq(alpha):
    """Bolsillo de esquina de la config rigida s = (1+alpha)/CPAR."""
    s = (1.0 + alpha) / CPAR
    return (math.sqrt(s) - math.sqrt(max(alpha, 1.0))) ** 2


def P_suelo(t):
    """Bolsillo en la normalizacion de la familia (r_1 = 1, r_2 = t)."""
    return (math.sqrt((1.0 + t) / CPAR) - 1.0) ** 2


def rho(radii):
    rs = sorted(radii, reverse=True)
    return max(sum(rs[i + 1:]) / rs[i] for i in range(len(rs) - 1))


# ---------------- solver de empaquetamiento en cuadrado ----------------
_RNG = np.random.default_rng(7)
_PANCACHE = {}


def pack_feasible_square(radii, s, restarts=40, iters=4000, tol=1e-6):
    """(factible, posiciones) para circulos disjuntos en cuadrado de lado s,
    centrado en el origen. Calco de sim.pack_feasible con proyeccion sobre el
    cuadrado (clip por coordenada) en vez del disco."""
    h = s / 2.0
    radii = np.array(sorted(radii, reverse=True), float)
    n = len(radii)
    if n == 0:
        return True, np.zeros((0, 2))
    if radii[0] > h + 1e-12:
        return False, None
    for i in range(n):                       # condicion exacta del par: necesaria
        for j in range(i + 1, n):
            if radii[i] + radii[j] > CPAR * s + 1e-12:
                return False, None
    if n == 1:
        return True, np.zeros((1, 2))
    if n == 2:                               # el par es exacto: colocar en diagonal
        d = h - radii
        return True, np.array([[-d[0], -d[0]], [d[1], d[1]]])
    if 2 * radii.sum() + (SQ2 - 1) * (radii[0] + radii[1]) <= SQ2 * s + 1e-12:
        pos = _fila_diagonal(radii, s)       # Lema 0 cuadrado: fila en la diagonal
        return True, pos
    if math.pi * (radii ** 2).sum() > s * s + 1e-12:
        return False, None                   # cota de area
    for _ in range(restarts):
        pos = _RNG.uniform(-h / 2, h / 2, (n, 2))
        for _it in range(iters):
            moved = 0.0
            for i in range(n):
                for j in range(i + 1, n):
                    d = pos[j] - pos[i]
                    dist = np.hypot(*d)
                    need = radii[i] + radii[j]
                    if dist < need:
                        if dist < 1e-9:
                            d = _RNG.normal(size=2)
                            dist = np.hypot(*d)
                        push = (need - dist) / 2 * d / dist
                        pos[i] -= push
                        pos[j] += push
                        moved += need - dist
            for i in range(n):
                lim = h - radii[i]
                cl = np.clip(pos[i], -lim, lim)
                moved += np.abs(cl - pos[i]).sum()
                pos[i] = cl
            if moved < tol:
                return True, pos
        ok = all(np.abs(pos[i]).max() <= h - radii[i] + 1e-7 for i in range(n))
        if ok:
            ok = all(np.hypot(*(pos[j] - pos[i])) >= radii[i] + radii[j] - 1e-7
                     for i in range(n) for j in range(i + 1, n))
        if ok:
            return True, pos
    return False, None


def _fila_diagonal(radii, s):
    """Fila tangente sobre la diagonal, extremos en las esquinas (los radios
    llegan ordenados de mayor a menor: mayor y segundo en los extremos)."""
    orden = [0] + list(range(2, len(radii))) + [1]
    h = s / 2.0
    pos = np.zeros((len(radii), 2))
    d = SQ2 * radii[orden[0]]                # distancia a la esquina (0,0) girada
    prev = None
    for k, i in enumerate(orden):
        if k > 0:
            d += radii[prev] + radii[i]
        u = d / SQ2 - h                      # coordenada sobre la diagonal x=y
        pos[i] = (u, u)
        prev = i
    return pos


def feas_pan(rs, s, effort=1):
    """Hermanos en la sarten cuadrada. Exacto para k <= 2; para k >= 3, cotas
    rapidas + solver fisico (evidencia numerica en la franja indecisa)."""
    rs = sorted(rs, reverse=True)
    if not rs:
        return True
    h = s / 2.0
    if rs[0] > h + 1e-12:
        return False
    for i in range(len(rs)):
        for j in range(i + 1, len(rs)):
            if rs[i] + rs[j] > CPAR * s + 1e-12:
                return False
    if len(rs) <= 2:
        return True                          # el par es exacto
    if 2 * sum(rs) + (SQ2 - 1) * (rs[0] + rs[1]) <= SQ2 * s + 1e-12:
        return True
    key = (tuple(round(r / s, 6) for r in rs), effort)
    if key not in _PANCACHE:
        rr, it = (40, 3000) if effort == 1 else (100, 5000)
        _PANCACHE[key] = pack_feasible_square(rs, s, restarts=rr, iters=it)[0]
    return _PANCACHE[key]


# ---------------- mayor circulo vacio y maximo insertable ----------------
def _campo(P, circles, h):
    """Holgura de cada punto de P (m x 2): min(dist a lados, dist a circulos
    menos su radio). El mayor circulo vacio centrado en p tiene radio campo(p)."""
    d = np.minimum(h - np.abs(P[:, 0]), h - np.abs(P[:, 1]))
    for (cx, cy, r) in circles:
        d = np.minimum(d, np.hypot(P[:, 0] - cx, P[:, 1] - cy) - r)
    return d


def mayor_circulo_vacio(circles, s, grid=110, rounds=8):
    """Radio del mayor circulo insertable dado un cuadrado de lado s con
    circulos ya colocados (lista de (x, y, r)). Rejilla + refinado local."""
    h = s / 2.0
    xs = np.linspace(-h, h, grid)
    X, Y = np.meshgrid(xs, xs)
    P = np.column_stack([X.ravel(), Y.ravel()])
    d = _campo(P, circles, h)
    best = P[np.argmax(d)]
    val = d.max()
    step = xs[1] - xs[0]
    for _ in range(rounds):
        xs2 = np.linspace(-2 * step, 2 * step, 21)
        X2, Y2 = np.meshgrid(best[0] + xs2, best[1] + xs2)
        P2 = np.column_stack([X2.ravel(), Y2.ravel()])
        d2 = _campo(P2, circles, h)
        k = np.argmax(d2)
        if d2[k] > val:
            val, best = d2[k], P2[k]
        step /= 4.0
    return float(val), best


def maximo_insertable(a, b, s, na=15, nb=15, top=8):
    """max sobre colocaciones legales del par {a, b} en el cuadrado del mayor
    circulo insertable como tercero. Es la funcion P(a, b, s) de la hoja de
    ruta (punto 1) en version cuadrada: el trio {a, b, x} empaqueta sii
    x <= maximo_insertable(a, b, s). Rejilla 4D sobre las cajas de centros +
    refinado por busqueda de patron (evidencia numerica)."""
    h = s / 2.0
    la, lb = h - a, h - b
    if la < -1e-12 or lb < -1e-12 or a + b > CPAR * s + 1e-12:
        return None                          # el par ni siquiera cabe
    axs = np.linspace(-la, la, na)
    bxs = np.linspace(-lb, lb, nb)
    cands = []
    for ax, ay in itertools.product(axs, axs):
        for bx, by in itertools.product(bxs, bxs):
            if math.hypot(bx - ax, by - ay) < a + b - 1e-12:
                continue
            v, _ = mayor_circulo_vacio([(ax, ay, a), (bx, by, b)], s,
                                       grid=48, rounds=5)
            cands.append((v, (ax, ay, bx, by)))
    cands.sort(reverse=True)
    best_v, best_p = cands[0]
    for v0, p0 in cands[:top]:               # refinado local de la colocacion
        p = np.array(p0)
        v = v0
        step = max(2 * la, 2 * lb) / (na - 1)
        while step > 1e-5:
            mejor = False
            for k in range(4):
                for sg in (-1.0, 1.0):
                    q = p.copy()
                    q[k] += sg * step
                    q[0:2] = np.clip(q[0:2], -la, la)
                    q[2:4] = np.clip(q[2:4], -lb, lb)
                    if math.hypot(q[2] - q[0], q[3] - q[1]) < a + b - 1e-12:
                        continue
                    v2, _ = mayor_circulo_vacio(
                        [(q[0], q[1], a), (q[2], q[3], b)], s, grid=48, rounds=6)
                    if v2 > v + 1e-9:
                        v, p, mejor = v2, q, True
            if not mejor:
                step /= 2.0
        if v > best_v:
            best_v, best_p = v, tuple(p)
    return best_v


# ---------------- voraz y lex-max en sarten cuadrada ----------------
def _feas_cont(rs, cont, s, effort=1):
    if cont["tipo"] == "pan":
        return feas_pan(rs, s, effort)
    return feas(rs, cont["cap"], effort)


def greedy_cuadrado(radii, w, s, rule, effort=1):
    """Voraz decreciente en sarten cuadrada; best fit = contenedor de menor
    capacidad (la sarten cuenta como capacidad s/2, su inradio)."""
    orden = sorted(range(len(radii)), key=lambda i: -radii[i])
    cont = [{"tipo": "pan", "cap": s / 2.0, "occ": []}]
    placed = []
    for i in orden:
        cands = [c for c in cont if radii[i] <= c["cap"] + 1e-9
                 and _feas_cont([radii[j] for j in c["occ"]] + [radii[i]],
                                c, s, effort)]
        if cands:
            c = (min(cands, key=lambda c: c["cap"]) if rule == "best"
                 else max(cands, key=lambda c: c["cap"]))
            c["occ"].append(i)
            placed.append(i)
            if radii[i] - w > 1e-9:
                cont.append({"tipo": "hole", "cap": radii[i] - w, "occ": []})
    return frozenset(placed)


def set_feasible_cuadrado(sub, radii, w, s, effort=1):
    """Existe un bosque de anidamiento en la sarten cuadrada que aloje sub?"""
    ch = [[-1] + [j for j in sub if j != i and radii[i] <= radii[j] - w + 1e-9]
          for i in sub]
    for ps in itertools.product(*ch):
        pm = dict(zip(sub, ps))
        if not all(pm[i] == -1 or radii[i] < radii[pm[i]] for i in sub):
            continue
        g = {}
        for i in sub:
            g.setdefault(pm[i], []).append(i)
        ok = True
        for p, kids in g.items():
            rs = [radii[k] for k in kids]
            ok = feas_pan(rs, s, effort) if p == -1 else feas(rs, radii[p] - w, effort)
            if not ok:
                break
        if ok:
            return True
    return False


def lexmax_cuadrado(radii, w, s, effort=1):
    L = []
    for i in sorted(range(len(radii)), key=lambda i: -radii[i]):
        if set_feasible_cuadrado(L + [i], radii, w, s, effort):
            L.append(i)
    return frozenset(L)


# ---------------- verificaciones ----------------
def algebra_exacta():
    """Verificacion simbolica (sympy, solo expand: barato) y a 60 digitos."""
    import sympy as sp
    z = sp.sqrt(2)
    x, t = sp.symbols('x t')
    c = 2 - z

    # (1) cuartica racional = producto de la cuadratica por su conjugada
    q = (7 - 4 * z) * x ** 2 + (2 - 2 * z) * x - (11 - 6 * z)
    qc = (7 + 4 * z) * x ** 2 + (2 + 2 * z) * x - (11 + 6 * z)
    quart = sp.expand(q * qc)
    ok1 = quart == sp.expand(17 * x ** 4 - 4 * x ** 3 - 62 * x ** 2 + 4 * x + 49)

    # (2) derivacion del suelo desde cero: P(t) = 1 - t  <=>
    #     sqrt((1+t)/c) = 1 + sqrt(1-t); dos cuadrados eliminan las raices
    pol = sp.expand((((1 + t) - c * (2 - t)) ** 2 - 4 * c ** 2 * (1 - t)))
    objetivo = sp.expand((11 - 6 * z) * t ** 2 + (2 * z - 2) * t + (4 * z - 7))
    ok2 = sp.simplify(pol - objetivo) == 0

    # (3) raiz explicita y residuo de la cuadratica
    Xe = ((2 * z - 2) + sp.sqrt(512 - 352 * z)) / (2 * (7 - 4 * z))
    ok3 = sp.simplify(q.subs(x, Xe)) == 0

    # (4) identidad b_sq(X) = X - 1, a 60 digitos
    bX = (sp.sqrt((1 + Xe) / c) - sp.sqrt(Xe)) ** 2
    res4 = abs(sp.N(bX - (Xe - 1), 60))
    ok4 = res4 < sp.Float('1e-55')

    # (5) cuartica de t* = 1/X: 49 t^4 + 4 t^3 - 62 t^2 - 4 t + 17
    #     (conjugar sqrt2 -> -sqrt2: el termino lineal 2 sqrt2 - 2 pasa a
    #      -2 sqrt2 - 2)
    qt = sp.expand(((11 - 6 * z) * t ** 2 + (2 * z - 2) * t - (7 - 4 * z))
                   * ((11 + 6 * z) * t ** 2 - (2 * z + 2) * t - (7 + 4 * z)))
    ok5 = qt == sp.expand(49 * t ** 4 + 4 * t ** 3 - 62 * t ** 2 - 4 * t + 17)

    # (6) minimo del bolsillo rigido: b_sq(sqrt2) = 1/sqrt2, via
    #     sqrt((4+3 sqrt2)/2) = 2^(1/4) + 2^(-1/4)
    ok6 = sp.simplify(sp.sqrt((4 + 3 * z) / 2)
                      - sp.root(2, 4) - 1 / sp.root(2, 4)) == 0

    Xnum = sp.N(Xe, 30)
    return ok1, ok2, ok3, ok4, ok5, ok6, Xnum


def peldano(g_de_alpha, lo=1.05, hi=4.0, tol=1e-12, creciente=True):
    """Cruce b_sq(alpha) = g(alpha) por biseccion. b - g es creciente en los
    peldanos 1 y 2 (g decrece) y DEcreciente en el 3 (g = alpha - 1 crece mas
    deprisa que b)."""
    f = lambda a: b_sq(a) - g_de_alpha(a)
    sg = 1.0 if creciente else -1.0
    while hi - lo > tol:
        m = 0.5 * (lo + hi)
        if sg * f(m) < 0:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


# polinomios racionales de los cruces (derivados en docs/drafts/cuadrado.md,
# eliminando sqrt(alpha), sqrt(s) y sqrt2 por cuadrados y conjugacion)
POLY_P1 = [4 * c for c in (4, 0, -64, 80, 100, -128, -48, 8, 49)]
POLY_P2 = (1, 16, -4, -208, 226, 400, -508, -208, 289)
POLY_P3 = (17, -4, -62, 4, 49)


def _evalpoly(cs, x):
    v = 0.0
    for cc in cs:
        v = v * x + cc
    return v


if __name__ == "__main__":
    VERIF = []
    print(f"T = {TRIB:.7f}   phi = {PHI:.7f}")
    print(f"X_sq = {XSQ:.10f}   t* = 1/X_sq = {TSTAR:.10f}\n")

    print("1. ALGEBRA EXACTA (sympy)")
    ok1, ok2, ok3, ok4, ok5, ok6, Xnum = algebra_exacta()
    print(f"  cuadratica x conjugada = 17x^4-4x^3-62x^2+4x+49 : {ok1}")
    print(f"  suelo P(t)=1-t  =>  (11-6r2)t^2+(2r2-2)t-(7-4r2)=0 : {ok2}")
    print(f"  raiz explicita anula la cuadratica : {ok3}")
    print(f"  identidad b_sq(X) = X - 1 (60 digitos) : {ok4}")
    print(f"  cuartica de t*: 49t^4+4t^3-62t^2-4t+17 : {ok5}")
    print(f"  min bolsillo: b_sq(sqrt2) = 1/sqrt2 exacto : {ok6}")
    print(f"  X = {Xnum}")
    VERIF.append(("seccion 1 algebra exacta (ok1..ok6)",
                  all((ok1, ok2, ok3, ok4, ok5, ok6))))
    print(f"  cuartica en X (float): "
          f"{17*XSQ**4 - 4*XSQ**3 - 62*XSQ**2 + 4*XSQ + 49:.2e}\n")

    print("2. CONDICION EXACTA DEL PAR EN EL CUADRADO vs solver")
    rng = np.random.default_rng(3)
    fallos = casos = 0
    for _ in range(120):
        srt = rng.uniform(2.0, 4.0)
        a = rng.uniform(0.2, srt / 2)
        # b a ambos lados del umbral exacto, con margen que el solver resuelva
        for db in (-0.02, 0.02):
            b = min(CPAR * srt - a, srt / 2) + db * srt
            if b <= 0.01 or b > a:
                continue
            casos += 1
            pred = (a + b <= CPAR * srt) and (b <= srt / 2)
            got = pack_feasible_square([a, b], srt)[0]
            if pred != got:
                fallos += 1
    print(f"  {casos} casos cerca del umbral, discrepancias: {fallos}\n")
    VERIF.append(("seccion 2 par vs solver", casos > 0 and fallos == 0))

    print("3. BOLSILLO DE ESQUINA = MAXIMO INSERTABLE (config rigida)")
    print(f"  {'alpha':>7} {'formula':>10} {'mayor circulo vacio':>20} {'dif':>9}")
    for al in (1.0, 1.2, SQ2, 1.585, XSQ, 2.0, 2.5):
        s = (1.0 + al) / CPAR
        h = s / 2.0
        # colocacion rigida: alpha en la esquina (-h,-h), 1 en la (h,h)
        circ = [(-(h - al), -(h - al), al), (h - 1.0, h - 1.0, 1.0)]
        lec, _ = mayor_circulo_vacio(circ, s)
        print(f"  {al:>7.4f} {b_sq(al):>10.6f} {lec:>20.6f} {lec - b_sq(al):>9.2e}")
        VERIF.append((f"seccion 3 bolsillo alpha={al:.3f}",
                      abs(lec - b_sq(al)) < 5e-4))
    print("  (dif ~ 0: el mayor hueco es exactamente el bolsillo de esquina)\n")

    print("4. SUELO DE LA FAMILIA: las dos presiones y su cruce")
    print(f"  {'t':>7} {'1 + P(t)/t':>11} {'1/t':>8}  ventana")
    for t in (0.50, 0.54, 0.57, TSTAR, 0.60, 0.63):
        lo_, hi_ = 1 + P_suelo(t) / t, 1 / t
        print(f"  {t:>7.4f} {lo_:>11.6f} {hi_:>8.6f}  "
              + ("no vacia" if lo_ <= hi_ + 1e-9 else "VACIA (t > t*)"))
    print(f"  P(t*) - (1 - t*) = {P_suelo(TSTAR) - (1 - TSTAR):.2e}")
    print(f"  valor comun en t*: {1 + P_suelo(TSTAR)/TSTAR:.10f} = X\n")
    VERIF.append(("seccion 4 cruce P(t*) = 1-t*",
                  abs(P_suelo(TSTAR) - (1 - TSTAR)) < 1e-12))
    VERIF.append(("seccion 4 valor comun = X",
                  abs(1 + P_suelo(TSTAR) / TSTAR - XSQ) < 1e-9))

    print("5. ESCALERA CUADRADA (cruces exactos sobre b_sq)")
    a1 = peldano(lambda a: 0.5 / (a - 1.0))          # bolsillo solo
    a2 = peldano(lambda a: (2.0 - a) / (a - 1.0))    # + trio completo
    a3 = peldano(lambda a: a - 1.0, creciente=False) # + testigo (S cabe en u)
    print(f"  bolsillo solo   : alpha = {a1:.7f}  Phi_sq = {1/(a1-1):.7f}"
          f"   (disco: phi = {PHI:.6f} con punto fijo)")
    print(f"  + trio completo : alpha = {a2:.7f}  rho = {1/(a2-1):.7f}"
          f"   (disco: 1.7990556)")
    print(f"  + testigo       : alpha = {a3:.7f}  rho = {1 + b_sq(a3):.7f}"
          f"   (= X = {XSQ:.7f}; disco: T)")
    print(f"  punto fijo del peldano final: |alpha - X| = {abs(a3 - XSQ):.2e}")
    VERIF.append(("seccion 5 punto fijo a3 = X", abs(a3 - XSQ) < 1e-7))
    print("  polinomios racionales de los cruces (residuo en la raiz):")
    for nombre, cs, r in (("peldano 1 (grado 8)", POLY_P1, a1),
                          ("peldano 2 (grado 8)", POLY_P2, a2),
                          ("peldano 3 (cuartica)", POLY_P3, a3)):
        res = _evalpoly(cs, r)
        print(f"    {nombre}: p({r:.7f}) = {res:.2e}")
        VERIF.append((f"seccion 5 residuo {nombre}", abs(res) < 1e-5))
    print()

    print("6. EL PAR DESLIZADO: en el cuadrado, sigma1 < 1 ABARATA el bloqueo")
    print("   M(alpha, sigma1) = maximo insertable con el par {alpha, sigma1}")
    print("   LIBRE en la sarten rigida s = (1+alpha)/(2-sqrt2). Bloqueo posible")
    print("   sii M < sigma1 (hace falta sigma2 en (M, sigma1]); entonces")
    print("   rho >= max(sigma1 + M, (1 + sigma1 + M)/alpha).")
    print(f"  {'alpha':>7} {'sigma1':>7} {'M':>9} {'M<s1?':>6} {'rho':>9} "
          f"{'testigo':>8}")
    mejor_libre = (float('inf'), None)
    for al in (1.66, XSQ, 1.845):
        s = (1.0 + al) / CPAR
        for s1 in (0.80, 0.84, 0.88, 0.92, 0.96, 1.0):
            M = maximo_insertable(al, s1, s, na=11, nb=11)
            ventana = M < s1 - 1e-9
            r_libre = max(s1 + M, (1 + s1 + M) / al)
            test = ventana and (s1 + M <= al + 1e-9)
            if test and r_libre < mejor_libre[0]:
                mejor_libre = (r_libre, (al, s1, M))
            print(f"  {al:>7.4f} {s1:>7.2f} {M:>9.5f} {'si' if ventana else 'NO':>6} "
                  + (f"{r_libre:>9.5f}" if ventana else f"{'-':>9}")
                  + (f" {'si':>8}" if test else f" {'no':>8}"))
    r0, (al0, s10, M0) = mejor_libre
    print(f"  minimo del relajado con testigo en la malla: rho = {r0:.5f}")
    print(f"  en alpha = {al0:.4f}, sigma1 = {s10:.2f} (M = {M0:.5f})")
    print(f"  << X = {XSQ:.5f}: la rebanada rigida sigma1 = 1 NO es el optimo")
    print("  del relajado de 3 ingredientes en el cuadrado. CONTRASTE disco:")
    from trio import min_s2_blocking, rho_of
    # s1 = 1 exacto degenera feas3 (tangencia rigida con error flotante);
    # trio.py usa la misma salvaguarda 0.999999
    for s1 in (0.80, 0.90, 0.96, 0.999999):
        s2m = min_s2_blocking(TRIB, s1)
        if s2m is None:
            print(f"    disco alpha=T sigma1={s1:.2f}: sin bloqueo posible "
                  "(el bolsillo del disco se abre por encima de sigma1)")
        else:
            print(f"    disco alpha=T sigma1={s1:.2f}: s2_min={s2m:.5f} "
                  f"rho={rho_of(TRIB, s1, s2m):.5f}")
    print("  (en el disco bajar sigma1 encarece o imposibilita el bloqueo; el")
    print("   deslizamiento del par es un fenomeno exclusivo de la esquina)\n")

    print("7. INSTANCIAS DE LA FAMILIA CUADRADA (gemelas del contraejemplo n=4)")
    instancias = [
        ("A (calco de 5ter)", [1.0, 0.5, 0.49, 0.48], 0.03),
        ("B (cerca del suelo)", [1.0, 0.5, 0.495, 0.405], 0.10),
        ("C (mas cerca aun)", [1.0, 0.5, 0.495, 0.385], 0.12),
    ]
    s = 1.5 / CPAR                       # sarten rigida para {1, 0.5}
    print(f"  lado s = {s:.6f}  (s/2 = {s/2:.6f}, capacidad del par = 1.5)")
    for nombre, radii, w in instancias:
        M = maximo_insertable(1.0, radii[2], s, na=13, nb=13)
        blq = radii[3] > M
        L = lexmax_cuadrado(radii, w, s, effort=2)
        gb = greedy_cuadrado(radii, w, s, "best", effort=2)
        gw = greedy_cuadrado(radii, w, s, "worst", effort=2)
        print(f"  {nombre}: radios={radii} w={w} rho={rho(radii):.4f}")
        print(f"     M(1, {radii[2]}) = {M:.5f}  ->  r4={radii[3]} "
              f"{'BLOQUEA' if blq else 'no bloquea'} el trio")
        print(f"     lex-max={len(L)}  best fit={len(gb)}  worst fit={len(gw)}"
              + ("   <-- FALLO de best fit" if gb != L else ""))
        # verificacion: el fenomeno esperado es lex-max 4, best fit atascado
        VERIF.append(("seccion 7 " + nombre,
                      len(L) == 4 and len(gb) == 3 and len(gw) == 4))
    print()

    print("8. FAMILIA DESLIZADA: fallos realizables con rho < X")
    print("   Estructura: sarten rigida {alpha, 1}; sigma1, sigma2 casi iguales")
    print("   por debajo de 1; w grande bloquea los anidamientos; el testigo mete")
    print("   {sigma1, sigma2} en el agujero de alpha. El trio {alpha, sigma1,")
    print("   sigma2} es infactible por DESLIZAMIENTO: sigma2 > M(alpha, sigma1).")
    candidatos = [
        # D vive casi en el suelo deslizado (margen sobre M fino: 3e-4);
        # D' es el control negativo: la ventana se cierra (M > sigma2) y el
        # trio es factible, no hay fallo; E se aparta del suelo para ganar
        # margen de bloqueo (~0.02) a costa de subir rho.
        ("D ", 1.845, 0.16, 0.844, 0.841),
        ("D'", 1.845, 0.17, 0.840, 0.835),
        ("E ", 1.859, 0.15, 0.856, 0.853),
    ]
    for nombre, al, w, s1, s2 in candidatos:
        s = (1.0 + al) / CPAR
        radii = [al, 1.0, s1, s2]
        M = maximo_insertable(al, s1, s, na=13, nb=13)
        cond = [
            ("s2 > M           (trio bloqueado)", s2 > M),
            ("s2 > 1 - w       (no cabe en agujero de m)", s2 > 1 - w),
            ("s2 > s1 - w      (no anida en sigma1)", s2 > s1 - w),
            ("s1 > 1 - w       (no cabe en agujero de m)", s1 > 1 - w),
            ("s1 + s2 <= al - w (testigo en agujero de alpha)",
             s1 + s2 <= al - w + 1e-12),
        ]
        print(f"  {nombre}: radios={radii} w={w} s={s:.6f} rho={rho(radii):.5f}"
              f"  (X = {XSQ:.5f}, T = {TRIB:.5f})")
        print(f"     M(alpha, sigma1) = {M:.5f}")
        for txt, ok in cond:
            print(f"     [{'ok' if ok else 'FALLA'}] {txt}")
        if all(ok for _, ok in cond):
            L = lexmax_cuadrado(radii, w, s, effort=2)
            gb = greedy_cuadrado(radii, w, s, "best", effort=2)
            gw = greedy_cuadrado(radii, w, s, "worst", effort=2)
            veredicto = "  <-- FALLO con rho < X" if (gb != L and rho(radii) < XSQ) else ""
            print(f"     lex-max={len(L)}  best fit={len(gb)}  worst fit={len(gw)}"
                  f"{veredicto}")
            # D y E deben realizar el fallo con rho < X (el fenomeno)
            VERIF.append(("seccion 8 " + nombre.strip(),
                          gb != L and rho(radii) < XSQ))
        else:
            # D' es el control negativo: debe caer exactamente su primera
            # condicion (s2 <= M: la ventana se cierra)
            VERIF.append(("seccion 8 control " + nombre.strip(),
                          nombre.strip() == "D'" and not cond[0][1]
                          and all(ok for _, ok in cond[1:])))
    print()
    print("RESUMEN: el bolsillo de esquina (sqrt(s)-sqrt(a))^2 reproduce en el")
    print("cuadrado el algebra del suelo del disco: la constante hermana de la")
    print(f"Tribonacci de la familia rigida es X = {XSQ:.7f}, raiz de")
    print("17x^4-4x^3-62x^2+4x+49, con b_sq(X) = X - 1 y punto fijo rho = alpha.")
    print(f"La escalera rigida es {1/(a1-1):.4f} -> {1/(a2-1):.4f} -> {XSQ:.4f} "
          "(disco: 1.6180 -> 1.7991 -> 1.8393).")
    print("PERO el cuadrado tiene un fenomeno nuevo sin analogo en el disco: el")
    print("par deslizado (seccion 6) produce bloqueos mas baratos que el limite")
    print("rigido, y la familia deslizada (seccion 8) los realiza como fallos de")
    print("best fit con rho < X. El umbral del cuadrado queda estrictamente por")
    print("debajo de X; X sigue siendo el suelo exacto de la familia rigida.")

    # Veredicto global de VERIFICACION: identidades algebraicas + las
    # expectativas de las secciones 7-8 (el "FALLO de best fit" es el
    # fenomeno ESPERADO; que no ocurra seria el fallo de verificacion).
    VERIF.append(("cuartica de X",
                  abs(17*XSQ**4 - 4*XSQ**3 - 62*XSQ**2 + 4*XSQ + 49) < 1e-9))
    VERIF.append(("b_sq(X) = X-1", abs(b_sq(XSQ) - (XSQ - 1.0)) < 1e-12))
    VERIF.append(("1 < X < T", 1.0 < XSQ < 1.8392867552141612))
    malos = [n for n, ok in VERIF if not ok]
    print()
    print(f"VERIFICACION GLOBAL: {len(VERIF) - len(malos)}/{len(VERIF)} "
          f"comprobaciones" + (f"  [FALLO] {malos}" if malos else "  (OK)"))
    import sys
    sys.exit(0 if not malos else 1)
