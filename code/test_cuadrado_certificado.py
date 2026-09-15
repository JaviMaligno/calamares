"""Exact checks, including feasible and boundary controls for the square lemma."""

from dataclasses import replace
from fractions import Fraction as F
import unittest

from cuadrado_certificado import Certificate, certifies_infeasibility, verify_d


class ConfinementTests(unittest.TestCase):
    def setUp(self):
        self.d = Certificate(*map(F, ("4.8568", "1.845", ".844", ".841", "1.591", "1.581")))

    def test_original_d_with_rationally_enlarged_pan_is_certified(self):
        self.assertTrue(certifies_infeasibility(self.d))

    def test_e_with_more_geometric_margin_is_certified(self):
        e = Certificate(*map(F, ("4.881", "1.859", ".856", ".853", "1.636", "1.627")))
        self.assertTrue(certifies_infeasibility(e))

    def test_feasible_three_disks_are_not_certified(self):
        # All three fit in a diameter row inside the square, with room left.
        # This checks only the supplied p,q; it does not search all certificates.
        self.assertFalse(certifies_infeasibility(replace(self.d, side=F(8))))

    def test_old_d_prime_control_is_not_certified(self):
        # Failure of these cuts alone is not a feasibility certificate.
        # D' is feasible by the explicit witness in the note and Square.lean.
        self.assertFalse(certifies_infeasibility(replace(self.d, b=F(".840"), c=F(".835"))))

    def test_lost_reflection_wall_is_rejected(self):
        self.assertFalse(certifies_infeasibility(replace(self.d, p=F("1.58"))))

    def test_zero_radii_and_wrong_order_are_rejected(self):
        self.assertFalse(certifies_infeasibility(replace(self.d, c=F(0))))
        self.assertFalse(certifies_infeasibility(replace(self.d, b=F(".840"))))

    def test_floats_cannot_be_used_as_exact_certificates(self):
        with self.assertRaises(TypeError):
            certifies_infeasibility(replace(self.d, side=4.8568))

    def test_tangent_feasible_boundary_is_not_rejected(self):
        # Three radius-1 disks at (1,1),(3,1),(1,3) fit side 4.
        self.assertFalse(certifies_infeasibility(Certificate(4, 1, 1, 1, 1, 1)))

    def test_complete_greedy_failure_includes_every_container_and_witness(self):
        checks = verify_d()
        required = {"proper_rings", "triple", "root_pair", "hole_pair", "nest_pivot", "best_fit",
                    "b_not_with_pivot", "c_not_with_pivot", "b_not_in_pivot",
                    "c_not_in_pivot", "c_not_in_b", "tail_a", "tail_b",
                    "rho", "below_X_bracket", "X_lower_sign", "X_upper_sign"}
        self.assertEqual(set(checks), required)
        self.assertTrue(all(checks.values()), checks)


if __name__ == "__main__":
    unittest.main()
