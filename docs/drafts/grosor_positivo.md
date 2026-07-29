# Grosor positivo en la plantilla canónica: la Proposición 3 con ω > 0

Borrador de trabajo sobre el punto 2 de `reinsercion.md` §10. La Proposición 3
establece que el ínfimo de ρ sobre los bloqueos del paso de intercambio en la
plantilla canónica es la constante de Tribonacci T, **en el límite w → 0**. Aquí
se extiende a grosor positivo ω = w/r_m > 0. Resultado principal: el ínfimo con
grosor queda acotado por debajo por una función explícita que **nunca baja de
T + 0.0098**, lo que confirma —con holgura uniforme, no solo en el margen— la
afirmación de `resultados.md` §5quater de que «el grosor solo lo sube». El
mecanismo tiene sorpresas: la curva del ínfimo **no es monótona en ω** (decrece
en (0, 1/7] y crece después), su mínimo global medido es la esquina racional
exacta ω = 1/7, α = 2, ρ = 13/7, y el suelo demostrado es una constante cúbica
nueva, 2(α_× − 1) con α_× la raíz de 2α³ = 2α² + 2α + 3.

Verificación: `code/grosor.py` (álgebra exacta en sympy + barrido de la frontera
de bloqueo por bisección con el método de `trio.py`).

## 1. El programa de bloqueo con grosor

Plantilla canónica normalizada a r_m = 1: `v` es la sartén de radio R = α + 1
ocupada por α y m tangentes; `u` es el agujero de α, de capacidad α − ω; el
testigo colocó S = {σ₁, σ₂} en `u` (σ₂ ≤ σ₁ < 1). El intercambio manda m a `u`
y debe reinsertar S. Con ω > 0 los recursos de reinserción son **cuatro**, no
dos:

- **D_m**: colocación en `v`. Falla solo si el trío {α, σ₁, σ₂} es infactible
  en el disco α + 1.
- **H_m**: el agujero de m, capacidad 1 − ω, que viaja con m.
- **`u` junto a m**: σ₂ puede volver a `u` como hermano de m; para el par
  {1, σ₂} en el disco α − ω la condición exacta es 1 + σ₂ ≤ α − ω. Este recurso
  no aparece en el análisis w → 0 y sin embargo es el que el contraejemplo n = 4
  bloquea con «agujero del 10 con el 5: 9.8 > 9.7» (`resultados.md` §5ter).
- **Anidamiento** de σ₂ en σ₁, capacidad σ₁ − ω.

Un bloqueo genuino y realizable por un testigo exige por tanto (clausuras para
los ínfimos):

    (B1)  trío {α, σ₁, σ₂} infactible en R = α + 1
    (B2)  σ₂ ≥ 1 − ω              (si no, H_m absorbe a σ₂)
    (B3)  σ₂ ≥ σ₁ − ω             (implicada por (B2), pues σ₁ ≤ 1)
    (B4)  σ₂ ≥ α − ω − 1          (si no, σ₂ entra en u junto a m)
    (W)   σ₁ + σ₂ ≤ α − ω         (S cabía en u; exacto para dos círculos)

más las condiciones de plantilla 1 ≤ α − ω y σ₂ ≤ σ₁ ≤ 1. Las presiones sobre
ρ son las de siempre: la cola de m da ρ ≥ σ₁ + σ₂ y la cola de α da
ρ ≥ (1 + σ₁ + σ₂)/α. Definimos

    T_can(ω) := inf max(σ₁ + σ₂, (1 + σ₁ + σ₂)/α)  sobre los bloqueos (B1)–(W).

**Observación previa que reencuadra la Proposición 3.** En ω = 0 el programa
completo es **vacío**: (B2) exigiría σ₂ ≥ 1 > σ₁, y en efecto con w = 0 todo aro
menor anida en cualquiera mayor y el intercambio nunca se bloquea. El valor T de
la Proposición 3 es el ínfimo del programa **relajado** que usa solo (B1) + (W)
—exactamente los tres ingredientes de la escalera de §9—, y ese relajado es una
cota inferior válida del completo para todo ω. La extensión correcta a ω > 0
consiste en (i) calcular el relajado con capacidad α − ω, y (ii) medir cuánto
añaden (B2) y (B4).

