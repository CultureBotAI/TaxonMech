"""Stream GOLD's complete identity tables into replayable compact projections."""

from __future__ import annotations

import gzip
import hashlib
import json
import posixpath
import re
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

from taxonmech.gold_genomes import _HEADERS

NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
FILENAMES = {"Organism": "organisms", "Sequencing Project": "projects", "Analysis Project": "analyses"}


def _column(reference: str) -> int:
    match = re.fullmatch(r"([A-Z]+)[1-9][0-9]*", reference)
    if not match:
        raise ValueError(f"invalid GOLD cell reference: {reference!r}")
    value = 0
    for character in match[1]:
        value = value * 26 + ord(character) - ord("A") + 1
    return value - 1


def workbook_rows(path: Path, sheet: str):
    """Read actual rows regardless of an incorrect worksheet dimension.

    Inline/shared strings and cached formula/numeric values follow the source
    workbook. No formula is evaluated, external link opened, or XML extracted.
    """
    with zipfile.ZipFile(path) as archive:
        relations = {
            item.attrib["Id"]: item.attrib["Target"]
            for item in ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        }
        sheets = ET.fromstring(archive.read("xl/workbook.xml")).find(NS + "sheets")
        target = next(
            (relations[item.attrib[REL + "id"]] for item in sheets if item.attrib["name"] == sheet), None
        )
        if target is None:
            raise ValueError(f"GOLD workbook is missing sheet {sheet!r}")
        member = target.lstrip("/") if target.startswith("/") else posixpath.normpath("xl/" + target)
        if not member.startswith("xl/worksheets/"):
            raise ValueError("GOLD worksheet relationship leaves its workbook")
        strings = []
        if "xl/sharedStrings.xml" in archive.namelist():
            with archive.open("xl/sharedStrings.xml") as handle:
                for _event, element in ET.iterparse(handle, events=("end",)):
                    if element.tag == NS + "si":
                        strings.append("".join(node.text or "" for node in element.iter(NS + "t")))
                        element.clear()
        header = positions = container = None
        with archive.open(member) as handle:
            for event, element in ET.iterparse(handle, events=("start", "end")):
                if event == "start" and element.tag == NS + "sheetData":
                    container = element
                if event != "end" or element.tag != NS + "row":
                    continue
                values = {}
                for cell in element.findall(NS + "c"):
                    column = _column(cell.attrib.get("r", ""))
                    if column in values:
                        raise ValueError("GOLD row repeats a column")
                    kind, value = cell.attrib.get("t"), cell.findtext(NS + "v", "")
                    if kind == "inlineStr":
                        value = "".join(node.text or "" for node in cell.iter(NS + "t"))
                    elif kind == "s":
                        value = strings[int(value)]
                    elif kind == "b":
                        value = "True" if value == "1" else "False"
                    values[column] = value
                if header is None:
                    header = [values.get(i, "") for i in range(max(values, default=-1) + 1)]
                    missing = set(_HEADERS[sheet]) - set(header)
                    if missing or len(header) != len(set(header)):
                        raise ValueError(f"GOLD {sheet}: missing or duplicate headers: {sorted(missing)}")
                    positions = {field: header.index(field) for field in _HEADERS[sheet]}
                elif any(values.values()):
                    if max(values) >= len(header):
                        raise ValueError(f"GOLD {sheet}: more cells than headers")
                    yield {field: values.get(index, "") for field, index in positions.items()}
                element.clear()
                if container is not None:
                    container.clear()
        if header is None:
            raise ValueError(f"GOLD {sheet}: no header")


def project(path: Path, directory: Path) -> dict:
    directory.mkdir(parents=True, exist_ok=True)
    with path.open("rb") as handle:
        _digest = hashlib.sha256()
        for _chunk in iter(lambda: handle.read(1 << 20), b""):
            _digest.update(_chunk)
        digest = _digest.hexdigest()
    outputs = {}
    for sheet, filename in FILENAMES.items():
        target = directory / (filename + ".jsonl.gz")
        count = 0
        with target.open("wb") as raw, gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as handle:
            for row in workbook_rows(path, sheet):
                handle.write(
                    (
                        json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
                    ).encode()
                )
                count += 1
        with target.open("rb") as handle:
            _digest = hashlib.sha256()
            for _chunk in iter(lambda: handle.read(1 << 20), b""):
                _digest.update(_chunk)
            output_digest = _digest.hexdigest()
        outputs[sheet] = {
            "path": target.name,
            "rows": count,
            "bytes": target.stat().st_size,
            "sha256": output_digest,
        }
        print(f"GOLD {sheet}: {count} source records", flush=True)
    source = {
        "source": "GOLD",
        "url": "https://gold.jgi.doe.gov/download?mode=site_excel",
        "workbook_sha256": digest,
        "workbook_bytes": path.stat().st_size,
        "projection": "all rows; identity, strain, taxon, project and genome columns",
        "outputs": outputs,
    }
    (directory / "SOURCE.json").write_text(json.dumps(source, indent=2, sort_keys=True) + "\n")
    return source
