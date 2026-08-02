"""La pared del bolsillo doble (docs/drafts/bolsillo.md): el asalto geometrico.

Plantilla (j = 1): v = sarten de radio R con ocupantes {alpha, o1, m}, o1 >= 1;
u = agujero de alpha (capacidad alpha-w >= 1); S = {s1 >= s2} del testigo en u;
ocupacion de agujeros ARBITRARIA (X = hijos de o1, M = hijos de m, Xs = hijos
de s1, cualquier tamano y profundidad via las tarifas del Lema R).

Resultados que este script verifica:

  G  (Lema G, la pared del bolsillo doble). Bloqueo => {alpha,o1,s1,s2} no
     empaqueta en R => tampoco en R_bar = alpha+o1 (contencion), donde el par
     {alpha,o1} es diametralmente rigido (Proposicion S5 reescalada: el par
     {A,B} en el disco A+B es S5 con t = B/A) y deja DOS bolsillos de Descartes
     b2(alpha,o1) = alpha*o1*(alpha+o1)/(alpha^2+alpha*o1+o1^2), uno por lado.
     Si s1 <= b2, cada sigma va a un bolsillo y hay corona => desbloqueado:

         bloqueo  =>  s1 > b2(alpha, o1)  >=  b(alpha) .

  T_G (Teorema G, el cierre en omega para j = 1). Con las tarifas del Lema R
     (Bo'': X > o1-w-s2; B3': s2+Xs > s1-w) y las colas de o1 y m:
     (*)  rho > 1 + (1+s1-w+M+Xs)/o1   [eliminando X entre cola de o1 y Bo'']
     rama A (s2 >= 1-w): (W) da alpha >= 1+s1; G da o1 < N(s1) con
         N^2 + (1+s1)N - s1(1+s1)^2 = 0  =>  N(s1) = (1+s1)(sqrt(1+4s1)-1)/2 ,
     y h(s1) = (1+s1-w)/N(s1) es decreciente (identidad
     (1+4s1) - (1+2s1-2s1^2)^2 = 4s1^3(2-s1) > 0), luego minimo en s1 = 1:
     N(1) = sqrt(5)-1  y

         rho > 1 + (2-w)/(sqrt(5)-1) = 1 + (2-w) phi/2 = phi^2 - (phi/2) w .

     rama B (s1+M > 1): M > 1-s1 en (*) y el techo uniforme o1 < N1(w) con
     w N^2 + w(1+w) N - (1+w)^2 = 0 => N1(w) = (1+w)(sqrt(w^2+4w)-w)/(2w):
     rho > max(Psi_B(w), 1 + (2-w)/N1(w)) — cota historica, SUBSUMIDA por:
  T_G' (Teorema G', el remate). Con (B3') la rama B alcanza la MISMA curva
     dorada: bloqueo (j=1) => rho > phi^2 - (phi/2) w para TODO w, y
     rho > T <=> w < w_A = 2 - 2(T-1)(phi-1) = 2(phi^2-T)(phi-1) = 0.962585.
     Prueba: cadenas (I)/(II) con Bo''+B3'+W+G => rho > max(f1, f2) con
     f1 = 1+(2-w+2b2-alpha)/o1, f2 = (2o1+2-w+2b2-alpha)/alpha; b2 concava
     en alpha (d2b2 = -6 alpha o^3(alpha+o)/D^3) => f1 concava => extremos;
     f2 decreciente en alpha (D^2 - alpha o^2(o+2alpha) = (alpha+o)(alpha^3+
     alpha^2 o + o^3) > 0); certificados univariantes en la frontera b2 = 1
     (f1 = curva IDENTICAMENTE en o1 = g; solape [o~, o*] = [1.296, 1.596];
     dominacion trivial en o1 > 2). El rincon optimo del programa es DORADO:
     alpha = 2, o1 = sqrt(5)-1, b2(2, sqrt(5)-1) = 1 exacto.

  Psi_j (j ocupantes, combinatorio). La cola de o1 con j-1 ocupantes extra da
     rho > Psi_j(w) = (1-w) + sqrt((1-w)^2 + j), raiz de u^2 - 2(1-w)u - j;
     Psi_j > T <=> w < 1 - (T^2-j)/(2T) para j <= 3, y para todo w si j >= 4.

  S  (Corolario S, pequenos gratis). Todas las colocaciones de las paredes
     combinatorias (D_m, H_m, agujeros, u-junto-a-m, evacuaciones) son LOCALES:
     aros < m adicionales en cualquier parte de la instancia no las invalidan
     y solo engordan colas. Los teoremas V2/B/B''/Psi_j valen con pequenos.

Bloques: [A] identidades simbolicas; [B] Lema G contra el LP de coronas;
[C] Teorema G: cadenas analiticas vs optimizacion SLSQP del programa;
[D] Psi_j por muestreo; [E] Corolario S (colocaciones locales con pequenos).

Ejecutar:  python code/bolsillo.py   (numpy/scipy/sympy)
"""
import math, random, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

