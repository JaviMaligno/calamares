# Generalizaciones del problema de los calamares

Registro de las generalizaciones y su estado. La v2 integrada del
2026-09-15 reúne las extensiones de forma y dimensión, las gemelas
cuadradas, la cota Y, el umbral global tau=phi en el disco para todo
inventario finito con agujeros independientes, la extensión hasta cinco
aros en toda dimensión d≥2 y la garantía exacta de área variable.
Véanse el [PDF unificado](../output/pdf/calamares_v2_integrada.pdf) y la
[validación editorial y técnica](reviews/2026-09-15-v2-integrada-validation.md).
La referencia del día 14 y los borradores se conservan como historial;
las restantes líneas mantienen el estado indicado abajo.

## 1. Forma del contenedor y dimensión (PARCIALMENTE RESUELTA)

Los teoremas de selección y de irrelevancia bajo superincrecencia valen
para **contenedor arbitrario en cualquier dimensión**. La v2 extiende
también el resultado positivo de hasta tres piezas a esa generalidad.
La reducción dimensional hereda la transición 3/4, las gemelas y el
suelo rígido Tribonacci para bolas de toda dimensión d≥2. En cuadrados
se prueban la transición, gemelas y una cota superior Y; el umbral
cuadrado exacto sigue abierto.

**Plan inicial (anotado el 2026-09-14, tras el envío a arXiv).** Esta es la
línea que se retoma primero. El programa concreto, en orden: (1) la constante
análoga a Tribonacci para contenedor cuadrado, donde el bolsillo de Descartes
se sustituye por los huecos de esquina; (2) el afilado n = 4 en R³, donde la
bola vacante deja más grados de libertad y la transición podría moverse; (3) si
las gemelas sobreviven fuera del disco. Lo positivo ya está cerrado y no
necesita trabajo: lo que se generaliza es el **filo**, que hoy solo está medido
en la sartén.

**Avance del 2026-09-14 — integrado en la v2 y revisado por Fable.** La nota
[`drafts/generalizacion_dimensional.md`](drafts/generalizacion_dimensional.md)
revisa ese plan: (a) el resultado positivo para `n ≤ 3` solo necesita que
reducir una bola conserve factibilidad, así que se extiende a cualquier
contenedor y dimensión; (b) todo empaquetamiento de tres bolas en una bola
se reduce a un plano trasladando la envolvente afín de sus centros hacia
el origen. Por ello, en contenedores esféricos y para todo `d ≥ 2`, se
heredan el fallo a cuatro piezas, las gemelas, el suelo rígido Tribonacci
y la cota superior áurea. No se deduce el valor del umbral global en
dimensión superior. Estos resultados se integraron en la **v2**.

El **cuadrado** queda como primera línea de investigación sustancial:
`drafts/cuadrado.md` ya tiene una constante algebraica `X≈1.7110185903`
para el análisis rígido. **Primer objetivo cerrado el 2026-09-14:**
[`drafts/cuadrado_certificado.md`](drafts/cuadrado_certificado.md) prueba
el fallo de best fit con `ρ=337/200=1.685 < X` mediante confinamiento
por cuadrantes, con exclusión cartesiana universal del trío verificada
en Lean y testigo explícito de cuatro aros. Así,
`1 ≤ tau_cuadrado ≤ 337/200`, y se obtiene el fallo a cuatro piezas en
cuadrado. **Continuación del mismo día:**
[`drafts/cuadrado_gemelas.md`](drafts/cuadrado_gemelas.md) demuestra
gemelas en cuadrado y mejora la cota a `tau_cuadrado ≤ 1.68449`.
El Lema Q ya está formalizado para parámetros generales; las tres
exclusiones y el testigo nuevo están en `SquareTwins.lean`. No se afirma
que la cota sea óptima ni que se haya cerrado la interpretación geométrica
completa de `X`. El lema de fila diagonal ya incluye `r1 ≤ s/2`.
La revisión estática de Fable confirmó D, el Lema Q y G1, con una
corrección menor de redacción ya atendida; informe en
[`reviews/2026-09-14-fable-square-review.md`](reviews/2026-09-14-fable-square-review.md).
**Avance posterior:** [`drafts/cuadrado_limite.md`](drafts/cuadrado_limite.md)
construye una familia aproximante y prueba por continuidad la cota
`tau_cuadrado ≤ Y≈1.684487745872346`. Tres ejemplos racionales pasan 39
paredes exactas y tres identidades nuevas se comprueban en Lean. La
continuidad y la familia completa permanecen como prueba escrita. Fable
acepta el límite y pide una aclaración menor en las gemelas, ya atendida:
[`reviews/2026-09-14-fable-v2-response.md`](reviews/2026-09-14-fable-v2-response.md).
La optimalidad, tanto de la familia como global, sigue abierta.

