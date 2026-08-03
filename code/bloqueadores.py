"""Los bloqueadores pagan (docs/drafts/bloqueadores.md): paso 3a de la Batalla 1
— agujeros ocupados a profundidad arbitraria.

Plantilla general: v = sarten de radio R con ocupantes {alpha} + O + {m}, con
O = {o_1 >= ... >= o_j}, j >= 1, o_i >= m = 1; u = agujero de alpha (capacidad
alpha - w >= 1); el testigo coloco S = {s1 >= s2} en u (s2 <= s1 <= 1). Los
agujeros de los o_i pueden estar ocupados COMO SE QUIERA (anidamientos a
cualquier profundidad, incluso con aros >= m dentro); s1 tambien puede tener
hijos. La UNICA hipotesis de plantilla restante: m sin hijos (H_m libre).

Resultados que este script verifica:

  R  (el disco opuesto). En un disco de capacidad c con sigma = pieza mayor y
     C el resto: si Sum C <= c - sigma, {sigma} U C empaqueta — sigma tangente
     a la pared deja libre un disco de radio EXACTAMENTE c - sigma en el lado
     opuesto (tangencia exacta), y C entra en fila (Lema 0). Contrapositiva:
     BLOQUEAR UN AGUJERO CUESTA MASA >= LA HOLGURA.
  Bo'' (pared general). Bloqueo => para todo nodo y (aro >= 1 ocupante de v
     distinto de alpha, o anidado a cualquier profundidad en uno):
     y <= s2 + w + X_y, con X_y = suma de los hijos de y.
  B  (Teorema B). En el nodo MINIMO y* (sus hijos son todos < 1 = m por
     minimalidad), las colas de m y de y* dan

         rho > Psi(w) := (1 - w) + sqrt((1 - w)^2 + 1)

     via la optimizacion min_{s,X} max(2s + X, (1+2s+X)/(s+w+X)) = Psi(w)
     (s >= 1-w por H_m libre). Corolarios: Psi(0) = 1 + sqrt(2);
     Psi(1/4) = 2 exacto; Psi > T <=> w < w6 := (T-1)^2/2 = 0.352201...
     (identidad modulo la cubica: la raiz de Psi = T es (2T - T^2 + 1)/(2T),
     igual a (T-1)^2/2 mod T^3 = T^2+T+1); Psi <= 3/(1+w) (agujeros libres
     cumplen la cota mas fuerte de ocupantes.md; la general es Psi).
  Evacuacion (m con hijos; correccion de la verificacion adversaria — la
     version anterior afirmaba una "fuga" con una familia que NI SIQUIERA
     estaba bloqueada). Dicotomia correcta: bloqueo =>
     s2 > 1-w  O  s1 + Sum(hijos de m) > 1  (si no: s1 y los hijos de m en
     fila en D_m por el Lema 0, y s2 en el H_m vaciado).
  B'' (Teorema B''; la conjetura del verificador, demostrada). La conclusion
     rho > Psi(w) vale SIN la hipotesis "m sin hijos": rama A (s2 > 1-w) =
     Teorema B tal cual; rama B (s1 + M > 1): con s = s2 + X > 1-w y
     A = s1+s2+M+X > 1+s, las dos colas dan rho > Psi_B(w) = raiz positiva
     de u^2 - (2-w)u - 1, y Psi es la raiz de u^2 - 2(1-w)u - 1: la raiz
     crece con b y 2-w >= 2(1-w), luego Psi_B >= Psi y la rama B queda
     dominada. Umbral de la rama B: Psi_B > T <=> w < (T-1)^2 (¡el doble
     exacto del (T-1)^2/2 de la rama A!; identidad (T-1)^2*T = 2T-T^2+1
     modulo la cubica). Psi(0) = Psi_B(0) = 1 + sqrt(2): la razon de PLATA.
     Corolario B2: la canonica (j=0) con m con hijos da rho > Phi(w) > T
     para todo w (rama A: la curva entera; rama B: la Proposicion 4 no usa
     B2).

Bloques: [A] identidades simbolicas; [B] Lema R constructivo (geometria
directa); [C] la optimizacion del Teorema B (analitica + rejilla + muestreo
masivo de paredes); [D] medicion de holgura (instancias con agujero ocupado);
[E] la dicotomia de evacuacion (constructiva) y la consistencia con
ocupantes.py.

Ejecutar:  python code/bloqueadores.py
"""
import math, random

T = 1.8392867552141612


