# Estado de la revisión independiente solicitada a Fable

**Estado: concluida. Dictamen: revisión menor de redacción, atendida.**

Fable confirma D, el Lema Q y G1 mediante auditoría estática. Informe
íntegro en [`2026-09-14-fable-square-review.md`](2026-09-14-fable-square-review.md)
y comprobaciones/respuesta en
[`2026-09-14-fable-square-response.md`](2026-09-14-fable-square-response.md).

El usuario pidió usar Claude Code con Fable. Se preparó el prompt
`2026-09-14-fable-square-prompt.txt` con dos fases: rederivar el resultado D
antes de leer su prueba, y después auditar fuentes, Lean y verificaciones.

- Cliente disponible: Claude Code `2.1.270`.
- Modelo solicitado: `fable`; el evento inicial resolvió
  `claude-fable-5-1`.
- El intento dentro del entorno aislado solo produjo reintentos de
  conexión, sin respuesta de revisión. Se interrumpió esa ejecución.
- La solicitud de ejecución con red fue rechazada por revisión automática:
  el motivo indicado fue que el envío de los archivos especificados a
  Claude Code/Fable necesitaba autorización explícita del contenido y
  del destino, además de la instrucción de usar Claude Code.
- El usuario autorizó expresamente el envío del contenido enumerado al
  destino Claude Code/Fable el 2026-09-14. La ejecución con red ya está
  iniciada y emite actividad del modelo `claude-fable-5-1`.
- El prompt autorizado se conserva sin cambios; los eventos se registran
  en `2026-09-14-fable-square-network-stream.jsonl` y los datos de la
  ejecución en `2026-09-14-fable-square-process.json`.
- La primera ejecución con red completó la rederivación y leyó los
  archivos, pero sus comandos fueron denegados por el cliente y terminó
  sin dictamen con código Windows `3221226505`. Se conservó el registro.
- Una segunda ejecución con Fable recibió únicamente los mismos archivos
  autorizados (G1 y los pasajes pertinentes del paper como extractos),
  junto a la rederivación anterior, para concluir la auditoría estática.
  No dispone de herramientas ni puede afirmar haber compilado Lean.
  Terminó correctamente, con evento `result: success` y código de
  salida 0. Su registro usa el prefijo `2026-09-14-fable-square-final` e incluye
  hashes de las fuentes enviadas. La memoria comprometida disponible
  medida durante el fallo era de unos 1.1 GB; no se ha alterado la
  configuración del sistema ni cerrado aplicaciones ajenas.

Los resultados locales posteriores (gemelas, cota `1.68449` y límite Y) NO están
revisados por Fable. Sus verificaciones matemáticas y de Lean son
distintas de la revisión independiente externa concluida sobre D.
