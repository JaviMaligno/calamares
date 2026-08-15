/-!
# Calamares.Basic — infraestructura de aritmética exacta

Capa de certificados exactos del paper de empaquetamiento de anillos:

* `Q5`: el cuerpo ℚ[√5] = ℚ[x]/(x²−5), representado como pares `(a b : Rat)`
  para `a + b·√5`.  Toda la aritmética es exacta sobre `Rat` (Lean core, sin
  mathlib) y todos los enunciados se deciden con `decide +kernel` (el kernel
  acelera `Nat.gcd`, así que la normalización de `Rat` reduce; el elaborador
  no, por eso `decide` a secas se atasca).
* El orden inducido por el encaje real con √5 ↦ +√5 > 0 (`Q5.posb`).
* Polinomios como listas de coeficientes ascendentes: `Poly` (ℚ[X]),
  `PolyZ` (ℤ[X]) y `Poly2` ((ℚ[e])[d], bivariados) para las identidades con
  variable libre y los certificados de coeficientes no negativos.

Sin `sorry`, sin axiomas nuevos: todo se demuestra por computación del kernel.
-/

namespace Calamares

/-- Elemento de ℚ[√5]: `⟨a, b⟩` representa `a + b·√5`.
La estructura es ℚ[x]/(x²−5) con la multiplicación
`(a,b)·(c,d) = (ac + 5bd, ad + bc)`. -/
structure Q5 where
  a : Rat
  b : Rat
deriving DecidableEq, Repr

namespace Q5

def add (x y : Q5) : Q5 := ⟨x.a + y.a, x.b + y.b⟩

def neg (x : Q5) : Q5 := ⟨-x.a, -x.b⟩

def sub (x y : Q5) : Q5 := ⟨x.a - y.a, x.b - y.b⟩

/-- `(a + b√5)(c + d√5) = (ac + 5bd) + (ad + bc)√5`. -/
def mul (x y : Q5) : Q5 := ⟨x.a * y.a + 5 * (x.b * y.b), x.a * y.b + x.b * y.a⟩

/-- Norma de cuerpo: `N(a + b√5) = a² − 5b²`. Es 0 sólo en el 0 (√5 ∉ ℚ). -/
def normSq (x : Q5) : Rat := x.a * x.a - 5 * (x.b * x.b)

/-- Inverso: `(a + b√5)⁻¹ = (a − b√5)/(a² − 5b²)`.
Convención `Rat`: dividir por 0 da 0, así que `inv 0 = 0` (nunca lo usamos). -/
def inv (x : Q5) : Q5 := ⟨x.a / x.normSq, -x.b / x.normSq⟩

def div (x y : Q5) : Q5 := x.mul y.inv

/-- Inclusión de ℚ en ℚ[√5]. -/
def ofRat (r : Rat) : Q5 := ⟨r, 0⟩

instance : Add Q5 := ⟨add⟩
instance : Neg Q5 := ⟨neg⟩
instance : Sub Q5 := ⟨sub⟩
instance : Mul Q5 := ⟨mul⟩
instance : Div Q5 := ⟨div⟩
instance : Coe Rat Q5 := ⟨ofRat⟩
instance (n : Nat) : OfNat Q5 n := ⟨⟨OfNat.ofNat n, 0⟩⟩

/-- Potencia natural (recursión estructural). -/
def pow (x : Q5) : Nat → Q5
  | 0 => 1
  | n + 1 => x * pow x n

instance : Pow Q5 Nat := ⟨pow⟩

/-!
## El orden del encaje real

`Q5.posb x` decide si `x.a + x.b·√5 > 0` en ℝ bajo el encaje que manda
`⟨0,1⟩` a la raíz POSITIVA √5.  Es aritmética exacta pura:

* `a ≥ 0, b ≥ 0`: positivo sii no es el cero.
* `a ≥ 0, b < 0`: `a > |b|√5  ⟺  a² > 5b²`.
* `a < 0, b ≥ 0`: `b√5 > −a  ⟺  5b² > a²`.
* `a < 0, b < 0`: nunca positivo.

`lt`/`le` se definen a partir de `posb`; es el orden total del subcuerpo
real ℚ(√5) ⊂ ℝ. -/
def posb (x : Q5) : Bool :=
  if 0 ≤ x.a then
    if 0 ≤ x.b then decide (¬(x.a = 0 ∧ x.b = 0))
    else decide (5 * (x.b * x.b) < x.a * x.a)
  else
    if 0 ≤ x.b then decide (x.a * x.a < 5 * (x.b * x.b))
    else false

instance : LT Q5 := ⟨fun x y => (y - x).posb = true⟩
instance : LE Q5 := ⟨fun x y => x = y ∨ x < y⟩

instance (x y : Q5) : Decidable (x < y) :=
  inferInstanceAs (Decidable ((y - x).posb = true))

instance (x y : Q5) : Decidable (x ≤ y) :=
  inferInstanceAs (Decidable (x = y ∨ x < y))

end Q5

/-- La razón áurea φ = (1 + √5)/2 como elemento de `Q5`. -/
def phi : Q5 := ⟨1/2, 1/2⟩

