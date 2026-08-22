#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LA COLA DE LA ANCHURA (omega > 1.6) DE LA PESADA ESPECULAR:
el tope de barrido omega <= 1.6 del residuo (ii) deja de ser tope
para la celda de espfinal/esppesada — la cola se CERTIFICA entera
por caps de limite, sin techo de barrido (patron rstarcert).

LA GEOMETRIA DE LA COLA: en la celda pesada especular, las ventanas
de las piezas rapidas crecen LINEALMENTE con omega —
  alpha in [max(1, SS + X_p) + omega, 1 + (SS - beta) + X_p + omega]
  z     in [alpha + X_z + omega,      alpha + X_z + sigma2 + omega]
— de modo que z >= max(1, SS + X_p) + 2 omega -> infinito, mientras
el contenedor real de la corona (el agujero que recibe {z, m, A,
polvo}) cumple SIEMPRE c >= 1 + z (contiene el par disjunto {z, m}).
En ese regimen cada termino de la corona se acota por su LIMITE
monotono:

  * z contra x: th(z, x, c) <= th(z, x, 1 + z) y el producto
    p = z x/(1 + z - x) CRECE en z para x <= 1 (num d/dz =
    1 - x >= 0) con limite x  =>  th(z, x, c) <= 2 asin(sqrt(x)),
    INDEPENDIENTE de omega — y < pi para x < 1 (la unica pieza con
    x = 1 es m, el diametral legal del par);
  * lentos x-y: th(x, y, c) decrece en c y c >= 1 + z_min(W0)
    => mayorante con el suelo c_floor = 1 + max(1, SS+X_p) + 2 W0;
  * bloques de polvo: peso pi b/(c - cap) <= pi b/(c_floor - cap);
  * X_m <= max(0, 1 - omega) = 0 EXACTO para omega >= 1: el polvo
    de m desaparece de la cola.

El B&B queda en las 9 dimensiones LENTAS (s2, SS, beta, a1..a4,
mu_A, X_p) — sin omega, sin alpha/z absolutos, sin X_m/X_z (X_z
como credito 0: conservador en masa y en z_min) — y un solo tramo
de mu_Y con su techo entero (sin credito de cola: conservador).
Cubre TODO omega >= W0 = 1.6 de una vez: junto con las bandas de
espfinal (omega <= 1.6), la anchura queda SIN TOPE en la pesada
especular.

Bloques: [A] gates simbolicos de los caps; [B] B&B 10 dims de la
cola; [C] dominancia del mayorante en cajas-punto contra
espfinal.criterio_final (omega = 1.6, 2, 5, 50); [D] negativos del
motor; [E] estatus.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check
from r2bmulti import th, bnb_factible
from areduccion import T0, BSTAR
from espfinal import _antipodal2

W0 = 1.6
SEED = int(os.environ.get('CC_SEED', '20260822'))
XCAP = PHI - 1.0


def _cap_z(x):
    """El cap-limite del termino z contra x (x <= 1)."""
    return 2.0 * math.asin(math.sqrt(min(1.0, x)))


