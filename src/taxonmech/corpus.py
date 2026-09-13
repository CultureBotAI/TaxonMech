"""Shared corpus loading for the scripts: one place that knows where the
records live and how a record maps to a page slug."""

from __future__ import annotations

import pickle
import sqlite3
import tempfile
from collections.abc import Sequence
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
TAXA_DIR = REPO_ROOT / "data" / "taxa"
SCHEMA_PATH = REPO_ROOT / "src" / "taxonmech" / "schema" / "taxonmech.yaml"


class DiskRecords(Sequence):
    """An invocation-local parsed snapshot with bounded memory on repeated scans.

    Pickles are produced here from safe-loaded YAML and read only from this
    private temporary database. No external pickle/cache file is accepted.
    Each iteration returns fresh objects, preserving read-only corpus use.
    """

    def __init__(self, paths: list[Path]):
        self._directory = tempfile.TemporaryDirectory(prefix="taxonmech-records-")
        self._db = sqlite3.connect(str(Path(self._directory.name) / "records.sqlite"))
        self._db.execute(
            "CREATE TABLE records (position INTEGER PRIMARY KEY, path TEXT, taxid INTEGER, document BLOB)"
        )
        for position, path in enumerate(paths):
            with path.open(encoding="utf-8") as handle:
                doc = yaml.load(handle, Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
            suffix = str(doc.get("identifier", "")).split(":")[-1]
            self._db.execute(
                "INSERT INTO records VALUES (?, ?, ?, ?)",
                (
                    position,
                    str(path),
                    int(suffix) if suffix.isdigit() else None,
                    pickle.dumps(doc, protocol=5),
                ),
            )
        self._db.execute("CREATE INDEX records_taxid ON records (taxid)")
        self._db.commit()
        self._count = len(paths)

    def __len__(self):
        return self._count

    def __iter__(self):
        for path, doc in self._db.execute("SELECT path, document FROM records ORDER BY position"):
            yield Path(path), pickle.loads(doc)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return [self[index] for index in range(*item.indices(len(self)))]
        index = item if item >= 0 else len(self) + item
        row = self._db.execute("SELECT path, document FROM records WHERE position = ?", (index,)).fetchone()
        if row is None:
            raise IndexError(item)
        return Path(row[0]), pickle.loads(row[1])

    def by_identifier(self):
        for path, doc in self._db.execute("SELECT path, document FROM records ORDER BY taxid"):
            yield Path(path), pickle.loads(doc)

    def close(self):
        self._db.close()
        self._directory.cleanup()


def load_records(root: Path = TAXA_DIR) -> Sequence[tuple[Path, dict]]:
    """Every record as (path, parsed doc), sorted by path."""
    paths = sorted(root.rglob("*.yaml"))
    if sum(path.stat().st_size for path in paths) > 250_000_000:
        return DiskRecords(paths)
    out = []
    for path in paths:
        with path.open(encoding="utf-8") as fh:
            out.append((path, yaml.load(fh, Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))))
    return out
