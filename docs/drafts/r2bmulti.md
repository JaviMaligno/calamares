# Multipieza R2b: G-b′ certificada y la ESP fuera del corte X = 0

Estado: v2 (2026-08-10), ADVERSARIADO (acta en VEREDICTOS.md:
CONFIRMADO CON CORRECCIONES — la matemática entera resiste, 1460
tests dirigidos sin grietas de solidez; las 4 reparaciones son de
enunciado/dominio y están aplicadas). Script: `code/r2bmulti.py`
(5/5). Sube a certificado-por-subdivisión dos de los barridos MC
que r2bcert dejó declarados fuera, con el motor «esquina pesimista
+ arc-LP» que su §4 esbozaba. Solo se usa la dirección de
SUFICIENCIA del arc-LP — elemental y válida para todo k (una d
factible coloca, y toda pareja queda ≥ θ por ambos lados); la
caracterización exacta k ≤ 5 / k = 6 no se invoca (corrección del
acta: la primera redacción atribuía la carga a la validación k = 6,
que solo concierne a la necesidad).

## 1. El motor

**Dominación**: θ_w crece con las piezas y decrece con la capacidad
(exacto); los requisitos de arcos r_A = max(Σθ_consec, θ_extremos)
son monótonos en las θ; la factibilidad del sistema es antítona en
los requisitos (la misma d vale). Sobre una caja, una **matriz
mayorante por término**: cada θ(a,b) en SU esquina — participantes
en techo INCLUIDO su aporte a la capacidad (válido: dθ/da tiene el
signo de R−a−b = ΣS+resto > 0, verificado por tipo de par en el
acta), resto en suelo. La esquina mixta global (pieza Y en techo,
capacidad con Y en suelo) NO se usa: pierde la holgura de pares
ΣS−1+Σx en la arista ΣS → 1.

**Criterio estricto** (lección de f3cierre + corrección del acta):
la banda ~10⁻⁹ del primal es favorable-a-factible — inaceptable
para suficiencia — y un margen sobre el primal por bases es
imposible (los vértices tienen filas activas EN igualdad). El LP de
**holgura máxima** (max t con arcos ≥ r_A + t, HiGHS) actúa de
BUSCADOR, y el CERTIFICADO es la **verificación en float puro de la
d devuelta** (holgura ≥ 5·10⁻⁸ por arco re-evaluada; error float
~10⁻¹⁵): el t* de HiGHS lleva error de objetivo medido de hasta
2.5·10⁻⁸ — la cita «precisión ~10⁻⁹ de HiGHS» del v1 era falsa — y
f3cierre E validó el LP de factibilidad, no el max-t; con la
verificación, la solidez no descansa en el solver. En R₃* exacto el
criterio rechaza (t* = 0); con holgura real acepta.

**Criterio antipodal** (decisivo en la arista ΣS → 1, donde el par
(Y, m) exige π por ambos lados y el margen del LP circular tiende a
0 incluso en puntos reales): Y y m a distancia exactamente π — con
θ(Y,m) < π ESTRICTO en todo punto real, por álgebra ((u−1)(u+Y) > 0
con u = ΣS+Σx > 1), sin apoyo numérico — y la cadena {σ₂, x's} en
un semicírculo como sistema de CAMINO, cuyo dual de familias
disjuntas es EXACTO (matrices de intervalo TU; el contraejemplo de
arcolp es circular; verificado en el acta contra LP, 400 sistemas,
0 discrepancias). El par (Y, m) sale del sistema (analítico); los
pares cadena-extremo van por el camino corto y el complementario
≥ π ≥ θ automático.

## 2. G-b′ certificada (X′ explícitas, k = 4, 5, 6)

Corona {Y, m, σ₂} ∪ X′ en c = ΣS + Y + ΣX′, certificada ENTERA por
B&B de factibilidad sobre un superconjunto de la **caja del barrido
MC** (corrección del acta: el techo Y ≤ 6.6 viene de Y < ΣS+X_Y+ω
con los topes de MUESTREO X_Y ≤ 3, ω ≤ 1.6 — no de una pared
derivada; hay puntos legales con X_Y = 4, Y = 7 fuera de la caja,
declarados FUERA): sin ventanas de α/Y, s₂ < 1 ENTERA (pared real,
extendida tras el acta), ligereza ΣS ∈ (1, 1+σ₂), s₁ ≥ σ₂,
x_i ∈ (0, Y]. j = 1 en 59 cajas, j = 2 en 87, j = 3 en 139 (el
antipodal certifica la mayoría; el LP circular el resto). Los pares
del superconjunto caben ESTRICTO por álgebra: la π-gorra de la
matriz nunca tapa un par imposible (el artefacto del arc-LP v1 no
puede reaparecer).

## 3. ESP fuera del corte X = 0 (rama X_Y = 0)

El acta de r2bcert (H1/H2) recortó la ESP al corte X = 0 por dos
motivos: ventanas desplazadas con X > 0, y X_Y viviendo en la
corona de v. Este certificado cubre el primero: trío {z, D_m, σ₂}
en c′ = Y−ω con X_α ≤ 1.5, X_z ≤ 1, X_m ≤ 1−ω (X_Y = 0) sobre la
caja del barrido (ω ≤ 1.6, α ≤ 5.1, z ≤ 8.7): sup < 2π − 0.3 con
948 cajas — y con holgura real: certifica también a 2π − 0.35 con
1863 cajas (acta), coherente con el sup MC ~5.74-5.80. B&B de 8
dims con coordenadas clampadas a las ventanas y DOS cotas por caja:
la global (esquina con c′ ≥ max(1+z_lo, cola−ω)) y la **acoplada al
suelo diametral** (c′ ≥ 1+z con el mismo z: θ(z,m) ≤ π
idénticamente, θ(σ₂,z;1+z) crece en z con signo 1−σ₂ > 0) — sin la
acoplada, 6M cajas no convergen. Podas exactas (600 controles
punto-caja del acta: 0 violaciones, 0 podas de cajas con puntos
reales).

## 4. Alcance honesto

FUERA (declarado): G-e / G-g pesadas (mural con A multipieza, |A|
sin cota — falta un lema de reducción de |A|); ESP con X_Y > 0 (el
análogo especular de G-b′ con capacidad φ-descontada: tarifa peor);
G-b′ con X_Y > 3 u ω > 1.6 (topes de muestreo del MC); ω > 1.6 en
la ESP (sup MC 5.7379 con ω hasta 3.0). Siguen como barridos MC
adversariados (puertocii G-b′/G-e/G-g). Los certificados nuevos
EXTIENDEN r2bcert sin circularidad (solo suficiencia del arc-LP +
pares por álgebra/convivencia).

## 5. Estatus

Exacto: las monotonías del motor (sympy, por tipo de par), el
álgebra de pares del superconjunto, la exactitud TU del camino
antipodal, la dirección del margen (rechazo en R₃* exacto), la
verificación en float de cada d certificante.
Certificado-por-subdivisión: G-b′ j ≤ 3 sobre la caja del barrido
(s₂ < 1 entera); ESP X > 0 (X_Y = 0) en la caja del barrido, con
margen doble (0.3 y 0.35). Controles: negativo doble, esquina
crítica de r2bcert reproducida, 400 sistemas de camino vs LP y 400
cajas-punto del motor sin violaciones (acta). Barridos MC que
PERMANECEN: los del §4.
