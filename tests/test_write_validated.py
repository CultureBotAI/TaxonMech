"""The write gate, and the round-trip property that makes bulk edits reviewable."""

from __future__ import annotations

import pytest
import yaml

from taxonmech.validation.write_validated import (
    ValidationFailedError,
    emit_taxon_yaml,
    validate_taxon,
    write_validated_taxon,
)

MINIMAL = {
    "identifier": "NCBITaxon:562",
    "label": "Escherichia coli",
    "rank": "SPECIES",
    "taxon_domain": "BACTERIA",
    "grounding_status": "EXACT",
    "mapping_status": "SEEDED",
    "source_attestations": [
        {"source": "NCBITAXON", "source_id": "NCBITaxon:562", "source_label": "Escherichia coli",
         "assertion_count": 1, "assertion_unit": "NAME"},
    ],
}


def test_valid_record_passes():
    assert validate_taxon(MINIMAL) == []


def test_missing_required_field_is_rejected():
    doc = {k: v for k, v in MINIMAL.items() if k != "label"}
    assert validate_taxon(doc)


def test_unknown_field_is_rejected():
    """Closed-mode validation is the point of this helper."""
    assert validate_taxon(dict(MINIMAL, taxon_domian="BACTERIA"))


def test_bad_enum_value_is_rejected():
    assert validate_taxon(dict(MINIMAL, rank="SUPERKINGDOM"))
    assert validate_taxon(dict(MINIMAL, taxon_domain="PROTISTS"))


def test_bad_identifier_pattern_is_rejected():
    assert validate_taxon(dict(MINIMAL, identifier="not a curie"))


def test_strain_without_source_is_rejected():
    doc = dict(MINIMAL, strain_count=1, strains=[{"strain_id": "kgmicrobe.strain:bacdive_1"}])
    assert validate_taxon(doc)


def test_nomenclature_requires_name_and_id():
    doc = dict(MINIMAL, nomenclature=[{"source": "LPSN", "name": "Escherichia coli"}])
    assert validate_taxon(doc)


def test_causal_edge_without_evidence_is_rejected():
    """Mechanism claims are curator-asserted, so the schema requires edge-level evidence."""
    doc = dict(
        MINIMAL,
        causal_graphs=[{
            "graph_id": "g1",
            "nodes": [
                {"node_id": "a", "label": "Escherichia coli", "node_type": "TAXON"},
                {"node_id": "b", "label": "lactose fermentation", "node_type": "TRAIT"},
            ],
            "edges": [{"edge_id": "e1", "subject": "a", "predicate": "has trait", "object": "b"}],
        }],
    )
    assert validate_taxon(doc)


def test_causal_edge_with_evidence_is_valid():
    doc = dict(
        MINIMAL,
        causal_graphs=[{
            "graph_id": "g1",
            "nodes": [
                {"node_id": "a", "label": "Escherichia coli", "node_type": "TAXON"},
                {"node_id": "b", "label": "lactose fermentation", "node_type": "TRAIT"},
            ],
            "edges": [{"edge_id": "e1", "subject": "a", "predicate": "has trait", "object": "b",
                       "evidence": [{"reference": "PMID:12345678", "notes": "n"}]}],
        }],
    )
    assert validate_taxon(doc) == []


def test_curation_timestamp_year_guard():
    event = {"curator": "x", "action": "y"}
    doc = dict(MINIMAL, curation_history=[{"timestamp": "2206-01-01T00:00:00Z", **event}])
    assert validate_taxon(doc)
    doc = dict(MINIMAL, curation_history=[{"timestamp": "2026-01-01T00:00:00Z", **event}])
    assert validate_taxon(doc) == []


def test_invalid_record_is_not_written(tmp_path):
    path = tmp_path / "bad.yaml"
    with pytest.raises(ValidationFailedError):
        write_validated_taxon({"identifier": "NCBITaxon:1"}, path)
    assert not path.exists(), "an invalid record must not reach disk"


def test_valid_record_is_written(tmp_path):
    path = tmp_path / "nested" / "good.yaml"
    write_validated_taxon(dict(MINIMAL), path)
    assert path.exists()
    assert yaml.safe_load(path.read_text())["identifier"] == MINIMAL["identifier"]


def test_emit_is_stable_across_calls():
    assert emit_taxon_yaml(MINIMAL) == emit_taxon_yaml(MINIMAL)


def test_every_record_round_trips_byte_identically(records):
    """Re-emitting the corpus through the helper must change nothing."""
    drifted = []
    for path, doc in records:
        if emit_taxon_yaml(doc) != path.read_text(encoding="utf-8"):
            drifted.append(str(path))
    assert not drifted, (
        f"{len(drifted)} record(s) are not what emit_taxon_yaml would write, "
        f"e.g. {drifted[:5]}. Reformat them through the helper rather than loosening this test."
    )
