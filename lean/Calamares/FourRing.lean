prelude
import Init.Grind.Ring
import Init.Grind.Ordered
import Init.Grind.Order
import Init.Grind.Tactics

/-! Algebra of the exact four-ring golden floor.
The reduction of forests to two exchange cases is a written proof.
-/

namespace Calamares.FourRing

open Std Lean.Grind

theorem large_leader_identity {K : Type u} [CommRing K]
    (a phi : K) (hp : phi*phi = phi+1) :
    2*a*(a+1)-phi*(a*a+a+1) =
      (a-phi)*((2-phi)*a+1) := by
  grind

theorem small_leader_identity {K : Type u} [CommRing K]
    (a phi : K) (hp : phi*phi = phi+1) :
    (a*a+a+1)+2*a*(a+1)-phi*a*(a*a+a+1) =
      (phi-a)*(phi*a*a+(2*phi-2)*a+phi-1) := by
  grind

theorem golden_balance {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (a phi g rho d : K) (ha : 1 < a) (hp1 : 1 < phi) (hp2 : phi < 2)
    (hp : phi*phi = phi+1) (hd : d = a*a+a+1)
    (hg : g*d = a*(a+1)) (hr1 : 2*g < rho)
    (hr2 : 1+2*g < rho*a) : phi < rho := by
  have haa : 0 ≤ a*a := OrderedRing.mul_nonneg (by grind) (by grind)
  have hdpos : 0 < d := by grind
  by_cases hc : phi ≤ a
  · have hprod : 0 ≤ (a-phi)*((2-phi)*a+1) :=
      OrderedRing.mul_nonneg (by grind)
        (by
          have := OrderedRing.mul_nonneg (a := 2-phi) (b := a) (by grind) (by grind)
          grind)
    have hid := large_leader_identity a phi hp
    have hgd : 0 ≤ (2*g-phi)*d := by grind
    by_cases h : phi < rho
    · exact h
    have hn : 0 < (phi-2*g)*d :=
      OrderedRing.mul_pos (by grind) hdpos
    grind
  · have hpa : 0 ≤ phi*a*a := by
      have h1 := OrderedRing.mul_nonneg (a := phi) (b := a) (by grind) (by grind)
      exact OrderedRing.mul_nonneg h1 (by grind)
    have hlin := OrderedRing.mul_nonneg (a := 2*phi-2) (b := a) (by grind) (by grind)
    have hprod : 0 ≤ (phi-a)*(phi*a*a+(2*phi-2)*a+phi-1) :=
      OrderedRing.mul_nonneg (by grind) (by grind)
    have hid := small_leader_identity a phi hp
    have heq : (1+2*g-phi*a)*d =
        (a*a+a+1)+2*a*(a+1)-phi*a*(a*a+a+1) := by
      calc
        _ = d+2*(g*d)-phi*a*d := by grind
        _ = _ := by rw [hg, hd]; grind
    have hgd : 0 ≤ (1+2*g-phi*a)*d := by
      rw [heq, hid]
      exact hprod
    by_cases h : phi < rho
    · exact h
    have hra := OrderedRing.mul_nonneg (a := phi-rho) (b := a) (by grind) (by grind)
    have hn : 0 < (phi*a-1-2*g)*d :=
      OrderedRing.mul_pos (by grind) hdpos
    grind

#print axioms large_leader_identity
#print axioms small_leader_identity
#print axioms golden_balance

end Calamares.FourRing
