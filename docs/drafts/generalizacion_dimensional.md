# Generalizaciones de forma y dimensión: primera derivación

Fecha: 2026-09-14. Base: `paper/main.tex` de `v1-arxiv`.

**Estado:** G1 fue confirmada por la revisión estática independiente de
Fable (`../reviews/2026-09-14-fable-square-review.md`). G2–G7 y su
transferencia a las ejecuciones de la v1 siguen pendientes de revisión
independiente. Toda la nota está pendiente de integración. Los corolarios
usan los resultados probados de la v1; no usan sus cierres computacionales.
No se afirma novedad bibliográfica del lema elemental de reducción dimensional.

## 1. Resultado para tres piezas: el contenedor puede ser arbitrario

**Proposición G1.** En el modelo de asignación del paper, con radios
estrictamente decrecientes y grosor común positivo, todo voraz descendente
sobre a lo sumo tres aros produce el conjunto factible lexicográficamente
máximo, para cualquier contenedor compacto `K` en cualquier dimensión `d ≥ 1`.
No se requiere convexidad ni superincrecencia.

La factibilidad sigue permitiendo recolocar a los hermanos dentro de su
contenedor; no se afirma el resultado para coordenadas previamente fijadas.

**Demostración.** Una pieza que se omite antes de colocar ninguna no cabe
en `K`. Tampoco puede aparecer en una solución factible: si anidase en otro
aro, su bola exterior estaría contenida en `K`. Se puede descartar.
Con una o dos piezas restantes no hay una elección anterior capaz de
perjudicar la selección. Basta estudiar `r1 > r2 > r3` cuando `r1` y `r2`
han sido admitidos.

Si `r2` se omite, el prefijo `{r1,r2}` es infactible: las únicas opciones
son poner `r2` en `K` o en el agujero de `r1`, y ambas se han comprobado.
La decisión de `r3` se hace entonces sobre el único aro colocado. Así que
tampoco en ese caso puede haber divergencia respecto del lex-máximo.

Supongamos que existe un testigo `P` que coloca las tres piezas, y sea `F`
la asignación del voraz después de colocar `r2`. El padre de `r1` es `K`;
el de `r2` solo puede ser `K` o `r1`.

- Si el padre de `r2` coincide en `F` y `P`, la ubicación de `r3` en `P`
  certifica su admisión en `F`, pues los conjuntos de hermanos coinciden.
- Si `F` anida `r2` y `P` lo deja en `K`, el testigo contiene dos bolas
  exteriores disjuntas de radios `r1,r2` dentro de `K`. Sustituir la
  segunda por una bola concéntrica de radio `r3 < r2` certifica que el
  contenedor raíz de `F` admite `r3`.
- Si `F` deja `r2` en `K` y `P` lo anida, entonces `r2 ≤ r1-w`, luego
  `r3 < r2 ≤ r1-w`. El agujero vacío de `r1` en `F` admite `r3`.

En todos los casos el voraz admite `r3` cuando el prefijo completo es
factible. La implicación contraria es automática: una inserción legal es
un testigo de factibilidad. Esto prueba la proposición. ∎

**Diferencia respecto de la v1.** La prueba de `prop:n3` invoca
`r1+r2 ≤ R`. Lo que realmente necesita es la clausura de la factibilidad
al reducir el radio de una bola manteniendo su centro. Esa propiedad vale
para cualquier `K`, incluido un cuadrado.

## 2. Lema de reducción dimensional de las consultas de hermanos

**Lema G2.** Para `k ≥ 2` y `d ≥ k-1`, unas bolas de radios
`a1,...,ak > 0` caben como hermanos en una bola de radio `R` de `R^d`
si y solo si los mismos radios caben en una bola de radio `R` de `R^(k-1)`.
Para `k=1`, basta `a1 ≤ R` en cualquier dimensión positiva.

**Demostración.** Una colocación en dimensión menor se eleva conservando
las coordenadas de los centros y añadiendo ceros: las distancias y las
condiciones de contención son las mismas.

Para la otra dirección, centre la bola contenedora en el origen y sean
`c1,...,ck` los centros de un empaquetamiento en `R^d`. Su envolvente afín
`A = aff{c1,...,ck}` tiene dimensión a lo sumo `k-1`. Sea `q` la proyección
ortogonal del origen sobre `A`. Para cada `i`, el vector `ci-q` es
ortogonal a `q`, y por tanto