## 2. La rama del testigo: Tribonacci deformado

**Lema 1.** Para α, ω > 0:  b(α) ≥ α − 1 − ω  ⟺  α³ ≤ (1 + ω)(α² + α + 1),
donde b(α) = α(α+1)/(α²+α+1) es el bolsillo de Descartes. *Demostración:*
identidad polinómica, b(α) − (α − 1 − ω) = −[α³ − (1+ω)(α²+α+1)]/(α²+α+1),
verificada en simbólico. ∎

Sea T_c la única raíz positiva de α³ = c(α² + α + 1) (única por la regla de los
signos de Descartes); T₁ = T es Tribonacci.

**Proposición 4 (rama del testigo).** El ínfimo de ρ sobre el programa relajado
(B1) + (W) con capacidad α − ω es

    Φ(ω) = T₍₁₊ω₎ − ω ,

alcanzado en el límite α = T₍₁₊ω₎, σ₁ → 1, σ₂ → b(α) = α − 1 − ω.

*Demostración (con el hueco H1 señalado).* Para α fijo, el mínimo de σ₁ + σ₂
sobre los tríos infactibles con σ₂ ≤ σ₁ ≤ 1 es 1 + b(α), alcanzado en σ₁ → 1,
σ₂ → b(α) **[hueco H1: este paso es el mismo de la Proposición 3; equivale a que
sobre la frontera de infactibilidad h(α, σ₁) del trío la pendiente cumple
κ = −∂h/∂σ₁ ≥ 1; verificado en malla con κ_min ≈ 1.02, sin prueba analítica]**.
Entonces todo bloqueo relajado en α cumple, por (W),

    1 + b(α) ≤ σ₁ + σ₂ ≤ α − ω ,

que por el Lema 1 equivale a α ≥ T₍₁₊ω₎. Como ρ ≥ σ₁ + σ₂ ≥ 1 + b(α) y b es
estrictamente creciente (b′ = (2α+1)/(α²+α+1)² > 0), el ínfimo sobre los α
admisibles se toma en α = T₍₁₊ω₎ y vale 1 + b(T₍₁₊ω₎) = T₍₁₊ω₎ − ω por el
Lema 1 con igualdad. La familia σ₁ = 1 − ε, σ₂ = b(α) + ε′ lo aproxima. ∎

En ω = 0 esto es exactamente la Proposición 3. Los dos efectos del grosor están
ya separados: la capacidad α − ω del testigo **deforma la cúbica de Tribonacci**
α³ = (1+ω)(α²+α+1), y H_m entra solo por (B2), que la Proposición 4 aún no usa.

**Proposición 5 (monotonía exacta de la rama del testigo).** Φ es estrictamente
creciente y cóncava, con derivada en forma cerrada

    Φ′(ω) = (2α + 1) / (α² (α² + 2α + 3)) > 0 ,   α = T₍₁₊ω₎ ,

y pendiente inicial c := Φ′(0) = (2T + 1)/(7T² + 4T + 3) ≈ 0.1374516. En
particular, para ω ∈ [0, 1/7],

    T + (13 − 7T)·ω  ≤  Φ(ω)  ≤  T + c·ω ,      13 − 7T ≈ 0.1249927 .

*Demostración.* Derivación implícita de la cúbica y sustitución de
1 + ω = α³/(α²+α+1): el numerador de Φ′ = dα/dω − 1 se reduce al polinomio
2α + 1 (identidad verificada en simbólico). Concavidad: log Φ′ tiene derivada
en α igual a 2/(2α+1) − 2/α − (2α+2)/(α²+2α+3) < 0 (el primer término es menor
que 2/α), y α es creciente en ω. La cota superior es la tangente en 0; la
inferior es la cuerda entre ω = 0 y ω = 1/7, cuyo extremo derecho es **exacto**:
T₍₈⁄₇₎ = 2 (porque 2³ = 8 = (8/7)·7) y Φ(1/7) = 2 − 1/7 = 13/7. ∎

Esto ya demuestra (módulo H1) la mitad de la afirmación de §5quater: **la rama
del testigo solo puede subir con el grosor**, a razón de ≈ 0.125–0.137 por
unidad de ω, con la constante c en forma cerrada sobre la cúbica de Tribonacci.

## 3. La rama H_m y el suelo uniforme

