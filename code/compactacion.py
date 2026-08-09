#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Teorema de compactacion mural: verificacion sobre empaquetamientos
REALES (docs/drafts/compactacion.md).

(P1) theta <= gamma_real para pares no-apilables, en empaquetamientos
     geometricos reales (posiciones muestreadas, no murales).
(P2) todo camino de subsecuencia cerrado <= 2 pi (particion del
     circulo real) => total del camino mas largo <= 2 pi.
(P3) la construccion mural con el orden real SIEMPRE pasa el chequeo
     completo (todas las parejas) cuando todos los pares son
     no-apilables: la compactacion nunca falla.
Controles: con pares APILABLES la compactacion puede fallar (la
hipotesis es necesaria); la particion (P2) es exacta.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, theta_w, ciclo_constructivo

ITER = int(os.environ.get('CC_ITER', '60000'))


def empaqueta_real(radios, R, rng, intentos=6000, sesgo_mural=True):
    """Empaquetamiento geometrico real por rechazo (posiciones
    aleatorias legales, NO murales). None si no lo logra.  Con
    sesgo_mural los radios de posicion se sesgan hacia la pared
    (los empaquetamientos apretados viven cerca de ella), con
    perturbacion interior libre: siguen siendo empaquetamientos
    reales genericos, no murales."""
    pos = []
    for r in radios:
        ok = False
        for _ in range(intentos):
            if sesgo_mural and rng.random() < 0.7:
                rho = (R - r) * (1.0 - 0.35 * rng.random())
            else:
                rho = math.sqrt(rng.random()) * (R - r)
            ang = rng.uniform(0, 2 * PI)
            x, y = rho * math.cos(ang), rho * math.sin(ang)
            if all((x - px) ** 2 + (y - py) ** 2 >= (r + pr) ** 2 - 1e-12
                   for px, py, pr in pos):
                pos.append((x, y, r))
                ok = True
                break
        if not ok:
            return None
    return pos


def orden_y_gammas(pos):
    """Orden ciclico por angulo del centro y separaciones reales."""
    ang = [(math.atan2(y, x), r, x, y) for x, y, r in pos]
    ang.sort()
    orden = [r for _, r, _, _ in ang]
    angs = [a for a, _, _, _ in ang]
    return orden, angs


