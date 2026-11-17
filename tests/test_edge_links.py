"""Typed source links preserve versions, provenance and unavailable review."""

import csv
import importlib
import io
import json
import os
from pathlib import Path

import pytest
import yaml

from taxonmech import edge_links as adapter

SCHEMA_BYTES = (Path(__file__).resolve().parents[1] / adapter.SCHEMA).read_bytes()


@pytest.fixture(autouse=True)
def shared_contract():
    if os.environ.get("REQUIRE_EDGE_CONTRACT") == "1":
        importlib.import_module("kg_microbe_curation.native")
    else:
        pytest.importorskip("kg_microbe_curation.native")


def row(surface, **changes):
    value = {
        "strain_id": "kgmicrobe.strain:bacdive_10",
        "source": "GOLD",
        "source_id": "gold:Ga001",
        "source_reference_id": "",
        "taxon_id": "NCBITaxon:562",
        "source_field": "assembly accession",
        "matched_strain_id": "kgmicrobe.strain:LMG-001a",
        "source_strain_identifiers": "LMG 001a",
        "source_strain_field": "strain",
        "source_organism_id": "gold:Go002",
        "source_project_id": "gold:Gp003",
    }
    if surface == "assemblies":
        value.update(
            assembly_id="ncbi.assembly:GCA_011516945", assembly_level="draft", assembly_name="native"
        )
    elif surface == "genomes":
        value.update(
            genome_id="patric:104097.005",
            source_database="patric",
            genome_name="native",
            assembly_level="plasmid",
        )
    else:
        value.update(record_id="gold:Go002", record_type="GOLD_ORGANISM", record_name="native")
    return {**value, **changes}


def direct(surface, original=None, owner=None):
    value = original or row(surface)
    owner = owner or {"strain_id": value["strain_id"], "taxon_ids": "NCBITaxon:999", "status": "REVIEWED"}
    paths = (
        adapter.SURFACES[surface]["source"],
        *adapter.OWNERS,
        adapter.MANIFEST,
        adapter.SCHEMA,
        *adapter.SEMANTIC_FILES,
    )
    return adapter.adapt_link(
        value,
        position=1,
        owners=[("strain_id", adapter.OWNERS[0], 1, owner)],
        missing=[{"role": "matched_strain_id", "strain_id": value["matched_strain_id"]}],
        commit="a" * 40,
        surface=surface,
        hashes={path: "b" * 64 for path in paths},
        rules=adapter.constraints(yaml.safe_load(SCHEMA_BYTES), surface),
        prefixes={},
        upstream="kg-microbe@fixture",
    )


@pytest.mark.parametrize("surface", adapter.SURFACES)
def test_typed_native_links_never_inherit_owner_review(surface):
    original = row(surface)
    assertion = direct(surface)
    assert assertion["payload"]["native_payload"] == original
    assert assertion["payload"]["predicate"] == "taxonmech:" + adapter.SURFACES[surface]["slot"]
    assert assertion["payload"]["context"]["native_class"] == adapter.SURFACES[surface]["class"]
    assert (
        assertion["payload"]["context"]["owner_bindings"][0]["native_payload"]["taxon_ids"] == "NCBITaxon:999"
    )
    assert assertion["payload"]["context"]["unavailable_owner_bindings"]
    assert assertion["assurance"] == "unassessed"
    assert assertion["native_review"]["locator"] is None
    assert assertion["independent_scientific_review"] is False


def test_versions_dotted_ids_and_gold_source_chain_are_lossless():
    unversioned = direct("assemblies")
    versioned = direct("assemblies", row("assemblies", assembly_id="ncbi.assembly:GCA_011516945.1"))
    assert unversioned["assertion_id"] != versioned["assertion_id"]
    assert unversioned["payload"]["object"] == "ncbi.assembly:GCA_011516945"
    assert direct("genomes")["payload"]["object"] == "patric:104097.005"
    payload = direct("related")["payload"]["native_payload"]
    assert payload["source_organism_id"] == "gold:Go002"
    assert payload["source_project_id"] == "gold:Gp003"
    assert payload["source_id"] == "gold:Ga001"


@pytest.mark.parametrize(
    "surface,changes",
    [
        ("genomes", {"source_database": "img"}),
        ("related", {"record_type": "GOLD_PROJECT"}),
        ("assemblies", {"assembly_id": "ncbi.assembly:GCA_011516945.0"}),
        ("assemblies", {"source": "STRAININFO"}),
        ("genomes", {"source": "ALLTHEBACTERIA"}),
    ],
)
def test_typed_target_mismatch_and_unbound_nested_overlay_are_rejected(surface, changes):
    with pytest.raises(ValueError):
        direct(surface, row(surface, **changes))


def test_owner_context_is_bound_and_never_alias_normalized():
    source = row("assemblies")
    owners = {
        "kgmicrobe.strain:lmg-001a": [(adapter.OWNERS[1], 1, {"strain_id": "kgmicrobe.strain:lmg-001a"})]
    }
    bindings, missing = adapter.owner_matches(source, owners)
    assert not bindings and len(missing) == 2
    original = direct("assemblies")
    changed = direct("assemblies", owner={"strain_id": source["strain_id"], "taxon_ids": "NCBITaxon:7"})
    assert original["native_locator"]["payload_sha256"] == changed["native_locator"]["payload_sha256"]
    assert original["assertion_id"] != changed["assertion_id"]


