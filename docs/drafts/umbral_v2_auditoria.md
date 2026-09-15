# Auditoría del umbral áureo para la v2

Fecha: 2026-09-14. La afirmación universal `tau=phi` permanece abierta.
La v2 añade una prueba completa de **`tau_4=phi`**, donde se restringe
el ínfimo a inventarios de como máximo cuatro aros. No hay fallo con
`rho≤phi` en esa clase; el ínfimo no se alcanza. La prueba está en
`paper/main.tex`, `thm:fourfloor`.

**Actualización del 2026-09-15, fuera de esta v2:**
[`cinco_aros.md`](cinco_aros.md) añade una clasificación nueva que
cubre hasta cinco aros, con 11 certificados Lean y revisión de Fable
con precisiones menores incorporadas. El texto siguiente conserva el estado
de la auditoría del día 14. El nuevo argumento deja el siguiente
incremento en seis aros; no cierra los residuos globales de esta lista.
La continuación local [`particion_bolsillos.md`](particion_bolsillos.md),
sin revisión externa, reduce seis al cuarto aro con tres mayores en raíz.

## Reducción que sí se cierra

Considérese la primera omisión que discrepa del lex-máximo. Si hay a
lo sumo dos aros admitidos, restringir a ellos y al omitido contradice
el teorema para tres aros. Por tanto, con cuatro, el inventario entero
es factible y el voraz admite los primeros tres y rechaza el cuarto.
Normalizando el segundo radio, escribimos `A>1>p>q>0`.

Si un testigo completo coincide con el voraz en el padre de `1`, se
puede adaptar también el padre de `p`: el único aro menor, `q<p`,
cabe en la bola vacante, o viaja con el subárbol de `p`. Esto daría
admisión del último. Así, todos los testigos completos tienen el
padre opuesto para `1`. Al intercambiarlo, el conjunto desplazado
debe ser exactamente los dos hijos inmediatos `{p,q}`, con `p+q>1`;
si hay uno solo o la suma es a lo sumo uno, cabe en la bola vacante.

- **Voraz anida `1`:** testigo con raíz `{A,1}` y `{p,q}` en el
  agujero de A; `R≥A+1`, `p+q≤A-w`. La raíz `{A,p,q}` debe ser
  infactible, pues de lo contrario anidar `1` daría un testigo ya
  alineado. Tras escalar por A, aplica el suelo rígido con holgura:
  `rho>T>phi`.
- **Voraz deja `1` en raíz:** el testigo lo anida en A, de modo que
  `A-w≥1`. El tercer aro debe estar dentro de A: cualquier otro
  padre deja ese agujero vacío y admite `q<1`. El rechazo en la raíz
  exige `q>g(A)=A(A+1)/(A²+A+1)`, por el bolsillo diametral en
  radio `A+1≤R`. Por ello `rho>2g(A)` y `rho*A>1+2g(A)`.
  Para `A≥phi`, `2g(A)≥phi`; para `1<A≤phi`,
  `1+2g(A)≥phi*A`. Las factorizaciones del manuscrito prueban ambas.

La familia áurea preexistente da los fallos con `rho↓phi` y cierra
el ínfimo. La reducción de bosques no depende de la dimensión;
las consultas finales son de dos o tres bolas. Por G2–G3 se obtiene
también `tau_(4,d)=phi` para todo `d≥2`.

`lean/Calamares/FourRing.lean` verifica las dos identidades y la
implicación ordenada completa `golden_balance`. Su compilación y
`lake build` dan salida 0, con solo `propext`, `Classical.choice` y
`Quot.sound`. El bosque y el bolsillo euclidiano siguen por escrito.
La revisión independiente tiene manifiesto separado en `docs/reviews/`.

## Por qué no prueba tau=phi para todo inventario

Desde cinco aros, el primer desacuerdo puede tener varios aros mayores
o desplazar más de dos hijos, con descendientes. La clasificación
anterior deja de ser exhaustiva. No puede aplicarse simplemente a
cada subconjunto de cuatro: la factibilidad de todos los subconjuntos
pequeños no equivale a la compatibilidad del bosque entero.

El inventario actual se toma del apéndice `Remaining cases` del
manuscrito y de los sellos finales de `docs/drafts/VEREDICTOS.md`,
no de hojas de ruta intermedias:

| Frente | Estado y alcance |
|---|---|
| Recuentos de ocupantes de cierres computacionales | Barridos hasta j=9 en raíz y j=8 anidado; los presupuestos de los teoremas escritos sí son uniformes |
| Coronas ESP reflejadas | Certificadas solo en sus cajas declaradas |
| Extras hoja ligeros | Cerrados hasta omega=1.25; banda [1.25,1.6] pendiente; en [1.6,2], cierre declarado para j_v≤1 |
| Familia invariante en anchura | j_v≥2 para omega>1.6 sigue pendiente |
| Extras padre | No extrapolar fuera de omega≤1.05, W_v≤8 y los dominios declarados de W_z |
| Perfil pesado de hojas | Corte sellado omega≤1.25, W_z≤34, W_v completo; el 1.15 del manuscrito anterior estaba desactualizado |
| Cruce anchura alta / W_z>34 de hojas | Sellado omega∈[1.6,6], excluyendo la familia j_v≥2 declarada; omega>6 sigue pendiente |
| Torres | Cadenas cerradas; ramificaciones pendientes |
| Contenido de u | Una exclusión estructural sigue condicionada al modelo |
| Converso gap⇒cell | Enunciado exacto con soporte de barrido muestreado; ese muestreo no sustituye una prueba ni refuta por sí solo el enunciado |

Sustituir un certificado riguroso por una prueba analítica es una
mejora de exposición. No es un hueco lógico adicional dentro del
dominio que el certificado cubre. Sí lo es extrapolar sus cajas.

## Próximo obstáculo matemático concreto

La nota 3j y los sellos finales describen una banda del quinteto
`{z,x1,x2,m,sigma2}` en la que una caja contiene tanto puntos factibles
como infactibles. Refutar mediante radios inferiores y certificar
mediante radios superiores no separa esa caja; los intentos con
subdivisión más fina agotan el presupuesto. Esto no demuestra que
ningún algoritmo de subdivisión pueda funcionar, pero identifica una
limitación comprobada del criterio actual.

Hace falta una desigualdad adicional que acople capacidad y radios,
o una caracterización más precisa de la frontera del quinteto y su
ensamblaje con las colas. `code/quintetocert.py` cierra el quinteto
del caso anidado j=1 en otro dominio: no elimina esta familia j_v≥2.
No se vuelve a ejecutar una campaña de horas sin cambiar esa pieza
matemática. El nuevo cierre de cuatro aros permite concentrar la
búsqueda en inventarios de cinco o más.
