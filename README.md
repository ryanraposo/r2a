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

Meet **Loom**, the little investigator with a magnifying glass. Loom is the recognizable face of Research to Action.

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

The standalone skill includes its own frontmatter, research references, schema, dossier CLI, examples and tests. The research lifecycle, evidence standards and executor handoff are defined directly in this repository.

## Repository layout

- `SKILL.md` — canonical methodology, research stages, evidence standards and deliverables.
- `references/` — detailed research, evidence, coverage and executor-handoff procedures.
- `schemas/` and `templates/` — structured dossier and mission examples.
- `scripts/r2actl.py` — portable dossier validation, readiness auditing and handoff generation.
- `agents/` and `runtimes/` — integration metadata for skill-capable agents.
- `AGENTS.md` and `tests/` — maintenance guidance and verification.

Research to Action is maintained and used directly from [ryanraposo/r2a](https://github.com/ryanraposo/r2a). The research procedures are portable across agents; runtime permissions and tool availability are established in the invoking environment.

## Development and verification

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/r2actl.py validate --input templates/brief.json
python3 scripts/r2actl.py audit --input templates/brief.json
```

The starter dossier is intentionally incomplete: its audit indicates further research is needed. See `AGENTS.md` for maintenance and verification guidance.

**Canonical repository:** [ryanraposo/r2a](https://github.com/ryanraposo/r2a) · **Version:** 0.2.0.
