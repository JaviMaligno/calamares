# El lema de optimización: sup G < 2π − 0.05 certificado

Estado: DRAFT con pruebas (2026-08-09), PRE-ADVERSARIO. Script:
`code/optimizacion.py` (5/5). Es el último asterisco estructural de
los teoremas de sombras: el sup del mayorante G del lema de la cola
geométrica deja de ser un barrido muestreado y pasa a estar
CERTIFICADO por branch-and-bound con cotas de esquina (aritmética
de intervalos por monotonía). Con la cadena

    presupuesto real ≤ G (dominación, colageometrica, exacta)
    sup G < 2π − 0.05 (este lema, certificado por B&B)

todos los presupuestos de sombras de los teoremas escritos
(thm:nestedwritten j ≥ 2, ramas de agujero k ≥ 3, thm:D1written)
quedan bajo 2π con certificado de cobertura TOTAL de la caja — no
muestreo denso, sino subdivisión exhaustiva con cota superior
válida en cada caja.

## 1. La palanca (exacta)

Cada término 2·asin((s+x)/(R−s)) es CRECIENTE en x, CRECIENTE en s
(d/ds = ((R−s)+(s+x))/(R−s)² > 0), DECRECIENTE en R (sympy, bloque
A), con la π-gorra. Sobre una caja [t₂]×[Σ]×[u]×[t₁], evaluar los
numeradores en el extremo ALTO y R en el BAJO da una cota superior
válida de G en TODA la caja (esquina pesimista — puede ser
infactible: sobra). Podas exactas que no pierden puntos reales:
t₂ ≥ 1+Σ (hipótesis del lema de la cola), u ≤ φt₂ (cascada de t₂),
t₁ ≥ máx(t₂, (t₂+u_lo)/φ) (el vínculo (V), con u_lo como cota
inferior válida del suelo en la caja).

Los tres modos de inserción se reducen a dos: el modo σ₂ queda
mayorado por el modo 1 (misma s_hi = mín(Σ/2, φ/2) por la ligadura
σ₂ ≤ Σ/2, y la misma pieza unidad como extra).

## 2. Las direcciones no acotadas

- **t₁ → ∞**: la caja final [T₁, ∞) usa la π-gorra en el término
  líder (2·asin ≤ π SIEMPRE) y R_lo = T₁+t₂_lo en el resto, que
  muere con T₁. La subdivisión [t₁, 4t₁] ∪ [4t₁, ∞) converge.
- **t₂ > 1000**: forma normalizada (dividir todo por t₂): a = t₁/t₂
  ∈ [1, 40] + cola a > 40 (π-gorra), u′ = u/t₂ ∈ [0, φ],
  σ = s/t₂ ≤ (φ/2)/1000, dominantes d′_r ≤ mín(1, u′/φ^r,
  u′/(r+1)) (soltar el −(1+Σ)/t₂ solo agranda: cota válida), serie
  truncada a 60 términos + resto analítico (asin(x) ≤ πx/2 y cola
  geométrica de razón 1/φ). B&B 2D: 9 cajas bastan (cota 6.04).

## 3. Resultado

**Lema (optimización de sups de sombras).** sup G < 2π − 0.05 sobre
la caja entera de hipótesis del lema de la cola geométrica.
*Certificado*: B&B con cotas de esquina — modo 1: 880 cajas;
modo 2: 881 cajas; cola t₂ > 1000: 9 cajas. Cada caja de la
subdivisión final tiene cota superior < 2π − 0.05 y la unión de las
cajas cubre el dominio entero (las podadas no contienen puntos
reales). ∎

**Ajuste**: la caja diminuta alrededor del argmax (t₂ = 2, Σ = 1,
u = 2φ, t₁ = 2φ, modo w*) da cota 5.2118 — a 3·10⁻⁴ del sup real
5.2115: el certificado no está inflado.

**Honestidad** (controles): (a) sin la hipótesis t₂ ≥ 1+Σ, la caja
de la navaja (t₂ = (1+Σ)/φ, t₁ = 1+Σ) da cota 6.93 > 2π y NO es
certificable por refinamiento — el presupuesto real ahí ES 6.93
(colageometrica E(e)): la hipótesis es exactamente lo que separa.
(b) Con objetivo 5.20 < sup real, el B&B NO certifica y se atasca
en 5.2115 exacto: la cota muerde en el sup verdadero, el
certificado no es vacuo.

## 4. Alcance y lo que queda

CUBIERTO por este lema: los sups de presupuestos de sombras de
todos los teoremas escritos (vía la dominación de colageometrica).
El estándar sube de «sup muestreado + esquinas» a «cota superior
certificada por subdivisión exhaustiva».

NO cubierto (estatus propio, declarado): (i) los barridos de
dominio de las coronas ACOTADAS (gaplemma j ≤ 1, ramas de agujero
k ≤ 2: el criterio k ≤ 5 es exacto POR INSTANCIA pero el dominio
se muestrea — certificarlo exigiría un B&B sobre la
factibilidad constructiva, otra naturaleza); (ii) los cierres
computacionales (dualidad/escala, barridos G de R2b, F2, F3).

Flotantes: IEEE double sin redondeo dirigido; los márgenes
certificados superan el error de redondeo en más de 12 órdenes de
magnitud. Declarado.

## 5. Estatus

Exacto (teorema): las monotonías de los términos (sympy), la
validez de la cota de esquina, las tres podas (no pierden puntos
reales), la π-gorra, la reducción de modos, el resto analítico de
la serie normalizada. Certificado-por-subdivisión: sup G < 2π−0.05
(B&B exhaustivo, cotas válidas en toda caja). Es el peldaño que el
programa llamaba «lema de optimización pendiente» para los
presupuestos de sombras; los dos residuos de §4 conservan su
etiqueta.
