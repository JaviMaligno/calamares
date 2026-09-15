import Calamares.FourRing

/-! Cartesian and ordered algebra for the five-ring extension.
All pocket coordinates are multiplied by the positive denominator d.
Forest classification, assembly and normalization remain written proofs.
-/

namespace Calamares.FiveRing

open Std Lean.Grind

theorem pocket_wall {K : Type u} [CommRing K] (a b : K)
    (d n x y : K) (hd : d = a*a+a*b+b*b) (hn : n = a*b*(a+b))
    (hx : x = (a-b)*(a+b)*(a+b)) (hy : y = 2*n) :
    x*x+y*y = ((a+b)*d-n)*((a+b)*d-n) := by
  rw [hx, hy, hn, hd]
  grind

theorem pocket_left {K : Type u} [CommRing K] (a b : K)
    (d n x y : K) (hd : d = a*a+a*b+b*b) (hn : n = a*b*(a+b))
    (hx : x = (a-b)*(a+b)*(a+b)) (hy : y = 2*n) :
    (x+b*d)*(x+b*d)+y*y = (a*d+n)*(a*d+n) := by
  rw [hx, hy, hn, hd]
  grind

theorem pocket_right {K : Type u} [CommRing K] (a b : K)
    (d n x y : K) (hd : d = a*a+a*b+b*b) (hn : n = a*b*(a+b))
    (hx : x = (a-b)*(a+b)*(a+b)) (hy : y = 2*n) :
    (x-a*d)*(x-a*d)+y*y = (b*d+n)*(b*d+n) := by
  rw [hx, hy, hn, hd]
  grind

theorem double_pocket_separation {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (n : K) (hn : 0 < n) : (2*n-(-2*n))*(2*n-(-2*n)) > (2*n)*(2*n) := by
  have := OrderedRing.mul_pos hn hn
  grind

theorem pocket_positive {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (a b d g : K) (ha : 0 < a) (hb : 0 < b)
    (hd : d = a*a+a*b+b*b) (hg : g*d = a*b*(a+b)) :
    0 < d ∧ 0 < g ∧ g < a+b := by
  have haa := OrderedRing.mul_pos ha ha
  have hbb := OrderedRing.mul_pos hb hb
  have hab := OrderedRing.mul_pos ha hb
  have hdpos : 0 < d := by grind
  have hn := OrderedRing.mul_pos hab (b := a+b) (by grind)
  have hgpos : 0 < g := by
    by_cases h : 0 < g
    · exact h
    have := OrderedRing.mul_nonneg (a := -g) (b := d) (by grind) (by grind)
    grind
  have hwall := OrderedRing.mul_pos (a := a+b) (b := a*a+b*b) (by grind) (by grind)
  have hw : 0 < (a+b)*d-g*d := by
    calc
      _ < (a+b)*(a*a+b*b) := hwall
      _ = (a+b)*d-g*d := by rw [hg, hd]; grind
  have hless : g < a+b := by
    by_cases h : g < a+b
    · exact h
    have := OrderedRing.mul_nonneg (a := g-(a+b)) (b := d) (by grind) (by grind)
    grind
  exact ⟨hdpos, hgpos, hless⟩

theorem two_leader_identity {K : Type u} [CommRing K]
    (a b b0 : K) (h0 : b0*b0+2*b0 = 4) :
    a*b*(a+b)-(a*a+a*b+b*b) =
      (a-2)*(a-2)*(b-1)+(a-2)*(b-1)*(b+4)+(b-b0)*(b+b0+2) := by grind

theorem two_leader_positive {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (a b b0 : K) (ha : 2 < a) (hb : b0 < b) (hb0 : 1 < b0)
    (h0 : b0*b0+2*b0 = 4) : a*a+a*b+b*b < a*b*(a+b) := by
  have haa := OrderedRing.mul_pos (a := a-2) (b := a-2) (by grind) (by grind)
  have ht1 := OrderedRing.mul_pos haa (b := b-1) (by grind)
  have hab := OrderedRing.mul_pos (a := a-2) (b := b-1) (by grind) (by grind)
  have ht2 := OrderedRing.mul_pos hab (b := b+4) (by grind)
  have ht3 := OrderedRing.mul_pos (a := b-b0) (b := b+b0+2) (by grind) (by grind)
  have hid := two_leader_identity a b b0 h0
  have hsum : 0 < a*b*(a+b)-(a*a+a*b+b*b) := by
    rw [hid]
    grind
  grind

theorem golden_base {K : Type u} [CommRing K]
    (phi b0 : K) (hp : phi*phi = phi+1) (h0 : b0 = 2*phi-2) :
    phi*b0 = 2 ∧ b0*b0+2*b0 = 4 := by
  rw [h0]
  constructor <;> grind

theorem two_leader_pressure {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (a b phi b0 : K) (hp : 0 < phi) (h0 : b0 = 2*phi-2)
    (hprod : phi*b0 = 2) (hb : 2 < phi*b) (ha : b+2 < phi*a) :
    b0 < b ∧ 2 < a := by
  have hbgt : b0 < b := by
    by_cases h : b0 < b
    · exact h
    have := OrderedRing.mul_nonneg (a := phi) (b := b0-b) (by grind) (by grind)
    grind
  constructor
  · exact hbgt
  · by_cases h : 2 < a
    · exact h
    have := OrderedRing.mul_nonneg (a := phi) (b := 2-a) (by grind) (by grind)
    grind

theorem golden_base_above_one {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (phi b0 : K) (hp : 1 < phi) (heq : phi*phi = phi+1)
    (h0 : b0 = 2*phi-2) : 1 < b0 := by
  by_cases h : 1 < b0
  · exact h
  have := OrderedRing.mul_nonneg (a := 3-2*phi) (b := 2*phi+1) (by grind) (by grind)
  grind

theorem one_leader_pressure {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (a phi g rho d p q : K) (ha : 1 < a) (hp1 : 1 < phi) (hp2 : phi < 2)
    (hp : phi*phi = phi+1) (hd : d = a*a+a+1) (hg : g*d = a*(a+1))
    (hpq : q ≤ p) (ht1 : p+q ≤ rho) (ht2 : 1+p+q ≤ rho*a)
    (hr : rho ≤ phi) : q ≤ g := by
  by_cases h : q ≤ g
  · exact h
  have hf := Calamares.FourRing.golden_balance a phi g rho d ha hp1 hp2 hp hd hg
    (by grind) (by grind)
  grind

#print axioms pocket_wall
#print axioms pocket_left
#print axioms pocket_right
#print axioms double_pocket_separation
#print axioms pocket_positive
#print axioms two_leader_identity
#print axioms two_leader_positive
#print axioms golden_base
#print axioms two_leader_pressure
#print axioms golden_base_above_one
#print axioms one_leader_pressure

end Calamares.FiveRing
