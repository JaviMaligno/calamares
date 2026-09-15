# Validación de la prueba de los tres mayores

Fecha: 2026-09-15. Estado: prueba escrita completa, aceptada por Fable
tras dos revisiones estáticas, con las aclaraciones incorporadas.
El resultado cierra tau=phi para todo inventario finito en el disco,
incluyendo agujeros independientes. Lean formaliza parte del álgebra.

## Alcance matemático

`docs/drafts/tres_mayores.md` demuestra T3: para una lista finita
`a>b≥c≥r4≥…>0` con todas las colas acotadas por phi veces su radio,
la factibilidad en un disco depende solo de los tres radios mayores.
Dos construcciones cubren toda longitud de cola. Su aplicación a
`a1,…,ak,m,m` crea dos plazas para el intercambio de un pivote y
cierra tau=phi para inventarios finitos arbitrarios en el plano,
incluso con agujeros independientes. No se afirma una extensión dimensional.

La prueba usa geometría euclidiana escrita: intervalos angulares,
reducción de tres discos a la pared, existencia de un contenedor mínimo,
Descartes y la identificación del círculo opuesto, y ensamblaje de bosques.
Estos pasos no se deducen de haber compilado los certificados algebraicos.

## Lean

`lean/Calamares/ThreeCore.lean` contiene siete teoremas nuevos:

| Teorema | Afirmación comprobada |
|---|---|
| `arbelos_margin_identity` | Identidad polinomial del margen angular |
| `arbelos_margin_nonneg` | Signo del margen bajo la cota de masa |
| `gap_sum_identity` | Identidad de la suma de curvaturas opuestas |
| `gap_sum_margin` | Signo de esa identidad |
| `opposite_height_positive` | Signo auxiliar de altura; no prueba la disyunción de los dos huecos |
| `envelope_bounds` | Las cotas de cola permiten las envolventes e,V |
| `curvature_gap_to_radius` | La desigualdad de curvaturas implica c+d≥2beta |

Se ejecutaron la compilación directa y `lake build` desde `lean/`, con
`ELAN_HOME=C:/Users/Usuario/.elan` y `LEAN_NUM_THREADS=1`. Terminaron
con código 0; el registro conjunto
`2026-09-15-three-core-lean-build.log` informa
`Build completed successfully (15 jobs)` sin avisos ni errores.
Los siete `#print axioms` solo contienen `propext`, `Classical.choice`
y `Quot.sound`. La biblioteca suma 122 declaraciones de teoremas.

Lean comprueba identidades e implicaciones de anillos ordenados; no
formaliza T3, el teorema global ni la existencia de la colocación geométrica.

## Controles de posiciones

Comando:

```
python code/tres_mayores.py --output docs/reviews/2026-09-15-three-core-controls.json
```

El script construye todos los centros mediante fórmulas explícitas y
una función separada comprueba cada pared y cada par de discos. No usa
un optimizador. Pasaron 10 000 listas aleatorias y seis casos de frontera:
9 617 usaron el par diametral y 389 el trío tangente. La mayor violación
relativa fue `2.073254767779225e-15`, inferior a la tolerancia `1e-9`.
Dos controles negativos detectan una posición inválida y una entrada
que excede la presión áurea. Los controles numéricos no prueban T3.

La figura `output/figures/tres_mayores_candidato.svg`, también en PNG,
ilustra ambos casos; se inspeccionó visualmente. Sus discos auxiliares
representan envolventes geométricas de filas, no cambios de inventario.

## Revisión externa

Se enviaron los paquetes autorizados expresamente por el usuario:

- `2026-09-15-fable-uniforme-manifest.json`: diez fuentes o extractos
  sobre intercambio, partición y reducción estructural.
- `2026-09-15-fable-three-core-manifest.json`: la prueba candidata y
  `ThreeCore.lean`, junto a cuatro dependencias ya autorizadas.
- `2026-09-15-fable-three-core-final-manifest.json`: los mismos seis
  archivos del segundo paquete, con las precisiones solicitadas en
  el primer dictamen incorporadas a la nota.

Los manifiestos y sus archivos metadata registran el contenido exacto,
sus hashes y la autorización. Claude Code/Fable recibe los textos para
revisión estática, sin herramientas para ejecutar Lean o Python.
La revisión amplia uniforme agotó dos límites sin dictamen y se detuvo;
su estado está en `2026-09-15-fable-uniforme-status.md`. No se atribuye
revisión externa al núcleo histórico de 40 mayores, que el cierre no usa.

Las dos revisiones de tres mayores terminaron con código 0. La primera
encontró tres omisiones de justificación, atendidas mediante inversión,
el paso a pared y el reparto explícito de plazas. La segunda acepta la
prueba completa y reaudita además las dependencias efectivas del
intercambio. Sus tres aclaraciones finales están incorporadas y
documentadas en `2026-09-15-fable-three-core-final-response.md`.
El dictamen original se conserva íntegro, incluida una desigualdad
estricta accidental que la respuesta identifica y que la prueba no usa.

El resultado tau=phi combina esta garantía con la cota superior ya
probada y revisada en la v2. Fable no hizo una nueva revisión de esa
familia superior ni afirmó novedad bibliográfica.

## Suplemento y control de entrega

`paper/golden_threshold.tex` reúne la prueba en inglés, en un suplemento
independiente de seis páginas: `output/pdf/golden_threshold.pdf`.
Se compila con dos pasadas de pdflatex y se inspeccionan las seis páginas
renderizadas con Poppler. La revisión externa se hizo sobre la prueba
española y sus dependencias; el texto inglés se preparó y revisó localmente.

Los diez artefactos de la v2 conservan los hashes de
`2026-09-14-v2-artifacts.json`. `git diff --check` pasa. Se comprueba
el recuento de 122 teoremas y la ausencia de admisiones, axiomas nuevos
y `native_decide` en el código Lean, excluyendo comentarios del análisis.
El manifiesto `2026-09-15-three-core-artifacts.json` registra las fuentes,
los informes y los resultados finales. Los cambios posteriores al último
envío consisten en las tres aclaraciones solicitadas y actualizaciones
de estado; no cambian las siete pruebas Lean.
