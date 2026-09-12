"""Primary-response completeness, replay and publication safety for StrainInfo."""

import gzip
import json

import pytest

from taxonmech import straininfo_snapshot as snapshot
from taxonmech.extract import write_tsv
from taxonmech.straininfo_links import project_record

STAMP = "2026-09-12T08:00:00Z"
BASE = snapshot.API_BASE


def record(number, deposit):
    own = {"siDP": number * 10, "designation": f"DSM {deposit}", "status": "available",
           "typeStrain": False, "lastUpdate": "2025-02-25",
           "cultureCollection": {"ccID": 1, "deprecated": False}}
    return {"strain": {"siID": number, "doi": f"10.60712/SI-ID{number}.1", "status": "published online",
                       "merged": [number + 1000], "relation": {"deposit": [
                           {"siDP": number * 10, "designation": f"DSM {deposit}", "ccID": 1,
                            "erroneous": False}]}, "sequence": []},
            "deposits": [own], "unrelated": {"discarded": True}}


@pytest.fixture
def primary(tmp_path, monkeypatch):
    root = tmp_path / "repo"
    raw = root / snapshot.INPUT_PATHS[0]
    raw.parent.mkdir(parents=True)
    write_tsv(raw, ["strain_id", "bacdive_id", "culture_collection_ids"], [
        {"strain_id": f"kgmicrobe.strain:bacdive_{i}", "bacdive_id": str(i),
         "culture_collection_ids": f"kgmicrobe.strain:DSM-{i}"} for i in (1, 2)])
    registry = root / snapshot.INPUT_PATHS[1]
    registry.parent.mkdir(parents=True)
    registry.write_bytes(snapshot.CAFI_REGISTRY_PATH.read_bytes())
    status = {"version": "2025.10", "private": False, "maintenance": {"status": False}}
    payloads = {
        BASE + "/": status,
        snapshot.API_SCHEMA: {"info": {"version": "2.1.0", "license": {
            "name": "CC BY 4.0", "url": "https://creativecommons.org/licenses/by/4.0/"}}},
        BASE + "/service/all/strains": [9, 5, 20],
        BASE + "/service/search/strain/all/0": {"count": 3, "next": 1,
                                               "data": [[9, ["DSM 2"], "Species", 0, "", 1]]},
        BASE + "/service/search/strain/all/1": {"count": 3, "data": [
            [5, ["DSM 1"], "Species", 0, "", 1], [20, ["ATCC 999"], "Other", 0, "", 3]]},
        BASE + "/v2/data/strain/max/5,9": [record(9, 2), record(5, 1)],
    }
    calls = []

    def request(url):
        calls.append(url)
        return json.dumps(payloads[url], indent=1).encode(), STAMP, {"Content-Type": "application/json"}

    monkeypatch.setattr(snapshot, "_request", request)
    return root, tmp_path / "capture", payloads, calls


def outputs(directory):
    return {n: (directory / n).read_bytes() for n in ("SNAPSHOT.json", "records.jsonl.gz")
            if (directory / n).exists()}


def rewrite_response(directory, metadata, value):
    data = json.dumps(value).encode()
    packed = gzip.compress(data, mtime=0)
    (directory / metadata["path"]).write_bytes(packed)
    metadata.update(bytes=len(data), sha256=snapshot._sha(data), compressed_bytes=len(packed),
                    compressed_sha256=snapshot._sha(packed))


def test_capture_retains_raw_bytes_and_replays_without_network(primary, monkeypatch):
    root, directory, payloads, calls = primary
    result = snapshot.capture(directory, root=root)
    assert result["catalog_count"] == 3 and result["candidate_count"] == 2
    rich = next(r for r in result["responses"] if r["kind"] == "records")
    assert snapshot.load_response(directory, rich) == json.dumps(payloads[rich["url"]], indent=1).encode()
    lines = gzip.decompress(outputs(directory)["records.jsonl.gz"]).splitlines()
    records = [json.loads(line) for line in lines]
    assert records == [project_record(record(5, 1)), project_record(record(9, 2))]
    before = outputs(directory)
    monkeypatch.setattr(snapshot, "_request", lambda _: pytest.fail("finished capture must replay offline"))
    assert snapshot.capture(directory, root=root) == result
    assert outputs(directory) == before
    assert calls.count(BASE + "/service/all/strains") == 2


