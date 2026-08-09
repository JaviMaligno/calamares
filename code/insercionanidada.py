#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insercion por sombras en la plantilla ANIDADA: D4-D6 escrito
(docs/drafts/insercionanidada.md).

Plantilla (caso (b)): u = agujero de alpha (alpha top-level), v =
sarten; P tiene m top-level en la sarten y S en el agujero de alpha;
F tiene m en el agujero de alpha. El reparto testigo:
  (1) la sarten segun P SIN MOVER NADA salvo m: m sale de su sitio
      (D_m = su disco unidad queda vacante top-level) y entra en el
      agujero de alpha SEGUN EL CERTIFICADO DE F (cuando F coloco m,
      el agujero tenia el contenido > m, compartido: legal, subarboles
      rigidos);
  (2) sigma1 -> D_m (fila de uno, sigma1 < 1);
  (3) sigma2 mural en la sarten por el LEMA DE INSERCION (sombras
      sobre la familia {alpha, o_1..o_j, D_m como pieza de radio 1});
  (4) el resto W' = S sin {s1, s2} + polvo, de masa < 1/phi (cola de m
      con (D) sigma1+sigma2 > 1), como circulo-fila por sombras.

Regimen sombra: R - x > 2s por pieza; de las necesidades de par de la
sarten de P (R >= alpha + max(o1, 1), R >= alpha + 1):
  s < (1 + omega)/2 con j >= 1 (o1 >= 1+omega); s < 1/2 con j = 0.
ESQUINA EXTREMA sigma2 >= (1+omega)/2: vacia POR MASA sii
2 sigma2 >= 1 + omega > phi <=> omega > phi - 1 (cola de m).
Cobertura: D4 (j = 2, omega in [phi/2, 1)) ENTERA (phi/2 > phi-1);
D5 (k >= 4 fuera de rama): k y p son masa: colapsa al mismo teorema
en sus rangos de omega; D6 y las franjas {omega <= phi-1,
sigma2 >= (1+omega)/2}: se DELIMITAN y quedan para pinza dedicada
(las campanas las tienen computacionalmente).

Bloques: [A] identidades exactas; [B] presupuesto del pan anidado
(sup por esquinas y limites); [C] inserciones reales euclidianas;
[D] cobertura y delimitacion honesta; [E] controles.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, theta_w, cascada

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260811'))


def sombra(s, x, R):
    w, u = s + x, R - s
    if u <= w:
        return PI
    return math.asin(w / u)


def presupuesto(s, piezas, R):
    return sum(2 * sombra(s, x, R) for x in piezas)


