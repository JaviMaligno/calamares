"""Teorema del suelo rigido (docs/drafts/suelo_rigido.md): verificacion numerica.

Subfamilia rigida F, normalizada a r1 = 1 (t = r2, u = r3, v = r4, omega = w):
    (F1) R = 1 + t          (tangencia diametral exacta: R = r1 + r2)
    (F2) u + v <= 1 - omega (la pareja {r3, r4} cabe en el agujero de r1)
    (F3) el trio {1, u, v} NO empaqueta en el disco de radio R
con 1 > t > u > v > 0 y omega > 0.

Teorema: toda instancia de F cumple rho > T (Tribonacci), y el infimo es
exactamente T (no alcanzado), aproximado por la familia u -> t -> t*,
v -> b(t)+, omega -> 0, donde b(t) = t(1+t)/(1+t+t^2) es el bolsillo de
Descartes de la configuracion rigida y t* es la raiz de t^3+t^2+t = 1 (T = 1/t*).

La prueba usa solo direcciones constructivas (nunca la exactitud de feas3):
  Lema 1  sin^2(theta/2) = f(a)f(b), f(x) = x/(R-x)  [angulo minimo en pared]
  Lema 2  theta(1,u)+theta(1,v)+theta(u,v) <= 2pi => empaqueta (construccion)
  Lema 3  psi(u)+psi(v) >= tau => suma angular <= 2pi,
          con psi(x) = sqrt((t-x)/x), tau = t/sqrt(1+t)
  Lema 4  psi(u)+psi(v) < tau => u+v > t+b(t) (si t < 1/phi; si no, u+v > 1)
  Prop 5  bolsillo rigido: {1,t,v} empaqueta en 1+t <=> v <= b(t)  [exactitud]
Cada seccion V* de este script verifica el lema correspondiente en una malla.
"""
import math
import numpy as np
import sympy as sp
from reinserta import feas3, sep_angle, TRIB, PHI

TSTAR = 1.0 / TRIB          # raiz real de t^3 + t^2 + t = 1
INVPHI = (math.sqrt(5) - 1) / 2


def b(t):
    """Bolsillo de Descartes de {1, t} llenando R = 1 + t (config rigida)."""
    return t * (1 + t) / (1 + t + t * t)


def tau(t):
    return t / math.sqrt(1 + t)


def psi(x, t):
    """Cambio de variable del Lema 4: psi decreciente, psi(b(t)) = tau(t)."""
    return math.sqrt((t - x) / x)


def L(t):
    """Cota inferior de rho2: L(t) = (t + b(t))/t, decreciente, L(t*) = T."""
    return 1 + (1 + t) / (1 + t + t * t)


def theta(a, bb, R):
    """Separacion angular minima de dos circulos tangentes a la pared (Lema 1)."""
    s2 = a * bb / ((R - a) * (R - bb))
    return 2 * math.asin(min(1.0, math.sqrt(s2)))


def construccion(t, u, v):
    """Colocacion explicita del Lema 2 (orden v, 1, u; el 1 en medio).

    Devuelve (valida, centros). Solo debe llamarse cuando la suma angular
    es <= 2pi; la validez se comprueba con geometria directa, sin criterios.
    """
    R = 1 + t
    th1u, th1v = theta(1, u, R), theta(1, v, R)
    c1 = np.array([R - 1.0, 0.0])
    cu = (R - u) * np.array([math.cos(th1u), math.sin(th1u)])
    cv = (R - v) * np.array([math.cos(th1v), -math.sin(th1v)])
    eps = 1e-9
    ok = (np.linalg.norm(c1 - cu) >= 1 + u - eps
          and np.linalg.norm(c1 - cv) >= 1 + v - eps
          and np.linalg.norm(cu - cv) >= u + v - eps
          and np.linalg.norm(c1) + 1 <= R + eps
          and np.linalg.norm(cu) + u <= R + eps
          and np.linalg.norm(cv) + v <= R + eps)
    return ok, (c1, cu, cv)


def rho_gadget(t, u, v):
    """rho de la instancia normalizada {1, t, u, v} (maximo de las tres colas)."""
    return max(t + u + v, (u + v) / t, v / u)


