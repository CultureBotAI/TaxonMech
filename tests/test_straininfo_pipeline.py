"""Pinned StrainInfo outputs cannot invent deposit bindings or hide incomplete source records."""

from __future__ import annotations

import gzip
import json
import shutil
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from taxonmech import straininfo
from taxonmech.extract import write_tsv


def source_record():
    return {
        "strain": {
            "siID": 14277,
            "doi": "10.60712/SI-ID14277.3",
            "status": "published online",
            "bdID": 5,
            "relation": {
                "deposit": [
                    {"siDP": 847459, "designation": "DSM 30083", "ccID": 1, "erroneous": False},
                    {"siDP": 11317, "designation": "ATCC 11775", "ccID": 2, "erroneous": False},
                ]
            },
            "sequence": [
                {
                    "accessionNumber": "GCA_000690815",
                    "type": "genome",
                    "assemblyLevel": "contig",
                    "deposit": [{"siDP": 847459, "designation": "DSM 30083"}],
                },
                {
                    "accessionNumber": "X80725.2",
                    "type": "rrnaop",
                    "description": "16S rRNA",
                    "deposit": [{"siDP": 847459, "designation": "DSM 30083"}],
                },
                {
                    "accessionNumber": "GCA_000005845.2",
                    "type": "genome",
                    "deposit": [{"siDP": 11317, "designation": "ATCC 11775"}],
                },
            ],
        },
        "deposits": [
            {
                "siDP": 847459,
                "designation": "DSM 30083",
                "status": "available",
                "cultureCollection": {"ccID": 1, "code": "DSMZ", "deprecated": False},
            },
            {
                "siDP": 11317,
                "designation": "ATCC 11775",
                "status": "available",
                "cultureCollection": {"ccID": 2, "code": "ATCC", "deprecated": False},
            },
        ],
    }


def _snapshot(tmp_path, *, declared_count=1, records=None):
    root = tmp_path / "repo"
    for name in straininfo.INPUT_PATHS:
        (root / name).parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(straininfo.ROOT / straininfo.INPUT_PATHS[1], root / straininfo.INPUT_PATHS[1])
    strains = [
        {
            "strain_id": "kgmicrobe.strain:bacdive_5",
            "bacdive_id": "5",
            "culture_collection_ids": "kgmicrobe.strain:DSM-30083",
        },
        {
            "strain_id": "kgmicrobe.strain:bacdive_10",
            "bacdive_id": "10",
            "culture_collection_ids": "kgmicrobe.strain:DSM-1",
        },
    ]
    write_tsv(root / straininfo.INPUT_PATHS[0], list(strains[0]), strains)
    snapshot = root / "snapshot"
    snapshot.mkdir()
    with gzip.open(snapshot / "records.jsonl.gz", "wt", encoding="utf-8") as handle:
        for record in records if records is not None else [source_record()]:
            handle.write(json.dumps(record) + "\n")
    source = {
        "format_version": 1,
        "captured_at": "2026-09-12T02:00:00Z",
        "api_version": "2.1.0",
        "license": "CC-BY-4.0",
        "api_base": "https://api.straininfo.dsmz.de",
        "catalog_count": 100,
        "candidate_count": declared_count,
        "records": {**straininfo.file_info(snapshot / "records.jsonl.gz"), "rows": declared_count},
        "inputs": straininfo.input_provenance(root),
        "responses": [
            {
                "kind": kind,
                "url": "https://api.straininfo.dsmz.de/" + endpoint,
                "bytes": 1,
                "sha256": "1" * 64,
            }
            for kind, endpoint in (
                ("ids", "v2/strain/all/"),
                ("search", "v2/data/strain/search/0"),
                ("records", "v2/data/strain/max/14277"),
            )
        ],
    }
    (snapshot / "SNAPSHOT.json").write_text(json.dumps(source))
    config = {
        "snapshot": "2026-09-12",
        "snapshot_path": "snapshot",
        "snapshot_sha256": straininfo.sha256(snapshot / "SNAPSHOT.json"),
        "api_version": "2.1.0",
        "api_base": source["api_base"],
        "license": "CC-BY-4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
        "citation": "https://doi.org/10.1093/database/baaf059",
    }
    (root / "conf").mkdir()
    (root / "conf/straininfo.yaml").write_text(yaml.safe_dump(config))
    return root, snapshot, root / "data/straininfo", config


def _published(tmp_path):
    fixture = _snapshot(tmp_path)
    root, snapshot, directory, config = fixture
    straininfo.generate(snapshot, directory, root, config, apply=True)
    return fixture


