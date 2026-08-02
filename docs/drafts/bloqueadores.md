# Los bloqueadores pagan: agujeros ocupados a profundidad arbitraria

Borrador. Ataca el **paso 3 de la Batalla 1** (`ESTADO_SESION.md` §3) en su
frente (a): ¿qué pasa cuando los agujeros de los ocupantes están ocupados y
la pared (Bo) de `ocupantes.md` se vuelve recursiva? Respuesta: la recursión
colapsa en dos piezas — un lema constructivo que tarifica el bloqueo de un
agujero (**bloquear cuesta masa ≥ la holgura**, Lema R) y un argumento de dos
colas en el **nodo mínimo** del árbol de ocupantes que no necesita inducción
(Teorema B). El resultado, con agujeros ocupados como se quiera y a cualquier
profundidad:

    bloqueo  ⟹  ρ > Ψ(ω) := (1 − ω) + √((1 − ω)² + 1) ,

con Ψ(0) = 1 + √2, Ψ(1/4) = 2 exacto, y

    Ψ(ω) > T   ⟺   ω < ω₆ := (T − 1)²/2 = 0.3522011… .

Y no queda ninguna hipótesis de ocupación: el **Teorema B″** (§5) elimina
también «m sin hijos» — la dicotomía de evacuación parte el bloqueo en la
rama `σ₂ > 1−ω` (donde el Teorema B aplica tal cual) y la rama
`σ₁ + Σ hijos(m) > 1`, cuya optimización es otra media metálica,
`Ψ_B = raíz de u² − (2−ω)u − 1 ≥ Ψ = raíz de u² − 2(1−ω)u − 1`, dominada
automáticamente (la raíz crece con b). De propina, `Ψ(0) = 1 + √2` es la
**razón de plata**, y el umbral de la rama B es `(T−1)²` exacto, el doble
del de la A.

Historia de verificación (actas en `VEREDICTOS.md`): Lema R, Bo″, Teorema B
y B1 confirmados por rederivación a ciegas idéntica; la §5 primera («la
fuga», que afirmaba que la hipótesis m-sin-hijos era necesaria) fue
REFUTADA por el verificador — su familia ni siquiera estaba bloqueada — y su
conjetura de lo contrario es ahora el Teorema B″. Verificación:
`code/bloqueadores.py` (6/6). Numeración local: Lema R, pared Bo″,
Teoremas B y B″, Corolarios B1–B2.

## 1. Marco

Como en `ocupantes.md` §1: `v` = sartén de radio `R` con ocupantes
`{α} ∪ O ∪ {m}`, `O = {o₁ ≥ … ≥ o_j}`, `j ≥ 1`, `o_i ≥ m = 1`; `u` = agujero
de `α` (capacidad `α − ω ≥ 1`); el testigo colocó `S = {σ₁ ≥ σ₂}` en `u`
(`σ₂ ≤ σ₁ ≤ 1`). **Se elimina la hipótesis de agujeros libres**: los `o_i`
pueden tener hijos, los hijos pueden tener hijos (a cualquier profundidad, y
pueden ser ≥ m), y `σ₁` puede tener hijos. Queda solo: `m` sin hijos.

Legalidad de las colocaciones (marco de `reinsercion.md` §1–2): el
intercambio construye una colocación nueva `P′` que conserva las
asignaciones de contenedor de los aros ≥ m; las **posiciones** dentro de
cada contenedor son existenciales (una colocación es un bosque de
anidamiento cuyos hermanos empaquetan). Insertar `σ₂` en el agujero de un
aro `y` solo cambia el contenedor de `σ₂` (< m): legal; y la factibilidad es
la del conjunto de hermanos `{σ₂} ∪ hijos(y)` en el disco `y − ω`, con todas
las posiciones re-elegibles.

## 2. Lema R: bloquear un agujero cuesta la holgura

**Lema R (el disco opuesto).** Sea un disco de capacidad `c`, `σ ≤ c` la
pieza mayor y `C` un multiconjunto de piezas ≤ σ. Si

    Σ C  ≤  c − σ ,

entonces `{σ} ∪ C` empaqueta en el disco.

