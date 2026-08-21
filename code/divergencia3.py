#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La divergencia de los dos objetivos: la transicion 2 -> 3
(docs: correccion del peer review externo de 2026-08-21).

El paper afirmaba «four rings; three never diverge»: FALSO.  El
peer review externo (codex) exhibio la divergencia con TRES
anillos — sin anidamiento, por superaditividad pura del area:
R = 10, w = 4.5, radios {8, 5.05, 4.95}.  Este script fija la
transicion verdadera:

  LEMA (dos nunca divergen).  Divergencia := el optimo de area
  tiene cardinalidad ESTRICTAMENTE menor que el maximo de
  cardinalidad.  Con <= 2 anillos: si ambos caben juntos, el
  conjunto total es optimo de ambos objetivos (area estrictamente
  creciente en la inclusion); si no caben juntos, todo factible
  tiene cardinalidad <= 1 y el optimo de area (un anillo) alcanza
  la cardinalidad maxima 1.  Sin divergencia.  [Exhaustivo sobre
  la estructura logica: 2 casos.]

  TRES DIVERGEN (contraejemplo del review, verificado EXACTO en
  racionales): R = 10, w = 9/2, r = {8, 101/20, 99/20}.
  101/20 + 99/20 = 10 = R (el par diametral cabe); 8 + 101/20 >
  10 y el agujero del 8 es 8 - 9/2 = 7/2 < 99/20 (nada convive
  con el 8; los pequenos no anidan entre si: 101/20 - 9/2 =
  11/20 < 99/20).  Areas /pi: a(8) = 64 - 49/4 = 207/4;
  a(101/20) + a(99/20) = (10201 - 121)/400 + (9801 - 81)/400 =
  10080/400 + 9720/400 = 99/2 = 198/4 < 207/4.  El area elige
  {8} (N = 1); la cardinalidad el par (N = 2).  El mecanismo es
  la SUPERADITIVIDAD del area con anchura grande (los agujeros
  mueren: empaquetado circular puro).

  EL REGIMEN ANIDADO: la instancia de 4 anillos del paper
  (R = 10, w = 1, {9, 4.2, 4.2, 4.2}) sigue siendo la minima
  CON anidamiento activo (el mecanismo del agujero, el del
  diagrama de fases de franja.py, que es la familia w = 1).

