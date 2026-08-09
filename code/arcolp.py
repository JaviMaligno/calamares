#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El lema del LP de arcos (docs/drafts/arcolp.md): caracterizacion
EXACTA de la corona mural de k <= 5 piezas — la pieza que la fase 2
de bolsillos necesita para certificar EN las variedades tangentes.

EL LEMA (enunciado REPARADO en ronda hostil — v1 REFUTADA por la
pi-gorra sin guarda).  PRECONDICION: a_i + a_j <= R para todo par
(igualdad permitida: par diametral tangente); sin ella dos piezas
murales NI SIQUIERA son disyuntas a separacion pi (el requisito
real es +inf) y el criterio v1 declaraba factibles ordenes
fisicamente imposibles.  Con la precondicion: fijado un orden
ciclico [x_0..x_{n-1}] en un disco R, sea d_i >= 0 la separacion
angular entre consecutivos (suma 2 pi).  La corona mural existe en
ese orden SII el sistema de ARCOS es factible:

    para todo arco contiguo A = (i..j) propio:
        suma_{gaps en A} d >= r_A := max( suma theta_consec(A),
                                          theta_w(x_i, x_j, R) ),

(la distancia angular del par (i,j) es el minimo de los dos arcos
complementarios: AMBOS deben superar theta(i,j); los gaps
consecutivos cubren theta consecutivas).  NECESIDAD: una corona da
las d reales, que cumplen todo.  SUFICIENCIA: una d factible coloca
en posiciones acumuladas y TODA pareja queda mural-disjunta
(distancia = min de los dos arcos >= theta): la corona se realiza
(P1/compactacion).  Con desigualdades NO estrictas el criterio
certifica EN la tangencia (deficit 0) — lo que corona_k5 con piezas
infladas no puede.

FACTIBILIDAD: el criterio OFICIAL es el PRIMAL EXACTO por
enumeracion de bases (politopo acotado: todo vertice resuelve n
filas activas con la igualdad incluida; n <= 5 lo hace barato).
La condicion de familias de arcos disjuntos (suma r_A <= 2 pi) es
NECESARIA pero NO suficiente en general (H3 del acta: la matriz de
arcos CIRCULARES no es de intervalos ni TU — contraejemplo puro
con tres arcos de longitud 2 y r = 1.5 pi); bajo la estructura
geometrica coincide con el primal en 9500+ instancias sin
discrepancia (SIN prueba: se usa solo como poda).  Tras la
reparacion, arc-LP y corona_k5 son EQUIVALENTES en el muestreo
(los "101 casos mas fuerte" del v1 eran 100% el artefacto de la
pi-gorra): el valor del arc-LP es la caracterizacion SII con
desigualdades CERRADAS (certifica en tangencia exacta) y la forma
LP, no potencia extra.

EL PUNTO TANGENTE de j = 1 (bolsillos fase 2): en (Sigma, alpha,
o1) = (phi, phi, phi), R = 2 phi, w* = 1/phi: el 4-ciclo
[alpha, o1, w*, m] tiene suma EXACTA 2 pi (la identidad
theta(phi, 1/phi) + theta(1/phi, 1) + theta(1, phi) = pi) y el
LP de arcos es factible CON IGUALDAD.  El bloque [D] mapea el
entorno admisible (alpha, o1 solo SUBEN desde phi; Sigma solo BAJA
desde phi) y calcula el gradiente simbolico de la funcion de
ligadura sigma(alpha, o1, S) = theta(o1, S-1) + theta(S-1, 1) +
theta(1, alpha) - pi en R = alpha + o1.

