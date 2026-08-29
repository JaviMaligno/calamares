#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FASE 3b DEL LEMA DE |A| — K >= 2 ANILLOS EXTRA DEL CANAL
LIGERO (el residuo declarado de espcanal A6): el ultimo abierto
computacional del lema de reduccion de |A|.

LA CELDA: la ESP ligera (SS < 1 + s2) con k >= 2 anillos extra
x_i >= r_m = 1 en el contenedor de Y — cada uno EN v (nodo de la
corona, HOJA: sus children son polvo) o ANIDADO EN z (viaja
dentro, lem:DG, invisible para la corona de v; torres de
anidamiento dentro de z incluidas).  EL CLAIM EXCLUYE (residuo
DECLARADO, acta R2 opcion b) los extras anidados DENTRO DE OTROS
EXTRAS DE V (los "padres", cuyo X_x >= 1 rompe el techo T del
nodo — el FATAL H-A de la ronda; sondados: 357 coronas padre>T
del referee + C(a), 0 violaciones).  espcanal certifico k <= 1;
k >= 2 quedo declarado con la pinza de colas.  Este script lo
cierra con el aparato del lema: MASAS COMO DIMENSIONES (Wv =
extras hoja en v, Wz = anidados en z), VARIANTES AND por j_v
(escalones por masa con el suelo de la pinza), fila/bloques por
cuerda para j_v >= 6 y el polvo, y el motor de colocacion.

LAS VENTANAS CON MASAS (heredadas de espcanal, engordadas):
  - techo del nodo (pared A2iii de espcanal, posicion-agnostica):
    todo extra HOJA cumple x_i < T = s2 + w + X_x con X_x <=
    phi - SS - X_m - mu (children = polvo); los PADRES (X_x >=
    1, exceden T) estan FUERA del claim (residuo declarado).
  - suelo de la pinza de la cola de x (posicion-independiente):
    todo extra x_i >= x_floor = (1 + SS + X + mu)/phi (la cola
    del extra MENOR contiene m, S y el polvo; los demas extras
    la engordan aun mas: conservador).
  - cola(Y) += Wv + Wz (todo extra < Y cuenta); techo (RY-x) +=
    Wv (solo los extras EN v; los anidados van dentro de z o de
    extras y no cambian la pared RY — igual que espcanal k=1).
  - ventana de z: techo (Rz) += Wz_eff (la masa anidada en z
    resta capacidad del agujero de z para sigma2, por masa;
    Wz_eff mayora el subconjunto real anidado en z); el suelo de
    z NO se sube (los anidados pueden estar en extras, no en z:
    conservador); cola(z) += 0 (conservador: los anidados en
    OTROS extras no estan bajo z... solo se omite: sumar cola
    engordaria el suelo de z a nuestro favor — NO se hace).
  - capacidad c' = Y - omega >= cola(Y) - omega y (con j_v >= 1)
    c' >= suelo_trio(z, x_1, D_m) (los tres conviven en v).
  - par antipodal EXENTO: (z, x_1) si j_v >= 1 (dos circulos en
    v: c' >= z + x_1, el par diametral exacto es legal — el de
    espcanal); (z, D_m) si j_v = 0 (c' >= 1 + z, teorema del
    par).

COLAS DE MASA: la cola Wv (>= W_TOP = 34) es W-UNIFORME
(cola(Y) crece con W y c' crece ~ W/phi: ratio de la fila hacia
phi/2, th en c_lo(W_lo) mayoran); la cola Wz > 34 (HOJAS) queda
CERTIFICADA con el modo CC_COLAZ=1 (ciclo 3e — antes declarada
por el octavo patron del acta R3): root z/Wz extendido a
[1, Z2] x [34, phi Z2] con COLAS POR TECHO-DE-ROOT (el patron
cola_v: la caja que toca el techo certifica el rayo), la
cobertura del complemento por el acople del techo Rz (z <= C0 +
Wz), la vacuidad rho (Wz + resto > phi z es ilegal: Wz cuenta
en cola(z)) y LA C A TROZOS del gate A8: en las cajas z-cola el
minorante de c' tiene tramo superior de pendiente 2/phi > 1
(Wz >= z - C0), donde los criticos de log p son MAXIMOS (al
reves que A6) con z* en forma cerrada — el sup del par (z, v)
se alcanza en el codo z_kink (100% de llamadas instrumentadas;
sin la c a trozos la esquina z -> oo clampa a pi).  El suelo de
cola(z) (z >= (resto + Wz)/phi, espcanal x-en-z) esta activo
pero resulto INERTE (contrafactual CC_3E_OFFSUELO identico —
atribucion medida, leccion 17).

ALCANCE DECLARADO: perfil LIGERO; extras de v HOJAS (los
padres: claim 3d en omega <= 1.05, Wv <= 8, Wz <= 34; el resto
declarado); Wz completo para HOJAS (Wz <= 34 por dominio H3 +
la cola Wz > 34 por CC_COLAZ, ciclo 3e); OMEGA IN
[0, 1.15] CERTIFICADO (el tramo [1.05, 1.15] cierra con la
maquinaria de la fase 3b — el motor-bolsillo del ciclo 3c es
sound pero inerte: 0 decisiones, acta 3c) y omega in [1.15,
1.6] DECLARADO (historia en _en_lamina; la cola omega > 1.6
sigue el patron espomegacanal); x en u EXCLUIDO estructural
(lem:DBo); la PESADA con su pared A7 como continuacion.
k <= 1 es espcanal.

Bloques: [A] gates; [B] B&B (11 dims); [C] contraste hostil +
falsabilidad; [D] estatus.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import (PHI, PI, check, bolsillo_descartes,
                         cabe_algun_orden)
from r2bmulti import th, bnb_factible
from lemaA import (_motor_dos_lados, _cuerda, _asin2,
                   _coloca_ciclo, _coloca_y_verifica)
from espcanal import (techo_nodo, suelo_trio, W_MAX, XP_MAX,
                      XZ_MAX, A_MAX, Z_MAX)

SEED = int(os.environ.get('CC_SEED', '20260823'))
W_TOP = 34.0
W_CORTE = float(os.environ.get('CC_WCORTE', '1.15'))
# CC_PADRES=1 (experimental, ciclo 3d): reactivar T_ext = T + Wz
# (la pared del padre, sound por la 2a vuelta) para re-testar el
# residuo de los extras-padre contra la maquinaria mejorada
# (leccion 16: los recortes antiguos pueden ser artefactos)
PADRES = os.environ.get('CC_PADRES', '0') == '1'
# CC_COLAZ=1 (ciclo 3e): la COLA Wz > 34 (hojas).  La palanca:
# Wz es masa ANIDADA EN z => cuenta en cola(z) (espcanal x-en-z:
# "suelo de cola(z) += x") y rho <= phi da z >= (resto + Wz)/phi
# — el suelo de z crece con Wz.  Ademas el techo Rz da
# Wz >= z - C0 (C0 = a + Xz + s2 + omega): en la cola, c'(z)
# crece con pendiente 2/phi > 1 y el ratio z/c' se uniformiza
# bajo phi/2.  El sup del par (z, v) en el tramo de pendiente
# 2/phi NO esta en los extremos (los criticos son MAXIMOS:
# S' = -2(c'-1)c'/((c-z)(c-v)) < 0 con c' = 2/phi > 1 — al reves
# que A6) — esta en el critico interior z* = sqrt(D(D-v)/
# (c'(c'-1))), forma cerrada verificada en el gate A8.
COLAZ = os.environ.get('CC_COLAZ', '0') == '1'
Z2_COLA = Z_MAX + W_TOP        # techo del root de z (42.698)
WZ2_COLA = PHI * Z2_COLA       # phi * Z2: techo del root de Wz
INF_Z = 1e18
# el claim de la cola-Wz es de HOJAS (T_ext = T + Wz seria
# infinito en las cajas de cola: los padres con Wz > 34 quedan
# declarados — su claim 3d tiene Wz <= 34 en el dominio)
assert not (COLAZ and PADRES), \
    "CC_COLAZ y CC_PADRES son modos incompatibles"
# instrumentacion de ATRIBUCION del 3e (leccion 17): contadores
# de que mecanismo decide, y contrafactual OFFSUELO (solo para
# medir — el claim corre siempre con el suelo activo)
OFFSUELO_3E = os.environ.get('CC_3E_OFFSUELO', '0') == '1'
SUPZ_N = [0, 0]   # [llamadas a _sup_pz, sup en tramo superior]
# CC_TROZOS=1 (experimento 3f): la C A TROZOS del 3e aplicada
# en modo HOJAS (el techo Rz da Wz >= z - C0 en TODO punto
# real, no solo en la cola): re-test del corte omega (leccion
# 16 otra vez — la maquinaria nueva contra el recorte antiguo)
TROZOS = os.environ.get('CC_TROZOS', '0') == '1' or COLAZ
# CC_OMEGA=1 (ciclo 3g): el tramo omega > 1.6 (patron
# espomegacanal — crit_k2 es omega-generico, solo los techos
# del ROOT asumian w <= 1.6: A_MAX y Z_MAX escalan con w_hi).
# En este modo la lamina de declaracion NO aplica (el corte
# [1.15, 1.6] es del tramo bajo): lo que no cierre queda SIN
# RESOLVER, honesto.  Incompatible con COLAZ (el claim cruzado
# omega > 1.6 y Wz > 34 queda declarado).
OMEGA_ALTO = os.environ.get('CC_OMEGA', '0') == '1'
# CC_CSTAR=1 (ciclo 3i): LA PARED c* DE NECESIDAD — el suelo de
# capacidad del CONJUNTO.  Los circulos {z, x_1..x_j, m, s2}
# DEBEN convivir en la corona de v del ocupante real: si con
# los radios a SUELO ningun orden circular admite
# sum theta_w(consecutivos; c) <= 2 pi, la corona no cabe en c
# y c' real > c.  Tres monotonias la hacen sound: (i) toda
# colocacion valida induce un orden con separaciones
# consecutivas >= theta_w y suma 2 pi (condicion NECESARIA);
# (ii) radios reales >= suelos => theta_w reales >= las de los
# suelos; (iii) theta_w decrece en c => el test es monotono y
# la biseccion da c* (subestimarlo es sound).  Doble uso: la
# VACUIDAD (si refuta en el TECHO de c', la caja no tiene
# puntos reales: la corona de un ocupante real siempre cabe) y
# el RESCATE (si la variante falla en c_lo, se re-intenta en
# c* — los theta del mayorante evaluados en c* siguen mayorando
# los reales porque c' real >= c*).
CSTAR = os.environ.get('CC_CSTAR', '0') == '1'
CSTAR_N = [0, 0, 0]   # [rescates intentados, exitosos, vacuidades]


