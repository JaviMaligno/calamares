# Acta de revisión ciega — BLOQUE 1

**Paper:** `paper/main.tex` (release del repo `calamares`).
**Objeto:** Secciones «Introduction» (l. 84–178), «Model and preliminaries» (l. 179–230),
«The superadditivity dichotomy» (l. 231–298), «Placement obliviousness under
superincreasing radii» (l. 300–353).
**Referee:** externo, ronda ciega sin líneas de ataque suministradas.
**Fecha:** 2026-08-20.

**VEREDICTO GLOBAL DEL BLOQUE: CONFIRMADO CON CORRECCIONES**
(ningún hallazgo FATAL; 1 OBLIGATORIA, 2 RECOMENDADAS, 5 MENORES; todos los
resultados matemáticos del bloque son correctos y fueron re-derivados de forma
independiente).

---

## Veredicto por sección

### §1 Introduction (l. 84–178) — CONFIRMADO (con H7, H8 menores)

Cada afirmación de las dos listas de contribuciones fue contrastada con el
enunciado del teorema citado en el cuerpo del paper; ninguna sobredeclara el
alcance de su fuente:

- (1) dicotomía de superaditividad ↔ Thm `thm:selection` + Prop `prop:count` (l. 263, 291). Coincide.
- (2) obliviousness ↔ Thm `thm:oblivious` (l. 303), «container-shape- and dimension-agnostic» — el enunciado y la prueba efectivamente no usan nada de la forma de K ni de la dimensión (verificado línea a línea, ver más abajo). Coincide.
- (3) sharpness n≤3 / n=4 / gemelas ↔ §5 (l. 354 ss., fuera del bloque; las etiquetas existen). Coincide.
- (4) umbral aditivo exactamente 1 ↔ `thm:additive` (l. 453): «universal threshold exactly 1», con la salvedad honesta «individual instances with larger ρ may of course still succeed». Suelo Tribonacci del subfamilia rígida ↔ `thm:rigidfloor` (l. 486, «no idealization», prueba en `app:rigidproof` l. 1359). Familia áurea ↔ `thm:golden` (l. 559) y `cor:goldencover` (l. 626, anchura fija ω=0.3 como dice la intro). τ≥φ «para pan exchanges con perfiles par» ↔ `thm:DP` (l. 2769), «extendido a perfiles mayores fuera de una región pesada explícita» ↔ `thm:DPp` (l. 2909, la región restante remitida a `op:assembly`(a) — el scoping de la intro es honesto), «conjectured in general» ↔ `conj:golden` (l. 651). Coincide.
- (5) cúbica deformada, mínimo 13/7 en esquina racional ↔ `thm:corner` (l. 788); cruce ω_T = 1/T − 1/2 = T² − T − 3/2 (l. 743): la identidad la comprobé desde T³=T²+T+1 (1/T = T²−T−1). Coincide.
- (6) muros de bloqueo con suelos metálicos y los rangos ω<0.9626 (j=1), 0.624 (j=2), 0.896 (j=3), todo ω con j≥4 ↔ párrafo «Status» (l. 963–975), literal. Nota: la «golden line» tiene un corner sin probar (l. 914–917), pero en ese corner la cota probada es ≥2>T, de modo que el reclamo de la intro («push every blocked exchange with extra occupants above T») queda íntegro — verificado que la salvedad no socava lo que la intro afirma. La intro además remite explícitamente los huecos a `op:assembly` (l. 172–173). Honesto.
- (7) diagrama de fases y desacoplamiento ↔ §§ `sec:divergence`, `sec:hardness` (l. 994, 1021). Coincide.
- Citas usadas en el bloque (`PedrosoCunhaTavares2016`, `Gleixner2020`, `CoffmanGareyJohnson1987`, `Edmonds1971`, `KorteHausmann1978`, `Gupte2016`): todas presentes en la bibliografía (l. 3818 ss.).

### §2 Model and preliminaries (l. 179–230) — CONFIRMADO CON CORRECCIONES (H1)