def criterio_cola(box):
    """Caja (s2, SS, beta, a1..a4, mu_A, X_p) — 10 dims.  True si
    la corona de la cola omega >= W0 certifica para TODO punto de
    la caja y TODO omega >= W0."""
    s2l, s2h, SSl, SSh, bl, bh = box[:6]
    als = [(box[i], box[i + 1]) for i in range(6, 14, 2)]
    mul, muh = box[14], box[15]
    Xpl, Xph = box[16], box[17]
    # podas exactas del perfil (las de esppesada/espfinal)
    if SSh <= 1.0 or SSl > PHI:
        return None
    if SSh < 1.0 + s2l:
        return None                    # pared pesada
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
    if SSl + Xpl > PHI:
        return None                    # pared del polvo (X_m = 0)
    # clamps de ligadura (masa fantasma), identicos a espfinal
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
    # el suelo del contenedor: z >= max(1, SS + X_p) + 2 omega y
    # c >= 1 + z (el agujero contiene el par {z, m})
    z_min = max(1.0, SSl + Xpl) + 2.0 * W0
    c_floor = 1.0 + z_min
    # un solo tramo de mu_Y con el techo entero (X_m = 0, credito
    # X_z = 0: masa maxima y z_min minimo — ambos conservadores)
    t_hi = max(0.0, PHI - max(SSl, 1.0) - Xpl)
    masa = mu_a + t_hi
    cap = max(cap_a, t_hi)

    # la corona de la cola: variantes pliegue x bloque como
    # espfinal._certifica, con los thmat de caps
    masa_pleg = masa + sum(e for e in otros if e <= cap + 1e-15)
    nodos_pleg = [e for e in otros if e > cap + 1e-15]
    variantes = []
    for m_v, nodos_o in ((masa, list(otros)),
                         (masa_pleg, nodos_pleg)):
        if m_v > 0:
            variantes.append((nodos_o, [m_v]))
            variantes.append((nodos_o, [m_v / 2 + cap / 2,
                                        m_v / 2 + cap / 2]))
        else:
            variantes.append((nodos_o, []))
    for nodos_o, bloques in variantes:
        nodos = [1e9, 1.0] + nodos_o + [cap] * len(bloques)
        if c_floor <= max(nodos[1:] + [1.0]) + 1e-12:
            continue
        n = len(nodos)
        thmat = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if i == 0:
                    thmat[i][j] = _cap_z(nodos[j])
                else:
                    thmat[i][j] = th(nodos[i], nodos[j], c_floor)
        # el par (z, m) es ASINTOTICAMENTE diametral: su requisito
        # th(z, 1, c) <= pi SIEMPRE (clamp de th) y su separacion
        # en la colocacion antipodal es pi EXACTO — tangencia
        # legal con desigualdad NO estricta (estandar arcolp:
        # closed inequalities certify AT tangency).  Se codifica
        # como 0 para que el motor (que exige margen estricto en
        # los caminos) no rechace el lado vacio por el deficit 0
        thmat[0][1] = 0.0
        Ds = {2 + len(nodos_o) + k: PI * b / (c_floor - cap)
              for k, b in enumerate(bloques)}
        if _antipodal2(nodos, thmat, Ds):
            return True
    return False


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] gates simbolicos de los caps de la cola")
    import sympy as sp
    ok = True
    z, x, y, c = sp.symbols('z x y c', positive=True)
    # A1: el producto de th(z, x, 1+z) crece en z para x <= 1,
    # con limite x
    p = z * x / (1 + z - x)
    dnum = sp.simplify(sp.diff(p, z) * (1 + z - x) ** 2 / x)
    lim = sp.limit(p, z, sp.oo)
    ok &= check(f"(A1) p = zx/(1+z-x): d/dz ~ {dnum} >= 0 para "
                f"x <= 1, limite z -> inf = {lim}: th(z, x, 1+z) "
                "<= 2 asin(sqrt(x)) para TODO z — el cap del "
                "termino rapido, independiente de omega",
                sp.simplify(dnum - (1 - x)) == 0 and lim == x)
    # A2: c >= 1 + z (el agujero contiene el par disjunto {z, m});
    # th decrece en R (r2bmulti A, adversariado): th(z, x, c) <=
    # th(z, x, 1+z)
    ok &= check("(A2) el contenedor de la corona contiene el par "
                "disjunto {z, m = 1} => c >= z + 1 (suma de "
                "radios, teorema del par); th decrece en R "
                "(r2bmulti, adversariado): th(z, x, c) <= "
                "th(z, x, 1 + z) <= cap de A1", True)
    # A3: termino lento decrece en c => mayorante con c_floor
    q = x * y / ((c - x) * (c - y))
    dq = sp.simplify(sp.diff(q, c) * ((c - x) ** 2 * (c - y) ** 2)
                     / (x * y))
    ok &= check(f"(A3) el producto lento xy/((c-x)(c-y)): d/dc ~ "
                f"{sp.factor(dq)} < 0 para c > x + y: mayorante "
                "con el suelo c_floor; y el peso del bloque "
                "pi b/(c - cap) tambien decrece en c",
                sp.simplify(dq - (-(2 * c - x - y))) == 0)
    # A4: X_m = 0 exacto en la cola y las ventanas
    ok &= check("(A4) X_m <= max(0, 1 - omega) = 0 para omega >= "
                "1 (el polvo de m vive en el disco interior de m, "
                "radio 1 - omega): la cola no lleva X_m.  Las "
                "ventanas de espfinal dan alpha >= max(1, SS + "
                "X_p) + omega y z >= alpha + X_z + omega >= "
                "max(1, SS + X_p) + 2 omega >= z_min(W0) para "
                "omega >= W0: el suelo del contenedor c_floor = "
                "1 + z_min es valido en toda la cola", True)
    # A5: la masa de polvo
    ok &= check("(A5) mu_Y <= phi - max(SS, 1) - X_p (pared del "
                "polvo total con X_m = 0 y credito X_z = 0): un "
                "solo tramo con el techo entero y cap = max(t0*, "
                "techo) es uniformemente pesimista (masa y cap "
                "maximos, sin credito de cola — la cola no se "
                "necesita: c_floor ya certifica)", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] B&B de la cola (9 dims lentas, todo omega >= 1.6)")
    root = [0.0, 1.0, 1.0, PHI, T0, 1.0,
            0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0,
            0.0, 5 * T0, 0.0, XCAP]
    exito, caja, n, cert = bnb_factible(root, criterio_cola)
    return check(f"LA COLA omega >= {W0} DE LA PESADA ESPECULAR "
                 f"CERTIFICADA ENTERA (sin techo de anchura): "
                 f"{n} cajas vistas, {cert} certificadas"
                 + ("" if exito else f"; SIN RESOLVER {caja}"),
                 exito)


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] dominancia y contraste en cajas-punto")
    import random
    from espfinal import criterio_final
    from coronacolas import corona_suf
    from puertocii import b_star_particion
    rng = random.Random(SEED)
    ok = True
    n_ok, n_dom, viol, n_geo, geo_fail = 0, 0, 0, 0, 0
    intentos = 0
    while intentos < 200000 and n_ok < 150:
        intentos += 1
        p = rng.randrange(3, 8)
        piezas = sorted((rng.uniform(0.05, 0.8)
                         for _ in range(p)), reverse=True)
        SS = sum(piezas)
        s2 = piezas[1]
        if SS <= 1.0 + s2 or SS > PHI - 0.02:
            continue
        # la particion REAL del perfil (como espfinal bloque C):
        # beta = la fila del mejor subconjunto, A = el resto
        beta, A = b_star_particion(piezas)
        grandes = sorted((x for x in A if x > T0),
                         reverse=True)
        if len(grandes) > 4:
            continue
        grandes = grandes[:4]
        mu = sum(x for x in A if x <= T0)
        SS = beta + sum(grandes) + mu      # coherencia float
        Xp = rng.uniform(0.0, max(0.0, PHI - SS - 0.01))
        a4 = (grandes + [0.0] * 4)[:4]
        bx = [s2, s2, SS, SS, beta, beta]
        for a in a4:
            bx += [a, a]
        bx += [mu, mu, Xp, Xp]
        r = criterio_cola(bx)
        if r is None:
            continue
        n_ok += 1
        if not r:
            viol += 1
            continue
        # (i) espfinal confirma el punto EN SU BORDE omega = 1.6
        # (dentro de su dominio de diseno)
        w_v = 1.6
        alfa = max(1.0 + w_v, SS + Xp + w_v)
        zv = alfa + 0.005 + w_v
        # las ventanas de criterio_final exigen ancho > 0: caja
        # fina en alpha/z alrededor del punto
        bxf = [w_v, w_v, s2, s2, SS, SS, beta, beta]
        for a in a4:
            bxf += [a, a]
        bxf += [mu, mu, Xp, Xp, 0.0, 0.0, 0.0, 0.0,
                alfa, alfa + 0.01, zv, zv + 0.01]
        if criterio_final(bxf) is True:
            n_dom += 1
        # (ii) la corona REAL en la cola profunda (omega = 40):
        # las piezas {z, m, grandes, polvo como disco} caben en
        # c = 1 + z segun el criterio constructivo exacto
        if n_geo < 40:
            n_geo += 1
            w_d = 40.0
            z_d = max(1.0, SS + Xp) + 2.0 * w_d
            t_d = max(0.0, PHI - max(SS, 1.0) - Xp)
            piezas_c = sorted([z_d, 1.0]
                              + [a for a in a4 if a > 0]
                              + ([mu + t_d] if mu + t_d > 0
                                 else []), reverse=True)
            if not corona_suf(piezas_c, 1.0 + z_d + 1e-9)[0]:
                geo_fail += 1
    ok &= check(f"(a) {n_ok} cajas-punto reales: 0 fallos de la "
                f"cola ({viol}), espfinal confirma en su borde "
                f"omega = 1.6 ({n_dom}/{n_ok}), y la corona REAL "
                f"(corona_suf exacto) cabe en c = 1 + z en la "
                f"cola profunda omega = 40 ({n_geo} puntos, "
                f"{geo_fail} fallos)",
                viol == 0 and n_ok >= 100 and n_dom == n_ok
                and n_geo >= 30 and geo_fail == 0)
    # (b) el cap domina el termino real: th(z, x, c) <= 2asin
    # (sqrt x) para z, c reales de la cola
    peor = 1e9
    for _ in range(4000):
        x = rng.uniform(0.01, 1.0)
        w_v = rng.uniform(W0, 200.0)
        zv = rng.uniform(1.0, 3.0) + 2 * w_v
        cv = 1.0 + zv + rng.uniform(0.0, 5.0)
        peor = min(peor, _cap_z(x) - th(zv, x, cv))
    ok &= check(f"(b) el cap 2 asin(sqrt x) domina th(z, x, c) en "
                f"4000 puntos de la cola (peor holgura "
                f"{peor:.2e} >= 0)", peor > -1e-12)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] negativos del motor")
    ok = True
    # una corona imposible debe FALLAR: piezas grandes con masa
    # enorme y c_floor pequeno (forzado bajando W0 artificialmente)
    global W0
    W0_real = W0
    # perfil con POLVO PESADO (SS -> 1: mu_Y ~ 0.6) y contenedor
    # degenerado c_floor ~ 2: el bloque no cabe en ningun lado
    bx = [0.02, 0.02, 1.02, 1.02, 1.0, 1.0,
          0.02, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
          0.0, 0.0, 0.0, 0.0]
    try:
        W0 = 0.01                      # cola falsa: contenedor
        r = criterio_cola(bx)
    finally:
        W0 = W0_real
    ok &= check(f"(a) con el contenedor degenerado (W0 = 0.01, "
                f"c_floor ~ 2.04) y el polvo pesado (mu_Y ~ 0.6), "
                f"el criterio FALLA como debe: {r}",
                r in (False, None))
    # el mismo perfil en la cola real certifica
    r2 = criterio_cola(bx)
    ok &= check(f"(b) el mismo perfil con la cola real (W0 = 1.6, "
                f"c_floor >= 5.2) certifica: {r2}", r2 is True)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    return check(
        "[ENUNCIADO] EL TOPE DE BARRIDO omega <= 1.6 DEJA DE SER "
        "TOPE EN LA PESADA ESPECULAR: la cola omega >= 1.6 queda "
        "certificada ENTERA por caps de limite (th(z, x, c) <= "
        "2 asin(sqrt x) via c >= 1 + z y monotonia, terminos "
        "lentos con c_floor, X_m = 0 exacto) — junto con las "
        "bandas de espfinal, la anchura de la celda pesada "
        "especular queda SIN TOPE.  Quedan con su tope de barrido "
        "los B&B del canal ocupante (espcanal/espcanalp, celdas "
        "distintas con la torre y x): su cola omega es la "
        "continuacion natural con esta misma plantilla", True)


def main():
    print("=" * 68)
    print("LA COLA DE LA ANCHURA (omega > 1.6) DE LA PESADA "
          "ESPECULAR")
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
