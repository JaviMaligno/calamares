# Gemelas en cuadrado y cota mejorada 1.68449

Fecha: 2026-09-14. Continúa `cuadrado_certificado.md`.

**Continuación:** [`cuadrado_limite.md`](cuadrado_limite.md) convierte el
candidato algebraico de §6 en una cota superior mediante una familia
aproximante. Las etiquetas de exploración de esta nota registran el
estado anterior; la optimalidad sigue abierta.

**Resultados:** (1) instancias gemelas en cuadrado que excluyen toda regla
determinista basada solo en el estado; (2) para una regla aleatoria, una
de las dos instancias falla con probabilidad al menos `1/2`; (3) mejora
de la cota demostrada a `tau_cuadrado ≤ 168449/100000 = 1.68449`.

**Verificación:** el Lema Q paramétrico completo, con sus reflexiones,
está ahora formalizado en `Square.no_packing`. Las exclusiones y el
testigo cartesiano de esta nota se comprueban en `SquareTwins.lean`.
El algoritmo y la interpretación euclidiana de las coordenadas se
justifican por escrito. Este bloque está pendiente de revisión externa;
la revisión autorizada a Fable abarca D, no las gemelas ni el límite Y.

## 1. Dos inventarios con el mismo estado decisivo

Fijamos exactamente

```text
s = 25607/5000 = 5.1214,
w = 301/1000 = 0.301,
a = 2, m = 1, H_a = a-w = 1.699,
I1 = {2, 1, 0.850, 0.849},
I2 = {2, 1, 0.950, 0.750}.
```

La sartén tiene capacidad `s/2=2.5607`. Al procesar `m=1` ambos
contenedores, sartén y agujero de `a`, son factibles y el estado
observable es idéntico. Los radios son estrictamente decrecientes
en ambos inventarios, que además tienen la misma cardinalidad.

## 2. Los tres hechos geométricos

Se utiliza el Lema Q de `cuadrado_certificado.md`. La siguiente tabla
da los parámetros racionales; todas sus desigualdades son exactas:

| Hecho | Radios `a,b,c` | `p,q` | Resultado |
|---|---|---|---|
| Trío de I1 | `2,.850,.849` | `1.72,1.718` | Infactible |
| Trío con pivote | `2,1,.750` | `2.12,1.39` | Infactible |
| Trío de I2 | `2,.950,.750` | Testigo de abajo | Factible |

El segundo hecho excluye también `{2,1,z}` para todo `z ≥ .750`:
si ese trío cupiera, reducir el tercer disco a `.750` manteniendo
su centro daría el trío prohibido.

Para el trío de I2, tome los centros

```text
A=(2.96,2), B=(.95,4.1714), C=(4.3714,4.3714).
```

Cada centro está en su caja de contención. Los márgenes entre distancia
al cuadrado y suma de radios al cuadrado son, respectivamente,

```text
AB: 1314449/25000000 > 0,
AC: 663599/12500000 > 0,
BC: 221399449/25000000 > 0.
```

Lean formaliza los tres hechos sobre coordenadas en un anillo conmutativo
linealmente ordenado, en unidades de `1/10000`. No es una comprobación
de una malla racional: las exclusiones cuantifican sobre todas las
coordenadas y el testigo satisface el mismo predicado `FitsTriple`.

## 3. Testigos completos y exclusiones de anidamiento

El par de raíz `{a,m}={2,1}` cabe en esquinas opuestas, con centros
`(2,2)` y `(s-1,s-1)`, porque ambos caben individualmente y
`2(s-3)^2 > 9`.
Reduciendo el disco `1` de ese par, con el mismo centro, se obtiene
también la factibilidad de `{2,z}` en la raíz para todo `0<z<1`.
Esto justifica la admisión del tercer aro cuando el pivote está anidado.

Para **I1**, coloque ese par en la sartén y anide los dos pequeños
en el agujero de `a`: `.850+.849=1.699=H_a`, fila diametral exacta.

Para **I2**, coloque el trío de §2 en la sartén y anide `m` dentro de
`a`, posible porque `1 ≤ H_a`.

Así, el lex-máximo contiene los cuatro aros en ambas instancias. Las
paredes escalares que fuerzan las ejecuciones son:

- Todo pequeño cabe individualmente en `H_a`.
- Ninguno cabe allí junto a `m`, pues incluso `1+.750=1.750>1.699`.
- Ninguno cabe en el agujero de `m`, de radio `.699`.
- El último no anida en el anterior: `.849>.850-.301` y
  `.750>.950-.301`.
- La pareja pequeña de I1 cabe en `H_a`; la de I2 no, porque
  `.950+.750=1.700>1.699`.

## 4. Las cuatro ejecuciones son forzadas tras decidir m

| Inventario | Padre de `m` | Padre del tercer aro | Último aro | Total |
|---|---|---|---|---|
| I1 | Agujero de `a` (best fit) | Sartén | Bloqueado | 3 |
| I1 | Sartén (worst fit) | Agujero de `a` | Mismo agujero | 4 |
| I2 | Agujero de `a` (best fit) | Sartén | Sartén | 4 |
| I2 | Sartén (worst fit) | Agujero de `a` | Bloqueado | 3 |

