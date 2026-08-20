# ACTA META — Ronda de revisión ciega por bloques (consistencia transversal)

**Paper:** `paper/main.tex` (repo `calamares`). **Fecha:** 2026-08-20.
**Insumos:** actas de los 7 referees de bloque (`acta_bloque1.md` … `acta_bloque7.md`),
todas leídas íntegras; comprobaciones transversales propias sobre `main.tex`, `code/` y
`lean/` (greps de referencias, colisiones de símbolos, recuentos disputados re-verificados
de primera mano). `docs/` no consultado (prohibido).

---

## VEREDICTO GLOBAL DEL PAPER

**PUBLICABLE TRAS CORRECCIONES. Ningún hallazgo FATAL, ni por bloque ni transversal.**

Los siete bloques recibieron veredicto CONFIRMADO/ACEPTAR CON CORRECCIONES, cada uno con
re-derivación independiente sustancial (sympy, aritmética racional exacta, walkthroughs
manuales, ejecuciones de scripts). Los dos únicos hallazgos con contenido matemático real
son reparables con material ya presente en el paper y ambos vienen con la reparación
verificada por el propio referee que los encontró:

- **B4-F1** (hueco de caso en la prueba de thm:DP(iv), j=3): el enunciado del teorema no
  cambia; la reparación usa solo paredes ya probadas y fue verificada por el referee 4.
- **B1-H1** (clausura hacia abajo de la factibilidad afirmada sin prueba): lema de una
  línea (los hijos del anillo retirado no se mueven; re-parentar preserva el anidamiento).

Todo lo demás obligatorio es de testigos impresos, recuentos, etiquetado y redacción.

---

## 1. CIRCULARIDAD INTER-SECCIONES — LIMPIA

Barrido propio de `\ref{}` sobre `main.tex`, contrastado con las DAGs reportadas por los
referees 3, 4, 6 y 7:

- **Orden de apéndices:** verifmap (1222) → rigidproof (1359) → widthproofs (1556) →
  genericproofs (2139) → campaign (3034) → verif-twins (3775). Cada apéndice importa solo
  de apéndices anteriores: widthproofs importa S1/S2/S5/S6a de rigidproof; genericproofs
  importa Cmin/Cwitness/corner de widthproofs y S5 de rigidproof; campaign consume
  genericproofs. **Ninguna prueba de un apéndice referencia un resultado de un apéndice
  posterior** (verificado por grep de todas las etiquetas D*, S*, C* con corte de línea).
- Las referencias «hacia delante» (cuerpo → apéndices) viven todas en secciones
  expositivas: intro (149), resumen de evidencia de conj:golden (665–683), phase diagram
  (987), open problems (1150–1168), verifmap (1331). Ninguna dentro de una prueba.
- Cadena del bloque 1 (row → lexdom → selection → oblivious) estrictamente hacia atrás
  (referee 1). Cadena de supersesión de la campaña acíclica (referee 7).
