# Respuesta a la revisión final del cierre uniforme

Fecha: 2026-09-15. El dictamen íntegro, sin modificaciones, está en
`2026-09-15-fable-three-core-final-review.md`. El proceso terminó con
código 0. Fable acepta la prueba escrita completa de la garantía
universal rho≤phi en el disco para todo inventario finito con radios
estrictamente decrecientes y agujeros independientes. Revisó A–C, T3,
el reparto de plazas, presión, partición, C1/C2 y el prefijo máximo.
No ejecutó Lean ni Python y no reauditó la familia superior de la v2.

Las tres aclaraciones solicitadas se incorporaron a `tres_mayores.md`
y al suplemento inglés:

1. El voraz conserva padres, admite recolocaciones de hermanos y
   rechaza solo cuando ningún contenedor hace factible el bosque extendido.
2. El centro de inversión queda dentro del círculo imagen de la pared,
   fuera de las dos soluciones de la franja. Sus imágenes inversas son
   por ello discos acotados.
3. La inversión exhibe exactamente dos discos admisibles y t<S hace
   distintas las raíces de Descartes, identificando la segunda mediante
   la reflexión clásica.

Estas son precisiones de la prueba aceptada, no nuevos lemas pendientes.
Se actualizaron los encabezados y estados de las notas y el comentario
de `ThreeCore.lean`; sus siete enunciados y pruebas Lean no cambiaron.
El suplemento inglés reúne el mismo argumento e incluye una versión
directa de C2: m+T≤2beta y T>m dan beta>m, de modo que los dos
bolsillos del par ya son las dos plazas que necesita el reparto general.
El texto inglés no se envió por separado a Fable.

Una frase del dictamen escribe `min(U,V)<T/2<m`. La nota revisada
usa correctamente `min(U,V)≤T/2<m`: puede haber grupos equilibrados
con igualdad en la primera relación. No se adopta esa desigualdad
estricta accidental ni se necesita para el argumento.

La cota superior tau≤phi ya estaba probada y revisada en la v2;
combinada con la nueva garantía, queda tau=phi, con ínfimo no alcanzado.
La revisión no afirma novedad bibliográfica ni una extensión dimensional.
La reducción histórica de 40 mayores no interviene en el cierre y
no se presenta como revisada externamente.
