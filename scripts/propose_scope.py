#!/usr/bin/env python3
"""Rank inventory taxa as candidates for curation/seed_scope.tsv.

The inventories cover every taxon a strain-bearing source attests; the
committed corpus is the explicit subset in curation/seed_scope.tsv. This
script proposes rows for that file — it never writes it. Redirect its output
and review the list before committing it.

Rules:

  core      species with a BacDive strain, an LPSN name that is the correct
            name and carries a type strain designation, and a GTDB identity
            mapping (LPSN-linked or 1:1 closeMatch; a broadMatch alone is
            pooling, not identity) — the best-corroborated taxa, ranked by
            how many sources attest them and then by BacDive strain count.
  attested  any attested taxon, ranked the same way.

    python scripts/propose_scope.py --rule core --top 100 > curation/seed_scope.tsv
    python scripts/propose_scope.py --rule core --top 100 --append   # skip ids already in scope
    python scripts/propose_scope.py --rule attested --rank '' --all --append
"""

from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from taxonmech.seed import SCOPE_PATH, load_inventory, load_scope, split  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--rule", choices=("core", "attested"), default="core")
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--top", type=int, default=100,
                           help="Maximum candidates to propose (default: 100).")
    selection.add_argument("--all", action="store_true",
                           help="Propose every eligible candidate without a count limit.")
    parser.add_argument("--rank", default="SPECIES",
                        help="Restrict to this NCBI rank (default SPECIES; '' for any rank at or below "
                             "species). Taxa above species are never proposed.")
    parser.add_argument("--append", action="store_true", help="Omit identifiers already in the scope file.")
    parser.add_argument("--date", default=datetime.date.today().isoformat())
    args = parser.parse_args(argv)
    if args.top < 1:
        parser.error("--top must be positive; use --all for every eligible candidate")

    inv = load_inventory()
    existing = set(load_scope()) if args.append else set()
    candidates = []
    for tid, row in inv.taxa.items():
        sources = set(split(row.get("attested_by", "")))
        if not sources or tid in existing:
            continue
        if not inv.is_species_or_below(tid):
            continue
        if args.rank and row.get("rank") != args.rank:
            continue
        names = [inv.lpsn[lid] for lid in inv.lpsn_by_taxon.get(tid, [])]
        correct_typed = [n for n in names if n.get("is_correct_name") == "1" and n.get("type_strain_ids")]
        # An identity mapping: LPSN links a GTDB species to the name, or the
        # species is a 1:1 closeMatch. A broadMatch alone is pooling, not identity.
        lpsn_gtdb = {g for n in names for g in split(n.get("gtdb_ids", ""))}
        has_gtdb = any(m["gtdb_id"] in lpsn_gtdb or m["predicate"] == "skos:closeMatch"
                       for m in inv.gtdb.get(tid, []))
        strain_count = len(inv.strains.get(tid, []))
        if args.rule == "core" and not (strain_count and correct_typed and has_gtdb):
            continue
        # NCBI itself, the attesting sources, and GTDB when it maps (#5).
        n_sources = 1 + len(sources) + (1 if has_gtdb else 0)
        candidates.append((-n_sources, -strain_count, int(tid.split(":")[1]), tid, row["label"], n_sources,
                           strain_count))
    candidates.sort()
    # A headerless append onto a missing or empty scope file would make the
    # first data row the header (#10).
    if not args.append or not SCOPE_PATH.exists() or SCOPE_PATH.stat().st_size == 0:
        print("identifier\tadded\treason")
    selected = candidates if args.all else candidates[:args.top]
    for _a, _b, _c, tid, label, n_sources, strain_count in selected:
        reason = (f"{args.rule} rule: {label}, {n_sources} sources incl. NCBI, "
                  f"{strain_count} BacDive strains, LPSN correct name with type strain, GTDB mapping"
                  if args.rule == "core" else f"{args.rule} rule: {label}, {n_sources} sources incl. NCBI")
        print(f"{tid}\t{args.date}\t{reason}")
    print(f"{len(selected)} of {len(candidates)} candidates proposed", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
