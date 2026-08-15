#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La certificacion k-piezas del sub-bolsillo (docs/drafts/
espkp.md): el REMATE de la celda ESP X_Y > 0 ligera.

Tras espvals (la vacuidad del peligro): toda pieza legal de X_Y
mide <= phi - Sigma_S < phi - 1 = 0.618 < x*(z) — sub-bolsillo
universal.  Quedaba certificar que la corona REAL de v — el trio
{z, D_m, sigma2} MAS el bloque de polvo X_Y (k piezas, k libre) —
cabe en c' = Y - omega en todo el dominio.  Este script lo
CERTIFICA por subdivision:

  LA PARED QUE CAPA EL POLVO (espvals/auditcolas, cola global de
  m): mu := Sigma X_Y <= phi - Sigma_S - X_m < 0.618 (Sigma_S > 1,
  pared D).  PIGEONHOLE: cada pieza de X_Y <= mu (la masa total) —
  el tope de pieza DECRECE con la caja.  El bloque se paga POR
  MASA (areduccion, convexidad del asin): cadena monotona interna
  <= pi mu / (c' - mu).

  EL CRITERIO (motor de areduccion/r2bmulti): antipodal z-m (el
  par diametral del suelo c' >= 1 + z, excluido analiticamente;
  theta(z, m) < pi estricto fuera del suelo y = pi cerrado en el),
  con sigma2 y el bloque de polvo repartidos en los dos
  semicirculos como sistemas de CAMINO (TU, dual disjunto exacto);
  para los pares con z, la cota ACOPLADA min(theta en 1+z_hi
  coherente, theta en c'_lo global); c'_lo = max(1 + z_lo,
  cola(Y)_lo - omega_hi) con la cola INCLUYENDO mu (el polvo de
  X_Y sube el suelo de Y: (...+mu)/phi).

  DOMINIO (ligera especular, caja del barrido de r2bmulti bloque
  D + la dimension nueva mu): omega <= 1.6, X_alpha <= 1.5,
  X_z <= 1, X_m <= 1 - omega, alpha <= 5.1, z <= 8.7, mu <=
  phi - Sigma_S - X_m (clamp por caja).  SUPERCONJUNTO del legal
  (las paredes usadas son verdaderas; omitir las demas agranda).

Bloques: [A] el enunciado y las paredes; [B] el B&B (9 dims); [C]
sanity end-to-end (piezas explicitas k = 1..4 vs arc-LP/
corona_suf); [D] controles (negativo, frontera x*); [E] estatus —
LA CELDA ESP X_Y > 0 LIGERA CERRADA (vacuidad + certificado); la
pesada con X_Y > 0 declarada (el polvo extra se funde con el
bloque de areduccion: siguiente).
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
from areduccion import antipodal_dos_lados
from espxy import x_star

SEED = int(os.environ.get('CC_SEED', '20260818'))
# (CC_ITER no aplica aqui: los tamanos estan cableados — acta)

W_MAX, XP_MAX, XZ_MAX = 1.6, 1.5, 1.0
A_MAX = 1.0 + 0.999 + XP_MAX + W_MAX
Z_MAX = A_MAX + XZ_MAX + 0.999 + W_MAX


def criterio_espkp(box):
    """Caja (w, s2, SS, Xp, Xz, Xm, a, z, mu) de la ESP ligera con
    polvo X_Y de masa mu.  None = sin puntos reales; True =
    certificada; False = partir."""
    wl, wh, s2l, s2h, SSl, SSh, Xpl, Xph, Xzl, Xzh, Xml, Xmh, \
        al, ah, zl, zh, mul, muh = box
    # podas exactas (dominio ligera + paredes verdaderas)
    if 2.0 * s2l > SSh:
        return None                    # s1 >= s2
    if SSl >= 1.0 + s2h:
        return None                    # ligera
    if SSl + Xml > PHI:
        return None                    # pared de masa (cola de m)
    if Xml > max(0.0, 1.0 - wl):
        return None                    # X_m <= 1 - omega
    # la pared del polvo (cola global de m): mu <= phi - SS - X_m
    mu_eff = min(muh, PHI - SSl - Xml)
    if mu_eff < mul:
        return None                    # sin mu legal en la caja
    # ventanas especulares (clamps, r2bmulti bloque D)
    a_lo = max(al, 1.0 + wl, SSl + Xpl + wl)
    a_hi = min(ah, 1.0 + s2h + Xph + wh)
    if a_lo >= a_hi:
        return None
    z_lo = max(zl, a_lo + Xzl + wl)
    z_hi = min(zh, a_hi + Xzh + s2h + wh)
    if z_lo >= z_hi:
        return None
    # ventana de Y no vacia: max(cola, 1+z+w) < SS + z + mu + w
    cola_lo = (1.0 + SSl + Xml + a_lo + Xpl + z_lo + Xzl
               + mul) / PHI
    if cola_lo >= SSh + z_hi + mu_eff + wh:
        return None                    # pinza: sin Y legal
    c_lo = max(1.0 + z_lo, cola_lo - wh)
    # nodos: 0 = z, 1 = m, 2 = sigma2, 3 = POLVO (masa mu_eff,
    # pieza <= mu_eff por pigeonhole)
    s2_p = min(s2h, SSh / 2.0)
    cap = mu_eff                       # tope de pieza del polvo
    hi = [z_hi, 1.0, s2_p, cap]
    es_polvo = [False, False, False, True]
    if c_lo <= max(1.0, s2_p, cap) + 1e-12:
        return False                   # sin resolver: partir
    n = len(hi)
    thmat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if i == 0:
                # pares con z: cota acoplada al suelo c' >= 1 + z
                t_ac = th(z_hi, hi[j], 1.0 + z_hi)
                t_gl = th(z_hi, hi[j], c_lo) \
                    if c_lo > z_hi + 1e-12 else PI
                thmat[i][j] = min(t_ac, t_gl)
            else:
                thmat[i][j] = th(hi[i], hi[j], c_lo)
    D = PI * mu_eff / (c_lo - cap) if mu_eff > 0 else 0.0
    return antipodal_dos_lados(hi, thmat, es_polvo, D)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] el enunciado y las paredes")
    ok = True
    ok &= check("[ENUNCIADO] LA PARED DEL POLVO (espvals/"
                "auditcolas), DENTRO DEL CONVENIO X_Y = polvo < m "
                "(acta de espkp: el canal 'ocupante >= r_m en v' "
                "es MODEL-CONDITIONAL con tarifa sin derivar — "
                "acta espxy corr. 5 y banda X >= 1 de auditcolas): "
                "la cola global de m capa mu = Sigma X_Y <= "
                "phi - Sigma_S - X_m < phi - 1 = 0.618 (pared D); "
                "PIGEONHOLE: cada pieza <= mu.  Con x*(z) > 0.618 "
                "en todo el dominio, todo el polvo es sub-bolsillo "
                "— queda certificar la corona conjunta {z, D_m, "
                "sigma2} U polvo, que comparte LA FORMA del mural "
                "de areduccion (el bloque de polvo pagado por "
                "masa, cadena MONOTONA <= pi mu/(c' - mu) — el "
                "orden monotono es carga real heredada, y la "
                "derivacion es cap-generica: fuzz del acta con "
                "cap = mu, 0/6000, contraejemplo no-monotono "
                "sigue violando)", True)
    ok &= check("[ENUNCIADO] el criterio es SUFICIENCIA sobre "
                "superconjunto (auditcolas): las paredes usadas "
                "(ligera, masa, cola de m para mu, ventanas de "
                "G-g, cola de Y con mu incluida) son verdaderas y "
                "las omitidas solo agrandan el dominio — el "
                "certificado cubre todo punto legal", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] el B&B de 9 dimensiones")
    ok = True
    root = [0.0, W_MAX, 0.0, 0.999, 1.0, PHI, 0.0, XP_MAX,
            0.0, XZ_MAX, 0.0, 1.0, 1.0, A_MAX, 1.0, Z_MAX,
            0.0, PHI - 1.0]
    exito, caja, n, cert = bnb_factible(root, criterio_espkp)
    ok &= check(f"ESP X_Y > 0 ligera CERTIFICADA (caja del barrido "
                f"de r2bmulti + la dimension mu <= phi - Sigma_S - "
                f"X_m): la corona {{z, D_m, sigma2}} U polvo cabe "
                f"en c' = Y - omega en toda la caja; {n} cajas "
                f"vistas, {cert} certificadas"
                + ("" if exito else f"; CAJA SIN RESOLVER {caja}"),
                exito)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] sanity end-to-end con piezas explicitas")
    rng = random.Random(SEED)
    ok = True
    n, caben = 0, 0
    intentos = 0
    while n < 250 and intentos < 500000:
        intentos += 1
        w = rng.uniform(0.05, W_MAX)
        s2 = rng.uniform(0.05, 0.999)
        s1 = rng.uniform(s2, 0.999)
        SS = s1 + s2
        if SS <= 1.0 or SS >= 1.0 + s2 or SS > PHI:
            continue
        Xp = rng.uniform(0.0, XP_MAX) if rng.random() < 0.3 else 0.0
        Xz = rng.uniform(0.0, XZ_MAX) if rng.random() < 0.3 else 0.0
        Xm = rng.uniform(0.0, max(0.0, 1 - w)) \
            if rng.random() < 0.3 else 0.0
        mu_max = PHI - SS - Xm
        if mu_max <= 0.02:
            continue
        mu = rng.uniform(0.02, mu_max)
        k = rng.randrange(1, 5)
        cortes = sorted(rng.uniform(0.0, mu) for _ in range(k - 1))
        piezas_x = [b - a for a, b in
                    zip([0.0] + cortes, cortes + [mu])]
        piezas_x = [x for x in piezas_x if x > 1e-4]
        lo_a = max(1.0 + w, SS + Xp + w)
        hi_a = 1.0 + s2 + Xp + w
        if lo_a >= hi_a:
            continue
        alfa = rng.uniform(lo_a, hi_a)
        z = rng.uniform(alfa + Xz + w, alfa + Xz + s2 + w)
        cola = (1.0 + SS + Xm + alfa + Xp + z + Xz + mu) / PHI
        lo_Y = max(cola, 1.0 + z + w)  # z+mu+w redundante (mu < 1)
        hi_Y = SS + z + mu + w
        if lo_Y >= hi_Y:
            continue
        cp = lo_Y - w                  # el peor c' (Y en su suelo)
        n += 1
        # la corona completa con las piezas explicitas (arc-LP si
        # k <= 3 piezas de polvo => n <= 6; corona_suf si mas)
        carga = sorted([z, 1.0, s2] + piezas_x, reverse=True)
        if len(carga) <= 6:
            base = carga[0]
            vistos = set()
            okc = False
            for perm in itertools.permutations(carga[1:]):
                if perm[::-1] in vistos:
                    continue
                vistos.add(perm)
                orden = [base] + list(perm)
                if dual_factible(orden, cp) \
                        and primal_factible(orden, cp):
                    okc = True
                    break
        else:
            okc = corona_suf(carga, cp)[0]
        if okc:
            caben += 1
    ok &= check(f"en {n} puntos legales con polvo EXPLICITO "
                f"(k = 1..4 piezas, particion aleatoria de mu, Y "
                f"en su suelo): la corona completa cabe en "
                f"{caben}/{n} (arc-LP primal para n <= 6, "
                f"corona_suf si mas) — el certificado por bloque "
                f"coincide con las piezas reales",
                n >= 200 and caben == n)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] controles")
    ok = True
    # (a) negativo: mu por encima de la pared no certifica en una
    #     caja-punto con cola sin rescate
    eps = 1e-9
    caja_mala = (1.2, 1.2 + eps, 0.4, 0.4 + eps, 1.05, 1.05 + eps,
                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                 2.25, 2.25 + eps, 3.45, 3.45 + eps,
                 1.5, 1.5 + eps)
    r = criterio_espkp(caja_mala)
    ok &= check(f"(a) control negativo: mu = 1.5 > phi - SS = "
                f"0.568 en caja-punto: criterio = {r} (None = "
                f"podada por la pared del polvo, no certificada) "
                f"— la pared capa de verdad", r is None)
    # (a2) control negativo del CERTIFICADOR (acta, rep. 2): el
    #      motor antipodal rechaza un bloque imposible (D > pi) y
    #      una matriz estrangulada
    mat = [[0.0, 2.0, 0.3, 0.3], [0.0] * 4, [0.0] * 4, [0.0] * 4]
    r_dpi = antipodal_dos_lados([3.0, 1.0, 0.5, 0.4], mat,
                                [False, False, False, True], D=4.0)
    mat2 = [[0.0, 2.5, 2.5, 2.5], [0.0, 0.0, 2.5, 2.5],
            [0.0, 0.0, 0.0, 2.5], [0.0] * 4]
    r_estr = antipodal_dos_lados([3.0, 1.0, 0.8, 0.6], mat2,
                                 [False, False, False, False],
                                 D=0.0)
    ok &= check(f"(a2) el CERTIFICADOR rechaza lo imposible (no "
                f"solo la poda): bloque con D = 4 > pi -> "
                f"{r_dpi}; matriz con todos los theta = 2.5 (dos "
                f"por lado exceden pi) -> {r_estr}",
                r_dpi is False and r_estr is False)
    # (b) la frontera x*: una pieza unica en (x*, 1) NO es polvo
    #     legal (mu <= 0.618 < x*): coherencia con espvals
    zv = 3.5
    ok &= check(f"(b) coherencia con espvals: x*(3.5) = "
                f"{x_star(3.5):.4f} > 0.618 >= mu legal — el "
                f"sliver del bolsillo diametral queda fuera del "
                f"dominio del polvo por la propia pared (la "
                f"vacuidad) y este certificado NUNCA necesita "
                f"colocar una pieza sobre-bolsillo",
                x_star(zv) > PHI - 1.0)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    ok = True
    ok &= check("[ENUNCIADO] LA CELDA ESP X_Y > 0 LIGERA queda "
                "CERRADA DENTRO DEL CONVENIO X_Y = polvo < m: "
                "vacuidad del peligro (espvals) + certificado "
                "k-piezas (este script, k libre por el pago por "
                "masa).  El canal 'ocupante >= r_m en el "
                "contenedor de Y' sigue MODEL-CONDITIONAL (tarifa "
                "sin derivar — acta espxy corr. 5): no lo cierra "
                "este script y queda declarado.  Declarado "
                "tambien: la PESADA con X_Y > 0 (el polvo se "
                "funde con el bloque de areduccion — mismo motor, "
                "dominio con particion B*/A: siguiente ciclo "
                "natural); los topes de muestreo X_alpha <= 1.5, "
                "X_z <= 1, omega <= 1.6 siguen siendo del "
                "barrido", True)
    return ok


def main():
    print("=" * 68)
    print("CERTIFICACION K-PIEZAS DEL SUB-BOLSILLO "
          "(drafts/espkp.md)")
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