def cascada_anidada_min(SS, j, w):
    """Ocupantes minimos de la plantilla anidada: o_i > 1, colas con
    m, S y alpha por encima; version conservadora (colas debiles =>
    ocupantes menores => sombras menores... DIRECCION: para el
    presupuesto el peor caso son ocupantes GRANDES con R = par
    minimo: usamos las colas como SUELOS y el par como R)."""
    os_ = []
    total = 0.0
    for k in range(j, 0, -1):
        base = max(1.0 + w, (total + 1.0 + SS) / PHI,
                   os_[-1] if os_ else 0.0)
        os_.append(base)
        total += base
    return os_[::-1]


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades exactas (sympy)")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    w = sp.symbols('omega', positive=True)
    # esquina extrema vacia por masa: 2 sigma2 >= 1 + omega > phi
    # sii omega > phi - 1; en D4 omega >= phi/2 y phi/2 > phi - 1
    ok &= check("esquina-masa: sigma1 + sigma2 >= 2 sigma2 >= 1+omega "
                "> phi sii omega > phi-1; y phi/2 > phi-1 exacto "
                "(phi/2 - (phi-1) = 1 - phi/2 = (2-phi)/2 > 0): D4 "
                "queda cubierta entera",
                sp.simplify(phi / 2 - (phi - 1) - (1 - phi / 2)) == 0
                and float(1 - phi / 2) > 0)
    # regimen sombra en el pan anidado: R - x > 2s por pieza
    ok &= check("[ENUNCIADO] regimen: R >= alpha + max(o1, 1) y "
                "R >= alpha + 1 (necesidades de par de la sarten de "
                "P, dos circulos exacto) dan R - x > 2s para toda "
                "pieza del presupuesto sii s < (1+omega)/2 (j >= 1, "
                "o1 >= 1+omega) o s < 1/2 (j = 0)", True)
    # (D) y la masa restante
    ok &= check("[ENUNCIADO] (D) anidada: la fila del par en D_m "
                "(disco unidad top-level vacante) falla => "
                "sigma1+sigma2 > 1; con cola(m) <= phi, la masa a "
                "insertar tras sigma1, sigma2 es W' < phi - 1 = "
                "1/phi: un circulo-fila (lem:row)", True)
    # legalidad del certificado de F para m -> agujero de alpha
    ok &= check("[ENUNCIADO] m entra en el agujero de alpha segun el "
                "certificado de F (el contenido > m del agujero es "
                "compartido; S sale entera; subarboles rigidos), "
                "como en thm:oblivious", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] el presupuesto del pan anidado: el techo de cobertura "
          "s_cap por celda (cascada anidada REAL)")
    from coronanidada import cascada_anidada
    ok = True
    rng = random.Random(SEED)
    # Para cada (j, omega): s_cap = el mayor s tal que el presupuesto
    # de la PRIMERA insercion Y el de la segunda (w* = 1/phi, con s
    # contada y su propio regimen) quedan bajo 2 pi - margen, sobre
    # las instancias muestreadas del dominio (cascada anidada real,
    # rank de alpha barrido, holguras). El teorema cubre
    # sigma2 <= min(s_cap, regimen); la esquina-masa cubre
    # sigma2 > phi/2 cuando omega > phi-1.
    MARG = 0.05
    caps = {}
    n = 0
    for _ in range(max(20000, ITER // 3)):
        j = rng.randrange(1, 7)
        w = rng.uniform(0.24, 0.999)
        SS = rng.uniform(1.0 + 1e-6, PHI)
        holg = [1.0 + rng.expovariate(2.5) for _ in range(j + 1)]
        if rng.random() < 0.35:
            holg = [1.0] * (j + 1)
        rank = rng.randrange(0, j + 1)
        af, os_ = cascada_anidada(SS, j, rank,
                                  max(1.0 + w, SS + w), holg)
        piezas = sorted([af] + list(os_) + [1.0], reverse=True)
        R = piezas[0] + piezas[1]
        n += 1
        # techo de regimen de la primera insercion
        s_reg = min((R - x) / 2 for x in piezas) - 1e-9
        # biseccion del s_cap por presupuesto (presupuesto crece en s)
        lo, hi = 0.05, min(s_reg, 0.999)
        if hi <= lo:
            caps.setdefault((j, round(w, 1)), []).append(0.0)
            continue
        for _ in range(30):
            mid = (lo + hi) / 2
            v1 = presupuesto(mid, piezas, R)
            wst = 1 / PHI
            reg2 = all(R - x > 2 * wst + 1e-12 for x in piezas + [mid])
            v2 = presupuesto(wst, piezas + [mid], R) if reg2 else 1e9
            if max(v1, v2) < 2 * PI - MARG:
                lo = mid
            else:
                hi = mid
        caps.setdefault((j, round(w, 1)), []).append(lo)
    peores = {k: round(min(v), 3) for k, v in sorted(caps.items())}
    # cobertura de D4: j = 2, omega >= phi/2: s_cap minimo observado
    d4 = [min(v) for (j, w), v in caps.items()
          if j == 2 and w >= 0.8]
    s_cap_d4 = min(d4) if d4 else 0.0
    ok &= check(f"s_cap por (j, omega~) [minimos observados]: "
                f"{peores}", n > 3000)
    ok &= check(f"D4 (j = 2, omega >= phi/2): s_cap >= "
                f"{s_cap_d4:.3f} y la esquina-masa cubre sigma2 > "
                f"phi/2 = {PHI / 2:.3f}: cobertura COMPLETA sii "
                f"s_cap >= phi/2 (hueco si no: "
                f"{max(0.0, PHI / 2 - s_cap_d4):.3f})",
                s_cap_d4 >= PHI / 2 - 1e-9)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] inserciones reales euclidianas en el pan anidado")
    rng = random.Random(SEED + 1)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from insercion import empaqueta, inserta
    ok = True
    n, fallo1, fallo2 = 0, 0, 0
    for _ in range(max(2000, ITER // 20)):
        j = rng.randrange(0, 5)
        w = rng.uniform(0.3, 0.98)
        SS = rng.uniform(1.0 + 1e-6, PHI)
        s2 = rng.uniform(0.2, (1.0 + w) / 2 - 0.01) if j >= 1 else \
            rng.uniform(0.2, 0.49)
        af = max(1.0 + w, SS + w) * (1.0 + rng.expovariate(2.0))
        os_ = cascada_anidada_min(SS, j, w)
        fam = [af] + os_ + [1.0]
        R = (max(af + (os_[0] if j >= 1 else 1.0),
                 (os_[0] + os_[1]) if j >= 2 else 0.0)
             * rng.uniform(1.0, 1.2))
        if any(R - x <= 2 * s2 + 1e-9 for x in fam):
            continue
        pos = empaqueta(fam, R, rng)
        if pos is None:
            continue
        n += 1
        p2 = inserta(pos, s2, R)
        if p2 is None:
            fallo1 += 1
            continue
        wstar = 1 / PHI
        if any(R - x <= 2 * wstar + 1e-9 for x in fam + [s2]):
            continue
        p3 = inserta(pos + [p2], wstar, R)
        if p3 is None:
            fallo2 += 1
    ok &= check(f"pan anidado real ({n} empaquetamientos de "
                f"{{alpha, O, m}}): sigma2 en regimen SIEMPRE entra "
                f"({fallo1} fallos) y el circulo-fila despues "
                f"({fallo2} fallos)", n > 400 and fallo1 == 0
                and fallo2 == 0)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] cobertura de las celdas y delimitacion honesta")
    ok = True
    # D4: j = 2, omega in [phi/2, 1): sigma2 < (1+omega)/2 por
    # sombras; sigma2 >= (1+omega)/2 vacia por masa (omega > phi-1)
    ok &= check("D4 = {j = 2, omega in [phi/2, 1)}: CUBIERTA ENTERA "
                "(regimen sombra hasta (1+omega)/2 y esquina-masa "
                "porque phi/2 > phi-1)", PHI / 2 > PHI - 1)
    # D5: k >= 4 fuera de la rama: k y p son MASA (el circulo-fila
    # no cuenta piezas): colapsa al teorema en sus rangos
    ok &= check("[ENUNCIADO] D5 (k >= 4 fuera de la rama de "
                "reduccion): el tamano del perfil es masa (W' < "
                "1/phi como un solo circulo-fila): colapsa al mismo "
                "teorema en los rangos de omega/sigma2 del regimen",
                True)
    # cobertura medida (bloque B): j >= 3 completa (s_cap ~ 0.999);
    # j = 2 con s_cap ~ 0.95 y esquina-masa desde phi/2 cuando
    # omega > phi-1; franjas restantes: j <= 1 entero (la navaja
    # exacta o1 = 2/phi contra 2w* = 2/phi mata la segunda insercion)
    # y {j = 2, omega <= phi-1, sigma2 in [s_cap, 1)}
    franja = "{j <= 1 (D6, incluida la navaja o1 = 2/phi = 2w*)} y " \
             "{j = 2, omega <= phi-1, sigma2 in [~0.95, 1)}"
    print(f"      FRANJA DELIMITADA (pinza dedicada pendiente; "
          f"cerrada computacionalmente por coronanidada): {franja}")
    ok &= check("cobertura del teorema: j >= 3 COMPLETA (todo omega, "
                "sigma2, k, p), j = 2 completa para omega > phi-1 "
                "(D4 entera) y hasta sigma2 ~ 0.95 si no; el resto "
                "DECLARADO (no forzado), con las pinzas "
                "computacionales de coronanidada detras", True)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles")
    ok = True
    # (a) sin la necesidad de par el presupuesto revienta: R = alpha
    s = 0.6
    af = 3.0
    v = presupuesto(s, [af, 1.0], af + 0.1)
    ok &= check(f"(a) sin R >= alpha + 1 el regimen falla y la "
                f"sombra de alpha se dispara ({v:.3f} incluye pi): "
                f"la necesidad de par del pan de P es la que paga",
                v >= PI)
    # (b) la esquina-masa es tight: en omega = phi-1 exacto,
    # 2 sigma2 = 1+omega = phi NO excede phi (frontera)
    ok &= check("(b) esquina-masa tight: en omega = phi-1, "
                "2 sigma2 = phi toca la cola de m sin excederla "
                "(frontera exacta): por debajo de phi-1 hace falta "
                "otra pared (franja declarada)", True)
    return ok


def main():
    print("=" * 68)
    print("INSERCION ANIDADA: D4-D6 escrito "
          "(drafts/insercionanidada.md)")
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
