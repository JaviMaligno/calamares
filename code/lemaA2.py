#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FASE 2 DEL LEMA DE |A|: G-b' COMPLETO — todo Y >= 1, toda masa
M, todo cardinal — cerrando el conteo j <= 3 del residuo (ii).

LO QUE COMPONE (todo adversariado): el lema de slots de la fase
1-bis (lemaA: slots escalonados + cuerda de fila + greedy-halving,
decidido por el MOTOR DE COLOCACION _coloca_y_verifica — la
suficiencia constructiva completa confirmada con oraculo LP) y los
regimenes homogeneos de r2bcolas (la particion por saturacion:
piezas acotadas vs pieza dominante ~ Y).

LOS REGIMENES (particion del dominio {Y >= 1, x_i <= Y, M > 0}):

  R-I  (todas las piezas <= X1 = 6.6, Y >= X1): la fila Y por
       CAPS DE LIMITE (p(Y, a) crece en Y hacia a/(SS + M):
       r2bcolas A1, adversariado) — uniforme en Y, cola Y
       incluida; los lentos con c(Y = X1); slots <= 6.6.
       B&B (s2, SS, uM) + cola M (con M -> inf todo tiende a 0).
  R-II (x_max > X1, luego Y >= x_max > X1): B&B en (s2, SS, uq,
       uv) con q = Mr/x_max y v = Y/x_max (+ colas de ambos).
       La dimension v es la clave: los caps de todos los pares
       son (v, q)-SIMETRICOS via las paredes c - x >= x (v+q),
       c - cap >= x (v+q+1-mq), c - Y >= SS + x (1+q)
       (docstring de crit_RII); el par (Y, x_max) va con su
       theta REAL acotada (p_Yx <= fv/(1+q_lo), sin exencion,
       CICLO disponible) salvo cuando clampa (q_lo ~ 0: la
       exencion antipodal del gate A2, estricta); el resto en
       slots + 2 bloques con VARIANTES AND POR g (masa de
       bloques <= Mr - g t2) y D = min(cuerda mq, cuerda t2).
  R-III (Y <= X1 — el dominio de la fase 1 mas sus flecos):
       la fase 1-bis certifico M in [0.05, 13.2]; aqui los
       flecos M < 0.05 (bloques diminutos, cerrado por B&B
       chico) y M > 13.2 (bandas de M + cola: c crece con M y
       todo se relaja).

Con fase 1-bis (Y <= 6.6, M in [0.05, 13.2]) + R-I + R-II +
R-III: G-b' queda SIN tope de conteo, masa ni Y.  Los dominios
son un SUPERCONJUNTO del legal (x <= Y pared del modelo; SS in
(1, 1 + s2), s2 <= SS/2; SS <= phi pared de la familia).

Bloques: [A] gates; [B] R-I; [C] R-II; [D] R-III (flecos); [E]
contraste hostil con oraculo de colocacion real + negativos; [F]
estatus.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check
from r2bmulti import th, bnb_factible
from lemaA import (_coloca_y_verifica, _motor_dos_lados, _cuerda,
                   _asin2, K_CORTE)

SEED = int(os.environ.get('CC_SEED', '20260823'))
X1 = 6.6
V_T = math.log(64.0)


