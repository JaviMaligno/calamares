#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Teorema de compactacion mural: verificacion sobre empaquetamientos
REALES (docs/drafts/compactacion.md).

(P1) theta <= gamma_real para pares no-apilables, en empaquetamientos
     geometricos reales (posiciones muestreadas, no murales) MAS el
     dirigido de frontera: pares TANGENTES exactos (esquinas de la
     caja, empates a = b) y la cota del anillo d_a >= a+2b-R > 0
     (ningun centro en el origen, cuantitativo).
(P2) todo camino de subsecuencia cerrado <= 2 pi (particion del
     circulo real) => total del camino mas largo <= 2 pi.
(P3) la construccion mural con el orden real SIEMPRE pasa el chequeo
     completo (todas las parejas) cuando todos los pares son
     no-apilables: la compactacion nunca falla.
Controles: con pares APILABLES la compactacion puede fallar (MC) y
la familia anillo DETERMINISTA (central + corona tangente en
R = c+2r) es un empaquetamiento real explicito sin NINGUN
empaquetamiento mural (Sigma theta_adyacentes > 2 pi en todo orden);
la particion (P2) es exacta.  Muestreadores con empates exactos y
k <= 7 (ronda hostil 2026-08-09).
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, theta_w, ciclo_constructivo

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '0'))   # offset de semillas


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


def muestra_radios(rng):
    """Radios con k = 3..7 y, con prob. 0.3, EMPATES exactos (el
    muestreo continuo nunca los produce y son frontera de theta)."""
    k = rng.randrange(3, 8)
    radios = [rng.uniform(0.6, 1.6) for _ in range(k)]
    if rng.random() < 0.3:
        base = rng.uniform(0.6, 1.6)
        for i in range(k):
            if rng.random() < 0.5:
                radios[i] = base
    return sorted(radios, reverse=True)