```text
||(ci-q)-(cj-q)|| = ||ci-cj|| ≥ ai+aj,
||ci-q||² = ||ci||²-||q||² ≤ (R-ai)².
```

Tras la traslación común `ci ↦ ci-q`, todos los centros están en el
subespacio lineal `A-q`, sus distancias se conservan y sus normas no
aumentan. Identificar isométricamente ese subespacio con un subespacio de
`R^(k-1)` da la colocación buscada. ∎

No se proyecta cada centro sobre un plano elegido de antemano: eso podría
reducir distancias y crear solapes. Se traslada la envolvente afín completa.
Tampoco se aplica este argumento al contenedor raíz cuando es un cuadrado:
la contención esférica `||ci||+ai ≤ R` es esencial.

**Corolario G3.** Las consultas de hasta tres hermanos en un contenedor
esférico tienen exactamente las mismas respuestas en todas las dimensiones
`d ≥ 2`, con radios y grosor fijos.

Más generalmente, un bosque de asignación fijo cuyos contenedores son todos
bolas y tienen a lo sumo `k` hijos es factible de manera independiente de la
dimensión para `d ≥ max(1,k-1)`. Se aplica el lema a cada grupo de hermanos
y se ensamblan las colocaciones desde las hojas. Los hijos de un aro
permanecen dentro de su bola interior, así que no interfieren con sus tíos.
Esta afirmación es sobre el bosque dado; no exige que todos los bosques
posibles del inventario tengan ese número máximo de hijos.

## 3. Qué se extiende de la v1 a todas las dimensiones d ≥ 2

En esta sección el contenedor raíz es una **bola**, los objetos son
cascarones esféricos y los parámetros numéricos son los mismos que en la v1.

### 3.1. La transición n = 3/4 no se desplaza

**Corolario G4.** La irrelevancia de colocación vale para hasta tres piezas
y falla para cuatro en una bola de cualquier dimensión `d ≥ 2`.

La parte positiva es G1. Para la negativa se conserva exactamente

```text
R = 15, w = 0.3, radios = {10, 5, 4.9, 4.8}.
```

El testigo pone `{10,5}` como hermanos de raíz y `{4.9,4.8}` dentro del
agujero del `10`. Ambos son problemas de dos bolas. Best fit anida el `5`,
coloca `4.9` en la raíz y rechaza `4.8`: el único rechazo geométrico de
tres hermanos usa `{10,4.9,4.8}` en radio `15`, infactible por `lem:cap`
de la v1 y por G3 en toda dimensión. Las otras opciones se descartan por
capacidad individual o por la condición exacta de dos bolas.

Todo el inventario es factible por el testigo y best fit solo coloca tres.
No importa si otros bosques, ajenos a estas ejecuciones, pudieran tener
cuatro hermanos: el testigo y el rechazo utilizados ya están certificados.

### 3.2. Las gemelas también se conservan

**Corolario G5.** El teorema `thm:twins` de la v1, incluida la obstrucción
a reglas deterministas de estado y la probabilidad de fallo de al menos
`1/2` para alguna instancia de toda regla aleatoria de estado, vale para
contenedores esféricos en cualquier dimensión `d ≥ 2`.

Se mantienen

```text
R = 15, w = 0.505,
I1 = {10, 5, 4.99, 4.50},
I2 = {10, 5, 4.76, 4.74}.
```

Las cuatro ejecuciones de la prueba de la v1 solo consultan uno, dos o
tres hermanos; G3 conserva tanto las admisiones como los rechazos, y las
condiciones de anidamiento solo dependen de radios y grosor. El estado
observable al decidir el padre del `5` sigue siendo idéntico en ambas
instancias a dimensión fija. Las elecciones necesarias son opuestas.
Si la regla elige raíz con probabilidad `p`, falla en `I2` con probabilidad
`p` y en `I1` con probabilidad `1-p`; el máximo es al menos `1/2`. ∎

El inventario completo de consultas triples es `{10,4.99,4.50}`,
`{10,5,4.99}`, `{10,5,4.50}`, `{10,4.76,4.74}`, `{10,5,4.76}`
y `{10,5,4.74}`. En particular, el rechazo de `{10,5,4.50}` usa el
bolsillo rígido general `30/7 < 4.50` (`prop:S5`), aunque el apartado
V2 de la v1 solo imprime las sustituciones `4.74` y `4.76`.

