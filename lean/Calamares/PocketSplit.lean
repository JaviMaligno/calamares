import Calamares.FourRing
import Calamares.VariableWidth

/-! A finite tail can be split between two pockets after its largest
element is reserved. This does not formalize assembly of ring forests.
-/

namespace Calamares.PocketSplit

open Std Lean.Grind
open Calamares.VariableWidth

def splitLoads {K : Type u} [Zero K] [Add K] [LE K] [DecidableLE K] :
    List K → K × K
  | [] => (0, 0)
  | x :: xs =>
    let loads := splitLoads xs
    if loads.1 ≤ loads.2 then (loads.1+x, loads.2)
    else (loads.1, loads.2+x)

theorem split_loads_spec {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K] [DecidableLE K]
    (xs : List K) (p : K) (hp : 0 ≤ p)
    (h : ∀ x ∈ xs, 0 ≤ x ∧ x ≤ p) :
    0 ≤ (splitLoads xs).1 ∧ 0 ≤ (splitLoads xs).2 ∧
    (splitLoads xs).1 + (splitLoads xs).2 = mass xs ∧
    (splitLoads xs).1 - (splitLoads xs).2 ≤ p ∧
    (splitLoads xs).2 - (splitLoads xs).1 ≤ p := by
  induction xs with
  | nil => simp only [splitLoads, mass]; grind
  | cons x xs ih =>
    have hx : 0 ≤ x ∧ x ≤ p := h x (by simp)
    have ht : ∀ y ∈ xs, 0 ≤ y ∧ y ≤ p := by
      intros y hy
      exact h y (by simp [hy])
    have hs := ih ht
    simp only [splitLoads, mass]
    split <;> grind

theorem split_loads_fit {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K] [DecidableLE K]
    (xs : List K) (p g : K) (hp : 0 ≤ p)
    (h : ∀ x ∈ xs, 0 ≤ x ∧ x ≤ p) (ht : mass xs+p ≤ 2*g) :
    (splitLoads xs).1 ≤ g ∧ (splitLoads xs).2 ≤ g := by
  have := split_loads_spec xs p hp h
  grind

theorem tail_le_double_pocket {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (a phi g rho d t : K) (ha : 1 < a) (hp1 : 1 < phi) (hp2 : phi < 2)
    (hp : phi*phi = phi+1) (hd : d = a*a+a+1) (hg : g*d = a*(a+1))
    (ht1 : t ≤ rho) (ht2 : 1+t ≤ rho*a) (hr : rho ≤ phi) : t ≤ 2*g := by
  by_cases h : t ≤ 2*g
  · exact h
  have hf := Calamares.FourRing.golden_balance a phi g rho d ha hp1 hp2 hp hd hg
    (by grind) (by grind)
  grind

#print axioms split_loads_spec
#print axioms split_loads_fit
#print axioms tail_le_double_pocket

end Calamares.PocketSplit
