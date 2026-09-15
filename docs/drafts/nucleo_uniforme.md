# Núcleo estructural del intercambio uniforme

**Nota histórica:** el cierre posterior de `tres_mayores.md` demuestra
tau=phi sin usar esta cota estructural. Esta reducción se conserva con
su estado original, sin dictamen externo; no es una premisa del cierre.

Fecha: 2026-09-15. Modelo: discos en el plano y aros de grosor común
w≥0, con radios exteriores distintos y positivos. El inventario es
finito, de tamaño arbitrario, y rho≤phi. Se conserva la convención de
agujero de radio max(r−w,0).

Esta nota reduce el intercambio pendiente a una familia de bosques de
mayores con complejidad acotada. **No demuestra tau=phi.** La geometría
y el recuento tienen prueba escrita local; Lean certifica las
desigualdades indicadas en §8. No hay revisión externa de esta nota.

## 1. Situación de partida y dos plazas libres

Use la reducción de `intercambio_uniforme.md`: P es un testigo completo
con el mayor prefijo posible de padres coincidentes con el voraz F.
El primer desacuerdo tiene radio m; su destino en F es u y su origen
en P es v, con u≠v. Los padres de todos los aros mayores que m ya
coinciden. El siguiente radio es p<m y los posteriores suman U≤m.
Escriba T=p+U. Si T≤m, el intercambio de fila alinea m. Por tanto,
un testigo que siga bloqueado cumple T>m.

El **árbol de mayores** contiene solo los aros de radio mayor que m y
la raíz virtual correspondiente a la sartén. El grado de un contenedor
es el número de sus hijos inmediatos en ese árbol. Los contenedores
u y v son la raíz o agujeros de aros de ese árbol. Todas las colocaciones
locales de los mayores pueden reconstruirse, conservando sus padres.

**Criterio R0.** Si algún contenedor z admite simultáneamente a todos
sus hijos mayores y dos discos adicionales de radio m, se puede alinear
el pivote, con cualquier número finito de menores.

- Si z≠u, coloque p en una de esas plazas y toda la cola posterior a p
  en la otra, por fila y U≤m. Coloque m en u usando el prefijo de F.
- Si z=u, coloque m en una plaza y p en la otra. Coloque toda la cola
  posterior a p, por fila, en la bola exterior que m deja libre en v,
  conservando allí la colocación de los hijos mayores del testigo P.

Todos los menores se reconstruyen como hojas. En los demás contenedores
se conservan los empaquetamientos locales de los mayores. Si uno de
u,v,z es antecesor de otro, se traslada el empaquetamiento interior con
su propietario. Los propietarios tienen radio mayor que m, por lo que
no se crea ningún ciclo. El nuevo testigo coincide con F hasta m,
contradiciendo la elección de P.

Así, en lo que sigue, un intercambio **bloqueado** significa uno que
no se puede alinear. En particular, en él fallan R0 y los criterios C1/C2
de `particion_bolsillos.md`. No se presume que tal intercambio exista.

## 2. Criterio de área para conservar todos los ocupantes mayores

Sea un disco contenedor de radio R≥m con una colocación factible fija de
k discos mayores, de radios a_1,...,a_k. Para introducir un disco de
radio m, su centro debe pertenecer al disco concéntrico de radio R−m.
El disco cerrado de radio a_i+m alrededor del centro del ocupante i
es una región prohibida para el nuevo centro. Excluir también las
tangencias es más restrictivo de lo necesario, pero resulta conveniente.

Si

`(R−m)² > sum_i (a_i+m)² + 4m²`,                         (1)

el disco de centros posibles tiene más área que la suma de todas las
regiones prohibidas, incluso añadiendo un disco de radio 2m.
La subaditividad finita del área garantiza un primer centro fuera de
las regiones de los ocupantes. Añada el disco prohibido de radio 2m
alrededor de ese primer centro. La misma desigualdad garantiza un
segundo centro fuera de todas las regiones. Los dos discos nuevos son
disjuntos entre sí, están contenidos y evitan a todos los ocupantes.

El argumento vale **para cualquier colocación fija** de los ocupantes.
Se suman áreas de discos prohibidos completos, aunque parte de ellas
quede fuera del dominio de centros, lo que solo empeora la cota.
No se infiere una plaza libre del mero déficit de área ocupada.

## 3. Un segundo hijo de radio al menos 9m activa R0

Sean a=a_1>b=a_2>...>a_k>m los hijos mayores de un contenedor, k≥2.
Ponga `C=sum_{i≥3}a_i` y `Q=sum_{i≥3}a_i²`; las sumas vacías son cero.
La factibilidad de los dos primeros obliga a `R≥a+b`. Además `Q≤bC`.

Como phi<5/3 y las colas de a y b contienen todos los hijos menores
seleccionados, además del pivote y su cola, se tiene

`3C≤5b−6m`,  `3C≤5a−3b−6m`,  `3km≤5b`.                (2)