- Definiciones consistentes: un anillo con r≤w es disco sin agujero y no puede
  tener hijos (r_child ≤ r−w ≤ 0), coherente. La convención «feasibility is a
  property of the assignment (siblings may be rearranged freely)» (l. 192–193)
  está declarada y es la que luego hace funcionar el paso de intercambio de
  `thm:oblivious` — bien que esté explícita.
- **Row lemma (l. 219–229): correcto.** Derivación propia: con
  p_j = −C + 2Σ_{l<j}x_l + x_j se tiene p_j ≥ −C+x_j y
  p_j ≤ −C+2Σx−x_j ≤ C−x_j, y p_{j+1}−p_j = x_j+x_{j+1} (tangentes, interiores
  disjuntos). Verificado además con barrido racional exacto (5.000 casos,
  incluido el caso apretado C = Σx): 0 fallos.
- La nota sobre el oráculo de factibilidad del selection greedy («information
  bound, not an efficient algorithm», l. 209–213) es un etiquetado honesto.
- Hallazgo H1 (clausura hacia abajo), abajo.

### §3 The superadditivity dichotomy (l. 231–298) — CONFIRMADO (H3, H6 menores)

- **Lemma `lem:superadd` (l. 233–244): correcto y completo.** Los cuatro casos
  cubren (x,y≥w; x+y≤w; x,y≤w<x+y; x≤w≤y, este último simétrico). Los
  verifiqué simbólicamente con sympy: caso A se reduce a w²≥0; caso B a 2xy≥0;
  caso C a la identidad w(x+y)−x²−y² = x(w−x)+y(w−y) ≥ 0 más w≤x+y; caso D a
  x≤2w. Barrido numérico adicional de 200.000 puntos de la a() completa
  (superaditividad + monotonía estricta): 0 fallos.
- **Lemma `lem:lexdom` (l. 246–261): correcto.** La cadena
  Σ_{T\P} v(r_j) ≤ v(Σ_{T\P} r_j) < v(r_i) usa superincrecencia estricta y
  monotonía estricta de v exactamente donde se anuncian; el caso T\P=∅ y la
  condición de igualdad («only if T⊆S») cuadran (v positiva).
- **Thm `thm:selection` (l. 263–275): correcto.** El argumento
  greedy=lex-max por inducción es completo (ambas direcciones). Verificación
  independiente del enunciado *abstracto* (sistemas de conjuntos downward-closed
  aleatorios + pesos superincrecientes + tres objetivos superaditivos, 400
  sistemas, comparación exhaustiva contra todos los subconjuntos factibles):
  0 fallos.
- **Prop `prop:count` (l. 291–298): la instancia es exacta y la comprobé con
  aritmética racional pura, sin oráculo heurístico.** Superincrecencia:
  9.95 > 9.9, 5.0 > 4.9, 4.3 > 0.6 ✓. La traza del greedy está forzada en cada
  paso por criterios exactos (círculo solo: r≤C; dos círculos en disco C:
  a+b≤C, exacto; fila: Σ≤C suficiente): 5.0 solo cabe anidado
  (5.0 ≤ 9.95−4.8 = 5.15; pan: 14.95>10), 4.3 y 0.6 rechazados en los tres
  contenedores (14.25>10; 9.3>5.15; 4.3>0.2 — 10.55>10; 5.6>5.15; 0.6>0.2), y
  el testigo {5.0,4.3,0.6} entra en fila (9.9≤10). N=2 vs N=3 ✓. «Optimal
  area» ✓ (el lex-max es {9.95,5.0} y lexdom aplica). Reproduje además
  `code/superinc.py`: N=2/A=306.1 vs N=3/A=306.1 — greedy óptimo en área,
  subóptimo en número, como se afirma.

### §4 Placement obliviousness (l. 300–353) — CONFIRMADO (H2, H4, H5 menores)