def en_F(t, u, v, omega=0.0):
    """Pertenencia a la subfamilia rigida (F3 via feas3, solo como oraculo
    de contraste: la prueba del teorema no usa feas3)."""
    if not (0 < v < u < t < 1):
        return False
    if u + v > 1 - omega:
        return False
    if u + v <= t:                     # fila: trio factible
        return False
    return not feas3(sorted([1.0, u, v], reverse=True), 1 + t)


# ---------------- V1: identidad del medio angulo contra sep_angle ----------------
def V1(muestras=20000, seed=1):
    rng = np.random.default_rng(seed)
    peor = 0.0
    for _ in range(muestras):
        t = rng.uniform(0.2, 0.95)
        R = 1 + t
        a = rng.uniform(0.05, t)
        c = rng.uniform(0.05, a)
        s = sep_angle(a, c, R)
        if not math.isfinite(s):
            continue
        peor = max(peor, abs(s - theta(a, c, R)))
    print(f"V1 identidad sin^2(theta/2)=f(a)f(b) vs sep_angle: err max = {peor:.2e}")
    return peor < 1e-9


# ---------------- V2+V3: lema constructivo ----------------
def V2V3(muestras=60000, seed=2):
    rng = np.random.default_rng(seed)
    casos = fallos_ang = fallos_geo = 0
    for _ in range(muestras):
        t = rng.uniform(0.2, 0.95)
        u = rng.uniform(0.05, t)
        v = rng.uniform(0.05, u)
        if psi(u, t) + psi(v, t) < tau(t):
            continue
        casos += 1
        R = 1 + t
        suma = theta(1, u, R) + theta(1, v, R) + theta(u, v, R)
        if suma > 2 * math.pi + 1e-12:
            fallos_ang += 1                     # refutaria el Lema 3
            continue
        ok, _ = construccion(t, u, v)
        if not ok:
            fallos_geo += 1                     # refutaria el Lema 2
    print(f"V2+V3 psi-suma>=tau => construccion valida: {casos} casos, "
          f"{fallos_ang} fallos angulares, {fallos_geo} fallos geometricos")
    return fallos_ang == 0 and fallos_geo == 0

# ---------------- V4: cota inferior de la suma ----------------
def V4(muestras=400000, seed=3):
    rng = np.random.default_rng(seed)
    na = nb = fallos = 0
    for _ in range(muestras):
        t = rng.uniform(0.2, 0.95)
        u = rng.uniform(0.05, t)
        v = rng.uniform(0.05, u)
        if psi(u, t) + psi(v, t) >= tau(t):
            continue
        if t >= INVPHI:
            nb += 1
            if u + v <= 1.0 - 1e-12:
                fallos += 1
        else:
            na += 1
            if u + v <= t + b(t) - 1e-12:
                fallos += 1
    print(f"V4 psi-suma<tau => u+v > t+b(t) (o > 1 si t>=1/phi): "
          f"{na}+{nb} casos, {fallos} fallos")
    # la afirmacion de concavidad: min de U(a)+U(tau-a) esta en los extremos
    peor = 0.0
    for t in np.linspace(0.2, INVPHI, 25):
        tv = tau(t)
        aa = np.linspace(0.0, tv, 2001)
        W = t / (1 + aa**2) + t / (1 + (tv - aa) ** 2)
        peor = max(peor, (t + b(t)) - W.min())
    print(f"V4b min_a U(a)+U(tau-a) vs t+b(t): exceso max del extremo = {peor:.2e}")
    return fallos == 0 and peor < 1e-9


