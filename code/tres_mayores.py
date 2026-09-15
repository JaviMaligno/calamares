"""Reproducible witness controls for docs/drafts/tres_mayores.md.

These floating-point controls do not prove T3 or packing impossibility.
The construction explicitly returns every center, then a separate check
examines all wall and pair constraints. No optimization is used.
"""

import argparse
import json
import math
from pathlib import Path
import random

PHI = (1 + math.sqrt(5)) / 2


def tail_ratio(radii):
    total = 0.0
    result = 0.0
    for r in reversed(radii):
        result = max(result, total / r)
        total += r
    return result


def construction(radii):
    radii = list(radii)
    if len(radii) < 3 or any(not math.isfinite(r) or r <= 0 for r in radii):
        raise ValueError('At least three positive finite radii required')
    if any(x < y for x, y in zip(radii, radii[1:])) or radii[0] <= radii[1]:
        raise ValueError('Require a>b and a nonincreasing list')
    if tail_ratio(radii) > PHI + 1e-12:
        raise ValueError('Tail pressure exceeds phi')
    a, b, c = radii[:3]
    denominator = a*a + a*b + b*b
    beta = a*b*(a+b) / denominator
    if c <= beta:
        case = 'diametral_pair'
        radius = a+b
        centers = [(-b, 0.0), (a, 0.0),
                   ((a-b)*radius*radius/denominator, -2*beta)]
        if len(radii) > 3:
            e = radii[3]
            angle = 2*math.asin(math.sqrt(b*e/(a*(radius-e))))
            centers.append(((radius-e)*math.cos(angle),
                            (radius-e)*math.sin(angle)))
            remainder = math.fsum(radii[4:])
            if remainder:
                angle = math.pi - 2*math.asin(math.sqrt(
                    a*remainder/(b*(radius-remainder))))
                row_center = ((radius-remainder)*math.cos(angle),
                              (radius-remainder)*math.sin(angle))
                cursor = -remainder
                for r in radii[4:]:
                    centers.append((row_center[0]+cursor+r, row_center[1]))
                    cursor += 2*r
    else:
        case = 'tangent_triple'
        length = a+b
        ca, cb, cc = 1/a, 1/b, 1/c
        root = math.sqrt(ca*cb + ca*cc + cb*cc)
        radius = 1/(2*root-ca-cb-cc)
        opposite = 1/(4*(ca+cb)+cc-4*root)
        cx = a+(a-b)*c/length
        cy = 2*math.sqrt(a*b*c*(length+c))/length
        ox = a-(a-b)*radius/length
        oy = (a*(a+c)-radius*(a-c)-cx*ox)/cy
        centers = [(-ox, -oy), (length-ox, -oy), (cx-ox, cy-oy)]
        row_center = (a+(a-b)*opposite/length-ox,
                      -2*math.sqrt(a*b*opposite*(length+opposite))/length-oy)
        remainder = math.fsum(radii[3:])
        if remainder > opposite + 1e-10*radius:
            raise ArithmeticError('Tail exceeds the constructed opposite disk')
        cursor = -remainder
        for r in radii[3:]:
            centers.append((row_center[0]+cursor+r, row_center[1]))
            cursor += 2*r
    return radius, centers, case


def violation(radii, radius, centers):
    """Largest normalized constraint violation; tangency has residual zero."""
    if len(radii) != len(centers):
        raise ValueError('One center per radius required')
    residuals = [(math.hypot(*xy)+r-radius)/radius
                 for r, xy in zip(radii, centers)]
    residuals += [(radii[i]+radii[j]-math.dist(centers[i], centers[j]))/radius
                  for i in range(len(radii)) for j in range(i)]
    if not all(math.isfinite(x) for x in residuals):
        raise ArithmeticError('Nonfinite geometry')
    return max(residuals)


def controls(samples=10000, seed=20260915):
    rng = random.Random(seed)
    beta = PHI*(PHI+1)/(PHI*PHI+PHI+1)
    fixed = [[PHI, 1, beta, beta], [PHI, 1, 1/PHI, .5, .5],
             [1.7, 1, .5, .3, .25, .15], [1.5, 1, .9],
             [1.5, 1, .9, .2], [1.5, 1, .9, .2, .1]]
    counts = {'diametral_pair': 0, 'tangent_triple': 0}
    worst = -math.inf
    for index in range(len(fixed)+samples):
        if index < len(fixed):
            radii = fixed[index]
        else:
            radii = [1.0]
            for _ in range(rng.randrange(2, 15)):
                radii.insert(0, max(radii[0]*1.001, math.fsum(radii)/PHI)
                             * rng.uniform(1, 1.7))
        radius, centers, case = construction(radii)
        residual = violation(radii, radius, centers)
        if residual > 1e-9:
            raise AssertionError({'radii': radii, 'residual': residual})
        worst = max(worst, residual)
        counts[case] += 1

    # Controls ensure that the verifier detects a broken placement and
    # the construction refuses inputs outside its mathematical hypotheses.
    radii = fixed[0]
    radius, centers, _ = construction(radii)
    damaged = [(10*radius, 0.0), *centers[1:]]
    assert violation(radii, radius, damaged) > 1
    try:
        construction([1.01, 1, .99, .98])
    except ValueError:
        pass
    else:
        raise AssertionError('Missing tail-pressure guard')
    return {'scope': 'floating_point_witness_controls_not_universal_proof',
            'seed': seed, 'random_trials': samples, 'boundary_trials': len(fixed),
            'cases': counts, 'largest_relative_violation': worst,
            'negative_controls': 2}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--samples', type=int, default=10000)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.samples < 0:
        parser.error('--samples must be nonnegative')
    report = json.dumps(controls(args.samples), indent=2)
    if args.output:
        args.output.write_text(report+'\n', encoding='utf-8')
    print(report)