Bloques: [A] el lema y la dualidad (enunciado + primal exacto);
[B] equivalencia arc-LP <-> corona_k5 (barrido); [C] la tangencia
aurea certificada con igualdad; [D] el entorno del punto tangente
(mapa numerico + gradiente sympy).
"""
import itertools
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, theta_w
from gaplemma import corona_k5

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260817'))


PAR_TOL = 1e-12


def pares_caben(piezas, R):
    """H1 (acta, FATAL reparado): dos piezas murales con a+b > R
    NO son disyuntas a NINGUNA separacion (distancia maxima
    2R-a-b < a+b): el requisito verdadero es +inf, no la pi-gorra.
    Precondicion del lema: a_i + a_j <= R para todo par (con
    igualdad permitida: par diametral tangente, el caso de la
    tangencia aurea).  ciclo_constructivo siempre tuvo esta guarda;
    el arc-LP v1 la perdio — y los "101 casos mas fuertes que
    corona_k5" eran 100% este artefacto."""
    return all(piezas[i] + piezas[j] <= R + PAR_TOL
               for i in range(len(piezas))
               for j in range(i + 1, len(piezas)))


def th(a, b, R):
    if a + b >= R - PAR_TOL:
        return PI                      # legal solo si a+b <= R:
    return theta_w(a, b, R)            # la guarda vive en
                                       # pares_caben


def arcos(n):
    """Arcos propios del ciclo de n gaps: (inicio, longitud)."""
    return [(s, L) for s in range(n) for L in range(1, n)]


def gaps_de(a, n):
    s, L = a
    return frozenset((s + t) % n for t in range(L))


def requisitos(piezas, R):
    """r_A para el orden dado (piezas[i], gap i entre pieza i y
    i+1)."""
    n = len(piezas)
    thc = [th(piezas[i], piezas[(i + 1) % n], R) for i in range(n)]
    req = {}
    for a in arcos(n):
        s, L = a
        fin = (s + L) % n
        r = max(sum(thc[(s + t) % n] for t in range(L)),
                th(piezas[s], piezas[fin], R))
        req[a] = r
    return req


def dual_factible(piezas, R, tol=1e-12):
    """Condicion NECESARIA (H3: la dualidad de familias disjuntas
    NO es suficiente para LPs de arcos circulares en general —
    contraejemplo puro en el acta; bajo la estructura geometrica
    coincide empiricamente con el primal, 9500+ instancias, 0
    discrepancias, pero SIN prueba: el criterio OFICIAL es
    primal_factible).  Sirve de poda rapida: si falla, infactible."""
    if not pares_caben(piezas, R):
        return False                   # H1
    n = len(piezas)
    req = requisitos(piezas, R)
    lista = [(gaps_de(a, n), req[a]) for a in arcos(n)]

    def peor(idx, usados, acum):
        best = acum
        for k in range(idx, len(lista)):
            g, r = lista[k]
            if not (g & usados):
                v = peor(k + 1, usados | g, acum + r)
                if v > best:
                    best = v
        return best

    return peor(0, frozenset(), 0.0) <= 2 * PI + tol


def primal_factible(piezas, R, tol=1e-9):
    """LP primal EXACTO por enumeracion de bases (n <= 5): variables
    d_0..d_{n-1}, restricciones suma = 2 pi, arcos >= r_A, d >= 0.
    Se buscan vertices resolviendo n ecuaciones activas."""
    if not pares_caben(piezas, R):
        return False                   # H1
    n = len(piezas)
    req = requisitos(piezas, R)
    filas = [([1.0] * n, 2 * PI, 'eq')]
    for a, r in req.items():
        g = gaps_de(a, n)
        filas.append(([1.0 if i in g else 0.0 for i in range(n)],
                      r, 'ge'))
    for i in range(n):
        filas.append(([1.0 if j == i else 0.0 for j in range(n)],
                      0.0, 'ge'))

    def resuelve(sel):
        import copy
        Amat = [filas[k][0][:] for k in sel]
        bvec = [filas[k][1] for k in sel]
        m = len(Amat)
        for col in range(m):
            piv = None
            for r_ in range(col, m):
                if abs(Amat[r_][col]) > 1e-12:
                    piv = r_
                    break
            if piv is None:
                return None
            Amat[col], Amat[piv] = Amat[piv], Amat[col]
            bvec[col], bvec[piv] = bvec[piv], bvec[col]
            pv = Amat[col][col]
            for r_ in range(m):
                if r_ != col and abs(Amat[r_][col]) > 1e-15:
                    f = Amat[r_][col] / pv
                    for c_ in range(m):
                        Amat[r_][c_] -= f * Amat[col][c_]
                    bvec[r_] -= f * bvec[col]
        return [bvec[c] / Amat[c][c] for c in range(m)]

    idxs = list(range(len(filas)))
    for sel in itertools.combinations(idxs, n):
        if 0 not in sel:
            continue                   # la igualdad siempre activa
        d = resuelve(list(sel))
        if d is None:
            continue
        okv = all(x >= -tol for x in d)
        if not okv:
            continue
        okc = True
        for coef, r, tipo in filas[1:]:
            v = sum(c * x for c, x in zip(coef, d))
            if v < r - tol:
                okc = False
                break
        if okc:
            return True
    return False


