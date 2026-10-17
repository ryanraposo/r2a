"""Package-level invariants for the standalone skill source."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class RepositoryTests(unittest.TestCase):
    def test_canonical_skill_identity(self):
        skill = (ROOT / 'SKILL.md').read_text()
        self.assertTrue(skill.startswith('---\nname: research-to-action\n'))
        self.assertIn('## Pillar 5', skill)
        self.assertIn('Loom', skill)
    def test_hermes_version_matches_source(self):
        version = (ROOT / 'VERSION').read_text().strip()
        hermes = (ROOT / 'runtimes/hermes-frontmatter.yaml').read_text()
        self.assertIn('name: research-to-action\n', hermes)
        self.assertIn(f'version: {version}\n', hermes)
    def test_standalone_repository_identity(self):
        readme = (ROOT / 'README.md').read_text()
        self.assertIn('ryanraposo/r2a', readme)
        self.assertIn('scripts/r2actl.py', readme)
        for path in ('README.md', 'SKILL.md', 'AGENTS.md'):
            self.assertNotIn('skill' + '-template', (ROOT / path).read_text())
        for retired in ('DERIVE.md', 'scripts/apply-to-template.py', 'scripts/build-repo.py'):
            self.assertFalse((ROOT / retired).exists())

    def test_schema_and_example_match_version(self):
        schema = json.loads((ROOT / 'schemas/dossier.schema.json').read_text())
        example = json.loads((ROOT / 'templates/brief.json').read_text())
        self.assertEqual(schema['properties']['schema_version']['const'], example['schema_version'])

if __name__ == '__main__':
    unittest.main()
