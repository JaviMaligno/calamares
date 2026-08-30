import Calamares.Basic

/-!
# Calamares.Identities — la capa de certificados exactos del paper

Cada teorema formaliza una identidad algebraica exacta sobre la que descansa
un resultado del paper (empaquetamiento de anillos).  La correspondencia con
el paper (`paper/main.tex`) y los scripts de verificación (`code/`) se anota
en el comentario de cada teorema.

Todo se demuestra con `decide +kernel`: aritmética exacta reducida por el
kernel de Lean (sin mathlib, sin `native_decide`, sin axiomas nuevos).
-/

namespace Calamares

/-! ## Definiciones del paper -/

/-- Rigidez S5 del par: `b2 A B = A·B·(A+B)/(A² + A·B + B²)` es el radio
máximo del tercer círculo junto al par tangente diametral `{A, B}`. -/
def b2 (A B : Q5) : Q5 := A * B * (A + B) / (A ^ 2 + A * B + B ^ 2)

/-- Bolsillo `b(A) = b2 A 1 = A(A+1)/(A² + A + 1)` (versión `Q5`). -/
def bpocket (A : Q5) : Q5 := A * (A + 1) / (A ^ 2 + A + 1)

/-- Bolsillo `b` sobre ℚ puro (para la esquina 13/7). -/
def bQ (a : Rat) : Rat := a * (a + 1) / (a ^ 2 + a + 1)

/-- Polinomio de Tribonacci `P(x) = x³ − x² − x − 1` sobre ℚ.
Su única raíz real es la constante de Tribonacci `T ≈ 1.8392867…`. -/
def PRat (x : Rat) : Rat := x ^ 3 - x ^ 2 - x - 1

/-- `s* = 4(√5 − 2) = −8 + 4√5`: el umbral exacto de existencia de la corona
del trío `{φ, s, s}` en el testigo del contraejemplo áureo. -/
def sstar : Q5 := ⟨-8, 4⟩

/-!
## Contraejemplo áureo — `thm:golden` (script `code/aureo.py`, bloque A)

La instancia áurea `R = φ + 1`, radios `{φ, 1, φ/2 + 2ε, φ/2 + ε}` refuta la
conjetura del umbral de Tribonacci.  Estas son sus identidades exactas.
-/

/-- (1) `φ² = φ + 1`: la ecuación áurea, base de toda la aritmética del
contraejemplo. [thm:golden; aureo.py A] -/
theorem phi_sq : phi ^ 2 = phi + 1 := by decide +kernel

/-- (1b) `φ > 0` en el orden real de `Q5`. -/
theorem phi_pos : (0 : Q5) < phi := by decide +kernel

/-- (2) `b2(φ, 1) = φ/2`: la rigidez S5 del par `{φ, 1}` es exactamente φ/2;
por eso `s₂ = φ/2 + ε` no cabe y el voraz se atasca. [thm:golden; aureo.py A] -/
theorem b2_phi_one : b2 phi 1 = phi / 2 := by decide +kernel

/-- (3) `(1 + φ)/φ = φ`: la cola de φ es áurea — el cociente del testigo
recupera φ, de ahí que el ínfimo de la familia sea φ. [thm:golden; aureo.py A] -/
theorem tail_golden : (1 + phi) / phi = phi := by decide +kernel

/-- (4) `2·b(φ)·φ = 1 + 2·b(φ)`: φ resuelve el punto fijo
`2 b(A) A = 1 + 2 b(A)` de la dicotomía. [thm:golden/thm:DP; aureo.py A] -/
theorem fixed_point : 2 * bpocket phi * phi = 1 + 2 * bpocket phi := by
  decide +kernel

/-- (5) Factorización del punto fijo en ℤ[A]:
`2A(A+1)(A−1) − (A²+A+1) = (A²−A−1)(2A+1)`.
La ecuación del punto fijo se reduce al factor áureo `A² − A − 1` (raíz φ)
por un factor `2A + 1 > 0`. [thm:golden/thm:DP; aureo.py A] -/
theorem fixed_point_factor :
    PolyZ.eq
      (PolyZ.sub (PolyZ.mul (PolyZ.mul [0, 2] [1, 1]) [-1, 1]) [1, 1, 1])
      (PolyZ.mul [-1, -1, 1] [1, 2]) = true := by
  decide +kernel

/-- (6) Certificado exacto del testigo: `f(s)(1 + 4φ²) = 4φ` exactamente en
`s* = 4(√5 − 2)`, con `f(s) = s/(φ² − s)`.  La corona del trío `{φ, s, s}`
existe sii `s < s*`. [thm:golden, acta del 2º dictamen; aureo.py A] -/
theorem witness_cert :
    (sstar / (phi ^ 2 - sstar)) * (1 + 4 * phi ^ 2) = 4 * phi := by
  decide +kernel

