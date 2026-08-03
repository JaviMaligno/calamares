"""El umbral es aureo: contraejemplo a la conjetura del umbral de Tribonacci.

Teorema A1 (docs/drafts/umbral_aureo.md): para todo omega en
(1 - phi/2, phi - 1) y todo eps > 0 suficientemente pequeno, la instancia

    sarten R = phi + 1,  anchura w = omega,
    radios {phi, 1, phi/2 + 2 eps, phi/2 + eps}   (estrictos)

tiene rho = phi + 2eps < T, su conjunto lex-max son los CUATRO aros
(testigo: m = 1 en el agujero de phi, {s, s} en corona con phi en la
sarten), y el voraz con worst fit (m -> sarten) se atasca en 3: la pareja
{phi, 1} llena la sarten por tangencia diametral (phi + 1 = R) y todo
tercer circulo cabe solo si <= b2(phi, 1) = phi/2 (rigidez S5, exacta);
s = phi/2 + eps no cabe; el agujero de phi no admite el par (2s > phi -
omega); H_m tampoco (s > 1 - omega). La obliviousness de colocacion FALLA
en rho = phi + 2eps < T: la conjetura del umbral T es FALSA tal cual; el
umbral geometrico es <= phi, y se conjetura = phi (el primer peldano de la
escalera: la subida a T usaba la capacidad del testigo (W), que solo
existe cuando u es un agujero; con u = sarten no hay (W)).

Bloques: [A] identidades exactas (sympy); [B] la instancia concreta:
paredes, testigo con coordenadas, arbol exhaustivo del voraz;
[C] la familia en eps -> 0 y toda la ventana de omega (delta = 0, todo
exacto); [D] robustez con holgura R = phi + 1 + delta (criterio angular,
evidencia); [E] el programa de la Batalla 2 (u = sarten, par): minimo
numerico -> phi (la nueva conjetura).
"""
import math, itertools

PHI = (1 + math.sqrt(5)) / 2
T = 1.8392867552141612

