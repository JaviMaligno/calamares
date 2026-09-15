import Init.Grind

/-!
# Exact square certificates

Coordinates in the geometric theorem are scaled by 10000. The argument
works in every linearly ordered commutative ring, not only at rational
sample points. No square-root or numerical packing oracle is used.
-/

namespace Calamares.Square

open Std Lean.Grind

section Geometry

variable {K : Type u} [CommRing K] [LE K] [LT K]
  [LawfulOrderLT K] [IsLinearOrder K] [OrderedRing K]

theorem sq_le_of_bounds {x m : K} (lo : -m ≤ x) (hi : x ≤ m) :
    x * x ≤ m * m := by
  have hp : 0 ≤ (m - x) * (m + x) :=
    OrderedRing.mul_nonneg (by grind) (by grind)
  grind

theorem separated_coordinate {x y p m r : K}
    (yl : -m ≤ y) (yu : y ≤ m)
    (xl : -p ≤ x) (gap : p*p + m*m < r*r)
    (sep : r*r ≤ x*x + y*y) : p < x := by
  have hy := sq_le_of_bounds yl yu
  by_cases h : x ≤ p
  · have hx := sq_le_of_bounds xl h
    grind
  · grind

/-- In the reflected quarter-square, the big disk forces both small
centers into a box too narrow for their required separation. -/
theorem d_no_normalized (ax ay bx byy cx cy : K)
    (ha : 18450 ≤ ax ∧ ax ≤ 24284 ∧ 18450 ≤ ay ∧ ay ≤ 24284)
    (hb : 8440 ≤ bx ∧ bx ≤ 40128 ∧ 8440 ≤ byy ∧ byy ≤ 40128)
    (hc : 8410 ≤ cx ∧ cx ≤ 40158 ∧ 8410 ≤ cy ∧ cy ≤ 40158)
    (hab : (26890:K)*26890 ≤ (bx-ax)*(bx-ax) + (byy-ay)*(byy-ay))
    (hac : (26860:K)*26860 ≤ (cx-ax)*(cx-ax) + (cy-ay)*(cy-ay))
    (hbc : (16850:K)*16850 ≤ (bx-cx)*(bx-cx) + (byy-cy)*(byy-cy)) : False := by
  have hbx : 15910 < bx-ax := separated_coordinate
    (y := byy-ay) (m := (21678:K)) (r := (26890:K))
    (by grind) (by grind) (by grind) (by grind) hab
  have hby : 15910 < byy-ay := separated_coordinate
    (y := bx-ax) (m := (21678:K)) (r := (26890:K))
    (by grind) (by grind) (by grind) (by grind) (by grind)
  have hcx : 15810 < cx-ax := separated_coordinate
    (y := cy-ay) (m := (21708:K)) (r := (26860:K))
    (by grind) (by grind) (by grind) (by grind) hac
  have hcy : 15810 < cy-ay := separated_coordinate
    (y := cx-ax) (m := (21708:K)) (r := (26860:K))
    (by grind) (by grind) (by grind) (by grind) (by grind)
  have hx : (bx-cx)*(bx-cx) ≤ (5898:K)*5898 :=
    sq_le_of_bounds (by grind) (by grind)
  have hy : (byy-cy)*(byy-cy) ≤ (5898:K)*5898 :=
    sq_le_of_bounds (by grind) (by grind)
  grind

