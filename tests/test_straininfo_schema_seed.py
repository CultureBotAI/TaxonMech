"""StrainInfo deposits remain distinct from strain identities and sequence records."""

from __future__ import annotations

import json
from copy import deepcopy

import pytest
import yaml
from jsonschema.validators import validator_for
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.generators.pydanticgen import PydanticGenerator
from pydantic import ValidationError

from taxonmech import seed
from taxonmech.validation.write_validated import (
    DEFAULT_SCHEMA_PATH,
    validate_taxon,
    write_validated_taxon,
)
from tests.test_seed import _inventory

STRAIN_ID = "kgmicrobe.strain:bacdive_5"


def _link(kind="assembly"):
    evidence = {
        "strain_id": "straininfo.strain:14277", "deposit_id": "straininfo.deposit:847459",
        "deposit_designation": "DSM 30083", "strain_status": "published online",
        "deposit_status": "available", "match_method": "culture_identifier",
        "strain_doi": "DOI:10.60712/SI-ID14277.3", "source_bacdive_id": "bacdive:5",
        "bacdive_reference_conflict": False,
    }
    link = {
        "strain_id": STRAIN_ID, "source": "STRAININFO", "source_id": "straininfo.strain:14277",
        "source_field": "strain.sequence.accessionNumber", "matched_strain_id": "kgmicrobe.strain:DSM-30083",
        "source_strain_identifiers": "DSM 30083", "source_strain_field": "deposits.designation",
        "straininfo_evidence": evidence,
    }
    if kind == "assembly":
        link["assembly_id"] = "ncbi.assembly:GCA_000690815"
        evidence.update(sequence_type="genome", sequence_deposit_id=evidence["deposit_id"])
    elif kind == "nucleotide":
        link.update(record_id="INSDC:X80725", record_type="NUCLEOTIDE_SEQUENCE", record_name="16S rRNA")
        evidence.update(sequence_type="rrnaop", sequence_deposit_id=evidence["deposit_id"])
    elif kind == "strain":
        link.update(record_id=evidence["strain_id"], record_type="STRAININFO_STRAIN",
                    source_field="strain.siID")
    elif kind == "deposit":
        link.update(record_id=evidence["deposit_id"], record_type="STRAININFO_DEPOSIT",
                    source_field="deposits.siDP", record_name=evidence["deposit_designation"])
    else:
        raise AssertionError(kind)
    return link


def _document(kind="assembly"):
    inventory = _inventory()
    field = "strain_assemblies" if kind == "assembly" else "strain_related_records"
    getattr(inventory, field)[STRAIN_ID] = [_link(kind)]
    concept = seed.build_concepts(inventory, ["NCBITaxon:562"])[0]
    return seed.build_document(concept, inventory)


def _assertion(document, kind="assembly"):
    return document["strains"][0]["genome_assemblies" if kind == "assembly" else "related_records"][0]


@pytest.fixture(scope="module", params=["write_time", "generated_json_schema"])
def errors(request):
    if request.param == "write_time":
        return validate_taxon
    schema = json.loads(JsonSchemaGenerator(str(DEFAULT_SCHEMA_PATH)).serialize())
    validator_class = validator_for(schema)
    validator_class.check_schema(schema)
    validator = validator_class(schema)
    return lambda document: list(validator.iter_errors(document))


@pytest.fixture(scope="module")
def pydantic_schema():
    # Compile from the authoritative YAML, independent of an ignored generated file.
    # LinkML conditionals are enforced by the JSON Schema/write-time checks above;
    # gen-pydantic currently retains them as metadata rather than validators.
    return PydanticGenerator(str(DEFAULT_SCHEMA_PATH)).compile_module()


@pytest.mark.parametrize("kind", ["assembly", "strain", "deposit", "nucleotide"])
def test_explicit_links_keep_source_and_deposit_evidence(errors, kind):
    document = _document(kind)
    assert not errors(document)
    link = _assertion(document, kind)
    assert link == {key: value for key, value in _link(kind).items() if key != "strain_id"}
    assert link["straininfo_evidence"]["bacdive_reference_conflict"] is False
    assert "genome_records" not in document["strains"][0]
    assert "genome_assemblies" not in document["strains"][1]


