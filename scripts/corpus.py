"""Shared corpus loading for the scripts: one place that knows where the
records live and how a record maps to a page slug."""

from __future__ import annotations

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
TAXA_DIR = REPO_ROOT / "data" / "taxa"
SCHEMA_PATH = REPO_ROOT / "src" / "taxonmech" / "schema" / "taxonmech.yaml"


def load_records(root: Path = TAXA_DIR) -> list[tuple[Path, dict]]:
    """Every record as (path, parsed doc), sorted by path."""
    out = []
    for path in sorted(root.rglob("*.yaml")):
        with path.open(encoding="utf-8") as fh:
            out.append((path, yaml.load(fh, Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))))
    return out
