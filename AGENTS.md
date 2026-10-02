# AGENTS.md — El problema de los calamares (Nested Ring Packing)

Repositorio de investigación matemática (repo personal, GitHub público): empaquetamiento de aros de grosor w con anidamiento recursivo en una sartén circular. Contiene el borrador del artículo, los documentos de trabajo con las demostraciones y los scripts Python que verifican cada afirmación. Ver `README.md` para el resumen de resultados y el mapa script → afirmación.

## Estructura

- `paper/main.tex` — borrador del artículo (en inglés, orientado a arXiv). `main.pdf` / `calamares_draft.pdf` son compilaciones.
- `docs/resultados.md` — documento de trabajo principal (español): modelo, lemas, teoremas con demostraciones, contraejemplos.
- `docs/hoja_de_ruta.md` — pendientes con estado, esqueleto de ataque y criterio de éxito (autocontenido).
- `docs/reinsercion.md`, `docs/generalizaciones.md` — lema de reinserción y generalizaciones.
- `docs/drafts/` — borradores de resultados (`suelo_rigido.md`, `h1.md`, `grosor_positivo.md`, `esquina.md`, `universal.md`, `cuadrado.md`, ...).
  - `docs/drafts/VEREDICTOS.md` — acta de verificación adversaria de cada borrador.
  - `docs/drafts/ESTADO_SESION.md` — documento de traspaso entre sesiones: leerlo primero al retomar el trabajo.
- `code/` — scripts de verificación reproducibles, uno por resultado (ver el mapa en `README.md`).
- `figures/` — figuras PNG usadas en el artículo.

## Comandos

```bash
# Dependencias (requirements.txt solo lista numpy y matplotlib;
# varios scripts necesitan además sympy: cuadrado, cuatrok, esquina, grosor, h1, rigido, tresk, universal)
pip install -r code/requirements.txt sympy

# Ejecutar un script de verificación (importan módulos hermanos: ejecutar desde code/)
cd code && python rigido.py

# Compilar el artículo (dos pasadas)
cd paper && pdflatex main.tex && pdflatex main.tex
```

No hay suite de tests ni runner: cada script es autocontenido, imprime sus comprobaciones por bloques y se ejecuta directamente. `test_oblivious.py` es también un script, no un test de pytest.

## Convenciones

- Idioma: documentos de trabajo, comentarios de código y mensajes de commit en español; `paper/main.tex` en inglés.
- Cada afirmación nueva debe ir respaldada por un script en `code/` y añadirse al "Mapa de verificación" de `README.md`.
- Los scripts reutilizan el núcleo compartido: `sim.py` (`pack_feasible`, solver de factibilidad), `reinserta.py` (`feas`, `feas3`, constantes `TRIB`, `PHI`), `trio.py`, `superinc.py`.
- El docstring de cabecera de cada script enumera sus bloques ([A], [B], ...) y qué borrador de `docs/drafts/` respalda; marcar explícitamente las exploraciones sin estatus.
- Los resultados se consideran cerrados solo tras verificación adversaria independiente (rehacer el álgebra con sympy, ejecutar el script, buscar contraejemplos dirigidos) registrada en `docs/drafts/VEREDICTOS.md`. Lo cerrado no se retoca.
- Al cerrar una sesión de trabajo, actualizar `docs/drafts/ESTADO_SESION.md` y `docs/hoja_de_ruta.md`.

## Gotchas

- `viz.py`, `franja.py` y `figrefuta.py` guardan las figuras en la ruta fija `/mnt/user-data/outputs/`; para regenerar `figures/` hay que cambiar esa ruta o crearla.
- `.gitignore` excluye artefactos de LaTeX en `paper/` y `__pycache__/`.
