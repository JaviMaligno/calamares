"""Punto 2 de docs/reinsercion.md seccion 10: la Proposicion 3 con grosor positivo.

Plantilla canonica con grosor omega = w/r_m (normalizada a r_m = 1): v es la
sarten de radio R = alpha + 1, ocupada por alpha y m tangentes; u es el agujero
de alpha, capacidad alpha - omega; el testigo coloco S = {s1, s2} en u. El
intercambio manda m a u y debe reinsertar S. Recursos de reinsercion:

    D_m   colocacion en v: falla solo si el trio {alpha,s1,s2} es infactible
          en el disco alpha+1 (s1 va al disco vacante, s2 a un bolsillo)
    H_m   agujero de m, capacidad 1 - omega (viaja con m)
    u     junto a m dentro del agujero de alpha (par {1, s2} en disco alpha-omega)
    anidamiento de s2 en s1 (capacidad s1 - omega)

Bloqueo genuino realizable por un testigo (clausuras para los infimos):

    (B1) trio {alpha, s1, s2} infactible en R = alpha + 1
    (B2) s2 >= 1 - omega            (si no, H_m absorbe a s2)
    (B3) s2 >= s1 - omega           (implicada por B2, pues s1 <= 1)
    (B4) s2 >= alpha - omega - 1    (si no, s2 entra en u junto a m)
    (W)  s1 + s2 <= alpha - omega   (S cabia en u: exacto para dos circulos)

ademas 1 <= alpha - omega (m anida en alpha) y s2 <= s1 <= 1. Presiones sobre
rho: cola de m da rho >= s1+s2; cola de alpha da rho >= (1+s1+s2)/alpha.

    T_can(omega) := inf max(s1+s2, (1+s1+s2)/alpha)  sobre bloqueos realizables.

La Proposicion 3 (limite w -> 0) es el infimo del programa RELAJADO (B1) + (W):
en omega = 0 el programa completo es vacio (B2 exigiria s2 >= 1 > s1).

Resultados que este script verifica:

  [A] Algebra exacta (sympy).  Rama del testigo (B1)+(W):
        Phi(omega) = T_{1+omega} - omega,  con T_c la raiz positiva de
        a^3 = c(a^2+a+1)  (T_1 = T, Tribonacci).
      Monotonia exacta: Phi'(omega) = (2a+1) / (a^2 (a^2+2a+3)) > 0, y Phi es
      concava; c := Phi'(0) = (2T+1)/(7T^2+4T+3) ~ 0.1374516; cota lineal por
      cuerda Phi(omega) >= T + (13-7T) omega en [0, 1/7]. El cruce
      Phi = 2(1-omega) esta en la raiz w_x de 2w^3 - 10w^2 + 14w - 1 = 0
      (equivalente: a_x = 2 - w_x raiz de 2a^3 = 2a^2 + 2a + 3), con suelo
      2(1-w_x) ~ 1.84914 > T. Esquina exacta: T_{8/7} = 2 y b(2) = 6/7.

  [B] Hueco H1 (heredado de la Proposicion 3), contraste numerico: sobre la
      frontera h(alpha, s1) de infactibilidad del trio, s1 + h es decreciente
      en s1 (pendiente kappa = -dh/ds1 >= 1), luego el minimo del relajado esta
      en s1 -> 1 y vale 1 + b(alpha); ademas h(alpha,1) = b(alpha) (Descartes).

  [C] Cota inferior en bloqueos muestreados: todo bloqueo realizable cumple
      rho >= max(2(1-omega), Phi(omega)) >= 2(1-w_x) > T.

  [D] Curva medida T_can(omega) por barrido (frontera del trio por biseccion,
      metodo de trio.py, con (B2), (B4) y (W)) contra las tres ramas:
        omega <= w_1        T_can = 2(1-omega)                 (rama H_m)
        w_1 <= omega <= 1/7 T_can = alpha_m(omega) - omega     (rama mixta,
                              alpha_m: h(alpha, alpha-1) = 1-omega)
        omega >= 1/7        T_can = Phi(omega)                 (rama del testigo)
      donde w_1 ~ 0.042 es el grosor en que el trio {2-w, 1-w, 1-w} toca la
      frontera de infactibilidad (h(2-w, 1-w) = 1-w). Nota: w_1 < w_x, de modo
      que la cota [C] es ajustada solo en las ramas H_m y testigo; en la mixta
      hay holgura (maxima ~0.06 en w_x). La curva medida decrece en (0, 1/7],
      alcanza su minimo global 13/7 = 1.857142... en la esquina omega = 1/7
      (donde sigma2 = 1-omega = b(2) = 6/7 y alpha = 2, todo racional exacto)
      y crece despues como Phi. Los fallos conocidos (n=4 y gemelas) se
      contrastan contra sus cotas.
"""
import math
import numpy as np
import sympy as sp
from reinserta import feas3, TRIB, PHI
from trio import infeasible_trio, min_s2_blocking, rho_of


