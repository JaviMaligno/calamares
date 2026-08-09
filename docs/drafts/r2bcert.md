# R2b certificada: el trío de [G] por subdivisión

Estado: DRAFT con pruebas (2026-08-09), ADVERSARIADO (acta en
VEREDICTOS.md, misma fecha: CONFIRMADO CON CORRECCIONES — la DR
resiste entera; el alcance de la ESP reescrito al corte X = 0 y la
narrativa de E(d) corregida). Script: `code/r2bcert.py` (5/5). Sube los barridos del trío del bloque [G]
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

**Certificado: sup < 2π − 0.3 con 41 948 cajas — SOBRE EL CORTE
X = 0 de la caja del barrido** (ω ≤ 1.6, α ≤ 3.7, z ≤ 6.5; alcance
reescrito por la ronda hostil, H1/H2): con X > 0 los TECHOS de las
ventanas se desplazan hacia arriba (X = 0 solo es «el peor» para el
suelo de cola(Y), no para las ventanas — 54k configuraciones
legales del MC del acta caían fuera del corte), y además las X_Y
viven en v: la corona real tiene más de 3 piezas y la suficiencia
k = 3 no aplica (el análogo especular de G-b′). La ESP con X > 0 u
ω > 1.6 PERMANECE como barrido MC (G-g, adversariado; el sup MC del
acta con X > 0 y ω hasta 3.0 es 5.7379 < objetivo — el interior
manda).

**La pared de masa es NECESARIA (control E(d), narrativa corregida
por el acta).** Sin ΣS ≤ φ, la esquina σ₂ → 1, ΣS → 2 tiene
ventanas no vacías (ΣS ∈ [2σ₂, 1+σ₂), ancho 1−σ₂ > 0) y allí la
corona GENUINAMENTE NO CABE — el par (z, 1) es diametral EXACTO
(disc de Descartes 0, la fórmula sin raíz coincide con el bolsillo
real: 0.958 < σ₂). G-g SÍ imponía la pared (`SS + Xm > φ:
continue`, ligera incluida) — el aporte del B&B no es rescatar a
G-g sino DEMOSTRAR que la pared es necesaria para el argumento del
trío ESP, mientras la DR certifica sin ella. Con la pared,
σ₂ ≤ φ/2 = 0.809 y la esquina queda excluida.

## 4. Resultado y alcance

**Lema (trío de R2b certificado, alcance honesto).** (i) Rama DR —
interior ligero (G-b/G-c) y profundidad d ≥ 2 con pieza libre (G-f):
suma de trío < 2π − 0.3 sobre el dominio legal ENTERO
(superconjunto genuino: fuzzing del acta con 200k cajas, X hasta 3,
T hasta 10¹⁰, 0 violaciones y 0 podas de puntos reales). (ii) Rama
ESP — especular ligera con X = 0 sobre la caja del barrido: ídem.
Con la suficiencia k = 3, las coronas se realizan en esos dominios.
∎

Coherencia: la caja diminuta en la esquina certificada da cota
5.6035 = π + 4asin(1/√3) exacto (ajustado, no inflado); objetivo
por debajo de la esquina NO certifica (se atasca en 5.6035 exacto).
La ESP certifica también a 2π−0.4 (98k cajas) pero no a 2π−0.5 (su
sup MC ronda 5.74-5.80).

FUERA (declarado, tras el acta): G-b′ (X′ explícitas), G-e / G-g
pesada (partición B*/A), y la ESP con X > 0 (ventanas desplazadas +
X_Y en la corona de v) u ω > 1.6 — coronas multipieza o cortes no
cubiertos: siguen como barridos MC adversariados. El análogo sería
un B&B de factibilidad con el argumento «las mismas posiciones
valen» (dominación de órdenes por θ puntual); esquema para una
campaña futura.

## 5. Estatus

Exacto: monotonías, relajaciones del dominio DR, límites T → ∞
(por los sympy de G-f0), suficiencia k = 3 (importada,
adversariada), el umbral 2/3, la necesidad de la pared de masa
ΣS ≤ φ para la ESP, las podas (sin puntos reales perdidos —
verificado con 200k cajas). Certificado-por-subdivisión: los dos
sups < 2π − 0.3; el margen que importa es el DELTA DE PARADA del
max-heap (DR 5.6·10⁻³, ESP 1.9·10⁻⁵), ~10 órdenes sobre el error
float de una suma de 3 asin — no «0.3 rad» (la lección de la ronda
de optimización, aplicada aquí de fábrica). Barridos MC que
PERMANECEN: G-b′, ramas pesadas y la ESP fuera del corte X = 0
(declarado).