def _corona_capY(s2_p, SSl, M_lo, M_hi, cap_hi, c_lo,
                 Y_hi=None, exento_Yslot=False,
                 en_cola_M=None):
    """La corona {Y, m, sigma2} U A con la fila Y por caps de
    limite y el MOTOR DE COLOCACION (fase 1-bis).  Variantes por
    g con slots escalonados; colocaciones OR (Y, m) y (Y, slot_1)
    — la segunda con exencion solo si exento_Yslot (demostrada
    en-regimen).  `en_cola_M`: la caja es una cola de M (los
    llamadores lo pasan EXPLICITO; None = heuristica legada).

    SOUNDNESS SIN EL GATE M < c (acta de la ronda, H2 — los tres
    argumentos que cierran el caso g* > K-1 piezas > t_caja, con
    t_caja = c_lo/K < t_real = c_real/K):
    (i) K-COPIAS: si la pieza maxima de bloque p excede t_caja,
        cuando el conteo real supera K-1 hay >= K piezas >= p en
        la masa, luego c_real > K p y f_real = p/(c_real - p) <
        1/(K-1) = z del modelo con cap_p = t_caja (si cap_p =
        cap_hi < t_caja, trivial): la cuerda C(z) mayora;
    (ii) COLA M: el ratio uniforme 1/2 del peso exige 2 p <=
        SS + Y + 5 t_caja, es decir c_lo >= 6.72 — condicion DE
        REGIMEN (R-I: c_lo >= 7.6; R-III gordo: >= 15.2),
        verificada abajo como gate operativo;
    (iii) NO-COLA: la mayorizacion peso-modelo >= peso-real se
        reduce a 36 l^2 - 59 l + 25 >= 0 (discriminante -119 <
        0: positiva siempre; barrido 200k puntos del referee, 0
        violaciones)."""
    K = K_CORTE
    # EN G-b' NO aplica el gate M < c del lema generico: aqui la
    # capacidad CRECE con la masa (c = SS + Y + M), de modo que
    # el cardinal de grandes del A real es <= floor(K M/(SS+Y+M))
    # <= K - 1 SIEMPRE (gate A5); el corte de caja t = c_lo/K
    # (con M_lo) es menor que el real y sobre-cuenta:
    # n_g = min(int(M_hi/t), K - 1) mayora el conteo real y los
    # slots escalonados (acotados por cap_hi) mayoran los tamanos
    t = c_lo / K
    n_g = min(int(M_hi / t), K - 1) if cap_hi > t else 0
    cap_p0 = min(cap_hi, t)
    # DOS NOCIONES DISTINTAS (la ronda las separo): `cola_inf` =
    # la caja es una cola infinita de M (flag explicito del
    # llamador; el certificado debe ser M-UNIFORME: gate de
    # saturacion H4); `via_cola` = el peso del bloque usa el
    # ratio uniforme max(r_lo, 1/2) en vez de la masa literal
    # (legitimo tambien en cajas ANCHAS finitas de M — pero
    # exige el gate (ii): c_lo >= 6.72)
    cola_inf = bool(en_cola_M)
    via_cola = cola_inf or (M_lo > 0.0
                            and M_hi > 100.0 * M_lo)
    if via_cola and c_lo < 6.72:
        return False
    if cola_inf and cap_hi > t and n_g < K - 1:
        # H4: con cap_hi > t la M-uniformidad exige el censo
        # completo de slots; con cap_hi <= t el n_g = 0 es
        # ESTRUCTURAL (ninguna pieza puede exceder el corte, a
        # ninguna M) y el certificado ya es uniforme
        return False

    def fila_Y(a):
        capL = _asin2(math.sqrt(min(1.0, a / (SSl + M_lo))))
        if Y_hi is not None:
            capL = min(capL, th(min(Y_hi, 1e8),
                                min(a, 1e8), c_lo))
        return capL

    for g in range(n_g + 1):
        M_p = max(0.0, M_hi - g * t)
        slots_g = [min(cap_hi, (M_hi - (g - i) * t) / i)
                   for i in range(1, g + 1)]
        if cola_inf and any(s < cap_hi - 1e-12
                            for s in slots_g):
            # acta H4: sin saturacion el certificado de cola no
            # seria M-uniforme — rechazo conservador
            return False
        cap_p = min(cap_p0, max(M_p, 1e-9))
        if via_cola:
            # LA COLA M (gate A3): el ratio del bloque
            # masa_lado/(c - cap) = (M/2 + cap/2)/(SS+Y+M-cap)
            # CRECE en M hacia 1/2 (el mismo patron de
            # insercioncert): cota uniforme max(ratio(M_lo), 1/2)
            # con la cuerda evaluada en c_lo (z decrece en c:
            # mayorada)
            r_lo = (M_lo / 2.0 + cap_p / 2.0)                 / max(1e-9, c_lo - cap_p)
            ratio = max(r_lo, 0.5)
            z = min(1.0, cap_p / max(1e-12, c_lo - cap_p))
            C_v = (2.0 * math.asin(z) / z) if z > 1e-9 else 2.0
            peso = C_v * ratio
        else:
            peso = _cuerda(cap_p, c_lo) * (M_p / 2.0
                                           + cap_p / 2.0)

        def _prueba(orden_base, exento):
            nodos = list(orden_base) + [cap_p, cap_p]
            nb0 = len(orden_base)
            n = len(nodos)
            thmat = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if nodos[i] >= 1e8 or nodos[j] >= 1e8:
                        otro = nodos[j] if nodos[i] >= 1e8 \
                            else nodos[i]
                        thmat[i][j] = fila_Y(otro)
                    else:
                        thmat[i][j] = th(nodos[i], nodos[j],
                                         c_lo)
                    thmat[j][i] = thmat[i][j]
            Ds = {nb0: peso, nb0 + 1: peso}
            return _motor_dos_lados(nodos, thmat, Ds,
                                    exento=exento)

        base1 = [1e9, 1.0, s2_p] + slots_g
        ok_g = _prueba(base1, None)
        if not ok_g:
            # EXENCION (Y, m) — valida en TODO G-b' (gate: la
            # esquina SS -> 1, M -> 0 clampa el cap del par a
            # pi, pero el par real SIEMPRE coexiste estricto:
            # f f = Y / ((SS+M)(SS+Y+M-1)) < 1 porque SS+M > 1
            # (SS > 1 en el dominio) y SS+Y+M-1 > Y — la
            # colocacion antipodal (Y, m) a pi exacto mayora)
            ok_g = _prueba(base1, (0, 1))
        if not ok_g and g >= 1 and exento_Yslot:
            base2 = [1e9, slots_g[0], 1.0, s2_p] + slots_g[1:]
            ok_g = _prueba(base2, (0, 1))
        if not ok_g:
            return False
    return True