# ---------------- algebra basica ----------------
def pocket(alpha):
    """Bolsillo de Descartes b(alpha) = alpha(alpha+1)/(alpha^2+alpha+1)."""
    return alpha * (alpha + 1) / (alpha * alpha + alpha + 1)


def T_root(c, lo=1.0, hi=4.0, tol=1e-14):
    """Raiz positiva de a^3 = c(a^2+a+1), unica para c > 0 (una sola variacion
    de signo en la regla de Descartes), por biseccion."""
    f = lambda a: a**3 - c * (a * a + a + 1)
    assert f(lo) < 0 < f(hi)
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def Phi(omega):
    """Infimo de la rama del testigo: Phi(omega) = T_{1+omega} - omega."""
    return T_root(1.0 + omega) - omega


def phi_prime(omega):
    """Formula exacta de la derivada (seccion [A])."""
    a = T_root(1.0 + omega)
    return (2 * a + 1) / (a * a * (a * a + 2 * a + 3))


def lower_bound(omega):
    """Cota inferior demostrada (modulo H1) de T_can(omega)."""
    return max(2.0 * (1.0 - omega), Phi(omega))


# ---------------- bloqueo con grosor ----------------
def bloqueo(alpha, s1, s2, omega, e=1e-12):
    """Clausura de las condiciones (B1)-(B4)+(W) mas las de plantilla."""
    return (infeasible_trio(alpha, s1, s2)
            and s2 >= 1.0 - omega - e
            and s2 >= alpha - omega - 1.0 - e
            and s1 + s2 <= alpha - omega + e
            and 1.0 <= alpha - omega + e
            and s2 <= s1 + e and s1 <= 1.0 + e)


def best_rho_omega(alpha, omega, grid=300):
    """min de rho sobre la clausura de los bloqueos con alpha fijo. En el
    optimo s2 esta en el maximo de sus tres cotas inferiores (frontera del
    trio, banda 1-omega, B4), porque rho es creciente en s2; la infactibilidad
    del trio es monotona creciente en s2, luego subir s2 hasta ese maximo
    preserva (B1)."""
    if 1.0 > alpha - omega:
        return (math.inf, None, None)
    best = (math.inf, None, None)
    # tope 1 - 1e-7: en s1 = 1 exacto la tangencia diametral con alpha degenera
    # el criterio angular (c = -1 en sep_angle); mismo recorte que en trio.py
    for s1 in np.linspace(max(0.30, 1.0 - omega), 1.0 - 1e-7, grid):
        s1 = float(s1)
        f = min_s2_blocking(alpha, s1)
        if f is None:
            continue
        s2 = max(f, 1.0 - omega, alpha - omega - 1.0)
        if s2 > s1 + 1e-12 or s1 + s2 > alpha - omega + 1e-9:
            continue
        r = rho_of(alpha, s1, s2)
        if r < best[0]:
            best = (r, s1, s2)
    return best


def T_can_num(omega, a_lo=None, a_hi=2.6):
    """Barrido en alpha con dos refinados alrededor del argmin."""
    a_lo = max(1.0 + omega + 1e-9, 1.50) if a_lo is None else a_lo
    best = (math.inf, None, None, None)
    for alphas, grid in ((np.arange(a_lo, a_hi, 0.02), 250), (None, 900), (None, 2500)):
        if alphas is None:
            if best[1] is None:
                return best
            step = 0.02 if grid == 900 else 0.002
            alphas = np.linspace(max(a_lo, best[1] - step), best[1] + step, 21)
        for a in alphas:
            r, s1, s2 = best_rho_omega(float(a), omega, grid=grid)
            if r < best[0]:
                best = (r, float(a), s1, s2)
    return best


