"""rho*_4 = rho*_3 (docs/drafts/cuatro.md): el perfil de cuatro aros no baja el umbral.

Proposicion 8: para todo omega en (0,1),

    rho*_4(omega) = rho*_3(omega) = max(1, min(2(1-w), max(phi, 2/(1+2w)))).

La prueba es puramente aditiva (Lema 0 + criterio exacto del par), con el arbol:
  - Sigma <= 1 => fila en A: reinsertable. Luego Sigma > 1 (cubre w >= 1/2).
  - w < 1/2 y rho < 2(1-w) =: 2 beta (si no, listo). Entonces:
    (0) a lo sumo un aro supera beta;
    (A) s1 > beta: {s2,s3,s4} -> B falla => s2+s3+s4 > beta => Sigma > 2 beta. Contra.
    (B) todos <= beta:
      B1 (s4 > s1-w, sin anidamientos): s1->B + {s2,s3,s4}->A falla => q3 > 1,
         y q3 >= 3 s4 > 3(s1-w): el programa min max(s1+q, q/s1) con
         q > max(1, 3(s1-w)) esta contenido en el del caso (iv) de perfil_tres
         (3(s1-w) >= 2(s1-w)): cota >= infimo del caso (iv) >= rho*_3.
      B2 (s4 <= s1-w, s3 > s1-w): s4 en s1, s1->B, {s2,s3}->A falla => q2 > 1;
         q2 >= 2 s3 > 2(s1-w): EXACTAMENTE el caso (iv) de perfil_tres.
      B3 (s4 <= s1-w, s3 <= s1-w): si s4 <= s2-w, la colocacion s3 en s1 -> A,
         s4 en s2 -> B es valida (contra bloqueo): luego s4 > s2-w. Los repartos
         s4 en s1 -> B + {s2,s3} -> A  y  s3 en s1 -> B + {s2,s4} -> A fallan:
         s2+s3 > 1 y s2+s4 > 1 => s3, s4 > 1-s2 => Sigma > 2 + (s1-s2) >= 2. Contra.
  (<=) es el argumento del polvo de perfil_tres.

Corolario 5: omega_c = omega_T = 1/T - 1/2 exacto (con el Corolario 2, que
excluye k >= 5 bajo T, y el Corolario 4).

Bloques: [A] identidades y dominaciones simbolicas, [B] busqueda adversaria con
oraculo generoso (nada bloqueado por debajo de rho*_3), [C] validacion mecanica
del arbol sobre perfiles bloqueados muestreados, [D] familias de polvo que
alcanzan rho*_3 en cada tramo.
"""
import math
import random
import itertools

TWO_PI = 2 * math.pi
PHI = (1 + math.sqrt(5)) / 2
TRIB = 1.839286755214161


def rho3(w):
    return max(1.0, min(2 * (1 - w), max(PHI, 2 / (1 + 2 * w))))


def rho_needed(S):
    S = sorted(S, reverse=True)
    r = sum(S)
    for j in range(len(S)):
        tail = sum(S[j + 1:])
        if tail > 0:
            r = max(r, tail / S[j])
    return r


# ---------------- oraculo generoso de reinsercion ----------------

def theta(a, b, R):
    p = (a / (R - a)) * (b / (R - b))
    if p >= 1.0:
        return math.pi if p <= 1 + 1e-12 else math.inf
    return 2 * math.asin(math.sqrt(p))


def feas3(a, b, c, R):
    if a + b > R or a + c > R or b + c > R:
        return False
    return theta(a, b, R) + theta(a, c, R) + theta(b, c, R) <= TWO_PI + 1e-12


def group_fits(group, cap):
    """Certificados de colocacion para un grupo de hermanos en capacidad cap.
    Generoso: fila (suficiente, todo k), suma exacta (k<=2), angular (k=3)."""
    g = sorted(group, reverse=True)
    if not g:
        return True
    if sum(g) <= cap:
        return True
    if len(g) == 1:
        return g[0] <= cap
    if len(g) == 2:
        return g[0] + g[1] <= cap
    if len(g) == 3:
        return feas3(g[0], g[1], g[2], cap)
    return False


