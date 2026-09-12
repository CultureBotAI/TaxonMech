"""Capture and replay complete, pinned StrainInfo discovery and detail responses."""

from __future__ import annotations

import argparse
import datetime
import gzip
import hashlib
import io
import json
import os
import re
import tempfile
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path, PurePosixPath

import yaml

from taxonmech.genome_sources import CAFI_REGISTRY_PATH, normalize_culture_identifier
from taxonmech.straininfo import INPUT_PATHS, ROOT, input_provenance, read_rows, source_metadata
from taxonmech.straininfo_links import candidate_ids, encoded, nonempty, objects, positive_id, project_record

API_BASE = "https://api.straininfo.dsmz.de"
API_SCHEMA = "https://straininfo.dsmz.de/api/v2/strinf_ex.yaml"
API_VERSION = "2.1.0"
SHA = re.compile(r"[0-9a-f]{64}")


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _utc(value: str | None = None) -> str:
    moment = (datetime.datetime.now(datetime.timezone.utc) if value is None else
              datetime.datetime.fromisoformat(value.replace("Z", "+00:00")))
    if moment.tzinfo is None or moment.utcoffset() != datetime.timedelta(0):
        raise ValueError("StrainInfo response timestamps must include UTC timezone")
    return moment.strftime("%Y-%m-%dT%H:%M:%SZ")


def _json_bytes(value: object) -> bytes:
    return (encoded(value) + "\n").encode("utf-8")


def _path(directory: Path, name: str) -> Path:
    if (not isinstance(name, str) or not name or PurePosixPath(name).is_absolute()
            or ".." in PurePosixPath(name).parts or "\\" in name):
        raise ValueError("Invalid relative StrainInfo response path")
    path = directory / name
    if not path.resolve().is_relative_to(directory.resolve()):
        raise ValueError("StrainInfo response path leaves its snapshot directory")
    return path


