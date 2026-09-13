"""Replayable current BacDive v2 capture from its complete public ID export."""

from __future__ import annotations

import argparse
import csv
import datetime
import gzip
import hashlib
import http.client
import io
import json
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

CENSUS_URL = "https://bacdive.dsmz.de/advsearch/csv?pfc=1"
FETCH_URL = "https://api.bacdive.dsmz.de/v2/fetch/"


def request(url: str) -> bytes:
    for attempt in range(5):
        try:
            with urllib.request.urlopen(
                urllib.request.Request(url, headers={"User-Agent": "TaxonMech source census"}), timeout=90
            ) as response:
                return response.read()
        except (OSError, http.client.IncompleteRead):
            if attempt == 4:
                raise
            time.sleep(2**attempt)
    raise AssertionError("unreachable")


def checkpoint(directory: Path, name: str, url: str) -> tuple[bytes, dict]:
    path, sidecar = directory / (name + ".gz"), directory / (name + ".metadata.json")
    if path.exists() or sidecar.exists():
        data = gzip.decompress(path.read_bytes())
        meta = json.loads(sidecar.read_text())
        if meta["url"] != url or hashlib.sha256(data).hexdigest() != meta["sha256"]:
            raise ValueError("BacDive checkpoint differs from its source pin")
        return data, meta
    for attempt in range(4):
        data = request(url)
        try:
            if name.startswith("census-"):
                census(data)
            break
        except ValueError:
            if attempt == 3:
                raise
            time.sleep(2**attempt)
    meta = {
        "url": url,
        "path": path.name,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    path.write_bytes(gzip.compress(data, mtime=0))
    sidecar.write_text(json.dumps(meta, sort_keys=True) + "\n")
    return data, meta


def census(data: bytes) -> list[int]:
    text = data.decode("utf-8-sig")
    start = text.index("ID,species,")
    rows = list(csv.DictReader(io.StringIO(text[start:])))
    # The public export contains a completely empty row. It supplies no
    # identifier, so retain/count it as a source defect rather than invent one.
    ids = [int(row["ID"]) for row in rows if any(row.values())]
    if not ids or len(set(ids)) != len(ids) or any(i <= 0 for i in ids):
        raise ValueError("BacDive census is empty or repeats/invalidates source IDs")
    return sorted(ids)


def project_record(record: dict) -> dict:
    fields = {
        "General": ("@ref", "BacDive-ID", "NCBI tax id", "doi", "enterobase link"),
        "Name and taxonomic classification": (
            "@ref",
            "domain",
            "phylum",
            "class",
            "order",
            "family",
            "genus",
            "species",
            "full scientific name",
            "strain designation",
            "type strain",
            "LPSN",
        ),
        "Sequence information": ("Genome sequences", "16S sequences"),
        "Literature": ("@ref", "culture collection no.", "straininfo link"),
    }
    general = record.get("General", {})
    if type(general.get("BacDive-ID")) is not int or general["BacDive-ID"] <= 0:
        raise ValueError("BacDive v2 record lacks a source strain ID")
    return {
        section: {key: record[section][key] for key in keys if key in record[section]}
        for section, keys in fields.items()
        if section in record
    }


def capture(directory: Path) -> dict:
    directory.mkdir(parents=True, exist_ok=True)
    source_path = directory / "SOURCE.json"
    existing = json.loads(source_path.read_text()) if source_path.exists() else None
    data, before = checkpoint(directory, "census-before.csv", CENSUS_URL)
    ids = census(data)
    batches = [ids[pos : pos + 100] for pos in range(0, len(ids), 100)]
    print(f"BacDive v2: {len(ids)} IDs in complete public census", flush=True)

    def batch(item):
        number, wanted = item
        raw, meta = checkpoint(directory, f"records-{number:04}.json", FETCH_URL + ";".join(map(str, wanted)))
        page = json.loads(raw)
        records = page["results"]
        if not isinstance(records, dict) or page.get("next") or page["count"] != len(records):
            raise ValueError("BacDive bounded fetch has unexpected pagination/count")
        projected = {}
        for key, value in records.items():
            record = project_record(value)
            identifier = record["General"]["BacDive-ID"]
            if str(identifier) != key or identifier not in wanted:
                raise ValueError("BacDive response differs from requested IDs")
            projected[identifier] = record
        meta["requested_ids"] = wanted
        if number % 25 == 0:
            print(f"BacDive v2: batch {number + 1}/{len(batches)}", flush=True)
        return meta, projected

    records, responses = {}, [before]
    with ThreadPoolExecutor(max_workers=2) as pool:
        for meta, values in pool.map(batch, enumerate(batches)):
            if records.keys() & values.keys():
                raise ValueError("BacDive batches repeat source strain IDs")
            records.update(values)
            responses.append(meta)
    data, after = checkpoint(directory, "census-after.csv", CENSUS_URL)
    if census(data) != ids:
        raise ValueError("BacDive source census changed during capture")
    responses.append(after)
    payload = "".join(
        json.dumps(records[i], sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n"
        for i in sorted(records)
    ).encode()
    target = directory / "records.jsonl.gz"
    compressed = gzip.compress(payload, mtime=0)
    missing = sorted(set(ids) - records.keys())
    source = {
        "source": "BacDive v2",
        "format_version": 1,
        "census_count": len(ids),
        "captured_at": (existing["captured_at"] if existing else
                        datetime.datetime.now(datetime.timezone.utc).isoformat()),
        "citation": "https://doi.org/10.1093/nar/gkae959",
        "license": "CC-BY-4.0",
        "missing_api_ids": missing,
        "responses": responses,
        "records": {
            "path": target.name,
            "rows": len(records),
            "bytes": len(compressed),
            "sha256": hashlib.sha256(compressed).hexdigest(),
        },
    }
    text = gzip.decompress((directory / "census-before.csv.gz").read_bytes()).decode("utf-8-sig")
    source["empty_census_rows"] = sum(
        not any(row.values()) for row in csv.DictReader(io.StringIO(text[text.index("ID,species,") :]))
    )
    if existing is not None:
        if source != existing or not target.is_file() or target.read_bytes() != compressed:
            raise ValueError("existing BacDive snapshot differs from replayed primary responses")
    else:
        target.write_bytes(compressed)
        source_path.write_text(json.dumps(source, indent=2, sort_keys=True) + "\n")
    print(
        f"BacDive v2: {len(records)} records, {len(missing)} census IDs unavailable from the API", flush=True
    )
    return source


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    capture(args.out)


if __name__ == "__main__":
    main()
