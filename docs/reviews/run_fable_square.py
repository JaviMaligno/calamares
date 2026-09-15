"""Run the explicitly authorized independent review and preserve its output."""

import hashlib
import json
from pathlib import Path
import subprocess


root = Path(__file__).resolve().parents[2]
review = root / "docs" / "reviews"
prompt_path = review / "2026-09-14-fable-square-prompt.txt"
args = [
    r"C:\Users\Usuario\.local\bin\claude.exe",
    "--print", "--model", "fable", "--effort", "high", "--safe-mode",
    "--strict-mcp-config", "--no-session-persistence",
    "--permission-mode", "dontAsk", "--tools", "Read,Glob,Grep,Bash",
    "--allowedTools", "Read", "Glob", "Grep", "Bash(python *)",
    "Bash(cd *)", "Bash(lake *)", "Bash(*lean.exe*)",
    "--output-format", "stream-json", "--verbose",
]
metadata = {
    "model_requested": "fable",
    "cli_version": "2.1.270",
    "prompt_sha256": hashlib.sha256(prompt_path.read_bytes()).hexdigest(),
    "authorization": "Explicit user authorization in the conversation, 2026-09-14",
}
with (review / "2026-09-14-fable-square-network-stream.jsonl").open(
    "w", encoding="utf-8"
) as out, (review / "2026-09-14-fable-square-network-stderr.txt").open(
    "w", encoding="utf-8"
) as err:
    proc = subprocess.Popen(
        args, stdin=subprocess.PIPE, stdout=out, stderr=err,
        text=True, encoding="utf-8", cwd=root,
    )
    metadata["pid"] = proc.pid
    (review / "2026-09-14-fable-square-process.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )
    proc.communicate(prompt_path.read_text(encoding="utf-8"))
metadata["returncode"] = proc.returncode
(review / "2026-09-14-fable-square-process.json").write_text(
    json.dumps(metadata, indent=2), encoding="utf-8"
)
print(json.dumps(metadata))
raise SystemExit(proc.returncode)