/-- (7a) `8φ + 5 = (2 + √5)²`: paso de la cadena del certificado del
testigo. [thm:golden; aureo.py A] -/
theorem eight_phi : 8 * phi + 5 = (2 + sqrt5) ^ 2 := by decide +kernel

/-- (7b) `φ³ = 2 + √5`: paso de la cadena del certificado del testigo
(`s(8φ+5) < 4φ³` ⟺ `s < s*`). [thm:golden; aureo.py A] -/
theorem phi_cubed : phi ^ 3 = 2 + sqrt5 := by decide +kernel

/-- (8) `4φ(√5 − φ) = 4`: el margen `s* − φ/2·(…)` del testigo es exacto;
fija el ε₀ de la familia. [thm:golden; aureo.py A] -/
theorem eps0_margin : 4 * phi * (sqrt5 - phi) = 4 := by decide +kernel

/-- (9) La ventana de ω es no vacía: `1 − φ/2 < φ − 1` en el orden real de
`Q5` (≈ 0.191 < 0.618). [thm:golden; aureo.py A] -/
theorem window : 1 - phi / 2 < phi - 1 := by decide +kernel

/-!
## Batalla 2 / Teorema P — suelo áureo con u = sartén
(`thm:DP`; script `code/batalla2.py`, bloque A)
-/

/-- (10a) `2·b(φ) = φ`: el bolsillo de φ es φ/2, forma equivalente del punto
fijo. [thm:DP; batalla2.py A] -/
theorem two_b_phi : 2 * bpocket phi = phi := by decide +kernel

/-- (10b) `g(φ) = (1 + 2 b(φ))/φ = φ`: el cociente de la dicotomía del caso
j = 1 vale exactamente φ en φ. [thm:DP; batalla2.py A] -/
theorem g_phi : (1 + 2 * bpocket phi) / phi = phi := by decide +kernel

/-- (11) Certificado de que `g(A) = (1 + 2b(A))/A` es decreciente:
`(3A² + 3A + 1)(A² + A + 1) − 2A(2A + 1) = 3A⁴ + 6A³ + 3A² + 2A + 1`,
cuyo lado derecho tiene TODOS los coeficientes ≥ 0 y término independiente 1;
en particular es > 0 para todo A ≥ 0, que es el numerador de `−g'` salvo
factores positivos. [thm:DP; batalla2.py A] -/
theorem g_decreasing_cert :
    PolyZ.eq
      (PolyZ.sub (PolyZ.mul [1, 3, 3] [1, 1, 1]) (PolyZ.mul [0, 2] [1, 2]))
      [1, 2, 3, 6, 3] = true
    ∧ ([1, 2, 3, 6, 3] : PolyZ).all (fun c => decide (0 ≤ c)) = true
    ∧ ([1, 2, 3, 6, 3] : PolyZ).getD 0 0 = 1 := by
  decide +kernel

/-!
### El patrón de eliminación de raíces cuadradas

Los programas Ψ del paper devuelven `(1 − ω) + √((1 − ω)² + c)`.  En `Q5` no
hay raíz cuadrada general, pero para valores concretos la identidad
`Ψ(ω) = v` se certifica con el patrón:

  `x := v − (1 − ω)` cumple `x² = (1 − ω)² + c`  y  `x > 0`,

es decir, `x` ES la raíz cuadrada positiva requerida, y entonces
`(1 − ω) + x = v`.  Los teoremas 12–14 instancian este patrón.
-/

/-- El valor `x = φ − 1/2 = √5/2`, la raíz que necesita `Ψ(1/2)`. -/
def xhalf : Q5 := phi - Q5.ofRat (1/2)

/-- (12) `Ψ(1/2) = φ`: con `x = φ − 1/2` se tiene `x² = (1 − 1/2)² + 1`,
`x > 0` y `(1 − 1/2) + x = φ`.  (Patrón de eliminación de la raíz.)
[thm:DP, caso j = 1 en ω = 1/2; batalla2.py A] -/
theorem Psi_half :
    xhalf ^ 2 = Q5.ofRat ((1 - 1/2) ^ 2 + 1)
    ∧ 0 < xhalf
    ∧ Q5.ofRat (1 - 1/2) + xhalf = phi := by
  decide +kernel

/-- (13) `Ψ_B(1) = φ`: `(2φ − 1)² = 5`, `2φ − 1 > 0` (o sea `2φ − 1 = √5`),
y `((2 − 1) + (2φ − 1))/2 = φ`.  La rama B de la evacuación toca φ en su
extremo. [thm:DP, rama B; batalla2.py A] -/
theorem PsiB_one :
    (2 * phi - 1) ^ 2 = 5
    ∧ 0 < 2 * phi - 1
    ∧ ((2 - 1) + (2 * phi - 1)) / 2 = phi := by
  decide +kernel