def _new_file(path: Path, data: bytes) -> None:
    """Install a new file, or verify an identical existing file, without replacement."""
    if path.exists() or path.is_symlink():
        if not path.is_file() or path.read_bytes() != data:
            raise ValueError(f"Refusing to replace different StrainInfo source file: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".straininfo-", delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(data)
    try:
        # A hard link fails if another capture installed this destination meanwhile.
        os.link(temporary, path)
    except FileExistsError:
        if path.read_bytes() != data:
            raise ValueError(f"Concurrent StrainInfo capture changed {path}") from None
    finally:
        temporary.unlink(missing_ok=True)


def store_response(directory: Path, *, kind: str, path: str, url: str, data: bytes,
                   retrieved_at: str, headers: dict | None = None,
                   requested_ids: list[int] | None = None) -> dict:
    """Retain original response bytes and their honest HTTP retrieval provenance.

    This also supports importing already acquired, checksum-verified responses
    into a maintained snapshot without repeating public requests.
    """
    _utc(retrieved_at)
    if not data or kind not in {"ids", "search", "records", "status", "schema"}:
        raise ValueError("StrainInfo response has an unsupported kind or empty body")
    if not path.startswith("responses/") or not path.endswith(".json.gz"):
        raise ValueError("StrainInfo responses must use gzip paths inside responses/")
    target = _path(directory, path)
    packed = gzip.compress(data, mtime=0)
    metadata = {"kind": kind, "path": path, "url": url, "bytes": len(data), "sha256": _sha(data),
                "compressed_bytes": len(packed), "compressed_sha256": _sha(packed),
                "retrieved_at": retrieved_at}
    if headers is not None:
        metadata["headers"] = headers
    if requested_ids is not None:
        metadata["requested_ids"] = requested_ids
    sidecar = target.with_name(target.name + ".metadata.json")
    if target.exists() or sidecar.exists():
        if not target.exists() or not sidecar.exists():
            raise ValueError(f"Incomplete StrainInfo response checkpoint: {target}")
        existing = json.loads(sidecar.read_text())
        if load_response(directory, existing) != data or any(
                existing.get(key) != metadata.get(key) for key in ("kind", "path", "url", "requested_ids")):
            raise ValueError(f"Different StrainInfo response checkpoint: {target}")
        return existing
    _new_file(target, packed)
    _new_file(sidecar, _json_bytes(metadata))
    return metadata


def load_response(directory: Path, metadata: dict) -> bytes:
    if (not isinstance(metadata, dict)
            or metadata.get("kind") not in {"ids", "search", "records", "status", "schema"}
            or not isinstance(metadata.get("url"), str)
            or type(metadata.get("bytes")) is not int or metadata["bytes"] <= 0
            or not isinstance(metadata.get("sha256"), str) or not SHA.fullmatch(metadata["sha256"])
            or type(metadata.get("compressed_bytes")) is not int or metadata["compressed_bytes"] <= 0
            or not isinstance(metadata.get("compressed_sha256"), str)
            or not SHA.fullmatch(metadata["compressed_sha256"])
            or not isinstance(metadata.get("retrieved_at"), str)):
        raise ValueError("Malformed StrainInfo response metadata")
    _utc(metadata["retrieved_at"])
    path = metadata.get("path")
    if not isinstance(path, str) or not path.startswith("responses/") or not path.endswith(".json.gz"):
        raise ValueError("Invalid StrainInfo response filename")
    packed = _path(directory, path).read_bytes()
    if len(packed) != metadata["compressed_bytes"] or _sha(packed) != metadata["compressed_sha256"]:
        raise ValueError(f"StrainInfo compressed response checksum differs: {path}")
    try:
        data = gzip.decompress(packed)
    except (OSError, EOFError) as exc:
        raise ValueError(f"Invalid StrainInfo gzip response: {path}") from exc
    if len(data) != metadata["bytes"] or _sha(data) != metadata["sha256"]:
        raise ValueError(f"StrainInfo original response checksum differs: {path}")
    return data


def _ids(value: object) -> list[int]:
    if not isinstance(value, list) or not value:
        raise ValueError("StrainInfo census must be a nonempty list")
    ids = [positive_id(item, "census ID") for item in value]
    if len(ids) != len(set(ids)):
        raise ValueError("StrainInfo census contains duplicate IDs")
    return ids


def _inputs(root: Path) -> tuple[list[dict], list[dict]]:
    before = input_provenance(root)
    if before[1]["sha256"] != _sha(CAFI_REGISTRY_PATH.read_bytes()):
        raise ValueError("StrainInfo candidate registry differs from the loaded CAFI authority snapshot")
    strains = read_rows(root / INPUT_PATHS[0], required=("strain_id", "bacdive_id", "culture_collection_ids"),
                        nonempty=True)
    if input_provenance(root) != before:
        raise ValueError("StrainInfo selection inputs changed while reading")
    return before, strains


def _catalog(directory: Path, responses: list[dict]) -> tuple[list[int], list[list]]:
    census = [r for r in responses if r.get("kind") == "ids"]
    if len(census) != 1 or census[0]["url"] != API_BASE + "/service/all/strains":
        raise ValueError("StrainInfo capture requires exactly one complete strain census")
    ids = _ids(json.loads(load_response(directory, census[0])))
    pages = {}
    for response in responses:
        if response.get("kind") != "search":
            continue
        match = re.fullmatch(re.escape(API_BASE) + r"/service/search/strain/all/([0-9]+)", response["url"])
        if not match or int(match[1]) in pages:
            raise ValueError("StrainInfo search page URLs are malformed or duplicated")
        pages[int(match[1])] = json.loads(load_response(directory, response))
    rows, visited, index = [], set(), 0
    while True:
        if index not in pages or index in visited:
            raise ValueError("StrainInfo search pagination is missing a page or repeats one")
        visited.add(index)
        page = pages[index]
        if (not isinstance(page, dict) or type(page.get("count")) is not int or page["count"] != len(ids)
                or not isinstance(page.get("data"), list) or not page["data"]):
            raise ValueError("StrainInfo search page count or data is malformed")
        rows.extend(page["data"])
        if "next" not in page:
            break
        index = positive_id(page["next"], "search next page")
    if visited != set(pages):
        raise ValueError("StrainInfo capture contains unreachable search pages")
    if (any(not isinstance(r, list) or len(r) != 6 for r in rows)
            or len(rows) != len(ids) or {r[0] for r in rows} != set(ids)):
        raise ValueError("StrainInfo search rows disagree with the complete census")
    return ids, rows


def _boundaries(directory: Path, plan: dict, ids: list[int]) -> None:
    checks = plan.get("checks")
    if not isinstance(checks, list) or len(checks) != 3:
        raise ValueError("StrainInfo capture requires API before/after and census-after checks")
    before, after, final_ids = checks
    if (before.get("kind") != "status" or after.get("kind") != "status"
            or before.get("url") != API_BASE + "/" or after.get("url") != API_BASE + "/"
            or final_ids.get("kind") != "ids" or final_ids.get("url") != API_BASE + "/service/all/strains"):
        raise ValueError("StrainInfo capture boundary endpoints differ from the primary source")
    a, b = [json.loads(load_response(directory, m)) for m in (before, after)]
    if (not isinstance(a, dict) or a != b or not isinstance(a.get("version"), str) or not a["version"]
            or a.get("private") is not False or not isinstance(a.get("maintenance"), dict)
            or a["maintenance"].get("status") is not False):
        raise ValueError("StrainInfo API changed or was unavailable during capture")
    if _ids(json.loads(load_response(directory, final_ids))) != ids:
        raise ValueError("StrainInfo complete census changed during capture")
    schema = plan.get("api_schema")
    if not isinstance(schema, dict) or schema.get("kind") != "schema" or schema.get("url") != API_SCHEMA:
        raise ValueError("StrainInfo capture requires its primary OpenAPI specification")
    api = yaml.safe_load(load_response(directory, schema))
    info = api.get("info") if isinstance(api, dict) else None
    license_info = info.get("license") if isinstance(info, dict) else None
    if (not isinstance(info, dict) or info.get("version") != API_VERSION
            or not isinstance(license_info, dict) or license_info.get("name") != "CC BY 4.0"
            or license_info.get("url") != "https://creativecommons.org/licenses/by/4.0/"):
        raise ValueError("StrainInfo API specification or data license changed")


def finalize(directory: Path, *, root: Path = ROOT) -> dict:
    """Verify every original response and atomically finish an offline snapshot."""
    before, strains = _inputs(root)
    plan_path = directory / "CAPTURE.json"
    plan_data = plan_path.read_bytes()
    plan = json.loads(plan_data)
    if not isinstance(plan, dict) or plan.get("inputs") != before:
        raise ValueError("StrainInfo capture used different candidate-selection inputs")
    stamp = _utc(nonempty(plan.get("captured_at"), "capture timestamp"))
    responses = objects(plan.get("responses"), "capture responses")
    if any(r.get("kind") not in {"ids", "search", "records"} for r in responses):
        raise ValueError("StrainInfo capture contains an unsupported response kind")
    if len({r.get("url") for r in responses}) != len(responses):
        raise ValueError("StrainInfo capture contains duplicate request URLs")
    ids, rows = _catalog(directory, responses)
    selected = candidate_ids(rows, strains)
    if not selected:
        raise ValueError("StrainInfo capture has no exact culture-identifier candidates")
    search = {row[0]: {normalize_culture_identifier(des) for des in row[1]} for row in rows}
    _boundaries(directory, plan, ids)
    projected = {}
    for response in responses:
        if response["kind"] != "records":
            continue
        requested = _ids(response.get("requested_ids"))
        expected_url = API_BASE + "/v2/data/strain/max/" + ",".join(map(str, requested))
        if len(requested) > 100 or response["url"] != expected_url:
            raise ValueError("StrainInfo rich response URL disagrees with its bounded requested IDs")
        records = objects(json.loads(load_response(directory, response)), "rich records")
        returned = []
        for record in records:
            projection = project_record(record)
            si_id = projection["strain"]["siID"]
            returned.append(si_id)
            if si_id in projected or si_id not in search:
                raise ValueError("StrainInfo rich responses repeat an ID or leave the census")
            for deposit in projection["deposits"]:
                designation = nonempty(deposit.get("designation"), "own deposit designation")
                key = normalize_culture_identifier(designation)
                if key and key not in search[si_id]:
                    raise ValueError("StrainInfo rich deposit was missing from its discovery index")
            projected[si_id] = encoded(projection)
        if len(returned) != len(requested) or set(returned) != set(requested):
            raise ValueError("StrainInfo rich response IDs differ from their request")
    if set(projected) != set(selected):
        raise ValueError("StrainInfo rich responses omit candidates or contain unselected records")
    descriptors = responses + plan["checks"] + [plan["api_schema"]]
    if len({m["path"] for m in descriptors}) != len(descriptors):
        raise ValueError("StrainInfo response descriptors reuse a source path")
    with tempfile.TemporaryDirectory(prefix=".straininfo-finalize-", dir=directory) as temporary:
        records_path = Path(temporary) / "records.jsonl.gz"
        with (records_path.open("wb") as raw,
              gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as zipped,
              io.TextIOWrapper(zipped, encoding="utf-8", newline="\n") as handle):
            for si_id in sorted(projected):
                handle.write(projected[si_id] + "\n")
        records_data = records_path.read_bytes()
        source = {"format_version": 1, "captured_at": stamp, "api_version": API_VERSION,
                  "api_base": API_BASE, "license": "CC-BY-4.0", "catalog_count": len(ids),
                  "candidate_count": len(selected), "inputs": before,
                  "records": {"path": "records.jsonl.gz", "bytes": len(records_data),
                              "sha256": _sha(records_data), "rows": len(projected)},
                  "responses": responses, "checks": plan["checks"], "api_schema": plan["api_schema"]}
        source_data = _json_bytes(source)
        temp_source = Path(temporary) / "SNAPSHOT.json"
        temp_source.write_bytes(source_data)
        source_metadata(temp_source)
        # Recheck compact source bytes and input pins after processing all records.
        for metadata in descriptors:
            if _sha(_path(directory, metadata["path"]).read_bytes()) != metadata["compressed_sha256"]:
                raise ValueError("StrainInfo original responses changed during finalization")
        if input_provenance(root) != before or plan_path.read_bytes() != plan_data:
            raise ValueError("StrainInfo source or selection inputs changed during finalization")
        targets = [(directory / "records.jsonl.gz", records_data), (directory / "SNAPSHOT.json", source_data)]
        for path, data in targets:
            if (path.exists() or path.is_symlink()) and (not path.is_file() or path.read_bytes() != data):
                raise ValueError(f"Refusing to replace a different StrainInfo snapshot: {path}")
        installed = []
        try:
            for path, data in targets:
                existed = path.exists()
                _new_file(path, data)
                if not existed:
                    installed.append(path)
        except BaseException:
            for path in installed:
                path.unlink(missing_ok=True)
            raise
    return source


def _request(url: str) -> tuple[bytes, str, dict]:
    for attempt in range(4):
        try:
            stamp = _utc()
            request = urllib.request.Request(
                url, headers={"User-Agent": "TaxonMech StrainInfo snapshot capture"})
            with urllib.request.urlopen(request, timeout=45) as response:
                if response.url != url:
                    raise ValueError("StrainInfo primary endpoint redirected unexpectedly")
                return response.read(), stamp, dict(response.headers)
        except OSError:
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)
    raise AssertionError("unreachable")