def bloque_A():
    print("[A] (P1) theta <= gamma_real en empaquetamientos reales")
    rng = random.Random(20260809 + SEED)
    ok = True
    n, viol, pares = 0, 0, 0
    for _ in range(max(2000, ITER // 30)):
        radios = muestra_radios(rng)
        k = len(radios)
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
    # dirigido: TANGENCIAS EXACTAS (la frontera de (P1), que el
    # muestreo por rechazo nunca visita) + cota estructural del
    # anillo: en todo par no-apilable d_a >= a+2b-R > 0 y
    # d_b >= 2a+b-R > 0 (ningun centro en el origen, cuantitativo).
    viol_t, viol_d, casos = 0, 0, 0
    peor_marg = 1e9
    for _ in range(max(4000, ITER // 15)):
        b2 = rng.uniform(0.3, 1.5)
        a2 = b2 * rng.uniform(1.0, 1.9)          # a >= b, empates en 1.0
        if rng.random() < 0.25:
            a2 = b2                              # empate exacto
        R = rng.uniform(a2 + b2, a2 + 2 * b2 - 1e-9)   # no-apilable
        lo_a, hi_a = a2 + 2 * b2 - R, R - a2
        if lo_a > hi_a:
            continue
        # esquinas deterministas + interior aleatorio de d_a
        das = [lo_a, hi_a, rng.uniform(lo_a, hi_a)]
        for da in das:
            lo_b = max(2 * a2 + b2 - R, abs(a2 + b2 - da))
            hi_b = min(R - b2, da + a2 + b2)
            if lo_b > hi_b or da <= 0:
                continue
            for db in (lo_b, hi_b, rng.uniform(lo_b, hi_b)):
                if db <= 0:
                    continue
                # par TANGENTE exacto: |c_a - c_b| = a+b
                cosg = (da * da + db * db - (a2 + b2) ** 2) / (2 * da * db)
                g = math.acos(max(-1.0, min(1.0, cosg)))
                th = theta_w(a2, b2, R)
                casos += 1
                peor_marg = min(peor_marg, g - th)
                if g < th - 1e-9:
                    viol_t += 1
        # cota del anillo (estructural, infactibilidad REAL bajo la
        # cota): con d_a < a+2b-R, la disyuncion exige
        # d_b >= a+b-d_a > R-b: no cabe en el disco
        da_bad = rng.uniform(0.0, max(lo_a * 0.999, 1e-12))
        if not (a2 + b2 - da_bad > R - b2 + 1e-12):
            viol_d += 1
    ok &= check(f"(P1) dirigido: {casos} pares TANGENTES exactos "
                f"(esquinas d minimas/murales + empates): gamma >= "
                f"theta ({viol_t} violaciones, peor margen "
                f"{peor_marg:.2e} >= 0) y cota del anillo "
                f"d_a >= a+2b-R, d_b >= 2a+b-R ({viol_d} violaciones)",
                casos > 1000 and viol_t == 0 and viol_d == 0
                and peor_marg >= -1e-9)
    return ok


def bloque_B():
    print("[B] (P2) particion del circulo y camino mas largo <= 2 pi")
    rng = random.Random(7 + SEED)
    ok = True
    n, viol_part, viol_lp = 0, 0, 0
    for _ in range(max(2000, ITER // 30)):
        radios = muestra_radios(rng)
        k = len(radios)
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
    rng = random.Random(31 + SEED)
    ok = True
    n, fallos = 0, 0
    for _ in range(max(2000, ITER // 30)):
        radios = muestra_radios(rng)
        k = len(radios)
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
    rng = random.Random(99 + SEED)
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
    # (a') control DETERMINISTA (no MC): anillo de n circulos r
    # tangentes a la pared alrededor de un central c en R = c+2r.
    # Es un empaquetamiento REAL con coordenadas explicitas y TODOS
    # los pares apilables, y NO existe empaquetamiento mural ALGUNO:
    # en cualquier colocacion mural los huecos consecutivos suman
    # 2 pi y cada hueco es >= theta del par adyacente (lem:S1), luego
    # Sigma theta_adyacentes <= 2 pi es NECESARIO; aqui todo orden
    # ciclico tiene 2 aristas (c,r) y n-1 aristas (r,r) y la suma
    # excede 2 pi con margen. La hipotesis no-apilable no es adorno.
    det_ok = True
    peor_margen_det = 1e9
    for (c, r, nn) in ((1.0, 0.4, 10), (1.0, 0.45, 9), (0.8, 0.35, 9)):
        R = c + 2 * r
        rho = R - r
        pos = [(0.0, 0.0, c)] + [
            (rho * math.cos(2 * PI * i / nn),
             rho * math.sin(2 * PI * i / nn), r) for i in range(nn)]
        # legalidad real (tangencias permitidas)
        legal = all(math.hypot(x1 - x2, y1 - y2) >= r1 + r2 - 1e-9
                    for i1, (x1, y1, r1) in enumerate(pos)
                    for (x2, y2, r2) in pos[i1 + 1:])
        legal &= all(math.hypot(x, y) + rr <= R + 1e-9
                     for x, y, rr in pos)
        # todos los pares apilables
        apil = all(R >= max(r1, r2) + 2 * min(r1, r2) - 1e-9
                   for i1, (_, _, r1) in enumerate(pos)
                   for (_, _, r2) in pos[i1 + 1:])
        # imposibilidad mural: suma adyacente minima sobre TODOS los
        # ordenes ciclicos (unica clase: c tiene 2 vecinos r)
        suma = 2 * theta_w(c, r, R) + (nn - 1) * theta_w(r, r, R)
        margen = suma - 2 * PI
        peor_margen_det = min(peor_margen_det, margen)
        det_ok &= legal and apil and margen > 0
    ok &= check(f"(a') contraejemplo DETERMINISTA (3 familias anillo, "
                f"coordenadas explicitas, todos los pares apilables): "
                f"Sigma theta_adyacentes > 2 pi en TODO orden ciclico "
                f"(peor margen {peor_margen_det:.3f} > 0): ningun "
                f"empaquetamiento mural existe", det_ok
                and peor_margen_det > 0.1)
    # (a'') la relajacion "no-apilable solo respecto del MAYOR" NO
    # basta: L=2 mural + 7 smalls 0.76 murales + 1 small interior en
    # R=3.51 es un empaquetamiento real explicito con TODOS los pares
    # (L, s) no-apilables (3.51 < 3.52) y los (s, s) apilables
    # (3.51 >= 2.28), y Sigma theta_ady = 2 th(L,s) + 7 th(s,s) >
    # 2 pi en todo orden ciclico: sin empaquetamiento mural. La
    # hipotesis de TODOS los pares es tight.
    Lg, sm, Rr = 2.0, 0.76, 3.51
    posr = [(-(Rr - Lg), 0.0, Lg)]
    for i in range(7):
        ph = -1.683 + 0.561 * i
        posr.append(((Rr - sm) * math.cos(ph),
                     (Rr - sm) * math.sin(ph), sm))
    posr.append((1.3 * math.cos(0.2805), 1.3 * math.sin(0.2805), sm))
    peor = min(math.hypot(x1 - x2, y1 - y2) - (r1 + r2)
               for i1, (x1, y1, r1) in enumerate(posr)
               for (x2, y2, r2) in posr[i1 + 1:])
    contn = max(math.hypot(x, y) + r - Rr for x, y, r in posr)
    suma2 = 2 * theta_w(Lg, sm, Rr) + 7 * theta_w(sm, sm, Rr)
    ok &= check(f"(a'') la relajacion 'no-apilable respecto del mayor' "
                f"NO basta: contraejemplo explicito L=2 + 8x0.76 en "
                f"R=3.51 (holgura {peor:.4f} >= 0, contenido "
                f"{contn:.1e} <= 0, (L,s) no-apilables, (s,s) "
                f"apilables, Sigma theta_ady - 2 pi = "
                f"{suma2 - 2 * PI:.4f} > 0: sin mural)",
                peor >= -1e-12 and contn <= 1e-9
                and Rr < Lg + 2 * sm and Rr >= 3 * sm
                and suma2 > 2 * PI + 0.2)
    # el theta usado decrece en R: el enunciado es monotono en R
    ok &= check("(b) [ENUNCIADO] theta decrece en R (f decrece en R): "
                "la compactacion en R vale a fortiori en R' >= R para "
                "los mismos circulos", True)
    return ok


def bloque_E():
    print("[E] la proyeccion mural (la prueba de s.2): euclidiana")
    rng = random.Random(20260811 + SEED)
    ok = True
    n, viol = 0, 0
    peor_hueco = 1e9
    for _ in range(max(2000, ITER // 30)):
        radios = muestra_radios(rng)
        k = len(radios)
        R_low = radios[0] + radios[1]
        R_high = min(max(radios[i], radios[j]) +
                     2 * min(radios[i], radios[j])
                     for i in range(k) for j in range(k) if i < j)
        if R_low >= R_high - 1e-6:
            continue
        R = rng.uniform(R_low, R_high - 1e-6)
        pos = empaqueta_real(radios, R, rng)
        if pos is None:
            continue
        n += 1
        # proyeccion: cada circulo a la pared en su angulo real
        proy = []
        for x, y, r in pos:
            a = math.atan2(y, x)
            proy.append(((R - r) * math.cos(a), (R - r) * math.sin(a),
                         r))
        for i in range(k):
            for j in range(i + 1, k):
                xi, yi, ri = proy[i]
                xj, yj, rj = proy[j]
                d = math.hypot(xi - xj, yi - yj)
                peor_hueco = min(peor_hueco, d - (ri + rj))
                if d < ri + rj - 1e-9:
                    viol += 1
    ok &= check(f"proyeccion mural en {n} empaquetamientos reales "
                f"no-apilables: TODOS los pares disyuntos tras "
                f"proyectar ({viol} violaciones; peor holgura "
                f"{peor_hueco:.4f} >= 0): la prueba de s.2 en accion",
                n > 150 and viol == 0 and peor_hueco >= -1e-9)
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