/-- (14) `Ψ₂(φ/2) = φ`: `((3/2)φ − 1)² = (1 − φ/2)² + 2`, `(3/2)φ − 1 > 0`
y `(1 − φ/2) + ((3/2)φ − 1) = φ`.  El programa de j = 2 toca φ en ω = φ/2.
[thm:DP, rama A j = 2; batalla2.py A] -/
theorem Psi2_goldenhalf :
    (Q5.ofRat (3/2) * phi - 1) ^ 2 = (1 - phi / 2) ^ 2 + 2
    ∧ 0 < Q5.ofRat (3/2) * phi - 1
    ∧ (1 - phi / 2) + (Q5.ofRat (3/2) * phi - 1) = phi := by
  decide +kernel

/-- (15) `Ψ₃(1) = √3 > φ`: equivale a `3 > φ²` (ambos lados positivos).
El programa de j = 3 queda estrictamente por encima de φ. [thm:DP, rama A
j = 3; batalla2.py A] -/
theorem Psi3_gt_phi : phi ^ 2 < 3 := by decide +kernel

/-!
## Suelo Tribonacci y esquina 13/7
(`thm:rigidfloor`, `thm:corner`; scripts `code/striple.py`, `code/cuadrado.py`,
`code/esquina.py`)
-/

/-- (16) `P(φ) = φ³ − φ² − φ − 1 = −1 < 0`: por tanto φ < T (T es la única
raíz real de P y P es creciente en x ≥ 1, teorema `P_mono_cert`).
[thm:rigidfloor; striple.py] -/
theorem P_phi : phi ^ 3 - phi ^ 2 - phi - 1 = -1 := by decide +kernel

/-- (17) Encajonamiento de T a 4 decimales, en ℚ puro:
`P(1.8392) < 0 < P(1.8393)`, luego `1.8392 < T < 1.8393` (con la monotonía
de `P_mono_cert`). [thm:rigidfloor; striple.py] -/
theorem T_bracket :
    PRat (18392/10000) < 0 ∧ 0 < PRat (18393/10000) := by
  decide +kernel

/-- El cociente exacto `Q(e, d)` con `P(1+e+d) − P(1+e) = d·Q(e, d)`:
`Q = (4e + 3e²) + (2 + 3e)·d + d²`, como elemento de (ℚ[e])[d].
(Derivado con sympy antes de escribirlo; el teorema verifica la identidad.) -/
def QCert : Poly2 := [[0, 4, 3], [2, 3], [1]]

/-- Tribonacci en (ℚ[e])[d]: `P(x) = x³ − x² − x − 1` para `x : Poly2`. -/
def Ptri2 (x : Poly2) : Poly2 :=
  Poly2.sub (Poly2.sub (Poly2.sub (Poly2.mul (Poly2.mul x x) x) (Poly2.mul x x)) x) [[1]]

/-- (18) Certificado de monotonía estricta de P en `x ≥ 1`:

`P(1+e+d) − P(1+e) = d · Q(e,d)` con `Q = (4e+3e²) + (2+3e)d + d²`,

donde (i) la identidad se verifica como polinomios bivariados en (ℚ[e])[d]
(`x = 1+e+d = [[1,1],[1]]`, `1+e = [[1,1]]`, `d = [[],[1]]`), (ii) todos los
coeficientes de Q son ≥ 0, y (iii) el coeficiente de `d¹` tiene término
constante 2 > 0.  Para `e ≥ 0, d > 0` esto da `Q(e,d) ≥ 2d > 0`, luego
`P(1+e+d) > P(1+e)`: P es estrictamente creciente en `[1, ∞)`.  Con (16) y
(17) sitúa `φ < T` y `1.8392 < T < 1.8393`. [thm:rigidfloor; striple.py] -/
theorem P_mono_cert :
    Poly2.eq (Poly2.sub (Ptri2 [[1, 1], [1]]) (Ptri2 [[1, 1]]))
      (Poly2.mul [[], [1]] QCert) = true
    ∧ Poly2.allNonneg QCert = true
    ∧ (0 : Rat) < (QCert.getD 1 []).getD 0 0 := by
  decide +kernel

/-- (19) `γ_{2/7} = 2`: `2³ = 2² + 2 + (2/7)(2² + 2 + 1)`; el parámetro 2
está en la familia del carve-out de la esquina. [thm:corner; esquina.py] -/
theorem gamma_27 :
    (2 : Rat) ^ 3 = 2 ^ 2 + 2 + (2/7) * (2 ^ 2 + 2 + 1) := by
  decide +kernel

