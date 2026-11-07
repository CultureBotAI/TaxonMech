"""Native taxonomy mappings cannot gain identity or scientific approval."""

import csv
import importlib
import io
import os
from pathlib import Path

import pytest
import yaml

from taxonmech import edge_curation as adapter
from taxonmech.edge_curation import MANIFEST, SCHEMA, SEMANTICS, SOURCE, adapt_mapping


@pytest.fixture(autouse=True)
def shared_contract():
    if os.environ.get("REQUIRE_EDGE_CONTRACT") == "1":
        importlib.import_module("kg_microbe_curation.native")
    else:
        pytest.importorskip("kg_microbe_curation.native")


def row(**changes):
    return {
        "gtdb_id": "GTDB:s__Example",
        "gtdb_label": "s__Example",
        "gtdb_parent": "GTDB:g__Example",
        "ncbitaxon_id": "NCBITaxon:1",
        "predicate": "skos:broadMatch",
        "genome_count": "002",
        **changes,
    }


def adapt(value):
    return adapt_mapping(
        value,
        position=1,
        commit="a" * 40,
        hashes={SOURCE: "b" * 64, MANIFEST: "c" * 64, SCHEMA: "d" * 64, SEMANTICS: "e" * 64},
        prefixes={},
        provenance="kg-microbe@pinned",
    )


@pytest.mark.parametrize(
    "predicate", ["skos:broadMatch", "skos:narrowMatch", "skos:closeMatch", "skos:exactMatch"]
)
def test_native_predicate_orientation_and_whole_payload_preserved(predicate):
    original = row(predicate=predicate)
    actual = adapt(original)
    assert actual["payload"]["subject"] == original["gtdb_id"]
    assert actual["payload"]["object"] == original["ncbitaxon_id"]
    assert actual["payload"]["predicate"] == predicate
    assert actual["payload"]["native_payload"] == original
    assert actual["assurance"] == "unassessed"
    assert actual["native_review"]["locator"] is None
    assert actual["independent_scientific_review"] is False


def test_record_status_cannot_approve_an_extracted_mapping():
    assert adapt(row(mapping_status="REVIEWED"))["assurance"] == "unassessed"


@pytest.mark.parametrize(
    "changes", [{"predicate": "owl:sameAs"}, {"gtdb_id": ""}, {"genome_count": "unknown"}]
)
def test_invalid_mapping_shape_fails(changes):
    with pytest.raises(ValueError):
        adapt(row(**changes))


def test_changed_count_or_parent_changes_identity():
    original = adapt(row())["assertion_id"]
    assert adapt(row(genome_count="3"))["assertion_id"] != original
    assert adapt(row(gtdb_parent="GTDB:g__Other"))["assertion_id"] != original


@pytest.fixture
def export_fixture(tmp_path, monkeypatch):
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=list(row()), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows([row(), row(gtdb_id="GTDB:s__Other", ncbitaxon_id="NCBITaxon:2")])
    source = stream.getvalue().encode()
    sources = {
        SOURCE: source,
        SCHEMA: b"prefixes: {}\n",
        SEMANTICS: b"Native taxonomy scope.\n",
        MANIFEST: yaml.safe_dump(
            {
                "kg_microbe_source": "kg-microbe@fixture",
                "outputs": [
                    {
                        "path": "gtdb_mappings.tsv",
                        "rows": 2,
                        "bytes": len(source),
                        "sha256": adapter.sha(source),
                    }
                ],
            }
        ).encode(),
    }

    def git(command, **kwargs):
        if "get-url" in command:
            return "https://github.com/CultureBotAI/TaxonMech.git\n"
        return sources[command[-1].split(":", 1)[1]]

    monkeypatch.setattr(adapter.subprocess, "check_output", git)
    return tmp_path, sources


@pytest.mark.parametrize("mutation", ["reverse", "duplicate"])
def test_export_rejects_changed_persisted_valid_membership(export_fixture, monkeypatch, mutation):
    tmp_path, _ = export_fixture
    original_open = Path.open
    changed = False

    def mutate_readback(path, mode="r", *args, **kwargs):
        nonlocal changed
        if path.name == "assertions.jsonl" and mode == "rb" and not changed:
            changed = True
            with original_open(path, "rb") as handle:
                lines = handle.readlines()
            replacement = lines[::-1] if mutation == "reverse" else [lines[0], lines[0]]
            with original_open(path, "wb") as handle:
                handle.writelines(replacement)
        return original_open(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", mutate_readback)
    output = tmp_path / "output"
    with pytest.raises(ValueError, match="Persisted native bytes"):
        adapter.export_assertions(tmp_path, "a" * 40, output, None)
    assert changed
    assert not output.exists()


def test_serial_and_spawn_parallel_exports_have_identical_bytes(export_fixture):
    root, _ = export_fixture
    serial, parallel = root / "serial", root / "parallel"
    serial_manifest = adapter.export_assertions(root, "a" * 40, serial, None, workers=1)
    parallel_manifest = adapter.export_assertions(root, "a" * 40, parallel, None, workers=4)
    assert (serial / "assertions.jsonl").read_bytes() == (parallel / "assertions.jsonl").read_bytes()
    for key in ("rows", "assertions_sha256", "assertion_membership_sha256", "native_status_counts"):
        assert serial_manifest[key] == parallel_manifest[key]


def test_spawn_worker_failure_publishes_nothing(export_fixture):
    root, sources = export_fixture
    invalid = sources[SOURCE].replace(b"skos:broadMatch", b"invalid:predicate", 1)
    sources[SOURCE] = invalid
    manifest = yaml.safe_load(sources[MANIFEST])
    manifest["outputs"][0].update(bytes=len(invalid), sha256=adapter.sha(invalid))
    sources[MANIFEST] = yaml.safe_dump(manifest).encode()
    output = root / "failed"
    with pytest.raises(ValueError, match="unsupported native taxonomy mapping"):
        adapter.export_assertions(root, "a" * 40, output, None, workers=4)
    assert not output.exists()


def test_parallel_submission_is_bounded_and_ordered(monkeypatch):
    consumed = 0

    def rows():
        nonlocal consumed
        for position in range(1, 1001):
            consumed += 1
            yield position, {"position": position}

    class Future:
        def __init__(self, jobs):
            self.jobs = jobs

        def result(self):
            return self.jobs

    class Executor:
        def __init__(self, **kwargs):
            assert kwargs["max_workers"] == 4

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def submit(self, function, jobs, common):
            assert len(jobs) <= adapter.VALIDATION_BATCH_SIZE
            return Future(jobs)

    monkeypatch.setattr(adapter, "ProcessPoolExecutor", Executor)
    stream = adapter._validated_assertions(rows(), {}, 4)
    first = next(stream)
    assert consumed == 4 * adapter.VALIDATION_BATCH_SIZE
    assert [first[0], *(position for position, _ in stream)] == list(range(1, 1001))