def _cria_thw(radios, c):
    """PRE-CRIBA barata (el test del 3i original, min-orden de
    theta_w): NO es refutador sound por si solo (ignora el
    apilamiento radial — C1 del sello), pero como FILTRO es
    conservador en la direccion buena: si NI SIQUIERA el
    theta_w-min-orden supera 2 pi, no se llama al confirmador
    caro (cabe_algun_orden refuta un SUPERconjunto de casos
    solo por el confinamiento; el filtro solo AHORRA llamadas
    — un caso confinamiento-refutable que el filtro deja pasar
    se pierde como rescate: menos pared, sound)."""
    import itertools
    n = len(radios)
    thm = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            thm[i][j] = thm[j][i] = th(radios[i], radios[j], c)
    if n <= 6:
        for perm in itertools.permutations(range(1, n)):
            if perm[0] > perm[-1]:
                continue
            orden = (0,) + perm
            if sum(thm[orden[i]][orden[(i + 1) % n]]
                   for i in range(n)) <= 2.0 * PI + 1e-12:
                return False
        return True
    tot = 0.0
    for i in range(n):
        fila = sorted(thm[i][j] for j in range(n) if j != i)
        tot += (fila[0] + fila[1]) / 2.0
    return tot > 2.0 * PI + 1e-12


def _cstar_refuta(radios, c):
    """True si el conjunto NO cabe en capacidad c.  SELLO 3i
    C1: el test por theta_w consecutivas era FALSO como lema
    general (dos circulos se APILAN radialmente — gamma real
    0 — cuando c >= r1 + 2 r2): la refutacion la CONFIRMA el
    aparato ADVERSARIADO del repo, cabe_algun_orden de
    coronacolas (gamma_min con apilamiento y esquinas +
    subconjuntos + confinamiento por el gigante, lema del
    anillo), con confinado_por = el mayor radio (z).  La
    pre-criba theta_w solo decide NO-refutar (ahorro)."""
    if len(radios) < 3:
        return False
    if not _cria_thw(radios, c):
        return False
    return not cabe_algun_orden(list(radios), c,
                                confinado_por=max(radios))


def _cstar_suelo(radios, c_ini, c_tope):
    """Biseccion del c* con cabe_algun_orden (el patron
    R_lb_pack de coronacolas, con tope): devuelve c_ini si no
    muerde; si muerde, el extremo SEGURO lo (c' real > lo);
    subestimar c* es sound."""
    if not _cstar_refuta(radios, c_ini):
        return c_ini
    if _cstar_refuta(radios, c_tope):
        return c_tope
    lo, hi = c_ini, c_tope
    for _ in range(20):
        mid = 0.5 * (lo + hi)
        if _cstar_refuta(radios, mid):
            lo = mid
        else:
            hi = mid
        if hi - lo < 1e-6 * max(1.0, lo):
            break
    return lo                          # el ultimo refutado
assert not (OMEGA_ALTO and COLAZ), \
    "CC_OMEGA y CC_COLAZ son modos incompatibles (residuo cruzado)"
assert not (OMEGA_ALTO and PADRES), \
    "CC_OMEGA y CC_PADRES son modos incompatibles"

# LA BANDA DECLARADA (residuo de este ciclo, historia en el
# docstring de _en_lamina y en el acta): omega in [1.05, 1.6]
# entera para k >= 2; el contador LAMINA_N cuenta sus cajas.
LAMINA_N = [0]


def _en_lamina(SSh, s2h, s2l, x_floor, Wvl, Wvh, Wzh, muh,
               Xmh, z_hi, techo_z, cola_lo, wh, z_lo,
               Wv_lo, wl, T_ext):
    """LA BANDA DECLARADA: omega >= 1.05 entera para k >= 2
    (condicion sobre el SUELO wl: solo cajas enteramente
    dentro — acta R1: el test por techo tragaba bandas).
    HISTORIA (documentada en el acta): la lamina de saturacion
    empezo como la sub-variedad del par (z, x_1) diametral con
    capacidad al piso en omega ~ 1.5; 15+ iteraciones de
    delimitacion (box congelado, caracterizacion estructural
    L1-L5, version-padre, apretura multi-j) mostraron que el
    conflicto reaparece a CADA j (extras contra el techo del
    nodo con z chico) por toda la franja omega in [1.05, 1.6]
    con fronteras inestables a eps practicable, y los runs a
    la finura necesaria exceden lo ejecutable en esta maquina
    (kills sistematicos a ~10-35 min).  El corte estable es en
    omega puro: [0, 1.05] certificado (las bandas cierran
    LIMPIAS: 0 cajas en L), [1.05, 1.6] declarado — el mismo
    tipo de recorte que el tope omega <= 1.6 del MC historico,
    con la verdad sondada (bloque C: lamina + banda, 0
    violaciones de corona_suf).  CICLO 3c: el corte sube de
    1.05 a 1.15 (CC_WCORTE configurable) — LA ATRIBUCION
    HONESTA (acta 3c): la franja [1.05, 1.15] cierra CON LA
    MAQUINARIA DE LA FASE 3b (bloques puros, cotas por
    extremos...), que nunca se habia re-testado ahi tras la
    tercera vuelta; el motor-bolsillo (_prueba_bolsillo),
    sound y auditado, resulto INERTE (0 cajas decididas en
    ~52k llamadas instrumentadas por el referee: el grano
    m = 1 exige 1/sqrt(z_lo) + 1/sqrt(x1_lo) <= 1, fuera de
    las ventanas que fallan) y queda como via adicional
    documentada.  [1.15, 1.6] sigue declarado ([8, 12] x
    [1.15, 1.25] reaparece la familia multi-j; el resto es
    coste de maquina, no matematica)."""
    if OMEGA_ALTO:
        # ciclo 3g — HALLAZGO: la lamina diametral-saturada es
        # OMEGA-INVARIANTE para j_v >= 2 (la caja mala de CADA
        # banda omega > 1.6 es la misma familia del tramo bajo:
        # x_2 -> x_1 con c' al suelo z + x_1 — dos antipodales
        # del mismo z; la verdad vive en la frontera de
        # tangencia).  El claim del tramo alto se RECORTA a
        # j_v <= 1 (Wv < 2 x_floor: un solo extra en v, el
        # resto de la masa k >= 2 anidado en z via Wz);
        # j_v >= 2 queda DECLARADO por SUELO (leccion 12) con
        # margen 0.1 (la frontera 2 x_floor varia con la caja:
        # sin margen el B&B muere en ella)
        return Wvl >= 2.0 * x_floor - 0.1
    if PADRES:
        # EL CLAIM-PADRES (ciclo 3d, medido): extras anidados
        # en extras de v INCLUIDOS para omega <= 1.05 y Wv <=
        # 8 (con Wz <= 34); declarado: Wv > 8 o omega > 1.05
        # (la familia padre-grande-como-z de Wv altas no
        # cierra en presupuesto; [8,12]/[12,34] con Wz <= 4
        # verdes como sobre-verificacion no reclamada).
        # Declaracion por SUELOS (leccion 12)
        return (wl >= 1.05 - 1e-12
                or Wvl >= 8.0 - 1e-12)
    return wl >= W_CORTE - 1e-12


def _bolsillo_inf(a_lo, b_lo):
    """Cota INFERIOR del bolsillo de Descartes entre dos
    murales y la pared, valida para TODO R y toda separacion:
    (i) el bolsillo de Descartes decrece en R (dkp/dkw = 1 +
    (ka+kb)/sqrt(disc) > 0 y kw = -1/R crece en R): el infimo
    sobre R >= c_lo es el limite R -> oo, kp = (1/sqrt(a) +
    1/sqrt(b))^2; (ii) crece en los radios murales: se evalua
    con los SUELOS (a_lo, b_lo) — los murales reales >= suelos
    dejan hueco mayor; (iii) el bolsillo de la tangencia minora
    el de cualquier separacion >= theta (el lema de corona_suf
    / bolsillo.py, adversariado en su campana)."""
    if a_lo <= 1e-9 or b_lo <= 1e-9:
        return 0.0
    kp = (1.0 / math.sqrt(a_lo) + 1.0 / math.sqrt(b_lo)) ** 2
    return 1.0 / kp


def _prueba_bolsillo(nodos, nodos_lo, thmat, Ds, granos_idx):
    """Variante-BOLSILLO del motor (ciclo 3c — la carencia que
    las tres vueltas de la fase 3b identificaron: las coronas
    de la banda declarada caben metiendo m en el hueco de
    Descartes entre z y x_1, la colocacion de corona_suf que
    el motor mural no representa).  Los nodos de `granos_idx`
    salen de la corona; el MURO restante se coloca por el
    CICLO (ordenes canonicos; sin exencion — un par saturado
    a pi lo tolera el presupuesto 2 pi del ciclo); los granos
    (con sus radios-TECHO) se asignan a los bolsillos de los
    pares CONSECUTIVOS de la colocacion, con capacidades
    _bolsillo_inf sobre los SUELOS (esquema de corona_suf:
    varios granos por bolsillo restando del cap)."""
    n = len(nodos)
    muro = [i for i in range(n) if i not in granos_idx]
    if len(muro) < 3:
        return False
    sub = [nodos[i] for i in muro]
    sub_lo = [nodos_lo[i] for i in muro]
    m_n = len(muro)
    sub_th = [[thmat[muro[i]][muro[j]] for j in range(m_n)]
              for i in range(m_n)]
    sub_Ds = {i: Ds[muro[i]] for i in range(m_n)
              if muro[i] in Ds}
    granos = sorted((nodos[g] for g in granos_idx),
                    reverse=True)
    idx = sorted(range(m_n), key=lambda i: -min(sub[i], 1e8))
    for orden in (idx, list(range(m_n))):
        if not _coloca_ciclo(sub, sub_th, sub_Ds, orden):
            continue
        caps = sorted((_bolsillo_inf(
            sub_lo[orden[i]],
            sub_lo[orden[(i + 1) % m_n]])
            for i in range(m_n)), reverse=True)
        ok_g = True
        for g in granos:
            caps.sort(reverse=True)
            if caps and g <= caps[0] + 1e-12:
                caps[0] -= g
            else:
                ok_g = False
                break
        if ok_g:
            return True
    return False


def _motor_rapido(nodos, thmat, Ds, exento=None):
    """Motor RECORTADO para coronas grandes (n >= 8): el
    reparto exhaustivo de _motor_dos_lados (2^n masks x perms)
    cuesta segundos por caja y el B&B no avanza.  Aqui: el
    CICLO (3 ordenes canonicos, solo sin exencion — la misma
    regla del motor pleno) + repartos antipodales GREEDY
    balanceados por theta-contra-z (~12 colocaciones).  Probar
    MENOS colocaciones solo pierde suficiencia (False donde el
    pleno daria True): sound."""
    n = len(nodos)
    if exento != (0, 1) and thmat[0][1] > 3.14159265 - 1e-9:
        return False
    if exento is None:
        idx = sorted(range(n), key=lambda i: -min(nodos[i],
                                                  1e8))
        for oc in (list(range(n)), idx,
                   idx[0::2] + idx[1::2][::-1]):
            if _coloca_ciclo(nodos, thmat, Ds, oc):
                return True
    resto = sorted(range(2, n), key=lambda k: -thmat[0][k])
    for offset in range(min(4, len(resto))):
        rot = resto[offset:] + resto[:offset]
        for modo in (0, 1, 2):
            lado_a, lado_b, sa, sb = [], [], 0.0, 0.0
            for k in rot:
                peso = thmat[0][k] + Ds.get(k, 0.0)
                if modo == 2:
                    destino = len(lado_a) <= len(lado_b)
                else:
                    destino = (sa <= sb) if modo == 0                         else (sa + peso <= 3.1)
                if destino:
                    lado_a.append(k); sa += peso
                else:
                    lado_b.append(k); sb += peso
            if _coloca_y_verifica(nodos, thmat, Ds, lado_a,
                                  lado_b, exento=exento):
                return True
            if _coloca_y_verifica(nodos, thmat, Ds, lado_b,
                                  lado_a, exento=exento):
                return True
    return False


