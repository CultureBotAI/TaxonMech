"""Independent source-to-page checks for genome identity and related records."""

from __future__ import annotations

import csv
import importlib
import json
from collections import defaultdict
from copy import deepcopy

import pytest
from jsonschema.validators import validator_for
from linkml.generators.jsonschemagen import JsonSchemaGenerator

from taxonmech import extract, seed
from taxonmech.genome_sources import extract_gtdb_strain_genomes, normalize_culture_identifier
from taxonmech.gold_genomes import extract_gold_genomes
from taxonmech.report import summarize
from taxonmech.validation.write_validated import DEFAULT_SCHEMA_PATH, validate_taxon, write_validated_taxon
from tests.test_genome_records import _StrainTableParser
from tests.test_gold_genomes import organism, workbook
from tests.test_seed import _inventory


def _gtdb_file(tmp_path, accession="RS_GCF_000005845.2", strain="DSM 30083;ATCC 11775", **extra):
    row = {
        "accession": accession, "ncbi_strain_identifiers": strain,
        "ncbi_genbank_assembly_accession": "GCA_000005845.2", "ncbi_taxid": "511145",
        "ncbi_assembly_level": "Complete Genome", "ncbi_assembly_name": "Source <assembly>",
        "ncbi_organism_name": "Source & organism", "ncbi_biosample": "SAMN02604091",
        "ncbi_bioproject": "PRJNA57779", **extra,
    }
    path = tmp_path / "gtdb.tsv"
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(row), delimiter="\t")
        writer.writeheader()
        writer.writerow(row)
    return path


@pytest.mark.parametrize("source", ["GTDB", "GOLD"])
@pytest.mark.parametrize("alias,deposits,accession,taxon,organism_name", [
    # Primary GTDB source: Pantoea sp. BR_17, taxid3055778. These deposits
    # belong to Azospirillum (BacDive13985) and Klebsiella (BacDive136200).
    ("BR_17", ["Br-17", "BR-17"], "RS_GCF_041955125.1", "3055778", "Pantoea sp. BR_17"),
    # Primary GTDB source: Escherichia coli Mu-3. These same bare names are
    # in BacDive138348 (Staphylococcus) and BacDive139900 (Anoxybacillus).
    ("Mu-3", ["Mu-3", "MU-3"], "RS_GCF_026797915.1", "562", "Escherichia coli"),
])
def test_unqualified_aliases_in_deposit_inventory_do_not_become_authority_ids(
    tmp_path, source, alias, deposits, accession, taxon, organism_name,
):
    strains = [{"strain_id": f"kgmicrobe.strain:bacdive_{index}",
                "culture_collection_ids": f"kgmicrobe.strain:{deposit}"}
               for index, deposit in enumerate(deposits, 1)]
    if source == "GTDB":
        path = _gtdb_file(tmp_path, accession, alias, ncbi_taxid=taxon, ncbi_organism_name=organism_name,
                          ncbi_genbank_assembly_accession=accession[3:].replace("GCF_", "GCA_"))
        result = extract_gtdb_strain_genomes([path], strains)
    else:
        result = extract_gold_genomes(workbook(tmp_path, organisms=[organism(culture=alias)]), strains)
    assert result[:3] == ([], [], [])


def test_authority_case_can_normalize_but_accession_case_and_alias_identity_cannot(tmp_path):
    assert normalize_culture_identifier("ccug : 123a") == "CCUG-123a"
    assert normalize_culture_identifier("CCUG 123A") == "CCUG-123A"
    # Unsupported suffixes remain inventoried, but cannot establish a new
    # cross-source identity until their authority template supports them.
    assert normalize_culture_identifier("ATCC 13706/60") == ""
    assert normalize_culture_identifier("CCAP 211/11A") == "CCAP-211/11A"
    assert normalize_culture_identifier("ACA-DC 001") == "ACA-DC-001"
    strains = [{"strain_id": "kgmicrobe.strain:bacdive_5", "culture_collection_ids":
                "kgmicrobe.strain:CCUG-123A|kgmicrobe.strain:IFO-123"}]
    for source_identifiers in ("CCUG 123a", "NBRC 123"):
        result = extract_gtdb_strain_genomes([_gtdb_file(tmp_path, strain=source_identifiers)], strains)
        assert result[:3] == ([], [], [])
    assemblies, genomes, _, drops = extract_gtdb_strain_genomes(
        [_gtdb_file(tmp_path, strain="ccug 123A")], strains,
    )
    assert assemblies and genomes and not drops


