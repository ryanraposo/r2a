# Derive a complete maintained skill from `ryanraposo/skill-template`

This repository ships its R2A-domain **overlay** and standard-library CLI. For a repository with transactional install, verified receipts, Hermes-native packaging, rollback, release archives and the parent skill UX controller, apply it to a fresh reviewed clone of the **actual** `ryanraposo/skill-template` source:

```bash
# Use a fresh local checkout of ryanraposo/skill-template (currently v1.2.0)
python3 /path/to/r2a-overlay/scripts/apply-to-template.py \
  --template-dir /path/to/fresh/skill-template \
  --repo ryanraposo/r2a
cd /path/to/fresh/skill-template
python3 scripts/components.py validate
python3 scripts/skill-uxctl.py validate
python3 -m unittest discover -s tests -p 'test_r2a.py'
./tests/run.sh
./install.sh --dry-run
```

The overlay invokes the parent **customizer first**, then installs R2A's skill, references, dossier schema, CLI, agent metadata, examples and tests. It registers the domain validator in the parent's component graph. It gives Loom a canonical graphic-only README/Pages/installer pose and verified-success variant. The parent's workflow controller, constitution, transactional installer and rollback remain the source of truth; the overlay only configures their child identity. Inspect generated diffs before publishing or deploying.

**Status distinctions:** Maintaining this source skill is not itself a checkout derivation. Successful derivation requires an actual source checkout plus its graph/controller/tests/dry-run. Publication, creating a GitHub repo, installing to a user's Hermes/Agent homes and making external changes are separate actions requiring the right environment and authorization. A failed test blocks a claim that installation/release is verified.
