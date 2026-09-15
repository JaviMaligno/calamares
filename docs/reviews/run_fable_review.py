"""Snapshot an explicit review manifest, run Fable, and preserve its verdict.

Only the files and line ranges in the manifest are sent. The external
review is static; compilation and tests must be verified separately.
"""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
REVIEWS = ROOT / 'docs' / 'reviews'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('manifest')
    parser.add_argument('action', choices=('prepare', 'run', 'extract'))
    args = parser.parse_args()
    manifest = json.loads((ROOT / args.manifest).read_text(encoding='utf-8'))
    prefix = manifest['prefix']
    paths = {kind: REVIEWS / f'{prefix}-{kind}{ext}' for kind, ext in
             [('prompt', '.txt'), ('stream', '.jsonl'), ('stderr', '.txt'),
              ('metadata', '.json'), ('review', '.md')]}
    if args.action == 'prepare':
        parts = [manifest['instructions']]
        snapshots = []
        for item in manifest['sources']:
            rel = item['path']
            source_path = (ROOT / rel).resolve()
            source_path.relative_to(ROOT)
            data = source_path.read_bytes()
            lines = data.decode('utf-8-sig').splitlines()
            ranges = item.get('ranges', [[1, len(lines)]])
            selected = [(i, lines[i-1]) for first, last in ranges
                        for i in range(first, min(last, len(lines))+1)]
            parts.append('\nFILE: ' + rel + '\n' + '\n'.join(
                f'{i}: {line}' for i, line in selected))
            snapshots.append({'path': rel, 'ranges': ranges,
                              'sha256': hashlib.sha256(data).hexdigest()})
        prompt = '\n\n'.join(parts)
        paths['prompt'].write_text(prompt, encoding='utf-8')
        metadata = {'model_requested': 'fable', 'sources': snapshots,
                    'prompt_sha256': hashlib.sha256(prompt.encode()).hexdigest(),
                    'authorization': manifest['authorization']}
        paths['metadata'].write_text(json.dumps(metadata, indent=2), encoding='utf-8')
        print(f'Prepared {prefix}: {len(prompt)} characters; {len(snapshots)} files')
    elif args.action == 'run':
        metadata = json.loads(paths['metadata'].read_text(encoding='utf-8'))
        prompt = paths['prompt'].read_text(encoding='utf-8')
        if hashlib.sha256(prompt.encode()).hexdigest() != metadata['prompt_sha256']:
            raise SystemExit('Prepared payload hash mismatch')
        command = [r'C:\Users\Usuario\.local\bin\claude.exe', '--print',
                   '--model', 'fable', '--effort', 'high', '--safe-mode',
                   '--strict-mcp-config', '--no-session-persistence',
                   '--permission-mode', 'dontAsk', '--tools', '',
                   '--output-format', 'stream-json', '--verbose']
        with paths['stream'].open('w', encoding='utf-8') as out, paths['stderr'].open(
                'w', encoding='utf-8') as err:
            proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=out,
                                    stderr=err, text=True, encoding='utf-8', cwd=ROOT)
            metadata['pid'] = proc.pid
            paths['metadata'].write_text(json.dumps(metadata, indent=2), encoding='utf-8')
            proc.communicate(prompt)
        metadata['returncode'] = proc.returncode
        paths['metadata'].write_text(json.dumps(metadata, indent=2), encoding='utf-8')
        print(json.dumps({'prefix': prefix, 'returncode': proc.returncode}))
        raise SystemExit(proc.returncode)
    else:
        events = [json.loads(line) for line in paths['stream'].read_text(
            encoding='utf-8').splitlines()]
        results = [e for e in events if e.get('type') == 'result']
        if not results or results[-1].get('is_error') or not results[-1].get('result'):
            raise SystemExit('No successful final verdict available')
        model = next(e['model'] for e in events if e.get('subtype') == 'init')
        header = (f'# {manifest["title"]}\n\nModelo: `{model}`. '
                  'Revisión externa estática mediante Claude Code: no ejecutó '
                  'Python ni Lean. Alcance y hashes en el manifiesto y metadata '
                  f'`{prefix}`. El dictamen se conserva íntegro.\n\n---\n\n')
        paths['review'].write_text(header + results[-1]['result'] + '\n', encoding='utf-8')
        print(f'Saved {paths["review"].name}')


if __name__ == '__main__':
    main()
