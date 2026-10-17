#!/usr/bin/env python3
"""Build the full R2A maintained child from an actual reviewed skill-template checkout."""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parents[1]

def build(source, output):
    source=source.resolve(); output=output.resolve()
    if output.exists():
        raise ValueError(f'output exists; choose an empty destination: {output}')
    if not source.is_dir() or not (source/'scripts/customize.sh').is_file():
        raise ValueError('provide an actual skill-template checkout with --template-dir')
    if source == HERE or output == HERE or source in output.parents or output in source.parents:
        raise ValueError('source and output must be distinct sibling workspaces')
    output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.r2a-build.',dir=output.parent) as td:
        stage=Path(td)/'source'
        shutil.copytree(source,stage,ignore=shutil.ignore_patterns('.git','__pycache__'))
        subprocess.run([sys.executable,str(HERE/'scripts/apply-to-template.py'),
                        '--template-dir',str(stage),'--repo','ryanraposo/r2a'],check=True)
        shutil.copytree(stage,output)
    print(f'[OK] Verified full R2A repository: {output}')
    print('[NEXT] Review, commit and push to ryanraposo/r2a')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--template-dir',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    try: build(a.template_dir,a.out)
    except (ValueError,OSError,subprocess.CalledProcessError) as e: p.exit(2,'[ERROR] '+str(e)+'\n')
