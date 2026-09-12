"""Exact catalogue lookups distinguish samples, snapshots and genome versions."""

import json
import sqlite3

import pytest
import yaml

from taxonmech import atb, atb_query
from taxonmech.atb import _add_index_links, sha256
from taxonmech.atb_catalog import build_catalog
from taxonmech.atb_links import build_links
from taxonmech.atb_query import open_catalog, query_catalog
from taxonmech.extract import ASSEMBLY_FIELDS, GENOME_RECORD_FIELDS, RELATED_RECORD_FIELDS, write_tsv
from tests.test_atb_catalog import assembly_row, metadata_file
from tests.test_atb_links import GTDB, SAMPLE, SID, genome, ncbi, sample


@pytest.fixture
def catalog(tmp_path):
    rows = [assembly_row(SAMPLE, assembly_accession="ERZ123"),
            assembly_row("SAMN2", assembly_accession="ERZ124"),
            assembly_row("SAMN3", asm_fasta_on_osf="0", assembly_accession="ERZ125"),
            assembly_row("SAMN4;SAMN5", asm_fasta_on_osf="0", assembly_accession="NA"),
            assembly_row("SAMN6", asm_pipe_filter="META_FAIL", assembly_accession="ERZ126")]
    index = tmp_path / "catalog.sqlite"
    manifest = tmp_path / "MANIFEST.yaml"
    manifest.write_text("snapshot: fixture\n")
    build_catalog(metadata_file(tmp_path, rows), index, release="2025-05")
    strains, genomes, _ = build_links(rows, [sample()], [ncbi()], [genome()], release="2025-05")
    with sqlite3.connect(index) as conn:
        _add_index_links(conn, [{"strain_id": SID, "bacdive_id": "5",
                                 "culture_collection_ids": "kgmicrobe.strain:DSM-30083"}], strains, genomes)
        conn.execute("INSERT INTO metadata VALUES (?,?)", ("crosslink_manifest_sha256", sha256(manifest)))
    conn = open_catalog(index, manifest=manifest)
    yield conn, index, manifest
    conn.close()


@pytest.fixture
def current_catalog(tmp_path):
    """A fully published local snapshot, deliberately outside any Git checkout."""
    raw = tmp_path / "data/raw"
    raw.mkdir(parents=True)
    strain = {"strain_id": SID, "bacdive_id": "5", "culture_collection_ids": "kgmicrobe.strain:DSM-30083"}
    write_tsv(raw / "bacdive_strains.tsv", list(strain), [strain])
    write_tsv(raw / "strain_related_records.tsv", RELATED_RECORD_FIELDS, [sample()])
    write_tsv(raw / "strain_assemblies.tsv", ASSEMBLY_FIELDS, [ncbi()])
    write_tsv(raw / "strain_genome_records.tsv", GENOME_RECORD_FIELDS, [genome()])
    source = metadata_file(tmp_path, [assembly_row(SAMPLE, comments='literal "source quotes"')])
    index = tmp_path / "data/indexes/atb.sqlite"
    out = tmp_path / "data/atb"
    config = {"release": "2025-05", "url": "https://osf.io/download/4kjh7/",
              "sha256": sha256(source), "metadata_path": str(source), "index_path": str(index),
              "license": "CC-BY-4.0", "citation": "https://doi.org/10.1101/2024.03.08.584059"}
    (tmp_path / "conf").mkdir()
    (tmp_path / "conf/allthebacteria.yaml").write_text(yaml.safe_dump(config))
    atb.generate(source, index, out, raw, config, apply=True)
    return tmp_path, index, out / "MANIFEST.yaml"


@pytest.mark.parametrize("by,value", [
    ("sample", SAMPLE), ("sample", "biosample:" + SAMPLE), ("ena_analysis", "ena.analysis:ERZ123"),
    ("atb_id", "atb.assembly:202505." + SAMPLE), ("strain", SID), ("strain", "bacdive:5"),
    ("strain", "kgmicrobe.strain:DSM-30083"), ("genome", "GCF_000005845.1"), ("genome", GTDB),
])
def test_forward_and_reverse_exact_lookups_retain_two_source_evidence(catalog, by, value):
    result = query_catalog(catalog[0], by=by, value=value, evidence=True)
    assert result["total"] == 1
    row = result["results"][0]
    assert row["sample_accession"] == SAMPLE
    assert row["atb_id"] == "atb.assembly:202505." + SAMPLE
    assert row["strain_links"][0]["strain_id"] == SID
    assert {link["genome_id"] for link in row["genome_links"]} == {GTDB, "ncbi.assembly:GCF_000005845.1"}
    assert row["genome_links"][0]["genome_id"].startswith("ncbi.assembly:")
    assert all(link["relationship"] == "shares_biosample" for link in row["genome_links"])
    assert row["genome_links"][0]["source_evidence"][0]["sample"]["record_id"] == "biosample:" + SAMPLE


@pytest.mark.parametrize("by,value", [
    ("genome", "GCF_000005845.2"), ("genome", "GCF_000005845"), ("strain", "DSM 30083"),
    ("sample", "SAMN4"), ("sample", "' OR 1=1 --"),
])
def test_lookups_do_not_guess_versions_names_or_split_composite_samples(catalog, by, value):
    assert query_catalog(catalog[0], by=by, value=value)["total"] == 0


