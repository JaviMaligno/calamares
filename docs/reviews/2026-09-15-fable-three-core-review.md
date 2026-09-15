# Revisión de la prueba candidata global mediante tres discos mayores

Modelo: `claude-fable-5-1`. Revisión externa estática mediante Claude Code: no ejecutó Python ni Lean. Alcance y hashes en el manifiesto y metadata `2026-09-15-fable-three-core`. El dictamen se conserva íntegro.

---

Voy a auditar estáticamente `docs/drafts/tres_mayores.md` lema a lema, rehaciendo a mano las derivaciones geométricas y algebraicas, sin ejecutar Lean ni Python.

## Veredicto por lema

| Pieza | Veredicto | Comentario |
|---|---|---|
| Lema A | Correcto | Intervalos, asignación de extremos, producto AB, signo del margen y semiplano verificados a mano. |
| Lema B | Correcto, con un paso que hay que explicitar | Reducción a pared, equivalencia angular, compacidad, `R0>a+b`, suma 2pi y rama de Descartes son válidos. |
| Lema C | Álgebra correcta; identificación geométrica incompleta | La fórmula de altura no prueba "lados opuestos". Reparable con un argumento estándar. |
| T3 | Correcto | Ambos casos, compresión con e,V, uso de las cuatro colas, radios iguales y V=0 cierran. |
| Aplicación §5 | Correcta en el fondo, incompleta en la escritura | El reparto de p y U en las plazas no está escrito y "R0" como criterio no está definido en el material adjunto. |

No he encontrado un fallo real que invalide la prueba. Sí hay tres huecos de rigor que deben cerrarse antes de afirmar el resultado.

## Comprobaciones y errores concretos

**Lema A, verificado.** Rehice la ley de cosenos respecto a b y a. Con `R=a+b` la condición frente a b es `sin²(θ/2) ≥ bx/(a(R−x))` y frente a a es `sin²((π−θ)/2) ≥ ax/(b(R−x))`, exactamente el intervalo del texto. La suma `X²+Y²` vale `x(a²+b²)/(ab(R−x))`, y es ≤1 exactamente cuando `x≤beta`. La separación exigida para dos discos tangentes a la pared es `2 asin sqrt(rs/((R−r)(R−s)))`, que coincide con `2 asin(AB)`. El margen multiplicado por `ab(R−r)(R−s)` da `R²(ab−br−as)+(a−b)²rs`, tal como afirma el texto y la identidad Lean. Comprobación de frontera: con `a=b=1, r=s=1/2` el margen es cero y los dos discos quedan exactamente tangentes, como debe ser. La ordenada del bolsillo inferior es `−2beta` en general; se deduce de la fórmula de altura del lema C con `x=beta`, aunque el centro no está sobre el eje vertical si `a≠b`. La nota no lo justifica, pero es cierto.

**Lema B, verificado.** La dirección común a dos semiplanos cerrados por el origen existe siempre en el plano, y a lo largo de ella las distancias no decrecen. La equivalencia `θab+θac+θbc≤2π` es correcta en ambos sentidos: los huecos elegidos en `[θij,π]` garantizan que el ángulo menor de cada par coincide con el hueco dirigido. El paso `R0=a+b ⇒ c≤beta` debería decir explícitamente que primero se lleva c a la pared con la reducción anterior, porque el intervalo del lema A supone tangencia a la pared. Es un detalle de redacción, no un error. La raíz de Descartes es la correcta: la otra da `1/R0<0`.

**Lema C, hueco de rigor.** La identidad (C2) es exacta: la desarrollé término a término y coincide, incluido el factor `2S+2t−C>0`. También `D>C>0 ⇔ t<S ⇔ c>beta` y `S/Q=beta`. Comprobación numérica manual con `a=3, b=1, c=1`:

```
t≈1.291  R0≈4.02  D≈1.169  d≈0.855
c+d≈1.855 ≥ 2beta≈1.846
```

El problema está en la frase "ambos discos quedan en lados opuestos de la recta". La fórmula `h²−x²>0` solo prueba que cada disco no cruza la recta de los centros, no que estén en lados distintos. Además, la recta de los centros no separa exactamente los dos huecos: como el centro del contenedor no está en esa recta cuando `a≠b`, el hueco del lado de c contiene dos pequeñas franjas al otro lado de la recta, cerca de los puntos de contacto de a y b con la pared. Reparación: invertir en el punto de tangencia de a y b. Entonces a y b se convierten en dos rectas paralelas y el contenedor en un círculo entre ellas; los círculos tangentes a las dos rectas y a ese círculo son exactamente dos, uno a cada lado. Luego los dos huecos curvilíneos tienen un único incírculo cada uno, sus curvaturas son las dos raíces de Descartes, y como `C≠D` el disco d es el incírculo del hueco que no contiene a c. La disyunción de c y d se sigue de estar en componentes distintas, y la afirmación sobre la recta puede eliminarse.

**T3, verificado.** (T1) sale de las colas de a y b con `t=(c+U)/b`, `a'=a/b>1` y la homogeneidad de beta. En el caso `c>beta` basta `d≥2beta−c≥U`. En el caso `c≤beta`, las colas de b y c dan `U≤b`, las de c y e dan `V≤c`, y el orden da `e≤c`; las tres hipótesis del lema A se cumplen. Se usan las colas de a, b, c y e, ninguna más. Radios iguales y `V=0` no rompen nada. La hipótesis `a>b` solo se necesita para el `1<a` de `tail_le_double_pocket`.

**Aplicación §5, dos omisiones.** Las colas de la lista auxiliar están acotadas por las originales porque la cola original de cada `ai` contiene `m+T>2m`. Sus tres mayores caben en el contenedor porque ya conviven en él. Lo que falta escribir es el reparto: p, con `p<m`, va a una plaza libre de radio m, y todos los aros posteriores a p, de suma `U≤m`, van en fila a otra plaza. Hacen falta dos plazas libres además del sitio de m en u. Si `u=w`, T3 da una plaza libre y el hueco que m deja en v da la otra. Si `u≠w`, las dos plazas de T3 bastan. Este reparto es correcto, pero la nota no lo formula, y el nombre "R0" como criterio no aparece en las notas adjuntas; conviene definirlo o sustituirlo.

## Cobertura para todo n

Con las cuatro dependencias tomadas como válidas, la prueba cubre cualquier inventario finito. La partición es exhaustiva e independiente de n: algún contenedor tiene grado ≥3 y se aplica T3, o alguno tiene grado 2 y se aplica C2, o el árbol de mayores es una cadena y uno de u, v tiene grado 1 y se aplica C1. Cada paso alarga el prefijo coincidente y el inventario es finito. No reaudité Proposición U, C1 ni C2, ni la afirmación de que las familias con rho descendiendo a phi dan el ínfimo. No afirmo tau=phi ni novedad bibliográfica ni la extensión dimensional.

## Sugerencias no verificadas

Sustituir en el lema C el argumento de la recta por el de inversión descrito arriba, y añadir en §5 un párrafo con el reparto de plazas y los tres subcasos `u=w`, `v=w`, ninguno. Si se quiere respaldo Lean, `opposite_height_positive` puede quedarse como certificado de que cada disco no cruza la recta, pero no debe citarse como prueba de la separación.