def _response(directory: Path, *, kind: str, name: str, url: str,
              requested_ids: list[int] | None = None) -> dict:
    relative = f"responses/{name}.json.gz"
    path = _path(directory, relative)
    sidecar = path.with_name(path.name + ".metadata.json")
    if sidecar.exists() or path.exists():
        if not sidecar.exists() or not path.exists():
            raise ValueError(f"Incomplete StrainInfo response checkpoint: {path}")
        metadata = json.loads(sidecar.read_text())
        if (metadata.get("kind") != kind or metadata.get("url") != url
                or metadata.get("path") != relative or metadata.get("requested_ids") != requested_ids):
            raise ValueError("StrainInfo cached request differs from the current request")
        load_response(directory, metadata)
        return metadata
    data, stamp, headers = _request(url)
    return store_response(directory, kind=kind, path=relative, url=url, data=data,
                          retrieved_at=stamp, headers=headers, requested_ids=requested_ids)


def capture(directory: Path, *, root: Path = ROOT, workers: int = 2) -> dict:
    """Capture public responses with at most two workers and resumable checkpoints."""
    if type(workers) is not int or not 1 <= workers <= 2:
        raise ValueError("StrainInfo capture permits one or two workers")
    before, strains = _inputs(root)
    if any((root / name).resolve().is_relative_to(directory.resolve()) for name in INPUT_PATHS):
        raise ValueError("StrainInfo snapshot directory cannot contain its selection inputs")
    if (directory / "SNAPSHOT.json").exists() or (directory / "CAPTURE.json").exists():
        return finalize(directory, root=root)
    directory.mkdir(parents=True, exist_ok=True)
    _new_file(directory / "SELECTION.json", _json_bytes({"inputs": before}))
    status_before = _response(directory, kind="status", name="api-before", url=API_BASE + "/")
    schema = _response(directory, kind="schema", name="openapi", url=API_SCHEMA)
    census = _response(directory, kind="ids", name="ids-before", url=API_BASE + "/service/all/strains")
    responses, index, visited = [census], 0, set()
    while True:
        if index in visited:
            raise ValueError("StrainInfo live search pagination repeats a page")
        visited.add(index)
        response = _response(directory, kind="search", name=f"search-{index:04}",
                             url=API_BASE + f"/service/search/strain/all/{index}")
        responses.append(response)
        page = json.loads(load_response(directory, response))
        if not isinstance(page, dict):
            raise ValueError("StrainInfo search response must be an object")
        if "next" not in page:
            break
        index = positive_id(page["next"], "search next page")
    _, rows = _catalog(directory, responses)
    selected = candidate_ids(rows, strains)
    batches = [selected[pos:pos + 100] for pos in range(0, len(selected), 100)]

    def fetch_batch(item: tuple[int, list[int]]) -> dict:
        number, ids = item
        return _response(directory, kind="records", name=f"records-{number:04}", requested_ids=ids,
                         url=API_BASE + "/v2/data/strain/max/" + ",".join(map(str, ids)))

    with ThreadPoolExecutor(max_workers=workers) as pool:
        responses.extend(pool.map(fetch_batch, enumerate(batches)))
    status_after = _response(directory, kind="status", name="api-after", url=API_BASE + "/")
    ids_after = _response(directory, kind="ids", name="ids-after", url=API_BASE + "/service/all/strains")
    if input_provenance(root) != before:
        raise ValueError("StrainInfo selection inputs changed during capture")
    plan = {"captured_at": _utc(), "inputs": before, "responses": responses,
            "checks": [status_before, status_after, ids_after], "api_schema": schema}
    _new_file(directory / "CAPTURE.json", _json_bytes(plan))
    return finalize(directory, root=root)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path, help="new ignored source snapshot directory")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--workers", type=int, choices=(1, 2), default=2)
    parser.add_argument("--finalize-only", action="store_true",
                        help="verify retained responses without network access")
    args = parser.parse_args(argv)
    try:
        source = finalize(args.out, root=args.root) if args.finalize_only else capture(
            args.out, root=args.root, workers=args.workers)
    except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
        parser.exit(1, f"StrainInfo capture failed: {exc}\n")
    print(encoded({"snapshot": str(args.out / "SNAPSHOT.json"),
                   "sha256": _sha((args.out / "SNAPSHOT.json").read_bytes()),
                   "catalog_count": source["catalog_count"], "candidate_count": source["candidate_count"],
                   "records": source["records"]}))
    return 0
