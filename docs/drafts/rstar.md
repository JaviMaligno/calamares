# El cierre de la región R* (Teorema DPr)

Estado: **cerrado salvo una celda** — C2, C3 y C4 enteras y C1 con
j ≤ 2 probadas; la celda {p ≥ 4, σ₁+M ≤ 1, j ≥ 3} queda declarada
abierta con la vía identificada. Acta REFUTADO→REPARADO (2026-08-06)
en VEREDICTOS.md; enunciado en el paper (thm:DPr).
Script: `code/rstar.py` (6/6; bloques [A] identidades exactas en
sympy, [A2] frontera de j = 2, [B] pinza-con-Σ y cadenas, [C] pared de
corona de C3.3, [D] celdas p ≥ 4, [E] controles negativos).

Notación: la de `perfilp.md` (S = {σ₁ ≥ … ≥ σ_p} < 1, W := Σ_{i≥3} σᵢ,
Σ := σ₁+σ₂+W, M := Σ hijos(m)), más s' := σ₂+…+σ_p+ω (la fila de
(Bo)-fila con p piezas) y las celdas C1–C4 de `perfilp.md` §2:

    C1 = { p ≥ 4, σ₁+M ≤ 1 }
    C2 = { p ≥ 4, σ₁+M > 1, j = 1, subárbol de o₁ = cadena hasta y }
    C3 = { p = 3, j = 2, σ₁+M ≤ 1, σ₂ > 1−ω, σ₃ > 1−ω }
    C4 = { p = 3, j ≥ 3, σ₁+M ≤ 1 }

todas dentro de {pesado σ₁+W > 1, no-anida W+X_{σ₁} > σ₁−ω,
σ₂ ≤ φ−1}.

## 0. Enunciado

**Teorema DPr.** En la región pesada no-anidable del Teorema DP-p, el
bloqueo del intercambio a sartén implica ρ > φ en cada una de: (i)
C4 = {p = 3, j ≥ 3}; (ii) C3 = {p = 3, j = 2} (tres ramas); (iii) C1 y
C2 con j = 1 (coronas murales); (iv) C1 con j = 2 (frontera π). Queda
abierta del intercambio a sartén una única celda:

    { p ≥ 4,  σ₁+M ≤ 1,  j ≥ 3 }

más los pequeños extra y el régimen de pivote sólido ω ≥ 1 con j ≥ 3.

## 1. El instrumento común: el criterio de camino más largo

**Colocación mural.** Círculos a₀, a₁, …, a_k, a_{k+1} tangentes a la
pared de un disco R̄, con el par {a₀, a_{k+1}} diametral (su propia
separación es exactamente π por el otro lado, así que solo hay que
llenar media circunferencia). Colocarlos en ángulos
0 = t₀ ≤ t₁ ≤ … ≤ t_k ≤ t_{k+1} = π con TODAS las parejas disjuntas es
un sistema de restricciones de diferencias: t_j − t_i ≥ θ(a_i, a_j)
para todo i < j (θ dado por la identidad del medio ángulo
sin²(θ/2) = f(a)f(b), Prop. S1/S5). Por la dualidad estándar de los
sistemas de diferencias (scheduling / camino crítico), el sistema es
factible ⟺ el **camino más largo** de a₀ a a_{k+1} sobre subsecuencias

    máx_{S ⊆ {1..k}}  Σ_{consecutivos en a₀, S, a_{k+1}} θ(a_i, a_j)

es ≤ π. Para desbloquear basta UN orden de los intermedios con camino
más largo ≤ π; el bloqueo exige que TODOS los órdenes fallen.

**El pentagrama.** El criterio ingenuo — sumar solo los arcos
adyacentes ≤ π — es una relajación (solo impone las parejas
consecutivas) y es INSUFICIENTE: con 5 círculos hay configuraciones
donde los arcos adyacentes suman < π pero una pareja no adyacente se
solapa (el mismo fenómeno que el certificado del «pentagrama» del
Teorema C7 de `corona.md`). El fallo fue detectado y corregido por el
hilo principal ANTES de la ronda adversaria; la ronda **confirmó la
suficiencia constructivamente**: 3 071 colocaciones murales
construidas con el criterio y contrastadas con distancias euclidianas,
0 inválidas. (Colateral de la misma ronda: `corona_cabe` de
`perfilp.py` usaba el criterio ingenuo; portado y re-ejecutado, 5/5.)

## 2. Palanca 1 — la pinza-con-Σ (cierra C4)

