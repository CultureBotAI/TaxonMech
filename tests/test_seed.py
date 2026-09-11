"""Unit tests for the seeder's pure helpers, on a tiny synthetic inventory."""

from __future__ import annotations

import pytest

from taxonmech import extract, seed
from taxonmech.validation.write_validated import validate_taxon


def _inventory() -> seed.Inventory:
    taxa = {
        "NCBITaxon:1": {"taxon_id": "NCBITaxon:1", "label": "root", "rank": "NO_RANK", "parent_id": "",
                        "genetic_code": "", "exact_synonyms": "", "related_synonyms": "all",
                        "broad_synonyms": "", "attested_by": ""},
        "NCBITaxon:2": {"taxon_id": "NCBITaxon:2", "label": "Bacteria", "rank": "DOMAIN",
                        "parent_id": "NCBITaxon:1", "genetic_code": "", "exact_synonyms": "",
                        "related_synonyms": "", "broad_synonyms": "", "attested_by": ""},
        "NCBITaxon:562": {"taxon_id": "NCBITaxon:562", "label": "Escherichia coli", "rank": "SPECIES",
                          "parent_id": "NCBITaxon:2", "genetic_code": "11", "exact_synonyms": "E. coli",
                          "related_synonyms": "Bacterium coli", "broad_synonyms": "",
                          "attested_by": "bacdive|lpsn|gold"},
        # A strain-level NCBI taxon below the species, where BacDive files the type strain.
        "NCBITaxon:83333": {"taxon_id": "NCBITaxon:83333", "label": "Escherichia coli K-12", "rank": "STRAIN",
                            "parent_id": "NCBITaxon:562", "genetic_code": "11", "exact_synonyms": "",
                            "related_synonyms": "", "broad_synonyms": "", "attested_by": "bacdive"},
    }
    gtdb = {"NCBITaxon:562": [
        # A pooled species with more genomes, listed first in the inventory: it
        # must NOT become the primary mapping.
        {"gtdb_id": "GTDB:s__Citrobacter_freundii", "gtdb_label": "s__Citrobacter_freundii",
         "gtdb_parent": "GTDB:g__Citrobacter", "ncbitaxon_id": "NCBITaxon:562",
         "predicate": "skos:broadMatch", "genome_count": "1691"},
        {"gtdb_id": "GTDB:s__Escherichia_coli", "gtdb_label": "s__Escherichia_coli",
         "gtdb_parent": "GTDB:g__Escherichia", "ncbitaxon_id": "NCBITaxon:562",
         "predicate": "skos:broadMatch", "genome_count": "42"},
    ]}
    lpsn = {"lpsn:776057": {"lpsn_id": "lpsn:776057", "name": "Escherichia coli", "rank": "SPECIES",
                            "authority": "(Migula 1895) Castellani and Chalmers 1919", "url": "https://lpsn.dsmz.de/species/escherichia-coli",
                            "deprecated": "0",
                            "status": "legitimate=True; validly published under the ICNP; correct name",
                            "validly_published": "1", "legitimate": "1", "is_correct_name": "1",
                            "parent_lpsn_id": "lpsn:515602", "ncbitaxon_ids": "NCBITaxon:562",
                            "gtdb_ids": "GTDB:s__Escherichia_coli",
                            "type_strain_ids": "kgmicrobe.strain:DSM-30083|kgmicrobe.strain:ATCC-11775",
                            # kg-microbe points same_as from the synonym to the correct name.
                            "synonym_of": "", "synonyms": "lpsn:4361",
                            "publications": "doi:10.1099/00207713-30-1-225",
                            "sequence_accessions": "INSDC:AB681728"},
            "lpsn:4361": {"lpsn_id": "lpsn:4361", "name": "Bacterium coli", "rank": "SPECIES",
                          "authority": "", "url": "", "deprecated": "1", "status": "",
                          "validly_published": "", "legitimate": "", "is_correct_name": "",
                          "parent_lpsn_id": "", "ncbitaxon_ids": "", "gtdb_ids": "", "type_strain_ids": "",
                          "synonym_of": "lpsn:776057", "synonyms": "", "publications": "",
                          "sequence_accessions": ""}}
    strains = {
        "NCBITaxon:562": [
            {"strain_id": "kgmicrobe.strain:bacdive_10", "bacdive_id": "10", "designation": "K-12",
             "taxon_ids": "NCBITaxon:562", "lpsn_ids": "", "culture_collection_ids": "kgmicrobe.strain:DSM-1",
             "medium_count": "2"},
        ],
        "NCBITaxon:83333": [
            {"strain_id": "kgmicrobe.strain:bacdive_5", "bacdive_id": "5", "designation": "",
             "taxon_ids": "NCBITaxon:83333", "lpsn_ids": "lpsn:776057",
             "culture_collection_ids": "kgmicrobe.strain:DSM-30083|kgmicrobe.strain:ATCC-11775",
             "medium_count": "0"},
        ],
    }
    return seed.Inventory(taxa, gtdb, lpsn, {"NCBITaxon:562": ["lpsn:776057"]}, strains,
                          {"NCBITaxon:562": ["kgmicrobe.strain:DSM-30083", "kgmicrobe.strain:CIP-99"]},
                          {}, {"NCBITaxon:562": 7}, {}, {})