def reinsertable(S, w):
    """Oraculo: todos los bosques de anidamiento (x en y sii x <= y - w, agujeros
    con contenido multiple via group_fits) y todos los repartos A/B del nivel
    superior. Cuanto mas generoso, menos bloqueados: sesgo seguro para [B]."""
    beta = 1 - w
    n = len(S)
    opciones = [[-1] + [j for j in range(n) if j != i] for i in range(n)]
    for parents in itertools.product(*opciones):
        ok = True
        for i, p in enumerate(parents):
            if p != -1 and not (S[i] <= S[p] - w + 1e-15):
                ok = False
                break
        if not ok:
            continue
        holes = {}
        for i, p in enumerate(parents):
            if p != -1:
                holes.setdefault(p, []).append(S[i])
        if any(not group_fits(cont, S[p] - w) for p, cont in holes.items()):
            continue
        top = [S[i] for i, p in enumerate(parents) if p == -1]
        m = len(top)
        for mask in range(1 << m):
            GA = [top[i] for i in range(m) if mask >> i & 1]
            GB = [top[i] for i in range(m) if not mask >> i & 1]
            if group_fits(GA, 1.0) and group_fits(GB, beta):
                return True
    return False


def check(label, ok):
    print(f"  [{'OK' if ok else 'FALLO'}] {label}")
    return ok


# ---------------- [A] identidades y dominaciones ----------------

def bloque_A():
    import sympy as sp
    w, s, q = sp.symbols('omega s q', positive=True)
    ok = True
    # A1: dominacion de B1 sobre el caso (iv): 3(s-w) >= 2(s-w) y
    #     3/(1+3w) > 2/(1+2w) para todo w > 0.
    ok &= check("A1 3/(1+3w) - 2/(1+2w) = 1/((1+3w)(1+2w)) > 0",
                sp.simplify(3 / (1 + 3 * w) - 2 / (1 + 2 * w)
                            - 1 / ((1 + 3 * w) * (1 + 2 * w))) == 0)
    # A2: B3: de s2+s3 > 1 y s2+s4 > 1 sale Sigma > 2 + (s1 - s2) >= 2:
    #     identidad s1 + s2 + (1-s2) + (1-s2) = 2 + s1 - s2.
    s1, s2 = sp.symbols('s1 s2', positive=True)
    ok &= check("A2 s1 + s2 + 2(1-s2) = 2 + (s1 - s2)",
                sp.simplify(s1 + s2 + 2 * (1 - s2) - (2 + s1 - s2)) == 0)
    # A3: el minimo aureo de la rama Q=1: min max(1+s, 1/s) = phi en s = 1/phi.
    ok &= check("A3 1 + 1/phi = phi (punto fijo del maximo)",
                sp.simplify(1 + 2 / (1 + sp.sqrt(5)) - (1 + sp.sqrt(5)) / 2) == 0)
    # A4: cruce de la hiperbola del caso (iv) con T: omega_T = 1/T - 1/2, y
    #     2/(1+2w) = T en w = omega_T (identidad directa).
    T = sp.symbols('T', positive=True)
    ok &= check("A4 2/(1+2(1/T-1/2)) = T (identidad directa)",
                sp.simplify(2 / (1 + 2 * (1 / T - sp.Rational(1, 2))) - T) == 0)
    # A5: rho*_3 en el tramo de la hiperbola supera a phi sii w < (sqrt5-2)/2
    #     (el cruce de perfil_tres), y 2(1-w) > 2/(1+2w) sii w(1-2w) > 0.
    ok &= check("A5 2(1-w)(1+2w) - 2 = 2w(1-2w)",
                sp.simplify(2 * (1 - w) * (1 + 2 * w) - 2 - 2 * w * (1 - 2 * w)) == 0)
    return ok


# ---------------- [B] busqueda adversaria ----------------

