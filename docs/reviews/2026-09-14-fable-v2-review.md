# Revisión independiente de las generalizaciones para la v2

Modelo: `claude-fable-5-1`. Revisión externa estática mediante Claude Code: no ejecutó Python ni Lean. Alcance y hashes en el manifiesto y metadata `2026-09-14-fable-v2`. El dictamen se conserva íntegro.

---

Reviso estáticamente G2–G7, el ejemplo 3D/2D, las gemelas cuadradas y la cota Y, comprobando a mano las desigualdades racionales y la lógica de cada ejecución. No he ejecutado Python ni Lean; toda afirmación sobre esos artefactos es lectura del código.

## Veredictos por bloque

| Bloque | Veredicto |
|---|---|
| G2–G3, reducción dimensional | Aceptar |
| G4, transición 3/4 | Aceptar |
| G5, gemelas esféricas en dimensión d | Aceptar |
| G6, suelo Tribonacci | Aceptar |
| G7, `1 ≤ τ_d ≤ φ` | Aceptar, con una dependencia que debe citarse |
| Ejemplo 3D/2D de §4 | Aceptar |
| Gemelas cuadradas y cota 1.68449 | Revisión menor |
| Cota límite Y | Aceptar, con notas de alcance |

No encontré contraejemplos ni hipótesis ausentes que invaliden ningún resultado. Los hallazgos son omisiones de redacción y precisiones de alcance.

## Hallazgos

1. **Pared omitida en las gemelas cuadradas.** `docs/drafts/cuadrado_gemelas.md:106` afirma que, con `m` anidado, el tercer aro va a la sartén "ya que sus alternativas de agujero están excluidas". Falta el hecho positivo: la raíz debe admitir `{2,.850}` y `{2,.950}` junto al `2`. Sin él, la ejecución I2 best podría colocar solo tres aros y la tabla de §4 no estaría justificada. El hecho es cierto, se deduce del par de raíz `{2,1}` reduciendo el radio del `1` con el mismo centro, y el oráculo de `code/cuadrado_gemelas.py:43` lo comprueba con el criterio exacto de dos discos en cuadrado. Reparación mínima: añadir en §3 la frase "reduciendo el disco `1` del par de raíz, `{2,z}` cabe en la sartén para `z<1`", y opcionalmente una línea en `twin_walls`. Esta es la razón de la revisión menor.

2. **Dependencia no citada en G7.** `docs/drafts/generalizacion_dimensional.md:169` deriva `τ_d ≥ 1` del teorema de superincrecencia débil. Eso exige que `thm:oblivious` valga en dimensión arbitraria, lo que `paper/main.tex:223-225` declara pero la nota no cita. Reparación: remitir explícitamente a esa cláusula del modelo.

3. **Consulta de tres hermanos no cubierta por V2 literal.** En la ejecución I1 worst de G5, el aro `4.50` consulta la raíz con `{10,5,4.50}`. `paper/main.tex:4437-4445` solo calcula `z∈{4.74,4.76}`; la exclusión de `z=4.50` sale de la fórmula general `z²−130z+625<(5+z)²` para `z>30/7` de `paper/main.tex:487`, que verifiqué para `z=4.5`. Además el conteo de cuatro es robusto a la respuesta. La nota debería mencionarlo para que el inventario de consultas de tres hermanos sea completo. Mejora, no error.

4. **Instanciación real de Lean.** `docs/drafts/cuadrado_limite.md:99-101` dice que `Square.excluded_of_conditions` "permite parámetros reales". La afirmación es correcta matemáticamente: el teorema vale en todo anillo conmutativo linealmente ordenado. Pero el proyecto no importa Mathlib y no exhibe instancia alguna de `ℝ` para las clases de `Init.Grind`. Conviene decir "vale para ℝ como caso particular del enunciado abstracto; Lean no instancia ℝ". Precisión de alcance.

5. **Hipótesis aparentemente redundante en Q.** En `lean/Calamares/Square.lean:90` la condición `s−b−c ≤ p+q` no interviene en la derivación de `no_normalized`: las cotas de `|bx−cx|` salen de `bx ≤ s−b`, `cx > a+q`, `cx ≤ s−c`, `bx > a+p`, más `c ≤ b` y `q ≤ p`. Como es hipótesis, no daña la corrección. Mejora opcional: eliminarla o justificar su papel en la versión escrita del lema.

## Afirmaciones confirmadas

**G2.** La traslación común `ci ↦ ci−q` es una isometría, así que ninguna distancia se reduce. La contención usa `(ci−q) ⊥ q`, cierto porque `q` es la proyección ortogonal del origen sobre la envolvente afín. La elevación por ceros es trivial. Correcto para `d ≥ k−1`; comprobé también el caso `k=2, d=1`.

