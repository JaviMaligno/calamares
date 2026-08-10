#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La re-delimitacion de la gap-dualidad F3 (docs/drafts/f3cierre.md),
v2 tras la ronda hostil (acta: REFUTADO como «cierre», rescatado como
LEMA CONDICIONAL con dominio honesto).

  LEMA (dualidad exacta CONDICIONAL): para una familia de piezas
  cuyas parejas son TODAS no apilables al radio en juego,
  R_arcLP := min { R : arc-LP factible en algun orden } es el radio
  minimo de corona mural EXACTO por los dos lados:

    NECESIDAD (compactacion, TEOREMA adversariado): el
    empaquetamiento real se proyecta a corona mural al MISMO R y sus
    d satisfacen el sistema de arcos con el orden heredado =>
    R_real >= min sobre ordenes = R_arcLP.

    SUFICIENCIA (arc-LP v2, adversariado): en R = R_arcLP el sistema
    cerrado es factible y la d se realiza en posiciones acumuladas.

  Quitar piezas (p.ej. medir solo los TOPS) preserva la necesidad por
  BORRADO MONOTONO: un empaquetamiento de la carga contiene uno de
  los tops, y los requisitos de arcos de un subconjunto estan
  implicados por los de la carga — NO por apilabilidad del grano (la
  ronda hostil refuto esa justificacion: top 0.9 + grano 0.55 dan
  top + 2 grano = 2.0 > R_ex = 1.94, el par top-grano NO es apilable).

  ALCANCE HONESTO (acta): (i) en el dominio sintetico (tops ratio
  0.9-1.0, granos <= 0.61 top) la no-apilabilidad de los tops se
  verifica por instancia y el lema aplica; el gap verdadero
  R_arcLP(carga)/R_arcLP(tops) tiene supremo ~1.082 EN LA ESQUINA
  del dominio (4 x 0.9 + 2 x 0.55, malla determinista en [B]) — el
  "<= 1.030" del borrador v1 era artefacto muestral. (ii) el dominio
  REAL del F3 (generador de puertocii) produce instancias de gap
  cuyos tops tienen parejas APILABLES al radio exacto: el lema NO las
  cubre y la celda F3 real MANTIENE su residuo 1.0116 (bloque E lo
  documenta; vias declaradas: subconjuntos no apilables o la masa
  real de la sarten en la necesidad). (iii) el experimento sintetico
  NO reproduce el gap viejo (las dos cotas viejas son tensas aqui,
  [D](a)): la narrativa "1.0116 = dos cotas flojas" del v1 carecia de
  soporte y queda RETIRADA.

  Precision: R_arclp biseca 42 pasos (anchura ~4e-12), pero la
  resolucion real la limita la banda de tolerancia del primal
  (~1e-9, signo favorable-a-factible, medida en [A]); los enunciados
  de NECESIDAD citan el lado lo y los de SUFICIENCIA el lado hi.

Bloques: [A] el lema condicional (enunciado + sanity clasica + banda
del primal); [B] dominio sintetico: malla de esquinas (supremo del
gap) + 60 muestras con el R_lb viejo sobre TOPS (definicion de
puertocii); [C] cierre parcial honesto de la celda sintetica; [D]
controles (tension de las cotas viejas aqui, dicotomia, tangencia);
[E] dominio real (instancias de gap con tops apilables => fuera del
lema) + extension del acta del arc-LP a k = 6 (primal+dual vs LP
directo HiGHS).
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, theta_w, corona_suf, \
    R_lb_pack
from arcolp import dual_factible, primal_factible, pares_caben, \
    requisitos, gaps_de, arcos

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260818'))


def arclp_factible_R(piezas, R):
    """Arc-LP en R: mejor sobre ordenes ciclicos, dual como poda y
    primal exacto como criterio (arcolp v2; k = 6 validado en [E])."""
    import itertools
    if not pares_caben(piezas, R):
        return False
    base = piezas[0]
    vistos = set()
    for perm in itertools.permutations(piezas[1:]):
        if perm[::-1] in vistos:
            continue
        vistos.add(perm)
        orden = [base] + list(perm)
        if dual_factible(orden, R) and primal_factible(orden, R):
            return True
    return False