/-- Full Cartesian infeasibility, with reflections proved inside Lean.
This quantifies over all coordinates in any linearly ordered commutative
ring. Side 48568 and radii 18450,8440,8410 are the D instance scaled by
10000. Thus this is a geometric inequality theorem, not a grid check. -/
theorem d_no_packing (ax ay bx byy cx cy : K)
    (ha : 18450 ≤ ax ∧ ax ≤ 30118 ∧ 18450 ≤ ay ∧ ay ≤ 30118)
    (hb : 8440 ≤ bx ∧ bx ≤ 40128 ∧ 8440 ≤ byy ∧ byy ≤ 40128)
    (hc : 8410 ≤ cx ∧ cx ≤ 40158 ∧ 8410 ≤ cy ∧ cy ≤ 40158)
    (hab : (26890:K)*26890 ≤ (bx-ax)*(bx-ax) + (byy-ay)*(byy-ay))
    (hac : (26860:K)*26860 ≤ (cx-ax)*(cx-ax) + (cy-ay)*(cy-ay))
    (hbc : (16850:K)*16850 ≤ (bx-cx)*(bx-cx) + (byy-cy)*(byy-cy)) : False := by
  by_cases hx : ax ≤ 24284
  · by_cases hy : ay ≤ 24284
    · exact d_no_normalized ax ay bx byy cx cy (by grind) hb hc hab hac hbc
    · apply d_no_normalized ax (48568-ay) bx (48568-byy) cx (48568-cy) <;> grind
  · by_cases hy : ay ≤ 24284
    · apply d_no_normalized (48568-ax) ay (48568-bx) byy (48568-cx) cy <;> grind
    · apply d_no_normalized (48568-ax) (48568-ay)
        (48568-bx) (48568-byy) (48568-cx) (48568-cy) <;> grind

/-- Parameter conditions of the written quadrant-confinement lemma.
The half-side is explicit, so no division or field structure is needed. -/
def Conditions (s h a b c p q : K) : Prop :=
  s = h+h ∧ (0 < c ∧ c ≤ b ∧ b ≤ a ∧ a ≤ h) ∧
  (0 ≤ q ∧ q ≤ p) ∧ h-b ≤ p ∧
  p*p + (s-a-b)*(s-a-b) < (a+b)*(a+b) ∧
  q*q + (s-a-c)*(s-a-c) < (a+c)*(a+c) ∧
  s-b-c ≤ p+q ∧ 0 ≤ s-c-a-q ∧
  2*((s-c-a-q)*(s-c-a-q)) < (b+c)*(b+c)

theorem no_normalized (s h a b c p q ax ay bx byy cx cy : K)
    (params : Conditions s h a b c p q)
    (ha : a ≤ ax ∧ ax ≤ h ∧ a ≤ ay ∧ ay ≤ h)
    (hb : b ≤ bx ∧ bx ≤ s-b ∧ b ≤ byy ∧ byy ≤ s-b)
    (hc : c ≤ cx ∧ cx ≤ s-c ∧ c ≤ cy ∧ cy ≤ s-c)
    (hab : (a+b)*(a+b) ≤ (bx-ax)*(bx-ax) + (byy-ay)*(byy-ay))
    (hac : (a+c)*(a+c) ≤ (cx-ax)*(cx-ax) + (cy-ay)*(cy-ay))
    (hbc : (b+c)*(b+c) ≤ (bx-cx)*(bx-cx) + (byy-cy)*(byy-cy)) : False := by
  rcases params with ⟨hh, ho, hcuts, hfirst, hgapb, hgapc, hsum, hlen, hcluster⟩
  have hbx : p < bx-ax := separated_coordinate
    (y := byy-ay) (m := s-a-b) (r := a+b)
    (by grind) (by grind) (by grind) hgapb hab
  have hby : p < byy-ay := separated_coordinate
    (y := bx-ax) (m := s-a-b) (r := a+b)
    (by grind) (by grind) (by grind) hgapb (by grind)
  have hcx : q < cx-ax := separated_coordinate
    (y := cy-ay) (m := s-a-c) (r := a+c)
    (by grind) (by grind) (by grind) hgapc hac
  have hcy : q < cy-ay := separated_coordinate
    (y := cx-ax) (m := s-a-c) (r := a+c)
    (by grind) (by grind) (by grind) hgapc (by grind)
  have hx : (bx-cx)*(bx-cx) ≤ (s-c-a-q)*(s-c-a-q) :=
    sq_le_of_bounds (by grind) (by grind)
  have hy : (byy-cy)*(byy-cy) ≤ (s-c-a-q)*(s-c-a-q) :=
    sq_le_of_bounds (by grind) (by grind)
  grind

