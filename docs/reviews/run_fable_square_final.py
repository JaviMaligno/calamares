"""Finish the same authorized review with a bounded, tool-free payload."""

import hashlib
import json
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[2]
review = root / 'docs' / 'reviews'
prefix = '2026-09-14-fable-square-final'
events = [json.loads(line) for line in
          (review / '2026-09-14-fable-square-network-stream.jsonl').read_text(
              encoding='utf-8').splitlines()]
first_derivation = '\n\n'.join(
    item['text'] for event in events if event.get('type') == 'assistant'
    for item in event.get('message', {}).get('content', [])
    if item.get('type') == 'text')
paths = [
    'docs/drafts/cuadrado_certificado.md',
    'code/cuadrado_certificado.py',
    'code/test_cuadrado_certificado.py',
    'lean/Calamares/Square.lean',
    'lean/Calamares.lean',
    'lean/README.md',
    'docs/drafts/generalizacion_dimensional.md',
    'paper/main.tex',
]
parts = [
    'Continúa una revisión matemática independiente con Fable. El usuario '
    'autorizó expresamente enviar estos archivos a Claude Code/Fable. '
    'La sesión anterior rederivó D antes de leer los archivos, después los '
    'leyó, y se cerró sin dictamen (código Windows 3221226505). '
    'Sus intentos de ejecutar Python y Lean fueron denegados. No afirmes '
    'haber ejecutado tests ni Lean. Esta continuación es una auditoría '
    'estática: todos los extractos necesarios están adjuntos con números '
    'de línea. No tienes herramientas. No revises las gemelas ni otros '
    'resultados nuevos cuyos archivos no se adjuntan. Revisa D, el Lema Q, '
    'su código y Lean, la Proposición G1, y el puente al modelo del paper. '
    'Comprueba signos, reflexiones, todas las posiciones, tangencias, '
    'contenedores, testigo, rho y comparación con X. Distingue fallos '
    'reales de ampliaciones opcionales. Devuelve un informe final en '
    'español, con hallazgos por severidad y archivo/línea, corrección '
    'mínima, afirmaciones confirmadas, límites de la formalización y '
    'veredicto aceptar/revisión menor/revisión mayor/refutado. '
    'No confundas la corrección matemática con que el kernel se haya '
    'ejecutado en esta sesión. No necesitas repetir toda la derivación; '
    'centra el informe en el dictamen y su evidencia.',
    '\nDERIVACIÓN DE LA PRIMERA SESIÓN (antes de leer las fuentes):\n' + first_derivation,
]
snapshots = {}
for rel in paths:
    source = (root / rel).read_text(encoding='utf-8')
    snapshots[rel] = hashlib.sha256((root / rel).read_bytes()).hexdigest()
    lines = source.splitlines()
    if rel == 'docs/drafts/generalizacion_dimensional.md':
        lines = source.split('\n## 2.')[0].splitlines()
    if rel == 'paper/main.tex':
        selected = [(i, lines[i-1]) for start, stop in
                    ((217, 292), (344, 430), (607, 625))
                    for i in range(start, stop+1)]
    else:
        selected = list(enumerate(lines, 1))
    parts.append('\nARCHIVO: ' + rel + '\n' + '\n'.join(
        f'{number}: {line}' for number, line in selected))
prompt = '\n\n'.join(parts)
(review / (prefix + '-prompt.txt')).write_text(prompt, encoding='utf-8')
metadata = {'model_requested': 'fable', 'cli_version': '2.1.270',
            'source_sha256': snapshots,
            'prompt_sha256': hashlib.sha256(prompt.encode('utf-8')).hexdigest(),
            'scope': 'Same expressly authorized files; static continuation'}
args = [r'C:\Users\Usuario\.local\bin\claude.exe', '--print', '--model', 'fable',
        '--effort', 'high', '--safe-mode', '--strict-mcp-config',
        '--no-session-persistence', '--permission-mode', 'dontAsk',
        '--tools', '', '--output-format', 'stream-json', '--verbose']
with (review / (prefix + '-stream.jsonl')).open('w', encoding='utf-8') as out, (
    review / (prefix + '-stderr.txt')).open('w', encoding='utf-8') as err:
    proc = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=out, stderr=err,
                            text=True, encoding='utf-8', cwd=root)
    metadata['pid'] = proc.pid
    (review / (prefix + '-process.json')).write_text(
        json.dumps(metadata, indent=2), encoding='utf-8')
    proc.communicate(prompt)
metadata['returncode'] = proc.returncode
(review / (prefix + '-process.json')).write_text(
    json.dumps(metadata, indent=2), encoding='utf-8')
print(json.dumps({'returncode': proc.returncode, 'pid': proc.pid}))
raise SystemExit(proc.returncode)
