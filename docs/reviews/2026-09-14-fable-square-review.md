# Revisión independiente de Fable: resultado D del cuadrado

Fecha: 2026-09-14. Cliente Claude Code 2.1.270; modelo `claude-fable-5-1`.

Informe externo conservado íntegramente a continuación. Revisión estática: Fable no ejecutó Python ni Lean. La primera sesión produjo una rederivación antes de leer las fuentes, pero terminó sin dictamen; la continuación recibió esa rederivación y los mismos archivos autorizados, con extractos de G1 y del modelo y teoremas pertinentes del paper. No se enviaron las fuentes nuevas de las gemelas, la mejora ni el límite Y.

Los hashes de las fuentes revisadas están en `2026-09-14-fable-square-final-process.json`. Las respuestas del agente principal y las comprobaciones locales se registran por separado en `2026-09-14-fable-square-response.md`.

---

Auditoría estática completada, sin ejecutar Python ni Lean. Todo lo que sigue procede de recálculo manual exacto sobre los extractos adjuntos.

## Veredicto: revisión menor, solo de redacción. La matemática es correcta.

**Resumen.** El Lema Q es correcto tal como está escrito y tal como está codificado en Lean. La instancia D cumple las cinco paredes con los márgenes exactos declarados. El testigo de cuatro aros, la traza de best fit, las cuatro exclusiones del último aro, el valor de rho y la separación de X se confirman. La Proposición G1 es correcta. No hay ningún fallo matemático. Los hallazgos son una ambigüedad de redacción en el testigo y algunas ampliaciones opcionales de los certificados.

## Hallazgos

**Menor, requiere corrección de redacción.**

- `docs/drafts/cuadrado_certificado.md:126-128`. El testigo del agujero dice que los discos b y c tienen centros relativos en `(-c,0)` y `(b,0)`. Con la lectura respectiva, b centrado en `(-c,0)` y c centrado en `(b,0)`, la colocación es correcta: cada disco queda tangente a la frontera del agujero y ambos son tangentes entre sí. Con la lectura opuesta, b centrado en `(b,0)`, el disco b sobresale del agujero. Corrección mínima: escribir "el disco de radio b con centro en `(-c,0)` y el disco de radio c con centro en `(b,0)`", o citar directamente el Row Lemma del paper con los centros `(-H+c, 0)` y `(-H+2c+b, 0)`.

```text
Lectura respectiva (correcta):
  disco b en x=-0.841: alcanza -0.841-0.844 = -1.685 = -H   tangente
  disco c en x= 0.844: alcanza  0.844+0.841 =  1.685 =  H   tangente
Lectura invertida (incorrecta):
  disco b en x= 0.844: alcanza  0.844+0.844 =  1.688 >  H
```

**Ampliaciones opcionales, sin efecto en la corrección.**

- `code/cuadrado_certificado.py:43-60`. `verify_d` no comprueba el orden estricto decreciente de los radios ni la desigualdad `b < 1`, que el paso 3 usa para sustituir el pivote por b en el testigo de raíz. Lean sí lo hace en `d_greedy_walls`, líneas 180-181. Añadir dos claves en Python igualaría ambos certificadores.
- `lean/Calamares/Square.lean:169-175`. `d_witness` certifica `b + c = a - w` pero no las dos contenciones cartesianas de b y c dentro del agujero. Son consecuencia inmediata del Row Lemma escrito. Añadirlas cerraría el testigo sin apelar al paper.
- `code/test_cuadrado_certificado.py:21-26`. Los tests "feasible not certified" y "D' control not certified" solo prueban que un certificado concreto con los p y q de D falla. No prueban que no exista certificado alguno, cosa que sí garantiza el lema por ser D' factible. El nombre de los tests promete algo más fuerte de lo que verifican. Basta un comentario.
- `docs/drafts/cuadrado_certificado.md:172-173`. La identificación de X como raíz de `P(x)=17x⁴-4x³-62x²+4x+49` en esa rama no se puede contrastar con la definición del paper, que no está adjunta. Lo demostrado es correcto respecto de ese polinomio.

