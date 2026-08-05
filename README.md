# El problema de los calamares — Nested Ring Packing

Investigación sobre el empaquetamiento de aros (anillos de grosor w) con anidamiento recursivo en una sartén circular: teoremas de superincrecencia, irrelevancia de colocación, instancias gemelas y umbrales: aditivo = 1; el geométrico REFUTA la conjetura de Tribonacci — el contraejemplo áureo falla en ρ = φ+3ε < T y el umbral conjeturado es la razón áurea φ, con T como suelo exacto de la familia rígida anidada. Variante circular y de selección del Recursive Circle Packing Problem.

## Estructura

- `paper/main.tex` — el artículo (inglés; compilar con `pdflatex main.tex` dos veces). Antes de subir a arXiv: congelar fecha y commit, repo público.
- `docs/resultados.md` — documento de trabajo completo en español: modelo, lemas y teoremas con demostraciones, contraejemplos, veredictos de novedad y estrategia de publicación.
- `docs/generalizaciones.md` — todas las generalizaciones anotadas, con estado y primeras preguntas.
- `docs/reinsercion.md` — lema de reinserción: la parte combinatoria del umbral de Tribonacci, cerrada con cota exacta, y la parte geométrica aislada (mínimo en la razón áurea).
- `figures/` — divergencia área/número, diagrama de fases, contraejemplo n = 4.
- `lean/` — formalización en Lean 4 (core, sin mathlib) de la capa de certificados exactos: 22 teoremas sobre ℚ y ℚ[√5] (aritmética áurea del contraejemplo, certificados de los medios metálicos, suelo Tribonacci con encajonamiento y monotonía, esquina 13/7, umbral aditivo). Cero `sorry`, cero axiomas nuevos, sin `native_decide`. Comando: `cd lean && lake build`. La geometría de empaquetamiento NO está formalizada — véase `lean/README.md`.
- `code/` — scripts de verificación reproducibles (Python; dependencias: numpy, scipy, sympy, matplotlib — véase `code/requirements.txt`). Comando único: `python code/run_all.py` (~27 min; `--quick` omite `cuadrado.py` y `perfilp.py`, ~8 min); código de salida 0 sólo si todo está en verde.

## Mapa de verificación (qué script respalda cada afirmación)

