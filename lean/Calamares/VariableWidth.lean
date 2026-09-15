prelude
import Init.Grind.Ring
import Init.Grind.Ordered
import Init.Grind.Order
import Init.Grind.Tactics

/-! Algebraic certificates for independent hole radii.
The forest exchange and tail-capture lemma remain written proofs.
No geometric or greedy-optimality statement is assumed here.
-/

namespace Calamares.VariableWidth

open Std Lean.Grind

def mass {K : Type u} [Zero K] [Add K] : List K → K
  | [] => 0
  | x :: xs => x + mass xs

def squares {K : Type u} [Zero K] [Add K] [Mul K] : List K → K
  | [] => 0
  | x :: xs => x*x + squares xs

theorem mass_nonneg {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (xs : List K) (h : ∀ x ∈ xs, 0 ≤ x) : 0 ≤ mass xs := by
  induction xs with
  | nil => simp [mass]
  | cons x xs ih =>
    have hx : 0 ≤ x := h x (by simp)
    have ht : ∀ y ∈ xs, 0 ≤ y := by intros y hy; exact h y (by simp [hy])
    have := ih ht
    simp only [mass]
    grind

theorem sum_squares_le_mass_sq {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (xs : List K) (h : ∀ x ∈ xs, 0 ≤ x) : squares xs ≤ mass xs * mass xs := by
  induction xs with
  | nil => simp only [squares, mass]; grind
  | cons x xs ih =>
    have hx : 0 ≤ x := h x (by simp)
    have ht : ∀ y ∈ xs, 0 ≤ y := by intros y hy; exact h y (by simp [hy])
    have hs := ih ht
    have hm := mass_nonneg xs ht
    have hp := OrderedRing.mul_nonneg hx hm
    simp only [mass, squares]
    grind

theorem area_pressure {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (r h t c b : K) (hh : 0 ≤ h) (hht : h < t) (hc : 0 ≤ c)
    (hb : b ≤ t*t) (hr : (1+c)*(t*t) ≤ r*r) : c*b < r*r-h*h := by
  have hgap := OrderedRing.mul_pos (a := t-h) (b := t+h) (by grind) (by grind)
  have htail := OrderedRing.mul_nonneg (a := c) (b := t*t-b) hc (by grind)
  grind

theorem common_prefix {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (common a b c : K) (hp : 0 ≤ common) (hc : c ≤ 1)
    (ha : c*b < a) : c*(common+b) < common+a := by
  have := OrderedRing.mul_nonneg (a := 1-c) (b := common) (by grind) hp
  grind

theorem scaled_tail {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (r t k c : K) (hr : 0 ≤ r) (ht : 0 ≤ t) (hk : 0 ≤ k)
    (hc : 0 ≤ c) (htail : t ≤ k*r) (hfactor : (1+c)*(k*k) ≤ 1) :
    (1+c)*(t*t) ≤ r*r := by
  have hkr := OrderedRing.mul_nonneg hk hr
  have hgap := OrderedRing.mul_nonneg (a := k*r-t) (b := k*r+t) (by grind) (by grind)
  have hs : 0 ≤ k*r*(k*r)-t*t := by grind
  have hs_scaled := OrderedRing.mul_nonneg (a := 1+c) (by grind) hs
  have hrr := OrderedRing.mul_nonneg hr hr
  have hbound := OrderedRing.mul_nonneg (a := 1-(1+c)*(k*k)) (by grind) hrr
  grind

theorem sharp_family_identity {K : Type u} [CommRing K] (k e : K) :
    1-(k-e)*(k-e) = (1-k*k)+2*k*e-e*e := by grind

theorem thin_family_identity {K : Type u} [CommRing K] (e : K) :
    (1+e)*(1+e)-(1-e)*(1-e) = 4*e := by grind

#print axioms mass_nonneg
#print axioms sum_squares_le_mass_sq
#print axioms area_pressure
#print axioms common_prefix
#print axioms scaled_tail
#print axioms sharp_family_identity
#print axioms thin_family_identity

end Calamares.VariableWidth