/-- (20) La esquina: `1 + b(2) = 13/7` (con `b(2) = 6/7`); el ínfimo global
de T_can es 13/7, alcanzado en la esquina `(ω, α, σ₂) = (1/7, 2, 6/7)`.
[thm:corner; esquina.py] -/
theorem corner_137 : 1 + bQ 2 = 13/7 := by decide +kernel

/-- (21) Cobertura: `18393/20000 < 4√5 − 8` en el orden real de `Q5`.
Cadena: por (17) `T < 1.8393`, luego `T/2 < 18393/20000 < 4(√5 − 2) = s*`:
la mitad de Tribonacci queda por debajo del umbral del testigo, así que la
familia áurea cubre todo el rango relevante. [thm:golden + thm:rigidfloor;
aureo.py C] -/
theorem coverage : Q5.ofRat (18393/20000) < 4 * sqrt5 - 8 := by decide +kernel

/-!
## La pinza que cierra j = 3 en el intercambio a sartén
(`thm:DP` caso (iv); script `code/microcelda.py`, bloques [A] y [B])

La cadena enfrenta `v* > φ(3φ − s)` con `v* < φ²(2s + φ − 4)`, donde
`s = σ₂ + ω`.  Son incompatibles exactamente hasta `s* = 11 − 4√5`.
-/

/-- (23) `3/φ + 3 = 3φ`: la cota de las colas cruza φ exactamente en
`o₁ = 3`; es la identidad que fija los umbrales 3 y 3/φ del árbol de
casos. [thm:DP (iv); microcelda.py A] -/
theorem tail_crossing : 3 / phi + 3 = 3 * phi := by decide +kernel

/-- (24) `1/(2 − φ) = φ²`: el factor que despeja (C4). [thm:DP (iv)] -/
theorem inv_two_sub_phi : 1 / (2 - phi) = phi ^ 2 := by decide +kernel

/-- (25) La constante de la pinza: `s* = (6φ−1)/(2φ+1) = 11 − 4√5 = 15 − 8φ`.
Para `s ≤ s*` las cotas (C2) y (C4) son incompatibles.
[thm:DP (iv); microcelda.py A] -/
theorem pincer_constant :
    (6 * phi - 1) / (2 * phi + 1) = 11 - 4 * sqrt5
    ∧ (11 : Q5) - 4 * sqrt5 = 15 - 8 * phi := by
  decide +kernel

/-- (26) `s* > 2`: como `σ₂ ≤ 1` (el perfil son anillos menores que el
pivote) y `ω < 1` (convenio de anchura), siempre `s < 2 < s*`.
[thm:DP (iv)] -/
theorem pincer_applies : (2 : Q5) < 11 - 4 * sqrt5 := by decide +kernel

/-- (27) La contradicción en el extremo `s = 2`: la cota inferior es
`φ(3φ−2) = φ+3` y la superior `φ²(2·2+φ−4) = φ³ = 2φ+1`, y `φ³ < φ+3`
con margen exactamente `2 − φ`. [thm:DP (iv); microcelda.py B] -/
theorem pincer_gap :
    phi * (3 * phi - 2) = phi + 3
    ∧ phi ^ 2 * (2 * 2 + phi - 4) = phi ^ 3
    ∧ phi ^ 3 < phi + 3
    ∧ (phi + 3) - phi ^ 3 = 2 - phi := by
  decide +kernel

/-- (28) La rama sin hijo-nodo: si el agujero de `v*` fuese polvo puro,
(Bo) daría `v* < s + φ − 1`, incompatible con (C2) mientras
`s ≤ (2φ+4)/φ² = 2.7639…`, que también supera 2. [thm:DP (iv)] -/
theorem pincer_child : (2 : Q5) < (2 * phi + 4) / phi ^ 2 := by
  decide +kernel

/-!
## Perfiles mayores en la sartén (`thm:DPp`; script `code/perfilp.py`)
-/

/-- (29) Legalidad universal de los espejos en régimen pesado:
`φ − 1 < 2/3 = b(1) ≤ b(o₁)`, así que toda pieza `σ ≤ φ−1` cabe en un
bolsillo espejo de `{o₁, m}` para cualquier `o₁ ≥ 1`.
[thm:DPp (v)-(vi); perfilp.py A] -/
theorem mirror_legal : phi - 1 < Q5.ofRat (2/3) := by decide +kernel

/-- (30) La cadena del caso pesado-grande: `(φ−1) + 1 = φ`, y la
frontera del swap: `2 − ω > φ ⟺ ω < 2 − φ`, con `2 − φ = 1/φ²·…`;
aquí certificamos `(2 − φ) + φ = 2` y `2 − φ > 0`.
[thm:DPp (iii),(vi); perfilp.py A/C] -/
theorem heavy_chains :
    (phi - 1) + 1 = phi ∧ (2 - phi) + phi = 2 ∧ (0 : Q5) < 2 - phi := by
  decide +kernel