- `sim.py` — solver de factibilidad (relajación física) + enumerador exacto; instancia de divergencia {9.0, 4.2, 4.2, 4.2}.
- `viz.py`, `franja.py` — figuras de divergencia y diagrama de fases (umbrales exactos de n círculos iguales).
- `voraz.py` — contraejemplos al voraz general en ambas métricas; tasa de fallo ~1 %.
- `superinc.py` — teorema de superincrecencia: 120 instancias sin fallo de área; contraejemplo de número bajo superincrecencia {9.95, 5.0, 4.3, 0.6}.
- `test_oblivious.py` — irrelevancia de colocación: best/worst/aleatoria idénticas en 100 instancias superincrecientes.
- `minima.py`, `frontera.py`, `frontera2.py` — búsqueda de condición mínima; contraejemplos aditivos ({8, 5.5, 3.5, 2.8, 2.8} y ρ = 1.234); gadget geométrico al filo rescatado.
- `refuta.py`, `figrefuta.py` — contraejemplo n = 4 ({10, 5, 4.9, 4.8}, R = 15, w = 0.3) con prueba de confinamiento y figura.
- `espejo.py`, `gemelas.py` — instancias gemelas I1/I2 con prefijo compartido (teorema de imposibilidad para reglas de estado).
- `minrho.py` — minimización de ρ en la familia; corroboración del suelo de Tribonacci.
- `umbral.py` — familia aditiva con ρ → 1 (umbral aditivo exacto) y búsqueda geométrica bajo T (0 fallos).
- `reinserta.py` — lema de reinserción: umbral ρ*(ω) del paso de intercambio, fórmula cerrada del perfil de dos aros max(1, 2(1−ω)), cota de banda k·r_k y grosor crítico ω_c ≈ 0.05.
- `banda.py` — búsqueda dirigida de fallos con ρ < T en la ventana crítica (α ≈ φ, ω > ω_c), con control positivo.
- `trio.py` — Proposición 3: en la plantilla canónica el ínfimo del intercambio con los tres ingredientes (bolsillo → trío → testigo) es exactamente la constante de Tribonacci; escalera φ → 1.7997 → T.
- `grosor.py` — grosor positivo: Φ(ω) = T₍₁₊ω₎ − ω (Tribonacci deformado), cota uniforme T_can(ω) ≥ T + 0.00985, esquina racional (1/7, 2, 6/7, 13/7); ver `docs/drafts/grosor_positivo.md`.
- `tresk.py` — perfil de 3 aros: Proposición 4 (cuatro casos) y fórmula cerrada ρ*₃(ω); el cruce con T es exacto: ω_T = 1/T − 1/2 ≈ 0.0437; ver `docs/drafts/perfil_tres.md`.
- `rigido.py` — Teorema S (suelo rígido sin idealización): ρ > T en toda la subfamilia rígida, para todo w > 0; identidad sin²(θ/2) = f(a)f(b), bolsillo rígido exacto (Prop. S5) y familia aproximante del ínfimo; ver `docs/drafts/suelo_rigido.md`.
- `cuadrado.py` — sartén cuadrada: bolsillo de esquina x = (√s−√a)², constante hermana X = 1.7110185903… (raíz de 17x⁴ − 4x³ − 62x² + 4x + 49 en su rama), escalera cuadrada; ver `docs/drafts/cuadrado.md`.
- `batalla2.py` — Teorema P (suelo áureo del intercambio a sartén, S par): identidades exactas del punto fijo áureo 2b(φ) = φ y de las medias metálicas (Ψ_B(1) = φ, Ψ₂(φ/2) = φ, Ψ₃(1) = √3), las cadenas de las ramas A y B, y el cierre del rincón (pared de bolsillos espejo en j = 2, árbol de casos en j = 3); ver `docs/drafts/batalla2.md`.
- `microcelda.py` — Teorema M: cierre de la última rama de j = 3 del intercambio a sartén por la pinza sobre v*, con la constante exacta s* = 11 − 4√5 = 15 − 8φ y sus controles negativos; ver `docs/drafts/microcelda.md`.
- `perfilp.py` — Teorema DP-p (suelo áureo a sartén para perfiles |S| = p ≥ 3, PARCIAL): herencia de las paredes del par en los casos (L)/(N), cadena (H1), programa Ψ_B con hoja estricta, bolsillos espejo (p = 3, j = 1 cerrado para todo ω > 0), swap con H_m (j = 2), controles negativos y barrido dirigido de la región abierta R*; ver `docs/drafts/perfilp.md` (~6–8 min por las coronas del bloque E).

## Hoja de ruta

1. Conjetura del umbral áureo (τ = φ): |S| ≥ 3 en el intercambio a sartén está PARCIALMENTE cerrado (Teorema DP-p, `docs/drafts/perfilp.md`: casos (L)/(N)/(H1)/(H2-ΨB)/(H2-espejos)/(H2-swap j = 2); p = 3 con j = 1 cerrado para todo ω > 0) — queda la región R* de `perfilp.md` §2 (cuatro celdas), los pequeños extra y ensamblar el lema universal de reinserción con umbral φ; en paralelo, fijar el suelo anidado en exactamente T (puntitas de anchura, gap lemma, perfiles k ≥ 4). La micro-celda de j = 3 ya está cerrada (Teorema M, `docs/drafts/microcelda.md`).
2. Pregunta de complejidad para reglas con input completo (oráculo de hermanos, número de consultas).
3. Afilados en cuadrado y en R³ (los teoremas de superincrecencia ya valen; la constante análoga a T es abierta).
4. Grosor variable, flexibilidad δ, inventarios infinitos (ver `docs/generalizaciones.md`).
5. Pulir `paper/main.tex` (nombres, agradecimientos, apéndice con verificaciones) y subir a arXiv; destino: Operations Research Letters o Discrete Applied Mathematics.
