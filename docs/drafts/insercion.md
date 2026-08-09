# El lema de inserción por medida y el teorema D1 escrito

Estado: DRAFT con pruebas (2026-08-09), ADVERSARIADO (acta en
VEREDICTOS.md, misma fecha). Script: `code/insercion.py` (7/7). Es el
paso (2) del programa de compactación: convierte la celda D1 (y D3)
en TEOREMA escrito, sin barridos, con el estatus de cada pieza
declarado (qué es exacto y qué es numérico-certificado).

## 1. Lema A (inserción por medida de arcos prohibidos)

**Lema A.** Sea P un empaquetamiento de la familia F = {x₁, …, x_n}
en el disco R y sea s un círculo en régimen apilable con cada pieza,

    R > 2s + x_i   para todo i,                       (régimen)

cuyas SOMBRAS suman menos que el círculo:

    Σ_i 2·Θ_i < 2π,   Θ_i := arcsin((s+x_i)/(R−s)).

Entonces existe un empaquetamiento de F ∪ {s} en R que NO MUEVE
ninguna pieza de P: s se coloca mural (tangente a la pared) en un
ángulo libre. (El régimen garantiza además (s+x_i)/(R−s) < 1: los
arcsin están definidos sin capar.)

*Prueba.* Colóquese s mural en el ángulo ψ: centro
c_s(ψ) = (R−s)(cos ψ, sin ψ). Para la pieza x_i, con centro real a
distancia d_i ∈ (0, R−x_i] del origen y ángulo ψ_i, el conflicto
s–x_i es |c_s(ψ) − c_i| < s+x_i, y por la ley de cosenos equivale a

    cos γ(ψ, ψ_i) > h(R−s, d_i),
    h(u, v) = (u² + v² − w²)/(2uv),   w := s + x_i, u := R−s

(identidad exacta: w² − |c_s−c_i|² = 2uv(cos γ − h); script, bloque
A1). El ARCO PROHIBIDO de x_i es A_i = {ψ: cos γ(ψ,ψ_i) > h(u, d_i)},
de semi-anchura arccos h(u, d_i) (0 si h ≥ 1, π si h ≤ −1). Sobre
v ∈ (0, ∞), ∂h/∂v = (v² − u² + w²)/(2uv²) tiene un único cero
v* = √(u²−w²) (mínimo global de h, pues bajo el régimen u > w los
extremos dan h → +∞ en v → 0⁺), con

    h(u, v*) = √(u²−w²)/u = cos(arcsin(w/u)) = cos Θ_i   exacto.

Luego h(u, d_i) ≥ cos Θ_i para TODA profundidad admisible d_i — si
v* cae fuera de (0, R−x_i] la cota solo mejora (el mínimo global
sigue minorando el rango restringido; en ese caso el máximo real del
arco es el extremo mural θ_R(s,x_i) < Θ_i) — y |A_i| ≤ 2Θ_i
uniformemente en la profundidad. Con Σ 2Θ_i < 2π la unión ∪A_i no
cubre el círculo: existe ψ libre, y en él s mural es disyunta de
todas las piezas (y está dentro del disco: tangente interior). ∎