def test_lineage_and_domain():
    inv = _inventory()
    assert inv.lineage("NCBITaxon:562") == ["NCBITaxon:1", "NCBITaxon:2"]
    assert inv.domain("NCBITaxon:562") == "BACTERIA"
    assert inv.domain("NCBITaxon:1") == "OTHER"


def test_build_document_is_valid_and_ordered():
    inv = _inventory()
    concept = seed.build_concepts(inv, ["NCBITaxon:562"])[0]
    doc = seed.build_document(concept, inv)
    assert validate_taxon(doc) == []
    assert doc["taxon_domain"] == "BACTERIA"
    assert doc["parent_taxon"] == "NCBITaxon:2"
    assert [a["taxon_id"] for a in doc["lineage"]] == ["NCBITaxon:1", "NCBITaxon:2"]
    # Type strain first, flagged from the LPSN designation.
    assert doc["strain_count"] == 2
    assert doc["strains"][0]["strain_id"] == "kgmicrobe.strain:bacdive_5"
    assert doc["strains"][0]["is_type_strain"] is True
    # Gathered from the strain-level taxon below the species, and says so.
    assert doc["strains"][0]["classified_as"] == "NCBITaxon:83333"
    assert "classified_as" not in doc["strains"][1]
    assert "is_type_strain" not in doc["strains"][1]
    assert doc["strains"][1]["medium_count"] == 2
    # Nomenclature carries the parsed booleans and the synonym label resolves.
    assert doc["nomenclature"][0]["is_correct_name"] is True
    assert doc["nomenclature"][0]["publications"] == ["DOI:10.1099/00207713-30-1-225"]
    assert {s["synonym_text"] for s in doc["synonyms"]} >= {"E. coli", "Bacterium coli"}
    lpsn_syn = [s for s in doc["synonyms"] if s["source"] == "LPSN"]
    assert lpsn_syn == [{"synonym_text": "Bacterium coli", "synonym_type": "RELATED_SYNONYM",
                         "source": "LPSN", "source_id": "lpsn:4361"}]
    assert "lpsn:776057" in doc["xrefs"]
    # The LPSN-linked GTDB species is the identity mapping: first, an xref,
    # a synonym, and the genome count the attestation reports. The pooled
    # species is kept but flagged, and is neither xref nor synonym.
    assert "GTDB:s__Escherichia_coli" in doc["xrefs"]
    assert "GTDB:s__Citrobacter_freundii" not in doc["xrefs"]
    assert [m["source_id"] for m in doc["taxonomy_mappings"]] == [
        "GTDB:s__Escherichia_coli", "GTDB:s__Citrobacter_freundii"]
    assert doc["taxonomy_mappings"][0]["genome_count"] == 42
    assert "LPSN links" in doc["taxonomy_mappings"][0]["notes"]
    assert "Pooled" in doc["taxonomy_mappings"][1]["notes"]
    assert {s["synonym_text"] for s in doc["synonyms"] if s["source"] == "GTDB"} == {"Escherichia coli"} - {
        "Escherichia coli"}  # the GTDB spelling equals the label, so no synonym is added
    gtdb = next(a for a in doc["source_attestations"] if a["source"] == "GTDB")
    assert gtdb["assertion_count"] == 42
    assert "1 further GTDB species pool" in gtdb["notes"]
    sources = [a["source"] for a in doc["source_attestations"]]
    assert sources == ["NCBITAXON", "LPSN", "GTDB", "BACDIVE", "GOLD"]
    bacdive = next(a for a in doc["source_attestations"] if a["source"] == "BACDIVE")
    assert bacdive["assertion_count"] == 2
    assert "1 strains are filed under 1 descendant" in bacdive["notes"]
    assert "1 further culture-collection deposit" in bacdive["notes"]
    assert doc["curation_history"][0]["action"] == "SEEDED_FROM_SOURCES"


