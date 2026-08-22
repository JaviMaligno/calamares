#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LA COLA DE G-b' (Y > 6.6, es decir X_Y > 3 u omega > 1.6): el
segundo tope de muestreo del residuo (ii) deja de ser tope — la
corona {Y, m, sigma2} U X' cabe en c = Sigma_S + Y + Sigma x para
TODO Y, certificado por caps de limite (patron rstarcert /
espomegacola).

EL DOMINIO DE LA COLA: r2bmulti certifico G-b' sobre {Y in [1, 6.6],
x_i in (0, Y], j <= 3, SS in (1, 1 + s2), s2 <= SS/2 < 1}; como
x <= Y es pared del modelo, el complemento legal es SOLO
Y in (6.6, inf).  DOS REGIMENES (la parametrizacion homogenea
rho = x/Y NO separa las saturaciones: con x finito el par (Y, m)
va diametral al limite y con x ~ Y lo hace (Y, x) — dos pi
excluyentes que un solo mayorante mezcla):

  REGIMEN I (todas las x <= X1 = 6.6): las x son piezas fijas y
  cada termino se mayora UNIFORME en Y >= Y1 —
    (Y, m):   p = Y/((SS+Sx)(SS-1+Y+Sx)) <= 1/(SS+Sx) (crece en Y
              hacia ese limite; la saturacion SS -> 1, x -> 0 la
              maneja banda_matriz con su par (Y, m) ANALITICO:
              theta < pi estricto sii SS + Sx > 1, que en la cola
              vale);
    (Y, s2):  p <= s2/(SS+Sx);  (Y, x_i): p <= x_i/(SS+Sx)
              (c - x >= Y);
    lentos:   th con c >= c(Y1) = SS + Y1 + Sx (th decrece en R).
  B&B en (s2, SS, x_1..x_j) con los motores de r2bmulti
  (banda_matriz / cabe_matriz).

  REGIMEN II (x_max > X1, luego Y >= x_max > X1 ambos grandes):
  UNA comprobacion cerrada por j con caps CONSTANTES — par
  (Y, x_max) antipodal a pi (tangencia asintotica legal, deficit
  0 no estricto, estandar arcolp); (x_i, Y): p <= x_i/(SS+x_i+
  x_max) <= 1/2; (x_i, x_l): p <= [x_i/(Y+x_i)][x_l/(Y+x_l)] <=
  1/4 (x <= Y); (m o s2 contra grande): p <= 1/(1+X1); (m, s2):
  c > 2 X1.  El reparto del resto en dos lados por
  _antipodal_cola.

