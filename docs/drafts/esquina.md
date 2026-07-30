# La esquina 13/7: curva exacta del grosor y el ínfimo global

Borrador que cierra H2 de `grosor_positivo.md` §6 usando la frontera cerrada
de `h1.md`. Resultados:

1. **La curva del grosor, entera, en forma cerrada.** Para ω ∈ (0, 0.30],

       T_can(ω) = 2(1−ω)          en (0, ω₁]      (rama H_m)
                = α_m(ω) − ω      en [ω₁, 1/7]    (rama mixta)
                = Φ(ω)            en [1/7, 0.30]  (rama del testigo)

   donde **ω₁ es la raíz en (1/25, 1/14) de la cúbica 4ω³ − 20ω² + 25ω − 1**
   (ω₁ = 0.0413570034…, antes «raíz de h(2−ω,1−ω) = 1−ω, sin forma
   cerrada») y **α_m(ω) es algebraica de grado 6**: la raíz en (1, 2] de

       t(α−1) + t(1−ω) = t(b(α)) = 1/√(α(α+1)) ,    t(s) = √((1−s)/s) ,

   cuyo polinomio P(α, ω), de bigrado (6, 2), es explícito (§4).

2. **Teorema de la esquina.** inf_{ω>0} T_can(ω) = 13/7, alcanzado (en el
   límite (α, σ₁) → (2⁺, 1⁻)) exactamente en la esquina
   (ω, α, σ₂) = (1/7, 2, 6/7). La
   cota inferior es universal y la familia de la esquina es **genuina**
   (Proposición S5 + Lema S6a de `suelo_rigido.md`), así que este teorema
   **no** está condicionado a la exactitud de `feas3`. La conjetura de la
   esquina de `grosor_positivo.md` §4 queda demostrada.

3. **Estructura fina, corregida.** La afirmación medida «la curva decrece en
   (0, 1/7]» es **falsa** en un tramo minúsculo: ω₁ es un **mínimo local**
   de T_can (valor 2(1−ω₁) = 1.9172860), la rama mixta *sube* al salir de la
   juntura — V′(ω₁⁺) > 0 es exacto y trivial, §5 — hasta un **máximo local**
   en ω_peak = 0.0444700 (raíz de un polinomio explícito de grado 8), de
   altura +1.1·10⁻⁴, y solo entonces baja hacia la esquina. El bump es
   invisible a la malla de `grosor.py` [D] (paso ≥ 0.005) y no afecta a
   ningún resultado previo: los valores medidos eran correctos punto a punto.

Verificación: `code/esquina.py` (5 bloques). Estatus: la cota inferior de la
curva y el Teorema de la esquina son demostraciones completas; la dirección
superior (que T_can no excede la fórmula) es exacta en la rama del testigo y
en la esquina, y en las ramas H_m y mixta hereda el módulo habitual de
exactitud del criterio angular (§7).

## 1. El programa, en coordenada t

Programa de bloqueo de `grosor_positivo.md` §1, con r_m = 1 y capacidades
c₂ := 1 − ω (agujero H_m) y c₄ := α − ω − 1 (u junto a m):

    (B1) trío {α, σ₁, σ₂} infactible en el disco R = α + 1
    (B2) σ₂ ≥ c₂        (B4) σ₂ ≥ c₄        (W) σ₁ + σ₂ ≤ α − ω

más la banda σ₂ ≤ σ₁ ≤ 1 y la plantilla α − ω ≥ 1. T_can(ω) es el ínfimo de
ρ = máx(σ₁ + σ₂, (1 + σ₁ + σ₂)/α) sobre los bloqueos; en toda la región
relevante manda σ₁ + σ₂ =: S (la otra rama queda por debajo en cuanto
S(1−ω) ≥ 1, que aquí sobra; `esquina.py` [C] usa el máximo completo).

El cambio de coordenada tᵢ = t(σᵢ) = √((1−σᵢ)/σᵢ) (decreciente; σ = 1/(1+t²))
convierte (B1) en **lineal**: por el Lema F de `h1.md` §3, y usando solo la
dirección constructiva del criterio angular (Lema S2: no-empaquetable ⟹
F ≥ 2π),

    trío no empaquetable  ⟹  t₁ + t₂ ≤ Θ(α) := t(b(α)) = 1/√(α(α+1)) .

