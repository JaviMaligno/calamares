# El cierre por bolsillos, fase 1: el cuarteto j = 0 exacto

Estado: DRAFT fase 1 (2026-08-09), PRE-ADVERSARIO. Script:
`code/bolsillos.py` (3/3). Fase 2 (j = 1, k ≤ 2) EN CURSO con el
diseño corregido en memoria de campaña.

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
    g(u) = p(u) − (φu−2) ≥ 0.19       en u ∈ [2/φ, φ],

con r > 0 en el intervalo (división polinómica exacta en ℚ(√5)) y
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

## 3. Fase 2 (en curso)

j = 1 (quinteto con la necesidad del trío R₃) y coronaagujero
k ≤ 2: B&B 2-3D en (Σ, α, o₁) — todos los demás parámetros solo
mueven el suelo de α — con bolsillos en esquinas (p sube con la
pieza a R fijo, baja con R) y el fit-esquina de respaldo; el
déficit 0 del punto áureo (2, 2/φ) se maneja con el mismo esquema
de acople (allí s′ ≤ 1/2 < p = 0.636 y w* → 0).

## 4. Estatus

Fase 1 exacta: disc = 0 en R = a+b, p(u) creciente, q = (φ−u)r con
r > 0 (división exacta en ℚ(√5)), tangencia áurea q(φ) = 0,
g ≥ 0.19, super-bolsillos, DIC importada (zigzag adversariada). El
dominio j = 0 de thm:gapwritten deja de ser barrido: es teorema
con una tangencia áurea en la esquina. Fase 2 pendiente de
construcción y ronda hostil.
