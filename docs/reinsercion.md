# El lema de reinserción: dónde acaba la combinatoria y empieza la geometría

Documento de trabajo sobre el punto 2 de la hoja de ruta (conjetura del umbral de
Tribonacci). El objetivo declarado allí era «convertir el rescate de bolsillos en un
lema universal de reinserción». Lo que sigue no demuestra la conjetura: la
descompone en una parte combinatoria, que queda cerrada con una cota exacta, y una
parte geométrica, que queda aislada y cuantificada, con la ventana de riesgo
localizada en la razón áurea.

## 1. El hueco exacto

En la prueba del Teorema 2 (irrelevancia de la colocación, `resultados.md` §5) la
superincrecencia se usa **una sola vez**. Sea `m` el mayor aro que el voraz `F` y el
testigo `P` colocan en contenedores distintos, `u = c_F(m)`, `v = c_P(m)`, y

    S = { aros de radio < r_m que P coloca en u }.

El paso de intercambio traslada `m` a `u` y necesita reubicar `S`. Bajo
superincrecencia `Σ S < r_m` y el Lema 0 mete `S` en fila dentro del disco que `m`
deja vacante en `v`. Sin superincrecencia `Σ S` puede superar `r_m` y el argumento se
detiene ahí. Todo lo que separa el Teorema 2 de la conjetura del umbral de
Tribonacci es ese paso.

## 2. Qué queda libre en el intercambio

Al sacar `m` de `v` y meterlo en `u` quedan disponibles exactamente dos contenedores,
y conviene nombrarlos porque el segundo se pasa por alto con facilidad:

- **`D_m`**, el disco de radio `r_m` que `m` ocupaba en `v`. Queda libre entero, y
  cualquier empaquetamiento dentro de su huella es legal sin tocar el resto de `v`.
- **`H_m`**, el agujero de `m`, de capacidad `r_m − w`. `m` viaja a `u` **con su
  agujero**, que sigue siendo un contenedor utilizable. Los aros de `S` son menores
  que `r_m`; los que además midan `≤ r_m − w` pueden alojarse ahí.

A esos dos se añade el anidamiento recursivo dentro del propio `S`. Son dos discos
disjuntos, de capacidades `r_m` y `r_m − w`, más los agujeros que `S` genera.

## 3. El problema abstracto

Normalizando `r_m = 1` y escribiendo `ω = w / r_m`, lo único que el parámetro `ρ`
impone sobre los aros menores que `r_m` es

    Σ X ≤ ρ        y        Σ_{l>j} X_l ≤ ρ · X_j  para todo j,

llamemos a tal secuencia **ρ-decreciente** (superincreciente es el caso `ρ < 1`).
Definimos

    ρ*(ω) := mín { ρ_needed(X) : X ⊂ (0,1) ρ-decreciente, no aceptada por N(1) ⊎ N(1−ω) },

donde `ρ_needed(X)` es el menor `ρ` compatible con `X` y `N(c)` denota un nido de
capacidad `c` con anidamiento recursivo. Como toda `S` realizable en una instancia
con parámetro `ρ` satisface esas dos desigualdades, **`ρ*(ω)` es una cota inferior
rigurosa del `ρ` que necesita cualquier fallo del paso de intercambio**:

> Si `ρ < ρ*(ω)`, la reinserción existe siempre, y sin mirar la geometría de `v`.

## 4. Perfiles de dos aros: fórmula cerrada

**Proposición 1.** Sean `σ₁ ≥ σ₂` los radios de `S` (con `r_m = 1`, `ω < 1`).
`S` **no** es reinsertable en `N(1) ⊎ N(1−ω)` si y solo si

    σ₁ + σ₂ > 1   y   σ₂ > 1 − ω.

