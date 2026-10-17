<div align="center">
<pre>
    .----.
   / o  o \
   |   ^  |    __
    \ \_/ /---(  )
     '---'     \_/
</pre>

# Research to Action

**Learn how to find. Find the field. Resolve the action. Test reality. Prepare the executor.**
</div>

Meet **Loom**, the little investigator with a magnifying glass. Its success pose appears only after a source-derived installation is actually verified.

Research to Action is a **five-pillar, domain-general research skill** that turns rigorous investigation into a specific downstream execution mission. The research skill produces a reproducible discovery method, broad field map, per-target operational dossiers, independent corroboration and a time-budgeted agent handoff. It researches real execution machinery and interfaces, beyond merely suggesting more research. It also preserves uncertainty, approval boundaries and proof of success.

| Pillar | Question | Concrete deliverable |
|---|---|---|
| 1 — Discover discovery | How do we find the field reliably? | Tested queries, authorities, yield and source map |
| 2 — Map the field | What actually merits attention? | Deduplicated candidates, coverage, shortlist |
| 3 — Resolve action paths | Exactly how would the intended action happen? | Steps, eligibility, entry points, proof, fallbacks |
| 4 — Confront reality | What do independent sources and real attempts show? | Independent/contrary evidence, limitations |
| 5 — Engineer execution | How can an actual agent achieve this within `{execution_hours}`? | Specific prompt, ranked queue, tools, permissions, receipts |

## Use in Hermes, Codex, ChatGPT, or another skill-capable agent

Invoke **Research to Action** with the desired outcome, constraints and optionally the downstream execution time budget. The skill researches all five pillars using available tools. It delivers six artifacts including a compact **Process Record**. Source links, recency and confidence travel into the executor dossier. UX flows are researched when the target action actually involves UX; other domains receive suitable operational procedures.

`execution_hours` is the *later executor's* time budget, defaulting to one hour; it does not impose a fictional research runtime.

## Dossier CLI (standard library only)

```bash
python3 scripts/r2actl.py validate --input dossier.json
python3 scripts/r2actl.py audit --input dossier.json
python3 scripts/r2actl.py audit --input dossier.json --require-ready
python3 scripts/r2actl.py handoff --input dossier.json --hours 1 --output executor.md --require-ready
python3 -m unittest discover -s tests -p 'test_r2a.py'
```

Start from `templates/brief.json`. `validate` verifies format, cross-references and internal support for verified claims; it is not online fact verification. `audit` lists missing source coverage/action evidence and clearly distinguishes **research-ready** from **needs-research**. `handoff` writes a structured, guarded agent mission with verifiable source details and explicit unresolved gaps. `--require-ready` refuses an incomplete dossier (exit code 3), useful in automation. The starter template is intentionally incomplete and is marked that way.

## Install as a skill

The repository root contains the standard `SKILL.md` and supporting files. Install it into an agent skill directory, or point a skill-capable agent at this repository. For example:

```bash
git clone https://github.com/ryanraposo/r2a.git ~/.hermes/skills/research-to-action
# Or clone to ~/.agents/skills/research-to-action for portable agents.
```

The direct skill has a standard frontmatter contract, references, schema, audit CLI, and tests. Complete Hermes-first transactional installation, rollback, verified receipts and release artifacts are available by deriving the maintained child from the upstream template as described below.

## Source-derived installation

This repository is the canonical standalone Research to Action agent skill. The `scripts/apply-to-template.py` overlay is also provided for building a full maintained repository from a **fresh, reviewed** copy of [ryanraposo/skill-template](https://github.com/ryanraposo/skill-template). The upstream template retains authority over its Hermes-first packaging, `skill-uxctl.py`, transactional installation, dry-runs, backups, recovery and release verification. See `DERIVE.md` to materialize and test it; an overlay alone is not a verified installation or published release.

The canonical skill is `SKILL.md`; the methodology, evidence policy, CLI and schema have matching references and tests. Read `AGENTS.md` for repo-facing guidance, `references/` for field practice, and `templates/` for output contracts.

## Development and verification

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/r2actl.py validate --input templates/brief.json
python3 scripts/r2actl.py audit --input templates/brief.json
```

The starter is intentionally incomplete: an audit indicates further research is needed. See `AGENTS.md` and `DERIVE.md` for the source-derived maintained installation.

**Canonical repository:** [ryanraposo/r2a](https://github.com/ryanraposo/r2a) · **Version:** 0.2.0 · **Upstream infrastructure:** [ryanraposo/skill-template](https://github.com/ryanraposo/skill-template).
