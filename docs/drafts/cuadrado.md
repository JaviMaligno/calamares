# La constante hermana de Tribonacci en la sartén cuadrada

Documento de trabajo sobre el punto 4 de la hoja de ruta (afilados en cuadrado).
Objetivo original: repetir el álgebra del suelo de la familia de 4 aros
(`resultados.md` §5quater) y la escalera del lema de reinserción
(`reinsercion.md` §7 y §9) en sartén **cuadrada**, con el hueco de esquina en el
papel del bolsillo de Descartes. El resultado tiene dos partes, y la segunda no
estaba en el guion:

1. **La constante hermana existe y es algebraica de grado 4.** El calco exacto
   de la familia rígida de 4 aros da

       X = 1.7110185903…,   raíz de   17x⁴ − 4x³ − 62x² + 4x + 49,

   con toda la estructura del disco intacta: las dos presiones, la identidad
   del punto fijo `b_□(X) = X − 1`, la escalera de tres peldaños en el límite
   rígido.

2. **Pero en el cuadrado el límite rígido no manda.** Hay un fenómeno nuevo sin
   análogo en el disco — el *par deslizado* — que produce bloqueos más baratos
   que los rígidos, y una familia de instancias que realiza fallos de best fit
   con `ρ < X`. La constante `X` es el suelo exacto de la familia rígida, pero
   **no** es el umbral del cuadrado, que queda estrictamente por debajo
   (mejor fallo verificado: `ρ = 1.685`).

Cada afirmación lleva su etiqueta: **[D]** demostrado, **[D*]** demostrado
módulo la idealización tangente (el mismo hueco declarado que tiene el disco en
el punto 1 de la hoja de ruta), **[N]** evidencia numérica. Verificación:
`code/cuadrado.py`.

## 1. Modelo

La sartén es ahora un cuadrado de lado `s` (en la notación del enunciado,
`s = 2L`). Los hermanos de la sartén se empaquetan como círculos disjuntos
dentro del cuadrado; **los agujeros de los aros siguen siendo discos**, de modo
que el anidamiento y la factibilidad dentro de agujeros no cambian y toda la
maquinaria de discos (`Lema 0`, `sim.pack_feasible`, `reinserta.feas`) se
reutiliza tal cual. Solo cambia la geometría del contenedor raíz.

## 2. Tres hechos exactos del cuadrado

**Lema C1 (el par es exacto). [D]** Dos círculos de radios `a ≥ b` caben en el
cuadrado de lado `s` si y solo si

    a ≤ s/2   y   a + b ≤ (2 − √2)·s.

*Demostración.* Los centros están confinados a las cajas `[a, s−a]²` y
`[b, s−b]²` (no vacías sii `a, b ≤ s/2`). La distancia máxima entre un punto de
cada caja se alcanza en esquinas extremas opuestas y vale `√2(s − a − b)`; la
condición de no solape es `√2(s − a − b) ≥ a + b`, que reordenada es
`a + b ≤ √2·s/(1+√2) = (2−√2)·s`. ∎

Dos diferencias con el disco: la capacidad del par no es `s` sino
`(2−√2)s ≈ 0.5858·s`, y la condición `a ≤ s/2` **no** está implicada por la
suma (en el disco `a + b ≤ R` implica `a ≤ R`). En el caso de igualdad
`a + b = (2−√2)s` la colocación es **rígida**: cada círculo clavado en su
esquina, tangentes sobre la diagonal (la distancia máxima solo se alcanza en
las esquinas extremas de las cajas).

**Lema C2 (fila diagonal; Lema 0 cuadrado). [D]** Círculos `r₁ ≥ r₂ ≥ … ≥ r_k`
caben en el cuadrado si, colocando los dos mayores en los extremos,

    2·Σrᵢ + (√2 − 1)(r₁ + r₂) ≤ √2·s.