El programa para α fijo es entonces: minimizar S = σ(t₁) + σ(t₂) sobre la
caja truncada

    0 ≤ t₁ ≤ t₂ ≤ τ := t(c) ,   c := máx(c₂, c₄) ,   t₁ + t₂ ≤ Θ(α) ,

sujeto a (W). Si α > 2 + ω no hay bloqueo alguno: (B4) y la banda dan
S ≥ 2c₄ = 2(α−ω−1) > α − ω, violando (W); en α = 2 + ω exacto el único
candidato es σ₁ = σ₂ = 1, con S = 2 ≥ 2(1−ω), irrelevante para el ínfimo.
Queda α − ω ∈ [1, 2].

## 2. El mínimo condicionado (Lema E1)

**Lema E1.** Sea α ∈ (1, 2 + ω), c = máx(1−ω, α−ω−1) < 1. El ínfimo de S
sobre los tríos no empaquetables con σ₂ ≥ c y σ₂ ≤ σ₁ ≤ 1 es

    (a) 1 + b(α)                        si c ≤ b(α)
    (b) c + σ( Θ(α) − t(c) )            si b(α) < c ≤ s*(α)
    (c) 2c                              si c > s*(α) ,

con s*(α) = 4α(α+1)/(2α+1)² el punto diagonal de la frontera (t(s*) = Θ/2).

*Demostración.* σ es decreciente, así que S baja al subir cualquier tᵢ. En la
región {t₁ ≤ t₂ ≤ τ, t₁ + t₂ ≤ Θ}: si 2τ ≤ Θ (caso c), la esquina de la caja
(τ, τ) es admisible y óptima: S = 2σ(τ) = 2c. Si 2τ > Θ, el mínimo vive en el
segmento t₁ + t₂ = Θ, sobre el cual

    dS/dt₂ = −σ′(Θ − t₂) + σ′(t₂) = 2[√G(t₁) − √G(t₂)] ≤ 0    (t₂ ≥ t₁)

por el G-lema de `h1.md` §4 (σ′(x) = −2x/(1+x²)² y (σ′/2)² = G(x) =
x²/(1+x²)⁴; la desigualdad G(t₂) ≥ G(t₁) sobre t₁ + t₂ = Θ ≤ 1/√2 es
exactamente κ ≥ 1). Luego conviene t₂ máximo: t₂ = mín(τ, Θ) — si τ ≥ Θ
(caso a) el tope es t₂ = Θ, t₁ = 0: (σ₁, σ₂) = (1, b(α)); si τ < Θ (caso b),
t₂ = τ, t₁ = Θ − τ: (σ₁, σ₂) = (σ(Θ−τ), c). ∎

El caso (a) es el Corolario 1 de `h1.md` (la rama del testigo); (c) es el
reparto igual (la rama H_m); (b) es la **rama mixta**, ahora con σ₁ en forma
cerrada. Nótese que el mínimo de S como función de α es lo único que queda:

**Lema E2 (monotonía en α).** En sus dominios respectivos, los tres casos de
E1 son no decrecientes en α (con ω fijo):

- (a): 1 + b(α), b creciente. ∎
- (b) con c = c₂ fijo: dS/dα = σ′(Θ−τ)·Θ′(α) ≥ 0, pues σ′ < 0 y Θ′ < 0. ∎
- (b)/(c) con c = c₄ = α−ω−1 (móvil, α ≥ 2): con τ₄ = t(c₄),
  S = σ(τ₄) + σ(Θ−τ₄) y

      dS/dα = τ₄′·[σ′(τ₄) − σ′(Θ−τ₄)] + σ′(Θ−τ₄)·Θ′
            = τ₄′·(−2)[√G(τ₄) − √G(t₁)] + σ′(t₁)·Θ′ ≥ 0 ,

  porque τ₄′ < 0, G(τ₄) ≥ G(t₁) (de nuevo el G-lema: τ₄ ≥ t₁ sobre el
  segmento) y los dos factores del segundo término son negativos. ∎

**El G-lema de H1 es el motor de las dos cosas**: dentro de cada α empuja el
óptimo a la esquina de la caja, y entre αs hace crecientes las ramas.

## 3. La curva exacta (Proposición 7)

**Proposición 7.** Para ω ∈ (0, 0.30], el ínfimo de S sobre los bloqueos
(B1)–(W) es la curva de tres tramos del resumen, con junturas exactas ω₁
(cúbica) y 1/7.

