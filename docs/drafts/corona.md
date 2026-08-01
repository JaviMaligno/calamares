# El criterio de corona: Lema U_k y el teorema exacto para k = 4

Borrador. Resuelve el **paso 1 de la Batalla 1** (`ESTADO_SESION.md` §3),
con dos correcciones importantes al plan: el enunciado que el plan proponía
(«si la suma de arcos consecutivos en algún orden ≤ 2π, empaqueta») es
**falso** para k ≥ 4, y el orden decreciente **no** es el orden óptimo. La
teoría correcta es la de este documento: la factibilidad de una corona en un
orden cíclico fijo es un **sistema lineal en los huecos angulares** (Lema C1),
todo subconjunto de una corona da un certificado necesario (Lema C2,
incondicional, la dirección que usan las cotas inferiores), y en **k = 4**
—el caso que la Batalla 1 necesita— los certificados caracterizan la
factibilidad **exactamente** (Teorema C4), con forma global cerrada que se
reduce a **dos desigualdades**: el trío top más el total del orden zigzag
(Teorema C5 + Corolario C5′, «Lema U₄»). En k = 5 el criterio de
solo-subconjuntos es falso (patrón «pentagrama»), pero añadiendo el
certificado del pentagrama vuelve a ser exacto para θ arbitrarias
(Teorema C7); que geométricamente el pentagrama sea redundante queda como
conjetura con evidencia fuerte (Conjetura C8). Sometido a verificación
adversaria independiente (acta en `VEREDICTOS.md`): ningún claim refutado;
el Corolario C5′, el Teorema C7, el oráculo euclídeo y el récord geométrico
del pentagrama son aportaciones del verificador. Verificación:
`code/corona.py` (5/5).

**Numeración local**: Lemas C1–C3, Teoremas C4–C5 (con Corolario C5′),
Proposición C6, Teorema C7, Conjetura C8. Notación de `suelo_rigido.md` §3
(Lema S1): para dos círculos
de radios `a, b` tangentes interiormente a la pared de un disco de radio `R`,

    sin²(θ(a,b)/2) = f(a)·f(b),     f(x) = x/(R−x),

y `θ(a,b) ∈ [0, π]` es la separación angular mínima que garantiza interiores
disjuntos; `θ` está definida si y solo si `a + b ≤ R`, y es creciente en
ambos argumentos.

## 1. Marco: coronas y el sistema de huecos

**Definición.** Una **corona** de `{a₁, …, a_k}` en el disco de radio `R` es
un empaquetamiento de los k círculos con **todos tangentes interiormente a la
pared**. Si algún par cumple `aᵢ + aⱼ > R` no hay corona (la distancia entre
centros es a lo sumo `(R−aᵢ) + (R−aⱼ) < aᵢ + aⱼ`); supondremos en adelante
todos los pares admisibles.

Una corona queda determinada por las posiciones angulares de los centros.
Fijado el **orden cíclico** π en que aparecen (módulo rotación y reflexión),
córtese en el primer elemento: posiciones `0 = S₁ ≤ S₂ ≤ … ≤ S_k < 2π`
(numeramos por posición en π). Para el par en posiciones `i < j`, la
separación angular es `mín(S_j − S_i, 2π − (S_j − S_i))`, y el Lema S1 da:

**Lema C1 (sistema de huecos).** Existe una corona con orden cíclico π si y
solo si el sistema lineal

    θ_{ij} ≤ S_j − S_i ≤ 2π − θ_{ij}        para todo 1 ≤ i < j ≤ k,  S₁ = 0

es factible (con `θ_{ij} := θ` del par en posiciones `i, j`).

*Demostración.* `mín(Δ, 2π − Δ) ≥ θ ⟺ θ ≤ Δ ≤ 2π − θ` porque `θ ≤ π`. La
monotonía `S_i ≤ S_j` sale gratis de `θ_{ij} > 0`, y `S_k ≤ 2π − θ_{1k} < 2π`
mantiene todo en una vuelta. Cada círculo tangente a la pared está contenido
en el disco, y los pares son disjuntos por el Lema S1. ∎

