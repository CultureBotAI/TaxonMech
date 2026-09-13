#!/usr/bin/env python3
"""Capture all public SeqCode names and validly published type genomes.

The two endpoints have different scopes. Names are a discovery census, not
a nomenclatural-validity claim; type-genomes retains its own source statuses.
No source name is equated with an NCBI taxon by its spelling.
"""

from __future__ import annotations

import argparse
import datetime
import gzip
import hashlib
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://api.seqco.de/v1/"


def capture(directory: Path, endpoint: str) -> dict:
    if endpoint not in {"names", "type-genomes"}:
        raise ValueError("unsupported SeqCode capture endpoint")
    directory.mkdir(parents=True, exist_ok=True)
    source_path = directory / "SOURCE.json"
    existing = json.loads(source_path.read_text())["outputs"][endpoint] if source_path.exists() else None
    url = BASE + endpoint + ".json" + ("?status=public" if endpoint == "names" else "")
    records, responses, visited = {}, [], set()
    expected_count = expected_pages = None
    number = 0
    while url:
        parsed = urllib.parse.urlsplit(url)
        if (
            url in visited
            or parsed.scheme != "https"
            or parsed.netloc != "api.seqco.de"
            or parsed.path != f"/v1/{endpoint}.json"
            or (endpoint == "names" and urllib.parse.parse_qs(parsed.query).get("status") != ["public"])
        ):
            raise ValueError("SeqCode pagination repeats a page or leaves its endpoint")
        visited.add(url)
        number += 1
        path = directory / f"{endpoint}-{number:04}.json.gz"
        metadata_path = path.with_suffix(path.suffix + ".metadata.json")
        if path.exists() and metadata_path.exists():
            metadata = json.loads(metadata_path.read_text())
            data = gzip.decompress(path.read_bytes())
            if metadata["url"] != url or hashlib.sha256(data).hexdigest() != metadata["sha256"]:
                raise ValueError("cached SeqCode response differs from its request/hash")
        else:
            for attempt in range(4):
                try:
                    with urllib.request.urlopen(
                        urllib.request.Request(
                            url,
                            headers={"User-Agent": "TaxonMech source census", "Accept": "application/json"},
                        ),
                        timeout=60,
                    ) as response:
                        data = response.read()
                    break
                except (OSError, urllib.error.URLError):
                    if attempt == 3:
                        raise
                    time.sleep(2**attempt)
            metadata = {
                "url": url,
                "sha256": hashlib.sha256(data).hexdigest(),
                "bytes": len(data),
                "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            }
            path.write_bytes(gzip.compress(data, mtime=0))
            metadata_path.write_text(json.dumps(metadata, sort_keys=True) + "\n")
        page = json.loads(data)
        status, values = page["response"], page["values"]
        if number == 1:
            expected_count, expected_pages = status["count"], status["total_pages"]
        if (
            status["status"] != "ok"
            or status["current_page"] != number
            or status["count"] != expected_count
            or status["total_pages"] != expected_pages
            or not isinstance(values, list)
            or not values
        ):
            raise ValueError("SeqCode pagination/count changed during capture")
        for record in values:
            identifier = record.get("id")
            if type(identifier) is not int or identifier <= 0 or identifier in records:
                raise ValueError("SeqCode response has duplicate/invalid name IDs")
            records[identifier] = record
        responses.append({"path": path.name, **metadata})
        url = status.get("next")
        if number % 25 == 1:
            print(f"SeqCode {endpoint}: page {number}/{expected_pages}", flush=True)
    if number != expected_pages or len(records) != expected_count:
        raise ValueError("SeqCode capture did not cover every page/record")
    payload = "".join(
        json.dumps(records[key], sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n"
        for key in sorted(records)
    ).encode()
    target = directory / f"{endpoint}.jsonl.gz"
    compressed = gzip.compress(payload, mtime=0)
    result = {
        "rows": len(records),
        "path": target.name,
        "sha256": hashlib.sha256(compressed).hexdigest(),
        "responses": responses,
    }
    if existing is not None:
        if result != existing or not target.is_file() or target.read_bytes() != compressed:
            raise ValueError("existing SeqCode snapshot differs from replayed primary responses")
    else:
        target.write_bytes(compressed)
    return result


def capture_all(directory: Path) -> dict:
    source_path = directory / "SOURCE.json"
    existing = json.loads(source_path.read_text()) if source_path.exists() else None
    outputs = {endpoint: capture(directory, endpoint) for endpoint in ("names", "type-genomes")}
    source = {
        "source": "SeqCode Registry",
        "api": BASE,
        "captured_at": (existing["captured_at"] if existing else
                        datetime.datetime.now(datetime.timezone.utc).isoformat()),
        "outputs": outputs,
    }
    if existing is not None:
        if source != existing:
            raise ValueError("existing SeqCode snapshot differs from replayed primary responses")
    else:
        source_path.write_text(json.dumps(source, indent=2, sort_keys=True) + "\n")
    print({key: value["rows"] for key, value in outputs.items()})
    return source


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    capture_all(args.out)


if __name__ == "__main__":
    main()
