# S de tres piezas: el frente (iii) en la plantilla canónica (Teorema T3)

Borrador. Ataca el frente **«S con más de dos piezas»** de la Batalla 1
(`bolsillo.md` §7, `ESTADO_SESION.md`). Resultado principal:

**Teorema T3.** Bloqueo del paso de intercambio en la plantilla canónica
con `S = {σ₁ ≥ σ₂ ≥ σ₃}` (tres piezas, ocupación del agujero de m
arbitraria) ⟹

    ρ > máx( Φ(ω), 13/7 ) > T      para todo ω ∈ (0, 1)

si `σ₃ > ω`; en general (σ₃ ≤ ω posible: discos sólidos) queda
`ρ > Φ(ω) > T` siempre y `ρ ≥ 13/7` salvo en {rama 1B, σ₃ ≤ ω}
[CORRECCIÓN post-acta: la cadena `ρ > 1+σ₁` de la rama 1B usa `σ₃ > ω`,
que NO es una necesidad del modelo]. En la rama del zigzag la cota sube
a `17/7`. La
herramienta nueva es el **Lema U₄ leído al revés**: si el trío
`{α, σ₁, σ₂}` empaqueta pero el cuarteto no, el certificado que falla es
el **zigzag**, y el zigzag implica exactamente `σ₂ > b(α)` — el bolsillo
de Descartes reaparece por una tercera vía. El cruce de esa pared con (W)
vive en la **deformación áurea**

    γ_ω := raíz > 1 de  α³ = α² + α + ω·(α² + α + 1) ,     γ₀ = φ ,

(compárese con la deformación de Tribonacci `α³ = (1+ω)(α²+α+1)` de
`grosor_positivo.md`: la misma cúbica con el 1 del paréntesis pasado al
otro lado), cuyo suelo de colas es otra esquina racional:
`γ₍₂/₇₎ = 2` exacto (identidad `8 = 4 + 2 + 2`) con valor `17/7` — la
hermana de la esquina `13/7` del par. Sometido a verificación adversaria
(acta en `VEREDICTOS.md`): CONFIRMADO en todos los sub-claims; el
verificador aportó la pared `σ₂ + M > 1 − ω` que elimina la excepción de
rama de la primera redacción, el suelo cerrado 17/7 (que corrige el
2.4291 de rejilla), la línea B1+W en la rama 1A y el arreglo del oráculo
en M > 1−ω. Verificación: `code/striple.py` (5 bloques). Numeración
local: Teorema T3, Proposición T3j.

## 1. Marco

Plantilla canónica de `grosor_positivo.md` §1 con S de tres piezas:
`v` = sartén de radio `R = α + 1` con `{α, m}` diametrales; `u` = agujero
de `α`, capacidad `α − ω ≥ 1`; el testigo colocó
`S = {σ₁ ≥ σ₂ ≥ σ₃} ⊂ (0, 1)` en `u`; `m` puede tener hijos
(`M := Σ hijos(m)`); el intercambio manda `m` a `u` y debe reinsertar S.
Los σ pueden ser ≤ ω (discos sólidos, permitidos por el modelo).

Recursos de reinserción (colocaciones constructivas; los criterios de
fila, par y anidamiento son los de siempre):

- **D_m**: el disco libre de radio 1 que m deja en `v` (con α en su
  posición original); admite filas de suma ≤ 1.
- **H_m**: el agujero de m (capacidad `1 − ω`), con sus ocupantes M; la
  **evacuación** (B″): M puede mudarse en fila a D_m.
- **`u` junto a m**: fila `1 + Σ ≤ α − ω`.
- **Anidamiento** dentro de S.
- **Re-empaquetado de v**: colocar `{α} ∪ (raíces de S)` como corona en
  el disco `R = α + 1` (Lema C1, constructivo). Incompatible con D_m y
  con la evacuación (ambos usan el interior de `v` con α fijado).

Necesidad del testigo: el par mayor cabía en `u` ⟹
**(W)** `σ₁ + σ₂ ≤ α − ω` (par exacto).

## 2. El Teorema T3

