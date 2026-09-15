import Calamares.UniformExchange
import Calamares.VariableWidth

/-! Algebraic certificates for the uniform reservoir argument.
The area union bound, forest assembly and counting are written proofs.
-/

namespace Calamares.Reservoir

open Std Lean.Grind
open Calamares.VariableWidth

theorem golden_lt_five_thirds {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (phi : K) (heq : phi*phi = phi+1) : 3*phi < 5 := by
  by_cases h : 3*phi < 5
  · exact h
  have := OrderedRing.mul_nonneg (a := 3*phi-5) (b := 3*phi+2) (by grind) (by grind)
  grind

theorem squares_le_cap_mass {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (xs : List K) (b : K) (h : ∀ x ∈ xs, 0 ≤ x ∧ x ≤ b) :
    squares xs ≤ b * mass xs := by
  induction xs with
  | nil => simp only [squares, mass]; grind
  | cons x xs ih =>
    have hx := h x (by simp)
    have ht : ∀ y ∈ xs, 0 ≤ y ∧ y ≤ b := by
      intros y hy
      exact h y (by simp [hy])
    have hs := ih ht
    have hp := OrderedRing.mul_nonneg (a := x) (b := b-x) (by grind) (by grind)
    simp only [squares, mass]
    grind

theorem two_slot_margin {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (a b c m n : K) (hm : 0 < m) (hab : b ≤ a) (hb : 9*m ≤ b)
    (hc1 : 3*c ≤ 5*b-6*m) (hc2 : 3*c ≤ 5*a-3*b-6*m)
    (hn : 3*n*m ≤ 5*b) :
    0 < 2*a*b-(b+2*m)*c-4*m*(a+b)-(n+3)*m*m := by
  have hm2 := OrderedRing.mul_pos hm hm
  have hx : 0 ≤ b-9*m := by grind
  have hxx := OrderedRing.mul_nonneg hx hx
  have hmx := OrderedRing.mul_nonneg (a := m) (by grind) hx
  have hf : 0 < 23*b*b-201*b*m+15*m*m := by grind
  have hg : 0 < 4*b*b-27*b*m+3*m*m := by grind
  have hb2 : 0 ≤ b+2*m := by grind
  have hcn := OrderedRing.mul_nonneg (a := 5*b-3*n*m) (b := m) (by grind) (by grind)
  by_cases ha : 8*b ≤ 5*a
  · have hc := OrderedRing.mul_nonneg (a := 5*b-6*m-3*c) (b := b+2*m) (by grind) hb2
    have hx := OrderedRing.mul_nonneg (a := 5*a-8*b) (b := b-2*m) (by grind) (by grind)
    grind
  · have hc := OrderedRing.mul_nonneg (a := 5*a-3*b-6*m-3*c) (b := b+2*m) (by grind) hb2
    by_cases hl : b ≤ 22*m
    · have hx := OrderedRing.mul_nonneg (a := 8*b-5*a) (b := 22*m-b) (by grind) (by grind)
      grind
    · have hx := OrderedRing.mul_nonneg (a := a-b) (b := b-22*m) (by grind) (by grind)
      grind

theorem clearance_area_margin {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (r a b c q m n : K) (hr : a+b ≤ r) (hpos : m ≤ a+b)
    (hq : q ≤ b*c)
    (hmargin : 0 < 2*a*b-(b+2*m)*c-4*m*(a+b)-(n+3)*m*m) :
    (a+m)*(a+m)+(b+m)*(b+m)+q+2*m*c+(n-2)*m*m+4*m*m <
      (r-m)*(r-m) := by
  have hp := OrderedRing.mul_nonneg (a := r-a-b) (b := r+a+b-2*m)
    (by grind) (by grind)
  grind

-- Coordinates multiplied by 2: the two new disks have radius b,
-- centers (-b,y) and (b,y); the old disks have centers (-2*b,0), (2*a,0).
theorem upper_half_slots {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (a b y : K) (hb : 0 < b) (hab : b ≤ a) (hy : 0 ≤ y)
    (hy2 : y*y = 4*a*(a+b)) :
    b*b+y*y = (2*a+b)*(2*a+b) ∧
    (2*a+b)*(2*a+b) ≤ (3*b)*(3*b)+y*y ∧
    (3*b)*(3*b) ≤ (-b-2*a)*(-b-2*a)+y*y ∧
    (3*b)*(3*b) ≤ (b-2*a)*(b-2*a)+y*y ∧
    (b-(-b))*(b-(-b)) = (2*b)*(2*b) ∧ b < y := by
  have hbb := OrderedRing.mul_pos hb hb
  have hprod := OrderedRing.mul_nonneg (a := a-b) (b := a+b) (by grind) (by grind)
  have habprod := OrderedRing.mul_nonneg (a := a) (b := b) (by grind) (by grind)
  have hyy : b < y := by
    by_cases h : b < y
    · exact h
    have hp := OrderedRing.mul_nonneg (a := b-y) (b := b+y) (by grind) (by grind)
    grind
  grind

theorem six_radii_exceed_cutoff {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (m a b c d e f : K) (hm : 0 < m)
    (ha : 3*(b+c+d+e+f+2*m) ≤ 5*a)
    (hb : 3*(c+d+e+f+2*m) ≤ 5*b)
    (hc : 3*(d+e+f+2*m) ≤ 5*c)
    (hd : 3*(e+f+2*m) ≤ 5*d)
    (he : 3*(f+2*m) ≤ 5*e)
    (hf : 6*m ≤ 5*f) : 9*m < a := by
  grind

theorem no_six_unary_nodes {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (m w a b c d e f : K) (hm : 0 < m) (hw : 0 ≤ w) (hf : m ≤ f)
    (hab : a ≤ b+w+2*m) (hbc : b ≤ c+w+2*m)
    (hcd : d+w ≤ c) (hde : e+w ≤ d) (hef : f+w ≤ e)
    (ht : 3*(b+c+d+e+f+2*m) ≤ 5*a) : False := by
  grind

#print axioms golden_lt_five_thirds
#print axioms squares_le_cap_mass
#print axioms two_slot_margin
#print axioms clearance_area_margin
#print axioms upper_half_slots
#print axioms six_radii_exceed_cutoff
#print axioms no_six_unary_nodes

end Calamares.Reservoir
