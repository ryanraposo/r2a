#!/usr/bin/env python3
"""Stage and verify R2A as a child of a fresh reviewed skill-template checkout.

Does not publish, install to agent homes or mutate the checkout until verification passes.
"""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parents[1]
LOOM = r'''    .----.
   / o  o \
   |   ^  |    __
    \ \_/ /---(  )
     '---'     \_/'''
VICTORY = r'''    .----.
   / ^  ^ \
   |   v  |    __
    \ \_/ /---(  )
     '---'     \_/'''
COPY = [
    'SKILL.md', 'AGENTS.md', 'README.md', 'DERIVE.md', 'VERSION',
    'agents/openai.yaml', 'runtimes/hermes-frontmatter.yaml',
    'references/pillars.md', 'references/evidence-and-coverage.md',
    'references/exec-agent.md', 'schemas/dossier.schema.json',
    'scripts/r2actl.py', 'tests/test_r2a.py',
    'templates/brief.json', 'templates/executor-prompt.md'
]
NEEDED = ['SKILL.md', 'README.md', 'AGENTS.md', 'VERSION', 'install.sh',
          'index.html', 'scripts/customize.sh', 'scripts/install-skill.sh',
          'scripts/components.py', 'scripts/skill-uxctl.py', 'tests/run.sh',
          'components/manifest.json', 'contracts/skill-ux.json']


def exactly_once(source, pattern, replacement, *, flags=0, label='patch'):
    result, count = re.subn(pattern, replacement, source, count=1, flags=flags)
    if count != 1:
        raise ValueError(f'expected exactly one {label} insertion point')
    return result


def transform(stage, repo, old_version, new_version):
    # Invoke the parent's actual customization machinery first.
    subprocess.run([str(stage / 'scripts/customize.sh'), '--name', 'research-to-action',
                    '--display-name', 'Research to Action', '--description',
                    'Source-grounded five-pillar research with operational dossiers and executor-ready handoffs.',
                    '--repository', repo], cwd=stage, check=True)
    # Keep version-dependent parent runtime, tests, URLs, and release names aligned.
    for path in stage.rglob('*'):
        if not path.is_file() or '.git' in path.parts or path.suffix.lower() not in ('.md','.json','.yaml','.yml','.html','.py','.sh','.txt'):
            continue
        try:
            raw = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        if old_version in raw:
            path.write_text(raw.replace(old_version, new_version), encoding='utf-8')

    for name in COPY:
        dest = stage / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(HERE / name, dest)
    (stage / 'scripts/r2actl.py').chmod(0o755)

    manifest_path = stage / 'components/manifest.json'
    manifest = json.loads(manifest_path.read_text())
    if not any(c.get('id') == 'r2a-validator' for c in manifest['components']):
        manifest['components'].append({'id': 'r2a-validator', 'kind': 'script',
            'path': 'scripts/r2actl.py', 'scopes': ['runtime-core'], 'executable': True})
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')

    index = stage / 'index.html'
    html = index.read_text()
    html = exactly_once(html, r'<pre class="mascot" aria-label="[^"]+">.*?</pre>',
        lambda m: '<pre class="mascot" aria-label="Loom, the investigator">' + LOOM + '</pre>',
        flags=re.S, label='Pages canonical mascot')
    html = exactly_once(html, r'<pre class="mascot success" aria-label="[^"]+">.*?</pre>',
        lambda m: '<pre class="mascot success" aria-label="Loom, the investigator">' + VICTORY + '</pre>',
        flags=re.S, label='Pages success mascot')
    html = html.replace('Meet Patch, the skillwright.', 'Meet Loom, the curious investigator.')
    html = html.replace('Seriously good skills.', 'Research, ready for action.')
    html = html.replace('A Hermes-first template for seriously good agent skills.',
                        'Source-grounded, five-pillar research into an agent execution mission.')
    html = html.replace('Every child skill gets its own named little guy.',
                        'Find out how to find out. Resolve action with evidence.')
    html = exactly_once(html, r'<div class="grid">.*?</div>\s*<div class="hermes">',
      '''<div class="grid">
      <div class="card"><strong>1 · Method</strong>Test discovery strategies and map trustworthy sources.</div>
      <div class="card"><strong>2 · Field</strong>Build the eligible candidate universe, coverage and ranking.</div>
      <div class="card"><strong>3 · Action</strong>Research observed steps, entry points, blockers and receipts.</div>
      <div class="card"><strong>4 · Reality</strong>Challenge each target with independent evidence and failures.</div>
      <div class="card"><strong>5 · Execution</strong>Hand the next agent a time-budgeted mission and proven leads.</div>
      <div class="card"><strong>Auditability</strong>Track citations, readiness gaps, approvals and verified results.</div>
    </div>

    <div class="hermes">''', flags=re.S, label='Pages cards')
    # Parent customizer replaces repository identity and link URLs.
    index.write_text(html)
    boot = stage / 'install.sh'; content = boot.read_text()
    content = exactly_once(content, r"cat <<'MASCOT'\n.*?\nMASCOT",
                           lambda m: "cat <<'MASCOT'\n" + LOOM + "\nMASCOT",
                           flags=re.S, label='bootstrap mascot')
    boot.write_text(content)
    installer = stage / 'scripts/install-skill.sh'; content = installer.read_text()
    content = exactly_once(content, r"printf '< -- ! -- >.*$",
                           lambda m: "cat <<'MASCOT'\n" + VICTORY + "\nMASCOT",
                           flags=re.M, label='verified-success mascot')
    installer.write_text(content)
    with (stage / 'SKILL.md').open('a') as f:
        f.write('\n## Child skill identity\n\nLoom is the named little guy. Every ASCII hero block remains graphic-only. The README, Pages and bootstrap have identical canonical poses; the success variant appears only after verified installation and the exact `Next:` instruction.\n')
    boot.chmod(0o755)
    installer.chmod(0o755)


