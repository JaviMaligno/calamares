# Acta de revisión ciega — BLOQUE 2

**Objeto**: `paper/main.tex`, secciones «Sharpness: the n=4 transition and twin instances» (ll. 354–449) y «Thresholds: the Tribonacci floor and the golden counterexample» (ll. 450–685), con sus apéndices de soporte (App. de la prueba rígida, ll. 1359–1554; App. de verificación de twins, ll. 3775–3814) y el verifmap (ll. 1222–1357).

**Método**: rederivación independiente de toda la álgebra con sympy; recomputación de todas las cotas de confinamiento con aritmética racional exacta (`fractions.Fraction`); reconstrucción a mano de los árboles del voraz en las cuatro instancias (n=4, I1, I2, dorada); ejecución de `code/aureo.py` (5/5), `code/rigido.py` (7/7, V5 10/10), `code/gemelas.py`, `code/umbral.py`, `code/universal.py` (5/5). Scripts de la revisión: `refcheck_b2.py`, `refcheck_caps.py` (este directorio).

**Veredicto global**: **ACEPTAR CON CORRECCIONES**. El bloque es matemáticamente sólido: cada teorema enuncia lo que su prueba establece, las direcciones constructiva/exacta están separadas con honestidad, y toda la álgebra rederiva limpia. Hay UNA corrección obligatoria (el certificado explícito V3 de las gemelas, tal como está impreso, viola sus propias restricciones por redondeo en la dirección desfavorable), dos recomendadas (citas de infactibilidad del pan que el texto no cubre en el punto de uso, aunque las conclusiones son robustas) y varias menores.

---

## Veredicto por sección

### §Sharpness (ll. 354–449): SÓLIDA, con una corrección obligatoria en su apéndice de verificación

- **Prop. n≤3 (l. 356)**: correcta. El único punto de ramificación es r2; los cuatro casos F×P cierran; la inducción implícita (el conjunto del voraz = prefijo lex-max) y «rings outside the lex-max set are never admissible» son válidos (infactibilidad de conjunto ⇒ ningún contenedor admite). Verificado a mano caso por caso, incluyendo los casos degenerados (r1 no colocado, sin agujero por r1 ≤ w).
- **Lema cap (l. 378)**: verificado con racionales exactos, todas las desigualdades en la dirección segura: a ∈ [4.8,5]; c_X·u ≥ 9.5 y c_Y·u ≥ 9.0 (mínimos en a=5, monotonía comprobada); transversales ≤ 3.43 y = 4.8; |c_X−c_Y|² ≤ 67.978 ≤ 67.98 < 9.7² . Correcto.
- **Tma. n=4 (l. 395)**: rama best-fit íntegramente cubierta por las herramientas citadas (lema cap + condiciones exactas de dos círculos); lex-max = 4 con testigo exacto (15 = 15, 9.7 = 9.7). Rama worst-fit: cierto pero ver hallazgo 2.
- **Tma. gemelas (l. 413)**: correcto. V1, V2, V4 rederivados con racionales exactos (ver abajo); identidad del estado en el paso decisivo verificada (historia incluida: el prefijo 10→sartén es forzado e idéntico); el argumento aleatorizado max(p,1−p) ≥ 1/2 es correcto; los árboles de las cuatro ramas (best/worst × I1/I2) reconstruidos a mano quedan cubiertos por V1–V4 (con la salvedad del hallazgo 3). `gemelas.py` corrobora (best: 3/4 en I1, 4/4 en I2; worst al revés).
- **App. verif (l. 3775)**: V1 exacto (77.294 ≤ 77.30, 8.792 ≤ 8.80 < 9.49 ✓); V2 exacto para z ∈ {4.74, 4.76} (28.8576 → 5.372 < 9.76; 31.2676 → 5.592 < 9.74 ✓); V4 trivialmente exacto. **V3 impreso es infactible** — hallazgo 1.

### §Thresholds (ll. 450–685): SÓLIDA