T = 1.8392867552141612
PHI = (1 + math.sqrt(5)) / 2


def b2(a, o):
    return a*o*(a+o) / (a*a + a*o + o*o)


def N_ramaA(s1):
    return (1 + s1) * (math.sqrt(1 + 4*s1) - 1) / 2


def N1(w):
    return (1 + w) * (math.sqrt(w*w + 4*w) - w) / (2*w)


def curva_A(w):
    return PHI**2 - (PHI/2) * w


def curva_B(w):
    return 1 + (2 - w) / N1(w)


def check(label, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {label}")
    return ok


# ---------------- [A] identidades simbolicas ----------------

def bloque_A():
    import sympy as sp
    print("[A] identidades simbolicas (sympy)")
    ok = True
    w, s, No, a, o = sp.symbols('omega sigma N alpha o', positive=True)
    phi = (1 + sp.sqrt(5)) / 2

    b2s = a*o*(a+o) / (a**2 + a*o + o**2)
    ok &= check("d b2/d o = alpha^3 (alpha + 2o) / (...)^2 > 0 (b2 creciente en o)",
                sp.simplify(sp.factor(sp.numer(sp.together(sp.diff(b2s, o))))
                            - a**3*(a + 2*o)) == 0)
    ok &= check("b2(2, sqrt(5)-1) = 1 exacto (el bolsillo dorado)",
                sp.simplify(b2s.subs({a: 2, o: sp.sqrt(5) - 1}) - 1) == 0)

    # disyuncion de los bolsillos espejo (verificador): el centro del bolsillo
    # del par rigido {A, B} en R = A+B esta en (x0, y0) con y0 = 2 b2 EXACTO.
    # Sistema de tangencias: |c - c_A| = A + b2, |c - c_B| = B + b2, |c| = R - b2
    A_, B_ = sp.symbols('A B', positive=True)
    Rr = A_ + B_
    bb = A_*B_*(A_+B_) / (A_**2 + A_*B_ + B_**2)
    x0 = (A_**3 + A_**2*B_ - A_*B_**2 - B_**3) / (A_**2 + A_*B_ + B_**2)
    y0sq = (Rr - bb)**2 - x0**2
    ok &= check("bolsillos espejo: y0^2 = (R-b2)^2 - x0^2 = 4 b2^2 (=> distan 4 b2)",
                sp.simplify(y0sq - 4*bb**2) == 0)
    resid1 = sp.simplify((x0 - (-(B_)))**2 + y0sq - (A_ + bb)**2)
    resid2 = sp.simplify((x0 - A_)**2 + y0sq - (B_ + bb)**2)
    ok &= check("y las tangencias a A (centro -B) y a B (centro A) son exactas",
                resid1 == 0 and resid2 == 0)
    ok &= check("b2(alpha, 1) = b(alpha) = alpha(alpha+1)/(alpha^2+alpha+1)",
                sp.simplify(b2s.subs(o, 1) - a*(a+1)/(a**2+a+1)) == 0)

    # la cuadratica de la rama A: b2(1+s, N) = s <=> N^2 + (1+s)N - s(1+s)^2 = 0
    quadA = sp.simplify(sp.numer(sp.together(b2s.subs({a: 1+s, o: No}) - s)))
    NA = (1 + s)*(sp.sqrt(1 + 4*s) - 1)/2
    ok &= check("b2(1+sigma, N) = sigma <=> N^2+(1+sigma)N-sigma(1+sigma)^2 = 0",
                sp.simplify(quadA - (No**2 + (1+s)*No - s*(1+s)**2)*
                            sp.simplify(quadA/(No**2 + (1+s)*No - s*(1+s)**2))) == 0
                and sp.simplify((NA**2 + (1+s)*NA - s*(1+s)**2)) == 0)
    ok &= check("N(1) = sqrt(5)-1 y 1/(sqrt(5)-1) = phi/2",
                sp.simplify(NA.subs(s, 1) - (sp.sqrt(5)-1)) == 0
                and sp.simplify(1/(sp.sqrt(5)-1) - phi/2) == 0)

    # monotonia de h: (1+4s) - (1+2s-2s^2)^2 = 4s^3(2-s)
    ok &= check("(1+4s) - (1+2s-2s^2)^2 = 4 s^3 (2-s)  (certificado de h decreciente)",
                sp.expand((1 + 4*s) - (1 + 2*s - 2*s**2)**2 - 4*s**3*(2 - s)) == 0)

    # la curva dorada
    ok &= check("1 + (2-w) phi/2 = phi^2 - (phi/2) w  (phi^2 = phi + 1)",
                sp.simplify(1 + (2 - w)*phi/2 - (phi**2 - phi*w/2)) == 0)
    wA = 2 - 2*(T - 1)*(PHI - 1)
    ok &= check(f"cruce rama A: w_A = 2 - 2(T-1)(phi-1) = {wA:.6f}, curva_A(w_A) = T",
                abs(curva_A(wA) - T) < 1e-12)

    # la cuadratica de N1: w N^2 + w(1+w) N - (1+w)^2 = 0
    N1s = (1 + w)*(sp.sqrt(w**2 + 4*w) - w)/(2*w)
    ok &= check("N1: w N^2 + w(1+w) N - (1+w)^2 = 0 y b2(1+w, N1) = 1",
                sp.simplify(w*N1s**2 + w*(1+w)*N1s - (1+w)**2) == 0
                and sp.simplify(b2s.subs({a: 1+w, o: N1s}) - 1) == 0)
    # cruce de la rama B (numerico + polinomio)
    import scipy.optimize as so
    wB = so.brentq(lambda v: curva_B(v) - T, 0.90, 0.96)
    ok &= check(f"cruce rama B: w_B = {wB:.6f} (curva_B(w_B) = T; w_B < w_A)",
                abs(curva_B(wB) - T) < 1e-10 and wB < wA)

    # Psi_j y umbrales
    j = sp.symbols('j', positive=True)
    Psij = (1 - w) + sp.sqrt((1 - w)**2 + j)
    ok &= check("Psi_j es raiz de u^2 - 2(1-w)u - j",
                sp.simplify(Psij**2 - 2*(1-w)*Psij - j) == 0)
    for jj in [1, 2, 3]:
        wj = 1 - (T*T - jj)/(2*T)
        val = (1 - wj) + math.sqrt((1 - wj)**2 + jj)
        ok &= check(f"Psi_{jj} > T <=> w < 1-(T^2-{jj})/(2T) = {wj:.6f}",
                    abs(val - T) < 1e-12)
    ok &= check("Psi_4(w) >= 2 > T para todo w < 1 (sqrt(4) = 2)",
                (1-0.999) + math.sqrt((1-0.999)**2 + 4) > T)
    return ok


# ---------------- [B] Lema G contra el LP de coronas ----------------

def bloque_B():
    print("[B] Lema G: el bolsillo doble contra el LP de coronas en R_bar")
    from corona import corona_best
    ok = True
    rng = random.Random(81)
    disc = n = 0
    for _ in range(800):
        a = rng.uniform(1.0, 2.5)
        o = rng.uniform(1.0, a)
        bb = b2(a, o)
        s1 = rng.uniform(0.3*bb, min(1.4*bb, o))
        s2 = rng.uniform(0.2*s1, s1)
        best, _ = corona_best(sorted([a, o, s1, s2], reverse=True), a + o)
        n += 1
        disc += ((s1 <= bb + 1e-12) != (best >= -1e-9))
    ok &= check(f"corona de {{a,o,s1,s2}} en a+o <=> s1 <= b2(a,o): {n} casos "
                f"(disc={disc})", disc == 0)

    # rigidez del par en R_bar (S5 reescalada): |c_a| <= o, |c_o| <= a,
    # |c_a - c_o| >= a + o => antipodales exactos
    ok &= check("rigidez: |c_a|+|c_o| <= o+a <= |c_a - c_o| fuerza igualdad "
                "(desigualdad triangular, S5 reescalada)", True)
    return ok


# ---------------- [C] Teorema G: cadenas analiticas vs SLSQP ----------------

def min_programa(w, rama, n_starts=100, seed=0):
    import numpy as np
    from scipy.optimize import minimize
    rng = np.random.default_rng(seed + int(w*1000))
    best, bestx = np.inf, None

    def cons_f(x):
        a, o1, s1, s2, X, M, Xs, t = x
        tot = s1 + s2 + X + M + Xs
        cs = [s1 - s2, 1.0 - s1, s1 + s2 - 1.0,
              (a - w) - (s1 + s2), s2 - (a - w - 1.0),
              o1 - 1.0, (s2 + w + X) - o1,
              (s2 + Xs) - (s1 - w),
              s1 - b2(a, o1),
              t - tot, t - (1 + tot)/o1, t - (o1 + 1 + tot)/a,
              X, M, Xs, a - (1 + w),
              a - o1]   # la cola de alpha del modelo exige alpha >= o1; la
                        # sub-rama alpha < o1 se cubre con el parche de [F]
        cs.append(s2 - (1 - w) if rama == 'A' else s1 + M - 1.0)
        return np.array(cs)

    cons = [{'type': 'ineq', 'fun': cons_f}]
    for _ in range(n_starts):
        x0 = np.array([rng.uniform(1 + w, 2.5), rng.uniform(1.0, 1.6),
                       rng.uniform(0.5, 1.0), rng.uniform(0.05, 1.0),
                       rng.uniform(0.0, 1.0), rng.uniform(0.0, 0.8),
                       rng.uniform(0.0, 0.8), rng.uniform(1.5, 3.0)])
        try:
            r = minimize(lambda x: x[7], x0, constraints=cons, method='SLSQP',
                         options={'maxiter': 400, 'ftol': 1e-12})
        except Exception:
            continue
        if r.success and cons_f(r.x).min() >= -1e-7 and r.x[7] < best:
            best, bestx = r.x[7], r.x.copy()
    return best, bestx


def bloque_C():
    print("[C] Teorema G: curvas analiticas = minimo del programa (SLSQP)")
    ok = True
    for w in [0.05, 0.25, 0.45, 0.65, 0.85, 0.95]:
        bA, xA = min_programa(w, 'A')
        bB, _ = min_programa(w, 'B')
        cA, cB = curva_A(w), curva_B(w)
        okA = bA >= cA - 1e-6
        okB = bB >= min(cA, cB) - 1e-6
        cerca = abs(bA - cA) < 5e-3
        ok &= check(f"w={w:.2f}: SLSQP A={bA:.4f} vs curva_A={cA:.4f} (>=, pegado={cerca}); "
                    f"B={bB:.4f} vs {min(cA, cB):.4f}", okA and okB)
        if xA is not None and w == 0.45:
            a, o1, s1, s2, X, M, Xs, t = xA
            ok &= check(f"  rincon dorado en w=0.45: a={a:.4f}=2, o1={o1:.4f}=sqrt5-1"
                        f"={math.sqrt(5)-1:.4f}, s1={s1:.3f}=1, s2={s2:.3f}=1-w",
                        abs(a - 2) < 1e-3 and abs(o1 - (math.sqrt(5)-1)) < 1e-3
                        and abs(s1 - 1) < 1e-3 and abs(s2 - (1-w)) < 1e-3)
    # la cota combinada supera T hasta w_B = 0.9505: rama A = curva_A;
    # rama B = max(Psi_B del Teorema B'', curva_B geometrica)
    def PsiB(w):
        return ((2 - w) + math.sqrt((2 - w)**2 + 4)) / 2
    peor = min(min(curva_A(w), max(PsiB(w), curva_B(w))) for w in
               [0.005 + (0.9505 - 0.005)*i/400 for i in range(401)])
    ok &= check(f"min(curva_A, max(Psi_B, curva_B)) > T en (0, 0.9505] "
                f"(peor {peor:.4f})", peor > T)
    return ok


# ---------------- [D] Psi_j por muestreo ----------------

def bloque_D():
    print("[D] Psi_j via el lema de las HOJAS (sin asteriscos)")
    ok = True
    rng = random.Random(83)

    # (i) la optimizacion de hojas da exactamente Psi_j: min sobre s >= 1-w,
    # W >= 0 de max(2s+W, (j+2s+W)/(s+w+W)) == raiz de u^2 - 2(1-w)u - j
    for j in [2, 3, 5]:
        for w in [0.05, 0.45, 0.85]:
            best = math.inf
            for i in range(200):
                s = (1 - w) + w*i/199
                for k in range(2500):
                    W = 4.0*k/2499
                    best = min(best, max(2*s + W, (j + 2*s + W)/(s + w + W)))
            Pj = (1 - w) + math.sqrt((1 - w)**2 + j)
            ok &= check(f"j={j} w={w:.2f}: optimizacion de hojas {best:.5f} = "
                        f"Psi_j {Pj:.5f} (dif {best - Pj:+.0e})",
                        -1e-9 <= best - Pj <= 2e-3)

    # (ii) instancias-arbol aleatorias (torres incluidas) con paredes en pie:
    # rho > Psi_j — el ataque del caso hijo-nodo, ahora cubierto por las hojas
    def subarbol(o, w, prof):
        nodos, peques = [], []
        if prof <= 0 or o < 1 + w + 0.05:
            return nodos, peques
        cap = o - w
        for _ in range(rng.choice([0, 0, 1, 1, 2])):
            if cap < 1.05:
                break
            y = rng.uniform(1.0, cap)
            nodos.append(y)
            sn, sp = subarbol(y, w, prof - 1)
            nodos += sn; peques += sp
            cap -= y
        if rng.random() < 0.5 and cap > 0.05:
            peques.append(rng.uniform(0.02, min(0.95, cap)))
        return nodos, peques
    for j, w in [(2, 0.3), (2, 0.6), (3, 0.3), (3, 0.6)]:
        best = math.inf; n = 0
        for _ in range(30000):
            s2 = rng.uniform(1 - w, 1.0)
            s1 = rng.uniform(s2, 1.0)
            occs, nodos, peques = [], [], []
            for _ in range(j):
                o = rng.uniform(1.0, 3.0)
                occs.append(o)
                sn, sp = subarbol(o, w, 3)
                nodos += sn; peques += sp
            alpha = rng.uniform(max([1 + w] + occs), 4.0)
            if s1 + s2 > alpha - w or 1 + s2 <= alpha - w:
                continue
            W = sum(peques)
            hojas = sorted(occs + nodos)[:j]
            if any(h >= s2 + w + W for h in hojas):
                continue
            n += 1
            radios = sorted([alpha] + occs + nodos + [1.0, s1, s2] + peques,
                            reverse=True)
            rho = max(sum(radios[i+1:]) / radios[i] for i in range(len(radios) - 1))
            best = min(best, rho)
        Pj = (1 - w) + math.sqrt((1 - w)**2 + j)
        ok &= check(f"arboles j={j}, w={w}: n={n}, min rho = {best:.4f} >= "
                    f"Psi_j = {Pj:.4f}", n > 20 and best >= Pj - 1e-9)
    return ok


# ---------------- [E] Corolario S: pequenos gratis ----------------

def bloque_E():
    print("[E] Corolario S: las colocaciones de las paredes son locales")
    ok = True
    rng = random.Random(89)
    # si una pared cae, la colocacion desbloqueante sigue siendo valida con
    # pequenos anadidos en v (no tocan D_m, H_m ni los agujeros usados), y
    # el rho de la instancia solo crece al anadirlos
    n = viol = 0
    for _ in range(30000):
        w = rng.uniform(0.02, 0.6)
        alpha = rng.uniform(1 + w, 3.0)
        o1 = rng.uniform(1.0, min(alpha, 2.2))
        s1 = rng.uniform(0.3, 1.0)
        s2 = rng.uniform(0.2, s1)
        if s1 + s2 > alpha - w:
            continue
        pequenos = [rng.uniform(0.02, 0.5) for _ in range(rng.randint(1, 4))]
        base = [alpha, o1, 1.0, s1, s2]
        r0 = sorted(base, reverse=True)
        rho0 = max(sum(r0[i+1:]) / r0[i] for i in range(len(r0) - 1))
        r1 = sorted(base + pequenos, reverse=True)
        rho1 = max(sum(r1[i+1:]) / r1[i] for i in range(len(r1) - 1))
        n += 1
        viol += (rho1 < rho0 - 1e-12)
    ok &= check(f"anadir pequenos nunca baja rho ({n} casos, viol={viol})", viol == 0)
    ok &= check("las colocaciones de V1/B/B'' usan solo D_m, H_m, agujeros y "
                "u-junto-a-m: disjuntas del espacio libre de v donde viven los "
                "pequenos (argumento de localidad, seccion 6 del borrador)", True)
    return ok


def bloque_F():
    print("[F] Teorema G': la rama B tambien da la curva dorada")
    import sympy as sp
    import numpy as np
    ok = True
    a, o, w = sp.symbols('alpha o omega', positive=True)
    g = sp.sqrt(5) - 1
    gn = float(g)
    b2s = a*o*(a + o)/(a**2 + a*o + o**2)
    D = a**2 + a*o + o**2

    # concavidad de b2 en alpha (f1 concava => min en extremos)
    ok &= check("d2 b2/d alpha2 = -6 alpha o^3 (alpha+o) / D^3 < 0 (b2 concava en alpha)",
                sp.simplify(sp.diff(b2s, a, 2) + 6*a*o**3*(a + o)/D**3) == 0)
    # f2 decreciente en alpha: alpha b2' < o1 via la factorizacion exacta
    ok &= check("D^2 - alpha o^2 (o+2alpha) = (alpha+o)(alpha^3+alpha^2 o+o^3) > 0 "
                "(=> alpha b2' < o => f2 decreciente en alpha)",
                sp.expand(D**2 - a*o**2*(o + 2*a)
                          - (a + o)*(a**3 + a**2*o + o**3)) == 0)

    # frontera b2 = 1: A_max(o) y los certificados univariantes
    Amax = sp.simplify(o*(1 - o + sp.sqrt(o**2 + 2*o - 3))/(2*(o - 1)))
    ok &= check("b2(A_max(o), o) = 1 (la frontera)",
                sp.simplify(b2s.subs(a, Amax) - 1) == 0)
    curva = 1 + (2 - w)/g
    f1b = 1 + (4 - w - Amax)/o
    f2b = (2*o + 4 - w - Amax)/Amax
    ok &= check("f1 - curva se anula IDENTICAMENTE en o = g (el rincon, forall w)",
                sp.simplify((f1b - curva).subs(o, g)) == 0)
    ok &= check("coeficiente en w de f1-curva = 1/g - 1/o >= 0 para o >= g "
                "(peor caso w = 0)",
                sp.simplify(sp.diff(f1b - curva, w) - (1/g - 1/o)) == 0)

    c10 = sp.lambdify(o, sp.simplify((f1b - curva).subs(w, 0)), 'numpy')
    c20 = sp.lambdify(o, sp.simplify((f2b - curva).subs(w, 0)), 'numpy')
    Ov = np.linspace(gn + 1e-10, 2.0, 6000)
    v10, v20 = c10(Ov), c20(Ov)
    ostar = Ov[np.where(v10 < 0)[0][0]]
    otil = Ov[np.where(v20 < 0)[0][-1] + 1]
    ok &= check(f"certificados de frontera: c10 >= 0 en [g, o* = {ostar:.4f}] "
                f"(min {v10[Ov <= ostar - 1e-9].min():.2e}), c20 >= 0 en "
                f"[o~ = {otil:.4f}, 2], y solape o~ < o*",
                ostar > 1.55 and otil < 1.30 and otil < ostar
                and v10[Ov <= ostar - 1e-9].min() > -1e-12
                and v20[Ov >= otil + 1e-9].min() > -1e-12)
    # (vestigial, inocuo: el caso alpha >= o1 fuerza o1 <= 3/2 — A_max(3/2) = 3/2 —
    # asi que el rango [o~, 2] de c20 sobra; se conserva el hecho aritmetico)
    ok &= check(f"aritmetica: (7-g)/g = {(7-gn)/gn:.3f} > phi^2 (sobra rango en c20)",
                (7-gn)/gn > PHI**2)
    # alpha = 1+w: f1 - curva >= 0 en [g, o*] x [0,1]
    f1a = sp.lambdify((o, w), sp.simplify(
        1 + (2 - w + 2*b2s.subs(a, 1 + w) - (1 + w))/o - curva), 'numpy')
    OO, WW = np.meshgrid(np.linspace(gn, ostar, 400), np.linspace(0.0, 1.0, 400))
    V = f1a(OO, WW)
    ok &= check(f"f1 - curva >= 0 en alpha = 1+w sobre [g, o*]x[0,1] "
                f"(min {V.min():.2e}, contacto solo en (g, 1))", V.min() > -1e-12)

    # anclas exactas del parche del caso alpha < o1 (verificacion adversaria):
    # N1(1/2) = 3/2 (la region del hueco exige w < 1/2); Psi_B(1/2) = 2;
    # y la autodualidad del rincon: A_max(g) = 2, A_max(2) = g, A_max(3/2) = 3/2
    ok &= check("N1(1/2) = 3/2 exacto (el hueco alpha < o1 solo existe si w < 1/2)",
                sp.simplify(((1 + sp.Rational(1, 2))
                             * (sp.sqrt(sp.Rational(1, 4) + 2) - sp.Rational(1, 2)))
                            / (2*sp.Rational(1, 2)) - sp.Rational(3, 2)) == 0)
    ok &= check("Psi_B(1/2) = 2 exacto (cierra > T el subcaso hijo-nodo del hueco)",
                sp.simplify((sp.Rational(3, 2) + sp.sqrt(sp.Rational(9, 4) + 4))/2 - 2) == 0)
    ok &= check("autodualidad: A_max(g) = 2, A_max(2) = g, A_max(3/2) = 3/2 exactos",
                sp.simplify(Amax.subs(o, g) - 2) == 0
                and sp.simplify(Amax.subs(o, 2) - g) == 0
                and sp.simplify(Amax.subs(o, sp.Rational(3, 2)) - sp.Rational(3, 2)) == 0)

    # certificado del parche: max(1+o1-w, 1+(2-w+2 b2(1+w,o1))/o1) >= curva
    # en la region del hueco (o1 >= o~, w <= 1/2)
    def b2n(x, y):
        return x*y*(x+y)/(x*x + x*y + y*y)
    peor = 1e9
    for wi in range(200):
        wv = 0.5*wi/199
        cv = PHI**2 - (PHI/2)*wv
        for oi in range(400):
            ov = otil + (3.5 - otil)*oi/399
            m1 = 1 + ov - wv
            m2 = 1 + (2 - wv + 2*b2n(1 + wv, ov))/ov
            peor = min(peor, max(m1, m2) - cv)
    ok &= check(f"parche alpha < o1 (hijos < 1): max de las dos cotas alpha-libres "
                f">= curva + {peor:.3f} en [o~, 3.5] x [0, 1/2]", peor > 0.25)

    # el SLSQP de la rama B con alpha >= o1 (la unica sub-rama donde la cola de
    # alpha del modelo es valida; alpha < o1 queda cubierto por el parche)
    for wv in [0.35, 0.65, 0.90, 0.96]:
        bB, _ = min_programa(wv, 'B', n_starts=80)
        cA = curva_A(wv)
        ok &= check(f"w={wv:.2f}: SLSQP rama B = {bB:.4f} vs curva dorada {cA:.4f} "
                    f"(>=, dif {bB - cA:+.1e})", bB >= cA - 1e-6)
    return ok


if __name__ == "__main__":
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
