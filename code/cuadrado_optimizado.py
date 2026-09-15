"""A finite exact upper bound; the later limit proof is in cuadrado_limite.md."""

from fractions import Fraction as F
from cuadrado_certificado import Certificate, certifies_infeasibility

IMPROVED=Certificate(*map(F,('4.85201606','1.8422452','.8422451','.8422449','1.5837677','1.5837671')))
WIDTH=F('.1577552')


def family_gates(cert,width):
    """Sufficient exact gates for the nested-pivot counterexample family."""
    if not isinstance(width,(int,F)):
        raise TypeError('Use an exact width')
    s,a,b,c=cert.side,cert.a,cert.b,cert.c
    if not (a>0 and b>0):
        raise ValueError('Positive leading radii are required')
    h=a-width
    rho=b+c
    return {
        'proper_rings':a>1>b>c>0 and width>0,
        'triple':certifies_infeasibility(cert),
        'root_pair':a<=s/2 and 1<=s/2 and s-a-1>=0 and 2*(s-a-1)**2>=(a+1)**2,
        'hole_pair':b+c<=h,
        'pivot_nests':1<=h,
        'best_fit':h<s/2,
        'b_not_with_pivot':1+b>h,
        'c_not_with_pivot':1+c>h,
        'b_not_in_pivot':b>1-width,
        'c_not_in_pivot':c>1-width,
        'c_not_in_b':c>b-width,
        'tail_a':(1+b+c)/a<=rho,
        'tail_b':c/b<=rho,
    }


if __name__ == '__main__':
    gates=family_gates(IMPROVED,WIDTH)
    for name,ok in gates.items():
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    rho=IMPROVED.b+IMPROVED.c
    print(f'PROVED upper bound: rho = {rho} = {float(rho):.8f}')
    print('This script certifies the finite bound only; see cuadrado_limite.md for the later limit proof.')
    print(f'RESUMEN exacto: {sum(gates.values())}/{len(gates)}')
    raise SystemExit(0 if all(gates.values()) else 1)
