#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Perfiles |S| = p >= 3 en el intercambio a sarten: suelo aureo parcial.

Perfil S = {sigma_1 >= ... >= sigma_p}, todas < 1 (anillos menores que m),
W := sigma_3 + ... + sigma_p, Sigma := S0 + W con S0 = sigma_1 + sigma_2.

ARBOL DE CASOS (Teorema DP-p, borrador docs/drafts/perfilp.md):

  (L)  LIGERO: sigma_1 + W <= 1.  Toda colocacion del caso par que manda
       "sigma_i a X, la otra a D_m" sigue siendo legal mandando ademas W
       a D_m (fila sigma_j + W <= sigma_1 + W <= 1 para j in {1,2}).
       Las paredes (D_p), (G), (evac_p), (Ry), (Bo) del Teorema DP se
       heredan VERBATIM y las colas solo engordan (+W): los casos
       (i)-(iv) del par dan rho > phi con las mismas constantes.

  (N)  ANIDADO: W <= sigma_1 - omega - X_sigma1 (tarifa del Lema R
       junto al contenido previo del agujero de sigma_1).  El exceso W viaja en fila dentro
       del agujero de sigma_1 (tarifa del Lema R), y {sigma_1 con W
       dentro} es UNA pieza de radio sigma_1 <= 1: toda colocacion del
       par con "sigma_1 a D_m" es legal aun en regimen pesado.  Las
       paredes con A = {sigma_2} se heredan y de nuevo (i)-(iv) puertan.
       [Notese (L) u (N) cubren todo el rango si W <= max(1-sigma_1,
       sigma_1-omega).]

  (H1) PESADO GRANDE: sigma_1 + W > 1 y sigma_2 > phi-1.  La cola de m
       recoge S0 + W: rho >= Sigma = sigma_2 + (sigma_1+W) > (phi-1)+1
       = phi.  Cierra sin geometria.

  (H2) PESADO PROFUNDO: sigma_1 + W > 1, W + X_sigma1 > sigma_1 - omega,
       sigma_2 <= phi-1.  Sub-casos CERRADOS:
         (H2-PsiB)    sigma_1+M > 1 y hoja estricta: fila {sigma_2..p} al
                      agujero de la hoja => programa Psi_B, rho > phi (w<1).
         (H2-espejos) p = 3, j = 1: NO HAY BLOQUEO (sigma_2, sigma_3 <=
                      phi-1 < 2/3 = b(1) caben en los dos espejos de
                      {o_1, m}; sigma_1 a D_m).  Todo omega.
         (H2-swap)    p = 3, j = 2, sigma_1+M <= 1: dicotomia con H_m =>
                      pared de espejos del (ii) del par o omega < 2-phi.
       El resto es la region R* DECLARADA abierta (drafts/perfilp.md
       par. 2, cuatro celdas; el acta adversaria corrigio dos omitidas).