La factibilidad de coronas es por tanto **decidible exactamente**: un
programa lineal por cada uno de los `(k−1)!/2` órdenes. Lo que sigue es la
combinatoria de ese sistema.

## 2. Certificados de subconjunto (la dirección de las cotas inferiores)

**Lema C2 (necesidad, todo k).** Si `{a₁, …, a_k}` admite corona en el disco
`R` con orden cíclico π, entonces **todo** subconjunto `T` con `|T| ≥ 3`
cumple, en el orden cíclico inducido por π,

    Σ_{pares consecutivos de T} θ ≤ 2π .

*Demostración.* Los círculos de `T`, en sus posiciones de la corona, son una
corona de `T` (las restricciones son por pares). Sus huecos consecutivos
suman `2π` y cada hueco es ≥ θ del par correspondiente (Lema C1, cota
inferior, aplicada al par consecutivo). ∎

**Corolario C2′ (forma sin orden).** Si existe `T` tal que la suma cíclica de
`T` excede `2π` **en todos los órdenes cíclicos de T**, no hay corona en
ningún orden. — Esta es la contrapositiva que usan las cotas inferiores del
programa: es incondicional, como la dirección ⟹ del Lema U.

Con cabeza en el trío: si `T = {A, x, y}` con `A = máx T`, su certificado se
linealiza con el **Lema U** (`universal.md` §1; la hipótesis `A ≥ mín(x,y)`
se cumple automáticamente): con `c = R − A`,

    T pasa  ⟺  T_c(x) + T_c(y) ≥ τ_R .

## 3. La desigualdad triangular condicional y la caída del enunciado ingenuo

**Lema C3 (triángulo condicional).** Si `b ≥ mín(a, c)`, entonces
`θ(a,c) ≤ θ(a,b) + θ(b,c)`. Sin la hipótesis el enunciado es **falso**.

*Demostración.* Sin pérdida `c ≤ a`; con `b ≥ c`, la monotonía del Lema S1 da
`θ(a,b) ≥ θ(a,c)`. Contraejemplo sin hipótesis: `R = 1`, `a = c = 0.45`,
`b → 0`: el miembro izquierdo es `2 arcsin(9/11) = 1.9165…` y el derecho
tiende a 0. ∎

**Observación (el enunciado ingenuo del plan es falso para k = 4).** Tómese
`R = 1` y `{x, x, x, ε}` con `x = 0.47`, `ε = 0.02`. La suma cíclica
consecutiva mínima sobre los órdenes es `4.9012 ≤ 2π` (el ε, intercalado
entre dos x, «descuenta» un arco grande: exactamente el fallo del triángulo
del Lema C3). Pero el trío `{x, x, x}` ya es infactible en el disco —por el
criterio exacto de tres círculos iguales, factible ⟺ `2x ≤ √3(R−x)` ⟺
`x ≤ √3/(2+√3) = 0.46410…`, y también por su propio certificado
`3·θ(x,x) = 6.5421 > 2π`— luego no hay corona (ni empaquetamiento alguno) de
los cuatro. La suma sobre pares consecutivos no basta: hacen falta **todos
los subconjuntos**. La «misma prueba que S2 par a par» que sugería el plan se
rompe justamente donde S2 usa la monotonía con la cabeza en medio (Lema C3):
con k = 3 y el máximo centrado la hipótesis del triángulo se cumple; con
k ≥ 4 los pares no adyacentes con intermediarios pequeños la violan.

## 4. El teorema exacto para k = 4

Aquí está la sorpresa buena: en k = 4 los certificados de subconjunto son
**exactamente** la factibilidad, y el teorema no necesita geometría ninguna —
vale para cualquier matriz simétrica de separaciones en `(0, π]`.