def test_interrupted_capture_resumes_only_missing_requests(primary, monkeypatch):
    root, directory, _, calls = primary
    original = snapshot._request

    def interrupted(url):
        if "/v2/data/" in url:
            raise OSError("interrupted request")
        return original(url)

    monkeypatch.setattr(snapshot, "_request", interrupted)
    with pytest.raises(OSError, match="interrupted"):
        snapshot.capture(directory, root=root)
    assert not outputs(directory)
    previous_calls = list(calls)
    monkeypatch.setattr(snapshot, "_request", original)
    snapshot.capture(directory, root=root)
    assert calls[:len(previous_calls)] == previous_calls
    assert calls.count(snapshot.API_SCHEMA) == 1
    assert calls.count(BASE + "/service/search/strain/all/0") == 1


@pytest.mark.parametrize("mutation", ["bad_count", "repeated_next", "duplicate_id", "missing_id",
                                      "wrong_requested_id", "duplicate_record", "missing_record",
                                      "new_own_deposit", "api_version", "census_after", "license"])
def test_semantically_invalid_capture_fails_even_with_updated_checksums(primary, mutation):
    root, directory, _, _ = primary
    snapshot.capture(directory, root=root)
    saved = outputs(directory)
    plan = json.loads((directory / "CAPTURE.json").read_text())
    if mutation in {"api_version", "census_after", "license"}:
        metadata = (plan["checks"][1] if mutation == "api_version" else
                    plan["checks"][2] if mutation == "census_after" else plan["api_schema"])
    else:
        kind = "records" if mutation in {"wrong_requested_id", "duplicate_record", "missing_record",
                                        "new_own_deposit"} else "search"
        metadata = next(r for r in plan["responses"] if r["kind"] == kind)
    value = json.loads(snapshot.load_response(directory, metadata))
    if mutation == "bad_count":
        value["count"] = 2
    elif mutation == "repeated_next":
        value["next"] = 0
    elif mutation == "duplicate_id":
        value["data"].append(value["data"][0])
    elif mutation == "missing_id":
        value["data"] = []
    elif mutation == "wrong_requested_id":
        value[0]["strain"]["siID"] = 20
    elif mutation == "duplicate_record":
        value.append(value[0])
    elif mutation == "missing_record":
        value.pop()
    elif mutation == "new_own_deposit":
        value[0]["deposits"][0]["designation"] = "DSM 999"
    elif mutation == "api_version":
        value["version"] = "2026.01"
    elif mutation == "census_after":
        value[0] = 999
    else:
        value["info"]["license"]["name"] = "different"
    rewrite_response(directory, metadata, value)
    (directory / "CAPTURE.json").write_bytes(snapshot._json_bytes(plan))
    with pytest.raises(ValueError):
        snapshot.finalize(directory, root=root)
    assert outputs(directory) == saved


@pytest.mark.parametrize("mutation", ["gzip", "raw_hash", "path_escape", "input", "projection", "timestamp"])
def test_integrity_failures_preserve_existing_snapshot(primary, mutation):
    root, directory, _, _ = primary
    snapshot.capture(directory, root=root)
    plan = json.loads((directory / "CAPTURE.json").read_text())
    if mutation == "gzip":
        (directory / plan["responses"][0]["path"]).write_bytes(b"changed")
    elif mutation == "raw_hash":
        plan["responses"][0]["sha256"] = "0" * 64
    elif mutation == "path_escape":
        plan["responses"][0]["path"] = "responses/../../outside.json.gz"
    elif mutation == "input":
        with (root / snapshot.INPUT_PATHS[0]).open("a") as handle:
            handle.write("\n")
    elif mutation == "projection":
        (directory / "records.jsonl.gz").write_bytes(b"different existing snapshot")
    else:
        plan["responses"][0]["retrieved_at"] = "2026-09-12T08:00:00"
    (directory / "CAPTURE.json").write_bytes(snapshot._json_bytes(plan))
    saved = outputs(directory)
    with pytest.raises(ValueError):
        snapshot.finalize(directory, root=root)
    assert outputs(directory) == saved