*Demostración.* Fijo ω, minimizamos sobre α el valor de E1 sujeto a (W).

**Tramo H_m (ω ≤ ω₁).** El caso (c) da S = 2(1−ω), constante en α, admisible
sii (W): 2(1−ω) ≤ α−ω ⟺ α ≥ 2−ω, y sii c₂ > s*(α) ⟺ α ≤ ᾱ(ω) :=
(1/√ω − 1)/2. La ventana [2−ω, ᾱ] es no vacía ⟺ s*(2−ω) ≤ 1−ω. Como

    (1−ω) − s*(2−ω)  tiene numerador  −(4ω³ − 20ω² + 25ω − 1)

y la cúbica es estrictamente creciente en (0, 5/6) (su derivada es
(5−2ω)(5−6ω)), la ventana existe exactamente para ω ≤ ω₁, la raíz de la
cúbica (1/25 < ω₁ < 1/14 por signos). Los demás casos no bajan de 2(1−ω)
(E2 + continuidad en las junturas de caso), luego T_can = 2(1−ω) ahí.

**Tramo mixto (ω₁ < ω ≤ 1/7).** Para α ≤ 2 el caso (c) queda vacío (exigiría
1−ω ≥ s*(α) con α ≥ 2−ω por (W), y s*(α) ≥ s*(2−ω) > 1−ω para ω > ω₁, la
cúbica) y el caso (a) exige b(α) ≥ 1−ω, imposible (b(2) = 6/7 ≤ 1−ω). Queda
(b) con c = c₂ para α ≤ 2: S^b(α) = 1−ω + σ(Θ−t(1−ω)), creciente (E2), con
(W) ⟺

    σ(Θ(α) − t(1−ω)) ≤ α − 1   ⟺   Ψ(α) := t(b(α)) − t(α−1) ≥ t(1−ω) .

Ψ es estrictamente creciente (Ψ′ = 1/(2√(g(α−1))) − (2α+1)/(2(α²+α)^{3/2}),
positiva en (1, 2]: el primer término domina), con Ψ(1⁺) = −∞ y Ψ(2) =
t(6/7) ≥ t(1−ω) ⟺ ω ≤ 1/7: hay una única raíz α_m(ω) ∈ (1, 2], y los α
admisibles son [α_m, 2]. Por E2 el mínimo es S^b(α_m) = α_m − ω ((W) con
igualdad). Para α ∈ (2, 2+ω): si b(α) ≤ 1−ω, todo bloqueo cumple σ₂ ≥ c₄ ≥
c₂ y por tanto S ≥ S^b(α) > S^b(2) ≥ S^b(α_m) (relajando (B4) a (B2), E2);
si b(α) > 1−ω, S ≥ 1 + b(α) > 2 − ω > α_m − ω. Luego T_can = α_m(ω) − ω.
(En el paso «S ≥ S^b(α) para α ∈ (2, 2+ω)»: al relajar (B4) a (B2) el caso
(c) con c₂ tampoco aparece, pues 1−ω ≥ s*(α) > s*(2) = 24/25 exigiría
ω < 1/25 < ω₁.) Elevando al cuadrado dos veces la ecuación de α_m se obtiene
el polinomio

    P(α, ω) = α⁶ + 2α⁵ω − 2α⁵ + 5α⁴ω² − 6α⁴ω − α⁴ − 4α³ω² + 4α³ω
              − 2α²ω² + 3α² + 4αω² − 6αω + 2α + ω² − 2ω + 1 = 0

(condición necesaria: producto de las cuatro ramas (Z ± X ± Y); la rama
correcta se identifica por α_m ∈ (1, 2] y verificación numérica, bloque B).
P es **irreducible** sobre ℚ[α, ω] —luego sobre ℚ(ω)[α], por primitividad—:
«algebraica de grado 6» es exacto, no solo una cota. Dos identidades útiles:
P(2−ω, ω) = (ω−1)³·(4ω³−20ω²+25ω−1), que da α_m(ω₁) = 2−ω₁ en exacto, y la
parametrización x := t(α−1), con la que la ecuación de la rama es
x + √(ω/(1−ω)) = (1+x²)/√((2+x²)(3+2x²)) y el alcance de la rama es
transparente: x ≥ 0 ⟺ ω ≤ 1/7, con x = 0 ⟺ α = 2 ⟺ ω = 1/7.

