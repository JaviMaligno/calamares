# Un contraejemplo cuadrado exacto con rho = 337/200

Fecha: 2026-09-14. Continúa `cuadrado.md`, instancia D.

**Continuación:** `cuadrado_gemelas.md` añade gemelas, mejora la cota a
`1.68449` y formaliza también el Lema Q con parámetros arbitrarios.
La presente nota conserva el resultado D original, ahora caso particular.

**Resultado:** existe una instancia de cuatro aros en una sartén cuadrada
con `rho = 337/200 = 1.685 < X` en la que best fit coloca tres aros y el
conjunto lexicográficamente máximo contiene los cuatro. La exclusión
geométrica del trío está formalizada en Lean para todas las coordenadas,
sin búsqueda numérica ni hipótesis sobre patrones óptimos de tangencia.

**Estado:** prueba escrita y comprobación del kernel de Lean del núcleo
cartesiano de infactibilidad, más certificados exactos de las paredes
escalares. La traducción entre círculos y desigualdades cartesianas, la
semántica del bosque y la ejecución del algoritmo se explican aquí; no
están modeladas como objetos geométricos/algorítmicos en Lean. La revisión
estática independiente de Fable confirmó D, el Lema Q y G1: revisión menor
de redacción, atendida. Informe y respuesta en
[`../reviews/2026-09-14-fable-square-review.md`](../reviews/2026-09-14-fable-square-review.md)
y [`../reviews/2026-09-14-fable-square-response.md`](../reviews/2026-09-14-fable-square-response.md).

## 1. Lema general de confinamiento por cuadrantes

Sean tres discos de radios `a ≥ b ≥ c > 0` en un cuadrado `[0,s]^2`,
con `a ≤ s/2`. Supongamos que existen racionales `p ≥ q ≥ 0` tales que

```text
(Q1)  p ≥ s/2-b,
(Q2)  p²+(s-a-b)² < (a+b)²,
(Q3)  q²+(s-a-c)² < (a+c)²,
(Q4)  p+q ≥ s-b-c,
(Q5)  L := s-c-a-q ≥ 0  y  2L² < (b+c)².
```

**Lema Q.** Bajo estas condiciones los tres discos no caben.

**Demostración.** Denote sus centros por `A,B,C`. Reflejando todo el
empaquetamiento respecto de los ejes medios del cuadrado, podemos suponer

```text
a ≤ Ax,Ay ≤ s/2.
```

Los centros pequeños satisfacen `b ≤ Bx,By ≤ s-b` y
`c ≤ Cx,Cy ≤ s-c`. En cada coordenada la separación absoluta entre
`A` y `B` es como máximo `s-a-b`: la separación hacia el lado bajo es
a lo sumo `s/2-b ≤ s-a-b`, y hacia el alto es a lo sumo `s-a-b`.
Lo mismo vale con `c` para `A,C`.

Si `|Bx-Ax| ≤ p`, entonces

```text
|B-A|² ≤ p²+(s-a-b)² < (a+b)²,
```

en contradicción con la separación de los discos. Por tanto
`|Bx-Ax| > p`. La alternativa `Bx-Ax < -p` es imposible por Q1:
`Ax-Bx ≤ s/2-b ≤ p`. Así que `Bx > Ax+p`, y simétricamente
`By > Ay+p`. La contención de `B` fuerza ahora

```text
Ax,Ay < s-b-p.
```

La misma cota cuadrática con Q3 da `|Cx-Ax| > q`. La alternativa
negativa vuelve a ser imposible porque

```text
Ax-Cx < s-b-p-c ≤ q                       (Q4).
```

En consecuencia `Cx > Ax+q`, `Cy > Ay+q`. Puesto que `p ≥ q` y
`b ≥ c`, los centros `B` y `C` pertenecen ambos al cuadrado de
coordenadas entre `a+q` y `s-c`. Su distancia al cuadrado no supera
`2L² < (b+c)²`, contradicción. ∎

El argumento excluye **todos** los patrones de colocación. No necesita
probar que el mayor hueco se alcanza en una esquina ni resolver la función
de máximo insertable del borrador antiguo.

## 2. Instancia D racional y márgenes exactos

Fijamos