**Umbral con cuatro aros:** la nueva reducción del bosque demuestra
`tau_(4,d)=phi`, ínfimo no alcanzado, para todo d≥2. Las dos identidades
y la implicación ordenada están verificadas en `FourRing.lean`. Esto
no demuestra `tau_d=phi` para inventarios arbitrarios. Prueba y residuos
en [`drafts/umbral_v2_auditoria.md`](drafts/umbral_v2_auditoria.md).

**Continuación fuera de la v2, 2026-09-15:**
[`drafts/cinco_aros.md`](drafts/cinco_aros.md) presenta una prueba completa
de `tau_(≤5,d)=phi` para todo d≥2, incluso con agujeros independientes.
Usa dos bolsillos simultáneos y distingue el desacuerdo en el segundo
y en el tercer aro. Once certificados Lean verifican las coordenadas,
sus signos y las presiones áureas. Fable acepta la cota inferior y
pide dos precisiones menores en la cota superior, ya incorporadas:
[`respuesta`](reviews/2026-09-15-fable-extras-response.md).
La clasificación de bosques sigue por escrito. Una
[`continuación local`](drafts/particion_bolsillos.md) alinea el segundo
y tercer aro con cualquier cola finita y
reduce seis al desacuerdo en el cuarto con tres mayores en raíz.
Añade tres certificados Lean; Fable revisó después sus criterios C1/C2
como dependencias del cierre global siguiente.

**Cierre uniforme, 2026-09-15: tau=phi en el disco.**
[tres_mayores.md](drafts/tres_mayores.md) demuestra T3: bajo las cotas
áureas, caben todos los discos de una lista finita si y solo si caben
sus tres mayores. Sus dos construcciones cubren cualquier longitud de
cola. Aplicado a los hijos mayores de un contenedor junto con dos plazas
auxiliares m,m, cierra el intercambio en cualquier ramificación.
Las cadenas se resuelven con C1. Así, todo voraz descendente obtiene
el lex-máximo cuando rho≤phi; la familia superior de v2 da tau=phi
con ínfimo no alcanzado, incluso permitiendo agujeros independientes.

Fable [acepta la prueba completa](reviews/2026-09-15-fable-three-core-final-review.md)
y las dependencias de presión, partición y prefijo máximo. Las
[aclaraciones están incorporadas](reviews/2026-09-15-fable-three-core-final-response.md).
Siete certificados nuevos en Lean y controles de posiciones respaldan
la capa algebraica y la construcción; la geometría y los bosques siguen
escritos. La versión inglesa está en
[`../paper/golden_threshold.tex`](../paper/golden_threshold.tex), con
[PDF independiente](../output/pdf/golden_threshold.pdf).

Las notas de [intercambio adyacente](drafts/intercambio_uniforme.md) y
[núcleo de 40 mayores](drafts/nucleo_uniforme.md) se conservan como
historial. El cierre no necesita la permutación A/B ni la cota de 40;
esta última no tiene dictamen externo. La v2 de referencia permanece
congelada. La extensión global a dimensiones superiores queda por
auditar separadamente; no se afirma aquí.

## 2. Grosor variable w_i (GARANTÍA DE ÁREA RESUELTA Y REVISADA)