@pytest.mark.parametrize("accession", ["GCA_000690815", "GCA_000690815.1", "GCF_000005845.2"])
def test_ncbi_supplied_version_is_never_invented_or_removed(errors, accession):
    document = _document()
    _assertion(document)["assembly_id"] = f"ncbi.assembly:{accession}"
    assert not errors(document)
    assert _assertion(document)["assembly_id"].split(":", 1)[1] == accession


@pytest.mark.parametrize("kind", ["assembly", "strain", "deposit", "nucleotide"])
@pytest.mark.parametrize("value", [None, {}, []])
def test_straininfo_evidence_cannot_be_null_or_empty(errors, kind, value):
    document = _document(kind)
    _assertion(document, kind)["straininfo_evidence"] = value
    assert errors(document)


@pytest.mark.parametrize("kind", ["assembly", "strain", "deposit", "nucleotide"])
@pytest.mark.parametrize("field", [
    "source", "source_id", "straininfo_evidence", "matched_strain_id", "source_field",
    "source_strain_field", "source_strain_identifiers",
])
def test_source_and_match_fields_are_required(errors, kind, field):
    document = _document(kind)
    del _assertion(document, kind)[field]
    assert errors(document)


@pytest.mark.parametrize("field", [
    "strain_id", "deposit_id", "deposit_designation", "strain_status", "deposit_status", "match_method",
])
def test_nested_deposit_evidence_requires_every_identity_field(errors, field):
    document = _document()
    del _assertion(document)["straininfo_evidence"][field]
    assert errors(document)


@pytest.mark.parametrize("changes", [
    {"strain_id": "straininfo.deposit:14277"}, {"deposit_id": "straininfo.strain:847459"},
    {"strain_id": "straininfo.strain:0"}, {"deposit_id": "straininfo.deposit:01"},
    {"strain_doi": "DOI:10.60712/SI-DP847459.1"}, {"strain_doi": "DOI:10.60712/SI-ID14277"},
    {"source_bacdive_id": "NCBITaxon:5"}, {"deposit_designation": ""}, {"deposit_status": " "},
    {"strain_status": "erroneous"}, {"strain_status": "deposition"}, {"match_method": "strain_name"},
    {"sequence_type": "gene"}, {"sequence_type": None}, {"sequence_deposit_id": None},
    {"unexpected_field": "must not disappear"},
])
def test_assembly_evidence_rejects_mistyped_or_unpublished_records(errors, changes):
    document = _document()
    _assertion(document)["straininfo_evidence"].update(changes)
    assert errors(document)


@pytest.mark.parametrize("field", ["sequence_type", "sequence_deposit_id"])
@pytest.mark.parametrize("kind", ["assembly", "nucleotide"])
def test_sequence_assertions_require_their_own_source_deposit(errors, field, kind):
    document = _document(kind)
    del _assertion(document, kind)["straininfo_evidence"][field]
    assert errors(document)


@pytest.mark.parametrize("sequence_type", ["gene", "rrnaop", "patent"])
@pytest.mark.parametrize("accession", ["X80725", "GU134316.2", "NR_024570.1"])
def test_source_nucleotide_categories_and_accession_versions_remain_related_records(
    errors, sequence_type, accession,
):
    document = _document("nucleotide")
    link = _assertion(document, "nucleotide")
    link["record_id"] = f"INSDC:{accession}"
    link["straininfo_evidence"]["sequence_type"] = sequence_type
    assert not errors(document)
    assert "genome_assemblies" not in document["strains"][0]


@pytest.mark.parametrize("sequence_type", ["genome", None])
def test_genome_or_unspecified_sequence_categories_cannot_be_labeled_as_markers(errors, sequence_type):
    document = _document("nucleotide")
    _assertion(document, "nucleotide")["straininfo_evidence"]["sequence_type"] = sequence_type
    assert errors(document)