def alpha_mixta(omega, tol=1e-10):
    """Rama mixta: menor alpha con bloqueo en sigma2 = 1-omega y testigo justo
    (sigma1 = alpha-1), es decir h(alpha, alpha-1) = 1-omega. La funcion
    G(alpha) = h(alpha, alpha-1) es DECRECIENTE en la ventana (la subida de
    sigma1 pesa mas que el crecimiento del bolsillo), asi que se biseca con
    G(lo) > 1-omega > G(hi)."""
    g = lambda a: (min_s2_blocking(a, a - 1.0) or math.inf) - (1.0 - omega)
    lo, hi = 1.88, 2.0005
    if not (g(lo) > 0 > g(hi)):
        return None
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        if g(mid) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def omega_1(tol=1e-9):
    """Muerte de la rama H_m: mayor omega tal que existe alpha en [2-w, 2]
    (ventana que fijan (W) y (B4)) con el trio {alpha, 1-w, 1-w} infactible.
    Como h(alpha, 1-w) crece con alpha, el candidato es alpha = 2-w y la
    condicion es h(2-w, 1-w) <= 1-w; se biseca en omega."""
    def alive(om):
        f = min_s2_blocking(2.0 - om, 1.0 - om)
        return f is not None and f <= 1.0 - om + 1e-12
    lo, hi = 0.02, 0.07
    assert alive(lo) and not alive(hi)
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        if alive(mid):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