Las dos primeras usan `m+T>2m`. La tercera se sigue de la primera
y `C≥(k−2)m`. Los aros en otros contenedores o subárboles solo aumentan
las colas completas: omitirlos al obtener (2) es válido.

Al expandir el margen de (1), usando R≥a+b y Q≤bC, queda la cota inferior

`D=2ab−(b+2m)C−4m(a+b)−(k+3)m²`.                       (3)

**Lema R9.** Bajo (2), a≥b y b≥9m, se tiene D>0. Por tanto el
contenedor admite dos plazas de radio m y aplica R0.

Prueba algebraica. Escriba x=b−9m≥0. Son estrictamente positivos

`F=23b²−201bm+15m²=23x²+213mx+69m²`,

`G=4b²−27bm+3m²=4x²+45mx+84m²`.

Si 5a≥8b, la primera cota de C y la cota de k dan

`3D≥6a(b−2m)−5b²−21bm+3m²`.

Multiplicando por 5 y usando `(5a−8b)(b−2m)≥0`, resulta `15D≥F>0`.
Si 5a<8b, la segunda cota de C y la de k dan

`3D≥a(b−22m)+3b²−5bm+3m²`.

Para b≤22m, use `(8b−5a)(22m−b)≥0` y obtenga `15D≥F>0`.
Para b>22m, use `(a−b)(b−22m)≥0` y obtenga `3D≥G>0`.
Esto prueba el lema, incluyendo los extremos b=9m y b=22m.

**Consecuencia uniforme.** En un intercambio bloqueado, todo hijo
que no sea el mayor de su contenedor tiene radio en `(m,9m)`.
No hay una hipótesis previa sobre el grado del contenedor.

### Un criterio constructivo adicional para cualquier grado

Si k≥3, sea c el tercer hijo mayor. Las colas parciales
`c+(m+T)≤phi b` y `m+T≤phi c`, por el lema de dos colas, dan
`m+T≤b`. Así, **b>2m** en cualquier ramificación bloqueada.

Hay una construcción útil en el par diametral a,b dentro del disco
de radio a+b: centros `(-b,0)` para a y `(a,0)` para b. Ponga
`y=sqrt(a(a+b))`. Los discos de radio b/2 y centros

`(-b/2,y)`, `(b/2,y)`

están contenidos, son tangentes entre sí y evitan ambos discos
mayores. En efecto, sus normas son `a+b/2`; el primero es tangente
al disco a. Para el segundo, el cuadrado de la distancia a a excede
el cuadrado requerido en 2b². Respecto al disco b, las diferencias
de cuadrados son, respectivamente,

`2a(a+b)−2b²≥0`, `2(a²−b²)≥0`.

Además y>b/2, de modo que los dos discos nuevos están por completo
en el semiplano superior. Lean comprueba estas identidades y signos
con todas las coordenadas multiplicadas por 2.

El bolsillo inferior de radio beta(a,b) tiene centro de ordenada
`−2 beta`, por lo que está por completo en el semiplano inferior.
Si **C≤beta(a,b)**, coloque allí por fila a todos los hijos a partir
del tercero, trasladando sus subárboles. Reserve las dos plazas de
radio b/2>m del semiplano superior. Esto activa R0, cualquiera que sea k.
No se retiran hijos mayores ni se cambian sus padres.

Por tanto, en cada ramificación de un intercambio que siga bloqueado
son necesarias simultáneamente

`2m<b<9m`, `C>beta(a,b)`.

Estas condiciones tampoco prueban un bloqueo. Describen lo que no
cubren los dos criterios suficientes de esta sección.

## 4. Solo cinco radios pueden pertenecer a esa franja

Si hubiese seis radios a>b>c>d>e>f>m en la franja, las colas, incluyendo
el pivote y T>m, implicarían

```
3(b+c+d+e+f+2m) ≤ 5a
  3(c+d+e+f+2m) ≤ 5b
    3(d+e+f+2m) ≤ 5c
      3(e+f+2m) ≤ 5d
        3(f+2m) ≤ 5e
            6m ≤ 5f.
```

La eliminación sucesiva da

`a ≥ (6/5)(8/5)^5 m = (196608/15625)m > 9m`,

contradicción. Estas son colas parciales, por lo que el argumento vale
aunque los seis aros no sean consecutivos. Lean verifica la consecuencia
directamente a partir de las seis desigualdades lineales.

Por §3, hay a lo sumo cinco hijos que no sean el mayor de su contenedor
en **todo** el árbol de mayores, no cinco por contenedor.

## 5. A lo sumo dos ramificaciones y seis hojas

En cualquier árbol finito con raíz, si L es el número de hojas,

`L−1 = sum_{contenedores de grado≥2}(grado−1)`.

La suma de la derecha cuenta precisamente los hijos que no son el
mayor de su contenedor. Por §4 es a lo sumo 5 y, por tanto, L≤6.
La raíz virtual se incluye en esta identidad y en los grados.

El criterio C2 descarta el grado 2 en cualquier contenedor de un
intercambio bloqueado. Cada ramificación restante tiene grado al menos
3 y aporta al menos 2 a esa suma. En consecuencia hay a lo sumo dos
ramificaciones en todo el árbol. Cada grado es a lo sumo 6.
Además C1 exige que los grados de u y v sean 0 o al menos 3.

