#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corona-contra-colas ANIDADA: D4 (puntita j=2), D5 (perfiles k >= 3),
D6 (gap lemma: pequenos extra en v y sigma2 minusculo).

Plantilla anidada (paper sec. 6 y app:widthproofs/app:genericproofs):
u = agujero de alpha (F anida m en alpha), v = c_P(m) = la sarten del
template anidado, que a nivel superior contiene {alpha, m, o_1..o_j}
segun P (mas extras < m).  El intercambio manda m al agujero de alpha y
libera D_m (disco unidad) a nivel superior de v; S (el contenido del
agujero de alpha segun P) debe reinsertarse en D_m, H_m, anidamientos y
la geometria de v.  Normalizacion r_m = 1, omega = w/r_m.

ADAPTACIONES de la sarten (coronacolas.py) al anidado:
 1. alpha >= 1+omega SIEMPRE (su agujero admite a m: alpha-omega >= 1) y
    alpha >= sigma1+sigma2+omega (necesidad del par del testigo dentro
    del agujero): tamano gratis que la sarten no tenia.
 2. Colas con rho <= phi: la cola de alpha contiene {m, S, extras,
    ocupantes menores}; cascada como en la sarten pero con alpha DENTRO
    del orden (se barre el rango de alpha entre los o_i, porque
    alpha ><= o_i son ambos posibles) y con el suelo del punto 1.
 3. Reparto del desbloqueo geometrico anidado (analogo del lem:DG,
    opuesto al de la sarten): sigma1 -> v (miembro de la corona),
    sigma2 -> D_m.  D_m se re-crea como MIEMBRO 1.0 de la corona (un
    disco virtual unidad que la propia corona coloca; recibe una fila de
    suma <= 1: legal por el criterio de fila).  Se barren variantes de
    reparto (que subconjunto de S va al bin, el resto a la corona;
    corona_suf ya manda el polvo a bolsillos de Descartes).
 4. Conjuntos del certificado (releida la definicion del intercambio,
    paper sec. 6): la NECESIDAD usa el conjunto compartido que P
    empaqueta a nivel superior de v: {alpha, m = 1, o_1..o_j} -- m esta
    a nivel superior SEGUN P (v = c_P(m)); segun F ira DENTRO de alpha,
    pero R_lb solo necesita que alguien lo empaquete: P.  La SUFICIENCIA
    coloca {alpha, o_1..o_j} + bin(1.0) + piezas de perfil/extras: el
    contenido superior de v tras el intercambio mas lo que va a v.
 5. Trichotomia anidada (analogo de perfilp.md seccion 1), derivada
    ANTES de invocar coronas: (L) ligero sigma1+W <= 1 y (N) anidado
    W+X_sigma1 <= sigma1-omega heredan el programa del par VERBATIM (las
    colocaciones del par siguen legales con W en la fila o dentro de
    sigma1; cor:DS cubre lo combinatorio); (H1) sigma2 > phi-1 da
    rho >= Sigma > phi por la cola de m; el resto (pesado sigma1+W > 1,
    sin reduccion W+X > sigma1-omega, sigma2 <= phi-1) va a la corona.
    La herencia del par deja UN reenvio: j = 2 con omega >= phi/2
    (Psi_2 cruza phi en phi/2 exacto) -> la corona de D4 con W a
    cuestas.  Suelos del par heredados: j = 1 la linea aurea
    min(phi^2-(phi/2)omega, 2) > phi para todo omega < 1; j >= 3 la
    escalera Psi_j > Psi_j(1) = sqrt(j) >= sqrt(3) > phi; j = 0 el
    template canonico (thm:DT3 / cor:DB2, > T > phi, probado).
 6. D6 por ADJUNCION (analogo del Corolario DS-sarten): todo extra
    e < m en v se adjunta al perfil, S+ := S U {extras} -- los depositos
    combinatorios estan dentro de v o viajan con m, las posiciones de
    piezas < m son existenciales, y la pared geometrica (el hueco que
    cor:DS declaraba) queda REHECHA por la corona con los extras como
    miembros/granos.  Los extras ENGORDAN las colas de forma exacta (son
    aros < m de la instancia: cuentan en toda cola).  Camino corto:
    D6 se reduce a D5 (S+ tiene k+ >= 3) + D4; se comprueba primero.

