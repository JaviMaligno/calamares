# La pared del bolsillo doble: el asalto geométrico y el cierre en ω

Borrador. Es el asalto geométrico pendiente de la Batalla 1: los tramos de
ω grande que las cotas combinatorias (Ψ y las medias metálicas de
`bloqueadores.md`) no alcanzan. La herramienta nueva es una pared geométrica
que NO usa el criterio angular, ni el Lema U₄, ni `feas3` — solo la rigidez
de la Proposición S5 reescalada y la monotonía del empaquetamiento en R:

**Lema G.** Bloqueo (plantilla j = 1) ⟹ `σ₁ > b₂(α, o₁)`, el bolsillo de
Descartes del par `{α, o₁}`.

Con ella, el programa de paredes tiene un **rincón óptimo dorado**
(`α = 2`, `o₁ = √5 − 1`, `b₂(2, √5−1) = 1` exacto, `σ₁ = 1`, `σ₂ = 1−ω`) y
su valor es una recta en ω con pendiente áurea, válida en AMBAS ramas
(Teorema G′, §3bis):

    bloqueo (j = 1)  ⟹  ρ > φ² − (φ/2)·ω      para todo ω ,

que cruza T en `ω_A = 2 − 2(T−1)(φ−1) = 0.962585…`. **En total: bloqueo
con un ocupante extra ⟹ ρ > T para todo ω < 0.9626** — el tramo de ω
grande queda cerrado salvo la puntita final. De regalo: la generalización `Ψ_j = (1−ω) + √((1−ω)² + j)` para j
ocupantes (todo ω si j ≥ 4) y el **Corolario S**: los aros menores que m
adicionales son gratis para todas las paredes combinatorias, porque sus
colocaciones son locales. Sometido a verificación adversaria (acta en
`VEREDICTOS.md`): rederivación a ciegas idéntica hasta el rincón dorado;
ningún claim refutado; el verificador demostró la disyunción de los
bolsillos espejo (`y₀ = 2b₂` exacto) y cazó el hueco del caso «hijo-nodo»
en Ψ_j, cerrado después con el **lema de las hojas** (§4): la Proposición
Ψ_j vale sin asteriscos para todo j y toda ocupación. Verificación:
`code/bolsillo.py` (6/6). Numeración local: Lema G, Teoremas G y G′,
Proposición Ψ_j, Corolario S.

## 1. Marco

Plantilla de `bloqueadores.md` con j = 1: `v` = sartén de radio `R` con
ocupantes `{α, o₁, m}`, `o₁ ≥ m = 1`; `u` = agujero de `α` (capacidad
`α − ω ≥ 1`); `S = {σ₁ ≥ σ₂}` colocado por el testigo en `u`
(`σ₂ ≤ σ₁ ≤ 1`); ocupación de agujeros **arbitraria** (X = Σ hijos de o₁,
M = Σ hijos de m, X_σ = Σ hijos de σ₁, a cualquier profundidad vía las
tarifas del Lema R). Paredes combinatorias en pie (de `ocupantes.md` y
`bloqueadores.md`, todas con colocaciones exactas):

    (W)   σ₁ + σ₂ ≤ α − ω              (B4)  σ₂ > α − ω − 1
    (Bo″) o₁ < σ₂ + ω + X              (B3′) σ₂ + X_σ > σ₁ − ω
    (D)   σ₁ + σ₂ > 1                  (evac) σ₂ > 1 − ω  ∨  σ₁ + M > 1

## 2. El Lema G: la pared del bolsillo doble

Recuérdese el bolsillo de Descartes del par (resultados.md §5bis):

    b₂(A, B) = A·B·(A+B) / (A² + A·B + B²) ,

creciente en cada argumento (`∂b₂/∂B = A³(A+2B)/(·)² > 0`, verificado en
simbólico) y con `b₂(α, 1) = b(α)`.

**Lema G.** Si el intercambio está bloqueado, entonces

    σ₁ > b₂(α, o₁)   ( ≥ b(α) ) .