def muestras(w, rnd, n_total):
    """Muestreo dirigido a las familias criticas (CON polvo) + aleatorio."""
    beta = 1 - w
    for _ in range(n_total):
        kind = rnd.random()
        if kind < 0.25:      # caso (iv) + polvo
            s1 = 0.5 + w + rnd.uniform(-0.03, 0.06)
            s2 = 0.5 + rnd.uniform(0, 0.05)
            s3 = 0.5 + rnd.uniform(0, 0.03)
            s4 = rnd.choice((rnd.uniform(1e-4, 0.05), rnd.uniform(0.05, 0.5)))
        elif kind < 0.45:    # caso (i) + polvo (gemelos en max(beta, 1/2))
            base = max(beta, 0.5)
            s1 = base + rnd.uniform(0, 0.02)
            s2 = base + rnd.uniform(0, 0.02)
            s3 = rnd.uniform(1e-3, 0.3)
            s4 = rnd.uniform(1e-4, s3)
        elif kind < 0.6:     # meseta
            s1 = 1 / PHI + rnd.uniform(-0.03, 0.03)
            s2 = 0.5 + rnd.uniform(0, 0.04)
            s3 = 0.5 + rnd.uniform(0, 0.02)
            s4 = rnd.uniform(1e-4, 0.1)
        elif kind < 0.8:     # cuatro en banda (anti-B1)
            base = rnd.uniform(0.3, 0.6)
            s1 = base + w + rnd.uniform(0, 0.05)
            s2 = base + rnd.uniform(0, 0.04)
            s3 = base + rnd.uniform(0, 0.02)
            s4 = base + rnd.uniform(0, 0.01)
        else:                # aleatorio
            s1, s2, s3, s4 = (rnd.uniform(0.02, 0.999) for _ in range(4))
        S = sorted((min(max(x, 1e-4), 0.999) for x in (s1, s2, s3, s4)),
                   reverse=True)
        yield S


def bloque_B():
    ok = True
    print("     w        rho3      min bloqueado   margen")
    peor = math.inf
    for w in (0.02, 0.0437, 0.05, 0.08, 0.10, 0.118, 0.15, 0.19, 0.25,
              0.35, 0.45, 0.55, 0.7):
        rnd = random.Random(12345)
        r3 = rho3(w)
        best = None
        for S in muestras(w, rnd, 30000):
            r = rho_needed(S)
            if r >= r3 + 0.08 or (best is not None and r >= best):
                continue
            if not reinsertable(S, w):
                best = r
        margen = (best - r3) if best is not None else math.nan
        peor = min(peor, margen if best is not None else math.inf)
        print(f"     {w:<8} {r3:.6f}  "
              + (f"{best:.6f}      {margen:+.2e}" if best is not None
                 else "(nada bajo rho3+0.08)"))
    ok &= check(f"B  ningun bloqueo por debajo de rho*_3 (peor margen {peor:+.2e})",
                peor > -1e-9)
    return ok


# ---------------- [C] validacion mecanica del arbol ----------------

def clasifica_y_acota(S, w):
    """Devuelve (rama, cota_inferior_del_arbol) para un perfil bloqueado."""
    s1, s2, s3, s4 = S
    beta = 1 - w
    Sig = sum(S)
    rho = rho_needed(S)
    if w >= 0.5:
        return ('w>=1/2', 1.0 if Sig > 1 else math.inf)
    if rho >= 2 * beta - 1e-12:
        return ('rho>=2beta', 2 * beta)
    if s2 > beta:
        return ('dos>beta', math.inf)      # imposible bajo rho < 2beta
    if s1 > beta:
        return ('A', math.inf)             # imposible: Sigma > 2beta
    # subcaso B
    q3 = s2 + s3 + s4
    if s4 > s1 - w:
        # B1: q3 > 1 y q3 > 3(s1-w)
        cond = q3 > 1 - 1e-12 and q3 > 3 * (s1 - w) - 1e-12
        return ('B1', max(s1 + q3, q3 / s1) if cond else -math.inf)
    if s3 > s1 - w:
        q2 = s2 + s3
        cond = q2 > 1 - 1e-12 and q2 > 2 * (s1 - w) - 1e-12
        return ('B2', max(s1 + q2, q2 / s1) if cond else -math.inf)
    # B3
    cond = s4 > s2 - w - 1e-12 and s2 + s3 > 1 - 1e-12 and s2 + s4 > 1 - 1e-12
    return ('B3', Sig if cond else -math.inf)