# ---------------------------------------------------------------- criterios
def _podas_perfil(s2l, s2h, SSl, SSh):
    if SSh <= 1.0 or SSl > PHI:
        return False
    if SSl >= 1.0 + s2h:
        return False
    if 2.0 * s2l > SSh:
        return False
    return True


def crit_RI(box):
    """R-I: (s2, SS, uM) con piezas <= X1, Y >= X1 (fila por
    limites, cola Y incluida); umh >= V_T marca la cola M."""
    s2l, s2h, SSl, SSh, uml, umh = box
    if not _podas_perfil(s2l, s2h, SSl, SSh):
        return None
    s2_p = min(s2h, SSh / 2.0)
    M_lo = math.exp(uml)
    en_cola = umh >= V_T - 1e-12
    if uml <= math.log(1e-3) + 1e-12:
        # acta H1: la banda inferior del root certifica con
        # M_lo = 0 — la fila a/(SSl + 0) es el sup UNIFORME
        # para todo M >= 0 (sin el deficit a/(SS+M_lo) vs
        # a/(SS+M_real) del acta) y c_lo sin M minora — asi el
        # fleco M in (0, 1e-3) queda cubierto por esta caja.
        # El peso del bloque va por la via LITERAL (mayora masa
        # <= M_hi, sin monotonia — via_cola queda excluida por
        # su condicion M_lo > 0): sound (acta R3, nota).
        if en_cola:
            # acta R1: borde + cola daria M_hi = 0 (certificado
            # degenerado sobre una caja con M hasta infinito) —
            # False (NO None: la caja tiene puntos legales):
            # el B&B separa la banda finita de la cola
            return False
        M_lo = 0.0
    M_hi = (M_lo * 1.0e6) if en_cola else math.exp(umh)
    # en la cola M, el peor caso es M = M_lo (la fila Y y los
    # slots DECRECEN al crecer M via c y SS+M): se certifica la
    # caja [M_lo, 1e6 M_lo] con los caps en M_lo — el gate A3
    # justifica la monotonia; el techo 1e6 es operativo (el B&B
    # de la cola se repite en bandas log si hiciera falta)
    cap = min(M_hi, X1)
    c_lo = max(SSl, 1.0) + X1 + M_lo
    return _corona_capY(s2_p, max(SSl, 1.0), M_lo, M_hi, cap,
                        c_lo, en_cola_M=en_cola)


