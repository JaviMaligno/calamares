# Partición de colas y reducción del siguiente umbral

Fecha: 2026-09-15. Avance local durante la revisión de los extras.
**Estado posterior:** Fable revisó la presión, partición y criterios
C1/C2 como dependencias de `tres_mayores.md`, que cierra tau=phi en
el disco. Esta nota tiene tres certificados Lean; sus referencias a
casos aún abiertos conservan el estado histórico anterior a T3.

## 1. Presión de la cola completa

Sean A>m los dos radios mayores y T la suma de todos los menores que m.
Si rho≤phi, entonces

`T≤2 beta(A,m)`.

Normalice m=1 y escriba g=beta(A,1). Las colas dan `T≤rho` y
`1+T≤rho A`. Si T>2g, las dos desigualdades estrictas
`2g<rho`, `1+2g<rho A` contradicen `golden_balance` de FourRing.
La fórmula homogénea de beta devuelve el resultado sin normalizar.
El certificado `PocketSplit.tail_le_double_pocket` verifica la
implicación normalizada para cualquier anillo conmutativo linealmente
ordenado; no presupone ninguna clasificación de bosques.

## 2. Partición de la cola restante

Sea p el mayor radio de una cola no vacía. Reserve p aparte. Los demás
radios son a lo sumo p y su suma es T-p. Asígnelos, uno por uno y en
cualquier orden, al grupo cuya suma actual sea menor.

Las dos sumas u,v satisfacen siempre `u-v≤p` y `v-u≤p`. En efecto,
si u≤v y se añade x≤p al primer grupo, entonces
`u+x-v≤x≤p`, mientras que `v-u-x≤v-u≤p` porque x≥0.
La otra elección es simétrica. Al terminar, u+v=T-p, y por tanto

`2u=(u+v)+(u-v)≤T`, `2v≤T`.

Si T≤2 beta(A,m), ambos grupos tienen suma de radios a lo sumo beta.
El lema de fila permite colocar cada grupo completo en uno de los
dos bolsillos disjuntos. No hay cota sobre el número finito de piezas.

`PocketSplit.splitLoads` calcula las sumas por esta regla.
`split_loads_spec` prueba conservación de masa, no negatividad y el
invariante de diferencia para una lista arbitraria. `split_loads_fit`
prueba la cota final de cada suma. La interpretación como partición de
piezas y el alojamiento por filas siguen escritos aquí.

## 3. Aplicación al desacuerdo en el segundo aro

Considérese un bosque voraz F y un testigo completo P sobre el mismo
prefijo admitido y un último aro omitido, como en `cinco_aros.md`.
Si el padre del segundo aro m difiere, un bosque lo pone en raíz y
el otro en el agujero de A. Luego `R≥A+m` y `h_A≥m`.

Los aros menores se pueden reconstruir como hojas; aún no se pretende
preservar sus padres. Si la cola es vacía no hay nada que repartir.
Si no lo es, sea p su radio mayor, con p<m.

- Si F pone m en raíz, coloque el par A,m en una bola concéntrica de
  radio A+m≤R, p en el agujero de A y los dos grupos de §2 en sus dos
  bolsillos.
- Si F pone m dentro de A, use en raíz el par fantasma A,m. Coloque
  p en la bola exterior reservada para el m fantasma, los dos grupos
  en los bolsillos y el m real en el agujero de A. El fantasma se elimina.

El resultado conserva todas las piezas y coincide con F en los padres
de A y m. Los agujeros pueden ser independientes: solo se usa h_A≥m.
La construcción es plana y cabe en toda bola de dimensión d≥2.

**Conclusión.** Bajo rho≤phi, el desacuerdo en el segundo aro puede
alinearse para cualquier tamaño finito de inventario. La limitación a
tres menores en §3 de `cinco_aros.md` no es necesaria. La prueba de
cinco aros queda válida tal como fue enviada; esta nota amplía uno de
sus pasos. Este argumento por sí solo no resuelve los desacuerdos
en el tercero y en el cuarto. No se deduce `tau_6=phi` ni `tau=phi`.

## 4. Dos criterios generales para alinear un pivote

Sea m un pivote cualquiera durante la alineación y T la suma de todos
los radios menores en el inventario restringido. Los padres de todos
los aros mayores ya coinciden en F y P. Siempre `T≤rho m≤phi m<2m`.
Si T≤m basta el intercambio por filas. Suponga T>m. Podemos reconstruir
todos los menores como hojas: solo hay que conservar los padres mayores
que m y colocar m en su destino u, distinto de su origen v.

