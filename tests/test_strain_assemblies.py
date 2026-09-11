"""Strain-to-assembly links need explicit evidence, never a species-level join."""

from __future__ import annotations

import json
from copy import deepcopy

import pytest

from taxonmech import extract, seed
from taxonmech.report import summarize
from taxonmech.validation.write_validated import validate_taxon
from tests.test_seed import _inventory


def _raw_record(bid, genomes):
    return {"General": {"BacDive-ID": bid}, "Sequence information": {"Genome sequences": genomes}}


def _extract(tmp_path, records, strain_ids=("kgmicrobe.strain:bacdive_5",)):
    path = tmp_path / "bacdive.json"
    path.write_text(json.dumps(records), encoding="utf-8")
    return extract.extract_bacdive_assemblies(path, set(strain_ids))


def _genome(accession="GCA_000005845.2", **kwargs):
    return {"accession": accession, "database": "ncbi", "@ref": 66792,
            "NCBI tax ID": 511145, "description": "Escherichia coli K-12 MG1655",
            "assembly level": "complete", **kwargs}


def test_extract_keeps_versions_and_distinct_assertions_without_pairing(tmp_path):
    genomes = [_genome(), _genome(), _genome("GCA_000005845"), _genome("GCA_000005845.3"),
               _genome(**{"@ref": 8})]
    rows, dropped = _extract(tmp_path, [_raw_record(5, genomes)])
    assert dropped == []
    assert len(rows) == 4  # Only the identical duplicate was removed.
    assert {r["assembly_id"] for r in rows} == {
        "ncbi.assembly:GCA_000005845", "ncbi.assembly:GCA_000005845.2", "ncbi.assembly:GCA_000005845.3",
    }
    assert {r["source_reference_id"] for r in rows} == {"8", "66792"}
    assert all(r["source_id"] == "bacdive:5" and r["taxon_id"] == "NCBITaxon:511145" for r in rows)
    assert all(r["assembly_name"] == genomes[0]["description"] for r in rows)
    assert _extract(tmp_path, [_raw_record(5, list(reversed(genomes)))])[0] == rows


def test_gene_chromosome_project_and_other_genome_ids_are_not_ncbi_assemblies(tmp_path):
    record = _raw_record(5, [_genome(a) for a in (
        "AB681728", "CP015081", "JHYL00000000", "SAMN12345678", "1122957.3", "2756170237",
    )])
    # A valid-looking accession in the wrong source section is not evidence.
    record["Sequence information"]["16S sequences"] = _genome()
    assert _extract(tmp_path, [record]) == ([], [])


def test_same_assembly_can_be_reported_for_several_strains(tmp_path):
    rows, dropped = _extract(tmp_path, [_raw_record(5, _genome()), _raw_record(10, _genome())],
                             ("kgmicrobe.strain:bacdive_5", "kgmicrobe.strain:bacdive_10"))
    assert len(rows) == 2 and not dropped
    assert len({r["assembly_id"] for r in rows}) == 1
    assert len({r["strain_id"] for r in rows}) == 2


def test_refseq_is_kept_only_when_explicitly_supplied(tmp_path):
    rows, dropped = _extract(tmp_path, [_raw_record(5, _genome("GCF_000005845.2"))])
    assert not dropped
    assert [r["assembly_id"] for r in rows] == ["ncbi.assembly:GCF_000005845.2"]


def test_unknown_strains_and_malformed_assemblies_are_auditable(tmp_path):
    rows, dropped = _extract(tmp_path, [_raw_record(99, _genome()),
                                      _raw_record(5, _genome("GCA_000005845.0"))])
    assert rows == []
    assert len(dropped) == 2
    assert {r["kind"] for r in dropped} == {"bacdive_assembly"}
    assert any("absent from bacdive_strains.tsv" in r["reason"] for r in dropped)
    assert any("malformed" in r["reason"] for r in dropped)


def test_assembly_without_source_record_identity_is_refused(tmp_path):
    with pytest.raises(ValueError, match="BacDive-ID"):
        _extract(tmp_path, [_raw_record(None, _genome())])


