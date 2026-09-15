"""Shared fixtures: the corpus, loaded once per session. Tests treat it as read-only."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

import pytest

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
    sys.path.insert(0, str(REPO_ROOT / "scripts"))
    from corpus import load_records
    out = load_records(TAXA_DIR)
    if not out:
        pytest.skip(f"corpus at {TAXA_DIR} is empty")
    yield out
    if hasattr(out, "close"):
        out.close()


@pytest.fixture
def fixture_renderer(tmp_path, repo_root, monkeypatch):
    """Render synthetic records against an explicit temporary site configuration."""
    from taxonmech import text_map_site

    monkeypatch.syspath_prepend(str(repo_root / "scripts"))
    renderer = importlib.import_module("render_pages")
    config = tmp_path / "conf" / "text_map.yaml"
    config.parent.mkdir()
    config.write_text("enabled: false\n", encoding="utf-8")
    legacy = tmp_path / "curation" / "legacy_page_paths.tsv"
    legacy.parent.mkdir()
    legacy.write_text("identifier\tpage\n", encoding="utf-8")
    monkeypatch.setattr(renderer, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(renderer, "TAXA_DIR", tmp_path / "data" / "taxa")

    def unexpected_export(*_args, **_kwargs):
        pytest.fail("synthetic renderer fixtures must not export a real semantic corpus")

    # Keep actual prepare_text_map/config validation. Fail immediately if a
    # fixture ever leaks back to the enabled repository corpus.
    monkeypatch.setattr(text_map_site, "export_inputs", unexpected_export)
    return renderer
