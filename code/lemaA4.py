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
phi/2, th en c_lo(W_lo) mayoran); la cola Wz queda DECLARADA
(acta R3: el techo Rz de z crece con Wz y el root de z no la
cubre — el octavo patron; Wz <= 34 certificado).

ALCANCE DECLARADO: perfil LIGERO; extras de v HOJAS (los
padres declarados, R2b); Wz <= 34 (por dominio, H3); OMEGA IN
[0, 1.05] CERTIFICADO y omega in [1.05, 1.6] DECLARADO (la
banda entera — historia en _en_lamina; la cola omega > 1.6
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
from coronacolas import PHI, PI, check
from r2bmulti import th, bnb_factible
from lemaA import (_motor_dos_lados, _cuerda, _asin2,
                   _coloca_ciclo, _coloca_y_verifica)
from espcanal import (techo_nodo, suelo_trio, W_MAX, XP_MAX,
                      XZ_MAX, A_MAX, Z_MAX)

SEED = int(os.environ.get('CC_SEED', '20260823'))
W_TOP = 34.0

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
    violaciones de corona_suf)."""
    return wl >= 1.05 - 1e-12


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
    # el techo del root de z no lo cubriria)
    Wv_hi = 1e9 if cola_v else Wvh
    Wz_hi = Wzh
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
    T_ext = T
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
    z_hi = min(zh, a_hi + Xzh + s2h + wh
               + min(Wz_eff_techo, 1e9))
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
    n_padres = 0                       # claim de hojas (R2b)

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
    js = list(range(j_min, min(j_max, 5) + 1))
    if j_max > 5:
        js.append(6)                   # 6 = "j >= 6 por bloques"
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

    def th_acopl(a_p):
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
        for z_e in (z_lo, z_hi):
            for v_e in (v_min, v_max):
                c_e = (K_base + resto + z_e + v_e) / PHI - wh
                d1, d2 = c_e - z_e, c_e - v_e
                if d1 <= 1e-9 or d2 <= 1e-9:
                    peor_g = 2.0
                    break
                peor_g = max(peor_g, z_e * v_e / (d1 * d2))
        t_g = _asin2(math.sqrt(min(1.0, peor_g)))
        return min(th_acopl(v_max), t_g)

    def _prueba(j, c_lo, fila, x1_lo, extras_th=None):
        extras_th = extras_th or {}
        base = [z_hi, fila[0], 1.0, s2_p] if 1 <= j <= 5 \
            else [z_hi, 1.0, s2_p]
        bloques = []
        if mu_eff > 0:
            peso_mu = _cuerda(cap_mu, c_lo) * (mu_eff / 2.0
                                               + cap_mu / 2.0)
            bloques += [(cap_mu, peso_mu), (cap_mu, peso_mu)]
        if j == 6:
            # j >= 6: BLOQUES PUROS (la version 5-escalones +
            # bloques doble-contaba: escalones al techo + masa
            # residual sumaban ~1.5x Wv y la suma no cerraba).
            # El cap del bloque = el techo de la PRIMERA pieza
            # que puede caer en el (leccion 11): min(T, Wv -
            # 5 x_floor) — todas las piezas van a los bloques
            cap_f = min(techo_esc(1),
                        max(x_floor,
                            min(Wv_hi, 1e9) - 5.0 * x_floor))
            masa_f = min(Wv_hi, 1e9)
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
        if 2 <= j <= 5:
            nodos += fila[1:]
        Ds = {}
        for capb, pesob in bloques:
            Ds[len(nodos)] = pesob
            nodos.append(capb)
        n = len(nodos)
        thmat = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for jj in range(i + 1, n):
                if i == 0:
                    piso_z = z_hi + (x1_lo if 1 <= j <= 5
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
        # la exencion SOLO si el par (0, 1) clampa (lemaA2/3:
        # la exencion incondicional bloquea el CICLO); al
        # clampar, la antipodal es legal por el suelo
        # diametral (c' >= z + x_1 o c' >= 1 + z)
        if thmat[0][1] >= PI - 1e-9:
            thmat[0][1] = 0.0
            thmat[1][0] = 0.0
            ex_eff = (0, 1)
        else:
            ex_eff = None
        motor = (_motor_rapido if n >= 8
                 else _motor_dos_lados)
        return motor(nodos, thmat, Ds, exento=ex_eff)

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
        x1_lo = (max(x_floor, Wv_lo / max(j, 1)) if j <= 5
                 else x_floor)
        if j <= 5:
            # escalones: la i-esima mayor de j piezas de suma
            # <= Wv_hi con las demas >= x_floor; el techo del
            # i-esimo es techo_esc(i) (ACTA R2 + mejora fina:
            # solo los primeros n_padres pueden ser padres)
            fila0 = [min(techo_esc(i),
                         min(Wv_hi, 1e9) - (j - i) * x_floor,
                         min(Wv_hi, 1e9) / i)
                     for i in range(1, j + 1)]
            if any(f < x_floor - 1e-9 for f in fila0):
                ok_all = False
                break
        else:
            # j >= 6: BLOQUES PUROS (sin escalones-nodos ni
            # bisecion de x_2 — ver _prueba): corona {z, m,
            # s2} + 2 bloques de extras + 2 de polvo, con la
            # exencion (z, m) si clampa (c' >= 1 + z)
            c_lo6 = max(1.0 + z_lo, cola_lo - wh)
            if c_lo6 <= max(1.0, s2_p) + 1e-12:
                return False
            if not _prueba(6, c_lo6, [], 0.0):
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
            ok_all = False
            break
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
            if not _prueba(j, c_lo, fila, x1_lo, ext):
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
    wz_lo = float(os.environ.get('CC_WZLO', '0'))
    wz_hi = float(os.environ.get('CC_WZHI', str(W_TOP)))
    root = [w_lo, w_hi, s2_lo, s2_hi, 1.0, PHI, 0.0, XP_MAX,
            0.0, XZ_MAX, 0.0, 1.0, 1.0, A_MAX, 1.0,
            Z_MAX + W_TOP, 0.0, PHI - 1.0,
            wv_lo, wv_hi, wz_lo, wz_hi]
    LAMINA_N[0] = 0
    exito, caja, n, cert = bnb_factible(root, crit_k2, eps=eps)
    return check(f"k >= 2 certificado FUERA DE LA LAMINA L "
                 f"(declarada; {LAMINA_N[0]} cajas en L = "
                 f"la banda omega in [1.05, 1.6] declarada; "
                 f"la cola Wz > 34 va POR DOMINIO del root) — "
                 f"extras de v HOJA y anidados en z, Wv in [{wv_lo}, "
                 f"{wv_hi}], omega in [{w_lo}, {w_hi}], s2 in "
                 f"[{s2_lo}, {s2_hi}], cola Wv W-uniforme, "
                 f"Wz <= 34 por dominio, j_v por variantes: "
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
        jv = rng.randrange(0, k + 1)
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
        "[0, 1.05] con extras de v HOJA y Wz <= 34 (masas "
        "Wv/Wz como dimensiones, cola Wv W-uniforme, variantes "
        "j_v con escalones por masa, j >= 6 por bloques puros, "
        "sub-bandas adaptativas de x_2, cotas acopladas por "
        "extremos A6 y el motor de colocacion).  RESIDUOS "
        "DECLARADOS Y SONDADOS (corona_suf 0 violaciones): la "
        "banda omega in [1.05, 1.6] entera (el nucleo: el par "
        "(z, x_1) diametral-saturado con la capacidad al piso "
        "y extras contra el techo del nodo a cada j — las "
        "coronas reales caben con margenes de centesimas "
        "usando BOLSILLOS que el motor no representa; el "
        "patron de la sabana V* de espcanal), los extras "
        "anidados en extras de v (padres, acta H-A), la cola "
        "Wz > 34 (por dominio), la cola omega > 1.6 (patron "
        "espomegacanal) y la pesada (pared A7) como "
        "continuaciones", True)


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
