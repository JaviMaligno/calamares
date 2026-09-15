# Respuesta al dictamen independiente de la v2

Fecha: 2026-09-14. Modelo del informe: `claude-fable-5-1` vía Claude
Code. Envío de los diez archivos/extractos autorizado expresamente por
el usuario. Payload estático de 82 510 caracteres, con hashes en la
metadata; el dictamen íntegro se conserva en
[`2026-09-14-fable-v2-review.md`](2026-09-14-fable-v2-review.md).

Fable acepta G2–G7, el ejemplo 3D/2D y el límite Y, y pide revisión
menor para las gemelas. No señala una refutación matemática.

1. **Admisión del primer pequeño: corregida.** La prueba de las
   gemelas ahora explicita que reducir el disco unidad del par raíz
   produce `{2,z}` factible para `z<1`. Añadido tanto al borrador como
   al manuscrito integrado. El oráculo exacto ya verificaba esos pares.
2. **Referencia de G7: corregida.** Se cita `thm:oblivious` y su
   alcance explícito en cualquier contenedor y dimensión.
3. **Consulta `{10,5,4.50}`: aclarada.** Se enumeran las seis consultas
   triples de las gemelas esféricas. El rechazo adicional usa el
   bolsillo rígido general `30/7`, aunque V2 imprimía otros dos radios.
4. **Instancia real: aclarada.** El borrador de Y distingue el
   enunciado abstracto sobre anillos ordenados de una instancia Lean
   de los reales, que este proyecto no contiene.
5. **Q4 supuestamente redundante: no se elimina.** La observación
   identifica correctamente que Q4 no se necesita *después* de tener
   `cx > ax+q` y `cy > ay+q`. Pero esas desigualdades se prueban antes:
   de `bx > ax+p` y `bx ≤ s-b` resulta `ax < s-b-p`; junto con
   `cx ≥ c` y Q4, `s-b-c ≤ p+q`, esto excluye `cx-ax < -q`.
   El argumento es el mismo para y. En Lean, `hsum` está disponible
   al `grind` que prueba la tercera premisa de `separated_coordinate`
   en `hcx`/`hcy`. La versión escrita muestra explícitamente ese uso.

No se implementan las mejoras opcionales de formalización de signos
de G: la prueba escrita y el alcance de `SquareLimit.lean` ya son
explícitos. El nuevo teorema `tau_4=phi` se envía en una revisión
separada; no forma parte de este dictamen.

La revisión no ejecutó herramientas. La verificación local de esta
revisión comprende `lake build` (84 teoremas tras añadir FourRing),
21 pruebas unitarias del cuadrado y cuatro pruebas del bundle.
La compilación y revisión visual del PDF se registran en el acta final
de la v2. No se ha repetido la campaña histórica de varias horas.