*Demostración.* Bloqueo ⟹ `{α, o₁, σ₁, σ₂}` no empaqueta en el disco `R`
(el re-empaquetado de la sartén es un recurso: los hijos viajan dentro de
sus padres y las posiciones son existenciales). Como `α + o₁ ≤ R` (el par
convive en la sartén), la no-empaquetabilidad se hereda por contención en el
disco `R̄ = α + o₁`. En `R̄` el par es **diametralmente rígido**: los centros
cumplen `|c_α| ≤ R̄ − α = o₁`, `|c_{o₁}| ≤ α` y `|c_α − c_{o₁}| ≥ α + o₁`,
y la desigualdad triangular fuerza igualdad en todo — es la rigidez de la
Proposición S5 de `suelo_rigido.md`, reescalada (el par `{A, B}` en el disco
`A + B` es exactamente S5 con `t = B/A`, multiplicado por `A`). Por la
necesidad de S5 (la factorización exacta, reescalada), cualquier tercer
círculo disjunto de ambos y contenido en el disco tiene radio
`≤ b₂(α, o₁)`, y hay **dos** bolsillos, uno a cada lado del diámetro,
disjuntos entre sí con holgura: el centro del bolsillo está en
`(x₀, ±y₀)` con `x₀ = (α³ + α²o₁ − αo₁² − o₁³)/(α² + αo₁ + o₁²)` y

    y₀² − b₂² = 3·b₂²   ⟹   y₀ = 2·b₂     (identidad exacta) ,

así que los dos círculos espejo distan `4b₂ ≥ 2b₂` entre centros
[identidad aportada por la verificación adversaria]. Si `σ₁ ≤ b₂(α, o₁)`,
entonces también `σ₂ ≤ σ₁ ≤ b₂`, y colocando cada σ concéntrico en un
bolsillo se empaqueta `{α, o₁, σ₁, σ₂}` en `R̄` ⊆ disco `R`: contradicción.
∎

Nótese qué NO se usa: ni el criterio angular, ni el Lema U₄, ni `feas3` —
solo S5 (verificada) y contención. La dirección es la de las cotas
inferiores, incondicional. (El criterio exacto de coronas confirma la
exactitud en R̄: corona de `{α, o₁, σ₁, σ₂}` en `α+o₁` ⟺ `σ₁ ≤ b₂`,
contrastado con el LP de `corona.py` en el bloque [B].)

## 3. El Teorema G: el cierre en ω

**Paso previo (la cadena (\*)).** La cola de `o₁` contiene a
`{m, σ₁, σ₂} ∪ hijos(o₁) ∪ hijos(m) ∪ hijos(σ₁)` (todos ≤ o₁; empates por
primera copia), luego `ρ·o₁ ≥ 1 + σ₁ + σ₂ + X + M + X_σ`; eliminando X con
(Bo″) (`X > o₁ − σ₂ − ω`):

    (*)   ρ  >  1 + (1 + σ₁ − ω + M + X_σ) / o₁ .

**Teorema G.** Bloqueo en la plantilla (j = 1, ocupación arbitraria) ⟹

    rama A (σ₂ ≥ 1−ω):   ρ > φ² − (φ/2)·ω
    rama B (σ₁+M > 1):   ρ > máx( Ψ_B(ω) ,  1 + (2−ω)/N₁(ω) )

con `Ψ_B` la media metálica de `2−ω` (Teorema B″) y
`N₁(ω) = (1+ω)(√(ω²+4ω) − ω)/(2ω)` la raíz positiva de
`ω·N² + ω(1+ω)·N − (1+ω)² = 0` (es decir, `b₂(1+ω, N₁) = 1`). En
particular, `ρ > T` para todo `ω < ω_B = 0.950531…`, con
`ω_A = 2 − 2(T−1)(φ−1) = 2(φ²−T)(φ−1) = 0.962585…` para la rama A sola
(la segunda forma, del verificador, vía `φ³ = 2φ+1`).

*Demostración.* **Rama A.** De (W) y `σ₂ ≥ 1−ω`:
`α ≥ σ₁ + σ₂ + ω ≥ 1 + σ₁`. El Lema G con `b₂` creciente en α da
`σ₁ > b₂(1+σ₁, o₁)`, que resuelta en `o₁` (la condición
`b₂(1+σ₁, N) = σ₁` es la cuadrática `N² + (1+σ₁)N − σ₁(1+σ₁)² = 0`,
verificada en simbólico) equivale a

    o₁ < N(σ₁) := (1+σ₁)·(√(1+4σ₁) − 1)/2 .