## Afirmaciones confirmadas

**Lema Q, prueba escrita, líneas 22-75.** La reflexión respecto de los ejes medios preserva contención y separación, y lleva el centro grande a `[a, s/2]²`. La cota de separación por coordenada `s-a-b` usa `a ≤ s/2` correctamente. La exclusión del signo negativo para B usa Q1, y para C usa la cota mejorada `Ax < s-b-p` junto con Q4. El confinamiento final de B y C en un cuadrado de lado L usa `p ≥ q` y `b ≥ c`. Cada paso es válido y el argumento cubre todas las posiciones, incluidas las tangencias, porque las desigualdades de separación son no estrictas.

**Márgenes de D, líneas 97-105 y Lean 157-165.** Recalculados en exacto y coincidentes con la tabla y con `d_margins`.

| Pared | Valor recalculado | Declarado |
|---|---|---|
| Q1: p − (s/2 − b) | 0.0066 | 33/5000 |
| Q2: (a+b)² − p² − (s−a−b)² | 0.00008316 | 2079/25000000 |
| Q3: (a+c)² − q² − (s−a−c)² | 0.00266236 | 66559/25000000 |
| Q4: p + q − (s−b−c) | 0.0002 | 1/5000 |
| Q5: (b+c)² − 2L², L = 0.5898 | 2.14349692 | 53587423/25000000 |

**Lean `d_no_normalized`, líneas 38-61.** Las constantes escaladas son correctas: `40128 = s-b`, `40158 = s-c`, `21678 = s-a-b`, `21708 = s-a-c`, `5898 = L`. He comprobado cada hipótesis que `grind` debe cerrar. El paso delicado es la cota inferior `-15810 ≤ cx-ax`, que no sale de la contención sola, puesto que `8410-24284 = -15874`. Sale porque `hbx` ya está en el contexto y da `ax < 24218`, luego `cx-ax > -15808`. El margen de dos unidades es exactamente el de Q4. La caja final de lado 5898 se verifica con `bx-cx ∈ (-5798, 5868)`.

```text
15910² + 21678² = 723063784 < 723072100 = 26890²   (diferencia 8316)
15810² + 21708² = 721193364 < 721459600 = 26860²   (diferencia 266236)
2·5898² = 69572808 < 283922500 = 16850²
```

**Reflexiones, `d_no_packing` y `no_packing`, líneas 67-81 y 121-136.** Los cuatro casos cubren `ax ≤ h` o no, `ay ≤ h` o no. La reflexión `x ↦ s-x` lleva el centro grande a `[a,h]` y preserva los intervalos de contención de B y C. Las distancias al cuadrado son invariantes por identidad de anillo. Correcto.

**`Conditions` y `no_normalized`, líneas 85-118.** El predicado reproduce las cinco paredes con el semilado explícito. Las cotas `yl`, `yu`, `xl` de cada aplicación de `separated_coordinate` se derivan de las hipótesis del contexto, con `hbx` disponible para `hcx` y `hby` para `hcy`, igual que en la versión especializada.

**`sq_le_of_bounds` y `separated_coordinate`, líneas 20-34.** Correctos: el primero es `m²-x² = (m-x)(m+x) ≥ 0`, el segundo un caso por `x ≤ p`.

**Testigo de raíz, líneas 111-129 y Lean 169-175.** A en `(a,a)` y M en `(s-1,s-1)` están contenidos, y `2(s-a-1)² - (a+1)² = 0.00065348` es positivo. El lado supera el lado rígido `(a+1)/(2-√2)` en unas ocho cienmilésimas, coherente con esa holgura.

