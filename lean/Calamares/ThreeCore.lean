import Calamares.Reservoir

/-! Algebra for the three-largest-disks theorem.
Angular placement, the minimal three-disk container and forest assembly
remain written geometric arguments; their independent review is recorded
in docs/reviews/2026-09-15-fable-three-core-final-review.md.
-/

namespace Calamares.ThreeCore
open Std Lean.Grind

theorem arbelos_margin_identity {K : Type u} [CommRing K] (a b r s : K) :
    a*b*(a+b-r)*(a+b-s)-a*a*s*(a+b-r)-b*b*r*(a+b-s)-3*a*b*r*s =
      (a+b)*(a+b)*(a*(b-r-s)+(a-b)*r)+(a-b)*(a-b)*r*s := by grind

theorem arbelos_margin_nonneg {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (a b r s : K) (hb : 0 ≤ b) (hab : b ≤ a)
    (hr : 0 ≤ r) (hs : 0 ≤ s) (hmass : r+s ≤ b) :
    0 ≤ a*b*(a+b-r)*(a+b-s)-a*a*s*(a+b-r)-b*b*r*(a+b-s)-3*a*b*r*s := by
  have h1 := OrderedRing.mul_nonneg (a := a) (b := b-r-s) (by grind) (by grind)
  have h2 := OrderedRing.mul_nonneg (a := a-b) (b := r) (by grind) hr
  have h3 := OrderedRing.mul_nonneg (a := a+b) (b := a+b) (by grind) (by grind)
  have h4 := OrderedRing.mul_nonneg h3 (b := a*(b-r-s)+(a-b)*r) (by grind)
  have h5 := OrderedRing.mul_nonneg (a := a-b) (b := a-b) (by grind) (by grind)
  have h6 := OrderedRing.mul_nonneg (OrderedRing.mul_nonneg h5 hr) hs
  rw [arbelos_margin_identity]
  grind

theorem gap_sum_identity {K : Type u} [CommRing K]
    (s p c d t : K) (ht : t*t = p+s*c) (hd : d = 4*s+c-4*t) :
    (s*s-p)*(c+d)-2*s*c*d = 2*(s-t)*(s-t)*(2*s+2*t-c) := by
  rw [hd]
  grind

theorem gap_sum_margin {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (s p c d t : K) (hs : 0 < s) (ht0 : 0 ≤ t)
    (hc : c ≤ s) (ht : t*t = p+s*c) (hd : d = 4*s+c-4*t) :
    2*s*c*d ≤ (s*s-p)*(c+d) := by
  have hsq : 0 ≤ (s-t)*(s-t) := by
    by_cases h : 0 ≤ s-t
    · exact OrderedRing.mul_nonneg h h
    · have h' := OrderedRing.mul_nonneg (a := t-s) (b := t-s) (by grind) (by grind)
      grind
  have hprod := OrderedRing.mul_nonneg hsq (b := 2*s+2*t-c) (by grind)
  have hid := gap_sum_identity s p c d t ht hd
  grind

theorem opposite_height_positive {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (a b x : K) (hb : 0 < b) (hab : b ≤ a) (hxb : x ≤ b) :
    0 < 4*a*b*(a+b)-x*(a-b)*(a-b) := by
  have ha : 0 < a := by grind
  have haa := OrderedRing.mul_pos ha ha
  have hbb := OrderedRing.mul_pos hb hb
  have habp := OrderedRing.mul_pos ha hb
  have hdiff := OrderedRing.mul_nonneg (a := a-b) (b := a-b) (by grind) (by grind)
  have hbound := OrderedRing.mul_nonneg (a := b-x) (by grind) hdiff
  have hapos := OrderedRing.mul_nonneg (a := a-b) (b := a+b) (by grind) (by grind)
  have hprod := OrderedRing.mul_pos hb (b := 3*a*a+6*a*b-b*b) (by grind)
  grind

theorem envelope_bounds {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (b c e v phi beta : K) (hp : 0 < phi) (heq : phi*phi = phi+1)
    (hb : c+(e+v) ≤ phi*b) (hc : e+v ≤ phi*c) (he : v ≤ phi*e)
    (hec : e ≤ c) (hbeta : c ≤ beta) :
    e ≤ beta ∧ v ≤ beta ∧ e+v ≤ b := by
  have h1 := Calamares.UniformExchange.golden_second_tail b c (e+v) phi hp heq hb hc
  have h2 := Calamares.UniformExchange.golden_second_tail c e v phi hp heq hc he
  grind

theorem curvature_gap_to_radius {K : Type u} [CommRing K] [LE K] [LT K]
    [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]
    (q c d s beta rc rd : K) (hq : 0 < q) (hc : 0 < c) (hd : 0 < d)
    (hbeta : beta*q = s) (hrc : rc*c = 1) (hrd : rd*d = 1)
    (hmargin : 2*s*c*d ≤ q*(c+d)) : 2*beta ≤ rc+rd := by
  have hid : (rc+rd-2*beta)*q*c*d = q*(c+d)-2*s*c*d := by
    calc
      _ = q*d*(rc*c)+q*c*(rd*d)-2*(beta*q)*c*d := by grind
      _ = _ := by rw [hrc, hrd, hbeta]; grind
  by_cases h : 2*beta ≤ rc+rd
  · exact h
  have hp := OrderedRing.mul_pos (a := 2*beta-rc-rd) (b := q*c*d)
    (by grind) (OrderedRing.mul_pos (OrderedRing.mul_pos hq hc) hd)
  grind

#print axioms arbelos_margin_identity
#print axioms arbelos_margin_nonneg
#print axioms gap_sum_identity
#print axioms gap_sum_margin
#print axioms opposite_height_positive
#print axioms envelope_bounds
#print axioms curvature_gap_to_radius
end Calamares.ThreeCore