Con (\*) (y `M, X_σ ≥ 0`): `ρ > 1 + (1+σ₁−ω)/N(σ₁) =: 1 + h(σ₁)`. La
función `h` es **decreciente** en σ₁: escribiendo
`h = 2/(√(1+4σ₁)−1) − 2ω/[(1+σ₁)(√(1+4σ₁)−1)]`, la comparación de
derivadas se reduce (tras multiplicar y elevar al cuadrado) a la identidad
polinómica

    (1 + 4σ₁) − (1 + 2σ₁ − 2σ₁²)²  =  4σ₁³(2 − σ₁)  >  0 ,

verificada en simbólico. Luego el ínfimo está en `σ₁ = 1`:
`N(1) = √5 − 1`, `1/(√5−1) = φ/2`, y

    ρ > 1 + (2−ω)·φ/2 = φ² − (φ/2)·ω .

**Rama B.** La cota combinatoria: es la rama B del Teorema B″ (misma
dicotomía), `ρ > Ψ_B(ω)`. La geométrica: en (\*), `M > 1 − σ₁` da
`ρ > 1 + (2−ω)/o₁`; y el Lema G con `α ≥ 1+ω` (plantilla) y `σ₁ ≤ 1` da
`b₂(1+ω, o₁) < σ₁ ≤ 1`, es decir `o₁ < N₁(ω)`: `ρ > 1 + (2−ω)/N₁(ω)`. ∎

## 3bis. El remate: la rama B también da la curva dorada (Teorema G′)

La cota de la rama B en el Teorema G (máx(Ψ_B, geométrica)) era un
parcheado; con la pared (B3′) — el anidamiento con tarifa, que la primera
optimización de esta racha olvidó y sin el cual hay configuraciones bajo la
curva — la rama B alcanza la MISMA curva dorada, y el teorema se unifica:

**Teorema G′ (cierre unificado, j = 1).** Bloqueo en la plantilla
(ocupación arbitraria) ⟹ `ρ > φ² − (φ/2)·ω` para **todo** ω. En
particular `ρ > T ⟺ ω < ω_A = 2(φ²−T)(φ−1) = 0.962585…`.

*Demostración (rama B; la A es el Teorema G).* Con `g := √5 − 1`. Las
cadenas, usando `σ₁ + M > 1`, (Bo″), (B3′), (W) y (G):

    (I)   ρ·o₁ ≥ 1+σ₁+σ₂+M+X+X_σ > 2+σ₂+X+X_σ > 2+o₁−2ω+σ₁−σ₂
              ≥ 2+o₁−ω+2σ₁−α > 2+o₁−ω+2b₂(α,o₁)−α
    (II)  ρ·α  ≥ o₁+1+σ₁+σ₂+M+X+X_σ > 2o₁+2−ω+2b₂(α,o₁)−α   [SI α ≥ o₁]

(en (I): X > o₁−ω−σ₂ por Bo″, X_σ > σ₁−ω−σ₂ por B3′, −σ₂ ≥ σ₁+ω−α por W,
σ₁ > b₂ por G; (II) es lo mismo sobre la cola de α, que contiene a o₁ y a
sus hijos **solo si α ≥ o₁** — matiz de la verificación adversaria: la
plantilla no ordena α y o₁). Sea `f₁ := 1+(2−ω+2b₂−α)/o₁` y
`f₂ := (2o₁+2−ω+2b₂−α)/α`. Si `o₁ ≤ g`, la cadena corta (solo σ₁+M>1 y
Bo″, válida en cualquier orden) da
`ρ > 1+(2−ω)/o₁ ≥ 1+(2−ω)/g = φ²−(φ/2)ω`. Si `o₁ > g`, la región de α es
`[1+ω, A_máx(o₁)]` (G y σ₁ ≤ 1 dan `b₂(α,o₁) < 1`), y:

- `f₂` es **estrictamente decreciente en α**: su numerador de derivada es
  `2αb₂′ − (2o₁+2−ω+2b₂)` y `αb₂′ < o₁` por la identidad exacta

      (α²+αo₁+o₁²)² − α·o₁²·(o₁+2α) = (α+o₁)·(α³+α²o₁+o₁³) > 0 ;

