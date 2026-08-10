# F3 re-delimitado: la dualidad exacta del arc-LP

Estado: DRAFT (2026-08-10), PRE-ADVERSARIO. Script:
`code/f3cierre.py` (4/4). Re-delimita la gap-dualidad F3 (≥ 3 tops
casi iguales, el viejo R_fit/R_lb ≤ 1.0116) con las dos piezas
nuevas de la campaña.

## 1. El teorema de dualidad exacta

Para familias con todas las parejas NO apilables:

- **Necesidad** (compactación, teorema adversariado): todo
  empaquetamiento real se proyecta a corona mural al mismo R ⟹ las
  d reales satisfacen el sistema de arcos ⟹ R_real ≥ R_arcLP :=
  mín{R : arc-LP factible}.
- **Suficiencia** (arc-LP v2, adversariado): en R_arcLP el sistema
  cerrado es factible y se realiza.

⟹ **R_arcLP es el radio mínimo de corona mural EXACTO por los dos
lados**. Sanity clásica: R_arcLP(3 iguales) = 1+2/√3 y R_arcLP(4
iguales) = 1+√2 (los óptimos conocidos, aterrizados EN la
tangencia: 3θ = 2π con déficit ~10⁻¹⁰ — el criterio cerrado la
admite). Dicotomía apilable: cubierta por M (blindada), comprobada
por instancia sobre los TOPS (un grano siempre es apilable tras un
top y es irrelevante para la necesidad).

## 2. Lo que el gap viejo medía y lo que queda

El 1.0116/1.15 del F3 viejo era la distancia entre DOS COTAS
FLOJAS (el R_lb angular «que no ve los bolsillos» y el R_fit del
constructivo muestreado). Con los dos radios EXACTOS:

- 60 instancias F3 sintéticas (3-4 tops casi iguales, ratio
  0.9-1.0, + 1-2 granos de 0.15-0.55·top): tops no apilables al
  radio exacto 60/60.
- **El gap verdadero**: R_arcLP(carga)/R_arcLP(tops) = 1 en 39/60
  (granos ligeros insertan gratis) y ≤ 1.030 en el resto — con
  granos pesados (~0.5·top) hay un gap REAL de hasta ~3%: la carga
  necesita genuinamente más radio que los tops solos. NO es
  artefacto al 100%: es un intervalo real, ahora delimitado por
  dos radios exactos en vez de dos cotas muestreadas.

## 3. Estatus nuevo de la celda F3

R_real ≥ R_arcLP(tops) es TEOREMA (compactación + arc-LP +
no-apilabilidad por instancia). La clausura restante es el
intervalo EXACTO [R_arcLP(tops), R_arcLP(carga)] — vacío con
granos ligeros, ≤ 3% con pesados. La vía de cierre total
(pendiente, declarada): añadir la MASA REAL de la sartén de P a la
necesidad — el empaquetamiento real contiene más que los tops, y
esa masa extra empuja R_real por encima de R_arcLP(tops); la
cascada de colas es el candidato natural para cuantificarlo.

## 4. Estatus

Exacto: el teorema de dualidad (dos piezas adversariadas
compuestas), la dicotomía, los óptimos clásicos reproducidos en
tangencia. Medido-exacto: el gap verdadero por bisección cerrada de
ambos radios (42 pasos). Muestreado: el dominio F3 sintético (60
instancias; el generador del F3 original en puertocii tiene más
estructura — la ronda hostil debe comparar). Residuo que PERMANECE:
el intervalo carga-vs-tops con granos pesados, con su vía de
cierre declarada.