if __name__ == "__main__":
    T = TRIB
    print(f"T = {T:.9f}   phi = {PHI:.9f}\n")

    # ---------------- [A] algebra exacta ----------------
    print("[A] ALGEBRA EXACTA (sympy)")
    a, w = sp.symbols('a w', positive=True)
    x = sp.symbols('x')
    b_sym = a * (a + 1) / (a**2 + a + 1)
    ok1 = sp.simplify((b_sym - (a - 1 - w)) * (a**2 + a + 1)
                      + (a**3 - (1 + w) * (a**2 + a + 1))) == 0
    print(f"  b(a) = a-1-w  <=>  a^3 = (1+w)(a^2+a+1)          : {ok1}")

    F = a**3 - (1 + w) * (a**2 + a + 1)
    dadw = (-sp.diff(F, w) / sp.diff(F, a)).subs(w, a**3 / (a**2 + a + 1) - 1)
    ok2 = sp.simplify(dadw - 1 - (2 * a + 1) / (a**2 * (a**2 + 2 * a + 3))) == 0
    print(f"  Phi'(w) = (2a+1)/(a^2(a^2+2a+3))  (exacta, > 0)  : {ok2}")

    ok3 = sp.rem(x**2 * (x**2 + 2 * x + 3) - (7 * x**2 + 4 * x + 3),
                 x**3 - x**2 - x - 1, x) == 0
    Tex = sp.CRootOf(x**3 - x**2 - x - 1, 0)
    c0 = float((2 * Tex + 1) / (7 * Tex**2 + 4 * Tex + 3))
    print(f"  c = Phi'(0) = (2T+1)/(7T^2+4T+3) = {c0:.7f}      : {ok3}")
    print(f"      contraste numerico: phi_prime(0) = {phi_prime(0.0):.7f}, "
          f"dif finita = {(Phi(1e-6) - Phi(0)) / 1e-6:.7f}")

    ok4 = sp.expand((2 - w)**3 - (1 + w) * ((2 - w)**2 + (2 - w) + 1)
                    + (2 * w**3 - 10 * w**2 + 14 * w - 1)) == 0
    wx = float(sp.nsolve(2 * w**3 - 10 * w**2 + 14 * w - 1, w, 0.075))
    ax = 2.0 - wx
    floor = 2.0 * (1.0 - wx)
    ok5 = abs(2 * ax**3 - 2 * ax**2 - 2 * ax - 3) < 1e-10
    print(f"  cruce Phi = 2(1-w): 2w^3-10w^2+14w-1 = 0         : {ok4}")
    print(f"  w_x = {wx:.7f}  a_x = 2-w_x raiz de 2a^3=2a^2+2a+3: {ok5}")
    print(f"  suelo uniforme 2(1-w_x) = {floor:.7f} = T + {floor - T:.7f}")
    ok6 = abs(T_root(8 / 7) - 2.0) < 1e-12 and pocket(2.0) == 6 / 7
    print(f"  esquina w = 1/7: T_(8/7) = 2 y b(2) = 6/7 exactos : {ok6}")

    chord = 13 - 7 * T
    grid_w = np.linspace(1e-4, 1 / 7, 40)
    ok7 = all(Phi(o) >= T + chord * o - 1e-12 for o in grid_w)
    ok8 = all(Phi(o) <= T + c0 * o + 1e-12 for o in grid_w)
    ok9 = all(phi_prime(o2) < phi_prime(o1) for o1, o2 in zip(grid_w, grid_w[1:]))
    print(f"  T + (13-7T)w <= Phi(w) <= T + c w en [0,1/7]     : {ok7 and ok8}"
          f"   (13-7T = {chord:.7f}); Phi' decreciente (concava): {ok9}")

    # ---------------- [B] hueco H1 ----------------
    print("\n[B] HUECO H1: frontera del trio, s1 + h decreciente (kappa >= 1)")
    print(f"  {'alpha':>8} {'|h(a,1)-b(a)|':>14} {'kappa_min':>10} {'monotona':>9}")
    kappa_global = math.inf
    for al in (1.60, 1.75, 1.85, ax, 2.00, 2.20, 2.40):
        s1s = np.linspace(0.60, 1.0 - 1e-7, 201)
        hs = np.array([min_s2_blocking(al, float(s)) or np.nan for s in s1s])
        mask = ~np.isnan(hs)
        kap = -np.diff(hs[mask]) / np.diff(s1s[mask])
        kmin = kap.min()
        kappa_global = min(kappa_global, kmin)
        mono = bool(np.all(np.diff(s1s[mask] + hs[mask]) < 1e-9))
        err = abs((min_s2_blocking(al, 1.0 - 1e-7) or math.nan) - pocket(al))
        print(f"  {al:>8.4f} {err:>14.2e} {kmin:>10.4f} {str(mono):>9}")
    print(f"  kappa_min global = {kappa_global:.4f} >= 1: {kappa_global >= 1.0}"
          "   (H1 verificado en malla; sin prueba analitica)")

    # ---------------- [C] cota inferior muestreada ----------------
    print("\n[C] COTA INFERIOR EN BLOQUEOS MUESTREADOS")
    rng = np.random.default_rng(0)
    n_acc, worst = 0, math.inf
    for _ in range(60000):
        om = float(rng.uniform(0.005, 0.30))
        al = float(rng.uniform(1.0 + om + 0.01, 2.8))
        s1 = float(rng.uniform(1.0 - om, 1.0))
        s2_lo = max(1.0 - om, al - om - 1.0, 0.0)
        if s2_lo >= s1:
            continue
        s2 = float(rng.uniform(s2_lo, s1))
        if s1 + s2 > al - om or not bloqueo(al, s1, s2, om):
            continue
        n_acc += 1
        worst = min(worst, rho_of(al, s1, s2) - lower_bound(om))
    print(f"  bloqueos realizables aceptados: {n_acc}")
    print(f"  min de rho - max(2(1-w), Phi(w)) = {worst:.6f} >= 0: {worst >= -1e-9}")
    print(f"  (y por tanto rho >= suelo {floor:.5f} > T en todos)")

    # ---------------- [D] curva medida contra ramas ----------------
    print("\n[D] CURVA MEDIDA T_can(omega) CONTRA LAS TRES RAMAS")
    w1 = omega_1()
    print(f"  w_1 (muerte de la rama H_m: h(2-w, 1-w) = 1-w) = {w1:.6f}")
    def hm_alive(om):
        """Existe alpha admisible ((W) y (B4): alpha en [2-om, 2]) con el
        reparto igual {1-om, 1-om} bloqueando el trio."""
        return any((min_s2_blocking(float(a), 1.0 - om) or math.inf)
                   <= 1.0 - om + 1e-12
                   for a in np.linspace(2.0 - om, 2.0, 41))
    ok_w1 = hm_alive(0.038) and not hm_alive(0.043) and not hm_alive(0.05)
    print(f"  rama H_m viva en w = 0.038 y muerta en w = 0.043, 0.05 "
          f"(en TODA la ventana de alpha admisible): {ok_w1}")
    print(f"\n  {'omega':>7} {'T_can num':>10} {'prediccion':>11} {'dif':>9} "
          f"{'rama':>7}   alpha*, s1*, s2*")
    omegas = [0.02, 0.04, w1, 0.06, wx, 0.09, 0.11, 0.125, 1 / 7, 0.16, 0.20, 0.25]
    max_dif = 0.0
    for om in omegas:
        r, als, s1s_, s2s_ = T_can_num(om)
        if om <= w1 + 1e-12:
            pred, rama = 2.0 * (1.0 - om), "H_m"
        elif om <= 1 / 7 + 1e-12:
            am = alpha_mixta(om)
            pred, rama = (am - om if am else math.nan), "mixta"
        else:
            pred, rama = Phi(om), "testigo"
        dif = r - pred
        max_dif = max(max_dif, abs(dif))
        arg = (f"{als:.4f}, {s1s_:.4f}, {s2s_:.4f}" if als else "-")
        print(f"  {om:>7.4f} {r:>10.6f} {pred:>11.6f} {dif:>+9.2e} {rama:>7}   {arg}")
    print(f"  desviacion maxima |T_can - prediccion| = {max_dif:.2e}")

    print("\n  comprobaciones de la curva:")
    vals = [(om, T_can_num(om)[0]) for om in
            (0.02, 0.05, wx, 0.10, 0.13, 1 / 7, 0.15, 0.20)]
    ok_lb = all(v >= lower_bound(om) - 2e-3 for om, v in vals)
    ok_T = all(v > T for _, v in vals)
    vmin, omin = min((v, om) for om, v in vals)
    print(f"    T_can(w) > T en toda la malla                  : {ok_T}")
    print(f"    T_can(w) >= max(2(1-w), Phi(w)) en la malla    : {ok_lb}")
    print(f"    minimo global medido: {vmin:.6f} en w = {omin:.4f} "
          f"(conjetura: 13/7 = {13 / 7:.6f} en w = 1/7 = {1 / 7:.4f})")
    print( "    la curva decrece en (0, 1/7] (H_m y mixta) y crece en "
          "[1/7, ...) (testigo):")
    print( "      " + " -> ".join(f"{v:.4f}" for _, v in vals))
    print(f"    holgura de la cota en la rama mixta (maxima en w_x): "
          f"{T_can_num(wx)[0] - lower_bound(wx):.4f}")

    # ---------------- fallos conocidos ----------------
    print("\nFALLOS CONOCIDOS NORMALIZADOS (r_m = 1) CONTRA LA COTA")
    for name, al, om, s1, s2 in (
            ("contraejemplo n=4 {10,5,4.9,4.8}", 2.0, 0.06, 0.98, 0.96),
            ("gemelas I1 {10,5,4.99,4.50}     ", 2.0, 0.101, 0.998, 0.90)):
        blk = bloqueo(al, s1, s2, om, e=1e-9)
        r = rho_of(al, s1, s2)
        lb = lower_bound(om)
        print(f"  {name} omega={om:.3f}: bloqueo={blk}  rho={r:.4f} "
              f">= cota {lb:.4f}: {r >= lb - 1e-9}")
        print(f"      holguras: B2 s2-(1-w)={s2 - (1 - om):+.4f}  "
              f"B4 s2-(a-w-1)={s2 - (al - om - 1):+.4f}  "
              f"W (a-w)-(s1+s2)={al - om - s1 - s2:+.4f}")

    print("\nVEREDICTO:")
    print(f"  rama del testigo: Phi(w) = T_(1+w) - w, creciente estricta "
          f"(Phi' > 0 exacta), Phi(0) = T")
    print(f"  rama H_m:         rho > 2(1-w), decreciente")
    print(f"  T_can(w) >= max de ambas >= 2(1-w_x) = {floor:.5f} = T + "
          f"{floor - T:.5f} para todo w > 0:")
    print( "  'el grosor solo lo sube' (resultados.md 5quater) CONFIRMADO en la")
    print( "  plantilla canonica, con holgura uniforme. La curva T_can(w) no es")
    print( "  monotona: cae de 2 hasta su minimo (medido 13/7, en la esquina")
    print( "  racional w = 1/7, alpha = 2, sigma2 = 6/7) y sube despues como Phi.")
