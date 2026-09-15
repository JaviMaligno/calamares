from fractions import Fraction as F
import unittest

from cuadrado_optimizado import IMPROVED, WIDTH, family_gates


class ImprovedSquareTests(unittest.TestCase):
    def test_improved_exact_counterexample(self):
        gates=family_gates(IMPROVED,WIDTH)
        self.assertIn('triple',gates)
        self.assertIn('hole_pair',gates)
        self.assertTrue(all(gates.values()),gates)
        self.assertEqual(IMPROVED.b+IMPROVED.c,F(168449,100000))
        self.assertLess(IMPROVED.b+IMPROVED.c,F(337,200))

    def test_thinner_boundary_allows_last_ring_in_pivot(self):
        gates=family_gates(IMPROVED,1-IMPROVED.c)
        self.assertIn('c_not_in_pivot',gates)
        self.assertFalse(gates['c_not_in_pivot'])

    def test_thicker_ring_destroys_four_piece_witness(self):
        gates=family_gates(IMPROVED,WIDTH+F(1,1000000))
        self.assertIn('hole_pair',gates)
        self.assertFalse(gates['hole_pair'])


if __name__ == '__main__':
    unittest.main()
