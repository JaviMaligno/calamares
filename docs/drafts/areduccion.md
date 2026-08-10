# El lema de reducción 1/(4φ) y las pesadas de R2b

Estado: v2 (2026-08-10), ADVERSARIADO (acta en VEREDICTOS.md:
CONFIRMADO CON CORRECCIONES — cero grietas de solidez; las
reparaciones 1-5, incluido un REFUERZO del lema hallado por el
referee, están aplicadas). Script: `code/areduccion.py` (5/5,
bloques verificados individualmente; D tarda ~8-10 min). Cierra
las ramas PESADAS de R2b (G-e directa y G-g especular), declaradas
fuera por r2bcert/r2bmulti porque el mural {·, m} ∪ A tiene |A|
sin cota.

## 1. El lema de reducción (exacto)

Sea B* el mejor subconjunto de S con ΣB* ≤ 1 (la partición
adversariada de puertocii G-e; B* va en fila a D_m), A = S∖B*,
β = ΣB*, bajo la pared de masa ΣS ≤ φ y piezas < 1. Con
**t₀ = (φ−1)/4 = 1/(4φ)** y **β* = (9−√5)/8**:

(i) *Maximalidad*: a + β > 1 para toda a ∈ A (si no, B*∪{a} mejora)
y β ≥ σ₁ ≥ max A (el subconjunto {σ₁} es candidato). Corolario:
a ≤ φ/2 para toda a ∈ A (ΣS ≥ β + a ≥ 2a).

(ii) *Conteo*: **|{a ∈ A : a > t₀}| ≤ 4 SIEMPRE.** Si β ≤ β*:
|A| < (φ−β)/(1−β) ≤ 5 y toda a > 1−β ≥ 1−β* = t₀ (A entera es
grande). Si β > β*: cinco piezas > t₀ sumarían > 5t₀ =
**5(√5−1)/8 = φ−β*** (igualdad EXACTA en ℚ(√5)) ≥ φ−β ≥ ΣA —
contradicción.

(iii) *Polvo*: piezas ≤ t₀ de A existen solo si β > β*, y su masa
μ ≤ φ−β < 5t₀ ≈ 0.7725.

(iv) *Refuerzo (hallado por el referee)*: **4t₀ = φ−1 EXACTO** ⟹
|A_big| = 4 y polvo son INCOMPATIBLES: con 4 grandes,
μ < φ−β−(φ−1) = 1−β < toda pieza de polvo (que exige d > 1−β). El
mural real tiene ≤ 6 nodos; el modelo de 7 es superconjunto
estricto, y la incompatibilidad se usa como poda exacta en ambos
B&B.

## 2. El bloque de polvo: coste por masa

θ(a,b) = 2asin√(f(a)f(b)) ≤ asin f(a) + asin f(b) (AM-GM + asin
convexo, exactos, sympy). Con asin x ≤ πx/2: la suma consecutiva
interna de una cadena de polvo (piezas ≤ t₀, masa μ, radio R) es
≤ **πμ/(R−t₀)** — independiente del NÚMERO de piezas. Los extremos
del bloque se mayoran con talla t₀; los arcos que acaban dentro
quedan cubiertos por el arco al borde atómico. **El orden interno
del polvo es MONÓTONO (creciente hacia el interior) y es carga
real del argumento** (reparación 4 del acta): los pares interiores
saltados se validan porque en una cadena monótona la separación
acumulada domina el θ directo — el contraejemplo no-monótono
[t₀, ε, t₀] del referee viola pares saltados (sep 0.023 < θ
0.147). Fuzz: 4000 cadenas + 3000 cadenas ordenadas del acta, 0
violaciones, peor cociente 0.599.

## 3. Los cierres

Mural pesado = {Y ó z, m} + A_big (≤ 4) + UN bloque de polvo
agregado (μ, t₀): ≤ 7 nodos, certificado con el motor de r2bmulti
extendido — **antipodal de dos lados**: el par grande-m a distancia
exacta π y el resto repartido en DOS semicírculos, cada lado un
sistema de CAMINO (TU ⟹ dual de familias disjuntas exacto); el
bloque de polvo entra como nodo atómico con dos extremos virtuales
t₀ y arista interna πμ/(R−t₀).

El lado degenerado (semicírculo sin cadena) devuelve presupuesto 0
— ES el par excluido y no lo reintroduce (reparación 1 del acta:
antes, en la tangencia de G-g con θ(z,m) ≡ π en c′ = 1+z, el arco
completo de un solo gap exigía π ≤ π−margen y el verde dependía del
accidente de que la bisección nunca anula un slot).

- **G-e pesada (DR)**: mural {Y, m} ∪ A_big ∪ polvo en c = ΣS+Y;
  matriz por término (participantes en techo CON su aporte a c;
  el polvo NUNCA infla la capacidad como participante). 501 cajas
  vistas, 109 certificadas — el resto, podas exactas (caja del
  barrido: Y ≤ ΣS+1.6).
- **G-g pesada especular (corte X = 0)**: mural {z, m} ∪ A_big ∪
  polvo en c′ = Y−ω ≥ max(1+z, cola(Y)−ω), ventanas de G-g con la
  partición (techo de α con ΣS−β). Dos ingredientes de
  convergencia: cota ACOPLADA θ(z,·;1+z_hi) para los pares con z
  (crece en z: d ∝ 1−x ≥ 0), y **clamp de masa fantasma** — con
  capacidad fija, las cajas con Σtechos > ΣS jamás certifican: los
  techos de cada pieza se clampan por la ligadura β+Σa+μ = ΣS.
  6887 cajas vistas, 1678 certificadas — el resto, podas exactas.

## 4. Alcance honesto

Cajas del barrido MC (ω ≤ 1.6; Y < ΣS+ω en G-e; corte X = 0 en la
especular). Las X > 0 de las pesadas y ω > 1.6 siguen como MC
adversariado (puertocii G-e/G-g). Con esto, todas las ramas
multipieza de R2b con tarifa derivada quedan certificadas salvo las
X > 0 declaradas (incluida X_Y > 0, r2bmulti §4).

## 5. Estatus

Exacto: el lema entero (§1, álgebra en ℚ(√5) — candidato a Lean),
la cota del polvo (§2, convexidad), a ≤ φ/2, la exactitud TU de los
caminos. Certificado-por-subdivisión: los dos cierres de §3.
Controles: fuzz de partición 25000 perfiles + 1312 adversarios del
acta en los umbrales (máx |A_big| observado 3), sanity end-to-end
vs corona_suf (200 instancias, 0 discrepancias) + colocaciones
físicas construidas por el referee (5 instancias adversarias, 0
pares violados), negativo (D > π no certifica). Sustitución
honesta (reparación 2): el MC de G-e pesada queda SUSTITUIDO en su
caja; del MC de G-g pesada queda sustituida **solo la rebanada
X = 0** — su masa con X > 0 sigue siendo solo-MC (declarado en
§4).