def _refresh_output_hashes(directory):
    manifest = yaml.safe_load((directory / "MANIFEST.yaml").read_text())
    manifest["outputs"] = [straininfo.output_info(directory / name) for name in straininfo.OUTPUT_NAMES]
    (directory / "MANIFEST.yaml").write_text(yaml.safe_dump(manifest))
    return manifest


def _component_bytes(directory):
    return {path.name: path.read_bytes() for path in directory.iterdir()}


def _tracked_component(monkeypatch):
    def tracked(command, **kwargs):
        assert command == ["git", "ls-files", "--", "data/straininfo"]
        return "\n".join(f"data/straininfo/{name}" for name in (*straininfo.OUTPUT_NAMES, "MANIFEST.yaml"))

    monkeypatch.setattr(straininfo.subprocess, "check_output", tracked)


def test_source_replay_keeps_own_deposit_sequence_and_is_reproducible(tmp_path, monkeypatch):
    root, snapshot, directory, config = _snapshot(tmp_path)
    dry = straininfo.generate(snapshot, directory, root, config)
    assert not directory.exists()
    assert dry["summary"]["source_records"] == 1
    assert dry["summary"]["ncbi_assemblies"] == 1
    assert dry["summary"]["nucleotide_sequences"] == 1
    straininfo.generate(snapshot, directory, root, config, apply=True)
    before = _component_bytes(directory)
    straininfo.generate(snapshot, directory, root, config, apply=True)
    assert _component_bytes(directory) == before
    assemblies, related = straininfo.record_links(directory, root=root)
    assert set(assemblies) == {"kgmicrobe.strain:bacdive_5"}
    assert [row["assembly_id"] for row in assemblies["kgmicrobe.strain:bacdive_5"]] == [
        "ncbi.assembly:GCA_000690815",
    ]
    assert {row["record_type"] for row in related["kgmicrobe.strain:bacdive_5"]} == {
        "STRAININFO_STRAIN",
        "STRAININFO_DEPOSIT",
        "NUCLEOTIDE_SEQUENCE",
    }
    assert all(
        row["straininfo_evidence"]["deposit_id"] == "straininfo.deposit:847459"
        for row in [*assemblies["kgmicrobe.strain:bacdive_5"], *related["kgmicrobe.strain:bacdive_5"]]
    )
    _tracked_component(monkeypatch)
    assert straininfo.provenance_problems(root) == []
    assert straininfo.provenance_problems(root, reproduce=False) == []


def test_related_table_has_exactly_one_record_name_header(tmp_path):
    assert len(straininfo.RELATED_COLUMNS) == len(set(straininfo.RELATED_COLUMNS))
    assert straininfo.RELATED_COLUMNS.count("record_name") == 1
    path = tmp_path / "related_records.tsv.gz"
    straininfo.write_table(path, straininfo.RELATED_COLUMNS, [])
    assert straininfo.read_rows(path, required=straininfo.RELATED_COLUMNS) == []
    with gzip.open(path, "wt") as handle:
        handle.write("record_name\trecord_name\n")
    with pytest.raises(ValueError, match="duplicate TSV headers"):
        straininfo.read_rows(path)


@pytest.mark.parametrize("name", ["assemblies.tsv", "related_records.tsv.gz", "strain_links.tsv"])
def test_rehashed_derived_rows_cannot_transfer_a_deposit_to_another_strain(tmp_path, name):
    root, _, directory, _ = _published(tmp_path)
    rows = straininfo.read_rows(directory / name)
    rows[0]["strain_id"] = "kgmicrobe.strain:bacdive_10"
    straininfo.write_table(directory / name, straininfo.TABLES[name], rows)
    _refresh_output_hashes(directory)
    with pytest.raises(ValueError, match="does not reproduce from primary deposit evidence"):
        straininfo.record_links(directory, root=root)


def test_rehashed_assembly_cannot_borrow_another_deposits_sequence(tmp_path):
    root, _, directory, _ = _published(tmp_path)
    rows = straininfo.read_rows(directory / "assemblies.tsv")
    # A real accession elsewhere in the same source SI-ID is still not an own-deposit assertion.
    rows[0]["assembly_id"] = "ncbi.assembly:GCA_000005845.2"
    straininfo.write_table(directory / "assemblies.tsv", straininfo.ASSEMBLY_COLUMNS, rows)
    _refresh_output_hashes(directory)
    with pytest.raises(ValueError, match="does not reproduce from primary deposit evidence"):
        straininfo.record_links(directory, root=root)


