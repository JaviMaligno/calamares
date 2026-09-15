# El problema de los calamares — Nested Ring Packing

Investigación sobre el empaquetamiento de aros con anidamiento recursivo: superincrecencia, irrelevancia de colocación, instancias gemelas y umbrales. El suplemento del 2026-09-15 prueba **τ = φ**, con ínfimo no alcanzado, para cualquier inventario finito en el disco, incluso con agujeros independientes. La prueba escrita tiene revisión independiente de Fable y certificados algebraicos parciales en Lean. La v2 de referencia prueba **τ₄ = φ** en contenedores esféricos de cualquier dimensión d ≥ 2. El umbral aditivo es 1 y el suelo exacto de la familia rígida anidada es Tribonacci, T. En cuadrado se prueban gemelas y la cota algebraica **τ_cuadrado ≤ Y ≈ 1.684487745872346**.

**V2 integrada, 2026-09-15:** el [PDF unificado](output/pdf/calamares_v2_integrada.pdf)
incorpora la prueba global de **τ = φ**, las generalizaciones anteriores,
el teorema de cinco aros en dimensión arbitraria y la garantía exacta de
área con agujeros independientes. Fuentes en [paper/v2/main.tex](paper/v2/main.tex)
y paquete autónomo en [arxiv-v2-integrada.tar.gz](paper/arxiv-v2-integrada.tar.gz).

Construcción y comprobación del paquete desde la raíz:
`python paper/build_v2.py --verify-bundle`.
La [revisión de integración](docs/reviews/2026-09-15-v2-integrada-validation.md)
registra la revisión editorial, visual, Lean y los controles ejecutados.
Las pruebas fuente fueron revisadas por Claude Code/Fable; la revisión del
manuscrito inglés integrado y de su PDF es local. Es una versión de trabajo
lista para leer, todavía no publicada.

La v2 anterior (`paper/main.tex`, `paper/generalizations_v2.tex` y
`output/pdf/calamares_v2.pdf`) se conserva como referencia del día 14,
sin modificar sus diez artefactos registrados. Su auditoría histórica está
en `docs/drafts/umbral_v2_auditoria.md`; el cierre posterior está en
`docs/drafts/tres_mayores.md`.

**Extras del 2026-09-15:** hay pruebas nuevas de
[`tau_(≤5,d)=phi`](docs/drafts/cinco_aros.md), incluso con agujeros
independientes, y del [umbral de área `1/sqrt(2)` con grosor variable](docs/drafts/grosor_variable.md).
Para `rho≤kappa<1`, la garantía de área exacta es
`min(1,kappa^(-2)-1)`. Estos extras tienen 18 certificados nuevos en
Lean y revisión independiente de Fable, con precisiones menores
[incorporadas](docs/reviews/2026-09-15-fable-extras-response.md). Están incorporados
al PDF y al bundle de la v2 integrada; la referencia del día 14 se conserva. Por sí solos no prueban
el resultado global posterior. Véase la
[validación y el alcance](docs/reviews/2026-09-15-extras-validation.md).

**Cierre uniforme, 2026-09-15:** [tres_mayores.md](docs/drafts/tres_mayores.md)
demuestra que, bajo las cotas de cola áureas, basta colocar los tres
discos mayores para poder colocar la lista completa. Esto crea dos
plazas auxiliares en todo contenedor ramificado y cierra el intercambio
para cualquier inventario finito, sin clasificar tamaños sucesivos.
Junto a la familia aproximante ya probada, resulta **tau=phi**.
Fable [acepta la prueba y sus dependencias](docs/reviews/2026-09-15-fable-three-core-final-review.md);
las [aclaraciones están incorporadas](docs/reviews/2026-09-15-fable-three-core-final-response.md).

El [suplemento independiente](paper/golden_threshold.tex) y su
[PDF de seis páginas](output/pdf/golden_threshold.pdf) reúnen la prueba
en inglés, también integrada en el artículo unificado. Siete certificados nuevos compilan en Lean y el script
`code/tres_mayores.py` comprueba posiciones completas. La geometría y
el ensamblaje del bosque siguen siendo pruebas escritas; véase la
[validación](docs/reviews/2026-09-15-three-core-validation.md).
La [reducción anterior a 40 mayores](docs/drafts/nucleo_uniforme.md)
se conserva como historial, sin dictamen externo: el cierre no la usa.

## Estructura