**Criterio C1.** Si u tiene exactamente un hijo inmediato mayor a,
o si v tiene exactamente un hijo inmediato mayor a, se puede alinear m.

En el primer caso, F certifica que a,m caben como hermanos en u;
en el segundo, P lo certifica en v. En ambos, la capacidad de ese
contenedor es al menos a+m. Las colas del inventario implican
`T≤rho m`, `m+T≤rho a`, así que §1, aplicado al par a,m, da
`T≤2 beta(a,m)` incluso si hay otros aros mayores en otros contenedores.

Si se usa el par en u, coloque allí a,m y los dos grupos de §2 en
los bolsillos, mientras p ocupa la bola que m deja en v. Si se usa
el par en v, conserve a, coloque p en la bola del m fantasma y los
dos grupos en los bolsillos; el m real ocupa u junto a los mayores
que F certifica allí. No hay otro hijo mayor que estorbe al par en
el contenedor elegido. Todos los subárboles de a que contienen aros
mayores conservan sus padres y se ensamblan mediante coordenadas locales.

**Criterio C2.** Si algún contenedor w del bosque de aros mayores
tiene exactamente dos hijos inmediatos a>b>m, se puede alinear m,
sean cuales sean u y v.

Las colas en b y a contienen respectivamente m y todos los menores,
y además b en la segunda. Por §1 normalizado por b, tomando la cola
parcial `s=m+T`, se obtiene

`m+T≤2 beta(a,b)`.

Como T>m, beta>m. La capacidad de w es al menos a+b. Parta **toda**
la cola en dos grupos equilibrados, con suma U,V y mayor pieza p<m.
La prueba de §2 da `2U≤T+p<T+m≤2 beta`, y lo mismo para V.
Además `min(U,V)≤T/2<m`.

- Si u≠w, coloque a,b en w y ambos grupos en sus bolsillos; coloque
  m en u usando el certificado de F junto a los aros mayores.
- Si u=w, coloque m en un bolsillo de a,b, el grupo de mayor suma
  en el otro y el de menor suma en la bola exterior que m deja en v.

Todos los radios de los grupos caben por filas. Solo se han cambiado
padres menores y el de m; a,b siguen siendo hijos de w. Si uno de los
contenedores es antecesor de otro, los empaquetamientos interiores se
trasladan con su propietario. Ningún propietario de u,v,w puede ser
descendiente de m porque todos tienen radio mayor. Esto evita ciclos.

## 5. Qué reduce para seis aros

Con exactamente dos aros mayores A,B, o son hermanos en raíz (C2),
o forman una cadena A→B. En la cadena solo el agujero de B carece
de hijos mayores; como u≠v, uno de ellos tiene exactamente un hijo
mayor, y se aplica C1. Por tanto el **tercer aro también se puede
alinear con cualquier número finito de menores**, bajo rho≤phi.

Para un inventario de seis, los desacuerdos desde el quinto aro tienen
a lo sumo un menor y se resuelven por el intercambio de fila. Queda el
cuarto, con tres mayores A>B>C y dos menores p>q. Los seis bosques
posibles de los mayores se enumeran eligiendo el padre de B entre
raíz/A y el de C entre raíz/A/B:

| Padres (B,C) | Criterio |
|---|---|
| (raíz,raíz) | Caso pendiente: A,B,C en raíz |
| (raíz,A) | C2 en raíz, con A,B |
| (raíz,B) | C2 en raíz, con A,B |
| (A,raíz) | C2 en raíz, con A,C |
| (A,A) | C2 en el agujero de A, con B,C |
| (A,B) | Cadena: C1, pues solo el agujero de C tiene cero hijos mayores |

Así, un fallo con seis aros y rho≤phi exigiría un desacuerdo en el
cuarto con **los tres mayores en raíz**, y los dos menores como hijos
inmediatos de u en P con `p+q>m`; de otro modo bastaría la fila.
Los padres distintos u,v de m pertenecen a `{raíz,A,B,C}`.

Esta es una reducción local, no una solución del caso pendiente.
Con tres hermanos mayores no se puede aplicar C2 a un par descartando
el tercero: sigue ocupando el mismo contenedor. No se afirma que las
configuraciones restantes sean imposibles ni que exista un fallo.
La clasificación y C1/C2 siguen escritos; los tres teoremas Lean solo
formalizan la presión normalizada y las sumas de la partición finita.
