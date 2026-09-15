"""Exact rational witnesses approaching the written square-limit upper bound.

Finite examples certify only their own rho. The limiting conclusion uses
the continuity argument in docs/drafts/cuadrado_limite.md.
"""

from fractions import Fraction as F
from math import isqrt

from cuadrado_certificado import Certificate
from cuadrado_optimizado import family_gates


def approximating_certificate(t, max_steps=80):
    """Find a checked rational perturbation, or fail without a geometry verdict.

    The fixed 120-digit upper approximation to sqrt(2) is just a choice of
    rational side. Soundness depends on the exact gates, not its precision.
    Exhaustion does not prove geometric infeasibility or family optimality.
    """
    if not isinstance(t, (int, F)):
        raise TypeError('Use an exact rational t')
    t = F(t)
    den = 10**120
    sqrt2_upper = F(isqrt(2*den*den) + 1, den)
    for step in range(1, max_steps + 1):
        eta = F(1, 10**step)
        a, b, c = 1+t+2*eta, t+eta, t-eta
        width = 1-t+2*eta
        side = (1+sqrt2_upper/2)*(a+1)
        cut = side/2-t
        cert = Certificate(side, a, b, c, cut, cut)
        if a > 0 and b > 0 and all(family_gates(cert, width).values()):
            return cert, width
    raise ValueError('No certificate found within the requested perturbations')


if __name__ == '__main__':
    for t in map(F, ('.842244', '.842243873', '.8422438729362')):
        cert, width = approximating_certificate(t)
        checks = family_gates(cert, width)
        print(f'[PASS] rho={2*t}, eta={(cert.b-cert.c)/2}, '
              f'{sum(checks.values())}/{len(checks)} exact gates')
    print('The limiting bound uses the written continuity proof; '
          'finite certificates alone do not prove the limit.')
    print('RESUMEN exacto: 39/39; three rational approximants')