*Demostración.* Colóquese `σ` tangente a la pared: centro en `(−(c−σ), 0)`.
El disco de radio `r = c − σ` centrado en `(c − r, 0)` es interiormente
tangente a la pared y **exactamente** tangente a σ: la distancia entre
centros es `(c−σ) + (c−r) = c = σ + r`. Su interior es por tanto disjunto de
σ y está contenido en el contenedor: es un disco libre de radio `c − σ`.
Como `Σ C ≤ c − σ`, `C` entra en él en fila (Lema 0 de `resultados.md`:
piezas con suma de radios ≤ r caben alineadas a lo largo de un diámetro del
disco de radio r). ∎

**Contrapositiva (la tarifa).** Si `{σ₂} ∪ hijos(y)` **no** empaqueta en el
disco `y − ω` (y σ₂ es la pieza mayor, cierto en cuanto los hijos de `y`
sean ≤ σ₂ — véase §3 para el caso general), entonces

    Σ hijos(y)  >  (y − ω) − σ₂ ,      es decir      y  <  σ₂ + ω + X_y ,

con `X_y := Σ hijos(y)`. Bloquear el agujero de `y` contra σ₂ cuesta masa
al menos igual a la holgura que el agujero le sacaba a σ₂. Con `X_y = 0`
esta es exactamente la pared (Bo) de `ocupantes.md`.

## 3. La pared general y el nodo mínimo

**Definición (nodos).** Llámese **nodo** a todo aro de radio ≥ 1 (= r_m) que
sea ocupante de `v` distinto de `α` **y de m**, o esté anidado — a
cualquier profundidad — dentro de uno. Por hipótesis `j ≥ 1`, hay al menos
un nodo, y m nunca es nodo ni aparece dentro de uno (los nodos y sus
descendientes viven fuera de m). [La exclusión explícita de m es un matiz
de la verificación adversaria: sin ella, `y* = m` rompería el paso 3 del
Teorema B y duplicaría masa en la rama B de B″.]

**Pared Bo″.** Bloqueo ⟹ para todo nodo `y`: `y < σ₂ + ω + X_y`.

*Demostración.* Si no, `Σ hijos(y) ≤ (y−ω) − σ₂`; nótese que entonces cada
hijo de `y` tiene radio ≤ (y−ω) − σ₂ < y − ω... y σ₂ ≤ 1 podría no ser la
pieza mayor del conjunto `{σ₂} ∪ hijos(y)` solo si algún hijo supera σ₂;
en ese caso aplíquese el Lema R con ese hijo como pieza mayor σ′ y el resto
(incluida σ₂) como C: `Σ C = X_y − σ′ + σ₂ ≤ (y−ω) − σ′` equivale a la misma
desigualdad. En ambos casos el Lema R empaqueta `{σ₂} ∪ hijos(y)` en el
agujero de `y` (posiciones re-elegibles, §1), y con `σ₁ → D_m` el
intercambio queda desbloqueado. ∎

**El nodo mínimo.** Sea `y*` un nodo de radio mínimo. Sus hijos son todos
`< 1`: un hijo de radio ≥ 1 sería un nodo estrictamente menor que `y*`
(anidar exige radio ≤ y* − ω < y*). En particular `X_{y*}` es una suma de
aros menores que m, que viven en la cola de m.

## 4. Teorema B: las dos colas

**Teorema B.** Bloqueo en la plantilla (agujeros ocupados arbitrarios,
`m` sin hijos, `j ≥ 1`) ⟹

    ρ  >  Ψ(ω) = (1 − ω) + √((1 − ω)² + 1) .

*Demostración.* Sea `y*` el nodo mínimo, `X := X_{y*}` y `σ := σ₂`
(variable; por (B2), con H_m libre, `σ = σ₂ > 1 − ω`). Tres hechos:

1. `σ₁ ≥ σ₂ = σ`.
2. (cola de m) los hijos de `y*` son < 1 y distintos de σ₁, σ₂:
   `ρ ≥ σ₁ + σ₂ + X ≥ 2σ + X`.
3. (cola de `y*` y Bo″) la cola de `y*` contiene a `{m, σ₁, σ₂} ∪ hijos(y*)`
   (todos ≤ y*; empates por la convención de la primera copia) y
   `y* < σ₂ + ω + X = σ + ω + X`:
   `ρ ≥ (1 + σ₁ + σ₂ + X)/y* > (1 + 2σ + X)/(σ + ω + X)`.