# ---------------- V5: identidades simbolicas ----------------
def V5():
    t, v, a = sp.symbols('t v a', positive=True)
    B = t * (1 + t) / (1 + t + t**2)
    TAU = t / sp.sqrt(1 + t)
    ok = []
    # psi(b(t)) = tau
    ok.append(sp.simplify(sp.sqrt(sp.simplify((t - B) / B)) - TAU) == 0)
    # b(t) < 1-t <=> t^3+t^2+t < 1
    ok.append(sp.expand((1 - t) * (1 + t + t**2) - t * (1 + t)) ==
              sp.expand(1 - t - t**2 - t**3))
    # L decreciente: numerador de L' es -(t^2+2t)
    Lsym = 1 + (1 + t) / (1 + t + t**2)
    ok.append(sp.simplify(sp.diff(Lsym, t) * (1 + t + t**2)**2 + t**2 + 2 * t) == 0)
    # L(t*) = 1/t* modulo la cubica de Tribonacci
    resto = sp.rem(sp.expand(sp.together(Lsym - 1 / t) * t * (1 + t + t**2)),
                   t**3 + t**2 + t - 1, t)
    ok.append(sp.simplify(resto) == 0)
    # 2b - 1 tiene el signo de t^2+t-1 (raiz 1/phi)
    ok.append(sp.simplify(sp.together(2 * B - 1) - (t**2 + t - 1) / (t**2 + t + 1)) == 0)
    # U'' tiene el signo de 3a^2-1 (concavidad hasta 1/sqrt(3))
    ok.append(sp.simplify(sp.diff(t / (1 + a**2), a, 2) -
                          2 * t * (3 * a**2 - 1) / (a**2 + 1)**3) == 0)
    # t/(1+tau^2) = b(t): el extremo del segmento es el bolsillo
    ok.append(sp.simplify(t / (1 + TAU**2) - B) == 0)
    # tau <= 1/sqrt(3) <=> 3t^2-t-1 <= 0 (raiz (1+sqrt13)/6 = 0.7676 > 1/phi)
    ok.append(sp.simplify(sp.together(TAU**2 - sp.Rational(1, 3)) -
                          (3 * t**2 - t - 1) / (3 * (t + 1))) == 0)
    # necesidad del bolsillo rigido: la eliminacion factoriza como
    # (1+t)(1+t-v)^2 - (1+v)^2 - t(t+v)^2 + t(1+t) = 4(1+t+t^2)(b(t) - v)... salvo factor
    expr = sp.expand((1 + t) * (1 + t - v)**2 - (1 + v)**2 - t * (t + v)**2 + t * (1 + t))
    ok.append(sp.simplify(expr - 4 * (t * (t + 1) - v * (t**2 + t + 1))) == 0)
    # b(T) = T-1 en el diccionario alpha = 1/t: alpha(alpha+1)/(alpha^2+alpha+1) - (alpha-1)
    al = sp.symbols('alpha', positive=True)
    resto2 = sp.rem(sp.expand((al * (al + 1) - (al - 1) * (al**2 + al + 1))),
                    al**3 - al**2 - al - 1, al)
    ok.append(sp.simplify(resto2) == 0)
    print(f"V5 identidades simbolicas: {sum(ok)}/{len(ok)} verificadas -> {ok}")
    return all(ok)


# ---------------- V6: bolsillo rigido, necesidad y suficiencia ----------------
def V6():
    """Prop 5: {1, t, v} empaqueta en R = 1+t sii v <= b(t).

    Suficiencia: coordenadas explicitas del bolsillo (tangente a pared, al 1 y
    al t) y colocacion de v concentrica dentro de el. Necesidad: barrido de
    centros (d, gamma): ninguna posicion admite v > b(t). El solver fisico no
    sirve aqui: la configuracion rigida es de medida nula y no la encuentra.
    """
    fallos_suf = fallos_nec = casos = 0
    for t in np.linspace(0.3, 0.9, 13):
        R, bb = 1 + t, b(t)
        casos += 1
        # centro del bolsillo: distancia d = R - b, angulo gamma con cos dado
        # por la tangencia al circulo t (centro (1,0)); c1 = (-t, 0)
        d = R - bb
        x = (d * d + 1 - (t + bb) ** 2) / 2.0
        X = np.array([x, math.sqrt(max(0.0, d * d - x * x))])
        r1_ = math.dist(X, (-t, 0)) - (1 + bb)      # residuo tangencia al 1
        r2_ = math.dist(X, (1, 0)) - (t + bb)       # residuo tangencia al t
        if max(abs(r1_), abs(r2_)) > 1e-9:
            fallos_suf += 1
        # colocacion de v < b concentrica: margenes estrictamente positivos
        for v in (0.5 * bb, 0.9 * bb, 0.999 * bb):
            m = min(math.dist(X, (-t, 0)) - (1 + v),
                    math.dist(X, (1, 0)) - (t + v),
                    R - (np.linalg.norm(X) + v))
            if m < -1e-12:
                fallos_suf += 1
        # necesidad: para v > b, ningun centro (d, gamma) es valido
        for v in (bb + 0.01, bb + 0.05):
            if v > t:
                continue
            dd = np.linspace(0.0, R - v, 400)[:, None]
            gg = np.linspace(0.0, math.pi, 400)[None, :]
            m1 = dd**2 + t**2 + 2 * dd * t * np.cos(gg) - (1 + v)**2
            m2 = dd**2 + 1 - 2 * dd * np.cos(gg) - (t + v)**2
            mejor = np.minimum(m1, m2).max()
            if mejor > 1e-9:
                fallos_nec += 1
    print(f"V6 bolsillo rigido {{1,t,v}} en 1+t <=> v<=b(t): {casos} valores de t, "
          f"{fallos_suf} fallos de suficiencia, {fallos_nec} de necesidad")
    return fallos_suf == 0 and fallos_nec == 0


