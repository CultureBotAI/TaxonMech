"""ATB links retain their complete sample evidence through schema and seeding."""

from __future__ import annotations

import json
from copy import deepcopy

import pytest
import yaml
from jsonschema.validators import validator_for
from linkml.generators.jsonschemagen import JsonSchemaGenerator

from taxonmech import atb, seed
from taxonmech.atb_catalog import ASSEMBLY_COLUMNS, assembly_id
from taxonmech.extract import write_tsv
from taxonmech.validation.write_validated import (
    DEFAULT_SCHEMA_PATH,
    validate_taxon,
    write_validated_taxon,
)
from tests.test_atb_catalog import assembly_row
from tests.test_seed import _inventory


def _source(tmp_path):
    directory = tmp_path / "atb"
    directory.mkdir()
    sample = "SAMN02604091"
    row = assembly_row(sample, scientific_name="Escherichia coli")
    evidence = {
        "record_id": f"biosample:{sample}", "record_type": "BIOSAMPLE", "source": "GTDB",
        "source_id": "gtdb.genome:RS_GCF_000005845.2", "source_field": "ncbi_biosample",
        "matched_strain_id": "kgmicrobe.strain:DSM-30083",
        "source_strain_identifiers": "DSM 30083;ATCC 11775", "source_strain_field": "ncbi_strain_identifiers",
    }
    write_tsv(directory / "assemblies.tsv", list(ASSEMBLY_COLUMNS), [row])
    write_tsv(directory / "strain_links.tsv", list(atb.STRAIN_FIELDS), [{
        "strain_id": "kgmicrobe.strain:bacdive_5", "atb_id": assembly_id("2025-05", sample),
        "sample_id": f"biosample:{sample}", "sample_evidence_json": json.dumps([evidence]),
    }])
    write_tsv(directory / "genome_links.tsv", list(atb.GENOME_FIELDS), [])
    write_tsv(directory / "exclusions.tsv", list(atb.EXCLUSION_FIELDS), [])
    digest = "1" * 64
    (directory / "MANIFEST.yaml").write_text(yaml.safe_dump({
        "source": {"release": "2025-05", "sha256": digest, "url": "https://osf.io/download/4kjh7/",
                   "license": "CC-BY-4.0", "citation": "https://doi.org/10.1101/2024.03.08.584059"},
        "extracted_at": "2026-09-12T01:00:00Z",
        "catalog": {"release": "2025-05", "source_sha256": digest, "rows": 1,
                    "available_assemblies": 1, "unavailable_rows": 0, "non_single_sample_rows": 0,
                    "datasets": {"661k": 1}, "filters": {"PASS": 1}},
        "crosslinks": {"matched_samples": 1, "assembly_identifiers": 1, "strain_pairs": 1,
                       "strains": 1, "genome_pairs": 0, "excluded_samples": 0},
        "inputs": [{"path": f"data/raw/{name}", "bytes": 1, "sha256": digest} for name in atb.INPUT_NAMES],
        "outputs": [atb.describe_output(directory / name) for name in atb.OUTPUT_NAMES],
    }))
    return directory


def _document(tmp_path):
    inventory = _inventory()
    inventory.strain_genome_records = atb.genome_records(_source(tmp_path))
    concept = seed.build_concepts(inventory, ["NCBITaxon:562"])[0]
    return seed.build_document(concept, inventory)


@pytest.fixture(scope="module", params=["write_time", "generated_json_schema"])
def errors(request):
    if request.param == "write_time":
        return validate_taxon
    schema = json.loads(JsonSchemaGenerator(str(DEFAULT_SCHEMA_PATH)).serialize())
    validator_class = validator_for(schema)
    validator_class.check_schema(schema)
    validator = validator_class(schema)
    return lambda document: list(validator.iter_errors(document))


def test_complete_source_contract_is_valid_and_preserves_nested_assertions(tmp_path, errors):
    document = _document(tmp_path)
    assert not errors(document)
    link = document["strains"][0]["genome_records"][0]
    assert link["source"] == "ALLTHEBACTERIA"
    assert link["genome_id"] == link["source_id"] == "atb.assembly:202505.SAMN02604091"
    assert link["atb_evidence"]["sample_links"][0]["matched_strain_id"] == "kgmicrobe.strain:DSM-30083"
    assert "genome_records" not in document["strains"][1]


