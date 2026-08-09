# El lema del LP de arcos: la corona mural k ≤ 5 exacta

Estado: DRAFT (2026-08-09), ADVERSARIADO (acta en VEREDICTOS.md:
**REFUTADO EN SU ENUNCIADO, núcleo reparado** — v2 con las cuatro
reparaciones integradas). Script: `code/arcolp.py` (5/5). La pieza
que la fase 2 de bolsillos necesitaba: un criterio de corona que
certifica EN las variedades tangentes (déficit 0), donde
`corona_k5` con piezas infladas no puede.

## 1. El lema (v2, enunciado reparado)

**Precondición (H1, FATAL del acta)**: a_i + a_j ≤ R para todo par,
con igualdad permitida (par diametral tangente). Sin ella, dos
piezas murales no son disyuntas a NINGUNA separación (el requisito
real es +∞, no la π-gorra) y el criterio v1 declaraba factibles
órdenes físicamente imposibles — `ciclo_constructivo` siempre tuvo
esta guarda y el arc-LP v1 la perdió.

Con la precondición: fijado un orden cíclico [x₀..x_{n−1}] en un
disco R, con d_i ≥ 0 las separaciones angulares consecutivas
(Σd = 2π), la corona mural existe en ese orden SII para todo arco
contiguo propio A = (i..j):

    Σ_{gaps ∈ A} d ≥ r_A := máx(Σ θ_consec(A), θ_w(x_i, x_j, R)).

*Necesidad*: las d reales de una corona lo cumplen (la distancia de
cada par es el mínimo de los dos arcos complementarios: ambos ≥ θ).
*Suficiencia*: una d factible colocada en posiciones acumuladas
deja toda pareja mural-disjunta (P1/compactación) — legítimo
precisamente porque los pares caben. Con desigualdades NO estrictas
certifica en tangencia exacta.

**Factibilidad**: el criterio OFICIAL es el **primal exacto por
enumeración de bases** (politopo acotado; todo vértice resuelve n
filas activas con la igualdad incluida; barato para n ≤ 5). La
condición dual de familias de arcos disjuntos (Σr_A ≤ 2π) es
NECESARIA pero **no suficiente en general** (H3: la matriz de arcos
CIRCULARES no es de intervalos ni totalmente unimodular —
contraejemplo puro del acta con tres arcos de longitud 2 y
r = 1.5π: el certificado de infactibilidad necesita cobertura
doble, invisible para familias disjuntas); bajo la estructura
geométrica coincide con el primal en 9 500+ instancias sin
discrepancia, SIN prueba — se usa solo como poda.

**Contra corona_k5 (H2)**: tras la reparación son EQUIVALENTES en
el muestreo (3000/3000; los «101 casos estrictamente más fuerte»
del v1 eran al 100% el artefacto de la π-gorra — pares imposibles).
El valor del arc-LP no es potencia extra: es la caracterización SII
con desigualdades cerradas (tangencia) y la forma LP (dualizable,
apta para cotas de esquina).

## 2. La tangencia áurea certificada

En el punto peligroso de j = 1 ((Σ, α, o₁) = (φ, φ, φ), R = 2φ,
w* = 1/φ): el 4-ciclo [φ, φ, 1/φ, m] suma EXACTAMENTE 2π (la
identidad `golden_pi_trio`, Lean 39) y el arc-LP es factible con
igualdad — el único par con suma = R es (φ, φ), en la frontera
LEGAL de la precondición. El quinteto con s′ = φ/2 suma
π + 4asin(1/√3) — la constante de R2b — y su diagonal (φ,φ) consume
el slack 0.6797 EXACTO. Estabilidad verificada por el acta:
perturbación adversa 10⁻¹² en α o w* rompe la factibilidad, m−ε la
mantiene.

## 3. El entorno del punto tangente

Gradiente simbólico de σ(α,o₁,Σ) = θ(o₁,Σ−1)+θ(Σ−1,1)+θ(1,α) − π
en R = α+o₁, en el punto: σ_α = −0.687, σ_{o₁} = −1.112,
σ_Σ = +1.799 (verificado por diferencias finitas en el acta; el
check ahora EXIGE los signos — H5). En V = [φ, φ+0.15]² ×
[φ−0.15, φ]: signos estrictos en malla 25³ ⟹ σ ≤ 0 en toda V.

**H4 (hueco lógico del v1, cerrado)**: σ ≤ 0 solo controla la suma
consecutiva; las DIAGONALES del 4-ciclo no son redundantes — la
desigualdad triangular de θ es FALSA en parte de V (margen −0.098
medido por el acta). El certificado v2 añade el LP COMPLETO del
4-ciclo (primal exacto, diagonales incluidas) sobre la malla 13³ de
V: 0 infactibles — el slack de las d absorbe el déficit diagonal en
toda V.

## 4. Estatus

Exacto (teorema): el lema v2 con su precondición (necesidad +
suficiencia por posiciones acumuladas), la precondición como
condición necesaria de cualquier corona, las desigualdades
cerradas, la tangencia certificada, el gradiente (sympy + FD).
Exacto-por-enumeración: el primal (criterio oficial).
Numérico-certificado: la coincidencia dual/primal bajo estructura
(poda, sin prueba — declarado), las mallas de V (σ-signos 25³ +
LP completo 13³; sin cota de Lipschitz formal, como el resto del
programa — anotado por el acta). Pendiente de fase 2: usar
`primal_factible` como certificado del B&B (con θ_ub en esquinas:
conservador tras H1 — un par inflado que no cabe da infactible,
sin testigo en falso) + exclusión de V + caso-análisis de órdenes
para u < 1.5.
