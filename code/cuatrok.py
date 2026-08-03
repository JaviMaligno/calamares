"""rho*_k = rho*_3 (docs/drafts/cuatro.md): ningun tamano de perfil baja el umbral.

Proposicion 8: para todo omega en (0,1) y todo k >= 3,

    rho*_k(omega) = rho*_3(omega) = max(1, min(2(1-w), max(phi, 2/(1+2w)))).

Prueba puramente aditiva (arbol general, aportado por la verificacion
adversaria; corrige el cierre ilegitimo por el Corolario 2, que solo cubre
perfiles con todos los aros en banda):
  0. Sigma > 1 (fila en A falla): cubre w >= 1/2. Sea w < 1/2 y rho < 2 beta.
  1. s1 <= beta (dos aros > beta o "s1->A solo, resto->B fila" dan Sigma > 2beta).
  2. "s1->B, resto->A fila" falla => Q = Sigma - s1 > 1 => rho >= max(1+s1, 1/s1):
     cierra w >= (sqrt5-2)/2; si no, rho < 2/(1+2w) fuerza s1 > 1/2 + w.
  3. p := #{i: s_i > s1 - w} <= 3 (todos ellos > 1/2 y Sigma < 2).
     p >= 3: {s1,s2,s3} ya es no reinsertable (pares > 1, nadie anida) =>
             rho >= rho_needed(prefijo) >= rho*_3.
     p = 2:  fila {s3..sk} en el agujero de s1 (+ s1->A, s2->B) falla =>
             R = Sigma_{i>=3} > s1 - w => Q = s2 + R > max(1, 2(s1-w)):
             el caso (iv) de perfil_tres => rho >= I_2(w) >= rho*_3.
     p = 1:  s2 en s1, s1->B, resto->A falla => R' = Sigma_{i>=3} > 1 =>
             rho >= max(1+2s2+w, 1/s2) >= ((1+w)+sqrt((1+w)^2+8))/2 >= 2. Contra.
  (<=) es el argumento del polvo de perfil_tres.

El arbol original de k=4 (A/B1/B2/B3, docs/drafts/cuatro.md par. 3) se conserva
y se valida tambien; B2 <-> p=2 es la unica rama que muerde.

Corolario 5: omega_c = omega_T = 1/T - 1/2 exacto (ya sin el Corolario 2).

Bloques: [A] identidades y dominaciones simbolicas, [B] busqueda adversaria
(nada bloqueado por debajo de rho*_3), [C] validacion mecanica de los DOS
arboles con muestreadores por rama, [D] familias de polvo que alcanzan rho*_3
en cada tramo, [E] barrido k = 5 y 6.
"""
import math
import random
import itertools

TWO_PI = 2 * math.pi
PHI = (1 + math.sqrt(5)) / 2
TRIB = 1.839286755214161


def rho3(w):
    return max(1.0, min(2 * (1 - w), max(PHI, 2 / (1 + 2 * w))))


def rho_needed(S):
    S = sorted(S, reverse=True)
    r = sum(S)
    for j in range(len(S)):
        tail = sum(S[j + 1:])
        if tail > 0:
            r = max(r, tail / S[j])
    return r


# ---------------- oraculo generoso de reinsercion ----------------

def theta(a, b, R):
    p = (a / (R - a)) * (b / (R - b))
    if p >= 1.0:
        return math.pi if p <= 1 + 1e-12 else math.inf
    return 2 * math.asin(math.sqrt(p))


def feas3(a, b, c, R):
    if a + b > R or a + c > R or b + c > R:
        return False
    return theta(a, b, R) + theta(a, c, R) + theta(b, c, R) <= TWO_PI + 1e-12