*Demostración.* Las únicas colocaciones posibles son cuatro. (i) Ambos en `N(1)`:
para dos círculos en un disco de radio `C` la condición exacta es `σ₁ + σ₂ ≤ C` —
la suficiencia es el Lema 0 y la necesidad sale de `σ₁ + σ₂ ≤ |c₁ − c₂| ≤
(1−σ₁) + (1−σ₂)`; excluida por la primera hipótesis. (ii) Uno en cada nido: el que
va a `N(1−ω)` mide `≥ σ₂`, luego exige `σ₂ ≤ 1 − ω`; excluida. (iii) `σ₂` anidado en
`σ₁`: exige `σ₂ ≤ σ₁ − ω ≤ 1 − ω`; excluida. (iv) Ambos en `N(1−ω)`: más fuerte que
(ii); excluida. El recíproco es inmediato: si falla la primera condición vale (i), y
si falla la segunda vale (ii). ∎

**Corolario 1.** Para perfiles de dos aros,

    ρ*₂(ω) = máx(1, 2(1 − ω)),

y el ínfimo se aproxima con `σ₁ = σ₂ → máx(1/2, 1−ω)⁺`. En particular el paso de
intercambio **nunca** se bloquea con dos aros mientras

    w ≤ (1 − ρ/2) · r_m,     y con ρ < T:   w ≤ 0.080357 · r_m ≈ r_m / 12.4.

Esto explica de golpe la aritmética de los dos fallos conocidos. El contraejemplo
`n = 4` tiene `ω = 0.3/5 = 0.06`, luego su `ρ` está obligado a superar
`2(1 − 0.06) = 1.88`, y en efecto vale `1.94`: **por debajo de `ω₀ = 1 − T/2` la
cota combinatoria ya es más exigente que Tribonacci**, y ningún gadget de dos aros
puede vivir bajo `T`. Las gemelas tienen `ω = 0.505/5 = 0.101 > ω₀`, cota `1.798`,
y su `ρ = 1.898` no está forzado por esta cota sino por la geometría.

## 5. Perfiles de k aros en la banda

Si los `k` aros de `S` caen todos en la banda `(1−ω, 1)`, ninguno cabe en `H_m` ni
anida en otro (anidar exige `σ_i ≤ σ_j − ω < 1 − ω`), así que los `k` deben entrar en
`N(1)`. Para que no quepan basta `1 − ω ≥ r_k`, con `r_k` el radio umbral de `k`
círculos iguales en el disco unidad, y entonces `ρ ≥ k(1−ω) ≥ k·r_k`:

| k | r_k | k·r_k |
|---|-----|-------|
| 2 | 1/2 = 0.5 | 1.000 |
| 3 | 2√3 − 3 = 0.4641 | 1.392 |
| 4 | √2 − 1 = 0.4142 | 1.657 |
| 5 | 0.37019 | **1.851 > T** |
| 6 | 1/3 | **2.000 > T** |

**Corolario 2.** Ningún bloqueo con cinco o más aros en banda es compatible con
`ρ < T`. El caso crítico tiene por tanto entre dos y cuatro aros bloqueantes.

## 6. El umbral medido y el grosor crítico

`code/reinserta.py` calcula `ρ*(ω)` por descenso sobre perfiles no reinsertables
(los valores son **cotas superiores del ínfimo**: la búsqueda es heurística, de modo
que el `ρ*` real solo puede ser menor).

| ω | k=2 | k=3 | k=4 | mín |
|---|-----|-----|-----|-----|
| 0.030 | 1.940 | 1.907 | 1.909 | 1.907 |
| 0.040 | 1.920 | 1.873 | 1.869 | 1.869 |
| 0.050 | 1.900 | 1.846 | 1.839 | **1.839 ≈ T** |
| 0.060 | 1.880 | 1.814 | 1.796 | 1.796 |
| 0.080 | 1.840 | 1.749 | 1.751 | 1.749 |
| 0.120 | 1.760 | 1.618 | 1.620 | 1.618 |
| 0.200 | 1.600 | 1.601 | 1.602 | 1.600 |
| 0.450 | 1.100 | 1.101 | 1.103 | 1.100 |

La columna `k=2` reproduce `máx(1, 2(1−ω))` con cuatro decimales, lo que valida la
Proposición 1 contra la búsqueda. Y aparece un hecho que la fórmula del par no
anticipa: **para `ω` pequeño mandan los perfiles de tres y cuatro aros, no los de
dos**. El mínimo cruza `T` entre `ω = 0.04` (donde vale `1.869 > T`) y `ω = 0.05`
(donde vale `1.839`, ya por debajo):

    ω_c ≈ 0.05,   es decir  w ≈ r_m / 20.