def test_gold_sample_chain_and_available_non_hq_assembly_without_ena_are_supported(tmp_path, errors):
    document = _document(tmp_path)
    evidence = document["strains"][0]["genome_records"][0]["atb_evidence"]
    evidence.pop("ena_analysis_id")
    evidence["assembly_filter"] = "ENA_ASM_SUBMIT_ERR"
    evidence["hq_filter"] = "MAX_CONTIG_NUM"
    evidence["sample_links"][0].update({
        "source": "GOLD", "source_id": "gold:Gp1", "source_organism_id": "gold:Go1",
        "source_project_id": "gold:Gp1", "source_field": "NCBI BIOSAMPLE ACCESSION",
        "source_strain_field": "ORGANISM CULTURE COLLECTION ID",
    })
    assert not errors(document)


@pytest.mark.parametrize("field", ["genome_id", "source_database", "source", "source_id", "atb_evidence"])
def test_atb_links_require_identity_database_and_evidence(tmp_path, errors, field):
    document = _document(tmp_path)
    del document["strains"][0]["genome_records"][0][field]
    assert errors(document)


@pytest.mark.parametrize("evidence", [None, {}, []])
def test_required_atb_evidence_cannot_be_null_or_an_empty_container(tmp_path, errors, evidence):
    document = _document(tmp_path)
    document["strains"][0]["genome_records"][0]["atb_evidence"] = evidence
    assert errors(document)


@pytest.mark.parametrize("field", [
    "release", "sample_id", "dataset", "run_accessions", "assembly_seqkit_sum", "assembly_filter",
    "hq_filter", "download_url", "archive_url", "archive_filename", "sample_links",
])
def test_atb_evidence_fields_cannot_be_silently_omitted(tmp_path, errors, field):
    document = _document(tmp_path)
    del document["strains"][0]["genome_records"][0]["atb_evidence"][field]
    assert errors(document)


@pytest.mark.parametrize("changes", [
    {"source_database": "patric"}, {"genome_id": "img.taxon:123"}, {"source": "BACDIVE"},
    {"source_id": "biosample:SAMN02604091"},
    {"genome_id": "atb.assembly:SAMN02604091"}, {"genome_id": "atb.assembly:202513.SAMN02604091"},
    {"genome_id": "patric:123.4", "source_id": "bacdive:5", "source_database": "patric", "source": "BACDIVE"},
])
def test_database_source_and_namespace_cannot_be_mixed(tmp_path, errors, changes):
    document = _document(tmp_path)
    document["strains"][0]["genome_records"][0].update(changes)
    assert errors(document)


@pytest.mark.parametrize("changes", [
    {"sample_links": []}, {"ena_analysis_id": "ncbi.assembly:GCA_000005845.2"},
    {"sample_id": "biosample:SAMN1;SAMN2"}, {"release": "latest"},
    {"assembly_seqkit_sum": "22841afbe77ffd5789a81fb81082f04f"}, {"assembly_filter": "RUN_CHANGE"},
    {"download_url": "https://example.org/assembly.fa.gz"}, {"unexpected_evidence": "discard me"},
])
def test_evidence_keeps_typed_identifiers_and_closed_shape(tmp_path, errors, changes):
    document = _document(tmp_path)
    document["strains"][0]["genome_records"][0]["atb_evidence"].update(changes)
    assert errors(document)


@pytest.mark.parametrize("changes", [
    {"record_type": "BIOPROJECT", "record_id": "bioproject:PRJNA1"},
    {"record_type": "BIOPROJECT"}, {"record_id": "gold:Go1"},
    {"source": "ALLTHEBACTERIA"},
    {"unmodeled_field": "silently lost"},
])
def test_nested_sample_evidence_is_biosample_only_and_closed(tmp_path, errors, changes):
    document = _document(tmp_path)
    sample = document["strains"][0]["genome_records"][0]["atb_evidence"]["sample_links"][0]
    sample.update(changes)
    assert errors(document)


