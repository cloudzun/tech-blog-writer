#!/usr/bin/env python3
# Adapter that runs the original quality_checker.py and wraps its JSON output

import sys
import json
import subprocess
from pathlib import Path
from dataclasses import asdict

ROOT = Path(__file__).resolve().parents[2]
QC_SCRIPT = ROOT / 'scripts' / 'quality_checker.py'

if not QC_SCRIPT.exists():
    print(json.dumps({"success": False, "message": f"quality_checker.py not found at {QC_SCRIPT}"}, ensure_ascii=False))
    sys.exit(1)

def run_quality_checker(content: str):
    proc = subprocess.run([sys.executable, str(QC_SCRIPT), content, '--json'], capture_output=True, text=True)
    if proc.returncode != 0:
        # try to parse stdout anyway
        try:
            out = proc.stdout.strip()
            data = json.loads(out)
            data.setdefault('success', False)
            data.setdefault('message', 'quality_checker failed')
            return data
        except Exception:
            return {"success": False, "message": proc.stderr.strip() or 'quality_checker error'}
    try:
        data = json.loads(proc.stdout)
        # normalize fields
        data.setdefault('success', True)
        data.setdefault('message', 'ok')
        return data
    except Exception as e:
        return {"success": False, "message": f"failed parse output: {e}", "raw": proc.stdout}

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"success": False, "message": "usage: quality_check_adapter.py <content> [--json]"}, ensure_ascii=False))
        sys.exit(1)
    content = sys.argv[1]
    out = run_quality_checker(content)
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