/-!
## El cierre de la región pesada (`thm:DPr`; script `code/rstar.py`)
-/

/-- (31) La pinza-con-Σ: la frontera `s' ≤ (φ−1)Σ + (16−9φ)` degenera en
`Σ = 1` a la constante `15 − 8φ = 11 − 4√5` del Teorema M, y sobre la
celda `sup(s' − (φ−1)Σ) = 5φ−7` queda bajo la frontera con margen
exacto `23 − 14φ > 0`. [thm:DPr (i); rstar.py A/B] -/
theorem pincer_sigma :
    (phi - 1) * 1 + (16 - 9 * phi) = 15 - 8 * phi
    ∧ (5 * phi - 7) < (16 - 9 * phi)
    ∧ (16 - 9 * phi) - (5 * phi - 7) = 23 - 14 * phi
    ∧ (0 : Q5) < 23 - 14 * phi := by
  decide +kernel

/-- (32) La esquina de frontera de `p ≥ 4, j = 2`: en `σ₁ = 1, W = 0`
las colas dan `o₂ = 2/φ`, `o₁ = 2`, `R̄ = 2φ`, el par `{o₁, o₂}` es
diametral exacto (`f(o₁)f(o₂) = 1`) y los dos arcos de `m` suman `π`:
`sin²(θ/2)` valen `1/2 ∓ √5/10` y suman `1`.  La esquina está FUERA del
dominio (perfil < 1 estricto, pesado exige `σ₁+W > 1`): el interior
queda estrictamente bajo `π`. [thm:DPr (iv); rstar.py A2] -/
theorem corner_pi :
    ((2 : Q5) / phi) / (2 * phi - 2 / phi) * (1 / (2 * phi - 1))
      = Q5.ofRat (1/2) - sqrt5 / 10
    ∧ (1 / (2 * phi - 1)) * (2 / (2 * phi - 2))
      = Q5.ofRat (1/2) + sqrt5 / 10
    ∧ ((2 : Q5) / phi) / (2 * phi - 2 / phi) * (1 / (2 * phi - 1))
      + (1 / (2 * phi - 1)) * (2 / (2 * phi - 2)) = 1
    ∧ (2 / (2 * phi - 2)) * ((2 / phi) / (2 * phi - 2 / phi)) = 1 := by
  decide +kernel

/-!
## Lema de dualidad/zigzag y ensamblaje
(`docs/drafts/zigzag.md`, `docs/drafts/ensamblaje.md`;
scripts `code/zigzag.py` bloque A, `code/ensamblaje.py` bloques A/F)
-/

/-- (33) DIC áurea, discriminante de Descartes CERO: con curvaturas
`k_a = 1/φ`, `k_b = 1`, `k_w = −1/(φ+1)` (pared cóncava),
`k_a·k_b + k_b·k_w + k_w·k_a = 0`: el bolsillo del par `{φ, 1}` en el
disco `R = φ+1` es la tangencia crítica del modelo. [zigzag.py A] -/
theorem descartes_disc_zero :
    (1 / phi) * 1 + 1 * (-(1 / (phi + 1)))
      + (-(1 / (phi + 1))) * (1 / phi) = 0 := by
  decide +kernel

/-- (34) El radio del bolsillo áureo: con disc = 0,
`k_p = k_a + k_b + k_w = 2/φ` y el radio es `1/k_p = φ/2` — exactamente
el `b₂(φ,1)` de la rigidez y el σ crítico del contraejemplo.
[zigzag.py A] -/
theorem descartes_pocket_golden :
    1 / (1 / phi + 1 - 1 / (phi + 1)) = phi / 2 := by
  decide +kernel

/-- (35) NS-2 áurea es IGUALDAD: con `R = φ+1` y `f(x) = x/(R−x)`,
`f(φ)·f(φ/2) + f(1)·f(φ/2) = 1` y `f(φ)·f(1) = 1` (par diametral):
`θ(φ, φ/2) + θ(φ/2, 1) = π = θ(φ, 1)`.  El margen NS-2 se anula en
`s = φ/2` = bolsillo de Descartes: la dicotomía hueco/muro reconoce el
contraejemplo como su punto crítico exacto. [zigzag.py A/E] -/
theorem ns2_golden :
    (phi / (phi + 1 - phi)) * ((phi / 2) / (phi + 1 - phi / 2))
      + (1 / (phi + 1 - 1)) * ((phi / 2) / (phi + 1 - phi / 2)) = 1
    ∧ (phi / (phi + 1 - phi)) * (1 / (phi + 1 - 1)) = 1 := by
  decide +kernel