@pytest.mark.parametrize("payload", [
    {"error": "upstream response was not a strain array"},
    {}, None, "not a strain array", [None], ["not a record"],
    [{"Sequence information": []}],
    [{"Sequence information": {"Genome sequences": "not a genome entry"}}],
    [_raw_record(5, [None])],
])
def test_malformed_source_structure_cannot_silently_empty_the_inventory(tmp_path, payload):
    with pytest.raises(ValueError, match="BacDive"):
        _extract(tmp_path, payload)


def test_valid_empty_array_is_distinct_from_a_malformed_source(tmp_path):
    assert _extract(tmp_path, []) == ([], [])


def _document(tmp_path):
    inv = _inventory()
    rows, _ = _extract(tmp_path, [_raw_record(5, [_genome(), _genome("GCA_000005845.3")])])
    inv.strain_assemblies = {"kgmicrobe.strain:bacdive_5": rows}
    return seed.build_document(seed.build_concepts(inv, ["NCBITaxon:562"])[0], inv), inv


def test_seeding_attaches_only_to_the_asserted_strain_and_carries_taxon_disagreement(tmp_path):
    doc, inv = _document(tmp_path)
    assert validate_taxon(doc) == []
    strain = doc["strains"][0]
    assert strain["strain_id"] == "kgmicrobe.strain:bacdive_5"
    assert strain["classified_as"] == "NCBITaxon:83333"
    assert len(strain["genome_assemblies"]) == 2
    assert strain["genome_assemblies"][0]["taxon_id"] == "NCBITaxon:511145"
    # Another strain with the same species has no explicit genome assertion.
    assert "genome_assemblies" not in doc["strains"][1]
    # Neither the taxon identifier nor the LPSN marker sequence becomes an assembly xref.
    assert not any(x.startswith("ncbi.assembly:") for x in doc["xrefs"])
    assert "INSDC:AB681728" in doc["nomenclature"][0]["sequence_accessions"]
    # A record for the descendant taxon retains the same source assertion.
    child = seed.build_document(seed.build_concepts(inv, ["NCBITaxon:83333"])[0], inv)
    assert child["strains"][0]["genome_assemblies"] == strain["genome_assemblies"]


def test_listing_cap_does_not_modify_the_full_assembly_inventory(tmp_path, monkeypatch):
    doc, inv = _document(tmp_path)
    rows = deepcopy(inv.strain_assemblies)
    monkeypatch.setattr(seed, "STRAIN_LISTING_CAP", 0)
    capped = seed.build_document(seed.build_concepts(inv, ["NCBITaxon:562"])[0], inv)
    assert capped["strains"] == [] and capped["strain_count"] == doc["strain_count"]
    assert inv.strain_assemblies == rows


@pytest.mark.parametrize("accession", [
    "INSDC:AB681728", "ncbi.assembly:CP015081", "NCBITaxon:562",
    "ncbi.assembly:GCA_123", "ncbi.assembly:GCF_000005845.0", "ncbi.assembly:GCA_000005845.2oops",
])
def test_schema_rejects_identifiers_of_the_wrong_kind(tmp_path, accession):
    doc, _ = _document(tmp_path)
    doc["strains"][0]["genome_assemblies"][0]["assembly_id"] = accession
    assert validate_taxon(doc)


@pytest.mark.parametrize("field", ["source", "source_id", "assembly_id"])
def test_each_link_requires_its_evidence_and_target(tmp_path, field):
    doc, _ = _document(tmp_path)
    del doc["strains"][0]["genome_assemblies"][0][field]
    assert validate_taxon(doc)


def test_report_deduplicates_pairs_across_records_and_repeated_evidence(tmp_path):
    doc, _ = _document(tmp_path)
    doc["strains"][0]["genome_assemblies"].append(deepcopy(doc["strains"][0]["genome_assemblies"][0]))
    stats = summarize([(tmp_path / "a.yaml", doc), (tmp_path / "b.yaml", deepcopy(doc))])
    assert stats["listed_strains_with_assemblies"] == 1
    assert stats["listed_strain_assembly_links"] == 2
    assert stats["listed_assemblies"] == 2