- `f₁` es **cóncava en α** (`∂²b₂/∂α² = −6αo₁³(α+o₁)/D³ < 0`, exacto), así
  que su mínimo en α está en los extremos.

**Caso `o₁ ∈ (g, õ]`, õ = 1.29558…** (válido en cualquier orden α/o₁,
porque solo usa (I)/f₁): por concavidad basta ver los dos extremos de
`f₁`: en `α = A_máx`, `f₁ − curva = c₁₀ + ω(1/g − 1/o₁)` con el
coeficiente de ω ≥ 0 (peor caso ω = 0) y `c₁₀ ≥ 0` en
`[g, o* = 1.5958…]` ⊇ `(g, õ]`, con la **identidad exacta `f₁ ≡ curva` en
`o₁ = g`** (∀ω, el rincón dorado; la tangencia sale con pendiente
`c₁₀′(g⁺) = φ`); y en `α = 1+ω`, `f₁ − curva ≥ 0` en `[g, o*]×[0,1]` con
contacto solo en `(g, ω→1)`.

**Caso `o₁ > õ` con `α ≥ o₁`** (que fuerza `o₁ ≤ 3/2`: `A_máx` es
decreciente con `A_máx(3/2) = 3/2` exacto — y de propina `A_máx(g) = 2` y
`A_máx(2) = g`: el rincón dorado es autodual): `f₂(α) ≥ f₂(A_máx)`, y en
la frontera `f₂ − curva = c₂₀(o₁) + ω·c₂₁(o₁)` con
`c₂₁ = 1/g − 1/A_máx ≥ 0` para `o₁ ≤ 2` (peor caso ω = 0) y `c₂₀ ≥ 0` en
`[õ, 3/2]`.

**Caso `o₁ > õ` con `α < o₁`** (el hueco que cazó la verificación; su
región exige `ω < 1/2`: hace falta `1+ω ≤ α < o₁ < N₁(ω)` y
`N₁(1/2) = 3/2 = 1 + 1/2` **exacto**, con N₁ decreciente y 1+ω creciente):
si los hijos de o₁ son < 1, valen las dos cotas α-libres

    ρ > 1 + o₁ − ω              (cola de m: σ₁+M > 1 y Bo″)
    ρ > 1 + (2−ω+2b₂(1+ω,o₁))/o₁   (cola de o₁, que ahora CONTIENE a α:
                                    Bo″ + B3′ + W hacen cancelar α, y
                                    G con α ≥ 1+ω)

y `máx` de ambas ≥ curva + 0.311 en toda la región (mínimo del margen en
ω ≈ 0.015, o₁ ≈ 1.93 — certificado en malla del bloque [F], verificado
también por el verificador). Si o₁ tiene un hijo-nodo, la cota de la curva
queda con el asterisco de recursión de Ψ_j (numéricamente el adversario no
baja de 3.1), pero la conclusión `ρ > T` es incondicional: estamos en la
rama B con `ω < 1/2`, y el Teorema B″ da
`ρ > Ψ_B(ω) > Ψ_B(1/2) = 2 > T` (¡`Ψ_B(1/2) = 2` exacto!). ∎

**Resumen del estatus de G′:** la conclusión `ρ > T para ω < ω_A` está
demostrada **sin asteriscos** en todos los casos; la forma fuerte
`ρ > φ²−(φ/2)ω` vale en todos salvo el rincón {rama B, α < o₁, o₁ > õ,
hijo-nodo, ω < 1/2}, donde la cota demostrada es ≥ 2. Con G′, la puntita
de j = 1 se encoge de `[0.9505, 1)` a `[ω_A, 1) = [0.9626, 1)`, y la cota
de la rama B del Teorema G queda subsumida.