### 3.3. Suelo rígido Tribonacci y contraejemplo áureo

**Corolario G6.** El suelo de la familia `thm:rigidfloor` es exactamente
`T`, no alcanzado con grosor positivo, en toda dimensión `d ≥ 2`.

Las condiciones F1 y F2 son escalares. F3 es la infactibilidad de tres
bolas `{1,p,q}` en radio `1+t`, que por G3 equivale exactamente a F3 en
el plano. La familia admisible de parámetros `(t,p,q,w)` es la misma,
y también lo es la función `ρ` que se minimiza. Se heredan la cota
estricta y la sucesión aproximante de la v1. ∎

**Corolario G7.** Si `τ_d` denota el umbral global de irrelevancia de
colocación para contenedores esféricos en dimensión `d`, entonces

```text
1 ≤ τ_d ≤ φ, para todo d ≥ 2.
```

La cota inferior viene de `thm:oblivious` de `paper/main.tex`, cuyo
enunciado y prueba de superincrecencia débil incluyen expresamente
contenedores arbitrarios en toda dimensión.
Para la superior, se usa la familia de `thm:golden`, con los mismos
`w` y `ε`: el testigo de tres hermanos y todos los rechazos de hasta
tres hermanos se conservan por G3. Sigue habiendo fallos con
`ρ = φ+3ε → φ`.

**No se deduce `τ_d = τ_2` ni `τ_d = φ`.** Otros contraejemplos pueden
involucrar cuatro o más hermanos; la reducción a un plano no los cubre.
La monotonía de la factibilidad en la dimensión tampoco establece por
sí sola monotonía del umbral de fallo del voraz.

## 4. Dónde puede aparecer geometría distinta en dimensión 3

La primera consulta de hermanos que puede distinguir las dimensiones
2 y 3 tiene **cuatro** piezas. Existe incluso un ejemplo con radios
estrictamente distintos y margen positivo:

```text
R = 1,
radios = {441, 440, 439, 438}/1000.
```

**Factible en 3D.** Use los centros

```text
( a, a, a), ( a,-a,-a), (-a, a,-a), (-a,-a, a), a = 8/25.
```

Todos tienen norma `sqrt(3)*a` y las distancias entre pares son
`sqrt(8)*a`. Basta verificar los márgenes racionales

```text
(1-441/1000)² - 3(8/25)² = 5281/1000000 > 0,
8(8/25)² - (2·441/1000)² = 10319/250000 > 0.
```

**Infactible en 2D.** Si cupieran, reducir todos los radios a
`r=438/1000` daría cuatro discos iguales. Sus centros tienen norma
a lo sumo `1-r`. Si uno está en el origen, su distancia a cualquier
otro es a lo sumo `1-r < 2r`, imposible. En otro caso, dos centros
consecutivos en orden angular forman un ángulo de a lo sumo `π/2`.
Su distancia al cuadrado es a lo sumo `2(1-r)²`, pero

```text
(2r)² - 2(1-r)² = 16961/125000 > 0.
```

Contradicción. Este es un ejemplo de diferencia de factibilidad, no un
nuevo contraejemplo de irrelevancia de colocación. Con `w=1` todos los
objetos son sólidos y se fuerza precisamente ese grupo de hermanos.

## 5. Cuadrado: lo que realmente sigue abierto

**Actualización posterior del 2026-09-14:**
[`cuadrado_certificado.md`](cuadrado_certificado.md) cierra el primer
objetivo de esta sección: prueba el fallo de D con `rho=337/200`, con
exclusión cartesiana del trío comprobada en Lean. También se corrigió
la condición individual de C2. El inventario que sigue documenta el
diagnóstico inicial; la fórmula global de M y el suelo rígido X
conservan los límites allí señalados.

G1 cierra el punto de `n ≤ 3` también en cuadrado. Los demás argumentos
de esta nota no sustituyen su geometría de raíz por la del disco.

El borrador `cuadrado.md` ya contiene mucho trabajo aprovechable, pero
hay que conservar sus dependencias y sus límites:

- La cuártica `17X⁴-4X³-62X²+4X+49=0` y la raíz relevante
  `X≈1.7110185903` son resultados algebraicos. Su interpretación como
  suelo exacto de una familia geométrica requiere las hipótesis que
  el propio borrador etiqueta `[D*]`; no es el umbral global probado.
- El par deslizado y las instancias con `ρ≈1.685` son evidencia
  numérica. Que un optimizador no encuentre un trío factible no prueba
  su infactibilidad. La cota global `τ_cuadrado ≤ 1.685` exige cerrar
  esa parte, aunque el borrador la formule como consecuencia.
- Hay una omisión elemental en el Lema C2 tal como está escrito:
  la fila diagonal necesita además que el mayor círculo quepa
  individualmente, `r1 ≤ s/2`. Para `s=1`, los radios `{0.57,0.01}`
  satisfacen `Σr=0.58 < 2-sqrt(2)` y la desigualdad de fila para dos
  piezas, pero el primero ni siquiera cabe en el cuadrado. La versión
  corregida debe incluir esa condición; el oráculo de pares de C1
  sí la declara. Esta nota registra la corrección pendiente del
  borrador histórico, sin presuponer que afecte a sus instancias.
- La revisión antigua limita la cota basada en `min b_cuadrado`
  al dominio `α ≥ 1`. Conviene fijar ese dominio antes de reutilizar
  las cotas en otras plantillas.

**Primer objetivo sustancial del cuadrado:** obtener un certificado
global de infactibilidad para una instancia del par deslizado por debajo
de `X`, con un testigo explícito de cuatro aros y todas las exclusiones
de anidamiento. Se puede intentar una clasificación completa de patrones
de tangencia o una cobertura rigurosa de las cajas de centros mediante
aritmética racional/de intervalos. Una fórmula para un único patrón de
tangencias solo demuestra que ese patrón existe; aún hay que excluir
los otros patrones para certificar un máximo insertable.

Después: determinar el ínfimo realizable de esa familia, distinguirlo
del umbral global y buscar gemelas en cuadrado. No es necesario resolver
el umbral global para que una separación geométrica rigurosa sea valiosa.

## 6. Encaje editorial propuesto

| Bloque | Encaje | Resultado exigible |
|---|---|---|
| G1–G7: tres piezas, reducción dimensional, transición, gemelas, suelos | v2 del artículo actual | Revisar estas pruebas e incorporarlas junto a los teoremas que amplían |
| Raíz cuadrada: par deslizado y dependencia de la forma | Candidato a segundo artículo | Al menos una separación certificada y un teorema estructural sobre su mecanismo |
| Grupos de cuatro o más hermanos en dimensión superior | Investigación posterior | Una diferencia en los fallos del voraz, además de una diferencia de factibilidad |
| Grosor variable, flexibilidad, complejidad y objetivos | Líneas separadas aún sin elegir | Fijar el modelo y una pregunta central antes de ampliar el alcance |

La decisión editorial puede esperar al primer teorema propio del cuadrado.
Las extensiones por reducción dimensional son breves y comparten todas
las pruebas esenciales con la v1, por lo que por sí solas encajan mejor
como ampliación del manuscrito actual.

## 7. Bibliografía de orientación y verificación

La búsqueda inicial no establece novedad ni ausencia de antecedentes del
lema G2. Dos puntos de entrada primarios para el trabajo posterior:

- López y Beasley, *Packing unequal circles using formulation space search*
  (2013), estudian heurísticas para círculos desiguales en varios
  contenedores, incluido el cuadrado. Su resumen ayuda a situar el problema;
  no se usa como certificado geométrico:
  [página del autor](https://people.brunel.ac.uk/~mastjjb/jeb/unequal.html).
- Pedroso, Cunha y Tavares, *Recursive circle packing problems* (2016),
  antecedente del modelo recursivo ya citado en la v1:
  [artículo en el servidor institucional](https://cmup.fc.up.pt/cmup/cv/2016-International_Transactions_in_Operational_Research.pdf).

La prueba universal de G2 es la identidad ortogonal de §2, no una
simulación. Los tres márgenes de §4 se pueden verificar exactamente
con `fractions.Fraction`. G1 ya fue revisada por Fable; la revisión
independiente de G2–G7 y de su transferencia a las ejecuciones de la v1
sigue pendiente.
