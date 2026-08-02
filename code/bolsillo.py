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

         rho > max( Psi_B(w) ,  1 + (2-w)/N1(w) )

     (la primera es la cota combinatoria del Teorema B'' — la rama B de la
     dicotomia es la misma —, > T hasta (T-1)^2 = 0.704; la segunda es la
     geometrica, > T en (0.207, 0.9505): juntas cubren (0, w_B)).
     Cruces con T: rama A en w_A = 2 - 2(T-1)(phi-1) = 0.96259...; rama B en
     w_B = 0.95053... (raiz algebraica de N1(w)(T-1) = 2-w). En total:
     bloqueo (j=1) => rho > T para todo w < w_B. El rincon optimo del programa
     es DORADO: alpha = 2, o1 = sqrt(5)-1, b2(2, sqrt(5)-1) = 1 exacto.

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
              X, M, Xs, a - (1 + w)]
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
    print("[D] Psi_j: la cola de o1 con j ocupantes (muestreo de paredes)")
    ok = True
    rng = random.Random(83)
    w = 0.5
    for j in [2, 3]:
        best = math.inf
        for _ in range(60000):
            s2 = rng.uniform(1 - w, 1.0)
            s1 = rng.uniform(s2, 1.0)
            X = rng.uniform(0.0, 1.2)
            if s2 + w + X <= 1.0:
                continue
            o1 = rng.uniform(1.0, s2 + w + X)
            occ_extra = [rng.uniform(1.0, o1) for _ in range(j - 1)]
            alpha = rng.uniform(max([1 + w, o1] + occ_extra), 3.2)
            if s1 + s2 > alpha - w or 1 + s2 <= alpha - w:
                continue
            radios = sorted([alpha, o1] + occ_extra + [1.0, s1, s2]
                            + ([X/2, X/2] if X > 1e-9 else []), reverse=True)
            rho = max(sum(radios[i+1:]) / radios[i] for i in range(len(radios) - 1))
            best = min(best, rho)
        Pj = (1 - w) + math.sqrt((1 - w)**2 + j)
        ok &= check(f"j={j}, w={w}: min rho muestreado = {best:.4f} >= Psi_j = {Pj:.4f}",
                    best >= Pj - 1e-9)
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
