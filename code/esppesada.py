#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La pesada especular con X_Y > 0 (docs/drafts/esppesada.md):
el ultimo cuarto de la celda especular, dentro del convenio.

Tras espkp (ligera con X_Y > 0 cerrada) y areduccion (pesada en el
corte X = 0 cerrada), quedaba la PESADA con X_Y > 0.  DENTRO DEL
CONVENIO X_Y = polvo < m (el canal ocupante >= r_m sigue
MODEL-CONDITIONAL, acta espxy corr. 5):

  LA FUSION DE BLOQUES: el polvo de X_Y (masa mu_Y <= phi -
  Sigma_S, cola global de m; cada pieza <= mu_Y por pigeonhole) se
  funde con el polvo de la particion B*/A de areduccion en UNA
  cadena monotona: masa total = mu_A + mu_Y, tope de pieza =
  max(t0, mu_Y), coste <= pi (mu_A + mu_Y)/(c' - tope).

  LA REDUCCION SIN DIMENSION NUEVA: el criterio con mu_Y clavado
  en su techo phi - Sigma_S_lo y la cola de Y SIN el termino +mu_Y
  es UNIFORMEMENTE PESIMISTA — mas polvo solo endurece, y omitir
  +mu_Y en la cola da una cota inferior valida de c' (renuncia
  declarada al beneficio de capacidad del polvo).  El B&B corre en
  las MISMAS 11 dimensiones de areduccion criterio_gg.

Bloques: [A] enunciado (fusion + renuncia + convenio); [B] el B&B;
[C] sanity end-to-end con piezas explicitas; [D] controles
(certificador negativo + pared del polvo); [E] estatus — LA CELDA
ESPECULAR ENTERA (ligera + pesada, X_Y > 0 incluido) cerrada
dentro del convenio en sus cortes/cajas declarados.
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