**G3 y ensamblaje del bosque.** Los hijos viven en la bola interior de su padre, contenida en la bola exterior, y las exteriores de hermanos tienen interiores disjuntos. Correcto.

**G4.** Enumeré la ejecución best fit. Las consultas son: dos de una bola, dos de dos bolas y una de tres, `{10,4.9,4.8}`. La prueba de `lem:cap` en `paper/main.tex:431-443` es ya coordenada-libre, así que la transferencia está doblemente asegurada.

**G5.** Las consultas de tres hermanos en las cuatro ejecuciones son exactamente `{10,4.99,4.50}`, `{10,5,4.99}`, `{10,5,4.50}`, `{10,4.76,4.74}`, `{10,5,4.76}`, `{10,5,4.74}`; todas las demás son de una o dos bolas. Estado idéntico al decidir el `5`, ambos contenedores factibles, pasos posteriores forzados, fallos con probabilidad `1−p` en I1 y `p` en I2.

**G6.** F1 y F2 escalares, F3 es una consulta de tres bolas. Familia de parámetros y función `ρ` idénticas; la cota estricta y la sucesión aproximante se heredan.

**G7.** El testigo áureo usa una corona de tres hermanos y un anidamiento simple; los rechazos son `{φ,1,s1}` y `{φ,1,s2}`, ambos de tres hermanos. Las reservas de la nota sobre `τ_d=τ_2` son correctas.

**Ejemplo 3D/2D.** Verifiqué las fracciones: `5281/10^6`, `10319/250000` y `16961/125000`. Como todas las normas y distancias del tetraedro coinciden, basta probar radio máximo y suma máxima. El argumento angular en 2D es correcto, incluido el caso de un centro en el origen.

**Gemelas cuadradas.** Comprobé a mano las nueve condiciones de `Conditions` para los dos certificados de `lean/Calamares/SquareTwins.lean:16-23` y las tres cajas y tres márgenes del testigo de la línea 28. Los márgenes decimales de `cuadrado_gemelas.md:64-66` son exactos. Las cuatro ejecuciones coinciden con los padres esperados en `code/cuadrado_gemelas.py:92-93` y todos los pasos posteriores al decisivo son forzados. Colas `1.699` y `1.700`, ambas bajo `X>1.7`.

**Instancia 1.68449.** Recalculé las condiciones Q con enteros a escala `10^8`. Los márgenes de Q2 y Q3 son de orden `1.2·10^-7` y `8·10^-8`, positivos; el par de raíz tiene margen `4·10^-8`. Todas las paredes de `improved_gates` son ciertas.

**Cota Y.** Verifiqué que `G` coincide con `balanced_gap_identity` y con el desarrollo a mano; signo negativo en `21/25` con `k>7/5` y positivo en `17/20` con `k<10/7`; monotonía por coeficientes positivos. En la familia perturbada: Q1 exacta con margen `η`, Q4 identidad, Q2, Q3, Q5, `a<s/2` y `p>0` por continuidad tras elegir `η0(t)` para un conjunto finito; orden `a>1>b>c>w>0` bajo `η<t`, `η<1−t`, `3η<2t−1`. Best fit anida `1` porque `2t<1+t<a<s/2`; las cinco exclusiones de agujero tienen los márgenes indicados. Cola dominante `2t` porque `2t²>1`. Dirección del ínfimo correcta: fallos con `ρ=2t ↓ Y`. La familia racional de §4 conserva Q1 y Q4 exactamente y las estrictas por continuidad en `s`. Las tres filas de la tabla son consistentes con un análisis de derivadas: el margen de Q3 decrece con `η` a razón aproximada de `10.5`, y `G(t)` crece a razón aproximada de `12.5` en `t−t0`, así que `η` una o dos décadas menor que `t−t0` basta.

## Alcance de Lean y limitaciones

`Square.no_packing` y `excluded_of_conditions` son teoremas geométricos genuinos: cuantifican sobre todas las coordenadas y prueban las reflexiones dentro de Lean. `SquareTwins` formaliza las tres exclusiones, el testigo cartesiano y las paredes racionales. No está formalizado: la semántica del voraz, el criterio de dos discos en cuadrado, la obstrucción informacional, ni en `SquareLimit.lean` la continuidad, la existencia de `t0`, los signos de `G` en los extremos ni la familia. Los tres lemas de `SquareLimit` son identidades polinómicas; la nota lo declara correctamente. Mejora opcional: añadir a Lean las dos desigualdades racionales que fijan el signo de `G`, pues solo necesitan `49<50` y `98<100`.

Sobre novedad: el lema de reducción es folclore de empaquetamientos de pocas bolas en una bola; la nota no reclama novedad y así debe mantenerse. No puedo verificar que `grind` cierre las instancias con enteros de nueve cifras ni la salida de `#print axioms`; ambas son afirmaciones del autor que esta revisión no confirma.