# ---------------- V7: teorema end-to-end y familia aproximante ----------------
def V7(muestras=300000, seed=5):
    rng = np.random.default_rng(seed)
    peor, arg, nF = math.inf, None, 0
    for _ in range(muestras):
        t = rng.uniform(0.25, 0.95)
        u = rng.uniform(0.05, t - 1e-9)
        v = rng.uniform(0.05, u)
        if not en_F(t, u, v):
            continue
        nF += 1
        r = rho_gadget(t, u, v)
        if r < peor:
            peor, arg = r, (t, u, v)
    print(f"V7a malla aleatoria de F: {nF} instancias, rho minimo = {peor:.6f} "
          f"> T = {TRIB:.6f}: {peor > TRIB}")
    ok_a = peor > TRIB

    # familia aproximante: t -> t*, u = t - delta, y v el minimo bloqueante
    # (biseccion sobre feas3; la infactibilidad es monotona creciente en v).
    # rho debe bajar hacia T por encima, confirmando que el infimo es T.
    print("V7b familia aproximante (u = t - delta, v = minimo bloqueante + delta/10;")
    print("    el umbral bloqueante sube como sqrt(delta), luego t* - t = sqrt(delta)):")
    ok_b = True
    for delta in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6):
        t = TSTAR - math.sqrt(delta)
        u = t - delta
        lo, hi = 0.0, u
        if feas3(sorted([1.0, u, u], reverse=True), 1 + t):
            print(f"   delta={delta:.0e}: sin bloqueo posible (u = v = {u:.4f})")
            ok_b = False
            continue
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            blo = (u + mid > t) and not feas3(sorted([1.0, u, mid], reverse=True), 1 + t)
            if blo:
                hi = mid
            else:
                lo = mid
        v = hi + delta / 10
        pert = en_F(t, u, v, omega=max(1e-12, (1 - u - v) / 2))
        r = rho_gadget(t, u, v)
        print(f"   delta={delta:.0e}: en F = {pert}, rho = {r:.6f} "
              f"(exceso sobre T = {r - TRIB:+.2e}), v - b(t) = {v - b(t):+.2e}")
        ok_b = ok_b and pert and r > TRIB
    return ok_a and ok_b


# ---------------- V8: instancias conocidas ----------------
def V8():
    print("V8 instancias conocidas normalizadas a r1 = 1:")
    ok = True
    for nombre, r1, w, radios in (
            ("contraejemplo n=4 {10,5,4.9,4.8}", 10.0, 0.3, (5.0, 4.9, 4.8)),
            ("gemela I1 {10,5,4.99,4.50}", 10.0, 0.505, (5.0, 4.99, 4.50))):
        t, u, v = (x / r1 for x in radios)
        omega = w / r1
        pert = en_F(t, u, v, omega)
        r = rho_gadget(t, u, v)
        print(f"   {nombre}: en F = {pert}, rho = {r:.4f} > T: {r > TRIB}")
        ok = ok and pert and r > TRIB
    return ok


if __name__ == "__main__":
    print(f"T = {TRIB:.9f}  t* = 1/T = {TSTAR:.9f}  1/phi = {INVPHI:.9f}")
    print(f"b(t*) = {b(TSTAR):.9f} = 1 - t* = {1 - TSTAR:.9f}  (identidad exacta)")
    print(f"L(t*) = {L(TSTAR):.9f} = T  (identidad exacta)\n")
    res = [V1(), V2V3(), V4(), V5(), V6(), V7(), V8()]
    print(f"\nRESULTADO GLOBAL: {sum(res)}/{len(res)} bloques verificados"
          + ("  -- TODO OK" if all(res) else "  -- HAY FALLOS"))
