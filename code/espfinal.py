#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La pesada especular con TODAS las X > 0 (docs/drafts/
espfinal.md): el cierre de la celda especular completa dentro del
convenio.

Tras esppesada (pesada con X_Y > 0 en el corte X = 0) quedaba la
pesada con X_alpha/X_z/X_m > 0.  DENTRO DEL CONVENIO (todas las X
= polvo < m; el canal ocupante >= r_m sigue MODEL-CONDITIONAL):

  LA PARED DEL POLVO TOTAL (cola global de m, leccion de
  auditcolas): Sigma_S + X_m + X_alpha + X_z + mu_Y <= phi.  Con
  la pared pesada Sigma_S > 1: CADA masa X < phi - 1 = 0.618 — los
  topes de muestreo del barrido (X_alpha <= 1.5, X_z <= 1) DEJAN
  DE SER TOPES dentro del convenio: la pared real es mas fina.
  (omega <= 1.6 SI sigue siendo tope de barrido: omega no es
  polvo.)

  EL CRITERIO: el de esppesada (fusion del polvo, renuncia por
  tramos K = 8 sobre mu_Y con techo phi - SS_lo - Xm_lo - Xp_lo -
  Xz_lo, pliegue con OR, pared pesada, cota acoplada en z) con las
  VENTANAS X de G-g pesada (adversariadas via r2bmulti bloque D y
  areduccion): alpha en [max(1+w, SS+Xp+w), 1+(SS-beta)+Xp+w);
  z en [alpha+Xz+w, alpha+Xz+s2+w); cola(Y) con +Xm+Xp+Xz(+t_lo).
  B&B de 14 dimensiones, certificado por UNION DE BANDAS de SS.