- **Tma. aditivo (l. 453)**: correcto y completo. Rederivé todas las paredes: testigo (r1+r2 = R; r3+r4 = s+δ ≤ r1−ω ⇐ ω < r1/2−δ), best fit anida r2, r3 → sartén (r1+r3 ≤ R ⇐ δ < r1/4), r4 bloqueado en los tres contenedores por ω > r1/4 (y en el agujero de r3 a fortiori); orden estricto; ρ = 1+2δ/r1 ≤ 1+ε ⇐ δ < εr1/2; colas correctas. La dirección ρ ≤ 1 aplica el Tma. oblivious verbatim (el lema de fila es trivial en el modelo aditivo). «Verified instances reach ρ = 1.03 and 1.02»: reproducido (`umbral.py`: 1.0300, 1.0199/1.0200) — ver hallazgo 9.
- **Tma. suelo rígido (l. 485) + App. rigidproof (l. 1359)**: correcto en su totalidad. Rederivación sympy de: identidad del semiángulo sin²(θ/2) = f(a)f(b); identidad G(x) = f(1)/f(x)−f(1)² = (1+t)(t−x)/(t²x); √G = (√(1+t)/t)ψ; ψ(b(t)) = τ_t y t/(1+τ²) = b(t); U'' = 2t(3z²−1)/(1+z²)³ con concavidad sii τ_t ≤ 1/√3 ⟺ t ≤ (1+√13)/6 = 0.76759 (cubre 1/φ = 0.61803 con margen); 2b−1 = (t²+t−1)/(1+t+t²); t+b−1 = (t³+t²+t−1)/(1+t+t²); L' < 0; L(t*) = 1/t* = T módulo la cúbica; **la factorización de S5: (1+t)(1+t−q)² − (1+q)² − t(t+q)² + t(1+t) = 4(t²+t+1)(b(t)−q), exacta**, y la derivación de la compatibilidad de las dos cotas de cos γ que la precede. Lógica: solo se usa la dirección SUFICIENTE del criterio angular (contrapositiva de F3), declarado explícitamente (l. 1434) — honestidad ejemplar; el lema de clausura S6a es correcto (segmento inicial cerrado con máximo alcanzado); la familia aproximante cae genuinamente en F (ω > 0, órdenes estrictos, ρ₁ < 3t < 3t* < T, ρ₂ ≤ L(t)+ε_t/t → T). Pertenencia de n=4 y de I1 a F: verificada (también `rigido.py` V8). Script `rigido.py` 7/7 con V5 10/10, en línea con el verifmap.
- **Remark slack (l. 531)**: la dirección de la antitonía es correcta (empaqueta en radio menor ⇒ empaqueta en radio mayor; contrapositiva: F3 en R ⇒ F3 en r1+r2 ≤ R) y la familia aproximante tiene R = r1+r2, luego el ínfimo no cambia. Correcto; corroborado por `universal.py` bloque D (0 fallos).
- **Definición del umbral geométrico τ (l. 541)**: bien planteada (ínfimo; el enunciado deja explícito que puede o no alcanzarse). Sin gates infalsables.
- **Tma. dorado (l. 558)**: correcto y completo. Rederivación sympy de todas las identidades: f(φ) = φ en R = φ+1; 8φ+5 = (2+√5)²; φ³ = 2+√5; 1+4φ² = 8φ+5; el umbral del certificado σ* = 4φ³/(8φ+5) = 4(2+√5)(9−4√5) = 4(√5−2) = 0.94427 (racionalización con (9+4√5)(9−4√5) = 1); en ε = 0, 4φ(√5−φ) = 4; f(φ/2) = 1/√5; b₂(φ,1) = φ/2 (directo y vía S5 reescalado: φ·b(1/φ) = φ/2, con 1+t+t² = 2 en t = 1/φ); (1+φ)/φ = φ. La cadena del certificado de corona (2A+B < π ⟺ sinB < sin2A en el caso 2A > π/2, con el caso 2A ≤ π/2 inmediato) verificada, incluida la equivalencia f² < 4φf(1−φf) ⟺ f(1+4φ²) < 4φ. Ventana (1−φ/2, φ−1) = (0.19098, 0.61803) no vacía; los tres topes de ε* positivos en toda la ventana ((T−φ)/3 = 0.0738; ≥ 0.0955; 0.0676). Árbol del voraz reconstruido a mano: con 1 en sartén quedan 3 (bolsillo φ/2 exacto por S5 — sin circularidad: S5 se prueba independientemente en el apéndice rígido —, par rechazado en H_φ, s2 > 1−ω en H_m, no anidamiento por ω > ε), con 1 en agujero quedan 4 (corona certificada); coincide con `aureo.py` bloque B (exacto) y C (toda la ventana, ε → 0). ρ = φ+3ε con cola dominante s1+s2, verificado.
- **Cor. cobertura (l. 625)**: correcto. Dominancia de la cola: (1+ρ₀)/φ ≤ ρ₀ ⟺ ρ₀ ≥ φ ✓; s1 = φ/2+(ρ₀−φ)/2+η/2 < T/2+η/2 < 4(√5−2) para η < 0.0494; el resto de paredes exactas verificadas. Ver hallazgos 5 y 10.
- **Remark cuádruple dorado (l. 641)**: punto fijo 2b(A)A = 1+2b(A): la cúbica 2A³−A²−3A−1 = 2(A−φ)(A+1/φ)(A+1/2) tiene única raíz positiva φ ✓; anchura de ventana 3φ/2−2 = 0.42705 ✓; δ* = 0.0248 **etiquetado honestamente como numérico** ✓ (reproducido por `aureo.py` bloque D, que además se marca «evidencia»).
- **Conjetura dorada (l. 651)**: etiquetada como conjetura; el resumen de evidencia remite a resultados de secciones/apéndices fuera de este bloque (auditar allí); internamente consistente (T > φ ✓).