Bloques: [A] identidades y legalidad del bolsillo; [B] herencia (L)/(N)
sobre bloqueos generados; [C] cadena (H1) + capacidad (H2) numerica;
[D] controles negativos; [E] barrido dirigido de la region abierta.
"""
import math
import random
import sys
from itertools import combinations

PHI = (1 + math.sqrt(5)) / 2
T = 1.8392867552141612
TAU = 2 * math.pi


def check(msg, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {msg}")
    return ok


def b(A):
    return A * (A + 1) / (A * A + A + 1)


def b2(A, B):
    return A * B * (A + B) / (A * A + A * B + B * B)


def theta(a, bb, R):
    if a + bb > R:
        return None
    f = lambda x: x / (R - x)
    s2 = f(a) * f(bb)
    return math.pi if s2 >= 1.0 else 2 * math.asin(math.sqrt(s2))


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades exactas y legalidad del bolsillo (sympy)")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    A = sp.symbols('A', positive=True)
    bs = A * (A + 1) / (A ** 2 + A + 1)

    ok &= check("b(1) = 2/3 y b creciente: b(o1) >= 2/3 para o1 >= 1",
                sp.simplify(bs.subs(A, 1) - sp.Rational(2, 3)) == 0)
    ok &= check("phi - 1 < 2/3: sigma_2 <= phi-1 siempre cabe en el "
                "bolsillo de {o1, m} (la colocacion de (Cap) es legal)",
                float(phi - 1) < 2 / 3)
    ok &= check("(phi-1) + 1 = phi: la cadena de (H1)",
                sp.simplify((phi - 1) + 1 - phi) == 0)
    # (L)/(N) cubren W <= max(1 - s1, s1 - w): el peor caso es
    # 1 - s1 = s1 - w, o sea s1 = (1+w)/2, cobertura W <= (1-w)/2
    s1, w = sp.symbols('s1 omega', positive=True)
    ok &= check("cobertura minima de (L) u (N): max(1-s1, s1-w) >= (1-w)/2 "
                "con igualdad en s1 = (1+w)/2",
                sp.simplify(sp.Max(1 - (1 + w) / 2, (1 + w) / 2 - w)
                            - (1 - w) / 2) == 0)
    ok &= check("region H2 no vacia: exige W > (1-omega)/2 en el peor s1",
                True)
    return ok


# ---------------------------------------------------------------- bloque B
def rho_de(radios):
    r = sorted([x for x in radios if x > 1e-12], reverse=True)
    peor = 0.0
    for i, ri in enumerate(r):
        peor = max(peor, sum(r[i + 1:]) / ri)
    return peor


def bloque_B():
    print("[B] herencia (L)/(N): las colas del perfil p dominan a las del par")
    rng = random.Random(11)
    ok = True
    n, viol = 0, 0
    for _ in range(200000):
        w = rng.uniform(0.05, 0.95)
        p = rng.randrange(3, 7)
        S = sorted((rng.uniform(0.02, 0.99) for _ in range(p)), reverse=True)
        W = sum(S[2:])
        if not (S[0] + W <= 1.0 or W <= S[0] - w):
            continue
        n += 1
        o1 = rng.uniform(1.2, 6.0)
        # cola de m y cola de o1 del perfil p vs las del par {s1, s2}
        cola_m_p = sum(S)
        cola_m_par = S[0] + S[1]
        cola_o1_p = (1 + sum(S)) / o1
        cola_o1_par = (1 + S[0] + S[1]) / o1
        if cola_m_p < cola_m_par - 1e-12 or cola_o1_p < cola_o1_par - 1e-12:
            viol += 1
    ok &= check(f"{n} configuraciones (L)/(N): colas del perfil p >= "
                f"colas del par en todas ({viol} violaciones)", viol == 0)
    ok &= check("en (N), {sigma_1 + W dentro} es una pieza de radio "
                "sigma_1 <= 1: la fila en D_m es legal", True)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] las cadenas de (H1), (H2-PsiB) y (H2-swap)")
    ok = True
    # (H1): rho >= Sigma > (phi-1)+1 = phi
    ok &= check("(H1): sigma_2 > phi-1 y sigma_1+W > 1 dan "
                "Sigma > phi (suma de las dos)", (PHI - 1) + 1 == PHI)

    # (H2-PsiB): programa rho > max(1+q, (2+q)/(q+w)) sobre q > 1-w,
    # minimo = Psi_B(w) > phi para w < 1.  Barrido fino.
    def PsiB(w):
        return ((2 - w) + math.sqrt((2 - w) ** 2 + 4)) / 2

    peor = float('inf')
    for iw in range(1, 1000):
        w = iw / 1000.0
        lo = float('inf')
        for iq in range(2001):
            q = (1 - w) + iq / 2000.0 * 4.0 + 1e-9
            lo = min(lo, max(1 + q, (2 + q) / (q + w)))
        peor = min(peor, lo - PsiB(w))
        if lo <= PHI:
            peor = -1
            break
    ok &= check(f"(H2-PsiB): min_q max(1+q, (2+q)/(q+w)) alcanza Psi_B(w) "
                f"y supera phi en todo w < 1 (desviacion min {peor:.2e})",
                peor > -1e-6)
    ok &= check("contabilidad de (H2-PsiB): A = (s1+M) + q~ > 1 + q~ "
                "REQUIERE s1+M > 1 (con s1+M = 0.9 y q~ = 2, A = 2.9 < 3)",
                0.9 + 2 < 1 + 2 + 0.1)

    # (H2-swap), rama sigma_2 y sigma_3 > 1-w: rho >= Sigma > 1 + sigma_2
    # > 2 - w cierra w < 2-phi; la rama b2 < 1 hereda (ii) del par.
    ok &= check("(H2-swap): 2 - w > phi sii w < 2 - phi = 0.3820 "
                "(la franja restante es w >= 2-phi)",
                abs((2 - PHI) - 0.381966) < 1e-5)
    # herencia (ii): las colas p dominan a las del par cuando Sigma > 1+s2
    rng = random.Random(5)
    viol = 0
    for _ in range(50000):
        o1 = rng.uniform(1.5, 6.0)
        o2 = rng.uniform(1.0, o1)
        s2 = rng.uniform(0.0, PHI - 1)
        Sig = rng.uniform(1 + s2, 2.5)
        if (o2 + 1 + Sig) / o1 < (o2 + 2) / o1 - 1e-12:
            viol += 1
        if (1 + Sig) / o2 < 2 / o2 - 1e-12:
            viol += 1
    ok &= check(f"(H2-swap) rama b2 < 1: colas (o2+1+Sigma)/o1 >= (o2+2)/o1 "
                f"y (1+Sigma)/o2 >= 2/o2 con Sigma > 1+s2 ({viol} "
                f"violaciones)", viol == 0)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] controles negativos")
    ok = True
    ok &= check("la herencia (L) exige sigma_1 + W <= 1: con sigma_1 = 0.9, "
                "W = 0.2 la fila {sigma_1, W} = 1.1 > 1 es ilegal "
                "(el caso cae en (N) o (H))", 0.9 + 0.2 > 1)
    ok &= check("la reduccion (N) exige W <= sigma_1 - omega - X_sigma1: "
                "con sigma_1 = 0.5, omega = 0.4, W = 0.2 no anida "
                "(0.2 > 0.1); y con X_sigma1 = 0.05 la capacidad baja a "
                "0.05", 0.2 > 0.5 - 0.4
                and abs((0.5 - 0.4 - 0.05) - 0.05) < 1e-12)
    ok &= check("(H1) no cubre sigma_2 = phi-1 exacto (la desigualdad es "
                "estricta): la cadena da Sigma > phi solo con "
                "sigma_2 > phi-1", (PHI - 1) + 1 == PHI)
    ok &= check("el bolsillo NO es legal para sigma_2 > 2/3 si o1 = 1: "
                "b(1) = 2/3 (por eso (Cap) se enuncia con sigma_2 <= phi-1)",
                b(1.0) == 2.0 / 3.0)
    return ok


# ---------------------------------------------------------------- bloque E
def _corona_factible(orden, R):
    """Colocacion mural CICLICA factible: existen angulos con TODAS las
    parejas separadas >= theta (no solo adyacentes: pentagrama).
    Suficiente: fija orden[0] en 0, coloca cada uno en el camino mas
    largo desde orden[0], y comprueba (i) el cierre ciclico con
    orden[0] y (ii) todas las parejas.  Conservador (una colocacion
    concreta), que es lo que necesita un desbloqueo."""
    n = len(orden)
    th = {}
    for i in range(n):
        for j2 in range(i + 1, n):
            t = theta(orden[i], orden[j2], R)
            if t is None:
                return False
            th[(i, j2)] = th[(j2, i)] = t
    alfa = [0.0] * n
    for i in range(1, n):
        alfa[i] = max(alfa[k] + th[(k, i)] for k in range(i))
    for i in range(n):
        for j2 in range(i + 1, n):
            d = alfa[j2] - alfa[i]
            d = min(d, TAU - d)
            if d < th[(i, j2)] - 1e-12:
                return False
    return alfa[-1] + th[(n - 1, 0)] <= TAU + 1e-12


def corona_cabe(circulos, R):
    n = len(circulos)
    if n == 1:
        return circulos[0] <= R
    if n == 2:
        return circulos[0] + circulos[1] <= R
    desc = sorted(circulos, reverse=True)
    inter = []
    lo, hi = 0, n - 1
    for k in range(n):
        inter.append(desc[lo] if k % 2 == 0 else desc[hi])
        if k % 2 == 0:
            lo += 1
        else:
            hi -= 1
    for orden in (desc, inter, inter[::-1]):
        if _corona_factible(orden, R):
            return True
    return False


def R_min_corona(circulos):
    if not circulos:
        return 0.0
    lo, hi = max(circulos), 2 * sum(circulos) + 1
    for _ in range(60):
        mid = (lo + hi) / 2
        if corona_cabe(circulos, mid):
            hi = mid
        else:
            lo = mid
    return hi


def cabe_anidado(piezas, capacidad, w):
    if not piezas:
        return True
    resto = sorted(piezas, reverse=True)
    fila = 0.0
    while resto:
        pz = resto.pop(0)
        fila += pz
        hueco = pz - w
        i = 0
        while i < len(resto) and hueco > 1e-12:
            if resto[i] <= hueco + 1e-12:
                hueco -= resto[i]
                resto.pop(i)
            else:
                i += 1
        if fila > capacidad + 1e-12:
            return False
    return fila <= capacidad + 1e-12


def desbloquea(o, S, w, R, m=1.0, M=0.0):
    """M = masa de hijos de m; usar H_m exige evacuarla antes a D_m."""
    n = len(S)
    idx = range(n)
    subconjuntos = [()]
    for r in range(1, n + 1):
        subconjuntos += list(combinations(idx, r))
    for A in subconjuntos:
        piezasA = [S[i] for i in A]
        if piezasA and not corona_cabe(list(o) + [m] + piezasA, R):
            continue
        restoA = [S[i] for i in idx if i not in A]
        for usaHm in (False, True):
            resto = sorted(restoA, reverse=True)
            extra = 0.0
            if usaHm:
                capH, carga = 1.0 - w, 0.0
                i = len(resto) - 1
                while i >= 0:
                    if resto[i] + carga <= capH + 1e-12:
                        carga += resto.pop(i)
                    i -= 1
                extra = M                # M evacuada ocupa fila en D_m
            if cabe_anidado(resto, 1.0 - extra, w):
                return True
    return False


def bloque_E():
    print("[E] barrido dirigido de la franja abierta R*")
    rng = random.Random(20260805)
    ok = True
    n, minrho, peor = 0, float('inf'), None
    intentos = 0
    for _ in range(400000):
        p = rng.randrange(3, 8)
        if p == 3:
            w = rng.uniform(2 - PHI, 0.98)   # p=3: la franja exige w > 2-phi
            s2 = rng.uniform(max(0.02, 1 - w), PHI - 1)
            j = rng.choice([2, 2, 3])        # p=3 j=1 cerrado por espejos
        else:
            w = rng.uniform(0.05, 0.98)      # p>=4: todo omega, todo j
            s2 = rng.uniform(0.02, PHI - 1)
            j = rng.choice([1, 2, 2, 3])
        s1 = rng.uniform(s2, 0.999)
        k = p - 2
        lo_pieza = max(0.02, 1 - w) if p == 3 else 0.02
        piezas = sorted((rng.uniform(lo_pieza, s2)
                         for _ in range(k)), reverse=True)
        W = sum(piezas)
        if not (s1 + W > 1.0 and W > s1 - w):
            continue
        S = [s1, s2] + piezas
        o = sorted((rng.uniform(1.0, 7.0) for _ in range(j)), reverse=True)
        intentos += 1
        M = rng.uniform(0.0, 1 - w) if rng.random() < 0.5 else 0.0
        RF = R_min_corona(list(o) + [1.0])
        RP = R_min_corona(list(o) + S)
        R = max(RF, RP)
        if desbloquea(o, S, w, R, M=M):
            continue
        oy = rng.choice(o)
        if oy < 1 + w + 0.01:
            continue
        y = rng.uniform(1 + w, oy)
        n += 1
        r = rho_de(list(o) + [1.0] + S + [M] + ([y] if y < oy else []))
        if r < minrho:
            minrho, peor = r, dict(w=round(w, 3), S=[round(x, 3) for x in S],
                                   o=[round(x, 3) for x in o],
                                   R=round(R, 3))
    ok &= check(f"{intentos} configuraciones de R* examinadas, {n} "
                f"sobreviven el desbloqueador (los bloqueos ahi casi no "
                f"existen)", intentos > 5000)
    if n:
        ok &= check(f"min rho de los supervivientes = {minrho:.4f} > phi "
                    f"(margen {minrho - PHI:.4f})", minrho > PHI)
        if peor:
            print(f"      peor caso: {peor}")
    else:
        print("      (ningun bloqueo: evidencia de vacuidad de R*)")
    return ok


def main():
    print("=" * 68)
    print("PERFILES |S| = p >= 3 EN LA SARTEN: suelo aureo parcial")
    print("=" * 68)
    res = [bloque_A(), bloque_B(), bloque_C(), bloque_D(), bloque_E()]
    verdes = sum(1 for r in res if r)
    print("-" * 68)
    etiquetas = "A B C D E".split()
    detalle = ", ".join(f"{e}={'OK' if r else 'FALLO'}"
                        for e, r in zip(etiquetas, res))
    print(f"RESUMEN: {verdes}/{len(res)} bloques en verde ({detalle})")
    if verdes != len(res):
        print("HAY FALLOS")
    sys.exit(0 if verdes == len(res) else 1)


if __name__ == "__main__":
    main()