*Demostración.* Tres ramas según la posición de σ₃ y el trío.

**Rama 1 (σ₃ ≤ σ₁ − ω): el polvo cabalga sobre el par.** Anídese σ₃ en
σ₁ en cada colocación del programa del par; su fallo da las cuatro
paredes de `grosor_positivo.md` §1 para `{σ₁, σ₂}`, más una quinta:

- (B1) `«σ₃ ⊂ σ₁; corona {α, σ₁, σ₂} en v»` falla ⟹ el trío no admite
  corona ⟹ `F(σ₁, σ₂) > 2π` (equivalencia exacta corona ⟺ F ≤ 2π para
  tres círculos, C1/C2 — sin feas3).
- (B2/dicotomía) `«σ₁(σ₃) + M en fila en D_m; σ₂ → H_m vaciado»` falla
  ⟹ `σ₂ > 1 − ω` ∨ `σ₁ + M > 1` (σ₃ viaja dentro de σ₁ y no suma).
- (B4) `«σ₂ → u junto a m; corona {α, σ₁(σ₃)} en v»` falla ⟹
  `σ₂ > α − ω − 1` (la corona del par α, σ₁ siempre existe).
- (BH) `«σ₁(σ₃) → D_m; σ₂ + M en fila en H_m»` falla ⟹
  `σ₂ + M > 1 − ω` (σ₁ < 1 cabe sola en D_m; pared del acta).
- (W) del testigo.

De (B1)+(W), por el Corolario 1 de `h1.md` y el Lema 1 de
`grosor_positivo.md`, **en ambas ramas de la dicotomía**:
`σ₁ + σ₂ ≥ 1 + b(α)`, `α ≥ T₍₁₊ω₎` y por tanto
`ρ ≥ σ₁ + σ₂ ≥ 1 + b(T₍₁₊ω₎) = Φ(ω) > T` (Φ estrictamente creciente,
Φ(0) = T). Además: en la rama A (`σ₂ > 1 − ω`) el programa
(B1)+(B2)+(B4)+(W) es exactamente el del Teorema de la esquina
(`esquina.md` §4), cuya cota inferior universal da
`σ₁ + σ₂ > 13/7`; y en la rama B (`σ₁ + M > 1`), (BH) y `σ₃ > ω` dan

    ρ ≥ σ₁ + σ₂ + σ₃ + M > σ₁ + (1 − ω) + ω = 1 + σ₁ ≥ 1 + Φ(ω)/2
      ≥ 1 + T/2 = 1.9196 > 13/7

(σ₁ ≥ (σ₁+σ₂)/2 ≥ Φ/2; margen ≥ 0.0625 para todo ω). Luego
`ρ > máx(Φ, 13/7)` en toda la Rama 1.

**Ramas 2 (σ₃ > σ₁ − ω): nadie anida.** De `σ₂, σ₃ ∈ (σ₁ − ω, σ₁]`
ningún σ anida en otro (ni la estrella: `σ₂ + σ₃ > 2(σ₁−ω) ≥ σ₁ − ω`
para σ₁ ≥ ω, y si σ₁ < ω no hay agujero). Dicotomía por el trío:

**Rama 2A (el trío `{α, σ₁, σ₂}` no admite corona en R).**
`F(σ₁, σ₂) > 2π` y el argumento de la rama B anterior aplica tal cual
(solo usa (W) y la frontera): `σ₁ + σ₂ ≥ 1 + b(α) ≥ Φ(ω)` ⟹
`ρ ≥ ΣS > Φ(ω) > T`. De regalo, con σ₃ > σ₁ − ω ≥ Φ(ω)/2 − ω:
`ρ > (3/2)Φ(ω) − ω` cuando ω ≤ Φ/2, que por la cuerda
`Φ ≥ T + (13−7T)ω` (Prop. 5 de `grosor_positivo.md`) es ≥ 2.64 en
(0, 1/7]; y para ω ≥ 1/7, `Φ(ω) ≥ 13/7`. En ambos casos `ρ ≥ 13/7`.

**Rama 2B (el trío admite corona): el zigzag paga.** Tres colocaciones
mixtas fallan:

- `«σ₃ (+M) en fila en H_m; corona {α, σ₁, σ₂} en v»` ⟹
  **(m1)** `σ₃ + M > 1 − ω`.
- `«σ₃ → u junto a m; corona {α, σ₁, σ₂} en v»` ⟹
  **(m2)** `1 + σ₃ > α − ω`, es decir `α < 1 + ω + σ₃`.
- `«corona {α, σ₁, σ₂, σ₃} en v»` ⟹ no hay corona del cuarteto ⟹
  (Lema U₄, exacto) el trío top falla ∨ el **zigzag** falla. El trío top
  `{α, σ₁, σ₂}` pasa su certificado (tiene corona, Lema C2): falla el
  zigzag,

      θ(α,σ₂) + θ(α,σ₃) + θ(σ₁,σ₂) + θ(σ₁,σ₃) > 2π .

**El zigzag implica el bolsillo.** Por monotonía de θ (σ₂ ≥ σ₃):
`2[θ(α,σ₂) + θ(σ₁,σ₂)] > 2π`, luego `A + B > π/2` con
`A = θ(α,σ₂)/2`, `B = θ(σ₁,σ₂)/2`, ambos < π/2 (A ≥ π/2 forzaría
σ₂ ≥ 1; B < π/2 porque σ₁ + σ₂ < R). Entonces
`sin A > cos B` ⟹ `sin²A + sin²B > 1`:

    f(σ₂)·[f(α) + f(σ₁)] > 1 ,    f(x) = x/(R−x) ,  f(α) = α ,

y con `f(σ₁) ≤ f(1) = 1/α`:  `f(σ₂)(α + 1/α) > 1`, que es **exactamente**
`σ₂ > b(α)` (identidad `σ₂(α²+α+1) > α(α+1)`, verificada en simbólico).

**El cruce dorado.** De `σ₁ ≥ σ₂ > b(α)` y (W):
`2b(α) < σ₁ + σ₂ ≤ α − ω`. La función `α ↦ α − ω − 2b(α)` es
estrictamente creciente (`1 − 2b′ > 0` para α ≥ 1, identidad
`(α²+α+1)² > 2(2α+1)`), luego `α > γ_ω`, la raíz de `2b(α) = α − ω`
(la cúbica del resumen; en ω = 0 es la cota áurea `2b(φ) = φ`,
identidad A6 de `h1.md`). Las colas: por (m1) y la cola de m,

    ρ ≥ σ₁ + σ₂ + σ₃ + M > 2b(α) + (1 − ω) > 2b(γ_ω) + 1 − ω
      = γ_ω + 1 − 2ω ,

y por (m2), `σ₃ > α − 1 − ω`:

    ρ > 2b(α) + α − 1 − ω ≥ 2γ_ω − 1 − 2ω .

La primera cota decrece en ω y la segunda crece (`1 < γ′ < 2`), y su
cruce es **exacto y racional**: `γ = 2` en `ω = 2/7` (identidad
`8 = 4 + 2 + 2` en la cúbica), donde ambas valen `3 − 4/7 = 17/7`. Luego

    ρ > 17/7 = 2.428571…    en toda la rama 2B

(en ω → 0 la primera cota vale φ + 1 = φ² = 2.618; suelo cerrado
aportado por la verificación adversaria, que corrige el `2.4291` de
rejilla de la primera redacción). ∎

**Por qué no contradice ρ*₃ < T.** El umbral combinatorio
`ρ*₃(ω) = 2/(1+2ω) < T` (ω > ω_T) usa SOLO los recursos `N(1) ⊎ N(1−ω)`;
la plantilla canónica añade `u` junto a m y el re-empaquetado de `v`, y
los perfiles baratos de `perfil_tres.md` (p. ej. `{½+ω, ½+ε, ½+ε}`) se
desbloquean con ellos: la corona de `{α, ½+ω, ½+ε, ½+ε}` en `α + 1`
existe para los α que (W) permite. El Teorema T3 dice que el precio del
bloqueo REAL con tres piezas nunca baja de Φ(ω) — más caro que el par en
casi todas las ramas.