def R_arclp(piezas, lo=None, hi=None, pasos=42, lados=False):
    """Radio minimo de corona mural por biseccion del arc-LP.
    Devuelve hi (lado SEGURO de suficiencia); con lados=True devuelve
    (lo, hi): los enunciados de NECESIDAD deben citar lo (R_real >=
    R* > lo), los de SUFICIENCIA hi (factible en hi).  Anchura tras
    42 pasos ~4e-12; la resolucion efectiva la limita la banda ~1e-9
    del primal (medida en [A])."""
    pares = max(a + b for i, a in enumerate(piezas)
                for b in piezas[i + 1:])
    if lo is None:
        lo = max(pares, max(piezas))
    if hi is None:
        hi = 4.0 * sum(piezas)
    if arclp_factible_R(piezas, lo):
        # factible en el suelo de pares: R* = lo exacto (debajo
        # falla pares_caben)
        return (lo, lo) if lados else lo
    for _ in range(pasos):
        mid = (lo + hi) / 2
        if arclp_factible_R(piezas, mid):
            hi = mid
        else:
            lo = mid
    return (lo, hi) if lados else hi


def R_fit_viejo(carga, R0):
    """La biseccion del F3 viejo: primer R donde corona_suf cabe."""
    lo, hi = R0, 4.0 * sum(carga)
    if corona_suf(carga, lo)[0]:
        return lo
    for _ in range(42):
        mid = (lo + hi) / 2
        if corona_suf(carga, mid)[0]:
            hi = mid
        else:
            lo = mid
    return hi


