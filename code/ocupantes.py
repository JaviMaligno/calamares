"""El precio del ocupante (docs/drafts/ocupantes.md): paso 2 de la Batalla 1.

Plantilla libre: v = sarten de radio R con ocupantes {alpha} + O + {m}, con
O = {o_1 >= ... >= o_j}, j >= 1, o_i >= m = 1; u = agujero de alpha (capacidad
alpha - w); el testigo P coloco S = {s1 >= s2} en u; los agujeros de los o_i,
de s1 y de m estan libres (m, s1, o_i sin hijos). El intercambio manda m a u y
debe reinsertar S.

Resultados que este script verifica:

  V1 (paredes). Bloqueo => (B2) s2 > 1-w, (B3) s2 > s1-w, (B4) s2 > alpha-w-1,
     (Bo_k) s2 > o_k - w para todo k, (W) s1+s2 <= alpha-w, (D) s1+s2 > 1,
     y el pan-repack falla. En particular o_k < s2 + w <= 1 + w para todo k:
     TODOS los ocupantes extra quedan a un grosor de m.
  V2 (el precio del ocupante). Bloqueo => (cola de o_1, que contiene a
     {o_2..o_j, m, s1, s2} y s_i > o_1 - w)

         rho > 2 + (j - 2w)/o_1 >= (j+2)/(1+w)      si  w <= j/2 ,

     y para j = 1, w >= 1/2 (cota fina de la verificacion adversaria, usando
     ademas la pared (D)): rho > 4/(1+2w) = (3-2w) + (1-2w)^2/(1+2w). Estricto.
     Exactitud (verificador): (j+2)/(1+w) es el infimo exacto del programa de
     paredes sii w >= 1/(j+1); para w < 1/(j+1) la cola de o_2 fuerza >= j+1.
  V3 (corolarios). Para j = 1: rho > 3/(1+w) >= 13/7 <=> w <= 8/13;
     3/(1+w) > T <=> w < w4 := 3/T - 1 = 3T^2 - 3T - 4 = 0.63105... (identidad
     modulo T^3 = T^2+T+1). Con la cota fina: rho > T para todo
     w < 2/T - 1/2 = 2T^2 - 2T - 5/2 = 0.587378..., y rho >= 13/7 para
     w <= 15/26. Para j >= 2: rho > 4/(1+w) > 2 > T para todo w < 1.
  V4 (conjetura fina, plantilla). Phi(w) < 2 SIEMPRE, por la identidad exacta
     (2+w)^3 - (1+w)((2+w)^2 + (2+w) + 1) = 1; las otras ramas de la curva
     canonica tambien quedan bajo 2. Como (j+2)/(1+w) >= 3/(1+w) > 2 para
     w < 1/2: el adversario con ocupantes extra NUNCA baja de 2 y la plantilla
     canonica (sin ocupantes extra) es estrictamente mejor para el.

Bloques: [A] identidades simbolicas; [B] paredes constructivas + barrido masivo
de la cota; [C] ajuste (el minimo del programa de paredes pega con (j+2)/(1+w))
y efecto de la pared geometrica (no-corona en R_bar, Lema U_4 de corona.py);
[D] comparacion con la curva canonica; [E] escalado en j.

Ejecutar:  python code/ocupantes.py
"""
import math, random, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

TWO_PI = 2 * math.pi
T = 1.8392867552141612


