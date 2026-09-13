"""Current primary BacDive identities and explicit v2 genome assertions."""

from __future__ import annotations

import gzip
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

from taxonmech.bacdive_snapshot import project_record
from taxonmech.genome_sources import normalize_culture_identifier


def objects(value, field: str) -> list[dict]:
    if value is None:
        return []
    if isinstance(value, dict):
        return [value]
    if not isinstance(value, list) or any(not isinstance(row, dict) for row in value):
        raise ValueError(f"BacDive {field} must contain objects")
    return value


def records(directory: Path):
    source = json.loads((directory / "SOURCE.json").read_text())
    path = directory / "records.jsonl.gz"
    with path.open("rb") as handle:
        _digest = hashlib.sha256()
        for _chunk in iter(lambda: handle.read(1 << 20), b""):
            _digest.update(_chunk)
        digest = _digest.hexdigest()
    if source.get("source") != "BacDive v2" or digest != source["records"]["sha256"]:
        raise ValueError("BacDive v2 source projection differs from its pin")
    seen = set()
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            if project_record(record) != record:
                raise ValueError("BacDive source contains fields outside its pinned projection")
            identifier = record["General"]["BacDive-ID"]
            if identifier in seen:
                raise ValueError("duplicate BacDive v2 strain ID")
            seen.add(identifier)
            yield record
    if (
        len(seen) != source["records"]["rows"]
        or len(seen) + len(source["missing_api_ids"]) != source["census_count"]
    ):
        raise ValueError("BacDive records do not cover the captured census")


def load_identities(directory: Path, previous: dict) -> tuple[dict, dict]:
    strains, cc_parents = {}, defaultdict(set)
    for record in records(directory):
        general = record["General"]
        bid = str(general["BacDive-ID"])
        sid = f"kgmicrobe.strain:bacdive_{bid}"
        taxonomy = record.get("Name and taxonomic classification", {})
        matches = objects(general.get("NCBI tax id"), "NCBI tax id")
        # Prefer the source's explicit strain-level classification, as in
        # kg-microbe. A source species match remains in the primary projection.
        preferred = [row for row in matches if row.get("Matching level") == "strain"] or matches
        tids = set()
        for row in preferred:
            value = row.get("NCBI tax id")
            if isinstance(value, bool) or not str(value).isdigit() or int(value) <= 0:
                raise ValueError(f"BacDive {bid}: invalid explicit NCBI taxon ID")
            tids.add(f"NCBITaxon:{value}")
        literature = record.get("Literature", {})
        culture_values = literature.get("culture collection no.", "")
        if not isinstance(culture_values, str):
            raise ValueError(f"BacDive {bid}: culture collection numbers must be text")
        ccs = set()
        for value in culture_values.split(","):
            token = value.strip()
            if not token:
                continue
            # Do not turn unsupported suffix whitespace into punctuation that
            # a later adapter could mistake for a registered accession.
            local = quote(normalize_culture_identifier(token) or token, safe="-._~:")
            ccs.add("kgmicrobe.strain:" + local)
        strains[sid] = {
            "bacdive_id": bid,
            "designation": taxonomy.get("strain designation", ""),
            "taxon_ids": tids,
            "lpsn_ids": previous.get(sid, {}).get("lpsn_ids", set()),
            "culture_collection_ids": ccs,
            "medium_count": 0,
        }
        for cc in ccs:
            cc_parents[cc].update(tids)
    return strains, cc_parents


def genome_links(directory: Path) -> tuple[list, list, list]:
    from taxonmech.extract import ASSEMBLY_FIELDS, GENOME_RECORD_FIELDS

    assemblies, genomes, exclusions = {}, {}, []
    identifiers = (
        ("INSDC accession", "ncbi.assembly", "", re.compile(r"GC[AF]_[0-9]{9}(?:\.[1-9][0-9]*)?")),
        ("BV-BRC accession", "patric", "patric", re.compile(r"[0-9]+\.[0-9]+")),
        ("IMG accession", "img.taxon", "img", re.compile(r"[0-9]+")),
    )
    for record in records(directory):
        bid = str(record["General"]["BacDive-ID"])
        sid = f"kgmicrobe.strain:bacdive_{bid}"
        for genome in objects(
            record.get("Sequence information", {}).get("Genome sequences"), "Genome sequences"
        ):
            taxon, reference = str(genome.get("NCBI tax ID") or ""), str(genome.get("@ref") or "")
            if (taxon and not taxon.isdigit()) or (reference and not reference.isdigit()):
                raise ValueError(f"BacDive {bid}: invalid genome taxon/reference ID")
            for field, prefix, database, pattern in identifiers:
                accession = genome.get(field)
                if accession in (None, ""):
                    continue
                if not isinstance(accession, str) or not pattern.fullmatch(accession):
                    exclusions.append(
                        {
                            "kind": "bacdive_v2_genome",
                            "id": f"{sid}/{accession}",
                            "reason": f"invalid or non-assembly identifier in {field}",
                        }
                    )
                    continue
                row = {
                    "strain_id": sid,
                    "genome_id" if database else "assembly_id": f"{prefix}:{accession}",
                    **({"source_database": database} if database else {}),
                    "source": "BACDIVE",
                    "source_id": f"bacdive:{bid}",
                    "source_reference_id": reference,
                    "source_field": "Sequence information.Genome sequences." + field,
                    "assembly_level": str(genome.get("assembly level") or ""),
                    "genome_name" if database else "assembly_name": str(genome.get("description") or ""),
                    "taxon_id": f"NCBITaxon:{taxon}" if taxon else "",
                }
                target, columns = (
                    (genomes, GENOME_RECORD_FIELDS) if database else (assemblies, ASSEMBLY_FIELDS)
                )
                target[tuple(row.get(column, "") for column in columns)] = row
    return (
        [assemblies[key] for key in sorted(assemblies)],
        [genomes[key] for key in sorted(genomes)],
        sorted(exclusions, key=lambda row: (row["id"], row["reason"])),
    )
