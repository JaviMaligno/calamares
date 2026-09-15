import Calamares.Square

/-! Square twins and a stronger rational upper bound. All exclusion
theorems quantify over arbitrary coordinates in an ordered commutative
ring, using the parameterized geometric theorem from Square. -/

namespace Calamares.SquareTwins

open Std Lean.Grind Calamares.Square

section Geometry
variable {K : Type u} [CommRing K] [LE K] [LT K]
  [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]

/-- Balanced tail of I1, in units of 1/10000. -/
theorem balanced_excluded : ¬ FitsTriple (51214:K) 20000 8500 8490 := by
  apply excluded_of_conditions 51214 25607 20000 8500 8490 17200 17180
  unfold Conditions
  grind

/-- Every tail disk in either twin is at least 7500. -/
theorem root_pivot_excluded : ¬ FitsTriple (51214:K) 20000 10000 7500 := by
  apply excluded_of_conditions 51214 25607 20000 10000 7500 21200 13900
  unfold Conditions
  grind

/-- A complete Cartesian witness for I2's unbalanced root triple. -/
theorem unbalanced_fits : FitsTriple (51214:K) 20000 9500 7500 := by
  refine ⟨29600, 20000, 9500, 41714, 43714, 43714, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> grind

/-- Improved counterexample: units of 1/100000000. -/
theorem improved_excluded : ¬ FitsTriple (485201606:K) 184224520 84224510 84224490 := by
  apply excluded_of_conditions 485201606 242600803 184224520 84224510 84224490 158376770 158376710
  unfold Conditions
  grind

end Geometry

/-- Root witness and all scalar hole walls shared by the twins. -/
theorem twin_walls :
    (2:Rat) < 25607/10000 ∧
    2*(25607/5000-3:Rat)^2 > (3:Rat)^2 ∧
    (2-301/1000:Rat) = 1699/1000 ∧
    (1:Rat) ≤ 1699/1000 ∧ (1699/1000:Rat) < 25607/10000 ∧
    (17/20+849/1000:Rat) = 1699/1000 ∧
    (19/20+3/4:Rat) > 1699/1000 ∧
    (19/20:Rat) < 1699/1000 ∧
    (1+3/4:Rat) > 1699/1000 ∧
    (1-301/1000:Rat) < 3/4 ∧
    (19/20-301/1000:Rat) < 3/4 ∧
    (17/20-301/1000:Rat) < 849/1000 ∧
    (3/4:Rat) < 849/1000 ∧ (849/1000:Rat) < 17/20 ∧
    (17/20:Rat) < 19/20 ∧ (19/20:Rat) < 1 := by
  decide +kernel

theorem twin_tails :
    (17/20+849/1000:Rat) = 1699/1000 ∧
    (1+17/20+849/1000:Rat)/2 < 1699/1000 ∧
    (849/1000:Rat)/(17/20) < 1699/1000 ∧
    (19/20+3/4:Rat) = 17/10 ∧
    (1+19/20+3/4:Rat)/2 < 17/10 ∧
    (3/4:Rat)/(19/20) < 17/10 := by
  decide +kernel

/-- Exact witness and greedy gates for the improved bound, scaled by 1e8. -/
theorem improved_gates :
    (0:Rat) < 15775520 ∧
    (0:Rat) < 84224490 ∧ (84224490:Rat) < 84224510 ∧
    (84224510:Rat) < 100000000 ∧ (100000000:Rat) < 184224520 ∧
    (2*184224520:Rat) < 485201606 ∧
    (485201606-184224520-100000000:Rat) > 0 ∧
    2*(485201606-184224520-100000000:Rat)^2 > (184224520+100000000:Rat)^2 ∧
    (84224510+84224490:Rat) = 184224520-15775520 ∧
    (100000000:Rat) ≤ 184224520-15775520 ∧
    (2*(184224520-15775520):Rat) < 485201606 ∧
    (100000000+84224490:Rat) > 184224520-15775520 ∧
    (84224490:Rat) > 100000000-15775520 ∧
    (84224490:Rat) > 84224510-15775520 ∧
    (100000000+84224510+84224490:Rat)*100000000 < 184224520*(84224510+84224490:Rat) ∧
    (84224490:Rat)/84224510 < 168449/100000 ∧
    (84224510+84224490:Rat)/100000000 = 168449/100000 ∧
    (168449/100000:Rat) < 337/200 := by
  decide +kernel

#print axioms balanced_excluded
#print axioms root_pivot_excluded
#print axioms unbalanced_fits
#print axioms improved_excluded
#print axioms twin_walls
#print axioms twin_tails
#print axioms improved_gates

end Calamares.SquareTwins
