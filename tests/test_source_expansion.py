"""Whole-source capture, exact identifiers and bounded-memory corpus behavior."""

import csv
import json

import pytest
import yaml

from scripts.corpus import DiskRecords
from taxonmech import bacdive_snapshot
from taxonmech.bacdive_v2 import genome_links, load_identities, records
from taxonmech.gold_genomes import _HEADERS, _rows, extract_gold_genomes
from taxonmech.gold_snapshot import project, workbook_rows
from taxonmech.ncbi_assemblies import extract_links, read_summary
from taxonmech.source_catalog import index_terms, query, write_chunks
from tests.test_gold_genomes import STRAINS, organism, workbook


def test_gold_projection_preserves_all_rows_and_exact_chain_behavior(tmp_path):
    from openpyxl import load_workbook

    path = workbook(tmp_path, organisms=[organism(), organism("Go2", "")], bad_dimensions=True)
    book = load_workbook(path, read_only=True, data_only=True)
    try:
        for sheet in _HEADERS:
            assert list(workbook_rows(path, sheet)) == list(_rows(book, sheet))
    finally:
        book.close()
    destination = tmp_path / "projection"
    result = project(path, destination)
    assert result["outputs"]["Organism"]["rows"] == 2
    assert extract_gold_genomes(destination, STRAINS) == extract_gold_genomes(path, STRAINS)
    (destination / "organisms.jsonl.gz").write_bytes(b"corrupt")
    with pytest.raises(ValueError, match="checksum"):
        extract_gold_genomes(destination, STRAINS)


def test_disk_corpus_preserves_order_fresh_objects_and_independent_iterations(tmp_path):
    paths = []
    for number in [10, 2, 4]:
        path = tmp_path / f"taxon-{number}.yaml"
        path.write_text(yaml.safe_dump({"identifier": f"NCBITaxon:{number}", "strains": [{"label": "Ω"}]}))
        paths.append(path)
    records = DiskRecords(paths)
    try:
        assert len(records) == 3
        assert [path for path, _ in records] == paths
        assert records[-1] == records[2]
        assert records[::-1] == list(records)[::-1]
        assert [doc["identifier"] for _, doc in records.by_identifier()] == [
            "NCBITaxon:2",
            "NCBITaxon:4",
            "NCBITaxon:10",
        ]
        records[0][1]["strains"][0]["label"] = "changed"
        assert records[0][1]["strains"][0]["label"] == "Ω"
        left, right = iter(records), iter(records)
        assert next(left) == next(right)
        next(left)
        assert next(right)[0] == paths[1]
        with pytest.raises(IndexError):
            records[3]
    finally:
        records.close()


def bacdive_record(number=1):
    return {
        "General": {
            "BacDive-ID": number,
            "NCBI tax id": [
                {"NCBI tax id": 2, "Matching level": "species"},
                {"NCBI tax id": 3, "Matching level": "strain"},
            ],
        },
        "Name and taxonomic classification": {"strain designation": "Native strain"},
        "Literature": {"culture collection no.": "DSM 1, ATCC BAA-1556"},
        "Sequence information": {
            "Genome sequences": [
                {
                    "INSDC accession": "GCA_000000001",
                    "BV-BRC accession": "123.45",
                    "IMG accession": "1234567890",
                    "@ref": 1,
                }
            ],
            "16S sequences": [{"accession": "GCA_000000002.1"}],
        },
    }


def test_bacdive_complete_capture_and_v2_same_row_identifiers(tmp_path, monkeypatch):
    census = (b"Comments\nID,species,designation_header,strain_number_header,is_type_strain_header\n"
              b"1,Species,X,DSM 1,1\n,,,,\n2,Other,Y,,0\n")
    payload = {"results": {str(i): bacdive_record(i) for i in (1, 2)}, "count": 2, "next": None}
    monkeypatch.setattr(
        bacdive_snapshot, "request", lambda url: census if "csv" in url else json.dumps(payload).encode()
    )
    result = bacdive_snapshot.capture(tmp_path)
    assert result["census_count"] == 2 and result["empty_census_rows"] == 1
    assert result["missing_api_ids"] == [] and len(list(records(tmp_path))) == 2
    strains, _ = load_identities(tmp_path, {})
    assert strains["kgmicrobe.strain:bacdive_1"]["taxon_ids"] == {"NCBITaxon:3"}
    assemblies, genomes, excluded = genome_links(tmp_path)
    assert not excluded
    assert {r["assembly_id"] for r in assemblies} == {"ncbi.assembly:GCA_000000001"}
    assert {r["genome_id"] for r in genomes} == {"patric:123.45", "img.taxon:1234567890"}
    assert all("16S" not in row["source_field"] for row in [*assemblies, *genomes])
    monkeypatch.setattr(bacdive_snapshot, "request", lambda _: pytest.fail("cached capture must replay"))
    assert bacdive_snapshot.capture(tmp_path)["records"] == result["records"]


