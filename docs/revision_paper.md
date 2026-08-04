# Plan de revisión mayor del paper (2026-08-02)

Dictamen externo: revisión mayor. Directriz de Javier: **reforzar, no
rebajar** — donde el revisor sugiere retirar afirmaciones o acortar, la vía
preferida es demostrar/completar; la longitud es libre (apéndices), el
objetivo es UNA pieza coherente, completa y correcta. Este documento tría los
puntos del dictamen y registra las decisiones.

## Bloqueo 1 — Pruebas anunciadas que no están en el paper

**Decisión: versión completa.** Portar TODAS las demostraciones desde los
drafts a apéndices del paper, con enunciados formales (hipótesis explícitas):

- [x] Apéndice B: prueba completa del Teorema del suelo rígido
  (S1–S4 + teorema + S5 + S6a + S6 + holgura U1), desde `suelo_rigido.md`
  y `universal.md`. — HECHO en esta pasada.
- [x] Apéndice C: el programa de anchura formalizado — HECHO
  (`app:widthproofs`): Prop. ρ*₂, caracterización y fórmula de ρ*₃
  (íntegras), ρ*_k = ρ*₃ (árbol general), frontera cerrada + identidad κ
  + cierre Tribonacci, Φ con derivada y concavidad, Lemas E1/E2, curva
  exacta de tres regímenes, demostración completa del Teorema 13/7
  (cota + quíntica Q₅ + familia genuina vía S5/S6a) y remark del bump.
- [x] Apéndice D: contenedores genéricos formalizados — HECHO
  (`app:genericproofs`): Lema U (con su hipótesis y contraejemplo),
  criterio de coronas (sistema de huecos, certificados, C4 exacto, zigzag,
  U₄ en dos desigualdades, nota k = 5/pentagrama como conjetura no usada),
  paredes V1/V2 con rama fina y corolarios, Lema R, Bo″, Teoremas B/B″
  (dicotomía de evacuación, identidad Tribonacci del umbral), Lema G
  (bolsillos espejo y₀ = 2b₂), Teorema G′ (ambas ramas, todos los casos),
  Ψ_j incondicional (lema de las hojas) y Corolario S. Cuerpo de las
  secciones 8–9 con referencias cruzadas a los apéndices.
- [x] **Demostrar el parche de recursión de Ψ_j** — HECHO vía el **lema de
  las hojas** (`bolsillo.md` §4): cada subárbol de ocupante contiene una
  hoja; la cola de la hoja mayor + la pared Bo″ en ella reproducen
  exactamente el programa de Ψ_j. Sin asteriscos; verificado en
  `code/bolsillo.py` bloque [D] (rejilla = Ψ_j; instancias-árbol
  aleatorias). Caveats eliminados del paper (sec:generic, Status,
  op:assembly). REFORZADO, no explicado.
- [x] Secciones 8–9 del cuerpo sobre los apéndices: cada párrafo remite a
  los enunciados formales de C/D; lo demostrado es teorema/proposición con
  prueba en apéndice, y lo no demostrado queda explícito (conjetura del
  pentagrama declarada como no usada; huecos en Status/op:assembly).

## Bloqueo 2 — Sobre-afirmación del teorema de objetivos

- [x] "every monotone superadditive value" → "every positive, strictly
  increasing, superadditive value" en abstract, contribuciones, Teorema de
  obliviousness y generalizaciones (e). (La positividad es necesaria —
  contraejemplo v ≡ −1 del revisor — y la estricta creciente es la que usa
  la prueba de dominancia.)

## Bloqueo 3 — Sección de complejidad

- [x] La cita propuesta por el revisor (FKS, DCG 69:51–90, Teorema 5.1 =
  NP-dureza en contenedor disco) **NO SE PUDO VERIFICAR**: el preprint
  arXiv:1903.07908 (única versión) no la contiene, y la survey SoCG 2021 de
  los mismos autores atribuye la dureza solo al contenedor cuadrado (DFL).
  NO se cita. Resuelto por otra vía (reforzando):
- [x] Capa geométrica: nuestro modelo admite contenedor arbitrario ⟹ con
  sartén CUADRADA y banda sin anidamiento contiene literalmente el problema
  de DFL ⟹ NP-dura dentro del modelo, sin citas dudosas. El caso de sartén
  circular se declara abierto en la literatura, con Abrahamsen–Miltzow–
  Seiferth (∃R-completitud de packing 2D) como contexto de por qué la
  pertenencia a NP ya es delicada.
- [x] Capa aditiva: reducción COMPLETA desde PARTITION (no "≈"): radios
  r_i = δ(a_i + 3B) con δ ∈ (w/(3B), w/(2B)) — banda < w (sin anidamiento),
  r_i > w (aros genuinos), y el análisis de los tres casos |S| ⋚ n/2 domina
  la penalización −πw²|S|. Proposición con prueba en el paper.

## Bloqueo 4 — Novedad insuficientemente situada

- [x] El lema de selección presentado como hecho general de sistemas de
  independencia (citas en texto a Edmonds y Korte–Hausmann), comparación
  explícita con la mochila supercreciente (Gupte); la novedad se reclama
  para el teorema geométrico de placement-obliviousness; "No analogue was
  known" suavizado a "we are not aware of".
- [x] Aviso temprano de que el selection greedy usa un oráculo de
  factibilidad de conjuntos (no es un algoritmo eficiente per se).

## Bloqueo 5 — Repositorio como suplemento reproducible

- [x] URL del repo + commit citado en el paper. PENDIENTE de Javier: hacer
  público el repo antes de subir a arXiv, y decidir si Zenodo/DOI.
- [x] `code/requirements.txt` corregido (numpy, scipy, sympy, matplotlib).
- [x] `code/run_all.py`: comando único que ejecuta todas las verificaciones
  y resume los verdes.
- [x] Clasificación exacto-vs-numérico: ya está por diseño en los bloques
  ([A] simbólico vs resto); frase explícita añadida al apéndice del paper.
- [x] Redacción: la garantía matemática son las pruebas escritas y las
  identidades exactas; el flujo adversario con LLMs se describe como
  metodología de control de calidad (agradecimientos), no como garantía.
- [ ] Zenodo/DOI al congelar la versión de arXiv.

## Editoriales

- [x] Abstract a ~240 palabras.
- [x] Contribuciones reestructuradas: teoremas principales / programa y
  evidencia / abiertos.
- [x] "threshold exactly 1" formulado como umbral universal (no "toda
  instancia con ρ > 1 falla").
- [x] Litvinchev citado en texto (formulaciones MIP); Edmonds y
  Korte–Hausmann citados en texto (Bloqueo 4).
- [x] Figuras autocontenidas en `paper/figures/` (sin `../figures`);
  colocación revisada.
- [x] "Draft" fuera de la nota de autor; fecha fijada.
- [x] Overfull hbox: 0 en el log tras la pasada de maquetación (los tres
  restantes — ρ_needed, Q₅, configuración de V3 — reformateados).

## Estado

Pasada 1: bloqueos 2–5 y editoriales ejecutados; apéndice B (suelo
rígido) portado. Pasada 2: parche de Ψ_j demostrado (lema de las hojas) y
caveats eliminados; apéndices C y D portados íntegros (32 pp.); secciones
8–9 referenciadas sobre ellos. Queda: pasada final de maquetación
(overfull de las gemelas, colocación de figuras, congelar fecha),
verificación adversaria del lema de las hojas (en curso), y los puntos de
Javier (repo público, Zenodo/DOI).
El email de endorsement (math.MG) espera a que esto esté cerrado.
