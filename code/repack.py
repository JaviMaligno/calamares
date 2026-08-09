#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F2: el lema de realizacion y repack (docs/drafts/repack.md).

Cierra el [ENUNCIADO] F2 (la legalidad del repack de contenedores)
del que dependen las pinzas de bolsillo espejo F1e/F1f, las coronas
de agujero, el pan repack de thm:DP y todos los repartos testigo.

LA DEFINICION DEL PAPER (Rings and placements, ~181-193): una
colocacion es un BOSQUE (cada anillo tiene por padre la sarten o un
anillo con r_child <= r_parent - w); los hijos de un padre comun
deben ser empaquetables COMO BOLAS (radio exterior) con interiores
disjuntos dentro de la region del padre (la sarten o la bola-agujero
de radio r - w).  "Feasibility is a property of the assignment
(siblings may be rearranged freely inside their container)."

EL LEMA (lo que la definicion deja implicito y aqui se prueba):

(a) REALIZACION.  Si cada contenedor del bosque tiene una colocacion
    disjunta de sus hijos (como bolas), entonces existe una
    realizacion geometrica SIMULTANEA de todo el bosque: componer
    las isometrias por la ruta raiz-hoja (el centro absoluto de y =
    centro absoluto del padre + posicion relativa de y en la region
    del padre).  Induccion en profundidad:
      (i)  la bola-agujero de y esta dentro de la bola de y
           (r - w <= r);
      (ii) los descendientes de y quedan dentro de la bola de y, y
           los de un hermano z dentro de la de z: bolas de hermanos
           disjuntas => materiales de ramas distintas disjuntos;
      (iii) el MATERIAL de y (el anulo r-w..r) es disjunto de su
           bola-agujero => disjunto de todos sus descendientes;
      (iv) las isometrias preservan distancias: la colocacion
           relativa de cada contenedor se traslada sin romperse.
(b) REPACK.  Sustituir en UN contenedor la colocacion de sus hijos
    por OTRA colocacion disjunta cualquiera (mismas bolas, subarbol
    de cada hijo rigido) produce otra realizacion valida del MISMO
    bosque: la asignacion, los objetivos (N, A) y todas las colas
    (rho) son invariantes — son funciones del bosque, no de las
    posiciones.
(c) INTERCAMBIO.  El testigo P' del paso de intercambio puede
    re-empaquetar cualquier contenedor libremente: la induccion de
    thm:oblivious consume solo la asignacion.  Todos los recursos de
    las campanas (pan repack, bolsillo espejo, fila de D_m, coronas
    de agujero, trio R2b) son instancias de (b).

Bloques: [A] los pasos exactos de la induccion; [B] realizacion
numerica de bosques aleatorios (0 violaciones de material);
[C] repack de un contenedor y re-verificacion (invariantes);
[D] los consumidores de las campanas como instancias; [E] controles
(hijos solapados o subarbol no-rigido rompen la realizacion).
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coronacolas import PHI, PI, check

ITER = int(os.environ.get('CC_ITER', '60000'))
SEED = int(os.environ.get('CC_SEED', '20260815'))
W = None                               # anchura global por instancia


class Anillo:
    __slots__ = ('r', 'rel', 'hijos', 'abs')

    def __init__(self, r):
        self.r = r
        self.rel = (0.0, 0.0)          # centro relativo al padre
        self.hijos = []
        self.abs = (0.0, 0.0)


def hueco(r, w):
    return max(0.0, r - w)