**Teorema C4 (criterio exacto por orden, k = 4).** Sean `θ_{ij} ∈ (0, π]`
arbitrarios (`1 ≤ i < j ≤ 4`, simétricos). El sistema del Lema C1 para el
orden `(1, 2, 3, 4)` es factible si y solo si

    (T₁₂₃)  θ₁₂ + θ₂₃ + θ₁₃ ≤ 2π
    (T₁₂₄)  θ₁₂ + θ₂₄ + θ₁₄ ≤ 2π
    (T₁₃₄)  θ₁₃ + θ₃₄ + θ₁₄ ≤ 2π
    (T₂₃₄)  θ₂₃ + θ₃₄ + θ₂₄ ≤ 2π
    (TOT)   θ₁₂ + θ₂₃ + θ₃₄ + θ₁₄ ≤ 2π .

*Demostración.* Necesidad: Lema C2 (los cuatro tríos y el conjunto total).

Suficiencia, por dualidad de sistemas de diferencias. El sistema es de la
forma `S_j − S_i ≤ w` para las aristas de un digrafo sobre las posiciones
{1, 2, 3, 4}: cada cota superior `S_j − S_i ≤ 2π − θ_{ij}` es una arista «de
subida» `i → j` con peso `2π − θ_{ij}`, y cada cota inferior
`S_j − S_i ≥ θ_{ij}`, reescrita `S_i − S_j ≤ −θ_{ij}`, es una arista «de
bajada» `j → i` con peso `−θ_{ij}`. Por el lema estándar de restricciones de
diferencias, el sistema es factible si y solo si el digrafo no tiene ciclos
dirigidos de peso negativo, y basta mirar ciclos **simples** (todo paseo
cerrado negativo contiene uno: los pesos se suman al descomponerlo). [Si no
hay ciclo negativo, `S_i :=` distancia mínima desde el nodo 1 satisface todas
las restricciones.]

Sea Γ un ciclo simple con `U` aristas de subida (`U ≥ 1`: los índices no
pueden solo bajar; y `U ≤ #aristas − 1`). Su peso es

    w(Γ) = Σ_subida (2π − θ) − Σ_bajada θ = 2πU − Σ_{e ∈ Γ} θ_e ,

luego `w(Γ) < 0 ⟺ Σ_{e∈Γ} θ_e > 2πU`. Como `θ ≤ π`, esto exige
`#aristas(Γ) > 2U`. En k = 4 un ciclo simple tiene a lo sumo 4 aristas, así
que solo `U = 1` puede dar ciclo negativo. Un ciclo con `U = 1` es una arista
de subida `i → j` seguida de una cadena estrictamente decreciente de `j` a
`i`, y su condición de negatividad, `θ_{ij} + Σ_cadena θ > 2π`, es
exactamente el certificado del subconjunto `{i, cadena, j}`: enumerando (lo
hace `corona.py` [B]), los subconjuntos de tamaño 2 dan `2θ > 2π`, imposible;
los de tamaño 3 son (T₁₂₃)–(T₂₃₄); el de tamaño 4 es (TOT). ∎

Obsérvese qué se usó: **solo** `θ ≤ π` y la simetría. Es un lema puro de
separación circular; la geometría de los círculos entra únicamente al
calcular θ con el Lema S1. [La verificación adversaria aportó además una
**demostración constructiva alternativa** sin dualidad: elegir primero
`Δ₁₃ = g₁ + g₂` en su ventana y después `Δ₂₄ = g₂ + g₃` en la suya, con
intervalos que las cinco condiciones mantienen no vacíos.]

## 5. El Lema U₄ global: tríos + zigzag

Para pasar de «orden fijo» a «algún orden» solo hay que observar que en
k = 4 los certificados de trío **no dependen del orden** (el orden cíclico
inducido en 3 elementos es único), y el único certificado que depende del
orden es (TOT). Los tres órdenes cíclicos de 4 elementos tienen totales

    orden (1,2,3,4):  θ₁₂ + θ₂₃ + θ₃₄ + θ₁₄     (excluye el par {θ₁₃, θ₂₄})
    orden (1,3,2,4):  θ₁₃ + θ₂₃ + θ₂₄ + θ₁₄     (excluye {θ₁₂, θ₃₄})
    orden (1,2,4,3):  θ₁₂ + θ₂₄ + θ₃₄ + θ₁₃     (excluye {θ₁₄, θ₂₃}) ,