**Proposición 6 (rama H_m).** Todo bloqueo del programa completo cumple
ρ ≥ σ₁ + σ₂ ≥ 2(1 − ω). *Demostración:* (B2) y σ₁ ≥ σ₂. ∎ (Es la misma cota
del par de la Proposición 1 de `reinsercion.md` §4, ρ*₂(ω) = 2(1−ω),
reapareciendo dentro de la plantilla: con grosor, los dos bloqueantes viven en
la banda (1−ω, 1).)

Las dos ramas tienen signos opuestos: Φ crece con ω, 2(1−ω) decrece. El máximo
de ambas se minimiza en su cruce Φ(ω) = 2(1−ω), es decir T₍₁₊ω₎ = 2 − ω, que al
sustituir en la cúbica da

    2ω³ − 10ω² + 14ω − 1 = 0   ⟺   α = 2 − ω raíz de 2α³ = 2α² + 2α + 3 ,

con raíz relevante ω_× ≈ 0.0754315 (α_× ≈ 1.9245685).

**Teorema (grosor positivo, plantilla canónica; módulo H1).** Para todo
ω ∈ (0, 0.30],

    T_can(ω) ≥ max( 2(1 − ω), Φ(ω) ) ≥ 2(1 − ω_×) = 2(α_× − 1) ≈ 1.8491370
             = T + 0.0098503 .

*Demostración.* La primera desigualdad junta las Proposiciones 4 (el relajado
acota al completo) y 6. La segunda: máximo de una función decreciente y una
creciente, minimizado en el cruce. ∎

Es decir: **el ínfimo con grosor no solo nunca baja de T: nunca baja de
T + 0.0098**. El límite w → 0 de la Proposición 3 es genuinamente un límite: el
valor T no se alcanza ni se aproxima con grosor positivo, porque los bloqueos
que lo aproximan tienen σ₂ = b(T) = T − 1 ≈ 0.839, que H_m absorbe en cuanto
1 − ω > T − 1, o sea para todo ω < 2 − T ≈ 0.161 (y para ω ≥ 1/7 la rama del
testigo ya está en Φ(ω) ≥ 13/7 > T).

## 4. La curva verdadera: tres regímenes y la esquina racional

El barrido numérico (`grosor.py`, sección [D]: frontera del trío por bisección
sobre el criterio angular exacto, con (B2), (B4) y (W) impuestas, y refinado en
α) muestra una estructura más fina que la del Teorema, con una rama intermedia
que las dos cotas no capturan:

| régimen | T_can(ω) medido | configuración óptima |
|---|---|---|
| 0 < ω ≤ ω₁ | 2(1 − ω) | σ₁ = σ₂ = 1 − ω, α = 2 − ω ((B2) y (W) activas) |
| ω₁ ≤ ω ≤ 1/7 | α_m(ω) − ω | σ₂ = 1 − ω, σ₁ = α_m − 1, con α_m la solución de h(α, α−1) = 1 − ω ((B1), (B2) y (W) activas) |
| ω ≥ 1/7 | Φ(ω) = T₍₁₊ω₎ − ω | σ₁ → 1, σ₂ = b(α) = α − ω − 1 ((B1), (B4) y (W) activas) |

donde h(α, σ₁) es la frontera de infactibilidad del trío y

    ω₁ ≈ 0.041357   es la raíz de   h(2 − ω, 1 − ω) = 1 − ω ,

el grosor en que el trío de reparto igual {2−ω, 1−ω, 1−ω} toca la frontera
(verificado: infactible en ω = 0.0414, factible en ω = 0.045). **La rama H_m
muere en ω₁, no en ω_×**: como la pendiente de la frontera es κ > 1, al moverse
sobre σ₁ + σ₂ = const desde (1, s−1) hacia el reparto igual la frontera sube más
deprisa que σ₂, y el reparto igual cae del lado factible en cuanto ω > ω₁. Entre
ω₁ y ω_× ninguna de las dos cotas del Teorema se alcanza (holgura máxima ≈ 0.06
en ω_×). Valores medidos (desviación frente a la rama predicha ≤ 4·10⁻⁴, la
malla; la rama mixta se resuelve con bisección independiente en `alpha_mixta`):

