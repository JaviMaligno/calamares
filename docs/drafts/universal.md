# La frontera universal: el toolkit para contenedores genéricos

Primer borrador del asalto al punto 1 de `reinsercion.md` §10 (contenedores
v/u genéricos, EL hueco de la conjetura del umbral de Tribonacci). Este
documento no cierra ese hueco: aporta el **toolkit geométrico** —la frontera
de bloqueo del trío en un disco de radio arbitrario, en forma lineal—, cierra
con él una extensión que estaba abierta (**Teorema S con holgura**,
`hoja_de_ruta.md` §1), y deja formuladas y exploradas las dos batallas que
quedan. Verificación: `code/universal.py`.

## 1. Lema U (la frontera universal)

Trío {A, x, y} tangente a la pared de un disco de radio R **arbitrario**
(sin la restricción R = A + B de `suelo_rigido.md` ni R = α + 1 de `h1.md`),
en el dominio interior A + x, A + y, x + y < R. Sea c := R − A y

    T_c(x) := √((c − x)/x) ,      τ_R := c/√(AR) .

**Lema U.** En el dominio interior, la suma angular cumple

    F = θ(A,x) + θ(A,y) + θ(x,y) ≥ 2π   ⟺   T_c(x) + T_c(y) ≤ τ_R .

*Demostración.* Idéntica a la del Lema F de `h1.md` §3 con una sola
generalización: el término cruzado. Con sin²(θ_{Az}/2) = f(A)f(z),
f(z) = z/(R−z), la identidad general (bloque A1 de `universal.py`)

    f(A) f(x) · (1 − f(A) f(y)) = [AR/(R−A)²] · [(c−y)/y] · f(x) f(y)

—que en `h1.md` requería R = α + 1 solo porque allí se evaluaba f(α) = α—
da sin(θ_{Ax}/2)cos(θ_{Ay}/2) = [√(AR)/(R−A)]·T_c(y)·√(f(x)f(y)), y sumando
el término simétrico, la ecuación F = 2π se convierte en
√(AR)(T_c(x)+T_c(y))/(R−A) = 1. La equivalencia (dirección ⟸, unicidad,
extremo diagonal) es el mismo argumento de monotonía de allí. ∎

El Lema U **unifica** las dos coordenadas del repo: con A = 1, c = t es el
ψ(x) = √((t−x)/x) y τ = t/√(1+t) del Lema S3 (que era la dirección ⟸,
suficiente); con A = α, c = 1 es la t(s) = √((1−s)/s) de `h1.md`. Y todos
los acompañantes son uniformes en R:

- **Bolsillo general.** En x = c (el compañero llena el hueco junto a A):

      b_R(A) = ARc/(AR + c²) ,

  que en R = A + B es exactamente la fórmula de Descartes
  AB(A+B)/(A² + AB + B²) de `resultados.md` §5bis — ahora válida con
  holgura. b_R(A) es creciente en R: **la holgura solo agranda el bolsillo**.
- **Pendiente.** κ = −dy/dx sobre la frontera = √(g_c(y)/g_c(x)) con
  g_c(s) = s³(c−s): la identidad de `h1.md`, uniforme en R (T_c es
  primitiva de −c/(2√g_c) y el factor c se cancela en el cociente).
- **G_c-lema.** Sobre el segmento T_c(x) + T_c(y) = τ_R el mínimo de x + y
  se alcanza empujando x al máximo permitido, con el mismo análisis de dos
  casos de `h1.md` §4; la condición del caso fácil τ_R ≤ 1/√3 es
  3c² ≤ AR, que en A = 1, R = 1 + t es t ≤ (1+√13)/6 — **la constante de
  concavidad del Lema S4**, que resulta ser el mismo umbral.
- **Invariancia de escala**: T_c y τ_R son homogéneos de grado 0: basta
  normalizar A = 1 (o m = 1) en todo lo que sigue.
- **Aviso de dominio.** Con holgura grande la frontera de infactibilidad
  puede cruzar por la rama del **par** (x + y > R, θ(x,y) = π) antes que por
  la angular; la forma lineal describe solo la rama angular. En los usos del
  programa (x, y ≤ 1 < A, R ≥ A + 1) la rama del par no aparece; con
  contenedores genéricos hay que comprobarlo caso a caso.

Como siempre, la dirección que los teoremas usan es la constructiva
(F ≤ 2π ⟹ empaqueta, Lema S2, válido para todo R): genuinamente
no-empaquetable ⟹ F > 2π ⟹ T_c(x) + T_c(y) < τ_R.

## 2. Teorema S con holgura