**El rincón dorado.** El mínimo del programa completo de paredes (SLSQP
multi-arranque, bloque [C]) coincide con la curva de la rama A en TODO el
rango, y su minimizador es universal: `α = 2` (tope de B4 con
`σ₂ = 1−ω`), `o₁ = √5 − 1` (tope del Lema G: `b₂(2, √5−1) = 1` **exacto**,
identidad verificada — el par `{2, √5−1}` tiene bolsillo unidad),
`σ₁ = 1`, `X = √5 − 2`. El oro reaparece por partida triple: el par de
bolsillo unidad, la pendiente `φ/2` de la curva, y el valor en ω = 0,
`φ² = φ + 1`. (El rincón es el punto de clausura donde m satura el bolsillo
del par — por eso `b₂ = 1`: la frontera de bloqueo coincide con la frontera
de existencia del testigo.)

## 4. j ocupantes: la escalera Ψ_j

**Proposición Ψ_j.** Bloqueo con j ≥ 1 ocupantes extra (ocupación
arbitraria, las hipótesis de `bloqueadores.md`) ⟹

    ρ > Ψ_j(ω) := (1−ω) + √((1−ω)² + j)      (raíz de u² − 2(1−ω)u − j) ,

con umbrales exactos: `Ψ_j > T ⟺ ω < 1 − (T²−j)/(2T)`, es decir
`0.352201` (j = 1, el ω₆ de `bloqueadores.md`), `0.624046` (j = 2),
`0.895890` (j = 3), y **todo ω** para j ≥ 4 (`Ψ_j ≥ √j ≥ 2 > T`).

*Demostración (Lema de las hojas — cierra el caso general, sin
asteriscos).* Llámese **hoja** a un nodo sin hijos-nodo. El subárbol de
nodos de cada ocupante `o_i` es finito y no vacío (contiene a `o_i`),
luego contiene una hoja `ℓ_i`; los subárboles son disjuntos, así que hay
`j` hojas distintas `ℓ₁, …, ℓ_j`, todas ≥ 1. Sea `L` la mayor,
`X_L = Σ hijos(L)` (todos < 1, por hoja), `M = Σ hijos(m)` y `W` la masa
total de aros < 1 de la instancia distintos de σ₁, σ₂ (así `X_L ≤ W` y
`M ≤ W`, con `X_L` y `M` disjuntos). Tres hechos:

1. (Bo″ en la hoja) `L < σ₂ + ω + X_L ≤ σ₂ + ω + W`.
2. (cola de `L`) las otras `j−1` hojas, `m`, `σ₁, σ₂` y toda la masa < 1
   son menores o iguales que `L` (empates por la primera copia):
   `ρ·L ≥ (j−1) + 1 + σ₁ + σ₂ + W ≥ j + 2σ₂ + W`.
3. (cola de `m`) `σ₁, σ₂` y toda la masa < 1 están en la cola de m:
   `ρ ≥ σ₁ + σ₂ + W ≥ 2σ₂ + W`.

En la rama A de la dicotomía (`σ₂ ≥ 1−ω`), los hechos 1–3 dan
`ρ > máx(2σ+W, (j+2σ+W)/(σ+ω+W))` en `σ = σ₂`; minimizar sobre
`σ ≥ 1−ω`, `W ≥ 0` da el cruce `u² + u(ω−σ−1) − j = 0` (`u = 2σ+W`),
creciente en σ, con mínimo en `σ = 1−ω`: exactamente `Ψ_j(ω)`, la raíz de
`u² − 2(1−ω)u − j`. (Si el cruce cae en `W < 0` — posible con ω > 1/2,
j = 1, σ → 1 —, el valor en `W = 0` es `2σ`, que satisface
`(2σ)² − 2(1−ω)(2σ) − j ≥ j > 0`, luego `2σ > Ψ_j` igualmente: sin fuga
por esa esquina.) En la rama B (`σ₁ + M > 1`), sea `s := σ₂ + X_L`: por
el hecho 1 y `L ≥ 1` es `s > 1 − ω`; la cola de L contiene además a `M`
(disjunta de `X_L`), luego
`ρ·L ≥ j + σ₁ + M + σ₂ + X_L > j + 1 + s` con `L < s + ω`, y la cola de m
da `ρ ≥ σ₁ + M + σ₂ + X_L > 1 + s`. Minimizar
`máx(1+s, (j+1+s)/(s+ω))` da, con `u = 1+s`, la metálica
`u² − (2−ω)u − j = 0` (la análoga de Ψ_B), de raíz ≥ Ψ_j porque
`2−ω ≥ 2(1−ω)` y la raíz crece con el coeficiente: dominante. ∎
*(El paso de la rama B de la primera redacción contaba M dos veces —
corregido tras la verificación adversaria con la variable `s = σ₂ + X_L`;
la esquina del cruce en W < 0 también es suya.)*