**Tramo del testigo (ω ≥ 1/7).** Ahora b(T₍₁₊ω₎) = T₍₁₊ω₎ − 1 − ω ≥ 1 − ω
⟺ T₍₁₊ω₎ ≥ 2 ⟺ ω ≥ 1/7 (T₍₈⁄₇₎ = 2): el óptimo del caso (a) satisface
(B2). El caso (a) con (W) exige α ≥ T₍₁₊ω₎ (Lema 1 de `grosor_positivo.md`)
y su mínimo es 1 + b(T₍₁₊ω₎) = Φ(ω); los casos (b)/(c₄) con α > T₍₁₊ω₎ son
crecientes (E2) y arrancan en Φ(ω); y los α < T₍₁₊ω₎ no admiten bloqueo:
para α ∈ (2, T₍₁₊ω₎) rige el caso (a) (c₄ ≤ b(α)) y su (W) exige
α ≥ T₍₁₊ω₎; para α ≤ 2 (c = c₂ = 1−ω ≤ 6/7), el caso (a) —si b(α) ≥ 1−ω—
tiene mínimo 1 + b(α) y (W) vuelve a exigir α ≥ T₍₁₊ω₎ > 2; el caso (b)
exigiría bajo (W) Ψ(α) ≥ t(1−ω), pero Ψ(α) ≤ Ψ(2) = t(6/7) ≤ t(1−ω), con
igualdad solo en la esquina (ω = 1/7, α = 2); y el caso (c) exigiría
1−ω ≥ s*(α) ≥ s*(2−ω), imposible para ω > ω₁. ∎

En la juntura ω₁: α_m(ω₁) = 2 − ω₁ y α_m(1/7) = 2 exacto (t(1) = 0 y
t(b(2)) = t(6/7)), con V continua: V(ω₁) = 2(1−ω₁), V(1/7) = 13/7.

## 4. Teorema de la esquina

**Teorema.** inf_{ω>0} T_can(ω) = 13/7 = T + 0.0178561…, y el ínfimo se
alcanza (en el límite (α, σ₁) → (2⁺, 1⁻)) solo en la esquina
(ω, α, σ₂) = (1/7, 2, 6/7).

*Demostración de la cota inferior.* Sea un bloqueo cualquiera con grosor ω.
Si α ≥ 2: por el Corolario 1 de `h1.md` (sin usar (B2), (B4) ni (W)),
S ≥ 1 + b(α) ≥ 1 + b(2) = 13/7. Si α < 2: por la Proposición 7,

- ω ≥ 1/7: S ≥ ... (no hay bloqueo con α < T₍₁₊ω₎, y T₍₁₊ω₎ ≥ 2 > α): vacío.
- ω ≤ ω₁: S ≥ 2(1−ω) ≥ 2(1−ω₁) = 1.91728… > 13/7 (⟸ ω₁ < 1/14).
- ω₁ < ω < 1/7: S ≥ α_m(ω) − ω =: V(ω), y **V > 13/7 en [ω₁, 1/7)**: si
  V(ω′) = 13/7 en algún ω′, entonces (α, ω) = (13/7 + ω′, ω′) satisface la
  ecuación de la rama y por tanto P = 0; pero

      q(ω) := P(13/7 + ω, ω) = 4(7ω − 1)·Q₅(ω) / 7⁶ ,
      Q₅(ω) = 33614ω⁵ + 235298ω⁴ + 620830ω³ + 766066ω² + 397831ω − 289 ,

  y Q₅ **no tiene raíces en [1/25, 1/7] ⊇ [ω₁, 1/7)** (aislamiento exacto de
  raíces, bloque A2; la única raíz positiva de Q₅ es ≈ 0.000725 < 1/25), así
  que la única raíz de q ahí es ω = 1/7. Como V(ω₁) − 13/7 = 1/7 − 2ω₁ > 0 y
  V es continua, V > 13/7 en todo [ω₁, 1/7). ∎

Dos observaciones de alcance. Primero, la cota inferior vale para **todo**
ω > 0, no solo ω ≤ 0.30: las viñetas α ≥ 2 y ω ≥ 1/7 no usan esa cota, y las
restantes viven en ω < 1/7. Segundo, la unicidad del ínfimo: la igualdad en
la viñeta α ≥ 2 fuerza S = 1 + b(α) = 13/7, es decir α = 2, σ₁ = 1,
σ₂ = 6/7; entonces (B2) da 1 − ω ≤ 6/7 (ω ≥ 1/7) y (W) da
13/7 ≤ 2 − ω (ω ≤ 1/7): solo la esquina.

