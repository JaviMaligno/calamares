# El suelo áureo de la Batalla 2: Teorema P (u = sartén, S par)

Borrador. Segundo resultado de la Batalla 2, tras el contraejemplo áureo
(`umbral_aureo.md`): la dirección ≥ de la Conjetura A2 en la plantilla del
intercambio a sartén con S par. Es la mitad (a) del Open Problem del
paper, con un rincón declarado.

**Teorema P.** Bloqueo del intercambio a sartén (u = sartén; el testigo
tiene a m = 1 en v = agujero de un nodo y; S = {σ₁ ≥ σ₂} en la sartén;
j ≥ 1 ocupantes > 1 a nivel superior con ocupación anidada arbitraria;
m con hijos M arbitrarios) ⟹ `ρ > φ` en todos los casos siguientes:

| caso | cobertura | mecanismo |
|---|---|---|
| j = 1 | **toda ω** | dicotomía del punto fijo áureo |
| rama B (σ₁+M > 1), j ≥ 2 | **toda ω** | hoja estricta + `Ψ_B(1) = φ` |
| rama A, j ≥ 4 | **toda ω** | hojas estrictas, `Ψ₃(1) = √3 > φ` |
| rama A, j = 3 | y no hoja: toda ω; y hoja: ω < φ/2 | `Ψ₃` / `Ψ₂(φ/2) = φ` |
| rama A, j = 2 | y no hoja: ω < φ/2; y hoja: ω < 1/2 | `Ψ₂` / `Ψ(1/2) = φ` |

Queda un **rincón declarado**: {j ∈ {2, 3}, rama A, ω por encima de los
umbrales}, parcialmente cubierto por el Lema Z (abajo) y con evidencia
numérica mín ρ ≥ φ + 0.41 (bloque [D] y el generador del acta). El
ínfimo global de la plantilla
es exactamente φ: la familia áurea (Teorema A1) lo realiza dentro del
caso j = 1. Verificación: `code/batalla2.py` (5 bloques). Numeración
local: Teorema P, Lema Z.

## 1. Marco

Sartén de radio R con ocupantes O = {o₁ ≥ … ≥ o_j} (> 1, nivel superior,
compartidos por F y P), con nodos anidados y pequeños en los agujeros;
y = portador de m según P (nodo con 1 + X_y^resto ≤ y − ω); S en la
sartén según P; el intercambio manda m a la sartén y debe reinsertar S.
Recursos: **D_m** (disco libre de radio 1 en el agujero de y), **H_m**
(capacidad 1−ω, viaja con m; masa M evacuable a D_m), **agujeros de
nodos** (tarifa del Lema R), **anidamiento en S**, **re-empaquetado de la
sartén**. Necesidades de la plantilla: los pares de la sartén de F
(`{O, m}`) dan `o_i + 1 ≤ R` y `o_i + o_k ≤ R`.

Paredes generales del bloqueo (todas contrapositivas de colocaciones con
criterios exactos o filas):

    (D)    σ₁ + σ₂ > 1                        [fila en D_m]
    (evac) σ₂ > 1−ω  ∨  σ₁ + M > 1           [dicotomía de evacuación]
    (Ry)   σ₁ + σ₂ + X_y^resto > y − ω       [ambas al agujero de y, Lema R]
    (Bo)   z < σ₂ + ω + X_z                   [todo nodo z con agujero ≠ y]
    (G)    {O, m, σᵢ} no re-empaqueta en la sartén (la otra σ → D_m)

## 2. El caso j = 1: la dicotomía del punto fijo (toda ω)

*Demostración.* La pared (G) para cada σᵢ: el re-empaquetado «σᵢ a la
sartén, la otra a D_m, todo lo anidado viaja» exige empaquetar los
círculos `{o₁, m, σᵢ}` en el disco R; su fallo, con la antitonía en R y
`R ≥ o₁ + 1`, da la no-empaquetabilidad en el disco `o₁ + 1`, donde el
par `{o₁, 1}` es diametralmente rígido: por la necesidad exacta de la
Proposición S5 (reescalada),

    σ₁ , σ₂  >  b₂(o₁, 1) = b(o₁)

(basta el fallo de (G) con σ₂ y σ₁ ≥ σ₂, matiz cosmético del acta).

