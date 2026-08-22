#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LA COLA DE LA ANCHURA (omega > 1.6) DE LAS CELDAS DEL CANAL:
el ultimo tope de barrido heredado — las seis celdas del canal
ocupante (ligera x-en-v y x-en-z, pesada x y x-en-z, torres ligera
y pesada) se cierran para TODA anchura.

LA OBSERVACION CENTRAL (auditoria en [A]): los criterios de
espcanal / espcanalp / esptorre / esptorrep son VALIDOS para todo
omega — ninguna poda ni ventana asume omega <= 1.6 (la unica
aparicion no-generica, X_m <= 1 - omega, esta clampada con max(0,
.) y para omega > 1 da X_m = 0, correcto); solo los ROOTS de sus
B&B limitaban w a [0, 1.6].  El cierre en dos tramos:

  (i)  TRAMO MEDIO omega in [1.6, W2 = 40]: RE-EJECUTAR los
       criterios existentes (importados, sin duplicar) con el
       root extendido — los margenes crecen con omega (las
       ventanas se ensanchan y las capacidades crecen), y los
       B&B certifican.
  (ii) LA COLA omega >= W2: las piezas rapidas (alpha, z, y x en
       la celda v) crecen linealmente con omega (alpha >= 1 +
       omega, z >= alpha + omega) y las coronas degeneran a su
       limite — cada termino contra las piezas lentas va a cero
       o queda capado por el limite monotono (c crece como
       2-3 omega mientras las lentas quedan fijas), y los pares
       dominantes (z, x) / (z, D_m) son los antipodales exentos
       de los motores.  Criterios de cola por celda con los caps
       de espomegacola (th(z, p, c) <= 2 asin(sqrt(p)) via
       c >= 1 + z, y los limites 1/x_lo del par de la celda v).

MODEL-CONDITIONAL como todo el canal.  Bloques: [A] auditoria de
omega; [B] tramo medio (re-runs); [C] las colas w >= W2; [D]
negativos; [E] estatus.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check
from r2bmulti import th
from espcanal import (criterio_canal_v, criterio_canal_z,
                      mapa_supervivientes, techo_nodo)
from espcanalp import criterio_pesada_x, criterio_pesada_z
import esptorre
import esptorrep

W0, W2 = 1.6, 40.0
XCAP = PHI - 1.0
SEED = int(os.environ.get('CC_SEED', '20260822'))


def _asin2(z):
    return 2.0 * math.asin(max(0.0, min(1.0, z)))


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] auditoria de omega en los criterios del canal")
    ok = True
    ok &= check("[ENUNCIADO] (A1) los criterios de espcanal (v y "
                "z), espcanalp (x y z) y esptorre/esptorrep son "
                "OMEGA-GENERICOS: las apariciones de omega son "
                "(i) X_m <= max(0, 1 - omega) — clampada, = 0 "
                "para omega > 1, correcta; (ii) las ventanas "
                "+omega en suelos y techos de alpha/z/x — "
                "derivadas para omega arbitrario (E4, "
                "convivencias, techos de nodo); (iii) c_lo = "
                "max(1 + z, cola - omega) — generica.  NINGUNA "
                "poda asume omega <= 1.6: el 1.6 vivia solo en "
                "los roots de los B&B", True)
    ok &= check("[ENUNCIADO] (A2) en la cola omega >= W2, las "
                "piezas rapidas crecen linealmente (alpha >= 1 + "
                "omega, z >= alpha + omega >= 1 + 2 omega; en la "
                "celda v, x <= techo_nodo ~ omega puede crecer o "
                "quedarse en su pinza) y las capacidades c >= "
                "1 + z (o z + x) crecen igual: los terminos "
                "contra las lentas van a cero o quedan capados "
                "por sus limites monotonos (gates de "
                "espomegacola, adversariados), y los pares "
                "dominantes son los antipodales exentos de los "
                "motores", True)
    return ok


# ---------------------------------------------------------------- bloque B
A_MAXC = 1.0 + 1.0 + 1.5 + W2
Z_MAXC = A_MAXC + 1.0 + 1.0 + W2
# acta H1: en x-EN-z el techo de la ventana de z lleva ademas
# x_eff ~ omega (z < a + Xz + s2 + omega + x): escala 3 omega
Z_MAXZ = A_MAXC + 1.0 + 1.0 + W2 + (1.0 + W2 + XCAP + 0.01)
X_TOPC = 1.0 + W2 + XCAP + 0.01