Como los valores tabulados son cotas superiores del ínfimo, `ω_c` solo puede ser
menor; lo que queda establecido con certeza es la dirección útil: por debajo de `ω_c`
la búsqueda no encuentra ningún bloqueo con `ρ < T`, y para `k = 2` la Proposición 1
lo garantiza sin margen de error hasta `ω₀ = 0.0804`. La lectura es:

> **El paso de intercambio se cierra por vía puramente combinatoria —Lema 0, densidad
> crítica 1/2, agujero de `m` y anidamiento— en el régimen de grosor fino
> `w ≲ r_m/20`. Por encima de ese grosor la reinserción ya no está garantizada sin
> mirar la geometría de `v`, y el bolsillo de Descartes pasa a ser imprescindible.**

Los dos fallos conocidos viven, como debe ser, en el régimen donde la combinatoria
no cierra: `ω = 0.060` y `ω = 0.101`, ambos por encima de `ω_c`.

**Nota de consolidación.** La estimación `ω_c ≈ 0.05` quedó superada: el cruce
exacto es

    ω_T = 1/T − 1/2 ≈ 0.043689

(Corolario 4 de `drafts/perfil_tres.md`, en forma cerrada). La discrepancia se
explica porque los valores de la columna `k=3` de la tabla anterior para
`ω ≤ 0.08` eran mínimos locales del descenso por coordenadas, ~0.02–0.03 por
encima del ínfimo real: en `ω = 0.05` el valor tabulado `1.846` debe leerse
`2/(1+2ω) = 20/11 ≈ 1.8182`, ya por debajo de `T`. Las columnas con `ω ≥ 0.12`
sí coinciden con la fórmula exacta `ρ*₃(ω)`. La conclusión cualitativa de esta
sección no cambia (por debajo del umbral la combinatoria cierra), pero el umbral
pasa de `≈ 0.05` medido a `ω_c = ω_T` demostrado (`ρ*_k = ρ*₃` para todo `k ≥ 3`, `drafts/cuatro.md`)
(abierto).

## 7. La geometría de v: por qué el bolsillo solo llega a φ

En el régimen crítico hay que colocar `σ₂` en un bolsillo de `v`. Tomemos la
configuración rígida canónica: `v` es la sartén, contiene `m` y un aro `r₁ = α`
(normalizado `r_m = 1`), con `R = α + 1`, de modo que `{α, m}` son tangentes y llenan
la sartén. Retirado `m`, colocamos `σ₁` en `D_m` y `σ₂` debe caber en el bolsillo de
Descartes tangente a `α`, a `σ₁` y a la pared. En el peor caso (`σ₁ = 1`) ese
bolsillo mide

    b(α) = α(α+1) / (α² + α + 1).

Para que el intercambio falle hace falta `σ₂ > b(α)` (si no, el bolsillo lo absorbe),
y como `σ₁ ≥ σ₂`, `ρ ≥ σ₁ + σ₂ > 2b(α)`. Si además `α` es un aro de la instancia, su
propia cola da `ρ ≥ (1 + σ₁ + σ₂)/α > (1 + 2b(α))/α`. Luego `ρ > B(α)`, con

    B(α) = máx( 2b(α),  (1 + 2b(α))/α ).

**Proposición 2.** `mín_{α>0} B(α) = φ`, alcanzado exactamente en `α = φ`.

*Demostración.* La primera rama crece y la segunda decrece, así que el mínimo está
en el cruce `2b(α)(α−1) = 1`, que tras despejar es `2α³ − α² − 3α − 1 = 0`. Este
polinomio factoriza como `(2α + 1)(α² − α − 1)`, cuya única raíz positiva es
`α = φ`. Allí `b(φ) = (1+√5)/4 = φ/2`, luego `B(φ) = φ`. ∎