La nota [`drafts/grosor_variable.md`](drafts/grosor_variable.md) separa
dos umbrales. La colocación sigue siendo irrelevante bajo `rho≤1`,
para cualquier K compacto y dimensión, mediante el mismo intercambio
de subárboles. Para el área en el plano, con agujeros independientes,
el umbral universal exacto de optimalidad pasa a **`1/sqrt(2)`**.
Más generalmente, bajo `rho≤kappa<1`, la garantía exacta es
`min(1,kappa^(-2)-1)`. La captura de la cola cuando cabe en el agujero
del pivote permite probarlo; una familia de dos aros alcanza el límite.
Con solo superincrecencia estricta no hay factor positivo uniforme.
Siete certificados Lean respaldan las desigualdades y familias;
11 tests y 15 comprobaciones racionales respaldan los ejemplos y sus
controles. El cierre T3 posterior prueba además el umbral global de
colocación phi en el disco con agujeros independientes; quedan abiertas
otras métricas y formas. Fable acepta las pruebas de V1, captura de cola y V2;
sus precisiones sobre unicidad y no consecución se han incorporado.
Estado preciso en [`reviews/2026-09-15-extras-validation.md`](reviews/2026-09-15-extras-validation.md).

## 3. Flexibilidad de los calamares: parámetro δ (ABIERTA)

Modelo: un aro parcialmente montado sobre otro toca la sartén en todo lo que no está solapado, salvo una rampa levantada de anchura δ alrededor de cada solape. δ = 0 es la idealización totalmente flexible (contacto = anillo menos región solapada); δ > 0 penaliza cada solape con una banda muerta proporcional a su perímetro. Esto define una relajación continua donde las colocaciones parciales intercambian contacto por cardinalidad. Primeras preguntas: con δ = 0, ¿cuándo conviene solapar en el óptimo de área (conjetura: nunca, porque solapar solo resta contacto sin liberar más superficie que retirar el aro)?; con la métrica de número redefinida ("aros con contacto positivo"), ¿la relajación es total (siempre caben todos parcialmente)? ¿Y con umbral de contacto mínimo por aro?

## 4. Inventarios infinitos y casos degenerados (ABIERTA)

Ya usada tácitamente en el diagrama de fases (pequeños ilimitados). Límites interesantes: cadenas anidadas maximales r, r−w, r−2w, …; densidad asintótica de contacto alcanzable con inventario libre (¿cuál es el sup de A/πR² sobre todos los inventarios?); configuraciones límite de tipo apolonio cuando w → 0 con anidamiento prohibido por bandas. Primera pregunta concreta: con inventario libre de radios y w fijo, ¿el sup de densidad de contacto es 1 (rellenando con discos macizos r ≤ w) y cuál es la tasa de convergencia con n aros?

## 5. Métricas alternativas (PARCIALMENTE RESUELTA)

El teorema de selección cubre toda v monótona superaditiva (área de contacto, suma de radios, suma de perímetros…). Fuera de la clase: cardinalidad (v ≡ 1) falla incluso con superincrecencia (contraejemplo explícito), y cualquier v cóncava caerá igual. Frontera exacta demostrada: la superaditividad. Abierto: aproximabilidad de la cardinalidad; métricas mixtas (área sujeta a número mínimo).

## 6. Sustituto aditivo con radios enteros (ABIERTA)

El modelo aditivo (hermanos factibles sii suma ≤ capacidad) es la capa combinatoria del problema: contiene SUBSET-SUM, su umbral de irrelevancia de colocación es exactamente 1, y es candidato natural a algoritmo pseudopolinómico con radios enteros (DP sobre capacidades con estructura de bosque; obstáculo: el acoplamiento tipo multiple-knapsack entre contenedores generados por los propios objetos).

## 7. Reglas con input completo (ABIERTA, complejidad)

Las gemelas cierran las reglas función-del-estado. Para reglas que ven todos los radios por adelantado la pregunta es de complejidad: ¿se puede alcanzar el lex-máximo con un número polinómico de consultas al oráculo de empaquetamiento de hermanos? El testigo existe siempre (seguirlo es una ejecución voraz legal); encontrarlo es lo que puede ser caro.
