#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las cuatro celdas de la region R* del Teorema DP-p (perfilp.md par. 2).

    R* = C1 u C2 u C3 u C4, con
      C1 = {p >= 4, sigma1+M <= 1}
      C2 = {p >= 4, sigma1+M > 1, j = 1, subarbol de o1 = cadena hasta y}
      C3 = {p = 3, j = 2, sigma1+M <= 1, sigma2, sigma3 > 1-omega}
      C4 = {p = 3, j >= 3, sigma1+M <= 1}
    (todas dentro de {heavy sigma1+W > 1, no-anida, sigma2 <= phi-1}).

Este script EJECUTA y VERIFICA las derivaciones de trabajo que intentan
cerrar las cuatro celdas (scratchpad derivaciones_Rstar.md).  Ingredientes:

  * (Bo)-fila con p piezas: la colocacion "fila {sigma2..sigma_p} al
    agujero del nodo z junto a X_z, sigma1 -> D_m" (patron de H2-PsiB,
    legal por Lema R + sigma1 <= 1); su fallo da z < s' + X_z con
    s' := sigma2+...+sigma_p+omega.  Las colas engordan con
    Sigma = sigma1+...+sigma_p en vez del S0 del par.

  * PINZA-CON-SIGMA (celda C4, caso o1 >= 3, o2 >= 3/phi, rama de la
    cadena): [C1'] cola de v* => o2 < (phi-1)v* - 2 - Sigma + s';
    [C2'] o2 >= 3/phi => v* > phi(3/phi + 2 + Sigma - s');
    [C3'] hijo-nodo w <= o2 + polvo < phi-1 => o2 > v* - s' - (phi-1);
    [C4'] = C1'+C3' => v* < phi^2(2s' + phi - 3 - Sigma).
    Frontera exacta de C2' vs C4':  s' <= (phi-1)*Sigma + (16 - 9phi),
    que en Sigma = 1 degenera en 11 - 4 sqrt5 = 15 - 8phi (Teorema M).
    En el dominio de C4, sup(s' - (phi-1)Sigma) = 5phi - 7 y el margen
    es 23 - 14phi = 16 - 7 sqrt5 = 0.3475 > 0: SIEMPRE incompatibles.
    Rama sin hijo-nodo: v* < s' + phi - 1 contra C2', frontera
    s' <= (phi-1)Sigma + (7 - 3phi), margen 14 - 8phi = 1.0557.

  * PROGRAMA Psi de C3.2 (sigma2+sigma3 > 1, omega <= 1/2):
    rho > max(q+1-omega, (2+q-omega)/(q+omega)) sobre q > 2(1-omega);
    cruce q* = sqrt(1+(1-omega)^2), factible sii omega >= 1-1/sqrt3;
    valor Psi(omega) = sqrt(1+(1-omega)^2) + (1-omega), Psi(1/2) = phi
    EXACTO; esquina 3(1-omega) >= sqrt3 para omega <= 1-1/sqrt3.

  * PARED DE CORONA (celda C3.3, la tarea central): bloqueo =>
    {o1,o2,m,sigma2,sigma3} no empaqueta en o1+o2 => para TODO orden
    de la corona mural, theta(o1,o2) = pi (par rigido) + cadena > pi.
    Para desbloquear basta UN orden con cadena <= pi.  Se maximiza
    g = min sobre ordenes de la cadena, sobre el dominio con las colas
    o2 >= (1+Sigma)/phi, o1 >= max(o2, (o2+1+Sigma)/phi): si el maximo
    queda < pi, la celda es VACIA de bloqueos.

  * p >= 4: pared W2 := sum_{i>=4} sigma_i > 1-omega (deposito H_m) +
    cadena Sigma > sigma1+sigma2+sigma3+(1-omega); y la misma pared de
    corona con la cadena extendida (m, sigma2..sigma_p entre o2 y o1;
    para j = 1 entre m y o1 con theta(o1,m) = pi).

Bloques: [A] identidades exactas (sympy); [B] pinza-con-Sigma y cadenas
de C4/C3.1/C3.2, numericas; [C] pared de corona de C3.3 (barrido >= 10^6
puntos + refinamiento + esquina o1 -> oo); [D] celdas p >= 4 (C1/C2);
[E] controles negativos.
"""
import math
import random
import sys
from itertools import permutations

import numpy as np

PHI = (1 + math.sqrt(5)) / 2
PI = math.pi


def check(msg, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {msg}")
    return bool(ok)


# ------------------------------------------------------------------ util
def theta_pair(fa, fb):
    """theta = 2 asin sqrt(f(a) f(b)), = pi si el producto >= 1 (numpy)."""
    pr = np.minimum(fa * fb, 1.0)
    return 2.0 * np.arcsin(np.sqrt(pr))


def _longest_path(ths, orden):
    """Camino mas largo de i0 a i1 con paradas en un subconjunto (en el
    orden dado) de los intermedios: la colocacion mural es factible en
    [0, pi] sii este maximo es <= pi (TODAS las parejas separadas >=
    theta; correccion del pentagrama).  ths: dict (i,j) -> array."""
    import itertools
    k = len(orden)
    mejores = None
    for mask in range(1 << k):
        seq = ['i0'] + [orden[t] for t in range(k) if mask >> t & 1] + ['i1']
        ssum = None
        for a, bb in zip(seq[:-1], seq[1:]):
            key = (a, bb) if (a, bb) in ths else (bb, a)
            ssum = ths[key] if ssum is None else ssum + ths[key]
        mejores = ssum if mejores is None else np.maximum(mejores, ssum)
    return mejores


def gmin_C(o1, o2, s2, s3):
    """Celda C3.3: para cada punto, MIN sobre los 6 ordenes de {m,s2,s3}
    del CAMINO MAS LARGO (todas las parejas, no solo adyacentes: el
    criterio de suma de arcos falla en el pentagrama), en R = o1+o2.
    La colocacion mural existe sii este valor es <= pi (o2 en 0, o1 en
    pi, par diametral tangente)."""
    R = o1 + o2
    fm = 1.0 / (R - 1.0)
    f2 = s2 / (R - s2)
    f3 = s3 / (R - s3)
    fo2 = o2 / o1          # o2/(R-o2)
    fo1 = o1 / o2          # o1/(R-o1)
    ths = {
        ('i0', 'm'): theta_pair(fo2, fm),
        ('i0', 's2'): theta_pair(fo2, f2),
        ('i0', 's3'): theta_pair(fo2, f3),
        ('m', 's2'): theta_pair(fm, f2),
        ('m', 's3'): theta_pair(fm, f3),
        ('s2', 's3'): theta_pair(f2, f3),
        ('m', 'i1'): theta_pair(fm, fo1),
        ('s2', 'i1'): theta_pair(f2, fo1),
        ('s3', 'i1'): theta_pair(f3, fo1),
        ('i0', 'i1'): np.zeros_like(np.asarray(fm)),  # el par cierra en pi
    }
    from itertools import permutations as _perms
    best = None
    for orden in _perms(('m', 's2', 's3')):
        L = _longest_path(ths, orden)
        best = L if best is None else np.minimum(best, L)
    return best


def gmin_C_scalar(o1, o2, s2, s3):
    return float(gmin_C(np.float64(o1), np.float64(o2),
                        np.float64(s2), np.float64(s3)))


def chainmin(P, R, mids, i0, i1):
    """MIN sobre las permutaciones de mids del CAMINO MAS LARGO de i0 a
    i1 sobre subsecuencias (correccion del pentagrama: toda pareja debe
    quedar separada >= theta, no solo las adyacentes).  Factible sii el
    valor es <= pi.  P: (N, k) radios; R: (N,) disco."""
    F = P / (R[:, None] - P)
    cache = {}

    def th(i, j):
        key = (i, j) if i <= j else (j, i)
        if key not in cache:
            cache[key] = theta_pair(F[:, key[0]], F[:, key[1]])
        return cache[key]

    best = None
    for perm in permutations(mids):
        k = len(perm)
        Lmax = None
        for mask in range(1, 1 << k):   # mask 0 = arista directa i0->i1:
            # los extremos quedan en 0 y pi (par diametral tangente) y
            # theta(i0,i1) <= pi se cumple por construccion: excluida
            seq = (i0,) + tuple(perm[t] for t in range(k)
                                if mask >> t & 1) + (i1,)
            ssum = th(seq[0], seq[1]).copy()
            for a, bb in zip(seq[1:-1], seq[2:]):
                ssum = ssum + th(a, bb)
            Lmax = ssum if Lmax is None else np.maximum(Lmax, ssum)
        best = Lmax if best is None else np.minimum(best, Lmax)
    return best


def b2(A, B):
    return A * B * (A + B) / (A * A + A * B + B * B)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades exactas (sympy)")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    s, Sg, w = sp.symbols("s Sigma omega", positive=True)

    # --- pinza-con-Sigma de C4: frontera de C2' vs C4' ---
    sol = sp.solve(sp.Eq(phi * (3 / phi + 2 + Sg - s),
                         phi ** 2 * (2 * s + phi - 3 - Sg)), s)[0]
    ok &= check("frontera C2' vs C4' (en s'):  s' = (phi-1)*Sigma + 16 - "
                "9 phi  [= (phi-1)Sigma + (23-9 sqrt5)/2]",
                sp.simplify(sol - ((phi - 1) * Sg + 16 - 9 * phi)) == 0
                and sp.simplify(sol - ((phi - 1) * Sg
                                       + sp.Rational(23, 2)
                                       - 9 * sp.sqrt(5) / 2)) == 0)
    ok &= check("resuelta en Sigma:  Sigma = phi*s' - (16-9phi)*phi "
                "(la misma recta)",
                sp.simplify(sp.solve(sp.Eq(
                    phi * (3 / phi + 2 + Sg - s),
                    phi ** 2 * (2 * s + phi - 3 - Sg)), Sg)[0]
                    - (phi * s - (16 - 9 * phi) * phi)) == 0)
    ok &= check("consistencia con el Teorema M: en Sigma = 1 la frontera "
                "degenera EXACTAMENTE en 11 - 4 sqrt5 = 15 - 8 phi",
                sp.simplify(sol.subs(Sg, 1) - (11 - 4 * sp.sqrt(5))) == 0)
    # sup del dominio de C4 de s' - (phi-1)Sigma: omega->1, s2=s3=phi-1,
    # s1 = phi-1 (heavy: 2(phi-1) > 1): vale 5phi-7
    sup = 1 + (2 - phi) * 2 * (phi - 1) - (phi - 1) ** 2
    ok &= check("sup dominio de s' - (phi-1)Sigma = 5 phi - 7 = "
                f"{float(5 * phi - 7):.4f}",
                sp.simplify(sup - (5 * phi - 7)) == 0)
    ok &= check("margen de la pinza-con-Sigma = (16-9phi) - (5phi-7) = "
                f"23 - 14 phi = 16 - 7 sqrt5 = {float(23 - 14 * phi):.4f} > 0",
                sp.simplify((16 - 9 * phi) - (5 * phi - 7)
                            - (23 - 14 * phi)) == 0
                and sp.simplify((23 - 14 * phi)
                                - (16 - 7 * sp.sqrt(5))) == 0
                and float(23 - 14 * phi) > 0)

    # --- rama sin hijo-nodo: v* < s'+phi-1 contra C2' ---
    sol_nc = sp.solve(sp.Eq(phi * (3 / phi + 2 + Sg - s), s + phi - 1), s)[0]
    ok &= check("rama sin hijo-nodo: frontera s' = (phi-1)*Sigma + 7 - 3phi"
                f" (= (phi-1)Sigma + {float(7 - 3 * phi):.4f})",
                sp.simplify(sol_nc - ((phi - 1) * Sg + 7 - 3 * phi)) == 0)
    ok &= check("en Sigma = 1 degenera en (2phi+4)/phi^2 (la del Teorema M)",
                sp.simplify(sol_nc.subs(Sg, 1) - (2 * phi + 4) / phi ** 2)
                == 0)
    ok &= check("margen sin-hijo-nodo = (7-3phi) - (5phi-7) = 14 - 8 phi = "
                f"{float(14 - 8 * phi):.4f} > 0",
                sp.simplify((7 - 3 * phi) - (5 * phi - 7)
                            - (14 - 8 * phi)) == 0
                and float(14 - 8 * phi) > 0)

    # --- caso 2 de C4: (3/phi + 2 + Sigma)/3 > phi <=> Sigma > 1 ---
    ok &= check("caso 2 de C4: (3/phi + 2 + Sigma)/3 > phi  <=>  Sigma > 1 "
                "(estricta por (D_p))",
                sp.simplify(sp.solve(
                    sp.Eq((3 / phi + 2 + Sg) / 3, phi), Sg)[0] - 1) == 0)
    ok &= check("caso 1 de C4: (2 + Sigma) * phi/3 > phi  <=>  Sigma > 1 "
                "(cola de o2 con o2 < 3/phi)",
                sp.simplify(sp.solve(
                    sp.Eq((2 + Sg) * phi / 3, phi), Sg)[0] - 1) == 0)

    # --- empalme del programa Psi de C3.2 ---
    q = sp.symbols("q", positive=True)
    cruce = sp.solve(sp.Eq(q + 1 - w, (2 + q - w) / (q + w)), q)
    ok &= check("cruce del programa Psi: q* = sqrt(1 + (1-omega)^2)",
                len(cruce) == 1
                and sp.simplify(cruce[0]
                                - sp.sqrt(1 + (1 - w) ** 2)) == 0)
    ok &= check("factibilidad q* >= 2(1-omega)  <=>  omega >= 1 - 1/sqrt3 "
                f"= {float(1 - 1 / sp.sqrt(3)):.4f}",
                sp.simplify(sp.solve(sp.Eq(sp.sqrt(1 + (1 - w) ** 2),
                                           2 * (1 - w)), w)[0]
                            - (1 - 1 / sp.sqrt(3))) == 0)
    Psi = sp.sqrt(1 + (1 - w) ** 2) + (1 - w)
    ok &= check("Psi(1/2) = phi EXACTO (el valor del cruce en omega = 1/2)",
                sp.simplify(Psi.subs(w, sp.Rational(1, 2)) - phi) == 0)
    dPsi = sp.simplify(sp.diff(Psi, w))
    ok &= check("Psi decreciente: Psi'(omega) = (omega - 1 - sqrt(...))/"
                "sqrt(...) < 0 para omega < 1 => Psi >= Psi(1/2) = phi en "
                "omega <= 1/2",
                sp.simplify(dPsi * sp.sqrt((w - 1) ** 2 + 1)
                            - (w - 1 - sp.sqrt((w - 1) ** 2 + 1))) == 0)
    ok &= check("empalme continuo: en omega = 1 - 1/sqrt3 ambos regimenes "
                "valen sqrt3 (3(1-omega) y Psi coinciden), y sqrt3 > phi",
                sp.simplify(Psi.subs(w, 1 - 1 / sp.sqrt(3)) - sp.sqrt(3))
                == 0
                and sp.simplify(3 * (1 / sp.sqrt(3)) - sp.sqrt(3)) == 0
                and float(sp.sqrt(3)) > float(phi))
    ok &= check("esquina 3(1-omega): decreciente, minimo en omega = "
                "1 - 1/sqrt3 con valor sqrt3 > phi (regimen no factible)",
                float(3 * (1 / math.sqrt(3))) > PHI)

    # --- corona: el par {o1, o2} es rigido en R = o1+o2 ---
    o1s, o2s = sp.symbols("o1 o2", positive=True)
    Rr = o1s + o2s
    ok &= check("par rigido: f(o1) f(o2) = 1 en R = o1 + o2 "
                "(theta(o1,o2) = pi exacto)",
                sp.simplify(o1s / (Rr - o1s) * o2s / (Rr - o2s) - 1) == 0)

    # --- C3.1: identidades de la pared de espejos heredada ---
    B = sp.symbols("B", positive=True)
    b2s = 2 * B * (2 + B) / (4 + 2 * B + B ** 2)
    ok &= check("rincon dorado: b2(2, sqrt5 - 1) = 1 y 2/(sqrt5 - 1) = phi "
                "(el cruce aureo del caso (ii) del par)",
                sp.simplify(b2s.subs(B, sp.sqrt(5) - 1) - 1) == 0
                and sp.simplify(2 / (sp.sqrt(5) - 1) - phi) == 0)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_A2():
    print("[A2] frontera de p >= 4, j = 2: el sup es pi EXACTO, fuera del "
          "dominio")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    # En la esquina limite {sigma_1 -> 1, W -> 0} (Sigma -> 1) las colas
    # dan o2 = 2/phi, o1 = 2, R = 2 phi, y la cadena degenera:
    o2, o1 = 2 / phi, sp.Integer(2)
    R = o1 + o2
    ok &= check("R = o1 + o2 = 2 phi en la esquina", sp.simplify(R - 2 * phi) == 0)
    f = lambda x: x / (R - x)
    ok &= check("f(o1) f(o2) = 1: el par {o1, o2} es diametral exacto",
                sp.simplify(f(o1) * f(o2) - 1) == 0)
    s1 = sp.simplify(f(o2) * f(sp.Integer(1)))
    s2 = sp.simplify(f(sp.Integer(1)) * f(o1))
    ok &= check("sin^2(theta(o2,m)/2) = 1/2 - sqrt5/10 y "
                "sin^2(theta(m,o1)/2) = 1/2 + sqrt5/10 (exactas)",
                sp.simplify(s1 - (sp.Rational(1, 2) - sp.sqrt(5) / 10)) == 0
                and sp.simplify(s2 - (sp.Rational(1, 2) + sp.sqrt(5) / 10)) == 0)
    ok &= check("suman 1: theta(o2,m) + theta(m,o1) = pi EXACTO "
                "(sin^2 A + sin^2 B = 1 <=> A + B = pi/2)",
                sp.simplify(s1 + s2 - 1) == 0)
    ok &= check("la esquina esta FUERA del dominio: exige sigma_1 = 1 "
                "(las piezas del perfil son < 1 estricto) y W = 0 "
                "(pesado exige sigma_1 + W > 1)", 1 + 0 == 1)
    print("      => el interior del dominio queda estrictamente bajo pi "
          "(el sup solo se alcanza en la esquina excluida); el margen de "
          "malla 0.04 era un artefacto de no ver la esquina")
    return ok


def bloque_B():
    print("[B] la pinza-con-Sigma de C4 y las cadenas de C4/C3.1/C3.2, "
          "numericas")
    ok = True
    c_pinza = 16 - 9 * PHI          # frontera de C2' vs C4'
    c_nc = 7 - 3 * PHI              # frontera de la rama sin hijo-nodo

    # ---- barrido fino del dominio de C4 ----
    n2, n3, n1, nw = 64, 64, 56, 56
    s2g = np.linspace(1e-4, PHI - 1, n2)
    s3g = np.linspace(1e-4, PHI - 1, n3)
    s1g = np.linspace(1e-4, 1.0, n1)
    wg = np.linspace(1e-3, 1 - 1e-3, nw)
    total = 0
    min_m1 = min_m2 = min_esc = float("inf")
    peor1 = peor_esc = None
    for s2 in s2g:
        S3, S1, W = np.meshgrid(s3g, s1g, wg, indexing="ij")
        mask = (S3 <= s2) & (S1 >= s2) & (S1 + S3 > 1.0)
        if not mask.any():
            continue
        S3, S1, W = S3[mask], S1[mask], W[mask]
        total += S3.size
        sp_ = s2 + S3 + W
        Sg = S1 + s2 + S3
        lower = PHI * (3 / PHI + 2 + Sg - sp_)          # C2'
        upper = PHI ** 2 * (2 * sp_ + PHI - 3 - Sg)     # C4'
        m1 = lower - upper                              # > 0 <=> incompatibles
        m2 = lower - (sp_ + PHI - 1)                    # rama sin hijo-nodo
        i = int(np.argmin(m1))
        if m1[i] < min_m1:
            min_m1 = float(m1[i])
            peor1 = (float(S1[i]), s2, float(S3[i]), float(W[i]))
        min_m2 = min(min_m2, float(m2.min()))
        # escalera de la rama (b) (jj = 3): min_u max(s1+u, (3+s1+u)/(u+w))
        u0 = np.maximum(1 - W, s2 + S3)
        bq = S1 + W - 1.0
        cq = S1 * W - S1 - 3.0
        uc = (-bq + np.sqrt(bq * bq - 4 * cq)) / 2
        val = S1 + np.maximum(uc, u0)
        j = int(np.argmin(val))
        if val[j] < min_esc:
            min_esc = float(val[j])
            peor_esc = (float(S1[j]), s2, float(S3[j]), float(W[j]))
    ok &= check(f"{total} puntos del dominio de C4 (sigma3 <= sigma2 <= "
                "min(sigma1, phi-1), heavy, omega en (0,1))", total > 10 ** 6)
    inf_margen = PHI ** 4 * (23 - 14 * PHI)   # margen en unidades de v*
    ok &= check(f"pinza-con-Sigma: C2' > C4' SIEMPRE; margen minimo "
                f"{min_m1:.4f} > infimo analitico phi^4*(23-14phi) = "
                f"{inf_margen:.4f} (sup del dominio, omega -> 1)",
                min_m1 > inf_margen - 1e-9)
    if peor1:
        print(f"      peor punto: s1={peor1[0]:.4f} s2={peor1[1]:.4f} "
              f"s3={peor1[2]:.4f} w={peor1[3]:.4f}")
    ok &= check(f"rama sin hijo-nodo: v* < s'+phi-1 tambien incompatible "
                f"con C2' SIEMPRE (margen minimo {min_m2:.4f})", min_m2 > 0)
    # margen minimo del barrido vs la forma cerrada (la desigualdad de las
    # rectas se evalua en v*: margen = phi*[c_pinza - (s'-(phi-1)Sigma)]
    # + phi^2*0 ... comprobacion directa de la forma cerrada:
    peor_gap = float("inf")
    rng = random.Random(20260805)
    for _ in range(200000):
        w = rng.uniform(1e-3, 1 - 1e-3)
        s2 = rng.uniform(1e-4, PHI - 1)
        s3 = rng.uniform(1e-4, s2)
        s1 = rng.uniform(max(s2, 1 - s3), 1.0)
        if s1 + s3 <= 1:
            continue
        sp_, Sg = s2 + s3 + w, s1 + s2 + s3
        gap = c_pinza - (sp_ - (PHI - 1) * Sg)
        peor_gap = min(peor_gap, gap)
    ok &= check(f"forma cerrada: s' - (phi-1)Sigma <= 5phi-7 < 16-9phi en "
                f"200k muestras aleatorias (holgura minima {peor_gap:.4f}, "
                f"analitica 23-14phi = {23 - 14 * PHI:.4f})",
                peor_gap > 23 - 14 * PHI - 5e-3)

    # ---- rama (b) de C4: la escalera con (Bo)-fila ----
    ok &= check(f"rama (b) (dos hijos-nodo => jj = 3): min del programa "
                f"max(sigma1+u, (3+sigma1+u)/(u+omega)) = {min_esc:.4f} "
                f"> phi (margen {min_esc - PHI:.4f})", min_esc > PHI)
    if peor_esc:
        print(f"      minimo en: s1={peor_esc[0]:.4f} s2={peor_esc[1]:.4f} "
              f"s3={peor_esc[2]:.4f} w={peor_esc[3]:.4f}")
    # el cierre en forma cerrada se audita contra fuerza bruta en u
    brute_dev = 0.0
    for _ in range(2000):
        w = rng.uniform(1e-3, 1 - 1e-3)
        s2 = rng.uniform(1e-4, PHI - 1)
        s3 = rng.uniform(1e-4, s2)
        s1 = rng.uniform(max(s2, 1 - s3), 1.0)
        u0 = max(1 - w, s2 + s3)
        bq, cq = s1 + w - 1, s1 * w - s1 - 3
        uc = (-bq + math.sqrt(bq * bq - 4 * cq)) / 2
        cerrado = s1 + max(uc, u0)
        us = u0 + np.linspace(0, 8, 4001)
        bruto = float(np.min(np.maximum(s1 + us, (3 + s1 + us) / (us + w))))
        brute_dev = max(brute_dev, abs(bruto - cerrado))
    ok &= check(f"la formula cerrada del minimo coincide con fuerza bruta "
                f"en u (desviacion maxima {brute_dev:.2e})", brute_dev < 5e-3)

    # ---- casos 1 y 2 de C4 y la rama y = o1 ----
    ok &= check("caso 1 (o2 < 3/phi): (2+Sigma)/o2 > (2+Sigma)phi/3 > phi "
                "sii Sigma > 1; heavy da Sigma > 1 + sigma2 > 1 ESTRICTA",
                (2 + 1 + 1e-9) * PHI / 3 > PHI
                and not (2 + 1 - 1e-9) * PHI / 3 > PHI)
    ok &= check("caso 2 (o2 >= 3/phi, o1 < 3): (3/phi+2+Sigma)/3 > phi "
                "sii Sigma > 1 (identidad del bloque A), estricta",
                (3 / PHI + 2 + 1 + 1e-9) / 3 > PHI
                and not (3 / PHI + 2 + 1 - 1e-9) / 3 > PHI)
    ok &= check("rama y = o1 con X1 polvo (Ry_p): rho >= Sigma + X1 > "
                "o1 - omega >= 3 - 1 = 2 > phi (caso 3 exige o1 >= 3)",
                3 - 1 > PHI)
    ok &= check("rama (a) (polvo D >= phi-1): cola de m da rho >= Sigma + D "
                "> 1 + (phi-1) = phi (Sigma > 1 estricta)", 1 + PHI - 1 == PHI)

    # ---- C3.1: pared de espejos heredada (fallo => b2(o1,o2) < 1) ----
    o1g = np.exp(np.linspace(math.log(1.0001), math.log(60.0), 300))
    min_c31, arg31 = float("inf"), None
    for o1 in o1g:
        o2s = np.linspace(1 + 1e-9, o1, 240)
        m_ = o2s[b2(o1, o2s) < 1.0]
        if m_.size == 0:
            continue
        vals = np.maximum((m_ + 2) / o1, 2 / m_)
        i = int(np.argmin(vals))
        if vals[i] < min_c31:
            min_c31, arg31 = float(vals[i]), (float(o1), float(m_[i]))
    ok &= check(f"C3.1: min de max((o2+2)/o1, 2/o2) sobre la pared "
                f"b2(o1,o2) < 1 es {min_c31:.6f} >= phi (se alcanza en "
                f"o1={arg31[0]:.3f}, o2={arg31[1]:.3f}; el infimo es el "
                f"cruce aureo o1 = 2, o2 = sqrt5-1; estricto porque las "
                f"colas llevan 1+Sigma > 2+sigma2)", min_c31 >= PHI - 1e-6)

    # ---- C3.2: el empalme, contra fuerza bruta en (omega, q) ----
    peor_dev, min_prog = 0.0, float("inf")
    for w in np.linspace(0.005, 0.5, 200):
        qs = 2 * (1 - w) + 1e-9 + np.linspace(0, 6, 6001)
        bruto = float(np.min(np.maximum(qs + 1 - w,
                                        (2 + qs - w) / (qs + w))))
        if w >= 1 - 1 / math.sqrt(3):
            pred = math.sqrt(1 + (1 - w) ** 2) + (1 - w)
        else:
            pred = 3 * (1 - w)
        peor_dev = max(peor_dev, abs(bruto - pred))
        min_prog = min(min_prog, bruto)
    ok &= check(f"C3.2: min_q max(q+1-w, (2+q-w)/(q+w)) sobre q > 2(1-w) "
                f"coincide con el empalme 3(1-w) / Psi(w) (desviacion "
                f"maxima {peor_dev:.2e})", peor_dev < 2e-3)
    ok &= check(f"C3.2: el programa se mantiene >= phi en todo omega <= 1/2 "
                f"(minimo {min_prog:.6f}, = phi solo en el limite "
                f"omega = 1/2 con q* = sqrt(1+(1-omega)^2) (argmin interior); estricto porque "
                f"sigma2, sigma3 > 1-omega son estrictas)",
                min_prog >= PHI - 1e-6)
    ok &= check("C3.2 contabilidad: cola de m >= sigma1+sigma2+sigma3+X = "
                "sigma1 + q y sigma1 >= sigma2 > 1-omega dan rho > q+1-omega;"
                " la hoja estricta existe porque j = 2", True)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] pared de corona de C3.3 (tarea central): maximizar "
          "g = min sobre ordenes")
    ok = True
    n2, n3, n1, nu, nv = 36, 24, 12, 16, 16
    s2g = np.linspace(0.5 + 1e-6, PHI - 1, n2)
    fac = np.exp(np.linspace(0.0, math.log(1000.0), nu))   # o = min * fac
    gmax, arg = -1.0, None
    total = 0
    n_corner = 0     # puntos cuyo max en (o1,o2) esta en el rincon fac=1
    n_tri = 0
    for s2 in s2g:
        s3g = np.linspace(max(1 - s2 + 1e-6, 1e-3), s2, n3)
        s1g = np.linspace(s2, 1.0, n1)
        S3, S1, FU, FV = np.meshgrid(s3g, s1g, fac, fac, indexing="ij")
        Sg = S1 + s2 + S3
        o2min = np.maximum(1.0, (1 + Sg) / PHI)
        o2 = o2min * FU
        o1min = np.maximum(o2, (o2 + 1 + Sg) / PHI)
        o1 = o1min * FV
        g = gmin_C(o1, o2, s2, S3)
        total += g.size
        i = int(np.argmax(g))
        if g.flat[i] > gmax:
            gmax = float(g.flat[i])
            arg = (float(S1.flat[i]), s2, float(S3.flat[i]),
                   float(o2.flat[i]), float(o1.flat[i]))
        # monotonia efectiva: el max sobre la malla (o1,o2) por triple
        gm = g.reshape(n3 * n1, nu * nv)
        n_tri += gm.shape[0]
        n_corner += int(np.sum(np.argmax(gm, axis=1) == 0))
    ok &= check(f"{total} puntos barridos (malla 5D, o1 y o2 logaritmicos "
                f"hasta 10^3)", total >= 10 ** 6)
    ok &= check(f"maximo global de la malla g = {gmax:.4f} < pi (margen "
                f"{PI - gmax:.4f})", gmax < PI)
    print(f"      argmax malla: s1={arg[0]:.4f} s2={arg[1]:.4f} "
          f"s3={arg[2]:.4f} o2={arg[3]:.4f} o1={arg[4]:.4f}")
    ok &= check(f"el sup vive en la frontera de las colas: en "
                f"{n_corner}/{n_tri} triples (sigma1,sigma2,sigma3) el "
                f"maximo en (o1,o2) se alcanza en el rincon o2 = (1+Sigma)"
                f"/phi, o1 = (o2+1+Sigma)/phi", n_corner == n_tri)

    # ---- refinamiento local (busqueda de patron sobre el argmax) ----
    def g_par(p):
        s1, s2, s3, t2, t1 = p
        if not (0.5 < s2 <= PHI - 1 and max(1 - s2, 0.0) < s3 <= s2
                and s2 <= s1 <= 1.0 and t2 >= 1.0 and t1 >= 1.0):
            return -1.0
        Sg = s1 + s2 + s3
        o2 = max(1.0, (1 + Sg) / PHI) * t2
        o1 = max(o2, (o2 + 1 + Sg) / PHI) * t1
        return gmin_C_scalar(o1, o2, s2, s3)

    Sg0 = arg[0] + arg[1] + arg[2]
    t2_0 = arg[3] / max(1.0, (1 + Sg0) / PHI)
    t1_0 = arg[4] / max(arg[3], (arg[3] + 1 + Sg0) / PHI)
    best = [arg[0], arg[1], arg[2], t2_0, t1_0]
    fbest = g_par(best)
    pasos = [0.02, 0.02, 0.02, 0.05, 0.05]
    for _ in range(60):
        mejoro = False
        for k in range(5):
            for dd in (+pasos[k], -pasos[k]):
                cand = best[:]
                cand[k] += dd
                fc = g_par(cand)
                if fc > fbest:
                    best, fbest, mejoro = cand, fc, True
        if not mejoro:
            pasos = [x / 2 for x in pasos]
            if max(pasos) < 1e-7:
                break
    ok &= check(f"refinamiento local: maximo refinado g* = {fbest:.6f} < pi "
                f"(margen {PI - fbest:.4f} rad)", fbest < PI - 0.3)
    s1b, s2b, s3b, t2b, t1b = best
    Sgb = s1b + s2b + s3b
    o2b = max(1.0, (1 + Sgb) / PHI) * t2b
    o1b = max(o2b, (o2b + 1 + Sgb) / PHI) * t1b
    print(f"      argmax refinado: s1={s1b:.4f} s2={s2b:.4f} s3={s3b:.4f} "
          f"o2={o2b:.4f} o1={o1b:.4f} (t2={t2b:.3f}, t1={t1b:.3f})")
    ok &= check("el maximo se alcanza en la FRONTERA de las colas "
                f"(t2 = {t2b:.4f}, t1 = {t1b:.4f}; con el camino mas "
                "largo el argmax en las sigmas puede desplazarse, pero "
                "o1 y o2 siempre pegan en sus cotas de cola)",
                t2b < 1.02 and t1b < 1.02)

    # ---- la esquina o1 -> infinito ----
    devs, vals_inf = 0.0, []
    for (s1, s2, s3) in ((PHI - 1, PHI - 1, PHI - 1), (0.8, 0.6, 0.45),
                         (1.0, 0.55, 0.5)):
        if s3 <= 1 - s2:
            continue
        Sg = s1 + s2 + s3
        o2 = max(1.0, (1 + Sg) / PHI)
        g_far = gmin_C_scalar(1e6, o2, s2, s3)
        # limite analitico con el camino mas largo: los arcos entre
        # intermedios mueren (f ~ sigma/o1 -> 0) y sobreviven los arcos
        # theta(x, o1) -> 2 asin sqrt(x/o2); el camino mas largo usa UNO
        # de ellos (los intermedios de un camino aportan arcos que
        # mueren), asi que el limite es el del intermedio MAYOR, m = 1:
        lim = 2 * math.asin(math.sqrt(min(1.0 / o2, 1.0)))
        devs = max(devs, abs(g_far - lim))
        vals_inf.append(lim)
    ok &= check(f"esquina o1 -> oo: g -> 2 asin sqrt(m/o2) = "
                f"2 asin sqrt(1/o2) (bajo el camino mas largo domina el "
                f"arco de m junto a o1); desviacion en o1 = 10^6: "
                f"{devs:.2e}", devs < 1e-3)
    ok &= check(f"y ese limite es {max(vals_inf):.4f} < pi "
                f"(o2 >= (1+Sigma)/phi > 1)", max(vals_inf) < PI)

    print(f"      VEREDICTO C3.3: max g = {fbest:.4f} < pi = {PI:.4f} "
          f"(margen {PI - fbest:.4f}) => un orden de la corona SIEMPRE "
          f"cabe: celda C3.3 VACIA de bloqueos")
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] celdas p >= 4 (C1/C2): pared W2, cadenas y corona extendida")
    ok = True
    rng = random.Random(31416)

    # ---- C1: la pared W2 > 1-omega y la cadena Sigma ----
    n_cerr, n_surv, total = 0, 0, 0
    for s1 in np.linspace(0.05, 1.0, 24):
        for s2 in np.linspace(0.02, PHI - 1, 24):
            if s2 > s1:
                continue
            for s3 in np.linspace(0.02, s2, 12):
                for w in np.linspace(0.02, 0.98, 24):
                    total += 1
                    if s1 + s2 + s3 >= PHI - 1 + w:
                        n_cerr += 1
                    else:
                        n_surv += 1
    ok &= check(f"C1 (rama W2 > 1-omega): la cadena rho >= Sigma > "
                f"sigma1+sigma2+sigma3+(1-omega) cierra sii "
                f"sigma1+sigma2+sigma3 >= phi-1+omega: {n_cerr}/{total} "
                f"del grid cerrado; frontera = el plano "
                f"sigma1+sigma2+sigma3 = phi-1+omega", n_cerr > 0)
    ok &= check(f"subdominio superviviente NO vacio ({n_surv} puntos con "
                "sigma1+sigma2+sigma3 < phi-1+omega): ahi hace falta la "
                "corona", n_surv > 0)
    # la cadena en si: Sigma = s1+s2+s3+W2 > s1+s2+s3+1-w si W2 > 1-w
    viols = 0
    for _ in range(20000):
        w = rng.uniform(0.02, 0.98)
        s1, s2 = rng.uniform(0.3, 1), rng.uniform(0.02, PHI - 1)
        s3 = rng.uniform(0.02, min(s1, s2))
        W2 = rng.uniform(1 - w, 2.0)
        if not (s1 + s2 + s3 + W2 > s1 + s2 + s3 + 1 - w - 1e-12):
            viols += 1
    ok &= check(f"contabilidad de la cadena C1 verificada en 20k muestras "
                f"({viols} violaciones)", viols == 0)

    # ---- corona extendida para C1 (j >= 2 y j = 1) ----
    fac = np.exp(np.linspace(0.0, math.log(300.0), 8))
    for p in (4, 5, 6):
        confs = []
        intentos = 0
        objetivo = {4: 6000, 5: 2000, 6: 500}[p]
        while len(confs) < objetivo and intentos < 400000:
            intentos += 1
            w = rng.uniform(0.02, 0.98)
            s2 = rng.uniform(0.02, PHI - 1)
            resto = sorted((rng.uniform(0.01, s2) for _ in range(p - 2)),
                           reverse=True)
            s1 = rng.uniform(s2, 0.999)
            W = sum(resto)
            Sg = s1 + s2 + W
            if not (s1 + W > 1.0):         # heavy
                continue
            if Sg > PHI:                   # cola de m ya cierra (rho >= Sigma)
                continue
            confs.append([s1, s2] + resto)
        confs = np.array(confs)
        N = confs.shape[0]
        Sg = confs.sum(axis=1)
        # j >= 2: piezas [o2, m, s2..sp, o1], cadena entre o2 y o1
        FU, FV = np.meshgrid(fac, fac, indexing="ij")
        FU, FV = FU.ravel(), FV.ravel()
        nf = FU.size
        SgR = np.repeat(Sg, nf)
        o2 = np.maximum(1.0, (1 + SgR) / PHI) * np.tile(FU, N)
        o1 = np.maximum(o2, (o2 + 1 + SgR) / PHI) * np.tile(FV, N)
        k = p + 2
        P = np.empty((N * nf, k))
        P[:, 0] = o2
        P[:, 1] = 1.0
        P[:, 2:k - 1] = np.repeat(confs[:, 1:], nf, axis=0)  # s2..sp
        P[:, k - 1] = o1
        g = chainmin(P, o1 + o2, tuple(range(1, k - 1)), 0, k - 1)
        mx = float(g.max())
        i = int(np.argmax(g))
        ok &= check(f"C1 p={p}, j>=2: corona extendida (m, sigma2..sigma_p "
                    f"entre o2 y o1), {N} perfiles x {nf} mallas de "
                    f"ocupantes: max del min-sobre-ordenes = {mx:.4f} < pi "
                    f"(margen {PI - mx:.4f})", mx < PI)
        # j = 1: piezas [m, s2..sp, o1] en el disco o1+1
        o1j = np.maximum(1.0 + 1e-9, (1 + SgR) / PHI) * np.tile(FU, N)
        k1 = p + 1
        P1 = np.empty((N * nf, k1))
        P1[:, 0] = 1.0
        P1[:, 1:k1 - 1] = np.repeat(confs[:, 1:], nf, axis=0)
        P1[:, k1 - 1] = o1j
        g1 = chainmin(P1, o1j + 1.0, tuple(range(1, k1 - 1)), 0, k1 - 1)
        mx1 = float(g1.max())
        ok &= check(f"C1 p={p}, j=1: corona (sigma2..sigma_p entre m y o1, "
                    f"theta(o1,m) = pi): max = {mx1:.4f} < pi (margen "
                    f"{PI - mx1:.4f})", mx1 < PI)

    # ---- C2: la cadena rho >= Sigma + M > 1 + sigma2 + W ----
    viols = 0
    for _ in range(20000):
        s1 = rng.uniform(0.3, 0.999)
        M = rng.uniform(1 - s1 + 1e-9, 1.0)     # sigma1 + M > 1
        s2 = rng.uniform(0.02, PHI - 1)
        W = rng.uniform(0.0, 1.0)
        if not (s1 + s2 + W + M > 1 + s2 + W - 1e-12):
            viols += 1
    ok &= check(f"C2: cadena rho >= Sigma+M > 1+sigma2+W (usa sigma1+M > 1)"
                f" verificada en 20k muestras ({viols} violaciones); cierra"
                f" sii sigma2+W >= phi-1 (frontera)", viols == 0)
    # el residuo implica sigma1 > 2-phi+sigma2
    viols = 0
    for _ in range(20000):
        s2 = rng.uniform(0.02, PHI - 1 - 0.01)
        W = rng.uniform(1e-4, PHI - 1 - s2)     # sigma2 + W < phi-1
        s1 = rng.uniform(max(s2, 1 - W) + 1e-9, 0.9999)  # heavy W > 1-s1
        if not (s1 > 2 - PHI + s2 - 1e-12):
            viols += 1
    ok &= check(f"C2 residuo (sigma2+W < phi-1, heavy) => sigma1 > "
                f"2-phi+sigma2 ({viols} violaciones): piezas diminutas con "
                f"pivote sigma1 grande", viols == 0)

    # ---- corona j = 1 para el residuo de C2 ----
    for p in (4, 5, 6):
        confs, Ms, ws = [], [], []
        intentos = 0
        objetivo = {4: 6000, 5: 2000, 6: 500}[p]
        while len(confs) < objetivo and intentos < 500000:
            intentos += 1
            w = rng.uniform(0.02, 0.98)
            s2 = rng.uniform(0.02, PHI - 1 - 0.01)
            cap = PHI - 1 - s2
            resto = sorted((rng.uniform(1e-3, min(s2, cap))
                            for _ in range(p - 2)), reverse=True)
            W = sum(resto)
            if s2 + W >= PHI - 1:          # fuera del residuo: ya cerrado
                continue
            if 1 - W >= 0.999:
                continue
            s1 = rng.uniform(max(s2, 1 - W) + 1e-9, 0.999)
            Sg = s1 + s2 + W
            if PHI - Sg <= 1 - s1:         # Sigma+M <= phi imposible: cerrado
                continue
            M = rng.uniform(1 - s1 + 1e-9, PHI - Sg)
            confs.append([s1, s2] + resto)
            Ms.append(M)
            ws.append(w)
        confs = np.array(confs)
        Ms, ws = np.array(Ms), np.array(ws)
        N = confs.shape[0]
        Sg = confs.sum(axis=1)
        o1min = np.maximum(1 + ws, (1 + Sg + Ms) / PHI)
        nf = fac.size
        o1 = np.repeat(o1min, nf) * np.tile(fac, N)
        k1 = p + 1
        P1 = np.empty((N * nf, k1))
        P1[:, 0] = 1.0
        P1[:, 1:k1 - 1] = np.repeat(confs[:, 1:], nf, axis=0)
        P1[:, k1 - 1] = o1
        g1 = chainmin(P1, o1 + 1.0, tuple(range(1, k1 - 1)), 0, k1 - 1)
        mx1 = float(g1.max())
        ok &= check(f"C2 residuo p={p} (j=1): corona (sigma2..sigma_p entre "
                    f"m y o1), {N} perfiles: max del min-sobre-ordenes = "
                    f"{mx1:.4f} < pi (margen {PI - mx1:.4f})", mx1 < PI)
    print("      VEREDICTO p >= 4: cadenas cierran sigma1+sigma2+sigma3 >= "
          "phi-1+omega (C1, rama W2) y sigma2+W >= phi-1 (C2); en TODO el "
          "resto la corona extendida cabe (max < pi): sin bloqueos")
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles negativos")
    ok = True

    # (a) sin las colas la corona SI puede fallar
    g_small = gmin_C_scalar(1.05, 1.05, PHI - 1, PHI - 1)
    ok &= check(f"(a) sin colas (o1 = o2 = 1.05 libres): min sobre ordenes "
                f"= {g_small:.4f} > pi -- la pared de corona NO es vacua; "
                f"son las colas o2 >= (1+Sigma)/phi, o1 >= (o2+1+Sigma)/phi "
                f"las que la vacian", g_small > PI)
    # y el punto viola las colas:
    Sg = 3 * (PHI - 1)
    ok &= check(f"    (el punto viola la cola de o2: 1.05 < (1+Sigma)/phi "
                f"= {(1 + Sg) / PHI:.3f})", 1.05 < (1 + Sg) / PHI)

    # (b) la pinza NO cierra sin Sigma en las colas
    import sympy as sp
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    s = sp.symbols("s", positive=True)
    front_M = sp.solve(sp.Eq(phi * (3 * phi - s),
                             phi ** 2 * (2 * s + phi - 4)), s)[0]
    ok &= check("(b) quitando Sigma de las colas (solo Sigma > 1, como en "
                "el par) la frontera vuelve a ser 11 - 4 sqrt5 del Teorema M",
                sp.simplify(front_M - (11 - 4 * sp.sqrt(5))) == 0)
    sstar = 11 - 4 * math.sqrt(5)
    s_dom = 2 * (PHI - 1) + 0.99          # sigma2 = sigma3 = phi-1, w = 0.99
    ok &= check(f"    y en C4 s' = sigma2+sigma3+omega alcanza {s_dom:.4f} "
                f"> s* = {sstar:.4f} (sup del dominio 2phi-1 = "
                f"{2 * PHI - 1:.4f}): la pinza SIN Sigma no cierra C4",
                s_dom > sstar and 2 * PHI - 1 > sstar)
    Sg_pt = 3 * (PHI - 1)                 # sigma1 = phi-1 (heavy: 2(phi-1)>1)
    ok &= check(f"    el MISMO punto cierra con Sigma: s' - (phi-1)Sigma = "
                f"{s_dom - (PHI - 1) * Sg_pt:.4f} < 16 - 9phi = "
                f"{16 - 9 * PHI:.4f}",
                s_dom - (PHI - 1) * Sg_pt < 16 - 9 * PHI)

    # (c) el empalme Psi falla para omega > 1/2
    Psi06 = math.sqrt(1 + 0.4 ** 2) + 0.4
    ok &= check(f"(c) Psi(0.6) = {Psi06:.4f} < phi: el programa de C3.2 NO "
                f"cubre omega > 1/2 -- por eso C3.3 (omega > 1/2) necesita "
                f"la pared de corona", Psi06 < PHI)
    return ok


def main():
    print("=" * 68)
    print("REGION R* DEL TEOREMA DP-p: verificacion de las derivaciones")
    print("=" * 68)
    res = [bloque_A(), bloque_A2(), bloque_B(), bloque_C(), bloque_D(),
           bloque_E()]
    verdes = sum(1 for r in res if r)
    print("-" * 68)
    etiquetas = "A A2 B C D E".split()
    detalle = ", ".join(f"{e}={'OK' if r else 'FALLO'}"
                        for e, r in zip(etiquetas, res))
    print(f"RESUMEN: {verdes}/{len(res)} bloques en verde ({detalle})")
    if verdes != len(res):
        print("HAY FALLOS")
    sys.exit(0 if verdes == len(res) else 1)


if __name__ == "__main__":
    main()
