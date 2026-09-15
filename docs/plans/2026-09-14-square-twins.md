# Continuación del cuadrado: revisión, cota y gemelas

Fecha: 2026-09-14. Autorizado por el usuario: revisión independiente con
Claude Code/Fable y continuación del trabajo, usando Lean cuando sea viable.

1. Revisar el bloque D con Fable en dos fases, rederivación y auditoría.
   Tras el primer rechazo automático, el usuario autorizó expresamente
   el envío de los archivos enumerados. La revisión está concluida:
   D, Q y G1 confirmados, con una corrección menor de redacción atendida.
   Su registro distingue la auditoría estática de la compilación local.
2. Generalizar la prueba Lean de confinamiento a los parámetros del Lema Q.
   Mantener el teorema D como instancia, con su interfaz original.
3. Probar gemelas de prefijo `a=2,m=1,w=.301,s=5.1214`, con colas
   `{.850,.849}` y `{.950,.750}`. Certificar los dos tríos infactibles,
   el testigo factible y las cuatro ejecuciones completas.
4. Optimizar la familia certificada: distinguir una nueva instancia
   racional demostrada de un candidato a ínfimo todavía exploratorio.
5. Guardar pruebas y verificaciones en `docs/drafts/cuadrado_gemelas.md`,
   `code/cuadrado_gemelas.py`, `code/test_cuadrado_gemelas.py` y
   `lean/Calamares/SquareTwins.lean`; actualizar el mapa y ejecutar tests,
   scripts, `lake build`, inspección de axiomas y `git diff --check`.

Las observaciones del revisor se comprobarán antes de aplicar cambios.
No se integra ni publica el manuscrito durante esta revisión.

## Resultado del trabajo local

- Lema Q formalizado con parámetros arbitrarios, incluidas las reflexiones.
- Gemelas probadas: los cuatro recorridos exactos devuelven 3/4/4/3 aros.
- Cota mejorada demostrada `tau_cuadrado ≤ 168449/100000 = 1.68449`.
- Bloque cuadrado: 14 teoremas en Square y 7 en SquareTwins; compilación
  conjunta correcta, solo axiomas estándar en los resultados inspeccionados.
- 18 tests pasan; scripts exactos: D 16/16, gemelas 17/17, mejora 13/13.
- `Y≈1.684487745872346` y su cuártica se registran como exploración,
  sin afirmar que Y sea una cota demostrada ni un ínfimo.
- Revisión Fable de D concluida, corrección menor atendida. Informe,
  respuesta y alcance en `docs/reviews/2026-09-14-fable-square-*.md`.
  Las gemelas y la mejora no se incluyeron en esa revisión externa.