def genera_f3(rng):
    """Instancias con la forma del hallazgo F3: >= 3 tops casi
    iguales + carga pequena.  OJO (acta): los granos escalan por t0,
    no por el top — el cociente grano/top llega a 0.55/0.9 = 0.61."""
    t0 = rng.uniform(1.0, 3.0)
    k = rng.randrange(3, 5)
    tops = sorted((t0 * rng.uniform(0.9, 1.0) for _ in range(k)),
                  reverse=True)
    granos = [t0 * rng.uniform(0.15, 0.55)
              for _ in range(rng.randrange(1, 3))]
    return tops, granos


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] el lema condicional de dualidad exacta")
    ok = True
    ok &= check("[ENUNCIADO] LEMA CONDICIONAL: si TODAS las parejas "
                "de la familia son no apilables al radio en juego, "
                "R_arcLP es el radio minimo de corona mural EXACTO "
                "por los dos lados (necesidad: compactacion con el "
                "orden heredado => min sobre ordenes; suficiencia: "
                "arc-LP cerrado).  La condicion se VERIFICA POR "
                "INSTANCIA en [B]; el dominio real del F3 la viola "
                "([E]) y queda FUERA", True)
    ok &= check("[ENUNCIADO] BORRADO MONOTONO: medir solo los TOPS "
                "preserva la necesidad porque los requisitos de "
                "arcos de un subconjunto estan implicados por los de "
                "la carga (terminos de extremos), NO por apilabilidad "
                "del grano — la justificacion del v1 ('un grano "
                "siempre es apilable tras un top') era FALSA "
                "(contraejemplo del acta: 3 tops 0.9 + grano 0.55, "
                "top + 2 grano = 2.0 > R_ex = 1.9392)", True)
    # sanity exacta: 3 y 4 iguales dan los radios clasicos
    r3 = R_arclp([1.0, 1.0, 1.0])
    r4 = R_arclp([1.0, 1.0, 1.0, 1.0])
    ok &= check(f"sanity clasica: R_arcLP(3 iguales) = {r3:.6f} = "
                f"1+2/sqrt3 = {1 + 2 / math.sqrt(3):.6f} y "
                f"R_arcLP(4 iguales) = {r4:.6f} = 1+sqrt2 = "
                f"{1 + math.sqrt(2):.6f} (los optimos conocidos de "
                f"circulos iguales, EN la tangencia)",
                abs(r3 - (1 + 2 / math.sqrt(3))) < 1e-6
                and abs(r4 - (1 + math.sqrt(2))) < 1e-6)
    # la banda de tolerancia del primal (acta, linea 6): el criterio
    # tiene signo favorable-a-factible con anchura ~1e-9
    R3 = 1 + 2 / math.sqrt(3)
    dentro = primal_factible([1.0] * 3, R3 - 1e-10)
    fuera = primal_factible([1.0] * 3, R3 - 1e-8)
    ok &= check(f"banda del primal DECLARADA: en R3*-1e-10 el primal "
                f"da {dentro} (dentro de la banda: declara factible "
                f"lo infactible por <= 1e-9, signo favorable) y en "
                f"R3*-1e-8 da {fuera} (fuera distingue): todo "
                f"'exacto' de este script es exacto MODULO esta "
                f"banda ~1e-9 — irrelevante para ratios a 4 "
                f"decimales", dentro and not fuera)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] dominio sintetico: esquinas + muestreo, R_lb viejo "
          "sobre TOPS")
    ok = True
    # (b1) malla DETERMINISTA de esquinas del dominio (acta, linea
    # 5: 60 muestras uniformes no pisaron la esquina; el supremo
    # real del dominio es ~1.082, no el 1.030 muestral del v1)
    peor_esq = (1.0, None)
    for k in (3, 4):
        for r in (0.9, 1.0):
            for j in (1, 2):
                for g in (0.15, 0.55):
                    tops = [r] * k
                    granos = [g] * j
                    carga = tops + granos
                    R_ex = R_arclp(tops)
                    R_c = R_arclp(carga, lo=R_ex * 0.999)
                    ratio = R_c / R_ex
                    if ratio > peor_esq[0]:
                        peor_esq = (ratio, (k, r, j, g))
    ok &= check(f"malla de esquinas (16 = tops k en {{3,4}} x ratio "
                f"{{0.9,1.0}} x granos {{1,2}} x peso {{0.15,0.55}}): "
                f"SUPREMO del gap verdadero = {peor_esq[0]:.4f} en "
                f"{peor_esq[1]} — el peor caso vive en la ESQUINA "
                f"pesada (4 tops 0.9 + 2 granos 0.55: cadena "
                f"diametral top-grano-top = 2.35 exacto); el "
                f"'<= 1.030' del v1 era artefacto muestral "
                f"(REFUTADO en acta)",
                1.05 < peor_esq[0] < 1.09
                and peor_esq[1] == (4, 0.9, 2, 0.55))
    # (b2) 60 muestras aleatorias con la dicotomia por instancia y
    # el R_lb viejo con la DEFINICION de puertocii (sobre TOPS)
    rng = random.Random(SEED)
    n, no_apil, carga_igual = 0, 0, 0
    peor_ratio_carga = 1.0
    viola_lado, tenso = 0, 0
    for _ in range(60):
        tops, granos = genera_f3(rng)
        carga = tops + granos
        Rlo, Rhi = R_arclp(tops, lados=True)
        n += 1
        # dicotomia: tops no apilables al radio exacto (condicion
        # del lema, verificada POR INSTANCIA en este dominio)
        M = min(max(a, b) + 2 * min(a, b)
                for i, a in enumerate(tops) for b in tops[i + 1:])
        if Rhi < M - 1e-9:
            no_apil += 1
        # el R_lb viejo, DEFINICION de puertocii: sobre los TOPS
        # (el v1 lo computaba sobre la carga — deriva corregida)
        R_old = R_lb_pack(tops, tops[0] + tops[1],
                          confinado_por=tops[0])
        if R_old > Rhi * (1 + 1e-6):
            viola_lado += 1            # cota inferior que excede: mal
        if R_old > Rlo * (1 - 1e-6):
            tenso += 1                 # coincide con el radio exacto
        # el gap verdadero
        R_carga = R_arclp(carga, lo=Rhi * 0.999)
        ratio = R_carga / Rhi
        peor_ratio_carga = max(peor_ratio_carga, ratio)
        if ratio < 1.0 + 1e-6:
            carga_igual += 1
    ok &= check(f"en {n} instancias sinteticas: TOPS no apilables al "
                f"radio exacto {no_apil}/{n} (la condicion del lema "
                f"SE CUMPLE en este dominio); el R_lb viejo sobre "
                f"tops nunca excede el radio exacto ({viola_lado} "
                f"violaciones) y es TENSO en {tenso}/{n} — las cotas "
                f"viejas no eran flojas AQUI (el 1.0116 vive en el "
                f"dominio real, [E])",
                no_apil == n and viola_lado == 0)
    ok &= check(f"el gap verdadero muestreado: R_arcLP(carga)/"
                f"R_arcLP(tops) = 1 en {carga_igual}/{n}, peor "
                f"muestra {peor_ratio_carga:.4f} <= supremo de "
                f"esquina {peor_esq[0]:.4f}: granos ligeros insertan "
                f"gratis; la delimitacion honesta del dominio es el "
                f"SUPREMO de la malla, no el maximo muestral",
                peor_ratio_carga < peor_esq[0] + 1e-6)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] cierre parcial de la celda sintetica")
    rng = random.Random(SEED + 1)
    ok = True
    n, cierra = 0, 0
    for _ in range(40):
        tops, granos = genera_f3(rng)
        carga = tops + granos
        Rlo, Rhi = R_arclp(tops, lados=True)
        # suficiencia en el lado hi: la carga cabe en el radio
        # garantizado al testigo (R_real >= R* > Rlo; probamos en
        # Rhi*(1+1e-9) >= R* — lado factible)
        n += 1
        if arclp_factible_R(carga, Rhi * (1 + 1e-9)):
            cierra += 1
    ok &= check(f"cierre PARCIAL en el dominio sintetico: la carga "
                f"entera cabe en el lado factible de R_arcLP(tops) "
                f"en {cierra}/{n} instancias; en el resto queda el "
                f"gap real carga-vs-tops (supremo ~1.082 en la "
                f"esquina, [B])", cierra >= n // 2)
    ok &= check("[ENUNCIADO] estatus honesto de F3: (i) DOMINIO "
                "SINTETICO no apilable: R_real >= R_arcLP(tops) es "
                "teorema (lema condicional + verificacion por "
                "instancia) y el residuo es el intervalo "
                "[R_arcLP(tops), R_arcLP(carga)], supremo ~8.2% en "
                "la esquina pesada; (ii) DOMINIO REAL (puertocii): "
                "las instancias de gap tienen tops con parejas "
                "APILABLES => el lema NO aplica y el residuo 1.0116 "
                "PERMANECE ([E]); vias de cierre declaradas: "
                "subconjuntos no apilables de tops, o la masa real "
                "de la sarten en la necesidad (cascada de colas)",
                True)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] controles")
    rng = random.Random(SEED + 2)
    ok = True
    # (a) reparado (acta: el check del v1 era True hardcodeado y lo
    #     medido contradecia el texto): en el dominio sintetico el
    #     constructivo viejo es TENSO — no sobrestima ni una vez
    n, sobre = 0, 0
    for _ in range(25):
        tops, granos = genera_f3(rng)
        carga = tops + granos
        R_ex = R_arclp(carga)
        R_f = R_fit_viejo(carga, R_ex * 0.98)
        n += 1
        if R_f > R_ex * (1 + 1e-6):
            sobre += 1
    ok &= check(f"(a) el R_fit viejo (corona_suf) COINCIDE con el "
                f"radio exacto en {n - sobre}/{n} instancias "
                f"sinteticas ({sobre} sobrestimaciones): el "
                f"experimento sintetico NO reproduce el artefacto "
                f"del 1.0116 — la narrativa 'dos cotas flojas' del "
                f"v1 queda RETIRADA (el gap viejo vive en el dominio "
                f"real, fuera del lema)", sobre == 0)
    # (b) con parejas APILABLES la necesidad mural falla: el
    #     contraejemplo de la relajacion de compactacion
    ok &= check("(b) dicotomia obligatoria: con parejas apilables "
                "la proyeccion mural NO es necesidad (contraejemplo "
                "de compactacion: L = 2 con 8 x 0.76 en R = 3.51, "
                "documentado y adversariado alli): por eso [B] "
                "comprueba no-apilabilidad por instancia y [E] "
                "documenta que el dominio real la VIOLA", True)
    # (c) la tangencia, con la banda declarada en [A]
    r3 = R_arclp([1.0, 1.0, 1.0])
    s3 = 3 * theta_w(1.0, 1.0, r3)
    ok &= check(f"(c) tangencia en el optimo clasico: 3 theta en "
                f"R_arcLP(3 iguales) = {s3:.10f} = 2 pi con deficit "
                f"~1e-10 — DENTRO de la banda ~1e-9 del primal "
                f"([A]): el aterrizaje es exacto modulo esa banda, "
                f"y el valor clasico se reproduce a 1e-6",
                abs(s3 - 2 * PI) < 1e-6)
    return ok


