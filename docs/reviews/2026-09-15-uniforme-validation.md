# Validación de la reducción uniforme

Fecha: 2026-09-15. El objetivo de investigación pasa de una clasificación
por tamaño a un intercambio válido para todo inventario finito. Se
conservan los resultados anteriores, pero no se cuentan como cierre global.

## Prueba escrita

`docs/drafts/intercambio_uniforme.md` demuestra la cota U≤m a partir
de dos colas consecutivas y reduce un testigo de prefijo máximo a un
intercambio adyacente de padres. El argumento considera cualquier
inventario finito, no una lista de tamaños. C1/C2 de la nota de particiones
dan un corolario condicional para ejecuciones con bosque binario de
tamaño arbitrario. No se afirma que siempre exista tal ejecución.

La sección 4 formula el intercambio geométrico que falta, con un número
arbitrario de ocupantes mayores, para el modelo original de grosor común
en el disco. No está demostrado. La reducción adyacente, los bosques
y el uso geométrico del lema de fila no están formalizados en Lean.

## Lean

Comando desde `lean/`:

```powershell
$env:ELAN_HOME = 'C:/Users/Usuario/.elan'
$env:LEAN_NUM_THREADS = '1'
& 'C:/Users/Usuario/.elan/toolchains/leanprover--lean4---v4.32.2/bin/lake.exe' build
```

Resultado: salida 0, `Build completed successfully (13 jobs)`.
`UniformExchange.lean` incorpora tres teoremas:

- `two_step_pressure`: `(k+1)U≤k²m` a partir de ambas cotas de cola;
- `golden_second_tail`: U≤m cuando k es la raíz positiva de k²=k+1;
- `additive_control`: testigo, prefijo, rechazos y rho=21/17<3/2 de
  una instancia aditiva que satisface las cotas pero falla.

Los tres `#print axioms` solo contienen `propext`, `Classical.choice`
y `Quot.sound`. El control racional usa `decide +kernel`; no hay
admisiones ni axiomas añadidos. La biblioteca suma 108 teoremas.

El control aditivo demuestra la necesidad de una justificación geométrica
adicional. No refuta el umbral euclidiano: la desigualdad de suma que
excluye su raíz no es necesaria para el empaquetamiento en el disco.

## Alcance de revisión y artefactos

Esta nota y este módulo no se enviaron a Fable. Las autorizaciones de
envío anteriores no se reutilizaron para nuevos archivos. No se atribuye
a Fable la aceptación de estos argumentos.

`2026-09-15-uniforme-artifacts.json` registra los hashes de esta entrega
y comprueba que los diez artefactos de la v2 de referencia conservan
los hashes de `2026-09-14-v2-artifacts.json`. Las notas nuevas no se
incorporan al PDF ni al bundle de v2. No hay publicación nueva.