---

## Hallazgos numerados

**1. [OBLIGATORIA] El certificado explícito V3 de las gemelas, tal como está impreso, viola sus propias tangencias.**
Cita: ll. 3803–3810 («Explicit boundary configuration: … c_X = 10.24(cos 30.77°, sin 30.77°) … c_Y = 10.26(cos 32.02°, −sin 32.02°) … |c_A−c_X| = 14.76 and |c_A−c_Y| = 14.74 (exact tangencies, chosen via the boundary angles)») y l. 434 («angles 180°, 30.8°, −32.0°»).
Con los ángulos impresos: |c_A−c_X| = 14.75949 **< 14.76** y |c_A−c_Y| = 14.73969 **< 14.74** — ambas restricciones de disyunción falladas, error en la dirección **contraria** a la conclusión (el testigo impreso no es testigo). Los ángulos de tangencia exacta son 30.7535° y 32.0103°; los impresos (30.77°, 32.02°) no son redondeos de estos (30.7535 → 30.75, no 30.77). El empaquetamiento existe (con 30.75°/32.01° salen 14.76011 ≥ 14.76, 14.74001 ≥ 14.74, |c_X−c_Y| = 10.675 ≥ 9.50; solver y suma angular 352.5° < 360° lo corroboran).
Corrección: sustituir los ángulos por 30.75°/32.01° (o por los de tangencia con 4 decimales, presentando las distancias como desigualdades estrictas verificables), en el apéndice y en la l. 434.

**2. [RECOMENDADA] Tma. n=4: la rama worst-fit descansa en una infactibilidad del pan no cubierta por las citas del enunciado.**
Cita: ll. 399–401 («…blocks the 4.8 everywhere by Lemma cap and the exact two-circle conditions; worst fit places all four») y el pie de la Fig. (l. 407).
El recorrido real de worst fit (5 → sartén; 4.9 → agujero; 4.8 → agujero, el par exacto 9.7) exige saber que {10,5,z} NO empaqueta en R = 15 para z = 4.9, 4.8 — eso es la rigidez diametral + bolsillo b₂(10,5) = 30/7 ≈ 4.286 (Prop. S5 reescalada, probada solo en el apéndice rígido, posterior), no el lema cap ni condiciones de dos círculos. La conclusión «places all four» es robusta a ambas respuestas del oráculo (si el pan admitiera z, worst fit lo pondría ahí y los cuatro entran igualmente), pero la configuración dibujada y la frase del pie («the witness … realized by worst fit») requieren la infactibilidad.
Corrección: añadir una línea citando el bolsillo 30/7 (S5 reescalada) o anotar la robustez del recuento.

**3. [RECOMENDADA] Gemelas: el texto reclama «no third circle of radius ≥ 4.7 fits» pero el apéndice V2 solo verifica z ∈ {4.74, 4.76}.**
Cita: ll. 431–432 vs. ll. 3792–3800. El recorrido worst-fit de I1 consulta además z = 4.99 (cubierto por la afirmación ≥ 4.7 pero no instanciado en V2) y z = 4.50 (**no cubierto** por la afirmación, al ser < 4.7; benigno: el recuento es robusto como en el hallazgo 2, y de hecho 4.50 > 30/7 también está bloqueado). La verificación general es una línea: c_z·u ≥ 5z−15 y |c_z−c_B|² ≤ z²−130z+625, decreciente en z, que en z = 4.7 vale 36.09 < (5+z)² = 94.09.
Corrección: dar la cota general en z en V2 (la fórmula anterior) o restringir la afirmación a los radios realmente consultados anotando la robustez.