Luego `ρ > F(σ, X) := máx(2σ + X, (1 + 2σ + X)/(σ + ω + X))` en el punto
`(σ₂, X)` de la instancia, y basta minimizar `F` sobre `σ ≥ 1 − ω`,
`X ≥ 0`. Para σ fijo, el primer término crece en X y el
segundo decrece (su derivada tiene el signo de `(σ+ω+X) − (1+2σ+X) =
ω − σ − 1 < 0`); en `X = 0` domina el segundo (equivale a
`2σ² + 2σω − 2σ − 1 ≤ 0`, cierto para σ ≤ 1, ω ≤ 1/2), así que el mínimo en
X está en el cruce `u := 2σ + X` con

    u (u + ω − σ) = 1 + u   ⟺   u² − (1 + σ − ω) u − 1 = 0
    ⟹  u(σ) = [ (1+σ−ω) + √((1+σ−ω)² + 4) ] / 2 ,

creciente en σ (`u′ = [1 + (1+σ−ω)/√((1+σ−ω)²+4)]/2 > 0`). El mínimo del
programa está por tanto en `σ = 1 − ω`:

    ρ > u(1−ω) = (1−ω) + √((1−ω)² + 1) = Ψ(ω) .   ∎

(El paso `y* ≤ σ₂ + ω + X` se usó con `y*` en su tope; la restricción
`y* ≥ 1` es consistente: en el óptimo `y* = 1 + X`. Todas las desigualdades
de las paredes son estrictas.)

**Corolario B1 (cruces).** `Ψ(0) = 1 + √2 = 2.4142…`; `Ψ(1/4) = 2` exacto;
y

    Ψ(ω) > T   ⟺   ω < ω₆ = (T−1)²/2 = 0.3522011… ,

donde la raíz de `Ψ = T` es `(T(2−T)+1)/(2T)`, igual a `(T−1)²/2` módulo
`T³ = T²+T+1` (verificado en simbólico). Además `Ψ(ω) < 3/(1+ω)`
**estricta y para todo ω ≥ 0** (se reduce a `5ω² − 2ω + 2 > 0`,
discriminante −36; afilado por el verificador): el caso de agujeros libres
(`X = 0`, `ocupantes.md`) satisface la cota más fuerte; la cota del árbol
general es Ψ. La evidencia numérica de `universal.py` [E] (mejor
bloqueo-proxy `ρ = 2.5617` en caja ω ≤ 0.25) queda por encima de ambas,
como debe.

**Observación (nota de minimalidad y afinado).** El argumento del nodo
mínimo usa `radio del hijo ≤ y − ω < y`, que degenera en ω = 0; el programa
siempre tiene ω > 0. Y Ψ no es el ínfimo del programa completo: añadiendo
(B4) y la cola de α (`α < 1 + ω + σ₂`) sale
`ρ ≥ (y* + 1 + σ₁ + σ₂ + X)/(1 + ω + σ₂)` ≈ Ψ + 0.05 en ω = 0.05
(cuantificado por el verificador; explica las holguras del bloque [D]).
No se necesita para `> T`.

## 5. «m con hijos»: la dicotomía de evacuación y el Teorema B″

[Historia: la primera versión de esta sección afirmaba que sin «m sin
hijos» la combinatoria se fugaba; la verificación adversaria la REFUTÓ (la
supuesta familia de la fuga no estaba bloqueada, y la dicotomía enunciada
olvidaba colocar a σ₁) y conjeturó lo contrario. La conjetura es ahora el
Teorema B″.]

Si m tiene hijos, H_m no está libre y la pared (B2) se debilita. La
herramienta correcta es la **evacuación a D_m** (Lema 0): colóquense σ₁ y
todos los hijos de m **en fila dentro de D_m** (posible si
`σ₁ + Σ hijos(m) ≤ 1`; los hijos de σ₁ viajan dentro de σ₁) y σ₂ en el H_m
vaciado (posible si `σ₂ ≤ 1 − ω`). Contrapositiva, con `M := Σ hijos(m)`:

    bloqueo  ⟹  σ₂ > 1 − ω   ∨   σ₁ + M > 1 .