**Corolario U1 (Teorema S con holgura).** Sea una instancia de 4 aros con
sartén de radio R ≥ r₁ + r₂ tal que (F2) r₃ + r₄ ≤ r₁ − w y (F3') el trío
{r₁, r₃, r₄} no empaqueta en el disco R. Entonces ρ > T, y el ínfimo sigue
siendo T (alcanzado en el límite rígido R → r₁ + r₂).

*Demostración.* Un empaquetamiento en un disco es un empaquetamiento en
cualquier disco mayor (contención, centrándolos): la no-empaquetabilidad es
**decreciente en R**. Luego (F3') implica que {r₁, r₃, r₄} tampoco empaqueta
en el disco r₁ + r₂ ≤ R, y la instancia satisface (F2) + (F3) de la
subfamilia rígida F de `suelo_rigido.md` con el disco 1 + t: el Teorema S da
ρ > T tal cual (su prueba solo usa (F2) y (F3), no el valor real de la
sartén). La exactitud del ínfimo la da la propia Proposición S6 (la familia
aproximante tiene R = 1 + t, admisible aquí). ∎

Esto cierra la extensión «holgura R > r₁ + r₂ en el Teorema S» de
`hoja_de_ruta.md` §1 y §7. La lectura importante para el asalto: **la
holgura de la sartén nunca ayuda al bloqueo del trío** — el caso crítico es
siempre el rígido. Lo que la holgura sí cambia (y el Teorema S no cubre) es
el **conjunto de ocupantes**: con R > r₁ + r₂ caben más cosas junto a r₁, y
ahí empieza la batalla real.

## 3. Las dos batallas que quedan (formulación)

**Batalla 1 (v genérico, el hueco del mayor).** En el paso de intercambio, m
sale de v y S debe reinsertarse en v ∪ H_m ∪ anidamientos. La plantilla
canónica supone v = sartén con un único vecino grande α y da
T_can(ω) ≥ 13/7 (`drafts/esquina.md`). El caso genérico: v contiene
ocupantes O = {o₁ ≥ … ≥ o_j} ∪ {m} (los mayores que m coinciden en F y en
P). Bloqueo ⟹ {O, S} no empaqueta en v. La pregunta cuantitativa:

    ¿inf { ρ : bloqueo con v genérico } ≥ T ?

El mecanismo a favor: cada ocupante extra o_i añade presión de cola
(ρ ≥ (Σ_{menores})/o_i) además de estorbar; la conjetura fina es que la
plantilla canónica (un solo vecino, tangencia rígida) es **el v óptimo para
el adversario**. La pieza que falta es una cota inferior del mayor hueco de
un empaquetamiento en función de la capacidad libre («lema del hueco»); el
Lema U da el lenguaje para el caso «una corona de tangentes a pared» (los
arcos se suman y la infactibilidad de la corona es aditiva en T_c), pero el
caso de ocupantes interiores está abierto.

**Batalla 2 (u = sartén).** Si u (el contenedor de m según F) es la sartén,
la restricción del testigo no es una capacidad simple («S cabía en u») sino
la empaquetabilidad de S junto a los ocupantes mayores de u. El análogo de
(W) es entonces una condición de corona, que el Lema U vuelve a hacer lineal
en T_c. Sin explorar aún.

## 4. Exploración numérica (sin estatus)

`universal.py` [E] muestrea la Batalla 1 con **tres** ocupantes
{α, γ, m = 1} en la sartén (γ ∈ [1, α] el ocupante extra) y S = {u, v} par,
con las paredes del programa canónico y el bloqueo medido por el **proxy
angular de 4 círculos** (suma de arcos consecutivos ≥ 2π en el mejor orden;
para 4 círculos la tangencia a pared es solo un proxy — se declara como tal,
igual que las partes numéricas de `grosor_positivo.md` §4). Resultado del
muestreo (60 000 configuraciones, 321 bloqueos-proxy): el mejor bloqueo tiene
ρ = 2.5617, muy por encima de 13/7 = 1.8571 — el ocupante extra γ paga en la
cola de α ((γ + 1 + u + v)/α) más de lo que aporta estorbando. Es evidencia
(no prueba) a favor de la conjetura fina de la Batalla 1.

## 5. Huecos declarados

1. Este borrador **no** cierra el punto 1 de `reinsercion.md` §10; cierra el
   Lema U, sus corolarios y el Teorema S con holgura. Las Batallas 1 y 2
   quedan formuladas con evidencia exploratoria.
2. El proxy angular de 4 círculos de §4 no es un criterio exacto ni en
   dirección suficiente ni necesaria para ocupantes interiores; solo mapea
   el paisaje de bloqueos de corona.
3. La rama del par en holgura grande (aviso de dominio de §1) debe
   comprobarse en cada aplicación del Lema U fuera de la banda del programa.

## Mapa de verificación

`code/universal.py`, cinco bloques: **[A]** identidades en sympy exacto (el
término cruzado general A1 — la única pieza nueva respecto de `h1.py` —, el
bolsillo b_R(A) y su reducción a Descartes en R = A + B, la primitiva
T_c′ = −c/(2√g_c), κ uniforme en R, la condición 3c² ≤ AR con su reducción a
(1+√13)/6, y la invariancia de escala); **[B]** frontera lineal y κ contra
bisección angular en malla sobre (A, R) con holguras de 0 a 0.8 (≥ 300
puntos, rama del par excluida por dominio); **[C]** bolsillo general contra
bisección y crecimiento en R; **[D]** la cadena del Teorema S con holgura
(monotonía de F en R + instancias de F_hol: infactible en R ⟹ infactible en
1 + t ⟹ ρ > T); **[E]** la exploración de tres ocupantes (proxy declarado).