Es decir: **el bolsillo de Descartes, por sí solo, solo protege hasta `φ ≈ 1.618`,
no hasta `T ≈ 1.839`.** La diferencia `T − φ ≈ 0.221` mide exactamente lo que aporta
la condición completa —que el trío `{α, σ₁, σ₂}` sea infactible en `v`— frente a la
condición débil «`σ₂` no cabe en el bolsillo». El bolsillo se calcula con `σ₁ = 1`;
cuando `σ₁ < 1` el hueco disponible crece, y capturar esa ganancia es justo el paso
que falta para llegar a `T`. Esta es la razón estructural de que la familia de 4 aros
alcance `T` y no `φ`: allí la restricción activa no es el bolsillo sino la
infactibilidad del trío, que es la que produce el álgebra `t³ + t² + t ≤ 1`.

La razón áurea reaparece aquí en un papel nuevo. En `resultados.md` §5bis marcaba el
umbral `A ≤ φB` bajo el cual el bolsillo absorbe a los pequeños; ahora marca
**el punto de mínima protección**: `α ≈ φ` es la ventana donde la cota por bolsillos
es más débil y, por tanto, donde debería aparecer el contraejemplo si la conjetura
fuese falsa.

## 8. Búsqueda dirigida a la ventana

Esa lectura convierte la ventana en un plan de búsqueda concreto, y explica por qué
los barridos previos no probaban nada en la zona que importa: `umbral.py` muestrea
radios y `R` uniformemente, mientras que los fallos conocidos viven en tangencias
exactas —conjunto de medida nula—. `code/banda.py` construye las instancias con la
estructura del bloqueo en lugar de sortearlas: `R = α + 1` (sartén rígida), `σ₁, σ₂`
dentro de la banda `(1−ω, 1)`, pareja alojable en el agujero de `r₁`, `α` barrido
alrededor de `φ` y `ω` en el régimen crítico `ω > ω_c`.

**Resultado: 1450 instancias dirigidas con `ρ < T`, cero fallos.** El control
positivo del mismo script es lo que da valor al cero: alimentado con los tres fallos
conocidos —normalizados a `r_m = 1`, es decir `α = 2`, `R = 3`— reproduce el
comportamiento publicado aro por aro y regla por regla: en el contraejemplo `n = 4`
(`ω = 0.06`, `ρ = 1.940`) falla *best fit*; en la gemela `I1` (`ω = 0.101`,
`ρ = 1.898`) falla *best fit*; y en `I2` (`ρ = 1.900`) falla *worst fit*, la
inversión que sostiene el teorema de imposibilidad para reglas de estado. El
detector funciona, y aun así no encuentra nada por debajo de `T` en la ventana donde
la combinatoria ya no protege.

Esto es evidencia, no demostración, pero es evidencia de un tipo distinto al previo:
antes el cero salía de un muestreo que casi con seguridad nunca visitó la región
crítica; ahora sale de barrer justo la ventana que el análisis señala como la más
débil.

## 9. De φ a T: los tres ingredientes exactos

El paso previsto era sustituir «`σ₂` cabe en el bolsillo» por la condición completa
«el trío `{α, σ₁, σ₂}` empaqueta en `v`». `code/trio.py` lo hace con el criterio
angular exacto, y el resultado enseña algo que la predicción no decía: **la condición
del trío tampoco basta**. El ínfimo sin más restricciones es

    ρ = 1 + b(α*) = 1.7990559…   en   α* = raíz de 2α³ = α² + 2α + 2 ≈ 1.5558471

(la cúbica es el cruce `1 + b(α) = (2 + b(α))/α`, donde ambas ramas valen también
`1/(α* − 1)`; verificada en simbólico. *Cifra corregida en la consolidación: una
versión anterior daba `≈ 1.79966`, el valor de la malla numérica; el cruce
exacto, recalculado en sympy, es `1.7990559`, que difiere ya en la cuarta cifra
decimal*), todavía
por debajo de `T`. Pero en ese óptimo `σ₁ + σ₂ ≈ 1.80 > α ≈ 1.556`: **S no cabría en
`u`**, y el testigo colocó `S` precisamente en `u`. La colocación del testigo es una
restricción activa que el análisis de bolsillos nunca usó: `Σ S ≤ cap(u)`, y en la
plantilla canónica `u` es el agujero de `α`, de capacidad `α − w → α`.

Con esa restricción el problema cambia de naturaleza. En la frontera de bloqueo
(`σ₁ → 1`, `σ₂ → b(α)`) la condición «S cabe en u» es `1 + b(α) ≤ α`, y

    b(α) − (α − 1) = −(α³ − α² − α − 1) / (α² + α + 1),