es decir, `Σ_{i<j} θ_{ij}` menos uno de los tres emparejamientos perfectos.
El total mínimo corresponde al emparejamiento excluido **máximo**.

**Proposición C6 (el zigzag es el total mínimo).** Sean `a₁ ≥ a₂ ≥ a₃ ≥ a₄`.
Entonces el emparejamiento de suma máxima es el de extremos juntos,
`θ(a₁,a₂) + θ(a₃,a₄)`, y por tanto el total cíclico mínimo es el del orden
**zigzag** `(a₁, a₃, a₂, a₄)`:

    mín_π TOT(π) = Σ_{i<j} θ_{ij} − θ₁₂ − θ₃₄ .

*Demostración.* Con `σᵢ := log f(aᵢ)` (decreciente en i) se tiene la
identidad `θ(aᵢ,aⱼ) = g(σᵢ + σⱼ)` con `g(s) = 2 arcsin(e^{s/2})`, definida en
`s ≤ 0` (que es `f f' ≤ 1`), y

    g″(s) = e^{−s} / ( 2 (e^{−s} − 1)^{3/2} ) > 0     (identidad exacta, corona.py [A]):

`g` es convexa y creciente en `s < 0`; en el borde `s = 0` (par tangente a la
vez a la pared y entre sí, `θ = π`) `g` es continua y la convexidad en el
dominio cerrado vale por paso al límite. Los tres emparejamientos tienen sumas de pares
`{σ₁+σ₂, σ₃+σ₄}`, `{σ₁+σ₃, σ₂+σ₄}`, `{σ₁+σ₄, σ₂+σ₃}` con el mismo total
`Σσ`, y sus «anchuras» son respectivamente

    (σ₁−σ₃) + (σ₂−σ₄)  ≥  (σ₁−σ₂) + (σ₃−σ₄)  ≥  |(σ₁−σ₂) − (σ₃−σ₄)| ,

es decir, `{σ₁+σ₂, σ₃+σ₄}` mayoriza a los otros dos pares. Para `g` convexa,
mayorización con igual total implica suma de imágenes mayor:
`g(σ₁+σ₂) + g(σ₃+σ₄)` es la máxima de las tres. ∎

**Teorema C5 (Lema U₄, criterio global cerrado).** `{a₁ ≥ a₂ ≥ a₃ ≥ a₄}`
admite corona en el disco `R` (con todos los pares admisibles) si y solo si

    (i)  los cuatro tríos pasan:  θ(aᵢ,aⱼ) + θ(aⱼ,aₗ) + θ(aᵢ,aₗ) ≤ 2π ,
    (ii) Σ_{i<j} θ_{ij} − θ₁₂ − θ₃₄ ≤ 2π          (total del zigzag) .

*Demostración.* Corona ⟺ algún orden factible ⟺ (C4) los tríos pasan y algún
total ≤ 2π ⟺ tríos y total mínimo ≤ 2π ⟺ (C6) (i) y (ii). ∎

**Corolario C5′ (dos desigualdades bastan).** En (i) solo hace falta el
**trío top** `{a₁, a₂, a₃}`: por la monotonía de θ (Lema S1), cada par de
cualquier otro trío está dominado por el par correspondiente de
`{θ₁₂, θ₁₃, θ₂₃}` (p. ej. para `{a₁,a₃,a₄}`: `θ₁₃ ≤ θ₁₂`, `θ₁₄ ≤ θ₁₃`,
`θ₃₄ ≤ θ₂₃`), luego su suma es menor. El Lema U₄ completo es

    θ₁₂ + θ₁₃ + θ₂₃ ≤ 2π    y    Σ_{i<j} θ_{ij} − θ₁₂ − θ₃₄ ≤ 2π .

[Aportado por la verificación adversaria; en la frontera ambas condiciones
se activan por separado (652 y 520 veces en su barrido): ninguna es
redundante.]

