# Reducción uniforme a un intercambio de aros consecutivos

Fecha: 2026-09-15. Cambio de estrategia: el parámetro de inducción es
la longitud del prefijo de padres ya alineado, para un inventario finito
arbitrario. No se clasifican por separado los tamaños n=6,7,8,…

**Estado posterior:** `tres_mayores.md` cierra tau=phi en el disco.
Fable revisó la cota de dos colas, el primer fallo y el prefijo máximo
como dependencias de ese cierre; no se atribuye revisión a los pasos
adyacentes A/B, que el cierre no necesita. El resto de esta nota conserva
su estado histórico de investigación anterior a T3.

## 1. Una desigualdad para cualquier longitud de cola

Sean m>p los radios de dos aros consecutivos de un inventario restringido,
y U la suma de todos los posteriores a p. Las dos cotas de rho≤phi dan

`p+U≤phi m`, `U≤phi p`.

Multiplique la primera por phi y use la segunda:

`(phi+1)U ≤ phi p+phi U ≤ phi² m = (phi+1)m`.

Como phi+1>0, **U≤m**. No hay cota sobre el número de sumandos de U.
Más generalmente, con k≥0 y las mismas cotas con k, se tiene
`(1+k)U≤k²m`. El corte en phi aparece porque `phi²=phi+1`.

Para una secuencia `r_1>...>r_n`, esto dice

`sum_{j≥i+2}r_j≤r_i` para todo i para el que exista r_(i+1).

El lema de fila aloja toda esa cola en una bola de radio r_i. Lean
verifica la desigualdad para cualquier anillo conmutativo linealmente
ordenado, con las sumas representadas por U; no formaliza el bosque.

## 2. Reducción del primer intercambio que no se puede alinear

Restrinja un primer fallo del voraz a su conjunto admitido G y al aro
omitido final. La factibilidad completa y rho≤phi se conservan al
restringir. Sea F el bosque de G. Entre todos los testigos completos P,
elija uno cuyo prefijo de padres coincidente con F tenga longitud máxima.
Existe tal máximo porque las asignaciones de padres son finitas.

Si no hay desacuerdo, el testigo admite el último aro en F. En caso
contrario sea m el mayor desacuerdo, u su padre en F y v su padre en P,
con u≠v. Los padres de los mayores que m ya coinciden. Sea p el siguiente
radio y U la suma de los posteriores; por §1, U≤m.

**Paso A: necesariamente P(p)=u.** Los hijos inmediatos de u menores
que m forman el conjunto desplazado S. Si p no pertenece a S, su suma
es a lo sumo U≤m: el intercambio de fila los lleva con sus subárboles
a la bola exterior que m deja en v, mientras m ocupa u bajo el certificado
del prefijo de F. Esto alinea m y contradice la maximalidad de P.
Por tanto p es hijo inmediato de u en P. Además `sum_{s in S}r_s>m`.

Si p fuese el aro final omitido, sería el único menor y la fila bastaría
porque p<m. Por tanto p pertenece a G y tiene padre definido en F.

**Paso B: necesariamente F(p)=v.** Suponga F(p)≠v. Tome el prefijo
real de F hasta p: es un bosque factible y ya fija los padres de todos
los mayores, m y p. Dentro de v, sus únicos hijos inmediatos son los
mayores que m, pues m y p tienen padres distintos de v.

En P, esos mismos hijos mayores coexistían con m. Conserve su
empaquetamiento local en v y sustituya la bola exterior de m por una
fila que contenga **todos** los aros posteriores a p, de masa U≤m.
Su padre pasa a ser v. En todos los demás contenedores use los
empaquetamientos del prefijo de F hasta p. Los padres de u y v son
mayores que m, de modo que los empaquetamientos se ensamblan localmente
sin ciclos, aunque un contenedor sea antecesor del otro.

El resultado coloca el inventario completo y coincide con F hasta p.
Es una contradicción. Así, F(p)=v.

**Proposición U.** Para cualquier n finito, un testigo máximo que no se
puede alinear bajo rho≤phi tiene obligatoriamente el patrón adyacente

| Aro | Padre en P | Padre en F |
|---|---|---|
| m | v | u |
| siguiente p | u | v |

con `U≤m`, `U≤phi p`, `p+U≤phi m`, y desplazamiento inmediato en u
de suma mayor que m. Las demás piezas son una cola finita, no nuevos
casos indexados por n. La reducción solo usa el lema de fila dentro de
la bola vacante, así que también vale para K arbitrario y agujeros
independientes en el modelo del paper.

## 3. Qué cubren los criterios geométricos existentes

En bolas de dimensión d≥2, C1/C2 de `particion_bolsillos.md` cierran,
para cualquier número de piezas, un intercambio si:

- u o v tiene exactamente un hijo inmediato mayor que m; o
- algún contenedor del bosque de mayores tiene exactamente dos hijos
  inmediatos mayores que m.

Luego, en un testigo máximo que siga bloqueado, ningún contenedor del
bosque de mayores tiene grado 2 y los grados de u y v son 0 o al menos 3.
Se pueden recorrer cadenas de grado 1, pero no se puede eliminar una
ramificación de grado ≥3 sin un argumento geométrico adicional.

**Corolario uniforme para bosques binarios.** Toda ejecución descendente
cuyo bosque final tenga a lo sumo dos hijos inmediatos por contenedor
coloca el lex-máximo si rho≤phi, para cualquier n finito, en bolas de
dimensión d≥2, incluso con agujeros independientes.

En efecto, cada prefijo de mayores sigue siendo binario. Si hay un
contenedor con dos hijos, aplica C2. Si no, el árbol con raíz virtual
(la sartén) tiene a lo sumo un hijo por nodo: es una cadena, con un solo
contenedor sin hijos mayores. Como u≠v, uno tiene exactamente un hijo
mayor y aplica C1. Cada intercambio aumenta el prefijo coincidente;
la inducción termina para todo n. El enunciado es condicional a la
ejecución binaria; no afirma que toda ejecución tenga esa propiedad,
ni que siempre exista una ejecución voraz de ese tipo.

## 4. El enunciado geométrico pendiente

Para cerrar tau=phi por esta vía basta demostrar lo siguiente:

> En todo inventario de grosor común y rho≤phi en el disco, dadas las
> asignaciones F y P de §2 con el intercambio adyacente m,p y el prefijo
> de mayores coincidente, existe un testigo completo P' que coincide con
> F en los mayores y en el padre de m, cualquiera que sea el número de
> hijos mayores de cada contenedor.

No es un teorema demostrado. §2 explica por qué sería suficiente: si
fallara la alineación, su testigo máximo cumpliría exactamente estas
hipótesis. Probarlo para grados acotados no lo prueba para todos los grados.
Los casos C1/C2 ya cubiertos se pueden excluir de su dominio residual.

El objetivo original es el grosor común y el disco. La formulación con
agujeros independientes o dimensión mayor es más fuerte; no se exige
resolverla para dar por cerrado ese objetivo. La desigualdad U≤m es
uniforme, pero no crea automáticamente una bola vacante después del
intercambio: p puede ocupar precisamente el lugar liberado por m en v.

## 5. Control que impide confundir álgebra con geometría

En el **modelo aditivo**, donde hermanos caben si y solo si su suma de
radios no supera la capacidad, tome

`r={17/10,1,3/5,1/2}`, `w=11/20`, `R=27/10`.

Los agujeros son `23/20,9/20,1/20,0` y rho=21/17<3/2<phi.
Un testigo coloca 17/10 y 1 en raíz, y 3/5,1/2 en el agujero del mayor.
La ejecución que anida 1 en ese agujero coloca después 3/5 en raíz
y rechaza 1/2: la raíz sumaría 28/10>R, el agujero mayor sumaría
3/2>23/20 y los otros dos agujeros disponibles son menores que 1/2.

Se cumplen la desigualdad U≤m y el patrón adyacente, pero falla el
intercambio aditivo. Por ello, la cota de cola y la inducción combinatoria
por sí solas no bastan: hace falta geometría del disco. Este ejemplo
**no refuta** tau=phi en el modelo euclidiano: la desigualdad de suma
que bloquea la raíz aditiva no es una exclusión geométrica en el disco.
`UniformExchange.additive_control` certifica exactamente sus paredes
y las tres razones de cola en los racionales.

## 6. Siguiente trabajo y criterio de cierre

Investigar el intercambio adyacente de §4 con grados arbitrarios:
o construir una recolocación uniforme que conserve todos los ocupantes
mayores, o encontrar una obstrucción geométrica real. Las búsquedas
numéricas servirán para refutar candidatos, no para extrapolar una
garantía universal de una lista finita de tamaños.

La reducción no pone un límite al tamaño de un contraejemplo mínimo,
no certifica que no existan contraejemplos y no convierte los cierres
computacionales históricos fuera de sus dominios en pruebas globales.

**Avance posterior, misma fecha:** `nucleo_uniforme.md` acota la
estructura del intercambio que siga bloqueado en el disco con grosor
común: a lo sumo dos ramificaciones, seis hojas y 40 aros mayores que
el pivote. La cola puede tener longitud arbitraria. Esto acota el
prefijo mayor, no el tamaño total de un contraejemplo, y deja pendiente
la factibilidad geométrica del intercambio en esa familia.