@pytest.mark.parametrize("kind,changes", [
    ("assembly", {"assembly_id": "INSDC:X80725"}),
    ("assembly", {"source_id": "straininfo.deposit:847459"}),
    ("assembly", {"source": "BACDIVE"}),
    ("assembly", {"matched_strain_id": None}),
    ("assembly", {"source_field": None}),
    ("assembly", {"source_strain_identifiers": None}),
    ("assembly", {"source_strain_field": "strain.relation.designation"}),
    ("strain", {"record_id": "straininfo.deposit:14277"}),
    ("deposit", {"record_id": "straininfo.strain:847459"}),
    ("deposit", {"record_type": "GOLD_ORGANISM"}),
    ("strain", {"source": "BACDIVE"}),
    ("strain", {"record_id": "biosample:SAMN1", "record_type": "BIOSAMPLE"}),
    ("nucleotide", {"record_id": "INSDC:GCA_000690815"}),
    ("nucleotide", {"record_id": "ncbi.assembly:GCA_000690815"}),
    ("nucleotide", {"record_id": "INSDC:X80725.0"}),
    ("nucleotide", {"record_type": "STRAININFO_STRAIN"}),
])
def test_entity_types_sources_and_assembly_namespaces_cannot_be_mixed(errors, kind, changes):
    document = _document(kind)
    _assertion(document, kind).update(changes)
    assert errors(document)


@pytest.mark.parametrize("kind", ["strain", "deposit"])
def test_strain_and_deposit_references_need_not_assert_a_sequence(errors, kind):
    document = _document(kind)
    evidence = _assertion(document, kind)["straininfo_evidence"]
    evidence.pop("strain_doi")
    evidence.pop("source_bacdive_id")
    evidence["strain_status"] = "published offline"
    evidence["deposit_status"] = "dead"
    assert "sequence_type" not in evidence
    assert not errors(document)


@pytest.mark.parametrize("kind", ["assembly", "strain", "deposit", "nucleotide"])
def test_pydantic_preserves_typed_nested_evidence(pydantic_schema, kind):
    document = _document(kind)
    loaded = pydantic_schema.TaxonRecord.model_validate(document).model_dump(exclude_none=True)
    assert (_assertion(loaded, kind)["straininfo_evidence"]
            == _assertion(document, kind)["straininfo_evidence"])


@pytest.mark.parametrize("changes", [
    {"unexpected_field": "closed"}, {"deposit_id": "straininfo.strain:1"},
    {"strain_status": "erroneous"}, {"match_method": "strain_name"},
])
def test_pydantic_structural_validation_is_closed(pydantic_schema, changes):
    document = _document()
    _assertion(document)["straininfo_evidence"].update(changes)
    with pytest.raises(ValidationError):
        pydantic_schema.TaxonRecord.model_validate(document)


def _mock_raw_inventory(monkeypatch):
    fixture = _inventory()
    original_ncbi = {"strain_id": STRAIN_ID, "assembly_id": "ncbi.assembly:GCF_000005845.2",
                     "source": "BACDIVE", "source_id": "bacdive:5"}
    original_genome = {"strain_id": STRAIN_ID, "genome_id": "patric:123.10", "source_database": "patric",
                       "source": "BACDIVE", "source_id": "bacdive:5"}
    original_related = {"strain_id": STRAIN_ID, "record_id": "biosample:SAMN1", "record_type": "BIOSAMPLE",
                        "source": "GTDB", "source_id": "gtdb.genome:RS_GCF_000005845.2"}
    tables = {
        "ncbitaxon_taxa.tsv": list(fixture.taxa.values()),
        "gtdb_mappings.tsv": [row for rows in fixture.gtdb.values() for row in rows],
        "lpsn_names.tsv": list(fixture.lpsn.values()),
        "bacdive_strains.tsv": [row for rows in fixture.strains.values() for row in rows],
        "culture_collection_strains.tsv": [], "mediadive_taxa.tsv": [], "gold_organisms.tsv": [],
        "madin_taxa.tsv": [], "bactotraits_taxa.tsv": [],
        "strain_assemblies.tsv": [original_ncbi], "strain_genome_records.tsv": [original_genome],
        "strain_related_records.tsv": [original_related],
    }
    monkeypatch.setattr(seed, "read_tsv", lambda name: deepcopy(tables[name]))
    monkeypatch.setattr(seed.atb, "genome_records", lambda directory: {})
    return original_ncbi, original_genome, original_related