@pytest.mark.parametrize("mutation", ["missing", "duplicate", "extra"])
def test_table_replay_checks_every_assertion_and_its_cardinality(tmp_path, mutation):
    root, _, directory, _ = _published(tmp_path)
    rows = straininfo.read_rows(directory / "related_records.tsv.gz")
    if mutation == "missing":
        rows.pop()
    else:
        added = deepcopy(rows[-1])
        if mutation == "extra":
            added["record_name"] = "invented source description"
        rows.append(added)
    straininfo.write_table(directory / "related_records.tsv.gz", straininfo.RELATED_COLUMNS, rows)
    _refresh_output_hashes(directory)
    with pytest.raises(ValueError, match="does not reproduce from primary deposit evidence"):
        straininfo.record_links(directory, root=root)


@pytest.mark.parametrize(
    "declared_count,records", [(2, None), (1, []), (2, [source_record(), source_record()])]
)
def test_generation_requires_the_actual_unique_source_record_census(tmp_path, declared_count, records):
    root, snapshot, directory, config = _snapshot(tmp_path, declared_count=declared_count, records=records)
    with pytest.raises(ValueError, match="actual source record count|Duplicate StrainInfo projected record"):
        straininfo.generate(snapshot, directory, root, config, apply=True)
    assert not directory.exists()


@pytest.mark.parametrize("reproduce", [True, False])
def test_conversion_and_provenance_reject_rehashed_false_source_counts(tmp_path, monkeypatch, reproduce):
    root, _, directory, _ = _published(tmp_path)
    source = json.loads((directory / "SOURCE.json").read_text())
    source["candidate_count"] = source["records"]["rows"] = 2
    (directory / "SOURCE.json").write_text(json.dumps(source))
    manifest = _refresh_output_hashes(directory)
    manifest["source"]["snapshot_sha256"] = straininfo.sha256(directory / "SOURCE.json")
    manifest["summary"]["source_records"] = 2
    (directory / "MANIFEST.yaml").write_text(yaml.safe_dump(manifest))
    config = yaml.safe_load((root / "conf/straininfo.yaml").read_text())
    config["snapshot_sha256"] = manifest["source"]["snapshot_sha256"]
    (root / "conf/straininfo.yaml").write_text(yaml.safe_dump(config))
    with pytest.raises(ValueError, match="actual source record count"):
        straininfo.record_links(directory, root=root)
    _tracked_component(monkeypatch)
    problems = straininfo.provenance_problems(root, reproduce=reproduce)
    assert len(problems) == 1 and "actual source record count" in problems[0]


def test_current_strain_inventory_must_match_the_captured_inputs(tmp_path):
    root, _, directory, _ = _published(tmp_path)
    path = root / straininfo.INPUT_PATHS[0]
    path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="input inventories changed"):
        straininfo.record_links(directory, root=root)


def test_consistently_rewritten_primary_source_cannot_replace_the_configured_snapshot(tmp_path):
    root, _, directory, _ = _published(tmp_path)
    config_before = (root / "conf/straininfo.yaml").read_bytes()
    records = list(straininfo.read_records(directory / "records.jsonl.gz"))
    records[0]["strain"]["sequence"][0]["accessionNumber"] = "GCA_009999999"
    with gzip.open(directory / "records.jsonl.gz", "wt", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record) + "\n")
    source = json.loads((directory / "SOURCE.json").read_text())
    source["records"] = {**straininfo.file_info(directory / "records.jsonl.gz"), "rows": len(records)}
    (directory / "SOURCE.json").write_text(json.dumps(source))
    tables = straininfo.build_links(records, straininfo.read_rows(root / straininfo.INPUT_PATHS[0]))
    for (name, columns), rows in zip(straininfo.TABLES.items(), tables, strict=True):
        straininfo.write_table(directory / name, columns, rows)
    manifest = _refresh_output_hashes(directory)
    manifest["source"]["snapshot_sha256"] = straininfo.sha256(directory / "SOURCE.json")
    manifest["summary"] = straininfo.summary(tables, source)
    (directory / "MANIFEST.yaml").write_text(yaml.safe_dump(manifest))
    assert (root / "conf/straininfo.yaml").read_bytes() == config_before
    # All internal evidence and checksums agree; only the external configured pin exposes the substitution.
    with pytest.raises(ValueError, match="source pin differs from configuration"):
        straininfo.record_links(directory, root=root)