El árbol de casos de j = 3 del par (Teorema DP(iv) / Teorema M) porta
a p = 3 con dos sustituciones: la fila de (Bo)-fila es
s' = σ₂+σ₃+ω (en vez del s = σ₂+ω del par) y TODAS las colas llevan la
masa Σ del perfil (en vez de S₀). Sobre v* — el nodo más pequeño del
subárbol de o₁ cuya cola contiene a o₂ y o₃ — la cadena da:

    [C1']  cola de v*        ⟹  o₂ < (φ−1)v* − 2 − Σ + s'
    [C2']  o₂ ≥ 3/φ          ⟹  v* > φ(3/φ + 2 + Σ − s')
    [C3']  hijo-nodo w ≤ o₂ + polvo < φ−1
                             ⟹  o₂ > v* − s' − (φ−1)
    [C4']  = C1' + C3'       ⟹  v* < φ²(2s' + φ − 3 − Σ)

C2' y C4' son incompatibles (pinza) sii

    s' ≤ (φ−1)Σ + (16 − 9φ)      [frontera exacta, sympy]

y esto vale en TODA la celda: el sup del dominio de s' − (φ−1)Σ es
5φ − 7 (en ω → 1, σ₂ = σ₃ = σ₁ = φ−1), y el margen es exactamente

    (16 − 9φ) − (5φ − 7) = 23 − 14φ = 16 − 7√5 = 0.3475 > 0.

Consistencia: en Σ = 1 la frontera degenera EXACTAMENTE en
11 − 4√5 = 15 − 8φ, la constante s* del Teorema M — la pinza-con-Σ es
su generalización estricta, y el control negativo [E](b) muestra que
SIN Σ la pinza no cierra C4 (s' alcanza 2.226 > s*). Rama sin
hijo-nodo: v* < s' + φ − 1 contra C2', frontera
s' = (φ−1)Σ + (7−3φ), margen 14 − 8φ = 1.0557. Las demás ramas del
árbol: caso 1 (o₂ < 3/φ): cola de o₂ da (2+Σ)φ/3 > φ ⟺ Σ > 1, y
pesado da Σ > 1+σ₂ estricta; caso 2 (o₂ ≥ 3/φ, o₁ < 3):
(3/φ+2+Σ)/3 > φ ⟺ Σ > 1 (identidad exacta); rama y = o₁ con polvo
(Ry_p): ρ ≥ Σ + X₁ > o₁ − ω ≥ 2 > φ; rama (a) (polvo D ≥ φ−1): cola de
m da ρ ≥ Σ + D > φ; rama (b) (dos hijos-nodo ⟹ jj = 3): programa
máx(σ₁+u, (3+σ₁+u)/(u+ω)) con **mínimo real 2.000363 > φ** (el 2.0058
del barrido era artefacto de malla; multistart de la ronda).

## 3. Palanca 2 — las tres ramas de C3 (cierra C3)

- **C3.1 (σ₂+σ₃ ≤ 1):** resucita la pared de bolsillos espejo del caso
  (ii) del par (o₂ < Ā(o₁)) con las colas engordadas 1+Σ > 2+σ₂. El
  mín-máx de máx((o₂+2)/o₁, 2/o₂) sobre la pared b₂(o₁,o₂) < 1 es
  ≥ φ: el ínfimo es exactamente φ, alcanzado solo en el **rincón
  áureo** (o₁, o₂) = (2, √5−1) — donde b₂(2, √5−1) = 1 exacto y
  2/(√5−1) = φ — que queda FUERA de la pared; estricto además porque
  las colas llevan 1+Σ > 2+σ₂ > 2.
- **C3.2 (σ₂+σ₃ > 1, ω ≤ 1/2):** con q := σ₂+σ₃+X, la cola de m
  (ρ > q+1−ω, usando σ₁ ≥ σ₂ > 1−ω) y el programa de la hoja estricta
  (ρ > (2+q−ω)/(q+ω); la hoja existe porque j = 2) dan
  ρ > máx(q+1−ω, (2+q−ω)/(q+ω)) sobre q > 2(1−ω). El cruce es
  **interior**: q* = √(1+(1−ω)²), factible sii ω ≥ 1 − 1/√3 = 0.4226,
  con valor Ψ(ω) = √(1+(1−ω)²) + (1−ω), decreciente, y
  **Ψ(1/2) = φ EXACTO**; para ω < 1 − 1/√3 manda la esquina
  3(1−ω) ≥ √3 > φ, con empalme continuo en √3.
- **C3.3 (ω > 1/2): la celda es VACÍA de bloqueos.** Las colas de un
  hipotético bloqueo con ρ ≤ φ fuerzan o₂ ≥ (1+Σ)/φ y
  o₁ ≥ (o₂+1+Σ)/φ; sobre ese dominio la colocación mural de
  {o₂, m, σ₂, σ₃, o₁} en el disco o₁+o₂ (par {o₁,o₂} diametral:
  f(o₁)f(o₂) = 1 exacto en R̄ = o₁+o₂) SIEMPRE cabe: el máximo del
  mín-sobre-órdenes del camino más largo es 2.6476 < π (margen
  0.4940), con el máximo en la frontera de las colas y la esquina
  o₁ → ∞ controlada por el límite exacto 2 asin √(1/o₂) ≤ 1.71 < π.
  Barrido ≥ 2.6·10⁶ puntos + refinamiento local. El control negativo
  [E](c) — Ψ(0.6) = 1.477 < φ — muestra que el programa de C3.2 NO
  cubre ω > 1/2: la pared de corona no es opcional.

## 4. Palanca 3 — coronas j = 1 (cierra C2 y C1 con j = 1)

Con un solo ocupante la corona mural pone σ₂…σ_p entre m y o₁ con
θ(o₁, m) = π (el par {o₁, m} hace de extremos). Máximos del
mín-sobre-órdenes, todos < π con margen: C1 p = 4/5/6: 2.6014 / 2.5182
/ 2.3115 (márgenes 0.54 / 0.62 / 0.83); residuo de C2 p = 4/5/6:
2.4413 / 2.4426 / 2.2855 (márgenes 0.70 / 0.70 / 0.86). Antes de la
corona, las cadenas ya cierran una parte: en C1, la rama
W₂ := Σ_{i≥4} σᵢ > 1−ω da ρ ≥ Σ > σ₁+σ₂+σ₃+(1−ω), que cierra sii
σ₁+σ₂+σ₃ ≥ φ−1+ω (frontera plana); en C2, la cadena
ρ ≥ Σ+M > 1+σ₂+W (usa σ₁+M > 1) cierra sii σ₂+W ≥ φ−1, y el residuo
(piezas diminutas con pivote σ₁ grande: σ₁ > 2−φ+σ₂) cae por la
corona. C2 es j = 1 por definición de la celda: queda CERRADA entera.

## 5. Palanca 4 — la frontera π de j = 2 (cierra C1 con j = 2)

Con j = 2 la corona extendida pone {m, σ₂…σ_p} entre o₂ y o₁ en el
disco o₁+o₂. La malla daba márgenes 0.038–0.042 — **artefacto**: el
sup real del camino más largo sobre el dominio CERRADO es **π
EXACTO**, alcanzado solo en la esquina de frontera {σ₁ = 1, W = 0}
(Σ = 1), donde las colas dan o₂ = 2/φ, o₁ = 2, R̄ = 2φ y valen las
identidades exactas (bloque [A2], sympy):

    f(o₁)f(o₂) = 1                        [par diametral exacto]
    sin²(θ(o₂,m)/2) = 1/2 − √5/10
    sin²(θ(m,o₁)/2)  = 1/2 + √5/10        [suman 1 ⟹ θ+θ' = π]

La esquina está EXCLUIDA del dominio: exige σ₁ = 1 (las piezas del
perfil son < 1 estricto) y W = 0 (pesado exige σ₁+W > 1). El interior
queda por tanto estrictamente bajo π y el cierre de j = 2 es **por
análisis de frontera, no por malla** (~10⁶ muestras interiores de la
ronda adversaria sin ningún punto ≥ π).

## 6. Por qué no prueba de más

- **La familia áurea (p = 2) no entra**: R* exige p ≥ 3, y su
  extensión con polvo cae en el caso (L) del Teorema DP-p, donde el
  suelo φ se realiza — consistente.
- **La pared de corona no es vacua** ([E](a)): sin las colas
  o₂ ≥ (1+Σ)/φ, o₁ ≥ (o₂+1+Σ)/φ el mín-sobre-órdenes alcanza
  5.46 > π; son las colas de ρ ≤ φ las que vacían la celda, no el
  criterio.
- **La Σ trabaja de verdad** ([E](b)): quitándola de las colas la
  frontera de la pinza vuelve al 11 − 4√5 del Teorema M y C4 NO
  cierra (s' alcanza 2.226 > s* = 2.0557; el mismo punto cierra con
  Σ: s' − (φ−1)Σ = 1.0802 < 16−9φ = 1.4377).
- **Cada palanca es necesaria** ([E](c)): el Ψ-programa de C3.2 no
  cubre ω > 1/2 (Ψ(0.6) = 1.477 < φ).

## 7. La celda superviviente y la vía identificada

**{p ≥ 4, σ₁+M ≤ 1, j ≥ 3} queda ABIERTA.** Diagnóstico de la ronda
(el punto REFUTADO): la corona extendida de la palanca 4 vive en el
disco o₁+o₂ y por tanto **no recoloca a o₃** — la contención al disco
de los dos mayores ocupantes no es una colocación legal cuando hay
tres o más, porque o₃ tiene que ir a alguna parte. La reparación
ingenua (insertar o₃ en la cadena mural) NO funciona: el camino más
largo da 4.86–4.93 ≫ π en toda la celda muestreada.

La vía identificada: **la corona cíclica a nivel de sartén.** En vez
de contener a los ocupantes en o₁+o₂, trabajar en la sartén completa
de radio R con la corona CÍCLICA (sin extremos diametrales, suma de la
vuelta entera ≤ 2π con todas las parejas separadas — el criterio de
`corona.md` con el certificado de camino más largo cíclico) de
O ∪ {m} ∪ {σ₂…σ_p}: el bloqueo fuerza R < R_corona(O ∪ {m}), o sea la
pared cuantitativa

    R ≥ R_corona(O ∪ {m})  ⟹  desbloqueo,

y las colas de los j ≥ 3 ocupantes contra esa pared deberían dar
ρ > φ. Evidencia a favor (heredada del DP-p): 0 bloqueos
supervivientes en los barridos dirigidos de la celda (bloque E de
`perfilp.py` y los ~2M de puntos MC + multistart de la ronda,
`audit1.py`/`audit2.py` del scratchpad del verificador). Los
«pequeños extra» del ensamblaje convergen a esta misma corona.