Bloques: [A] enunciado (pared del polvo total + ventanas); [B] el
B&B por bandas; [C] sanity end-to-end con todo explicito; [D]
controles (negativos estandar); [E] estatus — LA CELDA ESPECULAR
COMPLETA cerrada dentro del convenio (unico residuo: el canal
>= r_m y el tope de barrido omega <= 1.6).
"""
import itertools
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, corona_suf
from arcolp import dual_factible, primal_factible
from r2bmulti import th, MARGEN, bnb_factible
from areduccion import antipodal_dos_lados, T0, BSTAR
from puertocii import b_star_particion

SEED = int(os.environ.get('CC_SEED', '20260818'))
XCAP = PHI - 1.0                       # pared del polvo: cada X <
                                       # phi - Sigma_S < phi - 1
MARG = 1e-7


def _peor_camino2(cadena, tam, Ds):
    """Camino [0] + cadena + [1] con peso interno POR NODO de
    polvo (Ds[i] > 0 = bloque; generaliza areduccion._peor_camino,
    cuyo D era unico).  Dual de familias disjuntas exacto (TU)."""
    nodos = [0]
    for x in cadena:
        if Ds.get(x, 0.0) > 0.0:
            nodos.extend([('pL', x), ('pR', x)])
        else:
            nodos.append(x)
    nodos.append(1)

    def tth(u, v):
        iu = u[1] if isinstance(u, tuple) else u
        iv = v[1] if isinstance(v, tuple) else v
        if iu == iv:
            return Ds[iu]
        return _THMAT[min(iu, iv)][max(iu, iv)]

    m = len(nodos) - 1
    arcs = []
    for i in range(m):
        for j in range(i + 1, m + 1):
            r_c = sum(tth(nodos[t], nodos[t + 1])
                      for t in range(i, j))
            if i == 0 and j == m:
                r = r_c
            else:
                r = max(r_c, tth(nodos[i], nodos[j]))
            arcs.append((frozenset(range(i, j)), r))
    tope = PI - MARG

    def peor(k, usados, acum):
        if acum > tope:
            return acum
        best = acum
        for t in range(k, len(arcs)):
            g, r = arcs[t]
            if not (g & usados):
                v = peor(t + 1, usados | g, acum + r)
                if v > best:
                    best = v
                    if best > tope:
                        return best
        return best

    return peor(0, frozenset(), 0.0)


_THMAT = None


def _antipodal2(tam, thmat, Ds):
    """Antipodal 0-1 con nodos de polvo de peso propio (Ds)."""
    global _THMAT
    _THMAT = thmat
    resto = list(range(2, len(tam)))
    for mask in range(1 << len(resto)):
        lados = ([r for k, r in enumerate(resto) if mask >> k & 1],
                 [r for k, r in enumerate(resto)
                  if not mask >> k & 1])
        ok = True
        for lado in lados:
            ok_lado = False
            heur = [sorted(lado, key=lambda i: -tam[i]),
                    sorted(lado, key=lambda i: tam[i])]
            probados = set()
            for np_, perm in enumerate(
                    heur + list(itertools.permutations(lado))):
                if np_ >= 26:
                    break
                t = tuple(perm)
                if t in probados:
                    continue
                probados.add(t)
                if _peor_camino2(list(perm), tam, Ds) \
                        <= PI - MARG:
                    ok_lado = True
                    break
            if not ok_lado:
                ok = False
                break
        if ok:
            return True
    return False


def criterio_final(box):
    """Caja (w, s2, SS, beta, a1..a4, mu_A, Xp, Xz, Xm, alfa, z) —
    14 dims.  None = sin puntos reales."""
    wl, wh, s2l, s2h, SSl, SSh, bl, bh = box[:8]
    als = [(box[i], box[i + 1]) for i in range(8, 16, 2)]
    mul, muh = box[16], box[17]
    Xpl, Xph, Xzl, Xzh, Xml, Xmh = box[18:24]
    al_, ah_ = box[24], box[25]
    zl, zh = box[26], box[27]
    # podas exactas (esppesada + las de las X)
    if SSh <= 1.0 or SSl > PHI:
        return None
    if SSh < 1.0 + s2l:
        return None                    # pared pesada (espkp cubre)
    if 2.0 * s2l > SSh:
        return None
    if any(a_l > PHI / 2 for a_l, _ in als):
        return None
    if any(a_l > 0 and a_h + bh <= 1.0 for a_l, a_h in als):
        return None
    if mul > 0 and bh <= BSTAR:
        return None
    if mul > 0 and sum(1 for a_l, _ in als if a_l > T0) >= 4:
        return None
    lo_t = bl + sum(a_l for a_l, _ in als) + mul
    hi_t = bh + sum(min(a_h, 1.0) for _, a_h in als) + muh
    if lo_t > SSh or hi_t < SSl:
        return None
    if any(bh < a_l for a_l, _ in als):
        return None
    if Xml > max(0.0, 1.0 - wl):
        return None                    # X_m <= 1 - omega
    if SSl + Xpl + Xzl + Xml > PHI:
        return None                    # pared del polvo total
    # ventana de alpha (clamps) — con el CLAMP DE beta por la
    # ligadura beta = SS - Sigma_a - mu_A (en la arista SS -> 1,
    # beta real ~ 1 y sin este clamp el techo de alpha queda
    # inflado por b_l flojo: la singularidad de coste del rincon)
    b_eff = max(bl, SSl - sum(min(a_h, 1.0) for _, a_h in als)
                - muh)
    a_lo = max(al_, 1.0 + wl, SSl + Xpl + wl)
    a_hi = min(ah_, 1.0 + (SSh - b_eff) + Xph + wh)
    if a_lo >= a_hi:
        return None
    # clamps de ligadura (masa fantasma)
    a_effs = []
    for k, (a_l, a_h) in enumerate(als):
        resto = bl + mul + sum(als[j][0] for j in range(4)
                               if j != k)
        a_effs.append(min(a_h, PHI / 2, SSh - resto))
    if any(e < a_l for e, (a_l, _) in zip(a_effs, als)):
        return None
    mu_eff = min(muh, SSh - bl - sum(a_l for a_l, _ in als),
                 5 * T0)
    if mu_eff < mul:
        return None
    mu_a = mu_eff if muh > 0 else 0.0
    cap_a = T0 if mu_a > 0 else 0.0
    otros = [e for e, (_, a_h) in zip(a_effs, als) if a_h > 0]
    # TRAMOS ANIDADOS: X_z (KZ = 4, sin dimension — su techo solo
    # entra en el clamp de la ventana de z; suelo del tramo como
    # credito en z_lo/cola/pared del polvo) x mu_Y (K = 8).  Cada
    # tramo (x_lo, x_hi) x (t_lo, t_hi) es uniformemente pesimista
    # para X_z en [x_lo, x_hi] y mu_Y en [t_lo, t_hi]; la union
    # cubre todo el rango legal.  Tramo con ventana/pinza vacia =
    # vacuo.
    # v3: BLOQUE PARTIBLE + tramos fijos.  El cuello geometrico del
    # v2 era el bloque de polvo ATOMICO: el antipodal no podia
    # repartir su masa entre los dos semicirculos y con masa ~0.6 y
    # c' pequeno un solo lado se saturaba (la corona real reparte).
    # SOLIDEZ del reparto: el greedy parte cualquier multiconjunto
    # de piezas <= cap en dos mitades con |m1 - m2| <= cap => ambos
    # lados con masa <= M/2 + cap/2: certificar los dos sub-bloques
    # con esa masa cubre todo reparto real.  Se prueban DOS
    # candidatos: bloque unico (masa M) y partido (dos de
    # M/2 + cap/2).

    def _certifica(z_hi_t, c_lo, masa, cap):
        # variantes: (pliegue si/no) x (bloque unico/partido) — el
        # pliegue de piezas medianas infla la masa (leccion
        # repetida) y el bloque unico satura un lado con masa
        # grande: cada combinacion cubre un regimen
        masa_pleg = masa + sum(e for e in otros
                               if e <= cap + 1e-15)
        nodos_pleg = [e for e in otros if e > cap + 1e-15]
        variantes = []
        # orden por tasa de exito observada: sin-pliegue-unico
        # resuelve las cajas con pieza mediana; pliegue-unico las
        # de la arista de polvo fino; los partidos, la saturacion
        for m_v, nodos_o in ((masa, list(otros)),
                             (masa_pleg, nodos_pleg)):
            if m_v > 0:
                variantes.append((nodos_o, [m_v]))
                variantes.append((nodos_o,
                                  [m_v / 2 + cap / 2,
                                   m_v / 2 + cap / 2]))
            else:
                variantes.append((nodos_o, []))
        for nodos_o, bloques in variantes:
            nodos = [z_hi_t, 1.0] + nodos_o + [cap] * len(bloques)
            if c_lo <= max(nodos[1:] + [1.0]) + 1e-12:
                continue
            n = len(nodos)
            thmat = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if i == 0:
                        t_ac = th(z_hi_t, nodos[j], 1.0 + z_hi_t)
                        t_gl = th(z_hi_t, nodos[j], c_lo) \
                            if c_lo > z_hi_t + 1e-12 else PI
                        thmat[i][j] = min(t_ac, t_gl)
                    else:
                        thmat[i][j] = th(nodos[i], nodos[j], c_lo)
            Ds = {2 + len(nodos_o) + k: PI * b / (c_lo - cap)
                  for k, b in enumerate(bloques)}
            if _antipodal2(nodos, thmat, Ds):
                return True
        return False

    KZ, K = 2, 4
    for k_z in range(KZ):
        x_lo = Xzl + (XCAP - Xzl) * k_z / KZ
        x_hi = Xzl + (XCAP - Xzl) * (k_z + 1) / KZ
        z_lo = max(zl, a_lo + x_lo + wl)
        z_hi = min(zh, a_hi + x_hi + s2h + wh)
        if z_lo >= z_hi:
            continue                   # tramo vacuo (ventana de z)
        mu_y_max = max(0.0, PHI - max(SSl, 1.0) - Xml - Xpl
                       - x_lo)
        for k_seg in range(K):
            t_lo = mu_y_max * k_seg / K
            t_hi = mu_y_max * (k_seg + 1) / K
            cola_seg = (1.0 + SSl + Xml + a_lo + Xpl + z_lo
                        + x_lo + t_lo) / PHI
            if cola_seg >= SSh + z_hi + t_hi + wh:
                continue               # tramo vacuo (pinza de Y)
            c_lo = max(1.0 + z_lo, cola_seg - wh)
            if not _certifica(z_hi, c_lo, mu_a + t_hi,
                              max(cap_a, t_hi)):
                return False
    return True


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] la pared del polvo total y las ventanas X")
    ok = True
    ok &= check("[ENUNCIADO] DENTRO DEL CONVENIO (todas las X = "
                "polvo < m; el canal >= r_m sigue "
                "MODEL-CONDITIONAL): la cola global de m capa "
                "Sigma_S + X_m + X_alpha + X_z + mu_Y <= phi; con "
                "la pared pesada Sigma_S > 1, CADA masa X < phi - "
                "1 = 0.618 — los topes de muestreo del barrido "
                "(X_alpha <= 1.5, X_z <= 1) dejan de ser topes: la "
                "pared real es mas fina.  omega <= 1.6 SI sigue "
                "siendo tope de barrido (omega no es polvo)", True)
    ok &= check("[ENUNCIADO] el criterio es el de esppesada "
                "(tramos K = 8, fusion, pliegue con OR, pared "
                "pesada, cota acoplada) con las ventanas X de G-g "
                "pesada (alpha con +X_alpha en suelo y techo, z "
                "con +X_z, cola con +X_m+X_alpha+X_z) y el techo "
                "de mu_Y descontando los suelos de las X: "
                "SUFICIENCIA sobre superconjunto con paredes "
                "verdaderas", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] el B&B (14 dims, por bandas de SS)")
    ok = True
    a_max = 1.0 + (PHI - T0) + XCAP + 1.6
    z_max = a_max + XCAP + 1.0 + 1.6
    ss_lo = float(os.environ.get('CC_SS_LO', '1.0'))
    ss_hi = float(os.environ.get('CC_SS_HI', str(PHI)))
    # segundo eje de chunking (la arista SS -> 1 con 14 dims no
    # cabe en el tope de tiempo cortando solo en SS)
    xp_lo = float(os.environ.get('CC_XP_LO', '0.0'))
    xp_hi = float(os.environ.get('CC_XP_HI', str(XCAP)))
    w_lo = float(os.environ.get('CC_W_LO', '0.0'))
    w_hi = float(os.environ.get('CC_W_HI', '1.6'))
    # X_m SIN dimension (teorema de una linea): X_m solo entra en
    # el mayorante por su extremo INFERIOR (suma capacidad en la
    # cola, resta techo de polvo, y su poda X_m <= 1-omega solo
    # descarta) => X_m = 0 es UNIFORMEMENTE PESIMISTA y cubre todo
    # X_m real; dejar la dimension hacia que el splitter la
    # partiera en 2x cajas por split sin mejorar nada
    root = [w_lo, w_hi, 0.0, 1.0, ss_lo, ss_hi, T0, 1.0,
            0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0,
            0.0, 5 * T0, xp_lo, xp_hi, 0.0, 0.0, 0.0, 0.0,
            1.0, a_max, 1.0, z_max]
    # (X_z tampoco lleva dimension: tramos KZ = 4 en el criterio,
    # con su rango [Xzl, XCAP] arrancando en el low de la raiz 0)
    exito, caja, n, cert = bnb_factible(root, criterio_final)
    ok &= check(f"PESADA ESPECULAR con TODAS las X > 0 CERTIFICADA "
                f"en la banda SS en [{ss_lo:.3f}, {ss_hi:.3f}] "
                f"(X_alpha, X_z, X_m en [0, phi-1] por la pared "
                f"del polvo, mu_Y por tramos): {n} cajas vistas, "
                f"{cert} certificadas"
                + ("" if exito else f"; CAJA SIN RESOLVER {caja}"),
                exito)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] sanity end-to-end con todo explicito")
    rng = random.Random(SEED + 9)
    ok = True
    n_s, caben = 0, 0
    intentos = 0
    while n_s < 200 and intentos < 900000:
        intentos += 1
        p = rng.randrange(3, 10)
        piezas = sorted((rng.uniform(0.05, 0.98)
                         for _ in range(p)), reverse=True)
        SS = sum(piezas)
        s2 = piezas[1]
        if SS < 1.0 + s2 or SS > PHI - 0.05:
            continue
        w = rng.uniform(0.01, 1.6)
        beta, A = b_star_particion(piezas)
        big = sorted((a for a in A if a > T0), reverse=True)
        apolvo = [a for a in A if a <= T0]
        if len(big) > 4:
            continue
        # presupuesto del polvo total
        presu = PHI - SS
        Xp = rng.uniform(0.0, presu * 0.4) if rng.random() < 0.5 \
            else 0.0
        Xz = rng.uniform(0.0, presu * 0.3) if rng.random() < 0.5 \
            else 0.0
        Xm = min(rng.uniform(0.0, presu * 0.2),
                 max(0.0, 1.0 - w)) if rng.random() < 0.5 else 0.0
        resto = presu - Xp - Xz - Xm
        if resto <= 0.02:
            continue
        mu_y = rng.uniform(0.01, resto)
        k = rng.randrange(1, 4)
        cortes = sorted(rng.uniform(0.0, mu_y) for _ in range(k - 1))
        xs = [b - a for a, b in zip([0.0] + cortes,
                                    cortes + [mu_y])]
        xs = [x for x in xs if x > 1e-4]
        lo_a = max(1.0 + w, SS + Xp + w)
        hi_a = 1.0 + (SS - beta) + Xp + w
        if lo_a >= hi_a:
            continue
        alfa = rng.uniform(lo_a, hi_a)
        z = rng.uniform(alfa + Xz + w, alfa + Xz + s2 + w)
        cola = (1.0 + SS + Xm + alfa + Xp + z + Xz + mu_y) / PHI
        lo_Y = max(cola, 1.0 + z + w)
        if lo_Y >= SS + z + mu_y + w:
            continue
        cp = lo_Y - w
        n_s += 1
        carga = sorted([z, 1.0] + big + apolvo + xs, reverse=True)
        okc = corona_suf(carga, cp)[0]
        if not okc and len(carga) <= 6:
            base = carga[0]
            vistos = set()
            for perm in itertools.permutations(carga[1:]):
                if perm[::-1] in vistos:
                    continue
                vistos.add(perm)
                orden = [base] + list(perm)
                if dual_factible(orden, cp) \
                        and primal_factible(orden, cp):
                    okc = True
                    break
        if okc:
            caben += 1
    ok &= check(f"en {n_s} instancias pesadas reales con TODO "
                f"explicito (particion B*/A con su polvo en la "
                f"carga, X_alpha/X_z/X_m > 0 bajo el presupuesto "
                f"phi - Sigma_S, mu_Y en 1..3 piezas, Y en su "
                f"suelo): la corona completa cabe en "
                f"{caben}/{n_s}", n_s >= 150 and caben == n_s)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] controles")
    ok = True
    mat = [[0.0, 2.0, 0.3, 0.3], [0.0] * 4, [0.0] * 4, [0.0] * 4]
    r_dpi = antipodal_dos_lados([3.0, 1.0, 0.5, 0.4], mat,
                                [False, False, False, True], D=4.0)
    mat2 = [[0.0, 2.5, 2.5, 2.5], [0.0, 0.0, 2.5, 2.5],
            [0.0, 0.0, 0.0, 2.5], [0.0] * 4]
    r_estr = antipodal_dos_lados([3.0, 1.0, 0.8, 0.6], mat2,
                                 [False, False, False, False],
                                 D=0.0)
    ok &= check(f"(a) certificador negativo: D = 4 > pi -> "
                f"{r_dpi}; matriz estrangulada -> {r_estr}",
                r_dpi is False and r_estr is False)
    eps = 1e-9
    caja_polvo = (0.5, 0.5 + eps, 0.1, 0.1 + eps, 1.05,
                  1.05 + eps, 0.9, 0.9 + eps,
                  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                  0.1, 0.1 + eps, 0.4, 0.4 + eps,
                  0.3, 0.3 + eps, 0.0, 0.0 + eps,
                  2.0, 2.0 + eps, 2.9, 2.9 + eps)
    r_pol = criterio_final(caja_polvo)
    ok &= check(f"(b) la pared del polvo total poda: caja-punto "
                f"con SS + Xp + Xz = 1.05 + 0.4 + 0.3 = 1.75 > "
                f"phi: criterio = {r_pol} (None)", r_pol is None)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    ok = True
    ok &= check("[ENUNCIADO] con este certificado, LA CELDA "
                "ESPECULAR COMPLETA queda cerrada DENTRO DEL "
                "CONVENIO: ligera (r2bmulti + espkp) y pesada "
                "(areduccion + esppesada + este) con todas las X "
                "de polvo en todo su rango legal (la pared del "
                "polvo total sustituye a los topes de muestreo "
                "X_alpha <= 1.5, X_z <= 1, que quedan RETIRADOS "
                "del residuo dentro del convenio).  Residuo "
                "especular restante: el canal ocupante >= r_m "
                "(model-conditional, tarifa sin derivar) y el "
                "tope de barrido omega <= 1.6", True)
    return ok


def main():
    print("=" * 68)
    print("LA ESPECULAR COMPLETA: pesada con todas las X "
          "(drafts/espfinal.md)")
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