En particular basta `Σrᵢ ≤ (2−√2)·s`. *Demostración.* Fila tangente sobre la
diagonal con los extremos encajados en las esquinas: el primer centro a
distancia `√2·r₁` de la esquina a lo largo de la diagonal, consecutivos a
distancia `rᵢ + rᵢ₊₁`, el último a `√2·r₂` de la otra esquina; la longitud
requerida es `√2 r₁ + (2Σr − r₁ − r₂) + √2 r₂ ≤ √2 s`, que es la condición. La
holgura lateral de un círculo intermedio `rᵢ` a los lados próximos es su
distancia a la esquina dividida por `√2`, al menos `(√2 r₁ + r₁ + rᵢ)/√2 ≥ rᵢ`
porque `r₁ ≥ rᵢ` (y simétricamente desde la otra esquina con `r₂ ≥ rᵢ`). Para
`k = 2` la condición se reduce al Lema C1, que es exacto. ∎

**Lema C3 (bolsillo de esquina). [D]** Sea un círculo de radio `a` encajado en
una esquina (tangente a sus dos lados). El mayor círculo tangente a los dos
lados de una esquina **adyacente** que no lo corta tiene radio

    x = (√s − √a)².

*Demostración.* Con la esquina de `a` en el origen y la adyacente en `(s, 0)`,
los centros son `(a, a)` y `(s − x, x)`. Entonces
`|Δ|² − (a+x)² = (s − a − x)² + (x − a)² − (a + x)² = (s − a − x)² − 4ax`,
y la tangencia externa da `s − a − x = 2√(ax)`, es decir `√x = √s − √a`
(rama positiva; el signo de `s − a − x` es correcto en todo el rango usado,
pues en la raíz vale `2√(ax) ≥ 0`). ∎

En la esquina **opuesta** el mismo cálculo sobre la diagonal da
`x = (2−√2)s − a`. Contraste con el disco: el bolsillo de Descartes
`AB(A+B)/(A²+AB+B²)` depende de los dos círculos colocados; el bolsillo de
esquina solo ve, de cada círculo, la cota `(√s − √a)²`, que **decrece en a**:
cuando varios círculos acechan la misma esquina adyacente, manda el grande.
La demostración de C3 solo usa la tangencia del círculo `a` a los dos lados de
*su* esquina a través de la posición `(a, a)`; la fórmula de la cota vale para
`a` en cualquier posición `(a_x, a_y)` sustituyendo la distancia — esto será
relevante en §6.

## 3. La configuración rígida y el bolsillo b_□

Configuración canónica: `{α, 1}` llenan la sartén cuadrada al límite,

    α + 1 = (2 − √2)·s,   es decir   s = (1 + α)/(2 − √2),

colocación forzada en diagonal (igualdad del Lema C1; hace falta además
`α ≤ s/2`, que vale para todo `α < 3 + 2√2 ≈ 5.83`). Quedan libres las otras
dos esquinas, ambas adyacentes a los dos círculos; por el Lema C3 el bolsillo
de cada una es

    b_□(α) = (√s − √max(α, 1))²,   s = (1 + α)/(2 − √2).

**V1 (bolsillo = máximo insertable, caso rígido). [N]** El mayor círculo
insertable en la configuración rígida es exactamente `b_□(α)`: la dirección
`≥` es el Lema C3 (el bolsillo *es* insertable); la dirección `≤` está
verificada con un buscador de mayor círculo vacío (rejilla + refinado):
diferencia `< 10⁻⁵` en todo el barrido de α (`cuadrado.py`, sección 3).

**Mínimo cerrado del bolsillo. [D]** A diferencia del disco (donde el bolsillo
rígido `b(α)` es creciente), `b_□` tiene un mínimo interior exacto:

    min_α b_□(α) = b_□(√2) = 1/√2,