def test_seed_appends_the_overlay_preserves_ncbi_priority_and_emits_identically(tmp_path, monkeypatch):
    ncbi, genome, related = _mock_raw_inventory(monkeypatch)
    overlay = ({STRAIN_ID: [_link()]}, {STRAIN_ID: [_link("strain"), _link("deposit"), _link("nucleotide")]})
    original_overlay = deepcopy(overlay)
    directory = tmp_path / "straininfo"
    monkeypatch.setattr(seed, "STRAININFO_DIR", directory)

    def record_links(path):
        assert path == directory
        return deepcopy(overlay)

    monkeypatch.setattr(seed.straininfo, "record_links", record_links)
    inventory = seed.load_inventory()
    assert inventory.strain_assemblies[STRAIN_ID] == [ncbi, _link()]
    assert inventory.strain_genome_records[STRAIN_ID] == [genome]
    assert inventory.strain_related_records[STRAIN_ID] == [related, *overlay[1][STRAIN_ID]]
    document = seed.build_document(seed.build_concepts(inventory, ["NCBITaxon:562"])[0], inventory)
    strain = document["strains"][0]
    assert list(strain).index("genome_assemblies") < list(strain).index("genome_records")
    assert "data/straininfo/ inventories" in document["curation_history"][0]["changes"]
    destination = tmp_path / "taxon.yaml"
    write_validated_taxon(document, destination)
    before = destination.read_bytes()
    write_validated_taxon(document, destination)
    assert destination.read_bytes() == before
    assert yaml.safe_load(before) == document
    assert overlay == original_overlay


def test_missing_or_invalid_source_overlay_cannot_silently_seed_a_partial_corpus(tmp_path, monkeypatch):
    _mock_raw_inventory(monkeypatch)
    monkeypatch.setattr(seed, "STRAININFO_DIR", tmp_path / "missing")

    def missing_manifest(directory):
        assert not (directory / "MANIFEST.yaml").exists()
        raise ValueError("StrainInfo manifest missing")

    monkeypatch.setattr(seed.straininfo, "record_links", missing_manifest)
    with pytest.raises(ValueError, match="StrainInfo manifest missing"):
        seed.load_inventory()


@pytest.mark.parametrize("raw_stamp,atb_stamp,straininfo_stamp,expected", [
    ("2026-09-10T15:00:00Z", "2026-09-12T01:00:00Z", "2026-09-13T02:00:00Z", "2026-09-13T02:00:00Z"),
    ("2026-09-14T15:00:00Z", "2026-09-12T01:00:00Z", "2026-09-13T02:00:00Z", "2026-09-14T15:00:00Z"),
    ("2026-09-10T15:00:00Z", "2026-09-14T01:00:00Z", "2026-09-13T02:00:00Z", "2026-09-14T01:00:00Z"),
    ("2026-09-10T15:00:00Z", "2026-09-12T01:00:00Z", "2026-09-12T04:00:00+02:00", "2026-09-12T02:00:00Z"),
])
def test_seed_timestamp_includes_all_source_snapshots(
    tmp_path, monkeypatch, raw_stamp, atb_stamp, straininfo_stamp, expected,
):
    for name, stamp in (("raw", raw_stamp), ("atb", atb_stamp), ("straininfo", straininfo_stamp)):
        directory = tmp_path / name
        directory.mkdir()
        monkeypatch.setattr(seed, name.upper() + "_DIR", directory)
        (directory / "MANIFEST.yaml").write_text(yaml.safe_dump({"extracted_at": stamp}))
    assert seed._seed_timestamp() == expected
    assert seed._seed_timestamp() == expected
