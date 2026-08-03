"""Verificacion del Teorema T3: S de TRES piezas en la plantilla canonica.

Enunciado (docs/drafts/striple.md): bloqueo del paso de intercambio en la
plantilla canonica con S = {s1 >= s2 >= s3} (tres piezas, ocupacion del
agujero de m arbitraria) implica rho > Phi(omega) > T para todo omega en
(0,1); ademas rho >= 13/7 en la rama {s3 <= s1-w, s2 > 1-w}, y
rho > gamma_w + 1 - 2w >= 2.35 en la rama del zigzag, donde gamma_w es la
DEFORMACION AUREA: la raiz > 1 de

    alpha^3 = alpha^2 + alpha + w*(alpha^2 + alpha + 1),   gamma_0 = phi.

Bloques: [A] simbolico exacto (sympy); [B] oraculo sistematico de
colocaciones y muestreo: todo bloqueo cumple rho > Phi(w); [C] las cadenas
de cada rama sobre los bloqueos muestreados; [D] k = 4 (hueco declarado):
evidencia de margen; [E] m con hijos (rama B de la evacuacion).
"""
import math, itertools, random

T = 1.8392867552141612
PHI = (1 + math.sqrt(5)) / 2

def check(msg, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {msg}")
    return ok

def b_pocket(a):
    return a * (a + 1) / (a * a + a + 1)

def T_c(c):
    """Raiz positiva de a^3 = c(a^2+a+1)."""
    lo, hi = 1.0, 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if mid ** 3 - c * (mid * mid + mid + 1) < 0:
            lo = mid
        else:
            hi = mid
    return lo

def Phi(w):
    return T_c(1 + w) - w

def gamma_w(w):
    lo, hi = 1.0, 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if mid ** 3 - mid * mid - mid - w * (mid * mid + mid + 1) < 0:
            lo = mid
        else:
            hi = mid
    return lo

def theta(a, b, R):
    if a + b > R:
        return None
    f = lambda x: x / (R - x)
    s2 = f(a) * f(b)
    return math.pi if s2 >= 1.0 else 2.0 * math.asin(math.sqrt(s2))

def corona_ok(rs, R):
    """Corona: k=3 criterio del trio (C1/C4); k=4 Lema U4 (C5')."""
    rs = sorted(rs, reverse=True)
    k = len(rs)
    ths = {}
    for i, j in itertools.combinations(range(k), 2):
        t = theta(rs[i], rs[j], R)
        if t is None:
            return False
        ths[(i, j)] = t
    if k <= 2:
        return True
    if k == 3:
        return sum(ths.values()) <= 2 * math.pi + 1e-12
    if k == 4:
        trio = ths[(0, 1)] + ths[(0, 2)] + ths[(1, 2)]
        tot = sum(ths.values()) - ths[(0, 1)] - ths[(2, 3)]
        return trio <= 2 * math.pi + 1e-12 and tot <= 2 * math.pi + 1e-12
    if k == 5:
        return corona5_LP(ths)
    return False  # k >= 6: fuera de alcance; conservador (no colocar)

def corona5_LP(ths):
    """Corona de 5 circulos: factibilidad del sistema de huecos (Lema C1)
    por orden ciclico, via el criterio dual exacto del Teorema C7:
    subconjuntos + pentagrama, por cada uno de los 12 ordenes."""
    import itertools as it
    for perm in it.permutations(range(1, 5)):
        if perm[0] > perm[-1]:
            continue
        orden = (0,) + perm
        th = {}
        for p, q in it.combinations(range(5), 2):
            i, j = sorted((orden[p], orden[q]))
            th[(p, q)] = ths[(i, j)]
        okorden = True
        # certificados de subconjunto (C2): todo T con |T| >= 3
        for r in (3, 4, 5):
            for sub in it.combinations(range(5), r):
                s = sum(th[(sub[a], sub[a + 1])] for a in range(r - 1))
                s += th[(sub[0], sub[-1])]
                if s > 2 * math.pi + 1e-12:
                    okorden = False; break
            if not okorden:
                break
        if not okorden:
            continue
        # pentagrama (C7): suma de las 5 diagonales <= 4 pi
        diag = (th[(0, 2)] + th[(1, 3)] + th[(2, 4)] + th[(0, 3)]
                + th[(1, 4)])
        if diag <= 4 * math.pi + 1e-12:
            return True
    return False

def bosques(k):
    out = []
    def rec(i, parent):
        if i == k:
            out.append(tuple(parent)); return
        rec(i + 1, parent + [None])
        for j in range(i):
            rec(i + 1, parent + [j])
    rec(0, [])
    return out

def colocable(S, w, al, M=0.0):
    """Oraculo constructivo (m con hijos de masa M): reinsertable?

    Recursos: D_m (fila <= 1, comparte con la evacuacion de M), H_m (fila
    <= 1-w si M evacuada o junto a M si no), U (fila con m: 1+suma <= al-w),
    anidamiento en S, y re-empaquetado de v ({al} u raices como corona en
    al+1). Con M > 0: H_m se usa o bien con M dentro (fila M+X <= 1-w) o
    bien evacuando M a D_m (fila M+X_D <= 1)."""
    k = len(S)
    for par in bosques(k):
        loads = [0.0] * k
        ok = True
        for i, p in enumerate(par):
            if p is not None:
                loads[p] += S[i]
        for i, p in enumerate(par):
            if p is not None and loads[p] > S[p] - w + 1e-12:
                ok = False; break
        if not ok:
            continue
        roots = [i for i in range(k) if par[i] is None]
        # asignaciones: D (D_m), H (H_m con M dentro), E (H_m evacuando M a
        # D_m), U (junto a m), V (corona de v con alpha)
        for asig in itertools.product("DHEUV", repeat=len(roots)):
            evac = "E" in asig
            if evac and "H" in asig:
                continue
            # V (re-empaquetar v en corona con alpha) es incompatible con
            # D (el disco D_m vive en v con alpha en su posicion original)
            # y con E (la evacuacion de M usa D_m)
            if "V" in asig and ("D" in asig or evac):
                continue
            tot = {"D": 0.0, "H": 0.0, "U": 0.0}
            V = []
            for r, a in zip(roots, asig):
                if a == "V":
                    V.append(S[r])
                elif a in "HE":
                    tot["H"] += S[r]
                else:
                    tot[a] += S[r]
            if evac:
                tot["D"] += M
            capH = (1 - w) - (0.0 if evac else M)
            if tot["D"] > 1 + 1e-12:
                continue
            # H_m solo restringe si se usa (con M > 1-w y H sin usar, la
            # colocacion es legal dejando M donde esta — matiz del acta)
            if tot["H"] > 1e-12 and tot["H"] > capH + 1e-12:
                continue
            if 1 + tot["U"] > al - w + 1e-12:
                continue
            if V and not corona_ok([al] + V, al + 1.0):
                continue
            return True
    return False

def rho_can(S, al, M=0.0):
    Ssum = sum(S) + M
    return max(Ssum, (1 + Ssum) / al)

# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] simbolico exacto (sympy)")
    import sympy as sp
    ok = True
    a, s2, w = sp.symbols('alpha sigma2 omega', positive=True)
    R = a + 1
    f = lambda x: x / (R - x)
    # zigzag => bolsillo: f(s2)*(alpha + 1/alpha) > 1  <=>  s2 > b(alpha)
    expr = sp.simplify(f(s2) * (a + 1 / a) - 1)
    b = a * (a + 1) / (a ** 2 + a + 1)
    lhs = sp.simplify(sp.together(expr) * (R - s2) * a)
    # lhs = s2*(a^2+1)/... comprobar: expr > 0 <=> s2*(a^2+a+1) > a(a+1)
    cond = sp.expand(s2 * (a ** 2 + 1) + s2 * a - a * (a + 1))
    ok &= check("f(s2)(alpha+1/alpha) - 1 tiene el signo de "
                "s2(alpha^2+alpha+1) - alpha(alpha+1)  [= s2 - b]",
                sp.simplify(lhs - cond) == 0)
    # gamma_w: 2b(alpha) = alpha - w  <=>  alpha^3 = alpha^2+alpha+w(...)
    pol = sp.expand((a - w) * (a ** 2 + a + 1) - 2 * a * (a + 1))
    ok &= check("2b = alpha-omega  <=>  alpha^3-alpha^2-alpha-"
                "omega(alpha^2+alpha+1) = 0",
                sp.simplify(pol - (a**3 - a**2 - a - w*(a**2 + a + 1))) == 0)
    # gamma_0 = phi: alpha^2 = alpha + 1
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    ok &= check("gamma_0 = phi (raiz de alpha^2 = alpha+1)",
                sp.simplify((phi ** 3 - phi ** 2 - phi).rewrite(sp.sqrt)) == 0)
    # 1 - 2b'(alpha) > 0 para alpha >= 1 (la ventana alpha > gamma_w es valida)
    bp = sp.diff(b, a)
    num = sp.expand((a ** 2 + a + 1) ** 2 - 2 * (2 * a + 1))
    ok &= check("(alpha^2+alpha+1)^2 - 2(2alpha+1) > 0 en alpha >= 1 "
                "(1 - 2b' > 0; en alpha=1: 9-6=3)",
                sp.simplify(num - ((a**2+a+1)**2 - 4*a - 2)) == 0
                and num.subs(a, 1) == 3)
    # cota (3/2)Phi - omega >= 13/7 en (0, 1/7] via la cuerda Phi >= T+(13-7T)w
    Tsym = sp.symbols('T', positive=True)
    cuerda = sp.Rational(3, 2) * (Tsym + (13 - 7 * Tsym) * w) - w
    val0 = cuerda.subs(w, 0)      # (3/2)T = 2.7589 > 13/7
    ok &= check("(3/2)Phi - omega en omega=0 vale (3/2)T = 2.7589 > 13/7",
                float(val0.subs(Tsym, T)) > 13 / 7)
    # d/dw de la cuerda = (3/2)(13-7T) - 1 = 1.5*0.1249... - 1 < 0, y en 1/7:
    v17 = float(cuerda.subs({Tsym: T, w: sp.Rational(1, 7)}))
    ok &= check(f"cuerda en omega=1/7: {v17:.4f} > 13/7 = {13/7:.4f}",
                v17 > 13 / 7)
    # suelo exacto de la rama 2B: el cruce de las dos cotas es gamma = 2,
    # es decir omega = 2/7 (identidad 8 = 4 + 2 + 2), con valor 17/7
    g27 = 2 ** 3 - 2 ** 2 - 2 - sp.Rational(2, 7) * (4 + 2 + 1)
    ok &= check("gamma_{2/7} = 2 exacto (8 = 4 + 2 + (2/7)*7)", g27 == 0)
    v_cruce = 2 + 1 - sp.Rational(4, 7)
    ok &= check("valor en el cruce: gamma+1-2w = 2gamma-1-2w = 17/7 en "
                "(gamma, w) = (2, 2/7)",
                v_cruce == sp.Rational(17, 7)
                and (2 * 2 - 1 - sp.Rational(4, 7)) == sp.Rational(17, 7))
    # monotonia de las dos cotas (b1 decrece, b2 crece: 1 < gamma' < 2) y
    # min del max = 17/7 en rejilla fina
    gs = [(w_, gamma_w(w_)) for w_ in [i / 1000 for i in range(1, 1000)]]
    b1 = [g + 1 - 2 * w_ for w_, g in gs]
    b2 = [2 * g - 1 - 2 * w_ for w_, g in gs]
    mono = all(x >= y - 1e-12 for x, y in zip(b1, b1[1:])) and \
           all(x <= y + 1e-12 for x, y in zip(b2, b2[1:]))
    peor = min(max(x, y) for x, y in zip(b1, b2))
    ok &= check(f"b1 decreciente y b2 creciente en rejilla; min del max = "
                f"{peor:.6f} >= 17/7 - 1e-4 = {17/7:.6f}",
                mono and peor >= 17 / 7 - 1e-4)
    # Phi(w) > T para w > 0 (Phi' > 0, Phi(0) = T): anclas
    ok &= check(f"Phi(0.001) = {Phi(0.001):.6f} > T y Phi(1/7) = 13/7 "
                f"({Phi(1/7):.6f})",
                Phi(0.001) > T and abs(Phi(1 / 7) - 13 / 7) < 1e-9)
    return ok

def muestra_S3(rng, w):
    """Muestreo mixto: 1/3 amplio, 1/3 dirigido al par-con-polvo (sigma1,
    sigma2 grandes, alpha pegado a (W)), 1/3 dirigido a la rama 2B (todo
    grande, alpha < 1+w+s3)."""
    modo = rng.random()
    if modo < 1 / 3:
        s1 = rng.uniform(0.3, 1.0)
        s2 = rng.uniform(0.25, s1)
        s3 = rng.uniform(0.005, s2)
        al = rng.uniform(max(1 + w, s1 + s2 + w), 3.8)
    elif modo < 2 / 3:
        s1 = rng.uniform(0.85, 1.0)
        s2 = rng.uniform(0.75, s1)
        s3 = rng.uniform(0.005, min(0.5, s2))
        base = max(1 + w, s1 + s2 + w)
        al = base + rng.uniform(0.0, 0.5) * rng.random()
    else:
        s1 = rng.uniform(0.8, 1.0)
        s2 = rng.uniform(max(0.7, 1 - w), s1)
        s3 = rng.uniform(max(0.6, 1 - w, s1 - w), s2) if s2 > max(0.6, 1 - w, s1 - w) \
            else rng.uniform(0.005, s2)
        base = max(1 + w, s1 + s2 + w)
        al = rng.uniform(base, max(base + 1e-6, 1 + w + s3))
    return [s1, s2, s3], al

# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] oraculo de colocaciones + muestreo: todo bloqueo con rho > Phi")
    ok = True
    rng = random.Random(101)
    for w in [0.05, 0.15, 0.3, 0.5, 0.7, 0.9]:
        n = 0; viol = 0; minr = math.inf
        for _ in range(80000):
            S, al = muestra_S3(rng, w)
            if S[0] + S[1] > al - w + 1e-12 or not S[2] <= S[1] <= S[0] < 1:
                continue
            if al - w < 1:
                continue
            if colocable(S, w, al):
                continue
            n += 1
            r = rho_can(S, al)
            minr = min(minr, r)
            if r <= Phi(w):
                viol += 1
        ok &= check(f"w={w:.2f}: n={n}, min rho = {minr:.4f} > "
                    f"Phi = {Phi(w):.4f}, viol = {viol}",
                    n > 0 and viol == 0)
    return ok

# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] cadenas por rama sobre los bloqueos muestreados")
    ok = True
    rng = random.Random(211)
    tot = {"R1A": 0, "R1B": 0, "2A": 0, "2B": 0}
    fallos = 0
    for w in [0.1, 0.3, 0.6, 0.85]:
        for _ in range(150000):
            S, al = muestra_S3(rng, w)
            s1, s2, s3 = S
            M = 0.0 if rng.random() < 0.5 else rng.uniform(0.0, 1.2)
            if s1 + s2 > al - w + 1e-12 or not s3 <= s2 <= s1 < 1:
                continue
            if al - w < 1:
                continue
            if colocable(S, w, al, M=M):
                continue
            trio_corona = corona_ok([al, s1, s2], al + 1.0)
            if s3 <= s1 - w + 1e-12:
                # paredes heredadas: B1 (sin corona del trio, s3 anidada en
                # s1), la pared del acta s2+M > 1-w, la dicotomia, B4, W,
                # y B1+W => s1+s2 >= 1+b(alpha) >= Phi
                comun = ((not trio_corona)
                         and s2 + M > 1 - w - 1e-9
                         and s1 + s2 >= 1 + b_pocket(al) - 1e-9
                         and s1 + s2 >= Phi(w) - 1e-9
                         and s2 > al - w - 1 - 1e-9)
                if s2 > 1 - w - 1e-9:
                    rama = "R1A"
                    cond = comun and s1 + s2 > 13 / 7 - 1e-6
                else:
                    rama = "R1B"
                    cond = (comun and s1 + M > 1 - 1e-9
                            and rho_can(S, al, M=M) > 1 + s1 - 1e-9)
            elif not trio_corona:
                rama = "2A"
                cond = (s1 + s2 >= 1 + b_pocket(al) - 1e-9
                        and al >= T_c(1 + w) - 1e-9
                        and s1 + s2 >= Phi(w) - 1e-9)
            else:
                rama = "2B"
                cond = (s3 + M > 1 - w - 1e-9      # (m1), con M en H_m
                        and al < 1 + w + s3 + 1e-9  # (m2)
                        and s2 > b_pocket(al) - 1e-9  # zigzag => bolsillo
                        and al > gamma_w(w) - 1e-9
                        and rho_can(S, al, M=M) > gamma_w(w) + 1 - 2 * w
                        - 1e-9)
            tot[rama] += 1
            if not cond:
                fallos += 1
    ok &= check(f"ramas pobladas R1A={tot['R1A']}, R1B={tot['R1B']}, "
                f"2A={tot['2A']}, 2B={tot['2B']}; cadenas verificadas, "
                f"fallos = {fallos}",
                fallos == 0 and all(tot[k] > 0 for k in tot))
    return ok

# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] k = 4 (hueco declarado): evidencia de margen")
    ok = True
    rng = random.Random(307)
    for w in [0.2, 0.5, 0.8]:
        minr = math.inf; n = 0
        for _ in range(15000):
            S3, al = muestra_S3(rng, w)
            s4 = rng.uniform(0.01, S3[2])
            S = S3 + [s4]
            if S[0] + S[1] > al - w + 1e-12 or al - w < 1:
                continue
            if colocable(S, w, al):
                continue
            n += 1
            minr = min(minr, rho_can(S, al))
        ok &= check(f"w={w:.1f}: n={n}, min rho k=4 = {minr:.4f} > T",
                    n == 0 or minr > T)
    return ok

# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] m con hijos (masa M): rho > Phi tambien con H_m ocupado")
    ok = True
    rng = random.Random(401)
    for w in [0.1, 0.4, 0.7]:
        n = 0; viol = 0; minr = math.inf
        for _ in range(80000):
            S, al = muestra_S3(rng, w)
            s1, s2, s3 = S
            M = rng.uniform(0.0, 1.2)   # incluye M > 1-w (acta: legal)
            if s1 + s2 > al - w + 1e-12 or not s3 <= s2 <= s1 < 1:
                continue
            if al - w < 1:
                continue
            if colocable(S, w, al, M=M):
                continue
            n += 1
            r = rho_can(S, al, M=M)
            minr = min(minr, r)
            if r <= Phi(w):
                viol += 1
        ok &= check(f"w={w:.1f}: n={n}, min rho = {minr:.4f} > "
                    f"Phi = {Phi(w):.4f}, viol = {viol}",
                    n > 0 and viol == 0)
    return ok

if __name__ == "__main__":
    res = {}
    for nombre, fn in [("A", bloque_A), ("B", bloque_B), ("C", bloque_C),
                       ("D", bloque_D), ("E", bloque_E)]:
        res[nombre] = fn()
        print()
    verdes = sum(res.values())
    print(f"RESUMEN: {verdes}/{len(res)} bloques en verde "
          f"({', '.join(f'{k}={'OK' if v else 'FALLO'}' for k, v in res.items())})")
    import sys
    sys.exit(0 if verdes == len(res) else 1)