def group_fits(group, cap):
    """Certificados de colocacion para un grupo de hermanos en capacidad cap:
    fila (suficiente, todo m), suma exacta (m<=2), angular (m=3). Para m >= 4
    solo la fila: el oraculo es CONSERVADOR (bloqueante) en grupos grandes.
    Ese es el sesgo seguro para la busqueda [B]: sobredeclarar bloqueos solo
    puede crear falsos candidatos por debajo de rho*_3 — y no aparece ninguno.
    Para [D] el sesgo importa al reves, pero ninguna familia de polvo depende
    de grupos de >= 4 hermanos (los pares ya fallan; confirmado ademas por el
    oraculo permisivo independiente de la verificacion adversaria)."""
    g = sorted(group, reverse=True)
    if not g:
        return True
    if sum(g) <= cap:
        return True
    if len(g) == 1:
        return g[0] <= cap
    if len(g) == 2:
        return g[0] + g[1] <= cap
    if len(g) == 3:
        return feas3(g[0], g[1], g[2], cap)
    return False


def reinsertable(S, w):
    """Oraculo: todos los bosques de anidamiento (x en y sii x <= y - w, agujeros
    con contenido multiple via group_fits) y todos los repartos A/B del nivel
    superior. Cuanto mas generoso, menos bloqueados: sesgo seguro para [B]."""
    beta = 1 - w
    n = len(S)
    opciones = [[-1] + [j for j in range(n) if j != i] for i in range(n)]
    for parents in itertools.product(*opciones):
        ok = True
        for i, p in enumerate(parents):
            if p != -1 and not (S[i] <= S[p] - w + 1e-15):
                ok = False
                break
        if not ok:
            continue
        holes = {}
        for i, p in enumerate(parents):
            if p != -1:
                holes.setdefault(p, []).append(S[i])
        if any(not group_fits(cont, S[p] - w) for p, cont in holes.items()):
            continue
        top = [S[i] for i, p in enumerate(parents) if p == -1]
        m = len(top)
        for mask in range(1 << m):
            GA = [top[i] for i in range(m) if mask >> i & 1]
            GB = [top[i] for i in range(m) if not mask >> i & 1]
            if group_fits(GA, 1.0) and group_fits(GB, beta):
                return True
    return False


