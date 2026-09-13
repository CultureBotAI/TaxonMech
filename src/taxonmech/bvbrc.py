"""BV-BRC native genome records and explicit culture-deposit evidence."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from taxonmech.genome_sources import index_culture_identifiers, normalize_culture_identifier
from taxonmech.source_catalog import json_rows, sha256


def records(directory: Path):
    source = json.loads((directory / "SOURCE.json").read_text())
    if source.get("source") != "BV-BRC" or source.get("format_version") != 1:
        raise ValueError("unsupported BV-BRC snapshot")
    ids = []
    for item in source["files"]:
        if Path(item["path"]).name != item["path"]:
            raise ValueError("BV-BRC source path leaves its projection")
        path = directory / item["path"]
        if sha256(path) != item["sha256"] or path.stat().st_size != item["bytes"]:
            raise ValueError("BV-BRC projection differs from its pin")
        count = 0
        for row in json_rows(path):
            gid = row.get("genome_id")
            if (
                not isinstance(gid, str)
                or not re.fullmatch(r"[0-9]+\.[0-9]+", gid)
                or row.get("superkingdom") not in {"Bacteria", "Archaea"}
                or row.get("public") is not True
            ):
                raise ValueError("BV-BRC source record lacks its public prokaryote identity")
            ids.append(gid)
            count += 1
            yield row
        if count != item["rows"]:
            raise ValueError("BV-BRC projection file count differs from its pin")
    if (
        ids != sorted(set(ids))
        or len(ids) != source["census_count"]
        or hashlib.sha256("\n".join(ids).encode()).hexdigest() != source["census_sha256"]
    ):
        raise ValueError("BV-BRC projection differs from its complete ID census")


def extract_links(directory: Path, strains: list[dict]) -> tuple[list, list, list, list]:
    from taxonmech.extract import ASSEMBLY_FIELDS, GENOME_RECORD_FIELDS, RELATED_RECORD_FIELDS

    deposits = index_culture_identifiers(strains)
    assemblies, genomes, related, excluded = {}, {}, {}, []
    for row in records(directory):
        source_id = "patric:" + row["genome_id"]
        for field in ("culture_collection", "strain"):
            raw = row.get(field, "")
            values = raw if isinstance(raw, list) else [raw]
            if any(not isinstance(value, str) for value in values):
                raise ValueError("BV-BRC culture identifiers must be source text")
            for source_value in values:
                matches = set()
                for token in re.split(r"[;,|]", source_value):
                    matches.update(deposits.get(normalize_culture_identifier(token.strip()), ()))
                for sid, deposit in sorted(matches):
                    taxid = row.get("taxon_id")
                    if type(taxid) is not int or taxid <= 0:
                        raise ValueError("BV-BRC matched genome lacks a positive NCBI taxon ID")
                    evidence = {
                        "strain_id": sid,
                        "source": "BV_BRC",
                        "source_id": source_id,
                        "source_reference_id": "",
                        "matched_strain_id": deposit,
                        "source_strain_identifiers": source_value,
                        "source_strain_field": field,
                        "taxon_id": f"NCBITaxon:{taxid}",
                    }
                    genome = {
                        **evidence,
                        "genome_id": source_id,
                        "source_database": "patric",
                        "source_field": "genome_id",
                        "assembly_level": "",
                        "genome_name": row.get("genome_name", ""),
                    }
                    genomes[tuple(genome.get(key, "") for key in GENOME_RECORD_FIELDS)] = genome
                    accession = row.get("assembly_accession", "")
                    if accession:
                        if isinstance(accession, str) and re.fullmatch(
                            r"GC[AF]_[0-9]{9}(?:\.[1-9][0-9]*)?", accession
                        ):
                            assembly = {
                                **evidence,
                                "assembly_id": "ncbi.assembly:" + accession,
                                "source_field": "assembly_accession",
                                "assembly_level": "",
                                "assembly_name": row.get("genome_name", ""),
                            }
                            assemblies[tuple(assembly.get(key, "") for key in ASSEMBLY_FIELDS)] = assembly
                        else:
                            excluded.append(
                                {
                                    "kind": "bvbrc_assembly",
                                    "id": source_id,
                                    "reason": "unsupported assembly accession; source value retained",
                                }
                            )
                    for key, prefix, kind, pattern in (
                        ("biosample_accession", "biosample", "BIOSAMPLE", r"SAM[EDN][A-Z]?[0-9]+"),
                        ("bioproject_accession", "bioproject", "BIOPROJECT", r"PRJ(?:NA|DB|DA|EB|EA)[0-9]+"),
                    ):
                        value = row.get(key, "")
                        if not value:
                            continue
                        if not isinstance(value, str) or not re.fullmatch(pattern, value):
                            excluded.append(
                                {
                                    "kind": "bvbrc_related",
                                    "id": source_id,
                                    "reason": f"unsupported {key}; retained in source catalog",
                                }
                            )
                            continue
                        assertion = {
                            **evidence,
                            "record_id": prefix + ":" + value,
                            "record_type": kind,
                            "source_field": key,
                            "record_name": "",
                        }
                        related[tuple(assertion.get(key, "") for key in RELATED_RECORD_FIELDS)] = assertion
    return (
        [assemblies[key] for key in sorted(assemblies)],
        [genomes[key] for key in sorted(genomes)],
        [related[key] for key in sorted(related)],
        excluded,
    )
