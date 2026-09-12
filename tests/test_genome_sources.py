"""GTDB relationships require a complete, explicit culture-identifier match."""

from __future__ import annotations

import csv
import gzip
import json
from copy import deepcopy

import pytest

from taxonmech import genome_sources
from taxonmech.genome_sources import (
    GTDB_METADATA_FIELDS,
    extract_gtdb_strain_genomes,
    index_culture_identifiers,
    normalize_culture_identifier,
)
from taxonmech.gold_genomes import extract_gold_genomes
from tests.test_gold_genomes import organism, workbook

SID = "kgmicrobe.strain:bacdive_5"
OTHER_SID = "kgmicrobe.strain:bacdive_10"
DEPOSIT = "kgmicrobe.strain:DSM-123"


def _strain(strain_id=SID, deposits=DEPOSIT):
    return {"strain_id": strain_id, "culture_collection_ids": deposits,
            "designation": "DSM 123", "taxon_ids": "NCBITaxon:562"}


def _metadata(**overrides):
    return {
        "accession": "RS_GCF_000005845.1", "ncbi_genbank_assembly_accession": "GCA_000005845.2",
        "ncbi_strain_identifiers": "DSM 123", "ncbi_taxid": "511145",
        "ncbi_assembly_level": "Complete Genome", "ncbi_assembly_name": "ASM584v2",
        "ncbi_organism_name": "Escherichia coli K-12 MG1655", "ncbi_biosample": "SAMN02604091",
        "ncbi_bioproject": "PRJNA57779", **overrides,
    }


