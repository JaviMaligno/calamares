# Segunda revisión de tres mayores e intercambio global

Modelo: `claude-fable-5-1`. Revisión externa estática mediante Claude Code: no ejecutó Python ni Lean. Alcance y hashes en el manifiesto y metadata `2026-09-15-fable-three-core-final`. El dictamen se conserva íntegro.

---

Dictamen sobre la versión adjunta, leída estáticamente. No he ejecutado Lean ni Python; los enunciados Lean se comparan solo con el texto.

**Veredicto: los argumentos presentes son correctos y el cierre no tiene huecos matemáticos reales.** Con las precisiones incorporadas, la cadena lema A, lema B, lema C, T3, reparto de plazas en §5, más C1/C2 y la reducción al prefijo máximo, prueba que con `rho<=phi` no existe primera omisión del voraz en un inventario finito factible de radios estrictamente decrecientes, disco y agujeros independientes. Lo que sigue son aclaraciones de redacción, no errores.

Comprobaciones hechas:

- **Lema A.** Las dos cotas angulares por ley de cosenos, la equivalencia `X²+Y²<=1 ⇔ x<=beta`, la separación mínima `2 asin(AB)` y la reducción a (A1) son correctas. La identidad del margen coincide con `arbelos_margin_identity` y el signo con `arbelos_margin_nonneg`. La contención en el semiplano abierto superior y la disyunción con el bolsillo inferior de ordenada `-2beta` están bien justificadas.
- **Lema B.** El desplazamiento a pared, la caracterización por suma de huecos angulares, el paso `R0=a+b ⇒ c<=beta` con c llevado a pared dejando a,b fijos, y la elección de la raíz positiva de Descartes son correctos.
- **Lema C.** La inversión en el punto de tangencia envía los interiores de a,b a los semiplanos exteriores de la franja y el interior del contenedor al exterior de un círculo tangente a ambas rectas. Las dos soluciones equidistantes sobre la recta media son disjuntas y quedan en componentes distintas de la franja menos ese círculo, luego c y d están en huecos distintos. Con `1/R0=2t-S-C` las dos raíces de Descartes son `C` y `4S+C-4t`, distintas porque `t<S`, lo que confirma la orientación y el uso de la reflexión clásica. La identidad (C2) está verificada a mano y coincide con `gap_sum_identity`; el paso a radios coincide con `curvature_gap_to_radius`.
- **T3.** (T1) sale de `tail_le_double_pocket` con `a>b`. El caso `c>beta` usa `d>=2beta-c>=U`. El caso `c<=beta` obtiene `e<=c<=beta`, `V<=c<=beta`, `e+V<=b` como en `envelope_bounds` y aplica el lema A correctamente. Las plazas iguales al final de la lista están permitidas por las hipótesis.
- **§5.** Las colas de la lista auxiliar están acotadas por las originales porque `2m<m+T`. Los casos `w!=u` con `w=v` reconstruido sin tercera plaza, y `w=u` con U en la bola vacante de v, colocan todo el inventario respetando los padres mayores y el de m. El ensamblaje por contenedor con subárboles rígidos es válido aunque haya antecesores. El reparto grado `>=3` T3, grado 2 C2, cadena C1 es exhaustivo.
- **Dependencias.** En `particion_bolsillos.md` verifiqué a mano las identidades de `golden_balance`, la cota `T<=2beta`, el invariante `|u-v|<=p` de la partición y las dos construcciones de C1 y C2, incluido `min(U,V)<T/2<m`. En `intercambio_uniforme.md` la cota `U<=m`, la restricción al prefijo `G∪{x}` y el intercambio por fila si `T<=m` son correctos.

Aclaraciones necesarias, todas de una línea:

1. **Semántica del voraz.** El paso "si no hay desacuerdo, el testigo admite el último aro en F" requiere que el voraz falle solo cuando ningún contenedor hace factible el bosque extendido, no cuando unas coordenadas ya fijadas lo impiden. Conviene enunciarlo explícitamente, pues no aparece en los ficheros adjuntos.
2. **Retorno de la inversión.** Justificar que las imágenes inversas de las dos soluciones son discos: sus interiores caen en el espacio libre acotado, luego ninguna circunferencia pasa por el centro de inversión.
3. **Identificación de d.** Indicar que la reflexión clásica se aplica porque la inversión muestra exactamente dos discos admisibles y las dos raíces son distintas.

Distinción escrito/formal: Lean certifica solo identidades y signos en anillos ordenados. Inversión, colocación angular, compacidad, Descartes, la partición como piezas y el bosque siguen siendo prueba escrita. Con eso, y sin reauditar la familia superior de v2, el resultado de esta nota es una prueba escrita completa de la garantía universal `rho<=phi`.
