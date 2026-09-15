"""Exact two-ring geometry for docs/drafts/grosor_variable.md.

This finite checker verifies examples and controls. It does not prove
the universal forest exchange or area bound; see the written proof and Lean.
Areas omit the common factor pi. Tangency is permitted.
"""

from dataclasses import dataclass
from fractions import Fraction as Q


def exact(value):
    if not isinstance(value, (int, Q)) or isinstance(value, bool):
        raise TypeError('Use integers or Fraction, not floating-point values')
    return Q(value)


@dataclass(frozen=True)
class Ring:
    radius: Q
    hole: Q

    def __post_init__(self):
        object.__setattr__(self, 'radius', exact(self.radius))
        object.__setattr__(self, 'hole', exact(self.hole))
        if not 0 <= self.hole < self.radius:
            raise ValueError('Require 0 <= hole < outer radius')

    @property
    def area(self):
        return self.radius**2 - self.hole**2


def two_ring(pan, large, small):
    """Enumerate every feasible subset using the exact two-ball criterion."""
    pan = exact(pan)
    if pan <= 0 or large.radius <= small.radius:
        raise ValueError('Require positive pan and strictly decreasing radii')
    siblings = large.radius + small.radius <= pan
    nested = large.radius <= pan and small.radius <= large.hole
    feasible = [()]
    if large.radius <= pan:
        feasible.append((0,))
    if small.radius <= pan:
        feasible.append((1,))
    if siblings or nested:
        feasible.append((0, 1))
    rings = (large, small)

    def area(indices):
        return sum((rings[i].area for i in indices), Q(0))

    greedy = ()
    for i in range(2):
        if greedy + (i,) in feasible:
            greedy += (i,)
    optimal = max(feasible, key=area)
    return {'siblings': siblings, 'nested': nested,
            'feasible': tuple(feasible), 'greedy': greedy, 'optimal': optimal,
            'greedy_area': area(greedy), 'optimal_area': area(optimal),
            'rho': small.radius / large.radius,
            'ratio': area(greedy) / area(optimal) if area(optimal) else None}


def area_factor(kappa):
    kappa = exact(kappa)
    if not 0 < kappa < 1:
        raise ValueError('Require 0 < kappa < 1')
    return min(Q(1), 1/kappa**2-1)


def sharp_pair(kappa, epsilon):
    kappa, epsilon = exact(kappa), exact(epsilon)
    if not 0 < epsilon < kappa < 1:
        raise ValueError('Require 0 < epsilon < kappa < 1')
    return Q(1), Ring(1, kappa-epsilon), Ring(kappa, 0)


def thin_pair(epsilon):
    epsilon = exact(epsilon)
    if not 0 < epsilon < Q(1, 4):
        raise ValueError('Require 0 < epsilon < 1/4')
    return 1+epsilon, Ring(1+epsilon, 1-epsilon), Ring(1, 0)


def main():
    count = 0
    for kappa in (Q(7, 10), Q(3, 4), Q(9, 10), Q(99, 100)):
        for denominator in (100, 1000, 10000):
            result = two_ring(*sharp_pair(kappa, Q(1, denominator)))
            if result['siblings'] or result['nested'] or result['ratio'] < area_factor(kappa):
                raise AssertionError(result)
            count += 1
        print(f'kappa={kappa}; guaranteed factor={area_factor(kappa)}; '
              f'last exact ratio={result["ratio"]}')
    for denominator in (10, 100, 1000):
        epsilon = Q(1, denominator)
        result = two_ring(*thin_pair(epsilon))
        if result['rho'] >= 1 or result['ratio'] != 4*epsilon:
            raise AssertionError(result)
        count += 1
    print(f'RESUMEN: {count}/{count} exact family checks passed (not a universal proof).')


if __name__ == '__main__':
    main()
