# Intercambio residual y revisión independiente

**Estado final:** completado el 2026-09-15. T3 y el reparto de dos plazas
cierran tau=phi para inventarios finitos arbitrarios en el disco, incluso
con agujeros independientes. Fable acepta la prueba y dependencias tras
dos revisiones; siete certificados nuevos compilan en Lean. Suplemento
separado en `paper/golden_threshold.tex`, con PDF y validación registrada.
La revisión amplia del núcleo se sustituyó por la revisión focalizada
del cierre y no se atribuye aceptación externa a la cota de 40 mayores.

**Goal:** cerrar el intercambio uniforme si se encuentra una prueba válida,
o aislar una obstrucción precisa, con verificación independiente de Fable.

**Architecture:** revisar el núcleo ya escrito en paralelo con el estudio
local de una extensión geométrica: añadir dos discos m a un contenedor
con al menos dos ocupantes mayores y presión de colas áurea. La geometría
puede reconstruirse conservando padres. Una búsqueda numérica sirve para
descartar construcciones, no para certificar imposibilidad universal.

**Tech Stack:** Lean 4.32.2 core, geometría escrita, Python/SciPy cuando
ayude a encontrar testigos, Claude Code/Fable para revisión estática.

**Risks:** confundir dos plazas suficientes con necesarias; confiar en
un fallo de optimización como prueba de imposibilidad; usar solo áreas
ocupadas ignorando exclusiones; perder padres mayores al recolocar;
presentar una cota de prefijo como una cota de inventario completo.

## Trabajo

1. Preparar `docs/reviews/2026-09-15-fable-uniforme-manifest.json` con
   fuentes exactas y la autorización de la petición actual. Ejecutar
   `python docs/reviews/run_fable_review.py <manifest> prepare` y `run`.
   La revisión debe distinguir pruebas aceptadas, errores y sugerencias
   de investigación, y no afirmar que ejecutó Lean.
2. Investigar el lema de extensión simultánea de dos plazas, incluyendo
   las restricciones de colas de todos los hermanos. Contrastar con las
   notas existentes y buscar una construcción uniforme o un contraejemplo
   exacto al lema auxiliar. Conservar cualquier conclusión en una nota.
3. Formalizar en Lean las nuevas identidades o implicaciones comprobables.
   Ejecutar la compilación directa y `lake build` tras el último cambio.
4. Extraer el dictamen de Fable, comprobar cada hallazgo y corregir las
   notas cuando corresponda. Si surge una prueba nueva sustancial, pedir
   una revisión de seguimiento bajo esta misma solicitud del usuario.
5. Registrar alcance y hashes, conservando los diez artefactos de v2.
   Si no se cierra tau=phi, precisar el punto matemático abierto.