*Demostración del alcance (la familia es genuina).* En α = 2, ω = 1/7
exactos no hay familia: κ > 1 da σ₁ + h(2, σ₁) > 13/7 = α − ω para todo
σ₁ < 1, y (W) se viola — la esquina solo es accesible **abriendo (B4)**. La
familia correcta, con ω = 1/7 fijo y δ ↓ 0:

    α = 2 + δ ,   ε = δ²/4 ,   σ₁ = 1 − ε ,   σ₂ = (α − ω − 1) + ε/2 .

Paredes: (B4) con holgura ε/2; (B2) porque α − ω − 1 ≥ 1 − ω ⟺ α ≥ 2; (W)
porque σ₁ + σ₂ = α − ω − ε/2; banda porque σ₂ < σ₁. Genuinidad: como
α > T₍₈⁄₇₎ = 2, el Lema 1 da σ₂ > b(α) estricto (margen ≈ 0.898·δ), luego el
trío {α, 1, σ₂} es genuinamente no empaquetable —no solo según el criterio
angular— por la Proposición S5 de `suelo_rigido.md` (rigidez: el disco
R = α + 1 está diametralmente lleno por α y 1; reescálese con t = 1/α), y la
infactibilidad se propaga de σ₁ = 1 a σ₁ = 1 − ε por el Lema S6a(3) para
**cualquier ε ∈ (0, δ₀]** con el δ₀ = δ₀(δ) > 0 del lema — eso basta para el
teorema, sin invocar el criterio angular. (La elección numérica concreta
ε = δ²/4 del bloque E se valida además con el criterio angular: el umbral
medido es ε_máx ≈ 2.24·δ², coherente con la tasa √ε de la frontera.)
Entonces ρ = α − ω − ε/2 → 13/7. Que el ínfimo no se alcanza en ningún otro
ω es la cota inferior estricta fuera de la esquina. ∎

Obsérvese qué piezas soportan el teorema: H1 da la cota α ≥ 2 y el motor de
monotonía; la cúbica de ω₁ y la quíntica Q₅ dan el tramo central; S5 + S6a
dan la genuinidad. **El ínfimo global 13/7 no depende de la exactitud del
criterio angular.**

## 5. La estructura fina: ω₁ es un mínimo local y hay un bump

La rama mixta **no** sale decreciendo de la juntura. Derivando la ecuación de
α_m: V′(ω) = α_m′(ω) − 1 = r′(ω)/Ψ′(α_m) − 1, con r(ω) = t(1−ω) y, en la
juntura α = 2 − ω₁,

    Ψ′(2−ω₁) = 1/(2√(ω₁(1−ω₁)³)) − c₀ = r′(ω₁) − c₀ ,
    c₀ = (2α+1)/(2(α²+α)^{3/2}) > 0    (α = 2−ω₁) ,

porque (α−1)³(2−α) = (1−ω₁)³ω₁ ahí: **el primer término de Ψ′ es r′(ω₁)
exactamente**. Luego

    V′(ω₁⁺) = r′/(r′ − c₀) − 1 = c₀/(r′ − c₀) > 0 :

la curva **sube** al entrar en la rama mixta (numéricamente V′(ω₁⁺) =
+0.0721). Como V(1/7) = 13/7 < V(ω₁), hay un máximo local interior; los
puntos críticos de V sobre la curva P = 0 satisfacen P_α + P_ω = 0, y el
resultante de P y P_α + P_ω respecto de α tiene un único factor con raíces
en [1/25, 1/7], de grado 8:

    R₈(ω) = 1550ω⁸ + 1244ω⁷ − 3390ω⁶ − 2308ω⁵ + 2781ω⁴ + 1682ω³
            − 294ω² + 32ω − 1 ,

con **exactamente una raíz ahí** (Sturm): ω_peak = 0.0444699865… El bump
completo: T_can baja como 2(1−ω) hasta el mínimo local 2(1−ω₁) = 1.9172860
en ω₁, sube +1.105·10⁻⁴ hasta T_can(ω_peak) = 1.9173965, y baja hasta 13/7
en la esquina; después sube como Φ. **T_can tiene dos mínimos locales**, ω₁
y 1/7, y el global es la esquina.

