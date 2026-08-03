# El umbral es áureo: contraejemplo a la conjetura del umbral de Tribonacci

Borrador. Primer resultado de la **Batalla 2** (u = sartén,
`universal.md` §3) — y es una bomba: la Batalla 2 no defiende T, lo
refuta. La conjetura del umbral de Tribonacci (`resultados.md` §5quater,
Conjecture del paper) afirmaba que la obliviousness de colocación vale
para todo ρ < T; es **FALSA**. El umbral geométrico es a lo sumo φ:

**Teorema A1 (la familia áurea).** Para todo ω ∈ (1 − φ/2, φ − 1) =
(0.1910, 0.6180) y todo ε > 0 suficientemente pequeño, la instancia

    sartén R = φ + 1 ,   anchura w = ω ,
    radios {φ, 1, φ/2 + 2ε, φ/2 + ε}      (estrictos) ,

cumple ρ = φ + 3ε < T, su conjunto lex-max son los CUATRO aros, y el
voraz con worst fit coloca solo TRES: la obliviousness de colocación
falla en ρ = φ + 3ε. (La forma simétrica {φ, 1, s, s} con s = φ/2 + ε
funciona igual con ρ = φ + 2ε; la versión estricta respeta la
convención r₁ > … > r_n del paper — matiz del acta.)

*Demostración.* Todos los criterios que siguen son exactos.

1. **ρ = φ + 2ε.** Radios ordenados {φ, 1, s, s}: la cola de φ es
   (1 + 2s)/φ = (1 + φ)/φ + 2ε/φ = φ + 2ε/φ (identidad áurea); la cola
   de m = 1 es 2s = φ + 2ε, que domina; la de s es 1. Y
   φ + 2ε < T ⟺ ε < (T − φ)/2 = 0.1106….

2. **El testigo (lex-max = 4 aros).** m = 1 va al agujero de φ
   (capacidad φ − ω ≥ 1 ⟺ ω ≤ φ − 1 ✓); {φ, s, s} van a la sartén: su
   corona existe — F = 2θ(φ, s) + θ(s, s) = 5.004 < 2π con holgura 1.28
   (en ε → 0; colocación explícita con distancias verificadas en el
   bloque [B]). Cuatro aros colocados.

3. **El voraz con worst fit se atasca en 3.** Orden decreciente:
   φ → sartén. m = 1: cabe en la sartén (φ + 1 = R, par exacto, tangencia
   diametral — legal como en las gemelas) y en el agujero de φ; worst fit
   (el contenedor mayor) elige la **sartén**. Ahora {φ, 1} llena la
   sartén por tangencia diametral: es la configuración **rígida** de la
   Proposición S5, y todo tercer círculo disjunto tiene radio
   ≤ b₂(φ, 1) = φ/2 **exacto** (¡el par {φ, 1} tiene bolsillo φ/2, la
   identidad b(φ) = φ/2 del programa!). Entonces:
   - s = φ/2 + ε > φ/2: **ni s₁ ni s₂ caben en la sartén** (S5, sin
     criterio angular).
   - s → agujero de φ: cabe UNA (s ≤ φ − ω); las dos no: par exacto
     2s = φ + 2ε > φ − ω para todo ω > −2ε. El voraz mete s₁ ahí.
   - s₂ → H_m: s > 1 − ω ⟺ ω > 1 − φ/2 − ε ✓ (la ventana).
   - s₂ → agujero de s₁: s ≤ s − ω imposible.
   El árbol exhaustivo de colocaciones (bloque [B]) confirma: máximo
   alcanzable con m en la sartén = 3. ∎

**Lectura: por qué cae T y aparece φ.** La escalera de la Proposición 3
(φ → 1.799 → T, `resultados.md` §9) subía de φ a T usando la
**capacidad del testigo (W)** — «S cabía en u, luego σ₁ + σ₂ ≤ α − ω» —
y (W) existe solo cuando u = c_F(m) es un **agujero**. En la Batalla 2
(u = sartén) el testigo tiene a S en la sartén, sin pared de capacidad:
el programa pierde (W) y el ínfimo cae exactamente al primer peldaño de
la escalera, el del bolsillo de Descartes: **φ**. La instancia es áurea
por partida cuádruple: A = φ (el punto fijo 2b(A)·A = 1 + 2b(A)),
bolsillo b₂(φ,1) = φ/2, cola de φ = (1+φ)/φ = φ, y ρ = 2s → φ.

**Robustez.** No es una familia de medida nula: con holgura
R = φ + 1 + δ el bloqueo sobrevive (vía el criterio angular, evidencia
numérica) con ρ < T para todo δ < δ* = 0.0248, y la ventana de ω tiene
anchura 0.427. Fuera de la ventana (ω < 0.191) el programa de la
Batalla 2 sube por la rama H_m (2(1−ω)) y el mínimo queda > φ.

