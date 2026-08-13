# La vacuidad F3 cerrada: sub-bolsillo forzado

Estado: v2 (2026-08-10), ADVERSARIADO (acta en VEREDICTOS.md:
CONFIRMADO CON CORRECCIONES — el núcleo sobrevive los ataques
críticos; reparaciones 1-8 aplicadas). Script: `code/f3vacio.py`
(5/5). La mitad que faltaba tras auditcolas: la celda F3 (≥ 3 tops
casi iguales, el residuo 1.0116) es **ρ-vacía en el dominio del
programa**, también cuando la tercera pieza NO es comparable.

## 1. La cadena (exacta)

(i) La celda: par dominante casi igual (t₂ ≥ 0.9t₁ — frontera
EMPÍRICA del hallazgo, ver §3) más una tercera pieza. (ii)
ρ-legalidad con m = 1 y la pared D debajo: cola(t₁) ≥ t₂+t₃+1+ΣS ⟹
**t₃ < (φ−r₂)t₁ − 2**. (iii) El bolsillo del par dominante en el
suelo de pares es **q(r₂)·t₁ con q(r) = r(1+r)/(1+r+r²) =
r·x*(1/r)** — la función de espxy escalada por la pieza pequeña
(disc de Descartes = 0 exacto en R = a+b, verificado sympy; la
identidad de coherencia θ₁₃+θ₂₃ = π en t₃ = q·t₁ a 3.6e-15). (iv)
**Sub-bolsillo forzado** sii t₁ ≤ 2/(φ−r₂−q(r₂)): en r₂ = 0.9 el
techo es **23.0**, e infinito para r₂ > **r* = 0.963749** — la raíz
real de la cúbica áurea **r³+(2−φ)r²+(2−φ)r = φ** (donde
r+q(r) = φ). El dominio REAL del programa es t₁ = α ≤ **6.64**
(techo medido del generador; el «5.1» del v1 era falso — acta):
margen 3.46×. (v) Con t₃ sub-bolsillo el trío cabe EN pares
(DIC/NS-2 cerrado) y **R_arclp = pares = R_lb** — verificado
CONTRA EL CONFINAMIENTO (el ataque del acta): en 5.300+ instancias
de la celda, R_lb_pack = pares al 100% (suma cíclica confinada máx
4.02 < 2π).

## 2. Verificación (v2, cobertura del acta)

600 instancias ρ-LEGALES de la celda con t₁ hasta 6.7 (dominio
real), 232 con t₃ < m y 19 con 4 tops: trío en pares 600/600,
fenómeno F3 **0/600**. Más el acta: 1.500 con t₃ ∈ (0.3, 1) — 0
gaps; 2.300 en la banda t₁ ∈ (5.1, 6.7] — 0 gaps; borde tangente
t₃ = bolsillo exacto — 0/300 fallos (desigualdades cerradas).
Piezas ulteriores: cola(t₃) ⟹ t₄ ≤ φt₃−1−ΣS (válido a toda
escala; medido t₄ ≤ 0.60; con t₁ ≤ 5.1 la celda de 4 tops con
t₃ > 1 es directamente vacía).

## 3. Estatus y alcance honesto

La celda F3 es ρ-vacía por dos pinzas: **trío prohibido**
(auditcolas, t₃ comparable) + **sub-bolsillo forzado** (este lema,
t₃ no comparable). **El residuo 1.0116 se retira del programa**
(con esta acta); sobreviven el lema condicional de dualidad de
f3cierre y el 1.0816 como enunciados abstractos del arc-LP.
Alcance: la frontera 0.9 es empírica y el converso «gap ⟹ celda»
queda ABIERTO — la evidencia lo apoya (fuera de la celda, r₂ ∈
0.60-0.90, el CONFINAMIENTO sube R_lb sobre pares — hasta 1.0126 —
justo donde t₃ excede el bolsillo, y corona_suf cabe en el R_lb
subido: 0 gaps en 5.100 instancias del acta; el techo cubre además
hasta r₂ ≈ 0.75). Fuera de vía: t₁ > 23 con r₂ ∈ (0.9, r*), y
r₂ ≲ 0.74 con t₃ sobre-bolsillo (allí manda el confinamiento).
Colateral del acta: clamp del disc en `bolsillo_descartes`
(devolvía 0.0 en ~38% de pares diametrales exactos — conservador
pero infiel; reparado, regresión en verde). Candidatos a Lean:
q(1) = 2/3 y la cúbica áurea.
