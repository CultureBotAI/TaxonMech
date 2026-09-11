"""Prove the independent corpus guards reject corrupted seeded metadata."""

from copy import deepcopy

import pytest

from tests.test_corpus_integrity import (
    test_every_record_is_species_level_or_below as check_scope,
)
from tests.test_corpus_integrity import (
    test_lineage_is_a_single_chain_carried_from_ncbi as check_lineage,
)


@pytest.mark.parametrize("mutation", [
    "missing", "empty", "label", "rank", "skipped", "reordered", "parent", "duplicate_root",
])
def test_lineage_guard_rejects_corrupted_ancestry(records, repo_root, mutation):
    path, original = next((p, d) for p, d in records if d["identifier"] == "NCBITaxon:562")
    doc = deepcopy(original)
    if mutation == "missing":
        del doc["lineage"]
    elif mutation == "empty":
        doc["lineage"] = []
    elif mutation == "label":
        doc["lineage"][-1]["taxon_label"] = "incorrect genus"
    elif mutation == "rank":
        doc["lineage"][-1]["rank"] = "SPECIES"
    elif mutation == "skipped":
        del doc["lineage"][1]
    elif mutation == "reordered":
        doc["lineage"][1:3] = reversed(doc["lineage"][1:3])
    elif mutation == "parent":
        doc["parent_taxon"] = "NCBITaxon:1"
    elif mutation == "duplicate_root":
        doc["lineage"].insert(0, deepcopy(doc["lineage"][0]))
    with pytest.raises(AssertionError):
        check_lineage([(path, doc)], repo_root)


def test_scope_guard_rejects_a_genus_below_a_species(records):
    path, original = next((p, d) for p, d in records if d["identifier"] == "NCBITaxon:562")
    doc = deepcopy(original)
    doc["rank"] = "GENUS"
    doc["lineage"][-1]["rank"] = "SPECIES"
    with pytest.raises(AssertionError):
        check_scope([(path, doc)])