Si `m` está anidado, el tercero va a la sartén, ya que sus alternativas
de agujero están excluidas. El último solo podría ir a la sartén:
en I1 el trío es infactible; en I2 el testigo lo admite.

Si `m` está en la sartén, el trío con pivote excluye de ella a ambos
pequeños. El tercero se anida en `H_a`, y el cuarto cabe allí
exactamente en I1. Las demás posibilidades están excluidas por §3.
En particular, esta tabla no depende de elegir reglas best/worst
en pasos posteriores: todas las decisiones posteriores son forzadas.

**Teorema de las gemelas cuadradas.** Toda regla determinista que use
solo el estado observable hace la misma elección al procesar `m` en
I1 e I2, y por tanto falla en una. Para una regla aleatoria de estado,
sea `p` la probabilidad de enviar `m` a la sartén. Las probabilidades
de fallo son `1-p` en I1 y `p` en I2, por lo que alguna es al menos `1/2`.
La afirmación no incluye reglas que consultan el inventario futuro.

Las colas dominantes son `rho(I1)=1.699` y `rho(I2)=1.700`; las colas
del aro grande son `1.3495` y `1.350`, respectivamente. Ambas gemelas
están por debajo de `X>1.7`.

## 5. Una instancia mejorada con rho = 1.68449

La exploración del Lema Q permitió escoger los siguientes racionales;
su validez final se comprueba sin usar las aproximaciones del optimizador:

```text
s = 4.85201606,
a = 1.8422452, m = 1, b = .8422451, c = .8422449,
w = .1577552,
p = 1.5837677, q = 1.5837671.
```

Todos los decimales son exactos. Multiplicar por `100000000` da

```text
s = 485201606, a = 184224520, m = 100000000,
b = 84224510, c = 84224490, w = 15775520,
p = 158376770, q = 158376710.
```

`SquareTwins.improved_excluded` aplica el Lema Q paramétrico y demuestra
que el trío `{a,b,c}` no cabe. `improved_gates` verifica las paredes
del testigo y del voraz, incluyendo:

```text
b+c = a-w = 1.68449,
a > 1+b,
c > 1-w                         (margen exacto 0.0000001),
2(s-a-1)^2 > (a+1)^2.
```

Se repite literalmente la prueba de D: un testigo coloca `{a,m}` en
la sartén y `{b,c}` dentro de `a`; best fit anida `m`, coloca `b` en
la sartén y rechaza `c` en todos los contenedores. Las comprobaciones
de las dos colas restantes muestran que la dominante es `b+c`.

**Corolario:** `1 ≤ tau_cuadrado ≤ 168449/100000 = 1.68449`.
La cota mejora `337/200`; no se afirma que sea óptima.

## 6. Candidato a límite: derivación inicial

En la frontera simétrica explorada se igualan `b=c=t`, `a=1+t` y
`s=(1+1/sqrt(2))(a+1)`. La frontera cuadrática geométrica resulta

```text
(a+t)^2 = (s/2-t)^2 + (s-a-t)^2.
```

Con esas sustituciones, la candidata `Y=2t` satisface

```text
(17+10sqrt(2))Y^2 + (72+16sqrt(2))Y - (112+96sqrt(2)) = 0,
89Y^4 + 1808Y^3 + 4704Y^2 - 9984Y - 5888 = 0,
Y ≈ 1.684487745872346.
```

Esta eliminación algebraica no prueba un ínfimo. La configuración de
frontera tiene radios pequeños iguales y el rescate por anidamiento
justo en igualdad; no es un contraejemplo legal de radios estrictos.
Faltan una familia aproximante con todas las paredes estrictas y, para
afirmar optimalidad de la familia, una cota inferior que no suponga de
antemano simetría ni saturación de las otras restricciones.

**Solo `1.68449` es una cota superior demostrada en esta nota.**

## 7. Reproducción y correspondencia

```text
python -m unittest discover -s code -p "test_cuadrado_*.py" -v
python code/cuadrado_gemelas.py
python code/cuadrado_optimizado.py
```

Desde `lean/`: `lake build`. Los nuevos resultados son
`Square.no_packing`, `Square.excluded_of_conditions`,
`SquareTwins.balanced_excluded`, `root_pivot_excluded`,
`unbalanced_fits`, `improved_excluded`, `twin_walls`, `twin_tails`
y `improved_gates`.

El script de gemelas contiene un oráculo exacto **restringido a las
consultas alcanzables en estas cuatro ejecuciones**: pares mediante
su criterio exacto, tríos mediante los dos certificados y el testigo
explícito. Una consulta desconocida lanza un error, no se interpreta
como infactible. El algoritmo devuelve la asignación de padres completa.

La inspección de axiomas de Lean solo devuelve `propext`,
`Classical.choice`, `Quot.sound`. El núcleo geométrico está formalizado;
la obstrucción informacional y la semántica del voraz están probadas
por escrito y contrastadas por las cuatro ejecuciones exactas.
