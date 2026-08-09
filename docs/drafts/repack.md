# F2: el lema de realización y repack

Estado: DRAFT con pruebas (2026-08-09), ADVERSARIADO (acta en
VEREDICTOS.md, misma fecha: CONFIRMADO CON CORRECCIONES; (a) y (b)
resistieron todos los sondeos — tangencias exactas, sólidos,
micro-agujeros, rotaciones/reflexiones, equivalencia del chequeo —;
(c) reescrito). Script: `code/repack.py` (5/5). Cierra el [ENUNCIADO] F2 — la legalidad del
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
de todo T con materiales de INTERIORES disjuntos: componer las
traslaciones por la ruta raíz-hoja (centro absoluto de y = centro
absoluto de su padre + posición relativa de y). *Prueba*, inducción
en profundidad con HIPÓTESIS INDUCTIVA explícita (ronda hostil):
para todo anillo y, material(subárbol(y)) ⊂ bola(y) y
material(descendientes estrictos de y) ⊂ bola-agujero(y). Pasos:
(i) la bola-agujero de y está dentro de la bola de y (r−w ≤ r);
(ii) con la hipótesis en los hijos, los descendientes de y quedan
confinados a su bola — hermanos de interiores disjuntos como bolas
⟹ materiales de ramas distintas de interiores disjuntos (cubre
hermanos, primos y tío/sobrino a niveles distintos);
(iii) el MATERIAL de y (el ánulo r−w..r) tiene interior disjunto
del interior de su bola-agujero ⟹ del de todos sus descendientes
(cubre ancestro/descendiente a cualquier profundidad);
(iv) las traslaciones preservan distancias: la colocación relativa
de cada contenedor (disyunción y contención, todas condiciones en
distancias) se transporta sin romperse. Las traslaciones BASTAN:
cualquier isometría de una colocación por contenedor (rotar, como
las colocaciones murales; reflejar, como el bolsillo espejo) es
simplemente OTRA colocación por contenedor — las regiones son
rotacionalmente simétricas. Los anillos sólidos (r ≤ w: bola-agujero
de radio 0, sin hijos posibles) son hojas triviales de la
inducción. El argumento vale verbatim con la sartén K compacta
arbitraria y en dimensión d (solo el contenedor raíz cambia; todo
lo demás vive en bolas) — como reclama thm:oblivious. ∎

**(b) Repack.** Sustituir en UN contenedor la colocación de sus
hijos por OTRA colocación de interiores disjuntos cualquiera
(mismas bolas; el subárbol de cada hijo viaja rígido) produce otra
realización válida del MISMO bosque. Invariantes, con la finura
correcta (ronda hostil): ρ es función SOLO del multiconjunto de
radios de la instancia (invariante bajo todo, incluso
re-asignación); N y A son funciones del CONJUNTO colocado S
(invariantes bajo (b) y bajo cualquier re-asignación que conserve
S); la asignación es invariante bajo (b) por definición. *Prueba*:
(a) con la nueva colocación en ese contenedor y las mismas en el
resto. ∎

**(c) El testigo del intercambio (reescrito por la ronda hostil).**
El testigo P′ del paso de intercambio se especifica por DOS datos:
(1) una asignación bosque-factible — que en general DIFIERE de la
de P: m se muda de v a u, los menores se recolocan — y (2) una
colocación factible por cada contenedor tocado, aportada por el
recurso que corresponda: heredada de P, certificada por F (el
destino de m), o construida (fila de D_m por lem:row, corona
acotada, bolsillo espejo, inserción por sombras). El lema (a)
COMPONE esas colocaciones en una realización global; (b) es el caso
particular en que la asignación no cambia (pan repack de thm:DP,
bolsillo espejo F1e/F1f cuando re-colocan el mismo conjunto
top-level). La legalidad de una asignación NUEVA no la da este
lema: la carga cada certificado por contenedor — este lema da el
paso de composición que los junta. Deslinde con el lema de
inserción: las posiciones de P son EXISTENCIALES — se toma una
realización cualquiera y se modifica contenedor a contenedor;
algunas colocaciones nuevas se construyen POSICIONALMENTE sobre esa
realización (la bola vacante de m, la inserción mural por sombras
«sin mover nada») y otras por certificado de conjunto (fila,
corona, criterio k ≤ 5): son recursos complementarios que
desembocan ambos en (a). ∎

## 3. Verificación

Bloque B: bosques aleatorios (profundidad hasta 4, anchuras
0.05–0.5, SÓLIDOS incluidos — el filtro 3w de la v1 los excluía,
reparado): la composición raíz-hoja produce 0 violaciones de
material/contención. El chequeo por pares (bolas de interiores
disjuntos o una dentro de la bola-agujero de la otra) es
EQUIVALENTE a la disyunción de interiores de materiales — no más
fuerte: el acta lo probó con el argumento del punto extremo (una
bola que sobresale de la bola-agujero sin salir de la bola exterior
mete su circunferencia en el interior del ánulo) y lo confirmó
contra un criterio analítico por arcos (3 000 pares, 0
discrepancias): «0 violaciones» prueba exactamente lo que dice.
Sub-bloque DETERMINISTA (exigido por el acta): hermanos tangentes
exactos, fila tangente en el agujero, sólidos r ≤ w tangentes
internos, micro-margen 0.05, agujero llenado exacto, y
rotación 45°/reflexión de las colocaciones de dos contenedores — 0
violaciones. Bloque C: repacks con movimiento real de un contenedor
aleatorio: 0 violaciones tras recomponer, asignación invariante
(módulo permutación de radios iguales y redondeo 10⁻⁹ — la noción
correcta con anillos indistinguibles). Bloque D: consumidores como
instancias ILUSTRATIVAS (el peso probatorio está en B/C y en el
lema). Bloque E, controles: hermanos solapados se detectan; mover
un hijo SIN su padre rompe (el repack mueve bolas con su interior);
una bola mayor que su región no se coloca (el lema transporta
packabilidad, no crea espacio).

## 4. Consecuencia

El [ENUNCIADO] F2 desaparece de la lista de residuo: las pinzas de
bolsillo espejo y todos los repacks del programa quedan apoyados en
un lema probado desde la definición, no en una frase. El residuo
computacional del programa queda en: la dirección j de los cierres
de escala, los barridos G de R2b y la gap-dualidad F3, y los
dominios muestreados de las coronas acotadas.

## 5. Estatus

Exacto (teorema, prueba completa de definición): (a) con su
hipótesis inductiva explícita, (b), y (c) como composición — la
legalidad de las asignaciones nuevas la cargan los certificados por
contenedor de cada campaña (ya adversariados cada uno), y este lema
aporta el paso de composición que faltaba como [ENUNCIADO]. No hay
maximización alguna. Numérico: los bloques B/C son CONTROL de la
prueba (una prueba de definición puede verificarse por instancias
sin asterisco: si la inducción fallara, los bosques aleatorios y
las tangencias exactas lo delatarían), no un certificado con
dominio muestreado que haga de sup.