@pytest.mark.parametrize("value", [b"ID,species,\n1,X,\n1,Y,\n", b"ID,species,\n,X,\n"])
def test_bacdive_census_rejects_duplicate_and_nonempty_missing_ids(value):
    with pytest.raises(ValueError):
        bacdive_snapshot.census(value)


def summary(tmp_path, rows, header_prefix="#"):
    fields = [
        "assembly_accession",
        "taxid",
        "species_taxid",
        "organism_name",
        "infraspecific_name",
        "biosample",
        "bioproject",
        "version_status",
        "assembly_level",
        "asm_name",
    ]
    path = tmp_path / "assembly_summary.txt"
    with path.open("w", newline="") as handle:
        handle.write("## source metadata\n" + header_prefix + "\t".join(fields) + "\n")
        writer = csv.DictWriter(handle, fields, delimiter="\t", lineterminator="\n")
        for row in rows:
            writer.writerow(
                {
                    "assembly_accession": "GCA_000000001.1",
                    "taxid": "5",
                    "species_taxid": "5",
                    "organism_name": "Source name",
                    "infraspecific_name": "strain=DSM 6724",
                    "biosample": "SAMN1",
                    "bioproject": "PRJNA1",
                    "version_status": "latest",
                    "assembly_level": "Complete Genome",
                    "asm_name": "Assembly",
                    **row,
                }
            )
    return path


@pytest.mark.parametrize("prefix", ["#", "# "])
def test_primary_ncbi_culture_links_keep_same_assembly_sample_chain(tmp_path, prefix):
    path = summary(tmp_path, [{}, {"assembly_accession": "GCF_000000001.7", "biosample": "SAMN2"}], prefix)
    assemblies, related, excluded = extract_links([path], STRAINS, {"NCBITaxon:5"})
    assert not excluded and len(assemblies) == 2
    assert {(r["source_id"], r["record_id"]) for r in related if r["record_type"] == "BIOSAMPLE"} == {
        ("ncbi.assembly:GCA_000000001.1", "biosample:SAMN1"),
        ("ncbi.assembly:GCF_000000001.7", "biosample:SAMN2"),
    }


@pytest.mark.parametrize(
    "row",
    [
        {"infraspecific_name": "strain=6724"},
        {"infraspecific_name": "strain=DSM 06724"},
        {"infraspecific_name": "cultivar=DSM 6724"},
        {"infraspecific_name": "strain=Species DSM 6724"},
        {"version_status": "suppressed"},
        {"version_status": "replaced"},
        {"taxid": "99"},
    ],
)
def test_primary_ncbi_does_not_infer_strain_identity_or_use_historical_versions(tmp_path, row):
    path = summary(tmp_path, [row])
    assert len(list(read_summary(path))) == 1
    assert extract_links([path], STRAINS, {"NCBITaxon:5"}) == ([], [], [])


def test_catalog_paging_lookup_counts_and_integrity(tmp_path):
    rows = [{"assembly_accession": f"GCA_{i:09}.1", "biosample": "SAMN1"} for i in range(1, 6)]
    directory = tmp_path / "data/catalog"
    files = write_chunks(directory, "ncbi_genbank", rows, chunk_size=2)
    assert [item["rows"] for item in files] == [2, 2, 1]
    before = [(directory / item["path"]).read_bytes() for item in files]
    assert write_chunks(directory, "ncbi_genbank", rows, chunk_size=2) == files
    assert before == [(directory / item["path"]).read_bytes() for item in files]
    source = {
        "id": "ncbi_genbank",
        "rows": 5,
        "format": "jsonl.gz",
        "files": [{**item, "path": "data/catalog/" + item["path"]} for item in files],
    }
    result = query(source, "biosample:SAMN1", tmp_path, limit=2)
    assert result["total"] == 5 and len(result["records"]) == 2
    assert query(source, "ncbi.assembly:GCA_000000005.1", tmp_path)["total"] == 1
    assert query(source, "GCA_000000005", tmp_path)["total"] == 0
    (directory / files[0]["path"]).write_bytes(b"changed")
    with pytest.raises(ValueError, match="pin"):
        query(source, "SAMN1", tmp_path)


def test_source_discovery_ids_do_not_guess_taxonomy_from_name():
    assert index_terms("seqcode_names", {"id": 4, "name": "Escherichia coli"}) == {"seqcode:4"}
    assert "NCBITaxon:562" not in index_terms("straininfo", {"strain": {"siID": 1, "name": "562"}})


def test_taxonomy_census_agrees_with_actual_attestations(repo_root):
    manifest = yaml.safe_load((repo_root / "data/raw/MANIFEST.yaml").read_text())["universe"]
    with (repo_root / "data/raw/ncbitaxon_taxa.tsv").open() as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert manifest["attested_taxa"] == sum(bool(row["attested_by"]) for row in rows)
    assert manifest["total_taxa"] == len(rows)
    assert (manifest["attested_taxa"] + manifest["ancestor_taxa"]
            + manifest["retired_context_taxa"]) == len(rows)