Las dos colas: `ρ ≥ σ₁ + σ₂ > 2b(o₁)` (cola de m) y
`ρ ≥ (1 + σ₁ + σ₂)/o₁ > (1 + 2b(o₁))/o₁ =: g(o₁)` (cola de o₁, que
contiene a m y a S). Con `b` estrictamente creciente y `g` estrictamente
decreciente (certificado polinómico:
`(3A² + 3A + 1)(A² + A + 1) − 2A(2A + 1)` tiene todos los coeficientes
positivos), el mínimo de `máx(2b, g)` está en el cruce
`2b(A)·A = 1 + 2b(A)`, cuya única raíz positiva es `A = φ`
(`2b(φ) = φ` y `g(φ) = (1+φ)/φ = φ`): `ρ > φ`. ∎

Nótese qué NO se usa: ni H_m, ni la evacuación, ni las hojas — el caso
j = 1 es puramente el bolsillo, y es donde vive la familia áurea (con
o₁ = φ exacto).

## 3. Rama B (σ₁ + M > 1): la hoja estricta y Ψ_B(1) = φ

**Hoja estricta**: una hoja (nodo sin hijos-nodo) cuyo agujero no es el
de y. Con j ≥ 2 siempre existe (cualquier subárbol de ocupante que no
contenga a y tiene una hoja, y los subárboles son disjuntos).

*Demostración (j ≥ 2, rama B).* Sea L′ la hoja estricta mayor y
`s := σ₂ + X_{L′}`. Por (Bo) en L′ y `L′ ≥ 1`: `s > L′ − ω ≥ 1 − ω`. La
cola de L′ contiene a `{m, σ₁, σ₂, M} ∪ hijos(L′)` (todos ≤ L′; M y
X_{L′} disjuntos): con σ₁ + M > 1,

    ρ·L′ ≥ 1 + σ₁ + σ₂ + M + X_{L′} > 2 + s ,      L′ < s + ω ,

y la cola de m da `ρ ≥ σ₁ + M + σ₂ + X_{L′} > 1 + s`. Es exactamente el
programa de la rama B del Teorema B″: `ρ > Ψ_B(ω)`, la raíz de
`u² − (2−ω)u − 1`. Y la identidad nueva:

    Ψ_B(1) = (1 + √5)/2 = φ      (exacta) ,

con Ψ_B estrictamente decreciente: `ρ > Ψ_B(ω) > φ` para **todo**
ω < 1. ∎ (La cuarta media metálica del programa que degenera en oro.
Matiz del acta: como S ⊂ (ω, 1), la rama B con σ₂ ≤ 1−ω y σ₂ > ω es
vacía para ω ≥ 1/2, así que en la región poblada
Ψ_B(ω) > Ψ_B(1/2) = 2: la identidad Ψ_B(1) = φ es el cierre estético
del programa, no una frontera activa — el margen real es ≥ 2 − φ.)

## 4. Rama A (σ₂ > 1−ω): hojas estrictas y la escalera Ψ

Sea `jj` = número de hojas estrictas garantizadas: `jj = j` si y no es
hoja (todos los subárboles aportan hojas estrictas), `jj = j − 1` si y es
hoja. La mayor hoja estricta L tiene el programa del lema de las hojas
con bono jj: `ρ·L ≥ (jj−1) + 1 + σ₁ + σ₂ + W` y `L < σ₂ + ω + W`, cuya
optimización en la rama A es `Ψ_jj(ω)`. Los cruces con φ son exactos:

    Ψ₁(1/2) = φ ,     Ψ₂(φ/2) = φ ,     Ψ₃(1) = √3 > φ :

j ≥ 4 (o jj ≥ 3): toda ω; jj = 2: ω < φ/2 = 0.809; jj = 1: ω < 1/2. ∎

## 5. El Lema Z y el rincón declarado

**Lema Z (j = 2).** Bloqueo ⟹ en R,

    f(1)·[f(o₁) + f(o₂)] > 1 ,      f(x) = x/(R − x) ,

y en consecuencia (evaluando en R = o₁ + o₂ por antitonía en R):
`o₂ < 1 + 1/o₁`.