**Traza de best fit, líneas 131-158 y Lean 179-189.** Capacidades: sartén 2.4284, agujero de a 1.685, agujero del pivote 0.84, agujero de b 0.684. El pivote cabe en ambos contenedores y best fit elige el agujero. El aro b solo cabe en la sartén. El aro c queda excluido de los cuatro contenedores con los motivos exactos de la tabla. La regla "no cambiar padres ya elegidos, sí recolocar hermanos" coincide con el modelo del paper, líneas 226-231 y 257-259. El lex-máximo contiene los cuatro aros por el testigo. La divergencia es real y solo para best fit, como afirma la nota.

**rho y X, líneas 160-188 y Lean 192-212.** Colas: 179/123 ≈ 1.455, 337/200 = 1.685, 841/844 ≈ 0.996. Signos `P(1.7) = -1.0463` y `P(1.72) = 0.89162752` recalculados. El polinomio desplazado `17z⁴+1116z³+21238z²+92604z-10463` es correcto, coeficiente a coeficiente, y su monotonía en `z ≥ 0` da unicidad de la raíz en la rama. Luego `rho < 1.7 < X`.

**Corolarios Q1 y Q2, líneas 190-197.** La cota superior del umbral es inmediata por la definición del paper en las líneas 607-616. La cota inferior usa el teorema de irrelevancia con hipótesis débil, que el paper enuncia para contenedor arbitrario en las líneas 347-358.

**Proposición G1, `generalizacion_dimensional.md:12-48`.** Correcta. El descarte de piezas que no caben en K usa que la bola exterior de cualquier aro colocado está contenida en K por anidamiento transitivo. Los tres casos con testigo P cubren todas las combinaciones de padres de `r2`, y cada uno produce una inserción legal para `r3` en la asignación del voraz. La única propiedad del contenedor que se usa es la clausura de la factibilidad bajo reducción concéntrica de radio, válida para cualquier compacto K en cualquier dimensión. Esto sustituye correctamente al uso de `r1+r2 ≤ R` en `prop:n3` del paper.

**Control D', líneas 204-215 y Lean 218-226.** Los tres centros están contenidos y las tres separaciones son estrictas.

| Par | Distancia² | Umbral² |
|---|---|---|
| A, B | 7.2397298 | 7.209225 |
| A, C | 7.2773818 | 7.1824 |
| B, C | 10.12387624 | 2.805625 |

**Puente al modelo del paper.** La codificación cartesiana de `FitsTriple` es exactamente "disco cerrado dentro del cuadrado cerrado" e "interiores disjuntos", con tangencias permitidas. Coincide con la definición de placement del paper. La exclusión sobre los reales es la instancia `K = ℝ` del teorema universal. El criterio de dos discos en un disco es exacto en ambos sentidos. Todo el puente es correcto aunque no esté en Lean.

## Límites de la formalización y de esta auditoría

- No he compilado Lean ni ejecutado los tests en esta sesión. El dictamen matemático no depende de ello. Lo que sí queda sin confirmar es que las llamadas a `grind` cierran cada objetivo y que las clases de `Lean.Grind` usadas en la línea 17-18 existen con esos nombres en la versión declarada de Lean. La estructura de cada objetivo es lineal o una identidad de anillo, así que es plausible, pero no está verificado aquí.
- Los `#print axioms` de las líneas 228-237 no se han inspeccionado en esta sesión.
- Lean core no tiene ℝ. La especialización del teorema universal a los reales es matemática, no mecánica. La nota lo declara con honestidad en las líneas 235-237.
- Lean no modela discos, el bosque de colocación ni el algoritmo. La ejecución de best fit y la semántica del lex-máximo son argumento escrito, respaldado por los certificados escalares.
- No he revisado las gemelas, `SquareTwins.lean`, ni los demás resultados nuevos.

**Corrección mínima antes de integrar en el paper:** desambiguar los centros del testigo en `cuadrado_certificado.md:127`. Todo lo demás es opcional.