/-- The full parameterized geometric criterion, including reflections. -/
theorem no_packing (s h a b c p q ax ay bx byy cx cy : K)
    (params : Conditions s h a b c p q)
    (ha : a ≤ ax ∧ ax ≤ s-a ∧ a ≤ ay ∧ ay ≤ s-a)
    (hb : b ≤ bx ∧ bx ≤ s-b ∧ b ≤ byy ∧ byy ≤ s-b)
    (hc : c ≤ cx ∧ cx ≤ s-c ∧ c ≤ cy ∧ cy ≤ s-c)
    (hab : (a+b)*(a+b) ≤ (bx-ax)*(bx-ax) + (byy-ay)*(byy-ay))
    (hac : (a+c)*(a+c) ≤ (cx-ax)*(cx-ax) + (cy-ay)*(cy-ay))
    (hbc : (b+c)*(b+c) ≤ (bx-cx)*(bx-cx) + (byy-cy)*(byy-cy)) : False := by
  have hh := params.1
  by_cases hx : ax ≤ h
  · by_cases hy : ay ≤ h
    · exact no_normalized s h a b c p q ax ay bx byy cx cy params (by grind) hb hc hab hac hbc
    · apply no_normalized s h a b c p q ax (s-ay) bx (s-byy) cx (s-cy) params <;> grind
  · by_cases hy : ay ≤ h
    · apply no_normalized s h a b c p q (s-ax) ay (s-bx) byy (s-cx) cy params <;> grind
    · apply no_normalized s h a b c p q (s-ax) (s-ay) (s-bx) (s-byy) (s-cx) (s-cy) params <;> grind

/-- Cartesian encoding of three disks inside a square. -/
def FitsTriple (s a b c : K) : Prop :=
  ∃ ax ay bx byy cx cy : K,
    (a ≤ ax ∧ ax ≤ s-a ∧ a ≤ ay ∧ ay ≤ s-a) ∧
    (b ≤ bx ∧ bx ≤ s-b ∧ b ≤ byy ∧ byy ≤ s-b) ∧
    (c ≤ cx ∧ cx ≤ s-c ∧ c ≤ cy ∧ cy ≤ s-c) ∧
    (a+b)*(a+b) ≤ (bx-ax)*(bx-ax) + (byy-ay)*(byy-ay) ∧
    (a+c)*(a+c) ≤ (cx-ax)*(cx-ax) + (cy-ay)*(cy-ay) ∧
    (b+c)*(b+c) ≤ (bx-cx)*(bx-cx) + (byy-cy)*(byy-cy)

theorem excluded_of_conditions (s h a b c p q : K)
    (params : Conditions s h a b c p q) : ¬ FitsTriple s a b c := by
  intro ⟨ax, ay, bx, byy, cx, cy, ha, hb, hc, hab, hac, hbc⟩
  exact no_packing s h a b c p q ax ay bx byy cx cy params ha hb hc hab hac hbc

end Geometry

/-- Exact positive margins for the six numerical walls of the proof.
Units here are the original unscaled radii. -/
theorem d_margins :
    (2689/1000:Rat)^2 - (1591/1000:Rat)^2 - (10839/5000:Rat)^2 = 2079/25000000 ∧
    (2686/1000:Rat)^2 - (1581/1000:Rat)^2 - (5427/2500:Rat)^2 = 66559/25000000 ∧
    (1591/1000:Rat) - (6071/2500 - 211/250) = 33/5000 ∧
    (1591/1000:Rat) + 1581/1000 - (6071/1250 - 211/250 - 841/1000) = 1/5000 ∧
    (337/200:Rat)^2 - 2*(2949/5000:Rat)^2 = 53587423/25000000 ∧
    (0:Rat) < 2079/25000000 ∧ (0:Rat) < 66559/25000000 ∧
    (0:Rat) < 33/5000 ∧ (0:Rat) < 1/5000 ∧ (0:Rat) < 53587423/25000000 := by
  decide +kernel