- `paper/v2/main.tex` — artículo integrado en inglés; `python paper/build_v2.py --verify-bundle`. `paper/main.tex` conserva la versión anterior.
- `paper/render_v2_figures.py` — regenera las tres figuras de v2 con rótulos legibles en inglés.
- `docs/resultados.md` — documento de trabajo completo en español: modelo, lemas y teoremas con demostraciones, contraejemplos, veredictos de novedad y estrategia de publicación.
- `docs/generalizaciones.md` — todas las generalizaciones anotadas, con estado y primeras preguntas.
- `docs/reinsercion.md` — lema de reinserción: la parte combinatoria del umbral de Tribonacci, cerrada con cota exacta, y la parte geométrica aislada (mínimo en la razón áurea).
- `figures/` — divergencia área/número, diagrama de fases, contraejemplo n = 4.
- `lean/` — 122 teoremas Lean 4 de core, sin mathlib: los 84 de v2, 18 para cinco aros y grosor variable, tres para particiones de colas, tres para la reducción adyacente, siete para plazas libres y cotas estructurales y siete para el álgebra de la prueba de tres mayores. Incluye el Lema Q paramétrico, exclusiones cartesianas, testigo de las gemelas, identidades de Y, balances áureos y desigualdades de área. Cero `sorry`, sin axiomas añadidos ni `native_decide`. Comando: `cd lean && lake build`. Bosques, interpretación euclidiana y continuidad siguen por escrito; alcance en `lean/README.md`.
- `code/` — scripts de verificación reproducibles (Python; dependencias: numpy, scipy, sympy, matplotlib — véase `code/requirements.txt`). Comando único: `python code/run_all.py` (~33 min; `--quick` omite `cuadrado.py`, `perfilp.py` y `rstar.py`, ~8 min); código de salida 0 sólo si todo está en verde.

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
- `cuadrado_certificado.py`, `cuadrado_gemelas.py`, `cuadrado_optimizado.py`, `cuadrado_limite.py` — certificados racionales del fallo D, las gemelas, la mejora finita y tres ejemplos de la familia aproximante a Y; el paso al límite se demuestra por escrito en `docs/drafts/cuadrado_limite.md`.
- `grosor_variable.py` — geometría exacta de dos aros con agujeros independientes, familias límite de la razón de áreas y controles donde el agujero sí admite al segundo. `test_grosor_variable.py`: 11 tests. La prueba universal está en `docs/drafts/grosor_variable.md`.
- `tres_mayores.py` — construcción explícita de todos los centros para las dos ramas de T3 y comprobación separada de paredes y pares: 10 000 listas aleatorias, seis casos de frontera y dos controles negativos. No usa optimización y no convierte el muestreo en prueba universal.
- `batalla2.py` — Teorema P (suelo áureo del intercambio a sartén, S par): identidades exactas del punto fijo áureo 2b(φ) = φ y de las medias metálicas (Ψ_B(1) = φ, Ψ₂(φ/2) = φ, Ψ₃(1) = √3), las cadenas de las ramas A y B, y el cierre del rincón (pared de bolsillos espejo en j = 2, árbol de casos en j = 3); ver `docs/drafts/batalla2.md`.
- `microcelda.py` — Teorema M: cierre de la última rama de j = 3 del intercambio a sartén por la pinza sobre v*, con la constante exacta s* = 11 − 4√5 = 15 − 8φ y sus controles negativos; ver `docs/drafts/microcelda.md`.
- `perfilp.py` — Teorema DP-p (suelo áureo a sartén para perfiles |S| = p ≥ 3, PARCIAL): herencia de las paredes del par en los casos (L)/(N), cadena (H1), programa Ψ_B con hoja estricta, bolsillos espejo (p = 3, j = 1 cerrado para todo ω > 0), swap con H_m (j = 2), controles negativos y barrido dirigido de la región abierta R*; ver `docs/drafts/perfilp.md` (~6–8 min por las coronas del bloque E).
- `rstar.py` — Teorema DPr (cierre de la región R* del DP-p salvo una celda): la pinza-con-Σ con su frontera exacta s' = (φ−1)Σ + (16−9φ) y margen 23−14φ (cierra p = 3, j ≥ 3), las tres ramas de p = 3, j = 2 (espejos / Ψ-programa con Ψ(1/2) = φ exacto / pared de corona con margen 0.494), las coronas murales de j = 1 (p ≥ 4) y el análisis de frontera de j = 2 (sup = π exacto en la esquina excluida {σ₁ = 1, W = 0}); criterio de camino más largo (corrección del pentagrama); queda abierta {p ≥ 4, σ₁+M ≤ 1, j ≥ 3}; ver `docs/drafts/rstar.md` (~5–8 min por el barrido de la pared de corona).

## Hoja de ruta

1. Umbral universal τ = φ en el disco: cerrado mediante T3 e intercambio para inventarios finitos arbitrarios, revisado por Fable. La prueba está integrada en el artículo unificado; queda auditar la extensión global a dimensiones superiores. Los residuos del manuscrito anterior se conservan como historial, resueltos por el nuevo argumento global en el plano.
2. Pregunta de complejidad para reglas con input completo (oráculo de hermanos, número de consultas).
3. Generalizaciones integradas en la v2: reducción dimensional, gemelas cuadradas y familia aproximante que prueba `tau_cuadrado ≤ Y≈1.684487745872346`. Fable acepta estos bloques con aclaraciones menores ya incorporadas. La geometría cartesiana y el álgebra tienen soporte Lean; la continuidad se prueba por escrito. Queda la optimalidad de Y.
4. Grosor variable: garantía exacta de área aceptada por Fable. Su extensión a volumen es una continuación posible. Flexibilidad δ e inventarios infinitos siguen abiertos (ver `docs/generalizaciones.md`).
5. La integración y revisión local de `paper/v2/main.tex` están completas. Queda la decisión editorial y la publicación de la revisión en arXiv; destino propuesto: Operations Research Letters o Discrete Applied Mathematics.

Fable confirmó D, Q y G1 en la [primera revisión](docs/reviews/2026-09-14-fable-square-review.md),
y los restantes bloques de generalizaciones en la
[revisión de la v2](docs/reviews/2026-09-14-fable-v2-review.md), con
[aclaraciones atendidas](docs/reviews/2026-09-14-fable-v2-response.md).
Una [tercera revisión](docs/reviews/2026-09-14-fable-four-ring-review.md)
acepta la prueba completa de `tau_4=phi`; sus cinco precisiones de
redacción están [incorporadas](docs/reviews/2026-09-14-fable-four-ring-response.md).
