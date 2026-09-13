"""Completed source captures must remain immutable when replay rejects drift."""

import gzip
import hashlib
import io
import json

import pytest

from scripts import fetch_bvbrc, fetch_seqcode
from taxonmech import bacdive_snapshot
from tests.test_source_expansion import bacdive_record


def test_rejected_bacdive_replay_does_not_overwrite_published_projection(tmp_path, monkeypatch):
    census = b"ID,species,designation_header\n1,Species,X\n"
    payload = {"results": {"1": bacdive_record()}, "count": 1, "next": None}
    monkeypatch.setattr(bacdive_snapshot, "request",
                        lambda url: census if "csv" in url else json.dumps(payload).encode())
    bacdive_snapshot.capture(tmp_path)
    before = {name: (tmp_path / name).read_bytes() for name in ("SOURCE.json", "records.jsonl.gz")}
    payload["results"]["1"]["Name and taxonomic classification"]["strain designation"] = "changed"
    raw = json.dumps(payload).encode()
    (tmp_path / "records-0000.json.gz").write_bytes(gzip.compress(raw, mtime=0))
    metadata_path = tmp_path / "records-0000.json.metadata.json"
    metadata = json.loads(metadata_path.read_text())
    metadata.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    metadata_path.write_text(json.dumps(metadata))
    with pytest.raises(ValueError, match="differs"):
        bacdive_snapshot.capture(tmp_path)
    assert {name: (tmp_path / name).read_bytes() for name in before} == before


def test_bvbrc_replay_is_identical_and_rejects_drift_before_publication(tmp_path, monkeypatch):
    rich = {"genome_id": "562.1", "superkingdom": "Bacteria", "public": True, "strain": "DSM 1"}

    def stage(_directory, name, _fields):
        yield ([rich.copy()] if name == "records" else [{"genome_id": "562.1"}]), {"stage": name}

    monkeypatch.setattr(fetch_bvbrc, "stage", stage)
    fetch_bvbrc.capture(tmp_path)
    before = {path.name: path.read_bytes() for path in tmp_path.iterdir() if path.is_file()}
    fetch_bvbrc.capture(tmp_path)
    assert {name: (tmp_path / name).read_bytes() for name in before} == before
    rich["strain"] = "DSM 2"
    with pytest.raises(ValueError, match="differs"):
        fetch_bvbrc.capture(tmp_path)
    assert {name: (tmp_path / name).read_bytes() for name in before} == before


def test_seqcode_replay_is_identical_and_rejects_drift_before_publication(tmp_path, monkeypatch):
    page = {"response": {"status": "ok", "count": 1, "total_pages": 1, "current_page": 1,
                         "next": None}, "values": [{"id": 1, "name": "Native name"}]}
    monkeypatch.setattr(fetch_seqcode.urllib.request, "urlopen",
                        lambda *_a, **_k: io.BytesIO(json.dumps(page).encode()))
    source = fetch_seqcode.capture_all(tmp_path)
    names = ["SOURCE.json", "names.jsonl.gz", "type-genomes.jsonl.gz"]
    before = {name: (tmp_path / name).read_bytes() for name in names}
    assert fetch_seqcode.capture_all(tmp_path) == source
    assert {name: (tmp_path / name).read_bytes() for name in names} == before
    page["values"][0]["name"] = "Changed native name"
    raw = json.dumps(page).encode()
    (tmp_path / "names-0001.json.gz").write_bytes(gzip.compress(raw, mtime=0))
    metadata_path = tmp_path / "names-0001.json.gz.metadata.json"
    metadata = json.loads(metadata_path.read_text())
    metadata.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    metadata_path.write_text(json.dumps(metadata))
    with pytest.raises(ValueError, match="differs"):
        fetch_seqcode.capture_all(tmp_path)
    assert {name: (tmp_path / name).read_bytes() for name in names} == before


def test_seqcode_pagination_cannot_drop_its_public_name_filter(tmp_path, monkeypatch):
    page = {"response": {"status": "ok", "count": 2, "total_pages": 2, "current_page": 1,
                         "next": fetch_seqcode.BASE + "names.json?page=2"},
            "values": [{"id": 1, "name": "Public name"}]}
    calls = []

    def request(value, **_kwargs):
        calls.append(value.full_url)
        return io.BytesIO(json.dumps(page).encode())

    monkeypatch.setattr(fetch_seqcode.urllib.request, "urlopen", request)
    with pytest.raises(ValueError, match="pagination"):
        fetch_seqcode.capture(tmp_path, "names")
    assert calls == [fetch_seqcode.BASE + "names.json?status=public"]