vía la identidad `√((4 + 3√2)/2) = 2^{1/4} + 2^{−1/4}` (elevar al cuadrado la
derecha da `(4+3√2)/2`; verificada en simbólico). Consecuencia inmediata:
cualquier bloqueo de la plantilla canónica cuadrada exige `ρ ≥ 2·b_□ ≥ √2` —
una cota universal que en el disco no existe (allí `b(α) → 0` con `α → 0`).

## 4. El suelo de la familia rígida de 4 aros: la ecuación

Calco del álgebra de `resultados.md` §5quater. Familia `{r₁ = 1, r₂ = t, r₃,
r₄}` en sartén cuadrada rígida `s = (1 + t)/(2 − √2)`, límite tangente
(`r₃ → t`, `w → 0`). Las dos presiones:

- **Infactibilidad del trío** `{1, r₃, r₄}` en la sartén: con `{1, r₃}` en
  diagonal rígida, hace falta `r₄` mayor que el bolsillo de esquina (manda el
  círculo grande, `a = 1`):

      r₄ > P(t) = (√((1+t)/(2−√2)) − 1)²
      ⟹  ρ₂ = (r₃ + r₄)/r₂ ≥ 1 + P(t)/t.

- **La pareja cabe en el agujero de r₁** (un disco, capacidad `1 − w → 1`):
  `r₃ + r₄ ≤ 1`, luego `ρ₂ ≤ 1/t`.

Compatibles si y solo si `P(t) ≤ 1 − t`, y el ínfimo de `ρ` se alcanza en el
cruce `P(t*) = 1 − t*`. Eliminando raíces (`√((1+t)/c) = 1 + √(1−t)` con
`c = 2−√2`, dos cuadrados):

    (11 − 6√2)·t² + (2√2 − 2)·t − (7 − 4√2) = 0,
    t* = 0.5844471858…

y la constante del cuadrado es `X = 1/t*`:

    (7 − 4√2)·X² + (2 − 2√2)·X − (11 − 6√2) = 0,

    X = [(2√2 − 2) + √(512 − 352√2)] / (2(7 − 4√2)) = 1.7110185903…

Multiplicando por la cuadrática conjugada (√2 → −√2) se obtiene el polinomio
racional mínimo, de grado 4 (las otras tres raíces, ≈ −1.446, −1.094, 1.065,
son las ramas espurias de los cuadrados):

    17·X⁴ − 4·X³ − 62·X² + 4·X + 49 = 0,

y para `t*`: `49t⁴ + 4t³ − 62t² − 4t + 17 = 0`. **[D*]** — el álgebra y las
identidades son exactas (verificadas en simbólico); el estatus `[D*]` viene de
la idealización tangente heredada del disco (§8) y de V1.

La identidad del punto fijo del disco, `b(T) = T − 1`, se conserva exacta:

    b_□(X) = X − 1

(en la normalización de la familia: `P(t*) = 1 − t*`; verificada en simbólico
a 60 dígitos y por álgebra de la cuadrática). La comparación:

|                       | disco                          | cuadrado (familia rígida)         |
|-----------------------|--------------------------------|-----------------------------------|
| capacidad del par     | `a + b ≤ R` (exacta)           | `a + b ≤ (2−√2)s` y `a ≤ s/2` (exacta) |
| bolsillo rígido       | `α(α+1)/(α²+α+1)` (Descartes)  | `(√s − √α)²` (esquina)            |
| ecuación del suelo    | `t³ + t² + t = 1`              | `49t⁴ + 4t³ − 62t² − 4t + 17 = 0` |
| constante             | `T = 1.8392868` (cúbica)       | `X = 1.7110186` (cuártica)        |
| identidad del suelo   | `b(T) = T − 1`                 | `b_□(X) = X − 1`                  |

## 5. La escalera cuadrada en la rebanada rígida

Plantilla canónica del intercambio (`reinsercion.md` §7): `v` es la sartén
cuadrada rígida `s = (1+α)/(2−√2)` ocupada por `α` y por `m` (`r_m = 1`,
normalizado); el intercambio saca a `m`, coloca `σ₁ ≤ 1` en su lugar y falla
solo si `σ₂` no cabe en ningún sitio de `v`.