/-- (36) La línea áurea de la herencia (N): `φ² − φ/2 = 1 + φ/2` y
`φ < 1 + φ/2`: la celda (N) con j = 1 cierra para todo `ω ≤ 1` al nivel
áureo (lema-extensión, C4). [ensamblaje.py F] -/
theorem golden_line_N :
    phi ^ 2 - phi / 2 = 1 + phi / 2 ∧ phi < 1 + phi / 2 := by
  decide +kernel

/-- (37) La esquina áurea del muro espejo: `b₂(2, √5−1) = 1` exacto
(numerador y denominador valen 8). [thm:DP (ii); ensamblaje.py A] -/
theorem b2_mirror_corner : b2 2 (sqrt5 - 1) = 1 := by decide +kernel

/-- (38) El lema de respiración fuerte (las dos ramas de agujero del
puerto): `φ(3−φ) = 2φ−1 = √5` y `√5 − (φ−1) = φ` — la I2 completa con
la pared `Σ_S > 1` da `X_Y + ω > √5`, el polvo se descuenta con
`< φ−1`, y la masa `> m` conserva EXACTAMENTE el umbral áureo
`X_{>m} + ω > φ`. [coronaagujero.py A(3)] -/
theorem strong_breathing :
    phi * (3 - phi) = 2 * phi - 1 ∧ 2 * phi - 1 = sqrt5
      ∧ sqrt5 - (phi - 1) = phi := by
  decide +kernel

/-- (39) El trío π áureo: con `f(x) = x/(2φ−x)`, los productos de
senos cuadrados del trío `{φ, 1/φ, 1}` en `R = 2φ` son
`x₁ = f(φ)f(1/φ) = √5−2`, `x₂ = f(1/φ)f(1) = 1−2√5/5`,
`x₃ = f(1)f(φ) = √5/5`, y la identidad de adición de senos
`sin(A+B) = cos C` (A, B, C = las mitades de los tres ángulos)
se reduce a las dos igualdades algebraicas de abajo:
`√(x₁x₂(1−x₁)(1−x₂)) = (7√5−15)/5` (cuadrado exacto, con
`7√5 > 15`) y `x₁(1−x₂) + x₂(1−x₁) + 2·(7√5−15)/5 = 1−x₃`.
Consecuencia: `θ(φ,1/φ) + θ(1/φ,1) + θ(1,φ) = π` EXACTO en
`R = 2φ` — la tangencia del punto peligroso de j = 1 (bolsillos
fase 2) y el 5-ciclo con `s′ = φ/2` en la constante de R2b.
[bolsillos.py C(d2); acta 2026-08-09] -/
theorem golden_pi_trio :
    ((7 * sqrt5 - 15) / 5) ^ 2
      = (sqrt5 - 2) * (1 - 2 * sqrt5 / 5)
        * (3 - sqrt5) * (2 * sqrt5 / 5)
    ∧ (sqrt5 - 2) * (2 * sqrt5 / 5)
        + (1 - 2 * sqrt5 / 5) * (3 - sqrt5)
        + 2 * ((7 * sqrt5 - 15) / 5)
      = 1 - sqrt5 / 5
    ∧ 7 * sqrt5 - 15 > 0 := by
  decide +kernel

/-- (40) El umbral del lema de reducción de |A| (las pesadas de R2b):
`t₀ = (φ−1)/4 = 1/(4φ)` (por `φ(φ−1) = 1`), y con `β* = (9−√5)/8`
las dos igualdades críticas de la dicotomía son EXACTAS:
`5t₀ = φ − β*` (cinco piezas grandes agotan la masa de A) y
`4t₀ = φ − 1` (cuatro grandes y polvo son incompatibles: el mural
pesado real tiene ≤ 6 nodos). [areduccion.py A; acta 2026-08-10] -/
theorem golden_reduction_threshold :
    (phi - 1) / 4 = 1 / (4 * phi)
      ∧ 5 * ((phi - 1) / 4) = phi - (9 - sqrt5) / 8
      ∧ 4 * ((phi - 1) / 4) = phi - 1 := by
  decide +kernel

/-- (41) El bolsillo del par diametral (la variedad ESP `X_Y > 0`):
la frontera de la corona en el suelo de convivencia es
`x*(z) = z(z+1)/(z²+z+1)`, y en `z = φ` todo es áureo:
`φ² + φ + 1 = 2φ²` (la anchura del sliver es `1/(2φ²)`),
`φ(φ+1) = (φ/2)(φ²+φ+1)` (es decir `x*(φ) = φ/2` — el bolsillo
áureo de thm:DP como frontera, y el mecanismo de la protección de
σ₂ por la pared de masa), y `φ(4−φ) = 3φ−1` (el umbral de
no-rescate de cola en `x = 1`; en `x = 0` es `φ(3−φ) = √5`, el
(38)). [espxy.py A; acta 2026-08-10] -/
theorem diametral_pocket_golden :
    phi ^ 2 + phi + 1 = 2 * phi ^ 2
      ∧ phi * (phi + 1) = (phi / 2) * (phi ^ 2 + phi + 1)
      ∧ phi * (4 - phi) = 3 * phi - 1 := by
  decide +kernel