**4. [MENOR] Errata numérica en l. 432**: «|c_z−c_B| ≤ √(204.86−20·8.8) ≤ 5.37» — √28.86 = 5.3722 > 5.37. El apéndice dice correctamente 5.38 (l. 3800). Corregir 5.37 → 5.38.

**5. [MENOR] Errata numérica en Cor. cobertura, l. 633**: «= 0.9195…» — el valor es φ/2+(T−φ)/2 = T/2 = 0.91964…; debe decir 0.9196. (La conclusión 0.9196 < 0.9443 queda intacta.)

**6. [MENOR] Paréntesis confuso en ε*, ll. 565–568**: «the middle one is read as (φ−ω−φ/2)/2 when it is the binding constraint» — (φ−ω−φ/2)/2 es *idénticamente* (φ/2−ω)/2, luego el paréntesis no dice nada; además el tope central nunca es el vinculante en la ventana (≥ (φ/2−(φ−1))/2 = 0.0955 > (T−φ)/3 = 0.0738 ≥ min de los otros). Reescribir o eliminar.

**7. [MENOR] Tma. dorado, l. 618: «s2 cannot nest in s1» sin justificación.** Se sigue de ω > 1−φ/2 = 0.191 > (T−φ)/3 ≥ ε (anidar exigiría ω ≤ ε). Una media línea lo cierra.

**8. [MENOR] Discrepancia de nombre en el verifmap, l. 1231**: «Theorem rigidfloor — suelo_rigido, 10/10 claims (7 blocks)»; el fichero es `code/rigido.py` (el propio apéndice lo cita bien en l. 1366). Los recuentos 10/10 (V5) y 7/7 bloques sí coinciden con la ejecución. Unificar el nombre.

**9. [MENOR] Tma. aditivo, l. 476: «verified instances reach ρ = 1.03 and 1.02» sin puntero al script.** Es `code/umbral.py` (reproducido: 1.0300, 1.0199, 1.0200); ni el verifmap ni el texto lo citan. Añadir el puntero.

**10. [MENOR] Cor. cobertura: «for η small» sin cuantificar.** Los topes efectivos son η < 2(4(√5−2)−T/2) ≈ 0.0494, η < ω = 0.3 y η < ρ₀−φ. Opcional cuantificarlo.

**11. [MENOR] Prop. S5, l. 1494: «d = |X| > 0» se asume sin descartar d = 0.** Trivial (en d = 0, |X−c_1| = t < 1+q), pero la frase lo presenta como dato. Media línea.

---

## Verificado positivamente (resumen)

- **Aritmética exacta** (racionales): lema cap completo; V1 completo; V2 en z ∈ {4.5, 4.7, 4.74, 4.76, 4.99}; V4. Todas las tolerancias de redondeo del texto van en la dirección segura, salvo los hallazgos 1 y 4.
- **Sympy**: las 20+ identidades del bloque (semiángulo, G, ψ/τ/U/b, factorización S5, L(t*) = T, cúbica, y todo el paquete áureo incluida σ* = 4(√5−2) y el punto fijo). Cero discrepancias.
- **Lógica**: solo la dirección suficiente del criterio angular se usa en el suelo rígido (declarado); sin circularidad (S5 ← apéndice rígido, independiente del Tma. dorado que la usa; cap y V1–V4 autónomos); enunciados = lo probado en los seis teoremas del bloque; el único ítem numérico-no-probado (δ* = 0.0248) está etiquetado como tal; la conjetura está etiquetada como conjetura.
- **Scripts** (verifmap contrastado): `aureo.py` 5/5, `rigido.py` 7/7 (V5 10/10), `universal.py` 5/5, `gemelas.py` y `umbral.py` reproducen las afirmaciones citadas. Los bloques heurísticos de los scripts (solver estocástico, criterio angular como proxy) no sostienen ninguna afirmación del paper: la carga probatoria está en las pruebas manuales, verificadas aquí.
- **Robustez de los recuentos del voraz**: en las cuatro instancias del bloque los recuentos reclamados (3 vs 4) son invariantes frente a las dos únicas consultas de oráculo no cubiertas por las citas (hallazgos 2–3), comprobado rama a rama.