**Peldaño 1 (bolsillo solo; Proposición 2 cuadrada). [D]** Si el intercambio
falla, `σ₂` supera el mayor hueco disponible, que contiene siempre al bolsillo
rígido: `σ₂ > b_□(α)`. Con las dos colas (`ρ ≥ σ₁ + σ₂ > 2b_□(α)` porque
`σ₁ ≥ σ₂`, y `ρ ≥ (1 + σ₁ + σ₂)/α`),

    ρ > B_□(α) = max( 2·b_□(α), (1 + 2·b_□(α))/α ).

La segunda rama decrece; la primera no es monótona (mínimo `√2` en `α = √2`,
§3) pero el mínimo de la envolvente está en el cruce `2·b_□(α)(α − 1) = 1`:

    α₁ = 1.7033992…,  raíz de  4α⁸ − 64α⁶ + 80α⁵ + 100α⁴ − 128α³ − 48α² + 8α + 49,

    Φ_□ = B_□(α₁) = 1/(α₁ − 1) = 1.4216678…

**En el disco este peldaño es un punto fijo — mínimo en `α = φ` con valor
exactamente `φ` — y esa coincidencia se rompe en el cuadrado**
(`Φ_□ = 1.4217 ≠ α₁ = 1.7034`): la coincidencia áurea es un accidente del
disco, no una propiedad del mecanismo. Nótese que este peldaño es una cota
inferior genuina para *todo* bloqueo de la plantilla canónica (usa solo que el
hueco disponible es al menos el bolsillo rígido), también para los bloqueos
deslizados de §6.

**Peldaños 2 y 3 en la rebanada rígida `σ₁ = 1`. [D*]** Si además se exige la
condición completa del trío en la frontera rígida (`σ₁ → 1`,
`σ₂ → b_□(α)⁺`), el ínfimo es `ρ = max(1 + b_□(α), (2 + b_□(α))/α)`,
minimizado en el cruce `b_□(α)(α − 1) = 2 − α`:

    α₂ = 1.5853122…,  raíz de  α⁸ + 16α⁷ − 4α⁶ − 208α⁵ + 226α⁴ + 400α³ − 508α² − 208α + 289,

    ρ = 1/(α₂ − 1) = 1.7084900…

(análogo del cruce exacto de la cúbica del disco `2α³ = α² + 2α + 2`, de valor
`1/(α* − 1) = 1.7990556`; `reinsercion.md` §9 lo reporta como `≈ 1.79966`
desde la malla numérica). Y con la colocación del testigo (`S` cabe en
`u` = agujero de `α`): `1 + b_□(α) ≤ α`, imposible para `α < X` y de ínfimo
creciente `1 + b_□(α)` para `α ≥ X`; mínimo global en

    α = X:   ρ = 1 + b_□(X) = X,

el mismo punto fijo `ρ = α` que en el disco produce `T`. La escalera rígida:

| recursos usados                        | disco    | cuadrado (σ₁ = 1) |
|----------------------------------------|----------|----------|
| bolsillo solo                          | `φ = 1.6180` (punto fijo) | `Φ_□ = 1.4217` (sin punto fijo) |
| + infactibilidad del trío (frontera rígida) | `1.7991` | `1.7085` |
| + colocación del testigo               | `T = 1.8393` (punto fijo) | `X = 1.7110` (punto fijo) |

En el disco la restricción a `σ₁ = 1` no cuesta nada: el criterio angular
exacto muestra que bajar `σ₁` encarece o imposibilita el bloqueo, así que la
rebanada rígida ES el óptimo y la escalera termina en `T`. La siguiente
sección muestra que en el cuadrado esto es falso.

## 6. La ruptura: el par deslizado