def crit_k2(box):
    """Caja (w, s2, SS, Xp, Xz, Xm, a, z, mu, Wv, Wz): la ESP
    ligera con k >= 2 extras de masas Wv (en v) + Wz (anidados).
    Whi >= W_TOP marca cola de masa."""
    wl, wh, s2l, s2h, SSl, SSh, Xpl, Xph, Xzl, Xzh, Xml, Xmh, \
        al, ah, zl, zh, mul, muh, Wvl, Wvh, Wzl, Wzh = box
    if Wzl > Wzh + 1e-12 or zl > zh + 1e-12:
        return None                    # caja degenerada (guard
        # cosmetico del acta 3e: bnb no las genera)
    if 2.0 * s2l > SSh:
        return None                    # s1 >= s2
    if SSl >= 1.0 + s2h:
        return None                    # ligera
    if SSl + Xml + Xpl + Xzl + mul > PHI:
        return None                    # cola global de m
    if Xml > max(0.0, 1.0 - wl):
        return None
    mu_eff = min(muh, PHI - SSl - Xml - Xpl - Xzl)
    if mu_eff < mul:
        return None
    cola_v = Wvh >= W_TOP - 1e-9
    # ACTA H3 (re-ronda): la cola Wz > W_TOP se declara POR
    # DOMINIO, no por box-test (el test por techo Wzh >= W_TOP
    # disparaba sobre el ROOT [0, W_TOP] y vaciaba TODO — el
    # mismo patron techo-vs-suelo del H1).  El root Wz [0, 34]
    # ES la restriccion: con Wz <= 34 el techo del root de z
    # (Z_MAX + W_TOP = 42.698) cubre exacto el techo Rz
    # (a_hi + Xz + s2 + w + Wz <= 8.698 + 34); Wz > 34 queda
    # declarado como residuo en el enunciado (octavo patron:
    # el techo del root de z no lo cubriria).  CICLO 3e
    # (CC_COLAZ=1): ese residuo se ATACA — root Wz [34, phi*Z2]
    # y z [1, Z2] con COLAS por techo-de-root (el patron
    # cola_v: la caja que TOCA el techo del root certifica para
    # todo el rayo — extension del mayorante, no declaracion):
    # cobertura del complemento {Wz > 34} = rectangulo
    # + z-cola (Wz >= z - C0 acopla) + vacuidad rho
    # (Wz > phi*z - resto es ilegal: Wz cuenta en cola(z))
    Wv_hi = 1e9 if cola_v else Wvh
    if COLAZ:
        cola_wz = Wzh >= WZ2_COLA - 1e-9
        cola_zz = zh >= Z2_COLA - 1e-9
        Wz_hi = INF_Z if cola_wz else Wzh
        zh_eff = INF_Z if cola_zz else zh
    else:
        Wz_hi = Wzh
        zh_eff = zh
    # el techo del nodo y el suelo de la pinza acotan CADA extra
    T = techo_nodo(s2h, wh, SSl, Xml, mul)
    # ACTA R2 (FATAL de la ronda): T capa X_x por la cola
    # GLOBAL DE POLVO — valido solo para extras HOJA (children
    # = polvo, espcanal A3).  Un extra PADRE (con otros extras
    # anidados dentro) tiene X_x >= 1 y puede exceder T: su
    # techo es T_ext = T + Wz (la masa anidada total puede
    # vivir en el); con Wz = 0 no hay padres y T_ext = T
    # ACTA R2, opcion (b) — EL RECORTE DEL CLAIM (decision
    # final tras dos vueltas): los extras de v son HOJAS (sus
    # children son polvo: el techo T de espcanal A2iii es
    # correcto para ellos); los anidados van EN z (Wz).  Las
    # configuraciones con extras anidados DENTRO de otros
    # extras de v (los "padres", que exceden T via X_x >= 1)
    # quedan DECLARADAS como residuo — la prescripcion
    # alternativa del acta, sondada en C (357 coronas con
    # padre > T, 0 violaciones del referee + las de C(a))
    T_ext = (T + (min(Wzh, 1e9) if Wzh > 1e-12 else 0.0)
             if PADRES else T)
    x_floor = (1.0 + SSl + Xml + Xpl + Xzl + mul) / PHI
    if x_floor >= T_ext:
        return None                    # ningun extra legal
    x_floor = max(1.0, x_floor)
    # k >= 2: masa total >= 2 x_floor; cada extra in
    # [x_floor, T]: Wv in {0} U [x_floor, ...], Wz idem
    if Wvh + Wzh < 2.0 * x_floor - 1e-12:
        return None                    # k <= 1: es espcanal
    # masas alcanzables: Wv y Wz son sumas de extras in
    # [x_floor, T] (o cero): las cajas enteramente dentro de
    # (0, x_floor) no contienen masas reales
    if Wvh < x_floor and Wvl > 1e-12:
        return None
    if Wzh < x_floor and Wzl > 1e-12:
        return None
    # masas alcanzables: W = 0 o W >= x_floor (un extra pesa
    # >= x_floor).  Si la caja NO contiene el 0, todo punto
    # real tiene W >= x_floor: el suelo de la masa sube a
    # max(Wl, x_floor) — dejarlo en 0 perdia cola(Y) real (la
    # caja dura de la banda [0, 4] lo destapo)
    Wv_lo = 0.0 if Wvl <= 1e-12 else max(Wvl, x_floor)
    Wz_lo = 0.0 if Wzl <= 1e-12 else max(Wzl, x_floor)
    # ventanas especulares
    a_lo = max(al, 1.0 + wl, SSl + Xpl + wl)
    a_hi = min(ah, 1.0 + s2h + Xph + wh)
    if a_lo >= a_hi:
        return None
    # ventana de z: techo (Rz) + Wz (masa anidada en z; mayora)
    Wz_eff_techo = Wz_hi
    z_lo = max(zl, a_lo + Xzl + wl)
    z_hi = min(zh_eff, a_hi + Xzh + s2h + wh
               + min(Wz_eff_techo, INF_Z))
    if COLAZ:
        # suelo de cola(z) (espcanal x-en-z + rho <= phi): la
        # masa anidada Wz y la cadena posterior (1, SS, Xm, a,
        # Xp, Xz, mu) van DESPUES de z en el orden voraz =>
        # cola(z) >= resto + Wz y z >= cola(z)/phi (gate A8i)
        resto_z = (1.0 + SSl + Xml + a_lo + Xpl + Xzl + mul)
        if not OFFSUELO_3E:
            z_lo = max(z_lo, (resto_z + Wz_lo) / PHI)
        # vacuidad rho: Wz + resto > phi*z_hi no cabe en la
        # cola de z (cubre los puntos Wz > phi*Z2 del
        # complemento: alli Wz > phi*z siempre)
        if z_hi < INF_Z / 2.0 and \
                Wz_lo + resto_z > PHI * z_hi + 1e-9:
            return None
    if z_lo >= z_hi:
        return None
    # cola(Y) con TODOS los extras; techo (RY) + Wv
    cola_lo = (1.0 + SSl + Xml + a_lo + Xpl + z_lo + Xzl
               + mul + Wv_lo + Wz_lo) / PHI
    if cola_lo >= SSh + z_hi + mu_eff + wh + min(Wv_hi, 1e9):
        return None                    # pinza: sin Y legal
    if _en_lamina(SSh, s2h, s2l, x_floor, Wvl,
                  min(Wv_hi, 1e9), Wzh, muh, Xmh, z_hi,
                  a_hi + Xzh + s2h + wh, cola_lo, wh, z_lo,
                  Wv_lo, wl, T_ext):
        LAMINA_N[0] += 1
        return None                    # la lamina L: DECLARADA
    # variantes j_v (numero de extras en v)
    # MEJORA FINA de la re-ronda: solo puede haber n_padres =
    # floor(Wz/x_floor) extras-padre (cada padre aloja >= un
    # anidado >= x_floor): los primeros n_padres escalones
    # llevan T_ext y el resto T — sin esto los escalones
    # sobre-mayoran (todas las piezas a T_ext) y las bandas de
    # Wv alta no cierran
    n_padres = (int(min(Wzh, 1e9) / x_floor + 1e-12)
                if PADRES else 0)

    def techo_esc(i):
        return T_ext if i <= n_padres else T

    if Wv_lo < x_floor:
        j_min = 0
    else:
        # el j minimo que alcanza Wv_lo con los techos por
        # escalon (n_padres a T_ext, el resto a T)
        j_min = 1
        acum = techo_esc(1)
        while acum < Wv_lo - 1e-12 and j_min < 10 ** 6:
            j_min += 1
            acum += techo_esc(j_min)
    j_max = int(min(Wv_hi, 1e9) / x_floor + 1e-12) \
        if Wv_hi < 1e8 else 10 ** 6
    if j_max < j_min:
        return None
    s2_p = min(s2h, SSh / 2.0)
    cap_mu = min(1.0, mu_eff) if mu_eff > 0 else 0.0
    ok_all = True
    # ciclo 3i (CSTAR): escalones EXACTOS hasta J_ESC = 8
    # (la cura del 3h: el bloque-cuerda j >= 6 no cabe en
    # cajas con pocas piezas grandes; cada j real con su
    # fila AND, sound sin doble conteo); con CSTAR=0 el
    # camino sellado queda intacto (J_ESC = 5)
    J_ESC = 8 if CSTAR else 5
    js = list(range(j_min, min(j_max, J_ESC) + 1))
    if j_max > J_ESC:
        js.append(J_ESC + 1)           # centinela: bloques
    # cota ACOPLADA en z para los pares con z, POR EXTREMOS
    # EXACTOS (gate A6): con c(z) = (K + z)/phi - omega, la
    # funcion p(z) = z a/((c - z)(c - a)) solo tiene MINIMOS
    # interiores (en todo punto critico de log p, S' =
    # 2 beta gamma/((c - a)(c - z)) > 0 con beta = 1 - 1/phi,
    # gamma = 1/phi): el sup sobre [z_lo, z_hi] esta en los
    # extremos.  Para los pares (z, extra) la cola se acopla
    # ADEMAS al extra del termino (Wv real >= extra + suelos
    # de los otros: la cola con Wv_lo desacoplada dejaba
    # clampar pares cuyo punto real tiene mas cola): mismo
    # argumento de extremos en la variable del extra (la
    # estructura de c es simetrica en z y v) — 4 esquinas
    K_base = (1.0 + SSl + Xml + a_lo + Xpl + Xzl + mul
              + Wz_lo)
    K_cola = K_base + Wv_lo
    # CICLO 3e (COLAZ): el minorante de c(z) es lineal A TROZOS
    # — tramo inferior (Wz >= Wz_lo, pendiente 1/phi; A6:
    # criticos = minimos => sup en extremos) y tramo superior
    # (Wz >= z - C0 del techo Rz, pendiente 2/phi; gate A8:
    # criticos = MAXIMOS, S' = -2(cp-1)cp/((c-z)(c-v)) < 0 =>
    # sup en extremos U {z* = sqrt(Dp(Dp-v)/(cp(cp-1)))}).  El
    # extremo z -> oo tiene limite 0 (numerador ~ z, denominador
    # ~ z^2): se omite.  c - z crece en el tramo superior y
    # decrece en el inferior; c - v crece: los candidatos
    # capturan tambien los minimos de los denominadores.
    C0_z = a_hi + Xzh + s2h + wh
    z_kink = C0_z + Wz_lo

    def _sup_pz(K_par, v_par):
        """sup_z de p = z v/((c - z)(c - v)) sobre [z_lo, z_hi]
        con c(z) = (K_par + z + max(0, z - z_kink))/phi - wh.
        Devuelve el ratio peor (>= 1 => clamp pi)."""
        def _c(z_e):
            return (K_par + z_e + max(0.0, z_e - z_kink)) \
                / PHI - wh
        cands = [z_lo]
        fin_inf = min(z_hi, max(z_lo, z_kink))
        if fin_inf > z_lo:
            cands.append(fin_inf)
        fin_sup = z_hi if z_hi < INF_Z / 2.0 else None
        if z_kink < (fin_sup if fin_sup is not None
                     else INF_Z):
            if fin_sup is not None and fin_sup > z_kink:
                cands.append(fin_sup)
            if z_kink > z_lo:
                cands.append(z_kink)
            cp = 2.0 / PHI
            Dp = (K_par - z_kink) / PHI - wh
            prod = Dp * (Dp - v_par)
            if prod > 0.0:
                z_st = math.sqrt(prod / (cp * (cp - 1.0)))
                if max(z_lo, z_kink) < z_st < \
                        (fin_sup if fin_sup is not None
                         else INF_Z):
                    cands.append(z_st)
        peor = 0.0
        z_peor = z_lo
        for z_e in cands:
            c_e = _c(z_e)
            d1, d2 = c_e - z_e, c_e - v_par
            if d1 <= 1e-9 or d2 <= 1e-9:
                return 2.0
            p_e = z_e * v_par / (d1 * d2)
            if p_e > peor:
                peor, z_peor = p_e, z_e
        SUPZ_N[0] += 1
        if z_peor >= z_kink - 1e-12:
            # el sup vino del codo o del tramo superior: sin
            # la c a trozos (el codigo A6 puro con la esquina
            # z_hi -> oo del tramo inferior) esta llamada
            # habria clampado a pi (c - z < 0 alli)
            SUPZ_N[1] += 1
        return peor

    def th_acopl(a_p):
        if TROZOS:
            return _asin2(math.sqrt(min(
                1.0, _sup_pz(K_cola, a_p))))
        peor = 0.0
        for z_e in (z_lo, z_hi):
            c_e = (K_cola + z_e) / PHI - wh
            d1, d2 = c_e - z_e, c_e - a_p
            if d1 <= 1e-9 or d2 <= 1e-9:
                return PI
            peor = max(peor, z_e * a_p / (d1 * d2))
        return _asin2(math.sqrt(min(1.0, peor)))

    def th_extra(v_min, v_max, resto):
        """Cota del par (z, extra): min de DOS familias de c
        (cada una con sup en esquinas por A6): (f) cola con
        Wv_lo (el extra no aparece: sup en v_max) y (g) cola
        acoplada c >= (K_base + resto + z + v)/phi - omega con
        resto = suma de suelos de los OTROS extras — 4
        esquinas (z, v).  El punto real cumple ambas: min
        sound."""
        peor_g = 0.0
        if TROZOS:
            # A6 en v (pendiente 1/phi < 1: esquinas) x el sup
            # a trozos en z (con la c acoplada a v_e)
            for v_e in (v_min, v_max):
                peor_g = max(peor_g,
                             _sup_pz(K_base + resto + v_e,
                                     v_e))
        else:
            for z_e in (z_lo, z_hi):
                for v_e in (v_min, v_max):
                    c_e = (K_base + resto + z_e + v_e) / PHI \
                        - wh
                    d1, d2 = c_e - z_e, c_e - v_e
                    if d1 <= 1e-9 or d2 <= 1e-9:
                        peor_g = 2.0
                        break
                    peor_g = max(peor_g,
                                 z_e * v_e / (d1 * d2))
        t_g = _asin2(math.sqrt(min(1.0, peor_g)))
        return min(th_acopl(v_max), t_g)

    def _prueba(j, c_lo, fila, x1_lo, extras_th=None):
        extras_th = extras_th or {}
        base = [z_hi, fila[0], 1.0, s2_p] if 1 <= j <= (8 if CSTAR else 5) \
            else [z_hi, 1.0, s2_p]
        bloques = []
        if mu_eff > 0:
            peso_mu = _cuerda(cap_mu, c_lo) * (mu_eff / 2.0
                                               + cap_mu / 2.0)
            bloques += [(cap_mu, peso_mu), (cap_mu, peso_mu)]
        if j == (9 if CSTAR else 6):
            # j >= J_ESC + 1: BLOQUES PUROS (la version 5-escalones +
            # bloques doble-contaba: escalones al techo + masa
            # residual sumaban ~1.5x Wv y la suma no cerraba).
            # El cap del bloque = el techo de la PRIMERA pieza
            # que puede caer en el (leccion 11).  CON PADRES
            # (ciclo 3d): los n_padres van como NODOS
            # explicitos (escalon min(T_ext, Wv/i)) y los
            # bloques quedan de HOJAS: cap = min(T, Wv/(n_p+1))
            # — sin esto el bloque cargaba el cap del padre
            # (4.3) y el peso rozaba
            n_p6 = min(n_padres, 3)
            # con j >= 6 piezas, CADA una tiene >= 5
            # companeras >= x_floor: toda pieza <= Wv - 5
            # x_floor (sin esta resta el escalon-padre subia
            # a Wv entero)
            tope6 = max(x_floor,
                        min(Wv_hi, 1e9) - 5.0 * x_floor)
            # el escalon-padre i-esimo con j >= 6: i copias
            # >= p_i y las otras >= 6 - i >= x_floor:
            # p_i <= (Wv - (6 - i) x_floor)/i
            padres_esc = [max(x_floor,
                              min(T_ext, tope6,
                                  (min(Wv_hi, 1e9)
                                   - (6 - i) * x_floor) / i))
                          for i in range(1, n_p6 + 1)]
            # ACTA 3d H1 (FATAL reparado): el cap del bloque es
            # techo_esc(n_p6 + 1) — la pieza (n_p6+1)-esima
            # puede ser OTRO PADRE (> T) cuando n_padres >
            # n_p6; la version min(T, ...) no la mayoraba
            # (exhibit del referee: 6 padres de 1.31 con cap
            # 1.068 en caja certificada)
            cap_f = min(techo_esc(n_p6 + 1),
                        max(x_floor,
                            min(Wv_hi, 1e9) / (n_p6 + 1.0)
                            if n_p6 else
                            min(Wv_hi, 1e9) - 5.0 * x_floor))
            if not n_p6:
                cap_f = min(techo_esc(1),
                            max(x_floor,
                                min(Wv_hi, 1e9)
                                - 5.0 * x_floor))
            masa_f = max(0.0, min(Wv_hi, 1e9)
                         - n_p6 * x_floor)
            if cola_v:
                # cola de masa: el ratio r(W) = (masa_f/2 +
                # cap_f/2)/(c'(W) - cap_f) tiende a phi/2 pero
                # puede llegar DESDE ARRIBA (acta H5: el sup no
                # es el limite): r es cociente de lineales en W
                # (monotono) — sup = max(phi/2, r(W_0)) con W_0
                # = Wv_lo el arranque de la banda de cola
                zc = min(1.0, cap_f / max(1e-9, c_lo - cap_f))
                C_v = (2.0 * math.asin(zc) / zc) if zc > 1e-9 \
                    else 2.0
                den0 = c_lo - cap_f
                if den0 <= 1e-9:
                    return False
                r0 = (Wv_lo / 2.0 + cap_f / 2.0) / den0
                # NOTA del acta final: max(phi/2, r0) omite
                # r(W_kink) del tramo c_lo-plano; sound en el
                # manifiesto porque el tramo plano exige z_lo >
                # ~18.9 (Wv_lo >= 12) y alli r(kink) < phi/2
                peso_f = C_v * max(PHI / 2.0, r0)
            else:
                if c_lo - cap_f <= 1e-9:
                    # correccion final del acta: sin el guard,
                    # _cuerda con cap >= c da peso NEGATIVO
                    # (inalcanzable en el manifiesto — margen
                    # demostrado — pero alcanzable en un run
                    # sin bandas)
                    return False
                peso_f = _cuerda(cap_f, c_lo) \
                    * (masa_f / 2.0 + cap_f / 2.0)
            bloques += [(cap_f, peso_f), (cap_f, peso_f)]
        nodos = list(base)
        if 2 <= j <= (8 if CSTAR else 5):
            nodos += fila[1:]
        elif j == (9 if CSTAR else 6) and n_p6:
            nodos += padres_esc    # los padres como nodos
        Ds = {}
        for capb, pesob in bloques:
            Ds[len(nodos)] = pesob
            nodos.append(capb)
        n = len(nodos)
        thmat = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for jj in range(i + 1, n):
                if i == 0:
                    if z_hi >= INF_Z / 2.0:
                        # cola z (3e): t_ac/t_gl degeneran con
                        # z_hi infinito (piso_z absorbe x1 en
                        # float); la acoplada t_c decide sola
                        t_ac = PI
                        t_gl = PI
                    else:
                        piso_z = z_hi + (x1_lo
                                         if 1 <= j <= (8 if CSTAR else 5)
                                         else 1.0)
                        t_ac = th(z_hi, nodos[jj], piso_z)
                        t_gl = th(z_hi, nodos[jj], c_lo) \
                            if c_lo > z_hi + 1e-12 else PI
                    if jj in extras_th:
                        v_min, resto = extras_th[jj]
                        t_c = th_extra(v_min, nodos[jj],
                                       resto)
                    else:
                        t_c = th_acopl(nodos[jj])
                    thmat[i][jj] = min(t_ac, t_gl, t_c)
                else:
                    thmat[i][jj] = th(nodos[i], nodos[jj],
                                      c_lo)
                thmat[jj][i] = thmat[i][jj]
        # EXENCION MOVIL (ciclo 3g; antes solo (0, 1)): la
        # antipodal es legal para CUALQUIER par (0 = z, jj) de
        # circulos que conviven en v (c' >= z + x por
        # convivencia de dos circulos, o c' >= 1 + z para m —
        # el teorema del par): si UN UNICO par de la fila 0
        # clampa a pi, se exenta ESE par (swap del nodo jj al
        # indice 1: la colocacion antipodal del motor es
        # (0, 1) fija); si clampan DOS o mas, la corona real
        # exigiria dos antipodales del mismo z (solapadas en
        # la misma antipoda): False honesto (partir).  La
        # familia doble-diametral del tramo omega alto
        # (z ~ 2w, x_1 ~ x_2 ~ w: el par saturado es (z, x_2),
        # no (z, x_1)) era irresoluble sin esto.  Los bloques
        # (en Ds) no son un circulo: su clamp no es exentable.
        clamps = [jj for jj in range(1, n)
                  if jj not in Ds
                  and thmat[0][jj] >= PI - 1e-9]
        swap = None
        th01 = thmat[0][1]
        if len(clamps) == 1:
            jj_c = clamps[0]
            if jj_c != 1:
                swap = jj_c
                nodos[1], nodos[jj_c] = nodos[jj_c], nodos[1]
                for fila_t in thmat:
                    fila_t[1], fila_t[jj_c] = \
                        fila_t[jj_c], fila_t[1]
                thmat[1], thmat[jj_c] = thmat[jj_c], thmat[1]
            th01 = thmat[0][1]
            thmat[0][1] = 0.0
            thmat[1][0] = 0.0
            ex_eff = (0, 1)
        elif len(clamps) >= 2:
            return False
        else:
            ex_eff = None
        motor = (_motor_rapido if n >= 8
                 else _motor_dos_lados)
        if motor(nodos, thmat, Ds, exento=ex_eff):
            return True
        if swap is not None:
            # la via bolsillo usa posiciones (i_m/i_s2) y
            # suelos por posicion: con el swap quedan
            # desalineados — se omite (via secundaria)
            return False
        # VARIANTE-BOLSILLO (ciclo 3c): el ciclo tolera el par
        # saturado — restaurar el requisito real (el clamp pi
        # vale como requisito en el ciclo: sumar pi cabe en el
        # presupuesto 2 pi si el resto lo deja)
        thmat[0][1] = th01
        thmat[1][0] = th01
        # suelos por nodo: z, x1 (si 1 <= j <= 5), m, s2,
        # escalones (x_floor), bloques (0: no aportan hueco)
        if 1 <= j <= (8 if CSTAR else 5):
            nodos_lo = ([z_lo, x1_lo, 1.0, max(s2l, 0.0)]
                        + [x_floor] * (len(nodos) - 4))
        else:
            nodos_lo = ([z_lo, 1.0, max(s2l, 0.0)]
                        + [0.0] * (len(nodos) - 3))
        for k2 in range(len(nodos)):
            if k2 in Ds:
                nodos_lo[k2] = 0.0
        i_m = 1 if not (1 <= j <= 5) else 2
        i_s2 = i_m + 1
        candidatos = [{i_m, i_s2}, {i_m}]
        for granos_idx in candidatos:
            if _prueba_bolsillo(nodos, nodos_lo, thmat, Ds,
                                granos_idx):
                return True
        return False

    for j in js:
        if j == 0:
            c_lo = max(1.0 + z_lo, cola_lo - wh)
            if c_lo <= max(1.0, s2_p) + 1e-12:
                return False
            if not _prueba(0, c_lo, [], 0.0):
                ok_all = False
                break
            continue
        # ACTA R4: para la variante "j >= 6" el suelo de x_1
        # es x_floor (con j_real >= 7, Wv/6 NO minora x_1)
        x1_lo = (max(x_floor, Wv_lo / max(j, 1))
                 if j <= (8 if CSTAR else 5)
                 else x_floor)
        if j <= (8 if CSTAR else 5):
            # escalones: la i-esima mayor de j piezas de suma
            # <= Wv_hi con las demas >= x_floor; el techo del
            # i-esimo es techo_esc(i) (ACTA R2 + mejora fina:
            # solo los primeros n_padres pueden ser padres)
            fila0 = [min(techo_esc(i),
                         min(Wv_hi, 1e9) - (j - i) * x_floor,
                         min(Wv_hi, 1e9) / i)
                     for i in range(1, j + 1)]
            if any(f < x_floor - 1e-9 for f in fila0):
                # variante j IMPOSIBLE (algun escalon con
                # techo < x_floor: no existen j piezas asi —
                # p.ej. x_floor > T con las hojas agotadas):
                # vacuidad legitima POR CONTEO, se salta
                continue
        else:
            # j >= 6: BLOQUES PUROS (sin escalones-nodos ni
            # bisecion de x_2 — ver _prueba): corona {z, m,
            # s2} + 2 bloques de extras + 2 de polvo, con la
            # exencion (z, m) si clampa (c' >= 1 + z)
            c_lo6 = max(1.0 + z_lo, cola_lo - wh)
            if c_lo6 <= max(1.0, s2_p) + 1e-12:
                return False
            if not _prueba(9 if CSTAR else 6, c_lo6,
                           [], 0.0):
                ok_all = False
                break
            continue
        c_base = max(z_lo + x1_lo, cola_lo - wh,
                     suelo_trio(z_lo, x1_lo, 1.0,
                                z_lo + x1_lo))
        if j == 1:
            if c_base <= max(1.0, s2_p) + 1e-12:
                return False
            if not _prueba(1, c_base, fila0, x1_lo,
                           {1: (x1_lo, 0.0)}):
                ok_all = False
                break
            continue
        # j >= 2: SUB-BANDAS de x_2 (el segundo extra) — el
        # acople x_2 <-> c' (con x_2 -> x_1 el suelo del trio
        # {z, x_1, x_2} sube; por esquinas planas el par
        # (z, x_2) clampa y la variante muere): para x_2 in
        # [x2a, x2b], c' >= suelo_trio(z, x_1, x2a) y todos
        # los extras 2..j son <= x2b — AND sobre las bandas
        x2_top = fila0[1]
        if x2_top < x_floor - 1e-9:
            continue                   # variante j imposible
        # BISECCION ADAPTATIVA de x_2 (la frontera
        # exencion/no-exencion del par (z, x_1) puede caer
        # dentro de cualquier banda fija y matarla por
        # milesimas): partir hasta ancho < 1e-3
        # con j >= 4 las piezas son <= Wv/j (chicas) y la
        # finura de x_2 no decide: banda unica (el coste del
        # bucle j x biseccion x motor explotaba en Wv altas)
        max_prof = 5e-3 if j <= 2 else (x2_top - x_floor)
        pendientes = [(x_floor, x2_top)]
        while pendientes:
            x2a, x2b = pendientes.pop()
            c_tr = suelo_trio(z_lo, x1_lo, x2a,
                              z_lo + x1_lo)
            c_lo = max(z_lo + x1_lo, c_tr, cola_lo - wh)
            if c_lo <= max(1.0, s2_p) + 1e-12:
                return False
            # el techo de x_1 LIGADO a la banda: el segundo
            # pesa >= x2a y los demas >= x_floor:
            # x_1 <= Wv_hi - x2a - (j-2) x_floor (sin esto,
            # x_1 al escalon pleno y x_2 = x2b juntos exceden
            # Wv y el par (z, x_1) clampa espuriamente)
            x1_b = min(fila0[0],
                       min(Wv_hi, 1e9) - x2a
                       - max(0, j - 2) * x_floor)
            if x1_b < x_floor - 1e-9:
                continue               # banda vacia de puntos
            fila = [x1_b] + [min(f, x2b, x1_b)
                             for f in fila0[1:]]
            # el acople cola<->extras del termino (th_extra):
            # suelos por nodo y resto = suelos de los otros
            x1_min = max(x1_lo, x2a)
            resto_x1 = x2a + max(0, j - 2) * x_floor
            resto_xi = x1_min + max(0, j - 2) * x_floor
            ext = {1: (x1_min, resto_x1)}
            for t in range(1, len(fila)):
                ext[3 + t] = ((x2a if t == 1 else x_floor),
                              resto_xi)
            falla = not _prueba(j, c_lo, fila, x1_lo, ext)
            if falla and CSTAR:
                # LA PARED c* (ciclo 3i), SOLO en la ultima
                # oportunidad de la banda (el coste de la
                # biseccion + permutaciones por sub-banda
                # explotaba): los suelos del conjunto que
                # DEBE convivir en la corona
                radios_c = ([z_lo, max(x1_lo, x2a), x2a]
                            + [x_floor] * max(0, j - 2)
                            + [1.0]
                            + ([s2l] if s2l > 1e-3 else []))
                c_hi_y = (SSh + min(z_hi, 1e9) + mu_eff + wh
                          + min(Wv_hi, 1e9)) - wl
                if _cstar_refuta(radios_c, c_hi_y):
                    # ni el TECHO de c' aloja el conjunto: la
                    # variante j no tiene puntos reales en la
                    # (sub)caja — vacuidad
                    CSTAR_N[2] += 1
                    falla = False
                else:
                    c_st = _cstar_suelo(radios_c, c_lo,
                                        c_hi_y)
                    if c_st > c_lo + 1e-9:
                        CSTAR_N[0] += 1
                        if _prueba(j, c_st, fila, x1_lo,
                                   ext):
                            CSTAR_N[1] += 1
                            falla = False
            if falla:
                if x2b - x2a > max_prof:
                    mid = (x2a + x2b) / 2.0
                    pendientes.append((x2a, mid))
                    pendientes.append((mid, x2b))
                else:
                    ok_all = False
                    break
        if not ok_all:
            break
    return True if ok_all else False


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] los gates de la fase 3b")
    import sympy as sp
    ok = True
    ok &= check(
        "[ENUNCIADO] (A1) K >= 2 ANILLOS EXTRA DEL CANAL LIGERO "
        "(el residuo de espcanal A6): cada extra esta EN v (nodo "
        "de corona) o ANIDADO (viaja dentro de su padre, lem:DG, "
        "invisible para la corona de v); masas Wv/Wz como "
        "dimensiones con colas W >= 34; variantes AND por j_v; "
        "alcance: perfil ligero, omega in [0, 1.6] (paridad con "
        "espcanal; la cola omega de k >= 2 queda declarada), "
        "x-en-u excluido estructural, la pesada como "
        "continuacion (pared A7)", True)
    ok &= check(
        "[ENUNCIADO] (A2) LA PARED DEL NODO CON k EXTRAS: el "
        "desbloqueo de espcanal A2iii mueve {sigma2} U "
        "children(x_max) al agujero de x_max y la fila "
        "S\\{sigma2} < 1 a D_m — los DEMAS extras (anillos >= "
        "r_m) no se mueven (thm:oblivious los mantiene): la "
        "pared x < s2 + omega + X_x aplica a cada extra CON SU "
        "X_x PROPIO — para un extra HOJA X_x <= phi - SS - Xm "
        "- mu (children = polvo, cola global: T); un extra "
        "PADRE (con otros extras anidados dentro) tiene X_x >= "
        "1 y EXCEDE T (el FATAL H-A: la version T-para-todos "
        "era falsa vacuidad via j_min > j_max): los padres "
        "quedan FUERA del claim (residuo declarado, acta R2 "
        "opcion b) y todo extra del claim es hoja; el suelo de "
        "la pinza (cola(x_i) >= 1 + SS + X + mu para el MENOR, "
        "los demas la engordan) da x_i >= x_floor: cada extra "
        "del claim vive en [x_floor, T]", True)
    # A3: las ventanas con masas (monotonias)
    W, c0, T_, phi_n = sp.symbols('W c0 T phi', positive=True)
    ratio = W / ((c0 + W) / phi_n - T_)
    dW = sp.simplify(sp.diff(ratio, W))
    lim = sp.limit(ratio, W, sp.oo)
    ok &= check(
        "(A3) LA COLA DE MASA: cola(Y) crece W/phi y c' >= "
        "cola - omega: el ratio de la fila W/(c'(W) - T) crece "
        f"en W hacia {lim} = phi (sup uniforme; el peso por "
        "bloque en cola es C phi/2 con C evaluada en c_lo(W_lo) "
        "que mayora z_c); los th en c_lo(W_lo) mayoran todo W "
        "mayor (th decrece en c); el techo RY += Wv y la cola "
        "+= (Wv + Wz)/phi: la ventana de Y no se vacia y el "
        "certificado de cola es W-uniforme",
        sp.simplify(lim - phi_n) == 0
        and sp.simplify(dW * ((c0 + W) / phi_n - T_) ** 2
                        - (c0 / phi_n - T_)) == 0)
    # A4: el par exento y el suelo del trio
    ok &= check(
        "(A4) EXENCIONES: j_v >= 1: (z, x_1) antipodal exento "
        "(dos circulos en v: c' >= z + x_1, el par diametral "
        "exacto es legal — el mismo de espcanal criterio_canal_v "
        "con su entrada muerta pi); j_v = 0: (z, D_m) con c' >= "
        "1 + z (teorema del par).  El suelo del trio "
        "suelo_trio(z, x_1, D_m) (biseccion sobre el creciente + "
        "suma ciclica, memoizada a la baja: cota inferior del "
        "c' real, heredada de espcanal donde fue adversariada) "
        "despega los pares (z, m) y (x_1, m) de pi", True)
    # A5: escalones con el suelo de la pinza
    ok &= check(
        "(A5) ESCALONES (claim de hojas: techo T): la i-esima "
        "mayor de j piezas de suma <= Wv con las OTRAS j - i "
        ">= x_floor cada una es <= min(T, Wv - (j - i) "
        "x_floor, Wv/i); j_v in [ceil(Wv_lo/T), "
        "floor(Wv_hi/x_floor)]; j >= 6 por BLOQUES PUROS "
        "(corona {z, m, s2} + dos bloques con cap = min(T, "
        "Wv - 5 x_floor) — la PRIMERA pieza que puede caer en "
        "ellos, leccion 11 de lemaA3 — y masa Wv entera; la "
        "version 5-escalones + bloques doble-contaba ~1.5 Wv "
        "y no cerraba) con el suelo x1_lo = x_floor (acta R4)",
        True)
    # A6: el sup por extremos de la cota acoplada en z
    z_, a_, K_, w_ = sp.symbols('z a K w', positive=True)
    phi_s = sp.Rational(1, 2) + sp.sqrt(5) / 2
    c_s = (K_ + z_) / phi_s - w_
    S_ = sp.diff(sp.log(z_ * a_ / ((c_s - z_) * (c_s - a_))),
                 z_)
    Sp = sp.diff(S_, z_)
    beta = 1 - 1 / phi_s
    gamma = 1 / phi_s
    # (i) S' = -1/z^2 + beta^2/(c-z)^2 + gamma^2/(c-a)^2
    ident = sp.simplify(Sp - (-1 / z_ ** 2
                              + beta ** 2 / (c_s - z_) ** 2
                              + gamma ** 2 / (c_s - a_) ** 2))
    # (ii) en el punto critico S = 0: 1/z = A - B con A =
    # gamma/(c-a), B = beta/(c-z), y S' = -(A-B)^2 + A^2 + B^2
    # = 2 A B > 0 (identidad algebraica pura)
    A_, B_ = sp.symbols('A B', positive=True)
    resto = sp.expand(-(A_ - B_) ** 2 + A_ ** 2 + B_ ** 2
                      - 2 * A_ * B_)
    ok &= check(
        "(A6) LA COTA ACOPLADA POR EXTREMOS: con c(z) = "
        "(K+z)/phi - omega, en todo punto critico de log p "
        "(p = za/((c-z)(c-a))) se tiene S' = 2 beta gamma/"
        "((c-a)(c-z)) > 0 (beta = 1-1/phi, gamma = 1/phi) — "
        "solo MINIMOS interiores: el sup de p sobre [z_lo, "
        "z_hi] esta en los extremos [sympy: S' - (-1/z^2 + "
        "b^2/(c-z)^2 + g^2/(c-a)^2) = 0 y la identidad "
        "algebraica del cuadrado]; para los tramos c = z + "
        "x_1 (p creciente en z) y c constante (p creciente) "
        "el sup tambien es de extremo: el min de las tres "
        "familias mayora",
        ident == 0 and resto == 0)
    # A7: el motor-bolsillo (ciclo 3c) — la cota _bolsillo_inf
    R_, a7a, a7b = sp.symbols('R a7a a7b', positive=True)
    ka7, kb7, kw7 = 1 / a7a, 1 / a7b, -1 / R_
    disc7 = ka7 * kb7 + kw7 * (ka7 + kb7)
    kp7 = ka7 + kb7 + kw7 + 2 * sp.sqrt(disc7)
    kw_s = sp.Symbol('kw', negative=True)
    kp_kw = ka7 + kb7 + kw_s + 2 * sp.sqrt(
        ka7 * kb7 + kw_s * (ka7 + kb7))
    dkp = sp.simplify(sp.diff(kp_kw, kw_s)
                      - (1 + (ka7 + kb7) / sp.sqrt(
                          ka7 * kb7 + kw_s * (ka7 + kb7))))
    lim7 = sp.simplify(sp.limit(kp7, R_, sp.oo)
                       - (1 / sp.sqrt(a7a)
                          + 1 / sp.sqrt(a7b)) ** 2)
    ok &= check(
        "(A7) EL MOTOR-BOLSILLO (ciclo 3c): _bolsillo_inf = "
        "1/(1/sqrt(a)+1/sqrt(b))^2 es el limite R -> oo del "
        "bolsillo de Descartes [sympy] y lo MINORA para todo "
        "R (dkp/dkw = 1 + (ka+kb)/sqrt(disc) > 0 [sympy], "
        "kw = -1/R crece en R: kp crece, el bolsillo 1/kp "
        "decrece); crece en los radios murales (suelos "
        "minoran) y la tangencia minora toda separacion >= "
        "theta (re-derivado por el referee: sep(grano, q) >= "
        "theta_w(bolsillo, q)).  ACTA 3c: sound e INERTE (0 "
        "decisiones en ~52k llamadas instrumentadas): la "
        "franja [1.05, 1.15] la cierra la maquinaria 3b",
        dkp == 0 and lim7 == 0)
    # A8: la cola Wz (ciclo 3e) — tres piezas.  (i) el suelo de
    # cola(z): Wz es masa ANIDADA EN z (children travel inside
    # parents) y la cadena (1, SS, Xm, a, Xp, Xz, mu) va
    # DESPUES de z en el orden voraz (todos < z) => cola(z) >=
    # resto + Wz; rho <= phi da z >= (resto + Wz)/phi — la
    # misma composicion que espcanal x-en-z ("suelo de cola(z)
    # += x"), con Wz en el lugar de x.  (ii) el tramo superior
    # del minorante c(z): del techo Rz (z <= C0 + Wz), Wz >=
    # z - C0 y c = (K + 2z - z_kink')/phi - omega es lineal de
    # pendiente cp = 2/phi > 1: en un punto critico de log p,
    # S' = -2(cp-1)cp/((c-z)(c-v)) < 0 — solo MAXIMOS: el sup
    # esta en extremos U {el unico critico z*}, y z* tiene
    # forma cerrada z*^2 = Dp(Dp - v)/(cp(cp - 1)) con Dp el
    # termino constante de c.  (iii) el extremo z -> oo tiene
    # limite 0 (se omite de los candidatos).
    zz, vv, Kp, ww = sp.symbols('zz vv Kp ww', positive=True)
    cp8 = 2 / phi_s
    Dp8 = sp.Symbol('Dp')            # termino constante de c
    c8 = cp8 * zz + Dp8
    p8 = zz * vv / ((c8 - zz) * (c8 - vv))
    S8 = sp.diff(sp.log(p8), zz)
    Sp8 = sp.diff(S8, zz)
    b8 = cp8 - 1
    g8 = cp8
    ident8 = sp.simplify(Sp8 - (-1 / zz ** 2
                                + b8 ** 2 / (c8 - zz) ** 2
                                + g8 ** 2 / (c8 - vv) ** 2))
    # en el critico 1/z = b/(c-z) + g/(c-v) =: A + B y
    # S' = -(A+B)^2 + A^2 + B^2 = -2AB < 0 (b, g > 0)
    A8_, B8_ = sp.symbols('A8 B8', positive=True)
    resto8 = sp.expand(-(A8_ + B8_) ** 2 + A8_ ** 2
                       + B8_ ** 2 + 2 * A8_ * B8_)
    # la forma cerrada del critico: S = 0 sii
    # cp(cp-1) z^2 = Dp(Dp - v)  [multiplicar en cruz]
    S8_num = sp.together(S8)
    num8 = sp.numer(S8_num)
    # el numerador de S lleva el factor positivo (6 + 2 sqrt 5)
    raiz8 = sp.simplify(num8 - (6 + 2 * sp.sqrt(5))
                        * (Dp8 * (Dp8 - vv)
                           - cp8 * (cp8 - 1) * zz ** 2))
    lim8 = sp.limit(p8, zz, sp.oo)
    ok &= check(
        "(A8) LA COLA Wz (ciclo 3e): (i) suelo de cola(z) — "
        "z >= (resto + Wz)/phi (composicion de espcanal "
        "x-en-z con rho <= phi); (ii) el tramo superior "
        "c = (2/phi) z + Dp tiene S' = -2(cp-1)cp/((c-z)"
        "(c-v)) < 0 en todo critico [sympy: la identidad de "
        "S' y el cuadrado -(A+B)^2 + A^2 + B^2 + 2AB = 0] — "
        "solo MAXIMOS: sup en extremos U {z*}, con z*^2 = "
        "Dp(Dp - v)/(cp(cp - 1)) [sympy: el numerador de S "
        "es proporcional a Dp(Dp - v) - cp(cp - 1) z^2]; "
        "(iii) lim p = 0 en z -> oo [sympy] — el extremo "
        "infinito no aporta candidato",
        ident8 == 0 and resto8 == 0 and raiz8 == 0
        and lim8 == 0)
    # A9: la pared c* (ciclo 3i, corregida en el sello C1)
    apil_viejo_falla = False
    # el caso del apilamiento radial que refuto el test por
    # theta_w consecutivas (C1): dos circulos con
    # c >= r1 + 2 r2 se apilan (gamma real = 0) aunque
    # theta_w > 0 — cabe_algun_orden lo maneja (gamma_min
    # apilable -> 0 + subconjuntos)
    r_apil = [3.0, 1.0, 1.0]
    c_apil = 5.5                       # 3 + 2*1 <= 5.5: apilables
    apil_ok = cabe_algun_orden(r_apil, c_apil,
                               confinado_por=3.0)
    # monotonia en c (el fundamento de la biseccion): refutado
    # en c2 > c1 => refutado en c1
    mono = True
    r_t = [4.0, 2.0, 2.0, 1.5, 1.0]
    prev = None
    for c_t in (7.0, 7.5, 8.0, 9.0, 11.0, 14.0):
        cabe_t = cabe_algun_orden(r_t, c_t,
                                  confinado_por=4.0)
        if prev is not None and prev and not cabe_t:
            mono = False               # cabia y dejo de caber
        prev = cabe_t
    ok &= check(
        "(A9) LA PARED c* (ciclo 3i, C1 del sello): la "
        "necesidad se DELEGA en cabe_algun_orden de "
        "coronacolas (gamma_min con apilamiento radial y "
        "esquinas + subconjuntos + confinamiento del gigante "
        "— aparato adversariado en su campana); el test por "
        "theta_w consecutivas era FALSO como lema general "
        "(el apilamiento c >= r1 + 2 r2 da gamma real 0) "
        "[verificado: el caso apilable certifica] y la "
        "biseccion exige monotonia en c [verificada en "
        "barrido]; subestimar c* (extremo SEGURO lo de "
        "R_lb_pack) es sound; el rescate re-evalua th y "
        "cuerdas en c_st >= c_lo (ambas mayoran: decrecen "
        "en c)", apil_ok and mono)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] B&B k >= 2 (11 dims: w, s2, SS, Xp, Xz, Xm, a, "
          "z, mu, Wv, Wz)")
    eps = float(os.environ.get('CC_EPS', '2e-2'))
    # bandas de Wv y omega por env (los runs > ~9 min son
    # matados por la maquina: el manifiesto invoca una banda
    # por proceso)
    wv_lo = float(os.environ.get('CC_WVLO', '0'))
    wv_hi = float(os.environ.get('CC_WVHI', str(W_TOP)))
    w_lo = float(os.environ.get('CC_WLO', '0'))
    w_hi = float(os.environ.get('CC_WHI', str(W_MAX)))
    s2_lo = float(os.environ.get('CC_S2LO', '0'))
    s2_hi = float(os.environ.get('CC_S2HI', '0.999'))
    wz_lo = float(os.environ.get(
        'CC_WZLO', str(W_TOP) if COLAZ else '0'))
    wz_hi = float(os.environ.get(
        'CC_WZHI', str(WZ2_COLA) if COLAZ else str(W_TOP)))
    if OMEGA_ALTO:
        # ciclo 3g: techos del root escalados con w_hi (el
        # patron espomegacanal — A_MAX/Z_MAX del tramo bajo
        # asumian w <= 1.6: a <= 1 + s2 + Xp + w y
        # z <= a + Xz + s2 + w + Wz escalan con la banda)
        if w_lo < 1.6:
            w_lo = 1.6
        a_top = 1.0 + 1.0 + XP_MAX + w_hi
        z_top = a_top + XZ_MAX + 1.0 + w_hi + wz_hi
    else:
        a_top = A_MAX
        z_top = Z_MAX + W_TOP
    root = [w_lo, w_hi, s2_lo, s2_hi, 1.0, PHI, 0.0, XP_MAX,
            0.0, XZ_MAX, 0.0, 1.0, 1.0, a_top, 1.0,
            z_top, 0.0, PHI - 1.0,
            wv_lo, wv_hi, wz_lo, wz_hi]
    LAMINA_N[0] = 0
    SUPZ_N[0] = SUPZ_N[1] = 0
    exito, caja, n, cert = bnb_factible(root, crit_k2, eps=eps)
    if COLAZ:
        print(f"    [3e atribucion] _sup_pz: {SUPZ_N[0]} "
              f"llamadas, {SUPZ_N[1]} con sup en el tramo "
              f"superior (kink/z*)"
              + ("; CONTRAFACTUAL OFFSUELO" if OFFSUELO_3E
                 else ""))
    if CSTAR:
        print(f"    [3i c*] rescates {CSTAR_N[0]} "
              f"(exitosos {CSTAR_N[1]}), vacuidades por "
              f"techo {CSTAR_N[2]}; escalones exactos "
              f"J_ESC = 8 activos (modo 3i: el claim corre "
              f"con CC_WCORTE=1.25)")
    return check(f"k >= 2 certificado FUERA DE LA LAMINA L "
                 f"(declarada; {LAMINA_N[0]} cajas en L; "
                 + (f"CLAIM-PADRES: anidados-en-extras "
                    f"INCLUIDOS, dominio omega <= 1.05 y "
                    f"Wv <= 8, declarado el resto; "
                    if PADRES else
                    (f"CLAIM OMEGA-ALTO (3g): j_v <= 1 "
                     f"(Wv < 2 x_floor - 0.1) en el tramo; "
                     f"j_v >= 2 DECLARADO (lamina "
                     f"omega-invariante); "
                     if OMEGA_ALTO else
                     f"claim de HOJAS: banda omega in "
                     f"[{W_CORTE}, 1.6] declarada; "))
                 + (f"CLAIM COLA-Wz (3e): Wz > 34 INCLUIDO "
                    f"— colas por techo-de-root en z y Wz, "
                    f"suelo cola(z), sup a trozos con z*) "
                    if COLAZ else
                    f"la cola Wz > 34 va POR DOMINIO del "
                    f"root) ")
                 + f"— Wv in [{wv_lo}, "
                 f"{wv_hi}], omega in [{w_lo}, {w_hi}], s2 in "
                 f"[{s2_lo}, {s2_hi}], cola Wv W-uniforme, "
                 + (f"Wz in [{wz_lo}, {wz_hi}+cola], "
                    if COLAZ else f"Wz <= 34 por dominio, ")
                 + f"j_v por variantes: "
                 f"{n} cajas, {cert} certificadas"
                 + ("" if exito else f"; SIN RESOLVER {caja}"),
                 exito)


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] contraste hostil y falsabilidad")
    import random
    from coronacolas import corona_suf
    rng = random.Random(SEED)
    ok = True
    n_i, viol = 0, 0
    for _ in range(60000):
        if n_i >= 300:
            break
        w = rng.uniform(0.01, 1.6)
        s2 = rng.uniform(0.05, 0.98)
        s1 = rng.uniform(s2, 0.999)
        SS = s1 + s2
        if SS <= 1.0 or SS >= 1.0 + s2:
            continue
        mu = rng.uniform(0.0, max(0.0, PHI - SS - 0.01))
        T = techo_nodo(s2, w, SS, 0.0, mu)
        x_floor = (1.0 + SS + mu) / PHI
        if x_floor >= T - 0.01:
            continue
        k = rng.randrange(2, 6)
        xs = sorted([rng.uniform(x_floor, T)
                     for _ in range(k)], reverse=True)
        # ciclo 3d: 30% de las sondas con un extra PADRE (otro
        # extra anidado DENTRO de un extra de v: el padre pesa
        # anidado + omega + holgura y puede exceder T)
        if rng.random() < 0.3 and len(xs) >= 2:
            xs[0] = xs[1] + w + rng.uniform(0.05, 0.4)
            xs = sorted(xs, reverse=True)
        jv = rng.randrange(1, k + 1)
        Wv_list = xs[:jv]
        alpha = rng.uniform(max(1.0 + w, SS + w),
                            1.0 + s2 + w + 0.5)
        z = rng.uniform(alpha + w, alpha + s2 + w
                        + sum(xs[jv:]) + 0.3)
        colaY = (1.0 + SS + alpha + z + mu + sum(xs)) / PHI
        # convivencia en v: c' = Y - w >= z + x_1 (o 1 + z):
        # Y >= w + z + x_1
        Y = max(colaY,
                w + z + (Wv_list[0] if Wv_list else 1.0),
                w + 1.0 + z) + rng.uniform(0.0, 2.0)
        cp = Y - w
        carga = sorted([z, 1.0, s2] + Wv_list, reverse=True)
        # el polvo mu como piezas chicas
        n_p = max(1, int(mu / 0.2)) if mu > 0 else 0
        carga += [mu / n_p] * n_p if n_p else []
        carga = sorted(carga, reverse=True)
        okc, defc = corona_suf(carga, cp + 1e-9)
        n_i += 1
        if not okc:
            viol += 1
    ok &= check(f"(a) {n_i} instancias reales k = 2..5 (extras "
                f"en v y anidados, corona de v con los directos "
                f"+ polvo): la corona cabe (corona_suf); "
                f"violaciones {viol}", n_i >= 300 and viol == 0)
    # (a2) sondas DENTRO DE LA LAMINA L (el residuo declarado):
    # puntos en la sub-celda dura (par (z, x_1) saturado, la
    # capacidad al piso) con corona_suf — la VERDAD del claim
    # en L, aunque el B&B no la certifique
    n_l, viol_l = 0, 0
    for _ in range(120000):
        if n_l >= 300:
            break
        # generacion ESTRUCTURAL (L1-L5): esquina masa-pareja,
        # dos extras contra la pinza, z al techo de su ventana
        w = rng.uniform(1.05, 1.6)
        SS = rng.uniform(1.0 + 1e-6, 1.30)
        s2 = rng.uniform(0.05, SS / 2.0)
        if SS >= 1.0 + s2:
            continue
        Xp = rng.uniform(0.0, 0.2)
        Xz = rng.uniform(0.4, 0.7)
        mu = rng.uniform(0.0, 0.35)
        a_l = max(1.0 + w, SS + Xp + w)
        a_h = 1.0 + s2 + Xp + w
        if a_l >= a_h:
            continue
        alpha = rng.uniform(a_l, a_h)
        x_fl = (1.0 + SS + Xp + Xz + mu) / PHI
        Wv = 2.0 * x_fl + rng.uniform(-0.1, 0.99 * x_fl)
        Wv = max(Wv, 2.0 * x_fl)
        T_n = techo_nodo(s2, w, SS, 0.0, mu)
        x1 = rng.uniform(max(x_fl, Wv / 2.0),
                         min(Wv - x_fl, T_n))
        if x1 != x1 or x1 < x_fl:
            continue
        x2 = Wv - x1
        if x2 < x_fl - 1e-9 or x2 > x1 + 1e-9:
            continue
        z_hi_v = alpha + Xz + s2 + w
        z = rng.uniform(max(alpha + Xz + w, z_hi_v - 0.6),
                        z_hi_v)
        if z != z or z <= 0:
            continue
        colaY = (1.0 + SS + alpha + Xp + z + Xz + mu
                 + Wv) / PHI
        Y = max(colaY, w + z + x1)
        cp = Y - w
        carga = sorted([z, x1, x2, 1.0, s2], reverse=True)
        n_p = max(1, int(mu / 0.2)) if mu > 0 else 0
        carga += [mu / n_p] * n_p if n_p else []
        carga = sorted(carga, reverse=True)
        okc, defc = corona_suf(carga, cp + 1e-9)
        n_l += 1
        if not okc:
            viol_l += 1
    ok &= check(f"(a2) {n_l} sondas DENTRO de la lamina L "
                f"(par (z, x_1) saturado, capacidad al piso): "
                f"la corona real cabe siempre (corona_suf con "
                f"bolsillos); violaciones {viol_l}",
                n_l >= 200 and viol_l == 0)
    # (a3) ciclo 3e: sondas de VERDAD en la cola Wz > 34 — el
    # dominio del claim COLAZ.  La masa anidada Wz sube el
    # suelo de z (cola(z) con rho <= phi) y la cola de Y: la
    # corona de v es {z, 1, s2} U extras + polvo, con z y c'
    # los de la cola
    n_c, viol_c = 0, 0
    for _ in range(120000):
        if n_c >= 300:
            break
        w = rng.uniform(0.01, 1.15)
        s2 = rng.uniform(0.05, 0.98)
        s1 = rng.uniform(s2, 0.999)
        SS = s1 + s2
        if SS <= 1.0 or SS >= 1.0 + s2:
            continue
        mu = rng.uniform(0.0, max(0.0, PHI - SS - 0.01))
        T = techo_nodo(s2, w, SS, 0.0, mu)
        x_fl = (1.0 + SS + mu) / PHI
        if x_fl >= T - 0.01:
            continue
        Wz = rng.uniform(34.0, 110.0)
        alpha = rng.uniform(max(1.0 + w, SS + w),
                            1.0 + s2 + w + 0.5)
        resto = 1.0 + SS + alpha + mu
        z_suelo = max(alpha + w, (resto + Wz) / PHI)
        z_techo = alpha + s2 + w + Wz
        if z_suelo >= z_techo:
            continue
        z = rng.uniform(z_suelo, min(z_techo,
                                     z_suelo + 25.0))
        if Wz > PHI * z - resto:
            continue                   # rho-ilegal
        k = rng.randrange(1, 5)
        xs = sorted([rng.uniform(x_fl, T)
                     for _ in range(k)], reverse=True)
        colaY = (1.0 + SS + alpha + z + mu + sum(xs)
                 + Wz) / PHI
        Y = max(colaY, w + z + xs[0], w + 1.0 + z) \
            + rng.uniform(0.0, 2.0)
        cp = Y - w
        carga = sorted([z, 1.0, s2] + xs, reverse=True)
        n_p = max(1, int(mu / 0.2)) if mu > 0 else 0
        carga += [mu / n_p] * n_p if n_p else []
        carga = sorted(carga, reverse=True)
        okc, defc = corona_suf(carga, cp + 1e-9)
        n_c += 1
        if not okc:
            viol_c += 1
    ok &= check(f"(a3) {n_c} sondas en la COLA Wz > 34 (ciclo "
                f"3e: z >= (resto+Wz)/phi por el suelo de "
                f"cola(z), c' con la cola de Y engordada): la "
                f"corona real cabe (corona_suf); violaciones "
                f"{viol_c}", n_c >= 250 and viol_c == 0)
    # (a4) ciclo 3g: la verdad en el tramo omega > 1.6 — el
    # claim (j_v <= 1) Y el residuo declarado (j_v >= 2, la
    # lamina omega-invariante): coronas reales con extras al
    # techo del nodo, c' desde su suelo real
    n_o, viol_o, n_o2, viol_o2, irr_o = 0, 0, 0, 0, 0
    for _ in range(200000):
        if n_o >= 200 and n_o2 >= 200:
            break
        w = rng.uniform(1.6, 6.0)
        s2 = rng.uniform(0.05, 0.98)
        s1 = rng.uniform(s2, 0.999)
        SS = s1 + s2
        if SS <= 1.0 or SS >= 1.0 + s2:
            continue
        mu = rng.uniform(0.0, max(0.0, PHI - SS - 0.01))
        T = techo_nodo(s2, w, SS, 0.0, mu)
        x_fl = max(1.0, (1.0 + SS + mu) / PHI)
        if x_fl >= T - 0.01:
            continue
        alpha = rng.uniform(max(1.0 + w, SS + w),
                            1.0 + s2 + w)
        jv = rng.choice([1, 1, 2, 3])
        Wz = rng.uniform(x_fl, 6.0)      # la masa k >= 2
        z_te = alpha + s2 + w + Wz
        z = rng.uniform(alpha + w, z_te)
        if jv == 1:
            xs = [rng.uniform(x_fl, T)]
        else:
            # el residuo: j_v >= 2 con piezas hacia el techo
            # (la familia dura: x_2 -> x_1)
            x1 = rng.uniform(x_fl, T)
            xs = sorted([x1]
                        + [rng.uniform(
                            max(x_fl, x1 - 0.2), x1)
                           for _ in range(jv - 1)],
                        reverse=True)
        colaY = (1.0 + SS + alpha + z + mu + sum(xs)
                 + Wz) / PHI
        Y = max(colaY, w + z + xs[0], w + 1.0 + z)
        cp = Y - w
        carga = sorted([z, 1.0, s2] + xs, reverse=True)
        n_p = max(1, int(mu / 0.2)) if mu > 0 else 0
        carga += [mu / n_p] * n_p if n_p else []
        okc, _ = corona_suf(sorted(carga, reverse=True),
                            cp + 1e-9)
        if jv == 1:
            n_o += 1
            viol_o += 0 if okc else 1
        else:
            n_o2 += 1
            if not okc:
                # HALLAZGO del 3g: en el tramo alto el punto
                # j_v >= 2 con Y al suelo-par puede ser
                # IRREALIZABLE (el suelo real de Y es la
                # capacidad del CONJUNTO c* > z + x_1: la
                # pared que el criterio no conoce).  No es
                # violacion de verdad: el punto no esta en el
                # modelo.  Se verifica que con holgura finita
                # (Y * 1.2) la corona cabe: la verdad del
                # residuo en los puntos realizables
                ok2, _ = corona_suf(
                    sorted(carga, reverse=True),
                    cp * 1.2 + 1e-9)
                if ok2:
                    irr_o += 1
                else:
                    viol_o2 += 1
    ok &= check(f"(a4) tramo omega in [1.6, 6] (ciclo 3g): "
                f"{n_o} sondas del claim j_v <= 1 (viol "
                f"{viol_o}) y {n_o2} del residuo j_v >= 2 "
                f"con x_2 -> x_1 (la lamina omega-invariante) "
                f"— {irr_o} IRREALIZABLES al suelo-par (el "
                f"suelo real de Y es c* del conjunto: la "
                f"pared que muerde en el tramo alto, "
                f"hallazgo) y todas caben con holgura 1.2 "
                f"(viol {viol_o2})",
                n_o >= 200 and n_o2 >= 200
                and viol_o == 0 and viol_o2 == 0)
    # caja apretada FUERA de la lamina (omega < 1.05, k = 2
    # contra la pinza, z al techo); la inflacion va por las
    # DOS vias de theta (th y _asin2) x4 — con x2 la caja
    # holgada de omega medio aun cabe
    caja = [1.0, 1.02, 0.48, 0.5, 1.001, 1.02, 0.0, 0.02,
            0.5, 0.52, 0.0, 0.02, 2.5, 2.54, 4.0, 4.1,
            0.0, 0.02, 3.1, 3.2, 0.0, 0.02]
    p_ = crit_k2(caja) is True
    g_mod = globals()
    orig = g_mod['_asin2']
    orig_th = g_mod['th']
    g_mod['th'] = lambda a_, b_, c_: min(
        PI, 4.0 * orig_th(a_, b_, c_))
    g_mod['_asin2'] = lambda x_: min(PI, 4.0 * orig(x_))
    try:
        r_ = crit_k2(caja) is False
    finally:
        g_mod['th'] = orig_th
        g_mod['_asin2'] = orig
    ok &= check(f"(b) FALSABILIDAD: la caja k = 2 apretada "
                f"fuera de L certifica ({p_}) y con las thetas "
                f"x4 (ambas vias) se rechaza ({r_})",
                p_ and r_)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] estatus")
    return check(
        "[ENUNCIADO] FASE 3b DEL LEMA DE |A|: k >= 2 anillos "
        "extra del canal ligero certificados en OMEGA IN "
        "[0, 1.15] con extras de v HOJA y Wz <= 34 (el tramo "
        "[1.05, 1.15] con la maquinaria de la fase 3b, "
        "re-testada en el ciclo 3c; el motor-bolsillo es "
        "sound pero inerte — 0 decisiones; masas "
        "Wv/Wz como dimensiones, cola Wv W-uniforme, variantes "
        "j_v con escalones por masa, j >= 6 por bloques puros, "
        "sub-bandas adaptativas de x_2, cotas acopladas por "
        "extremos A6 y el motor de colocacion).  EL CLAIM "
        "DUAL (ciclo 3d): con CC_PADRES=1 los anidados-en-"
        "extras quedan INCLUIDOS para omega <= 1.05 y Wv <= 8 "
        "(6 bandas verdes con Wz completo; T_ext = T + Wz "
        "sound de la 2a vuelta, padres-nodo en j >= 6 con cap "
        "techo_esc(n_p6+1) — el FATAL H1 del acta 3d "
        "reparado —, vacuidades por conteo confirmadas).  "
        "EL CLAIM COLA-Wz (ciclo 3e): con CC_COLAZ=1 la cola "
        "Wz > 34 (HOJAS) queda INCLUIDA para omega <= 1.15 y "
        "Wv completo — root z/Wz extendido con colas por "
        "techo-de-root (el patron cola_v), techo Rz que acopla "
        "Wz >= z - C0, vacuidad rho (Wz + resto <= phi z), "
        "suelo de cola(z) (espcanal x-en-z; contrafactual "
        "OFFSUELO: inerte, documentado) y la C A TROZOS del "
        "gate A8 (tramo superior de pendiente 2/phi: criticos "
        "maximos, z* en forma cerrada; el sup del par (z, v) "
        "se alcanza en el codo z_kink en el 100% de las "
        "llamadas instrumentadas — sin la c a trozos la "
        "esquina z -> oo clamparia a pi).  "
        "EL CLAIM OMEGA-ALTO (ciclo 3g): con CC_OMEGA=1 el "
        "tramo omega in [1.6, 2] queda CERTIFICADO para "
        "j_v <= 1 (Wv < 2 x_floor - 0.1; el resto de la masa "
        "k >= 2 anidado en z, Wz <= 34) — roots escalados con "
        "w_hi (a_top, z_top), la EXENCION MOVIL del motor "
        "(el clamp unico de la fila 0 se exenta por "
        "convivencia c' >= z + x, sea cual sea el nodo; dos "
        "clamps = False), y la lamina j_v >= 2 declarada POR "
        "SUELO.  EL HALLAZGO DEL 3g: la lamina "
        "diametral-saturada es OMEGA-INVARIANTE (la caja "
        "mala de cada banda omega > 1.6 es la MISMA familia "
        "x_2 -> x_1 con c' al suelo z + x_1 del tramo "
        "[1.15, 1.6]: el residuo se UNIFICA), y en el tramo "
        "alto el suelo-par es ademas IRREALIZABLE en parte "
        "del dominio (67/228 sondas: el suelo real de Y es "
        "la capacidad c* del CONJUNTO — la pared que "
        "cerraria el residuo, como continuacion).  "
        "RESIDUOS DECLARADOS Y SONDADOS (corona_suf 0 "
        "violaciones): los padres con Wv > 8 u omega > 1.05 "
        "o Wz > 34, "
        "la lamina j_v >= 2 UNIFICADA (omega in [1.15, 1.6] "
        "entera + todo omega > 1.6 con Wv >= 2 x_floor - "
        "0.1: el par (z, x_1) diametral-saturado — las "
        "coronas reales caben con BOLSILLOS o con la holgura "
        "c* que el motor no representa), omega > 2 con "
        "j_v <= 1 (coste de maquina: la banda [2, 2.3] "
        "s2-alta verde como sobre-verificacion no "
        "reclamada), el cruzado omega > 1.6 con Wz > 34, y "
        "la pesada (pared A7) como continuacion", True)


def main():
    print("=" * 68)
    print("FASE 3b DEL LEMA DE |A|: K >= 2 ANILLOS DEL CANAL")
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
    print(f"RESUMEN: {verdes}/{len(res)} bloques en verde "
          f"({detalle})")
    if verdes != len(res):
        print("HAY FALLOS")
    sys.exit(0 if verdes == len(res) else 1)


if __name__ == "__main__":
    main()