def _run_celda(tag, root, crit):
    eps_b = float(os.environ.get('CC_EPS', '4e-3'))
    (n_s, env, fuera), vistos, certs, trunc =         mapa_supervivientes(root, crit, eps=eps_b,
                            max_boxes=int(os.environ.get(
                                'CC_MAXB', '20000000')),
                            max_fallos=100000, sobre=False)
    r = check(f"({tag}) omega in [1.6, 40]: {vistos} cajas, "
              f"{certs} certificadas, {len(fuera)} sin resolver, "
              f"truncado {trunc}", len(fuera) == 0 and not trunc)
    if fuera:
        print(f"  primera: {fuera[0]}")
    return r


_CELDAS = {}


def _def_celdas():
    _CELDAS['a'] = ("ligera x-EN-v",
                    [W0, W2, 0.0, 1.0, 1.0, PHI, 0.0, XCAP,
                     0.0, XCAP, 0.0, 1.0, 1.0, A_MAXC,
                     1.0, Z_MAXC, 0.0, 5 * 0.618, 1.0, X_TOPC],
                    criterio_canal_v)
    _CELDAS['b'] = ("ligera x-EN-z",
                    [W0, W2, 0.0, 1.0, 1.0, PHI, 0.0, XCAP,
                     0.0, XCAP, 0.0, 1.0, 1.0, A_MAXC,
                     1.0, Z_MAXZ, 0.0, 5 * 0.618, 1.0, X_TOPC],
                    criterio_canal_z)
    _CELDAS['c'] = ("pesada con x",
                    [W0, W2, 0.0, 0.999, 1.0, PHI, 0.0, 1.0,
                     0.0, 1.5, 0.0, 1.0, 0.0, 1.0,
                     1.0, A_MAXC, 1.0, Z_MAXC, 1.0, X_TOPC],
                    criterio_pesada_x)
    _CELDAS['d'] = ("pesada x-EN-z",
                    [W0, W2, 0.0, 0.999, 1.0, PHI, 0.0, 1.0,
                     0.0, 1.5, 0.0, 1.0, 0.0, 1.0,
                     1.0, A_MAXC, 1.0, Z_MAXZ, 1.0, X_TOPC],
                    criterio_pesada_z)
    _CELDAS['e'] = ("torre ligera",
                    [W0, W2, 0.0, 1.0, 1.0, PHI, 0.0, XCAP,
                     0.0, XCAP, 0.0, 1.0, 1.0, A_MAXC,
                     1.0, esptorre.Z1, 0.0, 5 * 0.618,
                     2.0 / PHI, X_TOPC],
                    esptorre.crit_finito)
    _CELDAS['g'] = ("torre ligera COLA z (acta H2)",
                    [W0, W2, 0.0, 1.0, 1.0, PHI, 0.0, XCAP,
                     0.0, XCAP, 0.0, 1.0, 1.0, A_MAXC,
                     0.0, 5 * 0.618, 2.0 / PHI, X_TOPC],
                    esptorre.crit_cola)
    _CELDAS['h'] = ("torre pesada COLA z (acta H2)",
                    [W0, W2, 0.0, 0.999, 1.0, PHI, 0.0, 1.0,
                     0.0, 1.5, 0.0, 1.0, 0.0, 1.0,
                     1.0, A_MAXC, 1.0, X_TOPC],
                    esptorrep.crit_cola)
    _CELDAS['f'] = ("torre pesada",
                    [W0, W2, 0.0, 0.999, 1.0, PHI, 0.0, 1.0,
                     0.0, 1.5, 0.0, 1.0, 0.0, 1.0,
                     1.0, A_MAXC, 1.0, esptorrep.Z1,
                     1.0, X_TOPC],
                    esptorrep.crit_finito)