def run_checks(stage):
    checks = [
        [sys.executable, 'scripts/components.py', 'validate'],
        [sys.executable, 'scripts/skill-uxctl.py', 'validate'],
        [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_r2a.py'],
        ['./tests/run.sh'],
        ['./install.sh', '--dry-run']
    ]
    # Parent template tests use this flag for isolated root-only test environments.
    env = os.environ.copy()
    env['RESEARCH_TO_ACTION_ALLOW_ROOT_TEST'] = '1'
    for cmd in checks:
        print('[VERIFY] ' + ' '.join(cmd), flush=True)
        subprocess.run(cmd, cwd=stage, env=env, check=True)


def patch(template, repo):
    if not template.is_dir():
        raise ValueError(f'not a directory: {template}')
    for name in NEEDED:
        if not (template / name).is_file():
            raise ValueError(f'not an intact source template: missing {name}')
    if 'name: skill-template' not in (template / 'SKILL.md').read_text():
        raise ValueError('expected a fresh, uncustomized skill-template checkout')
    old_version = (template / 'VERSION').read_text().strip()
    new_version = (HERE / 'VERSION').read_text().strip()
    # Staged customization preserves the checkout untouched on validation/test failures.
    parent = template.parent
    stage = Path(tempfile.mkdtemp(prefix='.research-to-action.stage.', dir=parent))
    backup = None
    try:
        shutil.copytree(template, stage, dirs_exist_ok=True, symlinks=True)
        transform(stage, repo, old_version, new_version)
        run_checks(stage)
        backup = Path(tempfile.mkdtemp(prefix='.research-to-action.rollback.', dir=parent))
        backup.rmdir()
        template.rename(backup)
        try:
            stage.rename(template)
        except OSError:
            backup.rename(template)
            raise
        print(f'[OK] Verified and committed R2A {new_version} to {template}')
        print('[INFO] Next: review changes, commit to the chosen repository, publish/install with explicit authorization')
    finally:
        if stage.exists():
            shutil.rmtree(stage)
        if backup is not None and backup.exists():
            shutil.rmtree(backup)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--template-dir', required=True)
    parser.add_argument('--repo', default='ryanraposo/r2a')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', args.repo):
        parser.error('--repo must be OWNER/REPO')
    try:
        patch(Path(args.template_dir).resolve(), args.repo)
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        raise SystemExit('[ERROR] ' + str(exc))