def check(label, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {label}")
    return ok


# ---------------- [A] identidades y dominaciones ----------------

def bloque_A():
    import sympy as sp
    w, s, q = sp.symbols('omega s q', positive=True)
    ok = True
    # A1: dominacion de B1 sobre el caso (iv): 3(s-w) >= 2(s-w) y
    #     3/(1+3w) > 2/(1+2w) para todo w > 0.
    ok &= check("A1 3/(1+3w) - 2/(1+2w) = 1/((1+3w)(1+2w)) > 0",
                sp.simplify(3 / (1 + 3 * w) - 2 / (1 + 2 * w)
                            - 1 / ((1 + 3 * w) * (1 + 2 * w))) == 0)
    # A2: B3: de s2+s3 > 1 y s2+s4 > 1 sale Sigma > 2 + (s1 - s2) >= 2:
    #     identidad s1 + s2 + (1-s2) + (1-s2) = 2 + s1 - s2.
    s1, s2 = sp.symbols('s1 s2', positive=True)
    ok &= check("A2 s1 + s2 + 2(1-s2) = 2 + (s1 - s2)",
                sp.simplify(s1 + s2 + 2 * (1 - s2) - (2 + s1 - s2)) == 0)
    # A3: el minimo aureo de la rama Q=1: min max(1+s, 1/s) = phi en s = 1/phi.
    ok &= check("A3 1 + 1/phi = phi (punto fijo del maximo)",
                sp.simplify(1 + 2 / (1 + sp.sqrt(5)) - (1 + sp.sqrt(5)) / 2) == 0)
    # A4: cruce de la hiperbola del caso (iv) con T: omega_T = 1/T - 1/2 y
    #     ademas omega_T = T^2 - T - 3/2 MODULO la cubica de Tribonacci
    #     t^3 = t^2 + t + 1 (el contenido especifico de T, no solo algebra).
    T = sp.symbols('T', positive=True)
    ok &= check("A4a 2/(1+2(1/T-1/2)) = T (identidad directa)",
                sp.simplify(2 / (1 + 2 * (1 / T - sp.Rational(1, 2))) - T) == 0)
    dif = sp.together((1 / T - sp.Rational(1, 2)) - (T ** 2 - T - sp.Rational(3, 2)))
    ok &= check("A4b omega_T = T^2 - T - 3/2 modulo T^3 - T^2 - T - 1",
                sp.rem(sp.expand(sp.numer(dif)), T ** 3 - T ** 2 - T - 1, T) == 0)
    # A4c: minimo de la rama p=1 del arbol general:
    #      min_s max(1+2s+w, 1/s) = ((1+w)+sqrt((1+w)^2+8))/2 >= 2 para w >= 0.
    s_ = sp.symbols('s', positive=True)
    w_ = sp.symbols('w', nonnegative=True)
    s_cross = sp.solve(sp.Eq(1 + 2 * s_ + w_, 1 / s_), s_)
    s_pos = [sol for sol in s_cross if sol.subs(w_, 0) > 0][0]
    M = sp.simplify(1 / s_pos)
    ok &= check("A4c min max(1+2s+w, 1/s) = ((1+w)+sqrt((1+w)^2+8))/2",
                sp.simplify(M - ((1 + w_) + sp.sqrt((1 + w_) ** 2 + 8)) / 2) == 0
                and sp.simplify(M.subs(w_, 0) - 2) == 0)
    # A5: rho*_3 en el tramo de la hiperbola supera a phi sii w < (sqrt5-2)/2
    #     (el cruce de perfil_tres), y 2(1-w) > 2/(1+2w) sii w(1-2w) > 0.
    ok &= check("A5 2(1-w)(1+2w) - 2 = 2w(1-2w)",
                sp.simplify(2 * (1 - w) * (1 + 2 * w) - 2 - 2 * w * (1 - 2 * w)) == 0)
    return ok


# ---------------- [B] busqueda adversaria ----------------

def muestras(w, rnd, n_total):
    """Muestreo dirigido a las familias criticas (CON polvo) + aleatorio."""
    beta = 1 - w
    for _ in range(n_total):
        kind = rnd.random()
        if kind < 0.25:      # caso (iv) + polvo
            s1 = 0.5 + w + rnd.uniform(-0.03, 0.06)
            s2 = 0.5 + rnd.uniform(0, 0.05)
            s3 = 0.5 + rnd.uniform(0, 0.03)
            s4 = rnd.choice((rnd.uniform(1e-4, 0.05), rnd.uniform(0.05, 0.5)))
        elif kind < 0.45:    # caso (i) + polvo (gemelos en max(beta, 1/2))
            base = max(beta, 0.5)
            s1 = base + rnd.uniform(0, 0.02)
            s2 = base + rnd.uniform(0, 0.02)
            s3 = rnd.uniform(1e-3, 0.3)
            s4 = rnd.uniform(1e-4, s3)
        elif kind < 0.6:     # meseta
            s1 = 1 / PHI + rnd.uniform(-0.03, 0.03)
            s2 = 0.5 + rnd.uniform(0, 0.04)
            s3 = 0.5 + rnd.uniform(0, 0.02)
            s4 = rnd.uniform(1e-4, 0.1)
        elif kind < 0.8:     # cuatro en banda (anti-B1)
            base = rnd.uniform(0.3, 0.6)
            s1 = base + w + rnd.uniform(0, 0.05)
            s2 = base + rnd.uniform(0, 0.04)
            s3 = base + rnd.uniform(0, 0.02)
            s4 = base + rnd.uniform(0, 0.01)
        else:                # aleatorio
            s1, s2, s3, s4 = (rnd.uniform(0.02, 0.999) for _ in range(4))
        S = sorted((min(max(x, 1e-4), 0.999) for x in (s1, s2, s3, s4)),
                   reverse=True)
        yield S


def bloque_B():
    ok = True
    print("     w        rho3      min bloqueado   margen")
    peor = math.inf
    for w in (0.02, 0.0437, 0.05, 0.08, 0.10, 0.118, 0.15, 0.19, 0.25,
              0.35, 0.45, 0.55, 0.7):
        rnd = random.Random(12345)
        r3 = rho3(w)
        best = None
        for S in muestras(w, rnd, 30000):
            r = rho_needed(S)
            if r >= r3 + 0.08 or (best is not None and r >= best):
                continue
            if not reinsertable(S, w):
                best = r
        margen = (best - r3) if best is not None else math.nan
        peor = min(peor, margen if best is not None else math.inf)
        print(f"     {w:<8} {r3:.6f}  "
              + (f"{best:.6f}      {margen:+.2e}" if best is not None
                 else "(nada bajo rho3+0.08)"))
    ok &= check(f"B  ningun bloqueo por debajo de rho*_3 (peor margen {peor:+.2e})",
                peor > -1e-9)
    return ok


# ---------------- [C] validacion mecanica del arbol ----------------

def clasifica_k4(S, w):
    """Arbol original k=4: (rama, ok). Clasificacion por GEOMETRIA (no por rho):
    las condiciones forzadas de cada rama valen incondicionalmente (los
    certificados de colocacion fallidos no dependen de rho), asi que tambien
    se ejercitan las ramas que el arbol cierra por contradiccion con
    rho < 2beta (alli se comprueba que, en efecto, la cota fuerza rho >= 2beta
    o >= 2)."""
    s1, s2, s3, s4 = S
    beta = 1 - w
    Sig = sum(S)
    r3 = rho3(w)
    if w >= 0.5:
        return ('w>=1/2', Sig > 1 - 1e-12)
    if s2 > beta:                       # contra: Sigma > 2beta
        return ('dos>beta', Sig > 2 * beta - 1e-12)
    if s1 > beta:                       # contra: Sigma - s1 > beta
        return ('paso2', Sig - s1 > beta - 1e-12 and Sig > 2 * beta - 1e-12)
    q3 = s2 + s3 + s4
    if s4 > s1 - w:
        return ('B1', q3 > 1 - 1e-12 and q3 > 3 * (s1 - w) - 1e-12
                and max(s1 + q3, q3 / s1) >= min(r3, 2 * beta) - 1e-9)
    if s3 > s1 - w:
        q2 = s2 + s3
        return ('B2', q2 > 1 - 1e-12 and q2 > 2 * (s1 - w) - 1e-12
                and max(s1 + q2, q2 / s1) >= min(r3, 2 * beta) - 1e-9)
    return ('B3', s4 > s2 - w - 1e-12 and s2 + s3 > 1 - 1e-12
            and s2 + s4 > 1 - 1e-12 and Sig > 2 - 1e-12)


def clasifica_general(S, w):
    """Arbol general (todo k): (rama, ok). Geometria primero, como arriba."""
    beta = 1 - w
    s1, s2 = S[0], S[1]
    Sig = sum(S)
    rho = rho_needed(S)
    r3 = rho3(w)
    if w >= 0.5:
        return ('g:w>=1/2', Sig > 1 - 1e-12)
    if s1 > beta:                       # paso 1: contra via Sigma > 2beta
        return ('g:paso1', Sig > 2 * beta - 1e-12)
    Q = Sig - s1
    if Q <= 1 - 1e-12:
        return ('g:paso2', False)           # Q > 1 es forzado: fallo si no
    if w >= (math.sqrt(5) - 2) / 2:
        return ('g:meseta+', max(1 + s1, 1 / s1) >= r3 - 1e-9
                or rho >= r3 - 1e-9)
    p = sum(1 for x in S if x > s1 - w)
    if p >= 3:
        if s1 - w > 0.5:
            # la rama del arbol propiamente dicha (bajo rho < rho*_3 se llega
            # aqui con s1 - w > 1/2): prefijo bloqueado
            pref = rho_needed(S[:3])
            return ('g:p>=3', S[2] > 0.5 and pref >= min(r3, 2 * beta) - 1e-9
                    and rho >= pref - 1e-12)
        # s1 - w <= 1/2 solo es alcanzable con rho >= rho*_3 (el arbol lo
        # excluye bajo rho < rho*_3 via s1 > 1/2 + w): comprobarlo
        return ('g:p>=3-bajo', rho >= r3 - 1e-9)
    if p == 2:
        R = sum(S[2:])
        Qq = s2 + R
        return ('g:p=2', R > s1 - w - 1e-12
                and Qq > max(1, 2 * (s1 - w)) - 1e-12
                and max(s1 + Qq, Qq / s1) >= min(r3, 2 * beta) - 1e-9)
    Rp = sum(S[2:])
    # forzados: R' > 1; y la cota rho >= max(1+2 s2+w, R'/s2) >= 2 (contra)
    return ('g:p=1', Rp > 1 - 1e-12
            and max(Sig, Rp / s2) >= 2 - 1e-9
            and Sig > 1 + 2 * s2 + w - 1e-12)


def muestras_rama(w, rnd, n):
    """Muestreadores dedicados a las ramas que el muestreo global no visita."""
    beta = 1 - w
    for _ in range(n):
        kind = rnd.random()
        if kind < 0.25:      # paso 1 / A: s1 > beta
            s1 = beta + rnd.uniform(1e-4, min(0.999 - beta, 0.04))
            s2 = rnd.uniform(0.3, min(beta, 0.7))
            s3 = rnd.uniform(0.25, s2)
            s4 = rnd.uniform(0.2, s3)
        elif kind < 0.5:     # B1: cuatro en banda estrecha
            base = rnd.uniform(0.34, 0.52)
            s1 = min(base + rnd.uniform(0, w), beta)
            s2 = base + rnd.uniform(0, 0.02)
            s3 = base + rnd.uniform(0, 0.015)
            s4 = base + rnd.uniform(0, 0.01)
        elif kind < 0.75:    # B3: s3, s4 <= s1 - w con pares grandes
            s1 = rnd.uniform(0.8, min(beta, 0.98))
            s2 = rnd.uniform(0.6, s1)
            s3 = rnd.uniform(max(1 - s2 + 1e-3, 0.2), max(s1 - w, 0.21))
            s4 = rnd.uniform(max(s2 - w + 1e-4, 0.1), s3)
        else:                # p=1: s2 <= s1 - w y cola gorda
            s1 = rnd.uniform(0.6, min(beta, 0.95))
            s2 = rnd.uniform(0.3, max(s1 - w, 0.31))
            s3 = rnd.uniform(0.35, 0.6)
            s4 = rnd.uniform(0.35, s3)
        S = sorted((min(max(x, 1e-4), 0.999) for x in (s1, s2, s3, s4)),
                   reverse=True)
        yield S


def bloque_C():
    ok = True
    fallos, n_block = 0, 0
    ramas4, ramasg = {}, {}
    for w in (0.03, 0.0437, 0.06, 0.10, 0.15, 0.22, 0.30, 0.42, 0.55):
        rnd = random.Random(999)
        r3 = rho3(w)
        cands = list(muestras(w, rnd, 8000)) + list(muestras_rama(w, rnd, 8000))
        for S in cands:
            if rho_needed(S) >= 3.0:
                continue
            if reinsertable(S, w):
                continue
            n_block += 1
            rama, cond = clasifica_k4(S, w)
            ramas4[rama] = ramas4.get(rama, 0) + 1
            if not cond:
                fallos += 1
            rama, cond = clasifica_general(S, w)
            ramasg[rama] = ramasg.get(rama, 0) + 1
            if not cond:
                fallos += 1
    print(f"     bloqueados analizados: {n_block}")
    print(f"     arbol k=4:    {ramas4}")
    print(f"     arbol general: {ramasg}")
    ok &= check(f"C  condiciones forzadas de LOS DOS arboles y cotas >= rho*_3 "
                f"({fallos} fallos)", fallos == 0 and n_block > 500)
    return ok


# ---------------- [D] familias de polvo ----------------

def bloque_D():
    ok = True
    eps, dust = 1e-5, 1e-6
    casos = [
        ("hiperbola w=0.05", 0.05,
         lambda w: [0.5 + w, 0.5 + eps, 0.5 + eps, dust]),
        ("hiperbola w=omega_T", 1 / TRIB - 0.5,
         lambda w: [0.5 + w, 0.5 + eps, 0.5 + eps, dust]),
        ("meseta w=0.15", 0.15,
         lambda w: [1 / PHI, 0.5 + eps, 0.5 + eps, dust]),
        ("2(1-w) w=0.25", 0.25,
         lambda w: [1 - w + eps, 1 - w + eps, dust, dust / 2]),
        ("w=0.55", 0.55,
         lambda w: [0.5 + eps, 0.5 + eps, dust, dust / 2]),
    ]
    worst = 0.0
    for nombre, w, fam in casos:
        S = sorted(fam(w), reverse=True)
        blocked = not reinsertable(S, w)
        d = rho_needed(S) - rho3(w)
        worst = max(worst, abs(d))
        okc = blocked and 0 <= d < 1e-3
        ok &= check(f"D  {nombre}: bloqueado={blocked}, rho - rho3 = {d:+.1e}", okc)
    # el cruce con T en omega_T (Corolario 5): rho*_4(w_T) = rho*_3(w_T) = T
    wT = 1 / TRIB - 0.5
    ok &= check(f"D  omega_T = 1/T - 1/2 = {wT:.9f} y rho*_3(w_T) = T "
                f"(err {abs(rho3(wT) - TRIB):.1e})", abs(rho3(wT) - TRIB) < 1e-12)
    return ok


def muestras_k(w, rnd, n, k):
    """Muestreo k-aros: familias criticas con polvo multiple + aleatorio."""
    beta = 1 - w
    for _ in range(n):
        kind = rnd.random()
        if kind < 0.35:      # caso (iv) + k-3 polvos
            S = [0.5 + w + rnd.uniform(-0.02, 0.04), 0.5 + rnd.uniform(0, 0.04),
                 0.5 + rnd.uniform(0, 0.02)]
            S += [rnd.uniform(1e-4, 0.08) for _ in range(k - 3)]
        elif kind < 0.55:    # gemelos + polvos
            base = max(beta, 0.5)
            S = [base + rnd.uniform(0, 0.02), base + rnd.uniform(0, 0.02)]
            S += [rnd.uniform(1e-4, 0.2) for _ in range(k - 2)]
        elif kind < 0.75:    # p=2 con cola repartida (anti arbol general)
            s1 = 0.5 + w + rnd.uniform(0, 0.05)
            s2 = 0.5 + rnd.uniform(0, 0.04)
            resto = [rnd.uniform(0.05, max(s1 - w, 0.06)) for _ in range(k - 2)]
            S = [s1, s2] + resto
        else:
            S = [rnd.uniform(0.02, 0.999) for _ in range(k)]
        yield sorted((min(max(x, 1e-4), 0.999) for x in S), reverse=True)


def bloque_E():
    ok = True
    peor = math.inf
    for k, ws, n in ((5, (0.02, 0.0437, 0.08, 0.15, 0.30, 0.55), 2500),
                     (6, (0.0437, 0.10, 0.25), 700)):
        for w in ws:
            rnd = random.Random(777)
            r3 = rho3(w)
            best = None
            for S in muestras_k(w, rnd, n, k):
                r = rho_needed(S)
                if r >= r3 + 0.06 or (best is not None and r >= best):
                    continue
                if not reinsertable(S, w):
                    best = r
            margen = (best - r3) if best is not None else math.inf
            peor = min(peor, margen)
            print(f"     k={k} w={w:<7} rho3={r3:.6f}  "
                  + (f"min bloqueado={best:.6f}  margen={margen:+.2e}"
                     if best is not None else "(nada bajo rho3+0.06)"))
    ok &= check(f"E  k = 5 y 6: nada bloqueado bajo rho*_3 (peor margen {peor:+.2e})",
                peor > -1e-9)
    return ok


if __name__ == "__main__":
    print(f"phi = {PHI:.6f}  T = {TRIB:.6f}  omega_T = {1 / TRIB - 0.5:.9f}\n")
    res = []
    print("[A] identidades y dominaciones (sympy)")
    res.append(bloque_A())
    print("\n[B] busqueda adversaria (oraculo conservador en grupos >= 4)")
    res.append(bloque_B())
    print("\n[C] validacion mecanica de los dos arboles")
    res.append(bloque_C())
    print("\n[D] familias de polvo por tramo y Corolario 5")
    res.append(bloque_D())
    print("\n[E] barrido k = 5 y k = 6")
    res.append(bloque_E())
    print(f"\nRESULTADO: {sum(res)}/{len(res)} bloques OK"
          + ("" if all(res) else "  <-- REVISAR"))

    import sys
    sys.exit(0 if all(res) else 1)