**Observación (el orden decreciente no es óptimo).** Con `R = 1`,
`{B, B, s, s} = {0.499, 0.499, 0.33, 0.33}`: el orden decreciente
`(B, B, s, s)` es infactible (slack LP `−0.203`) y el zigzag `(B, s, B, s)`
es factible (slack `+0.019`). La lectura física: los dos círculos de casi
medio disco no deben ser vecinos angulares — el orden óptimo **separa los
grandes**, no los junta. (La intuición «ordenados como en S2» extrapolaba mal
el caso k = 3, donde poner el máximo en medio sí es óptimo.)

**Linealización T_c.** Por C5′ el criterio son dos condiciones, y la del
trío top tiene por cabeza a `a₁` (el máximo global): la hipótesis del Lema U
se cumple automáticamente y la condición es lineal en `T_c` con `c = R − a₁`:

    trío top pasa  ⟺  T_c(a₂) + T_c(a₃) ≥ τ_R .

La condición (ii) del zigzag es el objeto genuinamente nuevo: suma de cuatro
θ que no colapsa a un solo trío; para la Batalla 1 (paso 2) habrá que
tratarla directamente (véase §7).

## 6. El paisaje en k = 5: el pentagrama

En k = 5 el criterio de **solo** subconjuntos falla, y falla por un único
patrón. El recuento de ciclos simples del digrafo de diferencias da 84
ciclos: 26 con `U = 1` (= certificados de subconjunto, como en C4), 41 con
`U = 2`, y 17 con `U ≥ 3` que son imposibles por conteo (`≤ 5` aristas y
`Σθ ≤ 5π < 2πU`). De los 41 con `U = 2`, los 30 con `≤ 4` aristas son
imposibles también por conteo (`Σθ ≤ 4π`, nunca estrictamente mayor), y los
11 de 5 aristas se deciden con un LP exacto por patrón (maximizar la suma
del ciclo sujeta a todos los certificados de subconjunto y `θ ≤ π`,
`corona.py` [E]): **10 quedan dominados** (máximo exactamente `4π`, no
superable), y queda uno:

**El pentagrama.** El ciclo `(1→4, 4→2, 2→5, 5→3, 3→1)` usa los cinco pares
«diagonales» `D = {13, 24, 35, 14, 25}` (numeración por posición). Con

    θ* = π en D,   θ* = 0⁺ en los cinco pares «lado» {12, 23, 34, 45, 15} ,

todos los certificados de subconjunto pasan (con igualdad los ajustados) y
sin embargo `Σ_D θ* = 5π > 4π`: el sistema es infactible **sin certificado de
subconjunto**. El criterio de solo-subconjuntos es falso en k = 5. Pero el
pentagrama es lo ÚNICO que falta:

**Teorema C7 (criterio exacto por orden, k = 5, θ arbitrarias).** Para
`θ_{ij} ∈ (0, π]` arbitrarios simétricos, el sistema del Lema C1 para el
orden `(1, …, 5)` es factible si y solo si todos los certificados de
subconjunto pasan **y** `Σ_D θ ≤ 4π` (el certificado del pentagrama).

*Demostración.* Necesidad: C2 para los subconjuntos; para el pentagrama, su
ciclo tiene peso `4π − Σ_D θ`, que debe ser ≥ 0 si el sistema es factible
(cualquier ciclo del digrafo de un sistema factible tiene peso ≥ 0).
Suficiencia: como en C4, un ciclo negativo simple tiene `U = 1` (⟹ un
subconjunto falla), o `U = 2` con 5 aristas; de esos 11 patrones, 10 no
pueden ser negativos si los subconjuntos pasan (dominación LP exacta,
verificada con enumeración independiente por el autor y por el verificador)
y el undécimo es el pentagrama. `U ≥ 3` es imposible por conteo. ∎
[Enunciado aportado por la verificación adversaria, que ya lo contrastó en
30 000 matrices aleatorias además de las 2 500 de `corona.py` [E].]

`θ*` es además **no geométrico**, y la obstrucción es estructural: la matriz
geométrica `sin²(θ_{ij}/2) = fᵢfⱼ` es de rango 1 multiplicativo, y sobre el
pentagrama y el pentágono (dos 5-ciclos complementarios en K₅) vale la
identidad (`corona.py` [A])

    Π_D fᵢfⱼ = Π_lados fᵢfⱼ = (Π fᵢ)² :

