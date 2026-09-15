from fractions import Fraction as F
import unittest

from cuadrado_gemelas import layout_fits, run_greedy, verify_twins


class SquareTwinsTests(unittest.TestCase):
    def test_four_greedy_runs_require_opposite_pivot_choices(self):
        self.assertEqual(run_greedy("I1", "best"), [-1, 0, -1, None])
        self.assertEqual(run_greedy("I1", "worst"), [-1, -1, 0, 0])
        self.assertEqual(run_greedy("I2", "best"), [-1, 0, -1, -1])
        self.assertEqual(run_greedy("I2", "worst"), [-1, -1, 0, None])

    def test_explicit_unbalanced_trio_witness(self):
        s=F("5.1214")
        self.assertTrue(layout_fits(s, (F(2),F(".95"),F(".75")),
            ((F("2.96"),F(2)),(F(".95"),s-F(".95")),(s-F(".75"),s-F(".75")))))

    def test_overlap_and_escape_are_rejected(self):
        self.assertFalse(layout_fits(F(4),(F(1),F(1)),((F(1),F(1)),(F(1),F(1)))))
        self.assertFalse(layout_fits(F(4),(F(1),),((F(0),F(1)),)))

    def test_tangency_is_legal(self):
        self.assertTrue(layout_fits(F(4),(F(1),F(1)),((F(1),F(1)),(F(3),F(1)))))

    def test_complete_twins_gates(self):
        checks=verify_twins()
        self.assertIn("balanced_trio_blocked",checks)
        self.assertIn("root_pivot_trio_blocked",checks)
        self.assertIn("unbalanced_trio_fits",checks)
        self.assertIn("shared_state",checks)
        self.assertIn("four_runs",checks)
        self.assertTrue(all(checks.values()),checks)

    def test_float_coordinates_and_wrong_lengths_are_rejected(self):
        with self.assertRaises(TypeError):
            layout_fits(F(4),(F(1),),((1.0,F(1)),))
        with self.assertRaises(ValueError):
            layout_fits(F(4),(F(1),),())


if __name__ == "__main__":
    unittest.main()