def test_every_eligible_prokaryote_is_in_the_committed_scope(repo_root):
    from taxonmech.ncbi_taxdump import prokaryote_taxa
    from taxonmech.seed import Inventory, load_scope

    with (repo_root / "data/raw/ncbitaxon_taxa.tsv").open() as handle:
        taxa = {row["taxon_id"]: row for row in csv.DictReader(handle, delimiter="\t")}
    parents = {tid: row["parent_id"] for tid, row in taxa.items() if row["parent_id"]}
    inventory = Inventory(taxa=taxa, gtdb={}, lpsn={}, lpsn_by_taxon={}, strains={},
                          cc_strains={}, media={}, gold={}, madin={}, bacto={})
    eligible = {tid for tid in prokaryote_taxa(parents, taxa) if inventory.is_species_or_below(tid)}
    assert eligible, "the complete primary prokaryote inventory must not be empty"
    missing = eligible - load_scope().keys()
    assert not missing, f"eligible bacterial/archaeal taxa missing from scope: {sorted(missing)[:20]}"


def test_bacdive_preserves_accession_suffix_spaces(tmp_path, monkeypatch):
    from taxonmech.genome_sources import culture_curie_key

    value = bacdive_record()
    value["Literature"]["culture collection no."] = "ATCC BAA 1556"
    monkeypatch.setattr("taxonmech.bacdive_v2.records", lambda _: iter([value]))
    strains, _ = load_identities(tmp_path, {})
    deposited = strains["kgmicrobe.strain:bacdive_1"]["culture_collection_ids"]
    assert deposited == {"kgmicrobe.strain:ATCC%20BAA%201556"}
    # CAFI requires BAA-1556. Preserve the unsupported source value without
    # turning it into a different, eligible culture accession.
    assert culture_curie_key(next(iter(deposited))) == ""
    assert culture_curie_key("kgmicrobe.strain:ATCC-BAA-1556") == "ATCC-BAA-1556"


def test_catalog_indexes_native_genome_fields_without_reading_descriptive_text():
    si = {"strain": {"siID": 1, "sequence": [
        {"accessionNumber": "GCA_000000001", "description": "GCA_000000002.1"}
    ]}, "deposits": [{"siDP": 2, "taxon": {"lpsn": 3}}]}
    terms = index_terms("straininfo", si)
    assert {"straininfo.strain:1", "straininfo.deposit:2", "lpsn:3",
            "GCA_000000001", "ncbi.assembly:GCA_000000001"} <= terms
    assert "GCA_000000002.1" not in terms
    assert "img.taxon:1234567890" in index_terms("bacdive", {"IMG accession": "1234567890"})
    assert "img.taxon:1234567890" in index_terms("gold_analysis_project", {
        "AP IMG TAXON ID": "1234567890"})
    gold = {"AP PROJECT GOLD IDS": "Gp1; Gp2", "AP ORGANISM GOLD ID": "Go3", "AP GENBANK":
            '[{"genbankId":"AQXM00000000","assemblyAccession":"GCA_000376245.1"}]'}
    assert {"gold:Gp1", "gold:Gp2", "gold:Go3", "AQXM00000000",
            "ncbi.assembly:GCA_000376245.1"} <= index_terms("gold_analysis_project", gold)


def test_bvbrc_links_and_atb_sample_evidence_do_not_cross_source_records(tmp_path, monkeypatch):
    from taxonmech import bvbrc
    from taxonmech.atb_links import build_evidence

    rows = [{"genome_id": f"1.{i}", "public": True, "superkingdom": "Bacteria", "taxon_id": 5,
             "culture_collection": "DSM 6724", "assembly_accession": f"GCA_00000000{i}.1",
             "biosample_accession": f"SAMN{i}", "bioproject_accession": "PRJNA1"} for i in (1, 2)]
    monkeypatch.setattr(bvbrc, "records", lambda _: iter(rows))
    assemblies, genomes, related, excluded = bvbrc.extract_links(tmp_path, STRAINS)
    assert not excluded and len(genomes) == len(assemblies) == 2
    _, evidence = build_evidence(related, assemblies, genomes)
    assert {(sample, genome) for _sid, sample, genome in evidence} == {
        ("biosample:SAMN1", "patric:1.1"), ("biosample:SAMN1", "ncbi.assembly:GCA_000000001.1"),
        ("biosample:SAMN2", "patric:1.2"), ("biosample:SAMN2", "ncbi.assembly:GCA_000000002.1")}
    rows[0]["culture_collection"] = "ATCC BAA 1556"
    assert len(bvbrc.extract_links(tmp_path, STRAINS)[0]) == 1