θ ≈ π en las diagonales fuerza `fᵢfⱼ ≈ 1` alrededor de un ciclo **impar**, lo
que obliga a magnitudes alternantes `f, 1/f` incompatibles (con lados
admisibles, `fᵢfⱼ ≤ 1`, se propaga una contradicción). Cuantitativamente: el
**mejor valor hallado** de `Σ_D θ` sobre radios reales con todos los
certificados pasando es `7.5560` estricto (supremo de frontera `7.5742`,
radios ≈ `(0.310, 0.376, 0.303, 0.624, 0.200)` — nótese el radio `> R/2`;
récord del verificador con dos búsquedas independientes, incluida una en el
espacio `log f`; una optimización anterior del autor capada a radios `< R/2`
se quedaba en 7.311). Sigue lejísimos del `4π = 12.566` que necesitaría la
violación. Además los barridos geométricos (4 200 pares instancia-orden del
autor con radios hasta 0.9, y 44 962 del verificador) no encontraron ninguna
discrepancia entre el criterio de solo-subconjuntos y el LP.

**Conjetura C8 (k = 5 geométrico: el pentagrama es redundante).** Para θ
provenientes de radios (Lema S1) con todos los pares admisibles, si todos
los certificados de subconjunto pasan entonces `Σ_D θ ≤ 4π`.
Equivalentemente (por el Teorema C7): el criterio de solo-subconjuntos por
orden es exacto para θ geométricas también en k = 5. — Declarada como hueco;
la evidencia es la dominación exacta de 40/41 patrones (demostrada), la
identidad de rango 1 y el margen numérico `7.57` vs `12.57`.

**Advertencia (la forma global es falsa en k = 5, ya geométricamente).** A
diferencia de k = 4, los certificados de los subconjuntos de tamaño 4
dependen del orden inducido, y el cuantificador **no conmuta**: con radios
`{0.45920, 0.44376, 0.40188, 0.34898, 0.19152}` en `R = 1`, todo subconjunto
pasa con *su* mejor orden y sin embargo ningún orden único satisface todos
sus certificados a la vez (mejor slack `−0.00345`; el verificador comprobó
de propina que los cinco cuartetos tienen corona **real**, slacks `+0.005` a
`+0.46`, y aportó un contraejemplo propio con margen mayor: radios
`(0.43884, 0.38898, 0.37581, 0.37105, 0.35136)`, tríos ≥ `+0.62`, cuartetos
≥ `+0.156`, corona de 5 infactible con slack `−0.099`, confirmado con un
oráculo euclídeo sin S1). Para k ≥ 5 el criterio correcto es por orden (o el
LP directamente); «cada subconjunto por su cuenta» solo da la dirección
necesaria del Lema C2/C2′.

## 7. Lectura para la Batalla 1

El paso 2 de la Batalla 1 (dos ocupantes en corona: `v` = sartén de radio
`R = α + 1` con ocupantes `{α, γ}`, `m = 1` sale, `S = {σ₁, σ₂}` a
reinsertar) queda ahora **formulado exactamente** en su parte de corona:

- **Dirección de cota inferior (la que el programa necesita).** Bloqueo ⟹
  `{α, γ, σ₁, σ₂}` no empaqueta en `v` ⟹ en particular no hay corona ⟹
  (Corolario C5′) **o bien** el trío top `{α, γ, σ₁}` falla —una sola
  desigualdad lineal en `T_c`, `T_c(γ) + T_c(σ₁) < τ_R` con `c = R − α`, vía
  el Lema U con hipótesis automática— **o bien** el total del zigzag
  `(α, γ)` separados por `(σ₁, σ₂)` supera `2π`. Dos ramas algebraicas
  explícitas sobre `(α, γ, σ₁, σ₂)`: el programa de bloqueo de `esquina.md`
  gana dos ramas exactas en vez de un proxy.
- **Dirección constructiva (testigos y familias aproximantes).** El Lema C1
  produce colocaciones explícitas: cualquier solución del sistema de huecos
  es una corona válida (sin oráculos numéricos de empaquetamiento).
