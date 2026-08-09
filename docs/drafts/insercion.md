# El lema de inserción por medida y el teorema D1 escrito

Estado: DRAFT con pruebas (2026-08-09), PRE-ADVERSARIO. Script:
`code/insercion.py`. Es el paso (2) del programa de compactación:
convierte la celda D1 (y D3) en TEOREMA escrito, sin barridos.

## 1. Lema A (inserción por medida de arcos prohibidos)

**Lema A.** Sea P un empaquetamiento de la familia F = {x₁, …, x_n}
en el disco R y sea s un círculo con s ≤ R y

    Σ_i 2·θ_R(s, x_i) < 2π,

donde sin²(θ_R(a,b)/2) = f(a)f(b), f(x) = x/(R−x), θ capado a π.
Entonces existe un empaquetamiento de F ∪ {s} en R que NO MUEVE
ninguna pieza de P: s se coloca mural (tangente a la pared) en un
ángulo libre.

*Prueba.* Colóquese s mural en el ángulo ψ: centro
c_s(ψ) = (R−s)(cos ψ, sin ψ). Para la pieza x_i, con centro real a
distancia d_i ∈ (0, R−x_i] del origen y ángulo ψ_i, el conflicto
s–x_i es |c_s(ψ) − c_i| < s+x_i, y por la ley de cosenos equivale a

    cos γ(ψ, ψ_i) > h(R−s, d_i),
    h(u, v) = (u² + v² − w²)/(2uv),   w := s + x_i, u := R−s.

El ARCO PROHIBIDO de x_i es A_i = {ψ: cos γ(ψ,ψ_i) > h(u, d_i)},
de semi-anchura arccos h(u, d_i) (0 si h ≥ 1, π si h ≤ −1). El sup
de esa semi-anchura sobre TODAS las profundidades d_i, bajo la
hipótesis de régimen u > w (es decir R > 2s + x_i), es la SOMBRA

    Θ_i := arcsin(w/u) = arcsin((s+x_i)/(R−s)):

∂h/∂v = (v² − u² + w²)/(2uv²) tiene un único cero
v* = √(u²−w²) ∈ (0, u) (mínimo interior de h), con
h(u, v*) = √(u²−w²)/u = cos(arcsin(w/u)) exacto; en los extremos
h → +∞ (v → 0, pues u > w) y h(u, R−x_i) = cos θ_R(s,x_i) ≥
cos Θ_i. Luego |A_i| ≤ 2Θ_i uniformemente en la profundidad. Con
Σ 2Θ_i < 2π la unión ∪A_i no cubre el círculo: existe ψ libre, y en
él s mural es disyunta de todas las piezas (y está dentro del disco:
tangente interior). ∎

**La versión ingenua es falsa (control A4).** Sin la hipótesis de
régimen (si R < x_i + 2s, el par s–x_i no-apilable), una pieza
PROFUNDA prohíbe arcos de hasta π ≫ θ mural: la cota
«uniforme-en-profundidad = θ» no existe. Los dos regímenes son
mutuamente excluyentes (R ≷ x_i + 2s), y el lema usa SOLO la sombra,
con R > 2s + x_i por pieza — que el dominio garantiza (§2).

Nota: Θ_i ≥ θ_R(s, x_i) siempre (la sombra domina al mural), la
sombra decrece en R, y el lema NO mueve ninguna pieza ni usa
hipótesis alguna sobre el empaquetamiento P.

## 2. Lema B (el presupuesto de la celda D1/D3)

En la celda {p ≥ 4, σ₁+M ≤ 1, j ≥ 3} (y en D3, sin usar ω) con
ρ ≤ φ y las colas en cascada:

  (a) masa pequeña total ≤ φ (cola de m); con (D) σ₁+σ₂ > 1, el
      resto del perfil + polvo + extras tiene masa
      W' ≤ φ − σ₁ − σ₂ < φ − 1 = 1/φ.
  (b) los mínimos de la cascada: o_j ≥ (1+Σ)/φ ≥ 2/φ, o₂ ≥ 2,
      o₁ ≥ 2φ, R ≥ o₁+o₂ ≥ 2φ+2; masa acumulada T_k ≤ T₃/φ^{k−3}
      con T₃ ≤ φo₂ (decaimiento geométrico EXACTO: T_k ≥ φT_{k+1}).
  (b') RÉGIMEN SOMBRA en todo el dominio: para toda pieza x ≤ o₁ del
      presupuesto y todo insertando s ≤ φ−1:
      R − 2s − x ≥ (o₁+o₂) − 2s − o₁ = o₂ − 2s ≥ 2 − 2(φ−1)
      = 2(2−φ) > 0 exacto: la hipótesis del Lema A vale por pieza.
  (c) presupuesto de sombras: Σ_{x ∈ O∪{m}} 2·arcsin((σ₂+x)/(R−σ₂))
      + [segunda inserción del círculo-fila w* = W' ≤ 1/φ, con σ₂ ya
      contada] < 2π en todo el dominio: sup por esquinas (j = 3 en
      el mínimo (2φ, 2, 2/φ, 1): 4.72 y 5.26, márgenes 1.56 y 1.02)
      + cola geométrica para j > 3 (la serie de sombras converge con
      razón φ^{−1/2}; sup observado con holguras 4.52).

## 3. Teorema D1-escrito

**Teorema.** En la celda {p ≥ 4, σ₁+M ≤ 1, j ≥ 3} de la sartén (y
en el régimen de pivote sólido ω ≥ 1, j ≥ 3), ρ ≤ φ implica que el
intercambio no se bloquea.

*Prueba.* El bloqueo exige que falle toda colocación. Constrúyase:
(1) m al lugar que el certificado de F le da en la sartén (F
empaquetó {O, m}: la colocación existe, nada se mueve); (2) σ₁ → D_m
(fila de uno, σ₁ ≤ 1, siempre legal); (3) σ₂ mural por el Lema A
(el presupuesto del Lema B); (4) el resto del perfil + polvo +
extras, de masa W' ≤ 1/φ, como círculo-fila w* (lem:row) insertado
mural por el Lema A de nuevo (presupuesto del Lema B, con σ₂ ya
contada). Todas las piezas de S⁺ quedan colocadas con los recursos
del intercambio: no hay bloqueo. ∎

Uniformidades: j NO aparece (la cascada acota la serie para todo j);
p y k no aparecen (masa, no cantidad); ω no se usa (D3 incluido).

## 4. Qué queda para el resto de dominios

El mismo patrón (inserción por medida + presupuesto por esquinas)
para: D4-D6 (plantilla anidada: contenedor = disco de capacidad
α−ω o z−ω; las mismas dos inserciones), (c-i)/(c-ii)/R2b (los
presupuestos ya están delimitados por las pinzas de las campañas), y
la V-condición desaparece (no hay corona que validar: nada se mueve).
