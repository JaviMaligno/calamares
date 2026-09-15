# Acta de verificación de la v2

Fecha: 2026-09-14. Estado: revisión local completa y compilada, con
revisiones independientes atendidas. No se ha publicado ni creado un
tag de release. Los hashes de los artefactos finales están en
[`2026-09-14-v2-artifacts.json`](2026-09-14-v2-artifacts.json).

## Resultados integrados

- `prop:n3`: hasta tres aros en cualquier contenedor compacto y dimensión.
- `thm:fourfloor`: `tau_4=phi`, todo fallo tiene `rho>phi`, ínfimo no
  alcanzado; prueba por reducción exhaustiva a dos casos de bosque.
- `lem:dimreduce` y `cor:dimsharp`: reducción de k bolas a dimensión
  k−1; transferencia esférica y `tau_(4,d)=phi` para d≥2.
- `prop:dimfour`: ejemplo explícito de cuatro hermanos factibles en
  dimensión tres e infactibles en el plano.
- `lem:squareQ`, `prop:squareD`, `thm:squaretwins`: confinamiento
  cartesiano, fallo exacto D y gemelas cuadradas.
- `thm:squarelimit`: familia aproximante racional y cota
  `tau_cuadrado≤Y≈1.684487745872346`.

El umbral universal `tau=phi` y la optimalidad de Y quedan abiertos.
Los residuos actuales y el siguiente obstáculo del quinteto están
documentados en `docs/drafts/umbral_v2_auditoria.md`.

## Verificación ejecutada

| Comprobación | Resultado |
|---|---|
| Lean 4.32.2, `lake build`, `LEAN_NUM_THREADS=1` | Salida 0; 9 trabajos, 84 teoremas en los módulos |
| `FourRing.lean`, ejecución directa y `#print axioms` | Tres teoremas; solo `propext`, `Classical.choice`, `Quot.sound` |
| `python -m unittest discover -s code -p 'test_cuadrado_*.py' -v` | 21/21 |
| `python -m unittest discover -s paper -p 'test_make_arxiv_bundle.py' -v` | 4/4 |
| `code/cuadrado_certificado.py` | 17/17 comprobaciones racionales |
| `code/cuadrado_gemelas.py` | 17/17, incluidas las cuatro ejecuciones |
| `code/cuadrado_optimizado.py` | 13/13 |
| `code/cuadrado_limite.py` | 39/39 sobre tres aproximantes racionales |
| LaTeX del manuscrito | Salida 0; 66 páginas; pasada final sin avisos, referencias pendientes ni cajas desbordadas |
| `paper/make_arxiv_bundle.py` | Cinco miembros esperados, verificación OK |
| Extracción y compilación independiente del bundle | Ambos TeX idénticos a las fuentes; salida 0, 66 páginas, pasada final limpia |
| `git diff --check` | Salida 0 |

El bundle contiene `main.tex`, `generalizations_v2.tex` y las tres
figuras referenciadas. La compilación independiente se hizo a partir
exclusivamente de esos cinco archivos, desde
`tmp/pdfs/v2-bundle-check/`. Los tests del empaquetador cubren archivos
incluidos recursivamente, figuras compartidas, ciclos, comentarios,
entradas ausentes y rechazo de rutas que salen de `paper/`.

Se renderizaron las 66 páginas mediante Poppler a PNG. Se inspeccionaron
las once hojas de contacto completas y, en detalle, las páginas
1, 3, 6, 11, 20–24, 27 y 64. Se corrigieron los desbordamientos de las
filas nuevas del mapa y del párrafo de casos pendientes. El resumen
se condensó para evitar que continuase en una segunda página.
El PDF entregable coincide por hash con el PDF inspeccionado.

Artefactos: `output/pdf/calamares_v2.pdf` y
`paper/arxiv-bundle.tar.gz`. Los renders y logs locales de compilación
se conservan en `tmp/pdfs/` (ignorados por Git).

## Revisión independiente y alcance

Claude Code resolvió el alias `fable` a `claude-fable-5-1`. Ambos
procesos nuevos terminaron con código 0 y resultado final satisfactorio.

- Generalizaciones: acepta dimensión y Y; revisión menor para
  explicitar la admisión del primer pequeño en las gemelas. Corregida,
  junto con las precisiones de referencias y alcance de Lean.
- Cuatro aros: **ACEPTAR**, tras verificar la enumeración de padres,
  los dos casos y las dependencias; cinco precisiones no bloqueantes
  incorporadas al manuscrito.

Los dictámenes son estáticos sobre los payloads y hashes registrados,
anteriores a esas aclaraciones editoriales. No constituyen una
ejecución externa de Lean/Python ni una revisión de todo el histórico.
No se ha repetido la campaña histórica de varias horas. El bosque,
la interpretación euclidiana, la reducción dimensional y la continuidad
siguen siendo pruebas escritas; Lean comprueba las afirmaciones
algebraicas y cartesianas declaradas en su mapa.
