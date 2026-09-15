"""Preserve the final external verdict verbatim, only after a success event."""

import json
from pathlib import Path

review = Path(__file__).resolve().parent
events = [json.loads(line) for line in
          (review / '2026-09-14-fable-square-final-stream.jsonl').read_text(
              encoding='utf-8').splitlines()]
results = [e for e in events if e.get('type') == 'result']
if not results or results[-1].get('is_error'):
    raise SystemExit('No successful final result is available yet')
result = results[-1]
body = result.get('result', '')
if not body:
    raise SystemExit('The success event does not contain a review')
model = next(e['model'] for e in events if e.get('subtype') == 'init')
header = (
    '# Revisión independiente de Fable: resultado D del cuadrado\n\n'
    f'Fecha: 2026-09-14. Cliente Claude Code 2.1.270; modelo `{model}`.\n\n'
    'Informe externo conservado íntegramente a continuación. Revisión estática: '
    'Fable no ejecutó Python ni Lean. La primera sesión produjo una rederivación '
    'antes de leer las fuentes, pero terminó sin dictamen; la continuación '
    'recibió esa rederivación y los mismos archivos autorizados, con extractos '
    'de G1 y del modelo y teoremas pertinentes del paper. No se enviaron '
    'las fuentes nuevas de las gemelas, la mejora ni el límite Y.\n\n'
    'Los hashes de las fuentes revisadas están en '
    '`2026-09-14-fable-square-final-process.json`. Las respuestas del agente '
    'principal y las comprobaciones locales se registran por separado en '
    '`2026-09-14-fable-square-response.md`.\n\n---\n\n'
)
destination = review / '2026-09-14-fable-square-review.md'
destination.write_text(header + body + '\n', encoding='utf-8')
print(f'Saved {destination.name}; model={model}; result={result.get("subtype")}')