**El enunciado con θ murales es FALSO (control A6).** La versión con
Σ 2·θ_R(s, x_i) < 2π (θ_R el ángulo mural de lem:S1,
sin²(θ_R/2) = f(s)f(x)) en lugar de las sombras NO es un lema:
contraejemplo con n = 1, R = 3, x = 2.2 a profundidad d = 0.1,
s = 0.5 — par no apilable (R < 2s+x), Σ 2θ_R = 3.34 < 2π, y sin
embargo (R−s)+d = 2.6 < s+x = 2.7: TODO ángulo mural está en
conflicto y la inserción es imposible (script, bloque A6). Sin la
hipótesis de régimen una pieza PROFUNDA prohíbe arcos de hasta π
(control A4); los regímenes R ≷ x_i + 2s son mutuamente excluyentes
y el lema usa SOLO sombras con R > 2s + x_i por pieza — que el
dominio garantiza (§2, (b')).

Notas: Θ_i ≥ θ_R(s, x_i) siempre (la sombra domina al mural, por ser
cos Θ el mínimo global de h y cos θ_R su valor mural); la sombra
decrece en R y crece en s y en x_i (∂ exactas); el lema no mueve
ninguna pieza ni usa hipótesis alguna sobre el empaquetamiento P.

## 2. Lema B (el presupuesto de la celda D1/D3)

En la celda {p ≥ 4, σ₁+M ≤ 1, j ≥ 3} (heredera de thm:DPr, que trae
σ₂ ≤ φ−1: la rama σ₂ > φ−1 con σ₁+W > 1 la cierra thm:DPp(iii) por
masa, y la ligera/anidada con ω ∈ (0,1) la cierran thm:DPp(i)-(ii))
y en D3 = {ω ≥ 1, j ≥ 3} (donde σ₂ ≤ φ−1 NO está disponible: véase
(d)), con ρ ≤ φ y las colas en cascada:

  (a) masa pequeña total ≤ φ: la cola de m recoge TODAS las piezas
      < r_m = 1 del multiconjunto — el perfil entero, el polvo, los
      extras, M y los contenidos de agujeros X. Con (D) σ₁+σ₂ > 1,
      la masa A INSERTAR en la sartén, W' := (perfil ∖ {σ₁,σ₂}) +
      polvo + extras en sartén, cumple
      W' ≤ φ − σ₁ − σ₂ − (M + X's) ≤ φ − σ₁ − σ₂ < φ − 1 = 1/φ
      (las masas descontadas son ≥ 0: contabilidad conservadora).
  (b) los mínimos de la cascada: o_j ≥ (1+Σ)/φ ≥ 2/φ, o₂ ≥ 1+Σ ≥ 2
      (exacto con j ≥ 3, identidad φ² = 1+φ; script F2), o₁ ≥ 2φ,
      R ≥ o₁+o₂ ≥ 2φ+2; masa acumulada T_k ≤ T₃/φ^{k−3}
      (decaimiento geométrico EXACTO: T_k ≥ φT_{k+1}).
  (b') RÉGIMEN SOMBRA en todo el dominio: para toda pieza x ≤ o₁ del
      presupuesto y todo insertando s ≤ φ−1:
      R − 2s − x ≥ (o₁+o₂) − 2s − o₁ = o₂ − 2s ≥ 2 − 2(φ−1)
      = 2(2−φ) > 0 exacto; en la rama (d), con s = σ₂ ≤ φ/2 y
      Σ ≥ 2s, o₂ − 2s ≥ 1 + Σ − 2s ≥ 1 > 0 exacto.
  (c) presupuesto de sombras (D1, s ≤ φ−1): Σ_{x ∈ O∪{m}}
      2·arcsin((s+x)/(R−s)) evaluado en s = φ−1 (mayorante: la
      sombra crece en s) + [segunda inserción del círculo-fila
      w* = W' ≤ 1/φ, con σ₂ ya contada] < 2π en todo el dominio.
      Estatus por dirección:
      - R: EXACTO — la sombra decrece en R, R = o₁+o₂ es el peor.
      - o₂: EXACTO — la derivada del presupuesto en o₂ (con R =
        o₁+o₂ acoplado) es negativa: el término propio
        (u−w₂)/√(u²−w₂²) queda dominado por el solo término de o₁,
        w₁/√(u²−w₁²), pues u−w₂ = o₁−2s < o₁+s = w₁ y w₂ ≤ w₁
        (script, bloque D). El mínimo de o₂ es el peor.
      - o₁: el presupuesto NO es monótono — es BAÑERA exacta:
        N_i²/P² es estrictamente decreciente en o₁ (derivada
        racional con numerador 2w²(s²−o₁²−o₁o₂−o₂s−w²) < 0 y
        denominador (o₂−2s)(u²−w²)² > 0), luego el gradiente cambia
        de signo a lo sumo una vez (− → +) y el sup en la dirección
        o₁ es max(esquina, lim_{o₁→∞}) con límite = π < 2π exacto
        (script, bloque D). La afirmación ingenua «el mínimo de o₁
        es el peor» es falsa en general; el sup direccional queda
        acotado igualmente.
      - resto de direcciones (o₃.., m, Σ, j): NUMÉRICO-CERTIFICADO —
        el presupuesto CRECE en o_k (k ≥ 3), así que el sup vive en
        las caras de la cascada; optimización dirigida (coordinate
        ascent proyectado al politopo, multistart, j ≤ 8, Σ ∈
        [1, φ]) da sup = 4.7134 ≤ esquina y sondeo con holguras
        4.52 (bloques G1, D). El sup del dominio es la esquina
        j = 3, Σ → 1, mínimo (2φ, 2, 2/φ, m = 1), R = 2φ+2:
        4.7225 (σ₂) y 5.2644 (w*, con σ₂ contada), márgenes 1.56 y
        1.02 (bloque C, alta precisión). La cola j > 3 del mínimo
        decae geométricamente (razón ~φ^{−1/2}): j desaparece.
  (d) rama D3 con σ₂ ∈ (φ−1, 1) (sin thm:DPr disponible, p.ej.
      light σ₁+W ≤ 1 con ω ≥ 1): dos pasos.
      - σ₂ > φ/2 es VACÍA con ρ ≤ φ: cola(m) ≥ σ₁+σ₂ ≥ 2σ₂ > φ,
        exacto (bloque F1).
      - σ₂ ∈ (φ−1, φ/2]: presupuesto PARAMÉTRICO en s = σ₂ con la
        ligadura de masa Σ ≥ σ₁+σ₂ ≥ 2s, que engorda la cascada
        (o₂ ≥ 1+Σ ≥ 1+2s, F2) y agranda R: sup de la curva
        (mínimos de cascada, j = 3..8) 4.6144 (σ₂) y 4.9267 (w*),
        y sup optimizado con ligadura 4.60 < 2π, con el máximo en
        la esquina s = φ/2, Σ = φ, o = (φ³, φ², φ) (bloques F3-F4;
        numérico-certificado con margen ≥ 1.36).

## 3. Teorema D1-escrito

**Teorema.** En la celda {p ≥ 4, σ₁+M ≤ 1, j ≥ 3} de la sartén (y
en el régimen de pivote sólido ω ≥ 1, j ≥ 3, todo p), ρ ≤ φ implica
que el intercambio no se bloquea.

*Prueba.* El bloqueo exige que falle toda colocación con los
recursos. Constrúyase la colocación testigo:
(1) la sartén entera según el certificado de F: cuando F colocó m a
    nivel superior, la sartén contenía exactamente O ∪ {m} (los
    anillos > 1, compartidos con P), y F certificó ese
    empaquetamiento; cada ocupante viaja con su subárbol de P rígido
    dentro (el anidamiento es relativo al portador), m viaja con M
    dentro, y el portador y — ocupante o anidado en uno — conserva
    X_y^rest en su agujero, dejando vacante el disco unidad D_m
    (lem:row, segunda parte; como en la prueba de thm:oblivious);
(2) σ₁ → D_m (fila de uno, σ₁ ≤ 1, siempre legal; en la rama light
    de D3, σ₁ lleva además la fila {σ₁, W} con σ₁+W ≤ 1);
(3) σ₂ mural por el Lema A: presupuesto (c) si σ₂ ≤ φ−1, presupuesto
    paramétrico (d) si no (solo puede ocurrir en D3, y σ₂ ≤ φ/2);
(4) el resto del perfil + polvo + extras en sartén, de masa
    W' ≤ 1/φ (a), como círculo-fila w* (lem:row: piezas de radio
    total ≤ w* caben en el disco de radio w*; el disco virtual
    tangente a la pared es disjunto de todo lo exterior, luego las
    piezas reales dentro también) insertado mural por el Lema A de
    nuevo, con la sombra de σ₂ ya contada en el presupuesto.
σ₂ y w* son disjuntos de σ₁ y de los subárboles automáticamente:
las inserciones murales son disjuntas de cada pieza de nivel
superior, y los contenidos viven en el interior de sus portadores.
Todas las piezas de S⁺ quedan colocadas: no hay bloqueo. ∎

Uniformidades: j NO aparece (la cascada acota la serie para todo j);
p y k no aparecen (masa, no cantidad); ω no se usa (D3 incluido:
D_m existe con ω ≥ 1 y H_m no se usa en ningún paso); σ₁+M ≤ 1
tampoco se usa (M viaja dentro de m): la construcción cubre de hecho
{j ≥ 3, σ₂ ≤ φ−1, heavy} para toda p y todo ω, y la celda enunciada
con holgura.

Estatus epistémico: los eslabones geométricos (Lema A, régimen,
contabilidad de masa, direcciones R y o₂, bañera de o₁, vacuidad
σ₂ > φ/2, o₂ ≥ 1+Σ) son EXACTOS; el sup del presupuesto sobre las
direcciones restantes del politopo (o₃.., Σ, j y la rama (d)) es
numérico-certificado por esquinas de alta precisión + optimización
dirigida + esquinas euclidianas deterministas (bloques C, D, F, G),
con margen mínimo 1.02. El cierre plenamente formal de ese sup es un
lema de optimización pendiente (análogo al de la ley de escala).

## 4. Qué queda para el resto de dominios

El mismo patrón (inserción por medida + presupuesto por esquinas)
para: D4-D6 (plantilla anidada: contenedor = disco de capacidad
α−ω o z−ω; las mismas dos inserciones), (c-i)/(c-ii)/R2b (los
presupuestos ya están delimitados por las pinzas de las campañas), y
la V-condición desaparece (no hay corona que validar: nada se mueve).
