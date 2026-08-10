# La variedad del bolsillo diametral: ESP con X_Y > 0

Estado: v2 (2026-08-10), ADVERSARIADO (acta en VEREDICTOS.md:
CONFIRMADO CON CORRECCIONES — el hallazgo sobrevive con margen;
las 7 reparaciones aplicadas, incluida la identidad x*(φ) = φ/2
regalada por el referee). Script: `code/espxy.py` (5/5).
EXPLORACIÓN Y DELIMITACIÓN, no cierre: la celda especular de R2b
con X_Y > 0 (declarada fuera en r2bcert H2 y r2bmulti §4) contiene
una obstrucción REAL del testigo estándar, con frontera en forma
cerrada.

## 1. La variedad (álgebra exacta, bloque A)

En el suelo de convivencia c′ = 1+z el par (z, m) es diametral
EXACTO (f(z)f(1) ≡ 1). Una pieza x de X_Y cabe junto a m sii

  **x ≤ x*(z) = z(z+1)/(z²+z+1) = p(z, 1; 1+z)**

— el **bolsillo de Descartes del par diametral** (forma degenerada
1/(1/a+1/b−1/R), exacta en R = a+b): la frontera de la corona ES el
bolsillo. El sliver infactible x ∈ (x*, 1) tiene anchura
1−x* = 1/(z²+z+1); **en z = φ la anchura es 1/(2φ²) y
x*(φ) = φ/2, ambos exactos** (z²+z+1 = 2φ² por φ² = φ+1;
candidatos a Lean junto con 3φ−1). El rescate de cola(Y) no llega
cuando

  **z + ω ≥ φ(3+x−φ)** [= 3φ−1 exacto en x = 1; en x = 0 es
  φ(3−φ) = √5, la constante del lema de respiración]

(cola mínima legal (3+ω+z+x)/φ). **La protección de σ₂ es
exactamente áurea**: σ₂ ≤ ΣS/2 ≤ φ/2 = x*(φ) < x*(z) para todo
z > φ, y la zona sin rescate tiene z ≥ 2.84 ≫ φ (barrido del acta,
2M muestras, 0 puntos con σ₂ > x*) — la pared de masa ΣS ≤ φ y
σ₁ ≥ σ₂ protegen el segundo hueco con margen.

El lado x ≥ 1 es MODEL-CONDITIONAL (acta): el par diametral pasa a
(z, x) y m debe caber en su bolsillo (infactible sii z²+x² >
xz(z+x−1), banda finísima hasta x** — 0.005 en z = 4), pero una
pieza x ≥ 1 = r_m no está cubierta por el convenio de X_Y (polvo
< m) y su tarifa de cola está sin derivar.

## 2. La variedad es real y legal (bloques B/C)

300 puntos LEGALES del sliver (ventanas de G-g ligera, pared de
masa, las paredes de bloqueo (BH) y (Bσ₁) — añadidas tras el acta:
antes se cumplían por suerte de la caja —, Y en su suelo, cola sin
rescate): la corona {z, m, σ₂, x} refutada por el **dual del
arc-LP en todos los órdenes** (necesario ⟹ refutación SOUND) en
300/300 con esta semilla (gate > 80%), con déficit robusto (0.51
rad en el punto de z mínima — no es fenómeno de frontera). Dentro
del bolsillo (x < x*): la corona completa cabe en 300/300 (primal)
— la frontera separa exactamente. Los rescates adversariados
FALLAN: apilar x tras m es un corolario trivial del diámetro
agotado (2z+2+2x ≤ 2c′ ⟺ x ≤ 0); la fila de **D_m (capacidad 1,
recurso distinto de H_m = 1−ω−X_m que tarifica BH)** lleva σ₁+W y
solo admitiría x < σ₂ ≤ φ/2 < x*; la cola no levanta por
construcción. La imposibilidad de colocaciones INTERIORES
generales descansa en no-apilabilidad + compactación (el lema de
suficiencia k = 4 sigue pendiente): delimitación, no cierre
interior.

**No es un límite del certificado sino del TESTIGO**: la celda ESP
con X_Y > 0 necesita un testigo nuevo en la variedad.

## 3. Extensión (bloques D)

Síntesis del barrido del acta (ω libre): **min z = 2.84** y
**min ω = 0.906** en la zona sin rescate; anchura del sliver hasta
~0.08 ahí (1/(z²+z+1)). La nota del acta sobre pivote sólido está
RESUELTA EN NEGATIVO (análisis 2026-08-10 con citas): D3, DPr y
thm:D1written son celdas del intercambio de SARTÉN (caso (a) del
ensamblaje); la partición (a)/(b)/(c) es disjunta y definicional
(ensamblaje §«exactamente uno») y los programas de sartén no
portan (m debe cohabitar en la sartén con los j ocupantes —
«portabilidad de paredes ≠ cobertura de programa»). En (c-ii) el
régimen ω ≥ 1 nunca se delegó: es donde vive su residuo (R2 con
X = 0 en ω ∈ (0.927, 1) ∪ [1, ∞)). El pivote sólido además ayuda
al ADVERSARIO en la variedad: mata H_m (X_m = 0 forzado, la
colocación BH desaparece) mientras D_m (hueco unidad, cap 1) queda
intacto. La variedad completa ω ∈ (0.906, 1.6] queda ABIERTA. Dato
estructural del análisis: la variedad vive en la rama I2 «que
respira» (Y > z ≥ α exige X_Y+ω > φ — con x ≈ 1 y ω ≥ 0.9 se
cumple de sobra): es el corazón de la rama que respiraba, no un
accidente.

## 4. Rutas candidatas (bloque E; NADA hecho)

(i) **Simetría m↔x** (la más prometedora): x < 1 = r_m es libre
para el intercambio (thm:oblivious solo exige acuerdo en anillos
≥ r_m) — enviar x a otro contenedor y dejar la corona {z, m, σ₂}
certificada; exige derivar la tarifa del contenedor receptor.
Herramientas portables identificadas (análisis 2026-08-10):
lem:compact y lem:insert están enunciados para un disco R
ARBITRARIO (no para la sartén), y el precedente del mecanismo
receptor existe en la campaña (el desbloqueo «corona-α»: el
agujero de α admite corona {m, σ₂} ∪ X_α en su peor capacidad).
OJO: u = agujero de α NO puede recibir a x junto a m en general
(α < 1+σ₂+X_α+ω es el techo del bloqueo: m+x ≈ 2 no caben salvo
X_α grande) — el receptor natural es la SARTÉN vía el lema de
realización-y-repack (F2), con la holgura del pan por derivar.
(ii) Pared nueva: con x ~ m en v, (RY) engorda: ¿el bloqueo se
contradice solo en la variedad? (iii) Contar x en cola(Y) con
tarifa entera (no φ-descontada) cuando x > p.

## 5. Estatus

Exacto: toda el álgebra de §1 (verificada a mano por el referee
además de sympy). Muestreado-con-refutación-sound: la legalidad y
la infactibilidad de §2. La celda ESP X_Y > 0 pasa de «declarada
fuera» a **variedad peligrosa delimitada con geometría áurea
exacta** — la misma familia del contraejemplo de thm:DP, la
esquina R2b y la curva tangente de bolsillos: el bolsillo áureo
vuelve a ser la frontera.
