# Calamares — capa de certificados exactos en Lean 4

Formalización en Lean 4 (v4.32.2, **solo core, sin mathlib**) de la capa de
identidades algebraicas exactas sobre la que descansan las pruebas del paper
de empaquetamiento de anillos (`paper/main.tex`). Cero `sorry`, cero axiomas
nuevos: todos los teoremas se demuestran con `decide +kernel` (aritmética
exacta reducida por el kernel; verificado con `#print axioms` que solo
dependen de `propext`, `Classical.choice`, `Quot.sound` — los tres axiomas
estándar de core — y ninguno de `Lean.ofReduceBool` ni `sorryAx`).

## Qué formaliza

La **capa de certificados exactos**: las identidades de aritmética exacta en
ℚ y ℚ[√5] que los scripts de `code/` verifican con sympy y sobre las que se
apoyan los teoremas del paper.

- La aritmética áurea del contraejemplo (`thm:golden`): φ² = φ+1, la rigidez
  b2(φ,1) = φ/2, la cola áurea, el punto fijo y su factorización en ℤ[A], el
  certificado del testigo con s* = 4(√5−2), el margen ε₀ y la ventana de ω.
- Los certificados de los medios metálicos de la Batalla 2 / Teorema P
  (`thm:DP`): 2b(φ) = φ, g(φ) = φ, el certificado polinomial de que g es
  decreciente, y las evaluaciones Ψ(1/2) = φ, Ψ_B(1) = φ, Ψ₂(φ/2) = φ,
  Ψ₃(1) = √3 > φ (con el patrón de eliminación de raíces cuadradas:
  se exhibe x con x² = radicando y x > 0).
- El suelo Tribonacci (`thm:rigidfloor`): P(φ) = −1 < 0, el encajonamiento
  1.8392 < T < 1.8393 y el certificado de monotonía estricta de P en x ≥ 1
  (P(1+e+d) − P(1+e) = d·Q(e,d) con Q de coeficientes ≥ 0 y coeficiente de
  d con término constante 2 > 0).
- La esquina 13/7 (`thm:corner`): γ_{2/7} = 2 y 1 + b(2) = 13/7.
- Los certificados de perfiles mayores (`thm:DPp`): la legalidad
  universal de los espejos (φ−1 < 2/3 = b(1)) y las cadenas pesadas.
- La **pinza** que cierra j = 3 del intercambio a sartén (`thm:DP` (iv)):
  la constante exacta s* = (6φ−1)/(2φ+1) = 11−4√5 = 15−8φ, que s < 2 la
  cumple, y la contradicción en el extremo (φ³ = 4.236 < φ+3 = 4.618, con
  margen exactamente 2−φ).
- La cobertura T/2 < s* (vía 18393/20000 < 4√5 − 8).
- El umbral aditivo: la familia (1/4+2δ/3, 1/4+δ/3)/(1/2) = 1+2δ como
  identidad de polinomios en δ.

## Qué NO formaliza

La **geometría de empaquetamiento**: rigidez de coronas, criterios angulares
θ(a,b,R), árboles de colocación del voraz, evacuaciones y bolsillos espejo.
Esa capa está verificada por los scripts de `code/` (bloques B–E de
`aureo.py` y `batalla2.py`, `corona.py`, `rigido.py`, …); aquí solo se
formaliza el esqueleto algebraico exacto que esos argumentos consumen.

## Estructura

- `Calamares/Basic.lean` — `Q5` = ℚ[x]/(x²−5) como pares `(a b : Rat)` con
  aritmética completa; el orden del encaje real con √5 > 0 (`Q5.posb`,
  decidible); polinomios como listas de coeficientes ascendentes: `Poly`
  (ℚ[X]), `PolyZ` (ℤ[X]) y `Poly2` ((ℚ[e])[d]).
- `Calamares/Identities.lean` — los teoremas 1–30.
- `Calamares.lean` — raíz de la librería.

Nota técnica: `decide` a secas se atasca con `Rat` (el elaborador no reduce
`Nat.gcd`, definido por recursión bien fundada); `decide +kernel` sí
funciona porque el kernel acelera `Nat.gcd` sobre literales. No hace falta
`native_decide` en ningún teorema.

