"""StrainInfo source groupings must never transfer sequence links across deposits."""

import copy

import pytest

from taxonmech.straininfo_links import RELATED_COLUMNS, build_links, candidate_ids, project_record


def source_record():
    # Mirrors the mixed SI-ID 252 source counterexample: Acinetobacter deposits
    # coexist with a Campylobacter deposit and an aggregate Campylobacter bdID.
    deposits = [
        {"siDP": 1, "designation": "ATCC 19004", "status": "available",
         "cultureCollection": {"ccID": 4, "deprecated": False}, "taxon": {"ncbi": 1311774}},
        {"siDP": 2, "designation": "DSM 25618", "status": "available",
         "cultureCollection": {"ccID": 1, "deprecated": False}, "taxon": {"ncbi": 1311774}},
        {"siDP": 3, "designation": "LMG 6440", "status": "available",
         "cultureCollection": {"ccID": 2, "deprecated": False}, "taxon": {"ncbi": 195}},
    ]
    return {"strain": {"siID": 252, "doi": "10.60712/SI-ID252.1", "status": "published online",
                       "bdID": 2103, "taxon": {"ncbi": 195}, "alternative": [123], "merged": [321],
                       "relation": {"deposit": [
                           {"siDP": d["siDP"], "designation": d["designation"],
                            "ccID": d["cultureCollection"]["ccID"], "erroneous": False} for d in deposits]},
                       "sequence": [
                           {"accessionNumber": "GCA_000369045", "type": "genome", "assemblyLevel": "scaffold",
                            "deposit": [{"siDP": 1, "designation": "ATCC 19004"}]},
                           {"accessionNumber": "GCA_003590975", "type": "genome",
                            "deposit": [{"siDP": 3, "designation": "LMG 6440"}]},
                           {"accessionNumber": "AB123456.2", "type": "rrnaop",
                            "deposit": [{"siDP": 2, "designation": "DSM 25618"}]},
                       ]}, "deposits": deposits}


def strain_inventory():
    return [
        {"strain_id": "kgmicrobe.strain:bacdive_8146", "bacdive_id": "8146",
         "culture_collection_ids": "kgmicrobe.strain:ATCC-19004|kgmicrobe.strain:DSM-25618"},
        {"strain_id": "kgmicrobe.strain:bacdive_2103", "bacdive_id": "2103",
         "culture_collection_ids": "kgmicrobe.strain:DSM-4689"},
    ]


def test_mixed_source_group_preserves_own_deposit_paths_and_conflicting_metadata():
    import json

    source = source_record()
    before = copy.deepcopy(source)
    links, assemblies, related, excluded = build_links([project_record(source)], strain_inventory())
    assert source == before
    assert len(links) == 2
    assert {r["strain_id"] for r in links} == {"kgmicrobe.strain:bacdive_8146"}
    assert [r["assembly_id"] for r in assemblies] == ["ncbi.assembly:GCA_000369045"]
    assert assemblies[0]["taxon_id"] == "NCBITaxon:1311774"
    assert assemblies[0]["matched_strain_id"] == "kgmicrobe.strain:ATCC-19004"
    evidence = json.loads(assemblies[0]["straininfo_evidence_json"])
    assert evidence["source_bacdive_id"] == "bacdive:2103"
    assert evidence["bacdive_reference_conflict"] is True
    assert evidence["sequence_deposit_id"] == evidence["deposit_id"] == "straininfo.deposit:1"
    nucleotide = {r["record_id"] for r in related if r["record_type"] == "NUCLEOTIDE_SEQUENCE"}
    assert nucleotide == {"INSDC:AB123456.2"}
    assert {r["reason"] for r in excluded} == {"conflicting_bacdive_reference_not_used"}
    assert project_record(source)["strain"]["merged"] == [321]
    assert project_record(source)["strain"]["alternative"] == [123]


