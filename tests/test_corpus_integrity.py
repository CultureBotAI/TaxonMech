"""Corpus-wide invariants that per-record validation cannot see."""

from __future__ import annotations

import csv
from collections import Counter

from taxonmech.seed import PATHS_LOCKFILE, load_lockfile
from taxonmech.validation.write_validated import validate_taxon


def test_identifiers_are_unique(records):
    dupes = [k for k, v in Counter(d["identifier"] for _, d in records).items() if v > 1]
    assert not dupes, f"duplicate identifiers: {dupes}"


def test_every_record_validates_closed(records):
    bad = {str(p): [e.message[:120] for e in errs] for p, d in records if (errs := validate_taxon(d))}
    assert not bad, bad


def test_file_location_matches_domain_and_lockfile(records, repo_root):
    """`data/taxa/<domain>/<slug>.yaml`: the directory is derived from the
    record and the slug is pinned in PATHS.tsv, so a moved or renamed file and
    its content cannot disagree."""
    lock = load_lockfile()
    wrong = []
    for path, doc in records:
        expected_dir = (doc.get("taxon_domain") or "OTHER").lower()
        if path.parent.name != expected_dir:
            wrong.append(f"{path.relative_to(repo_root)}: domain {doc.get('taxon_domain')}")
        if lock.get(doc["identifier"]) != path.stem:
            wrong.append(f"{path.relative_to(repo_root)}: not pinned as {path.stem} in {PATHS_LOCKFILE.name}")
    assert not wrong, wrong


def test_lockfile_has_no_entries_without_a_record(records):
    on_disk = {d["identifier"] for _, d in records}
    orphans = sorted(set(load_lockfile()) - on_disk)
    assert not orphans, f"PATHS.tsv pins identifiers with no record: {orphans[:10]}"


def test_lineage_ends_at_the_parent(records):
    bad = []
    for path, doc in records:
        lineage = doc.get("lineage") or []
        parent = doc.get("parent_taxon")
        if lineage and parent and lineage[-1]["taxon_id"] != parent:
            bad.append(path.name)
    assert not bad, f"lineage does not end at parent_taxon: {bad}"


def test_gathered_strains_name_a_descendant_of_the_record(records, repo_root):
    """`classified_as` must be a taxon strictly below this record in the
    committed NCBI inventory (#9)."""
    parents = {}
    with (repo_root / "data" / "raw" / "ncbitaxon_taxa.tsv").open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            parents[row["taxon_id"]] = row["parent_id"]

    def is_ancestor(ancestor: str, taxon: str) -> bool:
        cur = parents.get(taxon)
        while cur:
            if cur == ancestor:
                return True
            cur = parents.get(cur)
        return False

    bad = [f"{p.name}:{s['strain_id']}:{s['classified_as']}" for p, d in records
           for s in d.get("strains") or []
           if s.get("classified_as") and not is_ancestor(d["identifier"], s["classified_as"])]
    assert not bad, bad


def test_strain_listing_never_exceeds_the_count(records):
    bad = [p.name for p, d in records if len(d.get("strains") or []) > (d.get("strain_count") or 0)]
    assert not bad, bad


def test_type_strains_match_a_nomenclature_designation(records):
    """A strain flagged as type must carry a deposit LPSN names for this taxon."""
    bad = []
    for path, doc in records:
        designations = {t for n in doc.get("nomenclature") or []
                        for t in n.get("type_strain_designations") or []}
        for s in doc.get("strains") or []:
            if s.get("is_type_strain") and not designations & set(s.get("culture_collection_ids") or []):
                bad.append(f"{path.name}:{s['strain_id']}")
    assert not bad, bad


def test_type_strains_are_listed_first(records):
    bad = []
    for path, doc in records:
        flags = [bool(s.get("is_type_strain")) for s in doc.get("strains") or []]
        if flags != sorted(flags, reverse=True):
            bad.append(path.name)
    assert not bad, f"type strains not listed first: {bad}"


def test_every_record_has_an_ncbi_attestation(records):
    bad = [p.name for p, d in records
           if not any(a["source"] == "NCBITAXON" for a in d.get("source_attestations") or [])]
    assert not bad, bad


def test_graph_edges_reference_declared_nodes(records):
    bad = []
    for path, doc in records:
        for g in doc.get("causal_graphs") or []:
            ids = {n["node_id"] for n in g["nodes"]}
            for e in g["edges"]:
                for end in (e["subject"], e["object"]):
                    if end not in ids:
                        bad.append(f"{path.name}:{g['graph_id']}:{end}")
    assert not bad, f"edges referencing undeclared nodes: {bad}"


def test_local_ids_are_unique_within_record(records):
    bad = []
    for path, doc in records:
        for key, idk in (("strains", "strain_id"), ("causal_graphs", "graph_id"),
                         ("discussions", "discussion_id"), ("nomenclature", "name_id")):
            ids = [x[idk] for x in doc.get(key) or []]
            if len(ids) != len(set(ids)):
                bad.append(f"{path.name}:{key}")
    assert not bad, f"duplicate local ids: {bad}"


def test_discussion_anchors_resolve(records):
    """`attaches_to` uses `<section>#<local id>`; the id must exist in that section."""
    bad = []
    for path, doc in records:
        anchors = {
            "strains": {s["strain_id"] for s in doc.get("strains") or []},
            "causal_graphs": {g["graph_id"] for g in doc.get("causal_graphs") or []},
            "nomenclature": {n["name_id"] for n in doc.get("nomenclature") or []},
        }
        for disc in doc.get("discussions") or []:
            for a in disc.get("attaches_to") or []:
                section, _, local = a.partition("#")
                if section in anchors and local not in anchors[section]:
                    bad.append(f"{path.name}:{disc['discussion_id']}:{a}")
    assert not bad, bad


def test_reviewed_records_carry_history(records):
    bad = [p.name for p, d in records
           if d.get("mapping_status") == "REVIEWED" and not d.get("curation_history")]
    assert not bad, bad