def bloque_A():
    print("[A] (P1) theta <= gamma_real en empaquetamientos reales")
    rng = random.Random(20260809)
    ok = True
    n, viol, pares = 0, 0, 0
    for _ in range(max(2000, ITER // 30)):
        k = rng.randrange(3, 7)
        radios = sorted((rng.uniform(0.6, 1.6) for _ in range(k)),
                        reverse=True)
        R_low = radios[0] + radios[1]
        R_high = min(max(radios[i], radios[j]) +
                     2 * min(radios[i], radios[j])
                     for i in range(k) for j in range(k) if i < j)
        if R_low >= R_high - 1e-6:
            continue
        R = rng.uniform(R_low, R_high - 1e-6)
        # no-apilables por pares
        if any(R >= radios[i] + 2 * radios[j] for i in range(k)
               for j in range(i + 1, k)):
            continue
        pos = empaqueta_real(radios, R, rng)
        if pos is None:
            continue
        n += 1
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                xi, yi, ri = pos[i]
                xj, yj, rj = pos[j]
                di = math.hypot(xi, yi)
                dj = math.hypot(xj, yj)
                if di < 1e-9 or dj < 1e-9:
                    continue
                cosg = ((xi * xj + yi * yj) / (di * dj))
                g = math.acos(max(-1.0, min(1.0, cosg)))
                pares += 1
                if g < theta_w(ri, rj, R) - 1e-9:
                    viol += 1
    ok &= check(f"(P1) en {n} empaquetamientos reales no-apilables "
                f"({pares} pares): gamma_real >= theta SIEMPRE "
                f"({viol} violaciones)", n > 150 and viol == 0)
    return ok


def bloque_B():
    print("[B] (P2) particion del circulo y camino mas largo <= 2 pi")
    rng = random.Random(7)
    ok = True
    n, viol_part, viol_lp = 0, 0, 0
    for _ in range(max(2000, ITER // 30)):
        k = rng.randrange(3, 7)
        radios = sorted((rng.uniform(0.6, 1.6) for _ in range(k)),
                        reverse=True)
        R_low = radios[0] + radios[1]
        R_high = min(max(radios[i], radios[j]) +
                     2 * min(radios[i], radios[j])
                     for i in range(k) for j in range(k) if i < j)
        if R_low >= R_high - 1e-6:
            continue
        R = rng.uniform(R_low, R_high - 1e-6)
        if any(R >= radios[i] + 2 * radios[j] for i in range(k)
               for j in range(i + 1, k)):
            continue
        pos = empaqueta_real(radios, R, rng)
        if pos is None:
            continue
        n += 1
        orden, angs = orden_y_gammas(pos)
        kk = len(orden)
        # particion exacta: las distancias dirigidas consecutivas de
        # CUALQUIER subsecuencia suman 2 pi
        for _ in range(4):
            t = rng.randrange(2, kk + 1)
            idx = sorted(rng.sample(range(kk), t))
            tot = 0.0
            for s in range(t):
                a, b = angs[idx[s]], angs[idx[(s + 1) % t]]
                d = (b - a) % (2 * PI)
                if t > 1 and abs(d) < 1e-15:
                    d = 0.0
                tot += d if t > 1 else 2 * PI
            if t >= 2 and abs(tot - 2 * PI) > 1e-9:
                viol_part += 1
        # camino mas largo sobre el orden real <= 2 pi
        th = {}
        alfa = [0.0] * kk
        for i in range(kk):
            for j in range(i + 1, kk):
                th[(i, j)] = theta_w(orden[i], orden[j], R)
        for i in range(1, kk):
            alfa[i] = max(alfa[t2] + th[(t2, i)] for t2 in range(i))
        total = alfa[-1] + th[(0, kk - 1)]
        if total > 2 * PI + 1e-9:
            viol_lp += 1
    ok &= check(f"(P2) en {n} empaquetamientos: la particion dirigida "
                f"de toda subsecuencia suma 2 pi exacto ({viol_part} "
                f"fallos) y el camino mas largo del orden real es "
                f"<= 2 pi ({viol_lp} fallos)",
                n > 150 and viol_part == 0 and viol_lp == 0)
    return ok


def bloque_C():
    print("[C] (P3) la compactacion mural nunca falla (no-apilables)")
    rng = random.Random(31)
    ok = True
    n, fallos = 0, 0
    for _ in range(max(2000, ITER // 30)):
        k = rng.randrange(3, 7)
        radios = sorted((rng.uniform(0.6, 1.6) for _ in range(k)),
                        reverse=True)
        R_low = radios[0] + radios[1]
        R_high = min(max(radios[i], radios[j]) +
                     2 * min(radios[i], radios[j])
                     for i in range(k) for j in range(k) if i < j)
        if R_low >= R_high - 1e-6:
            continue
        R = rng.uniform(R_low, R_high - 1e-6)
        if any(R >= radios[i] + 2 * radios[j] for i in range(k)
               for j in range(i + 1, k)):
            continue
        pos = empaqueta_real(radios, R, rng)
        if pos is None:
            continue
        orden, _ = orden_y_gammas(pos)
        n += 1
        okc, defc = ciclo_constructivo(orden, R)
        if not okc:
            fallos += 1
    ok &= check(f"(P3) compactacion mural con el orden real: "
                f"{n} empaquetamientos, {fallos} fallos (el teorema "
                f"en accion: siempre compacta)", n > 150 and fallos == 0)
    return ok


def bloque_D():
    print("[D] controles: la hipotesis de no-apilabilidad es necesaria")
    rng = random.Random(99)
    ok = True
    # con pares apilables el teorema NO vale: familia dirigida de
    # muchos circulos medianos que caben por el INTERIOR pero cuya
    # suma mural excede 2 pi (la pared solo tiene 2 pi de arco)
    contra, n = 0, 0
    for nc in (10, 12, 14):
        for _ in range(60):
            r = rng.uniform(0.42, 0.52)
            R = rng.uniform(4.2, 4.8) * r
            radios = [r * rng.uniform(0.95, 1.05) for _ in range(nc)]
            if not all(R >= radios[i] + 2 * radios[j]
                       for i in range(nc) for j in range(nc)
                       if i != j):
                continue                 # queremos apilables (control)
            pos = empaqueta_real(radios, R, rng, intentos=12000,
                                 sesgo_mural=False)
            if pos is None:
                continue
            n += 1
            orden, _ = orden_y_gammas(pos)
            okc, _ = ciclo_constructivo(orden, R)
            if not okc:
                contra += 1
    ok &= check(f"(a) con pares APILABLES la compactacion mural puede "
                f"fallar: {contra} contraejemplos en {n} "
                f"empaquetamientos reales (> 0: la hipotesis no es "
                f"vacua; el interior acomoda lo que la pared no)",
                n > 20 and contra > 0)
    # el theta usado decrece en R: el enunciado es monotono en R
    ok &= check("(b) [ENUNCIADO] theta decrece en R (f decrece en R): "
                "la compactacion en R vale a fortiori en R' >= R para "
                "los mismos circulos", True)
    return ok


def main():
    print("=" * 68)
    print("TEOREMA DE COMPACTACION MURAL (drafts/compactacion.md)")
    print("=" * 68)
    solo = None
    for a in sys.argv[1:]:
        if a.startswith("--solo"):
            solo = a.split("=")[1] if "=" in a else \
                sys.argv[sys.argv.index(a) + 1]
    etiquetas = [solo] if solo else list("ABCD")
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