Corrección a `grosor_positivo.md` §4: «la curva decrece en todo (0, 1/7]» es
falsa en (ω₁, ω_peak). El error no estaba en los valores medidos (todos
correctos, el más cercano al bump era ω = 0.06, ya en el tramo decreciente)
sino en la interpolación monótona entre ellos; el bump (+1.1·10⁻⁴) queda por
debajo de la resolución declarada de aquella malla (4·10⁻⁴).

## 6. Constantes nuevas

- **ω₁**: raíz en (1/25, 1/14) de 4ω³ − 20ω² + 25ω − 1 = 0; equivalentemente
  √ω₁ = 1/(5 − 2ω₁). Antes solo numérica.
- **α_m(ω)**: sextica P(α, ω) = 0 (bigrado (6,2)). Antes «sin forma cerrada».
- **ω_peak**: raíz en (ω₁, 1/7) de R₈; con α_peak = α_m(ω_peak) =
  1.9618665… (el resultante completo es −2¹⁸·(ω−1)¹⁰·R₈).
- **Q₅**: la quíntica que separa la rama mixta de la recta V = 13/7.
- La juntura ω_× ≈ 0.0754 del Teorema de `grosor_positivo.md` §3 pierde su
  papel de candidata a juntura real: era solo el cruce de las dos cotas del
  máximo; las junturas verdaderas son ω₁ y 1/7.

## 7. Estatus y alcance

- **Demostrado sin condición**: la cota inferior T_can(ω) ≥ curva de la
  Proposición 7 (usa solo la dirección constructiva del criterio angular,
  vía el Lema F de `h1.md`); el Teorema de la esquina entero (cota inferior
  + familia genuina vía S5 + S6a); ω₁, P, R₈, Q₅ como objetos exactos; el
  bump y las dos junturas.
- **Módulo exactitud del criterio angular** (el mismo módulo declarado en
  `perfil_tres.md` §5 y heredado por todo el repo): que T_can no exceda la
  fórmula en las ramas H_m y mixta — sus configuraciones óptimas tienen
  σ₁ < 1 (salvo el extremo ω = 1/7 de la mixta, que tiene σ₁ = 1 y sí queda
  cubierto por S5) y su no-empaquetabilidad genuina más allá del criterio
  angular no está demostrada (a diferencia de la esquina y de la rama del
  testigo, que viven en σ₁ → 1 y quedan cubiertas por S5 + S6a). El barrido
  [C] de `esquina.py` y el [D] de `grosor.py` la respaldan numéricamente.
- **Alcance**: plantilla canónica (H3 de `grosor_positivo.md`), como todo el
  bloque de grosor.

## Mapa de verificación

`code/esquina.py`, cinco bloques: **[A]** álgebra exacta en sympy — P, sus
grados y su irreducibilidad sobre ℚ[α,ω], la factorización q = 4(7ω−1)Q₅/7⁶
con aislamiento de raíces de Q₅ en [1/25, 1/7] (cero), la cúbica de ω₁
(numerador de (1−ω) − s*(2−ω), derivada (5−2ω)(5−6ω), unicidad de la raíz),
la identidad de juntura P(2−ω, ω) = (ω−1)³·cúbica, b(2) = 6/7 y
P(2, 1/7) = 0, la identidad del primer término de Ψ′ en la juntura
(V′(ω₁⁺) > 0 exacto; su valor es +0.0721380…), el resultante y R₈ con
exactamente una raíz (Sturm), el motor σ′ = −2√G, la positividad de Ψ′ en
(1, 2] y la exclusión α > 2 + ω; **[B]** la raíz bisecada de la rama mixta anula P,
reproduce los 5 valores medidos de `grosor_positivo.md` y da las junturas
α_m(ω₁) = 2 − ω₁, α_m(1/7) = 2; **[C]** curva completa contra fuerza bruta
con el criterio angular puro (sin coordenada t) en 14 valores de ω sobre los
tres tramos y las junturas; **[D]** estructura fina: bump, mínimo local en
ω₁, mínimo global en malla de 1200 puntos = esquina, margen positivo fuera
de la esquina; **[E]** familia genuina de la esquina (α = 2 + δ, ε = δ²/4):
paredes con holgura, margen sobre b(α) (ancla S5), infactibilidad angular en
σ₁ = 1 − ε y ρ → 13/7.