def test_taxa_above_species_are_refused():
    """Repository rule: records are species and strains; a genus or domain in
    the scope is an error, not a record without strains."""
    inv = _inventory()
    inv.taxa["NCBITaxon:2"]["attested_by"] = "bacdive"
    with pytest.raises(SystemExit, match="above species level"):
        seed.build_concepts(inv, ["NCBITaxon:2"])


def test_strain_level_and_unranked_taxa_under_a_species_are_records():
    inv = _inventory()
    inv.taxa["NCBITaxon:1234"] = {"taxon_id": "NCBITaxon:1234", "label": "Escherichia coli O157",
                                  "rank": "NO_RANK", "parent_id": "NCBITaxon:562", "genetic_code": "11",
                                  "exact_synonyms": "", "related_synonyms": "", "broad_synonyms": "",
                                  "attested_by": "gold"}
    assert inv.is_species_or_below("NCBITaxon:83333")
    assert inv.is_species_or_below("NCBITaxon:1234")
    assert not inv.is_species_or_below("NCBITaxon:2")
    concepts = seed.build_concepts(inv, ["NCBITaxon:83333", "NCBITaxon:1234"])
    assert [c.rank for c in concepts] == ["STRAIN", "NO_RANK"]


@pytest.mark.parametrize("rank", ["GENUS", "FAMILY", "DOMAIN", "SPECIES_GROUP", "SPECIES_SUBGROUP"])
def test_species_ancestor_does_not_admit_a_higher_rank(rank):
    inv = _inventory()
    inv.taxa["NCBITaxon:83333"]["rank"] = rank
    assert not inv.is_species_or_below("NCBITaxon:83333")
    with pytest.raises(SystemExit, match="above species level"):
        seed.build_concepts(inv, ["NCBITaxon:83333"])


@pytest.mark.parametrize("rank", ["NO_RANK", "", "CLADE"])
def test_position_dependent_ranks_need_a_species_ancestor(rank):
    inv = _inventory()
    inv.taxa["NCBITaxon:83333"]["rank"] = rank
    assert inv.is_species_or_below("NCBITaxon:83333")
    inv.taxa["NCBITaxon:83333"]["parent_id"] = "NCBITaxon:2"
    assert not inv.is_species_or_below("NCBITaxon:83333")


def test_all_scope_and_proposals_exclude_higher_ranks_under_species(monkeypatch, capsys):
    from scripts import propose_scope

    inv = _inventory()
    inv.taxa["NCBITaxon:83333"]["rank"] = "GENUS"
    monkeypatch.setattr(seed, "load_inventory", lambda: inv)
    monkeypatch.setattr(seed, "load_scope", dict)
    monkeypatch.setattr(seed, "load_lockfile", dict)
    assert [c.identifier for c in seed.build_corpus(everything=True).concepts] == ["NCBITaxon:562"]

    monkeypatch.setattr(propose_scope, "load_inventory", lambda: inv)
    assert propose_scope.main(["--rule", "attested", "--rank", ""]) == 0
    proposed = capsys.readouterr().out.splitlines()
    assert [line.split("\t")[0] for line in proposed[1:]] == ["NCBITaxon:562"]


