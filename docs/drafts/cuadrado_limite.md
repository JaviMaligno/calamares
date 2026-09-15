# Una familia aproximante y una cota algebraica para el cuadrado

Fecha: 2026-09-14. Continúa `cuadrado_gemelas.md`.

**Resultado escrito:** el candidato anterior sí da una cota superior:

```text
1 ≤ tau_cuadrado ≤ Y ≈ 1.684487745872346,
(17+10√2)Y² + (72+16√2)Y − (112+96√2) = 0, Y > 0.
```

Se construyen fallos de best fit con cuatro radios estrictamente distintos,
grosor positivo y rho arbitrariamente próximo a Y por arriba. No se prueba
que Y sea el umbral global ni el ínfimo de toda la familia deslizada o del
certificador Q. La configuración equilibrada de límite no es por sí misma
un contraejemplo: permite anidar el último aro y tiene dos radios iguales.

**Alcance:** demostración por continuidad escrita, identidades algebraicas
comprobadas por el kernel de Lean y ejemplos racionales comprobados con
`Fraction`. La continuidad, la raíz real y la sucesión completa no están
formalizadas en Lean. Este bloque no forma parte de la revisión externa
autorizada a Fable, limitada al resultado D y sus archivos enumerados.

## 1. La pared equilibrada

Escriba k=√2 y C=1+k/2. Para t>0 considere provisionalmente

```text
a0=1+t, b0=c0=t, s0=C(2+t), p0=q0=s0/2−t.
```

El par de raíz {a0,1} cabe en esquinas opuestas con tangencia exacta,
porque `2(s0−a0−1)²=(a0+1)²`. La holgura cuadrática común de Q2 y Q3 es

```text
G(t)=(a0+t)²−p0²−(s0−a0−t)²
    = ((17+10k)t²+(36+8k)t−(28+24k))/8.
```

Todos los coeficientes no constantes son positivos, por lo que G es
estrictamente creciente para t≥0. Además,

```text
G(21/25)=8897/5000−639k/500 < 0,
G(17/20)=5953/3200−399k/320 > 0.
```

Los signos se deducen respectivamente de `7/5<k` y `k<10/7`, ambas
desigualdades justificadas al cuadrar números positivos. Por continuidad
hay una única raíz positiva t0, con `21/25<t0<17/20`. Defina Y=2t0.
La ecuación anunciada es exactamente `32G(Y/2)=0`.

En todo el intervalo `21/25<t<17/20`, la longitud de la caja de Q5 en
el punto equilibrado es

```text
L0=s0/2−a0=k/2+(k−2)t/4,
1/2 < 229/400 < L0 < 5/7.
```

Por tanto `a0<s0/2`, `p0>0`, y

```text
2L0² < 50/49 < 4(21/25)² < (2t)².
```

Así, Q5 tiene margen positivo. Para t>t0 también Q2 y Q3 tienen
margen positivo. Las igualdades restantes se preservarán estructuralmente.

## 2. Perturbación que produce radios distintos y bloquea los agujeros

Fije cualquier `t0<t<17/20`. Para η>0 defina

```text
a=1+t+2η, m=1, b=t+η, c=t−η,
w=1−t+2η, H=a−w=2t,
s=C(a+1), p=q=s/2−t.
```

En η=0 las condiciones estrictas de Q2, Q3, Q5, `a<s/2` y `p>0`
acaban de probarse. Todas sus expresiones son continuas en η. Al haber
un número finito de ellas, existe η0(t)>0 tal que se conservan para
`0<η<η0(t)`. Reduciendo η0 si hace falta, suponga también

```text
η<t, η<1−t, 3η<2t−1.
```

Entonces `a>1>b>c>w>0`. Q1 y Q4 no necesitan un argumento de continuidad:

```text
p−(s/2−b)=η>0,
p+q−(s−b−c)=0.
```

Además `p=q≥0`. La longitud de Q5 es ahora `s/2−a+η`, y su margen
sigue siendo positivo por la elección anterior. Todas las condiciones
del Lema Q se cumplen, de modo que `{a,b,c}` no cabe en el cuadrado.
Se usa la versión universal del lema, `Square.excluded_of_conditions`,
cuyo enunciado abstracto vale para todo anillo conmutativo linealmente
ordenado. Matemáticamente incluye los reales; el proyecto Lean de core
no define ni instancia `ℝ`. La elección racional de p,q en D era una
comodidad para su certificado numérico.

## 3. Testigo, ejecución y cola dominante

