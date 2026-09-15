"""Compile the integrated v2 and verify its standalone source bundle."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile

from make_arxiv_bundle import collect_sources

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'paper/v2'
OUTPUT = ROOT / 'output/pdf/calamares_v2_integrada.pdf'
BUNDLE = ROOT / 'paper/arxiv-v2-integrada.tar.gz'
REPORT = ROOT / 'docs/reviews/2026-09-15-v2-integrada-build.json'


def compile_tex(directory):
    compiler = shutil.which('pdflatex')
    if not compiler:
        raise RuntimeError('pdflatex is required')
    for attempt in range(1, 5):
        result = subprocess.run(
            [compiler, '-interaction=nonstopmode', '-halt-on-error', 'main.tex'],
            cwd=directory, capture_output=True)
        (directory / 'build-console.log').write_bytes(result.stdout + result.stderr)
        if result.returncode:
            raise RuntimeError(f'LaTeX failed; inspect {directory / "main.log"}')
        log = (directory / 'main.log').read_text(encoding='utf-8', errors='replace')
        unresolved = any(x in log for x in (
            'undefined references', 'Label(s) may have changed',
            'Rerun to get', 'Rerun to get outlines'))
        if not unresolved:
            return attempt, log
    raise RuntimeError('References did not stabilize after four passes')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-bundle', action='store_true')
    args = parser.parse_args()
    passes, log = compile_tex(SOURCE)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE / 'main.pdf', OUTPUT)
    sources = collect_sources(SOURCE)
    with tarfile.open(BUNDLE, 'w:gz') as archive:
        for filename, rel in sources:
            info = archive.gettarinfo(filename, arcname=rel)
            info.mtime = info.uid = info.gid = 0
            info.uname = info.gname = ''
            with open(filename, 'rb') as source:
                archive.addfile(info, source)
    report = {
        'source': SOURCE.relative_to(ROOT).as_posix(),
        'pdf': OUTPUT.relative_to(ROOT).as_posix(),
        'latex_passes': passes,
        'bundle': BUNDLE.relative_to(ROOT).as_posix(),
        'members': [rel for _, rel in sources],
        'overfull_boxes': log.count('Overfull'),
        'underfull_boxes': log.count('Underfull'),
        'latex_warnings': [line for line in log.splitlines() if 'Warning:' in line],
        'standalone_bundle_compiled': False,
    }
    if args.verify_bundle:
        scratch = ROOT / 'tmp/pdfs'
        scratch.mkdir(parents=True, exist_ok=True)
        extracted = Path(tempfile.mkdtemp(prefix='v2-bundle-', dir=scratch)).resolve()
        extracted.relative_to(scratch.resolve())
        with tarfile.open(BUNDLE) as archive:
            for member in archive.getmembers():
                target = (extracted / member.name).resolve()
                target.relative_to(extracted)
                if not member.isfile():
                    raise RuntimeError('Unexpected non-file member')
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.extractfile(member) as source, target.open('wb') as dest:
                    shutil.copyfileobj(source, dest)
        archive_passes, archive_log = compile_tex(extracted)
        report.update(standalone_bundle_compiled=True,
                      standalone_latex_passes=archive_passes,
                      standalone_directory=extracted.relative_to(ROOT).as_posix())
        assert archive_log.count('Overfull') == report['overfull_boxes']
    for key, path in [('pdf', OUTPUT), ('bundle', BUNDLE)]:
        report[key + '_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
    REPORT.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