| ω | T_can medido | rama | predicción |
|---|---|---|---|
| 0.02 | 1.960000 | H_m | 2(1−ω) = 1.960000 |
| 0.04 | 1.920000 | H_m | 1.920000 |
| ω₁ = 0.041357 | 1.917303 | juntura | 2(1−ω₁) = 1.917286 |
| 0.06 | 1.915080 | mixta | 1.915073 |
| ω_× = 0.075431 | 1.909131 | mixta | 1.909120 |
| 0.09 | 1.901024 | mixta | 1.901000 |
| 0.11 | 1.886743 | mixta | 1.886734 |
| 0.125 | 1.874100 | mixta | 1.874074 |
| 1/7 | 1.857543 | esquina | 13/7 = 1.857143 |
| 0.16 | 1.859400 | testigo | Φ = 1.859070 |
| 0.20 | 1.863800 | testigo | 1.863408 |
| 0.25 | 1.868800 | testigo | 1.868538 |

La curva decrece en todo (0, 1/7] —primero como 2(1−ω), luego suavemente como
α_m(ω) − ω, con α_m creciendo de 2 − ω₁ hacia 2— y crece en [1/7, ∞) como Φ.

**La esquina ω = 1/7 es una tangencia cuádruple racional.** En α = 2, ω = 1/7,
σ₁ → 1, σ₂ = 6/7 se saturan a la vez las cuatro paredes del programa:

    (B1)  σ₂ = b(2) = 6/7        (frontera del trío: el bolsillo de Descartes)
    (B2)  σ₂ = 1 − ω = 6/7       (el agujero de m)
    (B4)  σ₂ = α − ω − 1 = 6/7   (el agujero de α junto a m)
    (W)   σ₁ + σ₂ = 13/7 = α − ω (la capacidad del testigo)

y el valor es ρ = 13/7 ≈ 1.8571 = T + 0.01786. **Conjetura:** el ínfimo global
de T_can sobre ω > 0 es exactamente 13/7, alcanzado en esta esquina. (Medido:
mínimo 1.85754 en ω = 1/7 con las mallas usadas; las identidades T₍₈⁄₇₎ = 2 y
b(2) = 6/7 = 1 − 1/7 son exactas.)

Notas de coherencia, todas verificadas en `grosor.py`:

- **(B4) no mueve el ínfimo pero lo esculpe.** En la rama del testigo el óptimo
  tiene σ₂ = b(α) = α − ω − 1: (B4) se satura exactamente (con κ > 1, subir σ₂
  por encima del umbral de (B4) y bajar σ₁ solo empeora). En las ramas H_m y
  mixta, (B4) equivale a α ≤ 2, compatible con la ventana α ≥ 2 − ω de (W); por
  eso α_m → 2 al acercarse a la esquina. Las «tangencias exactas por doquier» de
  los contraejemplos de §5ter/§5quater son exactamente esta saturación
  simultánea.
- **Los fallos conocidos respetan la cota.** Contraejemplo n = 4 normalizado
  (α = 2, ω = 0.06, σ = {0.98, 0.96}): bloqueo genuino, ρ = 1.94 ≥ 1.88 =
  2(1−ω), y T_can(0.06) ≈ 1.9151. Gemela I1 (α = 2, ω = 0.101,
  σ = {0.998, 0.90}): bloqueo genuino con holguras 0.001 en (B2), 0.001 en (B4)
  y 0.001 en (W) —vive pegada a las tres paredes del programa, como predice el
  análisis— y ρ = 1.898 ≥ Φ(0.101) ≈ 1.8523; el óptimo canónico en su grosor es
  T_can(0.101) = α_m(0.101) − 0.101 ≈ 1.8936 (rama mixta), de modo que las
  gemelas están a 0.004 del ínfimo de su plantilla.

## 5. Lectura

1. **«El grosor solo lo sube» es cierto, con holgura uniforme.** Respecto del
   valor límite T de la Proposición 3, todo ω > 0 sube el ínfimo al menos hasta
   2(α_× − 1) ≈ T + 0.0098 (demostrado módulo H1), y según la curva medida hasta
   13/7 = T + 0.0179 (conjetura de la esquina). En la conjetura del umbral de
   Tribonacci el caso crítico es por tanto el límite de grosor fino: cualquier
   prueba que cierre w → 0 cierra automáticamente w > 0 **en la plantilla
   canónica**.