Este es un recuento simultáneo de todas las ramificaciones. No es una
clasificación de inventarios de tamaños sucesivos.

## 6. El grosor común también acota las cadenas

Si un aro de radio a tiene un solo hijo mayor de radio b, la capacidad
de su agujero es a−w≥b. Si fuese a−w≥b+2m, el lema de fila colocaría
ese hijo y dos discos adicionales m en el agujero, activando R0.
En un intercambio bloqueado se cumple, por tanto,

`b+w≤a<b+w+2m`.                                         (4)

No pueden existir seis aros consecutivos a→b→c→d→e→f>m en un tramo
cuyos primeros cinco nodos tengan un solo hijo mayor. En efecto, (4)
en las dos primeras aristas y la mera factibilidad en las tres últimas
dan

`a≤b+w+2m`, `b≤c+w+2m`,

`c≥d+w`, `d≥e+w`, `e≥f+w`.

La cola de a da `3(b+c+d+e+f+2m)≤5a`. Eliminando a,b, y luego
acotando c,d,e por f y w, estas desigualdades fuerzan

`10f+5w≤8m`,

imposible porque f>m, w≥0 y m>0. Lean prueba la contradicción incluso
con f≥m y las desigualdades no estrictas indicadas.

Así, antes de llegar a una hoja o una ramificación puede haber a lo
sumo cuatro aros unarios seguidos: cinco aros contando el nodo final.
La raíz virtual no es un aro y no se le asigna el grosor w.

## 7. Cota uniforme del prefijo mayor, y lo que queda abierto

Suprima los nodos de grado 1. Por §5, el árbol reducido tiene a lo sumo
dos ramificaciones y seis hojas, es decir, ocho nodos.

Si la raíz virtual es unaria, suprímala también: hay a lo sumo ocho
tramos, contando el tramo inicial desde la raíz hasta el primer nodo
no unario y un tramo por cada arista del árbol reducido. Cada tramo
contiene a lo sumo cuatro aros unarios y su nodo final, por §6.
El árbol original tiene a lo sumo `5·8=40` aros mayores que m.
Si la raíz virtual ramifica, cuenta como uno de los ocho nodos; hay
a lo sumo siete aristas y la cota se mejora a 35. Si la raíz no tiene
hijos mayores, la cota es inmediata.

**Teorema de reducción.** Todo intercambio que siga bloqueado bajo
rho≤phi, con grosor común en el disco, tiene a lo sumo dos ramificaciones,
seis hojas y 40 aros mayores que el pivote; ningún contenedor tiene
grado 2. Todo hijo que no es el mayor pertenece a `(m,9m)`, y la cola
posterior al siguiente aro tiene masa U≤m, cualquiera que sea su longitud.

Las constantes son cotas suficientes, sin pretensión de optimalidad.
Las etapas hasta §5 admiten agujeros independientes. La cota de cadenas
y de 40 aros usa expresamente el grosor común. El criterio de área es
plano: no se afirma aquí el mismo resultado en dimensión superior.

**Esta cota no limita el número total de aros de un contraejemplo.**
Puede haber arbitrariamente muchos aros menores que m. Reemplazarlos
por un solo aro de radio U no está justificado: alteraría los radios,
sus agujeros, el orden y las cotas de rho. Solo se usa que todos caben
por fila dentro de una plaza de radio m cuando esta existe.

Queda una familia finita de formas del árbol de mayores, con parámetros
geométricos continuos y una cola finita de longitud arbitraria. Cerrar
tau=phi por esta vía exige demostrar que también en esta familia se
puede alinear m, o encontrar una obstrucción geométrica real. Acotar la
estructura no demuestra la factibilidad de ese intercambio. El paso
siguiente es un lema común a esas ramificaciones, no calcular tau_n
para n=6,...,40 ni suponer que una exploración numérica es una prueba.

## 8. Alcance de Lean

`lean/Calamares/Reservoir.lean` verifica:

- `golden_lt_five_thirds`: la ecuación áurea implica 3phi<5;
- `squares_le_cap_mass`: Q≤bC para una lista finita de radios en [0,b];
- `two_slot_margin`: positividad de (3) bajo (2) y b≥9m;
- `clearance_area_margin`: paso algebraico de ese margen a (1);
- `upper_half_slots`: coordenadas de las dos plazas superiores de
  radio b/2, disjuntas del bolsillo inferior;
- `six_radii_exceed_cutoff`: exclusión de seis radios bajo el corte;
- `no_six_unary_nodes`: contradicción del tramo de seis aros.

Los certificados no postulan el resultado deseado; reciben las
desigualdades expuestas en cada paso. La subaditividad del área,
la interpretación de centros prohibidos, la obtención de esas
desigualdades desde un inventario y el recuento del árbol permanecen
como pruebas escritas. No se presenta el teorema de reducción completo
como un teorema formalizado en Lean.