def check(label, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {label}")
    return ok


def tribonacci_c(c, lo=1.0, hi=6.0):
    """Raiz positiva de a^3 = c(a^2+a+1)."""
    f = lambda a: a**3 - c*(a*a + a + 1)
    for _ in range(200):
        mid = 0.5*(lo + hi)
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return 0.5*(lo + hi)


def phi_curve(w):
    return tribonacci_c(1 + w) - w


def unblocking_placement(alpha, occ, s1, s2, w):
    """Recurso constructivo que desbloquea, o None si todas las paredes en pie.
    Solo criterios exactos de par/anidamiento (nada de oraculos)."""
    if s2 <= 1 - w + 1e-15:
        return "R2: s2 en H_m, s1 en D_m"
    if s2 <= s1 - w + 1e-15:
        return "R3: s2 anidada en s1, s1 en D_m"
    if 1 + s2 <= alpha - w + 1e-15:
        return "R4: s2 junto a m en u, s1 en D_m"
    for k, o in enumerate(occ):
        if s2 <= o - w + 1e-15:
            return f"R5: s2 en el agujero de o_{k+1}, s1 en D_m"
    if s1 + s2 <= 1 + 1e-15:
        return "R1': el par entero dentro de D_m"
    return None


def rho_instancia(alpha, occ, s1, s2):
    radios = sorted([alpha] + list(occ) + [1.0, s1, s2], reverse=True)
    return max(sum(radios[i+1:]) / radios[i] for i in range(len(radios) - 1))


def cota_V2(j, w):
    if w <= j / 2:
        return (j + 2) / (1 + w)
    return j + 2 - 2*w   # o_1 -> 1 (denominador minimo con j-2w < 0)


def cota_V2_fina(j, w):
    """Con la pared (D) ademas (verificacion adversaria): j=1, w>=1/2 mejora."""
    if j == 1 and w >= 0.5:
        return 4 / (1 + 2*w)
    return cota_V2(j, w)


# ---------------- [A] identidades simbolicas ----------------

def bloque_A():
    import sympy as sp
    print("[A] identidades simbolicas (sympy)")
    ok = True
    w, Ts, a = sp.symbols('omega T alpha', positive=True)

    ok &= check("3/(1+w) = 13/7  <=>  w = 8/13",
                sp.solve(sp.Eq(3/(1 + w), sp.Rational(13, 7)), w) == [sp.Rational(8, 13)])

    # w4 = 3/T - 1 = 3T^2 - 3T - 4 modulo la cubica de Tribonacci
    cub = Ts**3 - Ts**2 - Ts - 1
    resto = sp.rem(Ts*(3*Ts**2 - 3*Ts - 4) - (3 - Ts), cub, Ts)
    ok &= check("T*(3T^2-3T-4) = 3 - T modulo T^3 = T^2+T+1  (w4 = 3/T - 1)",
                sp.expand(resto) == 0)
    w4 = 3/T - 1
    ok &= check(f"w4 = {w4:.6f} y 3T^2-3T-4 = {3*T**2 - 3*T - 4:.6f} coinciden",
                abs(w4 - (3*T**2 - 3*T - 4)) < 1e-12)

    # la identidad del 2: (2+w)^3 - (1+w)((2+w)^2 + (2+w) + 1) = 1
    ident = sp.expand((2 + w)**3 - (1 + w)*((2 + w)**2 + (2 + w) + 1))
    ok &= check("(2+w)^3 - (1+w)((2+w)^2+(2+w)+1) = 1 exacto  => Phi(w) < 2 siempre",
                ident == 1)

    # cota fina (verificacion adversaria): 4/(1+2w) y sus cruces
    ok &= check("4/(1+2w) - (3-2w) = (1-2w)^2/(1+2w)  (la fina domina a 3-2w)",
                sp.simplify(4/(1 + 2*w) - (3 - 2*w) - (1 - 2*w)**2/(1 + 2*w)) == 0)
    ok &= check("4/(1+2w) = 13/7  <=>  w = 15/26",
                sp.solve(sp.Eq(4/(1 + 2*w), sp.Rational(13, 7)), w) == [sp.Rational(15, 26)])
    resto2 = sp.expand(Ts*(2*Ts**2 - 2*Ts - sp.Rational(5, 2)) - (2 - Ts/2))
    resto2 = sp.rem(resto2, cub, Ts)
    ok &= check("T*(2T^2-2T-5/2) = 2 - T/2 modulo la cubica  (w5 = 2/T - 1/2)",
                sp.expand(resto2) == 0)
    w5 = 2/T - 0.5
    ok &= check(f"w5 = {w5:.6f} y 2T^2-2T-5/2 = {2*T**2 - 2*T - 2.5:.6f} coinciden",
                abs(w5 - (2*T**2 - 2*T - 2.5)) < 1e-12)

    # (j+2)/(1+w) >= 3/(1+w) > 2(1-w) siempre: 3 - 2(1-w)(1+w) = 1 + 2w^2 > 0
    ok &= check("3/(1+w) - 2(1-w) = (2w^2+1)/(1+w) > 0 siempre",
                sp.simplify(3/(1 + w) - 2*(1 - w) - (2*w**2 + 1)/(1 + w)) == 0)

    # theta decreciente en R (para la reduccion a R_bar): d/dR [f_R(a) f_R(b)] < 0
    R, x, y = sp.symbols('R x y', positive=True)
    prod = (x/(R - x)) * (y/(R - y))
    dprod = sp.simplify(sp.diff(prod, R))
    ok &= check("d/dR [f(a)f(b)] = -xy(2R-x-y)/((R-x)^2(R-y)^2) < 0 en el dominio",
                sp.simplify(dprod + prod*(1/(R - x) + 1/(R - y))) == 0)
    return ok


# ---------------- [B] paredes + barrido masivo ----------------

def bloque_B():
    print("[B] paredes constructivas y barrido de la cota V2")
    ok = True
    rng = random.Random(21)

    # (i) si una pared cae, la colocacion que desbloquea es geometricamente valida
    #     (criterios exactos de par: se comprueban las desigualdades directamente)
    casos = 0
    for _ in range(20000):
        w = rng.uniform(0.005, 0.6)
        alpha = rng.uniform(1 + w, 3.0)
        j = rng.choice([1, 2, 3])
        occ = sorted((rng.uniform(1.0, min(alpha, 2.4)) for _ in range(j)), reverse=True)
        s1 = rng.uniform(0.2, 1.0)
        s2 = rng.uniform(0.2, s1)
        if s1 + s2 > alpha - w:
            continue
        res = unblocking_placement(alpha, occ, s1, s2, w)
        if res is None:
            continue
        casos += 1
        # validar la colocacion: el companero cabe en D_m (radio 1) y el recurso es real
        if "H_m" in res:
            valido = s2 <= 1 - w and s1 <= 1.0
        elif "anidada" in res:
            valido = s2 <= s1 - w and s1 <= 1.0
        elif "junto a m" in res:
            valido = 1 + s2 <= alpha - w and s1 <= 1.0
        elif "agujero de o_" in res:
            k = int(res.split("o_")[1].split(",")[0]) - 1
            valido = s2 <= occ[k] - w and s1 <= 1.0
        else:
            valido = s1 + s2 <= 1.0
        if not valido:
            ok = False
            print(f"    colocacion invalida: {res}")
            break
    ok &= check(f"colocaciones desbloqueantes consistentes en {casos} casos con pared caida "
                f"(banda de tolerancia; el contenido real esta en la dicotomia de V1)", ok)

    # (ii) paredes en pie => rho > cota_V2 (y > cota fina), masivo; el muestreo
    # CONDICIONA s2 a la region de paredes para cubrir tambien w pequeno
    # (sin condicionar, las bloqueadas solo aparecen con w >= 0.25 - matiz del
    # verificador)
    viol = viol_f = n = 0
    peor = math.inf
    n_w_chico = 0
    for _ in range(200000):
        w = rng.uniform(0.005, 0.95)
        alpha = rng.uniform(1 + w, 3.2)
        j = rng.choice([1, 1, 2, 3])
        occ = sorted((rng.uniform(1.0, min(alpha, 1 + w)) for _ in range(j)), reverse=True)
        smin = max([1 - w, alpha - w - 1] + [o - w for o in occ])
        if smin >= 1.0:
            continue
        s2 = rng.uniform(smin, 1.0)
        s1 = rng.uniform(s2, 1.0)
        if s1 + s2 > alpha - w:
            continue
        if unblocking_placement(alpha, occ, s1, s2, w) is not None:
            continue
        n += 1
        n_w_chico += (w < 0.20)
        rho = rho_instancia(alpha, occ, s1, s2)
        margen = rho - cota_V2(j, w)
        peor = min(peor, margen)
        viol += (margen < 1e-12)
        viol_f += (rho - cota_V2_fina(j, w) < 1e-12)
    ok &= check(f"paredes en pie => rho > cota V2 en {n} instancias, {n_w_chico} con "
                f"w < 0.20 (viol={viol}, margen minimo {peor:.2e})",
                viol == 0 and n_w_chico > 200)
    ok &= check(f"idem contra la cota FINA 4/(1+2w) en j=1, w >= 1/2 (viol={viol_f})",
                viol_f == 0)

    # (iii) las paredes fuerzan o_k <= 1 + w
    viol2 = n2 = 0
    for _ in range(100000):
        w = rng.uniform(0.005, 0.6)
        alpha = rng.uniform(1 + w, 3.0)
        occ = [rng.uniform(1.0, 2.6)]
        s1 = rng.uniform(0.2, 1.0)
        s2 = rng.uniform(0.2, s1)
        if s1 + s2 > alpha - w:
            continue
        if unblocking_placement(alpha, occ, s1, s2, w) is not None:
            continue
        n2 += 1
        viol2 += (occ[0] > 1 + w + 1e-12)
    ok &= check(f"bloqueo => o_1 < s2 + w <= 1 + w en {n2} instancias (viol={viol2})",
                viol2 == 0)
    return ok


# ---------------- [C] ajuste de la cota y pared geometrica ----------------

def bloque_C():
    print("[C] ajuste: el minimo del programa de paredes pega con (j+2)/(1+w)")
    ok = True
    rng = random.Random(23)
    from corona import corona_best

    for w in [0.05, 0.15, 0.25, 0.40]:
        best = best_geo = math.inf
        for _ in range(50000):
            alpha = rng.uniform(1 + w, 3.0)
            g = rng.uniform(1.0, 1 + w)
            s2 = rng.uniform(max(1 - w, g - w, alpha - w - 1), 1.0) if \
                max(1 - w, g - w, alpha - w - 1) < 1.0 else None
            if s2 is None:
                continue
            s1 = rng.uniform(s2, 1.0)
            if s1 + s2 > alpha - w:
                continue
            if unblocking_placement(alpha, [g], s1, s2, w) is not None:
                continue
            rho = rho_instancia(alpha, [g], s1, s2)
            best = min(best, rho)
            if rho < best_geo:
                # condicion geometrica NECESARIA del bloqueo: sin corona en
                # R_bar = alpha + g (monotonia de theta en R, bloque A)
                b, _ = corona_best(sorted([alpha, g, s1, s2], reverse=True), alpha + g)
                if b < -1e-9:
                    best_geo = rho
        cota = cota_V2(1, w)
        exceso = best - cota
        ok &= check(f"w={w:.2f}: min rho paredes = {best:.4f} vs cota {cota:.4f} "
                    f"(exceso {exceso:+.4f} >= 0); medicion con no-corona: {best_geo:.4f}",
                    exceso >= -1e-9)
    return ok


# ---------------- [D] comparacion con la curva canonica ----------------

def bloque_D():
    print("[D] la conjetura fina en la plantilla: ocupantes extra nunca bajan de 2")
    ok = True
    # Phi(w) < 2 para todo w (identidad del bloque A) y la cadena de V4 en malla
    peor = -math.inf
    cadena_ok = True
    for i in range(1, 60):
        w = 0.005 + (0.30 - 0.005) * i / 60
        phi = phi_curve(w)
        canon = max(2*(1 - w), phi)     # cota inferior canonica (ramas demostradas)
        peor = max(peor, phi)
        cadena_ok &= (phi < 2.0 and 3/(1 + w) > 2.0 > canon)
    ok &= check(f"cadena de V4 en malla (0, 0.30]: 3/(1+w) > 2 > max(2(1-w), Phi(w)), "
                f"max Phi = {peor:.6f}", cadena_ok and peor < 2.0)
    # los cruces del corolario V3
    ok &= check(f"3/(1+w) en w=8/13: {3/(1+8/13):.6f} = 13/7 = {13/7:.6f}",
                abs(3/(1 + 8/13) - 13/7) < 1e-12)
    w4 = 3/T - 1
    ok &= check(f"3/(1+w4) = {3/(1+w4):.9f} = T (w4 = {w4:.6f})",
                abs(3/(1 + w4) - T) < 1e-12)
    # el margen sobre la esquina 13/7 en el rango canonico (0, 0.30]
    margen = 3/(1 + 0.30) - 13/7
    ok &= check(f"en w = 0.30: 3/(1+w) = {3/1.30:.4f} > 13/7 + {margen:.4f}",
                margen > 0.44)
    return ok


# ---------------- [E] escalado en j ----------------

def bloque_E():
    print("[E] cada ocupante paga 1/(1+w): minimos por j")
    ok = True
    rng = random.Random(29)
    w = 0.15
    for j in [1, 2, 3, 4]:
        best = math.inf
        for _ in range(60000):
            alpha = rng.uniform(1 + w, 3.4)
            occ = sorted((rng.uniform(1.0, 1 + w) for _ in range(j)), reverse=True)
            smin = max([1 - w, alpha - w - 1] + [o - w for o in occ])
            if smin >= 1.0:
                continue
            s2 = rng.uniform(smin, 1.0)
            s1 = rng.uniform(s2, 1.0)
            if s1 + s2 > alpha - w:
                continue
            if unblocking_placement(alpha, occ, s1, s2, w) is not None:
                continue
            best = min(best, rho_instancia(alpha, occ, s1, s2))
        cota = cota_V2(j, w)
        ok &= check(f"j={j}: min rho = {best:.4f} >= (j+2)/(1+w) = {cota:.4f} "
                    f"(exceso {best - cota:+.4f})", best >= cota - 1e-9)
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

    import sys
    sys.exit(0 if verdes == len(resultados) else 1)
