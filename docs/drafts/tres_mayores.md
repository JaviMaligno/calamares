# Cierre uniforme: los tres mayores determinan la capacidad local

Fecha: 2026-09-15. **Prueba escrita completa, aceptada en la segunda
revisión independiente de Fable, con aclaraciones incorporadas.**
El lema de empaquetamiento de discos cierra el intercambio para cualquier
inventario finito en el plano y demuestra tau=phi, usando la cota superior
ya probada en la v2. No utiliza una enumeración de tamaños. La versión
en inglés está en `paper/golden_threshold.tex`; la v2 de referencia se
conserva. Lean formaliza la capa algebraica, no toda la geometría.

Escriba phi=(1+sqrt(5))/2 y
`beta(a,b)=ab(a+b)/(a²+ab+b²)`.

## 1. Dos discos desiguales en un mismo hueco

**Lema A.** Sean a≥b>0. Coloque los discos a,b en el disco de radio
R=a+b, con centros (-b,0),(a,0). Si r,s>0 cumplen

`r≤beta(a,b)`, `s≤beta(a,b)`, `r+s≤b`,

los dos discos r,s caben simultáneamente en el semiplano superior,
evitando a,b. El bolsillo inferior de radio beta queda libre.

Prueba. Para un disco x≤beta, los ángulos posibles de su centro cuando
es tangente a la pared, medidos desde el eje horizontal positivo, forman
el intervalo

`[2 asin sqrt(bx/(a(R−x))), pi−2 asin sqrt(ax/(b(R−x)))]`.

Las dos cotas vienen de la ley de cosenos respecto a b y a. El intervalo
no es vacío exactamente cuando

`ax/(b(R−x)) + bx/(a(R−x)) ≤ 1`,

equivalente a x≤beta. En efecto, para X,Y∈[0,1],
`asin X+asin Y≤pi/2` equivale a `X²+Y²≤1`.

Ponga r en el extremo inferior de su intervalo y s en el extremo
superior del suyo. Defina

`A²=as/(b(R−s))`, `B²=br/(a(R−r))`, con A,B≥0.

La separación angular entre esos centros es
`pi−2 asin A−2 asin B`. La separación mínima exigida por los discos
r,s es `2 asin(AB)`, pues `A²B²=rs/((R−r)(R−s))`.
Por tanto basta demostrar

`A²+B²+3A²B²≤1`.                                        (A1)

Esta desigualdad implica A²+B²≤1 y
`sqrt(1−A²)sqrt(1−B²)≥2AB`; así,
`cos(asin A+asin B)≥AB` y
`asin A+asin B+asin(AB)≤pi/2`.

Multiplicando (A1) por el denominador positivo ab(R−r)(R−s), el
margen es exactamente

`R²(ab−br−as)+(a−b)²rs`

`=R²[a(b−r−s)+(a−b)r]+(a−b)²rs ≥ 0`.

Esto prueba la disyunción. Ambos centros están en el semiplano superior.
Los discos completos también: el diámetro del contenedor está cubierto
por los discos a,b, de modo que un disco disjunto de ellos no puede
atravesarlo. El bolsillo inferior tiene centro de ordenada −2beta y
radio beta; por tanto permanece disjunto de ambos discos nuevos.
Los casos r=0 o s=0 se resuelven omitiendo el disco de radio cero.

## 2. Una colocación mínima de tres discos

**Lema B.** Sean a≥b≥c>0 y c>beta(a,b). En el menor disco contenedor
de esos tres discos hay una colocación en la que los tres discos son
mutuamente tangentes y cada uno toca la pared. Si sus curvaturas son
`A=1/a`, `B=1/b`, `C=1/c`, y `t=sqrt(AB+AC+BC)`, el radio mínimo R0
cumple `1/R0=2t−A−B−C`.

Prueba. El radio mínimo existe por compacidad; una fila aporta una
cota superior y los centros permanecen en un conjunto acotado.
Primero, cualquier colocación de tres discos puede hacerse tangente
a la pared: para mover uno con centro x, elija una dirección no nula
v con `(x−x_j)·v≥0` para los otros dos centros. Dos semiplanos cerrados
por el origen siempre tienen una dirección común no nula en el plano.
Al mover x a lo largo de ese rayo, las distancias a los otros centros
no disminuyen. Deténgase al alcanzar la pared. Repita para los otros
discos, dejando fijos los ya situados.

Para tres discos tangentes a la pared y con ri+rj≤R, sea theta_ij∈[0,pi]
el ángulo mínimo de separación dado por la ley de cosenos. Existen
tres posiciones si y solo si

`theta_ab+theta_ac+theta_bc≤2pi`.

La necesidad sigue sumando los tres huecos angulares dirigidos de una
colocación; cada uno es al menos el ángulo mínimo de ese par. Para la
suficiencia, elija tres huecos en `[theta_ij,pi]` que sumen 2pi: existen
porque las sumas de los extremos son, respectivamente, ≤2pi y 3pi.
Así, el ángulo menor de cada par coincide con su hueco dirigido.

