# Validación local de los extras: cinco aros y grosores independientes

Fecha: 2026-09-15. Estos resultados continúan la v2 y no modifican sus
fuentes, PDF ni bundle. No se ha publicado ni enviado una nueva versión.

## Resultados y alcance

- `docs/drafts/cinco_aros.md`: prueba escrita de `tau_(≤5,d)=phi`, no
  alcanzado, en bolas de dimensión d≥2. Permite agujeros independientes.
  La prueba clasifica el mayor desacuerdo de padres en el segundo y
  tercer aro, usa dos bolsillos simultáneos y alinea el prefijo completo.
- `docs/drafts/grosor_variable.md`: el intercambio sobrevive a agujeros
  independientes bajo `rho≤1`; para área plana, el umbral de optimalidad
  universal es `1/sqrt(2)` y la garantía exacta bajo `rho≤kappa<1` es
  `min(1,kappa^(-2)-1)`. Captura de cola y una familia de dos aros prueban
  las cotas opuestas. Solo superincrecencia estricta no da factor uniforme.

Ambos tienen demostración escrita, certificados locales y revisión
independiente de Fable con precisiones menores incorporadas. El umbral
global `tau=phi` no está demostrado. La continuación local descrita al
final reduce seis a un caso de bosque concreto, todavía sin resolver.
Tampoco se afirma novedad bibliográfica.

## Lean

Comando desde `lean/` con Lean 4.32.2 y `LEAN_NUM_THREADS=1`:

```powershell
$env:ELAN_HOME = 'C:/Users/Usuario/.elan'
$env:LEAN_NUM_THREADS = '1'
& 'C:/Users/Usuario/.elan/toolchains/leanprover--lean4---v4.32.2/bin/lake.exe' build
```

Resultado inicial: salida 0, `Build completed successfully (11 jobs)`.
`VariableWidth.lean` añade siete teoremas y `FiveRing.lean` once;
102 en total con los 84 de v2. Los 18 `#print axioms` nuevos solo
declaran `propext`, `Classical.choice`, `Quot.sound`.

Durante la formalización, las tangencias a los dos aros detectaron un
error de signo en la primera versión de la coordenada horizontal:
para centros del par `(-b,0)` y `(a,0)`, corresponde
`x=(a-b)(a+b)^2/(a^2+ab+b^2)`. Se corrigió en nota y Lean. La igualdad
con la pared por sí sola no detectaba ese error. Ahora las tres
tangencias, la separación de los bolsillos y los signos compilan.

Lean verifica esas identidades cartesianas, las presiones áureas, la
suma de cuadrados, las desigualdades de área y las identidades límite.
No formaliza el bosque, la captura de cola, la clasificación de padres,
la normalización real ni los límites de familias. Esos pasos se
justifican en las notas escritas.

## Python exacto

```powershell
& 'C:/Python313/python.exe' -m unittest discover -s code -p 'test_grosor_variable.py' -v
& 'C:/Python313/python.exe' code/grosor_variable.py
```

Resultado: 11 tests pasan; 15/15 comprobaciones de familias pasan.
Se verificó primero el estado rojo de los 11 tests por ausencia del
comprobador, después su implementación y el estado verde. El módulo
solo admite enteros y `Fraction`, sin tolerancias de coma flotante.

Los controles distinguen admisión en el agujero, admisión como hermanos,
tangencia exacta y rechazo de ambas vías. Incluyen la alternativa óptima,
inventario vacío factible, aro mayor que no cabe y entradas inválidas.
Para kappa=3/4, las razones aproximan 7/9 desde arriba; para la familia
del aro fino, son exactamente 4e con rho<1. Estos controles verifican
ejemplos; no se usan como prueba del resultado universal.

El script se añadió al manifiesto de `code/run_all.py`. No se ha vuelto
a ejecutar la campaña histórica completa, cuyo código no cambia.

## Revisión externa y artefactos

`2026-09-15-fable-extras-manifest.json` delimita dos notas nuevas,
`FourRing.lean` y extractos de `paper/main.tex`; el payload preparado
tiene hashes en `2026-09-15-fable-extras-metadata.json`.

La revisión automática de permisos rechazó inicialmente ejecutar el envío: consideró
que las autorizaciones previas cubrían otros archivos y que este payload
contiene notas privadas e inéditas dirigidas a un servicio externo.
El usuario autorizó después expresamente esos cuatro archivos y extractos.
La ejecución autorizada terminó con código 0 y resultado success, modelo
`claude-fable-5-1`. El dictamen íntegro está en
`2026-09-15-fable-extras-review.md`: acepta la cota inferior de F5, V1,
captura de cola y V2; pide dos precisiones menores para la cota superior
en dimensión mayor y para exactamente cinco aros. Se incorporaron junto
con las precisiones editoriales; respuesta detallada en
`2026-09-15-fable-extras-response.md`. Las correcciones no recibieron una
segunda revisión. Fable no ejecutó herramientas ni recibió FiveRing o
VariableWidth: la verificación Lean es local.

`2026-09-15-extras-artifacts.json` registra los hashes de los nuevos
archivos y la comparación de los diez artefactos congelados en
`2026-09-14-v2-artifacts.json`. Incluye el PDF de 66 páginas, bundle,
fuentes de v2 y certificados/revisiones anteriores.

## Continuación local durante la revisión

`docs/drafts/particion_bolsillos.md` desarrolla una partición de cualquier
cola finita en dos grupos, después de reservar su mayor pieza. La presión
áurea y el invariante de equilibrio permiten alineaciones con uno o dos
hermanos mayores. El segundo y tercer aro se pueden alinear para cualquier
inventario finito; para seis queda el cuarto con los tres mayores en raíz.
Ese caso no está resuelto. La nota no forma parte del envío a Fable.

`PocketSplit.lean` formaliza el invariante de las dos sumas, su cota final
y la presión de cola normalizada en tres teoremas. Compila sin admisiones
ni axiomas añadidos. La biblioteca suma **105 teoremas** y la compilación
final da `Build completed successfully (12 jobs)`. La interpretación como
partición geométrica y los criterios de bosques C1/C2 permanecen escritos.
