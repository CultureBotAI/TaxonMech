#!/usr/bin/env python3
"""Verify that data/taxa/ is exactly what data/raw/ and curation/seed_scope.tsv produce.

The corpus is derived data and its inputs are committed, so it is reproducible
from the repo alone — but nothing else checks that it actually reproduces.
Schema validation checks each record's *shape*, the corpus tests check
cross-record *invariants*, and the round-trip test checks the *emit format*.
None of them compares a record's content to what the seeder would write, so a
hand-edit, a bad merge, or a silent seeder change all pass unnoticed.

This runs the seeder's own pipeline (``build_corpus`` / ``build_document`` /
``emit_taxon_yaml``, imported rather than reimplemented, so it cannot drift
from what ``seed-apply`` does) and compares the result byte-for-byte against
what is on disk.

Usage:
    python3 scripts/verify_corpus.py
    python3 scripts/verify_corpus.py --max-diffs 3

Exits non-zero on any missing, extra, or differing record.

NOTE for when curation starts: today every record is 100% seeder-generated, so
an exact comparison is right. Once curators add causal_graphs or flip records to
REVIEWED, records will legitimately diverge and this will need to compare only
the seeder-owned fields.
"""

from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from taxonmech.seed import (  # noqa: E402
    TAXA_DIR,
    assign_paths,
    build_corpus,
    build_document,
    load_lockfile,
)
from taxonmech.validation.write_validated import emit_taxon_yaml  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--max-diffs", type=int, default=1,
                        help="How many differing records to show a diff for (default: 1).")
    args = parser.parse_args(argv)

    if not TAXA_DIR.exists():
        print(f"no corpus at {TAXA_DIR}; run `just seed-apply` first", file=sys.stderr)
        return 2

    corpus = build_corpus()
    paths, _ = assign_paths(corpus.concepts, load_lockfile())
    expected = {paths[c.identifier]: c for c in corpus.concepts}
    on_disk = set(TAXA_DIR.rglob("*.yaml"))

    missing = sorted(set(expected) - on_disk)
    extra = sorted(on_disk - set(expected))
    differing: list[tuple[Path, str, str]] = []
    for path, concept in sorted(expected.items(), key=lambda kv: str(kv[0])):
        if path not in on_disk:
            continue
        want = emit_taxon_yaml(build_document(concept, corpus.inventory))
        got = path.read_text(encoding="utf-8")
        if want != got:
            differing.append((path, want, got))

    print(f"expected {len(expected)} records, found {len(on_disk)} on disk")
    print(f"  missing:   {len(missing)}")
    print(f"  extra:     {len(extra)}")
    print(f"  differing: {len(differing)}")
    for path in missing[:10]:
        print(f"  MISSING {path.relative_to(REPO_ROOT)}", file=sys.stderr)
    for path in extra[:10]:
        print(f"  EXTRA   {path.relative_to(REPO_ROOT)}", file=sys.stderr)
    for path, want, got in differing[: args.max_diffs]:
        print(f"\n  DIFFERS {path.relative_to(REPO_ROOT)}", file=sys.stderr)
        diff = difflib.unified_diff(want.splitlines(), got.splitlines(),
                                    fromfile="expected (from data/raw)", tofile="on disk", lineterm="", n=1)
        for line in list(diff)[:40]:
            print(f"    {line}", file=sys.stderr)
    if len(differing) > args.max_diffs:
        print(f"\n  ... and {len(differing) - args.max_diffs} more differing record(s)", file=sys.stderr)

    if missing or extra or differing:
        print("\ncorpus does not match data/raw/ + curation/seed_scope.tsv. Either re-seed "
              "(`just seed-apply --force --prune`) or, if the change was intended, "
              "make it in the seeder so it survives the next re-seed.", file=sys.stderr)
        return 1
    print("\ncorpus reproduces exactly from data/raw/ and curation/seed_scope.tsv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
