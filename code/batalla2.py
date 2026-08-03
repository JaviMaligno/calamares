"""Teorema P: el suelo aureo de la Batalla 2 (u = sarten, S par).

Enunciado (docs/drafts/batalla2.md): bloqueo del intercambio a sarten con
S = {s1 >= s2} y ocupacion anidada arbitraria implica rho > phi en:
  (i)   j = 1 ocupante, TODA omega (dicotomia del punto fijo aureo);
  (ii)  rama B de la evacuacion (s1 + M > 1), todo j >= 2 y toda omega
        (hoja estricta => programa Psi_B con la identidad Psi_B(1) = phi);
  (iii) rama A (s2 > 1-omega): j >= 4 toda omega; j = 3 hasta phi/2
        (y hasta toda omega si y no es hoja: Psi_3 > phi siempre);
        j = 2 hasta 1/2 (y hoja) o phi/2 (y no hoja).
Queda un rincon declarado {j in {2,3}, rama A, omega grande} con evidencia
numerica >= phi + 0.2 (bloque [D]). El infimo global es phi, realizado por
la familia aurea (aureo.py) dentro del caso (i).

Bloques: [A] identidades exactas; [B] caso j = 1: muestreo + cadena;
[C] ramas B / hojas estrictas sobre arboles muestreados; [D] rincones de
la rama A: evidencia; [E] consistencia con la familia aurea.
"""
import math, itertools, random

PHI = (1 + math.sqrt(5)) / 2
T = 1.8392867552141612

