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
- [ ] Apéndice C: el programa de anchura formalizado — Prop. ρ*₂, Prop. ρ*₃
  (casos completos), ρ*_k = ρ*₃ (árbol), H1 (κ = √(g/g)), Prop. 4 (Φ),
  curva completa y Teorema de la esquina. Fuentes: `perfil_tres.md`,
  `cuatro.md`, `h1.md`, `grosor_positivo.md`, `esquina.md`.
- [ ] Apéndice D: contenedores genéricos formalizados — Lema U (con su
  hipótesis), criterio de coronas (C1–C7), paredes de ocupantes (V1–V2,
  Lema R, Teoremas B/B″), bolsillo doble (Lema G, Teoremas G/G′), Ψ_j,
  Corolario S. Fuentes: `universal.md`, `corona.md`, `ocupantes.md`,
  `bloqueadores.md`, `bolsillo.md`.
- [ ] **Demostrar el parche de recursión de Ψ_j** (el único "modulo" del
  texto): lema de recursión para el caso hijo-nodo del mayor ocupante
  (esbozo en `bolsillo.md` §4; robustez numérica ya atacada sin éxito).
  REFORZAR: eliminar el asterisco demostrándolo, no explicándolo.
- [ ] Tras portar C y D: reescribir las secciones 8–9 del cuerpo como
  resumen con referencias a los apéndices, y re-etiquetar qué es teorema
  (todo salvo las conjeturas C8/tribo y los huecos declarados).

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
- [ ] Overfull hbox de las gemelas y marcadores PDF: revisar en la pasada
  final de maquetación.

## Estado

Pasada 1 (esta): bloqueos 2–5 y editoriales ejecutados; apéndice B (suelo
rígido) portado. Pasadas siguientes: apéndices C y D, parche de Ψ_j,
reescritura de las secciones 8–9 sobre los apéndices, maquetación final.
El email de endorsement a Bas Lemmens espera a que esto esté cerrado.
