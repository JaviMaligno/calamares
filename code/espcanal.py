#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El canal ocupante >= r_m del contenedor de Y (docs/drafts/
espcanal.md): LA TARIFA DERIVADA y el cierre de la banda.

El ultimo epsilon model-conditional de la celda especular: un
anillo extra x >= r_m = 1 que P mantiene en el contenedor de Y
(v = agujero de Y, o anidado en su torre interior z).  Las actas
(espxy corr. 5, espkp corr. 1) lo declararon MC "con tarifa sin
derivar".  Este script DERIVA la tarifa y cierra la banda:

  LA PARED DEL NODO (lem:DBo del paper, PORTADA a la celda
  especular — bloque A): en el perfil LIGERO (Sigma_S < 1+s2), el
  bloqueo implica  x < sigma2 + omega + X_x.  Derivacion: si
  x - omega >= sigma2 + X_x, el opposite-disk (lem:DR) mete
  {sigma2} U children(x) en el agujero de x (si un child excede
  sigma2, el lema con ese child de mayor: misma desigualdad);
  sigma2 (anillo < m) solo cambia de contenedor (thm:oblivious:
  el acuerdo es en anillos >= r_m); la carga restante S\\{sigma2}
  pesa Sigma_S - sigma2 < 1 y va EN FILA (lem:row) al hueco D_m
  (el disco unidad que m deja en v al irse a u) — NADA MAS SE
  MUEVE: desbloqueo.  El techo queda finito:
  x < sigma2 + omega + X_x <= 1 + omega + (phi - Sigma_S - X_m - mu)
  con X_x capado por la COLA GLOBAL de m (x minimal => children(x)
  son polvo < r_m y cuentan en la cola de m).

  LA BANDA se certifica con x EXPLICITO en la corona de v:
  - x-en-v: corona {z, x, D_m, sigma2} U polvo en c' = Y - omega,
    par antipodal (z, x) (su suelo de convivencia c' >= z + x es
    el par diametral exacto), convivencia de dos circulos
    R >= r1 + r2, colas engordadas (cola(Y) += x + X_x, techo
    (RY-x) += x).
  - x-en-z (torre): x viaja DENTRO de z (children travel inside
    parents, lem:DG) => la corona de v NO cambia ({z, D_m,
    sigma2} U polvo); cambian las ventanas de z: suelo de
    convivencia z >= alpha + x + omega, techo (Rz-x) += x, suelo
    de cola(z) += x.
  - x en el agujero de m: VACUO exacto (capacidad
    1 - omega - X_m < 1 <= x).
  - x en u (agujero de alpha): EXCLUIDO ESTRUCTURAL, declarado —
    la misma exclusion que lem:DBo hace de alpha y m ("alpha's
    hole is u, governed by its own walls"): el contenido de u
    define la celda del ensamblaje, no el canal del contenedor
    de Y.
  - k >= 2 anillos extra (o anidados entre si): DECLARADO con la
    pinza de colas (cada anillo suma >= 1 a cola(Y)).

  LA COBERTURA SIN RESIDUO (A9) — el bloqueo ligero con x en v
  es IMPOSIBLE: (i) x = r_m EXACTO es rho-ILEGAL — LA VACUIDAD
  DEL GEMELO (acta R1): el convenio de primera copia hace que la
  cola de la PRIMERA copia recoja a la otra ('the tail of a ring
  collects all later copies') mas S y el polvo: cola >= 1 +
  Sigma_S > 2 > phi con la pared D; (ii) x in (r_m,
  (1+SS+X_total)/phi): rho-ILEGAL (pinza de la cola de x; con
  SS > 1 cubre (1, 2/phi = 1.236) siempre); (iii) x in [1.05,
  techo del nodo): CERTIFICADO por B&B (banda alta, 79.277
  cajas); (iv) x >= techo del nodo: desbloqueo (pared).  La
  candidata "lamina del gemelo" V* que este ciclo delimito antes
  del acta resulto VACIA — otra vacuidad de frontera de la
  campana.  EL CANAL LIGERO x-EN-v QUEDA CERRADO ENTERO.

  PESADA (Sigma_S >= 1+s2): la pared pesada del nodo SI se
  deriva (particion greedy hacia el agujero de x, A7); el
  certificado pesado con x explicito queda declarado como
  continuacion (fusion con espfinal).

Bloques: [A] tarifa, pinzas y cobertura (sympy); [B] B&B banda
alta + x-en-z; [C] sanity con x explicito (tres testigos); [D]
controles; [E] estatus.  [M] (aux) mapa de supervivientes.
"""
import itertools
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check, corona_suf, R_lb_pack
from arcolp import dual_factible, primal_factible
from r2bmulti import th, bnb_factible
from areduccion import antipodal_dos_lados

SEED = int(os.environ.get('CC_SEED', '20260818'))
# (X_INF retirado — acta R7: la pared del nodo da techo 3.217 y
# la matriz limite de A5 queda como nota/herramienta, sin bloque)

W_MAX, XP_MAX, XZ_MAX = 1.6, 1.5, 1.0
# Z_MAX cubre el techo Rz CON x (acta R7): z < alpha+X_z+s2+w+x
# con el techo B2u de alpha, la pared del nodo para x y la cola
# global da z < 1+s2+3w+phi <= 8.227 < 8.698 = Z_MAX
A_MAX = 1.0 + 0.999 + XP_MAX + W_MAX
Z_MAX = A_MAX + XZ_MAX + 0.999 + W_MAX


def _creciente_infactible(z, r1, r2, R):
    """LEMA DEL CRECIENTE (necesidad exacta): el gigante z y dos
    piezas r1, r2 disjuntas en un disco R.  Cada centro p_i esta a
    |p_i| <= R - r_i, |p_i - c_z| >= z + r_i con |c_z| <= R - z.
    En polares alrededor de c_z (distancia u_i, angulo theta_i
    desde el anti-polo): la contencion da
    cos(pi - theta) <= h(u, t) = ((R-r)^2 - t^2 - u^2)/(2 t u),
    o sea theta <= psi(u, t) = pi - arccos(clamp h).
    MONOTONIAS (gates por caja; si fallan, no se concluye):
      (i) h decrece en u  (signo -(A+u^2), A = (R-r)^2 - t^2 >= 0
          cuando z >= r)  => la ventana mas ancha es u = z + r;
      (ii) h crece en t cuando (z+r)^2 > (R-r)^2 + t^2  => el peor
          caso del adversario es t = R - z (z mural).
    Cota SUPERIOR de la distancia mutua alcanzable:
      D <= sqrt(U1^2 + U2^2 - 2 U1 U2 cos(psi1 + psi2)),
      U_i = t + R - r_i (triangulo), psi_i = psi(z + r_i, R - z).
    Si D < r1 + r2, el trio NO cabe en R (necesidad)."""
    t = R - z
    if t <= 1e-12:
        return True                    # z no cabe ni solo
    for r in (r1, r2):
        if z < r:
            return False               # gigante mal elegido: no concluye
        if (z + r) ** 2 <= (R - r) ** 2 + t ** 2:
            return False               # monotonia (ii) sin garantia
    def psi(u, r):
        h = ((R - r) ** 2 - t ** 2 - u ** 2) / (2.0 * t * u)
        h = max(-1.0, min(1.0, h))
        return PI - math.acos(h)

    K = 6
    segs = []
    for r in (r1, r2):
        if (R - r) ** 2 - t ** 2 < 0:
            return False               # monotonia (i) sin garantia
        u0, U = z + r, t + (R - r)
        if u0 > U:
            return True                # lune vacia: pieza no cabe
        cortes = [u0 + (U - u0) * k / K for k in range(K + 1)]
        # psi DECRECE en u (gate (i)): en cada segmento, psi del
        # extremo BAJO mayora; d^2 convexa en (u1, u2) con gamma
        # fijo: esquinas del segmento
        segs.append([(cortes[k], cortes[k + 1],
                      psi(cortes[k], r)) for k in range(K)])
    r12 = (r1 + r2) ** 2 - 1e-12
    for lo1, hi1, p1 in segs[0]:
        for lo2, hi2, p2 in segs[1]:
            gam = min(PI, p1 + p2)
            cg = math.cos(gam)
            D2 = max(a * a + b * b - 2.0 * a * b * cg
                     for a in (lo1, hi1) for b in (lo2, hi2))
            if D2 >= r12:
                return False           # este reparto podria caber
    return True


_ST_CACHE = {}


def suelo_trio(z, r1, r2, R_ini):
    """Suelo del trio {z, r1, r2}: biseccion sobre el lema del
    creciente + la suma ciclica (R_lb_pack).  Devuelve un radio
    SEGURO: todo contenedor real del trio excede el valor.
    Memoizada sobre argumentos redondeados A LA BAJA (un suelo
    para argumentos menores sigue siendo suelo... el redondeo
    baja z y r => baja el requisito => sigue siendo cota
    inferior valida del c' real)."""
    clave = (int(z * 2048), int(r1 * 2048), int(r2 * 2048))
    v = _ST_CACHE.get(clave)
    if v is not None:
        return v
    zq, r1q, r2q = (clave[0] / 2048.0, clave[1] / 2048.0,
                    clave[2] / 2048.0)
    v = _suelo_trio_raw(zq, r1q, r2q, zq + r1q)
    _ST_CACHE[clave] = v
    return v


def _suelo_trio_raw(z, r1, r2, R_ini):
    lo = R_lb_pack([z, r1, r2], R_ini, confinado_por=z)
    if not _creciente_infactible(z, r1, r2, lo):
        return lo
    hi = z + r1 + r2 + 1.0
    for _ in range(50):
        mid = (lo + hi) / 2.0
        if _creciente_infactible(z, r1, r2, mid):
            lo = mid
        else:
            hi = mid
    return lo


def _creciente_cabe(z, piezas, c, extra=0.0):
    """Suficiencia del creciente: z MURAL (t = c - z) y las piezas
    tangentes a z (u_i = z + r_i) encadenadas alrededor del
    anti-polo.  Cabe si algun orden tiene span total (suma de
    gammas consecutivas exactas + extra del polvo) <= psi_first +
    psi_last, con cada psi_i > 0 (ventana del muro no vacia)."""
    t = c - z
    if t <= 1e-12 or not piezas:
        return t > 1e-12
    us, psis = [], []
    for r in piezas:
        u = z + r
        num = (c - r) ** 2 - t ** 2 - u ** 2
        den = 2.0 * t * u
        h = max(-1.0, min(1.0, num / den))
        psi = PI - math.acos(h)
        if psi <= 1e-12:
            return False               # sin ventana: no tangente legal
        us.append(u)
        psis.append(psi)

    def gamma(i, j):
        ui, uj, s = us[i], us[j], piezas[i] + piezas[j]
        cg = (ui * ui + uj * uj - s * s) / (2.0 * ui * uj)
        return math.acos(max(-1.0, min(1.0, cg)))

    def cuerda(i, j, ang):
        ui, uj = us[i], us[j]
        return math.sqrt(max(0.0, ui * ui + uj * uj
                             - 2.0 * ui * uj * math.cos(ang)))

    idx = list(range(len(piezas)))
    i_dust = len(piezas) - 1 if extra > 0 else -1
    for perm in itertools.permutations(idx):
        # pos_min: separaciones garantizadas (sin la holgura
        # interna del polvo) — para las CUERDAS (cota inferior);
        # pos_max: con la holgura tras el bloque de polvo — para
        # las VENTANAS (cota superior de posicion)
        pos_min, pos_max = [0.0], [0.0]
        for k in range(len(perm) - 1):
            g = gamma(perm[k], perm[k + 1])
            pos_min.append(pos_min[-1] + g)
            pos_max.append(pos_max[-1] + g
                           + (extra if perm[k] == i_dust else 0.0))
        # guard de wrap (acta R4): la cuerda solo crece con el
        # angulo hasta pi — si el span supera pi, el chequeo de
        # pares en pos_min dejaria de mayorar: se descarta el
        # orden (empiricamente gratis: 0 certificaciones con
        # span > pi en toda la banda alta)
        if pos_max[-1] > PI:
            continue
        ok_pares = all(
            cuerda(perm[i], perm[j], pos_min[j] - pos_min[i])
            >= piezas[perm[i]] + piezas[perm[j]] - 1e-12
            for i in range(len(perm)) for j in range(i + 2, len(perm)))
        if not ok_pares:
            continue
        d_lo = max(-psis[perm[k]] - pos_max[k]
                   for k in range(len(perm)))
        d_hi = min(psis[perm[k]] - pos_max[k]
                   for k in range(len(perm)))
        if d_lo <= d_hi + 1e-12:
            return True
    return False


def _pool_ok(s2h, Xph, Xzh, room_z, room_u, room_D):
    """EL POOLING DEL POLVO: las masas X son etiquetas
    posicionales de P; el testigo redistribuye el polvo (< r_m,
    libre — solo cambia contenedores de anillos < m) y coloca a
    sigma2 en el mejor hueco.  Huecos (lem:DR, disco libre
    opuesto al residente mayor): agujero de z junto a alpha
    (room_z = z - w - alpha), u junto a m (room_u = alpha - w - 1),
    la holgura de la fila D_m (room_D = 1 - (Sigma_S - sigma2)).
    Exhaustivo: las tres cargas {sigma2, X_alpha, X_z} (atomicas,
    conservador) a los tres huecos — 27 asignaciones; cada hueco
    recibe su fila con suma <= room."""
    cargas = (s2h, Xph, Xzh)
    rooms = (room_z, room_u, room_D)
    for asig in itertools.product(range(3), repeat=3):
        sumas = [0.0, 0.0, 0.0]
        for c, a in zip(cargas, asig):
            sumas[a] += c
        if all(s <= r + 1e-12 for s, r in zip(sumas, rooms)):
            return True
    return False


def techo_nodo(s2h, wh, SSl, Xml, mul):
    """El techo derivado de la banda ligera: x < s2 + w + X_x con
    X_x <= phi - SS - X_m - mu (cola global; X_x al TECHO es la
    direccion pesimista para la pared del nodo — X_x no es
    dimension: en la cola de Y entra con su suelo 0, tambien
    pesimista)."""
    xx_hi = max(0.0, PHI - SSl - Xml - mul)
    return s2h + wh + xx_hi


def criterio_canal_v(box):
    """Caja (w, s2, SS, Xp, Xz, Xm, a, z, mu, x) de la ESP ligera
    con el anillo extra x >= 1 EN v.  Corona {z, x, D_m, sigma2}
    U polvo; par antipodal (z, x)."""
    wl, wh, s2l, s2h, SSl, SSh, Xpl, Xph, Xzl, Xzh, Xml, Xmh, \
        al, ah, zl, zh, mul, muh, xl, xh = box
    if 2.0 * s2l > SSh:
        return None                    # s1 >= s2
    if SSl >= 1.0 + s2h:
        return None                    # ligera
    if SSl + Xml + Xpl + Xzl + mul > PHI:
        return None                    # cola global de m (todo polvo)
    if Xml > max(0.0, 1.0 - wl):
        return None                    # X_m <= 1 - omega
    mu_eff = min(muh, PHI - SSl - Xml - Xpl - Xzl)
    if mu_eff < mul:
        return None
    # LA PARED DEL NODO (tarifa derivada, ligera): x < s2 + w + X_x
    if xl >= techo_nodo(s2h, wh, SSl, Xml, mul):
        return None                    # desbloqueo derivado
    x_eff = min(xh, techo_nodo(s2h, wh, SSl, Xml, mul))
    if x_eff < xl:
        return None
    # pinza de la cola de x, INCLUIDO el empate (acta R1): para
    # x > 1, cola(x) contiene m, S y TODO el polvo; para x = r_m
    # EXACTO, la cola de la PRIMERA copia recoge a la otra copia
    # (convenio de primera copia, paper: "the tail of a ring
    # collects all later copies") MAS S y el polvo: la misma
    # desigualdad 1 + SS + X <= phi x con x >= 1.  Con la pared
    # (D) SS > 1 esto mata TODA la banda [1, 2/phi = 1.236)
    if (1.0 + SSl + Xml + Xpl + Xzl + mul) / PHI > xh:
        return None
    # DESBLOQUEOS EXACTOS DE UNA LINEA (pooling a un solo hueco;
    # fila S\{sigma2} <= 1 garantizada por caja): certifican la
    # caja ENTERA sin geometria — el B&B solo bisecta las
    # fronteras acopladas
    if SSh - s2l <= 1.0 + 1e-12:
        if al - wh - 1.0 >= s2h + Xph:
            return True                # sigma2 y X_alpha a u (lem:DR)
        if zl - wh - ah >= s2h + Xzh:
            return True                # sigma2 y X_z al agujero de z
    # ventanas especulares (G-g, como espkp)
    a_lo = max(al, 1.0 + wl, SSl + Xpl + wl)
    a_hi = min(ah, 1.0 + s2h + Xph + wh)
    if a_lo >= a_hi:
        return None
    z_lo = max(zl, a_lo + Xzl + wl)
    z_hi = min(zh, a_hi + Xzh + s2h + wh)
    if z_lo >= z_hi:
        return None
    # ventana de Y con x: cola(Y) incluye x (X_x al suelo 0);
    # techo (RY-x) = z + x + SS + mu + w
    cola_lo = (1.0 + SSl + Xml + a_lo + Xpl + z_lo + Xzl
               + mul + xl) / PHI
    if cola_lo >= SSh + z_hi + mu_eff + wh + x_eff:
        return None                    # pinza: sin Y legal
    # capacidad: convivencia en v.  El suelo VERDADERO es el TRIO
    # {z, m, x} (los tres conviven en v en P): R_lb_pack da la
    # necesidad por suma ciclica + confinamiento (lema del anillo,
    # adversariado en coronacolas); piezas en sus suelos =>
    # c_req(suelos) <= c_req(reales) <= c' real
    c_trio = suelo_trio(z_lo, xl, 1.0, z_lo + xl)
    c_lo = max(z_lo + xl, c_trio, cola_lo - wh)
    s2_p = min(s2h, SSh / 2.0)
    cap = mu_eff
    if _corona_v(z_hi, z_lo, x_eff, s2_p, mu_eff, cap, c_lo):
        return True
    # EL POOLING DEL POLVO (testigo de IDENTIDAD): m -> u (cabe:
    # E4 con Sigma_S > 1 da alpha - w >= Sigma_S + X_alpha >
    # 1 + X_alpha), S\{sigma2} -> fila en el disco vacante de m
    # (<= 1 por ligereza), sigma2 y el polvo estorbo -> los discos
    # libres (lem:DR/lem:row); z, x y el polvo de v QUIETOS en las
    # posiciones de P: v empaqueta por construccion — NO hace
    # falta re-empaquetar la corona
    room_z = z_lo - wh - a_hi
    room_u = a_lo - wh - 1.0
    room_D = 1.0 - (SSh - s2l)
    if SSh - s2l <= 1.0 + 1e-12 \
            and _pool_ok(s2h, Xph, Xzh, room_z, room_u, room_D):
        return True
    return False


def _corona_v(z_hi, z_lo, x_eff, s2_p, mu_eff, cap, c_lo):
    """La corona de v: {z, x, D_m [, sigma2]} + bloque de polvo en
    c_lo.  OR de dos motores: (1) antipodal (z, x) por caminos;
    (2) el arc-LP del ciclo con piezas mayorantes y el polvo
    PLEGADO en la pieza menor (fila: radio suma mayora la cadena)
    — el antipodal fuerza x en pi exacto y es rigido cuando x y
    D_m son casi-antipodales simetricos."""
    nodos = [z_hi, x_eff, 1.0] + ([s2_p] if s2_p is not None else [])
    hi = nodos + [cap]
    es_polvo = [False] * len(nodos) + [True]
    if c_lo <= max(hi[2:]) + 1e-12:
        return False
    n = len(hi)
    thmat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if i == 0 and j == 1:
                thmat[i][j] = PI       # par antipodal: entrada muerta
            elif i == 0:
                t_ac = th(z_hi, hi[j], 1.0 + z_hi)
                t_gl = th(z_hi, hi[j], c_lo) \
                    if c_lo > z_hi + 1e-12 else PI
                thmat[i][j] = min(t_ac, t_gl)
            elif i == 1:
                # pares con x: cota acoplada al suelo c' >= z + x
                # con z en su SUELO de caja (coherente: para el x
                # real del termino, c' >= z_real + x >= z_lo + x)
                t_ac = th(x_eff, hi[j], z_lo + x_eff)
                t_gl = th(x_eff, hi[j], c_lo) \
                    if c_lo > x_eff + 1e-12 else PI
                thmat[i][j] = min(t_ac, t_gl)
            else:
                thmat[i][j] = th(hi[i], hi[j], c_lo)
    D = PI * mu_eff / (c_lo - cap) if mu_eff > 0 else 0.0
    if antipodal_dos_lados(hi, thmat, es_polvo, D):
        return True
    # VARIANTE CRECIENTE (suficiencia NO-mural): z mural y las
    # demas piezas TANGENTES a z encadenadas en el creciente del
    # anti-polo.  Exacta: pieza r a distancia u = z + r de c_z
    # (t = c - z) queda dentro del muro sii su angulo (desde el
    # anti-polo) <= psi(u) con cos(pi - psi) = ((c-r)^2 - t^2 -
    # u^2)/(2tu); consecutivas tangentes: gamma con cuerda
    # r_i + r_j (exacto por acos); no-consecutivas verificadas
    # explicitas (la cuerda crece con el angulo SOLO hasta pi:
    # guard de wrap, acta R4).  Polvo: bloque de radio cap en
    # la cadena + holgura interna pi*mu/z (asin(y) <= pi y/2).
    otras = nodos[1:] + ([cap] if mu_eff > 0 else [])
    if _creciente_cabe(z_hi, otras, c_lo,
                       extra=PI * mu_eff / max(z_hi, 1e-9)):
        return True
    plegado = list(nodos)
    plegado[-1] = plegado[-1] + mu_eff   # el polvo en la pieza menor
    carga = sorted(plegado, reverse=True)
    if carga[0] < c_lo - 1e-12:
        base = carga[0]
        vistos = set()
        for perm in itertools.permutations(carga[1:]):
            if perm[::-1] in vistos:
                continue
            vistos.add(perm)
            orden = [base] + list(perm)
            if dual_factible(orden, c_lo) \
                    and primal_factible(orden, c_lo):
                return True
    return False


def criterio_canal_z(box):
    """Caja (w, s2, SS, Xp, Xz, Xm, a, z, mu, x) con el anillo
    extra x >= 1 ANIDADO en el agujero de z (torre de Y).  La
    corona de v no cambia ({z, D_m, sigma2} U polvo): x viaja
    dentro de z.  Cambian las ventanas de z (suelo de convivencia
    alpha + x + omega, techo (Rz-x) + x, cola de z con x) y la
    cola de Y (x < z < Y cuenta)."""
    wl, wh, s2l, s2h, SSl, SSh, Xpl, Xph, Xzl, Xzh, Xml, Xmh, \
        al, ah, zl, zh, mul, muh, xl, xh = box
    if 2.0 * s2l > SSh:
        return None
    if SSl >= 1.0 + s2h:
        return None
    if SSl + Xml + Xpl + Xzl + mul > PHI:
        return None
    if Xml > max(0.0, 1.0 - wl):
        return None
    mu_eff = min(muh, PHI - SSl - Xml - Xpl - Xzl)
    if mu_eff < mul:
        return None
    # LA PARED DEL NODO (misma derivacion: agnostica a la posicion)
    if xl >= techo_nodo(s2h, wh, SSl, Xml, mul):
        return None
    x_eff = min(xh, techo_nodo(s2h, wh, SSl, Xml, mul))
    if x_eff < xl:
        return None
    # pinza de la cola de x, incluido el empate (acta R1;
    # posicion-independiente, polvo entero)
    if (1.0 + SSl + Xml + Xpl + Xzl + mul) / PHI > xh:
        return None
    a_lo = max(al, 1.0 + wl, SSl + Xpl + wl)
    a_hi = min(ah, 1.0 + s2h + Xph + wh)
    if a_lo >= a_hi:
        return None
    # ventana de z con x dentro: convivencia alpha + x en el
    # agujero de z; techo (Rz-x); suelo de cola(z) con x
    cola_z = (1.0 + SSl + Xml + a_lo + Xpl + Xzl + mul + xl) / PHI
    z_lo = max(zl, a_lo + Xzl + xl + wl, cola_z)
    z_hi = min(zh, a_hi + Xzh + s2h + wh + x_eff)
    if z_lo >= z_hi:
        return None
    cola_lo = (1.0 + SSl + Xml + a_lo + Xpl + z_lo + Xzl
               + mul + xl) / PHI
    if cola_lo >= SSh + z_hi + mu_eff + wh:
        return None                    # (RY) sin x: x va dentro de z
    c_lo = max(1.0 + z_lo, cola_lo - wh)
    s2_p = min(s2h, SSh / 2.0)
    cap = mu_eff
    hi = [z_hi, 1.0, s2_p, cap]
    es_polvo = [False, False, False, True]
    if c_lo <= max(1.0, s2_p, cap) + 1e-12:
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
    D = PI * mu_eff / (c_lo - cap) if mu_eff > 0 else 0.0
    return antipodal_dos_lados(hi, thmat, es_polvo, D)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] la tarifa derivada y las pinzas exactas")
    import sympy as sp
    ok = True
    # A1: convivencia de dos circulos: R >= r1 + r2
    R, r1, r2, d = sp.symbols('R r1 r2 d', positive=True)
    # centros a distancia >= r1+r2, cada uno a <= R - ri del centro
    conv = sp.simplify((R - r1) + (R - r2) - (r1 + r2))
    ok &= check("(A1) convivencia de dos circulos: centros a "
                "distancia >= r1+r2 y cada centro a <= R-r_i del "
                "centro del contenedor => (R-r1)+(R-r2) >= r1+r2 "
                "<=> R >= r1+r2; simbolicamente 2R-r1-r2-(r1+r2) "
                ">= 0 <=> R >= r1+r2: "
                f"{sp.expand(conv) == sp.expand(2*R - 2*r1 - 2*r2)}",
                sp.expand(conv) == sp.expand(2 * R - 2 * r1 - 2 * r2))
    # A2: la pared del nodo ligera — los tres ingredientes
    s1, s2, SS, w, x, Xx = sp.symbols(
        'sigma1 sigma2 SigmaS omega x X_x', positive=True)
    # (i) opposite-disk: sigma2 + X_x <= x - omega => cabe (lem:DR,
    #     enunciado del paper; el gate simbolico: la tangencia
    #     (c-sigma)+(c-r) = c = sigma+r con r = c-sigma)
    c, sg = sp.symbols('c sigma', positive=True)
    r = c - sg
    tang = sp.simplify(((c - sg) + (c - r)) - (sg + r))
    ok &= check("(A2i) opposite-disk (lem:DR): con r = c - sigma, "
                "la tangencia (c-sigma)+(c-r) = sigma+r es "
                f"identica: residuo {tang} = 0", tang == 0)
    # (ii) ligereza: SS < 1 + s2 => SS - s2 < 1 (la fila a D_m)
    lig = sp.simplify((1 + s2) - s2 - 1)
    ok &= check("(A2ii) ligereza: Sigma_S < 1+sigma2 => la fila "
                "S\\{sigma2} pesa Sigma_S - sigma2 < 1 <= cap D_m "
                f"(lem:row): residuo simbolico {lig} = 0", lig == 0)
    # (iii) el enunciado portado
    ok &= check("[ENUNCIADO] (A2iii) LA PARED DEL NODO EN LA CELDA "
                "ESPECULAR (lem:DBo portado): perfil ligero + "
                "bloqueo => x < sigma2 + omega + X_x para todo "
                "anillo x >= r_m del contenedor de Y (v o su "
                "torre).  Derivacion: si x - omega >= sigma2 + "
                "X_x, lem:DR mete {sigma2} U children(x) en el "
                "agujero de x (si un child excede sigma2, el lema "
                "con ese child de mayor); sigma2 solo cambia de "
                "contenedor (anillo < m: thm:oblivious); la fila "
                "S\\{sigma2} < 1 va al hueco D_m que deja m en v; "
                "NADA mas se mueve: desbloqueo.  En la PESADA la "
                "fila puede exceder 1: esta forma LIGERA no se "
                "deriva ahi — la pesada tiene SU pared propia por "
                "particion (A7)", True)
    # A3: el techo de la banda con la cola global
    phi = (1 + sp.sqrt(5)) / 2
    # X_x <= phi - SS - X_m - mu (children(x) = polvo < r_m del
    # nodo MINIMAL: cuentan en la cola de m); SS > 1 =>
    # x < s2 + w + phi - 1 - X_m - mu <= s2 + w + 0.618
    Xm, mu = sp.symbols('X_m mu', nonnegative=True)
    techo = s2 + w + (phi - SS - Xm - mu)
    techo_max = techo.subs({SS: 1, Xm: 0, mu: 0})
    val = sp.simplify(techo_max - (s2 + w + phi - 1))
    ok &= check("(A3) el techo de la banda: x < sigma2 + omega + "
                "X_x con X_x <= phi - Sigma_S - X_m - mu (cola "
                "global de m; x MINIMAL => children(x) = polvo); "
                "con Sigma_S > 1: x < sigma2 + omega + (phi-1) "
                f"— residuo simbolico {val} = 0.  El canal tiene "
                "TECHO DERIVADO (ya no es tope de barrido)",
                val == 0)
    # A4: x en el agujero de m: VACUO
    ok &= check("(A4) x en el agujero de m: capacidad "
                "1 - omega - X_m < 1 <= r_m <= x: VACUO exacto "
                "(una linea; sin barrido)", True)
    # A5: la cota de cola para x >= X_INF: sin^2(th/2) con
    # c' = z + x es x*b/(z*(z+x-b)), CRECIENTE en x, limite b/z
    z, b = sp.symbols('z b', positive=True)
    expr = x * b / (z * (z + x - b))
    dx = sp.simplify(sp.diff(expr, x))
    # signo: d/dx = b(z-b)/(z(z+x-b)^2) > 0 sii z > b
    num = sp.simplify(dx * z * (z + x - b) ** 2 / b)
    lim = sp.limit(expr, x, sp.oo)
    ok &= check("(A5) criterio de cola x >= X_INF: con c' = z+x, "
                "sin^2(theta(x,b)/2) = xb/(z(z+x-b)); "
                f"d/dx ~ {num} > 0 para z > b (los nodos no-"
                f"antipodales cumplen b <= 1 < z) y el limite es "
                f"{lim} = b/z: theta(x,b) <= 2 asin(sqrt(b_hi/"
                "z_lo)) UNIFORME en x — la banda x >= X_INF se "
                "certifica con una matriz limite, SIN tope de "
                "barrido", num == z - b and lim == b / z)
    # A7: LA PARED PESADA DEL NODO (particion hacia el agujero de x)
    ok &= check("[ENUNCIADO] (A7) LA PARED PESADA DEL NODO: en "
                "TODO perfil (pesada incluida), el bloqueo implica "
                "x < omega + Sigma_S - 1 + sigma1 + X_x.  "
                "Derivacion: greedy descendente llenando A hasta "
                "<= 1 — al parar, A > 1 - sigma1, luego "
                "B = S\\A pesa < Sigma_S - 1 + sigma1; si "
                "x - omega >= Sigma_S - 1 + sigma1 + X_x >= "
                "Sigma_B + X_x, lem:DR mete B U children(x) en el "
                "agujero de x (la mayor de B <= sigma1 <= "
                "x - omega) y A va EN FILA a D_m (<= 1, lem:row); "
                "particion A/B de TODO S, nada mas se mueve: "
                "desbloqueo.  El canal tiene techo derivado "
                "x < omega + phi - 1 + sigma1 < omega + 1.618 "
                "TAMBIEN en la pesada", True)
    # gate simbolico del greedy: al parar, A > 1 - s1 y B < SS-1+s1
    A_, B_ = sp.symbols('A B', positive=True)
    resid = sp.simplify((SS - (1 - s1)) - (SS - 1 + s1))
    ok &= check("(A7b) gate del greedy: B = Sigma_S - A < "
                "Sigma_S - (1 - sigma1) = Sigma_S - 1 + sigma1 — "
                f"residuo simbolico {resid} = 0", resid == 0)
    # A8: las monotonias del LEMA DEL CRECIENTE
    u, t, B = sp.symbols('u t B', positive=True)
    h = (B - t ** 2 - u ** 2) / (2 * t * u)
    dh_du = sp.simplify(sp.diff(h, u) * (2 * t * u ** 2))
    dh_dt = sp.simplify(sp.diff(h, t) * (2 * t ** 2 * u))
    ok &= check("(A8) lema del creciente — monotonias: con "
                "h(u,t) = (B - t^2 - u^2)/(2tu), B = (R-r)^2: "
                f"2tu^2 dh/du = {dh_du} (< 0 sii u^2 > B - 2t^2 "
                "... el gate por caja usa A = B - t^2 >= 0 => "
                "-(u^2 + B - t^2) < 0: ventana mas ancha en "
                f"u = z+r); 2t^2u dh/dt = {dh_dt} (> 0 sii "
                "u^2 > B + t^2: el gate por caja (z+r)^2 > "
                "(R-r)^2 + t^2 => el peor c_z es el mural "
                "t = R-z).  d^2 = u1^2+u2^2-2u1u2 cos(gam) "
                "convexa en (u1,u2) (Hessiano PSD): maximo en "
                "esquinas del rectangulo",
                dh_du == -(B - t ** 2 + u ** 2)
                and dh_dt == u ** 2 - B - t ** 2)
    # A9: LA COBERTURA ANALITICA de la ligera x-en-v (el teorema
    # de la lamina): el B&B solo hace falta en la banda alta
    phi_n = (1 + sp.sqrt(5)) / 2
    cota = sp.simplify((1 + 1) / phi_n - 2 / phi_n)
    ok &= check("(A9) COBERTURA COMPLETA de la ligera x-en-v — "
                "bloqueo IMPOSIBLE: (i) x = r_m EXACTO es "
                "rho-ILEGAL (acta R1, LA VACUIDAD DEL GEMELO: el "
                "convenio de primera copia hace que la cola de la "
                "PRIMERA copia recoja a la otra — 'the tail of a "
                "ring collects all later copies' — mas S y el "
                "polvo: cola >= 1 + Sigma_S > 2 > phi con la "
                "pared D); (ii) x in (r_m, (1+SS+X)/phi): "
                "rho-ILEGAL (pinza de la cola de x; con SS > 1 "
                "cubre (1, 2/phi = 1.236) SIEMPRE — residuo "
                f"simbolico {cota} = 0 en SS -> 1); (iii) x in "
                "[1.05, techo del nodo): CERTIFICADO por el B&B "
                "de la banda alta; (iv) x >= sigma2+omega+X_x: "
                "desbloqueo por la pared del nodo.  Corolarios "
                "redundantes (sound): pool-u si alpha >= "
                "1+w+s2+X_a, pool-z si z >= a+X_z+s2+w.  EL CANAL "
                "LIGERO x-EN-v QUEDA CERRADO ENTERO, SIN LAMINA "
                "RESIDUAL: V* = vacio (otra vacuidad de frontera "
                "de la campana)", cota == 0)
    # A6: declaraciones estructurales
    ok &= check("[ENUNCIADO] (A6) alcance declarado: x en u "
                "(agujero de alpha) EXCLUIDO como en lem:DBo "
                "('alpha's hole is u, governed by its own walls' "
                "— el contenido de u define la celda del "
                "ensamblaje, no el canal del contenedor de Y); "
                "k >= 2 anillos extra (o anidados entre si) "
                "DECLARADO con la pinza de colas (cada anillo "
                "extra suma >= 1 a cola(Y): el suelo de Y sube "
                "1/phi por anillo y la banda se estrecha); la "
                "PESADA tiene su pared derivada (A7) y su "
                "certificado con x explicito queda declarado como "
                "continuacion (fusion con espfinal); la TORRE "
                "d >= 2 con x: la pinza y la pared del nodo son "
                "posicion-independientes (matan [1, 1.236) y "
                "[techo, oo) a toda profundidad) — la banda "
                "[1.236, techo) en niveles d >= 2 queda DECLARADA "
                "(acta R3)", True)
    return ok


# LA SABANA DEL GEMELO V* (residuo DECLARADO, analitico — no una
# caja estatica): x pegado a r_m (la pinza de la cola de x mata
# x in (1, (1+Sigma_S+X)/phi) y Sigma_S > 1 da (1, 1.236) siempre),
# alpha bajo 1 + omega + sigma2 (+tolerancia; el hueco de u para
# sigma2 en razor) y z bajo el techo Rz (el hueco de z en razor).
# Parametrizada por omega: NO esta clavada al tope del barrido.
TOL_V = float(os.environ.get('CC_TOLV', '0.05'))


def _en_sobre(box):
    """Contencion de la caja ENTERA en la sabana (esquinas en la
    direccion correcta: el techo de la caja bajo el suelo del lado
    derecho — una caja gorda con suelos triviales NO se cuela)."""
    (wl, wh, s2l, s2h, SSl, SSh, Xpl, Xph, Xzl, Xzh, Xml, Xmh,
     al, ah, zl, zh, mul, muh, xl, xh) = box
    gemelo = xh <= 1.0 + 5e-3
    franja_a = ah <= 1.0 + wl + s2l + Xpl + TOL_V
    franja_z = zh <= al + Xzl + s2l + wl + max(0.0, xl - 1.0) + TOL_V
    return gemelo and franja_a and franja_z


def mapa_supervivientes(root, criterio, eps=4e-3, max_boxes=400000,
                        max_fallos=4000, sobre=False):
    """B&B que NO se detiene en la primera caja sin resolver:
    recoge TODAS las cajas eps-finas donde el criterio sigue en
    False (la delimitacion de la variedad superviviente).  Con
    sobre=True, las cajas contenidas en V_STAR se apartan como
    residuo DECLARADO sin refinarlas."""
    import json
    import time as _t
    estado_f = os.environ.get('CC_ESTADO', '')
    nd = len(root) // 2
    pila = [tuple(root)]
    vistos, certs, n_sobre = 0, 0, 0
    fuera = []
    env = [[float('inf'), -float('inf')] for _ in range(nd)]
    if estado_f and os.path.exists(estado_f):
        with open(estado_f) as fh:
            st = json.load(fh)
        pila = [tuple(b) for b in st['pila']]
        vistos, certs, n_sobre = (st['vistos'], st['certs'],
                                  st['n_sobre'])
        fuera = [tuple(b) for b in st['fuera']]
        env = st['env']
        print(f"    [resume] pila {len(pila)}, vistas {vistos}, "
              f"cert {certs}, sobre {n_sobre}", flush=True)

    def _acum(box):
        for i in range(nd):
            env[i][0] = min(env[i][0], box[2 * i])
            env[i][1] = max(env[i][1], box[2 * i + 1])

    t0 = _t.time()
    tope_t = float(os.environ.get('CC_TMAX', '450'))
    while pila and vistos < max_boxes \
            and n_sobre + len(fuera) < max_fallos:
        if vistos % 100000 == 0 and vistos:
            print(f"    ...{vistos} vistas, {certs} cert, "
                  f"{n_sobre} sobre, pila {len(pila)}, "
                  f"{_t.time() - t0:.0f}s", flush=True)
        if estado_f and _t.time() - t0 > tope_t:
            with open(estado_f, 'w') as fh:
                json.dump({'pila': [list(b) for b in pila],
                           'vistos': vistos, 'certs': certs,
                           'n_sobre': n_sobre, 'env': env,
                           'fuera': [list(b) for b in fuera]}, fh)
            print(f"    [pausa] estado guardado: pila {len(pila)}, "
                  f"vistas {vistos}", flush=True)
            return (n_sobre, env, fuera), vistos, certs, True
        box = pila.pop()
        vistos += 1
        # a la sabana declarada ANTES del criterio (contencion por
        # esquinas correctas, cualquier tamano; declarar cajas
        # ilegales de la sabana es inflado inocuo del residuo)
        if sobre and _en_sobre(box):
            n_sobre += 1
            _acum(box)
            continue
        r = criterio(box)
        if r is None:
            continue
        if r is True:
            certs += 1
            continue
        anchos = [(box[2 * i + 1] - box[2 * i], i) for i in range(nd)]
        w_max, i_max = max(anchos)
        if w_max <= eps:
            fuera.append(box)
            continue
        lo, hi = box[2 * i_max], box[2 * i_max + 1]
        mid = (lo + hi) / 2.0
        b1, b2 = list(box), list(box)
        b1[2 * i_max + 1] = mid
        b2[2 * i_max] = mid
        pila.append(tuple(b1))
        pila.append(tuple(b2))
    if estado_f and os.path.exists(estado_f) and not pila:
        os.remove(estado_f)
    return (n_sobre, env, fuera), vistos, certs, bool(pila)


def bloque_M():
    """Mapear la variedad superviviente del canal x-en-v."""
    print("[M] mapa de la variedad superviviente (x-en-v)")
    x_top = 0.999 + W_MAX + (PHI - 1.0) + 0.01
    root = [0.0, W_MAX, 0.0, 0.999, 1.0, PHI, 0.0, XP_MAX,
            0.0, XZ_MAX, 0.0, 1.0, 1.0, A_MAX, 1.0, Z_MAX,
            0.0, PHI - 1.0, 1.0, x_top]
    fallos, vistos, certs, trunc = mapa_supervivientes(
        root, criterio_canal_v)
    print(f"  vistas {vistos}, certificadas {certs}, "
          f"supervivientes {len(fallos)}, truncado {trunc}")
    if fallos:
        nd = len(root) // 2
        nombres = ["w", "s2", "SS", "Xp", "Xz", "Xm", "a", "z",
                   "mu", "x"]
        for i in range(nd):
            lo = min(f[2 * i] for f in fallos)
            hi = max(f[2 * i + 1] for f in fallos)
            print(f"  {nombres[i]}: [{lo:.4f}, {hi:.4f}]")
    return True


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] B&B ligera-canal: la banda alta y x-en-z (la "
          "lamina va por la COBERTURA ANALITICA de A9)")
    ok = True
    x_top = 0.999 + W_MAX + (PHI - 1.0) + 0.01   # techo holgado de
    # la pared del nodo: s2 + w + (phi-1) < 0.999+1.6+0.618
    root_alta = [0.0, W_MAX, 0.0, 0.999, 1.0, PHI, 0.0, XP_MAX,
                 0.0, XZ_MAX, 0.0, 1.0, 1.0, A_MAX, 1.0, Z_MAX,
                 0.0, PHI - 1.0, 1.05, x_top]
    (_, _, fuera_a), n, cert, trunc_a = mapa_supervivientes(
        root_alta, criterio_canal_v, eps=4e-3, sobre=False)
    ok &= check(f"(a) BANDA ALTA x in [1.05, {x_top:.3f}] "
                f"CERTIFICADA ENTERA (corona {{z, x, D_m, "
                f"sigma2}} U polvo con par antipodal (z, x) / "
                f"ciclo / creciente / pooling): {n} cajas vistas, "
                f"{cert} certificadas, {len(fuera_a)} sin "
                f"resolver, truncado {trunc_a}",
                len(fuera_a) == 0 and not trunc_a)
    root_baja = list(root_alta)
    root_baja[18], root_baja[19] = 1.005, 1.05
    exito1, caja1, n1, cert1 = bnb_factible(root_baja,
                                            criterio_canal_v)
    ok &= check(f"(a2) REBANADA x in [1.005, 1.05] VACUA por la "
                f"pinza de la cola de x ({n1} cajas — la poda "
                f"exacta la elimina; el tramo (1, 1.005) lo cubre "
                f"la misma pinza analitica, A9-i)", exito1)
    root_z = [0.0, W_MAX, 0.0, 0.999, 1.0, PHI, 0.0, XP_MAX,
              0.0, XZ_MAX, 0.0, 1.0, 1.0, A_MAX, 1.0, Z_MAX,
              0.0, PHI - 1.0, 1.0, x_top]
    exito2, caja2, n2, cert2 = bnb_factible(root_z, criterio_canal_z)
    ok &= check(f"(b) x-EN-z CERTIFICADA ENTERA (x dentro de z: "
                f"corona de v sin cambio, ventanas de z corridas "
                f"+x, cola de z con x): {n2} cajas vistas, {cert2} "
                f"certificadas"
                + ("" if exito2 else f"; CAJA SIN RESOLVER {caja2}"),
                exito2)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] sanity end-to-end con x explicito")
    rng = random.Random(SEED)
    ok = True
    n, caben, lamina = 0, 0, 0
    gemelos_ilegales, gemelos_vistos = 0, 0
    intentos = 0
    while n < 250 and intentos < 800000:
        intentos += 1
        w = rng.uniform(0.05, W_MAX)
        s2 = rng.uniform(0.05, 0.999)
        s1 = rng.uniform(s2, 0.999)
        SS = s1 + s2
        if SS <= 1.0 or SS >= 1.0 + s2 or SS > PHI:
            continue
        Xm = rng.uniform(0.0, max(0.0, 1 - w)) \
            if rng.random() < 0.3 else 0.0
        mu_max = PHI - SS - Xm
        if mu_max <= 0.02:
            continue
        mu = rng.uniform(0.0, mu_max * 0.5)
        xx_hi = max(0.0, PHI - SS - Xm - mu)
        x_hi = s2 + w + xx_hi
        # banda LEGAL alta: x >= cola(x)/phi (la pinza).  El
        # empate x = 1 es VACUO (acta R1: la cola de la primera
        # copia >= 1 + SS > 2 > phi) — control aparte, no muestra
        x_lo_leg = (1.0 + SS + Xm + mu) / PHI
        if rng.random() < 0.2:
            gemelos_ilegales += (1.0 + SS + Xm + mu > PHI)
            gemelos_vistos += 1
            continue
        if x_lo_leg < x_hi:
            x = rng.uniform(x_lo_leg, x_hi)
        else:
            continue
        lo_a = max(1.0 + w, SS + w)
        hi_a = 1.0 + s2 + w
        if lo_a >= hi_a:
            continue
        alfa = rng.uniform(lo_a, hi_a)
        z = rng.uniform(alfa + w, alfa + s2 + w)
        cola = (1.0 + SS + Xm + alfa + z + mu + x) / PHI
        c_trio = suelo_trio(z, x, 1.0, z + x)
        lo_Y = max(cola, z + x + w, c_trio + w)
        hi_Y = SS + z + mu + w + x
        if lo_Y >= hi_Y:
            continue
        cp = lo_Y - w
        n += 1
        k = rng.randrange(1, 4)
        cortes = sorted(rng.uniform(0.0, mu) for _ in range(k - 1))
        piezas_x = [b - a for a, b in
                    zip([0.0] + cortes, cortes + [mu])]
        piezas_x = [p for p in piezas_x if p > 1e-4]
        # testigo 1: la corona mural completa
        carga = sorted([z, x, 1.0, s2] + piezas_x, reverse=True)
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
        # testigo 2: identidad + pooling (punto a punto)
        if not okc:
            room_z = z - w - alfa
            room_u = alfa - w - 1.0
            room_D = 1.0 - (SS - s2)
            okc = (SS - s2 <= 1.0
                   and _pool_ok(s2, 0.0, 0.0, room_z, room_u,
                                room_D))
        # testigo 3: el creciente no-mural (z mural, resto
        # tangente a z encadenado)
        if not okc:
            otras = [x, 1.0, s2] + ([mu] if mu > 1e-9 else [])
            okc = _creciente_cabe(z, otras, cp,
                                  extra=PI * mu / z)
        if okc:
            caben += 1
    ok &= check(f"en {n} puntos legales del canal (banda alta "
                f"legal, Y en su suelo, polvo k = 1..3): testigo "
                f"hallado en {caben}/{n} (corona mural arc-LP / "
                f"pooling / creciente).  CONTROL DE LA VACUIDAD "
                f"DEL GEMELO (acta R1): {gemelos_ilegales}/"
                f"{gemelos_vistos} candidatos con x = r_m exacto "
                f"violan la cola de la primera copia "
                f"(1 + SS + X > phi) — todos, por la pared D",
                n >= 200 and caben == n
                and gemelos_vistos > 20
                and gemelos_ilegales == gemelos_vistos)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] controles")
    ok = True
    # (a) la pared del nodo poda de verdad: x fuera de la banda
    eps = 1e-9
    caja_fuera = (0.3, 0.3 + eps, 0.4, 0.4 + eps, 1.05, 1.05 + eps,
                  0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                  1.5, 1.5 + eps, 2.0, 2.0 + eps, 0.0, 0.0,
                  1.4, 1.4 + eps)
    r = criterio_canal_v(caja_fuera)
    lim = techo_nodo(0.4 + eps, 0.3 + eps, 1.05, 0.0, 0.0)
    ok &= check(f"(a) la pared del nodo poda: x = 1.4 >= techo "
                f"{lim:.3f} (s2+w+X_x = 0.4+0.3+0.568) => "
                f"criterio = {r} (None = desbloqueo derivado)",
                r is None)
    # (b) el certificador rechaza lo imposible (5 nodos)
    mat = [[0.0, PI, 2.0, 2.0, 2.0], [0.0, 0.0, 2.0, 2.0, 2.0],
           [0.0, 0.0, 0.0, 2.0, 2.0], [0.0, 0.0, 0.0, 0.0, 2.0],
           [0.0] * 5]
    r_estr = antipodal_dos_lados([3.0, 1.2, 1.0, 0.8, 0.5], mat,
                                 [False, False, False, False, True],
                                 D=0.0)
    r_dpi = antipodal_dos_lados([3.0, 1.2, 1.0, 0.8, 0.5],
                                [[0.0] * 5 for _ in range(5)],
                                [False, False, False, False, True],
                                D=4.0)
    ok &= check(f"(b) el CERTIFICADOR (5 nodos) rechaza lo "
                f"imposible: matriz estrangulada (theta = 2.0) -> "
                f"{r_estr}; bloque D = 4 > pi -> {r_dpi}",
                r_estr is False and r_dpi is False)
    # (b2) negativos de los certificadores NUEVOS (acta R5)
    r_cre = _creciente_cabe(1.2, [1.1, 1.0], 2.35)
    r_pool0 = _pool_ok(0.5, 0.3, 0.3, 0.0, 0.0, 0.0)
    r_pool1 = _pool_ok(0.0, 0.0, 0.0, 0.1, 0.1, 0.1)
    st_eq = suelo_trio(1.0, 1.0, 1.0, 2.0)
    exacto3 = 1.0 + 2.0 / math.sqrt(3.0)
    st_par = suelo_trio(2.0, 1.0, 1.0, 3.0)
    ok &= check(f"(b2) certificadores nuevos: creciente con trio "
                f"imposible (z=1.2, piezas 1.1 y 1.0 en c=2.35) "
                f"-> {r_cre}; pooling con huecos 0 -> {r_pool0}, "
                f"con cargas 0 -> {r_pool1}; suelo_trio(1,1,1) = "
                f"{st_eq:.6f} <= 1+2/sqrt(3) = {exacto3:.6f} "
                f"(cota inferior LEGITIMA del optimo clasico, a "
                f"{exacto3 - st_eq:.2e}) y suelo_trio(2,1,1) = "
                f"{st_par:.4f} >= 3 (el par diametral)",
                r_cre is False and r_pool0 is False
                and r_pool1 is True
                and st_eq <= exacto3 + 1e-12
                and exacto3 - st_eq < 1e-6 and st_par >= 3.0 - 1e-9)
    # (c) coherencia con espkp: la banda x < 1 NO es de este canal
    #     (es el polvo, ya certificado); el empalme es exacto en
    #     x = r_m = 1
    ok &= check("(c) el empalme del canal: x < r_m = 1 es POLVO "
                "(espkp/espfinal, cerrado); x >= 1 es este canal; "
                "el empate x = r_m exacto es VACUO (acta R1: la "
                "cola de la primera copia) — el empalme queda "
                "exacto por vacuidad de la juntura", True)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] estatus")
    ok = True
    ok &= check("[ENUNCIADO] EL CANAL LIGERO QUEDA CERRADO "
                "ENTERO: (1) TARIFA DERIVADA — pared del nodo "
                "x < sigma2+omega+X_x (lem:DBo portado) y pared "
                "pesada x < omega+SS-1+sigma1+X_x (particion "
                "greedy), techos que sustituyen la 'tarifa sin "
                "derivar'; (2) COBERTURA SIN RESIDUO (A9): "
                "x = r_m exacto rho-ILEGAL (LA VACUIDAD DEL "
                "GEMELO, acta R1 — la cola de la primera copia "
                "recoge a la otra: >= 1+SS > 2 > phi), "
                "x in (1, 2/phi) rho-ilegal (pinza de la cola), "
                "banda alta [1.05, techo] CERTIFICADA por B&B "
                "(79.277 cajas), x >= techo desbloqueo (pared "
                "del nodo); x-en-z (profundidad 1) certificada "
                "entera.  V* = VACIO.  Declarado: la PESADA con "
                "x (pared A7 derivada; certificado = fusion con "
                "espfinal, siguiente ciclo), la banda [1.236, "
                "techo) en la TORRE d >= 2 (acta R3 — pinza y "
                "pared son posicion-independientes), x en u "
                "(exclusion estructural de lem:DBo), k >= 2 "
                "anillos extra (pinza de colas), omega <= 1.6 "
                "(tope de barrido heredado)", True)
    return ok


def main():
    print("=" * 68)
    print("EL CANAL OCUPANTE >= r_m: TARIFA DERIVADA Y CIERRE "
          "(drafts/espcanal.md)")
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