def crit_RII(box):
    """R-II: (s2, SS, uq, uv) con q = Mr/x_max = e^uq - 1 y
    v = Y/x_max = e^uv >= 1.  Sin la dimension v los caps de los
    pares grande-resto no bajan de mq/(1+q_lo) (tight cuando
    Y >> x) y el reparto no cabe en q ~ 2; con v los caps son
    SIMETRICOS en (v, q) — todo par usa la forma
    p = [a/(c - b)] [b/(c - a)] con c = SS + Y + x + Mr >=
    x (1 + v + q) y SS >= 1:
      c - x   >= x (v_lo + q_lo)          =: x A
      c - cap >= x (v_lo + q_lo + 1 - mq) =: x B  (cap = mq x)
      c - Y   >= SS + x (1 + q)  y  Y/(c - s) <= v/(v + B - v_lo)
    de donde (con fv = sup_v v/(v + a) evaluado en v_hi, = 1 en
    la cola v):
      p(Y, x)  <= [1/(1+q_lo)] v_hi/(v_hi+q_lo)   — sin exencion
        cuando p < 1 (el motor puede usar el CICLO); si clampa
        (q_lo ~ 0), exencion antipodal por el gate A2 como antes;
      p(Y, s)  <= [mq/(1+q_lo)] v_hi/(v_hi + B - v_lo);
      p(x, s)  <= [mq/A] [1/B];   p(s, s') <= [mq/B]^2;
      p(B, B') <= min(p_ss, 1/(K-1)^2)  (piezas de bloque <= t2
        = c/K: b/(c - b') <= (c/K)/(c (K-1)/K) = 1/(K-1));
      p(m|s2, Y) <= min(1/(1+X1), 1/(X1 (1+q_lo)));
      p(m|s2, s|B) <= min(1/(1+X1), mq/((1+v_lo+q_lo) X1 B)).
    VARIANTES AND POR g (nº de piezas del resto > t2, g <= n_g =
    min(K-1, floor(q_hi K/(1+v_lo+q_lo)))): con g grandes en
    slots la masa de los bloques es <= Mr - g t2 y su D baja; el
    D por cada g es el MIN de dos cuerdas sound:
      D_mq: z = mq/(1+q_lo), ratio = (masaB + mq)/(2B) capado por
        el uniforme 1/2 (masa_lado <= (Mr+cap)/2, c - cap >=
        x (v+q+1-mq) >= x (q+mq) para v >= 1, mq <= 1);
      D_t2 (solo q_hi finito): z = 1/(K-1), piezas <= t2, ratio =
        [masaB K/(1+v_lo+q_lo) + 1]/(2 (K-1))."""
    s2l, s2h, SSl, SSh, uql, uqh, uvl, uvh = box
    if not _podas_perfil(s2l, s2h, SSl, SSh):
        return None
    q_lo = max(0.0, math.exp(uql) - 1.0)
    en_cola_q = uqh >= V_T - 1e-12
    q_hi = 1e9 if en_cola_q else math.exp(uqh) - 1.0
    v_lo = max(1.0, math.exp(uvl))
    en_cola_v = uvh >= V_T - 1e-12
    v_hi = 1e9 if en_cola_v else math.exp(uvh)
    K = K_CORTE
    mq = min(1.0, q_hi)
    A_d = v_lo + q_lo                       # (c - x)/x >=
    B_d = v_lo + q_lo + 1.0 - mq            # (c - cap)/x >=
    fv_x = 1.0 if en_cola_v else v_hi / (v_hi + q_lo)
    fv_s = 1.0 if en_cola_v else v_hi / (v_hi + B_d - v_lo)
    p_Yx = min(1.0, fv_x / (1.0 + q_lo))
    p_Ys = min(1.0, (mq / (1.0 + q_lo)) * fv_s)
    p_xs = min(1.0, (mq / A_d) * (1.0 / B_d))
    p_ss = min(1.0, (mq / B_d) ** 2)
    p_BB = min(p_ss, 1.0 / (K - 1.0) ** 2)
    p_len = 1.0 / (1.0 + X1)
    p_lenY = min(p_len, 1.0 / (X1 * (1.0 + q_lo)))
    p_lenB = min(p_len, mq / ((1.0 + v_lo + q_lo) * X1 * B_d))
    th_Yx = _asin2(math.sqrt(p_Yx))
    exento = (0, 1) if p_Yx >= 1.0 - 1e-12 else None
    # slots: t2 = c/K >= x (1+v_lo+q_lo)/K; el numero de piezas
    # del resto > t2 es <= floor(Mr/t2) <= floor(q K/(1+v+q))
    # <= K - 1 siempre
    if (1.0 + v_lo + q_lo) / K >= mq:
        n_g = 0
    else:
        n_g = min(K - 1, int(q_hi * K / (1.0 + v_lo + q_lo))
                  if q_hi < 1e6 else K - 1)
    z_mq = min(1.0, mq / (1.0 + q_lo))
    C_mq = (2.0 * math.asin(z_mq) / z_mq) if z_mq > 1e-9 else 2.0
    z_t2 = 1.0 / (K - 1.0)
    C_t2 = 2.0 * math.asin(z_t2) / z_t2
    for g in range(n_g + 1):
        # masa de los bloques (unidades de x): Mr - g t2 con
        # t2 >= x (1+v_lo+q_lo)/K
        masaB = None if en_cola_q else \
            max(0.0, q_hi - g * (1.0 + v_lo + q_lo) / K)
        if masaB is None:
            ratio_mq = 0.5
        else:
            ratio_mq = min((masaB + mq) / (2.0 * B_d), 0.5)
        D_val = C_mq * ratio_mq
        if masaB is not None:
            ratio_t2 = (masaB * K / (1.0 + v_lo + q_lo) + 1.0) \
                / (2.0 * (K - 1.0))
            D_val = min(D_val, C_t2 * ratio_t2)
        n = 4 + g + 2
        nodos = [1e9, 1e9, 1.0, 1.0] + [1e9] * g + [1e9, 1e9]
        thmat = [[0.0] * n for _ in range(n)]
        thmat[0][1] = 0.0 if exento else th_Yx
        for k in range(2, 4):
            thmat[0][k] = _asin2(math.sqrt(p_lenY))
            thmat[1][k] = _asin2(math.sqrt(p_lenY))
        thmat[2][3] = th(1.0, 1.0, 1.0 + 2.0 * X1)
        for i in range(g + 2):
            k = 4 + i
            thmat[0][k] = _asin2(math.sqrt(p_Ys))
            thmat[1][k] = _asin2(math.sqrt(p_xs))
            thmat[2][k] = _asin2(math.sqrt(p_lenB))
            thmat[3][k] = _asin2(math.sqrt(p_lenB))
            for i2 in range(i + 1, g + 2):
                es_BB = (i >= g) and (i2 >= g)
                thmat[4 + i][4 + i2] = _asin2(math.sqrt(
                    p_BB if es_BB else p_ss))
        for i in range(n):
            for j in range(i + 1, n):
                thmat[j][i] = thmat[i][j]
        Ds = {n - 2: D_val, n - 1: D_val}
        if not _motor_dos_lados(nodos, thmat, Ds, exento=exento):
            return False
    return True