@pytest.mark.parametrize("canonical_config", ["missing", "different_pin"])
def test_generation_requires_explicit_config_to_use_a_different_source(tmp_path, canonical_config):
    root, snapshot, directory, config = _snapshot(tmp_path)
    config_path = root / "conf/straininfo.yaml"
    if canonical_config == "missing":
        config_path.unlink()
    else:
        config_path.write_text(yaml.safe_dump({**config, "snapshot_sha256": "0" * 64}))
    straininfo.generate(snapshot, directory, root, config, apply=True)
    assert straininfo.record_links(directory, root=root, config=config)[0]
    if canonical_config == "missing":
        with pytest.raises(FileNotFoundError):
            straininfo.record_links(directory, root=root)
    else:
        with pytest.raises(ValueError, match="source pin differs from configuration"):
            straininfo.record_links(directory, root=root)


def test_configured_pin_changed_during_conversion_cannot_authorize_the_returned_links(tmp_path, monkeypatch):
    root, _, directory, config = _published(tmp_path)
    real_build = straininfo.build_links

    def build(*args, **kwargs):
        result = real_build(*args, **kwargs)
        (root / "conf/straininfo.yaml").write_text(yaml.safe_dump({**config, "snapshot_sha256": "0" * 64}))
        return result

    monkeypatch.setattr(straininfo, "build_links", build)
    with pytest.raises(ValueError, match="configured source pin changed during conversion"):
        straininfo.record_links(directory, root=root)


def test_failure_partway_through_publication_restores_every_previous_file(tmp_path, monkeypatch):
    root, snapshot, directory, config = _published(tmp_path)
    before = _component_bytes(directory)
    real_replace = straininfo.os.replace
    failed = False

    def replace(source, destination):
        nonlocal failed
        if (
            not failed
            and Path(destination) == directory / "assemblies.tsv"
            and Path(source).name == "assemblies.tsv"
        ):
            failed = True
            raise OSError("simulated installation failure")
        return real_replace(source, destination)

    monkeypatch.setattr(straininfo.os, "replace", replace)
    with pytest.raises(OSError, match="simulated installation failure"):
        straininfo.generate(snapshot, directory, root, config, apply=True)
    assert failed
    assert _component_bytes(directory) == before


@pytest.mark.parametrize("changed", ["strain_inventory", "snapshot_metadata", "projected_records"])
def test_inputs_changed_during_generation_cannot_replace_the_published_component(
    tmp_path, monkeypatch, changed
):
    root, snapshot, directory, config = _published(tmp_path)
    before = _component_bytes(directory)
    real_build = straininfo.build_links
    modified = False
    path = {
        "strain_inventory": root / straininfo.INPUT_PATHS[0],
        "snapshot_metadata": snapshot / "SNAPSHOT.json",
        "projected_records": snapshot / "records.jsonl.gz",
    }[changed]

    def build(*args, **kwargs):
        nonlocal modified
        result = real_build(*args, **kwargs)
        if not modified:
            path.write_bytes(path.read_bytes() + b"\n")
            modified = True
        return result

    monkeypatch.setattr(straininfo, "build_links", build)
    with pytest.raises(ValueError, match="changed|differs|disagrees"):
        straininfo.generate(snapshot, directory, root, config, apply=True)
    assert _component_bytes(directory) == before


@pytest.mark.parametrize("collision", ["snapshot", "raw", "symlink_input", "output_alias", "directory"])
def test_destinations_cannot_overwrite_inputs_or_collide(tmp_path, collision):
    root, snapshot, directory, config = _snapshot(tmp_path)
    if collision == "snapshot":
        directory = snapshot
    elif collision == "raw":
        directory = root / "data/raw"
    else:
        directory.mkdir()
        if collision == "symlink_input":
            (directory / "assemblies.tsv").symlink_to(root / straininfo.INPUT_PATHS[0])
        elif collision == "output_alias":
            (directory / "assemblies.tsv").symlink_to(directory / "strain_links.tsv")
        else:
            (directory / "assemblies.tsv").mkdir()
    protected = {
        path: path.read_bytes()
        for path in [
            snapshot / "SNAPSHOT.json",
            snapshot / "records.jsonl.gz",
            root / straininfo.INPUT_PATHS[0],
        ]
    }
    with pytest.raises(ValueError, match="cannot overwrite inputs or another output"):
        straininfo.generate(snapshot, directory, root, config, apply=True)
    assert all(path.read_bytes() == before for path, before in protected.items())