def test_build_document_is_deterministic():
    inv = _inventory()
    concept = seed.build_concepts(inv, ["NCBITaxon:562"])[0]
    assert seed.build_document(concept, inv) == seed.build_document(concept, inv)


def test_strain_listing_is_capped():
    inv = _inventory()
    many = [dict(inv.strains["NCBITaxon:562"][0], strain_id=f"kgmicrobe.strain:bacdive_{i}",
                 bacdive_id=str(i), culture_collection_ids="")
            for i in range(100, 100 + seed.STRAIN_LISTING_CAP + 5)]
    inv.strains["NCBITaxon:562"] = inv.strains["NCBITaxon:562"] + many
    concept = seed.build_concepts(inv, ["NCBITaxon:562"])[0]
    doc = seed.build_document(concept, inv)
    assert doc["strain_count"] == seed.STRAIN_LISTING_CAP + 7
    assert len(doc["strains"]) == seed.STRAIN_LISTING_CAP
    assert doc["strains"][0]["is_type_strain"] is True


def test_unknown_scope_identifier_is_refused():
    inv = _inventory()
    with pytest.raises(SystemExit, match="not in data/raw"):
        seed.build_concepts(inv, ["NCBITaxon:999999"])


def test_assign_paths_pins_and_disambiguates():
    inv = _inventory()
    a = seed.Concept("NCBITaxon:562", "Escherichia coli", "SPECIES", "BACTERIA", inv.taxa["NCBITaxon:562"])
    b = seed.Concept("NCBITaxon:9999", "Escherichia coli", "SPECIES", "OTHER", inv.taxa["NCBITaxon:562"])
    paths, assignments = seed.assign_paths([a, b], {"NCBITaxon:9999": "pinned_name"})
    assert assignments["NCBITaxon:9999"] == "pinned_name"
    assert assignments["NCBITaxon:562"] == "escherichia_coli"
    assert paths["NCBITaxon:562"].parent.name == "bacteria"
    paths, assignments = seed.assign_paths([a, b], {})
    assert assignments["NCBITaxon:562"] == "escherichia_coli"
    assert assignments["NCBITaxon:9999"].startswith("escherichia_coli__")


def test_id_key_tolerates_minted_identifiers():
    ids = ["NCBITaxon:562", "taxonmech:candidatus_x", "NCBITaxon:54", "taxonmech:a"]
    assert sorted(ids, key=seed.id_key) == ["NCBITaxon:54", "NCBITaxon:562", "taxonmech:a",
                                            "taxonmech:candidatus_x"]


def test_slugify_is_filesystem_safe():
    assert seed.slugify("Escherichia coli O157:H7 str. Sakai") == "escherichia_coli_o157_h7_str_sakai"
    assert seed.SLUG_PATTERN.match(seed.slugify("Candidatus Pelagibacter ubique"))


@pytest.mark.parametrize("value,expected", [
    ("NCBITaxon:species", "SPECIES"),
    ("obo:NCBITaxon#_species_group", "SPECIES_GROUP"),
    ("NCBITaxon:forma_specialis", "FORMA_SPECIALIS"),
])
def test_rank_enum_from_semsql_value(value, expected):
    assert extract._rank_enum(value) == expected


@pytest.mark.parametrize("name,designation", [
    ("bacdive_100253 as STI43638(IMET) of NCBITaxon:562", "STI43638(IMET)"),
    ("bacdive_10 strain of NCBITaxon:104097", ""),
    ("bacdive_167799 as UdG 6026 (proposed neotype strain) of NCBITaxon:157109",
     "UdG 6026 (proposed neotype strain)"),
])
def test_strain_designation_parsing(name, designation):
    m = extract._STRAIN_NAME.match(name)
    assert m, name
    assert (m.group("designation") or "") == designation
