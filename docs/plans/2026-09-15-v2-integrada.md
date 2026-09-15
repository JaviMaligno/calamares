# Integración de la v2

**Goal:** entregar un artículo único con tau=phi, los extras revisados,
PDF legible y paquete de fuentes que compile de forma independiente.

**Architecture:** conservar `paper/main.tex` y el PDF del día 14 como
referencia. Crear `paper/v2/main.tex` con sus dependencias y figuras;
integrar el suplemento en `golden_global.tex` y los extras en
`extras_v2.tex`. Actualizar la narrativa del artículo y delimitar el
programa computacional anterior como trabajo especializado que ya no
es premisa del umbral global.

**Tech Stack:** LaTeX/MiKTeX, Poppler, Python, Lean 4.32.2.

**Risks:** referencias rotas, afirmaciones antiguas de conjetura global,
confundir resultados para discos con dimensión arbitraria, atribuir a
Fable revisión del nuevo texto inglés completo, perder figuras del bundle.

1. Copiar las dependencias estáticas mediante `collect_sources` del
   constructor existente. Integrar la prueba ya revisada, sin modificar
   sus hipótesis, y traducir las pruebas de área variable y hasta cinco
   aros. Conservar las afirmaciones dimensionales en su alcance revisado.
2. Revisar resumen, contribuciones, tabla de resultados, problemas
   abiertos, referencias al programa anterior y mapa Lean. Comprobar
   todas las etiquetas y citas mediante compilación y búsqueda textual.
3. Compilar `paper/v2/main.tex` hasta estabilizar referencias. Generar
   `output/pdf/calamares_v2_integrada.pdf`; renderizar e inspeccionar
   todas las páginas y corregir defectos de maquetación.
4. Crear `paper/arxiv-v2-integrada.tar.gz` con las fuentes referenciadas.
   Extraerlo bajo `tmp/pdfs/` y compilar allí para demostrar autosuficiencia.
   Ejecutar `lake build` y los controles de posiciones y área afectados.
5. Registrar resultados, revisión editorial y hashes en `docs/reviews/`;
   actualizar README con la entrega actual y verificar que los diez
   artefactos anteriores conservan sus hashes.

La revisión matemática independiente ya cubre las pruebas fuente; esta
integración requiere además revisión local de traducción, coherencia,
referencias y PDF. No se atribuirá a Fable un envío que no se haya hecho.

**Estado:** completados los cinco pasos. Entrega y evidencias en
`docs/reviews/2026-09-15-v2-integrada-validation.md`. La versión anterior
permanece intacta; el artículo integrado y su paquete se entregan en
rutas nuevas.