def test_search_is_only_a_candidate_list_and_aliases_do_not_supply_deposit_links():
    rows = [[252, ["DSM 25618"], "ignored taxon", True, "", 1],
            [99, ["U5/41"], "ignored taxon", True, "", 1]]
    assert candidate_ids(rows, strain_inventory()) == [252]
    source = source_record()
    source["deposits"] = source["deposits"][2:]
    source["strain"]["relation"]["deposit"] = source["strain"]["relation"]["deposit"][2:]
    source["strain"]["relation"]["designation"] = ["ATCC 19004", "DSM 25618"]
    source["strain"]["sequence"] = source["strain"]["sequence"][1:2]
    links, assemblies, related, excluded = build_links([source], strain_inventory())
    assert not links and not assemblies and not related
    assert excluded[0]["reason"] == "no_eligible_own_deposit_match"


@pytest.mark.parametrize("status", ["private", "dead", "unknown"])
def test_availability_is_not_an_identity_failure(status):
    source = source_record()
    source["strain"]["status"] = "published offline"
    source["deposits"][0]["status"] = status
    links, assemblies, _, _ = build_links([source], strain_inventory())
    assert len(assemblies) == 1
    assert any(r["deposit_status"] == status for r in links)


@pytest.mark.parametrize("change", ["erroneous", "deprecated", "erroneous_status"])
def test_deposit_identity_flags_prevent_sequence_links(change):
    source = source_record()
    if change == "erroneous":
        source["strain"]["relation"]["deposit"][0]["erroneous"] = True
    elif change == "deprecated":
        source["deposits"][0]["cultureCollection"]["deprecated"] = True
    else:
        source["deposits"][0]["status"] = "erroneous data"
    links, assemblies, _, excluded = build_links([source], strain_inventory())
    assert not assemblies
    assert len(links) == 1
    assert any(r["reason"] == "erroneous_deposit" for r in excluded)


@pytest.mark.parametrize("change", ["wrong_doi", "missing_flag", "wrong_designation", "unknown_deposit",
                                    "missing_detail", "duplicate", "boolean_id", "bad_collection"])
def test_corrupt_source_shapes_and_cross_record_paths_fail_closed(change):
    source = source_record()
    if change == "wrong_doi":
        source["strain"]["doi"] = "10.60712/SI-ID253.1"
    elif change == "missing_flag":
        del source["strain"]["relation"]["deposit"][0]["erroneous"]
    elif change == "wrong_designation":
        source["strain"]["sequence"][0]["deposit"][0]["designation"] = "DSM 25618"
    elif change == "unknown_deposit":
        source["strain"]["sequence"][0]["deposit"][0]["siDP"] = 99
    elif change == "missing_detail":
        source["deposits"].pop()
    elif change == "duplicate":
        source["deposits"].append(copy.deepcopy(source["deposits"][0]))
    elif change == "bad_collection":
        source["deposits"][0]["cultureCollection"]["ccID"] = 999
    else:
        source["strain"]["siID"] = True
    with pytest.raises(ValueError):
        build_links([source], strain_inventory())


@pytest.mark.parametrize("accession,seq_type", [("NC_000001", "genome"), ("GCA_000369045", "gene"),
                                               ("invalid", "genome"), ("AB123456", "unknown")])
def test_unknown_or_mistyped_identifiers_are_retained_as_exclusions(accession, seq_type):
    source = source_record()
    source["strain"]["sequence"][0].update(accessionNumber=accession, type=seq_type)
    _, assemblies, _, excluded = build_links([source], strain_inventory())
    assert not assemblies
    assert any(r["accession"] == accession and r["reason"] == "unsupported_sequence_type_or_accession"
               for r in excluded)


def test_related_headers_are_unique_and_link_order_is_reproducible():
    assert len(RELATED_COLUMNS) == len(set(RELATED_COLUMNS))
    source = source_record()
    baseline = build_links([source], strain_inventory())
    source["deposits"].reverse()
    source["strain"]["sequence"].reverse()
    assert build_links([source], list(reversed(strain_inventory()))) == baseline


def test_private_registered_isolate_without_collection_does_not_break_other_deposits():
    source = source_record()
    baseline = build_links([source], strain_inventory())
    source["strain"]["relation"]["deposit"].append(
        {"siDP": 4, "designation": "CLA-AA-H244", "erroneous": False})
    source["deposits"].append({"siDP": 4, "designation": "CLA-AA-H244", "status": "private"})
    assert build_links([source], strain_inventory()) == baseline
    assert project_record(source)["deposits"][-1]["designation"] == "CLA-AA-H244"
