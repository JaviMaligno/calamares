prelude
import Init.Grind.Ring
import Init.Grind.Tactics

/-!
Algebraic identities used in the written square-limit argument.
Continuity, the real root, and the asymptotic family are not formalized here.
-/

namespace Calamares.SquareLimit

open Lean.Grind

theorem balanced_gap_identity {K : Type u} [CommRing K]
    (t k : K) (hk : k*k = 2) :
    2*((4+8*t)^2 - ((2+k)*(2+t)-4*t)^2 -
      (2*(2+k)*(2+t)-4-8*t)^2) =
    (17+10*k)*(2*t)^2 + (72+16*k)*(2*t) - (112+96*k) := by
  grind

theorem norm_identity {K : Type u} [CommRing K] (y : K) :
    (17*y^2+72*y-112)^2 - 2*(10*y^2+16*y-96)^2 =
    89*y^4+1808*y^3+4704*y^2-9984*y-5888 := by
  grind

theorem norm_root {K : Type u} [CommRing K]
    (y k : K) (hk : k*k = 2)
    (hy : (17+10*k)*y^2+(72+16*k)*y-(112+96*k) = 0) :
    89*y^4+1808*y^3+4704*y^2-9984*y-5888 = 0 := by
  have hp : 89*y^4+1808*y^3+4704*y^2-9984*y-5888 =
      ((17+10*k)*y^2+(72+16*k)*y-(112+96*k)) *
      (17*y^2+72*y-112-k*(10*y^2+16*y-96)) := by
    clear hy
    grind
  rw [hp, hy]
  grind

#print axioms balanced_gap_identity
#print axioms norm_identity
#print axioms norm_root

end Calamares.SquareLimit