**El fenómeno. [N]** En la sartén rígida `s = (1+α)/(2−√2)`, sustitúyase `m`
por `σ₁ < 1`: el par `{α, σ₁}` gana holgura `1 − σ₁` y ya no está clavado en
la diagonal. La colocación adversaria que más abre el mayor hueco no es la
diagonal: es **σ₁ encajado en una esquina y α tangente a σ₁ y a un lado**,
deslizado por la pared hacia σ₁ todo lo que la tangencia permite. Eso aleja α
de la esquina libre opuesta y el bolsillo de esquina crece *linealmente* con
el deslizamiento. Medido con el buscador de mayor círculo vacío maximizado
sobre colocaciones del par (`M(α, σ₁)`, `cuadrado.py` sección 6):

    M(X, 1.00) = b_□(X) = 0.711,   M(X, 0.92) ≈ 0.766,   M(X, 0.84) ≈ 0.837.

El bloqueo exige `σ₂ ∈ (M(α, σ₁), σ₁]`, ventana no vacía mientras
`M(α, σ₁) < σ₁` (se cierra cerca de `σ₁ ≈ 0.837` en `α = X`), y cuesta solo
`ρ ≥ σ₁ + σ₂ > σ₁ + M(α, σ₁)`, que **decrece** al bajar `σ₁` (el bolsillo se
abre más despacio de lo que baja la cola): mínimo en la malla, con testigo
válido, `ρ = 1.6765` en `(α, σ₁) = (X, 0.84)` — por debajo de `X`.

**Por qué el disco no tiene este fenómeno. [N]** Con el criterio angular
exacto del disco: en `α = T`, bajar `σ₁` a `0.96` *sube* el mínimo `σ₂`
bloqueante a `0.948` (`ρ = 1.908 > T`), y en `σ₁ = 0.90` ya no existe ningún
`σ₂ ≤ σ₁` bloqueante — la pared circular abre el hueco por encima de `σ₁` en
cuanto el par respira, y la ventana se cierra. En el cuadrado la ventana
sobrevive porque el hueco relevante está en una esquina *lejana* cuya apertura
es más lenta. La geometría de la tangencia deslizada es una cadena explícita
(σ₁ en esquina, α tangente a σ₁ y a un lado, bolsillo tangente a α y a los dos
lados de la esquina libre), así que `M` tiene forma cerrada por el mismo
método del Lema C3; el sistema es

    (y + h − σ₁)² = (α + σ₁)² − (s − α − σ₁)²      (α tangente a σ₁ y al lado)
    (s − α − x)² + (h − x − y)² = (α + x)²          (bolsillo tangente a α)

con `h = s/2` y `x = M`. No lo reducimos aquí a un polinomio; la versión
numérica está contrastada punto a punto con el buscador de huecos.

**La familia deslizada: fallos realizables con ρ < X. [N]** El bloqueo
deslizado se convierte en instancia real `{α, 1, σ₁, σ₂}` con `w` grande (los
anidamientos internos de `S` y el agujero de `m` hay que bloquearlos:
`σ₂ > 1 − w`, `σ₂ > σ₁ − w`) y testigo `σ₁ + σ₂ ≤ α − w`. Instancias
verificadas (voraz cuadrado, `cuadrado.py` sección 8):

- **D**: `α = 1.845`, `w = 0.16`, `σ = {0.844, 0.841}`, sartén rígida
  `s = 4.8569`: best fit coloca 3, worst fit y el lex-máximo 4.
  **`ρ = 1.685 < X = 1.7110`.** El trío deslizado `{1.845, 0.844, 0.841}` es
  infactible (certificado `M = 0.8407 < 0.841` y solver con 120 reinicios).
  Vive casi en el suelo deslizado: margen sobre `M` de solo `3·10⁻⁴`.
- **D′** (control negativo): `σ₁ = 0.840` cierra la ventana
  (`M = 0.8447 > σ₂`), el trío es factible y no hay fallo — el certificado
  `M` predice exactamente dónde muere la familia.
