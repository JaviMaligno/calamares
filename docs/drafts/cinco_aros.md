# Umbral áureo exacto hasta cinco aros

Fecha: 2026-09-15. Continuación de `thm:fourfloor` de la v2.

Estado: prueba escrita completa y 11 certificados algebraicos/cartesianos
compilados en `lean/Calamares/FiveRing.lean`. Fable acepta la cota inferior
y pide dos precisiones menores en la cota superior, incorporadas abajo.
Dictamen y respuesta: `../reviews/2026-09-15-fable-extras-review.md`
y `../reviews/2026-09-15-fable-extras-response.md`.

**Teorema F5.** En una sartén esférica de dimensión d≥2, con radios
exteriores estrictamente decrecientes y agujeros independientes
`0≤h_i<r_i`, toda ejecución voraz sobre como máximo cinco aros
coloca el lex-máximo si `rho≤phi`. En consecuencia

`tau_(≤5,d)=phi`, con ínfimo no alcanzado.

Incluye el modelo de grosor común. La cota superior ya viene de la
familia áurea de cuatro aros del paper; solo hay que probar la inferior.

## 1. Dos hechos de geometría y dos presiones

Para dos bolas de radios a,b en una bola de radio a+b, el par es
diametral. En un plano de sus centros, los dos bolsillos simétricos
tangentes a ambas bolas y a la pared tienen radio

`beta(a,b)=ab(a+b)/(a²+ab+b²)`.

El denominador es positivo y mayor que ab, por lo que
`0<beta(a,b)<a+b`; así el radio interior de tangencia a la pared
`a+b-beta` es positivo.

Son disjuntos entre sí y de las bolas a,b. Para comprobarlo sin
invocar un oráculo, use centros `(-b,0)` y `(a,0)` para el par.
Los centros de los bolsillos son

`x=(a-b)(a+b)²/(a²+ab+b²)`, `y=±2 beta(a,b)`.

Satisfacen `x²+y²=(a+b-beta)²`,
`(x+b)²+y²=(a+beta)²` y
`(x-a)²+y²=(b+beta)²`. La distancia entre ellos es `4 beta`,
mayor que `2 beta`. Reducir cualquiera de sus radios, conservando
el centro, mantiene la factibilidad. La construcción cabe también
en cualquier bola mayor, y se embebe en toda dimensión d≥2.

**P1 (un ocupante).** Sea a>m>p≥q>0, con
`rho m≥p+q` y `rho a≥m+p+q`. Si rho≤phi, entonces
`q≤beta(a,m)`.

En efecto, normalice m=1. Si q>g(a), donde `g(a)=beta(a,1)`,
también p>g(a), y se tienen las dos presiones
`rho>2g(a)`, `rho a>1+2g(a)`. Las factorizaciones y
`golden_balance` de `FourRing.lean` dan rho>phi. Es la misma
álgebra revisada de `thm:fourfloor`, sin ninguna hipótesis de anchura.
P1 puede aplicarse ignorando otros radios de las colas.

**P2 (dos aros mayores en la raíz).** Sean A>B>m>p≥q>0,
`p+q>m` y rho≤phi para este inventario (o uno que lo contenga).
Entonces `beta(A,B)>m`.

Normalice m=1. Las colas dan `phi B≥1+p+q>2` y
`phi A≥B+1+p+q>B+2`, de donde
`B>2/phi=2phi-2=:b0` y `A>2`.
Con `b0²+2b0=4`, el numerador de beta(A,B)−1 se escribe

`AB(A+B)-(A²+AB+B²)
 = (A-2)²(B-1)+(A-2)(B-1)(B+4)+(B-b0)(B+b0+2)>0`.

Todos los factores pertinentes son positivos porque b0>1.
Esto prueba P2. Nótese que la construcción usa dos bolsillos
disjuntos, no una equivalencia de factibilidad de cuatro hermanos
entre dimensiones.

## 2. Reducción al intercambio de un prefijo

