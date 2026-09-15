# Respuesta a la primera revisión de tres mayores

Fecha: 2026-09-15. Dictamen íntegro conservado en
`2026-09-15-fable-three-core-review.md`; envío y hashes en su metadata.
Fable no encontró un fallo invalidante, pero solicitó tres precisiones
antes de afirmar el resultado. Se evaluaron y se incorporaron a
`docs/drafts/tres_mayores.md`:

1. **B: uso del intervalo de pared.** Antes de deducir c≤beta cuando
   R0=a+b, se lleva explícitamente c a la pared dejando a,b fijos.
   Así se cumplen las hipótesis del intervalo angular empleado.
2. **C: existencia y disyunción.** La positividad de una altura no
   prueba que dos discos estén en lados distintos. Se sustituye ese
   argumento por una inversión en el punto de contacto de a,b: el
   problema se transforma en una franja, con un círculo que la cruza
   y exactamente dos discos tangentes admisibles, uno en cada componente.
   La inversión de vuelta prueba contención y disyunción. La fórmula
   clásica de reflexión de Descartes identifica la curvatura D; se
   añade una referencia primaria para esa fórmula. El certificado
   `opposite_height_positive` se conserva como desigualdad auxiliar,
   sin atribuirle la disyunción ni la existencia geométrica.
3. **Aplicación: reparto de las plazas.** Se define completamente el
   criterio antes abreviado como R0. Si w≠u, las dos plazas alojan p
   y la fila U, y m ocupa su destino certificado en F. Si w=u, alojan
   m,p y U ocupa la bola que m deja en v. Se explican w=v, los posibles
   antecesores y el ensamblaje conservando todos los padres mayores.

No cambiaron las siete proposiciones Lean ni las fórmulas del script.
La segunda revisión, con prefijo `2026-09-15-fable-three-core-final`,
recibe los mismos seis archivos autorizados y debe auditar además
las dependencias del cierre: presión, partición, C1/C2, el primer fallo
y el prefijo máximo. La primera revisión las tomó como válidas y no
equivale a haberlas reauditado.

La cota superior tau≤phi ya tiene revisión en la v2. La nueva revisión
se centra en la garantía universal para rho≤phi; no se le atribuye
una nueva comprobación de aquella familia aproximante.