**Teorema B″ (m con hijos).** La conclusión del Teorema B vale sin la
hipótesis «m sin hijos»: bloqueo en la plantilla (agujeros ocupados
arbitrarios en todos los niveles, incluido H_m) ⟹ `ρ > Ψ(ω)`.

*Demostración.* Rama A (`σ₂ > 1 − ω`): la prueba del Teorema B aplica
literalmente — solo usaba `σ₂ > 1 − ω`, la pared Bo″ y las dos colas, y la
masa `M ≥ 0` solo puede engordarlas. Rama B (`σ₂ ≤ 1 − ω` y `σ₁ + M > 1`):
sea `y*` el nodo mínimo, `X := X_{y*}` y `s := σ₂ + X`. Por Bo″ y
`y* ≥ 1`: `s > 1 − ω`. Sea `A := σ₁ + σ₂ + M + X`; por la rama B,
`A > 1 + σ₂ + X = 1 + s`. Las dos colas (la de m contiene a
`{σ₁, σ₂} ∪ hijos(m) ∪ hijos(y*)`; la de `y*` añade a m):

    ρ ≥ A > 1 + s      y      ρ ≥ (1 + A)/y* > (2 + s)/(s + ω) = 1 + (2 − ω)/(s + ω) ,

y minimizando `máx(1 + s, 1 + (2−ω)/(s+ω))` sobre `s > 1 − ω` sale el
cruce `s² + sω = 2 − ω`, es decir `ρ > Ψ_B(ω)` con `u = 1 + s` raíz
positiva de

    u² − (2 − ω)·u − 1 = 0 ,      Ψ_B(ω) = [ (2−ω) + √((2−ω)² + 4) ] / 2 .

Ahora bien, `Ψ(ω)` es la raíz positiva de `u² − 2(1−ω)·u − 1 = 0` (la misma
familia con `b = 2(1−ω)` en vez de `b = 2 − ω`), y la raíz positiva de
`u² − bu − 1` es creciente en b: como `2 − ω ≥ 2(1−ω)`,

    Ψ_B(ω) ≥ Ψ(ω)      (igualdad solo en ω = 0) ,

y la rama B queda dominada por la A. ∎

**Observación (números metálicos).** Ψ y Ψ_B son medias metálicas — raíces
de `u² − bu − 1` —, y `Ψ(0) = Ψ_B(0) = 1 + √2` es la **razón de plata**: al
oro de la meseta de ρ*₃ y al Tribonacci del umbral se les une la plata en
el suelo de los agujeros ocupados. Y el cruce de la rama B con T tiene la
misma estética que el de la A:

    Ψ_B(ω) > T   ⟺   ω < (T − 1)²  = 0.7044022…  = 2·ω₆

(y aquí la identidad es aún mejor que «módulo la cúbica»:
`(T−1)²·T − (2T − T² + 1) = T³ − T² − T − 1` **es exactamente el polinomio
de Tribonacci**, como identidad polinómica — hallazgo de la verificación):
el umbral de la rama B es el **cuadrado** (T−1)², el doble del `(T−1)²/2`
de la rama A.

**Corolario B2 (la canónica tampoco necesita la hipótesis).** En la
plantilla canónica (`j = 0`) con m con hijos: rama A ⟹ la curva `T_can(ω)`
entera (su programa solo usa `σ₂ > 1−ω` como desigualdad); rama B ⟹ la
rama del testigo `S ≥ Φ(ω)` vale porque la Proposición 4 de
`grosor_positivo.md` no usa (B2) — solo (B1) y (W), intactas. En ambas
ramas `ρ > Φ(ω)`, y `Φ(ω) > T` para todo ω > 0 (Φ(0) = T y Φ es
estrictamente creciente; el modelo vive en ω > 0).

Ejemplo bloqueado genuino con H_m ocupado (verificador): `ω = 0.1`,
`σ₁ = 0.9`, `σ₂ = 0.81`, hijo de m `0.85`, `o₁ = 1` con hijo `0.81`,
`α = 1.81` — contenedores par-ajustados y tres piezas ≥ 0.81 no caben en
D_m (el trío de iguales en disco unidad exige radio ≤ 2√3 − 3 = 0.464):
ρ = 4.37 ≫ Ψ, coherente con el teorema.

