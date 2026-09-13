"""Primary NCBI assembly assertions through explicit registered culture IDs."""

from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

import yaml

from taxonmech.genome_sources import index_culture_identifiers, normalize_culture_identifier

ASSEMBLY = re.compile(r"GC[AF]_[0-9]{9}\.[1-9][0-9]*")
SAMPLE = re.compile(r"SAM[NED][A-Z]?[0-9]+")
PROJECT = re.compile(r"PRJ(?:NA|EA|EB|DA|DB)[0-9]+")


def settings(config: Path, root: Path) -> dict:
    value = yaml.safe_load(config.read_text())
    names = {"genbank", "refseq", "genbank_historical", "refseq_historical"}
    if (
        not isinstance(value, dict)
        or not value.get("snapshot")
        or not value.get("license")
        or {item["name"] for item in value.get("sources", [])} != names
        or len(value["sources"]) != len(names)
    ):
        raise ValueError("NCBI assembly configuration must pin all four source inventories")
    for item in value["sources"]:
        path = root / item["path"]
        if Path(item["path"]).is_absolute() or ".." in Path(item["path"]).parts:
            raise ValueError("NCBI assembly input path must stay in the repository")
        with path.open("rb") as handle:
            _digest = hashlib.sha256()
            for _chunk in iter(lambda: handle.read(1 << 20), b""):
                _digest.update(_chunk)
            digest = _digest.hexdigest()
        if path.stat().st_size != item["bytes"] or digest != item["sha256"]:
            raise ValueError(f"NCBI assembly source differs from its pin: {item['name']}")
    return value


def read_summary(path: Path):
    with path.open(encoding="utf-8", newline="") as handle:
        for line in handle:
            if line.lstrip("# ").startswith("assembly_accession\t"):
                header = line.lstrip("# ").rstrip("\r\n").split("\t")
                break
        else:
            raise ValueError(f"{path}: NCBI assembly header missing")
        required = {
            "assembly_accession",
            "taxid",
            "species_taxid",
            "organism_name",
            "infraspecific_name",
            "biosample",
            "bioproject",
            "version_status",
            "assembly_level",
            "asm_name",
        }
        if required - set(header) or len(header) != len(set(header)):
            raise ValueError(f"{path}: incomplete or duplicated NCBI assembly columns")
        for row in csv.DictReader(handle, fieldnames=header, delimiter="\t"):
            if None in row or None in row.values() or not ASSEMBLY.fullmatch(row["assembly_accession"]):
                raise ValueError(f"{path}: malformed NCBI assembly row")
            yield row


def strain_tokens(value: str) -> list[str]:
    """Only source-labeled strain tags; cultivar/breed/ecotype never join."""
    return [item.removeprefix("strain=") for item in value.split(", /") if item.startswith("strain=")]


def extract_links(paths: list[Path], strains: list[dict], prokaryotes: set[str]) -> tuple[list, list, list]:
    from taxonmech.extract import ASSEMBLY_FIELDS, RELATED_RECORD_FIELDS

    deposits = index_culture_identifiers(strains)
    assemblies, related, exclusions = {}, {}, []
    for path in paths:
        for row in read_summary(path):
            tid = "NCBITaxon:" + row["taxid"]
            # Historical versions remain in their native catalog, without
            # being asserted as currently available strain assemblies.
            if tid not in prokaryotes or row["version_status"] != "latest":
                continue
            matches = set()
            for token in strain_tokens(row["infraspecific_name"]):
                matches.update(deposits.get(normalize_culture_identifier(token), ()))
            source_id = "ncbi.assembly:" + row["assembly_accession"]
            for strain_id, matched in sorted(matches):
                evidence = {
                    "strain_id": strain_id,
                    "source": "NCBI_ASSEMBLY",
                    "source_id": source_id,
                    "source_reference_id": path.name,
                    "matched_strain_id": matched,
                    "source_strain_identifiers": row["infraspecific_name"],
                    "source_strain_field": "infraspecific_name",
                    "taxon_id": tid,
                }
                assembly = {
                    **evidence,
                    "assembly_id": source_id,
                    "source_field": "assembly_accession",
                    "assembly_level": row["assembly_level"],
                    "assembly_name": row["asm_name"],
                }
                assemblies[tuple(assembly.get(key, "") for key in ASSEMBLY_FIELDS)] = assembly
                for field, prefix, record_type, pattern in (
                    ("biosample", "biosample", "BIOSAMPLE", SAMPLE),
                    ("bioproject", "bioproject", "BIOPROJECT", PROJECT),
                ):
                    value = row[field]
                    if value in ("", "na"):
                        continue
                    if not pattern.fullmatch(value):
                        exclusions.append(
                            {
                                "kind": "ncbi_assembly_related",
                                "id": source_id + "/" + value,
                                "reason": f"unsupported {field} identifier; source value retained in catalog",
                            }
                        )
                        continue
                    assertion = {
                        **evidence,
                        "record_id": prefix + ":" + value,
                        "record_type": record_type,
                        "source_field": field,
                        "record_name": "",
                    }
                    related[tuple(assertion.get(key, "") for key in RELATED_RECORD_FIELDS)] = assertion
    return (
        [assemblies[key] for key in sorted(assemblies)],
        [related[key] for key in sorted(related)],
        sorted(exclusions, key=lambda row: (row["id"], row["reason"])),
    )