def _document(tmp_path):
    inventory = _inventory()
    strains = [strain for group in inventory.strains.values() for strain in group]
    gtdb = extract_gtdb_strain_genomes([_gtdb_file(tmp_path)], strains)
    gold = extract_gold_genomes(workbook(tmp_path, organisms=[organism(culture="DSM 30083")]), strains)
    assert not gtdb[3] and not gold[3]
    for attribute, fields, name, rows in (
        ("strain_assemblies", extract.ASSEMBLY_FIELDS, "assemblies.tsv", gtdb[0] + gold[0]),
        ("strain_genome_records", extract.GENOME_RECORD_FIELDS, "genomes.tsv", gtdb[1] + gold[1]),
        ("strain_related_records", extract.RELATED_RECORD_FIELDS, "related.tsv", gtdb[2] + gold[2]),
    ):
        # Exercise the committed inventory format before the seeder sees rows.
        path = tmp_path / name
        extract.write_tsv(path, fields, rows)
        grouped = defaultdict(list)
        for row in extract.read_tsv(path):
            grouped[row["strain_id"]].append(row)
        setattr(inventory, attribute, grouped)
    concept = seed.build_concepts(inventory, ["NCBITaxon:562"])[0]
    return seed.build_document(concept, inventory), inventory


def test_both_primary_sources_survive_inventory_seed_validation_and_pair_counts(tmp_path):
    document, inventory = _document(tmp_path)
    assert validate_taxon(document) == []
    write_validated_taxon(document, tmp_path / "record.yaml")
    first, other = document["strains"]
    assert first["strain_id"] == "kgmicrobe.strain:bacdive_5"
    assert first["classified_as"] == "NCBITaxon:83333"
    assert all(field not in other for field in ("genome_assemblies", "genome_records", "related_records"))
    assert {row["source"] for row in first["genome_records"]} == {"GTDB", "GOLD"}
    assert all(row["matched_strain_id"] in first["culture_collection_ids"]
               for field in ("genome_assemblies", "genome_records", "related_records")
               for row in first[field])
    assert any(row.get("source_organism_id") == "gold:Go1" and row.get("source_project_id") == "gold:Gp1"
               for row in first["genome_records"])
    assert not any(identifier.startswith(("gtdb.genome:", "gold:", "biosample:", "bioproject:"))
                   for identifier in document["xrefs"])
    child = seed.build_document(seed.build_concepts(inventory, ["NCBITaxon:83333"])[0], inventory)
    stats = summarize([(tmp_path / "species.yaml", document), (tmp_path / "strain.yaml", child)])
    assert stats["listed_strains_with_any_genome"] == 1
    assert stats["listed_genome_links_by_database"] == {
        "NCBI": {"strain_links": 3, "strains": 1, "identifiers": 3},
        "GTDB": {"strain_links": 1, "strains": 1, "identifiers": 1},
        "PATRIC": {"strain_links": 0, "strains": 0, "identifiers": 0},
        "IMG": {"strain_links": 1, "strains": 1, "identifiers": 1},
        "AllTheBacteria": {"strain_links": 0, "strains": 0, "identifiers": 0},
    }
    assert stats["listed_related_records_by_type"]["GOLD_ANALYSIS"]["identifiers"] == 1
    assert stats["listed_related_records_by_type"]["BIOSAMPLE"]["identifiers"] == 2
    related_only = deepcopy(document)
    for strain in related_only["strains"]:
        strain.pop("genome_assemblies", None)
        strain.pop("genome_records", None)
    assert summarize([(tmp_path / "related.yaml", related_only)])["listed_strains_with_any_genome"] == 0


