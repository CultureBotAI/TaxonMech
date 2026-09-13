"""Shared fixtures: the corpus, loaded once per session. Tests treat it as read-only."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
TAXA_DIR = REPO_ROOT / "data" / "taxa"
SCHEMA_PATH = REPO_ROOT / "src" / "taxonmech" / "schema" / "taxonmech.yaml"


def pytest_collection_modifyitems(items):
    """Run full-corpus subprocess/reproduction checks before caching parsed YAML.

    Rendering the expanded site needs several GB on its own; retaining the
    session corpus in the parent process simultaneously wastes runner memory.
    Every test still runs, and the corpus is still parsed only once per session.
    """
    first = {"test_scripts.py", "test_verify_corpus.py"}
    items.sort(key=lambda item: item.path.name not in first)


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def schema_path() -> Path:
    return SCHEMA_PATH


@pytest.fixture(scope="session")
def records() -> list[tuple[Path, dict]]:
    """Every TaxonRecord as (path, parsed doc)."""
    if not TAXA_DIR.exists():
        pytest.skip(f"no corpus at {TAXA_DIR}")
    out = []
    for path in sorted(TAXA_DIR.rglob("*.yaml")):
        with path.open(encoding="utf-8") as fh:
            out.append((path, yaml.load(fh, Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))))
    if not out:
        pytest.skip(f"corpus at {TAXA_DIR} is empty")
    return out
