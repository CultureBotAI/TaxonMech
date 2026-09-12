"""Matching evidence must preserve the culture identifier's original syntax."""

from copy import deepcopy

import pytest

from taxonmech import seed
from taxonmech.validation.write_validated import validate_taxon
from tests.test_seed import _inventory

TARGETS = [
    ("genome_assemblies", {"assembly_id": "ncbi.assembly:GCA_000376245.1"}),
    ("genome_records", {"genome_id": "img.taxon:2517572146", "source_database": "img"}),
    ("related_records", {"record_id": "biosample:SAMN00002661", "record_type": "BIOSAMPLE"}),
]


def _document():
    inv = _inventory()
    return seed.build_document(seed.build_concepts(inv, ["NCBITaxon:562"])[0], inv)


@pytest.mark.parametrize("deposit", [
    "kgmicrobe.strain:ATCC-13706/60",
    "kgmicrobe.strain:BGSC-1A459/SU+III",
    "kgmicrobe.strain:ATCC-BAA–1538",
])
@pytest.mark.parametrize("field,target", TARGETS)
def test_existing_deposit_suffixes_remain_valid_when_attached_as_link_evidence(deposit, field, target):
    doc = _document()
    strain = doc["strains"][0]
    strain["culture_collection_ids"] = [deposit]
    assert validate_taxon(doc) == []
    strain[field] = [{
        **deepcopy(target), "source": "GOLD", "source_id": "gold:Ga1",
        "matched_strain_id": deposit, "source_organism_id": "gold:Go1", "source_project_id": "gold:Gp1",
        "source_strain_field": "ORGANISM CULTURE COLLECTION ID",
        "source_strain_identifiers": deposit.split(":", 1)[1],
    }]
    assert validate_taxon(doc) == []


@pytest.mark.parametrize("deposit", [
    "kgmicrobe.strain:", "kgmicrobe.strain:ATCC 13706/60", "ATCC:13706/60", "NCBITaxon:562",
])
def test_evidence_rejects_empty_whitespace_or_unrelated_identifiers(deposit):
    doc = _document()
    doc["strains"][0]["genome_assemblies"] = [{
        "assembly_id": "ncbi.assembly:GCA_000376245.1", "source": "GOLD", "source_id": "gold:Ga1",
        "matched_strain_id": deposit,
    }]
    assert validate_taxon(doc)