*Demostración.* (G) da la no-corona de `{o₁, o₂, m, σ₂}` (necesidad:
no-pack ⟹ no-corona). Por el Lema U₄, falla el trío top
`{o₁, o₂, m}` o falla el zigzag; **ambas ramas** implican
`θ(o₁,1) + θ(o₂,1) > π` (el trío top porque `θ(o₁,o₂) ≤ π`; el zigzag
por monotonía `θ(oᵢ,σ) ≤ θ(oᵢ,1)`). Con `A = θ(o₁,1)/2 ≤ π/2` (de
`R ≥ o₁+1`) y `B = θ(o₂,1)/2 ≤ π/2`: `sin²A + sin²B > 1`, que es la
desigualdad del enunciado (el truco del Teorema T3). Es decreciente en R
y en `R = o₁+o₂`: `o₁/o₂ + o₂/o₁ > o₁ + o₂ − 1`, cuyo miembro izquierdo
es decreciente en o₂ sobre [1, o₁] con máximo `o₁ + 1/o₁`:
`o₂ < 1 + 1/o₁`. ∎

**El rincón.** En {j = 2, rama A, ω ≥ 1/2 ∨ φ/2} el Lema Z y la cola de
o₁ (`ρ > (o₂ + 2)/o₁ ≥ 3/o₁` por (D) y `o₂ ≥ 1`) dan `ρ > φ` si
`o₁ ≤ 3/φ = 1.854`; queda el sliver `o₁ > 3/φ ∧ o₂ < 1 + 1/o₁ < 1.54`
(y su análogo j = 3, y hoja, ω ≥ φ/2), con evidencia numérica sobre el
programa completo: mín ρ ≥ φ + 0.41 (j = 2, generador propio del
verificador con profundidad 4) y ≥ φ + 0.62 (j = 3, bloque [D] con el
generador corregido). Declarado.

## 6. Lectura

- **El ínfimo de la plantilla es φ** (Teorema P + familia áurea): la
  dirección ≥ de la Conjetura A2 queda demostrada en la plantilla S par
  salvo el sliver, y la ≤ está realizada. Las medias metálicas del
  programa degeneran TODAS en oro en los bordes: Ψ(1/2) = φ,
  Ψ₂(φ/2) = φ, Ψ_B(1) = φ, y el punto fijo del bolsillo es φ.
- Para la conjetura completa faltan: el sliver, |S| ≥ 3 en la sartén,
  pequeños extra (Corolario-S-análogo), y el ensamblaje del lema
  universal con el umbral corregido.

## 7. Huecos declarados

1. **El sliver** {j ∈ {2,3}, rama A, ω grande, o₁ > 3/φ, o₂ < 1+1/o₁}:
   la geometría fina de la sartén con dos ocupantes (el análogo del
   «lema del hueco»); evidencia ≥ φ + 0.41 (j=2) y ≥ φ + 0.62 (j=3).
2. **|S| ≥ 3**: las paredes se heredan (fila en D_m, evacuación, Lema R)
   pero la optimización no está rehecha; la reducción del Teorema T3
   (polvo sobre el par) porta la rama de anidamiento.
3. **Pequeños extra en la sartén**: análogo del Corolario S pendiente
   (las colocaciones de las paredes son locales salvo (G)).
4. El generador de [B]–[D] muestrea árboles de profundidad ≤ 2 y NO
   impone la pared (G) cuando el conjunto tiene ≥ 5 círculos (sin
   criterio de corona cerrado): superset sano de los bloqueos. [La
   primera versión devolvía «corona existe» para k ≥ 5 y vaciaba la
   evidencia j = 3 — hallazgo del acta, corregido; el verificador repuso
   la evidencia con un generador propio de profundidad 4.]

## Mapa de verificación

`code/batalla2.py`, cinco bloques: **[A]** identidades exactas en sympy
(2b(φ) = φ; g(φ) = φ; el certificado de coeficientes de g′ < 0;
Ψ(1/2) = φ; **Ψ_B(1) = φ**; Ψ₂(φ/2) = φ; Ψ₃(1) = √3; la monotonía de la
pared Z y `dq/do₂ ≤ 0`); **[B]** j = 1: muestreo del programa con la
cadena del teorema verificada instancia a instancia (ambas σ > b(o₁),
ρ > máx(2b, g) ≥ φ), 0 fallos; **[C]** j ≥ 2: cadenas de la rama B
(ρ > Ψ_B > φ) y de la rama A cubierta (ρ > Ψ_jj en su ventana), 0
fallos; **[D]** el rincón: mín ρ ≥ φ + 0.1 en {j ∈ {2,3},
ω ∈ {0.85, 0.95}, rama A}; **[E]** consistencia con la familia áurea
(paredes en pie, ρ = φ + 3ε) y el mínimo del programa j = 1 = φ.
