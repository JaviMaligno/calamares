# La pesada especular con X_Y > 0

Estado: v2 (2026-08-16), ADVERSARIADO (acta en VEREDICTOS.md:
CONFIRMADO CON CORRECCIONES — cero grietas de solidez;
reparaciones 1-5 aplicadas). Script: `code/esppesada.py` (5/5; el
bloque B por UNIÓN DE BANDAS de ΣS — ver §2). El último cuarto de
la celda especular, dentro del convenio X_Y = polvo < m.

## 1. La fusión y la renuncia por tramos

**Fusión de bloques**: el polvo de X_Y (masa μ_Y ≤ φ−ΣS por la
cola global de m; cada pieza ≤ μ_Y por pigeonhole) se funde con el
polvo de la partición B*/A de areduccion en UNA cadena monótona:
masa μ_A+μ_Y, tope max(t₀, μ_Y), coste ≤ π·masa/(c′−tope)
(derivación cap-genérica, acta de espkp).

**Renuncia por tramos (K = 8)**: el rango oculto μ_Y ∈ [0, φ−ΣS_lo]
se parte en 8 tramos; cada uno se certifica con el polvo al TECHO
del tramo y el crédito de cola del SUELO del tramo — pesimista
uniforme POR TRAMO, la unión cubre todo μ_Y legal, y el B&B corre
en las MISMAS 11 dimensiones de areduccion. La renuncia total (v1)
creaba una tangencia fantasma en ΣS → 1 (el techo del polvo y el
suelo diametral coinciden justo donde la cola del polvo era el
rescate); K = 4 aún perdía ~0.10 de cola y rozaba π.

**Dos variantes en OR**: pliegue de ranuras ≤ tope al bloque
(rápida; pero infla la masa de piezas medianas — dos falsas
tangencias cazadas) y sin pliegue (completa) — ambas sound.

**La pared pesada como poda**: ΣS ≥ 1+σ₂ — la ligera con X_Y la
cierra espkp; sin esta poda el B&B re-certificaba carísimo la
región ligera en la arista ΣS → 1 (donde el polvo es máximo).

## 2. El certificado

B&B en las 11 dims de areduccion, certificado por **unión de seis
bandas de ΣS** (chunking: la máquina mata los runs > ~10 min y el
DFS no es resumible — se parte la RAÍZ): [1.0, 1.025] 19.809
cajas, [1.025, 1.05] 6.897, [1.05, 1.1] 3.797, [1.1, 1.2] 2.039,
[1.2, 1.4] 1.875, [1.4, φ] 371 — ~34.800 cajas, todas verdes con
el código final (5/6 re-ejecutadas por el referee con recuentos
EXACTOS — DFS determinista). Sanity end-to-end: 200/200 instancias
pesadas reales con polvo X_Y explícito Y EL A-POLVO EN LA CARGA
(reparación 1 del acta: antes muA era código muerto; el referee
verificó 2×200/200 con la versión fiel), partición B*/A real, Y en
su suelo con la cola contando μ_Y, y el clip ΣS ≤ φ−0.02 del
generador declarado. Controles (estándar espkp, reparación 3):
certificador negativo (D > π y matriz estrangulada → False),
negativo de la poda pesada (caja ligera → None), pared computada.
**Hallazgo del referee**: la frontera ΣS = 1+σ₂ EXACTA es VACUA
(S∖{σ₂} suma 1 ⟹ β = 1 ⟹ ventana de α = ∅) — la unión
espkp ∪ esppesada cubre la especular con X_Y sin hueco ni
solapamiento problemático.

## 3. Estatus

Con este certificado, **la celda especular entera queda cerrada
dentro del convenio en sus cortes/cajas declarados**: ligera con
X > 0 y X_Y = 0 (r2bmulti), ligera con X_Y > 0 (espkp, con
X_α/X_z/X_m > 0), pesada en X = 0 (areduccion) y pesada con
X_Y > 0 (este script, corte X_α = X_z = X_m = 0). RESIDUO
declarado de la especular: la pesada con X_α/X_z/X_m > 0
(solo-MC, G-g de puertocii), el canal ocupante ≥ r_m
(model-conditional) y los topes del barrido (ω ≤ 1.6, X_α ≤ 1.5,
X_z ≤ 1).
