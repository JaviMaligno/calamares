import Calamares.FourRing

/-! Uniform two-tail pressure, independent of the number of rings.
The adjacent-swap reduction is a written forest argument.
The additive control is not a counterexample for Euclidean packing.
-/

namespace Calamares.UniformExchange

open Std Lean.Grind

theorem two_step_pressure {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (m p t k : K) (hk : 0 ≤ k) (h1 : p+t ≤ k*m) (h2 : t ≤ k*p) :
    (k+1)*t ≤ (k*k)*m := by
  have hprod := OrderedRing.mul_nonneg (a := k) (b := k*m-p-t) hk (by grind)
  grind

theorem golden_second_tail {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (m p t phi : K) (hphi : 0 < phi) (heq : phi*phi = phi+1)
    (h1 : p+t ≤ phi*m) (h2 : t ≤ phi*p) : t ≤ m := by
  have h := two_step_pressure m p t phi (by grind) h1 h2
  rw [heq] at h
  by_cases ht : t ≤ m
  · exact ht
  have hprod := OrderedRing.mul_pos (a := phi+1) (b := t-m) (by grind) (by grind)
  grind

-- A=17/10, m=1, p=3/5, q=1/2, w=11/20, R=27/10.
-- The first four clauses certify the full additive witness and greedy prefix.
-- The next four exclude q from every currently available container.
theorem additive_control :
    (17/10 : Rat)+1 ≤ 27/10 ∧
    (3/5 : Rat)+1/2 ≤ 17/10-11/20 ∧
    (1 : Rat) ≤ 17/10-11/20 ∧
    (17/10 : Rat)+3/5 ≤ 27/10 ∧
    (27/10 : Rat) < 17/10+3/5+1/2 ∧
    (17/10-11/20 : Rat) < 1+1/2 ∧
    (1-11/20 : Rat) < 1/2 ∧
    (3/5-11/20 : Rat) < 1/2 ∧
    (1+3/5+1/2 : Rat) = (21/17)*(17/10) ∧
    (3/5+1/2 : Rat) ≤ 21/17 ∧
    (1/2 : Rat) ≤ (21/17)*(3/5) ∧
    (21/17 : Rat) < 3/2 := by decide +kernel

#print axioms two_step_pressure
#print axioms golden_second_tail
#print axioms additive_control

end Calamares.UniformExchange