Nótese por qué esto cierra el hueco que cazó la verificación adversaria
(el caso «hijo-nodo del mayor ocupante»): las torres de nodos anidados que
invalidaban la prueba vieja (inflan la X de o₁ sin pagar cola de m) siguen
dejando una **hoja** en el fondo de cada subárbol, y la hoja mayor tiene a
la vez el bono j en su cola y el techo de hoja `σ₂+ω+W`. El generador de
árboles aleatorios del bloque [D] no encuentra nada por debajo (mínimos
2.7–3.6 contra Ψ_j = 1.9–2.6).

Combinando Ψ_j (j ≥ 2) con el Teorema G (j = 1): el único residuo de ω
grande con varios ocupantes son los rincones `j = 2, ω ≥ 0.624` y
`j = 3, ω ≥ 0.896` (donde el Lema G no aplica tal cual porque el
re-empaquetado involucra 5+ círculos — véase §6).

## 5. Corolario S: los pequeños son gratis (para la combinatoria)

**Corolario S.** Los Teoremas V2 (`ocupantes.md`), B y B″
(`bloqueadores.md`) y la Proposición Ψ_j valen sin cambios si la instancia
contiene aros menores que m adicionales **en cualquier parte compatible
con la plantilla de cada teorema** (en el espacio libre de `v`, en
agujeros ya parametrizados por las X's… ; para V2, que supone agujeros
libres, un pequeño dentro del agujero de un `o_i` saca la instancia de su
plantilla y la manda a B″ — matiz del verificador; y siempre que S siga
siendo el par `{σ₁, σ₂}` — véase la nota).

*Demostración.* Todas las colocaciones desbloqueantes de esas paredes son
**locales**: viven en `D_m` (libre por el intercambio), en `H_m`, en los
agujeros de los nodos y de σ₁, o junto a m en `u` — nunca en el espacio
libre de `v`. Un aro extra menor que m, esté donde esté, no interseca
ninguno de esos recursos (los contenidos de agujeros ya están contados en
las X's; los aros en `v`-propio se quedan donde están, que es legal porque
las posiciones de los demás no cambian). Las colas solo pueden crecer. ∎

**Nota de alcance.** Los aros < m dentro de `u` son, por definición, parte
de S (`S` = todos los hijos de `u` menores que m en P): la plantilla
`S = par` los excluye; el caso `|S| ≥ 3` es el frente (iii). Y el Lema G
**no** está incluido en el corolario: su pared usa el re-empaquetado global
de la sartén, que sí ve a los pequeños de `v` (véase §6).

## 6. Huecos declarados

1. **La puntita final**: `j = 1, ω ∈ [ω_A, 1) = [0.9626, 1)` — encogida
   desde 0.9505 por el Teorema G′ (§3bis), que materializa la observación
   del verificador de la primera ronda (la rama B exacta nunca baja de la
   curva A; en ω = 0.98 el programa completo aún da 1.8252 = curva A). En
   ese régimen la curva dorada cae bajo T (hacia `1 + φ/2 = 1.809` en
   ω → 1). Cerrarla requiere la pared que el análisis en `R̄` no puede dar:
   con σ₂ minúsculo, ningún empaquetamiento razonable de `{α, o₁, σ₁}` en
   el `R` real (que tiene holgura sobre `R̄` porque el testigo necesita
   alojar a m) deja de tener un hueco para σ₂ — el «lema del hueco»
   cuantitativo, el mismo ingrediente que pide el frente de los pequeños.
1bis. ~~El parche de Ψ_j~~ — RESUELTO (lema de las hojas, §4): la
   Proposición Ψ_j vale sin asteriscos para todo j y toda ocupación.
2. **Los rincones j = 2, ω ≥ 0.624 y j = 3, ω ≥ 0.896**: el Lema G para
   varios ocupantes exige entender el re-empaquetado de 5+ círculos (el
   subconjunto `{α, o_i, σ₁, σ₂}` no hereda la no-empaquetabilidad del
   conjunto completo). Con j ≥ 4, Ψ_j cierra todo ω.