- **E**: `α = 1.859`, `w = 0.15`, `σ = {0.856, 0.853}`, margen de bloqueo
  holgado (`M ≈ 0.83`): best fit 3, lex-máximo 4, `ρ = 1.709 < X`.

Consecuencia: **el umbral del cuadrado es estrictamente menor que `X`**. El
mejor fallo verificado da cota `≤ 1.685`; el relajado de 3 ingredientes
(sin las ligaduras de anidamiento) baja hasta `≈ 1.6765`, y el suelo de la
familia deslizada realizable (donde la ventana `M(α, σ) = σ` se cierra contra
testigo y anidamiento) se estima numéricamente en `ρ ≈ 1.68`; por debajo actúa
la cota del peldaño 1 (`ρ > Φ_□ = 1.4217` para todo bloqueo de la plantilla
canónica). La brecha `(Φ_□, 1.685)` queda abierta.

## 7. Instancias de la familia rígida (los calcos directos de 5ter)

Aunque la familia deslizada la supera por abajo, la familia rígida cuadrada
funciona exactamente como su análoga del disco (`cuadrado.py`, sección 7;
sartén rígida `s = 1.5/(2−√2) = 2.560660` para `{1, 0.5}`):

- **A (calco de `resultados.md` §5ter).** `w = 0.03`, radios
  `{1, 0.5, 0.49, 0.48}`, `ρ = 1.94`. Best fit anida el `0.5` en el agujero
  del `1` (capacidad `0.97`), el `0.49` va a la sartén y el `0.48` queda
  bloqueado en todas partes: sartén `{1, 0.49, 0.48}` infactible
  (`M(1, 0.49) = 0.367 < 0.48`), agujero con el `0.5` (`0.98 > 0.97`),
  agujeros del `0.5, 0.49` (`0.47, 0.46 < 0.48`). Tres aros. El testigo — que
  coincide con worst fit — pone el `0.5` en la sartén (tangencia diagonal
  exacta) y la pareja `{0.49, 0.48}` en fila exacta en el agujero (`0.97`):
  cuatro aros. **[N]**
- **B**: `w = 0.10`, radios `{1, 0.5, 0.495, 0.405}`, `ρ = 1.80 < T`. Misma
  estructura (`M(1, 0.495) = 0.364 < 0.405`). Ya una instancia *rígida*
  cuadrada falla por debajo del umbral conjeturado del disco.
- **C**: `w = 0.12`, radios `{1, 0.5, 0.495, 0.385}`, `ρ = 1.76`.

Igual que en el disco, el suelo `X` de la familia rígida no se alcanza con
márgenes positivos (los bloqueos de anidamiento exigen `w > 0` que encoge el
agujero); la familia rígida se queda en `ρ ≈ 1.76` y es la deslizada la que
baja hasta `1.685`.

## 8. Estatus, conjetura y huecos

**Demostrado [D]:** Lemas C1–C3; rigidez del par en la igualdad; mínimo
cerrado `min b_□ = 1/√2` en `α = √2`; peldaño 1 completo (cota `ρ > Φ_□` para
todo bloqueo de la plantilla canónica, deslizados incluidos); las identidades
algebraicas (cuadráticas, cuárticas, `b_□(X) = X − 1`, ruptura del punto fijo
en el peldaño 1, punto fijo en el 3).

**Demostrado módulo idealización [D*]:** que `X` es el ínfimo del álgebra de
la familia rígida (las dos presiones de §4) y de la plantilla canónica
restringida a la rebanada `σ₁ = 1`. Supuestos no cerrados: V1 (máximo hueco =
bolsillo, evidencia `< 10⁻⁵`), y la idealización tangente heredada del disco.

**Evidencia numérica [N]:** V1; el par deslizado y la función `M(α, σ₁)`; la
infactibilidad de los tríos de las instancias A–E (solver con reinicios +
certificado `M`); los fallos/aciertos de best/worst fit contra el lex-máximo.

