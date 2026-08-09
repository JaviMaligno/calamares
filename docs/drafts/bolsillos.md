# El cierre por bolsillos, fase 1: el cuarteto j = 0 exacto

Estado: DRAFT fase 1 (2026-08-09), ADVERSARIADO (acta en
VEREDICTOS.md: CONFIRMADO CON CORRECCIONES, con mejoras — el
certificado quedó 100% algebraico y la identidad d2 DEMOSTRADA en
ℚ(√5)). Script: `code/bolsillos.py` (3/3). Fase 2 (j = 1, k ≤ 2)
EN CURSO — desbloqueada por `arcolp.md` (el LP de arcos, que
además incluye los wraps que a `_lp4` le faltaban, hallazgo H4).

## 1. El teorema de fase 1

**Teorema (cuarteto j = 0 por bolsillos).** En el dominio de
thm:gapwritten con j = 0, la corona {α, m, s′, w*} cabe en
R_test = α+1 para TODA instancia — por desigualdad algebraica, no
por barrido. *Prueba.* α y m diametrales (distancia π = θ(α,m),
exacta en R = α+1); un pequeño a cada hueco del par. (i) En
R = α+1 el disc de Descartes es 0 idéntico (lema de escala) y el
bolsillo es p(u) = u(u+1)/(u²+u+1), u = α, creciente. (ii)
Sub-bolsillo (DIC, zigzag): s ≤ p ⟹ θ(α,s)+θ(s,m) ≤ π: el
contenido de cada hueco cabe en su arco. (iii) Con el ACOPLE de
ligaduras (s′ ≤ Σ/2, w* ≤ Σ−1) y α ≥ (1+Σ)/φ (peor caso; ω, Σ_S y
holguras solo suben α y p): con Σ = φu−1,

    q(u) = 2u(u+1) − (φu−1)(u²+u+1) = (φ−u)·r(u) ≥ 0
    g(u) = p(u) − (φu−2) ≥ g(φ) = (3−√5)/4 = φ/2 − 1/φ

en u ∈ [2/φ, φ], AMBAS 100% ALGEBRAICAS (mejora de la ronda
hostil): **r(u) = φu² + 2(φ−1)u + (φ−1)** con los tres coeficientes
positivos (r > 0 sin malla), y g estrictamente decreciente
(g′ = p′ − φ con sup p′ = p′(2/φ) ≈ 0.30 < φ) con mínimo exacto en
φ. Dos ramas en α (H5): para α ≤ φ mandan q y g; para α > φ,
s′ ≤ φ/2 = p(φ) < p(α) y w* ≤ 1/φ < φ/2 < p(α) (p creciente). Y
**q(φ) = 0 EXACTO**: la tangencia áurea — en Σ = φ con α en su
suelo φ, el tope s′ = φ/2 = p(φ,1;φ+1), EL BOLSILLO ÁUREO DE
thm:DP (`descartes_pocket_golden` en Lean). El punto crítico de
j = 0 es el mismo bolsillo del contraejemplo. (iv) Pares no
consecutivos (α,m) y (s′,w*): super-bolsillo de las piezas
intermedias (p(s′max,w*max) ≤ 0.244 ≪ 1 ≤ m, α: NS-2 ≥ 0). (v)
R > R_test: todas las θ decrecen — las mismas posiciones valen
(fit-monotonía; el BOLSILLO decrece con R, por eso el certificado
vive en R_test y se extiende por fit). ∎

Verificación: 20 000 instancias del dominio real (holguras hasta
~100), 0 violaciones del certificado y 0 del cross-check
constructivo (`corona_k5`); la tangencia áurea realizada
({φ, 1, φ/2, 1/φ} cabe en φ+1).

## 2. Los dos errores del diseño v1 (documentados, controles)

(E1) La forma degenerada 1/(1/a+1/b−1/R) SOBRESTIMA el bolsillo
fuera de R = a+b (falta 2√disc): p(2,1;3.5) real 0.572 vs 0.824.
El punto áureo se salva por el ACOPLE de ligaduras (Σ→1 ⟹ s′ ≤ 1/2
y w* → 0), no por el bolsillo grande. (E2) dp/dR < 0: el bolsillo
SE ENCOGE con R — el certificado se monta en R_test y se extiende
por la monotonía del fit, no del bolsillo.