3. **El Lema G frente a pequeños en `v`**: la pared geométrica usa el
   re-empaquetado global; con pequeños presentes se debilita a «el conjunto
   completo no empaqueta». El presupuesto de masa (cola de m:
   `Σ pequeños ≤ ρ − σ₁ − σ₂ − …`) acota el daño pero el análisis
   cuantitativo (lema del hueco) está pendiente. La combinatoria (Corolario
   S) no se ve afectada.
4. La exactitud del ínfimo (¿es `φ² − (φ/2)ω` el ínfimo real de los
   bloqueos j = 1?) no se persigue: la cota basta para `> T`, y las
   familias realizadoras exigirían el estatus de `feas3`.

## 7. Estado de la Batalla 1 tras este asalto

| frente | estado |
|---|---|
| canónica (j = 0), toda ω | cerrado (`grosor_positivo.md`, `esquina.md`, B″) |
| j = 1, ω < 0.9626, ocupación arbitraria | **cerrado (Teorema G′ + B/B″)** |
| j ≥ 4, toda ω | cerrado (Ψ_j, lema de las hojas) |
| j = 2 hasta 0.624; j = 3 hasta 0.896 | cerrado (Ψ_j, lema de las hojas) |
| pequeños en v (paredes combinatorias) | cerrado (Corolario S) |
| puntitas: j=1 ω≥0.9626; j=2 ω≥0.624; j=3 ω≥0.896; Lema G con pequeños; S ≥ 3 piezas | abierto (lema del hueco / re-empaquetado 5+) |


## Mapa de verificación

`code/bolsillo.py`, seis bloques (6/6 OK):

- **[A]** simbólico: ∂b₂/∂o > 0; `b₂(2, √5−1) = 1`; `b₂(α,1) = b(α)`; la
  cuadrática de N(σ₁) y `N(1) = √5−1`; el certificado polinómico de la
  monotonía de h (`4σ³(2−σ)`); la curva dorada y su cruce
  `ω_A = 2−2(T−1)(φ−1)`; la cuadrática de N₁ y `b₂(1+ω, N₁) = 1`; el cruce
  numérico-algebraico `ω_B`; las cuadráticas de Ψ_j y sus umbrales
  `1−(T²−j)/(2T)`.
- **[B]** Lema G: exactitud del bolsillo doble contra el LP de coronas en
  R̄ (800 casos, 0 discrepancias) y la rigidez S5-reescalada.
- **[C]** Teorema G: el mínimo del programa completo (SLSQP multi-arranque,
  ambas ramas) coincide con la curva analítica en 6 valores de ω (pegado a
  <5·10⁻³) con el rincón dorado como minimizador, y la cota combinada
  supera T en toda la malla (0, 0.9505].
- **[D]** Ψ_j vía el lema de las hojas: (i) la optimización de hojas
  (rejilla sobre σ ≥ 1−ω, W ≥ 0) coincide con Ψ_j para j = 2, 3, 5 y
  ω = 0.05/0.45/0.85 (dif ≤ 2·10⁻³ de rejilla); (ii) instancias-árbol
  aleatorias (torres anidadas incluidas) con paredes en pie: mínimos
  2.75–3.61 sobre Ψ_j = 1.87–2.57, 0 violaciones.
- **[E]** Corolario S: añadir pequeños nunca baja ρ (26 852 casos) y el
  argumento de localidad de las colocaciones.
- **[F]** Teorema G′ (el remate de la rama B): las dos factorizaciones
  exactas (concavidad de b₂ en α: `−6αo³(α+o)/D³`; y
  `D² − αo²(o+2α) = (α+o)(α³+α²o+o³)` para el decrecimiento de f₂), los
  certificados univariantes de la frontera (`c₁₀ ≥ 0` en `[g, o*]` con
  ancla exacta `f₁ ≡ curva` en `o = g`; `c₂₀ ≥ 0` en `[õ, 2]`; dominación
  trivial en `o > 2`; `f₁(1+ω) ≥ curva` en `[g, o*]×[0,1]`), el solape
  `õ < o*`, y el SLSQP de la rama B con (B3′) pegado a la curva dorada.
