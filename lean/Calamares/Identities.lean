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

end Calamares
