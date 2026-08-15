# La certificación k-piezas del sub-bolsillo

Estado: v2 (2026-08-10), ADVERSARIADO (acta en VEREDICTOS.md:
CONFIRMADO CON CORRECCIONES — cero grietas de solidez dentro del
convenio; reparaciones 1-5 aplicadas). Script: `code/espkp.py`
(5/5). El remate de la celda ESP X_Y > 0 ligera tras la vacuidad
de espvals.

## 1. Las paredes y el criterio

**El convenio (reparación 1 del acta)**: todo lo que sigue vive
dentro de **X_Y = polvo < m**; el canal «ocupante ≥ r_m en el
contenedor de Y» es MODEL-CONDITIONAL con tarifa sin derivar (acta
de espxy corr. 5; banda X ≥ 1 de auditcolas) y NO lo cierra este
script.

**La pared del polvo** (cola global de m): μ = ΣX_Y ≤ φ−ΣS−X_m <
φ−1 = 0.618 (pared D); por **pigeonhole** cada pieza ≤ μ, con el
tope decreciendo por caja. Con x*(z) > 0.618 en todo el dominio,
todo el polvo es sub-bolsillo.

**El criterio** (motor areduccion/r2bmulti): antipodal z–m, σ₂ y
el bloque de polvo en los dos semicírculos como sistemas de CAMINO
(TU exacto); cota acoplada para los pares con z (signo verificado
en el acta con la fórmula real: d/dz ∝ x(1−x) ≥ 0); c′_lo =
max(1+z_lo, cola_lo−ω_hi) con la cola incluyendo μ; el bloque
pagado por masa — cadena MONÓTONA ≤ πμ/(c′−μ), con el orden
monótono como carga real heredada (areduccion rep. 4) y la
derivación cap-genérica re-fuzzeada por el acta con el tope grande
(cap = μ ≤ 0.618: 0/6000; el contraejemplo no-monótono reescalado
sigue violando). Suficiencia sobre superconjunto: las ventanas son
las de r2bmulti bloque D (adversariadas) con μ como única novedad.

## 2. El certificado y la verificación

**B&B de 9 dimensiones**: certificada entera en 1.329 cajas vistas
(483 certificadas, resto podas exactas — verificadas una a una en
el acta). Sanity: 250/250 puntos legales con polvo EXPLÍCITO
(k = 1..4; robusto a semilla: 3×250/250 en el acta, ~23% por
corona_suf con dirección solo-suficiente correcta; 0 piezas
sobre-bolsillo en 750). Controles: la poda de la pared (negativo),
**el certificador rechaza lo imposible** (reparación 2: bloque con
D > π y matriz estrangulada → False), coherencia con espvals.

## 3. Estatus

**La celda ESP X_Y > 0 LIGERA queda CERRADA dentro del convenio**:
vacuidad del peligro (espvals) + certificado k-piezas (k libre por
el pago por masa). Declarado: el canal ≥ r_m (model-conditional),
la PESADA con X_Y > 0 (fusión con el bloque de areduccion — mismo
motor, siguiente ciclo natural), y los topes del barrido (X_α ≤
1.5, X_z ≤ 1, ω ≤ 1.6). Colateral del acta: retirado el código
muerto `talla()` de areduccion (T0 hardcodeado — trampa latente
para topes ≠ t₀) y el CC_ITER sin uso.