- Únicas dependencias no citadas en el punto de uso (no circulares, sí de higiene):
  la rama worst-fit de thm:n4 usa el bolsillo 30/7 = S5 reescalada, probada después
  (B2-#2), y prop:n3 usa la clausura hacia abajo (B1-H1).

**Conclusión: sin circularidad en el paper.**

## 2. NOTACIÓN Y CONSTANTES ENTRE BLOQUES

- **ω₁ (B3-O1):** verificado por grep completo que la colisión es *local* — el único uso
  de ω₁=(√5−2)/2 es la l. 1692 (prueba de Ctrio); todos los demás (781–783, 805,
  2015–2135) son la raíz 0.0413570 de 4ω³−20ω²+25ω−1. No se propaga a otros bloques.
  La corrección de B3 (renombrar el local) basta.
- **Ψ vs Ψ₁ [hallazgo meta, MENOR]:** el paper usa Ψ₁ en ll. 671, 1148, 2824 y Ψ (mismo
  objeto: Ψ_j con j=1, raíz de u²−2(1−ω)u−1) en ll. 881, 2409, 3002. Los valores citados
  son consistentes (Ψ₁(1/2)=Ψ(1/2)=φ), pero el doble nombre es exactamente el patrón que
  produjo la colisión ω₁. Declarar Ψ₁≡Ψ una vez o unificar.
- **Primera copia [transversal, eleva B4-F11]:** el convenio se introduce entre paréntesis
  dentro de la prueba de DV2 (l. 2352) y hace trabajo portante en 2604 (DGp), 2860 (pinza
  de DP) **y 3573 (bloque 7: la vacuidad del empate del gemelo del canal ocupante)**. Su
  uso cruza la frontera de bloques 4→7: debe promoverse al preámbulo del apéndice de
  contenedores genéricos (o al modelo), como pedía B4-F11, ahora con rango RECOMENDADA.
- **Reuso local de g/G y T-subíndice [meta, MENOR]:** g(s)=2arcsin(e^{s/2}) (zigzag,
  2255), g(A) del certificado de DP(i) (2789+) y g(σ) de Ckappa (1846) son definiciones
  locales sin conflicto portante, dos de ellas en el mismo apéndice; T_c (primitiva, lem:DU)
  vs T_{1+ω} (raíz Tribonacci deformada, widthproofs) comparten patrón tipográfico con
  roles distintos. Tras el precedente ω₁, conviene una pasada de higiene de símbolos
  locales (basta «where locally g denotes…»).
- **Constantes contrastadas entre secciones:** los pares intro↔apéndice coinciden en todos
  los casos comprobados: 0.9626 ↔ ω_A=0.962585 (redondeo correcto), 0.624 ↔ 0.6240,
  0.896 ↔ 0.8959, ω_T=0.0436890 (bloques 1 y 3), (T−1)²/2=0.3522 y (T−1)²=0.7044
  (bloques 4 y 5), 13/7, 15/26, T/2=0.9196 (con la errata puntual B2-#5: «0.9195»).
  b(·), b₂(·,·) y f(·) se usan con una única definición coherente en todos los bloques
  (verificado: b(φ)=φ/2 cierra el punto fijo en las tres apariciones).
- **Convenciones divergentes:** no se encontraron. La convención de reordenación libre de
  hermanos (192–193) es la que usa thm:oblivious (B1); la de capacidad r−ω es uniforme;
  la de polvo por pieza <r_m del canal está declarada y confinada (B7).

## 3. VERIFMAP vs SCRIPTS vs TEXTO — BARRIDO COMPLETO DE DISCREPANCIAS

Re-verificado de primera mano por el meta-referee (grep/ls, no delegado):

| # | Dónde | Discrepancia | Realidad verificada |
|---|-------|--------------|---------------------|
| V1 | verifmap 1231 | «suelo_rigido» no existe como script | `code/rigido.py` (recuentos 10/10, 7 bloques sí cuadran — B2, B5, B6) |
| V2 | verifmap 1236 | «perfil_tres», «cuatro» son drafts | `code/tresk.py`, `code/cuatrok.py` (el mapa solo da cuatrok entre paréntesis) |
| V3 | verifmap 1288 | espfinal «(5/5)» | El runner ejecuta `list("ABCDFE")` = **6 bloques** (espfinal.py:622) |
| V4 | verifmap 1322 | «forty-two theorems» Lean | **45** `theorem` en `lean/Calamares/Identities.lean` (grep propio) |
| V5 | texto 476 + verifmap | ρ=1.03/1.02 de thm:additive sin script citado | Es `code/umbral.py` (existe, reproduce 1.0300/1.0200 — B2); además thm:additive ∈ sec:threshold, que el preámbulo del mapa declara cubierto, y no tiene entrada |
| V6 | texto 293, 348–351 | §§3–4 sin script nombrado | `code/superinc.py`, `code/test_oblivious.py` existen y reproducen (B1); fuera del alcance declarado del mapa pero el texto debería citarlos |
| V7 | apéndice width | esquina/grosor no citados en el apéndice | Existen, `esquina.py` 5/5 ejecutado (B3, B5); el verifmap sí los lista (1235) |
| V8 | texto 3701 | El párrafo del converso no cita `f3converso` | El script existe, 5/5 (B7); solo aparece en el verifmap (1303) |
| V9 | texto 3112–3114 | 185k instancias / 4.284 esquinas / re-validación euclidiana 1500/1500 | **No trazables**: `coronacolas.py` no computa ni imprime ninguno de los tres números (grep vacío — B7-H2) |
| V10 | texto 3449, 3420, 3607, 3633 | ∼45k familias, 55k adversariales, 20.000 fuzz, 1.460 tests | Cifras de rondas adversariales (docs/), no reproducibles desde los scripts: `colageometrica.py` da 22.976 familias por defecto; «55k» no está en `coronaagujero.py` (B7-H6) |
| V11 | texto 3066–3068 | «200.000 sampled, zero unassigned» como evidencia en la prueba de DSpan | El gate de coronacolas bloque C es un complemento booleano tautológico: no puede fallar (B7-H1) |
| V12 | texto 3697 | 1.266 gaps certificados sin umbral | `f3converso.py` usa TOL_GAP=2e-6 y declara la banda (1e-9, 2e-6] no barrida; el paper no lo menciona (B7-H10) |
| V13 | verifmap global | «5/5 all green» sin distinguir bloques-declaración | universal.py E y espfinal.py A son declaraciones sin gate (B5-H7) |

Todo lo demás cuadra: el referee 5 contrastó recuentos estáticos de bloques en 28 scripts
(única discrepancia espfinal = V3), ejecutó 4 en vivo, y el referee 7 verificó
correspondencia verifmap↔cabeceras en la campaña, incluida la realidad de las reparaciones
adversariales relatadas (cap 2ε₀ en espfinal.py, gate A3b de f3converso sustituido, control
A4/A6 de insercion). Los ~30 scripts citados existen todos en `code/`.

## 4. CONVERGENCIAS Y CONTRADICCIONES ENTRE ACTAS

**Confirmaciones cruzadas (referees independientes, mismo hallazgo):**
1. **V3 de las gemelas infeasible** — B2-#1 y B6-T1: mismos déficits (5.1·10⁻⁴ y
   3.1·10⁻⁴), mismos ángulos de tangencia exacta (30.7535°/32.0103°), misma dirección
   insegura del redondeo. La confirmación más fuerte de la ronda. Reparaciones
   compatibles; la de B6 (testigo racional con |c_A−c_X|²=217.8576=14.76² exacto) es
   la preferible.
2. **Errata 5.37→5.38** (l. 432) — B2-#4 y B6-T2, idéntica.
3. **«≥4.7» excede lo probado en V2** — B2-#3 y B6-T3; ambos derivaron
   independientemente la misma cota general (z²−130z+625 < (5+z)² ⟺ z>30/7).
4. **d=0 no descartado en S5** (1494) — B2-#11 y B6-R1, idéntica.
5. **DSpan** — B5-H6 (exhaustividad por muestreo, «complete proof» sobredeclarada) y
   B7-H1 (ese muestreo es además un gate tautológico): B7 refuerza a B5; la corrección
   única (enumeración lógica de la tricotomía) resuelve ambos y hace verdadera la
   etiqueta de op:assembly.
6. **Drafts en el verifmap** — B2-#8 (suelo_rigido) y B5-H4 (los tres nombres), mismo
   defecto.
7. **Punteros de script ausentes** — B1-H4, B2-#9, B3-R3, B7-H7: patrón sistémico
   (cuatro bloques distintos), consolidado en un solo ítem.
8. **Gates tautológicos en scripts** — B4 (batalla2.py: `max(Ψ₃,Ψ_B)>φ` independiente
   de la instancia, justo en la rama del hueco F1) y B7-H1 (coronacolas C): dos
   instancias del mismo patrón; el proyecto ya había cazado un tercero (espcanalp,
   registrado en el verifmap).
9. **Primera copia** — B4-F11 y el uso en el bloque 7 (l. 3573, detectado por el meta):
   transversal real.

**Contradicciones entre actas: NINGUNA.** Tres tensiones aparentes, resueltas:
- B2 valida prop:n3 mientras B1-H1 señala sin prueba la clausura hacia abajo que usa:
  complementarios (el hecho es verdadero; falta el lema, no la conclusión).
- B5 valida el recuento estático de coronacolas (5 bloques) mientras B7 caza el gate del
  bloque C: compatibles (recuento correcto, calidad del gate deficiente).
- B6 clasifica MENOR el mismo hallazgo que B2 clasifica RECOMENDADA (≥4.7): se adopta la
  severidad mayor.
- Nada verificado-en-positivo por un acta queda refutado por otra: los positivos de B5
  sobre op:assembly (recuento de celdas) son a nivel de enunciados y no chocan con
  B4-F7 (descripción obsoleta de la ruta U₄) ni con B5-H2 (la frase «exactly»).

## 5. LISTA CONSOLIDADA PRIORIZADA (deduplicada)

Recuento: **0 FATALES · 11 OBLIGATORIAS · 17 RECOMENDADAS · 33 MENORES = 61 ítems.**
Marca ⟳ = requiere (re-)ejecutar algo; sin marca = puramente editorial.

### FATALES
Ninguno.

### OBLIGATORIAS

| # | Origen | Línea(s) | Corrección |
|---|--------|----------|------------|
| O1 | B2-#1 ≡ B6-T1 | 3802–3810, 434 | Testigo V3 de las gemelas infeasible tal como está impreso: sustituir por el testigo racional exacto c_A=(−5,0), c_X=(8.8,√27.4176), c_Y=(8.7,−√29.5776) (14.76²/14.74² exactos) o ángulos redondeados hacia abajo (30.75°/32.01°) |
| O2 | B4-F1 | 2827–2844 | thm:DP(iv) j=3: añadir el caso «y hoja dentro del subárbol de o₁» con la reparación verificada de B4 ((b′) dos hijos-nodo → Ψ₃; (c′) cadena: pinza textual si v*≠y; si v*=y, contradicción y>3 vs y<φ+ω<φ²). ⟳ opcional: gate falsable en batalla2.py |
| O3 | B1-H1 | 207, 271, 344 | Clausura hacia abajo: lema de una línea (los hijos del anillo retirado no se mueven y se re-parentan; r_child ≤ r_m−ω < r_p−ω), enunciado en §2 |
| O4 | B3-O1 | 1692 vs 783/2020 | Colisión ω₁: renombrar el local de Ctrio (p.ej. ω_φ). Meta-verificado: no hay más usos conflictivos en el paper |
| O5 | B3-O2 | 1715 | prop:Callk dirección (≤): polvo superdecreciente δ, δ², …, δ^{k−3} en vez de k−3 anillos iguales |
| O6 | B3-O3 | 2129 | rem:Cbump: definir c₀ y r′ o sustituir por el enunciado numérico certificado |
| O7 | B5-H1 | 999–1000 | Divergencia: «fit k times in the pan but at most k−2 times in the hole» (con k−1 hay empate; 0 celdas divergentes con n_pan=n_hole+1 en la retícula) |
| O8 | B5-H2 | 1186–1191, 673, 682–683 | op:assembly «is exactly»: remitir al inventario de cinco partidas del honest residue (los topes de barrido y la banda media del canal no caben en la enumeración actual); alinear la cláusula final de conj:golden |
| O9 | B5-H3 (meta-re-verificado) | 1288, 1322 | Verifmap: espfinal 5/5 → **6/6** (runner ABCDFE); Lean «forty-two» → **forty-five** |
| O10 | B7-H1 + B5-H6 | 3066–3068, 1155 | Prueba de cor:DSpan: sustituir «200.000 sampled, zero unassigned» (gate tautológico, no puede fallar) por la enumeración lógica de la tricotomía sobre (|S⁺|, j, σ₁+M); con ello «a complete proof» en op:assembly queda sin asterisco. ⟳ opcional: gate falsable en coronacolas C |
| O11 | B7-H2 | 3112–3114 | Recuentos no trazables del cierre de la celda pesada (185k / 4.284 esquinas / 1500/1500): citarlos como cifras de informe, hacer que coronacolas los imprima ⟳, o dejar solo «j≤5, p≤6 swept» (la celda está superada por thm:D1written) |

### RECOMENDADAS

| # | Origen | Línea(s) | Corrección |
|---|--------|----------|------------|
| R1 | B2-#3 ≡ B6-T3 | 430–432, 3792–3800 | «no third circle ≥4.7»: añadir la cota general de una línea (z²−130z+625<(5+z)² ⟺ z>30/7) o restringir a los z consultados |
| R2 | B2-#2 | 399–401, 407 | thm:n4 worst-fit: citar el bolsillo 30/7 (S5 reescalada) o anotar la robustez del recuento |
| R3 | B6-T4 | thm:twins | Tabla de las cuatro ejecuciones greedy (todo forzado tras el paso decisivo) |
| R4 | B3-R1 | 777–778, 1925–1953 | Igualdad en la rama del testigo: remitir Cwitness/Ccurve al argumento de genuinidad de la esquina (vale verbatim en α=T_{1+ω}) |
| R5 | B3-R2 | 2050 | Monotonía de Ξ: media línea con la reducción polinómica (sin raíces en (1,2)) |
| R6 | B4-F2 | 2666–2669, 941–961 | Subir S⊂(ω,1) al enunciado de DT3 y a la sección, o remitir σ₃≤ω a app:campaign |
| R7 | B4-F3 | 2553–2565 | Etiquetar como asistidos por ordenador (o certificar por Sturm) los c₁₀≥0, c₂₀≥0, c₂₁≥0 de DGp |
| R8 | B4-F4 | 2686–2688 | DT3: reformular sobre ρ la cota atribuida a thm:corner |
| R9 | B4-F5 | 2553, 2559 | Constantes o* (raíz real 1.59557, no 1.5958) y õ (1.295564, no 1.29558…): corregir o definir como «la raíz de …» |
| R10 | B5-H4 ≡ B2-#8 | 1231, 1236 | Verifmap: nombres de fichero reales — rigido.py, tresk.py, cuatrok.py (drafts entre paréntesis). Meta-verificado: los nombres impresos no existen en code/ |
| R11 | B5-H5 | 1090–1091 | Precisar oráculo y conteo (O(n²) consultas de hermanos o n llamadas al oráculo fuerte) y citar thm:oblivious, no thm:selection |
| R12 | B1-H4 + B2-#9 + B3-R3 + B7-H7 | 293, 348–351, 476, apéndice width, 3701 | Punteros de script: superinc/test_oblivious (§§3–4, + declarar el oráculo heurístico como tope), umbral (thm:additive — añadir además su entrada al verifmap, cuyo alcance declarado lo cubre), esquina/grosor (apéndice width), f3converso (párrafo del converso) |
| R13 | B7-H3 | 3110–3112 | «deficit 0.0»: declarar la tolerancia real (2·10⁻³ de la bisección de R_lb + sonda de decrecimiento en R) |
| R14 | B7-H4 | 3188, 3224, 3269, 3648 | Definir «certified maximization» una vez (estándar thm:DPr vs B&B por cajas); en 3648 «evaluated over a deterministic corner mesh» |
| R15 | B7-H5 | 3572 | «light channel closed entirely on v and on the depth-one tower cut» |
| R16 | B7-H6 | 3449, 3420, 3607, 3633 | Distinguir tipográficamente recuentos de script (reproducibles) de recuentos de ronda adversarial (informes), o hacer que los scripts los reproduzcan ⟳ |
| R17 | B4-F11 + meta | 2352 → 2604, 2860, 3573 | Promover el convenio de primera copia al preámbulo del apéndice genérico: portante también en el bloque 7 (vacuidad del gemelo) — transversal 4→7 |

### MENORES

| # | Origen | Línea(s) | Qué |
|---|--------|----------|-----|
| M1 | B1-H2 | 304 | «weakly … suffices» necesita la versión no estricta de lexdom (un paréntesis) |
| M2 | B1-H3 | 234 | «strictly increasing» en lem:superadd |
| M3 | B1-H5 | 349–351 | «identical, optimal»: identidad por unicidad (Lemma 3.2), no por el experimento |
| M4 | B1-H6 | 292–295 | «every descending greedy»: anotar que ningún paso ofrece elección |
| M5 | B1-H7 | 105–107 | «determine exactly» → exacto en el modelo aditivo, bracketing en el geométrico |
| M6 | B1-H8 | 307–309 | Definir «capacity» de best/worst fit fuera del caso disco |
| M7 | B2-#4 ≡ B6-T2 | 432 | 5.37 → 5.38 (√28.86=5.3722) |
| M8 | B2-#5 | 633 | 0.9195 → 0.9196 (=T/2) |
| M9 | B2-#6 | 565–568 | Paréntesis de ε* tautológico; el tope central nunca es vinculante |
| M10 | B2-#7 | 618 | «s2 cannot nest in s1»: media línea (ω>1−φ/2>ε) |
| M11 | B2-#10 | Cor. cobertura | Cuantificar «for η small» (η<0.0494) |
| M12 | B2-#11 ≡ B6-R1 | 1494 | Descartar d=0 en S5 (media línea) |
| M13 | B6-R2 | 1514–1518 | «if nonempty» para p_max/δ₀ en S6a(3) |
| M14 | B3-M1 | 1770–1775 | Comegac: «ρ arbitrarily close to 2/(1+2ω)» |
| M15 | B3-M2 | esquina | ε=δ²/4 → «shrinking ε if needed» frente a δ₀ de S6a(3) |
| M16 | B3-M3 | Ccurve | Explicar el tope ω≤0.30 |
| M17 | B3-M4 | 2124–2137 | «exact coincidence» es la sustitución α=2−ω₁; reformular |
| M18 | B4-F6 | 2563–2564 | Errata: f₂(A_max)−curva = c₂₀+ωc₂₁ |
| M19 | B4-F7 | 1150 | op:assembly(a): descripción obsoleta de la ruta U₄ de DP j=3; actualizar a (Ry)/hojas/pinza |
| M20 | B4-F8 | 2199–2208 | Dgaps: enunciar la admisibilidad a_i+a_j≤R |
| M21 | B4-F9 | 829–831 | «pins the failure region exactly» → contraejemplo puntual (o remitir al script) |
| M22 | B4-F10 | 2955–2963 | DPp(vi): cláusula para el caso mixto |
| M23 | B4-F12 | 2276, 2834, 2838 | «Lemma U₄» siendo Theorem; «jj=3» jerga de script |
| M24 | B5-H7 | verifmap | Nota: algunos bloques son declaraciones/exploraciones sin gate |
| M25 | B5-H8 | 1061 | Hipótesis ociosa K>Σb_i |
| M26 | B5-H9 | 1000 | «A minimal instance (four rings; three never diverge)» |
| M27 | B5-H10 | 1194–1198 | op:oracle: «for arbitrary (non-superincreasing) radii» |
| M28 | B5-H11 | Generalizations (e) | El testigo es solo v≡1; matizar |
| M29 | B7-H8 | 3384, 3097/3539 | Gramática «use of the configuration»; remitir el duplicado de p(φ,1;φ+1) |
| M30 | B7-H9 | 3311–3314 | «whose algebraic core is kernel-checked in Lean» |
| M31 | B7-H10 | 3697 | Citar TOL_GAP=2·10⁻⁶ junto al recuento de gaps (V12) |
| M32 | meta | 671, 1148, 2824 vs 881, 2409, 3002 | Notación dual Ψ₁/Ψ: declarar Ψ₁≡Ψ o unificar |
| M33 | meta | 2255, 2789, 1846; T_c vs T_{1+ω} | Higiene de símbolos locales reutilizados (g/G, T-subíndice): una aclaración de ámbito local donde toque |

### Qué requiere ejecución vs editorial

- **Puramente editoriales:** todas salvo las marcadas ⟳. Incluye O1 (los dos referees ya
  verificaron el testigo de reemplazo en aritmética exacta), O3–O9, y todas las
  R/M salvo R16.
- **⟳ Con ejecución (todas opcionales u orientadas a scripts, ninguna bloquea el paper):**
  O2 (gate falsable nuevo en batalla2.py y re-run), O10 (gate falsable en coronacolas C),
  O11 y R16 (solo si se opta por hacer los scripts imprimir los contadores de ronda;
  la alternativa editorial — recortar/etiquetar las cifras — no ejecuta nada).

---

## Nota final del meta-referee

La ronda muestra un patrón sistémico y benigno: los defectos de mayor frecuencia son
(a) testigos/constantes impresos con redondeo en la dirección insegura (O1, R9, M7, M8 —
siempre con el enunciado verdadero detrás), (b) punteros y recuentos del aparato de
verificación desincronizados con el código real (O9, O11, R10, R12, R16, V5–V13), y
(c) gates de script que no pueden fallar (O2-bis en batalla2, O10 en coronacolas —
tercer y cuarto ejemplares de un patrón que el propio proyecto ya había cazado en
espcanalp). Nada de ello toca un enunciado: los siete referees re-derivaron
independientemente la matemática sustantiva de sus bloques y la encontraron correcta,
con los dos únicos huecos de prueba reales (O2, O3) reparados dentro de la propia ronda.
La honestidad de etiquetado (residuo, model-conditional, conjeturas, sketchs) fue
verificada punto a punto por los referees 5 y 7 y sale reforzada, con la única
sobredeclaración real en la frase «is exactly» de op:assembly (O8).
