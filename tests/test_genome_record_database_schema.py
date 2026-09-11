"""Genome-database labels and identifiers must describe the same resource."""

from __future__ import annotations

import json

import pytest
from jsonschema.validators import validator_for
from linkml.generators.jsonschemagen import JsonSchemaGenerator

from taxonmech import seed
from taxonmech.validation.write_validated import DEFAULT_SCHEMA_PATH, validate_taxon
from tests.test_seed import _inventory


def _document(database="patric", identifier="patric:123.10"):
    inventory = _inventory()
    concept = seed.build_concepts(inventory, ["NCBITaxon:562"])[0]
    document = seed.build_document(concept, inventory)
    document["strains"][0]["genome_records"] = [{
        "genome_id": identifier,
        "source_database": database,
        "source": "BACDIVE",
        "source_id": "bacdive:5",
    }]
    return document


@pytest.fixture(scope="module", params=["write_time", "generated_json_schema"])
def validation_errors(request):
    if request.param == "write_time":
        return validate_taxon
    schema = json.loads(JsonSchemaGenerator(str(DEFAULT_SCHEMA_PATH)).serialize())
    validator_class = validator_for(schema)
    validator_class.check_schema(schema)
    validator = validator_class(schema)
    return lambda document: list(validator.iter_errors(document))


@pytest.mark.parametrize(("database", "identifier", "valid"), [
    ("patric", "patric:123.10", True),
    ("img", "img.taxon:2756170237", True),
    ("patric", "img.taxon:2756170237", False),
    ("img", "patric:123.10", False),
])
def test_database_label_matches_identifier_namespace(validation_errors, database, identifier, valid):
    errors = validation_errors(_document(database, identifier))
    assert (not errors) == valid


@pytest.mark.parametrize("field", ["genome_id", "source_database", "source", "source_id"])
def test_database_rules_keep_identity_and_provenance_required(validation_errors, field):
    document = _document()
    del document["strains"][0]["genome_records"][0][field]
    assert validation_errors(document)
