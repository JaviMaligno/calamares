# R2b certificada: el trío de [G] por subdivisión

Estado: DRAFT con pruebas (2026-08-09), PRE-ADVERSARIO. Script:
`code/r2bcert.py` (5/5). Sube los barridos del trío del bloque [G]
de R2b (G-b/G-c interior, G-f profundidad, G-g ligera especular) de
MC+frontera a COTA CERTIFICADA por branch-and-bound con cotas de
esquina — la tecnología de `optimizacion.py` aplicada al trío mural.

## 1. La reducción

La suficiencia k = 3 (adversariada en puertocii: suma ≤ 2π con cada
θ ≤ π y pares cabiendo ⟹ la corona de 3 se realiza) reduce el
cierre a acotar la SUMA del trío. θ_w es creciente en las piezas y
decreciente en c (exacto): esquina pesimista = cota superior válida
por caja; podas EXACTAS sin tolerancia hacia la supervivencia (las
ventanas reales son semiabiertas — una caja-punto infactible con
holgura 10⁻¹² sobreviviría para siempre: bug cazado y reparado).

## 2. Rama DR (G-b + G-c + G-f de una vez)

Trío {T, m, σ₂} en c ≥ ΣS + T (tarifa DR; los X solo SUBEN c: peor
caso 0), con T la pieza grande LIBRE ≥ 1 — cubre Y en d = 1 y z en
TODO d ≥ 2 de un golpe. Relajaciones exactas (superconjunto del
dominio real): σ₁ < 1 ⟹ ΣS < 1+σ₂ (ligereza automática); σ₁ ≥ σ₂
⟹ σ₂ ≤ ΣS/2; pared (D) ⟹ ΣS > 1; σ's < 1 ⟹ ΣS < 2. Cola T → ∞
por monotonía exacta (los signos de G-f0: a c = ΣS+T, f_T·f_m crece
con límite 1/ΣS y f_{σ₂}·f_T crece con límite σ₂/ΣS — los sympy que
REFUTARON la monotonía de nivel ahora dan los límites).

**Certificado: sup < 2π − 0.3 con 148 cajas.** (Ni siquiera hace
falta la pared de masa ΣS ≤ φ: el superconjunto con ΣS < 2 ya
certifica — enunciado más fuerte.)

## 3. Rama ESP (G-g ligera, tarifas derivadas)

Corona {z, D_m, σ₂} en c′ = Y−ω, con las tarifas derivadas
adversariadas: convivencia m–z en v ⟹ Y ≥ 1+z+ω (c′ ≥ 1+z); suelo
de cola Y ≥ (1+ΣS+α+z)/φ (X's = 0 el peor: solo suben el suelo);
α ∈ [máx(1+ω, ΣS+ω), 1+σ₂+ω); z ∈ [α+ω, α+σ₂+ω); ventana de Y no
vacía. El umbral analítico: en c′ = 1+z el trío da
π + 4·asin(√(σ₂/(2−σ₂))), que alcanza 2π EXACTAMENTE en σ₂ = 2/3;
para σ₂ > 2/3 el rescate es el suelo de cola(Y) — el B&B lleva las
dos cotas de c′ y resuelve el trade-off.

**Certificado: sup < 2π − 0.3 con 41 948 cajas.**

**El hallazgo de esta certificación (control E(d)).** La rama ESP
NECESITA la pared de masa ΣS ≤ φ (cola(m) ≤ φ, exacta y estándar en
el programa): sin ella, la esquina σ₂ → 1, ΣS → 2 es alcanzable
(ΣS ∈ [2σ₂, 1+σ₂) tiene ancho 1−σ₂ > 0) y allí la corona
GENUINAMENTE NO CABE — z+1 = c′ diametral y el bolsillo de Descartes
b₂(z, 1; c′) = 0.958 < σ₂. El barrido G-g (0 fallos) nunca la
muestreó (medida cero en MC). Con la pared, σ₂ ≤ ΣS/2 ≤ φ/2 = 0.809
y la esquina queda excluida. Es la demostración de por qué los
certificados por subdivisión valen más que los barridos: el B&B la
ENCONTRÓ (caja atascada) en vez de pasarla por alto.

## 4. Resultado y alcance

**Lema (trío de R2b certificado).** Las ramas del trío de [G] —
interior ligero (G-b/G-c), profundidad d ≥ 2 con pieza libre (G-f)
y especular ligera (G-g) — tienen suma de trío < 2π − 0.3 sobre sus
cajas legales ENTERAS, certificado por subdivisión exhaustiva
(cotas de esquina válidas + podas exactas). Con la suficiencia
k = 3, las coronas se realizan en todo el dominio. ∎

Coherencia: la caja diminuta en la esquina certificada da cota
5.6035 = π + 4asin(1/√3) exacto (ajustado, no inflado); objetivo
por debajo de la esquina NO certifica (se atasca en 5.6035 exacto).

FUERA (declarado): G-b′ (X′ explícitas) y G-e / G-g pesada
(partición B*/A) — coronas multipieza, criterio de corona, no suma:
siguen como barridos MC adversariados. El análogo sería un B&B de
factibilidad con el argumento «las mismas posiciones valen»
(dominación de órdenes por θ puntual); esquema para una campaña
futura.

## 5. Estatus

Exacto: monotonías, relajaciones del dominio, límites T → ∞ (por
los sympy de G-f0), suficiencia k = 3 (importada, adversariada), el
umbral 2/3, la pared de masa ΣS ≤ φ, las podas (sin puntos reales
perdidos). Certificado-por-subdivisión: los dos sups (< 2π − 0.3,
margen > 13 órdenes sobre el error float de una suma de 3 asin).
Barridos MC que PERMANECEN: G-b′ y las ramas pesadas (declarado).
