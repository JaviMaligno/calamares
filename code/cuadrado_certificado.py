"""Rational certificates for the square counterexample; no numerical solver."""

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Certificate:
    side: Fraction
    a: Fraction
    b: Fraction
    c: Fraction
    p: Fraction
    q: Fraction


def certifies_infeasibility(cert: Certificate) -> bool:
    """Whether the written quadrant-confinement lemma excludes the triple."""
    values = (cert.side, cert.a, cert.b, cert.c, cert.p, cert.q)
    if any(not isinstance(v, (int, Fraction)) for v in values):
        raise TypeError("Certificates require integers or Fractions, never floats")
    side, a, b, c, p, q = map(Fraction, values)
    width = side - c - a - q
    return (
        0 < c <= b <= a <= side / 2
        and 0 <= q <= p
        and p >= side / 2 - b
        and p * p + (side - a - b) ** 2 < (a + b) ** 2
        and q * q + (side - a - c) ** 2 < (a + c) ** 2
        and p + q >= side - b - c
        and width >= 0
        and 2 * width * width < (b + c) ** 2
    )


def verify_d() -> dict[str, bool]:
    """All scalar gates for the explicit four-ring witness and bad greedy run."""
    F = Fraction
    side, a, b, c, p, q = map(F, ("4.8568", "1.845", ".844", ".841", "1.591", "1.581"))
    w, pivot = F(".16"), F(1)
    rho = F(337, 200)
    lo, hi = F(17, 10), F(43, 25)
    return {
        "proper_rings": w > 0 and 0 < c < b < pivot < a,
        "triple": certifies_infeasibility(Certificate(side, a, b, c, p, q)),
        "root_pair": a <= side/2 and 2*(side-a-pivot)**2 > (a+pivot)**2,
        "hole_pair": b+c == a-w,
        "nest_pivot": pivot <= a-w,
        "best_fit": a-w < side/2,
        "b_not_with_pivot": pivot+b > a-w,
        "c_not_with_pivot": pivot+c > a-w,
        "b_not_in_pivot": b > pivot-w,
        "c_not_in_pivot": c > pivot-w,
        "c_not_in_b": c > b-w,
        "tail_a": (pivot+b+c)/a < rho,
        "tail_b": c/b < rho,
        "rho": (b+c)/pivot == rho,
        "below_X_bracket": rho < lo,
        "X_lower_sign": 17*lo**4-4*lo**3-62*lo**2+4*lo+49 < 0,
        "X_upper_sign": 17*hi**4-4*hi**3-62*hi**2+4*hi+49 > 0,
    }


if __name__ == "__main__":
    checks = verify_d()
    for name, ok in checks.items():
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"RESUMEN exacto: {sum(checks.values())}/{len(checks)}; rho = 337/200 = 1.685")
    raise SystemExit(0 if all(checks.values()) else 1)