@pytest.fixture(scope="module", params=["write_time", "generated_schema"])
def validate(request):
    if request.param == "write_time":
        return validate_taxon
    schema = json.loads(JsonSchemaGenerator(str(DEFAULT_SCHEMA_PATH)).serialize())
    return lambda document: list(validator_for(schema)(schema).iter_errors(document))


@pytest.mark.parametrize("record_type,record_id", [
    ("GOLD_ORGANISM", "gold:Go123"), ("GOLD_PROJECT", "gold:Gp123"),
    ("GOLD_ANALYSIS", "gold:Ga123"), ("BIOSAMPLE", "biosample:SAMN123"),
    ("BIOPROJECT", "bioproject:PRJNA123"),
])
def test_related_entity_types_are_enforced_in_both_schema_paths(tmp_path, validate, record_type, record_id):
    document, _ = _document(tmp_path)
    link = {"record_id": record_id, "record_type": record_type, "source": "GOLD", "source_id": "gold:Gp1"}
    document["strains"][0]["related_records"] = [link]
    assert not validate(document)
    link["record_type"] = "BIOSAMPLE" if record_type != "BIOSAMPLE" else "GOLD_ANALYSIS"
    assert validate(document)


@pytest.mark.parametrize("database", ["img", "patric", "gtdb"])
def test_gtdb_genome_namespace_matches_database_label(tmp_path, validate, database):
    document, _ = _document(tmp_path)
    link = next(row for row in document["strains"][0]["genome_records"] if row["source_database"] == "gtdb")
    link["source_database"] = database
    assert bool(validate(document)) == (database != "gtdb")


def test_pages_show_typed_urls_and_provenance_without_counting_related_as_genomes(
    tmp_path, repo_root, monkeypatch,
):
    monkeypatch.syspath_prepend(str(repo_root / "scripts"))
    renderer = importlib.import_module("render_pages")
    monkeypatch.setattr(renderer, "ATB_DIR", tmp_path / "no-atb-bundle")
    document, _ = _document(tmp_path)
    path = renderer.TAXA_DIR / "bacteria" / "genome-integration.yaml"
    monkeypatch.setattr(renderer, "load_records", lambda: [(path, document)])
    output = tmp_path / "site"
    renderer.render(output)
    html = (output / "taxa/bacteria/genome-integration.html").read_text()
    parsed = _StrainTableParser("kgmicrobe.strain:bacdive_5")
    parsed.feed(html)
    ncbi, genomes, related = parsed.cells[5:8]
    assert "https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000005845.2" in ncbi["hrefs"]
    assert "https://gtdb.ecogenomic.org/genome?gid=GCF_000005845.2" in genomes["hrefs"]
    assert "gtdb.genome:RS_GCF_000005845.2" in genomes["text"]
    assert "https://gold.jgi.doe.gov/organism?id=Go1" in related["hrefs"]
    assert "https://gold.jgi.doe.gov/project?id=Gp1" in related["hrefs"]
    assert "https://gold.jgi.doe.gov/analysis_project?id=Ga1" in related["hrefs"]
    assert "https://www.ncbi.nlm.nih.gov/biosample/SAMN02604091" in related["hrefs"]
    assert "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA57779" in related["hrefs"]
    assert "Matched deposit" in genomes["text"] and "Source relationship" in genomes["text"]
    assert "GOLD analysis project" in related["text"]
    assert "biosample:SAMN" not in ncbi["text"] + genomes["text"]
    assert "Source &lt;assembly&gt;" in html and "Source &amp; organism" in html