```text
s = 6071/1250 = 4.8568,
w = 4/25 = 0.16,
radios = {a,m,b,c} = {369/200, 1, 211/250, 841/1000}
                  = {1.845, 1, 0.844, 0.841},
p = 1591/1000, q = 1581/1000.
```

Los radios y el grosor son exactamente los de la instancia D. El lado
se ha aumentado ligeramente respecto del lado rígido
`(a+1)/(2-sqrt(2)) ≈ 4.8567187925`, para trabajar solo con racionales.

Las cinco paredes de Q tienen los siguientes márgenes:

| Pared | Margen exacto positivo |
|---|---|
| `p-(s/2-b)` | `33/5000` |
| `(a+b)²-p²-(s-a-b)²` | `2079/25000000` |
| `(a+c)²-q²-(s-a-c)²` | `66559/25000000` |
| `p+q-(s-b-c)` | `1/5000` |
| `(b+c)²-2L²`, con `L=2949/5000` | `53587423/25000000` |

Así, `{a,b,c}` es infactible en el cuadrado de lado `6071/1250`.
También lo es en el cuadrado rígido original, por inclusión de
contenedores. El certificado no depende de un fallo del optimizador.

## 3. Testigo explícito de los cuatro aros

Ponga `a` y `m=1` en esquinas opuestas del cuadrado, con centros

```text
A=(a,a), M=(s-1,s-1).
```

Ambos discos caben individualmente. La separación está certificada por

```text
2(s-a-1)²-(a+1)² = 16337/25000000 > 0.
```

El agujero del aro grande tiene radio `a-w=337/200=1.685`.
Coloque en él, sobre un diámetro, el disco de radio `b` con centro relativo
`(-c,0)` y el disco de radio `c` con centro relativo `(b,0)`.
Como `b+c=a-w`, los dos son tangentes entre sí
y a la frontera del agujero, sin solapamiento de interiores. Por tanto
los cuatro aros son factibles y constituyen el conjunto lex-máximo.

## 4. Ejecución de best fit y todas las exclusiones

Best fit compara capacidades; la del cuadrado es su inradio `s/2=2.4284`.

1. El aro `a` se coloca en la sartén.
2. `m=1` cabe en la sartén junto a `a` por el testigo anterior y también
   en el agujero `a-w=1.685`. Best fit elige el agujero, de menor capacidad.
3. `b=0.844` no cabe en el agujero del grande junto a `m`, porque
   `1+b=1.844 > 1.685`. Tampoco cabe en el agujero de `m`, de radio
   `1-w=0.84`. Sí cabe junto a `a` en la sartén: basta sustituir el
   disco `m` del testigo de raíz por el disco menor `b`, conservando
   su centro. Su ubicación en la sartén es forzada.
4. `c=0.841` queda excluido de todos los contenedores:

| Contenedor | Motivo exacto del rechazo |
|---|---|
| Sartén, con hermanos `a,b` | Lema Q, o `Square.d_no_packing` |
| Agujero de `a`, ocupado por `m` | `1+c=1.841 > a-w=1.685` |
| Agujero de `m` | `c=0.841 > 1-w=0.84` |
| Agujero de `b` | `c=0.841 > b-w=0.684` |

Para los agujeros usamos el criterio exacto de dos discos: caben en
un disco de radio `H` si y solo si la suma de sus radios no supera `H`.
El algoritmo permite recolocar hermanos, pero no cambiar las asignaciones
de padre ya elegidas. No quedan otros contenedores disponibles.

**Conclusión:** best fit coloca exactamente `{a,m,b}`, mientras el
lex-máximo es `{a,m,b,c}`.

## 5. Valor de rho, comparación con X y consecuencias

Las tres colas relevantes son

```text
(1+b+c)/a = 179/123 < 337/200,
(b+c)/1  = 337/200,
c/b      = 841/844 < 337/200.
```

Luego `rho=337/200=1.685` exactamente.

Para la constante algebraica X del borrador `cuadrado.md`, sea
`P(x)=17x⁴-4x³-62x²+4x+49`, y sea `X` la raíz de la rama
`(17/10,43/25)`. Para identificarla sin decimales:

```text
P(17/10) = -10463/10000 < 0,
P(43/25) = 348292/390625 > 0,
10000 P((17+z)/10)
    = 17z⁴+1116z³+21238z²+92604z-10463.
```