def test_catalog_includes_unlinked_and_unsafe_available_rows_with_source_status(catalog):
    for sample_id in ("SAMN2", "SAMN6"):
        row = query_catalog(catalog[0], by="sample", value=sample_id)["results"][0]
        assert row["atb_id"] and row["strain_links"] == row["genome_links"] == []
        assert bool(row["crosslink_exclusion"]) == (sample_id == "SAMN6")
    assert query_catalog(catalog[0], by="ena_analysis", value="ERZ125")["total"] == 0
    row = query_catalog(catalog[0], by="ena_analysis", value="ERZ125", all_statuses=True)["results"][0]
    assert row["atb_id"] is None and row["crosslink_exclusion"] == "assembly_unavailable"
    row = query_catalog(catalog[0], by="sample", value="SAMN4;SAMN5", all_statuses=True)["results"][0]
    assert row["sample_accession"] == "SAMN4;SAMN5" and row["atb_id"] is None


def test_exact_species_search_pages_without_treating_classification_as_a_strain_link(catalog):
    args = {"by": "species", "value": "Paucilactobacillus hokkaidonensis", "limit": 1}
    first = query_catalog(catalog[0], **args)
    second = query_catalog(catalog[0], **args, offset=1)
    assert first["total"] == second["total"] == 3
    assert first["results"][0]["sample_accession"] != second["results"][0]["sample_accession"]
    assert second["results"][0]["strain_links"] == []


def test_snapshot_identifiers_cannot_be_resolved_against_another_release(catalog):
    with pytest.raises(ValueError, match="snapshot"):
        query_catalog(catalog[0], by="atb_id", value="atb.assembly:202408." + SAMPLE)
    result = query_catalog(catalog[0], by="atb_id", value="atb.assembly:202505.SAMN3", all_statuses=True)
    assert result["total"] == 0  # An unavailable metadata row is not an assembly.


@pytest.mark.parametrize("identifier", ["NA", "GCA_000005845.1", "ERZ123.1"])
def test_ena_lookup_does_not_treat_missing_values_or_assemblies_as_analysis_ids(catalog, identifier):
    with pytest.raises(ValueError, match="ERZ"):
        query_catalog(catalog[0], by="ena_analysis", value=identifier)


def test_missing_stale_or_incomplete_index_is_rejected_and_read_only(catalog, tmp_path):
    conn, index, manifest = catalog
    with pytest.raises(sqlite3.OperationalError, match="readonly"):
        conn.execute("DELETE FROM assembly")
    missing = tmp_path / "absent.sqlite"
    with pytest.raises(ValueError, match="missing"):
        open_catalog(missing)
    assert not missing.exists()
    manifest.write_text("snapshot: changed\n")
    with pytest.raises(ValueError, match="differs"):
        open_catalog(index, manifest=manifest)
    with sqlite3.connect(index) as writer:
        writer.execute("DELETE FROM metadata WHERE key = 'crosslink_manifest_sha256'")
    with pytest.raises(ValueError, match="completed"):
        open_catalog(index)


def test_cli_json_and_tsv_preserve_source_quotes_and_evidence(current_catalog, monkeypatch, capsys):
    root, index, manifest = current_catalog
    monkeypatch.setattr(atb_query, "ROOT", root)
    monkeypatch.setattr(atb_query, "ATB_DIR", manifest.parent)
    args = ["--index", str(index), "--sample", SAMPLE, "--evidence"]
    assert atb_query.main(args) == 0
    row = json.loads(capsys.readouterr().out)["results"][0]
    assert row["genome_links"][0]["source_evidence"]
    assert row["comments"] == 'literal "source quotes"'
    assert atb_query.main([*args, "--format", "tsv"]) == 0
    output = capsys.readouterr().out
    assert output.startswith("atb_id\tsample_accession\t") and "shares_biosample" in output


@pytest.mark.parametrize("change", ["source_pin", "raw_inventory", "crosswalk", "index_metadata"])
def test_cli_rejects_stale_dependencies_even_when_the_old_manifest_hash_still_matches(
    current_catalog, monkeypatch, capsys, change,
):
    root, index, manifest = current_catalog
    before = manifest.read_bytes()
    if change == "source_pin":
        path = root / "conf/allthebacteria.yaml"
        config = yaml.safe_load(path.read_text())
        config["sha256"] = "0" * 64
        path.write_text(yaml.safe_dump(config))
    elif change == "index_metadata":
        with sqlite3.connect(index) as conn:
            conn.execute("UPDATE metadata SET value='2024-08' WHERE key='release'")
    else:
        path = root / ("data/raw/strain_assemblies.tsv" if change == "raw_inventory"
                       else "data/atb/genome_links.tsv")
        path.write_text(path.read_text().replace("GCF_000005845.1", "GCF_000005845.99"))
    assert manifest.read_bytes() == before
    monkeypatch.setattr(atb_query, "ROOT", root)
    monkeypatch.setattr(atb_query, "ATB_DIR", manifest.parent)
    with pytest.raises(SystemExit) as error:
        atb_query.main(["--index", str(index), "--genome", "GCF_000005845.1"])
    assert error.value.code == 1
    assert "AllTheBacteria:" in capsys.readouterr().err


def test_standalone_api_can_read_an_explicit_historical_snapshot(current_catalog):
    root, index, manifest = current_catalog
    path = root / "data/raw/strain_assemblies.tsv"
    path.write_text(path.read_text().replace("GCF_000005845.1", "GCF_000005845.99"))
    conn = open_catalog(index, manifest=manifest)
    try:
        assert query_catalog(conn, by="genome", value="GCF_000005845.1")["total"] == 1
    finally:
        conn.close()


@pytest.mark.parametrize("options", [{"limit": 0}, {"limit": 1001}, {"offset": -1}])
def test_paging_limits_are_bounded(catalog, options):
    with pytest.raises(ValueError, match="limit"):
        query_catalog(catalog[0], by="sample", value=SAMPLE, **options)
