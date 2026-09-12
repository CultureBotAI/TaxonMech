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
    # Listed strain coverage only. Deduplicate when a strain occurs in both
    # a species and a descendant record, or the source cites it twice.
    assembly_pairs = {(s["strain_id"], a["assembly_id"]) for _, d in records
                      for s in d.get("strains") or [] for a in s.get("genome_assemblies") or []}
    genome_record_pairs = {(s["strain_id"], g["genome_id"]) for _, d in records
                           for s in d.get("strains") or [] for g in s.get("genome_records") or []}
    # NCBI first. These are identifier counts within each database; records
    # in different databases are not collapsed into biological genomes.
    pairs_by_database = {
        "NCBI": assembly_pairs,
        "GTDB": {(sid, gid) for sid, gid in genome_record_pairs if gid.startswith("gtdb.genome:")},
        "PATRIC": {(sid, gid) for sid, gid in genome_record_pairs if gid.startswith("patric:")},
        "IMG": {(sid, gid) for sid, gid in genome_record_pairs if gid.startswith("img.taxon:")},
        "AllTheBacteria": {(sid, gid) for sid, gid in genome_record_pairs
                          if gid.startswith("atb.assembly:")},
    }
    genome_coverage = {
        database: {"strain_links": len(pairs), "strains": len({sid for sid, _ in pairs}),
                   "identifiers": len({gid for _, gid in pairs})}
        for database, pairs in pairs_by_database.items()
    }
    related_pairs = {(s["strain_id"], link["record_type"], link["record_id"])
                     for _, d in records for s in d.get("strains") or []
                     for link in s.get("related_records") or []}
    related_coverage = {
        kind: {"strain_links": len(pairs), "strains": len({sid for sid, _ in pairs}),
               "identifiers": len({rid for _, rid in pairs})}
        for kind in ("BIOSAMPLE", "BIOPROJECT", "GOLD_ORGANISM", "GOLD_PROJECT", "GOLD_ANALYSIS",
                     "STRAININFO_STRAIN", "STRAININFO_DEPOSIT", "NUCLEOTIDE_SEQUENCE")
        if (pairs := {(sid, rid) for sid, record_type, rid in related_pairs if record_type == kind})
    }
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
        "listed_strains_with_assemblies": len({sid for sid, _ in assembly_pairs}),
        "listed_strain_assembly_links": len(assembly_pairs),
        "listed_assemblies": len({aid for _, aid in assembly_pairs}),
        "listed_genome_record_links": len(genome_record_pairs),
        "listed_genome_records": len({gid for _, gid in genome_record_pairs}),
        "listed_strains_with_genome_records": len({sid for sid, _ in genome_record_pairs}),
        "listed_genome_links_by_database": genome_coverage,
        "listed_strains_with_any_genome": len({sid for sid, _ in assembly_pairs | genome_record_pairs}),
        "listed_related_records_by_type": related_coverage,
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
        f"Listed strain-to-assembly links: {s['listed_strain_assembly_links']} pairs, "
        f"{s['listed_strains_with_assemblies']} strains, {s['listed_assemblies']} assembly identifiers "
        "(deduplicated; inventories in data/raw/strain_assemblies.tsv and data/straininfo/assemblies.tsv)"
    )
    print(
        f"Additional genome-record links: {s['listed_genome_record_links']} pairs, "
        f"{s['listed_strains_with_genome_records']} strains, {s['listed_genome_records']} identifiers "
        "(full inventories in data/raw/strain_genome_records.tsv and data/atb/strain_links.tsv)"
    )
    for database, coverage in s["listed_genome_links_by_database"].items():
        print(f"  {database}: {coverage['strain_links']} strain-identifier pairs, "
              f"{coverage['identifiers']} identifiers, {coverage['strains']} strains")
    print("Counts are database identifiers, not unique biological genomes across databases.")
    for kind, coverage in s["listed_related_records_by_type"].items():
        print(f"  Related {kind}: {coverage['strain_links']} strain-record pairs, "
              f"{coverage['identifiers']} identifiers, {coverage['strains']} strains (not genome counts)")
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
