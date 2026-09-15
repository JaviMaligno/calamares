"""Exact rational witnesses and all four executions for square twins."""

from fractions import Fraction as F
from itertools import combinations

from cuadrado_certificado import Certificate, certifies_infeasibility

SIDE = F("5.1214")
WIDTH = F(".301")
RADII = {"I1": tuple(map(F, ("2", "1", ".850", ".849"))),
         "I2": tuple(map(F, ("2", "1", ".950", ".750")))}
BALANCED = Certificate(SIDE, F(2), F(".850"), F(".849"), F("1.72"), F("1.718"))
ROOT_PIVOT = Certificate(SIDE, F(2), F(1), F(".75"), F("2.12"), F("1.39"))
UNBALANCED_CENTERS = ((F("2.96"), F(2)), (F(".95"), SIDE-F(".95")),
                      (SIDE-F(".75"), SIDE-F(".75")))


def layout_fits(side, radii, centers):
    """Verify all Cartesian constraints of a supplied rational placement."""
    if len(radii) != len(centers) or any(len(p) != 2 for p in centers):
        raise ValueError("One two-dimensional center is required for each radius")
    if any(not isinstance(x, (int, F)) for x in (side, *radii, *(v for p in centers for v in p))):
        raise TypeError("Use exact integers or Fractions")
    if side <= 0 or any(r <= 0 for r in radii):
        return False
    if any(not (r <= x <= side-r and r <= y <= side-r)
           for r, (x, y) in zip(radii, centers)):
        return False
    return all(sum((u-v)**2 for u,v in zip(centers[i],centers[j])) >= (radii[i]+radii[j])**2
               for i,j in combinations(range(len(radii)), 2))


def _root_fits(rs):
    """Exact oracle on the sibling sets reachable in the four twins runs.

    Larger sets are rejected by a certified triple subset; an unknown
    triple raises rather than treating an unsupported query as infeasible.
    """
    rs=tuple(sorted(rs, reverse=True))
    if len(rs) <= 1:
        return not rs or rs[0] <= SIDE/2
    if len(rs) == 2:
        return rs[0] <= SIDE/2 and SIDE >= sum(rs) and 2*(SIDE-sum(rs))**2 >= sum(rs)**2
    if rs[0] == 2 and rs[1] == 1 and rs[2] >= F(".75"):
        if not certifies_infeasibility(ROOT_PIVOT):
            raise RuntimeError("Invalid root-pivot certificate")
        return False
    if rs == (F(2), F(".850"), F(".849")):
        if not certifies_infeasibility(BALANCED):
            raise RuntimeError("Invalid balanced-trio certificate")
        return False
    if rs == (F(2), F(".950"), F(".750")):
        return layout_fits(SIDE, rs, UNBALANCED_CENTERS)
    raise ValueError(f"Unsupported sibling query: {rs}")


def run_greedy(instance, rule):
    """Return parent indices (-1=root, None=skipped) for an exact greedy run."""
    if rule not in ("best", "worst"):
        raise ValueError("Rule must be best or worst")
    radii=RADII[instance]
    parents=[]
    containers=[(-1, SIDE/2, [])]
    for i,r in enumerate(radii):
        candidates=[]
        for parent,capacity,children in containers:
            siblings=[radii[j] for j in children]+[r]
            if parent == -1:
                feasible=_root_fits(siblings)
            elif len(siblings) <= 2:
                feasible=sum(siblings) <= capacity
            else:
                raise ValueError("Unsupported hole query with more than two siblings")
            if feasible:
                candidates.append((parent,capacity,children))
        if not candidates:
            parents.append(None)
            continue
        choose=min if rule == "best" else max
        parent,capacity,children=choose(candidates,key=lambda item:item[1])
        children.append(i)
        parents.append(parent)
        if r > WIDTH:
            containers.append((i,r-WIDTH,[]))
    return parents


def verify_twins():
    a,m,b,c=RADII["I1"]
    _,_,u,v=RADII["I2"]
    h=a-WIDTH
    expected={('I1','best'):[-1,0,-1,None],('I1','worst'):[-1,-1,0,0],
              ('I2','best'):[-1,0,-1,-1],('I2','worst'):[-1,-1,0,None]}
    return {
        "balanced_trio_blocked":certifies_infeasibility(BALANCED),
        "root_pivot_trio_blocked":certifies_infeasibility(ROOT_PIVOT),
        "unbalanced_trio_fits":layout_fits(SIDE,(a,u,v),UNBALANCED_CENTERS),
        "root_pair_fits":layout_fits(SIDE,(a,m),((a,a),(SIDE-m,SIDE-m))),
        "hole_pair_I1":b+c == h,
        "hole_pair_I2_rejected":u+v > h,
        "pivot_can_nest":m <= h,
        "all_small_fit_individually":all(x <= h for x in (b,c,u,v)),
        "all_small_conflict_with_pivot":all(m+x > h for x in (b,c,u,v)),
        "pivot_hole_rejects_small":all(x > m-WIDTH for x in (b,c,u,v)),
        "no_small_nesting":c > b-WIDTH and v > u-WIDTH,
        "best_fit_prefers_hole":h < SIDE/2,
        "strict_order":all(all(x>y>0 for x,y in zip(rs,rs[1:])) for rs in RADII.values()),
        "shared_state":RADII['I1'][:2] == RADII['I2'][:2],
        "rho_I1":max((m+b+c)/a,b+c,c/b) == F('1.699'),
        "rho_I2":max((m+u+v)/a,u+v,v/u) == F('1.7'),
        "four_runs":all(run_greedy(*key) == value for key,value in expected.items()),
    }


if __name__ == "__main__":
    checks=verify_twins()
    for name,ok in checks.items():
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    for instance in RADII:
        for rule in ('best','worst'):
            print(instance,rule,run_greedy(instance,rule))
    print(f"RESUMEN exacto: {sum(checks.values())}/{len(checks)}")
    raise SystemExit(0 if all(checks.values()) else 1)
