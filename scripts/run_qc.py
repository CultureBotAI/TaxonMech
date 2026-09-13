#!/usr/bin/env python3
"""Run the authoritative TaxonMech quality gate locally and in CI."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

COMMANDS = [
    (
        "lint",
        [sys.executable, "-m", "ruff", "check", "."],
        "Fail fast on syntax, import, and style defects before expensive corpus checks.",
    ),
    (
        "documentation",
        [sys.executable, "scripts/check_docs.py", "--check"],
        "The README's current-corpus block must match the corpus that generated it.",
    ),
    (
        "raw-data provenance",
        [sys.executable, "scripts/check_provenance.py"],
        "Every committed inventory must be traceable to an extraction, byte for byte.",
    ),
    (
        "tests",
        [sys.executable, "-m", "pytest", "-q"],
        "Tests cover corpus-wide invariants that per-record validation cannot see.",
    ),
    (
        "history records",
        [sys.executable, "scripts/validate_history.py"],
        "Repository-level history records must validate against the vendored claw schema.",
    ),
    (
        "schema validation",
        [sys.executable, "scripts/validate_strict.py", "--quiet"],
        "Closed-mode validation checks every record shape; quiet mode keeps the error summary visible.",
    ),
    (
        "corpus reproduction",
        [sys.executable, "scripts/verify_corpus.py"],
        "data/taxa/ must be exactly what data/raw/ and curation/seed_scope.tsv produce.",
    ),
    (
        "generated site",
        [sys.executable, "scripts/render_pages.py", "--check"],
        "The committed, published site must not drift from the corpus that generated it.",
    ),
    (
        "site publication budget",
        [sys.executable, "scripts/build_pages_artifact.py", "--check"],
        "Publish only the site and reject artifacts beyond the GitHub Pages size budget.",
    ),
    (
        "corpus report",
        [sys.executable, "scripts/corpus_report.py"],
        "Exercise cross-corpus analyses and finish with the live curation summary.",
    ),
]


def main() -> int:
    for name, command, rationale in COMMANDS:
        print(f"\n=== qc: {name} ===", flush=True)
        print(f"why: {rationale}", flush=True)
        completed = subprocess.run(command, cwd=REPO_ROOT, check=False)
        if completed.returncode:
            print(f"qc stopped: {name} failed with exit code {completed.returncode}", file=sys.stderr)
            return completed.returncode
    print("\nAll TaxonMech quality gates passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