luego para `α < T` todo bloqueo exige `Σ S > cap(u)` —irrealizable por ningún
testigo— y para `α ≥ T` el ínfimo es `ρ = 1 + b(α)`, creciente, con mínimo en

    α = T:   b(T) = T − 1   (identidad exacta módulo T³ = T² + T + 1),   ρ = T.

**Proposición 3 (plantilla canónica).** En la configuración rígida `R = α + 1` con
`w → 0`, el ínfimo de `ρ` sobre los bloqueos del paso de intercambio realizables por
un testigo es exactamente `T`, alcanzado en `α = T`, `σ₁ → 1`, `σ₂ → T − 1`.

La medición numérica lo reproduce: `ρ* = 1.83999` en `α* = 1.83999` (la diferencia
`7·10⁻⁴` con `T` es la malla `σ₁ ≤ 0.999999`). La escalera queda así:

| recursos usados | ínfimo de ρ |
|---|---|
| bolsillo de Descartes solo | `φ ≈ 1.6180` |
| + infactibilidad del trío completo | `= 1.7990559…` (raíz de `2α³ = α²+2α+2`) |
| + colocación del testigo (`S` cabe en `u`) | **`T ≈ 1.8393`** |

Y la moraleja estructural: el álgebra `t³ + t² + t ≤ 1` del suelo de la familia no
es un accidente de la familia de 4 aros — es exactamente lo que producen los tres
ingredientes del intercambio en la plantilla canónica. El lema universal de
reinserción necesita los tres; con dos de ellos el umbral demostrable se queda en
`φ` o en `1.7991`.

## 10. Qué queda por demostrar

1. **Contenedores `v` genéricos. — SIGUE ABIERTO; es EL hueco principal de la
   conjetura.** *Avance parcial (`drafts/universal.md`):* el toolkit geométrico ya
   es uniforme en R — frontera lineal del trío para disco arbitrario (Lema U, con
   su hipótesis A ≥ mín(x,y)), bolsillo general b_R(A) creciente en R, Teorema S
   con holgura (Corolario U1), cota de existencia R < 2.1547·A — y las dos
   batallas restantes (ocupantes interiores; u = sartén) están formuladas con
   exploración numérica a favor. *Avance segundo (`drafts/corona.md`):* el
   criterio de coronas de k círculos tangentes a pared es un LP exacto por orden
   con certificados de subconjunto necesarios (todo k), y para k = 4 la
   caracterización es cerrada y demostrada — **Lema U₄**: corona ⟺ trío top +
   total del orden zigzag ≤ 2π (el orden decreciente NO es óptimo; la suma de
   arcos consecutivos NO basta) — con lo que el bloqueo de corona con dos
   ocupantes queda reducido a dos ramas algebraicas exactas. *Avance tercero
   (`drafts/ocupantes.md`):* en la plantilla de agujeros libres los bloqueos
   con ocupantes extra están **resueltos sin geometría** — el agujero de cada
   ocupante es un recurso de reinserción, bloquearlo lo confina a
   o_k ≤ 1 + ω, y la cola del mayor da ρ > (j+2)/(1+ω) > T (para
   ω < 2/T − 1/2 = 0.5874 con j = 1; para todo ω con j ≥ 2): cada ocupante
   paga su cola y la plantilla canónica es estrictamente óptima para el
   adversario. *Avance cuarto (`drafts/bloqueadores.md`):* con los agujeros de
   los ocupantes OCUPADOS a cualquier profundidad, el Lema R (bloquear un
   agujero cuesta masa ≥ la holgura) y el nodo mínimo dan ρ > Ψ(ω) =
   (1−ω)+√((1−ω)²+1) > T para ω < (T−1)²/2 = 0.3522, y el Teorema B″ elimina
   también «m con hijos» (rama B = media metálica Ψ_B ≥ Ψ, dominada): la
   plantilla ya no tiene ninguna hipótesis de ocupación. *Avance quinto
   (`drafts/bolsillo.md`):* la pared del bolsillo doble (σ₁ > b₂(α,o₁), por
   rigidez S5 reescalada) cierra el tramo geométrico: con un ocupante extra,
   ρ > φ² − (φ/2)ω > T para todo ω < ω_A = 0.9626 (Teorema G′; rincón dorado α = 2,
   o₁ = √5−1), más la escalera Ψ_j para j ocupantes y los pequeños gratis
   para la combinatoria. Quedan las puntitas de ω extremo, el lema del hueco
   (pequeños frente a la pared geométrica) y S con más de dos piezas. El análisis anterior supone `v` rígido con un solo
   vecino grande. Con varios ocupantes el bolsillo relevante es el mayor hueco del
   empaquetamiento, y hace falta una cota inferior universal en función de la
   capacidad libre. Igualmente, `u` genérico: si `u` es la sartén, la restricción del
   testigo no es una capacidad simple sino la empaquetabilidad de `S` junto a los
   ocupantes mayores de `u`, y hay que comprobar que la misma álgebra sobrevive.
   Tras la consolidación, ni el Teorema S de `drafts/suelo_rigido.md` (que exige
   `R = r₁ + r₂` exacto) ni la plantilla canónica con grosor lo cubren: todo lo
   demás del programa está cerrado o acotado, y la conjetura del umbral de
   Tribonacci se reduce exactamente a este punto.