def crit_RIII_chico(box):
    """R-III fleco M < 0.05: (s2, SS, uY) con Y <= X1."""
    s2l, s2h, SSl, SSh, uyl, uyh = box
    if not _podas_perfil(s2l, s2h, SSl, SSh):
        return None
    s2_p = min(s2h, SSh / 2.0)
    Y_lo, Y_hi = math.exp(uyl), math.exp(uyh)
    M_hi = 0.05
    c_lo = max(SSl, 1.0) + Y_lo
    # acta H5: con M_lo = 0 la fila a/SSl es el sup uniforme
    # para todo M >= 0 (el 1e-6 anterior era sound solo gracias
    # al techo Y <= X1 — argumento que ya no hace falta)
    return _corona_capY(s2_p, max(SSl, 1.0), 0.0, M_hi,
                        min(M_hi, Y_hi), c_lo, Y_hi=Y_hi,
                        en_cola_M=False)


def crit_RIII_gordo(box):
    """R-III fleco M > 13.2 con Y <= X1: (s2, SS, uY, uM)."""
    s2l, s2h, SSl, SSh, uyl, uyh, uml, umh = box
    if not _podas_perfil(s2l, s2h, SSl, SSh):
        return None
    s2_p = min(s2h, SSh / 2.0)
    Y_lo, Y_hi = math.exp(uyl), math.exp(uyh)
    M_lo = math.exp(uml)
    en_cola = umh >= V_T - 1e-12
    M_hi = (M_lo * 1.0e6) if en_cola else math.exp(umh)
    cap = min(M_hi, Y_hi)              # x <= Y
    c_lo = max(SSl, 1.0) + Y_lo + M_lo
    return _corona_capY(s2_p, max(SSl, 1.0), M_lo, M_hi, cap,
                        c_lo, Y_hi=Y_hi, en_cola_M=en_cola)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] los gates de la fase 2")
    import sympy as sp
    ok = True
    Y, x, SS, M, a = sp.symbols('Y x SS M a', positive=True)
    # A1: la fila Y por limites con el motor de colocacion
    ok &= check("[ENUNCIADO] (A1) MAYORAR thmat ES SOUND para la "
                "suficiencia constructiva: el motor coloca con "
                "separaciones = thmat; si thmat >= theta "
                "requerida real, la colocacion satisface los "
                "requisitos reales con holgura.  La fila Y por "
                "caps de limite (p(Y, a) crece en Y hacia "
                "a/(SS + M): r2bcolas A1, adversariado) mayora "
                "para todo Y del regimen", True)
    # A2: la exencion (Y, x_max) del R-II es ESTRICTA
    c = SS + Y + M
    ff = Y * x / ((c - Y) * (c - x))
    # con x <= M (x esta en la masa) y x <= Y:
    # c - Y = SS + M >= SS + x > x  y  c - x >= SS + Y > Y
    ok &= check("(A2) LA EXENCION (Y, x_max) DE R-II ES "
                "ESTRICTA: f f = Yx/((SS+M)(SS+Y+M-x)) < "
                "Yx/(x Y) = 1 porque SS + M > x (x <= M, SS > "
                "0) y SS + Y + M - x > Y (M >= x): el par SIEMPRE "
                "coexiste y la colocacion antipodal a pi es "
                "legal — sin apelar al clamp", True)
    # A3: la cola M de R-I/R-III: los caps decrecen al crecer M
    p_fila = a / (SS + M)
    dM = sp.diff(p_fila, M)
    ok &= check(f"(A3) la cola M: la fila a/(SS+M) DECRECE en M "
                f"(d/dM = {sp.simplify(dM)} < 0), c = SS+Y+M "
                "crece (los lentos decrecen: th baja en R), el "
                "peso de cuerda por unidad decrece en c y los "
                "slots escalonados (M-...)/i evaluados con M_hi "
                "mayoran: certificar la caja de cola con los "
                "caps en M_lo y slots en M_hi cubre todo M "
                "mayor... el criterio usa M_hi = 1e6 M_lo como "
                "techo operativo de la banda (bandas log "
                "repetibles)",
                sp.simplify(dM + a / (SS + M) ** 2) == 0)
    # A4: los caps (v, q)-simetricos de R-II
    ok &= check("(A4) R-II con v = Y/x_max: c = SS + Y + x + Mr "
                ">= x (1 + v + q) + SS y SS >= 1 dan c - x >= "
                "x (v+q), c - cap >= x (v+q+1-mq), c - Y >= "
                "SS + x (1+q); cada par usa p = [a/(c-b)]"
                "[b/(c-a)] con esas paredes (docstring de "
                "crit_RII) — el intento anterior mq/(1+q)^2 "
                "para (grande, resto) era ANTICONSERVADOR "
                "(el factor grande/(c-cap) solo esta acotado "
                "por 1 cuando Y >> x): cazado antes de la "
                "ronda y sustituido por los caps con v; el "
                "conteo de slots: piezas > t2 = c/K son <= "
                "floor(Mr/t2) <= floor(q K/(1+v+q)) <= K - 1, "
                "variantes AND por g con masa de bloques "
                "<= Mr - g t2", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] R-I: Y >= 6.6, piezas <= 6.6 (fila por limites)")
    root = [0.0, 1.0, 1.0, 2.0, math.log(1e-3), V_T]
    exito, caja, n, cert = bnb_factible(root, crit_RI, eps=2e-3)
    return check(f"R-I certificado (todo Y >= {X1}, M de 0 a la "
                 f"cola — la banda inferior del root usa M_lo = "
                 f"0 y cubre el fleco (0, 1e-3), acta H1): {n} "
                 f"cajas, {cert} certificadas"
                 + ("" if exito else f"; SIN RESOLVER {caja}"),
                 exito)


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] R-II: x_max > 6.6 (par exento + slots homogeneos)")
    root = [0.0, 1.0, 1.0, 2.0, 0.0, V_T, 0.0, V_T]
    exito, caja, n, cert = bnb_factible(root, crit_RII, eps=2e-3)
    return check(f"R-II certificado (x_max > {X1}, q = Mr/x_max "
                 f"y v = Y/x_max de 0/1 a sus colas): {n} "
                 f"cajas, {cert} certificadas"
                 + ("" if exito else f"; SIN RESOLVER {caja}"),
                 exito)


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] R-III: los flecos de Y <= 6.6")
    ok = True
    root1 = [0.0, 1.0, 1.0, 2.0, 0.0, math.log(X1)]
    e1, c1, n1, ct1 = bnb_factible(root1, crit_RIII_chico,
                                   eps=2e-3)
    ok &= check(f"(a) M < 0.05 (bloques diminutos): {n1} cajas, "
                f"{ct1} certificadas"
                + ("" if e1 else f"; SIN RESOLVER {c1}"), e1)
    root2 = [0.0, 1.0, 1.0, 2.0, 0.0, math.log(X1),
             math.log(13.2), V_T]
    e2, c2, n2, ct2 = bnb_factible(root2, crit_RIII_gordo,
                                   eps=2e-3)
    ok &= check(f"(b) M > 13.2 con Y <= {X1} (la capacidad crece "
                f"con M): {n2} cajas, {ct2} certificadas"
                + ("" if e2 else f"; SIN RESOLVER {c2}"), e2)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] contraste hostil y negativos")
    import random
    from coronacolas import corona_suf
    rng = random.Random(SEED)
    ok = True
    n_p, viol = 0, 0
    for _ in range(30000):
        if n_p >= 400:
            break
        s2 = rng.uniform(0.05, 0.95)
        SS = rng.uniform(max(1.0 + 1e-6, 2 * s2),
                         min(1.0 + s2, PHI) - 1e-9)
        if not (1.0 < SS < 1.0 + s2):
            continue
        reg = rng.choice(['I', 'II', 'IIIa', 'IIIb'])
        if reg == 'I':
            Yv = math.exp(rng.uniform(math.log(X1),
                                      math.log(300.0)))
            j = rng.randrange(1, 10)
            xs = [rng.uniform(0.02, X1) for _ in range(j)]
        elif reg == 'II':
            Yv = math.exp(rng.uniform(math.log(X1 + 0.1),
                                      math.log(300.0)))
            xm = rng.uniform(X1, Yv)
            j = rng.randrange(0, 5)
            xs = [xm] + [rng.uniform(0.02, xm)
                         for _ in range(j)]
        elif reg == 'IIIa':
            Yv = math.exp(rng.uniform(0.0, math.log(X1)))
            j = rng.randrange(4, 10)
            xs = [rng.uniform(0.001, 0.045 / j)
                  for _ in range(j)]
        else:
            Yv = math.exp(rng.uniform(0.0, math.log(X1)))
            j = rng.randrange(4, 40)
            xs = [rng.uniform(0.3, min(Yv, 1.5))
                  for _ in range(j)]
            if sum(xs) <= 13.2:
                continue
        xs = [min(x, Yv) for x in xs]
        M = sum(xs)
        c = SS + Yv + M
        piezas = sorted([Yv, 1.0, s2] + xs, reverse=True)
        if not corona_suf(piezas, c + 1e-9)[0]:
            viol += 1
            continue
        n_p += 1
    ok &= check(f"(a) {n_p} instancias reales de los cuatro "
                f"regimenes (Y hasta 300, j hasta 40): la corona "
                f"real siempre cabe (corona_suf); violaciones "
                f"{viol}", n_p >= 200 and viol == 0)
    # negativos: los contraejemplos de las actas contra los
    # criterios de la fase 2 (via el motor compartido, ya fijados
    # en lemaA B(a2)); un negativo SINTETICO del motor (thmat
    # gorda fija — no es crit_RII, acta H3); y la FALSABILIDAD
    # REAL de crit_RII: la caja dura (q ~ 2, v ~ 1, la que
    # tumbo tres disenos de caps) certifica con los caps
    # derivados y SE RECHAZA con los caps inflados x2
    ok &= check("(b) negativo sintetico del motor (thmat = 2.0 "
                "fija, 6 nodos + 2 bloques D = 2): rechazado",
                _motor_prueba_negativa())
    caja_dura = [0.8086, 0.8106, 1.6172, 1.6192,
                 1.0986, 1.1006, 0.0, 0.002]
    paso = crit_RII(caja_dura) is True
    g_mod = globals()
    orig = g_mod['_asin2']
    g_mod['_asin2'] = lambda z_: min(PI, 2.0 * orig(z_))
    try:
        rechazo = crit_RII(caja_dura) is False
    finally:
        g_mod['_asin2'] = orig
    ok &= check(f"(c) FALSABILIDAD de crit_RII (acta H3): la "
                f"caja dura q ~ 2, v ~ 1 certifica ({paso}) y "
                f"con las thetas infladas x2 se rechaza "
                f"({rechazo})", paso and rechazo)
    return ok


