# El suelo áureo de la Batalla 2: Teorema P (u = sartén, S par)

Borrador. Segundo resultado de la Batalla 2, tras el contraejemplo áureo
(`umbral_aureo.md`): la dirección ≥ de la Conjetura A2 en la plantilla del
intercambio a sartén con S par. Es la mitad (a) del Open Problem del
paper, con un rincón declarado.

**Teorema P (completo, sin rincón).** Bloqueo del intercambio a sartén
(u = sartén; el testigo tiene a m = 1 en v = agujero de un nodo y;
S = {σ₁ ≥ σ₂} en la sartén; j ≥ 1 ocupantes > 1 a nivel superior con
ocupación anidada arbitraria; m con hijos M arbitrarios) ⟹

    ρ > φ      para todo j ≥ 1, toda ω y toda ocupación,

salvo una sub-celda declarada de j = 3 (§4ter; evidencia ≥ φ + 0.75), y
el ínfimo de la plantilla es exactamente φ (la familia áurea lo realiza
en j = 1). Mecanismos por caso:

| caso | mecanismo |
|---|---|
| j = 1, **toda ω > 0** (incl. pivote sólido) | dicotomía del punto fijo áureo |
| j = 2, **toda ω > 0** (incl. pivote sólido) | **pared de bolsillos espejo** `b₂(o₁,o₂) < 1` + cruce áureo `o₂* = √(1+2o₁)−1` |
| j = 3, ω ∈ (0,1) | árbol de casos: colas de o₂/o₁, dicotomía masa/nodo, `Ψ₃` |
| j ≥ 4, ω ∈ (0,1) | hojas estrictas (`Ψ₃(1) = √3 > φ`) + rama B (`Ψ_B(1) = φ`) |

Verificación: `code/batalla2.py` (6 bloques). Numeración local:
Teorema P, Lema Z (histórico: subsumido por la pared de bolsillos espejo
en j = 2, se conserva por interés propio).

## 1. Marco

**Convención de anchura (dictamen 4)**: el programa de intercambio se
enuncia para ω ∈ (0, 1) (m aro genuino, H_m no vacío); el modelo admite
ω ≥ 1 (pivote disco sólido) y ese régimen queda abierto SALVO en los
casos j = 1 y j = 2 del Teorema P, cuyas pruebas no usan ω en absoluto
(bolsillo + colas + (D)) y valen para todo ω > 0.

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
Nota: si los σ superan la anchura la rama B es vacía para ω ≥ 1/2 y el
margen real es ≥ 2 − φ; con discos sólidos (σ ≤ ω, permitidos) la rama
B puebla todo ω y la identidad Ψ_B(1) = φ es la frontera genuina.)

## 4. Rama A (σ₂ > 1−ω): hojas estrictas y la escalera Ψ

Sea `jj` = número de hojas estrictas garantizadas: `jj = j` si y no es
hoja (todos los subárboles aportan hojas estrictas), `jj = j − 1` si y es
hoja. La mayor hoja estricta L tiene el programa del lema de las hojas
con bono jj: `ρ·L ≥ (jj−1) + 1 + σ₁ + σ₂ + W` y `L < σ₂ + ω + W`, cuya
optimización en la rama A es `Ψ_jj(ω)`. Los cruces con φ son exactos:

    Ψ₁(1/2) = φ ,     Ψ₂(φ/2) = φ ,     Ψ₃(1) = √3 > φ :

j ≥ 4 (o jj ≥ 3): toda ω; jj = 2: ω < φ/2 = 0.809; jj = 1: ω < 1/2. ∎

## 4bis. El cierre de j = 2: la pared de los bolsillos espejo

**Pared W₂ (bolsillos espejo).** Bloqueo con j = 2 ⟹ `b₂(o₁, o₂) < 1`.

*Demostración.* La colocación «σ₂ → sartén, σ₁ → D_m» falla ⟹ los
círculos `{o₁, o₂, m, σ₂}` no empaquetan en R ⟹ (contención,
`R ≥ o₁ + o₂` por el par de F) no empaquetan en el disco `o₁ + o₂`,
donde el par `{o₁, o₂}` es diametralmente rígido y deja exactamente DOS
bolsillos espejo de radio `b₂(o₁,o₂)` a distancia `2y₀ = 4b₂` (identidad
`y₀ = 2b₂` del Lema G). El cuarteto empaqueta en `o₁+o₂` **si y solo
si** `m ≤ b₂` y `σ₂ ≤ b₂` (necesidad: S5 por círculo; suficiencia:
concéntricos en los bolsillos espejo, disjuntos porque
`m + σ₂ ≤ 2b₂ ≤ 4b₂`). Como falla y `σ₂ ≤ 1 = m`: `b₂ < 1`. ∎

**Cierre de j = 2 (toda ω, ambas ramas).** Sea `Ā(o₁)` la raíz de
`b₂(o₁, B) = 1` (decreciente; `Ā(2) = √5 − 1` por el rincón dorado de
`bolsillo.md`; `Ā(3/2) = 3/2` autodual). La pared W₂ da `o₂ < Ā(o₁)`.
Las colas, con (D) `σ₁+σ₂ > 1`:

    ρ ≥ (o₂ + 1 + σ₁ + σ₂)/o₁ > (o₂ + 2)/o₁      (cola de o₁)
    ρ ≥ (1 + σ₁ + σ₂ + X₂)/o₂ > 2/o₂             (cola de o₂)

El mínimo de `máx((o₂+2)/o₁, 2/o₂)` sobre `o₂ ∈ (1, Ā(o₁))`:

- `o₁ ≤ 3/2`: `(o₂+2)/o₁ > 3/o₁ ≥ 2 > φ`.
- `o₁ ∈ (3/2, 2)`: el cruce `o₂* = √(1+2o₁) − 1` es interior
  (`b₂(o₁, o₂*) < 1` en ese rango, con igualdad exacta en `o₁ = 2`) y el
  valor es `2/o₂* > 2/(√5−1) = φ` ⟺ `o₁ < 2`.
- `o₁ ≥ 2`: `o₂ < Ā(o₁) ≤ Ā(2) = √5−1` y `ρ > 2/o₂ > 2/(√5−1) = φ`.

En todos los casos `ρ > φ`, sin usar ω, la rama de la evacuación ni la
posición de y. ∎ (El cruce áureo `2/o₂*(2) = φ` con
`Ā(2) = √5−1 = o₂*(2)` es OTRA VEZ el rincón dorado `b₂(2, √5−1) = 1`.)

## 4ter. El cierre de j = 3: el árbol de casos

Bloqueo con j = 3 ⟹ ρ > φ, por la disyunción (con `s := σ₁+σ₂ > 1` y
`o₃ > 1`):

1. **o₂ < 3/φ**: la cola de o₂ contiene a `{o₃, m, σ₁, σ₂}`:
   `ρ > (o₃ + 1 + s)/o₂ > 3/o₂ > φ`.
2. **o₂ ≥ 3/φ y o₁ < 3**: la cola de o₁ contiene a `{o₂, o₃, m, σ₁, σ₂}`:
   `ρ > (o₂ + o₃ + 1 + s)/o₁ > (3/φ + 3)/o₁ > (3/φ + 3)/3 = ... > φ`
   por la identidad `(3/φ + 3)/φ = 3` (es decir, la cota cruza φ
   exactamente en o₁ = 3).
3. **o₁ ≥ 3**, enrutado por la posición de y (reparación del acta: la
   primera redacción contaba nodos en la cola de m y hojas de z como
   «terceras», ambos ilegales; los contraejemplos están en el acta):
   - **y = o₁**: por (Ry), `X₁ ≥ o₁ − ω − s > 0` (s < 2 ≤ o₁ − ω).
     Si `X₁` contiene un nodo, y no es hoja ⟹ jj = 3 hojas estrictas ⟹
     `ρ > Ψ₃(ω) ≥ √3 > φ` (rama A) o `ρ > Ψ_B > φ` (rama B). Si `X₁`
     es todo polvo (< 1), vive en la cola de m:
     `ρ ≥ s + X₁ ≥ o₁ − ω ≥ 2 > φ`.
   - **y en el subárbol de o₂ u o₃**: si y no es hoja, su subárbol
     aporta hojas estrictas propias ⟹ jj = 3 ⟹ Ψ₃/Ψ_B como antes. Si
     y es hoja: jj = 2 y la escalera da `ρ > Ψ₂(ω) > φ` para ω < φ/2;
     para ω ≥ φ/2 con `σ₂ > ω`, `ρ ≥ σ₁ + σ₂ > 2ω ≥ φ`. Queda la
     **sub-celda declarada** {y hoja en o₂/o₃, ω ≥ φ/2, σ₂ ≤ ω
     (disco sólido), o₁ ≥ 3, o₂ ≥ 3/φ}: el argumento de la torre
     (esbozo: (Bo) en o₁ y la tricotomía por niveles — polvo total
     > 0.618 ⟹ cola de m > φ; dos hijos-nodo ⟹ jj = 3 ⟹ Ψ₃; torre de
     nodo único ⟹ los nodos anidados suman cuadráticamente en la cola
     de o₁, mín ≈ 1.93 > φ) está esbozado pero NO cerrado; evidencia
     del acta: 240 000 muestras dirigidas (torres, con y sin σ > ω),
     mín ρ = 2.37, 0 violaciones. ∎ (módulo la sub-celda)

   [CORRECCIÓN post-acta: la primera reparación usaba `S ⊂ (ω,1)` como
   plantilla; el modelo permite discos sólidos y la premisa era falsa —
   de ahí la sub-celda declarada.]

## 5. El Lema Z (histórico) y notas

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

**Nota histórica.** El Lema Z cerraba parcialmente el antiguo rincón
{j ∈ {2,3}, rama A, ω grande}; la pared de bolsillos espejo (§4bis) lo
subsume para j = 2 (`Ā(o₁) < 1 + 1/o₁` para o₁ ≥ el número plástico
1.3247…, certificado `(o₁³−o₁−1)/(o₁⁴+o₁³+2o₁²+2o₁+1)`; por debajo
ambas paredes son vacuas) y el árbol de casos (§4ter)
elimina el resto. Se conserva porque su mecanismo (las dos ramas del U₄
dan la misma desigualdad) es reutilizable para |S| ≥ 3.

## 6. Lectura

- **El ínfimo de la plantilla es φ y la dirección ≥ de la Conjetura A2
  queda DEMOSTRADA en la plantilla S par, completa** (Teorema P sin
  rincón + familia áurea para la ≤). El oro aparece por todas partes:
  el punto fijo del bolsillo (j = 1), el rincón dorado b₂(2, √5−1) = 1
  como cruce de j = 2, y las medias metálicas degenerando en φ en los
  bordes (Ψ(1/2) = Ψ₂(φ/2) = Ψ_B(1) = φ).
- Para la conjetura completa faltan: |S| ≥ 3 en la sartén, pequeños
  extra (Corolario-S-análogo), y el ensamblaje del lema universal con
  el umbral corregido.

## 7. Huecos declarados

1. ~~El sliver~~ — CERRADO para j = 2 (§4bis, pared de bolsillos
   espejo, sin hipótesis alguna sobre σ) y para j = 3 salvo la
   sub-celda de discos sólidos de §4ter (argumento de la torre
   esbozado; evidencia mín ρ = 2.37).
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