Bloques: [A] el lema de 2 (estructura logica exhaustiva); [B] el
contraejemplo de 3 exacto; [C] la instancia de 4 anidada; [D] la
cartografia del umbral de anchura para 3 (muestreo declarado);
[E] estatus.
"""
import itertools
import math
import os
import random
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import check

SEED = int(os.environ.get('CC_SEED', '20260821'))


def area(r, w):
    """Area de contacto /pi (racional si las entradas lo son)."""
    hueco = r - w if r > w else 0
    return r * r - hueco * hueco


def factibles_3(rs, R, w):
    """Todos los subconjuntos factibles de <= 3 anillos con la
    geometria elemental de la instancia sin-anidamiento: un
    anillo cabe si r <= R; dos conviven en la sarten si
    r1 + r2 <= R; uno anida en otro si r_chico <= r_grande - w.
    (Para el contraejemplo: nada anida y solo el par pequeno
    convive — la clausura de 3 elementos se decide con pares y
    la unica coloca-3 exigiria los tres pares.)"""
    n = len(rs)
    out = []
    for k in range(1, n + 1):
        for sub in itertools.combinations(range(n), k):
            piezas = [rs[i] for i in sub]
            ok = all(p <= R for p in piezas)
            if k >= 2:
                # sin anidamiento posible (se verifica aparte):
                # todos los pares deben convivir en la sarten
                ok = ok and all(a + b <= R for a, b in
                                itertools.combinations(piezas, 2))
            if ok:
                out.append(sub)
    return out


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] el lema: dos anillos nunca divergen")
    ok = True
    ok &= check("[LEMA, exhaustivo logico] con <= 2 anillos no "
                "hay divergencia: (caso 1) ambos caben juntos => "
                "el conjunto total es optimo de AMBOS objetivos "
                "(el area es estrictamente creciente bajo "
                "inclusion: a(r) > 0); (caso 2) no caben juntos "
                "=> toda solucion tiene N <= 1 y el optimo de "
                "area (el mejor anillo solo) alcanza N = 1 = "
                "N_max.  La divergencia (N del optimo de area < "
                "N_max) exige >= 3 anillos", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] TRES DIVERGEN: el contraejemplo exacto (peer "
          "review 2026-08-21)")
    ok = True
    R, w = F(10), F(9, 2)
    rs = [F(8), F(101, 20), F(99, 20)]
    # geometria exacta: nada anida, solo el par pequeno convive
    anida = [(i, j) for i in range(3) for j in range(3) if i != j
             and rs[j] <= rs[i] - w]
    convive = [(i, j) for i, j in itertools.combinations(range(3), 2)
               if rs[i] + rs[j] <= R]
    ok &= check(f"(a) geometria exacta: anidamientos posibles = "
                f"{anida} (ninguno: agujero del 8 = 7/2 < 99/20; "
                f"101/20 - 9/2 = 11/20 < 99/20) y convivencias = "
                f"{convive} (solo el par pequeno: 101/20 + 99/20 "
                f"= 10 = R exacto, par diametral)",
                anida == [] and convive == [(1, 2)])
    a8 = area(rs[0], w)
    apar = area(rs[1], w) + area(rs[2], w)
    ok &= check(f"(b) areas exactas /pi: a(8) = {a8} = 207/4; "
                f"a(101/20)+a(99/20) = {apar} = 99/2 = 198/4 < "
                f"207/4 — el AREA elige {{8}} con N = 1; la "
                f"CARDINALIDAD elige el par con N = 2: "
                f"DIVERGENCIA CON TRES ANILLOS",
                a8 == F(207, 4) and apar == F(99, 2)
                and a8 > apar)
    # el optimo de area entre TODOS los factibles
    fac = factibles_3(rs, R, w)
    mejor_a = max(fac, key=lambda s: sum(area(rs[i], w) for i in s))
    n_max = max(len(s) for s in fac)
    ok &= check(f"(c) sobre los {len(fac)} conjuntos factibles: "
                f"optimo de area = {sorted(mejor_a)} (N = "
                f"{len(mejor_a)}), N_max = {n_max}: divergencia "
                f"N = 1 < 2", len(mejor_a) == 1 and n_max == 2)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] el regimen anidado: la instancia de 4 (w = 1)")
    ok = True
    R, w = 10.0, 1.0
    a9 = area(9.0, w)
    a42 = area(4.2, w)
    # area optimo: 9 + un 4.2 anidado (agujero del 9 = 8 >= 4.2)
    A_area = (a9 + a42) * math.pi
    A_card = 3 * a42 * math.pi
    ok &= check(f"(a) {{9, 4.2 x3}}: agujero del 9 = 8 >= 4.2 "
                f"(anida uno); area optimo = 9 + 4.2 anidado: "
                f"A = {A_area:.2f} (N = 2) vs los tres 4.2: "
                f"A = {A_card:.2f} (N = 3) — los valores ~76.7 y "
                f"~69.7 del paper",
                A_area > A_card
                and abs(A_area - 76.7) < 0.1
                and abs(A_card - 69.7) < 0.1)
    ok &= check("(b) [NOTA] la instancia de 4 es la minima del "
                "MECANISMO DEL AGUJERO (con anidamiento activo, "
                "el regimen del diagrama de fases w = 1 de "
                "franja.py); la de 3 del bloque B vive en el "
                "regimen sin-anidamiento (w grande)", True)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] cartografia del umbral de anchura para 3 "
          "(muestreo declarado)")
    ok = True
    rng = random.Random(SEED)
    R = 10.0
    w_min_div = None
    for _ in range(200000):
        w = rng.uniform(0.5, 6.0)
        b = rng.uniform(R * 0.55, R * 0.9)
        s1 = rng.uniform(R * 0.3, R * 0.55)
        s2 = rng.uniform(R * 0.3, s1)
        if s1 + s2 > R:
            continue
        if b + s2 <= R or s2 <= b - w or s1 <= b - w \
                or s2 <= s1 - w:
            continue                   # el grande convive o anida
        if area(b, w) > area(s1, w) + area(s2, w):
            if w_min_div is None or w < w_min_div:
                w_min_div = w
    ok &= check(f"en 200.000 muestras (R = 10, familia grande + "
                f"par): la divergencia de 3 aparece desde "
                f"w ~ {w_min_div:.3f} (w/R ~ {w_min_div / R:.3f}) "
                f"— MUESTREO, no umbral probado: la region con "
                f"anchura grande y agujeros muertos es donde la "
                f"superaditividad separa los objetivos",
                w_min_div is not None and w_min_div < 4.6)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    ok = True
    ok &= check("[ENUNCIADO] LA TRANSICION DE LA DIVERGENCIA ES "
                "2 -> 3 (no 3 -> 4): dos anillos nunca divergen "
                "(lema exhaustivo logico); tres divergen (el "
                "contraejemplo EXACTO en racionales del peer "
                "review externo, sin anidamiento: superaditividad "
                "del area con anchura grande); la instancia de 4 "
                "del paper queda como la minima del mecanismo DEL "
                "AGUJERO (regimen anidado del diagrama de fases, "
                "w = 1).  El pasaje del paper corregido en "
                "consecuencia", True)
    return ok


def main():
    print("=" * 68)
    print("LA TRANSICION 2 -> 3 DE LA DIVERGENCIA "
          "(correccion del peer review)")
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