def _write(path, rows, fields=GTDB_METADATA_FIELDS):
    opener = gzip.open if path.suffix == ".gz" else type(path).open
    with opener(path, "wt", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    return path


def _extract(tmp_path, rows, strains=None, filename="metadata.tsv.gz"):
    path = _write(tmp_path / filename, rows)
    return extract_gtdb_strain_genomes([path], [_strain()] if strains is None else strains)


def test_primary_genbank_gtdb_and_related_ids_keep_their_evidence_and_versions(tmp_path):
    assemblies, genomes, related, drops = _extract(tmp_path, [_metadata()])
    assert not drops
    assert {row["assembly_id"] for row in assemblies} == {
        "ncbi.assembly:GCF_000005845.1", "ncbi.assembly:GCA_000005845.2",
    }
    assert {row["source_field"] for row in assemblies} == {"accession", "ncbi_genbank_assembly_accession"}
    assert len(genomes) == 1
    assert genomes[0]["genome_id"] == "gtdb.genome:RS_GCF_000005845.1"
    assert genomes[0]["source_database"] == "gtdb"
    assert {(row["record_id"], row["record_type"], row["source_field"]) for row in related} == {
        ("biosample:SAMN02604091", "BIOSAMPLE", "ncbi_biosample"),
        ("bioproject:PRJNA57779", "BIOPROJECT", "ncbi_bioproject"),
    }
    for row in assemblies + genomes + related:
        assert row["strain_id"] == SID
        assert row["source"] == "GTDB"
        assert row["source_id"] == "gtdb.genome:RS_GCF_000005845.1"
        assert row["matched_strain_id"] == DEPOSIT
        assert row["source_strain_identifiers"] == "DSM 123"
        assert row["source_strain_field"] == "ncbi_strain_identifiers"
        assert row["taxon_id"] == "NCBITaxon:511145"
    assert assemblies[0]["assembly_name"] == "ASM584v2"
    assert genomes[0]["genome_name"] == "Escherichia coli K-12 MG1655"


def test_genbank_is_not_invented_when_source_omits_it(tmp_path):
    assemblies, _, related, drops = _extract(tmp_path, [_metadata(
        ncbi_genbank_assembly_accession="none", ncbi_biosample="NA", ncbi_bioproject="",
    )])
    assert not drops and not related
    assert [row["assembly_id"] for row in assemblies] == ["ncbi.assembly:GCF_000005845.1"]


def test_genbank_versions_remain_unspecified_when_the_source_omits_the_suffix(tmp_path):
    assemblies, _, _, drops = _extract(tmp_path, [_metadata(ncbi_genbank_assembly_accession="GCA_000005845")])
    assert not drops
    assert "ncbi.assembly:GCA_000005845" in {row["assembly_id"] for row in assemblies}


def test_same_accession_in_two_source_fields_retains_both_assertions(tmp_path):
    assemblies, genomes, _, drops = _extract(tmp_path, [_metadata(
        accession="GB_GCA_000005845.2", ncbi_genbank_assembly_accession="GCA_000005845.2",
    )])
    assert not drops and len(genomes) == 1
    assert len(assemblies) == 2
    assert {row["assembly_id"] for row in assemblies} == {"ncbi.assembly:GCA_000005845.2"}
    assert {row["source_field"] for row in assemblies} == {"accession", "ncbi_genbank_assembly_accession"}


def test_whole_semicolon_tokens_match_case_and_collection_separator_variants(tmp_path):
    raw = " unknown; dsm : 123 ;ATCC BAA-1556; DSM 123 "
    strains = [_strain(deposits=DEPOSIT + "|kgmicrobe.strain:ATCC-BAA-1556")]
    assemblies, genomes, _, drops = _extract(tmp_path, [_metadata(ncbi_strain_identifiers=raw)], strains)
    assert not drops and len(assemblies) == 4 and len(genomes) == 2
    assert {row["matched_strain_id"] for row in genomes} == {DEPOSIT, "kgmicrobe.strain:ATCC-BAA-1556"}
    assert all(row["source_strain_identifiers"] == raw for row in genomes)


@pytest.mark.parametrize("raw", [
    "DSM123", "strain DSM 123", "DSM 1234", "DSM 00123", "DSM 123T", "DSM 12-3",
    "DSM 123, ATCC 555", "DSM 123=ATCC 555", "DSM 123 extra", "123", "ATCC 123",
])
def test_partial_names_suffixes_leading_zeros_and_other_collections_never_match(tmp_path, raw):
    assert _extract(tmp_path, [_metadata(ncbi_strain_identifiers=raw)]) == ([], [], [], [])


def test_shared_deposits_preserve_every_asserted_strain_without_species_propagation(tmp_path):
    strains = [_strain(), _strain(OTHER_SID), _strain("kgmicrobe.strain:bacdive_15", "")]
    assemblies, genomes, _, drops = _extract(tmp_path, [_metadata()], strains)
    assert not drops and len(assemblies) == 4 and len(genomes) == 2
    assert {row["strain_id"] for row in genomes} == {SID, OTHER_SID}
    assert {row["genome_id"] for row in genomes} == {"gtdb.genome:RS_GCF_000005845.1"}


def test_taxonomy_designation_and_isolate_fields_are_never_join_keys(tmp_path):
    row = _metadata(ncbi_strain_identifiers="none", ncbi_taxid="562", ncbi_isolate="DSM 123")
    path = _write(tmp_path / "metadata.tsv", [row], (*GTDB_METADATA_FIELDS, "ncbi_isolate"))
    assert extract_gtdb_strain_genomes([path], [_strain()]) == ([], [], [], [])


def test_only_identical_assertions_are_deduplicated_across_files(tmp_path):
    a = _metadata()
    b = _metadata(ncbi_assembly_name="Alternative assembly name", ncbi_organism_name="Alternative name")
    first = _write(tmp_path / "bacteria.tsv.gz", [a, deepcopy(a), b])
    second = _write(tmp_path / "archaea.tsv", [b, a])
    result = extract_gtdb_strain_genomes([first, second], [_strain()])
    assemblies, genomes, related, drops = result
    assert len(assemblies) == 4 and len(genomes) == 2 and len(related) == 2 and not drops
    assert extract_gtdb_strain_genomes([second, first], [_strain()]) == result


@pytest.mark.parametrize("accession", [
    "GCF_000005845.1", "RS_GCA_000005845.1", "GB_GCF_000005845.1",
    "RS_GCF_000005845", "RS_GCF_000005845.0", "RS_GCF_000005845.1extra", "none",
])
def test_malformed_primary_identifiers_are_auditable_and_do_not_retype(tmp_path, accession):
    assemblies, genomes, related, drops = _extract(tmp_path, [_metadata(accession=accession)])
    assert assemblies == genomes == related == []
    assert len(drops) == 1 and drops[0]["kind"] == "gtdb_genome_record"


def test_malformed_optional_targets_do_not_suppress_valid_primary_assertions(tmp_path):
    assemblies, genomes, related, drops = _extract(tmp_path, [_metadata(
        ncbi_genbank_assembly_accession="GCF_000005845.2", ncbi_biosample="SAMN123.4",
        ncbi_bioproject="PRJXX123",
    )])
    assert len(assemblies) == len(genomes) == 1 and related == []
    assert len(drops) == 3
    assert {row["kind"] for row in drops} == {"gtdb_assembly", "gtdb_related_record"}


def test_malformed_source_taxonomy_cannot_silently_be_attached_to_a_link(tmp_path):
    assemblies, genomes, related, drops = _extract(tmp_path, [_metadata(ncbi_taxid="562|83333")])
    assert assemblies == genomes == related == []
    assert len(drops) == 1 and "taxon" in drops[0]["reason"]


@pytest.mark.parametrize(("biosample", "bioproject"), [
    ("SAMN02604091", "PRJNA57779"), ("SAMD00008943", "PRJDB643"),
    ("SAMEA1123456", "PRJEB12345"), ("SAMEA1123456", "PRJEA12345"),
    ("SAMD00008943", "PRJDA12345"),
])
def test_insdc_partner_and_legacy_related_accessions_remain_separate_entities(
    tmp_path, biosample, bioproject,
):
    row = _metadata(ncbi_biosample=biosample, ncbi_bioproject=bioproject)
    _, _, related, drops = _extract(tmp_path, [row])
    assert not drops
    assert {row["record_id"] for row in related} == {"biosample:" + biosample, "bioproject:" + bioproject}


def test_empty_table_is_valid_but_incomplete_or_duplicate_headers_fail_closed(tmp_path):
    assert _extract(tmp_path, []) == ([], [], [], [])
    contents = ("", "accession\tncbi_strain_identifiers\n", "\t".join((*GTDB_METADATA_FIELDS, "accession")))
    for content in contents:
        path = tmp_path / "bad.tsv"
        path.write_text(content)
        with pytest.raises(ValueError, match="GTDB metadata.*headers"):
            extract_gtdb_strain_genomes([path], [_strain()])


def test_structurally_truncated_rows_fail_even_without_an_inventory_match(tmp_path):
    path = tmp_path / "bad.tsv"
    path.write_text("\t".join(GTDB_METADATA_FIELDS) + "\nRS_GCF_000005845.1\n")
    with pytest.raises(ValueError, match="malformed TSV row"):
        extract_gtdb_strain_genomes([path], [])


def test_culture_index_preserves_original_curie_and_rejects_invalid_deposits():
    assert normalize_culture_identifier(" ATCC BAA-01556 ") == "ATCC-BAA-01556"
    assert index_culture_identifiers([_strain(), _strain(OTHER_SID)]) == {
        "DSM-123": {(SID, DEPOSIT), (OTHER_SID, DEPOSIT)},
    }
    for bad in ("DSM-123", "kgmicrobe.strain:"):
        with pytest.raises(ValueError, match="culture-collection CURIE"):
            index_culture_identifiers([_strain(deposits=bad)])


@pytest.mark.parametrize("raw,expected", [
    ("as 1.2", "AS-1.2"), ("AS 01.2", "AS-01.2"),
    ("ATCC BAA-01556", "ATCC-BAA-01556"),
    ("CCAP 211/11A", "CCAP-211/11A"),
    ("ccug 123a", "CCUG-123a"), ("CCUG 123A", "CCUG-123A"),
    ("LMG 123t4", "LMG-123t4"), ("VKM Ac-123", "VKM-Ac-123"),
    ("HAMBI:FBCC 123", "HAMBI:FBCC-123"),
    ("AS-8", ""), ("As-7", ""), ("AS_2", ""),
    ("CT 123", ""), ("DSM 123A", ""), ("ATCC 13706/60", ""),
    ("LMG 123T4", ""), ("VKM AC-123", ""),
])
def test_registered_authorities_require_their_case_sensitive_accession_template(raw, expected):
    assert normalize_culture_identifier(raw) == expected


@pytest.mark.parametrize("source", ["GTDB", "GOLD"])
@pytest.mark.parametrize("alias,accession,taxon,source_name,strain_id", [
    # These whole aliases collide with the historical AS collection prefix,
    # whose real accession format is numeric.numeric, never a bare integer.
    ("AS-8", "RS_GCF_003045665.1", "1590", "Lactiplantibacillus plantarum",
     "kgmicrobe.strain:bacdive_132548"),  # Fictibacillus halophilus
    ("AS-7", "RS_GCF_003045685.1", "60520", "Lactiplantibacillus paraplantarum",
     "kgmicrobe.strain:bacdive_158762"),  # Paenibacillus xanthanilyticus
    ("AS_2", "RS_GCF_026891895.1", "2996755", "Peribacillus sp. AS_2",
     "kgmicrobe.strain:bacdive_5334"),  # Enterococcus asini
])
def test_registered_prefix_lab_aliases_cannot_create_real_cross_genus_links(
    tmp_path, source, alias, accession, taxon, source_name, strain_id,
):
    strains = [_strain(strain_id, "kgmicrobe.strain:" + alias.replace("_", "-"))]
    if source == "GTDB":
        row = _metadata(accession=accession, ncbi_strain_identifiers=alias,
                        ncbi_taxid=taxon, ncbi_organism_name=source_name)
        result = _extract(tmp_path, [row], strains)
    else:
        result = extract_gold_genomes(workbook(tmp_path, organisms=[organism(culture=alias)]), strains)
    assert result == ([], [], [], [])


def test_valid_as_accession_matches_without_erasing_zeros_or_rewriting_historical_authority(tmp_path):
    strains = [_strain(deposits="kgmicrobe.strain:AS-01.2")]
    for token in ("AS 1.2", "CGMCC 01.2"):
        assert _extract(tmp_path, [_metadata(ncbi_strain_identifiers=token)], strains) == ([], [], [], [])
    assemblies, genomes, _, drops = _extract(
        tmp_path, [_metadata(ncbi_strain_identifiers="as 01.2")], strains,
    )
    assert assemblies and len(genomes) == 1 and not drops
    assert genomes[0]["matched_strain_id"] == "kgmicrobe.strain:AS-01.2"


@pytest.mark.parametrize("registry,reason", [
    ({"1": {"acr": "DSM"}}, "missing accession template"),
    ({"1": {"acr": "DSM", "regex_id": {"full": "["}}}, "invalid accession template"),
    ({"1": {"acr": "DSM", "regex_id": {"full": "[0-9]+"}},
      "2": {"acr": "DSM", "regex_id": {"full": "[A-Z]+"}}}, "conflicting accession templates"),
])
def test_invalid_registry_templates_fail_closed(tmp_path, monkeypatch, registry, reason):
    path = tmp_path / "registry.json"
    path.write_text(json.dumps(registry))
    monkeypatch.setattr(genome_sources, "CAFI_REGISTRY_PATH", path)
    genome_sources._culture_identifier_patterns.cache_clear()
    try:
        with pytest.raises(ValueError, match=reason):
            normalize_culture_identifier("DSM 123")
    finally:
        genome_sources._culture_identifier_patterns.cache_clear()
