"""Exact geometry controls for the independent-width area theorem."""

from fractions import Fraction as Q
import unittest
from grosor_variable import Ring, two_ring, area_factor, sharp_pair, thin_pair


class VariableWidthTests(unittest.TestCase):
    def test_thin_large_ring_can_capture_small_ring(self):
        result = two_ring(1, Ring(1, Q(9, 10)), Ring(Q(3, 4), 0))
        self.assertTrue(result['nested'])
        self.assertFalse(result['siblings'])
        self.assertEqual(result['greedy'], (0, 1))
        self.assertEqual(result['ratio'], 1)

    def test_hole_boundary_is_inclusive(self):
        self.assertTrue(two_ring(1, Ring(1, Q(3, 4)), Ring(Q(3, 4), 0))['nested'])

    def test_sibling_boundary_is_inclusive(self):
        result = two_ring(Q(7, 4), Ring(1, 0), Ring(Q(3, 4), 0))
        self.assertTrue(result['siblings'])
        self.assertEqual(result['greedy'], (0, 1))

    def test_both_geometric_routes_can_fail(self):
        result = two_ring(1, Ring(1, Q(74, 100)), Ring(Q(3, 4), 0))
        self.assertFalse(result['nested'])
        self.assertFalse(result['siblings'])
        self.assertEqual(result['greedy'], (0,))
        self.assertEqual(result['optimal'], (1,))
        self.assertEqual(result['ratio'], Q(4524, 5625))

    def test_rational_anchor_below_threshold_is_optimal(self):
        result = two_ring(*sharp_pair(Q(7, 10), Q(1, 1000)))
        self.assertEqual(area_factor(Q(7, 10)), 1)
        self.assertEqual(result['optimal'], (0,))
        self.assertEqual(result['ratio'], 1)

    def test_sharp_family_approaches_lower_bound_from_above(self):
        bound = area_factor(Q(3, 4))
        self.assertEqual(bound, Q(7, 9))
        ratios = [two_ring(*sharp_pair(Q(3, 4), Q(1, 10**j)))['ratio']
                  for j in (2, 3, 4, 5)]
        self.assertTrue(all(x > bound for x in ratios))
        self.assertTrue(all(a > b for a, b in zip(ratios, ratios[1:])))
        self.assertLess(ratios[-1]-bound, Q(1, 10000))

    def test_strict_superincreasing_has_no_uniform_area_factor(self):
        for denominator in (10, 100, 1000):
            e = Q(1, denominator)
            result = two_ring(*thin_pair(e))
            self.assertLess(result['rho'], 1)
            self.assertEqual(result['optimal'], (1,))
            self.assertEqual(result['ratio'], 4*e)

    def test_largest_can_be_unavailable(self):
        result = two_ring(Q(3, 4), Ring(1, 0), Ring(Q(1, 2), 0))
        self.assertEqual(result['greedy'], (1,))
        self.assertEqual(result['ratio'], 1)

    def test_empty_feasible_inventory(self):
        result = two_ring(Q(1, 4), Ring(1, 0), Ring(Q(1, 2), 0))
        self.assertEqual(result['greedy'], ())
        self.assertIsNone(result['ratio'])

    def test_invalid_rings_and_inexact_inputs_are_rejected(self):
        for r, h in ((0, 0), (1, -1), (1, 1), (1, 2)):
            with self.assertRaises(ValueError):
                Ring(r, h)
        with self.assertRaises(TypeError):
            Ring(1.0, 0)

    def test_order_pan_and_parameter_validation(self):
        with self.assertRaises(ValueError):
            two_ring(1, Ring(1, 0), Ring(1, 0))
        with self.assertRaises(ValueError):
            two_ring(0, Ring(1, 0), Ring(Q(1, 2), 0))
        for k in (0, 1, -1):
            with self.assertRaises(ValueError):
                area_factor(k)
        with self.assertRaises(ValueError):
            sharp_pair(Q(3, 4), Q(3, 4))
        with self.assertRaises(ValueError):
            thin_pair(Q(1, 4))


if __name__ == '__main__':
    unittest.main()
