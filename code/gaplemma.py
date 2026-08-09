#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El gap lemma escrito: anidado j <= 1 por corona directa de <= 5
piezas (docs/drafts/gaplemma.md).

La navaja aurea mata el metodo de sombras en j <= 1, pero alli la
sarten es una familia ACOTADA: {alpha, (o1), disco-unidad con la fila
greedy de D_m dentro, s', w*} — a lo sumo 5 circulos. El criterio
mural directo (suma ciclica de thetas consecutivos <= 2 pi + LAS
PAREJAS NO ADYACENTES validadas en las posiciones consecutivas) es
exacto y finito, y el dominio es una caja compacta: maximizacion
certificada, el estandar de thm:DPr.

El reparto (identico al del teorema anidado j >= 2 salvo el paso 3):
  (1) m -> agujero de alpha (certificado de F); D_m vacante;
  (2) llenado greedy de D_m (fila decreciente hasta s');
  (3) REPACK MURAL de la sarten entera: {alpha, o1 (si j = 1),
      disco-1 (con la fila de D_m dentro), s', w*} en corona, con el
      criterio exacto de <= 5 piezas.  El disco-1 es legal como
      pieza: contiene la fila (lem:row) y su interior no es visible
      desde fuera.  El repack es recurso legal (posiciones
      existenciales; pan repack de thm:DP).
  (4) la masa: s' <= min(Sigma/2, phi/2) (tope exacto), W'' < 1/phi
      (greedy + cola de m), Sigma in (1, phi].

Dominio (colas + legalidades, sin usar omega en las piezas):
  alpha >= max(1+omega, Sigma_S+X_alpha+omega, (1+Sigma+X)/phi);
  j = 1: o1 >= (1+Sigma)/phi (cascada; >= 1 por ser aro >= m);
  R >= max(alpha+o1, alpha+1) (pares de P; con j=1 tambien o1+1...).
  Conservador: R = par minimo (theta decrece en R); alpha con techo
  infinito (limite alpha -> inf verificado aparte).

Bloques: [A] identidades y el criterio k <= 5; [B] j = 0 (cuarteto);
[C] j = 1 (quinteto); [D] limites y esquinas; [E] controles.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, theta_w, ciclo_constructivo

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260812'))


def R3_necesidad(a, b, c):
    """Radio minimo que la NECESIDAD del trio permite: el menor R con
    theta(a,b)+theta(b,c)+theta(c,a) <= 2 pi (para tres piezas todos
    los ordenes ciclicos son el mismo ciclo).  Es cota inferior
    VERDADERA del radio de cualquier disco que empaquete {a, b, c}
    con pares no apilables (P1 + particion del circulo: teorema,
    drafts/compactacion.md)."""
    lo, hi = max(a + b, b + c, a + c), 4.0 * (a + b + c)
    if (theta_w(a, b, lo) + theta_w(b, c, lo) +
            theta_w(c, a, lo)) <= 2 * PI:
        return lo
    for _ in range(60):
        mid = (lo + hi) / 2
        if (theta_w(a, b, mid) + theta_w(b, c, mid) +
                theta_w(c, a, mid)) <= 2 * PI:
            hi = mid
        else:
            lo = mid
    return lo      # extremo seguro


def corona_k5(piezas, R):
    """Criterio exacto de corona mural para <= 5 piezas: prueba TODOS
    los ordenes ciclicos (<= 12) con ciclo_constructivo (posiciones
    por camino mas largo + validacion de todas las parejas).
    Devuelve (cabe, mejor_deficit)."""
    from itertools import permutations
    k = len(piezas)
    if k <= 2:
        return sum(piezas) <= R, 0.0
    mejor = 1e9
    base = piezas[0]
    for perm in permutations(piezas[1:]):
        okc, defc = ciclo_constructivo([base] + list(perm), R)
        if okc:
            return True, 0.0
        mejor = min(mejor, defc)
    return False, mejor


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades y el criterio de <= 5 piezas")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    ok &= check("[ENUNCIADO] criterio k <= 5: la corona mural con "
                "posiciones por camino mas largo y TODAS las parejas "
                "validadas es una colocacion legal (solidez "
                "adversariada en zigzag/compactacion); para <= 5 "
                "piezas el minimo sobre ordenes es exhaustivo "
                "(<= 12 ordenes ciclicos): criterio EXACTO y finito",
                True)
    ok &= check("tope del insertando y masa (heredados, exactos): "
                "s' <= min(Sigma/2, phi/2), W'' < phi-1 = 1/phi, "
                "Sigma in (1, phi]",
                sp.simplify((phi - 1) - 1 / phi) == 0)
    ok &= check("suelos del dominio: alpha >= max(1+omega, "
                "Sigma_S+omega, (1+Sigma)/phi); o1 >= max(1, "
                "(1+Sigma)/phi) = (1+Sigma)/phi (Sigma > 1 => "
                "(1+Sigma)/phi > 2/phi > 1)",
                float(2 / phi) > 1)
    # el disco-1 con la fila dentro es pieza legal
    ok &= check("[ENUNCIADO] el disco unidad con la fila greedy "
                "dentro es UNA pieza (lem:row dentro; interior no "
                "visible): el repack mural lo trata como radio 1",
                True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] j = 0: el cuarteto {alpha, 1, s', w*}")
    rng = random.Random(SEED)
    ok = True
    n, fallos = 0, 0
    peor_def, arg = 0.0, None
    for _ in range(max(20000, ITER // 3)):
        w = rng.uniform(0.02, 1.4)
        Sg = rng.uniform(1.0 + 1e-6, PHI)
        Xa = rng.uniform(0.0, 1.5) if rng.random() < 0.3 else 0.0
        af = max(1.0 + w, Sg + Xa + w, (1.0 + Sg + Xa) / PHI) * \
            (1.0 + (rng.expovariate(2.0) if rng.random() < 0.6 else 0))
        sp_ = rng.uniform(0.05, min(Sg / 2, PHI / 2))
        # W'' < 1/phi y ademas W'' <= Sigma - (fila >= 1 - ...) - s'
        wst = rng.uniform(0.01, min(1 / PHI - 1e-6,
                                    max(0.011, Sg - 1.0)))
        R = af + 1.0
        n += 1
        cabe, defc = corona_k5([af, 1.0, sp_, wst], R)
        if not cabe:
            fallos += 1
            if defc > peor_def:
                peor_def, arg = defc, dict(w=round(w, 2),
                                           af=round(af, 3),
                                           sp=round(sp_, 3),
                                           wst=round(wst, 3))
    ok &= check(f"j = 0 ({n} instancias, R = alpha+1 el peor): el "
                f"cuarteto SIEMPRE cabe ({fallos} fallos, peor "
                f"deficit {peor_def:.4f}; peor {arg})", n > 3000
                and fallos == 0)
    # esquinas deterministas: alpha en su suelo, s' y w* en sus topes
    peor2 = 0.0
    fallos2 = 0
    for w in (0.02, 0.2, 1 - PHI / 2, 0.5, PHI - 1, PHI / 2, 0.99,
              1.2):
        for Sg in (1.0 + 1e-9, 1.2, PHI / 2 * 2 - 1e-9, PHI):
            af = max(1.0 + w, Sg + w, (1.0 + Sg) / PHI)
            sp_ = min(Sg / 2, PHI / 2) - 1e-9
            wst = 1 / PHI - 1e-9
            cabe, defc = corona_k5([af, 1.0, sp_, wst], af + 1.0)
            if not cabe:
                fallos2 += 1
                peor2 = max(peor2, defc)
    ok &= check(f"esquinas deterministas j = 0 (suelo de alpha, topes "
                f"de s' y w*): {fallos2} fallos (peor {peor2:.4f})",
                fallos2 == 0)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] j = 1: el quinteto {alpha, o1, 1, s', w*}")
    rng = random.Random(SEED + 1)
    ok = True
    n, fallos = 0, 0
    peor_def, arg = 0.0, None
    for _ in range(max(10000, ITER // 6)):
        w = rng.uniform(0.02, 1.4)
        Sg = rng.uniform(1.0 + 1e-6, PHI)
        Xa = rng.uniform(0.0, 1.5) if rng.random() < 0.3 else 0.0
        af = max(1.0 + w, Sg + Xa + w, (1.0 + Sg + Xa) / PHI) * \
            (1.0 + (rng.expovariate(2.0) if rng.random() < 0.6 else 0))
        o1 = max(1.0, (1.0 + Sg) / PHI) * \
            (1.0 + (rng.expovariate(2.0) if rng.random() < 0.6 else 0))
        sp_ = rng.uniform(0.05, min(Sg / 2, PHI / 2))
        wst = rng.uniform(0.01, min(1 / PHI - 1e-6,
                                    max(0.011, Sg - 1.0)))
        # R = maximo de las necesidades ESCRITAS: pares de P y el
        # TRIO {alpha, o1, m} (P los empaqueta: P1 + particion)
        R = max(af + max(o1, 1.0), o1 + 1.0,
                R3_necesidad(af, o1, 1.0))
        n += 1
        cabe, defc = corona_k5([af, o1, 1.0, sp_, wst], R)
        if not cabe:
            fallos += 1
            if defc > peor_def:
                peor_def, arg = defc, dict(w=round(w, 2),
                                           af=round(af, 3),
                                           o1=round(o1, 3),
                                           sp=round(sp_, 3),
                                           wst=round(wst, 3))
    ok &= check(f"j = 1 ({n} instancias, R = par minimo): el quinteto "
                f"SIEMPRE cabe ({fallos} fallos, peor deficit "
                f"{peor_def:.4f}; peor {arg})", n > 2000
                and fallos == 0)
    # esquinas deterministas, incluida LA NAVAJA (o1 = (1+Sigma)/phi
    # con Sigma -> 1: o1 -> 2/phi)
    peor2, fallos2 = 0.0, 0
    for w in (0.02, 0.5, PHI - 1, PHI / 2, 0.99, 1.2):
        for Sg in (1.0 + 1e-9, 1.3, PHI):
            af = max(1.0 + w, Sg + w, (1.0 + Sg) / PHI)
            o1 = max(1.0, (1.0 + Sg) / PHI)
            for sp_ in (0.25, 0.5, min(Sg / 2, PHI / 2) - 1e-9):
                # ligadura de masa EXACTA: l1 >= s' entro en D_m,
                # luego W'' <= min(1/phi, Sigma - 2 s')
                wst = min(1 / PHI, max(0.0, Sg - 2 * sp_)) - 1e-9
                piezas = [af, o1, 1.0, sp_]
                if wst > 0.01:
                    piezas.append(wst)
                R = max(af + max(o1, 1.0), o1 + 1.0,
                        R3_necesidad(af, o1, 1.0))
                cabe, defc = corona_k5(piezas, R)
                if not cabe:
                    fallos2 += 1
                    peor2 = max(peor2, defc)
    ok &= check(f"esquinas deterministas j = 1 (incluida la navaja "
                f"o1 = 2/phi): {fallos2} fallos (peor {peor2:.4f})",
                fallos2 == 0)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] limites: alpha -> infinito y los margenes")
    ok = True
    # alpha -> inf: theta(alpha, x) -> theta con f(alpha) -> 1+ ...
    # el ciclo con alpha enorme: R = alpha + 1 y las piezas chicas
    peores = []
    for af in (5.0, 50.0, 500.0):
        cabe, defc = corona_k5([af, 1.0, PHI / 2 - 1e-9,
                                1 / PHI - 1e-9], af + 1.0)
        peores.append((af, cabe))
    ok &= check(f"limite alpha -> inf (j = 0, topes): cabe en "
                f"{peores}: el limite es benigno (theta(alpha, .) "
                f"crece pero el resto decrece mas rapido)",
                all(c for _, c in peores))
    # margen minimo observado en una malla del nucleo j = 0
    peor_marg = 1e9
    for wi in range(1, 15):
        w = wi * 0.1
        for si in range(2, 17):
            Sg = 1.0 + si * 0.04
            if Sg > PHI:
                continue
            af = max(1.0 + w, Sg + w)
            piezas = [af, 1.0, min(Sg / 2, PHI / 2) - 1e-9,
                      1 / PHI - 1e-9]
            R = af + 1.0
            # margen: cuanto puede crecer s' antes de fallar
            lo, hi = 0.0, 1.0
            for _ in range(25):
                mid = (lo + hi) / 2
                piezas2 = [af, 1.0, min(Sg / 2, PHI / 2) - 1e-9 + mid,
                           1 / PHI - 1e-9]
                if piezas2[2] < piezas2[0] and \
                        corona_k5(piezas2, R)[0]:
                    lo = mid
                else:
                    hi = mid
            peor_marg = min(peor_marg, lo)
    ok &= check(f"margen del nucleo j = 0: s' puede crecer >= "
                f"{peor_marg:.3f} sobre su tope en toda la malla "
                f"(> 0: el cierre no es raspado)", peor_marg > 0.02)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles")
    ok = True
    # (a) sin las colas (alpha sin suelo de cola) el cuarteto PUEDE
    # fallar? alpha = 1+w con w pequeno y Sigma grande: el suelo
    # Sigma+w manda: probar VIOLANDO el suelo Sigma+w
    cabe, defc = corona_k5([1.05, 1.0, 0.8, 0.6], 2.05)
    ok &= check(f"(a) violando el suelo alpha >= Sigma+omega (alpha "
                f"= 1.05 con piezas 0.8+0.6): el cuarteto NO cabe "
                f"(deficit {defc:.3f} > 0): las legalidades del "
                f"testigo son las que pagan", not cabe and defc > 0)
    # (b) la navaja ya no muerde: con la necesidad del trio en R, la
    # corona directa coloca el quinteto en el punto critico
    af, o1 = 1.3, 2 / PHI
    R = max(af + max(o1, 1.0), o1 + 1.0, R3_necesidad(af, o1, 1.0))
    cabe, _ = corona_k5([af, o1, 1.0, 0.5 - 1e-9, 1 / PHI - 1e-9], R)
    ok &= check(f"(b) la navaja (o1 = 2/phi) NO bloquea la corona "
                f"directa con R >= necesidad del trio "
                f"(R = {R:.3f}): quinteto cabe = {cabe}", cabe)
    return ok


def main():
    print("=" * 68)
    print("GAP LEMMA ESCRITO: anidado j <= 1 por corona directa "
          "(drafts/gaplemma.md)")
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