2. **Grosor positivo. — RESUELTO en `drafts/grosor_positivo.md` (H1 demostrado en `drafts/h1.md`).**
   La Proposición 3 está en el límite `w → 0`; con `w > 0` la
   capacidad de `u` baja a `α − w` y el agujero `H_m` sube a `1 − ω`, dos efectos de
   signo contrario. El borrador los controla: la rama del testigo se gobierna por
   el Tribonacci deformado `Φ(ω) = T₍₁₊ω₎ − ω` (creciente, exacta) y la rama `H_m`
   por `2(1−ω)`, con cota uniforme `T_can(ω) ≥ T + 0.0098` para todo
   `ω ∈ (0, 0.30]`: «el grosor solo lo sube», como afirma `resultados.md`
   §5quater, con holgura uniforme (curva no monótona, mínimo medido en la esquina
   racional `(1/7, 2, 6/7, 13/7)`). Verificación 8/8 en el acta.
3. **Perfiles de tres y cuatro aros. — RESUELTO para `k = 3` en
   `drafts/perfil_tres.md`.** La fórmula cerrada análoga a la Proposición 1 es
   `ρ*₃(ω) = máx(1, mín(2(1−ω), máx(φ, 2/(1+2ω))))` (Proposición 4 y Corolario 3,
   demostrados por vía puramente aditiva), con cruce exacto `ω_T = 1/T − 1/2` con
   Tribonacci (Corolario 4; véase la nota de §6). La curva conjeturada `c·(1−ω)`
   era falsa: el tramo dominante es la hipérbola `2/(1+2ω)` y hay una meseta en
   `φ`. **`k` general RESUELTO en `drafts/cuatro.md`**: `ρ*_k = ρ*₃` para todo
   `k ≥ 3` (Proposición 8) y `ω_c = ω_T` exacto (Corolario 5; el Corolario 2
   solo cubría perfiles en banda y no bastaba). Queda el análogo de la
   Proposición 3 con tres bloqueantes en
   banda.

## Mapa de verificación

- `code/reinserta.py` — recursos del intercambio, `ρ*(ω)` por tamaño de perfil,
  fórmula del par contra búsqueda, cota de banda `k·r_k`, localización de `ω_c`, y
  comprobación de que los perfiles `S` de los dos fallos conocidos no son
  reinsertables. Incluye el criterio angular para tres círculos, validado contra los
  tres valores publicados en `resultados.md` (369.2°, 364.4°, 352.5°).
- `code/banda.py` — búsqueda dirigida de fallos con `ρ < T` en la ventana crítica,
  con control positivo sobre las instancias conocidas.
- `code/trio.py` — la escalera φ → 1.7991 → T: ínfimo de ρ con la condición completa
  del trío, sin y con la restricción del testigo; identidades `2α³ = α²+2α+2` y
  `b(T) = T−1` verificadas en simbólico (sympy) y por barrido numérico.
