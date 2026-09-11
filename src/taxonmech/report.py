#!/usr/bin/env python3
"""Corpus report: records per domain, rank and status; source coverage;
strain and type-strain totals; GTDB and LPSN coverage.

Usage:
    python scripts/corpus_report.py
    python scripts/corpus_report.py --tsv reports/corpus.tsv
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TAXA_DIR = REPO_ROOT / "data" / "taxa"


def load_records(root: Path = TAXA_DIR) -> list[tuple[Path, dict]]:
    import yaml

    out = []
    for path in sorted(root.rglob("*.yaml")):
        with path.open(encoding="utf-8") as fh:
            out.append((path, yaml.safe_load(fh)))
    return out


def summarize(records: list[tuple[Path, dict]]) -> dict:
    by_domain = Counter(d.get("taxon_domain") for _, d in records)
    by_rank = Counter(d.get("rank") for _, d in records)
    by_status = Counter(d.get("mapping_status") for _, d in records)
    by_source = Counter(a["source"] for _, d in records for a in d.get("source_attestations") or [])
    sources_per_record = Counter(len({a["source"] for a in d.get("source_attestations") or []})
                                 for _, d in records)
    strain_total = sum(d.get("strain_count") or 0 for _, d in records)
    strains_listed = sum(len(d.get("strains") or []) for _, d in records)
    with_type_strain = sum(1 for _, d in records
                           if any(s.get("is_type_strain") for s in d.get("strains") or []))
    with_lpsn = sum(1 for _, d in records if d.get("nomenclature"))
    with_correct_name = sum(1 for _, d in records
                            if any(n.get("is_correct_name") for n in d.get("nomenclature") or []))
    with_gtdb = sum(1 for _, d in records if d.get("taxonomy_mappings"))
    # The GTDB attestation carries the primary (identity) species' genomes; the
    # pooled broadMatch species in taxonomy_mappings belong to other taxa.
    genomes = sum(a.get("assertion_count") or 0 for _, d in records
                  for a in d.get("source_attestations") or [] if a.get("source") == "GTDB")
    with_graphs = sum(1 for _, d in records if d.get("causal_graphs"))
    edges = sum(len(g.get("edges") or []) for _, d in records for g in d.get("causal_graphs") or [])
    capped = sum(1 for _, d in records if (d.get("strain_count") or 0) > len(d.get("strains") or []))
    return {
        "total": len(records),
        "by_domain": dict(by_domain.most_common()),
        "by_rank": dict(by_rank.most_common()),
        "by_status": dict(by_status.most_common()),
        "by_source": dict(by_source.most_common()),
        "sources_per_record": dict(sorted(sources_per_record.items())),
        "strain_total": strain_total,
        "strains_listed": strains_listed,
        "records_with_capped_listing": capped,
        "with_type_strain": with_type_strain,
        "with_lpsn": with_lpsn,
        "with_correct_name": with_correct_name,
        "with_gtdb": with_gtdb,
        "genomes": genomes,
        "with_graphs": with_graphs,
        "edges": edges,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tsv", type=Path, help="Also write a per-record TSV here.")
    args = parser.parse_args(argv)

    records = load_records()
    if not records:
        print(f"No records under {TAXA_DIR}", file=sys.stderr)
        return 0
    s = summarize(records)
    print(f"{s['total']} taxon records")
    print("\nBy domain:")
    for k, v in s["by_domain"].items():
        print(f"  {k:16s} {v:6d}")
    print("\nBy rank:")
    for k, v in s["by_rank"].items():
        print(f"  {k:16s} {v:6d}")
    print("\nBy status:")
    for k, v in s["by_status"].items():
        print(f"  {k:16s} {v:6d}")
    print("\nRecords attested by source:")
    for k, v in s["by_source"].items():
        print(f"  {k:16s} {v:6d}")
    print("\nSources per record:")
    for k, v in s["sources_per_record"].items():
        print(f"  {k} source(s)      {v:6d}")
    print(
        f"\nStrains: {s['strain_total']} classified, {s['strains_listed']} listed "
        f"({s['records_with_capped_listing']} records capped); "
        f"{s['with_type_strain']} records list a type strain"
    )
    print(
        f"LPSN: {s['with_lpsn']} records carry nomenclature, {s['with_correct_name']} with a correct name   "
        f"GTDB: {s['with_gtdb']} records mapped, {s['genomes']} genomes"
    )
    print(f"Causal graphs: {s['with_graphs']} records ({s['edges']} evidence-backed edges)")

    if args.tsv:
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh, delimiter="\t", lineterminator="\n")
            w.writerow(["identifier", "label", "rank", "domain", "status", "sources", "strain_count",
                        "type_strain", "gtdb_mappings", "genomes"])
            for _path, d in records:
                w.writerow([
                    d["identifier"], d["label"], d.get("rank"), d.get("taxon_domain"),
                    d.get("mapping_status"),
                    len({a["source"] for a in d.get("source_attestations") or []}),
                    d.get("strain_count") or 0,
                    int(any(x.get("is_type_strain") for x in d.get("strains") or [])),
                    len(d.get("taxonomy_mappings") or []),
                    sum(a.get("assertion_count") or 0 for a in d.get("source_attestations") or []
                        if a.get("source") == "GTDB"),
                ])
    return 0


if __name__ == "__main__":
    sys.exit(main())
