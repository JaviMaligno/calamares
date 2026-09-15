# Certificado del contraejemplo cuadrado Implementation Plan

**Goal:** Probar un fallo realizable del voraz en cuadrado con rho < X,
con certificado exacto comprobado en Lean dentro del alcance disponible.

**Architecture:** Buscar primero una cota geométrica escrita para excluir
el trío grande-pequeño-pequeño. Usar radios y lado racionales, un testigo
explícito de cuatro aros y certificados aritméticos separados de la
geometría. Si la cota no basta, recurrir a subdivisión exacta de cajas.

**Tech Stack:** Python 3, fractions/sympy; Lean 4.32.2 core sin mathlib.

**Risks:** El máximo insertable numérico no demuestra infactibilidad.
La ampliación racional del lado debe preservar el bloqueo y admitir el
testigo. Lean debe declarar con precisión el alcance de lo certificado.

## Pasos

1. Derivar en `docs/drafts/cuadrado_certificado.md` un lema de confinamiento
   por cuadrantes. Probar primero la instancia E, con lado racional
   superior al lado mínimo del par. Intentar después D si la cota alcanza.
2. Escribir controles positivos, negativos y de frontera en
   `code/test_cuadrado_certificado.py`; ejecutar y observar el fallo por
   certificado aún no implementado. Implementar la comprobación exacta
   en `code/cuadrado_certificado.py`; ejecutar los controles.
3. Formalizar los certificados en `lean/Calamares/Square.lean`, importado
   desde `lean/Calamares.lean`. Comprobar con `lake build`, sin `sorry`
   ni `native_decide`, e inspeccionar `#print axioms`.
4. Escribir todas las asignaciones del voraz y del testigo; comprobar las
   paredes de anidamiento, rho y la comparación exacta con X. Documentar
   cualquier límite de la formalización y cualquier objetivo aún abierto.
5. Actualizar `docs/generalizaciones.md`, el borrador cuadrado y
   `lean/README.md`. Corregir la hipótesis individual de la fila diagonal
   en su enunciado. Ejecutar `python -m unittest discover -s code -p
   test_cuadrado_certificado.py`, `python code/cuadrado_certificado.py`,
   `lake build` desde `lean/` y `git diff --check`.

No se integra en `paper/main.tex` hasta revisar el nuevo bloque completo.

## Resultado de la ejecución (2026-09-14)

- Alcanzado el objetivo con la instancia D y lado racional `6071/1250`:
  `rho=337/200=1.685<X`. No hizo falta subdivisión de cajas.
- Prueba escrita del lema paramétrico de confinamiento por cuadrantes;
  infactibilidad cartesiana de D formalizada para todas las coordenadas
  en un anillo conmutativo linealmente ordenado, incluidas las reflexiones.
- `Square.lean`: 11 teoremas. Los ocho teoremas principales inspeccionados
  con `#print axioms` solo usan los tres axiomas estándar de Lean.
- TDD observado: primero fallaron D, E y el rechazo de floats; después
  falló el test del conjunto completo de paredes. Tras implementar las
  comprobaciones pasan los 9 tests y las 16 condiciones racionales.
- `lake build`: completado correctamente, 6 trabajos. `git diff --check`
  sin errores. El runner estándar incluye el certificador nuevo.
- Actualización tras revisión: Fable confirmó el bloque D y el Lema Q
  mediante auditoría estática, con una aclaración menor del testigo ya
  incorporada. Python añade una pared de orden/grosor: ahora 17/17.
  No se ha incorporado al manuscrito enviado.