2. **Pero la curva no es monótona.** T_can(ω) decrece desde 2⁻ (en ω → 0⁺)
   hasta la esquina ω = 1/7 y crece después: el grosor debilita H_m (capacidad
   1 − ω) más deprisa de lo que estrecha al testigo (capacidad α − ω) hasta la
   esquina, y a partir de ahí manda la deformación de la cúbica. La monotonía
   genuina es la de la rama del testigo (Proposición 5, exacta), que es la que
   responde a la pregunta de §10 punto 2: de los dos efectos de signo contrario,
   **gana siempre el del testigo en el ínfimo global** (nunca se baja de T),
   pero el efecto H_m domina la forma de la curva en ω < 1/7.
3. **Constantes nuevas.** La deformación de Tribonacci T₍₁₊ω₎ con
   α³ = (1+ω)(α²+α+1); el suelo demostrado 2(α_× − 1) con 2α_×³ = 2α_×² +
   2α_× + 3; la juntura ω₁ (raíz de h(2−ω, 1−ω) = 1−ω, sin forma cerrada); y la
   esquina racional (ω, α, σ₂, ρ) = (1/7, 2, 6/7, 13/7). La pendiente inicial
   c = (2T+1)/(7T²+4T+3) vive en el cuerpo de T.
4. **Conexión con ω_c de `reinsercion.md` §6.** El umbral combinatorio
   ω_c ≈ 0.05 (donde ρ*(ω) cruza T para perfiles generales) y las junturas
   ω₁, ω_× de la plantilla no son el mismo objeto: ρ*(ω) ignora la geometría de
   v (y por eso baja de T), mientras que T_can(ω) la incluye vía (B1) y no baja
   nunca de T + 0.0098. La comparación cuantifica lo que la geometría del trío
   añade sobre la contabilidad de nidos también con grosor.

## 6. Huecos y alcance

- **H1 (heredado de la Proposición 3).** Que el mínimo de σ₁ + σ₂ sobre los
  tríos infactibles se alcanza en σ₁ → 1 (equivalentemente κ = −∂h/∂σ₁ ≥ 1 en
  la frontera). Verificado en malla (κ_min ≈ 1.02 sobre α ∈ [1.6, 2.4],
  σ₁ ∈ [0.6, 1)); sin prueba analítica. Todo lo etiquetado «demostrado» que
  dependa de la Proposición 4 es módulo H1; la Proposición 6 y la cota
  ρ ≥ 2(1−ω) no dependen de H1.
- **H2.** La estructura de tres regímenes de la sección 4 (igualdad por tramos,
  el valor de ω₁ y la conjetura 13/7 de la esquina) es evidencia numérica: las
  familias óptimas están exhibidas y medidas, pero la rama mixta α_m(ω) no
  tiene forma cerrada (es la frontera del criterio angular) y su optimalidad no
  está demostrada. Lo demostrado (módulo H1) es la cota inferior del Teorema.
- **H3 (alcance).** Todo esto es la plantilla canónica: v rígido con un solo
  vecino grande α, S un par, u el agujero de α. Los puntos 1 y 3 de
  `reinsercion.md` §10 (contenedores genéricos, tres bloqueantes) siguen
  abiertos; este documento cierra el punto 2 en el mismo régimen en que la
  Proposición 3 cerraba el caso w → 0.

## Mapa de verificación

`code/grosor.py`, cuatro secciones: **[A]** álgebra exacta en sympy (Lema 1,
fórmula de Φ′, reducción de c módulo la cúbica de T, cúbica del cruce, esquina
1/7, cotas de cuerda y tangente, concavidad); **[B]** hueco H1 en malla
(κ_min, monotonía de σ₁ + h, y frontera h(α, 1⁻) = b(α) contra Descartes; la
comparación en σ₁ → 1 tiene condicionamiento ~10⁻⁴ por la tangencia diametral);
**[C]** 60 000 muestras aleatorias filtradas a bloqueos realizables, todas con
ρ ≥ max(2(1−ω), Φ(ω)); **[D]** ω₁ por bisección, curva medida contra las tres
ramas (desviación ≤ 4·10⁻⁴) y los dos fallos conocidos contra sus cotas y
holguras.
