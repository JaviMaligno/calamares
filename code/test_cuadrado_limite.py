"""Exact witnesses on the feasible side of the proposed limiting wall."""

from fractions import Fraction as F
import unittest

from cuadrado_limite import approximating_certificate
from cuadrado_optimizado import family_gates


class SquareLimitTests(unittest.TestCase):
    def test_three_rational_approximants_certify_every_gate(self):
        for t in map(F, ('.842244', '.842243873', '.8422438729362')):
            with self.subTest(t=t):
                cert, width = approximating_certificate(t)
                self.assertTrue(all(family_gates(cert, width).values()))
                self.assertEqual(cert.b + cert.c, 2*t)
                self.assertGreater(cert.c, 1-width)
                self.assertEqual(cert.a-width, 2*t)

    def test_below_balanced_wall_cannot_certify_this_family(self):
        with self.assertRaises(ValueError):
            approximating_certificate(F('.8422438'), max_steps=20)

    def test_floating_input_is_not_an_exact_witness(self):
        with self.assertRaises(TypeError):
            approximating_certificate(.842244)


if __name__ == '__main__':
    unittest.main()