R0≥a+b por la condición necesaria de dos discos. Si R0=a+b, estos dos
discos están forzosamente diametrales. Lleve c a la pared por el
procedimiento anterior, dejando a,b fijos; entonces sí se aplica el
intervalo angular del primer lema y se obtiene c≤beta, contradicción.
Luego R0>a+b, y todos los
ángulos mínimos están en (0,pi) y son continuos en R cerca de R0.
Su suma debe ser 2pi: una suma menor permitiría reducir R. Tomando
esos tres huecos exactos, todos los pares son tangentes. La ecuación
de Descartes para las curvaturas A,B,C,−1/R0 da la fórmula indicada;
la otra raíz tiene 1/R0<0 y queda excluida.

## 3. El hueco opuesto compensa el crecimiento del tercero

**Lema C.** En la colocación del lema B existe un cuarto disco disjunto,
en el otro hueco curvilíneo delimitado por a,b y la pared, de radio
d>0 tal que

`c+d≥2beta(a,b)`.                                        (C1)

Prueba. Ponga `S=A+B`, `P=AB`, `Q=S²−P` y `t²=P+SC`.
La hipótesis c>beta equivale a `SC<Q`, por lo que t<S.
Primero justifique la existencia geométrica de los dos incírculos.
Invierta respecto al punto de tangencia de a,b. Sus circunferencias
se convierten en dos rectas paralelas; sus interiores, en los dos
semiplanos exteriores a una franja. El punto de inversión está
estrictamente dentro del contenedor, de modo que el interior de este
se transforma en el exterior de un círculo tangente a ambas rectas,
contenido en la franja. Su radio es la semianchura de la franja.

Todo disco admisible tangente a ambas rectas tiene ese mismo radio y
su centro está en la recta media. Para ser además tangente al círculo
imagen de la pared, su centro debe estar en una de las dos posiciones
de esa recta a distancia dos veces ese radio de su centro. Son dos
discos con interiores disjuntos, separados por el círculo de la pared.
El centro de inversión está dentro del círculo imagen de la pared,
por lo que no pertenece a ninguno de esos discos; sus imágenes inversas
son discos acotados, no exteriores de discos ni semiplanos.
Al invertir de vuelta se obtienen dos discos contenidos en el contenedor,
externamente tangentes a a,b, internamente tangentes a la pared y
disjuntos entre sí. Uno es c; llame d al otro. Los dos huecos se
entienden como componentes abiertas del espacio libre, no como
semiplanos definidos por la recta de centros.

La fórmula clásica de reflexión de Descartes para estas dos soluciones
orientadas (referenciada en §6) da que sus curvaturas suman
`2(A+B−1/R0)`. Por tanto el segundo disco tiene curvatura

`D=2(A+B−1/R0)−C=4S+C−4t > C > 0`.

Las raíces son distintas porque t<S, y la inversión ha mostrado
exactamente dos discos admisibles; por ello la reflexión identifica d.
Su radio d=1/D es menor que c≤b. La contención y la disyunción ya
están probadas por la inversión, sin inferir la existencia del disco
de una raíz algebraica. La identidad de altura certificada en Lean
solo comprueba que un disco x≤b tangente a a,b no cruza su recta de
centros; no se usa como prueba de que c,d estén en lados distintos.

Para la cota de radios basta la identidad

`Q(C+D)−2SCD = 2(S−t)²(2S+2t−C) ≥ 0`.                  (C2)

Se obtiene sustituyendo D=4S+C−4t y t²=P+SC. El último factor es
positivo: SC<Q<S² implica C<S. Divida por QCD>0 y use
`beta=S/Q`; resulta `1/C+1/D≥2S/Q`, que es (C1).

## 4. Teorema local para cualquier longitud finita

**Teorema T3.** Sean `a>b≥c≥r4≥...≥rn>0`, n≥3, con todas las colas
de esta lista acotadas por phi veces el radio correspondiente. La lista
completa cabe en un disco de radio R si y solo si caben a,b,c.
Los menores pueden tener radios iguales. La condición a>b basta para
usar directamente el balance áureo ya certificado en FourRing.

La necesidad es inmediata. Para la suficiencia, sea U la suma de todos
los posteriores a c. Las cotas de a,b y `tail_le_double_pocket` dan

`c+U≤2beta(a,b)`.                                        (T1)

Si c>beta, coloque a,b,c en su contenedor mínimo R0≤R. Por el lema C,
su hueco opuesto tiene radio d≥2beta−c≥U. Toda la cola cabe allí por
fila, sin cambiar los tres discos mayores.

Si c≤beta, coloque a,b diametralmente en un disco de radio a+b≤R y c
en el bolsillo inferior. Si la cola no es vacía, llame e a su primer
radio y V a la suma de los posteriores. El lema de dos colas da

`U=e+V≤b`, `V≤c`, y por el orden `e≤c`.