**Lo que el cuadrado enseña sobre el disco.** La escalera del disco termina en
`T` gracias a un hecho que allí parece un detalle técnico y aquí se revela
esencial: *en el disco la rebanada rígida `σ₁ = 1` es óptima* (bajar `σ₁`
imposibilita el bloqueo). El cuadrado muestra que eso no es gratis — depende
de la curvatura de la pared. Cualquier intento de generalizar el lema
universal de reinserción a contenedores no circulares tendrá que controlar el
par deslizado, no solo el bolsillo rígido.

**Conjetura (umbral cuadrado).** El umbral de irrelevancia de colocación en
sartén cuadrada está en `[Φ_□, 1.685] = [1.4217, 1.685]`, estrictamente por
debajo de `X` y de `T`; conjeturamos que es el suelo de la familia deslizada,
`ρ_slide ≈ 1.68`, caracterizado por el sistema de tangencias de §6 con la
ventana cerrándose (`M(α, σ) = σ`). Reducirlo a forma cerrada es álgebra
elemental pero pesada (cadena de tres tangencias); queda pendiente.

**Huecos concretos, por orden de valor:**

1. Forma cerrada de `M(α, σ₁)` (sistema de §6) y del suelo deslizado; con
   ella, la versión cuadrada de la Proposición 3 con **cuatro** ingredientes
   (bolsillo deslizado + trío + testigo + recursos combinatorios `H_m` y
   anidamiento, que son exactamente los que encarecen la familia deslizada
   vía `σ₂ > 1 − ω`).
2. V1 como lema (análisis finito de patrones de tangencia del mayor círculo
   vacío: esquina/lado/círculos).
3. ¿Es la familia deslizada óptima? Búsqueda dirigida tipo `banda.py` en
   cuadrado por debajo de `1.685` (la ventana crítica ahora es el
   deslizamiento, no `α ≈ φ`).
4. La irrelevancia para `n ≤ 3` está demostrada en el disco; la demostración
   usa geometría del disco y hay que revisar qué sobrevive en el cuadrado.
5. Dimensión superior y otros polígonos: el par deslizado existirá en todo
   contenedor con esquinas; el disco podría ser exactamente el contenedor
   *más protector* (la pared curva cierra la ventana del deslizamiento).

## Mapa de verificación

- `code/cuadrado.py` — todo en un script, ejecutado desde `code/`:
  1. álgebra exacta en sympy (cuártica como producto de conjugadas, derivación
     del suelo por doble cuadrado, raíz explícita, `b_□(X) = X − 1` a 60
     dígitos, cuártica de `t*`, `b_□(√2) = 1/√2`);
  2. condición exacta del par contra el solver físico cuadrado
     (`pack_feasible_square`, calco de `sim.pack_feasible` con proyección por
     coordenada sobre el cuadrado);
  3. bolsillo de esquina = mayor círculo vacío en la configuración rígida
     (barrido en α, rejilla + refinado);
  4. las dos presiones del suelo y su cruce en `t*` (ventana no vacía sii
     `t ≤ t*`, valor común `X`);
  5. escalera rígida: los tres cruces por bisección, contra los polinomios
     racionales de grado 8, 8 y 4 (residuo en la raíz);
  6. el par deslizado: `M(α, σ₁)` por rejilla 4D de colocaciones + refinado,
     ventana `M < σ₁`, mínimo del relajado con testigo, y el contraste con el
     disco vía el criterio angular exacto (`trio.min_s2_blocking`);
  7. instancias rígidas A, B, C: voraz best/worst en sartén cuadrada contra
     el lex-máximo, con `M` como certificado del bloqueo del trío;
  8. familia deslizada: D (fallo con `ρ = 1.685 < X`), D′ (control negativo:
     la ventana se cierra donde `M` lo predice) y E (fallo con margen holgado,
     `ρ = 1.709 < X`).