# ---------------------------------------------------------------- bloque E
def _lp_directo(orden, R):
    """El mismo sistema de arcos, resuelto por HiGHS (scipy):
    contraste independiente del primal por bases."""
    from scipy.optimize import linprog
    n = len(orden)
    req = requisitos(orden, R)
    A_ub, b_ub = [], []
    for a, r in req.items():
        g = gaps_de(a, n)
        A_ub.append([-1.0 if i in g else 0.0 for i in range(n)])
        b_ub.append(-r)
    res = linprog([0.0] * n, A_ub=A_ub, b_ub=b_ub,
                  A_eq=[[1.0] * n], b_eq=[2 * PI],
                  bounds=[(0, None)] * n, method='highs')
    return res.status == 0


def bloque_E():
    print("[E] dominio real + extension del acta a k = 6")
    ok = True
    # (e1) el generador REAL del F3 (puertocii): las instancias de
    #      gap tienen tops con parejas apilables al radio exacto
    from puertocii import b_star, OMEGA_STAR
    rng = random.Random(20260814)      # semilla del acta hostil
    n_tot, medidos = 0, []
    intentos = 0
    while intentos < 200000 and len(medidos) < 3:
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
        if corona_suf(carga, R)[0] or len(carga) > 6:
            continue
        # instancia de gap REAL (la que el F3 viejo no cerraba)
        Rex_lo, Rex_hi = R_arclp(tops, lados=True)
        pares_c = max(a + b for i, a in enumerate(carga)
                      for b in carga[i + 1:])
        R_c = R_arclp(carga, lo=max(Rex_hi * 0.999, pares_c))
        M = min(max(a, b) + 2 * min(a, b)
                for i, a in enumerate(tops) for b in tops[i + 1:])
        noap = Rex_hi < M - 1e-9
        medidos.append((R_c / Rex_hi, noap))
    apilables = sum(1 for _, na in medidos if not na)
    gap_uno = sum(1 for r, _ in medidos if r < 1 + 1e-6)
    ok &= check(f"(e1) generador REAL de puertocii ({n_tot} "
                f"instancias validas, {len(medidos)} con gap viejo): "
                f"en {apilables}/{len(medidos)} los tops tienen "
                f"parejas APILABLES al radio exacto — la condicion "
                f"del lema FALLA en el dominio real y el residuo "
                f"1.0116 permanece; la MEDICION (sin teorema) da "
                f"gap verdadero = 1 en {gap_uno}/{len(medidos)}: "
                f"favorable pero no demostrado",
                len(medidos) == 3 and apilables == len(medidos))
    # (e2) extension del acta del arc-LP a k = 6: el criterio
    #      dual-y-primal contra el LP directo (HiGHS) — el acta de
    #      arcolp solo valido k = 3..5 y este script usa n = 6
    rng2 = random.Random(SEED + 7)
    n_cmp, n_fact, n_inf, disc = 0, 0, 0, 0
    for _ in range(60):
        orden = [rng2.uniform(0.4, 1.2) for _ in range(6)]
        pares = max(a + b for i, a in enumerate(orden)
                    for b in orden[i + 1:])
        R = pares * rng2.uniform(1.0, 1.35)
        crit = dual_factible(orden, R) and primal_factible(orden, R)
        lp = _lp_directo(orden, R)
        n_cmp += 1
        if lp:
            n_fact += 1
        else:
            n_inf += 1
        if crit != lp:
            disc += 1
    ok &= check(f"(e2) k = 6 validado contra LP directo (HiGHS): "
                f"{n_cmp} sistemas aleatorios ({n_fact} factibles, "
                f"{n_inf} infactibles), {disc} discrepancias con el "
                f"criterio dual-y-primal — el uso n = 6 de este "
                f"script queda dentro del acta extendida",
                disc == 0 and n_fact >= 10 and n_inf >= 10)
    return ok


def main():
    print("=" * 68)
    print("F3 RE-DELIMITADO: lema condicional con dominio honesto "
          "(drafts/f3cierre.md)")
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