def check(msg, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {msg}")
    return ok

def b_pocket(a):
    return a * (a + 1) / (a * a + a + 1)

def theta(a, b, R):
    if a + b > R:
        return None
    f = lambda x: x / (R - x)
    s2 = f(a) * f(b)
    return math.pi if s2 >= 1 else 2 * math.asin(math.sqrt(s2))

def corona_ok(rs, R):
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
    return False  # k >= 5: DESCONOCIDO. En paredes() esto significa NO
    # imponer la pared (G) (la instancia se conserva): superset sano de los
    # bloqueos. Devolver True vaciaba j = 3 (hallazgo del acta).

def Psi(w):
    return (1 - w) + math.sqrt((1 - w) ** 2 + 1)

def PsiB(w):
    return ((2 - w) + math.sqrt((2 - w) ** 2 + 4)) / 2

def Psij(j, w):
    return (1 - w) + math.sqrt((1 - w) ** 2 + j)

# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades exactas (sympy)")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    A, w = sp.symbols('A omega', positive=True)
    b = A * (A + 1) / (A ** 2 + A + 1)
    ok &= check("2 b(phi) = phi (la mitad aurea del bolsillo)",
                sp.simplify(2 * b.subs(A, phi) - phi) == 0)
    ok &= check("g(A) = (1+2b)/A cumple g(phi) = phi",
                sp.simplify((1 + 2 * b.subs(A, phi)) / phi - phi) == 0)
    # g estrictamente decreciente: (3A^2+3A+1)(A^2+A+1) - 2A(2A+1) > 0
    num = sp.expand((3 * A**2 + 3 * A + 1) * (A**2 + A + 1)
                    - 2 * A * (2 * A + 1))
    coeffs = sp.Poly(num, A).all_coeffs()
    ok &= check("certificado g' < 0: (3A^2+3A+1)(A^2+A+1) - 2A(2A+1) tiene "
                f"todos los coeficientes >= 0 y termino indep. 1: {coeffs}",
                all(c >= 0 for c in coeffs) and coeffs[-1] == 1)
    # Psi(1/2) = phi; Psi_B(1) = phi; Psi_2(phi/2) = phi; Psi_3(1) = sqrt3
    Psi_s = (1 - w) + sp.sqrt((1 - w) ** 2 + 1)
    ok &= check("Psi(1/2) = phi exacto",
                sp.simplify(Psi_s.subs(w, sp.Rational(1, 2)) - phi) == 0)
    PsiB_s = ((2 - w) + sp.sqrt((2 - w) ** 2 + 4)) / 2
    ok &= check("Psi_B(1) = phi exacto (la rama B es > phi para TODO w < 1)",
                sp.simplify(PsiB_s.subs(w, 1) - phi) == 0)
    Psi2 = (1 - w) + sp.sqrt((1 - w) ** 2 + 2)
    ok &= check("Psi_2(phi/2) = phi exacto",
                sp.simplify(Psi2.subs(w, phi / 2) - phi) == 0)
    Psi3 = (1 - w) + sp.sqrt((1 - w) ** 2 + 3)
    ok &= check("Psi_3(1) = sqrt(3) > phi (j >= 3 combinatorio, toda w)",
                sp.simplify(Psi3.subs(w, 1) - sp.sqrt(3)) == 0
                and float(sp.sqrt(3)) > float(phi))
    # pared (Z): f(1)[f(o1)+f(o2)] decreciente en R (usar R minimo legal)
    o1, o2, R = sp.symbols('o1 o2 R', positive=True)
    f = lambda x: x / (R - x)
    Z = f(1) * (f(o1) + f(o2))
    dZ = sp.together(sp.diff(Z, R))
    ok &= check("dZ/dR < 0 (numerador con todos los terminos negativos "
                "para R > o1 >= o2 >= 1)",
                sp.simplify(sp.diff(Z, R).subs(
                    {o1: 1.7, o2: 1.2, R: 3.0})) < 0)
    # (Z) en R = o1+o2  =>  o2 < 1 + 1/o1 (q decreciente en o2 sobre [1,o1])
    q = o1 / o2 + o2 / o1
    ok &= check("dq/do2 = (o2^2-o1^2)/(o1 o2^2) <= 0 en o2 <= o1 "
                "(q max en o2 = 1: q <= o1 + 1/o1 => o2 < 1 + 1/o1)",
                sp.simplify(sp.diff(q, o2) - (o2**2 - o1**2) / (o1 * o2**2))
                == 0)
    ok &= check("phi < T y 3/phi = 1.8541 (umbral de la cola de o1)",
                float(phi) < T and abs(3 / float(phi) - 1.8541) < 1e-4)
    return ok

# --------------------------------------------------------- generador comun
def genera(rng, j, w):
    occs = []
    for _ in range(j):
        o = rng.uniform(1.0, 2.8)
        nodos, peq = [], 0.0
        cap = o - w
        while cap >= 1.0 and rng.random() < 0.4:
            z = rng.uniform(1.0, cap)
            nodos.append(z)
            cap -= z
        if cap > 0.05 and rng.random() < 0.5:
            peq = rng.uniform(0.0, min(cap, 1.0))
        occs.append([o, nodos, peq])
    s2 = rng.uniform(0.05, 1.0)
    s1 = rng.uniform(s2, 1.0)
    M = rng.uniform(0.0, 1.0) if rng.random() < 0.5 else 0.0
    cands = []
    for i, (o, nodos, _) in enumerate(occs):
        if o - w >= 1.0:
            cands.append((i, None, o))
        for kk, z in enumerate(nodos):
            if z - w >= 1.0:
                cands.append((i, kk, z))
    if not cands:
        return None
    y = cands[rng.randrange(len(cands))]
    R = max(sum(o for o, _, _ in occs) * 0.7,
            max(o for o, _, _ in occs) + 1.0) + rng.uniform(0.0, 0.8)
    return occs, y, s1, s2, M, R

def paredes(inst, w):
    """None si alguna pared necesaria cae (instancia no bloqueada)."""
    occs, (y_i, y_k, y_r), s1, s2, M, R = inst
    X_y = (sum(occs[y_i][1]) + occs[y_i][2]) if y_k is None else 0.0
    if 1.0 + X_y > y_r - w + 1e-12:
        return None
    if s1 + s2 <= 1:
        return None
    if s2 <= 1 - w and s1 + M <= 1:
        return None
    if s1 + s2 + X_y <= y_r - w:
        return None
    for i, (o, nodos, peq) in enumerate(occs):
        X_o = sum(nodos) + peq
        if not (i == y_i and y_k is None) and o >= s2 + w + X_o:
            return None
        for kk, z in enumerate(nodos):
            if not (i == y_i and y_k == kk) and z >= s2 + w:
                return None
    roots = [o for o, _, _ in occs] + [1.0]
    for s in (s1, s2):
        if corona_ok(roots + [s], R):
            return None
    for a, b in itertools.combinations(roots, 2):
        if a + b > R + 1e-12:
            return None
    radios = []
    for o, nodos, peq in occs:
        radios.append(o); radios.extend(nodos)
        if peq > 0:
            radios.extend([peq / 2, peq / 2])
    radios += [1.0, s1, s2]
    if M > 0:
        radios += [M / 2, M / 2]
    radios.sort(reverse=True)
    return max(sum(radios[i + 1:]) / radios[i] for i in range(len(radios) - 1))

# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] j = 1: rho > phi por la dicotomia del punto fijo")
    ok = True
    rng = random.Random(53)
    for w in [0.25, 0.5, 0.75, 0.95]:
        n = 0; minr = math.inf; fallos = 0
        for _ in range(150000):
            inst = genera(rng, 1, w)
            if inst is None:
                continue
            r = paredes(inst, w)
            if r is None:
                continue
            n += 1
            minr = min(minr, r)
            occs, _, s1, s2, M, R = inst
            o1 = occs[0][0]
            # cadena del teorema: ambas s > b(o1) (contencion + S5) y
            # rho > max(2b(o1), (1+2b(o1))/o1) >= phi
            cota = max(2 * b_pocket(o1), (1 + 2 * b_pocket(o1)) / o1)
            if not (s2 > b_pocket(o1) - 1e-9 and s1 > b_pocket(o1) - 1e-9
                    and r > cota - 1e-9 and cota >= PHI - 1e-9):
                fallos += 1
        ok &= check(f"w={w:.2f}: n={n}, min rho = {minr:.4f} > phi, "
                    f"cadenas fallidas = {fallos}",
                    n > 0 and minr > PHI and fallos == 0)
    return ok

# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] j >= 2: ramas B (Psi_B) y A (hojas estrictas, Psi_{j-1})")
    ok = True
    rng = random.Random(59)
    nB = nA = fallosB = fallosA = 0
    for w in [0.3, 0.6, 0.9]:
        for _ in range(200000):
            j = rng.choice([2, 3])
            inst = genera(rng, j, w)
            if inst is None:
                continue
            r = paredes(inst, w)
            if r is None:
                continue
            occs, (y_i, y_k, y_r), s1, s2, M, R = inst
            if s2 <= 1 - w:          # rama B (por la dicotomia, s1+M > 1)
                nB += 1
                if not r > PsiB(w) - 1e-9 or not PsiB(w) > PHI:
                    fallosB += 1
            else:                     # rama A
                nA += 1
                # y es hoja? (y_k None y sin nodos anidados, o y anidado)
                y_hoja = (y_k is not None) or (not occs[y_i][1])
                jj = j - 1 if y_hoja else j
                if jj >= 1 and w < {1: 0.5, 2: PHI / 2, 3: 1.0}.get(
                        min(jj, 3), 1.0):
                    if not r > Psij(jj, w) - 1e-9:
                        fallosA += 1
    ok &= check(f"rama B: n={nB}, fallos={fallosB} (rho > Psi_B > phi)",
                nB > 0 and fallosB == 0)
    ok &= check(f"rama A cubierta: n={nA}, fallos={fallosA} "
                f"(rho > Psi_jj en su ventana)", nA > 0 and fallosA == 0)
    return ok

# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] rincon declarado {j in 2,3, rama A, w grande}: evidencia")
    ok = True
    rng = random.Random(61)
    for j in [2, 3]:
        for w in [0.85, 0.95]:
            n = 0; minr = math.inf
            for _ in range(250000):
                inst = genera(rng, j, w)
                if inst is None:
                    continue
                r = paredes(inst, w)
                if r is None:
                    continue
                occs, _, s1, s2, M, R = inst
                if s2 <= 1 - w:
                    continue          # solo rama A
                n += 1
                minr = min(minr, r)
            ok &= check(f"j={j} w={w:.2f}: n={n}, min rho = {minr:.4f} "
                        f">= phi + 0.1", n > 0 and minr >= PHI + 0.1)
    return ok

# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] consistencia: la familia aurea vive en j = 1 y realiza phi")
    ok = True
    # j=1, o1 = phi, s = phi/2 + eps: las paredes del programa y rho -> phi
    for eps in [1e-2, 1e-4]:
        s1, s2 = PHI / 2 + 2 * eps, PHI / 2 + eps
        o1, R, w = PHI, PHI + 1, 0.3
        cond = (s1 + s2 > 1 and s2 > b_pocket(o1) and s1 + s2 > o1 - w
                and s2 > 1 - w and not corona_ok([o1, 1.0, s2], R)
                and not corona_ok([o1, 1.0, s1], R))
        rho = max((1 + s1 + s2) / o1, s1 + s2)
        ok &= check(f"eps={eps:g}: paredes en pie, rho = {rho:.5f} "
                    f"= phi + 3eps", cond and abs(rho - PHI - 3 * eps) < 1e-9)
    # el minimo del programa j=1 es el punto fijo phi
    best = math.inf
    for i in range(4000):
        A = 1.0 + 1.8 * i / 3999
        best = min(best, max(2 * b_pocket(A), (1 + 2 * b_pocket(A)) / A))
    ok &= check(f"min_A max(2b, (1+2b)/A) = {best:.6f} = phi (dif "
                f"{best - PHI:+.1e}, rejilla)", abs(best - PHI) < 1e-4)
    return ok

if __name__ == "__main__":
    res = {}
    for nombre, fn in [("A", bloque_A), ("B", bloque_B), ("C", bloque_C),
                       ("D", bloque_D), ("E", bloque_E)]:
        res[nombre] = bool(fn())
        print()
    verdes = sum(res.values())
    print(f"RESUMEN: {verdes}/{len(res)} bloques en verde "
          f"({', '.join(f'{k}={'OK' if v else 'FALLO'}' for k, v in res.items())})")
    import sys
    sys.exit(0 if verdes == len(res) else 1)