## 3. Proposición T3j: la rama de reducción con ocupantes

**Proposición T3j.** En las plantillas con `j ≥ 1` ocupantes extra
(`ocupantes.md`, `bloqueadores.md`, `bolsillo.md`) y `S` de `k ≥ 3`
piezas con `Q := Σ_{i≥3} σᵢ ≤ σ₁ − ω`, todas las paredes y cotas del par
(Teoremas V2, B, B″, Proposición Ψ_j) valen sin cambios:
bloqueo ⟹ `ρ > Ψ_j(ω)`.

*Demostración.* Anídense `σ₃, …, σ_k` en fila en el agujero de σ₁
(`Q ≤ σ₁ − ω`). Toda colocación desbloqueante de esas paredes mueve a
σ₁ (con su carga, que viaja dentro) y a σ₂ exactamente como en el caso
par, y las colas solo crecen con Q ≥ 0. ∎

## 4. Huecos declarados

1. **k ≥ 4 en la canónica.** La rama de reducción (σ₃…σ_k en fila en σ₁)
   hereda el Teorema T3 vía la Rama 1; el análogo de las Ramas 2 exige un
   criterio de corona para 5+ círculos (el U₅ global es falso;
   `corona.md` §6). Evidencia (bloque [D]): mínimos muestreados
   2.22–2.83, muy por encima de T.
2. **j ≥ 1 con k ≥ 3 fuera de la rama de reducción** (σ₃ > σ₁ − ω con
   ocupantes): las colas de Ψ_j crecen con ΣS pero la pared Bo″ para k
   piezas es disyuntiva; sin optimizar. La Proposición T3j cubre la rama
   de reducción.
3. Las cotas de la rama 2B usan la fila como suficiencia en H_m/u
   (conservador); el ínfimo real de esa rama es mayor.
4. El mínimo del programa completo (bloque [B]) queda por encima de las
   cotas por rama con holgura creciente en ω; no se persigue el ínfimo
   exacto (basta > T, y la rama dominante — el par con polvo — ya tiene
   su curva exacta en `esquina.md`).

## Mapa de verificación

`code/striple.py`, cinco bloques: **[A]** simbólico exacto (zigzag ⟹
bolsillo: el signo de `f(σ₂)(α+1/α) − 1` es el de `σ₂ − b(α)`; la cúbica
de γ_ω y `γ₀ = φ`; `1 − 2b′ > 0`; la cuerda de (3/2)Φ − ω; el suelo
**exacto** de la rama 2B: `γ₍₂/₇₎ = 2` con valor 17/7 y la monotonía de
las dos cotas; anclas de Φ); **[B]** oráculo sistemático de colocaciones
(bosques de anidamiento × asignaciones a D_m/H_m/u/corona de v, con las
incompatibilidades D↮corona y evacuación↮corona, y H_m solo restrictivo
si se usa — matiz del acta para M > 1−ω) y muestreo: todo bloqueo cumple
`ρ > Φ(ω)`, 0 violaciones; **[C]** clasificación de los bloqueos
muestreados (con M ∈ [0, 1.2]) en las ramas 1A/1B/2A/2B y verificación
de la cadena de cada rama (paredes B1/B2/B4/BH, `σ₁+σ₂ ≥ 1+b(α) ≥ Φ`,
`σ₂ > b(α)`, `α > γ_ω`, `ρ > 1+σ₁` en 1B, las dos cotas de 2B, la cota
13/7 de la esquina); **[D]** k = 4: mínimos muestreados sobre el mismo
oráculo (hueco declarado, evidencia); **[E]** m con hijos
(M ∈ [0, 1.2], incluido M > 1−ω): 0 violaciones de Φ con H_m ocupado y
la evacuación en el oráculo. La verificación adversaria reescribió el
oráculo desde cero (0 discrepancias en 140k configs), atacó el zigzag
con 2M muestras (pared ajustada, margen mínimo 2.8·10⁻⁵) y barrió las
cadenas por rama en 11 valores de ω (~85k bloqueos, 0 fallos).