- **Thm `thm:oblivious` (l. 303–341): la prueba es correcta; la re-derivé
  paso a paso.** Puntos que verifiqué expresamente:
  - u ≠ v (m asignado a contenedores distintos), y tanto u como v son el pan o
    agujeros de anillos *mayores* que m (r_m ≤ r_p − w < r_p), que por
    maximalidad de m no se mueven — la prueba lo dice (l. 335–336).
  - «los ocupantes de u cuando F colocó m eran exactamente los anillos mayores
    que m que F asigna a u»: correcto por el orden decreciente; y por
    maximalidad de m coinciden con los de P. La certificación de F es a nivel
    de *conjunto*, y la convención de reordenación libre de hermanos
    (l. 192–193) es la que permite reutilizarla aunque P los tenga en otras
    posiciones — la hipótesis está declarada en el modelo.
  - Paso (i): la cota Σ_{j: r_j<r_m} r_j ≤ r_m es donde entra la
    superincrecencia (débil basta, ✓); los anillos movidos van con sus
    subárboles (la relación padre-hijo interna no cambia) y el nuevo padre
    (el anillo de v o el pan) satisface r_j < r_m ≤ r_{p'} − w. Si i estaba en
    u, se mueve también y P′ sigue colocando G∪{i}.
  - El mayor índice de desacuerdo decrece estrictamente; ≤|G| iteraciones; el
    contenedor c* de i en P* existe en F con ocupantes idénticos; la dirección
    recíproca (greedy coloca ⇒ factible) es inmediata. La inducción del
    conjunto es la de `thm:selection`. Completo.
  - Sin circularidad: row lemma → lexdom → selection → oblivious, todo hacia
    atrás.
- **Test de estrés independiente del núcleo combinatorio del intercambio:**
  en el modelo aditivo con oráculo *exacto* (Σ de radios ≤ capacidad), 3.000
  instancias débilmente superincrecientes (incluyendo el borde r_i = Σ cola),
  cada una ejecutada bajo 64 ramificaciones deterministas de regla de
  colocación: **las 64 reglas producen el mismo conjunto en las 3.000
  instancias.** Esto ejercita exactamente la versión del teorema que
  `thm:additive` (l. 453) invoca «verbatim».
- **Remark (l. 343–352):** reproduje la corroboración: `code/test_oblivious.py`
  → «100 instancias superincrecientes, fallos de área por regla: {best: 0,
  worst: 0, rand: 0}». Coincide con lo declarado. Está etiquetada como
  «computational corroboration» de un teorema ya probado: etiquetado honesto.
  Ver H4/H5 para dos matices.

---

## Hallazgos

### H1 [OBLIGATORIA] — La clausura hacia abajo de la factibilidad se afirma sin prueba, y el parche «obvio» vía Row lemma no funciona en general

**Cita:** l. 207 «Since feasibility is downward closed, $L$ is the unique
lexicographically maximal feasible set»; usada de nuevo en l. 271 («Feasibility
is downward closed, so the selection greedy computes $L$») y como ingrediente
(a) del Remark l. 344.

**Problema:** en el modelo de bosque, quitar un anillo m de un conjunto factible
deja huérfanos a sus hijos: hay que re-parentarlos, y eso es un paso geométrico,
no tautológico. Además, la vía que el texto sugiere implícitamente (la cláusula
«Consequently…» del Row lemma: reinsertar por radio total en la bola vacante)
**no cubre el caso general**: los hijos de m empaquetan en el agujero de radio
r_m−w pero su radio total puede exceder r_m (discos disjuntos en un disco de
radio h pueden sumar radios ≫ h), así que la reinserción en fila no está
garantizada para radios arbitrarios — y la clausura se usa en el modelo general
(la definición de L en l. 205–209 no está restringida a radios
superincrecientes; `prop:n3` la usa con radios arbitrarios).

**Corrección propuesta (una frase):** los hijos de m *no se mueven*: quedan
donde estaban, dentro de la región que ocupaba la bola de m, y pasan a ser
hijos del contenedor de m (o del pan). La restricción de anidamiento se
conserva: si el contenedor de m era el agujero de p, entonces
r_child ≤ r_m − w < r_m ≤ r_p − w. Con esto la clausura hacia abajo es un
lema de una línea; debería enunciarse en §2 (basta un paréntesis tras
«downward closed»). Verifiqué la contabilidad de la desigualdad con sympy.

**Severidad:** OBLIGATORIA porque el hecho es portante para los dos teoremas
del bloque y el argumento correcto no es el que el texto deja a mano; la
reparación es trivial y no toca ningún enunciado.

### H2 [MENOR] — El paréntesis «weakly … suffices» del Teorema 4.1 desborda la Lemma 3.2 tal como está enunciada

**Cita:** l. 304 «(weakly: $r_i\ge\sum_{j>i}r_j$ suffices)» junto con la
conclusión «are all optimal for every positive, strictly increasing,
superadditive objective» (l. 309–310); Lemma `lem:lexdom` (l. 246–251) está
enunciada solo para superincrecencia estricta.

**Problema:** bajo la hipótesis débil, la conclusión de optimalidad necesita la
versión no estricta de lexdom (que es cierta: Σ_{T\P} v(r_j) ≤ v(Σ) ≤ v(r_i),
perdiéndose solo la condición de igualdad). No es un error — la cadena
sobrevive — pero el lector debe reconstruirla.

**Corrección:** un paréntesis en lexdom o en 4.1: «bajo la versión débil la
dominancia vale con desigualdad no estricta, suficiente para la optimalidad».

### H3 [MENOR] — La Lemma 3.1 dice «increasing»; la aplicación al área en el Teorema 3.3 exige «strictly increasing»

**Cita:** l. 234 «The contact area $a$ is increasing and superadditive»; l.
266–268 «for every positive, strictly increasing, superadditive $v$; in
particular it maximizes the contact area $A$».

**Problema:** a es de hecho estrictamente creciente (πr² en r≤w, πw(2r−w) en
r≥w; lo verifiqué en el barrido), pero la lemma no lo reclama, de modo que el
«in particular» no queda formalmente cubierto por lo enunciado.

**Corrección:** escribir «strictly increasing» en `lem:superadd`.

### H4 [RECOMENDADA] — Los reclamos computacionales de §§3–4 no tienen script nombrado ni tope declarado del oráculo

**Cita:** l. 293 «Example (verified)»; l. 348–351 «Computational corroboration
… on $100$ random superincreasing instances …».

**Problema:** el mapa de verificación (`app:verifmap`, l. 1222) cubre
explícitamente «Sections threshold–generic»; §§3–4 quedan solo bajo el
paraguas genérico de la nota de autor, mientras el resto del paper sí nombra
sus scripts (p. ej. `code/aureo.py` en l. 624). Los scripts existen y los
reproduje (`code/superinc.py`, `code/test_oblivious.py`, ambos verdes). Además,
el oráculo de factibilidad de esos scripts, más allá de los criterios exactos
(uno/dos círculos, fila), es un empaquetador heurístico con reinicios
(`pack_feasible`): puede dar falsos negativos, compartidos por greedy y por el
óptimo exhaustivo. Para la instancia de `prop:count` esto es irrelevante
(comprobé que cada decisión cae en un criterio exacto — el «(verified)» es de
hecho redundante con una prueba exacta), pero para la corroboración de 100
instancias el sesgo direccional de un falso negativo en el testigo óptimo iría
*a favor* de «ningún fallo» (criterio 3), y conviene declararlo como tope.

**Corrección:** nombrar los dos scripts en el texto (o añadirlos al verifmap) y
una frase declarando que el oráculo muestral es heurístico fuera de los casos
exactos. Nada de esto afecta a los teoremas, que están probados.

### H5 [MENOR] — «identical, optimal outcomes»: lo comprobado directamente es la optimalidad, la identidad es corolario

**Cita:** l. 349–351 «best-fit, worst-fit and random placement produced
identical, optimal outcomes without exception».

**Problema:** `test_oblivious.py` compara el valor (área) de cada regla contra
el óptimo; no compara los conjuntos entre sí. La identidad de conjuntos se
sigue de la unicidad del óptimo (lexdom con v positiva y superincrecencia
estricta), no del experimento. Afirmación verdadera, evidencia indirecta.

**Corrección:** o comparar conjuntos en el script, o decir «optimal (hence, by
Lemma 3.2, identical) outcomes».

### H6 [MENOR] — «every descending greedy» en Prop 3.4: el cuantificador merece su media línea

**Cita:** l. 292–295 «There are superincreasing instances on which every
descending greedy is suboptimal for $N$. … Greedy places $\{9.95,5.0\}$».

**Problema:** «every» está justificado porque en esta instancia ninguna
iteración ofrece más de un contenedor factible (lo comprobé: 9.95 solo pan,
5.0 solo el agujero, 4.3 y 0.6 ninguno), de modo que todas las reglas
coinciden; alternativamente se sigue de Thm 4.1, que aparece *después*. Tal
como está escrito, el lector debe verificar la unicidad de la traza por su
cuenta para no leer una dependencia hacia delante.

**Corrección:** añadir «(no step offers a choice of container, so all
placement rules coincide)».

### H7 [MENOR] — «we determine exactly how far the hypothesis can be relaxed» sobredeclara en media frase

**Cita:** l. 105–107.

**Problema:** «exactly» es verdadero para la relajación aditiva (umbral 1,
teorema) pero para el modelo geométrico el paper prueba τ≤φ y deja τ≥φ
parcial/conjetural — como la propia frase siguiente admite («conjecturally,
exactly»). El verbo «determine» aplicado a ambos modelos es más fuerte que la
posición honesta del propio paper.

**Corrección:** p. ej. «and we determine exactly how far it can be relaxed in
the additive model, bracketing the geometric threshold».

### H8 [MENOR] — «best fit (place in the feasible container of smallest capacity)» presupone una capacidad escalar que el pan arbitrario no tiene

**Cita:** l. 307–309, en un enunciado que rige para K ⊂ R^d arbitrario.

**Problema:** para agujeros la capacidad es r−w; para un K arbitrario
«capacity» no está definida. Es solo la especialización ilustrativa (el
teorema cubre reglas arbitrarias, así que nada falla), pero la definición de
best/worst fit queda flotando fuera del caso disco.

**Corrección:** «(for the disk pan, the container of smallest capacity)» o
definir capacidad del pan como el radio de la mayor bola inscrita.

---

## Verificado positivamente (resumen)

1. **Lemma superadd:** 4 casos re-derivados simbólicamente (sympy) + barrido
   200k (superaditividad y monotonía estricta de la a() completa): 0 fallos.
2. **Row lemma:** desigualdades |p_j| ≤ C−x_j y tangencia re-derivadas; barrido
   racional exacto 5.000 casos incluyendo C = Σx: 0 fallos.
3. **Prop count:** instancia verificada con racionales exactos y criterios
   geométricos exactos en cada decisión; traza del greedy forzada; testigo en
   fila; superincrecencia; área óptima. Reproducción de `code/superinc.py` ✓.
4. **Thm selection:** re-derivado como enunciado sobre sistemas
   downward-closed; test independiente con 400 sistemas aleatorios × 3
   objetivos superaditivos contra enumeración exhaustiva: 0 fallos.
5. **Thm oblivious:** prueba re-derivada paso a paso (maximalidad de m,
   coincidencia de ocupantes, persistencia del anidamiento, descenso estricto
   del primer desacuerdo, dirección recíproca); núcleo combinatorio testeado
   con oráculo exacto aditivo: 3.000 instancias débilmente superincrecientes ×
   64 reglas → conjunto único siempre. Reproducción de
   `code/test_oblivious.py`: 0/100 fallos, como declara el Remark.
6. **Introducción:** todas las referencias cruzadas existen y los reclamos
   coinciden con los enunciados citados (incluida la identidad
   ω_T = 1/T−1/2 = T²−T−3/2, los rangos 0.9626/0.624/0.896, el scoping honesto
   de τ≥φ y la no-interferencia del corner sin probar de la golden line con el
   reclamo de la intro). Bibliografía del bloque completa.
7. **Sin circularidad** en el bloque; **sin gates tautológicos** en las pruebas
   (los tests computacionales del bloque son falsables — prop:count demuestra
   que el mismo arnés detecta subóptimos — con el matiz direccional de H4).
8. Aritmética de colas de la familia áurea citada por la intro
   (cola de φ = φ+3ε/φ < φ+3ε = cola de 1, luego ρ = φ+3ε): re-comprobada.

Script del referee: `scratchpad/ciega/ref_bloque1.py` (20/20 PASS).
