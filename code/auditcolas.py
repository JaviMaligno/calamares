#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auditoria de colas globales (docs/drafts/auditcolas.md): la
leccion de la vacuidad (espvals: la cola GLOBAL de m incluye TODAS
las piezas menores — las X entre ellas, por el convenio polvo < m)
aplicada a los reclamos de EXISTENCIA de la campana.

CRITERIO (el que ordena la auditoria):
  - Barridos de SUFICIENCIA (el testigo cabe en todos los puntos
    muestreados / certificados por cajas): omitir paredes AGRANDA
    el dominio — superconjunto, SOUND.  No requieren reparacion.
  - Reclamos de EXISTENCIA (residuos declarados, hallazgos,
    instancias de gap, variedades): requieren la legalidad ENTERA
    del adversario, y la unica cota inevitable con polvo de
    granularidad libre es cola(m) GLOBAL:
      Sigma_S + X_m + X_Y + X_alpha + X_z + ... <= phi
    (todo el polvo es < m y cuenta; las colas de piezas intermedias
    dependen de la granularidad y el adversario las optimiza).

OBJETIVO PRINCIPAL: las instancias de gap del F3 REAL (f3cierre
bloque E / puertocii F5) — el residuo 1.0116 que quedo en pie.
El generador imponia las colas de Y y alfa pero NO cola(m) global
con las X: ¿sobreviven instancias de gap con la cola entera?