def criterio_pesada_xy(box):
    """Caja (w, s2, SS, beta, a1..a4, mu_A, alfa, z) — las 11 dims
    de areduccion criterio_gg — con el polvo de X_Y FUNDIDO al
    techo phi - SS_lo y la cola SIN su termino (pesimista
    uniforme).  None = sin puntos reales."""
    wl, wh, s2l, s2h, SSl, SSh, bl, bh = box[:8]
    als = [(box[i], box[i + 1]) for i in range(8, 16, 2)]
    mul, muh = box[16], box[17]
    al_, ah_ = box[18], box[19]
    zl, zh = box[20], box[21]
    # podas exactas (identicas a criterio_gg) + LA PARED PESADA
    if SSh <= 1.0 or SSl > PHI:
        return None
    if SSh < 1.0 + s2l:
        return None                    # pared PESADA SS >= 1 + s2:
                                       # la ligera con X_Y la cierra
                                       # espkp — sin esta poda el
                                       # B&B re-certificaba carisimo
                                       # la region ligera en SS -> 1
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
    a_lo = max(al_, 1.0 + wl, SSl + wl)
    a_hi = min(ah_, 1.0 + (SSh - bl) + wh)
    if a_lo >= a_hi:
        return None
    z_lo = max(zl, a_lo + wl)
    z_hi = min(zh, a_hi + s2h + wh)
    if z_lo >= z_hi:
        return None
    # (la cola por tramos se calcula abajo; la pinza global usa la
    # cola sin mu_Y como poda conservadora)
    cola_base = (1.0 + SSl + a_lo + z_lo) / PHI
    if cola_base >= SSh + z_hi + (PHI - max(SSl, 1.0)) + wh:
        return None
    # clamps de ligadura (identicos)
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
    # LA RENUNCIA POR TRAMOS (reparacion del atasco en SS -> 1):
    # el rango oculto de mu_Y en [0, phi - SS_lo] se parte en K = 8
    # tramos [t_i, t_{i+1}]; cada tramo se certifica con el polvo
    # al TECHO del tramo (masa mu_A + t_{i+1}, cap max(t0*,
    # t_{i+1})) y el CREDITO de cola del SUELO del tramo
    # (cola >= (... + t_i)/phi para todo mu_Y >= t_i) — ambas
    # direcciones sound; sin el credito, el techo del polvo y el
    # suelo diametral coinciden en SS -> 1 y crean una tangencia
    # FANTASMA (la caja atascada del v1).  Un tramo cuya ventana
    # de Y es vacia queda vacuamente cubierto.
    mu_y_max = max(0.0, PHI - max(SSl, 1.0))
    mu_a = mu_eff if muh > 0 else 0.0
    cap_a = T0 if mu_a > 0 else 0.0
    murales = [z_hi, 1.0] + [e for e, (_, a_h) in zip(a_effs, als)
                             if a_h > 0]
    K = 8                              # K = 4 perdia hasta
                                       # (techo/4)/phi ~ 0.10 de
                                       # cola y rozaba pi en la
                                       # arista SS -> 1
    for k_seg in range(K):
        t_lo = mu_y_max * k_seg / K
        t_hi = mu_y_max * (k_seg + 1) / K
        # pinza del tramo: sin Y legal para mu_Y en [t_lo, t_hi]
        # => tramo vacuo
        cola_seg = (1.0 + SSl + a_lo + z_lo + t_lo) / PHI
        if cola_seg >= SSh + z_hi + t_hi + wh:
            continue
        c_lo = max(1.0 + z_lo, cola_seg - wh)
        masa = mu_a + t_hi
        cap = max(cap_a, t_hi)
        # PLIEGUE de ranuras fantasma (optimizacion sound): toda
        # pieza de A con techo <= cap la cubre el bloque por masa
        # (pieza <= cap y masa += su techo >= su valor real) — sin
        # el pliegue, los nodos diminutos cerca de SS -> 1
        # multiplican mascaras/permutaciones del camino y el B&B
        # no cabe en el tope de tiempo de la maquina
        # DOS VARIANTES sound, en OR (el pliegue de piezas
        # medianas duplica su coste — pi·masa/(R-cap) con cap
        # grande — y creaba falsas tangencias; sin pliegue, los
        # nodos fantasma disparan el coste combinatorio cerca de
        # SS -> 1): primero CON pliegue (rapida), y solo si falla,
        # SIN pliegue (completa) — ambas certifican suficiencia
        def _certifica(plegar):
            hi = [murales[0], murales[1]]
            masa_v = masa
            for e in murales[2:]:
                if plegar and e <= cap + 1e-15:
                    masa_v += e
                else:
                    hi.append(e)
            es_polvo = [False] * len(hi)
            if masa_v > 0:
                hi.append(cap)
                es_polvo.append(True)
            if c_lo <= max(hi[1:] + [1.0]) + 1e-12:
                return False
            n = len(hi)
            thmat = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if i == 0:
                        t_ac = th(z_hi, hi[j], 1.0 + z_hi)
                        t_gl = th(z_hi, hi[j], c_lo) \
                            if c_lo > z_hi + 1e-12 else PI
                        thmat[i][j] = min(t_ac, t_gl)
                    else:
                        thmat[i][j] = th(hi[i], hi[j], c_lo)
            D = PI * masa_v / (c_lo - cap) if masa_v > 0 else 0.0
            return antipodal_dos_lados(hi, thmat, es_polvo, D)

        if not (_certifica(True) or _certifica(False)):
            return False
    return True


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] la fusion, la renuncia y el convenio")
    ok = True
    ok &= check("[ENUNCIADO] DENTRO DEL CONVENIO X_Y = polvo < m "
                "(el canal ocupante >= r_m sigue MODEL-CONDITIONAL "
                "— acta espxy corr. 5): la cola global de m capa "
                "mu_Y <= phi - Sigma_S (< 0.618 - sigma2 en la "
                "pesada) y el pigeonhole capa cada pieza por mu_Y. "
                " FUSION: una sola cadena monotona con el polvo de "
                "la particion B*/A — masa mu_A + mu_Y, tope "
                "max(t0, mu_Y), coste <= pi masa/(c' - tope) (la "
                "derivacion es cap-generica, acta de espkp: fuzz "
                "0/6000 con tope grande)", True)
    ok &= check("[ENUNCIADO] LA REDUCCION SIN DIMENSION, POR "
                "TRAMOS: el rango oculto mu_Y en [0, phi - SS_lo] "
                "se parte en 8 tramos; cada uno se certifica con "
                "el polvo al TECHO del tramo y el CREDITO de cola "
                "del SUELO del tramo (cola >= (...+t_lo)/phi vale "
                "para todo mu_Y >= t_lo; polvo <= mu_A + t_hi "
                "vale para todo mu_Y <= t_hi): pesimista uniforme "
                "POR TRAMO, y la union cubre todo mu_Y legal.  "
                "(La renuncia total del v1 creaba una tangencia "
                "fantasma en SS -> 1: el techo del polvo y el "
                "suelo diametral coinciden justo donde la cola "
                "del polvo era el rescate.)  El B&B corre en las "
                "MISMAS 11 dims de areduccion", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] el B&B (11 dims, renuncia por tramos)")
    ok = True
    a_max = 1.0 + (PHI - T0) + 1.6
    z_max = a_max + 1.0 + 1.6
    # chunking por bandas de SS (la maquina mata los runs > ~10
    # min; el DFS no es resumible — se parte la RAIZ): CC_SS_LO /
    # CC_SS_HI seleccionan la banda; sin ellas, la caja entera.
    ss_lo = float(os.environ.get('CC_SS_LO', '1.0'))
    ss_hi = float(os.environ.get('CC_SS_HI', str(PHI)))
    root = [0.0, 1.6, 0.0, 1.0, ss_lo, ss_hi, T0, 1.0,
            0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0,
            0.0, 5 * T0, 1.0, a_max, 1.0, z_max]
    exito, caja, n, cert = bnb_factible(root, criterio_pesada_xy)
    ok &= check(f"PESADA ESPECULAR con X_Y > 0 CERTIFICADA en la "
                f"banda SS en [{ss_lo:.3f}, {ss_hi:.3f}] (corte "
                f"X_alpha = X_z = X_m = 0, renuncia por tramos): "
                f"el mural {{z, m}} U A_big U polvo fundido cabe "
                f"en c'; {n} cajas vistas, {cert} certificadas"
                + ("" if exito else f"; CAJA SIN RESOLVER {caja}"),
                exito)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] sanity end-to-end con piezas explicitas")
    rng = random.Random(SEED + 5)
    ok = True
    n_s, caben = 0, 0
    intentos = 0
    while n_s < 200 and intentos < 600000:
        intentos += 1
        p = rng.randrange(3, 10)
        piezas = sorted((rng.uniform(0.05, 0.98)
                         for _ in range(p)), reverse=True)
        SS = sum(piezas)
        s2 = piezas[1]
        if SS < 1.0 + s2 or SS > PHI - 0.02:
            continue
        w = rng.uniform(0.01, 1.6)
        beta, A = b_star_particion(piezas)
        big = sorted((a for a in A if a > T0), reverse=True)
        if len(big) > 4:
            continue
        # el polvo de X_Y explicito: masa <= phi - SS, 1..3 piezas
        mu_y_max = PHI - SS
        mu_y = rng.uniform(0.01, mu_y_max)
        k = rng.randrange(1, 4)
        cortes = sorted(rng.uniform(0.0, mu_y) for _ in range(k - 1))
        xs = [b - a for a, b in zip([0.0] + cortes,
                                    cortes + [mu_y])]
        xs = [x for x in xs if x > 1e-4]
        # ventanas de la pesada (X = 0): alpha, z, cola CON mu_y
        lo_a = max(1.0 + w, SS + w)
        hi_a = 1.0 + (SS - beta) + w
        if lo_a >= hi_a:
            continue
        alfa = rng.uniform(lo_a, hi_a)
        z = rng.uniform(alfa + w, alfa + s2 + w)
        cola = (1.0 + SS + alfa + z + mu_y) / PHI
        lo_Y = max(cola, 1.0 + z + w)
        if lo_Y >= SS + z + mu_y + w:
            continue
        cp = lo_Y - w
        n_s += 1
        # el A-polvo VA en la carga (acta rep. 1: muA era codigo
        # muerto y la puerta sobrevendia el test)
        apolvo = [a for a in A if a <= T0]
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
    ok &= check(f"en {n_s} instancias pesadas reales con polvo "
                f"X_Y explicito (1..3 piezas, particion aleatoria "
                f"de mu_Y <= phi - SS; A-polvo de la particion "
                f"B*/A; Y en su suelo con la cola CONTANDO mu_Y): "
                f"la corona completa cabe en {caben}/{n_s} "
                f"(corona_suf, arc-LP de refuerzo si n <= 6)",
                n_s >= 150 and caben == n_s)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] controles")
    ok = True
    # (a) el certificador rechaza lo imposible (estandar de espkp)
    mat = [[0.0, 2.0, 0.3, 0.3], [0.0] * 4, [0.0] * 4, [0.0] * 4]
    r_dpi = antipodal_dos_lados([3.0, 1.0, 0.5, 0.4], mat,
                                [False, False, False, True], D=4.0)
    mat2 = [[0.0, 2.5, 2.5, 2.5], [0.0, 0.0, 2.5, 2.5],
            [0.0, 0.0, 0.0, 2.5], [0.0] * 4]
    r_estr = antipodal_dos_lados([3.0, 1.0, 0.8, 0.6], mat2,
                                 [False, False, False, False],
                                 D=0.0)
    ok &= check(f"(a) certificador negativo (estandar espkp, acta "
                f"rep. 3): bloque con D = 4 > pi -> {r_dpi}; "
                f"matriz estrangulada (theta = 2.5) -> {r_estr} — "
                f"el motor rechaza lo imposible",
                r_dpi is False and r_estr is False)
    # (a2) negativo de la poda pesada: caja-punto LIGERA -> None
    eps = 1e-9
    caja_lig = (0.5, 0.5 + eps, 0.6, 0.6 + eps, 1.3, 1.3 + eps,
                0.9, 0.9 + eps, 0.35, 0.35 + eps, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.05, 0.05 + eps,
                2.0, 2.0 + eps, 2.8, 2.8 + eps)
    r_lig = criterio_pesada_xy(caja_lig)
    ok &= check(f"(a2) la pared pesada poda la ligera: caja-punto "
                f"con SS = 1.3 < 1 + s2 = 1.6: criterio = {r_lig} "
                f"(None — territorio de espkp)", r_lig is None)
    # (b) la pared del polvo, COMPUTADA (acta rep. 5)
    v_phi = max(0.0, PHI - PHI)
    v_uno = max(0.0, PHI - 1.0)
    ok &= check(f"(b) coherencia de la pared, computada: mu_Y_max "
                f"= {v_phi:.4f} en SS_lo = phi (masa agotada) y "
                f"{v_uno:.4f} = phi - 1 en SS_lo = 1 — el mismo "
                f"techo de espkp; en la pesada real ademas mu_Y "
                f"<= phi - 1 - sigma2, que el techo por caja "
                f"mayora", v_phi == 0.0
                and abs(v_uno - (PHI - 1.0)) < 1e-15)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    ok = True
    ok &= check("[ENUNCIADO] con este certificado, LA CELDA "
                "ESPECULAR ENTERA queda cerrada DENTRO DEL "
                "CONVENIO en sus cortes/cajas declarados: ligera "
                "con X > 0 y X_Y = 0 (r2bmulti), ligera con "
                "X_Y > 0 (espkp, con X_alpha/X_z/X_m > 0), pesada "
                "en X = 0 (areduccion) y pesada con X_Y > 0 (este "
                "script, corte X_alpha = X_z = X_m = 0).  RESIDUO "
                "declarado de la especular: la pesada con "
                "X_alpha/X_z/X_m > 0 (solo-MC, G-g de puertocii), "
                "el canal ocupante >= r_m (model-conditional) y "
                "los topes del barrido (omega <= 1.6, X_alpha <= "
                "1.5, X_z <= 1)", True)
    return ok


def main():
    print("=" * 68)
    print("LA PESADA ESPECULAR CON X_Y > 0 (drafts/esppesada.md)")
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
