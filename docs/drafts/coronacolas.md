# Corona-contra-colas (sartén): D1, D2, D3 y el argumento de dualidad

Estado: **cerrado computacionalmente** (acta CONFIRMADO CON CORRECCIONES,
2026-08-07, `VEREDICTOS.md`; script `code/coronacolas.py` 5/5). La
conversión a teorema pleno pende de UN lema (dualidad/zigzag, §4).

## 1. Los tres resultados

**(D2) Corolario DS-sartén (pequeños extra) — PROBADO, sin geometría.**
Todo anillo extra e < m se adjunta al perfil: S⁺ := S ∪ {extras}. El
bloqueo hace fallar todas las colocaciones-testigo de los teoremas
aplicados a S⁺ (los extras son piezas < 1 y el re-empaquetado es
existencial), luego DP/DP-p/DPr valen VERBATIM con S⁺. Los extras en
agujeros ya están contados en las X. El residuo de la partición sobre
S⁺ es exactamente la celda D1 (verificado sobre 200k instancias, 0 sin
caso). — Este es un resultado completo, no computacional.

**(D1) La celda final {p ≥ 4, σ₁+M ≤ 1, j ≥ 3}** y
**(D3) el pivote sólido ω ≥ 1, j ≥ 3**: vacíos de bloqueos con ρ ≤ φ,
por la cadena de §2, verificada en malla+MC+esquinas con **dualidad
exacta** (déficit 0.0 uniforme). D3 no usa la anchura en ningún paso.

## 2. La cadena

Supóngase bloqueo con ρ ≤ φ.

1. **Cascada de colas**: la cola de o_k contiene a los ocupantes
   menores, m y todo el perfil ⟹ o_k ≥ (Σ_{i>k} o_i + 1 + Σ)/φ.
   Cuasi-empates: la primera copia contiene a las siguientes ⟹
   o ≥ φ(1+Σ) (¡factor φ² sobre la ingenua!).
2. **Cota inferior del radio real, R ≥ R_lb** (lema del certificado
   angular, §3): F empaqueta {O, m} en R; para todo subconjunto y todo
   orden angular, la suma cíclica de separaciones mínimas γ ≤ 2π.
3. **Suficiencia constructiva en R_lb**: la corona cíclica en zigzag
   (posiciones por camino más largo, TODAS las parejas validadas, polvo
   y medianos a los bolsillos de Descartes como bins de fila) coloca el
   re-empaquetado {O, m} ∪ (S⁺∖σ₁) con σ₁ → D_m. Trasladada al disco
   R ≥ R_lb, desbloquea. Contradicción. ∎ (módulo §4)

## 3. El lema del certificado angular (nuevo, adversariado)

Para un par (a, b) en CUALQUIER empaquetamiento del disco R con centros
a distancias d_a ∈ [dmin_a, R−a], d_b ∈ [dmin_b, R−b]:

    cos γ ≤ h(d_a, d_b) := (d_a² + d_b² − (a+b)²)/(2 d_a d_b)

y el máximo de h sobre la caja está en una ESQUINA: en cada arista,
∂h/∂d tiene un único cambio de signo −→+ (mínimo interior). Luego
γ ≥ arccos(máx h en esquinas). Casos: sin confinamiento y R ≥
máx+2·mín, h alcanza 1 (apilamiento radial: certificado vacuo); el
**confinamiento por el gigante** (|c| ≥ 2o₁+r−R, desigualdad
triangular) lo reactiva. La suma de separaciones consecutivas en el
orden angular real es 2π ⟹ certificado por subconjuntos (un
subconjunto de un empaquetamiento es un empaquetamiento; el máximo
sobre subconjuntos evita que una pieza apilable haga de teletransporte).

## 4. El lema pendiente (dualidad / zigzag)

La evidencia: en R = R_lb la construcción de §2.3 tiene déficit 0.0
UNIFORME (todas las celdas (j,p) muestreadas, 185k + 4 284 esquinas +
validación euclidiana 1 500/1 500) — necesidad y suficiencia usan los
mismos certificados y coinciden en la frontera, donde la colocación es
tangente (legal: interiores disjuntos).

Para el teorema sobre (j, p) ARBITRARIOS falta probar: *en el orden
zigzag, el camino más largo del sistema de diferencias coincide con la
suma consecutiva* (ningún atajo de subsecuencia domina), de modo que la
factibilidad de la necesidad implique la de la construcción. La
herramienta es la MISMA convexidad/majorización con la que el paper
prueba la optimalidad del zigzag para el criterio k = 4
(θ = g(log f(a) + log f(b)) con g convexa): los grandes no deben ser
vecinos angulares, y en zigzag las parejas no adyacentes quedan
separadas por sumas que dominan su θ. El caso k = 5 añade el
pentagrama; nuestro chequeo constructivo (todas las parejas) es
suficiente para todo k, así que el lema solo necesita la dirección
«zigzag realiza el óptimo», no un criterio exacto.

## 5. Controles

- **La instancia áurea nunca se certifica**: en ε = 0 la construcción
  reproduce su tangencia exacta — sin²(θ(φ,σ)/2) = (φ+1)/(φ+2) y
  sin²(θ(1,σ)/2) = 1/(φ+2) suman 1 (suma cíclica = 2π exacto en
  σ = φ/2); para ε > 0 el ciclo excede 2π y los bolsillos espejo miden
  exactamente b(φ) = φ/2 < σ. La dualidad reconoce al contraejemplo
  como el punto crítico del modelo.
- Sin colas, la corona falla (la pared no es vacua).
- El rincón C3.3 de rstar se reproduce por debajo.

## 6. Qué implica y qué falta

Con D1–D3: **la sartén queda cerrada** — todo intercambio de sartén
bloqueado tiene ρ > φ, para todo perfil (con extras), toda ocupación y
todo ω > 0 — con el único asterisco del lema de §4 para (j, p) fuera
de los rangos barridos. Faltan: la versión anidada (D4–D6, misma
maquinaria) y el ensamblaje.