def fixture_sources(surface="assemblies"):
    def tsv(rows):
        handle = io.StringIO()
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
        return handle.getvalue().encode()

    source_path = adapter.SURFACES[surface]["source"]
    sources = {
        source_path: tsv([row(surface), row(surface, source_reference_id="002")]),
        adapter.OWNERS[0]: tsv([{"strain_id": row(surface)["strain_id"], "taxon_ids": "NCBITaxon:562"}]),
        adapter.OWNERS[1]: tsv(
            [{"strain_id": row(surface)["matched_strain_id"], "taxon_ids": "NCBITaxon:562"}]
        ),
        adapter.SCHEMA: SCHEMA_BYTES,
        **{path: b"Native scoped evidence.\n" for path in adapter.SEMANTIC_FILES},
    }
    sources[adapter.MANIFEST] = yaml.safe_dump(
        {
            "kg_microbe_source": "kg-microbe@fixture",
            "outputs": [
                {
                    "path": Path(path).name,
                    "rows": 2 if path == source_path else 1,
                    "bytes": len(sources[path]),
                    "sha256": adapter.sha(sources[path]),
                }
                for path in (source_path, *adapter.OWNERS)
            ],
        }
    ).encode()
    return sources


def install_sources(monkeypatch, sources):
    def git(command, **kwargs):
        if "get-url" in command:
            return "https://github.com/CultureBotAI/TaxonMech.git\n"
        return sources[command[-1].split(":", 1)[1]]

    monkeypatch.setattr(adapter.subprocess, "check_output", git)


def test_real_spawn_matches_serial_and_exact_membership(tmp_path, monkeypatch):
    install_sources(monkeypatch, fixture_sources())
    first, second = tmp_path / "serial", tmp_path / "parallel"
    serial = adapter.export_links(tmp_path, "a" * 40, "assemblies", first, None)
    parallel = adapter.export_links(tmp_path, "a" * 40, "assemblies", second, None, workers=4)
    assert (first / "assertions.jsonl").read_bytes() == (second / "assertions.jsonl").read_bytes()
    assert serial["assertion_membership_sha256"] == parallel["assertion_membership_sha256"]
    assert parallel["native_status_counts"] == {"unassessed": 2}
    assert parallel["source_missing_owner_counts"] == {}


@pytest.mark.parametrize("mutation", ["reverse", "duplicate"])
def test_persisted_valid_line_mutation_cannot_publish(tmp_path, monkeypatch, mutation):
    install_sources(monkeypatch, fixture_sources())
    original_open, changed = Path.open, False

    def mutate(path, mode="r", *args, **kwargs):
        nonlocal changed
        if path.name == "assertions.jsonl" and mode == "rb" and not changed:
            changed = True
            with original_open(path, "rb") as handle:
                lines = handle.readlines()
            assert all(json.loads(line)["assurance"] == "unassessed" for line in lines)
            with original_open(path, "wb") as handle:
                handle.writelines(lines[::-1] if mutation == "reverse" else [lines[0], lines[0]])
        return original_open(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", mutate)
    with pytest.raises(ValueError, match="Persisted native bytes"):
        adapter.export_links(tmp_path, "a" * 40, "assemblies", tmp_path / "output", None)
    assert changed and not (tmp_path / "output").exists()


@pytest.mark.parametrize("failure", ["hash", "count", "unselected_type"])
def test_full_preflight_verifies_inventory_and_unselected_rows(tmp_path, monkeypatch, failure):
    sources = fixture_sources()
    if failure == "hash":
        sources[adapter.OWNERS[0]] = sources[adapter.OWNERS[0]].replace(b"NCBITaxon:562", b"NCBITaxon:999")
    elif failure == "count":
        sources[adapter.MANIFEST] = sources[adapter.MANIFEST].replace(b"rows: 2", b"rows: 3")
    else:
        path = adapter.SURFACES["assemblies"]["source"]
        sources[path] = sources[path].replace(b"GCA_011516945", b"GCA_011516945.0")
    install_sources(monkeypatch, sources)
    with pytest.raises(ValueError):
        adapter.export_links(tmp_path, "a" * 40, "assemblies", tmp_path / "output", [1])
    assert not (tmp_path / "output").exists()


def test_spawn_worker_failure_never_publishes(tmp_path, monkeypatch):
    install_sources(monkeypatch, fixture_sources())
    original_prepare = adapter.prepare

    def broken(*args):
        prepared = original_prepare(*args)
        prepared["common"]["hashes"][adapter.SCHEMA] = "invalid"
        return prepared

    monkeypatch.setattr(adapter, "prepare", broken)
    with pytest.raises(ValueError):
        adapter.export_links(tmp_path, "a" * 40, "assemblies", tmp_path / "output", None, workers=4)
    assert not (tmp_path / "output").exists()