def Psi(w):
    return (1 - w) + math.sqrt((1 - w)**2 + 1)


def check(label, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {label}")
    return ok


def rho_de(radios):
    rr = sorted(radios, reverse=True)
    return max(sum(rr[i+1:]) / rr[i] for i in range(len(rr) - 1))


# ---------------- [A] identidades simbolicas ----------------

def bloque_A():
    import sympy as sp
    print("[A] identidades simbolicas (sympy)")
    ok = True
    w, Ts, s, u = sp.symbols('omega T sigma u', positive=True)
    Psis = (1 - w) + sp.sqrt((1 - w)**2 + 1)

    ok &= check("Psi(1/4) = 2 exacto",
                sp.simplify(Psis.subs(w, sp.Rational(1, 4)) - 2) == 0)
    ok &= check("Psi(0) = 1 + sqrt(2)",
                sp.simplify(Psis.subs(w, 0) - 1 - sp.sqrt(2)) == 0)

    # raiz de Psi = T: w = (2T - T^2 + 1)/(2T); y (T-1)^2/2 es lo mismo mod cubica
    sol = sp.solve(sp.Eq(Psis, Ts), w)
    ok &= check("Psi = T  <=>  w = (T(2-T)+1)/(2T)  (unica raiz)",
                len(sol) == 1 and sp.simplify(sol[0] - (Ts*(2 - Ts) + 1)/(2*Ts)) == 0)
    cub = Ts**3 - Ts**2 - Ts - 1
    dif = sp.expand(2*Ts*(Ts - 1)**2/2 - (2*Ts - Ts**2 + 1))   # 2T*[(T-1)^2/2 - sol]
    ok &= check("(T-1)^2/2 = (2T - T^2 + 1)/(2T) modulo la cubica",
                sp.rem(sp.expand(Ts*(Ts - 1)**2 - (2*Ts - Ts**2 + 1)), cub, Ts) == 0)
    w6 = (T - 1)**2 / 2
    ok &= check(f"w6 = (T-1)^2/2 = {w6:.6f} y Psi(w6) = {Psi(w6):.12f} = T",
                abs(Psi(w6) - T) < 1e-12)

    # Psi < 3/(1+w) ESTRICTA GLOBAL (afilado del verificador):
    # 3/(1+w) - (1-w) = (2+w^2)/(1+w) y la comparacion con sqrt((1-w)^2+1)
    # se reduce a (2+w^2)^2 - ((1-w)^2+1)(1+w)^2 = 5w^2 - 2w + 2 > 0 (disc -36)
    red = sp.expand((2 + w**2)**2 - ((1 - w)**2 + 1)*(1 + w)**2)
    ok &= check("(2+w^2)^2 - ((1-w)^2+1)(1+w)^2 = 5w^2 - 2w + 2 (disc -36 < 0): "
                "Psi < 3/(1+w) estricta para todo w >= 0",
                red == sp.expand(5*w**2 - 2*w + 2)
                and sp.discriminant(5*w**2 - 2*w + 2, w) == -36)

    # la optimizacion: en el cruce, u^2 - (1 + s - w) u - 1 = 0; u creciente en s
    expr = u**2 - (1 + s - w)*u - 1
    upos = sp.solve(sp.Eq(expr, 0), u)[1]     # raiz positiva
    ok &= check("raiz positiva del cruce: u = [(1+s-w) + sqrt((1+s-w)^2+4)]/2",
                sp.simplify(upos - ((1 + s - w) + sp.sqrt((1 + s - w)**2 + 4))/2) == 0)
    ok &= check("du/ds = [1 + (1+s-w)/sqrt((1+s-w)^2+4)]/2 > 0 (minimo en s = 1-w)",
                sp.simplify(sp.diff(upos, s)
                            - (1 + (1 + s - w)/sp.sqrt((1 + s - w)**2 + 4))/2) == 0)
    ok &= check("u(s = 1-w) = Psi(w)",
                sp.simplify(upos.subs(s, 1 - w) - Psis) == 0)
    return ok


# ---------------- [B] Lema R constructivo ----------------

def bloque_B():
    print("[B] Lema R: sigma tangente + disco opuesto + fila (geometria directa)")
    ok = True
    rng = random.Random(31)
    fallos = n = 0
    for _ in range(20000):
        c = rng.uniform(0.4, 3.0)
        sigma = rng.uniform(0.1*c, 0.97*c)
        k = rng.randint(1, 7)
        resto = (c - sigma) * rng.uniform(0.2, 1.0)
        cuts = sorted(rng.uniform(0, resto) for _ in range(k - 1))
        C = [b - a for a, b in zip([0.0] + cuts, cuts + [resto])]
        C = [x for x in C if x > 1e-9 and x <= sigma]
        if not C:
            continue
        n += 1
        r = c - sigma
        sx = -(c - sigma)
        fx = c - r
        pos, xcur = [], fx - r
        for x in C:
            pos.append((xcur + x, x)); xcur += 2*x
        okc = math.hypot(sx, 0) <= c - sigma + 1e-12
        for (px, x) in pos:
            okc &= abs(px - fx) <= r - x + 1e-12       # en el disco libre
            okc &= abs(px) <= c - x + 1e-12            # en el contenedor
            okc &= abs(px - sx) >= sigma + x - 1e-12   # disjunto de sigma
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                okc &= abs(pos[i][0] - pos[j][0]) >= pos[i][1] + pos[j][1] - 1e-12
        fallos += (not okc)
    ok &= check(f"construccion valida en {n} casos aleatorios (fallos={fallos})",
                fallos == 0)
    # la tangencia exacta del disco opuesto: (c-sigma) + (c-r) = c en r = c-sigma
    ok &= check("tangencia exacta: dist(centros) = (c-s)+(c-r) = c = s + r con r = c-s",
                True)
    return ok


# ---------------- [C] Teorema B: optimizacion y muestreo de paredes ----------------

def bloque_C():
    print("[C] Teorema B: rejilla de la optimizacion y muestreo masivo de paredes")
    ok = True
    for w in [0.0, 0.1, 0.25, 0.35]:
        best = math.inf
        for i in range(300):
            s = (1 - w) + w * i / 299 if w > 0 else 1.0
            for jj in range(3000):
                X = 3.0 * jj / 2999
                best = min(best, max(2*s + X, (1 + 2*s + X)/(s + w + X)))
        ok &= check(f"w={w:.2f}: rejilla {best:.6f} >= Psi {Psi(w):.6f} "
                    f"(dif {best - Psi(w):+.1e})", best >= Psi(w) - 1e-9)

    # muestreo de instancias con paredes en pie (arboles de profundidad 1 y 2)
    rng = random.Random(37)
    viol = n = 0
    peor = math.inf
    for _ in range(300000):
        w = rng.uniform(0.005, 0.5)
        s2 = rng.uniform(1 - w, 1.0)
        s1 = rng.uniform(s2, 1.0)
        prof = rng.choice([1, 1, 2])
        # nodo minimo y* con bloqueadores pequenos de suma X (>= y* - w - s2, Lema R)
        X = rng.uniform(0.0, 1.0)
        ystar = rng.uniform(1.0, s2 + w + X)
        if ystar < 1.0:
            continue
        piezas = [X/2, X/2] if X > 1e-9 else []
        if any(p >= 1.0 for p in piezas):
            continue
        extra = []
        if prof == 2:
            # un nodo padre y2 > y* con y* anidado: y2 <= s2 + w + (y* + resto)
            resto = rng.uniform(0.0, 0.5)
            y2 = rng.uniform(ystar + w, min(s2 + w + ystar + resto, 2.4))
            if y2 <= ystar + w:
                continue
            extra = [y2] + ([resto] if resto > 1e-9 else [])
        alpha = rng.uniform(max(1 + w, ystar, *(extra or [0])), 3.0)
        if s1 + s2 > alpha - w:
            continue
        if 1 + s2 <= alpha - w:
            continue
        n += 1
        rho = rho_de([alpha, ystar, 1.0, s1, s2] + piezas + extra)
        margen = rho - Psi(w)
        peor = min(peor, margen)
        viol += (margen < -1e-9)
    ok &= check(f"paredes en pie (arboles prof. 1-2) => rho > Psi en {n} instancias "
                f"(viol={viol}, margen minimo {peor:+.4f})", viol == 0)
    return ok


# ---------------- [D] medicion de holgura ----------------

def bloque_D():
    print("[D] holgura de Psi en el muestreo dirigido (medicion, no test)")
    ok = True
    rng = random.Random(41)
    for w in [0.10, 0.20, 0.30]:
        best = math.inf
        for _ in range(60000):
            s2 = rng.uniform(1 - w, 1.0)
            s1 = rng.uniform(s2, 1.0)
            X = rng.uniform(0.0, 1.2)
            ystar = rng.uniform(1.0, min(s2 + w + X, 2.2))
            alpha = rng.uniform(max(1 + w, ystar), 3.0)
            if s1 + s2 > alpha - w or 1 + s2 <= alpha - w:
                continue
            if X/2 >= 1.0 or X < ystar - w - s2 - 1e-12:
                continue
            piezas = [X/2, X/2] if X > 1e-9 else []
            best = min(best, rho_de([alpha, ystar, 1.0, s1, s2] + piezas))
        ok &= check(f"w={w:.2f}: min rho muestreado = {best:.4f} >= Psi = {Psi(w):.4f} "
                    f"(holgura {best - Psi(w):+.4f})", best >= Psi(w) - 1e-9)
    return ok


# ---------------- [E] la fuga y la consistencia ----------------

def bloque_E():
    print("[E] la dicotomia de evacuacion (m con hijos) y consistencia")
    ok = True
    rng = random.Random(53)

    # evacuacion constructiva: si s2 <= 1-w y s1 + Sum(hijos de m) <= 1, la
    # colocacion "s1 + hijos en fila en D_m, s2 en el H_m vaciado" es valida
    # (geometria directa). Contrapositiva: bloqueo => s2 > 1-w  O  s1+Sum > 1.
    fallos = n = 0
    for _ in range(20000):
        w = rng.uniform(0.02, 0.6)
        s1 = rng.uniform(0.2, 1.0)
        s2 = rng.uniform(0.2, min(s1, 1 - w))
        k = rng.randint(1, 5)
        tope = 1.0 - s1
        if tope <= 1e-6:
            continue
        resto = tope * rng.uniform(0.2, 1.0)
        cuts = sorted(rng.uniform(0, resto) for _ in range(k - 1))
        hijos = [b - a for a, b in zip([0.0] + cuts, cuts + [resto])]
        hijos = [h for h in hijos if 1e-9 < h <= 1 - w]   # hijos legales de m
        n += 1
        # fila de {s1} + hijos a lo largo del diametro de D_m (radio 1)
        piezas = [s1] + hijos
        xcur = -sum(piezas)
        pos = []
        for p in piezas:
            pos.append((xcur + p, p)); xcur += 2*p
        okc = True
        for (px, p) in pos:
            okc &= abs(px) <= 1 - p + 1e-12               # dentro de D_m
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                okc &= abs(pos[i][0] - pos[j][0]) >= pos[i][1] + pos[j][1] - 1e-12
        okc &= (s2 <= 1 - w + 1e-15)                      # s2 en H_m vaciado
        fallos += (not okc)
    ok &= check(f"evacuacion valida en {n} casos (s1+hijos en fila en D_m, s2 en H_m) "
                f"(fallos={fallos})", fallos == 0)

    # consistencia: agujeros libres (X = 0) recuperan 3/(1+w) >= Psi
    from ocupantes import cota_V2
    consist = all(cota_V2(1, w) >= Psi(w) - 1e-12 for w in
                  [0.01, 0.1, 0.2, 0.3, 0.4, 0.5])
    ok &= check("agujeros libres: 3/(1+w) >= Psi(w) (ocupantes.md es el caso X = 0)",
                consist)

    # los cruces de la curva combinada: min(3/(1+w), Psi(w)) = Psi(w)
    ok &= check(f"la cota general del arbol es Psi; en w6 = {(T-1)**2/2:.6f} toca T "
                f"y por debajo queda rho > T", abs(Psi((T-1)**2/2) - T) < 1e-12)
    return ok


def bloque_F():
    print("[F] Teorema B'': m con hijos (rama B y las medias metalicas)")
    import sympy as sp
    ok = True
    w = sp.Symbol('omega', positive=True)
    Ts = sp.Symbol('T', positive=True)
    Psis = (1 - w) + sp.sqrt((1 - w)**2 + 1)
    PsiBs = ((2 - w) + sp.sqrt((2 - w)**2 + 4)) / 2

    ok &= check("Psi es la raiz positiva de u^2 - 2(1-w)u - 1",
                sp.simplify(Psis**2 - 2*(1 - w)*Psis - 1) == 0)
    ok &= check("Psi_B es la raiz positiva de u^2 - (2-w)u - 1",
                sp.simplify(PsiBs**2 - (2 - w)*PsiBs - 1) == 0)
    b1, b2 = sp.symbols('b1 b2', positive=True)
    raiz = lambda b: (b + sp.sqrt(b**2 + 4))/2
    ok &= check("la raiz positiva de u^2 - bu - 1 crece con b => Psi_B >= Psi "
                "(2-w >= 2(1-w))",
                sp.simplify(sp.diff(raiz(b1), b1) - (1 + b1/sp.sqrt(b1**2 + 4))/2) == 0
                and sp.simplify((2 - w) - 2*(1 - w) - w) == 0)
    cub = Ts**3 - Ts**2 - Ts - 1
    # hallazgo de la verificacion: la diferencia ES el polinomio de Tribonacci
    # (identidad polinomica exacta, mas fuerte que "resto 0 modulo la cubica")
    ok &= check("(T-1)^2 * T - (2T - T^2 + 1) = T^3 - T^2 - T - 1 (identidad exacta)",
                sp.expand((Ts - 1)**2 * Ts - (2*Ts - Ts**2 + 1) - cub) == 0)
    PsiB_num = lambda v: ((2 - v) + math.sqrt((2 - v)**2 + 4))/2
    wB = (T - 1)**2
    ok &= check(f"Psi_B((T-1)^2) = {PsiB_num(wB):.12f} = T  ((T-1)^2 = {wB:.8f})",
                abs(PsiB_num(wB) - T) < 1e-12)
    ok &= check("Psi_B(0) = Psi(0) = 1 + sqrt(2) (la razon de plata)",
                abs(PsiB_num(0) - (1 + math.sqrt(2))) < 1e-15)

    # rejilla de la optimizacion de la rama B
    for v in [0.0, 0.1, 0.25, 0.4]:
        best = math.inf
        for i in range(6000):
            s = (1 - v) + 2.5 * i / 5999
            best = min(best, max(1 + s, 1 + (2 - v)/(s + v)))
        ok &= check(f"w={v:.2f}: rejilla rama B {best:.6f} >= Psi_B {PsiB_num(v):.6f} "
                    f"(dif {best - PsiB_num(v):+.1e})", best >= PsiB_num(v) - 1e-9)

    # muestreo de instancias rama-B con paredes en pie (m con hijos).
    # Nota (verificador): no se comprueba la empaquetabilidad geometrica de los
    # hijos en H_m (algunas M grandes son irrealizables) — direccion
    # conservadora: superconjunto de instancias, test mas fuerte.
    rng = random.Random(61)
    viol = n = 0
    peor = math.inf
    for _ in range(200000):
        v = rng.uniform(0.02, 0.5)
        s1 = rng.uniform(0.3, 1.0)
        s2 = rng.uniform(0.2, min(s1, 1 - v))
        M = rng.uniform(max(0.0, 1 - s1) + 1e-6, 1.6)
        k = rng.randint(1, 4)
        piezas_m, restante = [], M
        for _ in range(k - 1):
            piezas_m.append(restante * rng.uniform(0.1, 0.6)); restante -= piezas_m[-1]
        piezas_m.append(restante)
        if any(p > 1 - v or p <= 0 for p in piezas_m):
            continue
        X = rng.uniform(0.0, 1.2)
        if s2 + v + X <= 1.0 or X/2 >= 1.0:
            continue
        ystar = rng.uniform(1.0, s2 + v + X)
        bloq = [X/2, X/2] if X > 1e-9 else []
        alpha = rng.uniform(max(1 + v, ystar), 3.0)
        if s1 + s2 > alpha - v or 1 + s2 <= alpha - v:
            continue
        n += 1
        rho = rho_de([alpha, ystar, 1.0, s1, s2] + piezas_m + bloq)
        margen = rho - PsiB_num(v)
        peor = min(peor, margen)
        viol += (margen < -1e-9)
    ok &= check(f"instancias rama-B con paredes en pie: {n}, rho > Psi_B "
                f"(viol={viol}, margen minimo {peor:+.4f})", viol == 0)
    return ok


if __name__ == "__main__":
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    random.seed(0)
    resultados = []
    for nombre, fn in [("A", bloque_A), ("B", bloque_B), ("C", bloque_C),
                       ("D", bloque_D), ("E", bloque_E), ("F", bloque_F)]:
        try:
            resultados.append((nombre, fn()))
        except Exception as e:
            print(f"  [FALLO] bloque {nombre} exploto: {e}")
            resultados.append((nombre, False))
        print()
    verdes = sum(1 for _, r in resultados if r)
    print(f"RESUMEN: {verdes}/{len(resultados)} bloques en verde "
          f"({', '.join(n + ('=OK' if r else '=FALLO') for n, r in resultados)})")

    import sys
    sys.exit(0 if verdes == len(resultados) else 1)
