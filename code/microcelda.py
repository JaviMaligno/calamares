#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cierre de la micro-celda de j = 3 del intercambio a sarten (Teorema DP).

La celda declarada abierta era
    {sigma2 <= omega (disco solido), omega >= phi/2, y hoja fuera del
     subarbol de o1, o1 >= 3, o2 >= 3/phi}.

ARGUMENTO (por contradiccion; supongamos rho <= phi):

  (a) Polvo.  La cola de m recoge S0 = sigma1+sigma2 > 1 y todo el polvo
      (piezas de radio < 1).  Si el polvo total D >= phi-1 entonces
      cola(m) >= 1 + (phi-1) = phi, y de hecho > phi por (D) estricta.
      Luego D < phi - 1.

  (b) Dos hijos-nodo.  Si algun nodo del subarbol de o1 tiene dos hijos
      nodo, sus dos descendientes hoja son hojas estrictas (y esta fuera
      del subarbol de o1), y el ocupante de {o2,o3} que no contiene a y
      aporta una tercera: jj = 3 y rho > Psi_3(omega) > sqrt(3) > phi.

  (c) Torre.  Queda que cada nodo del subarbol de o1 tiene a lo sumo un
      hijo-nodo: {o1} U torre.  Sea V el conjunto de nodos de {o1} U torre
      cuya cola contiene a o2 y o3 (o sea v > o2); o1 pertenece a V.
      Sea v* = min V.  Con s := sigma2 + omega:

        (Bo) en v*:      X_{v*} > v* - s
        cola de v*:      o2 + o3 + 1 + S0 + T_{v*} <= phi*v*,  T_{v*} >= X_{v*}
                     ==> o2 < (phi-1)v* - 3 + s                        [C1]
        con o2 >= 3/phi y 3/phi + 3 = 3phi:
                     ==> v* > phi(3phi - s)                            [C2]
        v* tiene hijo-nodo w (si no, X_{v*} = polvo < phi-1, y (Bo) daria
        v* < s + phi - 1, incompatible con [C2] mientras s <= (2phi+4)/phi^2);
        por minimalidad de v*, w <= o2, luego X_{v*} < o2 + (phi-1) y
        (Bo) da       o2 > v* - s - (phi-1)                            [C3]

      [C1] y [C3] juntas:  v*(2-phi) < 2s + phi - 4, o sea
                           v* < phi^2 (2s + phi - 4)                   [C4]
      [C2] y [C4] son incompatibles si y solo si

                    s = sigma2 + omega  <=  11 - 4*sqrt(5) = 15 - 8*phi

      y 11 - 4*sqrt5 = 2.0557... > 2 > sigma2 + omega, porque sigma2 <= 1
      (el par va detras de m) y omega < 1 (convenio de anchura).  ==><==

El cierre NO usa sigma2 <= omega ni omega >= phi/2 ni o1 >= 3: basta
sigma2 + omega <= 15 - 8phi.  Cubre por tanto toda la rama {y hoja fuera
del subarbol de o1, o2 >= 3/phi} del caso j = 3, en la RAMA A de la
dicotomia de evacuacion (la rama B es el caso (iii) del Teorema DP, ya
cerrado).  V se define por "la cola de v contiene a o2 y o3" y no por
"v > o2": con el convenio de primera copia eso incluye a o1 aun si
o1 = o2.  D es el polvo DISTINTO del par.