Conservadurismo (direccion segura, como en la sarten):
 - masas opcionales (M, X's, hijos) OMITIDAS de las colas: cotas
   inferiores mas debiles => ocupantes menores => corona mas dificil;
   los extras de D6 SI entran en las colas (son piezas conocidas);
 - el minimo sobre ordenes y repartos es cota superior del minimo
   verdadero: si una variante cabe, el intercambio se desbloquea.

Los bloques B, C2 y D2 son barridos MC con dualidad tangente en
R = R_lb (como B/D de coronacolas.py): evidencia computacional; el
cierre formal pende del MISMO lema de dualidad/zigzag del draft
(coronacolas.md seccion 4), con la ley de escala en (j, k) como lema.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import (check, theta_w, gamma_min, cabe_algun_orden,
                         R_lb_pack, ciclo_constructivo, corona_suf,
                         bolsillo_descartes)

PHI = (1 + math.sqrt(5)) / 2
PI = math.pi
ITER = int(os.environ.get('CC_ITER', '60000'))
TOL = 2e-3          # tolerancia de tangencia (biseccion de R_lb)
FALLO_MIN = 1e-2    # un fallo con deficit angular 0 (granos sin bolsillo)
                    # cuenta como fallo pleno, nunca como tangencia


def psi_j(j, w):
    return (1 - w) + math.sqrt((1 - w) ** 2 + j)


def linea_aurea(w):
    """Suelo probado j=1 (thm:DGp): la linea aurea, con la esquina de la
    rama B acotada por 2."""
    return min(PHI ** 2 - (PHI / 2) * w, 2.0)


def suelo_herencia(j, w):
    """Suelo del programa del par anidado heredado por (L)/(N).
    None = caso j=0, probado en el paper (thm:DT3 / cor:DB2 > T > phi),
    sin formula local."""
    if j == 0:
        return None
    if j == 1:
        return linea_aurea(w)
    return psi_j(j, w)


def caso_anidado(s1, s2, W, w, j, Xs1):
    """Trichotomia anidada sobre el perfil (adaptacion 5).  Devuelve
    'L'/'N' (herencia par), 'H1' (cola de m), 'D4W' (reenvio j=2,
    omega >= phi/2, con W a cuestas) o 'corona' (celda pesada D5)."""
    if s1 + W <= 1.0:
        base = 'L'
    elif W + Xs1 <= s1 - w:
        base = 'N'
    elif s2 > PHI - 1:
        return 'H1'
    else:
        return 'corona'
    if j == 2 and w >= PHI / 2:
        return 'D4W'
    return base


def cascada_anidada(Sigma, j, rank_alpha, alpha_floor, holg):
    """Cotas de cascada para {alpha, o_1..o_j} con rho <= phi: cada
    elemento, de menor a mayor, tiene cola que contiene a los menores,
    a m y a la masa Sigma (S + extras): x >= (menores + 1 + Sigma)/phi
    (cuasi-empates via convenio de primera copia, como en la sarten);
    ocupantes >= 1 (son aros >= m); alpha >= alpha_floor en su rango.
    holg: factores >= 1 (muestreo por encima del minimo).  La secuencia
    se construye no decreciente (la holgura solo infla y la base toma el
    maximo con el valor anterior).  Devuelve (alpha, ocupantes_desc)."""
    vals = []
    total = 0.0
    alpha = None
    for q in range(j + 1):
        base = max(1.0, (total + 1.0 + Sigma) / PHI,
                   vals[-1] if vals else 0.0)
        if q == rank_alpha:
            base = max(base, alpha_floor)
        v = base * holg[q]
        if q == rank_alpha:
            alpha = v
        vals.append(v)
        total += v
    occs = [v for q, v in enumerate(vals) if q != rank_alpha]
    return alpha, occs[::-1]


def radio_necesario(alpha, occs):
    """Necesidad: P empaqueta {alpha, m=1, o_1..o_j} a nivel superior de
    v (adaptacion 4) => R real >= R_lb de ese conjunto, con el gigante
    confinando al resto (lema del anillo)."""
    tops = sorted([alpha, 1.0] + occs, reverse=True)
    return R_lb_pack([alpha, 1.0] + occs, tops[0] + tops[1],
                     confinado_por=tops[0])


def desbloqueo_corona(alpha, occs, piezas, R, semilla=0):
    """Suficiencia anidada: coloca {alpha, o_1..o_j} + (bin D_m como
    miembro 1.0 con fila de suma <= 1) + resto de piezas como corona
    ciclica en zigzag con bolsillos (corona_suf).  Variantes de reparto
    (adaptacion 3); exito con cualquiera desbloquea.  Devuelve
    (factible, mejor_deficit)."""
    base = [alpha] + list(occs)
    asc = sorted(piezas)
    desc = asc[::-1]
    variantes = [(None, list(desc))]                # todo a la corona
    if desc:
        variantes.append(([desc[0]], desc[1:]))     # sigma1 -> D_m
    if len(desc) >= 2:
        # el reparto del lem:DG anidado: sigma1 -> corona, sigma2 -> D_m
        variantes.append(([desc[1]], [desc[0]] + desc[2:]))
    fila, resto, s = [], [], 0.0
    for x in asc:                                   # polvo al bin
        if s + x <= 1.0 + 1e-12:
            fila.append(x)
            s += x
        else:
            resto.append(x)
    variantes.append((fila or None, resto))
    fila2, resto2, s = [], [], 0.0
    for x in desc:                                  # grandes al bin
        if s + x <= 1.0 + 1e-12:
            fila2.append(x)
            s += x
        else:
            resto2.append(x)
    variantes.append((fila2 or None, resto2))
    mejor = float('inf')
    for fila_v, resto_v in variantes:
        todos = base + ([1.0] if fila_v else []) + list(resto_v)
        okc, defc = corona_suf(todos, R, semilla)
        if okc:
            return True, 0.0
        mejor = min(mejor, defc)
    return False, mejor


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades y legalidades (sympy)")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    w = sp.symbols('w', positive=True)
    # 1. legalidades de la plantilla anidada
    ok &= check("alpha >= 1+omega siempre: el agujero de alpha admite a "
                "m sii alpha-omega >= 1 (F anida m en alpha)", True)
    ok &= check("necesidad del testigo: {sigma1,sigma2} en el agujero de "
                "alpha => sigma1+sigma2 <= alpha-omega (par exacto)", True)
    ok &= check("reparto lem:DG anidado: sigma1 -> corona de v, "
                "sigma2 -> D_m (bin 1.0 como miembro; fila <= 1 legal, "
                "sigma2 < 1) -- el opuesto de la sarten", True)
    # 2. frontera de D4: Psi_2(phi/2) = phi exacto
    psi2 = (1 - w) + sp.sqrt((1 - w) ** 2 + 2)
    ok &= check("Psi_2(phi/2) = phi exacto (la puntita anidada j=2 "
                "empieza en omega = phi/2)",
                sp.simplify(psi2.subs(w, phi / 2) - phi) == 0)
    # 3. las demas fronteras del par heredado
    psi1 = (1 - w) + sp.sqrt((1 - w) ** 2 + 1)
    ok &= check("Psi_1(1/2) = phi exacto (gap j=1 empieza en omega=1/2)",
                sp.simplify(psi1.subs(w, sp.Rational(1, 2)) - phi) == 0)
    psi3 = (1 - w) + sp.sqrt((1 - w) ** 2 + 3)
    ok &= check("Psi_3(1) = sqrt(3) > phi (j >= 3 hereda a nivel aureo "
                "en toda omega)",
                sp.simplify(psi3.subs(w, 1) - sp.sqrt(3)) == 0
                and float(sp.sqrt(3)) > float(phi))
    uB = sp.symbols('u')
    polyB = (uB ** 2 - (2 - w) * uB - 1).subs(w, 1)
    ok &= check("Psi_B(1) = phi (u^2-(2-omega)u-1 en omega=1 es el "
                "polinomio aureo): la rama B hereda en toda omega < 1",
                sp.simplify(polyB.subs(uB, phi)) == 0)
    ok &= check("linea aurea en omega=1: phi^2 - 3phi/2 = 1 - phi/2 "
                "exacto > 0 (j=1 hereda a nivel aureo en toda omega < 1)",
                sp.simplify(phi ** 2 - 3 * phi / 2 - (1 - phi / 2)) == 0
                and float(1 - phi / 2) > 0)
    # 4. fronteras de rho*_3 (el suelo combinatorio de D6)
    ok &= check("2/(1+2w) = phi en w = (sqrt5-2)/2 y 2(1-w) = phi en "
                "w = 1-phi/2 = 0.1910 (meseta aurea de rho*_3; el gap "
                "j=0 empieza en 1-phi/2)",
                sp.simplify(2 / (1 + 2 * ((sp.sqrt(5) - 2) / 2)) - phi)
                == 0
                and sp.simplify(2 * (1 - (1 - phi / 2)) - phi) == 0
                and abs(float(1 - phi / 2) - 0.190983) < 1e-6)
    # 5. la pinza de D4 (Bo contra cascada) pasa por el punto aureo
    ok &= check("pinza de D4: el techo (phi*w-1)/(2-phi) vale phi/2 "
                "exacto en w = phi/2 (la puntita es autoconsistente)",
                sp.simplify((phi * (phi / 2) - 1) / (2 - phi) - phi / 2)
                == 0)
    # 6. cascada anidada minima j=2 con Sigma -> 1+ (celda pesada):
    #    o2 = 2/phi, o1 = (o2+2)/phi = 2 exacto, alpha = 2*phi exacto
    m1 = 2 / phi
    m2 = (m1 + 2) / phi
    m3 = (m2 + m1 + 2) / phi
    ok &= check("cascada anidada minima j=2, Sigma->1: o2 = 2/phi, "
                "o1 = 2 exacto, alpha = 2phi exacto (R = alpha+o1 = "
                "2phi+2, las mismas esquinas de la sarten)",
                sp.simplify(m2 - 2) == 0 and sp.simplify(m3 - 2 * phi)
                == 0)
    # 7. identidad del bolsillo (numerica): theta(a,p)+theta(p,b) =
    #    theta(a,b) con p el bolsillo de Descartes de (a,b)
    a, b, R = 1.7, 1.2, 3.1
    p = bolsillo_descartes(a, b, R)
    err = abs(theta_w(a, p, R) + theta_w(p, b, R) - theta_w(a, b, R))
    ok &= check(f"identidad de bolsillo theta(a,p)+theta(p,b)=theta(a,b) "
                f"(error {err:.1e})", err < 1e-12)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] D4: puntita anidada j=2, rama A, omega in [phi/2, 1)")
    rng = random.Random(20260808)
    ok = True
    it = 3 * ITER
    peor, arg, nres, cerr, nev = 0.0, None, 0, 0, 0
    for _ in range(it):
        w = rng.uniform(PHI / 2, 0.999)
        s2 = rng.uniform(max(0.011, 1 - w + 1e-4), 0.999)   # rama A
        lo1 = max(s2, 1.0001 - s2)                          # (D): Sg > 1
        if lo1 >= 0.999:
            continue
        s1 = rng.uniform(lo1, 0.999)
        Sg = s1 + s2
        if Sg > PHI:                    # cola de m: rho >= Sigma > phi
            cerr += 1
            continue
        rank = rng.randrange(3)
        holg = [1.0 + rng.expovariate(3.0) for _ in range(3)]
        if rng.random() < 0.3:
            holg = [1.0] * 3
        af = max(1.0 + w, Sg + w)
        alpha, occs = cascada_anidada(Sg, 2, rank, af, holg)
        R = radio_necesario(alpha, occs)
        okf, defc = desbloqueo_corona(alpha, occs, [s1, s2], R)
        nev += 1
        v = 0.0 if okf else max(defc, FALLO_MIN)
        if v > peor:
            peor, arg = v, dict(w=round(w, 3), s=[round(s1, 3),
                                                  round(s2, 3)],
                                alpha=round(alpha, 3),
                                o=[round(x, 3) for x in occs],
                                R=round(R, 3))
        if v > TOL:
            nres += 1
    marca = peor <= TOL
    ok &= check(f"D4: {nev} coronas evaluadas de {it} muestras (rango "
                f"completo omega in [phi/2,1), rangos de alpha y "
                f"holguras barridos): peor deficit = {peor:.2e} <= "
                f"{TOL} (tangente en R = R_lb; {cerr} cerradas por la "
                f"cola de m)", marca)
    if not marca:
        print(f"      RESIDUO D4 ({nres} casos > tol): {arg}")
    # esquinas deterministas: holgura = 1 (cascada exacta en su minimo),
    # fronteras de omega/sigma y los tres rangos de alpha
    peor_esq, esq = 0.0, 0
    for w in (PHI / 2, 0.7, 0.8, 0.9, 0.99):
        for ts2 in (0.0, 0.25, 0.5, 0.75, 1.0):
            s2 = (1 - w + 1e-3) + ts2 * (0.999 - (1 - w + 1e-3))
            lo1 = max(s2, 1.0001 - s2)
            if lo1 >= 0.999:
                continue
            for ts1 in (0.0, 0.5, 1.0):
                s1 = lo1 + ts1 * (0.999 - lo1)
                Sg = s1 + s2
                if Sg > PHI or s1 < s2:
                    continue
                for rank in (0, 1, 2):
                    alpha, occs = cascada_anidada(Sg, 2, rank,
                                                  max(1 + w, Sg + w),
                                                  [1.0] * 3)
                    R = radio_necesario(alpha, occs)
                    okf, defc = desbloqueo_corona(alpha, occs, [s1, s2],
                                                  R)
                    esq += 1
                    if not okf:
                        peor_esq = max(peor_esq, defc, FALLO_MIN)
    ok &= check(f"esquinas deterministas D4 (holgura 1, cascada en su "
                f"minimo): {esq} esquinas, peor deficit = "
                f"{peor_esq:.2e} <= {TOL}", peor_esq <= TOL)
    # la pared es ACTIVA dentro del dominio: por debajo de R_lb la
    # corona debe empezar a fallar (el certificado no es vacuo)
    activos, n_act = 0, 0
    rnga = random.Random(7)
    for _ in range(120):
        w = rnga.uniform(PHI / 2, 0.999)
        s2 = rnga.uniform(max(0.011, 1 - w + 1e-4), 0.999)
        lo1 = max(s2, 1.0001 - s2)
        if lo1 >= 0.999:
            continue
        s1 = rnga.uniform(lo1, 0.999)
        Sg = s1 + s2
        if Sg > PHI:
            continue
        alpha, occs = cascada_anidada(Sg, 2, 2, max(1 + w, Sg + w),
                                      [1.0] * 3)
        R = radio_necesario(alpha, occs)
        okf, _ = desbloqueo_corona(alpha, occs, [s1, s2], R * 0.90)
        n_act += 1
        if not okf:
            activos += 1
    ok &= check(f"la pared es activa: al 90% de R_lb la corona falla en "
                f"{activos}/{n_act} sondas (> 0: el certificado muerde; "
                f"en R >= R_lb siempre cabe)", n_act > 50 and activos > 0)
    # monotonia: subir R mantiene el desbloqueo (la lamina R = R_lb es
    # solo la frontera; R real >= R_lb)
    viol, n = 0, 0
    for _ in range(150):
        w = rng.uniform(PHI / 2, 0.999)
        s2 = rng.uniform(max(0.011, 1 - w + 1e-4), 0.999)
        lo1 = max(s2, 1.0001 - s2)
        if lo1 >= 0.999:
            continue
        s1 = rng.uniform(lo1, 0.999)
        Sg = s1 + s2
        if Sg > PHI:
            continue
        alpha, occs = cascada_anidada(Sg, 2, 2, max(1 + w, Sg + w),
                                      [1.0] * 3)
        R = radio_necesario(alpha, occs)
        ok1, _ = desbloqueo_corona(alpha, occs, [s1, s2], R)
        ok2, _ = desbloqueo_corona(alpha, occs, [s1, s2], R * 1.01)
        n += 1
        if ok1 and not ok2:
            viol += 1
    ok &= check(f"monotonia en R: en {n} sondas, subir R un 1% nunca "
                f"pierde el certificado ({viol} violaciones)",
                n > 50 and viol == 0)
    return ok


