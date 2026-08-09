# El lema del LP de arcos: la corona mural k ≤ 5 exacta

Estado: DRAFT con pruebas (2026-08-09), PRE-ADVERSARIO. Script:
`code/arcolp.py` (5/5, bloques A-E). La pieza que la fase 2 de bolsillos
necesitaba: un criterio de corona que certifica EN las variedades
tangentes (déficit 0), donde `corona_k5` con piezas infladas no
puede.

## 1. El lema

Fijado un orden cíclico [x₀..x_{n−1}] en un disco R, con d_i ≥ 0
las separaciones angulares consecutivas (Σd = 2π): la corona mural
existe en ese orden SII el sistema de ARCOS es factible — para todo
arco contiguo propio A = (i..j):

    Σ_{gaps ∈ A} d ≥ r_A := máx(Σ θ_consec(A), θ_w(x_i, x_j, R)).

*Necesidad*: las d reales de una corona lo cumplen (la distancia de
cada par es el mínimo de los dos arcos complementarios: AMBOS ≥ θ).
*Suficiencia*: una d factible colocada en posiciones acumuladas deja
toda pareja mural-disjunta (P1/compactación). Caracterización
EXACTA por orden; sobre órdenes, el criterio de corona. Con
desigualdades NO estrictas certifica en tangencia exacta.

**Factibilidad (dualidad del LP de intervalos circular)**: el
sistema es factible SII toda FAMILIA de arcos propios disjuntos dos
a dos suma Σr_A ≤ 2π. Validada contra un LP primal exacto por
enumeración de bases: 4 000 órdenes aleatorios k = 3..5, 0
discrepancias. Contra `corona_k5`: k5 ⟹ arc-LP siempre (0
violaciones — el lema es caracterización) y el arc-LP es
estrictamente más fuerte (101/3000 instancias que el constructivo
no encuentra).

## 2. La tangencia áurea certificada

En el punto peligroso de j = 1 ((Σ, α, o₁) = (φ, φ, φ), R = 2φ,
w* = 1/φ): el 4-ciclo [φ, φ, 1/φ, m] suma EXACTAMENTE 2π (la
identidad θ(φ,1/φ)+θ(1/φ,1)+θ(1,φ) = π) y el arc-LP es factible
con igualdad. El quinteto con s′ = φ/2 suma π + 4asin(1/√3) — la
constante de R2b — y su diagonal (φ,φ) consume el slack 0.6797
EXACTO: certificado en la tangencia, imposible para cualquier
criterio con desigualdades estrictas o piezas infladas.

## 3. El entorno del punto (el dato para fase 2)

Mapa numérico: 125 puntos en las direcciones admisibles (α, o₁
suben desde φ; Σ baja desde φ), quinteto por arc-LP: 125/125 caben.
Gradiente simbólico de la ligadura σ(α,o₁,Σ) = θ(o₁,Σ−1) +
θ(Σ−1,1) + θ(1,α) − π en R = α+o₁, en el punto: σ_α = −0.687,
σ_{o₁} = −1.112, σ_Σ = +1.799 — LOS TRES SIGNOS FAVORABLES.

**Certificado de entorno (bloque E)**: en la vecindad definida
V = [φ, φ+0.15]² × [φ−0.15, φ], los signos de las tres derivadas
se mantienen ESTRICTOS en malla 25³ (máx σ_α = −0.42 < 0, máx
σ_{o₁} = −0.86 < 0, mín σ_Σ = +1.61 > 0): σ es monótona en V con
σ(punto) = 0 (la identidad) ⟹ σ ≤ 0 en TODA V — el 4-ciclo
[g1, g2, w*, m] cabe en la vecindad entera. El parche del punto
tangente queda al estándar de maximización certificada; el B&B de
fase 2 puede excluir V y trabajar con el arc-LP fuera.

**Caveat honesto para fase 2** (anotado, no resuelto): la ruta del
4-ciclo usa B′ ≤ slack, que equivale a θ(o₁,m)+θ(m,α) ≤ π; en los
suelos u = (1+Σ)/φ eso da 2asin(1/√(2u−1)) ≤ π/4 ⟺ u ≥ 1.5 — para
u ∈ (2/φ, 1.5) el orden [g1, g2, w*, m] no es el bueno y el
certificado debe cambiar de orden (ahí mandan los órdenes de fase 1
con m diametral). El cierre global de j = 1 es un caso-análisis por
órdenes con lemas monótonos por rama — ahora DESBLOQUEADO por el
arc-LP; queda como la construcción de fase 2.

## 4. Estatus

Exacto (teorema): el lema (necesidad + suficiencia por posiciones
acumuladas), las desigualdades cerradas, la tangencia certificada,
el gradiente en el punto (sympy). Validado: la dualidad (primal
exacto, 0 discrepancias — la prueba formal del vértice dual con
arcos disjuntos es dualidad LP estándar de matrices de intervalos,
enunciada); la equivalencia con corona_k5 (una dirección teorema,
la otra empírica: el arc-LP domina). Pendiente: integrar el arc-LP
como certificado del B&B de fase 2 con el caso-análisis por órdenes.