def test_inventory_appends_atb_evidence_without_changing_primary_ncbi_links(tmp_path, monkeypatch):
    fixture = _inventory()
    sid = "kgmicrobe.strain:bacdive_5"
    ncbi = {"strain_id": sid, "assembly_id": "ncbi.assembly:GCA_000005845.2",
            "source": "BACDIVE", "source_id": "bacdive:5"}
    existing = {"strain_id": sid, "genome_id": "patric:123.10", "source_database": "patric",
                "source": "BACDIVE", "source_id": "bacdive:5"}
    tables = {
        "ncbitaxon_taxa.tsv": list(fixture.taxa.values()),
        "gtdb_mappings.tsv": [row for rows in fixture.gtdb.values() for row in rows],
        "lpsn_names.tsv": list(fixture.lpsn.values()),
        "bacdive_strains.tsv": [row for rows in fixture.strains.values() for row in rows],
        "culture_collection_strains.tsv": [], "mediadive_taxa.tsv": [], "gold_organisms.tsv": [],
        "madin_taxa.tsv": [], "bactotraits_taxa.tsv": [], "strain_related_records.tsv": [],
        "strain_assemblies.tsv": [ncbi], "strain_genome_records.tsv": [existing],
    }
    monkeypatch.setattr(seed, "read_tsv", lambda name: deepcopy(tables[name]))
    monkeypatch.setattr(seed, "ATB_DIR", _source(tmp_path))
    # This fixture isolates ATB behavior; StrainInfo's own overlay has dedicated tests.
    monkeypatch.setattr(seed.straininfo, "record_links", lambda directory: ({}, {}))
    inventory = seed.load_inventory()
    assert inventory.strain_assemblies[sid] == [ncbi]
    assert inventory.strain_genome_records[sid][0] == existing
    assert inventory.strain_genome_records[sid][1]["source_database"] == "allthebacteria"
    document = seed.build_document(seed.build_concepts(inventory, ["NCBITaxon:562"])[0], inventory)
    assert ("Seeded from data/raw/, data/atb/ and data/straininfo/ inventories"
            in document["curation_history"][0]["changes"])
    strain = document["strains"][0]
    assert list(strain).index("genome_assemblies") < list(strain).index("genome_records")
    assert strain["genome_assemblies"] == [{key: value for key, value in ncbi.items() if key != "strain_id"}]
    destination = tmp_path / "record.yaml"
    write_validated_taxon(document, destination)
    before = destination.read_bytes()
    write_validated_taxon(document, destination)
    assert destination.read_bytes() == before


@pytest.mark.parametrize("raw_stamp,atb_stamp,expected", [
    ("2026-09-10T15:00:00Z", "2026-09-12T01:00:00Z", "2026-09-12T01:00:00Z"),
    ("2026-09-13T15:00:00Z", "2026-09-12T01:00:00Z", "2026-09-13T15:00:00Z"),
    ("2026-09-12T02:00:00+02:00", "2026-09-12T01:00:00Z", "2026-09-12T01:00:00Z"),
    ("2026-09-10T15:00:00Z", None, "2026-09-10T15:00:00Z"),
    (None, None, "1970-01-01T00:00:00Z"),
])
def test_seed_timestamp_uses_newest_source_snapshot_deterministically(
    tmp_path, monkeypatch, raw_stamp, atb_stamp, expected,
):
    # No StrainInfo source participates in these raw/ATB-only timestamp scenarios.
    monkeypatch.setattr(seed, "STRAININFO_DIR", tmp_path / "unused-straininfo")
    for name, stamp in (("raw", raw_stamp), ("atb", atb_stamp)):
        directory = tmp_path / name
        directory.mkdir()
        monkeypatch.setattr(seed, name.upper() + "_DIR", directory)
        if stamp:
            (directory / "MANIFEST.yaml").write_text(yaml.safe_dump({"extracted_at": stamp}))
    assert seed._seed_timestamp() == expected
    assert seed._seed_timestamp() == expected