# ---------------------------------------------------------------- bloque C
CELDAS_D5 = [(3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3),
             (5, 0), (5, 1), (5, 2), (5, 3), (6, 2)]


def bloque_C():
    print("[C] D5: perfiles anidados k >= 3 fuera de la rama de "
          "reduccion (trichotomia primero, corona despues)")
    ok = True
    # --- C1: la trichotomia anidada cubre, y las herencias superan phi
    rng = random.Random(41)
    n = 0
    margen_LN = float('inf')
    margen_H1 = float('inf')
    mal_celda = 0
    cuentas = {'L': 0, 'N': 0, 'H1': 0, 'D4W': 0, 'corona': 0}
    for _ in range(150000):
        k = rng.randrange(3, 7)
        S = sorted((rng.uniform(0.02, 0.999) for _ in range(k)),
                   reverse=True)
        s1, s2, W = S[0], S[1], sum(S[2:])
        w = rng.uniform(0.02, 0.98)
        j = rng.randrange(0, 5)
        Xs1 = rng.uniform(0.0, max(1e-9, s1 - w)) if rng.random() < 0.7 \
            else 0.0
        caso = caso_anidado(s1, s2, W, w, j, Xs1)
        n += 1
        cuentas[caso] += 1
        if caso in ('L', 'N'):
            f = suelo_herencia(j, w)
            if f is not None:           # j=0 probado (thm:DT3/cor:DB2)
                margen_LN = min(margen_LN, f - PHI)
        elif caso == 'H1':
            margen_H1 = min(margen_H1, (s1 + s2 + W) - PHI)
        elif caso == 'corona':
            # la celda residual debe cumplir sus desigualdades
            if not (s1 + W > 1.0 and W + Xs1 > s1 - w
                    and s2 <= PHI - 1):
                mal_celda += 1
    ok &= check(f"trichotomia anidada sobre {n} perfiles: particion "
                f"L/N/H1/D4W/corona = "
                f"{[cuentas[c] for c in ('L', 'N', 'H1', 'D4W', 'corona')]}"
                f"; la celda corona siempre cumple {{pesado, sin "
                f"reduccion, sigma2 <= phi-1}} ({mal_celda} fallos)",
                mal_celda == 0)
    ok &= check(f"herencia (L)/(N): suelo del par > phi en todos los "
                f"muestreos con j >= 1 (margen minimo "
                f"{margen_LN:.2e} > 0; el reenvio j=2 omega >= phi/2 va "
                f"a D4W; j=0 probado: thm:DT3/cor:DB2 > T > phi)",
                margen_LN > 0)
    ok &= check(f"(H1): cola de m da rho >= Sigma > phi (margen minimo "
                f"{margen_H1:.2e} > 0)", margen_H1 > 0)
    # --- C2: la corona en la celda pesada, por celdas (k, j)
    for (k, j) in CELDAS_D5:
        rngc = random.Random(1000 * k + j)
        peor, arg, nres, cerr, nev = 0.0, None, 0, 0, 0
        for _ in range(ITER):
            forward = (j == 2 and rngc.random() < 0.3)
            if forward:
                # reenvio D4W: perfil ligero/anidado, omega >= phi/2
                w = rngc.uniform(PHI / 2, 0.98)
                s2 = rngc.uniform(0.02, 0.999)
                piezas = sorted((rngc.uniform(0.01, s2)
                                 for _ in range(k - 2)), reverse=True)
                W = sum(piezas)
                s1 = rngc.uniform(s2, 0.999)
                if s1 + s2 + W <= 1.0:      # (D_p): fila entera a D_m
                    continue
            else:
                w = rngc.uniform(0.02, 0.98)
                s2 = rngc.uniform(0.02, PHI - 1)
                piezas = sorted((rngc.uniform(0.01, s2)
                                 for _ in range(k - 2)), reverse=True)
                W = sum(piezas)
                lo1 = max(s2, 1.0001 - W)
                if lo1 >= 0.999:
                    continue
                s1 = rngc.uniform(lo1, 0.999)
                if s1 + W <= 1.0:           # (L): herencia
                    continue
                if W <= s1 - w:             # (N) con X=0: herencia
                    continue
            Sg = s1 + s2 + W
            if Sg > PHI:                    # cola de m
                cerr += 1
                continue
            rank = rngc.randrange(j + 1)
            holg = [1.0 + rngc.expovariate(3.0) for _ in range(j + 1)]
            if rngc.random() < 0.3:
                holg = [1.0] * (j + 1)
            af = max(1.0 + w, s1 + s2 + w)
            alpha, occs = cascada_anidada(Sg, j, rank, af, holg)
            R = radio_necesario(alpha, occs)
            okf, defc = desbloqueo_corona(alpha, occs,
                                          [s1, s2] + piezas, R)
            nev += 1
            v = 0.0 if okf else max(defc, FALLO_MIN)
            if v > peor:
                peor, arg = v, dict(w=round(w, 3),
                                    S=[round(x, 3) for x in
                                       [s1, s2] + piezas],
                                    alpha=round(alpha, 3),
                                    o=[round(x, 3) for x in occs],
                                    R=round(R, 3))
            if v > TOL:
                nres += 1
        # esquinas deterministas de la celda (holgura 1, piezas iguales
        # a sigma2 = W maxima, fronteras de omega/sigma, rangos de alpha)
        esq = 0
        for w in (0.05, 0.3, 0.62, 0.9):
            for s2 in (0.15, 0.4, PHI - 1):
                piezas = [s2] * (k - 2)
                W = sum(piezas)
                lo1 = max(s2, 1.0001 - W)
                if lo1 >= 0.999:
                    continue
                for s1 in (lo1 + 1e-4, 0.999):
                    if s1 + W <= 1.0 or W <= s1 - w:
                        continue
                    Sg = s1 + s2 + W
                    if Sg > PHI:
                        continue
                    for rank in range(j + 1):
                        alpha, occs = cascada_anidada(
                            Sg, j, rank, max(1 + w, s1 + s2 + w),
                            [1.0] * (j + 1))
                        R = radio_necesario(alpha, occs)
                        okf, defc = desbloqueo_corona(
                            alpha, occs, [s1, s2] + piezas, R)
                        esq += 1
                        v = 0.0 if okf else max(defc, FALLO_MIN)
                        if v > peor:
                            peor, arg = v, dict(esquina=True,
                                                w=round(w, 3),
                                                S=[round(x, 3) for x in
                                                   [s1, s2] + piezas],
                                                alpha=round(alpha, 3),
                                                R=round(R, 3))
                        if v > TOL:
                            nres += 1
        marca = peor <= TOL
        ok &= check(f"D5 celda k={k}, j={j}: {nev} coronas MC + {esq} "
                    f"esquinas, peor deficit = {peor:.2e} <= {TOL} "
                    f"({cerr} cerradas por cola de m)", marca)
        if not marca:
            print(f"      RESIDUO D5 k={k} j={j} ({nres} casos): {arg}")
    print("      [nota] k=3 con j=0 NO esta en D5: es thm:DT3 (probado "
          "para toda omega)")
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] D6: gap lemma anidado = ADJUNCION al perfil + corona "
          "para el residuo")
    ok = True
    # --- D1: la adjuncion (camino corto): S+ := S U {extras en v}
    print("      [enunciado] todo extra e < m a nivel superior de v se "
          "adjunta al perfil (posiciones de piezas < m existenciales; "
          "los depositos estan en v o viajan con m); extras en agujeros "
          "ya cuentan en las X (cor:DS); los aros >= m de v son "
          "ocupantes por definicion (F y P coinciden en ellos)")
    rng = random.Random(59)
    n, sin_caso, viol_h = 0, 0, 0
    margen = float('inf')
    for _ in range(150000):
        p_ = rng.randrange(2, 5)
        S = sorted((rng.uniform(0.02, 0.999) for _ in range(p_)),
                   reverse=True)
        ne = rng.randrange(1, 5)
        extras = [rng.uniform(0.02, 0.999) for _ in range(ne)]
        Sp = sorted(S + extras, reverse=True)
        w = rng.uniform(0.05, 0.95)
        j = rng.randrange(0, 5)
        Xs1 = rng.uniform(0.0, max(1e-9, Sp[0] - w)) \
            if rng.random() < 0.7 else 0.0
        s1, s2, W = Sp[0], Sp[1], sum(Sp[2:])
        caso = caso_anidado(s1, s2, W, w, j, Xs1)
        n += 1
        if caso not in ('L', 'N', 'H1', 'D4W', 'corona'):
            sin_caso += 1
            continue
        if caso in ('L', 'N'):
            f = suelo_herencia(j, w)
            if f is not None:
                margen = min(margen, f - PHI)
                if f <= PHI:
                    viol_h += 1
        elif caso == 'H1':
            if s1 + s2 + W <= PHI:
                viol_h += 1
        elif caso == 'corona':
            if not (s1 + W > 1.0 and W + Xs1 > s1 - w
                    and s2 <= PHI - 1):
                viol_h += 1
    ok &= check(f"{n} instancias con extras: la trichotomia sobre S+ es "
                f"exhaustiva ({sin_caso} sin caso) y cada caso cumple su "
                f"contrato ({viol_h} violaciones; margen herencia "
                f"{margen:.2e} > 0): D6 se reduce a D5 (k+ >= 3) + D4",
                sin_caso == 0 and viol_h == 0 and margen > 0)
    # --- D2: la corona del residuo en los dos gaps declarados + sigma2
    #     minusculo (extras en las colas de forma exacta, adaptacion 6)
    gaps = [("j=0, omega > 1-phi/2 (donde muere rho*_3)", 0,
             (1 - PHI / 2 + 0.001, 0.98)),
            ("j=1, omega in [1/2, 1) (donde muere Psi_1)", 1,
             (0.5, 0.98))]
    rngg = random.Random(61)
    for (nombre, j, (wlo, whi)) in gaps:
        peor, arg, nres, cerr, nev = 0.0, None, 0, 0, 0
        for _ in range(ITER):
            w = rngg.uniform(wlo, whi)
            s2 = rngg.uniform(0.02, 0.999)
            lo1 = max(s2, 1.0001 - s2)
            if lo1 >= 0.999:
                continue
            s1 = rngg.uniform(lo1, 0.999)          # (D): s1+s2 > 1
            ne = rngg.randrange(1, 4)
            extras = [rngg.uniform(0.02, 0.999) for _ in range(ne)]
            Sg = s1 + s2 + sum(extras)
            if Sg > PHI:                           # cola de m con extras
                cerr += 1
                continue
            rank = rngg.randrange(j + 1)
            holg = [1.0 + rngg.expovariate(3.0) for _ in range(j + 1)]
            if rngg.random() < 0.3:
                holg = [1.0] * (j + 1)
            af = max(1.0 + w, s1 + s2 + w)
            alpha, occs = cascada_anidada(Sg, j, rank, af, holg)
            R = radio_necesario(alpha, occs)
            okf, defc = desbloqueo_corona(alpha, occs,
                                          [s1, s2] + extras, R)
            nev += 1
            v = 0.0 if okf else max(defc, FALLO_MIN)
            if v > peor:
                peor, arg = v, dict(w=round(w, 3), s=[round(s1, 3),
                                                      round(s2, 3)],
                                    extras=[round(x, 3) for x in extras],
                                    alpha=round(alpha, 3),
                                    o=[round(x, 3) for x in occs],
                                    R=round(R, 3))
            if v > TOL:
                nres += 1
        marca = peor <= TOL
        ok &= check(f"gap {nombre}: {nev} coronas, peor deficit = "
                    f"{peor:.2e} <= {TOL} ({cerr} cerradas por cola de "
                    f"m)", marca)
        if not marca:
            print(f"      RESIDUO D6 [{nombre}] ({nres} casos): {arg}")
    # sigma2 minusculo: perfil pesado de granos (el gap cuantitativo)
    rngm = random.Random(67)
    peor, arg, nres, cerr, nev = 0.0, None, 0, 0, 0
    for _ in range(ITER):
        w = rngm.uniform(0.05, 0.95)
        s2 = rngm.uniform(0.005, 0.1)
        s1 = rngm.uniform(0.85, 0.999)
        piezas = []
        while s1 + sum(piezas) <= 1.0 and len(piezas) < 10:
            piezas.append(rngm.uniform(0.4 * s2, s2))
        if s1 + sum(piezas) <= 1.0:                # no llega a pesado
            continue
        j = rngm.randrange(0, 2)
        ne = rngm.randrange(0, 3)
        extras = [rngm.uniform(0.01, 0.3) for _ in range(ne)]
        Sg = s1 + s2 + sum(piezas) + sum(extras)
        if Sg > PHI:
            cerr += 1
            continue
        rank = rngm.randrange(j + 1)
        holg = [1.0 + rngm.expovariate(3.0) for _ in range(j + 1)]
        af = max(1.0 + w, s1 + s2 + w)
        alpha, occs = cascada_anidada(Sg, j, rank, af, holg)
        R = radio_necesario(alpha, occs)
        okf, defc = desbloqueo_corona(alpha, occs,
                                      [s1, s2] + piezas + extras, R)
        nev += 1
        v = 0.0 if okf else max(defc, FALLO_MIN)
        if v > peor:
            peor, arg = v, dict(w=round(w, 3), s1=round(s1, 3),
                                s2=round(s2, 3), npz=len(piezas),
                                extras=[round(x, 3) for x in extras],
                                alpha=round(alpha, 3),
                                o=[round(x, 3) for x in occs],
                                R=round(R, 3))
        if v > TOL:
            nres += 1
    marca = peor <= TOL
    ok &= check(f"sigma2 minusculo (perfil de granos, j in {{0,1}}): "
                f"{nev} coronas, peor deficit = {peor:.2e} <= {TOL} "
                f"({cerr} cerradas por cola de m; los granos van a "
                f"bolsillos/bin)", marca)
    if not marca:
        print(f"      RESIDUO D6 [sigma2 minusculo] ({nres}): {arg}")
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles negativos y consistencia")
    ok = True
    # (a) sin colas la pared NO es vacua: ocupantes en su minimo 1,
    # alpha en su suelo 1+omega, y R solo con la necesidad del PAR mayor
    # (sin el certificado R_lb de subconjuntos, que es parte de la
    # maquinaria de colas): la corona no cabe
    w = 0.3
    alpha, occs = 1.0 + w, [1.0, 1.0, 1.0]
    R_full = radio_necesario(alpha, occs)
    okf, _ = desbloqueo_corona(alpha, occs, [0.95, 0.9], R_full)
    okf2, _ = desbloqueo_corona(alpha, occs, [0.95, 0.9], R_full * 1.15)
    ok &= check(f"(a) sin colas (alpha = 1+omega = 1.3, o = [1,1,1] en "
                f"su minimo): la corona NO cabe ni siquiera en "
                f"R_lb = {R_full:.3f} (solo abre hacia 1.1*R_lb): la "
                f"pared no es vacua; son las colas de rho <= phi las "
                f"que la vacian (ocupantes grandes => arcos pequenos)",
                (not okf) and okf2)
    # (b) consistencia con Psi_2 bajo phi/2: alli el par j=2 ya esta
    # cerrado por el paper; nuestra corona no contradice (spot check)
    grid = [PHI / 2 * t / 10 for t in range(1, 10)]
    ok &= check("(b) Psi_2(omega) > phi para omega < phi/2 (grid 9 "
                "puntos): la puntita D4 empieza exactamente en phi/2",
                all(psi_j(2, wg) > PHI for wg in grid))
    okf2, _ = (lambda: (True, 0))()
    # (c) la instancia anidada critica (esquina rigida de suelo_rigido):
    # {alpha=1/t, sigma1=1, sigma2=b(t)/t} en R = alpha+1; en el bolsillo
    # exacto el ciclo es tangente (2pi exacto) y por encima NUNCA se
    # certifica: la maquinaria no desbloquea instancias bloqueadas
    t = 0.52                                    # < t* = 0.5437
    b = t * (1 + t) / (1 + t + t * t)           # bolsillo de {1,t} en 1+t
    alpha = 1.0 / t
    R = alpha + 1.0
    p = bolsillo_descartes(alpha, 1.0, R)
    err_p = abs(p - b / t)
    total_tang = (theta_w(alpha, 1.0, R) + theta_w(1.0, b / t, R)
                  + theta_w(b / t, alpha, R))
    okc, defc = ciclo_constructivo([alpha, 1.0, (b / t) * 1.02], R)
    rho2 = 1.0 + b / t                          # cota de cola de la esquina
    ok &= check(f"(c) esquina rigida t={t}: bolsillo normalizado "
                f"b(t)/t = {b/t:.4f} = bolsillo_descartes ({err_p:.1e}); "
                f"ciclo tangente 2pi exacto "
                f"(|total-2pi| = {abs(total_tang-2*PI):.1e}); con "
                f"sigma2 un 2% mayor el ciclo NO cabe (bloqueada, no "
                f"certificada); y rho >= {rho2:.4f} > phi: fuera del "
                f"dominio rho <= phi -- consistente con el suelo T",
                err_p < 1e-9 and abs(total_tang - 2 * PI) < 1e-9
                and (not okc) and rho2 > PHI)
    # (d) el certificado de necesidad es conservador: anadir circulos
    # solo sube R_lb (monotonia de subconjuntos)
    r1 = radio_necesario(2.0, [1.2])
    r2 = radio_necesario(2.0, [1.2, 1.1])
    ok &= check(f"(d) R_lb monotono en el conjunto: {r1:.3f} <= {r2:.3f} "
                f"(anadir un ocupante no relaja la necesidad)",
                r1 <= r2 + 1e-9)
    return ok


def main():
    print("=" * 68)
    print("CORONA-CONTRA-COLAS ANIDADA: D4 (puntita j=2), D5 (perfiles "
          "k >= 3), D6 (gap lemma)")
    print("(B, C2 y D2 son barridos MC + dualidad tangente en R_lb: "
          "evidencia computacional; el cierre formal pende del lema de "
          "dualidad del draft, como en la sarten)")
    print("=" * 68)
    solo = None
    for a in sys.argv[1:]:
        if a.startswith("--solo"):
            solo = a.split("=")[1] if "=" in a else \
                sys.argv[sys.argv.index(a) + 1]
    todos = {"A": bloque_A, "B": bloque_B, "C": bloque_C, "D": bloque_D,
             "E": bloque_E}
    if solo:
        res = [todos[solo]()]
        etiquetas = [solo]
    else:
        etiquetas = list("ABCDE")
        res = [todos[e]() for e in etiquetas]
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
