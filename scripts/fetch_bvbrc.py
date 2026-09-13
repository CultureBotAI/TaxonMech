#!/usr/bin/env python3
"""Capture BV-BRC prokaryote genomes against identical before/after ID censuses."""

from __future__ import annotations

import argparse
import datetime
import gzip
import hashlib
import http.client
import json
import re
import tempfile
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from taxonmech.source_catalog import sha256, write_chunks

BASE = "https://www.bv-brc.org/api/genome/?"
FIELDS = (
    "genome_id",
    "genome_name",
    "taxon_id",
    "superkingdom",
    "strain",
    "culture_collection",
    "assembly_accession",
    "biosample_accession",
    "bioproject_accession",
    "genbank_accessions",
    "refseq_accessions",
    "genome_status",
    "type_strain",
    "reference_genome",
    "date_modified",
    "public",
    "taxon_lineage_ids",
    "taxon_lineage_names",
)
SIZE = 10_000


def request(url):
    for attempt in range(5):
        try:
            with urllib.request.urlopen(
                urllib.request.Request(
                    url, headers={"Accept": "application/json", "User-Agent": "TaxonMech source census"}
                ),
                timeout=60,
            ) as response:
                payload = response.read(40_000_001)
                if len(payload) > 40_000_000:
                    raise ValueError("BV-BRC page exceeded the bounded metadata response size")
                return payload, response.headers.get("Content-Range", "")
        except (OSError, http.client.IncompleteRead):
            if attempt == 4:
                raise
            time.sleep(2**attempt)
    raise AssertionError("unreachable")


def page(directory, stage, offset, fields):
    query = "in(superkingdom,(Bacteria,Archaea))&eq(public,true)&sort(+genome_id)&select(" + ",".join(fields)
    url = BASE + urllib.parse.quote(query + f")&limit({SIZE},{offset})", safe="(),=&")
    path = directory / "responses" / f"{stage}-{offset:08}.json.gz"
    sidecar = path.with_suffix(".metadata.json")
    if path.exists() or sidecar.exists():
        metadata = json.loads(sidecar.read_text())
        payload = gzip.decompress(path.read_bytes())
        if metadata["url"] != url or metadata["sha256"] != hashlib.sha256(payload).hexdigest():
            raise ValueError("BV-BRC cached request differs from its source pin")
    else:
        payload, content_range = request(url)
        metadata = {
            "url": url,
            "path": str(path.relative_to(directory)),
            "content_range": content_range,
            "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest(),
            "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(gzip.compress(payload, mtime=0))
        sidecar.write_text(json.dumps(metadata, sort_keys=True) + "\n")
    match = re.fullmatch(r"items ([0-9]+)-([0-9]+)/([0-9]+)", metadata["content_range"])
    records = json.loads(payload)
    if (
        not match
        or not isinstance(records, list)
        or int(match[1]) != offset
        or int(match[2]) - offset != len(records)
        or len(records) != min(SIZE, int(match[3]) - offset)
    ):
        raise ValueError("BV-BRC page size/range differs from its declared census")
    ids = [row.get("genome_id") for row in records]
    if any(
        not isinstance(value, str) or not re.fullmatch(r"[0-9]+\.[0-9]+", value) for value in ids
    ) or ids != sorted(set(ids)):
        raise ValueError("BV-BRC page has invalid, unsorted or duplicate genome IDs")
    if offset % 100_000 == 0:
        print(f"BV-BRC {stage}: {offset + len(records)}/{match[3]}", flush=True)
    return records, metadata, int(match[3])


def stage(directory, name, fields):
    first, metadata, count = page(directory, name, 0, fields)
    yield first, metadata
    with ThreadPoolExecutor(max_workers=2) as pool:
        for records, metadata, total in pool.map(
            lambda offset: page(directory, name, offset, fields), range(SIZE, count, SIZE)
        ):
            if total != count:
                raise ValueError("BV-BRC census changed during pagination")
            yield records, metadata


def capture(directory):
    directory.mkdir(parents=True, exist_ok=True)
    source_path = directory / "SOURCE.json"
    existing = json.loads(source_path.read_text()) if source_path.exists() else None
    with tempfile.TemporaryDirectory(prefix=".projection-", dir=directory) as temporary:
        return _capture(directory, Path(temporary), existing)


def _capture(directory, work, existing):
    responses = []

    def census(name):
        ids = []
        for rows, metadata in stage(directory, name, ("genome_id",)):
            ids.extend(row["genome_id"] for row in rows)
            responses.append(metadata)
        if ids != sorted(set(ids)):
            raise ValueError("BV-BRC ID census repeats IDs or changed ordering")
        return ids

    before = census("ids-before")
    observed = []

    def rich():
        for rows, metadata in stage(directory, "records", FIELDS):
            responses.append(metadata)
            for row in rows:
                if row.get("superkingdom") not in {"Bacteria", "Archaea"} or row.get("public") is not True:
                    raise ValueError("BV-BRC response left the public prokaryote filter")
                observed.append(row["genome_id"])
                yield row

    outputs = write_chunks(work, "bvbrc", rich())
    after = census("ids-after")
    if before != observed or before != after:
        raise ValueError("BV-BRC rich records disagree with the complete before/after census")
    source = {
        "source": "BV-BRC",
        "format_version": 1,
        "url": BASE[:-1],
        "captured_at": (existing["captured_at"] if existing else
                        datetime.datetime.now(datetime.timezone.utc).isoformat()),
        "census_count": len(before),
        "fields": list(FIELDS),
        "responses": responses,
        "files": outputs,
        "census_sha256": hashlib.sha256("\n".join(before).encode()).hexdigest(),
    }
    if existing is not None:
        if source != existing or any(
            not (directory / item["path"]).is_file()
            or sha256(directory / item["path"]) != item["sha256"] for item in outputs
        ):
            raise ValueError("existing BV-BRC snapshot differs from replayed primary responses")
    else:
        for item in outputs:
            (work / item["path"]).replace(directory / item["path"])
        (directory / "SOURCE.json").write_text(json.dumps(source, indent=2, sort_keys=True) + "\n")
    print(f"BV-BRC: {len(before)} public prokaryote genomes; census verified before and after", flush=True)
    return source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path)
    capture(parser.parse_args().out)