La primera desigualdad usa las colas consecutivas de b,c; la segunda,
las de c,e. El lema A aloja los discos auxiliares e,V en el hueco
superior porque ambos son ≤c≤beta y su suma es ≤b. Sustituya el disco
auxiliar V por la fila de sus piezas. Si V=0 se omite. El inventario
completo queda colocado. Se han agrupado piezas solo para construir
posiciones; no se ha sustituido el inventario en una afirmación sobre
rho, los agujeros o la ejecución voraz.

## 5. Consecuencia para el intercambio

Se usa el voraz del modelo de bosques: conserva los padres ya elegidos,
pero permite recolocar hermanos dentro de cada contenedor. Solo rechaza
cuando ningún contenedor hace factible el bosque extendido, no por
fallar unas coordenadas particulares ya dibujadas.

Considere el testigo bloqueado de `intercambio_uniforme.md`, con pivote
m, cola total T>m y resto posterior al siguiente aro de suma ≤m.
Si un contenedor tiene k≥3 hijos mayores `a1>...>ak>m`, forme la lista
auxiliar de discos

`a1,...,ak,m,m`.

Cada cola en ai está acotada por la cola original correspondiente,
pues `2m<m+T`. Las dos últimas razones son 1 y 0. Por tanto esta
lista satisface las cotas phi; sus tres mayores ya caben en el
contenedor. T3 produce dos plazas m junto a todos sus hijos mayores.

Escriba w para ese contenedor, u para el destino del pivote en F y v
para su origen en P. Escriba p para el siguiente aro y U para la suma
de los posteriores, con p<m y U≤m. El criterio de dos plazas es:

- Si w≠u, coloque p en una plaza y toda la cola U en la otra, por
  fila. Coloque m en u con el certificado del prefijo de F junto a
  sus hijos mayores. Esto incluye w=v: su colocación se reconstruye
  y no se reserva en ella una tercera plaza para m.
- Si w=u, coloque m y p en las dos plazas. Toda la cola U cabe por
  fila en la bola exterior que m deja en v, conservando allí la
  colocación de los hijos mayores del testigo P.

En los otros contenedores se conservan colocaciones de los mayores.
Todos los menores se reconstruyen como hojas. Los padres de los
mayores se conservan; sus empaquetamientos interiores se trasladan
con cada propietario. Los propietarios de u,v,w tienen radio mayor
que m, así que el ensamblaje no crea ciclos, incluso si alguno es
antecesor de otro. Esto prueba explícitamente el criterio de dos
plazas llamado R0 en `nucleo_uniforme.md`, sin depender de esa nota.

Un contenedor de grado 2 ya activa C2. Si no hay ninguno de grado ≥2,
el árbol de mayores, con la raíz virtual, es una cadena. Solo tiene
un contenedor de grado cero; como u≠v, uno de ellos tiene grado 1 y
activa C1. En todos los casos se puede aumentar el prefijo coincidente,
contradiciendo un bloqueo. La inducción por longitud de prefijo termina
para cualquier inventario finito.

**Los lemas A–C y su aplicación prueban que**
rho≤phi impide una primera omisión del lex-máximo en el disco. Junto
con la familia de fallos con rho descendiendo a phi desde arriba, ya
incluida en la v2, se obtiene tau=phi, con ínfimo no alcanzado.
La construcción no usa grosor común; en el plano también cubre
agujeros independientes. La extensión dimensional se auditará por
separado antes de afirmarla.

## 6. Revisión y alcance de la formalización

La primera revisión de Fable verifica A, el argumento de B, el álgebra
de C y la construcción T3, y considera correcta en el fondo la
aplicación global. Pide justificar la existencia y disyunción del
segundo incírculo, explicitar el uso de pared en B y escribir el
reparto de plazas en §5. Las tres precisiones están incorporadas.
El primer dictamen íntegro está en
`../reviews/2026-09-15-fable-three-core-review.md`.

La segunda revisión acepta la cadena completa, incluyendo presión,
partición, C1/C2, prefijo máximo y ensamblaje de padres, sin encontrar
huecos matemáticos reales. Sus aclaraciones sobre la semántica del voraz,
el retorno de la inversión y la identificación de la segunda raíz están
incorporadas arriba. Dictamen y respuesta en
`../reviews/2026-09-15-fable-three-core-final-review.md` y
`../reviews/2026-09-15-fable-three-core-final-response.md`.

La ecuación orientada y la operación que cambia un círculo tangente
por el otro son clásicas; véase Graham, Lagarias, Mallows, Wilks y Yan,
[Apollonian Circle Packings: Geometry and Group Theory I](https://arxiv.org/pdf/math/0010298),
§3.3, ecuación (3.25). Aquí se da además el argumento de inversión
para identificar los discos admisibles. No se afirma novedad de
Descartes ni de esa operación.

Lean certifica las identidades y sus signos; no formaliza la inversión,
la existencia de círculos, la colocación angular ni el bosque.
`opposite_height_positive` es una comprobación auxiliar del signo de
altura, no una prueba de disyunción entre los dos incírculos.