## Tabla teorema Lean ↔ resultado del paper ↔ script

| # | Teorema Lean | Resultado del paper | Script |
|---|---|---|---|
| 1 | `phi_sq`, `phi_pos` | `thm:golden` | `aureo.py` [A] |
| 2 | `b2_phi_one` | `thm:golden` (rigidez S5) | `aureo.py` [A] |
| 3 | `tail_golden` | `thm:golden` | `aureo.py` [A] |
| 4 | `fixed_point` | `thm:golden` / `thm:DP` | `aureo.py` [A] |
| 5 | `fixed_point_factor` | `thm:golden` / `thm:DP` | `aureo.py` [A] |
| 6 | `witness_cert` | `thm:golden` (testigo, s*) | `aureo.py` [A] |
| 7 | `eight_phi`, `phi_cubed` | `thm:golden` (cadena del testigo) | `aureo.py` [A] |
| 8 | `eps0_margin` | `thm:golden` (margen ε₀) | `aureo.py` [A] |
| 9 | `window` | `thm:golden` (ventana de ω) | `aureo.py` [A] |
| 10 | `two_b_phi`, `g_phi` | `thm:DP` (caso j = 1) | `batalla2.py` [A] |
| 11 | `g_decreasing_cert` | `thm:DP` (g decreciente) | `batalla2.py` [A] |
| 12 | `Psi_half` | `thm:DP` (Ψ(1/2) = φ) | `batalla2.py` [A] |
| 13 | `PsiB_one` | `thm:DP` (rama B, Ψ_B(1) = φ) | `batalla2.py` [A] |
| 14 | `Psi2_goldenhalf` | `thm:DP` (rama A, Ψ₂(φ/2) = φ) | `batalla2.py` [A] |
| 15 | `Psi3_gt_phi` | `thm:DP` (rama A, Ψ₃(1) = √3 > φ) | `batalla2.py` [A] |
| 16 | `P_phi` | `thm:rigidfloor` (φ < T) | `striple.py` |
| 17 | `T_bracket` | `thm:rigidfloor` (1.8392 < T < 1.8393) | `striple.py` / `cuadrado.py` |
| 18 | `P_mono_cert` | `thm:rigidfloor` (P creciente en x ≥ 1) | `striple.py` |
| 19 | `gamma_27` | `thm:corner` (carve-out, γ_{2/7} = 2) | `esquina.py` |
| 20 | `corner_137` | `thm:corner` (ínfimo 13/7) | `esquina.py` |
| 21 | `coverage` | `thm:golden` + `thm:rigidfloor` (T/2 < s*) | `aureo.py` [C] |
| 22 | `additive_family` | umbral aditivo | `umbral.py` / `frontera.py` |
| 23 | `tail_crossing` | `thm:DP` (iv) (3/φ+3 = 3φ) | `microcelda.py` [A] |
| 24 | `inv_two_sub_phi` | `thm:DP` (iv) (el factor de (C4)) | `microcelda.py` [A] |
| 25 | `pincer_constant` | `thm:DP` (iv) (s* = 11−4√5 = 15−8φ) | `microcelda.py` [A] |
| 26 | `pincer_applies` | `thm:DP` (iv) (s < 2 < s*) | `microcelda.py` [A] |
| 27 | `pincer_gap` | `thm:DP` (iv) (φ³ < φ+3, margen 2−φ) | `microcelda.py` [B] |
| 28 | `pincer_child` | `thm:DP` (iv) (la torre no acaba en v*) | `microcelda.py` [A] |
| 29 | `mirror_legal` | `thm:DPp` (v)-(vi) (φ−1 < 2/3 = b(1)) | `perfilp.py` [A] |
| 30 | `heavy_chains` | `thm:DPp` (iii),(vi) (cadenas pesadas) | `perfilp.py` [A]/[C] |

## Compilar

```bash
cd lean
lake build   # exit 0, sin sorry, sin warnings
```
