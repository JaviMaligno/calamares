# Validación de la v2 integrada — 2026-09-15

## Entrega y alcance

El artículo unificado está en `paper/v2/main.tex`, con la prueba global
en `golden_global.tex`, las generalizaciones anteriores en
`generalizations_v2.tex` y las extensiones de cinco aros y área variable
en `extras_v2.tex`. La entrega es `output/pdf/calamares_v2_integrada.pdf`
(73 páginas, incluidos apéndices y referencias), acompañada de
`paper/arxiv-v2-integrada.tar.gz`.

Integra el umbral global **tau=phi** para cualquier inventario finito de
radios estrictamente decrecientes en el disco, incluso con agujeros
independientes. Conserva la extensión hasta cinco aros para bolas de
toda dimensión d≥2, la cota Y y las gemelas cuadradas, y añade la prueba
de la garantía exacta de área `min(1,kappa^(-2)-1)` y su umbral `1/sqrt(2)`.
El resultado global en dimensiones superiores no se afirma aquí.

## Revisión matemática y editorial

La prueba global procede de los argumentos aceptados en
`2026-09-15-fable-three-core-final-review.md`, con las aclaraciones
de `2026-09-15-fable-three-core-final-response.md` incorporadas.
Las pruebas de cinco aros y área variable proceden de los borradores
revisados en `2026-09-15-fable-extras-review.md` y su respuesta.
Las revisiones del día 14 cubren las extensiones anteriores.

Esta integración recibió revisión **local** de la traducción inglesa,
hipótesis, dependencias, notación, referencias cruzadas, resumen,
contribuciones, conclusiones y problemas abiertos. No se hizo un nuevo
envío a Fable del manuscrito inglés completo ni se le atribuye ese dictamen.

El antiguo programa de casos especializados conserva sus resultados y
límites computacionales históricos. No es premisa del teorema global.
Los problemas abiertos distinguen la cota más fuerte de las familias
anidadas, la optimalidad de Y, la extensión dimensional global y otras
preguntas de complejidad y objetivos. Se actualizó el mapa de verificación
y se eliminó la presentación del umbral global como conjetura pendiente.

## Compilación y revisión visual

`python paper/build_v2.py --verify-bundle` compila el manuscrito y el
paquete extraído en un directorio nuevo. El registro
`2026-09-15-v2-integrada-build.json` recoge los hashes, las pasadas y los
siete archivos necesarios. La compilación final no tiene referencias
pendientes, advertencias LaTeX ni cajas desbordadas o insuficientemente llenas.

Se renderizaron e inspeccionaron las 73 páginas con Poppler: texto,
ecuaciones, figuras, tablas, apéndices y bibliografía. Las páginas que
cambiaron en los últimos ajustes se volvieron a inspeccionar; las demás
se comprobaron idénticas mediante hashes de los PNG renderizados.
Las imágenes de trabajo están en `tmp/pdfs/v2-integrada/`.

Correcciones visuales: tres figuras regeneradas con rótulos ingleses
legibles; eliminación de títulos superpuestos y del aro rechazado dibujado
fuera de la sartén; etiquetas del esquema de intercambio recolocadas;
enlaces activos sin recuadros de colores; eliminación de un encabezado
vacío y de letras de enumeración residuales; inicio del teorema global
en página nueva para mantener completo su enunciado.
`paper/render_v2_figures.py` conserva los parámetros matemáticos de las
figuras históricas y usa centros explícitos para el testigo de divergencia.

## Controles ejecutados

- `lake build`, Lean 4.32.2: éxito, 15 trabajos; 122 teoremas en el
  repositorio. Registro: `2026-09-15-v2-integrada-lean.log`.
- `code/tres_mayores.py`: 10 000 listas aleatorias, seis casos de
  frontera y dos controles negativos; éxito. Máxima violación relativa
  de coma flotante: `2.073254767779225e-15`.
- `code/grosor_variable.py`: 15/15 controles racionales exactos.
- `test_grosor_variable.py`: 11 pruebas superadas.
- `test_make_arxiv_bundle.py`: cuatro pruebas superadas.
- `git diff --check`: sin errores.

Los comandos y sus salidas se conservan en
`2026-09-15-v2-integrada-controls.json`. No se repitió la campaña histórica
completa de varias horas: esta revisión no modifica sus resultados.
El muestreo numérico no constituye una demostración universal.
Lean certifica álgebra y predicados cartesianos; la geometría euclidiana,
la inversión, la compacidad y el ensamblaje de bosques siguen siendo
demostraciones escritas, no una formalización completa del artículo.

## Conservación y estado

Los diez artefactos de `2026-09-14-v2-artifacts.json` conservan sus hashes:
PDF y bundle anteriores, las dos fuentes TeX, cuatro módulos Lean y dos
revisiones. El manifiesto `2026-09-15-v2-integrada-artifacts.json` identifica
la entrega actual. La revisión está lista para lectura; no se ha publicado
en arXiv ni se ha hecho commit, merge o push en esta tarea.