/-- The root pair fits in opposite corners, and the two smaller radii
fill the large ring's hole in a diameter row. -/
theorem d_witness :
    (369/200:Rat) ≤ 6071/2500 ∧ (1:Rat) ≤ 6071/2500 ∧
    (0:Rat) < 6071/1250 - 369/200 - 1 ∧
    2*(6071/1250 - 369/200 - 1:Rat)^2 - (369/200 + 1:Rat)^2 = 16337/25000000 ∧
    (0:Rat) < 16337/25000000 ∧
    (211/250:Rat) + 841/1000 = 369/200 - 4/25 := by
  decide +kernel

/-- Every alternative hole at the failing step is excluded; the pivot
was legally nested and best fit prefers its container over the root. -/
theorem d_greedy_walls :
    (0:Rat) < 841/1000 ∧ (841/1000:Rat) < 211/250 ∧
    (211/250:Rat) < 1 ∧ (1:Rat) < 369/200 ∧
    (1:Rat) ≤ 369/200 - 4/25 ∧
    (369/200 - 4/25:Rat) < 6071/2500 ∧
    (369/200 - 4/25:Rat) < 1 + 211/250 ∧
    (369/200 - 4/25:Rat) < 1 + 841/1000 ∧
    (1 - 4/25:Rat) < 211/250 ∧
    (1 - 4/25:Rat) < 841/1000 ∧
    (211/250 - 4/25:Rat) < 841/1000 := by
  decide +kernel

/-- The second tail is the largest, exactly 337/200. -/
theorem d_tail :
    (211/250 + 841/1000:Rat) = 337/200 ∧
    (1 + 211/250 + 841/1000:Rat)/(369/200) < 337/200 ∧
    (841/1000:Rat)/(211/250) < 337/200 ∧
    (337/200:Rat) < 17/10 := by
  decide +kernel

private def quartic (x : Rat) : Rat := 17*x^4 - 4*x^3 - 62*x^2 + 4*x + 49

/-- Sign bracket for the branch defining X. Uniqueness on x >= 1.7
follows in the written proof from the positive nonconstant coefficients
of the shift identity below. -/
theorem x_bracket :
    quartic (17/10) = -10463/10000 ∧ quartic (43/25) = 348292/390625 ∧
    quartic (17/10) < 0 ∧ 0 < quartic (43/25) := by
  decide +kernel

theorem x_shift {K : Type u} [CommRing K] (z : K) :
    17*(z+17)^4 - 40*(z+17)^3 - 6200*(z+17)^2 + 4000*(z+17) + 490000 =
    17*z^4 + 1116*z^3 + 21238*z^2 + 92604*z - 10463 := by
  grind

/-- A nearby feasible control, D': centers are
A=(24284,18450), B=(8400,40168), C=(40218,40218), side=48568.
The three positive separation margins prevent confusing the D theorem
with an indiscriminate rejection of nearby triples. -/
theorem d_prime_witness :
    (18450:Rat) ≤ 24284 ∧ (24284:Rat) ≤ 48568-18450 ∧
    (18450:Rat) ≤ 48568-18450 ∧
    (8400:Rat) ≤ 40168 ∧ (40168:Rat) = 48568-8400 ∧
    (8350:Rat) ≤ 40218 ∧ (40218:Rat) = 48568-8350 ∧
    (18450+8400:Rat)^2 < (24284-8400:Rat)^2 + (18450-40168:Rat)^2 ∧
    (18450+8350:Rat)^2 < (24284-40218:Rat)^2 + (18450-40218:Rat)^2 ∧
    (8400+8350:Rat)^2 < (8400-40218:Rat)^2 + (40168-40218:Rat)^2 := by
  decide +kernel

#print axioms d_no_packing
#print axioms no_packing
#print axioms excluded_of_conditions
#print axioms d_margins
#print axioms d_witness
#print axioms d_greedy_walls
#print axioms d_tail
#print axioms x_bracket
#print axioms x_shift
#print axioms d_prime_witness

end Calamares.Square