El testigo de los cuatro aros pone `{a,1}` en esquinas opuestas de la
raíz, y `{b,c}` como hermanos sobre un diámetro del agujero del grande.
La primera pareja cabe por `2(s−a−1)²=(a+1)²`, con ambos radios a lo
sumo s/2; la segunda porque `b+c=2t=H`.

Best fit anida 1 en a: `1<H<a<s/2`. Las demás decisiones se justifican
por las siguientes diferencias exactas:

| Exclusión | Margen positivo |
|---|---|
| b junto a 1 dentro de a | `1+b−H=1−t+η` |
| c junto a 1 dentro de a | `1+c−H=1−t−η` |
| b dentro de 1 | `b−(1−w)=3η` |
| c dentro de 1 | `c−(1−w)=η` |
| c dentro de b | `c−(b−w)=1−t` |

El aro b cabe en la raíz junto a a reduciendo el radio del disco 1 en
el testigo. Al llegar c, la raíz queda excluida por Q, y la tabla agota
los agujeros disponibles. Best fit coloca exactamente tres aros.

La cola tras 1 es `b+c=2t`. Las otras son menores:

```text
(1+b+c)/a=(1+2t)/(1+t+2η)<2t,
c/b<1<2t.
```

La primera desigualdad equivale a `1<2t²+4tη`, que vale ya porque
`t>21/25`. Luego `rho=2t` exactamente.

Como esto vale para cada t en `(t0,17/20)`, existen contraejemplos con
rho que tiende a `2t0=Y` desde arriba. Por la definición del umbral
como ínfimo de valores con fallo, `tau_cuadrado≤Y`. La cota inferior 1
proviene del teorema de superincrecencia débil de la v1. ∎

## 4. También se puede usar una familia enteramente racional

El argumento anterior admite elegir t racional arbitrariamente próximo
a t0 por arriba, y después η racional suficientemente pequeño. Fijados
ambos, todos los radios y el grosor son racionales. Sustituya ahora
`s=C(a+1)` por un racional ligeramente mayor, y recalcule `p=q=s/2−t`.

Q1 y Q4 conservan exactamente las identidades de §2. Las desigualdades
estrictas de Q y de contención se conservan por continuidad en s. La
pareja de raíz pasa de tangencia a separación estricta, y todos los
márgenes de agujeros permanecen iguales. La densidad de los racionales
asegura tal elección de s. Por tanto la aproximación al límite tampoco
depende de admitir datos irracionales.

`code/cuadrado_limite.py` produce tres ejemplos de esta familia. Para
elegir el lado usa una cota racional superior de √2 obtenida con raíz
cuadrada entera; después vuelve a verificar todas las paredes exactas.
La corrección no depende del número de dígitos de esa aproximación.

| rho exacto | Decimal exacto | η | Paredes |
|---|---|---|---|
| `210561/125000` | `1.684488` | `10^-7` | 13/13 |
| `842243873/500000000` | `1.684487746` | `10^-11` | 13/13 |
| `4211219364681/2500000000000` | `1.6844877458724` | `10^-14` | 13/13 |

Estos ejemplos por sí solos solo prueban sus cotas finitas. El paso al
límite usa la demostración de §§1–4, y no una extrapolación numérica.

## 5. Polinomio racional y alcance formal

La ecuación de Y se escribe `A(Y)+kB(Y)=0`, con

```text
A(y)=17y²+72y−112, B(y)=10y²+16y−96.
A(y)²−2B(y)²=89y⁴+1808y³+4704y²−9984y−5888.
```

En consecuencia Y anula esa cuártica. La rama se define por la ecuación
original con `k=√2>0`; eliminar el radical no autoriza a seleccionar
cualquier raíz positiva de la cuártica.

`lean/Calamares/SquareLimit.lean` comprueba `balanced_gap_identity`
(la identidad de G, con denominadores eliminados), `norm_identity` y
`norm_root`, sobre anillos conmutativos. Su dependencia de axiomas se
inspecciona con `#print axioms`. Las identidades no formalizan por sí
solas el argumento de continuidad ni la existencia de la familia.

Reproducción:

```text
python -m unittest discover -s code -p test_cuadrado_limite.py -v
python code/cuadrado_limite.py
```

Desde `lean/`: `lake env lean Calamares/SquareLimit.lean`.

Permanece abierta una cota inferior que fuerce rho≥Y para toda la
familia deslizada, y más aún para cualquier fallo en un cuadrado.
