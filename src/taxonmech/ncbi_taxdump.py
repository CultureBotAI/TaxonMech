"""Read the complete primary NCBI taxonomy without a KGX selection filter.

Parents, ranks and names are source assertions. Merged IDs are retained as
redirect evidence, never silently used to rewrite another source's assertion.
Archive members are streamed, not extracted to source-controlled paths.
"""

from __future__ import annotations

import hashlib
import tarfile
from collections import defaultdict
from collections.abc import Iterator
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / "conf/ncbi_taxdump.yaml"


def settings(path: Path = CONFIG) -> dict:
    value = yaml.safe_load(path.read_text())
    if not isinstance(value, dict) or set(value) != {"snapshot", "path", "url", "sha256", "license"}:
        raise ValueError("NCBI taxdump configuration must pin its snapshot, path, URL, SHA256 and license")
    if len(value["sha256"]) != 64 or any(c not in "0123456789abcdef" for c in value["sha256"]):
        raise ValueError("invalid NCBI taxdump SHA256")
    return value


def fields(handle, member: str) -> Iterator[list[str]]:
    for number, line in enumerate(handle, 1):
        text = line.decode("utf-8")
        if not text.endswith("\t|\n"):
            raise ValueError(f"{member}:{number}: invalid NCBI field terminator")
        yield text[:-3].split("\t|\t")


def load_taxdump(
    path: Path, *, expected_sha256: str | None = None
) -> tuple[dict, dict, dict, dict, dict, list]:
    """Return nodes, parents, ranks, synonyms, redirects and type-material rows.

    Keep the entire backbone while extracting, including non-prokaryotic
    ancestors needed by existing records. Record selection happens separately.
    NCBI's other name classes remain related names, not inferred equivalents.
    """
    if expected_sha256:
        with path.open("rb") as handle:
            _digest = hashlib.sha256()
            for _chunk in iter(lambda: handle.read(1 << 20), b""):
                _digest.update(_chunk)
            digest = _digest.hexdigest()
        if digest != expected_sha256:
            raise ValueError("NCBI taxonomy snapshot differs from its configured SHA256")
    nodes, parents, ranks, redirects = {}, {}, {}, {}
    synonyms = defaultdict(lambda: defaultdict(list))
    material = []
    wanted = {"nodes.dmp", "names.dmp", "merged.dmp", "typematerial.dmp", "excludedfromtype.dmp"}
    seen = set()
    with tarfile.open(path, "r|gz") as archive:
        for member in archive:
            if member.name not in wanted:
                continue
            if member.name in seen or not member.isfile():
                raise ValueError(f"duplicate or non-file NCBI archive member: {member.name}")
            seen.add(member.name)
            for row in fields(archive.extractfile(member), member.name):
                tid = "NCBITaxon:" + row[0]
                if not row[0].isdigit() or int(row[0]) <= 0:
                    raise ValueError("invalid NCBI taxon ID")
                if member.name == "nodes.dmp":
                    if len(row) < 13 or tid in ranks or not row[1].isdigit():
                        raise ValueError(f"invalid or duplicate NCBI node: {tid}")
                    ranks[tid] = row[2].upper().replace(" ", "_")
                    if row[0] != row[1]:
                        parents[tid] = "NCBITaxon:" + row[1]
                    elif row[0] != "1":
                        raise ValueError(f"non-root NCBI node is its own parent: {tid}")
                    nodes.setdefault(tid, {})["genetic_code"] = row[6] if row[6] != "0" else ""
                elif member.name == "names.dmp":
                    if len(row) != 4:
                        raise ValueError("invalid NCBI name row")
                    if row[3] == "scientific name":
                        node = nodes.setdefault(tid, {})
                        if "label" in node:
                            raise ValueError(f"duplicate NCBI scientific name: {tid}")
                        node["label"] = row[1]
                    else:
                        scope = (
                            "EXACT_SYNONYM" if row[3] in {"synonym", "equivalent name"} else "RELATED_SYNONYM"
                        )
                        synonyms[tid][scope].append(row[1])
                elif member.name == "merged.dmp":
                    if len(row) != 2 or not row[1].isdigit() or tid in redirects:
                        raise ValueError("invalid NCBI merged-ID row")
                    redirects[tid] = "NCBITaxon:" + row[1]
                else:
                    if len(row) != 4:
                        raise ValueError("invalid NCBI type-material row")
                    material.append(
                        {
                            "taxon_id": tid,
                            "taxon_name": row[1],
                            "type": row[2],
                            "designation": row[3],
                            "source_field": member.name,
                        }
                    )
    if seen != wanted:
        raise ValueError(f"NCBI taxdump lacks required members: {sorted(wanted - seen)}")
    if set(nodes) != set(ranks) or any(not node.get("label") for node in nodes.values()):
        raise ValueError("NCBI nodes and scientific names do not cover the same IDs")
    if set(parents.values()) - nodes.keys():
        raise ValueError("NCBI taxonomy contains unknown parents")
    # Also validates every parent path for cycles before any inventory writes.
    prokaryote_taxa(parents, nodes)
    return nodes, parents, ranks, synonyms, redirects, material


def prokaryote_taxa(parents: dict[str, str], nodes: dict) -> set[str]:
    """All descendants of the two NCBI domain roots, without name heuristics."""
    if "NCBITaxon:1" not in nodes or "NCBITaxon:1" in parents:
        raise ValueError("NCBI taxonomy must have a parentless NCBITaxon:1 root")
    roots = {"NCBITaxon:2", "NCBITaxon:2157"}
    domain = {"NCBITaxon:1": False}
    result = set()
    for tid in nodes:
        path, seen, current = [], set(), tid
        while current not in domain:
            if current in seen or current not in nodes or current not in parents:
                raise ValueError(f"NCBI taxonomy has a cycle or incomplete parent chain at {current}")
            seen.add(current)
            path.append(current)
            current = parents[current]
        inherited = domain[current]
        for item in reversed(path):
            inherited = inherited or item in roots
            domain[item] = inherited
        if domain[tid]:
            result.add(tid)
    return result