def check(msg, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {msg}")
    return ok

def b2(A, B):
    return A * B * (A + B) / (A * A + A * B + B * B)

def theta(a, b, R):
    if a + b > R:
        return None
    f = lambda x: x / (R - x)
    s2 = f(a) * f(b)
    return math.pi if s2 >= 1 else 2 * math.asin(math.sqrt(s2))

# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades exactas")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    A, B = sp.symbols('A B', positive=True)
    b2s = A * B * (A + B) / (A ** 2 + A * B + B ** 2)
    ok &= check("b2(phi, 1) = phi/2 exacto",
                sp.simplify(b2s.subs({A: phi, B: 1}) - phi / 2) == 0)
    ok &= check("(1 + phi)/phi = phi (la cola de phi es aurea)",
                sp.simplify((1 + phi) / phi - phi) == 0)
    ok &= check("el punto fijo 2b(A)*A = 1 + 2b(A) se resuelve en A = phi",
                sp.simplify(2 * b2s.subs(B, 1).subs(A, phi) * phi
                            - 1 - 2 * b2s.subs(B, 1).subs(A, phi)) == 0)
    # rho de la familia: max((1+2s)/phi, 2s) con s = phi/2 + eps
    e = sp.symbols('epsilon', positive=True)
    r1 = (1 + 2 * (phi / 2 + e)) / phi
    r2 = 2 * (phi / 2 + e)
    ok &= check("rho = max((1+2s)/phi, 2s) = phi + 2eps (la cola de m manda: "
                "2s - (1+2s)/phi = 2eps(1-1/phi) >= 0)",
                sp.simplify(r2 - (phi + 2 * e)) == 0
                and sp.simplify(r2 - r1 - 2 * e * (1 - 1 / phi)) == 0)
    ok &= check("phi < T", float(phi) < T)
    ok &= check("ventana no vacia: 1 - phi/2 = 0.1910 < phi - 1 = 0.6180",
                float(1 - phi / 2) < float(phi - 1))
    return ok

# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] la instancia concreta (w = 0.3, eps = 1e-3, radios estrictos)")
    ok = True
    w, eps = 0.3, 1e-3
    A = PHI
    s1, s = PHI / 2 + 2 * eps, PHI / 2 + eps   # estrictos: s1 > s
    R = A + 1.0
    radii = [A, 1.0, s1, s]
    rho = max(sum(radii[i + 1:]) / radii[i] for i in range(3))
    ok &= check(f"rho = {rho:.6f} < T = {T:.6f}", rho < T)
    ok &= check("paredes exactas: s > b2(A,1) (S5; s1 > s tambien), "
                "s1+s > A-w (par), s > 1-w (H_m), s1 <= A-w, 1 <= A-w, "
                "s1 < 1, w < s",
                s > b2(A, 1) and s1 + s > A - w and s > 1 - w
                and s1 <= A - w and 1 <= A - w and s1 < 1 and w < s)
    # testigo: coordenadas explicitas de la corona {A, s1, s} en R
    tA1, tAs, t1s = theta(A, s1, R), theta(A, s, R), theta(s1, s, R)
    F = tA1 + tAs + t1s
    ok &= check(f"corona del testigo: F = {F:.4f} < 2pi (holgura "
                f"{2*math.pi-F:.4f})", F < 2 * math.pi)
    g = (2 * math.pi - F) / 3
    angs = [0.0, tA1 + g, tA1 + 2 * g + t1s]
    rads = [A, s1, s]
    cents = [((R - r) * math.cos(a), (R - r) * math.sin(a))
             for r, a in zip(rads, angs)]
    okg = all(math.dist(cents[i], cents[j]) >= rads[i] + rads[j] - 1e-12
              for i, j in itertools.combinations(range(3), 2))
    ok &= check("colocacion del testigo valida (distancias >= sumas; "
                "m en el agujero de A, 1 <= A - w)", okg)

    # arbol exhaustivo de colocaciones (criterios exactos: par en disco,
    # rigidez S5 para el trio con par diametral, corona suficiente si no)
    def pan_ok(items):
        it = sorted(items, reverse=True)
        if len(it) <= 1:
            return not it or it[0] <= R
        if len(it) == 2:
            return it[0] + it[1] <= R + 1e-12
        if len(it) == 3:
            a, b, c = it
            if a + b >= R - 1e-12:
                # rama bolsillo: valida SOLO con par exactamente diametral
                # (assert del acta: a+b > R estricto seria par infactible)
                assert a + b <= R + 1e-12, "par infactible en la sarten"
                return c <= b2(a, b) + 1e-12
            ths = [theta(a, b, R), theta(a, c, R), theta(b, c, R)]
            return None not in ths and sum(ths) <= 2 * math.pi + 1e-12
        return False

    def hole_ok(cap, items):
        return sum(items) <= cap + 1e-12 if len(items) != 1 \
            else items[0] <= cap + 1e-12

    best = {True: 0, False: 0}
    def rec(k, pan, holes, m_in_pan):
        if k == len(radii):
            n = len(pan) + sum(len(v[1]) for v in holes.values())
            key = m_in_pan if m_in_pan is not None else False
            best[key] = max(best[key], n)
            return
        r = radii[k]
        placed = False
        if pan_ok(pan + [r]):
            nh = {p: (c, list(x)) for p, (c, x) in holes.items()}
            nh[(r, k)] = (r - w, [])
            rec(k + 1, pan + [r], nh,
                True if k == 1 else m_in_pan)
            placed = True
        for p, (cap, xs) in list(holes.items()):
            if r < p[0] and hole_ok(cap, xs + [r]):
                nh = {q: (c2, list(y)) for q, (c2, y) in holes.items()}
                nh[p] = (cap, xs + [r])
                nh[(r, k)] = (r - w, [])
                rec(k + 1, pan, nh,
                    False if k == 1 else m_in_pan)
                placed = True
        if not placed:
            rec(k + 1, pan, holes, m_in_pan)

    rec(0, [], {}, None)
    ok &= check(f"arbol exhaustivo: max aros con m EN LA SARTEN = "
                f"{best[True]} (< 4); con m en agujero = {best[False]}",
                best[True] == 3 and best[False] == 4)
    return ok

# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] la familia: toda la ventana de omega, eps -> 0 (exacto, "
          "radios estrictos)")
    ok = True
    for w in [0.20, 0.30, 0.45, 0.60]:
        for eps in [1e-2, 1e-4, 1e-6]:
            s1, s = PHI / 2 + 2 * eps, PHI / 2 + eps
            rho = max((1 + s1 + s) / PHI, s1 + s)
            paredes = (s > b2(PHI, 1) and s1 + s > PHI - w and s > 1 - w
                       and s1 < 1 and w < s and 1 <= PHI - w)
            F = (theta(PHI, s1, PHI + 1) + theta(PHI, s, PHI + 1)
                 + theta(s1, s, PHI + 1))
            testigo = F < 2 * math.pi
            ok &= check(f"w={w:.2f} eps={eps:g}: bloqueo exacto, testigo "
                        f"valido, rho = {rho:.6f} = phi + 3eps < T",
                        paredes and testigo
                        and abs(rho - PHI - 3 * eps) < 1e-12 and rho < T)
    return ok

# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] la ventana de holgura R = phi + 1 + delta (criterio angular)")
    ok = True
    w = 0.3

    def s_min(delta):
        """s minimo que bloquea angularmente el trio {phi, 1, s} en R."""
        R = PHI + 1 + delta
        c = R - PHI
        tau = c / math.sqrt(PHI * R)
        u = tau - math.sqrt(c - 1)
        return math.inf if u <= 0 else c / (1 + u * u)

    # con delta pequeno el contraejemplo sobrevive (rho < T)
    for delta in [0.005, 0.01, 0.02]:
        s = max(s_min(delta), 1 - w) + 1e-3
        rho = max(2 * s, (1 + 2 * s) / PHI)
        R = PHI + 1 + delta
        F = 2 * theta(PHI, s, R) + theta(s, s, R)
        bloquea = (2 * s > PHI - w and s > 1 - w and s < 1)
        ok &= check(f"delta={delta:.3f}: s = {s:.4f}, rho = {rho:.4f} < T, "
                    f"testigo ok (bloqueo angular, no S5: evidencia)",
                    bloquea and F < 2 * math.pi and rho < T)
    # el borde de la ventana: 2*s_min(delta*) = T; delta* > 0.02 (la
    # familia sub-T NO es de medida nula en delta)
    lo, hi = 0.0, 0.2
    for _ in range(80):
        mid = (lo + hi) / 2
        if 2 * s_min(mid) < T:
            lo = mid
        else:
            hi = mid
    ok &= check(f"borde de la ventana de holgura: delta* = {lo:.4f} "
                f"(2 s_min = T); delta* > 0.02", lo > 0.02)
    return ok

# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] programa de la Batalla 2 (par, un ocupante): minimo -> phi")
    ok = True
    # min sobre A de max(2*max(b2(A,1), 1-w), (1+2*max(...))/A): la nueva
    # conjetura dice que el umbral geometrico es exactamente phi
    for w in [0.25, 0.40, 0.55]:
        best = math.inf
        for i in range(2000):
            A = 1.0 + w + (2.5 - w) * i / 1999
            s = max(b2(A, 1.0), 1 - w)
            if 2 * s <= A - w:      # el par cabria en el agujero
                continue
            r = max(2 * s, (1 + 2 * s) / A)
            best = min(best, r)
        ok &= check(f"w={w:.2f}: min del programa = {best:.6f} vs phi = "
                    f"{PHI:.6f} (dif {best - PHI:+.1e})",
                    abs(best - PHI) < 2e-3)
    # fuera de la ventana: el minimo sube (H_m manda)
    for w in [0.10, 0.15]:
        best = math.inf
        for i in range(2000):
            A = 1.0 + w + (2.5 - w) * i / 1999
            s = max(b2(A, 1.0), 1 - w)
            if 2 * s <= A - w:
                continue
            best = min(best, max(2 * s, (1 + 2 * s) / A))
        ok &= check(f"w={w:.2f} (fuera de la ventana): min = {best:.4f} "
                    f"> phi", best > PHI + 1e-6)
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