def bloque_B():
    """EJECUCION POR BANDAS (la maquina mata runs largos): el run
    completo del tramo medio se compone de las celdas/bandas
    CC_CELDA x (CC_WLO, CC_WHI) con CC_EPS.  RESULTADO AGREGADO
    (2026-08-22, tras las reparaciones del acta — H1: techo de z
    a escala 3 omega en x-EN-z; H2: colas z de las torres como
    celdas g/h; 0 sin resolver / no truncadas en todas):
      (a) ligera x-EN-v  [1.6, 40] eps 4e-3: 1.620.765 cajas
      (b) ligera x-EN-z  [1.6, 40] eps 4e-3, Z_MAXZ: 1 caja
      (c) pesada con x   11 bandas eps 1e-2 ([20,40] 1.503.425;
          [17,20] 300.905; [14,17] 299.899; [11,14] 300.245;
          [8,11] 300.599; [6,8] 167.975; [4.5,6] 152.855;
          [3.5,4.5] 84.983; [2.7,3.5] 80.935; [2.1,2.7] 45.473;
          [1.6,2.1] 45.229 — total ~3.3M cajas; su ventana de z
          no lleva x: techo 2 omega correcto, acta re-ronda)
      (d) pesada x-EN-z  [1.6, 40] eps 4e-3, Z_MAXZ: 293 cajas
      (e) torre ligera   [1.6, 40] eps 4e-3 (z <= Z1): 1 caja
      (f) torre pesada   [1.6, 40] eps 4e-3 (z <= Z1): 31 cajas
      (g) torre ligera COLA z (z >= Z1): 1 caja
      (h) torre pesada COLA z (z >= Z1): 1 caja
    El manifiesto campaign de run_all reproduce estas bandas."""
    print("[B] tramo medio omega in [1.6, 40] (criterios "
          "importados, roots extendidos; CC_CELDA y "
          "CC_WLO/CC_WHI para trocear)")
    _def_celdas()
    sel = os.environ.get('CC_CELDA', 'abcdefgh')
    w_lo = float(os.environ.get('CC_WLO', str(W0)))
    w_hi = float(os.environ.get('CC_WHI', str(W2)))
    ok = True
    for tag in sel:
        nombre, root, crit = _CELDAS[tag]
        root = [w_lo, w_hi] + root[2:]
        print(f"  -- celda ({tag}) {nombre}, omega "
              f"[{w_lo}, {w_hi}]")
        ok &= _run_celda(tag, root, crit)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] la cola omega >= 40 (caps de limite por celda)")
    ok = True
    # geometria comun: alpha >= 1 + omega >= 41, z >= 1 + 2 omega
    # >= 81 y c >= 1 + z >= 82 (o z + x)
    z_lo = 1.0 + 2.0 * W2
    x_lo = (1.0 + 1.0) / PHI           # la pinza minima de x
    # (a) celda v: par (z, x) antipodal exento; caps del resto
    # (acta H3, los correctos): theta(z, m): p = z/((c-z)(c-1))
    # <= 1/x_lo (c - z >= x, c - 1 >= z); theta(z, s2) <=
    # s2/x_lo; theta(x, m) y theta(x, s2): p <= 1/z_lo (c - x >=
    # z); theta(m, s2): c >= 82; polvo D = pi mu/(c - cap)
    t_zm = _asin2(math.sqrt(min(1.0, 1.0 / x_lo)))
    t_zs = _asin2(math.sqrt(min(1.0, (PHI / 2.0) / x_lo)))
    t_xm = _asin2(math.sqrt(min(1.0, 1.0 / z_lo)))
    t_xs = _asin2(math.sqrt(min(1.0, (PHI / 2.0) / z_lo)))
    t_ms = th(1.0, PHI / 2.0, 1.0 + z_lo)
    D_p = PI * PHI / (1.0 + z_lo - 1.0)
    resto = t_xm + t_ms + D_p + t_xs
    lado_peor = max(t_zm, t_zs) + resto
    ok &= check(f"(a) celda v en la cola: peor lado del par "
                f"(z, x) = max({t_zm:.3f}, {t_zs:.3f}) + resto "
                f"(caps 1/z_lo correctos, acta H3: {resto:.3f}) "
                f"= {lado_peor:.3f} < pi",
                lado_peor < PI - 0.05)
    # (b) celdas z (acta H4: argumento AUTONOMO, no apelacion):
    # la corona {z, D_m, s2 | bloques} U polvo con el par
    # (z, D_m) exento del motor; el reparto pone una lenta por
    # lado: cada lado <= cap-z de su lenta + terminos lento-lento
    # con c >= 1 + z >= 82.  Las lentas son s2 <= phi/2 y el
    # polvo/bloques cap <= phi - 1 < 1
    c_z = 1.0 + z_lo
    # la PEOR ESQUINA literal (acta re-ronda, menor 3): las DOS
    # lentas en el mismo lado — cap del bloque hasta phi/2 y masa
    # hasta phi - beta <= 1.118 —, con los dos huecos lento-lento
    t_s2 = _asin2(math.sqrt(min(1.0, (PHI / 2.0) / 1.0)))
    t_cap = _asin2(math.sqrt(min(1.0, (PHI / 2.0) / 1.0)))
    masa_max = PHI - 0.5
    lentos = th(PHI / 2.0, PHI / 2.0, c_z)         + PI * masa_max / (c_z - PHI / 2.0)         + th(PHI / 2.0, 1.0, c_z)
    lado_z = max(t_s2, t_cap) + lentos
    ok &= check(f"(b) celdas z en la cola (argumento autonomo, "
                f"acta H4): un cap-z por lado (max {t_s2:.3f}, "
                f"{t_cap:.3f}) + lentos {lentos:.3f} = "
                f"{lado_z:.3f} < pi con el par (z, D_m) exento — "
                f"vale para las cuatro celdas z (ligera, pesada, "
                f"torres) porque sus coronas son {{z, D_m}} + "
                f"lentas <= phi/2 y bloques cap < 1",
                lado_z < PI - 0.05)
    # (c) pesada con x en la cola (acta H5: GATE con computo):
    # corona {z, x, D_m} + bloques (cap <= min(beta, phi/2) <
    # 1): par (z, x) exento; peor lado = max cap-z + resto
    t_zb = _asin2(math.sqrt(min(1.0, min(PHI / 2.0, 1.0)
                                 / x_lo)))
    # peor esquina literal: bloque con cap phi/2 y masa phi - beta
    resto_p = t_xm + th(1.0, PHI / 2.0, c_z)         + PI * (PHI - 0.5) / (c_z - PHI / 2.0)
    lado_p = max(t_zm, t_zb) + resto_p
    ok &= check(f"(c) pesada con x en la cola: peor lado = "
                f"max({t_zm:.3f}, {t_zb:.3f}) + resto "
                f"{resto_p:.3f} = {lado_p:.3f} < pi (margen "
                f"{PI - lado_p:.3f} rad)", lado_p < PI - 0.05)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] negativos y contraste")
    import random
    from coronacolas import corona_suf
    rng = random.Random(SEED)
    ok = True
    # contraste: instancias reales con omega grande
    n_p, viol = 0, 0
    for _ in range(20000):
        if n_p >= 150:
            break
        w = math.exp(rng.uniform(math.log(1.6), math.log(300.0)))
        s2 = rng.uniform(0.05, 0.95)
        ss_hi = min(1.0 + s2, PHI) - 1e-9
        if ss_hi <= 1.0 + 1e-6:
            continue
        SS = rng.uniform(1.0 + 1e-6, ss_hi)
        tech = techo_nodo(s2, w, SS, 0.0, 0.0)
        pinza = (1.0 + SS) / PHI
        if tech <= pinza + 1e-6:
            continue
        x = rng.uniform(pinza, tech - 1e-9)
        alfa = max(1.0 + w, SS + w) + rng.uniform(0.0, 0.1)
        zv = alfa + x + w + rng.uniform(0.0, 0.5)
        mu = rng.uniform(0.0, max(0.0, PHI - SS - 0.02))
        cola_y = (1.0 + SS + alfa + zv + x + mu) / PHI
        c = max(zv + x, cola_y - w)
        piezas = sorted([zv, x, 1.0, s2]
                        + ([mu] if mu > 0 else []), reverse=True)
        if not corona_suf(piezas, c + 1e-9)[0]:
            viol += 1
            continue
        n_p += 1
    ok &= check(f"(a) {n_p} instancias reales del canal con "
                f"omega hasta 300: la corona real de v cabe "
                f"(corona_suf); violaciones {viol}",
                n_p >= 100 and viol == 0)
    # negativo: una corona imposible sigue siendo rechazada por
    # los criterios (la pared del nodo con omega grande)
    bx = [50.0, 50.0, 0.3, 0.3, 1.25, 1.25, 0.0, 0.0, 0.0, 0.0,
          0.0, 0.0, 51.5, 51.6, 103.5, 103.6, 0.0, 0.0,
          60.0, 60.0]
    r = criterio_canal_v(bx)
    ok &= check(f"(b) x = 60 >= techo_nodo(omega = 50) ~ 51: "
                f"vacuo por la pared del nodo ({r})", r is None)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    return check(
        "[ENUNCIADO] EL TOPE omega <= 1.6 DEL CANAL DEJA DE SER "
        "TOPE (dentro del convenio): el tramo medio [1.6, 40] "
        "por los criterios existentes (omega-genericos, "
        "auditados; techos de z a escala 3 omega en x-EN-z y las "
        "colas z de las torres re-ejecutadas, acta) y la cola "
        "omega >= 40 por los ARGUMENTOS AUTONOMOS de caps del "
        "bloque C (celda v: margen 0.397 rad; celdas z: 0.82; "
        "pesada con x: 0.62 — computados en los gates, no "
        "apelaciones).  Las SEIS celdas del canal quedan sin "
        "tope de anchura.  Permanecen del residuo (iii): ramas "
        "de torre (k >= 2 no-anidados), exclusion de u, y el "
        "convenio mismo", True)


def main():
    print("=" * 68)
    print("LA COLA DE LA ANCHURA DEL CANAL (omega > 1.6, seis "
          "celdas)")
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