## 3. Fase 2 (COMPLETA, v3 — pre-adversario)

j = 1 y coronaagujero k ≤ 2 CERTIFICADOS por B&B 3D en (Σ, g1, g2),
con certificados por caja en este orden: (1) exclusión de V (lema
de entorno de arcolp); (2) bolsillos: ambos pequeños sub-bolsillo
de dos huecos distintos del TRÍO, que cabe POR CONSTRUCCIÓN —
R_used ≥ máx(pares, R₃), y en la banda donde R₃ manda el trío está
EXACTAMENTE TANGENTE (variedad 2D: la razón estructural por la que
ninguna desigualdad de esquina convergía); suficiencia k = 3
cerrada + hecho del dominio R₃ ≤ M (heredado de gaplemma con su
estatus de check no-suprimible); (3) F CERRADO: reducción GLOBAL de
s′ al hueco (g1,g2) (Σ/2 ≤ 2u/3 siempre: Σ(3φ−4) ≤ 4) y el 4-ciclo
[g1, g2, w*, m] con d₁ = π en forma cerrada — factible ⟺ −σ ≥
máx(B₁, B₂), con B_i los déficits NS-2 de las diagonales contra el
slack; unión bolsillo/ciclo en la dirección w*; (4) LP con testigo
verificado (HiGHS busca, se verifica) solo en la rama rara (banda
R₃ con w* > bolsillos; precondición pares-caben garantizada por el
dominio); (5) fit-esquina de respaldo. Resultados: j = 1 en
286 911 cajas (20 s), rama 1 k = 2 en 1 727, rama 2 k = 2 en
1 333; k = 1 heredado del certificado algebraico de fase 1; colas
g > 30 por fórmula. **Los dominios de las coronas acotadas quedan
certificados por subdivisión ENTEROS.**

## 3-bis. Historia (el WIP que precedió a v3)

j = 1 y k ≤ 2 vía B&B híbrido 3D en (Σ, α, o₁). Los B&B están
implementados (`--solo D`, `--solo E`) pero NO terminan, y el
diagnóstico es un hallazgo matemático: el punto peligroso real de
j = 1 es (Σ = φ, α = o₁ = φ, ambos en su suelo de cascada) — allí
los bolsillos laterales (p(φ,1;2φ) = 0.501 < w*-cap = 1/φ) no
albergan a w*, y el quinteto cabe SOLO con w* como MIEMBRO del
ciclo: el 4-ciclo {φ, φ, w*, m} con w* = 1/φ suma EXACTAMENTE 2π
(corrección de la ronda hostil, H3: el «margen 0.003» de la v1 era
espurio — venía de evaluar w* = 1/φ − 10⁻³; en el cierre w* → 1/φ
la variedad es EXACTAMENTE TANGENTE por la identidad d2, del mismo
rango que la tangencia áurea de fase 1). Capturarla exige un
criterio con desigualdades cerradas y all-pairs completo: **el lema
del LP de arcos** (`arcolp.md`, que además incluye los wraps que a
`_lp4` le faltaban — hallazgo H4 del acta) más el certificado de
entorno del punto tangente (gradiente estricto en V). Con ambos,
el certificado por caja añade el modo «w* en el ciclo» y los B&B
deberían terminar. Es el siguiente paso del programa, no un
parche.

## 4. Estatus

Fase 1 exacta: disc = 0 en R = a+b, p(u) creciente, q = (φ−u)r con
r > 0 (división exacta en ℚ(√5)), tangencia áurea q(φ) = 0,
g ≥ 0.19, super-bolsillos, DIC importada (zigzag adversariada). El
dominio j = 0 de thm:gapwritten deja de ser barrido: es teorema
con una tangencia áurea en la esquina. Fase 2 pendiente de
construcción y ronda hostil.