**Conjetura A2 (el umbral áureo).** La obliviousness de colocación vale
para toda instancia con ρ < φ, y la familia áurea la hace fallar en
todo ρ ∈ (φ, T) — con ρ > T ya fallaba (gemelas, n = 4): el umbral
geométrico es exactamente φ. (Formulación directa sobre obliviousness,
matiz del acta: «ningún intercambio se bloquea» es la noción interna de
la prueba y su equivalencia con obliviousness es el ensamblaje del lema
universal, aún abierto.) Evidencia: (i) el programa de paredes de la
Batalla 2 con un ocupante y S par tiene mínimo numérico = φ (bloque
[E], dif < 2·10⁻⁴; el punto fijo es el mismo mecanismo mín_A
máx(2b(A), (1+2b(A))/A) = φ); (ii) TODAS las cotas de la Batalla 1
(T_can ≥ 13/7, Ψ, Ψ_j, curva dorada φ² − (φ/2)ω ≥ 1.809, T3) están por
encima de φ con margen; (iii) el primer peldaño de la escalera era
ρ ≥ φ con solo el bolsillo — la protección mínima del disco es áurea.

**Qué queda en pie y qué cambia.**

- En pie: TODOS los teoremas del repo (S, esquina 13/7, ρ*_k, B/B″,
  G/G′, Ψ_j, T3…): son cotas de la Batalla 1 (u = agujero) y no
  afirmaban nada de la Batalla 2. También thm:additive (umbral aditivo
  1), las gemelas, n = 4.
- Cambia la INTERPRETACIÓN: T no es el umbral global; es el suelo del
  **intercambio anidado** (u = agujero de un aro). El programa de la
  Batalla 1 demuestra (en sus plantillas) que ese suelo es ≥ T y la
  familia rígida lo alcanza: T pasa de conjetura de umbral a
  **teorema-frontera del intercambio anidado**. El umbral global lo
  gobierna el intercambio a sartén, y es (conjeturalmente) φ.
- El paper: la Conjecture (Tribonacci threshold) debe reescribirse:
  teorema del contraejemplo áureo + conjetura del umbral áureo + T como
  umbral del intercambio anidado. La evidencia numérica antigua
  («ninguna instancia con ρ < 1.8 falla», 120 + 900 runs) no contradice:
  la familia vive en un rincón (tangencia diametral de la sartén ±
  δ < 0.025, s en una ventana de anchura ~0.1 sobre el bolsillo) que un
  muestreo aleatorio de radios no visita.

## Huecos declarados

1. La dirección ≥ de la Conjetura A2 (ρ < φ ⟹ nunca se bloquea) está
   abierta: exige rehacer el programa de paredes de la Batalla 2 en
   general (ocupantes múltiples, S ≥ 3, ocupación anidada, y = o no
   ancestro…) con suelo φ, y el ensamblaje del lema universal con el
   umbral corregido.
2. La robustez δ > 0 usa el criterio angular en la dirección de bloqueo
   (no S5): declarada como evidencia; el teorema vive en δ = 0, todo
   exacto.
3. El barrido del bloque [E] usa el programa de paredes relajado (como
   V2/B): el ínfimo real de los bloqueos de la Batalla 2 podría ser
   mayor que el del programa — pero la familia áurea REALIZA φ + 2ε, así
   que el ínfimo es exactamente φ en la plantilla del teorema.

## Mapa de verificación

`code/aureo.py`, cinco bloques: **[A]** identidades exactas en sympy
(b₂(φ,1) = φ/2; (1+φ)/φ = φ; el punto fijo en A = φ; ρ = φ + 2ε con la
cola de m dominante; φ < T; la ventana); **[B]** la instancia concreta
(ω = 0.3, ε = 10⁻³): las siete paredes exactas, la corona del testigo
con coordenadas y distancias verificadas, y el árbol EXHAUSTIVO de
colocaciones del voraz (máx 3 con m en la sartén, 4 con m en el
agujero); **[C]** la familia entera (ω ∈ {0.2, 0.3, 0.45, 0.6},
ε ∈ {10⁻², 10⁻⁴, 10⁻⁶}): bloqueo exacto + testigo válido + ρ = φ + 2ε;
**[D]** la ventana de holgura: δ* = 0.0248 (borde 2s_mín = T por
bisección de la frontera angular), contraejemplos sub-T en
δ ∈ {0.005, 0.01, 0.02}; **[E]** el mínimo del programa de la Batalla 2
= φ (dif < 2·10⁻⁴) dentro de la ventana y > φ fuera.