El polinomio desplazado es estrictamente creciente para `z ≥ 0`,
pues todos sus coeficientes no constantes son positivos. Por continuidad
y monotonía existe una única raíz en esa rama. En particular

```text
rho = 337/200 < 17/10 < X.
```

**Corolario Q1.** El umbral global para sartén cuadrada satisface
`1 ≤ tau_cuadrado ≤ 337/200 < X`. La cota inferior procede del
teorema de superincrecencia débil, válido para cualquier contenedor.

**Corolario Q2.** La transición de irrelevancia a fallo se produce
en `n=3/4` también en cuadrado: la parte positiva para todo contenedor
es la Proposición G1 de `generalizacion_dimensional.md`, y aquí se
demuestra la parte negativa.

No se afirma que `337/200` sea el umbral exacto. Tampoco se cierra la
interpretación geométrica completa de `X` como ínfimo de una familia
rígida, que sigue condicionada en el borrador anterior. Lo demostrado
es un fallo realizable por debajo de esa constante algebraica.

## 6. Control factible y alcance de Lean

Para el control D' mantenga `a,s`, reduzca los pequeños a
`b'=0.840`, `c'=0.835`, y tome

```text
A=(2.4284,1.845), B=(0.840,4.0168), C=(4.0218,4.0218).
```

Todos están dentro del cuadrado y las tres separaciones son estrictas.
Estas cuentas se formalizan en `Square.d_prime_witness`; D' es un
control factible explícito, no solo un rechazo del certificador.

El archivo `lean/Calamares/Square.lean` contiene:

| Teorema | Alcance |
|---|---|
| `sq_le_of_bounds`, `separated_coordinate` | Desigualdades universales sobre un anillo conmutativo linealmente ordenado |
| `d_no_normalized` | Exclusión del trío para el centro grande en el cuarto inferior izquierdo |
| `d_no_packing` | Exclusión cartesiana completa, incluidas las cuatro combinaciones de reflexiones |
| `d_margins` | Márgenes racionales del Lema Q para D |
| `d_witness`, `d_greedy_walls`, `d_tail` | Cuentas del testigo, de los agujeros y del valor de rho |
| `x_bracket`, `x_shift` | Signos y polinomio desplazado para identificar la rama de X |
| `d_prime_witness` | Control factible cercano con coordenadas racionales explícitas |

La formalización geométrica usa coordenadas multiplicadas por `10000`:
lado `48568` y radios `18450,8440,8410`. Su tipo es universal en un
anillo conmutativo linealmente ordenado; no restringe las coordenadas
a enteros o racionales. Las condiciones codificadas son exactamente
los intervalos de contención y las tres cotas de distancia al cuadrado.

Lean core no contiene aquí un tipo de disco euclidiano ni el algoritmo
de selección. La interpretación de esas desigualdades sobre los reales
y la ejecución de §4 forman el puente escrito hacia el modelo del paper.
El lema Q con parámetros arbitrarios quedó posteriormente formalizado
en `Square.no_packing` y `excluded_of_conditions`; la prueba original
especializada a D se conserva como `d_no_packing`.

La inspección de axiomas devuelve solo `propext`, `Classical.choice`
y `Quot.sound`. No aparece `sorryAx` ni `Lean.ofReduceBool`; no se usa
`native_decide` ni se añaden axiomas.

## 7. Reproducir y continuar

Desde la raíz:

```text
python -m unittest discover -s code -p test_cuadrado_certificado.py -v
python code/cuadrado_certificado.py
```

Desde `lean/`:

```text
lake build
lake env lean Calamares/Square.lean
```

El primer comando Python comprueba el certificador con D, E, D', un
caso factible, un caso tangente y certificados inválidos. El segundo
reproduce las 17 condiciones exactas de la instancia completa, incluido
el orden estricto y el grosor positivo añadidos tras la revisión. Ambos
usan enteros y `Fraction`, sin tolerancias ni solvers numéricos.

**Continuación realizada:** `cuadrado_gemelas.md` obtiene gemelas y una
cota mejorada `1.68449`. `cuadrado_limite.md` construye después una
familia aproximante que prueba la cota Y por continuidad. Quedan la
revisión externa de esos bloques y la optimalidad de la familia. Determinar una
fórmula del máximo insertable sigue siendo valioso, pero no fue necesario
para este resultado.