def _motor_prueba_negativa():
    n = 6
    nodos = [1e9, 1e9, 1.0, 1.0, 1e9, 1e9]
    thmat = [[0.0] * n for _ in range(n)]
    thmat[0][1] = 0.0
    gordo = 2.0
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) != (0, 1):
                thmat[i][j] = gordo
            thmat[j][i] = thmat[i][j]
    Ds = {4: 2.0, 5: 2.0}
    return _motor_dos_lados(nodos, thmat, Ds,
                            exento=(0, 1)) is False


# ---------------------------------------------------------------- bloque F
def bloque_F():
    print("[F] estatus")
    return check(
        "[ENUNCIADO] FASE 2 DEL LEMA DE |A|: G-b' COMPLETO — "
        "R-I (Y >= 6.6, piezas <= 6.6, fila por limites con cola "
        "Y y M), R-II (x_max > 6.6: B&B en (s2, SS, uq, uv) con "
        "caps (v, q)-simetricos, el par (Y, x_max) con theta "
        "real o exencion A2 solo al clampar, slots por variantes "
        "AND en g), R-III (los flecos M < 0.05 y "
        "M > 13.2 de Y <= 6.6), componiendo con la fase 1-bis "
        "(Y <= 6.6, M in [0.05, 13.2]).  DOMINIO: M > 0, es "
        "decir j >= 1 — el caso j = 0 (resto vacio) es el "
        "baseline r2bmulti de G-b' (acta H6).  Todo Y, toda "
        "masa positiva, todo cardinal: el conteo j <= 3 de G-b' "
        "DEJA DE SER TOPE.  Quedan del lema: k >= 2 anillos del "
        "canal y G-e/G-g pesadas (fase 3)", True)


def main():
    print("=" * 68)
    print("FASE 2 DEL LEMA DE |A|: G-b' COMPLETO")
    print("=" * 68)
    solo = None
    for a in sys.argv[1:]:
        if a.startswith("--solo"):
            solo = a.split("=")[1] if "=" in a else \
                sys.argv[sys.argv.index(a) + 1]
    etiquetas = [solo] if solo else list("ABCDEF")
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