def bloque_C():
    ok = True
    fallos, n_block = 0, 0
    ramas = {}
    for w in (0.03, 0.0437, 0.06, 0.10, 0.15, 0.22, 0.30, 0.42, 0.55):
        rnd = random.Random(999)
        r3 = rho3(w)
        for S in muestras(w, rnd, 8000):
            if rho_needed(S) >= r3 + 0.4:
                continue
            if reinsertable(S, w):
                continue
            n_block += 1
            rama, cota = clasifica_y_acota(S, w)
            ramas[rama] = ramas.get(rama, 0) + 1
            # la cota del arbol debe (i) estar bien definida (condiciones
            # forzadas ciertas) y (ii) valer >= rho*_3 o >= 2beta o Sigma > 2
            if cota == -math.inf:
                fallos += 1
            elif cota is not math.inf and cota < r3 - 1e-9:
                fallos += 1
    print(f"     bloqueados analizados: {n_block}; por rama: {ramas}")
    ok &= check(f"C  condiciones forzadas del arbol y cotas >= rho*_3 "
                f"({fallos} fallos)", fallos == 0 and n_block > 500)
    return ok


# ---------------- [D] familias de polvo ----------------

def bloque_D():
    ok = True
    eps, dust = 1e-5, 1e-6
    casos = [
        ("hiperbola w=0.05", 0.05,
         lambda w: [0.5 + w, 0.5 + eps, 0.5 + eps, dust]),
        ("hiperbola w=omega_T", 1 / TRIB - 0.5,
         lambda w: [0.5 + w, 0.5 + eps, 0.5 + eps, dust]),
        ("meseta w=0.15", 0.15,
         lambda w: [1 / PHI, 0.5 + eps, 0.5 + eps, dust]),
        ("2(1-w) w=0.25", 0.25,
         lambda w: [1 - w + eps, 1 - w + eps, dust, dust / 2]),
        ("w=0.55", 0.55,
         lambda w: [0.5 + eps, 0.5 + eps, dust, dust / 2]),
    ]
    worst = 0.0
    for nombre, w, fam in casos:
        S = sorted(fam(w), reverse=True)
        blocked = not reinsertable(S, w)
        d = rho_needed(S) - rho3(w)
        worst = max(worst, abs(d))
        okc = blocked and 0 <= d < 1e-3
        ok &= check(f"D  {nombre}: bloqueado={blocked}, rho - rho3 = {d:+.1e}", okc)
    # el cruce con T en omega_T (Corolario 5): rho*_4(w_T) = rho*_3(w_T) = T
    wT = 1 / TRIB - 0.5
    ok &= check(f"D  omega_T = 1/T - 1/2 = {wT:.9f} y rho*_3(w_T) = T "
                f"(err {abs(rho3(wT) - TRIB):.1e})", abs(rho3(wT) - TRIB) < 1e-12)
    return ok


if __name__ == "__main__":
    print(f"phi = {PHI:.6f}  T = {TRIB:.6f}  omega_T = {1 / TRIB - 0.5:.9f}\n")
    res = []
    print("[A] identidades y dominaciones (sympy)")
    res.append(bloque_A())
    print("\n[B] busqueda adversaria con oraculo generoso")
    res.append(bloque_B())
    print("\n[C] validacion mecanica del arbol de la prueba")
    res.append(bloque_C())
    print("\n[D] familias de polvo por tramo y Corolario 5")
    res.append(bloque_D())
    print(f"\nRESULTADO: {sum(res)}/{len(res)} bloques OK"
          + ("" if all(res) else "  <-- REVISAR"))
