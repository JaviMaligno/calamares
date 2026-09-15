# Agujeros independientes: colocación y umbral de área

Fecha: 2026-09-15. Continuación fuera de la v2 de referencia del día 14.

Estado: prueba escrita completa, siete certificados algebraicos compilados
en `lean/Calamares/VariableWidth.lean` y controles racionales exactos en
`code/grosor_variable.py`. Fable acepta V1, la captura de cola y V2;
sus precisiones editoriales están incorporadas. Véanse el dictamen
`../reviews/2026-09-15-fable-extras-review.md` y su respuesta.

## 1. Modelo y colocación

El aro i tiene radio exterior r_i y radio interior h_i, con
`r_1>...>r_n>0`, `0≤h_i<r_i`. Equivale a permitir grosores positivos
w_i distintos, con `h_i=max(0,r_i-w_i)`. Se admiten discos macizos.
Su área dividida por π es `a_i=r_i²-h_i²>0`. Los hijos de i se
empaquetan como bolas exteriores en su agujero de radio h_i; se
conserva el modelo de bosques y recolocación de hermanos del paper.

**V1.** Si `rho=max_i(sum_{j>i}r_j)/r_i≤1`, toda ejecución voraz
descendente produce el lex-máximo L, para cualquier contenedor
compacto K y en cualquier dimensión positiva.

**Prueba.** La clausura hacia abajo sigue siendo válida: al retirar
un aro, sus descendientes quedan dentro de su bola exterior y pueden
reparentarse. En el intercambio de `thm:oblivious`, el pivote m
viaja con su subárbol. Se trasladan los hijos inmediatos menores de
su destino u, con sus subárboles, a la bola exterior que m deja en v.
La suma de sus radios exteriores es a lo sumo la cola de m, que no
supera r_m, así que el lema de fila los aloja allí. Si v es un agujero,
la legalidad original de m certifica `r_m≤h_dueño(v)`; eso basta
para todos los trasladados. Los padres son mayores que m porque
`h_i<r_i`. El destino u admite m junto a los mayores bajo el certificado
de la ejecución. Ningún paso compara w_i con w_j. Se alinea el mayor
desacuerdo y se itera. ∎

La prueba de `prop:n3` tampoco necesita grosor común: al sustituir
r_2 por r_3 se usa `r_3<r_2≤h_1`. Por tanto la garantía para tres
aros en K arbitrario permanece válida. Las gemelas y los fallos de
cuatro aros de grosor uniforme son también ejemplos en este modelo.

V1 garantiza asimismo que L alcanza el máximo de toda suma
`sum v(r_i)` con v positiva, creciente y superaditiva; no se afirma
unicidad para esa clase, en particular si rho=1.
**No implica optimalidad de la
suma de a_i**: ahora esa área no es una función común del radio.

## 2. Captura de la cola

Sea `T_i=sum_{j>i}r_j`. Si i pertenece a L y `h_i≥T_i`, entonces
**todos los aros j>i pertenecen a L**.

En efecto, tome un testigo del prefijo lexicográfico hasta i.
Su agujero está vacío, pues aún no hay radios menores en el prefijo.
El lema de fila mete toda la cola como hijos de i. Esto da un testigo
de ese prefijo junto con todos los índices posteriores. La clausura
hacia abajo certifica cada admisión sucesiva del lex-máximo. Los
índices omitidos antes de i no se añaden. ∎

## 3. Garantía exacta para el área

**V2.** Fije `0<kappa<1`. Para cualquier inventario con agujeros
independientes, cualquier K compacto en el plano y `rho≤kappa`,
toda ejecución descendente satisface

`A_greedy ≥ c(kappa) A_opt`,
`c(kappa)=min(1, kappa^(-2)-1)`.

Para `kappa≤1/sqrt(2)`, el lex-máximo es el único conjunto óptimo
de área. Para `1/sqrt(2)<kappa<1`, la constante c(kappa) es la mejor
posible, incluso para dos aros en una sartén circular: es el ínfimo
de las razones con `A_opt>0`, y no se alcanza en esa franja de kappa.

**Prueba.** Por V1, el conjunto voraz es L. Compare L con cualquier
conjunto factible S distinto. El primer índice diferente i está en L.
Sea C el área normalizada de su prefijo común y B la de los aros
de S posteriores a i. Si `h_i≥T_i`, la captura de cola prueba S⊊L,
y por positividad `A(L)>A(S)`.

En caso contrario `0≤h_i<T_i≤kappa r_i`, y

`B≤sum_{j in S,j>i}r_j²≤T_i²`.

La segunda desigualdad usa radios positivos, la expansión del
cuadrado de una suma y la inclusión en la cola completa. Por ello

`a_i=r_i²-h_i² > r_i²-T_i²
                  ≥ (kappa^(-2)-1) T_i² ≥ c(kappa) B`.

Finalmente `A(L)≥C+a_i`, `A(S)=C+B`, `C≥0` y `0<c≤1` implican
`A(L)>c A(S)`. Para c=1 esto prueba optimalidad estricta frente a
todo S distinto; para c<1 se aplica al conjunto óptimo. Si S=L,
la garantía es inmediata. Todas las áreas anteriores se dividieron
por el mismo factor π. ∎

## 4. Optimalidad de la constante y del umbral

En una sartén de radio 1 use dos aros:

`r_1=1, h_1=kappa-epsilon; r_2=kappa, h_2=0`,
`0<epsilon<kappa<1`.

El primero llena la raíz por su bola exterior; el segundo no puede
ser su hermano ni anidar, pues `kappa>h_1`. El voraz coloca solo el
primero, de área normalizada `1-(kappa-epsilon)²`. El segundo cabe
solo y tiene área `kappa²`. No existe conjunto factible con ambos.
Además `rho=kappa` exactamente. Si `kappa>1/sqrt(2)`, elija

`epsilon<kappa-sqrt(1-kappa²)`.

Entonces el óptimo es el segundo aro, y

`A_greedy/A_opt = kappa^(-2)-1+2epsilon/kappa-epsilon²/kappa²
                 → kappa^(-2)-1`

desde arriba. Así el umbral universal de optimalidad de área es
**exactamente `1/sqrt(2)`**, incluido el extremo bueno, mientras
que la colocación sigue siendo irrelevante en toda la región rho≤1.
La restricción a grosores positivos se cumple: `w_1=1-kappa+epsilon>0`
y `w_2=kappa>0`.

Con solo superincrecencia estricta no hay factor positivo uniforme.
Para `0<e<1/4`, tome sartén `R=1+e`, radios exteriores `{1+e,1}`,
agujeros `{1-e,0}` y grosores `{2e,1}`. El voraz solo coloca el
primero, de área `4πe`, frente al óptimo π del segundo, y
`rho=1/(1+e)<1`. La razón `4e` tiende a cero.

Los discos macizos no son esenciales para el fenómeno: se puede
dar al segundo aro un agujero positivo arbitrariamente pequeño.
Las desigualdades estrictas persisten y el mismo ínfimo se aproxima.

## 5. Alcance y relación con cinco aros

El umbral de **colocación** no debe confundirse con V2. La nota
`cinco_aros.md` prueba la igualdad restringida `tau_(≤5,d)=phi`
para agujeros independientes en bolas de dimensión d≥2.
Ni esa afirmación ni V2 establecen el umbral global de colocación
para un número arbitrario de aros.

Lean verifica las desigualdades algebraicas de V2 y los certificados
de la familia. El bosque, la captura de cola y su interpretación
geométrica se prueban aquí por escrito. No se afirma una
formalización completa del algoritmo ni novedad bibliográfica.
