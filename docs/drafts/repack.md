# F2: el lema de realización y repack

Estado: DRAFT con pruebas (2026-08-09), PRE-ADVERSARIO. Script:
`code/repack.py` (5/5). Cierra el [ENUNCIADO] F2 — la legalidad del
repack de contenedores — del que dependen las pinzas de bolsillo
espejo (F1e/F1f), las coronas de agujero, el pan repack de thm:DP y
todos los repartos testigo del programa. Es una prueba de
DEFINICIÓN: la única de la lista de residuo que no necesitaba
geometría nueva, solo poner la inducción debajo de la frase del
paper.

## 1. La definición y lo que deja implícito

La definición del paper (Rings and placements): una colocación es
un BOSQUE — cada anillo tiene por padre la sartén o un anillo con
r_hijo ≤ r_padre − w — y los hijos de un padre común deben ser
empaquetables COMO BOLAS (radio exterior, interiores disjuntos)
dentro de la región del padre (la sartén, o la bola-agujero de
radio r − w). Y la frase clave: «Feasibility is a property of the
assignment (siblings may be rearranged freely inside their
container)».

Lo implícito, que este lema prueba: que las colocaciones POR
CONTENEDOR se componen en una realización geométrica GLOBAL, y que
por tanto «rearranged freely» es legítimo — cambiar la colocación
de un contenedor no puede romper nada en el resto del árbol.

## 2. El lema

**Lema (realización y repack).** Sea T un bosque de colocación
factible (cada contenedor con una colocación disjunta de sus hijos
como bolas). Entonces:

**(a) Realización.** Existe una realización geométrica simultánea
de todo T: componer las isometrías por la ruta raíz-hoja (centro
absoluto de y = centro absoluto de su padre + posición relativa de
y). *Prueba*, inducción en profundidad con cuatro pasos exactos:
(i) la bola-agujero de y está dentro de la bola de y (r−w ≤ r);
(ii) los descendientes de y quedan confinados a la bola de y (hijo
en la bola-agujero, bola-agujero en la bola, recursivo) — hermanos
disjuntos como bolas ⟹ materiales de ramas distintas disjuntos;
(iii) el MATERIAL de y (el ánulo r−w..r) es disjunto del interior
de su bola-agujero ⟹ disjunto de todos sus descendientes;
(iv) las isometrías preservan distancias: la colocación relativa de
cada contenedor (condiciones de disyunción y contención, todas en
términos de distancias) se traslada sin romperse. ∎

**(b) Repack.** Sustituir en UN contenedor la colocación de sus
hijos por OTRA colocación disjunta cualquiera (mismas bolas; el
subárbol de cada hijo viaja rígido) produce otra realización válida
del MISMO bosque. La asignación, los objetivos N y A, y todas las
colas (ρ) son invariantes: son funciones del multiconjunto y del
bosque, no de las posiciones. *Prueba*: (a) con la nueva colocación
en ese contenedor y las mismas en el resto. ∎

**(c) Intercambio.** El testigo P′ del paso de intercambio puede
re-empaquetar cualquier contenedor libremente: la inducción de
thm:oblivious consume solo la asignación. Todos los recursos de las
campañas son instancias de (b): el pan repack de thm:DP, el
bolsillo espejo de F1e/F1f (re-colocar el par top-level diametral y
σ₂ al bolsillo), la fila de D_m (lem:row), las coronas de agujero
(ramas 1 y 2: re-colocar {x's, m, σ₂} en la bola-agujero), el trío
mural de R2b. ∎

## 3. Verificación

Bloque B: 332 bosques aleatorios (889 anillos, profundidad hasta 4,
anchuras 0.05–0.5): la composición raíz-hoja produce 0 violaciones
de material/contención (chequeo GLOBAL por pares: bolas disjuntas o
una dentro de la bola-agujero de la otra, más contención recursiva
en el padre). Bloque C: 162 repacks con movimiento real de un
contenedor aleatorio (la sartén o un anillo interior): 0
violaciones tras recomponer, asignación bit a bit invariante.
Bloque D: los consumidores como instancias numéricas (bolsillo
espejo, fila de D_m, corona de agujero con el criterio k ≤ 5).
Bloque E, controles: hermanos solapados se detectan (la hipótesis
de colocación disjunta es la que carga); mover un hijo SIN su padre
rompe (el repack mueve bolas con su interior, no interiores
sueltos); una bola mayor que su región no se coloca (el lema
transporta packabilidad, no crea espacio).

## 4. Consecuencia

El [ENUNCIADO] F2 desaparece de la lista de residuo: las pinzas de
bolsillo espejo y todos los repacks del programa quedan apoyados en
un lema probado desde la definición, no en una frase. El residuo
computacional del programa queda en: la dirección j de los cierres
de escala, los barridos G de R2b y la gap-dualidad F3, y los
dominios muestreados de las coronas acotadas.

## 5. Estatus

Exacto (teorema, prueba completa de definición): (a), (b), (c) —
los cuatro pasos de la inducción son triviales por separado y la
composición es mecánica; no hay maximización alguna. Numérico: el
bloque B/C es CONTROL de la prueba (una prueba de definición puede
verificarse por instancias sin asterisco: si la inducción fallara,
los bosques aleatorios lo delatarían), no un certificado con
dominio muestreado que haga de sup.