def test_late_publication_failure_rolls_back_projection(primary, monkeypatch):
    root, directory, _, _ = primary
    snapshot.capture(directory, root=root)
    for name in outputs(directory):
        (directory / name).unlink()
    original = snapshot._new_file

    def failing(path, data):
        if path.name == "SNAPSHOT.json":
            raise OSError("publication failure")
        original(path, data)

    monkeypatch.setattr(snapshot, "_new_file", failing)
    with pytest.raises(OSError, match="publication failure"):
        snapshot.finalize(directory, root=root)
    assert not outputs(directory)


def test_input_change_during_finalization_is_detected(primary, monkeypatch):
    root, directory, _, _ = primary
    snapshot.capture(directory, root=root)
    saved = outputs(directory)
    original = snapshot.project_record

    def changing(value):
        with (root / snapshot.INPUT_PATHS[0]).open("a") as handle:
            handle.write("\n")
        return original(value)

    monkeypatch.setattr(snapshot, "project_record", changing)
    with pytest.raises(ValueError, match="changed during finalization"):
        snapshot.finalize(directory, root=root)
    assert outputs(directory) == saved


def test_wrong_checkpoint_is_not_refetched_or_replaced(primary, monkeypatch):
    root, directory, _, _ = primary
    snapshot.capture(directory, root=root)
    (directory / "CAPTURE.json").unlink()
    (directory / "SNAPSHOT.json").unlink()
    path = directory / "responses/ids-before.json.gz"
    path.write_bytes(b"bad cache")
    monkeypatch.setattr(snapshot, "_request", lambda _: pytest.fail("bad cache must not be replaced"))
    with pytest.raises(ValueError, match="checksum"):
        snapshot.capture(directory, root=root)
    assert path.read_bytes() == b"bad cache"


@pytest.mark.parametrize("workers", [0, 3, True])
def test_worker_limit_is_enforced_before_network(primary, workers):
    root, directory, _, calls = primary
    with pytest.raises(ValueError):
        snapshot.capture(directory, root=root, workers=workers)
    assert calls == [] and not directory.exists()


def test_cli_offline_finalize(primary, capsys):
    root, directory, _, _ = primary
    snapshot.capture(directory, root=root)
    assert snapshot.main(["--out", str(directory), "--root", str(root), "--finalize-only"]) == 0
    assert json.loads(capsys.readouterr().out)["candidate_count"] == 2


def test_network_retries_are_bounded_and_use_backoff(monkeypatch):
    attempts, pauses = [], []

    def unavailable(request, timeout):
        attempts.append((request.full_url, timeout))
        raise OSError("upstream unavailable")

    monkeypatch.setattr(snapshot.urllib.request, "urlopen", unavailable)
    monkeypatch.setattr(snapshot.time, "sleep", pauses.append)
    with pytest.raises(OSError, match="upstream unavailable"):
        snapshot._request(BASE + "/")
    assert len(attempts) == 4 and pauses == [1, 2, 4]
    assert all(timeout <= 60 for _, timeout in attempts)


def test_capture_cannot_write_inside_selection_input_parent(primary):
    root, _, _, calls = primary
    with pytest.raises(ValueError, match="cannot contain"):
        snapshot.capture(root / "data/raw", root=root)
    assert calls == []
    assert not (root / "data/raw/SELECTION.json").exists()