Bloques: [A] el criterio y la tabla de clasificacion; [B] el F3
real re-escaneado con cola(m) global; [C] espxy/espvals (ya
auditado: vacuidad, cita); [D] clasificacion del resto de
generadores de la campana; [E] estatus e impactos.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, corona_suf, R_lb_pack

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260818'))


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] el criterio de la auditoria (v2, reparado)")
    import sympy as sp
    ok = True
    ok &= check("[ENUNCIADO] CRITERIO v2 (acta): suficiencia sobre "
                "superconjunto = SOUND; existencia/residuo = exige "
                "legalidad ENTERA.  Colas inevitables "
                "(granularidad-independientes): las de TODA pieza "
                ">= m — su cola cuenta las tracked menores MAS la "
                "masa total del polvo (todo < m).  Bajo m: el "
                "PIGEONHOLE de masa (una masa agregada X < 1 es "
                "polvo forzoso: cada pieza <= la masa total < 1) y "
                "el CONFINAMIENTO (X_m vive en el agujero de m, "
                "piezas <= 1-omega) cierran los escapes de "
                "granularidad; una masa X >= 1 puede ser un anillo "
                "unico >= m y sale de cola(m) (banda declarada)",
                True)
    # el lema del trio prohibido: la aritmetica que decide
    phi = (1 + sp.sqrt(5)) / 2
    ok &= check("LEMA DEL TRIO PROHIBIDO (exacto, trivial y "
                "letal): tres piezas a >= b >= c con b, c >= "
                "(phi/2) a violan rho <= phi — cola(a) >= b + c >= "
                "2 (phi/2) a = phi a, y la desigualdad es estricta "
                "con cualquier masa menor extra (m, S, polvo).  "
                "2 (phi/2) = phi EXACTO: el umbral de "
                "comparabilidad es OTRA VEZ phi/2 — el gap de "
                "dualidad F3 exige >= 3 tops casi iguales (ratio "
                "0.9 > phi/2 = 0.809) y rho <= phi los prohibe",
                sp.simplify(2 * (phi / 2) - phi) == 0)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] el F3 real con cola(m) global")
    from puertocii import b_star, OMEGA_STAR
    ok = True
    rng = random.Random(20260814)      # la semilla del acta de
                                       # f3cierre (reproduce sus 3
                                       # instancias de gap)
    n_tot, gap_total, gap_legal = 0, 0, 0
    peor_exceso = 0.0
    ejemplos = []
    intentos = 0
    while intentos < 1400000 and gap_total < 30:
        intentos += 1
        wef = rng.uniform(OMEGA_STAR + 1e-4, 1.45)
        Xa = rng.uniform(0.0, 1.5) if rng.random() < 0.4 else 0.0
        XY = rng.uniform(0.0, 1.0) if rng.random() < 0.2 else 0.0
        Xm = rng.uniform(0.0, 0.5) if rng.random() < 0.3 else 0.0
        w = wef - Xa + PHI * (2 * XY + Xm)
        if w <= 0.02 or Xm > max(0.0, 1 - w):
            continue
        pesado = rng.random() < 0.35
        g = (3 - PHI - (PHI - 1) * wef) / PHI
        lo_s2, hi_s2 = max(g, 0.05), min(PHI * wef - 1, 0.999)
        if pesado:
            lo_s2, hi_s2 = max(0.05, 1 - w - Xm + 1e-4), 0.999
        if lo_s2 >= hi_s2:
            continue
        s2 = rng.uniform(lo_s2, hi_s2)
        s1 = rng.uniform(s2, 0.999)
        if pesado:
            S_lo, S_hi = 1 + s2, PHI - Xm
        else:
            S_lo = max(1.0, s1 + s2)
            S_hi = min(1 + s2, PHI - 2 + PHI * s2 + (PHI - 1) * wef)
        if S_hi <= S_lo:
            continue
        S = rng.uniform(S_lo, S_hi)
        W = S - s1 - s2
        if W < 0 or W > 1.0:
            continue
        lbY = max(1 + XY + w, (1 + S + Xm + XY) / PHI)
        ubY = S + XY + w
        if lbY >= ubY:
            continue
        Y = rng.uniform(lbY, ubY)
        lb_a = max(S + Xa + w, 1 + w,
                   (1 + S + Xm + Xa + XY + Y) / PHI)
        ub_a = 1 + (s2 if not pesado else S - b_star([s1, s2, W])) \
            + Xa + w
        if lb_a >= ub_a:
            continue
        alfa = rng.uniform(lb_a, ub_a)
        if Y >= alfa:
            continue
        d = rng.randrange(0, 3)
        T = Y + d * (w + 0.05)
        top = [alfa, T]
        for _ in range(rng.randrange(0, 3)):
            top.append(rng.uniform(0.3, alfa))
        n_tot += 1
        tops = sorted(top, reverse=True)
        R = R_lb_pack(tops, tops[0] + tops[1], confinado_por=tops[0])
        carga = top + ([s1, s2] if pesado else [s2])
        if corona_suf(carga, R)[0]:
            continue
        gap_total += 1
        # LEGALIDAD ENTERA (v2, acta): todas las colas <= phi.
        # Piezas tracked: tops + m + s's; polvo: X_m, X_Y y Xa < 1
        # (pigeonhole); Xa >= 1 = anillo unico (banda del acta:
        # fuera de cola(m), dentro de las colas de piezas mayores)
        smalls = [s1, s2] if pesado else [s2]
        polvo = Xm + XY + (Xa if Xa < 1.0 else 0.0)
        anillos = sorted(tops + [1.0] + smalls
                         + ([Xa] if Xa >= 1.0 else []), reverse=True)
        peor_rho = 0.0
        for i, p in enumerate(anillos):
            colap = sum(anillos[i + 1:]) + polvo
            peor_rho = max(peor_rho, colap / p)
        if peor_rho <= PHI + 1e-12:
            gap_legal += 1
            ejemplos.append(tuple(round(t, 2) for t in tops))
        else:
            peor_exceso = max(peor_exceso, peor_rho - PHI)
    ok &= check(f"F3 REAL con LEGALIDAD ENTERA ({n_tot} "
                f"instancias, {gap_total} con gap viejo, semilla "
                f"del acta de f3cierre): sobreviven "
                f"{gap_legal}/{gap_total} — el re-escaneo del "
                f"referee a 30 gaps dio 0/30 con peor cola de top "
                f"2.89-3.60 vs phi; el mecanismo es el lema del "
                f"trio prohibido ([A]): el gap exige >= 3 tops de "
                f"ratio 0.9 > phi/2 y cola(top mayor) >= 1.8 > "
                f"phi.  EL RESIDUO F3 REAL ES CANDIDATO FUERTE A "
                f"VACUIDAD (0 testigos legales conocidos; peor "
                f"exceso {peor_exceso:.2f})", gap_total >= 3
                and gap_legal == 0)
    ok &= check("[ENUNCIADO] consecuencia y deuda: f3cierre "
                "par. 3-4 ('el residuo 1.0116 PERMANECE') y el "
                "pasaje del paper se apoyaban en instancias "
                "rho-ilegales — errata registrada; el supremo "
                "sintetico 1.0816 de f3cierre queda como enunciado "
                "ABSTRACTO del arc-LP (su esquina 4x0.9+2x0.55 "
                "tambien viola el trio prohibido como instancia).  "
                "El CIERRE de la vacuidad (gap de dualidad => >= 3 "
                "tops comparables => ilegal, formalizado) merece "
                "su ciclo propio — declarado, no hecho aqui", True)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] espxy/espvals: ya auditado")
    ok = True
    ok &= check("[ENUNCIADO] la variedad del bolsillo diametral "
                "fue el CASO INDICE de esta auditoria (espvals v2, "
                "acta 2026-08-10): cola(m) global la vacio "
                "(300/300 fantasma, min 1.96 > phi) y el residuo "
                "ESP X_Y > 0 se cerro por vacuidad + sub-bolsillo "
                "universal.  Errata registrada en VEREDICTOS",
                True)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] clasificacion de los generadores de la campana")
    ok = True
    ok &= check("[ENUNCIADO] SUFICIENCIA sobre superconjunto "
                "(SOUND, sin reparacion): los B&B de r2bcert "
                "(DR/ESP), r2bmulti (G-b', ESP X>0), areduccion "
                "(pesadas), bolsillos (j<=1, ramas k<=2), "
                "optimizacion (sup <= 5.25), los barridos G de "
                "puertocii (G-b/b'/c/e/f/g: 0 fallos del testigo "
                "sobre dominios que INCLUYEN el legal), el fuzzing "
                "de actas (validacion de podas).  Los certificados "
                "solo se FORTALECEN si el dominio real es menor",
                True)
    ok &= check("[ENUNCIADO] EXISTENCIA/RESIDUO (auditables): (1) "
                "F3 real — auditado en [B]; (2) variedad espxy — "
                "caso indice, vacia; (3) residuo R2 de puertocii "
                "(581 instancias MC con omega en [0.989, 1.35] y "
                "malla B1b pesada, PRE-cierre por repack/[G]: hoy "
                "son celdas CERRADAS por otros medios — la "
                "auditoria no les debe nada); (4) el nucleo de "
                "espvals v1 — muerto con su variedad; (5) las "
                "'esquinas representativas' de los drafts "
                "(instancias ilustrativas, no reclamos).  No "
                "quedan reclamos de existencia sin auditar con "
                "colas globales", True)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus e impactos")
    ok = True
    ok &= check("[ENUNCIADO] IMPACTOS: la leccion de colas "
                "globales queda institucionalizada — todo "
                "generador de legalidad de adversario FUTURO debe "
                "imponer cola(m) global (y documentar que las "
                "colas intermedias dependen de la granularidad "
                "del polvo); los reclamos de existencia pasados "
                "quedan auditados ([B]-[D]); las dos actas "
                "afectadas (espxy, espvals v1) ya llevan su "
                "errata.  El criterio suficiencia-vs-existencia "
                "entra en los criterios de rigor de la RONDA "
                "FINAL CIEGA", True)
    return ok


def main():
    print("=" * 68)
    print("AUDITORIA DE COLAS GLOBALES (drafts/auditcolas.md)")
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
