# Revisión independiente del umbral exacto para cuatro aros

Modelo: `claude-fable-5-1`. Revisión externa estática mediante Claude Code: no ejecutó Python ni Lean. Alcance y hashes en el manifiesto y metadata `2026-09-14-fable-four-ring`. El dictamen se conserva íntegro.

---

Veredicto: **ACEPTAR**. No encuentro contraejemplo a la reducción ni error matemático en `thm:fourfloor` (líneas 740-815) ni en sus dependencias necesarias. Solo señalo precisiones de redacción no bloqueantes. Revisión estática: no he compilado ni ejecutado nada, y no afirmo nada sobre lo que Lean formaliza.

## Cadena verificada

- **Primer desacuerdo (747-753).** En el primer índice donde greedy y lex-max difieren, el greedy solo puede omitir un aro de L (si admitiera uno, el prefijo más el aro sería factible y L también lo incluiría). La restricción de la ejecución al subinventario "admitidos + omitido" es una ejecución greedy legal: los aros omitidos no dejan huella en F, los contenedores y ocupantes coinciden, y el lex-max del subinventario es todo él. Con ≤3 aros contradice `prop:n3`, cuya prueba (428-448) revisé y es correcta. Luego hay 3 admitidos y el rechazado es el cuarto.
- **Intercambio en p (757-767).** Con acuerdo en el padre de 1, los ocupantes mayores que p del destino u coinciden en F y P; el único aro menor es q, que cabe en la bola vacante de p o viaja con p si es su hijo. Anidamiento: q < p ≤ r_dueño(v) − w. El testigo resultante coincide con F en {A,1,p} y F admite q. Correcto, y no necesita superincrecimiento.
- **Intercambio en 1 (769-775).** S son los hijos inmediatos de dueño(u) entre {p,q}. Los casos q anidado en p, p o q anidados en 1, o p o q en v quedan cubiertos por |S| ≤ 1 (subárbol de un miembro cabe en la bola unidad vacante; el subárbol de 1 viaja con 1). S = {p,q} son hojas y con p+q ≤ 1 basta el lema de fila. Así, S = {p,q} y p+q > 1 es la única supervivencia.
- **Caso (a), 1 anidado en A (777-784).** R ≥ A+1 y p+q ≤ A−w salen del testigo; {A,p,q} no empaqueta en la bandeja porque, si lo hiciera, anidar 1 en A (certificado por F) daría un testigo con el padre prohibido. Escalando por 1/A: t = 1/A, ω = w/A, (F2) es p/A+q/A ≤ 1−ω, (F3) en radio R/A ≥ 1+t pasa a radio 1+t por antitonía (`rem:slack`). ρ es invariante de escala. Revisé `lem:S1`-`S4` y la prueba del suelo estricto (1659-1770): derivadas de U, concavidad hasta t ≤ 0.7676, ψ(b(t)) = τ_t, t/(1+τ_t²) = b(t), L'(t) < 0 y L(t*) = T. Todo cuadra: ρ > T > φ.
- **Caso (b), 1 en la raíz (786-812).** p en el agujero de A es forzado (si no, el agujero vacío admite q < 1 ≤ A−w). Solo se usa la dirección de suficiencia de `prop:S5` (bolsillo por Descartes, comprobado: curvaturas 1, 1/t, −1/(1+t) tienen suma de productos nula y dan b(t)); g(A) = A·b(1/A) es correcto. El empaquetado en radio A+1 se traslada a R ≥ A+1, luego q > g(A) estricto.
- **Identidades (803-809).** Ambas expandidas a mano con φ² = φ+1: D(2g−φ) = (2−φ)A² + (2−φ)A − φ = (A−φ)((2−φ)A+1); D(1+2g−φA) = −φA³ + (3−φ)A² + (3−φ)A + 1 = (φ−A)(φA² + (2φ−2)A + φ−1). Signos: (2−φ)A+1 > 0 y el cuadrático tiene coeficientes positivos, así que cubren A ≥ φ y 1 < A ≤ φ. Ambas se anulan en A = φ, coherente con la familia áurea (g(φ) = φ/2).
- **Cota superior (813-814).** Revisé `thm:golden` (665-712): valor de ρ, testigo por corona (el certificado reduce a s_1 < 4√5−8 vía 8φ+5 = (2+√5)² y φ³ = 2+√5), y la ejecución worst fit, que sí necesita la necesidad exacta de `prop:S5`, cuya factorización 4(t²+t+1)(b(t)−q) comprobé expandiendo. La familia es de 4 aros en disco con ρ = φ+3ε ↓ φ. Con la cota estricta, τ_4 = φ y no se alcanza.

## Por qué no falta un caso de bosque

El bosque de cuatro aros tiene padre(A) = raíz, padre(1) ∈ {raíz, A}, padre(p) ∈ {raíz, A, 1}, padre(q) ∈ {raíz, A, 1, p}. El paso 757-767 elimina todo P con padre_P(1) = padre_F(1), sea cual sea el resto. El paso 769-775 elimina, para padre_P(1) ≠ padre_F(1), todo P salvo aquel en que p y q son hijos inmediatos de dueño(u) con p+q > 1; eso fija P por completo en cada uno de los dos valores de padre_F(1). En el caso (a) la posición de p en F es irrelevante; en el caso (b) las tres posiciones de p en F se reducen a una. La enumeración es exhaustiva.

## Precisiones no bloqueantes

- **Línea 751.** Añadir que un aro omitido no altera F, por lo que la ejecución restringida es legal y el lex-max del subinventario es todo él.
- **Línea 773.** Decir explícitamente que 1 viaja con su propio subárbol al moverse a u (en P puede contener p o q).
- **Línea 780.** "feasible" debería leerse "empaqueta como hijos de la raíz en la bandeja", y citar que 1 ≤ A−w está certificado por F.
- **Línea 782.** Explicitar el escalado: t = 1/A, ω = w/A, bandeja R/A ≥ 1+t, ρ invariante.
- **Línea 795.** Indicar que solo se usa la dirección de suficiencia de `prop:S5`, sin rigidez.

Límites: no he auditado `thm:oblivious` más allá del paso de intercambio que aquí se reutiliza, ni la corona de `cor:goldencover`, que no es dependencia del teorema.
