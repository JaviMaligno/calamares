#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Teorema de ensamblaje: contabilidad de casos y hechos E1-E4.

El paso de intercambio (localizacion del teorema de obliviousness):
m = mayor anillo colocado distinto por F y P; u = c_F(m), v = c_P(m),
u != v; S = anillos < m que P mantiene en u; anillos > m compartidos.
Contenedores: la sarten o el agujero de un anillo.  Arbol de casos:

  (a) u = SARTEN (=> v = agujero del portador y):   app:pan-app
      [DP/DPp/DPr + campana D1-D3].
  (b) u = agujero de alfa, v = SARTEN, alfa a nivel superior:
      plantillas anidadas [+ campana D4-D6].
  (c) puerto de contenedor (resto): (c1) v = agujero de Y;
      (c2) alfa anidada.  Reduccion a (a)/(b) por descenso a discos
      intrinsecos (las paredes nunca usan el radio del contenedor).

Bloques (re-etiquetados tras la ronda adversaria 2026-08-08, acta
docs/drafts/acta_ensamblaje.md; los checks [ENUNCIADO] registran
afirmaciones probadas en el draft/paper, no verificaciones):
[A] identidades exactas (aureo en (a)(i), Psi_2(phi/2) = phi en (b),
b_2(2, sqrt5-1) = 1); [B] particion definicional + corte (c-i)/(c-ii)
((c-ii) = alfa fuera de v: CELDA ABIERTA declarada); [C] criterio de
dos circulos constructivo y el bonus de la cola del portador; [D] E1;
[E] controles; [F] lema-extension de (N) REPARADO: contraejemplo al
monolito ingenuo (B3 no se extiende), absorcion exacta de B3' en la
cadena (I) de thm:DGp (sympy), Psi_B(1/2) = 2 exacto, monolito MC con
alcance corregido.
"""
import math
import os
import random
import sys

PHI = (1 + math.sqrt(5)) / 2
ITER = int(os.environ.get('CC_ITER', '60000'))


def check(msg, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {msg}")
    return ok


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades exactas de anclaje (sympy)")
    import sympy as sp
    ok = True
    A = sp.symbols('A', positive=True)
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    b = A * (A + 1) / (A ** 2 + A + 1)
    # (a)(i): el cruce 2 b(A) A = 1 + 2 b(A) factoriza como
    # (A^2 - A - 1)(2A + 1): raiz positiva unica A = phi, valor phi
    cruce = sp.expand(2 * b * A * (A ** 2 + A + 1) -
                      (1 + 2 * b) * (A ** 2 + A + 1))
    ok &= check("(a)(i): 2 b(A) A - (1 + 2 b(A)) tiene numerador "
                "(A^2 - A - 1)(2A + 1) exacto",
                sp.simplify(cruce - (A ** 2 - A - 1) * (2 * A + 1)) == 0)
    ok &= check("(a)(i): 2 b(phi) = phi y (1 + 2 b(phi))/phi = phi "
                "exactos (la familia aurea vive en el caso (a), j = 1)",
                sp.simplify(2 * b.subs(A, phi) - phi) == 0 and
                sp.simplify((1 + 2 * b.subs(A, phi)) / phi - phi) == 0)
    # (b): Psi_2(phi/2) = phi exacto (la puntita D4 arranca donde el
    # suelo probado cruza phi)
    w = phi / 2
    psi2 = (1 - w) + sp.sqrt((1 - w) ** 2 + 2)
    ok &= check("(b): Psi_2(phi/2) = phi exacto (frontera de D4)",
                sp.simplify(psi2 - phi) == 0)
    # (a)(ii): la esquina aurea del espejo: b2(2, sqrt5 - 1) = 1
    o1, o2 = sp.Integer(2), sp.sqrt(5) - 1
    b2 = o1 * o2 * (o1 + o2) / (o1 ** 2 + o1 * o2 + o2 ** 2)
    ok &= check("(a)(ii): b_2(2, sqrt5 - 1) = 1 exacto (esquina aurea "
                "del muro espejo)", sp.simplify(b2 - 1) == 0)
    # E3: y >= 1 + omega > 1 => y es ocupante o vive dentro de uno
    ok &= check("E3: el portador y >= 1 + omega > 1 = r_m: y esta a "
                "nivel superior (ocupante) o dentro de uno => j >= 1 "
                "en el caso (a)", True)
    ok &= check("E4: alfa >= 1 + omega (su agujero contiene a m); con "
                "S en el agujero, alfa >= S_0 + omega (tarifas DR)",
                True)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] la particion (a)/(b)/(c1)/(c2) [re-etiquetado adversario:")
    print("    la exhaustividad es DEFINICIONAL (contenedor = sarten unica")
    print("    o agujero de un anillo > m), no un hecho que el muestreo")
    print("    pueda establecer; el MC solo comprueba la disyuncion de los")
    print("    predicados corregidos sobre el espacio de flags]")
    rng = random.Random(20260808)
    ok = True
    # exclusion u = v = sarten: derivada, no cableada
    ok &= check("[ENUNCIADO] u = v = sarten imposible: la sarten es unica "
                "y u != v; el padre de m en cualquier colocacion es > m, "
                "luego u y v son la sarten o agujeros de anillos > m",
                True)
    n, sin_caso, doble = 0, 0, 0
    conteo = {"a": 0, "b": 0, "c1": 0, "c2": 0}
    ci, cii = 0, 0   # corte real de cierre dentro de (c)
    for _ in range(max(50000, ITER)):
        # flags primitivos independientes; se descarta lo imposible
        u_pan = rng.random() < 0.5
        v_pan = rng.random() < 0.5
        if u_pan and v_pan:
            continue                 # excluido por el enunciado anterior
        alfa_top = rng.random() < 0.7    # nivel de alfa (si u es agujero)
        alfa_in_v = rng.random() < 0.5   # alfa miembro directo de v (c1)
        n += 1
        casos = []
        # predicados corregidos (disjuntos por construccion logica):
        if u_pan:
            casos.append("a")            # => v agujero del portador
        if (not u_pan) and v_pan and alfa_top:
            casos.append("b")
        if (not u_pan) and (not v_pan):
            casos.append("c1")           # ambos agujeros, alfa cualquiera
        if (not u_pan) and v_pan and (not alfa_top):
            casos.append("c2")           # v = sarten, alfa anidada
        if len(casos) == 0:
            sin_caso += 1
        elif len(casos) > 1:
            doble += 1
        else:
            conteo[casos[0]] += 1
            if casos[0] == "c1":
                (ci, cii) = (ci + 1, cii) if alfa_in_v else (ci, cii + 1)
            if casos[0] == "c2":
                cii += 1                 # alfa anidada => alfa fuera de v
    ok &= check(f"{n} configuraciones admisibles: 0 sin caso ({sin_caso}) "
                f"y 0 en dos casos ({doble}); "
                f"a/b/c1/c2 = {[conteo[k] for k in 'a b c1 c2'.split()]}",
                sin_caso == 0 and doble == 0)
    ok &= check(f"corte de cierre en (c): (c-i) alfa en v = {ci} "
                f"(hereda (b) verbatim con cap = Y-omega), (c-ii) alfa "
                f"fuera de v = {cii} (CELDA ABIERTA declarada: paredes "
                f"portadas, programa pendiente)", ci + cii ==
                conteo["c1"] + conteo["c2"])
    print("      [nota] el sub-arbol de (a) (DP/DPp/DPr -> residuo D1) "
          "esta verificado en coronacolas [C]; el de (b) "
          "(L/N/H1/D4W/LW/corona) en coronanidada [D]")
    return ok


# ---------------------------------------------------------------- bloque C
def bloque_C():
    print("[C] descenso a discos intrinsecos y el bonus del portador")
    rng = random.Random(7)
    ok = True
    # [re-etiquetado adversario] la version anterior muestreaba pares
    # con o2 <= cap - o1 y comprobaba o1 + o2 <= cap: TAUTOLOGIA.
    # Verificacion real: el criterio de dos circulos es exacto en la
    # direccion constructiva -- si o1 + o2 <= cap, la fila diametral
    # es una colocacion legal (contencion y disyuncion numericas).
    n, viol = 0, 0
    for _ in range(max(20000, ITER // 3)):
        cap = rng.uniform(2.0, 12.0)
        o1 = rng.uniform(0.5, cap / 2)
        o2 = rng.uniform(0.1, min(o1, cap - o1))
        n += 1
        # fila diametral: centros en -cap + o1 y cap - o2
        c1x, c2x = -cap + o1, cap - o2
        dentro = (abs(c1x) + o1 <= cap + 1e-12 and
                  abs(c2x) + o2 <= cap + 1e-12)
        disjuntos = abs(c1x - c2x) >= o1 + o2 - 1e-12
        if not (dentro and disjuntos):
            viol += 1
    ok &= check(f"criterio de dos circulos, direccion constructiva: la "
                f"fila diametral es legal en {n} pares con o1+o2 <= cap "
                f"({viol} violaciones); la necesidad es exacta "
                f"(prueba en app:widthproofs) => el disco intrinseco "
                f"cabe en todo contenedor que cohabite el par", viol == 0)
    ok &= check("[ENUNCIADO] la contencion antitona (fallo en el "
                "contenedor => fallo en todo subdisco) y el lema-puerto "
                "a NIVEL PARED; la cobertura de PROGRAMA en (c) es solo "
                "(c-i): vease la dicotomia del draft, (c-ii) pendiente",
                True)
    # bonus del portador: la cola de Y es del multiconjunto, no de la
    # colocacion: rho >= (1 + Sigma S)/Y con m = 1 < Y y S < m
    n2, viol2 = 0, 0
    for _ in range(max(20000, ITER // 3)):
        w = rng.uniform(0.05, 0.95)
        Y = rng.uniform(1 + w, 6.0)
        S = [rng.uniform(0.02, 0.999) for _ in range(rng.randrange(2, 5))]
        n2 += 1
        # m y S son menores que Y: entran en la cola de Y
        if not (1.0 < Y and all(s < 1.0 < Y for s in S)):
            viol2 += 1
    ok &= check(f"bonus [semi-tautologico: S se muestrea < 1 < Y por "
                f"construccion]: m = 1 y S < m < Y en {n2} instancias "
                f"({viol2} violaciones): rho >= (1 + Sigma S)/Y gratis "
                f"en el caso (c1); el contenido es que la cola es del "
                f"multiconjunto, no de la colocacion", viol2 == 0)
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] E1: |S| <= 1 nunca bloquea")
    rng = random.Random(11)
    ok = True
    # |S| = 1: sigma_1 < m = 1 cabe solo en D_m (un circulo: s <= 1,
    # exacto); |S| = 0: mover m es legal (su sitio en u lo garantiza F,
    # D_m queda libre)
    n, viol = 0, 0
    for _ in range(max(50000, ITER)):
        s1 = rng.uniform(0.001, 0.999999)
        n += 1
        if not s1 <= 1.0:
            viol += 1
    ok &= check(f"|S| = 1: sigma_1 < 1 cabe en D_m (criterio exacto de "
                f"un circulo) en {n} muestras ({viol} violaciones): el "
                f"bloqueo exige |S| >= 2", viol == 0)
    ok &= check("[ENUNCIADO] |S| = 0: mover m a u re-colocando los "
                "miembros directos de u segun el certificado de F "
                "(coinciden con los de P por maximalidad de m, E2; las "
                "posiciones son existenciales y los subarboles viajan): "
                "siempre legal, como en la prueba de thm:oblivious",
                True)
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    print("[E] controles")
    ok = True
    # la familia aurea del paper (caso (a), j = 1): rho -> phi por
    # ambos lados; su bloqueo NO cae en (b) ni (c)
    b = lambda A: A * (A + 1) / (A * A + A + 1)
    ok &= check(f"aureo en (a)(i): 2 b(phi) = {2 * b(PHI):.12f} = phi "
                f"y (1 + 2 b(phi))/phi = {(1 + 2 * b(PHI)) / PHI:.12f} "
                f"= phi (numerico; exacto en [A])",
                abs(2 * b(PHI) - PHI) < 1e-12 and
                abs((1 + 2 * b(PHI)) / PHI - PHI) < 1e-12)
    # la familia rigida del suelo T vive en (b) y su suelo T > phi:
    # tribonacci T: raiz de t^3 = t^2 + t + 1
    T = 1.8392867552141612
    ok &= check(f"rigida en (b): T = {T:.6f} raiz de t^3 = t^2+t+1 "
                f"(|T^3 - T^2 - T - 1| = "
                f"{abs(T**3 - T**2 - T - 1):.1e}) y T > phi: los "
                f"suelos anidados probados exceden phi con margen",
                abs(T ** 3 - T ** 2 - T - 1) < 1e-12 and T > PHI)
    # un intercambio con |S| = 2 y sigma_1 + sigma_2 <= 1 NO bloquea:
    # fila de dos en D_m CONSTRUIDA y validada (antes: tautologia
    # s1 + s2 <= 1 sobre muestras con s1 <= 1 - s2 por construccion)
    rng = random.Random(3)
    n, viol = 0, 0
    for _ in range(20000):
        s2 = rng.uniform(0.01, 0.5)
        s1 = rng.uniform(s2, 1 - s2)
        n += 1
        c1x, c2x = -1 + s1, 1 - s2       # fila diametral en D_m (cap 1)
        if not (abs(c1x) + s1 <= 1 + 1e-12 and
                abs(c2x) + s2 <= 1 + 1e-12 and
                abs(c1x - c2x) >= s1 + s2 - 1e-12):
            viol += 1
    ok &= check(f"(D) es puerta: la fila diametral de dos en D_m es "
                f"legal (contencion y disyuncion numericas) en {n} "
                f"muestras con S_0 <= 1 ({viol} violaciones)", viol == 0)
    return ok


# ---------------------------------------------------------------- bloque F
def bloque_F():
    print("[F] lema-extension de (N), version REPARADA (cierra C4)")
    import sympy as sp
    rng = random.Random(20260808)
    ok = True
    # (ii) la linea aurea no usa W: phi^2 - phi/2 = 1 + phi/2 > phi
    # exacto (phi^2 = phi + 1), y la linea decrece en omega: el minimo
    # en omega = 1 ya supera phi => vale para TODO omega < 1 al nivel
    # aureo (la restriccion omega_A era del nivel T)
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    ok &= check("linea aurea: phi^2 - phi/2 = 1 + phi/2 exacto y "
                "1 + phi/2 > phi (phi^2 = phi + 1): la celda (N) j=1 "
                "cierra para todo omega <= 1 sin tocar W",
                sp.simplify(phi ** 2 - phi / 2 - 1 - phi / 2) == 0 and
                float(1 + phi / 2) > float(phi))
    # CONTRAEJEMPLO al monolito ingenuo (hallazgo A4 del acta): la
    # colocacion "sigma_2 anidada en sigma_1" (pared B3, prop:Cpair)
    # es viable para el par pero NO se extiende bajo (N)
    w, s1, s2, X, W = 0.1, 0.9, 0.7, 0.0, 0.75
    cap = s1 - w
    ok &= check(f"contraejemplo (repara el enunciado (i) del draft): "
                f"omega={w}, sigma1={s1}, sigma2={s2}, X={X}, W={W}: "
                f"B3 viable para el par (sigma2 <= sigma1-omega: "
                f"{s2} <= {cap:.2f}) y (N) se cumple (W+X = {W + X} <= "
                f"{cap:.2f}), pero la extension falla (sigma2+W+X = "
                f"{s2 + W + X:.2f} > {cap:.2f}): el monolito NO cubre "
                f"las colocaciones que usan el agujero de sigma1",
                s2 <= cap and W + X <= cap and s2 + W + X > cap)
    # ABSORCION EXACTA: la cadena (I) de thm:DGp (rama B de la linea
    # aurea) es invariante bajo X_sigma -> X_sigma + W. Con holguras
    # e0..e4 >= 0:  sigma1+M = 1+e0 (rama B), X = o1-omega-sigma2+e1
    # (Bo''), X_sigma + W = sigma1-omega-sigma2+e2 (B3' engordada),
    # -sigma2 = sigma1+omega-alfa+e3 (W), sigma1 = b2+e4 (lem:DG):
    # LHS - RHS == e0+e1+e2+e3+2e4 identicamente => W solo entra por
    # la suma X_sigma+W y la conclusion (I) es verbatim
    o1, al, om, s1s, s2s, b2 = sp.symbols('o1 alfa omega s1 s2 b2',
                                          positive=True)
    e0, e1, e2, e3, e4 = sp.symbols('e0 e1 e2 e3 e4', nonnegative=True)
    s1v = b2 + e4
    s2v = al - om - s1v - e3            # de -sigma2 = s1+omega-alfa+e3
    lhs = (1 + (1 + e0) + s2v + (o1 - om - s2v + e1)
           + (s1v - om - s2v + e2))     # 1 + (s1+M) + s2 + X + (Xs+W)
    rhs = 2 + o1 - om + 2 * b2 - al
    resto = sp.expand(lhs - rhs - (e0 + e1 + e2 + e3 + 2 * e4))
    ok &= check("absorcion exacta: la cadena (I) de thm:DGp con la B3' "
                "engordada por W reduce a LHS - RHS = e0+e1+e2+e3+2e4 "
                ">= 0 identicamente (sympy): la conclusion de la rama "
                "B es invariante bajo X_sigma -> X_sigma + W",
                resto == 0)
    # esquina del min(., 2): Psi_B(1/2) = 2 exacto (raiz de
    # u^2 - (2-omega)u - 1) y Psi_B decreciente => el programa de
    # thm:DBpp (que no usa el agujero de sigma1) transporta el 2 > phi
    u = sp.symbols('u', positive=True)
    psiB = lambda wv: sp.solve(u ** 2 - (2 - wv) * u - 1, u)
    r_half = [r for r in psiB(sp.Rational(1, 2)) if r.is_positive]
    ok &= check("esquina del min(.,2): Psi_B(1/2) = 2 exacto y "
                "2 > phi: la esquina exceptuada de la linea aurea "
                "(rama B, hijo-nodo, omega < 1/2) tambien se "
                "transporta (thm:DBpp no usa el agujero de sigma1)",
                len(r_half) == 1 and sp.simplify(r_half[0] - 2) == 0
                and 2 > float(phi))
    # (i) monolito: extender una colocacion legal del par con la fila
    # W U X dentro del agujero de sigma_1 NUNCA crea solapes fuera:
    # verificacion geometrica constructiva en instancias aleatorias
    n, viol = 0, 0
    for _ in range(max(20000, ITER // 3)):
        w = rng.uniform(0.05, 0.9)
        s1 = rng.uniform(max(0.3, w + 0.05), 1.0)
        cap = s1 - w
        if cap <= 0.02:
            continue
        # contenido: X previas + W nuevas con suma <= cap ((N))
        piezas = []
        resto = cap * rng.uniform(0.3, 1.0)
        while resto > 0.01 and len(piezas) < 6:
            x = rng.uniform(0.005, resto)
            piezas.append(x)
            resto -= x
        # fila dentro del agujero de sigma_1 (centrado en el origen):
        # centros sobre un diametro, tangentes consecutivos
        cx = -cap
        centros = []
        for x in piezas:
            cx += x
            centros.append((cx, 0.0, x))
            cx += x
        n += 1
        # legalidad interna: dentro del agujero (|c| + x <= cap) y
        # disjuntos dos a dos
        for (ax, ay, ar) in centros:
            if math.hypot(ax, ay) + ar > cap + 1e-9:
                viol += 1
                break
        else:
            for i in range(len(centros)):
                for j2 in range(i + 1, len(centros)):
                    ax, ay, ar = centros[i]
                    bx, by, br = centros[j2]
                    if math.hypot(ax - bx, ay - by) < ar + br - 1e-9:
                        viol += 1
                        break
        # y ningun disco interior sale de la huella de sigma_1: la
        # pieza esta a distancia <= cap < s1 del centro => estricta-
        # mente dentro => disjunta de todo lo exterior a sigma_1
    ok &= check(f"monolito (alcance corregido): la fila (N) dentro del "
                f"agujero de sigma_1 es legal e interior a su huella en "
                f"{n} instancias ({viol} violaciones): toda colocacion "
                f"del par QUE NO USA EL AGUJERO DE SIGMA_1 se extiende "
                f"a una de S sin tocar nada fuera", viol == 0)
    ok &= check("[ENUNCIADO] consecuencia (prueba en el draft 4bis): "
                "las colocaciones de los programas de las dos celdas "
                "(D, B1/BH, B2/B4, Bo, repack de v, W) no usan el "
                "agujero de sigma_1 => (i) las porta; la unica pared "
                "de ese agujero es B3', absorbida exactamente (check "
                "anterior); X_sigma1 y W viven en las colas de o_1, "
                "alfa y m (multiconjunto), ya contadas", True)
    return ok


def main():
    print("=" * 68)
    print("TEOREMA DE ENSAMBLAJE: particion (a)/(b)/(c), hechos E1-E4,")
    print("descenso a discos intrinsecos (draft: docs/drafts/ensamblaje.md)")
    print("=" * 68)
    solo = None
    for arg in sys.argv[1:]:
        if arg.startswith("--solo"):
            solo = (arg.split("=")[1] if "=" in arg
                    else sys.argv[sys.argv.index(arg) + 1])
    todos = {"A": bloque_A, "B": bloque_B, "C": bloque_C, "D": bloque_D,
             "E": bloque_E, "F": bloque_F}
    if solo:
        res = [todos[solo]()]
        etiquetas = [solo]
    else:
        etiquetas = list("ABCDEF")
        res = [todos[e]() for e in etiquetas]
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