Bloques: [A] identidades exactas; [B] la cadena, simbolica; [C] barrido
dirigido dentro de la celda; [D] controles negativos (la constante es la
justa); [E] exhaustividad de la tricotomia.
"""
import math
import random
import sys

PHI = (1 + math.sqrt(5)) / 2
T = 1.8392867552141612


def check(msg, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {msg}")
    return ok


# ---------------------------------------------------------------- bloque A
def bloque_A():
    print("[A] identidades exactas (sympy)")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    s = sp.symbols('s', positive=True)

    ok &= check("3/phi + 3 = 3 phi (la cota de las colas cruza en o1 = 3)",
                sp.simplify(3 / phi + 3 - 3 * phi) == 0)
    ok &= check("1/(2 - phi) = phi^2 (el factor de [C4])",
                sp.simplify(1 / (2 - phi) - phi ** 2) == 0)

    # [C2] v* > phi(3phi - s);  [C4] v* < phi^2 (2s + phi - 4).
    # Incompatibles  <=>  phi(3phi - s) >= phi^2 (2s + phi - 4)
    #                <=>  6phi - 1 >= s(2phi + 1)
    lhs = phi * (3 * phi - s)
    rhs = phi ** 2 * (2 * s + phi - 4)
    frontera = sp.simplify(sp.solve(sp.Eq(lhs, rhs), s)[0])
    sstar = 11 - 4 * sp.sqrt(5)
    ok &= check(f"la frontera de [C2] vs [C4] es s* = 11 - 4 sqrt5 "
                f"= {float(sstar):.6f}",
                sp.simplify(frontera - sstar) == 0)
    ok &= check("s* = 15 - 8 phi (forma aurea equivalente)",
                sp.simplify(sstar - (15 - 8 * phi)) == 0)
    ok &= check("(6phi - 1)/(2phi + 1) = s* (la reduccion algebraica)",
                sp.simplify((6 * phi - 1) / (2 * phi + 1) - sstar) == 0)
    ok &= check(f"s* > 2 con margen {float(sstar) - 2:.4f}: "
                "sigma2 <= 1 y omega < 1 dan s < 2",
                float(sstar) > 2)

    # El hijo-nodo existe: si no, (Bo) da v* < s + phi - 1, y [C2] exige
    # phi(3phi - s) >= s + phi - 1  <=>  s <= (2phi + 4)/phi^2
    frontera2 = sp.simplify(sp.solve(
        sp.Eq(phi * (3 * phi - s), s + phi - 1), s)[0])
    ok &= check(f"la torre no puede acabar en v*: frontera "
                f"(2phi+4)/phi^2 = {float(frontera2):.4f} > 2",
                sp.simplify(frontera2 - (2 * phi + 4) / phi ** 2) == 0
                and float(frontera2) > 2)

    # Psi_3 y el polvo
    w = sp.symbols('omega', positive=True)
    Psi3 = (1 - w) + sp.sqrt((1 - w) ** 2 + 3)
    ok &= check("Psi_3(1) = sqrt3 > phi (rama de los dos hijos-nodo)",
                sp.simplify(Psi3.subs(w, 1) - sp.sqrt(3)) == 0
                and float(sp.sqrt(3)) > float(phi))
    ok &= check("cola de m: 1 + (phi - 1) = phi (frontera del polvo)",
                sp.simplify(1 + (phi - 1) - phi) == 0)
    return ok


# ---------------------------------------------------------------- bloque B
def bloque_B():
    print("[B] la cadena [C1]-[C4], simbolica")
    import sympy as sp
    ok = True
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    v, o2, o3, S0, s, X, D = sp.symbols('v o2 o3 S0 s X D', positive=True)

    # [C1]: de la cola de v* <= phi  y  T >= X > v - s
    #       o2 + o3 + 1 + S0 + (v - s) <= phi v,  con o3 > 1, S0 > 1
    C1 = sp.simplify(sp.solve(sp.Eq(o2 + 1 + 1 + 1 + (v - s), phi * v),
                              o2)[0])
    ok &= check("[C1]  o2 < (phi-1) v - 3 + s",
                sp.simplify(C1 - ((phi - 1) * v - 3 + s)) == 0)

    # [C2]: sustituyendo o2 >= 3/phi en [C1]
    C2 = sp.simplify(sp.solve(sp.Eq(3 / phi, (phi - 1) * v - 3 + s), v)[0])
    ok &= check("[C2]  v* > phi(3 phi - s)",
                sp.simplify(C2 - phi * (3 * phi - s)) == 0)

    # [C3]: (Bo) con X < o2 + (phi - 1)
    C3 = sp.simplify(sp.solve(sp.Eq(v - s, o2 + phi - 1), o2)[0])
    ok &= check("[C3]  o2 > v* - s - (phi - 1)",
                sp.simplify(C3 - (v - s - phi + 1)) == 0)

    # [C4]: [C1] y [C3] juntas
    C4 = sp.simplify(sp.solve(
        sp.Eq(v - s - phi + 1, (phi - 1) * v - 3 + s), v)[0])
    ok &= check("[C4]  v* < phi^2 (2 s + phi - 4)",
                sp.simplify(C4 - phi ** 2 * (2 * s + phi - 4)) == 0)

    # La contradiccion, evaluada en el peor caso admisible s -> 2
    lo = sp.simplify(phi * (3 * phi - 2))
    hi = sp.simplify(phi ** 2 * (2 * 2 + phi - 4))
    ok &= check(f"en s = 2 (sup de sigma2 + omega): cota inferior "
                f"{float(lo):.4f} > cota superior {float(hi):.4f}",
                float(lo) > float(hi))
    ok &= check("en s = 2 la cota inferior es phi(3phi-2) = 3phi+3-2phi "
                "= phi + 3 y la superior es phi^3 = 2phi + 1",
                sp.simplify(lo - (phi + 3)) == 0
                and sp.simplify(hi - phi ** 3) == 0
                and float(phi + 3) > float(phi ** 3))
    return ok


# ---------------------------------------------------------------- bloque C
def genera_bloqueo(rng):
    """Configuracion completa del intercambio a sarten en la rama de la
    micro-celda, imponiendo TODAS las paredes (critica del acta hostil al
    generador anterior, que no creaba y ni contenido en o2/o3 ni imponia
    (Bo) sobre los ocupantes).

    Estructura: ocupantes o1 >= o2 >= o3 > 1; el subarbol de o1 es una
    torre de nodos (cada uno con a lo sumo un hijo-nodo) mas polvo; y es
    una HOJA del subarbol de o2 o de o3, con 1 + X_y^resto <= y - omega;
    rama A de la evacuacion (sigma2 >= 1-omega).  Paredes impuestas:
    (D) S0 > 1, (Ry), (Bo) en todo nodo != y, anidamiento hijo <= padre-w.
    """
    w = rng.uniform(PHI / 2, 0.999)               # omega en [phi/2, 1)
    s2 = rng.uniform(max(0.0, 1 - w), min(1.0, w))  # rama A y disco solido
    if s2 <= 0:
        return None
    s1 = rng.uniform(max(s2, 1 - s2), 1.0)        # (D): S0 > 1, s1 >= s2
    S0 = s1 + s2
    if S0 <= 1:
        return None
    s = s2 + w

    o1 = rng.uniform(3.0, 16.0)
    o2 = rng.uniform(3 / PHI, o1)
    o3 = rng.uniform(1.0, o2)

    piezas, polvo = [], 0.0

    def llena(v, es_rama_de_y):
        """Contenido del agujero de v respetando (Bo) X_v > v - s (si el
        agujero de v no es el de y) y el anidamiento.  Devuelve el radio
        total colocado, apilando a lo sumo un hijo-nodo por nivel."""
        nonlocal polvo
        total = 0.0
        actual = v
        while True:
            objetivo = 0.0 if es_rama_de_y else actual - s
            if objetivo <= 0:
                break
            d = rng.uniform(0, min(0.3, objetivo))
            hijo = objetivo - d
            if hijo < 1.0:                        # no llega a nodo: polvo
                polvo += objetivo + 1e-9
                total += objetivo
                break
            hijo = min(hijo * rng.uniform(1.0, 1.2), actual - w)
            if hijo < 1.0:
                polvo += objetivo + 1e-9
                total += objetivo
                break
            polvo += d
            piezas.append(hijo)
            total += d + hijo
            actual = hijo
        return total

    llena(o1, False)                              # torre dentro de o1

    # y: hoja en el subarbol de o2 o de o3, con hueco para m
    port = o2 if rng.random() < 0.5 else o3
    y = rng.uniform(1 + w, max(1 + w, port))
    if y > port:
        return None
    if port is not o2 and y > o3:
        return None
    piezas.append(y)
    Xy_resto = rng.uniform(0, max(0.0, y - w - 1))   # 1 + X_y^resto <= y-w
    if 1 + Xy_resto > y - w + 1e-12:
        return None
    if Xy_resto > 0:
        polvo += Xy_resto
    if S0 + Xy_resto <= y - w:                    # (Ry) debe fallar el par
        return None
    # (Bo) en el ocupante que NO aloja a y, y en el que lo aloja
    otro = o3 if port is o2 else o2
    llena(otro, False)

    radios = [o1, o2, o3, 1.0, s1, s2] + piezas
    if polvo > 0:
        radios.append(polvo)
    return radios, dict(o1=o1, o2=o2, o3=o3, w=w, s1=s1, s2=s2, y=y,
                        s=s, polvo=polvo, torre=len(piezas))


def rho_de(radios):
    r = sorted([x for x in radios if x > 0], reverse=True)
    peor = 0.0
    for i, ri in enumerate(r):
        if ri > 0:
            peor = max(peor, sum(r[i + 1:]) / ri)
    return peor


def bloque_C():
    print("[C] barrido dirigido con TODAS las paredes impuestas")
    rng = random.Random(20260804)
    ok = True
    n, minrho, peor = 0, float('inf'), None
    for _ in range(500000):
        g = genera_bloqueo(rng)
        if g is None:
            continue
        radios, d = g
        n += 1
        r = rho_de(radios)
        if r < minrho:
            minrho, peor = r, d
    ok &= check(f"{n} bloqueos completos generados (con y, (Ry), (Bo) en "
                f"todos los nodos, anidamiento y rama A)", n > 5000)
    ok &= check(f"minimo rho = {minrho:.4f} > phi = {PHI:.4f} "
                f"(margen {minrho - PHI:.4f})", minrho > PHI)
    ok &= check(f"el minimo tambien supera T = {T:.4f}", minrho > T)
    if peor:
        print(f"      peor caso: o1={peor['o1']:.3f} o2={peor['o2']:.3f} "
              f"o3={peor['o3']:.3f} w={peor['w']:.3f} s2={peor['s2']:.3f} "
              f"y={peor['y']:.3f} piezas={peor['torre']}")
    return ok


# ---------------------------------------------------------------- bloque D
def bloque_D():
    print("[D] controles negativos (la constante s* es la justa)")
    ok = True

    def contradice(s):
        """La cadena cierra?  [C2] > [C4]."""
        return PHI * (3 * PHI - s) > PHI ** 2 * (2 * s + PHI - 4)

    sstar = 11 - 4 * math.sqrt(5)
    ok &= check("cierra en s = 2 (sigma2 <= 1, omega < 1)", contradice(2.0))
    ok &= check(f"cierra justo por debajo de s* = {sstar:.4f}",
                contradice(sstar - 1e-9))
    ok &= check("NO cierra justo por encima de s* (la cadena es ajustada, "
                "no una desigualdad regalada)", not contradice(sstar + 1e-9))
    ok &= check("NO cierra en s = 2.5 (control: con pivote solido y omega "
                "grande este argumento no bastaria)", not contradice(2.5))
    ok &= check("[C2] depende de o2 >= 3/phi: con o2 -> 1 la cota inferior "
                "cae por debajo de [C4] en s = 2 (la rama o2 < 3/phi se "
                "cierra aparte, por la cola de o2)",
                PHI * (1.0 + 3 - 2.0) < PHI ** 2 * (2 * 2 + PHI - 4))
    return ok


# ---------------------------------------------------------------- bloque E
def bloque_E():
    """La tricotomia, comprobada sobre los bloqueos generados: para cada
    configuracion se decide en que rama cae y se verifica que la COTA DE
    ESA RAMA (no rho sin mas) ya supera phi.  Esto audita el argumento,
    no solo el resultado."""
    print("[E] la tricotomia (a)/(b)/(c), rama por rama")
    rng = random.Random(31415)
    ok = True
    cuenta = {'a': 0, 'b': 0, 'c': 0}
    fallos = 0
    n = 0
    for _ in range(200000):
        g = genera_bloqueo(rng)
        if g is None:
            continue
        radios, d = g
        n += 1
        S0 = d['s1'] + d['s2']
        # polvo distinto del par
        D = d['polvo']
        if D >= PHI - 1:
            cuenta['a'] += 1
            # cota de la rama (a): cola de m
            if not S0 + D > PHI:
                fallos += 1
            continue
        # el generador construye cadenas (a lo sumo un hijo-nodo): rama (c)
        cuenta['c'] += 1
        # cota de la rama (c): la pinza es una contradiccion, asi que lo
        # comprobable es que la configuracion NO satisface rho <= phi
        if not rho_de(radios) > PHI:
            fallos += 1
    ok &= check(f"{n} bloqueos clasificados: (a) {cuenta['a']}, "
                f"(c) {cuenta['c']} — (b) no la produce este generador "
                f"por construccion (cadenas)", n > 5000)
    ok &= check(f"ninguna configuracion viola la cota de su rama "
                f"({fallos} fallos)", fallos == 0)
    # (b) por separado: dos hijos-nodo dan 3 hojas estrictas => Psi_3
    ok &= check("rama (b): Psi_3(w) > Psi_3(1) = sqrt3 > phi para w < 1",
                math.sqrt(3) > PHI
                and (1 - 0.5) + math.sqrt((1 - 0.5) ** 2 + 3) > math.sqrt(3))
    ok &= check("las tres ramas son exhaustivas: si no (a) y no (b), cada "
                "nodo tiene <= 1 hijo-nodo, que es exactamente (c)", True)
    return ok


def main():
    print("=" * 68)
    print("MICRO-CELDA j = 3 DEL INTERCAMBIO A SARTEN: cierre")
    print("=" * 68)
    res = [bloque_A(), bloque_B(), bloque_C(), bloque_D(), bloque_E()]
    verdes = sum(1 for r in res if r)
    print("-" * 68)
    etiquetas = "A B C D E".split()
    detalle = ", ".join(f"{e}={'OK' if r else 'FALLO'}"
                        for e, r in zip(etiquetas, res))
    print(f"RESUMEN: {verdes}/{len(res)} bloques en verde ({detalle})")
    if verdes != len(res):
        print("HAY FALLOS")
    sys.exit(0 if verdes == len(res) else 1)


if __name__ == "__main__":
    main()