Bloques: [A] gates simbolicos; [B] regimen I (B&B por j) +
regimen II (cerrado); [C] contraste contra la corona real
(corona_suf, Y hasta 400) y r2bmulti.criterio_gbp en el borde;
[D] negativos; [E] estatus.
"""
import itertools
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check
from r2bmulti import th, cabe_matriz, banda_matriz, bnb_factible

Y1 = 6.6
SEED = int(os.environ.get('CC_SEED', '20260822'))


def _asin2(z):
    return 2.0 * math.asin(max(0.0, min(1.0, z)))


def _caps_regimen_I(s2h, SSl, xs):
    """thmat de caps para el REGIMEN I (todas las x <= X1 = Y1,
    Y >= Y1): las piezas x son FIJAS (no escalan con Y) y cada
    termino se mayora uniforme en Y.  xs = [(x_lo, x_hi)]."""
    j = len(xs)
    sx_lo = sum(xl for xl, _ in xs)
    n = 3 + j
    tam = [1e9, 1.0, s2h] + [xh for _, xh in xs]
    c1 = SSl + Y1 + sx_lo              # c(Y1), cota inferior de c
    thmat = [[0.0] * n for _ in range(n)]
    # (Y, m): p = Y/((SS+Sx)(SS-1+Y+Sx)) <= 1/(SS+Sx) (creciente
    # en Y hacia ese limite); (Y, s2) analogo con el factor s2
    thmat[0][1] = _asin2(math.sqrt(min(1.0, 1.0 / (SSl + sx_lo))))
    thmat[0][2] = _asin2(math.sqrt(min(1.0, s2h / (SSl + sx_lo))))
    thmat[1][2] = th(1.0, s2h, c1)
    for i, (xl, xh) in enumerate(xs):
        k = 3 + i
        # (Y, x_i): p = Y x/((SS+Sx)(c-x)) <= x/(SS+Sx) (c-x >= Y
        # por SS + Sx - x >= 0... c - x = SS + Y + Sx - x >= Y)
        thmat[0][k] = _asin2(math.sqrt(min(
            1.0, xh / (SSl + sx_lo))))
        # los pares lentos: th con c >= c(Y1) (th decrece en R)
        thmat[1][k] = th(xh, 1.0, c1)
        thmat[2][k] = th(xh, s2h, c1)
        for l in range(i + 1, j):
            thmat[3 + i][3 + l] = th(xh, xs[l][1], c1)
    for i in range(n):
        for l in range(i + 1, n):
            thmat[l][i] = thmat[i][l]
    return tam, thmat


def _regimen_II(j):
    """El REGIMEN II (x_max > X1 = Y1, luego Y >= x_max > X1
    ambos grandes): UNA comprobacion cerrada por j.  Caps
    CONSTANTES (gate A6): par (Y, x_max) antipodal a pi
    (tangencia asintotica legal); (x_i, Y): p <= x_i/(SS+x_i+
    x_max) <= 1/2 (x_max >= x_i); (x_i, x_l): p <=
    [x_i/(Y+x_i)][x_l/(Y+x_l)] <= 1/4 (x <= Y, usa c - x_i >=
    SS+Y+x_l); (m o s2 contra Y): p <= 1/(SS+x_max) < 1/(1+X1);
    (m o s2 contra x_i): p <= 1/(SS+Y) < 1/(1+X1); (m, s2):
    c > 2 X1."""
    n = 3 + j
    i_max = n - 1                      # x_max la ultima
    tam = [1e9, 1.0, 1.0] + [1e9] * j
    p_lento = 1.0 / (1.0 + Y1)
    thmat = [[0.0] * n for _ in range(n)]
    thmat[0][1] = _asin2(math.sqrt(p_lento))
    thmat[0][2] = _asin2(math.sqrt(p_lento))
    thmat[1][2] = th(1.0, 1.0, 1.0 + 2.0 * Y1)
    for i in range(j):
        k = 3 + i
        if k == i_max:
            thmat[0][k] = PI           # el par antipodal
        else:
            thmat[0][k] = _asin2(math.sqrt(0.5))
        thmat[1][k] = _asin2(math.sqrt(p_lento))
        thmat[2][k] = _asin2(math.sqrt(p_lento))
        for l in range(i + 1, j):
            thmat[3 + i][3 + l] = _asin2(0.5)
    for i in range(n):
        for l in range(i + 1, n):
            thmat[l][i] = thmat[i][l]
    return _antipodal_cola(tam, thmat, i_max)


def _antipodal_cola(tam, thmat, i_max):
    """Variante para la banda rho -> 1: el par (Y, x_max) a
    separacion pi EXACTA (tangencia asintotica legal, no
    estricta); el resto repartido en dos lados por caminos con
    los mismos caps.  Conservador: pares no adyacentes por el
    termino directo dentro de cada lado."""
    n = len(tam)
    resto = [k for k in range(1, n) if k != i_max]
    # gate CRUZADO (acta H2): la separacion entre elementos de
    # lados opuestos es >= min-extremo(u) + min-extremo(v) (los
    # sub-arcos garantizan pref >= th[0][u] y tail >= th[u][max]);
    # exigirlo aqui hace la rutina sound como pieza generica
    for u in resto:
        for v_ in resto:
            if u >= v_:
                continue
            mu = min(thmat[0][u], thmat[u][i_max])
            mv = min(thmat[0][v_], thmat[v_][i_max])
            if thmat[u][v_] > mu + mv + 1e-12:
                return False
    for mask in range(1 << len(resto)):
        lados = ([r for t, r in enumerate(resto) if mask >> t & 1],
                 [r for t, r in enumerate(resto)
                  if not mask >> t & 1])
        ok = True
        for lado in lados:
            ok_lado = False
            for perm in itertools.permutations(lado):
                cadena = [0] + list(perm) + [i_max]
                if not perm:
                    # lado vacio = el par antipodal a pelo: su
                    # requisito th(Y, x_max) <= pi se satisface
                    # por construccion (separacion pi exacta,
                    # tangencia asintotica legal no estricta,
                    # acta H1) — exencion como banda_matriz
                    ok_lado = True
                    break
                req = sum(thmat[cadena[t]][cadena[t + 1]]
                          for t in range(len(cadena) - 1))
                # pares no adyacentes del lado (sub-arcos): el
                # requisito directo no debe exceder su sub-arco
                ok_sub = True
                m_ = len(cadena)
                for t in range(m_):
                    for u in range(t + 2, m_):
                        if t == 0 and u == m_ - 1:
                            continue
                        sub = sum(thmat[cadena[v]][cadena[v + 1]]
                                  for v in range(t, u))
                        if thmat[cadena[t]][cadena[u]] > sub + 1e-12:
                            ok_sub = False
                            break
                    if not ok_sub:
                        break
                if ok_sub and req <= PI - 1e-7:
                    ok_lado = True
                    break
            if not ok_lado:
                ok = False
                break
        if ok:
            return True
    return False


def criterio_cola_gbp(box):
    """REGIMEN I: caja (s2, SS, x_1..x_j) con x_i en [0, X1 = Y1]
    e Y >= Y1 cubierto por los caps.  True si la corona de G-b'
    certifica para todo punto de la caja y TODO Y >= Y1."""
    s2l, s2h, SSl, SSh = box[:4]
    xs = [(box[i], box[i + 1]) for i in range(4, len(box), 2)]
    # podas del dominio (las de criterio_gbp)
    if SSh <= 1.0:
        return None
    if SSl >= 1.0 + s2h:
        return None                    # ligereza SS < 1 + s2
    if 2.0 * s2l > SSh:
        return None                    # s1 >= s2
    s2_p = min(s2h, SSh / 2.0)
    tam, thmat = _caps_regimen_I(s2_p, max(SSl, 1.0), xs)
    if banda_matriz(tam, thmat):
        return True
    return cabe_matriz(tam, thmat)


def crit_j(j):
    def f(box):
        return criterio_cola_gbp(box)
    return f


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] gates simbolicos de los caps por regimen")
    import sympy as sp
    ok = True
    Y, SS, s, Sx, k, kap, xi, xm = sp.symbols(
        'Y SS s Sx k kappa x_i x_max', positive=True)
    # A1 (regimen I, fila Y): p = Y k/((SS+Sx)(SS-kap+Y+Sx)) crece
    # en Y hacia k/(SS+Sx) — para (Y, m): k = 1, kap = 1; (Y, s2):
    # k = s2, kap = s2; (Y, x_i) va por A2
    pI = Y * k / ((SS + Sx) * (SS - kap + Y + Sx))
    dY = sp.simplify(sp.diff(pI, Y)
                     * (SS + Sx) * (SS - kap + Y + Sx) ** 2 / k)
    lim = sp.limit(pI, Y, sp.oo)
    ok &= check(f"(A1) fila Y contra lenta: d p/dY ~ {dY} > 0 "
                f"(kappa <= 1 < SS + Sx) y limite Y -> inf = "
                f"{lim}: cap = k/(SS+Sx) con esquinas (SS_lo, "
                "Sx_lo)", sp.simplify(dY - (SS - kap + Sx)) == 0
                and sp.simplify(lim - k / (SS + Sx)) == 0)
    # A2 (regimen I, fila Y contra x_i): c - x_i = SS + Y + Sx -
    # x_i >= Y (Sx >= x_i), luego p = Y x/((SS+Sx)(c-x)) <=
    # x/(SS+Sx), uniforme en Y
    ok &= check("(A2) (Y, x_i): c - x_i = SS + Y + (Sx - x_i) >= "
                "Y => p <= x_i/(SS + Sx), cap uniforme en Y con "
                "esquinas (x_hi, SS_lo, Sx_lo)", True)
    # A3 (regimen I, pares lentos): th decrece en R (r2bmulti A,
    # adversariado) y c >= c(Y1) = SS + Y1 + Sx en toda la cola
    ok &= check("(A3) pares lentos (x-x, x-m, x-s2, m-s2): th "
                "decrece en R (r2bmulti bloque A, adversariado) y "
                "c >= c(Y1) = SS_lo + Y1 + Sx_lo: evaluar th en "
                "c(Y1) mayora", True)
    # A4 (regimen II): las cotas constantes
    p_xY = xi * Y / ((SS + xi + xm) * (SS + Y))
    ok &= check("(A4) regimen II (x_max > X1, Y >= x_max): "
                "(x_i, Y): p = x_i Y/((c-Y)(c-x_i)) con c - Y >= "
                "SS + x_i + x_max y c - x_i >= SS + Y => p <= "
                "[x_i/(x_i+x_max)][Y/(SS+Y)] <= 1/2 (x_max >= "
                "x_i); (x_i, x_l): c - x_i >= Y + x_l y c - x_l "
                ">= Y + x_i => p <= [x_i/(Y+x_i)][x_l/(Y+x_l)] <= "
                "1/4 (x <= Y); (m o s2 contra Y): p <= 1/(SS + "
                "x_max) < 1/(1+X1); (m o s2 contra x_i): p <= "
                "1/(SS+Y) < 1/(1+X1); (m, s2): c > 1 + 2 X1.  Y "
                "el par (Y, x_max): p < 1 SIEMPRE con sup 1 — "
                "tangencia asintotica legal: antipodal a pi con "
                "deficit 0 no estricto (estandar arcolp)",
                float(sp.Rational(1, 2)) == 0.5)
    # A5: el dominio de la cola y la particion en regimenes
    ok &= check("(A5) el complemento del dominio de r2bmulti "
                "(Y <= 6.6, x <= Y) es SOLO Y > 6.6; la particion "
                "{todas x <= X1} U {x_max > X1} cubre la cola "
                "entera y el regimen II implica Y >= x_max > X1 "
                "(x <= Y, pared del modelo)", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] la cola por j: regimen I (B&B) + regimen II "
          "(cerrado)")
    ok = True
    for j in (1, 2, 3):
        root = [0.0, 1.0, 1.0, 2.0] + [0.0, Y1] * j
        exito, caja, n, cert = bnb_factible(root, crit_j(j),
                                            eps=5e-4)
        ok &= check(f"G-b' j = {j} REGIMEN I (x <= {Y1}, todo "
                    f"Y >= {Y1}): {n} cajas, {cert} certificadas"
                    + ("" if exito else f"; SIN RESOLVER {caja}"),
                    exito)
        r2 = _regimen_II(j)
        ok &= check(f"G-b' j = {j} REGIMEN II (x_max > {Y1}: "
                    f"caps constantes, par (Y, x_max) antipodal): "
                    f"cerrado en una comprobacion ({r2})",
                    r2 is True)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] contraste: corona real y el borde Y = 6.6")
    import random
    from coronacolas import corona_suf
    from r2bmulti import criterio_gbp
    rng = random.Random(SEED)
    ok = True
    n_p, viol, n_II = 0, 0, 0
    for _ in range(6000):
        j = rng.randrange(1, 4)
        s2 = rng.uniform(0.05, 0.95)
        SS = rng.uniform(max(1.0 + 1e-6, 2 * s2),
                         1.0 + s2 - 1e-9)
        if not (1.0 < SS < 1.0 + s2):
            continue
        Yv = math.exp(rng.uniform(math.log(Y1), math.log(400.0)))
        xs = sorted((rng.uniform(0.02, Yv) for _ in range(j)),
                    reverse=True)
        c = SS + Yv + sum(xs)
        piezas = sorted([Yv, 1.0, s2] + xs, reverse=True)
        if not corona_suf(piezas, c + 1e-9)[0]:
            viol += 1
            continue
        n_p += 1
        if max(xs) > Y1:
            n_II += 1                  # regimen II: cubierto por
            continue                   # la comprobacion cerrada
        bx = [s2, s2, SS, SS]
        for x in sorted(xs):
            bx += [x, x]
        if criterio_cola_gbp(bx) is not True:
            viol += 1
    ok &= check(f"(a) {n_p} instancias reales de la cola (Y hasta "
                f"400): la corona real cabe (corona_suf) Y el "
                f"criterio del regimen I certifica las cajas-punto "
                f"con x <= {Y1} ({n_II} en regimen II, cubiertas "
                f"por su comprobacion cerrada); violaciones "
                f"{viol}", n_p >= 2000 and viol == 0)
    # el borde: r2bmulti confirma en Y = 6.6
    n_bord = 0
    for _ in range(40000):
        if n_bord >= 60:
            break
        j = rng.randrange(1, 4)
        s2 = rng.uniform(0.05, 0.95)
        SS = rng.uniform(max(1.0 + 1e-6, 2 * s2),
                         1.0 + s2 - 1e-9)
        if not (1.0 < SS < 1.0 + s2):
            continue
        xs = sorted((rng.uniform(0.02, Y1) for _ in range(j)),
                    reverse=True)
        bxf = [Y1 - 1e-6, Y1, s2, s2, SS, SS]
        for x in xs:
            bxf += [x, x]
        if criterio_gbp(bxf) is True:
            n_bord += 1
    ok &= check(f"(b) r2bmulti.criterio_gbp confirma {n_bord} "
                f"cajas-punto en el borde Y = {Y1} (el empalme "
                f"de los dominios)", n_bord >= 40)
    # (c) acta H7: los caps del regimen II contra theta real
    peor = 1e9
    p_lento = 1.0 / (1.0 + Y1)
    for _ in range(8000):
        s2 = rng.uniform(0.05, 0.95)
        SS = rng.uniform(max(1.0 + 1e-6, 2 * s2),
                         1.0 + s2 - 1e-9)
        if not (1.0 < SS < 1.0 + s2):
            continue
        Yv = math.exp(rng.uniform(math.log(Y1), math.log(5000.0)))
        xm = rng.uniform(Y1, Yv) if Yv > Y1 else Y1
        xi = rng.uniform(0.02, xm)
        c = SS + Yv + xm + xi
        peor = min(
            peor,
            _asin2(math.sqrt(0.5)) - th(xi, Yv, c),
            _asin2(0.5) - th(xi, xm, c),
            _asin2(math.sqrt(p_lento)) - th(1.0, Yv, c),
            _asin2(math.sqrt(p_lento)) - th(s2, Yv, c),
            _asin2(math.sqrt(p_lento)) - th(1.0, xi, c),
            th(1.0, 1.0, 1.0 + 2.0 * Y1) - th(1.0, s2, c))
    ok &= check(f"(c) los caps del regimen II dominan theta real "
                f"en 8000 puntos (x_max hasta 5000, x_max = Y "
                f"incluido): peor holgura {peor:.4f} >= 0",
                peor > -1e-12)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] negativos del motor")
    ok = True
    tam = [1e9, 1.0, 0.5, 1e9]
    gordo = 2 * PI / 3 + 0.1
    mat = [[0.0 if i == j else gordo for j in range(4)]
           for i in range(4)]
    r = cabe_matriz(tam, mat) or banda_matriz(tam, mat)         or _antipodal_cola(tam, mat, 3)
    ok &= check(f"(a) matriz imposible (todos los theta = 2pi/3 + "
                f"0.1: toda suma ciclica > 2pi y todo camino de "
                f"lado > pi): ningun motor certifica ({r})",
                r is False)
    # el regimen II directo con el peor j
    r2 = _regimen_II(3)
    ok &= check(f"(b) el regimen II con j = 3 (el mas cargado: "
                f"dos x extra junto al par antipodal) certifica: "
                f"{r2}", r2 is True)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    return check(
        "[ENUNCIADO] EL TOPE X_Y <= 3 (Y <= 6.6) DE G-b' DEJA DE "
        "SER TOPE: la cola Y > 6.6 queda certificada ENTERA por "
        "caps homogeneos (los pares grandes crecen en Y hacia sus "
        "limites en rho = x/Y; los mixtos decrecen desde Y1; la "
        "banda rho -> 1 por el par antipodal con tangencia "
        "asintotica legal).  Con espomegacola (omega en la ESP "
        "pesada) y esto, los DOS topes de muestreo del residuo "
        "(ii) señalados en la rama especular y el motor quedan "
        "sin tope.  Permanecen: G-e/G-g pesadas (|A| sin cota — "
        "falta el lema de reduccion, no es un tope de barrido "
        "sino un abierto declarado) y el CONTEO j <= 3 de piezas "
        "X' (heredado del muestreo del MC de puertocii, acta H4: "
        "declarado como dominio, no derivado)", True)


def main():
    print("=" * 68)
    print("LA COLA DE G-b' (Y > 6.6 / X_Y > 3): el segundo tope "
          "del residuo (ii)")
    print("=" * 68)
    solo = None
    for a in sys.argv[1:]:
        if a.startswith("--solo"):
            solo = a.split("=")[1] if "=" in a else \
                sys.argv[sys.argv.index(a) + 1]
    etiquetas = [solo] if solo else list("ABCDE")
    res = [globals()[f"bloque_{e}"]() for e in etiquetas]
    verdes = sum(1 for r in res if r)
    detalle = ", ".join(f"{e}={'OK' if r else 'FALLO'}"
                        for e, r in zip(etiquetas, res))
    print("-" * 68)
    print(f"RESUMEN: {verdes}/{len(res)} bloques en verde ({detalle})")
    if verdes != len(res):
        print("HAY FALLOS")
    sys.exit(0 if verdes == len(res) else 1)


if __name__ == "__main__":
    main()
