# Respuesta a la revisión del umbral de cuatro aros

Fecha: 2026-09-14. Fable (`claude-fable-5-1`, Claude Code) emite
**ACEPTAR** para `thm:fourfloor`: `tau_4=phi`, con todo fallo estricto
por encima de phi e ínfimo no alcanzado. Dictamen íntegro en
[`2026-09-14-fable-four-ring-review.md`](2026-09-14-fable-four-ring-review.md).

La revisión recibió solo los extractos de `paper/main.tex` que constan
en su manifiesto: 32 573 caracteres, con hash del payload y de la fuente
en la metadata. No recibió el archivo nuevo de Lean, ni ejecutó Python
o Lean. Revisó de forma independiente la clasificación de bosques,
las dependencias de tres aros, el suelo rígido, la suficiencia del
bolsillo, las factorizaciones y la familia que aproxima el ínfimo.

Se incorporan las cinco precisiones no bloqueantes:

1. Los omitidos no modifican el estado, por lo que la restricción de
   la ejecución al subinventario es legal y su inventario entero factible.
2. El aro unidad viaja con su propio subárbol durante el intercambio.
3. La factibilidad del trío se refiere a hijos de la raíz, y la
   legalidad de anidar la unidad ya fue certificada por el voraz.
4. El escalado se escribe explícitamente: t=1/A, omega=w/A,
   R/A≥1+t, rho invariante.
5. Se precisa que la cota inferior usa solo la suficiencia del bolsillo.

No hubo corrección matemática. La extensión esférica usa el mismo
argumento de bosques y las consultas finales de pares y tríos, junto
con la reducción dimensional revisada en el otro dictamen de la v2.
Fable no revisó esa extensión en este payload específico.

Verificación local: `FourRing.lean` comprueba las dos identidades y
`golden_balance`; `lake build` pasa con 84 teoremas en la biblioteca.
Solo axiomas estándar de Lean, sin `sorry`, sin `native_decide`.
Esto no formaliza la semántica del bosque ni prueba el umbral universal
para inventarios de cinco o más aros.