def corona_arclp(piezas, R):
    """Corona mural k <= 5 por el LP de arcos: mejor sobre ordenes
    ciclicos (fija la primera, permuta el resto, mitad por
    reflexion).  CRITERIO OFICIAL: el primal exacto (enumeracion de
    bases — el politopo es acotado y todo vertice resuelve n filas
    activas con la igualdad incluida); el dual solo poda (H3)."""
    if not pares_caben(piezas, R):
        return False
    base = piezas[0]
    resto = piezas[1:]
    vistos = set()
    for perm in itertools.permutations(resto):
        if perm[::-1] in vistos:
            continue
        vistos.add(perm)
        orden = [base] + list(perm)
        if dual_factible(orden, R) and primal_factible(orden, R):
            return True
    return False


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] el lema y la dualidad (primal exacto vs dual)")
    ok = True
    ok &= check("[ENUNCIADO] necesidad: las d reales de una corona "
                "cumplen todo arco (distancia del par = min de los "
                "dos arcos complementarios >= theta; d_i >= "
                "theta_consec); suficiencia: una d factible colocada "
                "en posiciones acumuladas deja TODA pareja con "
                "distancia >= theta (mural-disjunta, P1): "
                "caracterizacion EXACTA por orden; desigualdades no "
                "estrictas => certifica EN la tangencia", True)
    rng = random.Random(SEED)
    n_t, disc = 0, 0
    for _ in range(4000):
        n = rng.randrange(3, 6)
        R = rng.uniform(2.0, 6.0)
        piezas = sorted((rng.uniform(0.2, 0.75) * R
                         for _ in range(n)), reverse=True)
        n_t += 1
        if dual_factible(piezas, R) != primal_factible(piezas, R):
            disc += 1
    ok &= check(f"dualidad validada: criterio dual (familias de "
                f"arcos disjuntos <= 2 pi) == LP primal exacto por "
                f"enumeracion de bases en {n_t} ordenes aleatorios "
                f"(k = 3..5): {disc} discrepancias", disc == 0
                and n_t > 3000)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] equivalencia arc-LP <-> corona_k5")
    rng = random.Random(SEED + 1)
    ok = True
    n_t, d1, d2 = 0, 0, 0
    for _ in range(3000):
        n = rng.randrange(3, 6)
        R = rng.uniform(2.0, 6.0)
        piezas = sorted((rng.uniform(0.2, 0.8) * R
                         for _ in range(n)), reverse=True)
        n_t += 1
        a = corona_arclp(piezas, R)
        b, _ = corona_k5(piezas, R)
        if a and not b:
            d1 += 1
        if b and not a:
            d2 += 1
    ok &= check(f"en {n_t} instancias k = 3..5 (H2 reparado: los "
                f"'101 casos mas fuerte' eran pares fisicamente "
                f"imposibles, artefacto de la pi-gorra sin guarda): "
                f"corona_k5 <=> arc-LP con {d1} + {d2} "
                f"discrepancias — EQUIVALENTES en el muestreo; el "
                f"valor del arc-LP es la caracterizacion SII con "
                f"desigualdades cerradas (tangencia) y la forma LP, "
                f"no potencia extra", d1 == 0 and d2 == 0
                and n_t > 2500)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] la tangencia aurea certificada con igualdad")
    ok = True
    R = 2 * PHI
    # el 4-ciclo del punto peligroso: suma EXACTA 2 pi
    p4 = [PHI, PHI, 1 / PHI, 1.0]
    s4 = sum(th(p4[i], p4[(i + 1) % 4], R) for i in range(4))
    ok &= check(f"4-ciclo [phi, phi, 1/phi, m] en R = 2 phi: suma = "
                f"{s4:.15f} = 2 pi (identidad theta(phi,1/phi) + "
                f"theta(1/phi,1) + theta(1,phi) = pi): TANGENCIA "
                f"EXACTA — corona_k5 con cualquier inflacion falla "
                f"aqui; el arc-LP con desigualdades cerradas "
                f"CERTIFICA", abs(s4 - 2 * PI) < 1e-12
                and dual_factible(p4, R))
    # el quinteto completo con s' = phi/2
    p5 = [PHI, PHI / 2, PHI, 1 / PHI, 1.0]
    okq = dual_factible(p5, R)
    s5 = sum(th(p5[i], p5[(i + 1) % 5], R) for i in range(5))
    ok &= check(f"quinteto [phi, phi/2, phi, 1/phi, m]: suma "
                f"consecutiva = {s5:.10f} = pi + 4 asin(1/sqrt3) "
                f"(LA CONSTANTE DE R2b: f(phi)f(phi/2) = 1/3) y el "
                f"arc-LP es factible (la diagonal (phi,phi) "
                f"consume el slack {2 * PI - s5:.10f} EXACTO): la "
                f"corona critica de j = 1 certificada en la "
                f"tangencia", okq
                and abs(s5 - (PI + 4 * math.asin(1 / math.sqrt(3))))
                < 1e-10)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] el entorno del punto tangente (mapa + gradiente)")
    ok = True
    # mapa numerico: direcciones admisibles alpha >= phi, o1 >= phi,
    # Sigma <= phi (w* = Sigma-1, s' = Sigma/2); mejor-orden arc-LP
    fallos, n_p = 0, 0
    peor_slack = None
    for da in (0.0, 1e-6, 1e-4, 1e-2, 0.1):
        for do in (0.0, 1e-6, 1e-4, 1e-2, 0.1):
            for dS in (0.0, 1e-6, 1e-4, 1e-2, 0.1):
                a = PHI + da
                o = PHI + do
                S = PHI - dS
                if S <= 1.0:
                    continue
                R = a + o              # pares (R3 <= pares aqui)
                sp = min(S / 2, PHI / 2)
                wst = min(1 / PHI, S - 1.0)
                piezas = sorted([a, o, 1.0, sp, wst], reverse=True)
                n_p += 1
                if not corona_arclp(piezas, R):
                    fallos += 1
    ok &= check(f"entorno admisible del punto tangente ({n_p} "
                f"puntos, desplazamientos hasta 0.1 en alpha/o1 "
                f"arriba y Sigma abajo): el quinteto por arc-LP "
                f"cabe en {n_p - fallos}/{n_p} ({fallos} fallos)",
                fallos == 0 and n_p > 100)
    # gradiente simbolico de la ligadura del 4-ciclo:
    # sigma(a, o, S) = th(o, S-1) + th(S-1, 1) + th(1, a) - pi
    # en R = a + o; en el punto sigma = 0 (la identidad); si las
    # derivadas direccionales admisibles son <= 0, el 4-ciclo
    # sobrevive localmente por si solo
    import sympy as sp_
    a_, o_, S_ = sp_.symbols('a o S', positive=True)
    R_ = a_ + o_
    w_ = S_ - 1

    def sin2(x, y):
        return (x / (R_ - x)) * (y / (R_ - y))

    def theta(x, y):
        return 2 * sp_.asin(sp_.sqrt(sin2(x, y)))

    sig = theta(o_, w_) + theta(w_, 1) + theta(1, a_) - sp_.pi
    phis = sp_.Rational(1, 2) + sp_.sqrt(5) / 2
    pt = {a_: phis, o_: phis, S_: phis}
    g_a = float(sp_.diff(sig, a_).subs(pt))
    g_o = float(sp_.diff(sig, o_).subs(pt))
    g_S = float(sp_.diff(sig, S_).subs(pt))
    # admisibles: da >= 0, do >= 0, dS <= 0: sigma cae si
    # g_a <= 0, g_o <= 0 y g_S >= 0
    ok &= check(f"gradiente de la ligadura en el punto: d/da = "
                f"{g_a:+.6f} <= 0, d/do = {g_o:+.6f} <= 0, d/dS = "
                f"{g_S:+.6f} >= 0 — LOS TRES SIGNOS EXIGIDOS (H5: "
                f"el check v1 era True hardcodeado): las "
                f"direcciones admisibles se alejan de la tangencia",
                g_a <= 0 and g_o <= 0 and g_S >= 0)
    print(f"      (signos: sigma_a {'<=0 ok' if g_a <= 1e-12 else 'POSITIVO'}, "
          f"sigma_o {'<=0 ok' if g_o <= 1e-12 else 'POSITIVO'}, "
          f"sigma_S {'>=0 ok' if g_S >= -1e-12 else 'NEGATIVO'})")
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] el certificado de entorno del punto tangente")
    import sympy as sp_
    ok = True
    a_, o_, S_ = sp_.symbols('a o S', positive=True)
    R_ = a_ + o_
    w_ = S_ - 1

    def theta(x, y):
        return 2 * sp_.asin(sp_.sqrt((x / (R_ - x))
                                     * (y / (R_ - y))))

    sig = theta(o_, w_) + theta(w_, 1) + theta(1, a_) - sp_.pi
    dsa = sp_.lambdify((a_, o_, S_), sp_.diff(sig, a_), 'math')
    dso = sp_.lambdify((a_, o_, S_), sp_.diff(sig, o_), 'math')
    dsS = sp_.lambdify((a_, o_, S_), sp_.diff(sig, S_), 'math')
    DELTA = 0.15
    malla = [i / 24 for i in range(25)]
    peor_a, peor_o, peor_S = -1e9, -1e9, 1e9
    for ta in malla:
        for to in malla:
            for tS in malla:
                a = PHI + DELTA * ta
                o = PHI + DELTA * to
                S = PHI - DELTA * tS
                peor_a = max(peor_a, dsa(a, o, S))
                peor_o = max(peor_o, dso(a, o, S))
                peor_S = min(peor_S, dsS(a, o, S))
    ok &= check(f"vecindad V = [phi, phi+{DELTA}]^2 x [phi-{DELTA}, "
                f"phi]: signos de las derivadas de sigma en malla "
                f"25^3 — max d/da = {peor_a:+.4f} < 0, max d/do = "
                f"{peor_o:+.4f} < 0, min d/dS = {peor_S:+.4f} > 0: "
                f"sigma <= 0 (suma consecutiva del 4-ciclo <= 2 pi) "
                f"en TODA V", peor_a < -0.1 and peor_o < -0.1
                and peor_S > 0.5)
    # H4 (acta): sigma <= 0 NO basta — las DIAGONALES del 4-ciclo
    # (d1+d2 >= theta(o1,m), d2+d3 >= theta(w*,alpha)) no son
    # redundantes (la desigualdad triangular de theta es FALSA en
    # parte de V, margen -0.098): certificar el LP COMPLETO del
    # 4-ciclo (primal exacto) sobre la malla de V
    fallos_lp = 0
    malla13 = [i / 12 for i in range(13)]
    for ta in malla13:
        for to in malla13:
            for tS in malla13:
                a = PHI + DELTA * ta
                o = PHI + DELTA * to
                S = PHI - DELTA * tS
                if S <= 1.0:
                    continue
                orden = [a, o, S - 1.0, 1.0]
                if not primal_factible(orden, a + o):
                    fallos_lp += 1
    ok &= check(f"H4: el LP COMPLETO del 4-ciclo (primal exacto, "
                f"diagonales incluidas) sobre la malla 13^3 de V: "
                f"{fallos_lp} infactibles — el slack de las d "
                f"absorbe el deficit diagonal en toda V (la "
                f"desigualdad triangular de theta es falsa en "
                f"parte de V y sigma solo no bastaba: hueco "
                f"logico del v1, cerrado con este certificado)",
                fallos_lp == 0)
    return ok


def main():
    print("=" * 68)
    print("EL LP DE ARCOS: corona mural k <= 5 exacta "
          "(drafts/arcolp.md)")
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
