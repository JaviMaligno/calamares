# Respuesta y comprobaciones tras la revisión de Fable

Fecha: 2026-09-14. Informe externo íntegro:
[`2026-09-14-fable-square-review.md`](2026-09-14-fable-square-review.md).

**Dictamen externo:** revisión menor, solo de redacción. Fable confirma
la matemática de D, el Lema Q, su codificación cartesiana y G1. La
revisión fue estática: no ejecutó Python ni Lean. Las comprobaciones
de ejecución que se recogen aquí corresponden al agente principal.

## Observaciones y resolución

| Observación de Fable | Evaluación y acción |
|---|---|
| Ambigüedad de correspondencia entre los radios y los centros del testigo | La lectura respectiva era correcta. Se escribe ahora explícitamente: disco b en `(-c,0)` y disco c en `(b,0)`. No cambia ninguna coordenada. |
| Python no comprueba el orden estricto de los radios | Ampliación opcional incorporada: `proper_rings` comprueba grosor positivo y `0<c<b<m<a`, incluido `b<m`. El test existente exigió primero esa pared y falló; tras añadirla pasan los 21 tests. D pasa ahora 17/17 paredes. |
| Los controles factibles solo rechazan los p,q suministrados | Se aclara en ambos tests. Su resultado booleano no pretende demostrar factibilidad ni cuantificar sobre todos los certificados. D' tiene un testigo explícito escrito y verificado en Lean. |
| Añadir a Lean las contenciones de los dos discos en el agujero | Ampliación opcional no necesaria para cerrar la revisión. Se mantiene el alcance declarado: `d_witness` comprueba `b+c=H`; el argumento de fila y su interpretación geométrica están escritos. |
| La identificación de X no se puede contrastar con la definición en los extractos del paper | X se define en el borrador `docs/drafts/cuadrado.md`, no en el manuscrito v1. El polinomio coincide; la nota D identifica su propia rama mediante signos y monotonía. No se usa como hipótesis ningún suelo geométrico no probado. |

No se han cambiado las pruebas geométricas por sugerencia del revisor,
pues no señaló fallos en ellas. Después de congelar el envío se sustituyó
`import Std` por `import Init.Grind` en `Square.lean` para reducir las
dependencias cargadas; se recompilaron los mismos enunciados y pruebas.
La raíz de la biblioteca y su README incorporan además `SquareLimit`.
El informe externo describe la versión cuyos hashes están en
`2026-09-14-fable-square-final-process.json`; las aclaraciones posteriores
se documentan aquí, sin atribuirles una segunda aprobación de Fable.

## Verificación local

- `python -m unittest discover -s code -p 'test_cuadrado_*.py' -v`:
  21 tests pasan tras las correcciones.
- Scripts exactos: D 17/17, gemelas 17/17, mejora finita 13/13 y
  aproximantes 39/39; 86 comprobaciones racionales en total.
- `lake build`, Lean 4.32.2, con `LEAN_NUM_THREADS=1`: éxito, ocho
  trabajos. Se reconstruyeron Square, SquareTwins, SquareLimit y la raíz.
- Recuento: 57 teoremas anteriores, 14 en Square, 7 en SquareTwins,
  3 en SquareLimit; 81 en total.
- Los resultados inspeccionados con `#print axioms` solo dependen de
  `propext`, `Classical.choice` y `Quot.sound`. No hay `sorry`, axiomas
  nuevos ni uso de `native_decide` en los tres módulos nuevos.
- `git diff --check` y comparación del directorio `paper/` con
  `v1-arxiv`: sin diferencias de contenido en el manuscrito.

Durante los primeros intentos Lean falló al leer distintos archivos
`.olean.private` instalados, aunque los archivos eran legibles. Al
reducir las importaciones y usar un hilo, la compilación completa pasó.
No se reinstaló el compilador ni se modificó la configuración del sistema.

## Continuación matemática y límites

Mientras se completaba la revisión se escribió
[`../drafts/cuadrado_limite.md`](../drafts/cuadrado_limite.md): una familia
aproximante prueba `tau_cuadrado≤Y≈1.684487745872346`. La continuidad y
la interpretación del bosque se prueban por escrito; Lean comprueba las
identidades algebraicas y el lema cartesiano que consume la familia.
Hay tres ejemplos enteramente racionales, hasta `rho=1.6844877458724`.

**Fuera de esta revisión externa:** gemelas cuadradas, mejora finita,
límite Y y G2–G7. Permanecen abiertas su revisión independiente y la
optimalidad de Y. No se afirma que Fable haya aprobado estos resultados
ni que la familia aproximante esté completamente formalizada.

El manuscrito enviado permanece intacto; los resultados siguen en
borradores separados para decidir su integración editorial.
