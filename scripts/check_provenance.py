#!/usr/bin/env python3
"""Verify hashes and coverage for the committed source inventories.

Every tracked TSV under data/raw/ must be listed in MANIFEST.yaml with matching
row count, byte count and sha256, and every manifest output must be tracked.
A committed inventory nobody can trace to an extraction is the failure this
guards against.
The ATB component additionally verifies its pinned source, raw dependencies,
compact overlap and exact reproduction of the evidenced crosswalks.
"""

from __future__ import annotations

import csv
import hashlib
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = REPO_ROOT / "data" / "raw"
MANIFEST = RAW_DIR / "MANIFEST.yaml"
SHA256_RE = re.compile(r"[0-9a-f]{64}")
SOURCE_RE = re.compile(r"kg-microbe@[0-9a-f]{40}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tsv_rows(path: Path) -> int:
    csv.field_size_limit(min(sys.maxsize, 2**31 - 1))
    with path.open(newline="", encoding="utf-8") as fh:
        return sum(1 for _row in csv.reader(fh, delimiter="\t")) - 1


def tracked_raw_tsvs() -> set[str]:
    completed = subprocess.run(["git", "ls-files", "--", "data/raw/*.tsv"], cwd=REPO_ROOT,
                               check=True, capture_output=True, text=True)
    return {Path(line).name for line in completed.stdout.splitlines() if line}


def manifest_contract_problems(manifest: dict) -> list[str]:
    failures = []
    if not SOURCE_RE.fullmatch(str(manifest.get("kg_microbe_source", ""))):
        failures.append("MANIFEST: kg_microbe_source must be kg-microbe@<40-character commit>")
    if not manifest.get("extracted_at"):
        failures.append("MANIFEST: extracted_at missing")
    for entry in manifest.get("inputs", []):
        for key in ("path", "bytes", "mtime"):
            if entry.get(key) in (None, ""):
                failures.append(f"MANIFEST input {entry.get('path', '<unnamed>')}: missing {key}")
        if entry.get("sha256") is not None and not SHA256_RE.fullmatch(str(entry["sha256"])):
            failures.append(f"MANIFEST input {entry.get('path')}: malformed sha256")
    paths = []
    for entry in manifest.get("outputs", []):
        for key in ("path", "rows", "bytes", "sha256"):
            if entry.get(key) in (None, ""):
                failures.append(f"MANIFEST output {entry.get('path', '<unnamed>')}: missing {key}")
        if not SHA256_RE.fullmatch(str(entry.get("sha256", ""))):
            failures.append(f"MANIFEST output {entry.get('path')}: malformed sha256")
        paths.append(entry.get("path"))
    if len(paths) != len(set(paths)):
        failures.append("MANIFEST: duplicate output paths")
    return failures


def problems() -> list[str]:
    if not MANIFEST.exists():
        return [f"{MANIFEST.relative_to(REPO_ROOT)} is missing"]
    manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8")) or {}
    failures = manifest_contract_problems(manifest)
    outputs = {e["path"]: e for e in manifest.get("outputs", []) if e.get("path")}
    tracked = tracked_raw_tsvs()
    uncovered = sorted(tracked - outputs.keys())
    stale = sorted(outputs.keys() - tracked)
    if uncovered:
        failures.append(f"committed raw TSVs without provenance: {', '.join(uncovered)}")
    if stale:
        failures.append(f"manifest outputs not committed as raw TSVs: {', '.join(stale)}")
    for name in sorted(tracked & outputs.keys()):
        entry, path = outputs[name], RAW_DIR / name
        if tsv_rows(path) != int(entry["rows"]):
            failures.append(f"{name}: row count differs from its manifest")
        if path.stat().st_size != int(entry["bytes"]):
            failures.append(f"{name}: byte count differs from its manifest")
        if sha256(path) != entry["sha256"]:
            failures.append(f"{name}: sha256 differs from its manifest")
    return failures


def causal_graph_provenance_problems(repo_root: Path = REPO_ROOT) -> list[str]:
    from collections import defaultdict

    from taxonmech.seed import (
        load_causal_graphs,
        load_scope,
        load_uniprot_proteins,
        split,
    )

    failures: list[str] = []
    raw_dir = repo_root / "data" / "raw"
    curation_dir = repo_root / "curation"
    overlays_dir = curation_dir / "causal_graphs"
    uniprot_path = curation_dir / "uniprot_proteins.tsv"
    scope_path = curation_dir / "seed_scope.tsv"
    taxa_path = raw_dir / "ncbitaxon_taxa.tsv"
    strains_path = raw_dir / "bacdive_strains.tsv"

    try:
        taxa: dict[str, dict[str, str]] | None = None
        if taxa_path.exists():
            with taxa_path.open(newline="", encoding="utf-8") as fh:
                taxa = {row["taxon_id"]: row for row in csv.DictReader(fh, delimiter="\t")}
        strains: dict[str, list[dict[str, str]]] | None = None
        if strains_path.exists():
            strains = defaultdict(list)
            with strains_path.open(newline="", encoding="utf-8") as fh:
                for row in csv.DictReader(fh, delimiter="\t"):
                    for tid in split(row.get("taxon_ids", "")):
                        strains[tid].append(row)
        uniprot_proteins = load_uniprot_proteins(uniprot_path, taxa=taxa)
        graphs_by_taxon, events_by_taxon = load_causal_graphs(
            overlays_dir,
            uniprot_path=uniprot_path,
            taxa=taxa,
            strains=strains,
        )
        referenced_uniprot = {
            (node.get("grounding") or "").strip()
            for graphs in graphs_by_taxon.values()
            for graph in graphs
            for node in (graph.get("nodes") or [])
            if isinstance(node, dict) and node.get("node_type") == "GENE_OR_PROTEIN"
        }
        for uid in sorted(set(uniprot_proteins) - referenced_uniprot):
            failures.append(
                f"{uniprot_path.relative_to(repo_root)}: {uid} is not referenced by any "
                f"GENE_OR_PROTEIN node in curation/causal_graphs/*.yaml"
            )
        for tid in sorted(graphs_by_taxon):
            if not events_by_taxon.get(tid):
                failures.append(
                    f"causal-graph overlay {tid}: missing or empty 'curation_history'"
                )
            for graph in graphs_by_taxon[tid]:
                gid = (graph.get("graph_id") or "").strip() if isinstance(graph.get("graph_id"), str) else ""
                host_taxon_nids = {
                    (n.get("node_id") or "").strip()
                    for n in (graph.get("nodes") or [])
                    if isinstance(n, dict)
                    and n.get("node_type") == "TAXON"
                    and (n.get("grounding") or "").strip() == tid
                }
                if not host_taxon_nids:
                    failures.append(
                        f"causal-graph overlay {tid} graph {gid!r}: missing TAXON node grounded to {tid}"
                    )
                expressed_nids = {
                    (e.get("object") or "").strip()
                    for e in (graph.get("edges") or [])
                    if isinstance(e, dict)
                    and (e.get("subject") or "").strip() in host_taxon_nids
                    and (e.get("predicate_id") or "").strip() == "RO:0002292"
                }
                outgoing_subjects = {
                    (e.get("subject") or "").strip()
                    for e in (graph.get("edges") or [])
                    if isinstance(e, dict)
                }
                for node in graph.get("nodes") or []:
                    if not isinstance(node, dict) or node.get("node_type") != "GENE_OR_PROTEIN":
                        continue
                    nid = (node.get("node_id") or "").strip()
                    uid = (node.get("grounding") or "").strip()
                    if host_taxon_nids and nid not in expressed_nids:
                        failures.append(
                            f"causal-graph overlay {tid} graph {gid!r} node {nid!r}: "
                            f"GENE_OR_PROTEIN node is not linked from host TAXON node "
                            f"via RO:0002292 (expresses)"
                        )
                    if nid not in outgoing_subjects:
                        failures.append(
                            f"causal-graph overlay {tid} graph {gid!r} node {nid!r}: "
                            f"GENE_OR_PROTEIN node has no outgoing functional/regulatory/causal edge"
                        )
                    ref = uniprot_proteins.get(uid)
                    if ref is not None:
                        full_ref_ecs = [
                            ec for ec in split(ref.get("ec_numbers", "")) if "-" not in ec
                        ]
                        node_ecs = [
                            x
                            for x in (node.get("xrefs") or [])
                            if isinstance(x, str) and x.startswith("EC:") and "-" not in x
                        ]
                        if node_ecs != full_ref_ecs:
                            failures.append(
                                f"causal-graph overlay {tid} graph {gid!r} node {nid!r}: "
                                f"full 4-part EC xrefs {node_ecs} != reference {full_ref_ecs} for {uid}"
                            )
                for edge in graph.get("edges") or []:
                    if not isinstance(edge, dict):
                        continue
                    eid = (edge.get("edge_id") or "").strip()
                    pred_id = (
                        (edge.get("predicate_id") or "").strip()
                        if isinstance(edge.get("predicate_id"), str)
                        else ""
                    )
                    if not pred_id:
                        failures.append(
                            f"causal-graph overlay {tid} graph {gid!r} edge {eid!r}: missing 'predicate_id'"
                        )
                    for ev in edge.get("evidence") or []:
                        if isinstance(ev, dict):
                            has_text = bool(
                                (ev.get("notes") or "").strip()
                                or (ev.get("snippet") or "").strip()
                            )
                            if not has_text:
                                failures.append(
                                    f"causal-graph overlay {tid} graph {gid!r} edge {eid!r}: "
                                    f"evidence {ev.get('reference')!r} missing 'notes' or 'snippet'"
                                )
        if scope_path.exists():
            scope = load_scope(scope_path)
            for tid in sorted(graphs_by_taxon):
                if tid not in scope:
                    failures.append(
                        f"causal-graph overlay {tid}: not present in {scope_path.relative_to(repo_root)}"
                    )
        if overlays_dir.exists():
            for overlay_file in sorted(overlays_dir.glob("*.yaml")):
                data = yaml.safe_load(overlay_file.read_text(encoding="utf-8"))
                identifier = (
                    (data.get("identifier") or "").strip()
                    if isinstance(data, dict) and isinstance(data.get("identifier"), str)
                    else ""
                )
                expected_stem = identifier.replace(":", "_")
                if identifier and overlay_file.stem != expected_stem:
                    failures.append(
                        f"{overlay_file.relative_to(repo_root)}: filename stem {overlay_file.stem!r} "
                        f"does not match identifier {identifier!r} (expected '{expected_stem}.yaml')"
                    )
    except SystemExit as exc:
        failures.append(str(exc))
    return failures


def main() -> int:
    failures = problems()
    from taxonmech.atb import provenance_problems
    from taxonmech.bacdive_v2 import records as bacdive_records
    from taxonmech.bvbrc import records as bvbrc_records
    from taxonmech.gold_genomes import validate_projection
    from taxonmech.source_catalog import check as catalog_problems
    from taxonmech.straininfo import provenance_problems as straininfo_problems

    failures.extend(provenance_problems(REPO_ROOT))
    failures.extend(straininfo_problems(REPO_ROOT))
    failures.extend(catalog_problems(REPO_ROOT))
    failures.extend(causal_graph_provenance_problems(REPO_ROOT))
    # Verify full source projections independently of the smaller biological
    # crosswalks; matching only the overlap must never pass as a source census.
    sum(1 for _ in bacdive_records(REPO_ROOT / "data/bacdive"))
    sum(1 for _ in bvbrc_records(REPO_ROOT / "data/bvbrc"))
    validate_projection(REPO_ROOT / "data/gold")
    if failures:
        print("provenance check failed:\n  " + "\n  ".join(failures), file=sys.stderr)
        return 1
    manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    print(f"provenance current: {len(manifest.get('outputs', []))} committed inventories from "
          f"{manifest.get('kg_microbe_source')}; ATB and StrainInfo snapshots and crosswalks verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