Considérese el primer índice donde la ejecución difiere del
lex-máximo. Solo puede omitir un aro que era factible con su
conjunto admitido G. Restrinja el inventario a G y ese aro: los
omitidos anteriores no dejaron contenedores ni ocupantes, y el
inventario restringido, de N≤5 aros, es factible. Su rho no aumenta
al suprimir piezas. Sea F el bosque de G y P un testigo completo.

Se alinea iterativamente el mayor aro m cuyo padre difiere entre
F y P. Los padres y asignaciones de todos los mayores ya coinciden;
el certificado del voraz admite m en su destino u junto a esos
mayores. Su padre en P es v≠u. Si no hay desacuerdo, P admite el
último aro en F, contradicción.

Sea S el conjunto de hijos inmediatos menores que m que P tiene
en u. Si `sum_{s in S}r_s≤m`, el intercambio del lema de fila
los lleva, con sus subárboles, a la bola exterior que m deja en v;
m viaja con su propio subárbol a u. Esto alinea m. Los padres
son mayores y las capacidades de los agujeros no cambian.

En particular, un desacuerdo con a lo sumo un aro menor nunca
bloquea. Con N≤5, solo quedan el segundo y el tercer aro. Si
el desacuerdo en el tercero bloquea, necesariamente N=5 y hay
exactamente dos aros menores, con `S={p,q}`, `p+q>m`.
Ambos son hojas y no hay otros aros
menores que puedan obstruir las recolocaciones siguientes.
En particular, en ese testigo m tiene el agujero vacío: sus dos
posibles descendientes ya son hijos inmediatos de u, y u≠m.

## 3. Desacuerdo en el segundo aro

Escriba A>m y los aros restantes p>q>t cuando estén presentes.
Los únicos padres de m son la raíz y A. El desacuerdo implica
**ambas** condiciones: `R≥A+m` y `h_A≥m`. Con menos de dos
aros menores se aplica directamente el intercambio anterior.
En otro caso, P1 da `q≤beta(A,m)` y `t<q≤beta(A,m)` si hay t.

Construya el par diametral fantasma `{A,m}` y sus dos bolsillos:

- Si F pone m en la raíz, deje allí A,m, ponga p en el agujero
  de A (p<m≤h_A), y q,t en los dos bolsillos.
- Si F anida m en A, ponga m en su agujero, p en la bola exterior
  reservada por el m fantasma y q,t en los dos bolsillos. Quite
  el m fantasma: los hijos de raíz son A,p,q,t.

Si t no existe se omite su bolsillo. Todas las piezas menores se
pueden convertir en hojas, pues ya tienen un lugar individual
factible; no se impone conservar sus padres anteriores. Así se
obtiene un testigo completo que coincide en A y m con F. Luego
se prosigue la alineación, sin exigir coincidencia todavía en p.

Este argumento cubre también N=4. Para el subcaso de grosor común
en que el voraz anida m en A, basta aquí excluir rho≤phi; la cota
más fuerte rho>T que obtiene `thm:fourfloor` sigue siendo compatible.

## 4. Desacuerdo en el tercer aro

Escriba `A>B>m>p>q>0`. A y B tienen los mismos padres en F y P.
Por §2 solo queda `S={p,q}` con p+q>m.

### 4.1. A y B son hijos de raíz

Se tiene R≥A+B. Por P2 los dos bolsillos del par A,B tienen
radio mayor que m.

- Si u es la raíz, coloque m,p en esos bolsillos y q en la bola
  que m deja dentro de v. Aquí v es un agujero de A o B.
- Si u es un agujero de A o B, coloque p,q en los bolsillos y
  m en u, cuya admisión F certificó. A y B permanecen en la raíz.

En ambos casos están colocadas las cinco piezas, los mayores
siguen alineados y m tiene el padre prescrito por F.

### 4.2. B está anidado en A

Los posibles destinos de m son exactamente raíz, agujero de A y
agujero de B. Estos casos agotan todas las parejas ordenadas u≠v:

| Destino u | Construcción que alinea m |
|---|---|
| Raíz | F certifica el par A,m, luego R≥A+m. Por P1, q≤beta(A,m). Coloque A,m,q mediante el par y un bolsillo, y p dentro de la bola que m deja en v. B continúa en A. |
| Agujero de A | F certifica B,m como hermanos, luego h_A≥B+m. Por P1, q≤beta(B,m). Empaque B,m,q allí usando el bolsillo; coloque p en la bola que m deja en v. v es raíz o agujero de B. |
| Agujero de B, v=agujero de A | P certifica B,m como hermanos en A, así que h_A≥B+m. Use dentro de A el par fantasma B,m: p ocupa la bola del m fantasma y q un bolsillo, posible por P1. El m real se anida en B, como certificó F. |
| Agujero de B, v=raíz | P certifica A,m en la raíz, luego R≥A+m. Use el par fantasma A,m en la raíz, con p en la bola del m fantasma y q en un bolsillo (P1). Anide m en B y conserve B en A. |

La recolocación de B puede transportar su agujero y los hijos recién
reasignados: los empaquetamientos son locales y se ensamblan por
traslaciones, conforme al modelo del paper. Ninguna fila exige
igualdad entre grosores, ni permite interpenetración de hermanos.

## 5. Conclusión y alcance

Cada paso alinea el mayor desacuerdo conservando todas las piezas.
Tras finitos pasos el testigo coincide con F en todo G y muestra
un contenedor que admite el aro omitido: contradicción. Todo fallo
con N≤5 tiene por tanto rho>phi.

La familia áurea de cuatro aros da el ínfimo opuesto para N≤5,
en todas las dimensiones d≥2, con grosor común. El testigo plano se
embebe en cualquier d≥2. También persiste el fallo: el par de raíz
`{phi,1}` en radio phi+1 es diametral por igualdad en la desigualdad
triangular, en cualquier dimensión. Para una tercera bola, las distancias
al centro de la sartén y a los dos centros del par solo dependen de
la coordenada sobre ese eje y la distancia al eje. Se conserva toda
restricción trasladando el centro al plano que contiene el eje y ese
centro (si es colineal, a cualquier plano que contenga el eje).
Por `prop:S5` en ese plano, el radio de una tercera bola no puede
superar beta(phi,1)=phi/2. Las otras exclusiones de la familia solo
involucran una o dos bolas y son independientes de la dimensión.

El ínfimo no se alcanza. Para obtener inventarios de **exactamente
cinco** aros, añada a esa familia un aro de radio delta>0 en el
agujero vacío del aro de radio 1 del testigo, cuya capacidad es 1-w.
Su grosor puede seguir
siendo el común (tome `delta<min(w,1-w,s_2)`, y será un disco).
El primer fallo persiste, pues el quinto aro se procesa después.
Si rho_4 era el valor anterior, `rho_5≤rho_4+delta/s_2`:
cada cola antigua crece en delta y su divisor es al menos s_2;
la cola del quinto es cero. Elija delta tendiendo a cero junto con
el parámetro de la familia áurea. El testigo
completo contiene cinco aros. Con agujeros independientes también
puede elegirse que el quinto tenga agujero positivo.

No se afirma `tau=phi` para inventarios arbitrarios. La continuación
local `particion_bolsillos.md`, escrita durante esta revisión y fuera
de su envío, usa grupos de piezas en cada bolsillo y extiende la
alineación del segundo y tercer aro a cualquier inventario finito.
Reduce seis aros al desacuerdo en el cuarto con los tres mayores
en raíz, que sigue pendiente. Esa continuación tiene tres certificados
Lean adicionales, pero aún no revisión externa.

Dependencias: modelo y lema de fila del paper, fórmula explícita de
los bolsillos, las identidades P1/P2 y la familia áurea de v2. No se
usan los cierres computacionales históricos del programa universal.
La clasificación de bosques sigue escrita; Lean verifica los
certificados algebraicos y cartesianos indicados en su módulo.