- **Lo que este documento NO da** es el paso «empaquetamiento cualquiera ⟹
  corona» (ocupantes interiores, paso 3 del plan): el criterio caracteriza
  coronas, no empaquetamientos generales. Para k = 3 esa equivalencia es
  exactamente el hueco de exactitud de `feas3` (`perfil_tres.md` §5,
  `hoja_de_ruta.md` §7.6), que sigue abierto y **no** se usa aquí.

De regalo, el Teorema C5 con `k = 3` (tomar `a₄ = 0`) se reduce al criterio
del trío `Σθ ≤ 2π`, coherente con los Lemas S2/S3 (la dirección constructiva
de S2 es el caso k = 3 del Lema C1 + C4).

## 8. Huecos declarados

1. **Conjetura C8**: redundancia geométrica del pentagrama en k = 5 (la
   cota `Σ_D θ ≤ 4π` bajo certificados). No afecta a ninguna cota inferior:
   la necesidad (Lema C2, y C7-necesidad para el pentagrama) es
   incondicional y es la única dirección que las cotas usan.
2. **k ≥ 6**: sin criterio combinatorio cerrado; quedan el Lema C2
   (necesidad) y el LP por orden (decidible e implementado), que bastan para
   explorar. Dirección natural (observación del verificador): los
   certificados irreducibles de winding `q` son **polígonos estrella**
   `{m/q}` sobre subconjuntos, con condición `Σθ ≤ 2πq` — los subconjuntos
   son `{m/1}` y el pentagrama es `{5/2}`; candidato a censo general.
3. **Corona vs empaquetamiento general**: este documento caracteriza coronas.
   El «lema de empujar a la pared» (¿el v adversarialmente óptimo tiene a los
   ocupantes en corona?) es el paso 3 de la Batalla 1 y sigue abierto.
4. El slack del LP se calcula con `scipy` (método `highs`); los Teoremas
   C4/C5 son exactos y no dependen de ello (el LP es solo el oráculo de
   contraste en la verificación).

## Mapa de verificación

`code/corona.py`, cinco bloques (5/5 OK):

- **[A]** simbólico (sympy): `g″` en forma cerrada y positiva (convexidad),
  la identidad `θ = g(log f + log f)`, y la identidad de rango 1 del
  pentagrama/pentágono.
- **[B]** dual k = 4: enumeración de los ciclos simples del digrafo up/down
  (los `U = 1` de ≥ 3 nodos son exactamente {4 tríos, total}; todo ciclo con
  `U ≥ 2` tiene `≤ 2U` aristas ⟹ nunca negativo), y el criterio contra el LP
  en 1 500 matrices θ arbitrarias + 3 600 pares (instancia, orden)
  geométricos: 0 discrepancias.
- **[C]** Lema U₄ global contra LP-todos-los-órdenes (2 500 instancias, 0
  discrepancias), equivalencia con la forma reducida C5′ (0 discrepancias),
  la región antes no muestreada (radios hasta 0.9 y pares `a₁ + a₂ = R`
  exactos, 1 600 instancias, 0 discrepancias), LP contra dos oráculos no
  lineales independientes —el angular y uno **euclídeo puro sin S1**—, los
  dos contraejemplos fijados (ingenuo y decreciente) y la reducción k = 3 al
  certificado único (800 instancias).
- **[D]** zigzag: las dos desigualdades de intercambio en 20 000 cuádruplas
  (0 violaciones) y «el total mínimo es el zigzag» en 1 500 instancias.
- **[E]** k = 5: censo de 84 ciclos (30 patrones `U = 2` cortos por conteo +
  dominación LP exacta de 10/11 largos), el pentagrama alcanza `5π` con `θ*`
  que viola la identidad de rango 1 (no geométrico), el **Teorema C7**
  contra el LP en 2 500 matrices arbitrarias (0 discrepancias), barrido
  geométrico de 4 200 pares con radios hasta 0.9 sin discrepancias
  (Conjetura C8), el récord geométrico del pentagrama (`Σ_D = 7.556` con
  certificados holgados) y el contraejemplo a la versión global (el
  cuantificador no conmuta).
