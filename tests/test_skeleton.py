"""Example test — delete me and test YOUR project instead.

This is here to show what "project-level TDD" means in KISpec: a test that pins
a *requirement*, not an implementation detail. KISpec's requirement is its own
skeleton and thesis, so these tests guard exactly that. If the repo ever betrays
its argument — someone adds a design.md, or CLAUDE.md stops importing AGENTS.md —
a test goes red. The spec of record is executable; prose can't do this.

Zero dependencies. Run from the repo root:

    python -m unittest discover -s tests
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestSkeletonHoldsItsThesis(unittest.TestCase):
    def test_no_design_or_tasks_doc(self):
        """ADR 0001: the *how* is the model's job. No design.md / tasks.md — ever."""
        banned = {"design.md", "tasks.md"}
        offenders = [
            p.relative_to(ROOT).as_posix()
            for p in ROOT.rglob("*.md")
            if ".git" not in p.parts and p.name.lower() in banned
        ]
        self.assertEqual(offenders, [], f"forbidden how-docs present: {offenders}")

    def test_claude_md_imports_agents_md(self):
        """CLAUDE.md must be the one-line @AGENTS.md import, not a duplicated ruleset."""
        text = (ROOT / "CLAUDE.md").read_text(encoding="utf-8").strip()
        self.assertEqual(text, "@AGENTS.md")

    def test_expectations_keeps_what_why_whatfor(self):
        """The irreducible core: what / why / what for. The 'how' must not live here."""
        text = (ROOT / "EXPECTATIONS.md").read_text(encoding="utf-8")
        for section in ("## What", "## Why", "## What for"):
            self.assertIn(section, text, f"EXPECTATIONS.md is missing '{section}'")

    def test_every_adr_records_the_why_not(self):
        """An ADR that omits 'Alternatives discarded' has thrown away the why-not —
        the one thing the code never records. Guard the whole folder, template included."""
        required = ("## Context", "## Decision", "## Alternatives discarded", "## Consequences")
        adrs = sorted((ROOT / "decisions").glob("*.md"))
        self.assertTrue(adrs, "decisions/ has no ADRs")
        for adr in adrs:
            text = adr.read_text(encoding="utf-8")
            for section in required:
                self.assertIn(section, text, f"{adr.name} is missing '{section}'")

    def test_numbered_adrs_are_dated(self):
        """An ADR dates a decision; an undated one can't anchor 'why then'."""
        date = re.compile(r"\*\*Date:\*\*\s*\d{4}-\d{2}-\d{2}")
        for adr in sorted((ROOT / "decisions").glob("[0-9]*.md")):
            text = adr.read_text(encoding="utf-8")
            self.assertRegex(text, date, f"{adr.name} has no ISO date")


if __name__ == "__main__":
    unittest.main()
