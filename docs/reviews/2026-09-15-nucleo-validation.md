# Validación del núcleo estructural uniforme

Fecha: 2026-09-15. Continuación de la investigación de tau=phi para
inventarios finitos arbitrarios, en el disco con grosor común.

## Resultado y límite

`docs/drafts/nucleo_uniforme.md` contiene una prueba escrita local de
que un intercambio que siga bloqueado tiene a lo sumo dos ramificaciones,
seis hojas y 40 aros mayores que el pivote. La longitud de la cola menor
no está acotada. El resultado depende de los criterios C1/C2 y de la
reducción adyacente ya escritos en las notas anteriores.

Dos plazas de radio m en cualquier contenedor permiten alinear el
pivote: alojan el siguiente aro y toda la cola restante, con la
recomposición indicada según el contenedor coincida o no con su destino.
La cota de área crea esas plazas sin mover a los ocupantes mayores si
el segundo ocupante tiene radio b≥9m. Un segundo criterio las construye
si la suma C de los hijos a partir del tercero satisface C≤beta(a,b).
Este último utiliza dos discos de radio b/2 en el semiplano superior
y el bolsillo inferior del par mayor.

Sigue abierto el intercambio en la familia residual: en cada
ramificación, 2m<b<9m y C>beta(a,b), además de las restricciones de
colas y de los testigos F/P. No se ha probado tau=phi ni se ha hallado
un contraejemplo geométrico. La cota del prefijo mayor no permite
reemplazar la cola por un aro ni certificar el problema global mediante
una enumeración de inventarios hasta 40 aros.

## Lean

Comando desde `lean/`, con `ELAN_HOME=C:/Users/Usuario/.elan` y
`LEAN_NUM_THREADS=1`:

```
lake env lean -j 1 Calamares/Reservoir.lean
lake build
```

Ambos terminan con código 0. La compilación conjunta final informa
`Build completed successfully (14 jobs)`; registro en
`2026-09-15-nucleo-lean-build.log`.

| Certificado | Qué comprueba |
|---|---|
| `golden_lt_five_thirds` | La relajación racional de la ecuación áurea |
| `squares_le_cap_mass` | Q≤bC para una lista finita de radios acotados |
| `two_slot_margin` | Margen positivo con b≥9m y las tres cotas de cola |
| `clearance_area_margin` | Expansión del margen de áreas de exclusión |
| `upper_half_slots` | Contención, separación y altura de las dos plazas superiores |
| `six_radii_exceed_cutoff` | Seis radios seleccionados exceden el corte 9m |
| `no_six_unary_nodes` | Contradicción de la cadena de seis aros sin holgura |

Los siete `#print axioms` solo contienen `propext`, `Classical.choice`
y `Quot.sound`. El módulo no contiene admisiones, axiomas añadidos ni
`native_decide`. El recuento de declaraciones de la biblioteca es 115.
La primera compilación del lema de suma de cuadrados detectó una
importación ausente de `VariableWidth`; se incorporó esa dependencia
y se reutilizó su definición de `squares` antes de las verificaciones
finales satisfactorias.

La subaditividad del área, la existencia de centros reales a partir de
su margen, la extracción de colas desde el inventario, el ensamblaje
local y el recuento del árbol siguen como pruebas escritas. El módulo
Lean no formaliza el teorema geométrico completo ni postula su conclusión.

## Control de la entrega

- `git diff --check`: salida 0.
- Archivos nuevos: control de UTF-8 y espacios finales satisfactorio.
- Los diez hashes de `2026-09-14-v2-artifacts.json` coinciden, incluidos
  fuentes del paper, PDF y bundle de referencia.
- `2026-09-15-nucleo-artifacts.json` registra los archivos de esta
  entrega y sus hashes. No hay cambios nuevos en el paper ni publicación.

Las notas de intercambio, partición y núcleo, y sus certificados nuevos,
no se han enviado a Fable. No se atribuye revisión externa a esta
reducción; las revisiones anteriores mantienen su alcance original.

## Consulta bibliográfica orientativa

Se consultaron como orientación general
[Packing Disks into Disks with Optimal Worst-Case Density](https://link.springer.com/article/10.1007/s00454-022-00422-8)
y [Split Packing](https://arxiv.org/abs/1705.00924).
Ninguno se usa como premisa de la reducción: el criterio requerido
conserva ocupantes ya colocados y se prueba directamente mediante
regiones prohibidas para centros en §2 de la nota. No se afirma novedad
bibliográfica de ese argumento elemental.