/-- √5 como elemento de `Q5` (la raíz positiva bajo el encaje real). -/
def sqrt5 : Q5 := ⟨0, 1⟩

/-!
## Polinomios como listas de coeficientes ascendentes

`[c₀, c₁, c₂, …]` representa `c₀ + c₁X + c₂X² + …`.  La igualdad se decide
normalizando (recortando ceros finales).  Tres instancias concretas, sin
typeclasses genéricas para mantener la reducción del kernel trivial:

* `Poly`  : ℚ[X]
* `PolyZ` : ℤ[X]  (para los certificados que el paper enuncia en ℤ[A])
* `Poly2` : (ℚ[e])[d] — bivariados, coeficientes en `d` que son polinomios
  en `e`; usados en el certificado de monotonía de P(x) = x³−x²−x−1.
-/

/-- Recorta los "ceros" finales de una lista (para normalizar polinomios). -/
def trimEnd {α : Type} (isZero : α → Bool) (p : List α) : List α :=
  (p.reverse.dropWhile isZero).reverse

/-! ### `Poly` : ℚ[X] -/

abbrev Poly := List Rat

namespace Poly

def add : Poly → Poly → Poly
  | [], q => q
  | p, [] => p
  | c :: p, d :: q => (c + d) :: add p q

def neg (p : Poly) : Poly := p.map Neg.neg

def sub (p q : Poly) : Poly := add p (neg q)

def smul (c : Rat) (p : Poly) : Poly := p.map (c * ·)

def mul : Poly → Poly → Poly
  | [], _ => []
  | c :: p, q => add (smul c q) ((0 : Rat) :: mul p q)

/-- Forma normal: sin ceros finales. -/
def norm (p : Poly) : Poly := trimEnd (fun c => decide (c = 0)) p

/-- Igualdad de polinomios (compara formas normales). -/
def eq (p q : Poly) : Bool := decide (norm p = norm q)

end Poly

/-! ### `Poly5` : (ℚ[√5])[X]

Coeficientes en `Q5`, para las identidades con variable libre y
constantes áureas (la cúbica áurea de la vacuidad F3). Mismo patrón
que `Poly`, sin typeclasses genéricas. -/

abbrev Poly5 := List Q5

namespace Poly5

def add : Poly5 → Poly5 → Poly5
  | [], q => q
  | p, [] => p
  | c :: p, d :: q => (c + d) :: add p q

def neg (p : Poly5) : Poly5 := p.map Q5.neg

def sub (p q : Poly5) : Poly5 := add p (neg q)

def smul (c : Q5) (p : Poly5) : Poly5 := p.map (c * ·)

def mul : Poly5 → Poly5 → Poly5
  | [], _ => []
  | c :: p, q => add (smul c q) ((0 : Q5) :: mul p q)

def norm (p : Poly5) : Poly5 := trimEnd (fun c => decide (c = (0 : Q5))) p

def eq (p q : Poly5) : Bool := decide (norm p = norm q)

end Poly5

/-! ### `PolyZ` : ℤ[X] -/

abbrev PolyZ := List Int

namespace PolyZ

def add : PolyZ → PolyZ → PolyZ
  | [], q => q
  | p, [] => p
  | c :: p, d :: q => (c + d) :: add p q

def neg (p : PolyZ) : PolyZ := p.map Neg.neg

def sub (p q : PolyZ) : PolyZ := add p (neg q)

def smul (c : Int) (p : PolyZ) : PolyZ := p.map (c * ·)

def mul : PolyZ → PolyZ → PolyZ
  | [], _ => []
  | c :: p, q => add (smul c q) ((0 : Int) :: mul p q)

def norm (p : PolyZ) : PolyZ := trimEnd (fun c => decide (c = 0)) p

def eq (p q : PolyZ) : Bool := decide (norm p = norm q)

end PolyZ

/-! ### `Poly2` : (ℚ[e])[d]

Lista de coeficientes en `d`; cada coeficiente es un `Poly` en `e`.
`[[0,4,3], [2,3], [1]]` = (4e+3e²) + (2+3e)·d + d². -/

abbrev Poly2 := List Poly

namespace Poly2

def add : Poly2 → Poly2 → Poly2
  | [], q => q
  | p, [] => p
  | c :: p, d :: q => (Poly.add c d) :: add p q

def neg (p : Poly2) : Poly2 := p.map Poly.neg

def sub (p q : Poly2) : Poly2 := add p (neg q)

def smul (c : Poly) (p : Poly2) : Poly2 := p.map (Poly.mul c)

def mul : Poly2 → Poly2 → Poly2
  | [], _ => []
  | c :: p, q => add (smul c q) (([] : Poly) :: mul p q)

/-- Forma normal: normaliza cada coeficiente y recorta los coeficientes
finales que son el polinomio cero. -/
def norm (p : Poly2) : Poly2 :=
  trimEnd (fun c => c.isEmpty) (p.map Poly.norm)

def eq (p q : Poly2) : Bool := decide (norm p = norm q)

/-- ¿Todos los coeficientes racionales del bivariado son ≥ 0? -/
def allNonneg (p : Poly2) : Bool :=
  p.all fun c => c.all fun r => decide (0 ≤ r)

end Poly2

end Calamares