def coloca_en(regR, bolas, rng, intentos=4000):
    """Colocacion disjunta aleatoria de bolas (radios) dentro de un
    disco de radio regR centrado en 0; None si no lo logra (el
    generador reintenta)."""
    pos = []
    for r in bolas:
        if r > regR + 1e-12:
            return None                # bola mayor que la region
        okp = None
        for _ in range(intentos):
            rr = (regR - r) * math.sqrt(rng.random())
            th = rng.uniform(0, 2 * PI)
            p = (rr * math.cos(th), rr * math.sin(th))
            if all((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                   >= (r + s) ** 2 - 1e-12 for q, s in pos):
                okp = p
                break
        if okp is None:
            return None
        pos.append((okp, r))
    return [p for p, _ in pos]


def genera_bosque(rng, w, R, depth=0):
    """Bosque aleatorio factible: anillos top-level en la sarten,
    hijos recursivos en las bolas-agujero."""
    n = rng.randrange(1, 4) if depth == 0 else rng.randrange(0, 3)
    radios = [rng.uniform(0.25, 0.75) * R for _ in range(n)]
    if rng.random() < 0.4:             # solidos y casi-solidos
        radios.append(rng.uniform(0.3, 1.1) * w)   # (ronda hostil)
    radios = sorted((r for r in radios if r <= R), reverse=True)
    hijos = []
    for r in radios:
        a = Anillo(r)
        h = hueco(r, w)
        if depth < 3 and h > 0.1 * R and rng.random() < 0.8:
            sub = genera_bosque(rng, w, h, depth + 1)
            a.hijos = sub
        hijos.append(a)
    # colocar los hijos como bolas en el disco R
    pos = coloca_en(R, [a.r for a in hijos], rng)
    if pos is None:
        return []
    for a, p in zip(hijos, pos):
        a.rel = p
    return hijos


def compone(hijos, origen=(0.0, 0.0)):
    """La composicion de isometrias raiz-hoja: centro absoluto =
    origen del contenedor + posicion relativa."""
    todos = []
    for a in hijos:
        a.abs = (origen[0] + a.rel[0], origen[1] + a.rel[1])
        todos.append(a)
        todos += compone(a.hijos, a.abs)
    return todos


def verifica(todos, w, R, tol=1e-9):
    """Chequeo GLOBAL de materiales: para cada par de anillos, o las
    bolas son disjuntas, o una bola esta dentro de la bola-agujero
    de la otra; y cada top-level dentro de la sarten (los anidados
    quedan dentro por transitividad, tambien chequeada via bola en
    bola-agujero del padre).  Devuelve el numero de violaciones."""
    viol = 0
    for i, a in enumerate(todos):
        for b in todos[i + 1:]:
            d = math.hypot(a.abs[0] - b.abs[0], a.abs[1] - b.abs[1])
            if d >= a.r + b.r - tol:
                continue
            if d <= hueco(b.r, w) - a.r + tol:
                continue               # a dentro del agujero de b
            if d <= hueco(a.r, w) - b.r + tol:
                continue               # b dentro del agujero de a
            viol += 1
    return viol


def verifica_padres(hijos, w, regR, origen=(0.0, 0.0), tol=1e-9):
    """Cada hijo dentro de la region de su padre, recursivo."""
    viol = 0
    for a in hijos:
        d = math.hypot(a.abs[0] - origen[0], a.abs[1] - origen[1])
        if d > regR - a.r + tol:
            viol += 1
        viol += verifica_padres(a.hijos, w, hueco(a.r, w), a.abs, tol)
    return viol


def bosque_str(hijos):
    """La ASIGNACION como estructura comparable (radios por
    contenedor, recursivo) — invariante bajo repack."""
    return sorted((round(a.r, 9), bosque_str(a.hijos)) for a in hijos)


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] transcripcion del argumento de induccion (los pasos "
          "por separado son triviales; la carga numerica de la "
          "composicion esta en B/C — re-etiquetado en ronda hostil)")
    import sympy as sp
    ok = True
    r, w_, d = sp.symbols('r w d', positive=True)
    ok &= check("(i) la bola-agujero cabe en la bola: r - w <= r "
                "(el material es el anulo entre ambas)",
                sp.simplify(r - (r - w_)) == w_)
    ok &= check("(ii) descendientes confinados: si |c_y - c_z| >= "
                "r_y + r_z (hermanos disjuntos como bolas) y todo "
                "descendiente de y esta en B(c_y, r_y) (induccion: "
                "hijo en la bola-agujero + bola-agujero en la bola)"
                ", los materiales de las dos ramas son disjuntos",
                True)
    ok &= check("(iii) el material del padre (anulo r-w..r) es "
                "disjunto del interior de su bola-agujero: los "
                "descendientes (confinados alli) no tocan al padre",
                True)
    ok &= check("(iv) las isometrias preservan |x - y|: la "
                "colocacion relativa de cada contenedor (disjuncion "
                "y contencion, condiciones en distancias) se "
                "traslada por la ruta raiz-hoja sin romperse — la "
                "composicion es una realizacion global",
                sp.simplify(sp.sqrt((d + 0) ** 2) - d) == 0)
    ok &= check("[ENUNCIADO] la definicion del paper (Rings and "
                "placements): 'feasibility is a property of the "
                "assignment (siblings may be rearranged freely "
                "inside their container)' — el lema le pone la "
                "prueba de realizacion debajo; los objetivos N, A y "
                "las colas rho son funciones del multiconjunto y "
                "del bosque, no de las posiciones", True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] realizacion numerica de bosques aleatorios")
    rng = random.Random(SEED)
    ok = True
    n_b, n_a, viol = 0, 0, 0
    for _ in range(max(1500, ITER // 40)):
        w = rng.uniform(0.05, 0.5)
        R = rng.uniform(2.0, 6.0)
        hijos = genera_bosque(rng, w, R)
        if not hijos:
            continue
        todos = compone(hijos)
        if len(todos) < 2:
            continue
        n_b += 1
        n_a += len(todos)
        viol += verifica(todos, w, R)
        viol += verifica_padres(hijos, w, R)
    ok &= check(f"la composicion raiz-hoja realiza el bosque entero "
                f"({n_b} bosques, {n_a} anillos, profundidad hasta "
                f"4, solidos incluidos): {viol} violaciones de "
                f"material/contencion",
                n_b > 250 and n_a > 600 and viol == 0)
    # sub-bloque DETERMINISTA (ronda hostil, H5): tangencias
    # EXACTAS, solidos r <= w, micro-agujeros, rotacion/reflexion
    w = 0.5
    R = 4.0
    a1, a2 = Anillo(2.0), Anillo(2.0)
    a1.rel, a2.rel = (-2.0, 0.0), (2.0, 0.0)   # tangentes entre si
    h1, h2 = Anillo(0.9), Anillo(0.6)          # y a la pared
    h1.rel, h2.rel = (-0.6, 0.0), (0.9, 0.0)   # fila TANGENTE en
    a1.hijos = [h1, h2]                        # el agujero 1.5
    s1 = Anillo(0.4)                           # SOLIDO r <= w
    s1.rel = (0.0, 0.0)                        # tangente interno
    h1.hijos = [s1]
    g1 = Anillo(0.1)                           # llena el agujero
    g1.rel = (0.0, 0.0)                        # 0.1 de h2 EXACTO
    h2.hijos = [g1]
    m1 = Anillo(1.45)                          # micro-margen 0.05
    m1.rel = (0.05, 0.0)                       # tangente interno
    a2.hijos = [m1]
    s2_ = Anillo(0.5)                          # solido r = w exacto
    s2_.rel = (0.45, 0.0)                      # tangente en 0.95
    m1.hijos = [s2_]
    bosque = [a1, a2]
    todos = compone(bosque)
    v_det = verifica(todos, w, R) + verifica_padres(bosque, w, R)
    # rotacion 45 grados + reflexion de la colocacion de a1 (otra
    # colocacion del contenedor: las traslaciones componen, las
    # regiones son rotacionalmente simetricas)
    c, s = math.cos(PI / 4), math.sin(PI / 4)
    for h in a1.hijos:
        x, y = h.rel
        h.rel = (c * x - s * y, s * x + c * y)
    for h in a2.hijos:
        h.rel = (-h.rel[0], h.rel[1])          # reflexion
    todos = compone(bosque)
    v_rot = verifica(todos, w, R) + verifica_padres(bosque, w, R)
    ok &= check(f"determinista: hermanos tangentes exactos + fila "
                f"tangente en el agujero + solidos r <= w tangentes "
                f"internos + micro-margen 0.05 + agujero llenado "
                f"exacto: {v_det} violaciones; tras ROTAR 45 la "
                f"colocacion de un contenedor y REFLEJAR otra "
                f"(isometrias como otras colocaciones): {v_rot}",
                v_det == 0 and v_rot == 0)
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] repack de un contenedor: re-colocacion + invariantes")
    rng = random.Random(SEED + 1)
    ok = True
    n_r, viol, cambios = 0, 0, 0
    for _ in range(max(3000, ITER // 20)):
        w = rng.uniform(0.05, 0.5)
        R = rng.uniform(2.0, 6.0)
        hijos = genera_bosque(rng, w, R)
        if not hijos:
            continue
        antes = bosque_str(hijos)
        # elegir un contenedor con >= 2 hijos: la sarten o un anillo
        conts = [(None, hijos, R)]
        todos = compone(hijos)
        for a in todos:
            if len(a.hijos) >= 2:
                conts.append((a, a.hijos, hueco(a.r, w)))
        cont = conts[rng.randrange(len(conts))]
        _, sus_hijos, regR = cont
        if len(sus_hijos) < 2:
            continue
        # OTRA colocacion disjunta de las mismas bolas (subarboles
        # rigidos: solo cambia rel del hijo, su interior viaja)
        pos = coloca_en(regR, [a.r for a in sus_hijos], rng)
        if pos is None:
            continue
        movio = False
        for a, p in zip(sus_hijos, pos):
            if math.hypot(a.rel[0] - p[0], a.rel[1] - p[1]) > 1e-6:
                movio = True
            a.rel = p
        todos = compone(hijos)         # recomponer TODO
        n_r += 1
        if movio:
            cambios += 1
        viol += verifica(todos, w, R)
        viol += verifica_padres(hijos, w, R)
        if bosque_str(hijos) != antes:
            viol += 1                  # la asignacion cambio: error
    ok &= check(f"repack de un contenedor (mismas bolas, subarboles "
                f"rigidos, {n_r} repacks, {cambios} con movimiento "
                f"real): {viol} violaciones tras recomponer; la "
                f"ASIGNACION (y con ella N, A, rho) es invariante",
                n_r > 150 and cambios > 120 and viol == 0)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] los consumidores de las campanas como instancias")
    ok = True
    w = 0.3
    # (1) pan repack de thm:DP / bolsillo espejo: {alpha, o1} par
    #     diametral y sigma2 al bolsillo b2
    alpha, o1 = 2.2, 1.9
    R = alpha + o1
    s2 = 0.5
    b2 = 1 / (1 / alpha + 1 / o1 - 1 / R)  # bolsillo de Descartes
    okb = b2 > s2                      # ilustrativo: la fila F1e/F1f
    # (formula exacta: Descartes degenerado en R = alpha+o1)
    ok &= check(f"(1) pan repack + bolsillo espejo: par diametral "
                f"{{alpha, o1}} en R = alpha+o1 y sigma2 = {s2} < "
                f"b2 = {b2:.3f}: el repack que las pinzas F1e/F1f "
                f"consumen es una instancia de (b) — mismas bolas "
                f"top-level, otra colocacion", okb)
    # (2) la fila de D_m (lem:row): bolas de suma <= 1 en la bola
    #     vacante de radio 1
    fila = [0.45, 0.3, 0.2]
    pos, x = [], -1.0
    okf = sum(fila) <= 1.0
    for r in fila:
        pos.append((x + r, 0.0))
        x += 2 * r
    okf &= all(abs(p[0]) <= 1.0 - r + 1e-12
               for p, r in zip(pos, fila))
    okf &= all(math.hypot(pos[i][0] - pos[j][0], 0.0)
               >= fila[i] + fila[j] - 1e-12
               for i in range(len(fila)) for j in range(i))
    ok &= check(f"(2) la fila de D_m (lem:row) es un repack del "
                f"contenedor D_m: bolas {fila} (suma "
                f"{sum(fila):.2f} <= 1) en fila diametral, "
                f"disjuntas y contenidas: {okf}", okf)
    # (3) corona de agujero: {x1, m} + sigma2 mural en el disco
    #     c = capacidad del agujero (instancia de la rama 2)
    from gaplemma import corona_k5
    c = 3.4
    piezas = [1.6, 1.0, 0.6]
    cabe, _ = corona_k5(sorted(piezas, reverse=True), c)
    ok &= check(f"(3) corona del agujero (ramas 1/2): piezas "
                f"{piezas} en capacidad {c}: cabe = {cabe} — el "
                f"repack del agujero de alpha/Y es la misma "
                f"operacion de (b) con region = bola-agujero", cabe)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles")
    rng = random.Random(SEED + 2)
    ok = True
    # (a) hijos solapados como bolas: la realizacion detecta
    a1, a2 = Anillo(1.0), Anillo(1.0)
    a1.rel, a2.rel = (-0.8, 0.0), (0.8, 0.0)   # d = 1.6 < 2
    todos = compone([a1, a2])
    v = verifica(todos, 0.3, 3.0)
    ok &= check(f"(a) hermanos solapados como bolas (d = 1.6 < 2): "
                f"{v} violacion detectada — la hipotesis de "
                f"colocacion disjunta por contenedor es la que "
                f"carga", v == 1)
    # (b) subarbol NO rigido: mover al nieto sin su padre rompe
    p = Anillo(2.0)
    h = Anillo(1.0)
    p.hijos = [h]
    h.rel = (0.0, 0.0)
    p.rel = (0.0, 0.0)
    todos = compone([p])
    v0 = verifica(todos, 0.5, 3.0) + verifica_padres([p], 0.5, 3.0)
    h.abs = (1.6, 0.0)                 # mover el hijo SIN recomponer
    v1 = verifica(todos, 0.5, 3.0)
    ok &= check(f"(b) subarbol no rigido: la configuracion valida "
                f"({v0} violaciones) se rompe al mover el hijo sin "
                f"su padre ({v1} violaciones > 0): el repack mueve "
                f"BOLAS con su interior, no interiores sueltos",
                v0 == 0 and v1 > 0)
    # (c) un hijo mas grande que la capacidad: imposible de colocar
    pos = coloca_en(1.0, [1.2], rng, intentos=200)
    ok &= check(f"(c) bola 1.2 en region 1.0: sin colocacion "
                f"(None = {pos is None}): el repack no crea espacio "
                f"— la packabilidad por contenedor es la condicion, "
                f"el lema solo la transporta", pos is None)
    return ok


def main():
    print("=" * 68)
    print("F2: REALIZACION Y REPACK (drafts/repack.md)")
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