/-- (42) El trío prohibido y la cúbica áurea (la vacuidad F3):
(a) `2·(φ/2) = φ` — tres piezas con las dos siguientes `≥ (φ/2)·mayor`
violan `ρ ≤ φ` (la cola de la mayor suma ya `φ` veces su radio): el
gap de dualidad exige tres tops comparables y la cascada los prohíbe.
(b) La identidad polinomial de la CÚBICA ÁUREA en `(ℚ[√5])[r]`:
`r(1+r+r²) + r(1+r) − φ(1+r+r²) = r³ + (2−φ)r² + (2−φ)r − φ`
— es decir, `r + q(r) = φ ⟺` la cúbica, con
`q(r) = r(1+r)/(1+r+r²)` el bolsillo normalizado del par dominante
(su raíz real `r* ≈ 0.9637` marca el techo infinito del sub-bolsillo
forzado; `q(1) = 2/3`: conjunto (c)).
(d) El techo en el borde de la celda: `q(9/10) = 171/271` exacto
(`(9/10)(19/10) = (171/271)(271/100)`) y
`φ − 9/10 − 171/271 < 25/83` con el denominador positivo — es decir
`2/(φ − 9/10 − q(9/10)) > 166/25 = 6.64`, el dominio real del
generador: el sub-bolsillo queda forzado en toda la celda.
[auditcolas.py A, f3vacio.py A-B; actas 2026-08-10] -/
theorem forbidden_triple_cubic :
    2 * (phi / 2) = phi
    ∧ Poly5.eq
        (Poly5.add (Poly5.mul [0, 1] [1, 1, 1])
          (Poly5.add [0, 1, 1]
            (Poly5.neg (Poly5.smul phi [1, 1, 1]))))
        [-phi, 2 - phi, 2 - phi, 1] = true
    ∧ (1 : Q5) * (1 + 1) * 3 = (2 : Q5) * (1 + 1 + 1)
    ∧ (9 : Q5) / 10 * (19 / 10) = (171 / 271) * (271 / 100)
    ∧ (0 : Q5) < phi - 9 / 10 - 171 / 271
    ∧ phi - 9 / 10 - 171 / 271 < 25 / 83 := by
  decide +kernel

/-!
## Umbral aditivo (modelo aditivo; scripts `code/umbral.py`, `code/frontera.py`)
-/

/-- (22) La familia del umbral aditivo, como identidad de polinomios en δ:
con `r₁ = 1` y `s = 1/2`,
`((1/4 + 2δ/3) + (1/4 + δ/3)) / (1/2) = 1 + 2δ`
(dividir por 1/2 = multiplicar por 2).  En listas de coeficientes:
`[2] · ([1/4, 2/3] + [1/4, 1/3]) = [1, 2]`. [umbral aditivo; umbral.py] -/
theorem additive_family :
    Poly.eq (Poly.mul [2] (Poly.add [1/4, 2/3] [1/4, 1/3])) [1, 2] = true := by
  decide +kernel

/-!
## Campaña 3d–3i: el canal k ≥ 2 (scripts `code/lemaA4.py`, `code/lemaA5.py`)

Las identidades exactas de los gates nuevos: la pendiente del tramo
superior de la cola `W_z` (gate A8), el coeficiente del numerador del
crítico, y la constante de masa del sello pesado (`MASA_A_MAX`).
-/

/-- (23) `cp := 2/φ = √5 − 1`: la pendiente del tramo superior del
minorante de capacidad en la cola `W_z` (el techo `Rz` acopla
`W_z ≥ z − C₀`, gate A8). [lemaA4 A8; ciclo 3e] -/
theorem cp_closed : (2 : Q5) / phi = sqrt5 - 1 := by decide +kernel

/-- (23b) `cp > 1`: el tramo superior tiene pendiente mayor que uno —
por eso los críticos de `log p` pasan de mínimos (A6) a máximos (A8) y
aparece el crítico interior `z*`. [lemaA4 A8] -/
theorem cp_gt_one : (1 : Q5) < 2 / phi := by decide +kernel

/-- (24) `cp(cp − 1) = 7 − 3√5`: el denominador de la forma cerrada del
crítico `z*² = Dp(Dp − v)/(cp(cp − 1))`. [lemaA4 A8; ciclo 3e] -/
theorem cp_prod : (2 / phi) * (2 / phi - 1) = 7 - 3 * sqrt5 := by
  decide +kernel

