# F3 re-delimitado: el lema condicional de dualidad exacta

Estado: v2 (2026-08-10), ADVERSARIADO (acta: REFUTADO como
«cierre», rescatado como lema condicional; reparaciones 1-6
aplicadas). Script: `code/f3cierre.py` (5/5).

## 1. El lema (condicional a no-apilabilidad)

Para una familia cuyas parejas son TODAS no apilables al radio en
juego:

- **Necesidad** (compactación, teorema adversariado): el
  empaquetamiento real se proyecta a corona mural al mismo R con el
  orden heredado ⟹ R_real ≥ mín sobre órdenes = R_arcLP :=
  mín{R : arc-LP factible}.
- **Suficiencia** (arc-LP v2, adversariado): en R_arcLP el sistema
  cerrado es factible y se realiza.

⟹ **R_arcLP es el radio mínimo de corona mural EXACTO por los dos
lados** — condicional a la no-apilabilidad, que se verifica POR
INSTANCIA. Sanity clásica: R_arcLP(3 iguales) = 1+2/√3 y R_arcLP(4
iguales) = 1+√2, EN la tangencia. Medir solo los TOPS preserva la
necesidad por **borrado monótono** (los requisitos de arcos de un
subconjunto están implicados por los de la carga) — NO por
apilabilidad del grano: la justificación del v1 era falsa (3 tops
0.9 + grano 0.55 dan top+2·grano = 2.0 > R_ex = 1.939, par NO
apilable).

Precisión declarada: la bisección (42 pasos) cita el lado lo en
enunciados de necesidad y el hi en los de suficiencia; la
resolución efectiva la limita la banda ~10⁻⁹ del primal (signo
favorable-a-factible, medida en el bloque A). El uso con n = 6
piezas queda dentro del acta del arc-LP **extendida**: criterio
dual-y-primal validado contra LP directo (HiGHS), 60 sistemas, 0
discrepancias (bloque E).

## 2. El gap verdadero en el dominio sintético

Dominio sintético: 3-4 tops de ratio 0.9-1.0 + 1-2 granos de
0.15-0.55·t0 (cociente grano/top hasta 0.61). Aquí la
no-apilabilidad de los tops se cumple 60/60 y el lema aplica.

- **Supremo por malla de esquinas** (16 esquinas deterministas):
  R_arcLP(carga)/R_arcLP(tops) = **1.0816** en la esquina pesada
  4×0.9 + 2×0.55 (cadena diametral top-grano-top = 2.35 exacto). El
  «≤ 1.030» del v1 era artefacto muestral (60 muestras uniformes no
  pisan la esquina): REFUTADO en acta y corregido.
- Muestreo: gap = 1 en 39/60 (granos ligeros insertan gratis), peor
  muestra 1.0302 ≤ supremo de esquina.

## 3. El dominio real del F3 queda FUERA (hallazgo del acta)

El generador real del F3 (`puertocii`, tops = [α, T, extras con
uniform(0.3, α)]) produce instancias de gap viejo cuyos tops tienen
parejas **APILABLES** al radio exacto (3/3 medidas, bloque E): la
condición del lema falla y **R_real ≥ R_arcLP(tops) NO está
demostrado en la celda F3 real** — el residuo 1.0116 PERMANECE. La
medición sin teorema da gap verdadero = 1 en 3/3 (favorable, no
demostrado). Además, en el dominio sintético las dos cotas viejas
son TENSAS (R_lb sobre tops tenso 60/60; R_fit = radio exacto
25/25): la narrativa del v1 «el 1.0116 era la distancia entre dos
cotas flojas» carecía de soporte y queda **RETIRADA** — el gap
viejo vive en el dominio real, fuera del lema.

## 4. Estatus

Exacto (módulo banda ~10⁻⁹ declarada): el lema condicional (dos
piezas adversariadas compuestas), los óptimos clásicos en
tangencia, el supremo de esquina 1.0816. Medido-exacto: el gap por
bisección cerrada de ambos radios. Muestreado: 60 instancias
sintéticas + 3 instancias reales de gap. Residuo que PERMANECE: la
celda F3 real (tops apilables, 1.0116), con dos vías declaradas —
extender la necesidad por subconjuntos no apilables de tops, o
añadir la MASA REAL de la sartén de P a la necesidad (cascada de
colas).