## 6. Estado de la Batalla 1 tras este paso

| plantilla | resultado | dónde |
|---|---|---|
| canónica (j = 0) | ρ ≥ T_can(ω) ≥ máx(2(1−ω), Φ(ω)) > T ∀ω | `grosor_positivo.md`, `esquina.md` |
| canónica con m con hijos | ρ > Φ(ω) > T ∀ω | Corolario B2 |
| ocupantes extra, agujeros libres | ρ > (j+2)/(1+ω) | `ocupantes.md` |
| ocupantes extra, agujeros ocupados (cualquier profundidad, H_m incluido) | ρ > Ψ(ω) > T para ω < (T−1)²/2 | Teoremas B y B″ |

Fuera de las plantillas quedan, apuntando a la rama geométrica del testigo
(Lema U₄ de `corona.md`): los ocupantes de `v` menores que m (aplastamiento
por pequeños), el tramo `ω ≥ (T−1)²/2` con `j ≥ 1`, y S con más de dos
piezas (que la combinatoria ρ*_k = ρ*₃ de `cuatro.md` acota por otro
lado).

## 7. Huecos declarados

1. ~~**`m` con hijos**~~ — **RESUELTO** (Teorema B″, §5): la rama
   `σ₁ + Σ hijos(m) > 1` da la media metálica `Ψ_B ≥ Ψ` y queda dominada.
   La conjetura del verificador de la ronda anterior, demostrada.
2. **Tramo `ω ≥ ω₆ = 0.3522` con ocupantes y agujeros ocupados**: la cota Ψ
   cae bajo T; misma herramienta pendiente. (En el caso de agujeros libres,
   `ocupantes.md` llega hasta 0.5874.)
3. **Ajuste**: Ψ es el ínfimo del programa relajado de tres restricciones
   (B2 + Bo″ + dos colas); el muestreo dirigido con las paredes completas
   queda por encima con holgura creciente en ω (`+0.08` en ω = 0.1, `+0.22`
   en ω = 0.3, bloque [D]): el ínfimo real de los bloqueos es mayor. No se
   necesita más para `> T`.
4. La cota usa `S` = par; los perfiles mayores heredan las paredes pero la
   optimización no está rehecha (la presión combinatoria de `cuatro.md`
   sugiere que solo mejora).

## Mapa de verificación

`code/bloqueadores.py`, seis bloques (6/6 OK):

- **[A]** simbólico: Ψ(1/4) = 2, Ψ(0) = 1+√2, la raíz de Ψ = T y su
  identidad con (T−1)²/2 módulo la cúbica, Ψ ≤ 3/(1+ω) en malla, la raíz
  positiva del cruce de la optimización y `du/dσ > 0`.
- **[B]** Lema R: 18 975 construcciones aleatorias verificadas con geometría
  directa (contención, disjunción, tangencia exacta del disco opuesto), 0
  fallos.
- **[C]** Teorema B: rejilla fina de la optimización ≥ Ψ en 4 valores de ω,
  y 11 083 instancias muestreadas con paredes en pie (árboles de profundidad
  1 y 2) todas con ρ > Ψ (margen mínimo +0.057).
- **[D]** medición de holgura: mínimos dirigidos 2.32/2.20/2.14 vs
  Ψ = 2.25/2.08/1.92 en ω = 0.1/0.2/0.3.
- **[E]** la dicotomía de evacuación corregida (colocación constructiva:
  σ₁ + hijos de m en fila en D_m y σ₂ en el H_m vaciado, validada con
  geometría directa), la identidad `5ω² − 2ω + 2 > 0` de la comparación
  estricta con 3/(1+ω), y la consistencia con `ocupantes.py`.
- **[F]** Teorema B″: las dos cuadráticas metálicas (Ψ y Ψ_B como raíces de
  `u² − bu − 1` con `b = 2(1−ω)` y `2−ω`), la monotonía de la raíz en b
  (Ψ_B ≥ Ψ), la identidad `(T−1)²·T = 2T − T² + 1` del umbral de la rama B,
  la rejilla de la optimización de la rama B, y el muestreo de instancias
  rama-B con paredes en pie (m con hijos): 0 violaciones de Ψ_B.