/-- (24b) `(6 + 2√5)(7 − 3√5) = 12 − 4√5`: el factor positivo del
numerador de `S` por el denominador del crítico — el coeficiente de
`z²` en el numerador, verificado en el gate. [lemaA4 A8] -/
theorem num_coeff : ((6 : Q5) + 2 * sqrt5) * (7 - 3 * sqrt5)
    = 12 - 4 * sqrt5 := by decide +kernel

/-- (25) `2φ/3 < 1079/1000`: la constante `MASA_A_MAX = 1.079` del
canal pesado mayora la masa máxima del bloque `A` (el extremo
`masa_A ≤ 2φ/3`, alcanzado en `b = φ/3` con `|A| = 2`; MENOR del
sello 3h). [lemaA5; sello de la ronda triple] -/
theorem masa_A_max : 2 * phi / 3 < Q5.ofRat (1079/1000) := by
  decide +kernel

/-- (25b) El extremo es genuino: con `b = φ/3` y `|A| = 2`, la masa
`2(1 − b) = 2 − 2φ/3` queda estrictamente bajo el techo
`min(2b, φ − b) = 2φ/3` — equivalente a `φ > 3/2`.
[lemaA5; derivación del referee en el sello 3h] -/
theorem masa_A_extremo :
    (2 : Q5) - 2 * phi / 3 < 2 * phi / 3
    ∧ (2 : Q5) * (phi / 3) = phi - phi / 3 := by decide +kernel

/-- (26) La cota del desborde del testigo greedy de `thm:D1written`
(el cierre del gap `σ₁+σ₂ ≤ 1`, hallado por la revisión externa):
la parte de identidad — `(φ − s₂ − B) − ((φ−1) − (s₂ − s₃)) = 1 − B − s₃`
como identidad de polinomios en `B` con parámetros desplazados: en
listas de coeficientes sobre ℚ (la parte √5 se cancela),
`([1] − [B]) = [1, -1]` aplicado a la instancia del spot-check
`(s₂, s₃) = (38/100, 33/100)`:
`(φ − 38/100 − 93/100) < (φ − 1) − (38/100 − 33/100)`. [thm:D1written;
sello de la revisión externa, ronda 4] -/
theorem spill_spotcheck :
    phi - Q5.ofRat (38/100) - Q5.ofRat (93/100)
      < (phi - 1) - (Q5.ofRat (38/100) - Q5.ofRat (33/100))
    ∧ (phi - 1) - (Q5.ofRat (38/100) - Q5.ofRat (33/100))
      < phi - 1 := by decide +kernel

/-- (26b) `φ − 1 = 1/φ`: el techo de la cota del desborde es el
inverso áureo — ambos radios insertados quedan bajo los tamaños
certificados. [thm:D1written] -/
theorem phi_inv : phi - 1 = 1 / phi := by decide +kernel

/-!
## quintetocert: el certificado sin tolerancias del quinteto j = 1
(thm:gapwritten; script `code/quintetocert.py`)
-/

/-- (27) stack_golden: el margen del testigo apilado en el punto
aureo (phi, phi, phi) — dist² − (w*+α)² = 1/φ³ en la forma entera
`2φ⁴ − (φ+2)² = φ − 1`. [quintetocert P5] -/
theorem stack_golden : (2 : Q5) * phi^4 - (phi + 2)^2 = phi - 1 := by
  decide +kernel

/-- (27b) p_half_mid: la colocacion media de m es legal en el punto
aureo — f(φ)·f(1) en R = 2φ vale 1/√5 (`2φ − 1 = √5`), y
1/√5 ≤ 1/2 porque √5 ≥ 2. [quintetocert P5] -/
theorem p_half_mid : (2 : Q5) * phi - 1 = sqrt5 := by decide +kernel

/-- (27c) `√5 ≥ 2` en Q5 (⟹ 1/√5 ≤ 1/2: el criterio del arco
medio). [quintetocert P5] -/
theorem sqrt5_ge_two : (2 : Q5) ≤ sqrt5 := by decide +kernel

/-- (28) semiarc_golden: el umbral racional del semiarco vale
exactamente m = 1 en el punto W2 — `1 + f(2/φ) + f(2) = 1 + √5` en
R = 1+√5: `(√5−1)/2 + (√5+1)/2 + 1 = √5 + 1`. La configuracion
critica de thm:golden reaparece como testigo tangente-legal.
[quintetocert P6] -/
theorem semiarc_golden :
    (1 : Q5) + (sqrt5 - 1)/2 + (sqrt5 + 1)/2 = sqrt5 + 1 := by
  decide +kernel

end Calamares
