"""Evidence-preserving links to ATB assemblies through exact BioSample IDs.

Sharing a strain does not link every genome to every sample. Native genome
assertions must first reach a sample through their own GTDB record or GOLD
organism/project chain. The resulting association is never genome equivalence.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from collections.abc import Iterable

from taxonmech.atb_catalog import (
    assembly_id,
    crosslink_exclusion_reason,
    is_sample_accession,
    normalize_release,
)

STRAIN_LINK_FIELDS = ["strain_id", "atb_id", "sample_id", "sample_evidence_json"]
GENOME_LINK_FIELDS = [
    "strain_id", "atb_id", "sample_id", "genome_id", "relationship", "source_evidence_json",
]
EXCLUSION_FIELDS = ["sample_id", "reason"]

_STRAIN = re.compile(r"kgmicrobe\.strain:\S+")
_GTDB = re.compile(r"gtdb\.genome:(?:RS_GCF|GB_GCA)_[0-9]{9}\.[1-9][0-9]*")
_NCBI = re.compile(r"ncbi\.assembly:GC[AF]_[0-9]{9}(?:\.[1-9][0-9]*)?")
_IMG = re.compile(r"img\.taxon:[0-9]+")
_SOURCE_ID = re.compile(r"[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._-]+")
_GOLD_STRAIN_FIELDS = {"ORGANISM CULTURE COLLECTION ID", "ORGANISM STRAIN"}


def _text(row: dict, field: str) -> str:
    value = row.get(field)
    if not isinstance(value, str) or not value:
        raise ValueError(f"missing or non-string {field} in genome/sample evidence")
    return value


def _require_pattern(value: str, pattern: re.Pattern[str], field: str) -> None:
    if not pattern.fullmatch(value):
        raise ValueError(f"invalid {field} in genome/sample evidence: {value!r}")


def _evidence(row: dict) -> dict:
    return {key: value for key, value in row.items() if key != "strain_id" and value not in (None, "")}


def _json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _evidence_key(row: dict, *, sample: bool) -> tuple[str, ...] | None:
    """Return a source-specific assertion key; unsupported sources never join."""
    source = _text(row, "source")
    if source not in {"GTDB", "GOLD"}:
        return None
    # A direct GOLD organism/analysis link without a sequencing project does
    # not identify the project that asserted a BioSample.
    if source == "GOLD" and not sample and not row.get("source_project_id"):
        return None
    sid = _text(row, "strain_id")
    deposit = _text(row, "matched_strain_id")
    _require_pattern(sid, _STRAIN, "strain_id")
    _require_pattern(deposit, _STRAIN, "matched_strain_id")
    source_id = _text(row, "source_id")
    strain_field = _text(row, "source_strain_field")
    strain_text = _text(row, "source_strain_identifiers")
    key = (sid, source, deposit, strain_text, strain_field,
           row.get("taxon_id", ""), row.get("source_reference_id", ""))
    if source == "GTDB":
        _require_pattern(source_id, _GTDB, "GTDB source_id")
        if strain_field != "ncbi_strain_identifiers":
            raise ValueError("GTDB sample joins require the original ncbi_strain_identifiers field")
        if sample and row.get("source_field") != "ncbi_biosample":
            raise ValueError("GTDB BioSample evidence must come from ncbi_biosample")
        return (*key, source_id)
    organism = _text(row, "source_organism_id")
    project = _text(row, "source_project_id")
    if not re.fullmatch(r"gold:Go[0-9]+", organism) or not re.fullmatch(r"gold:Gp[0-9]+", project):
        raise ValueError("GOLD sample joins require explicit Go and Gp identifiers")
    if strain_field not in _GOLD_STRAIN_FIELDS:
        raise ValueError("GOLD sample joins require the original organism strain identifier field")
    if sample:
        if source_id != project or row.get("source_field") != "NCBI BIOSAMPLE ACCESSION":
            raise ValueError("GOLD BioSample evidence must come from its stated Gp project")
    elif not re.fullmatch(r"gold:Ga[0-9]+", source_id):
        raise ValueError("GOLD genome evidence must come from an analysis project")
    return (*key, project, organism)


def _genome_id(row: dict, *, ncbi: bool) -> str:
    identifier = _text(row, "assembly_id" if ncbi else "genome_id")
    source, field = row["source"], row.get("source_field")
    if ncbi:
        _require_pattern(identifier, _NCBI, "NCBI assembly identifier")
        permitted = {"accession", "ncbi_genbank_assembly_accession"} if source == "GTDB" else {
            "AP GENBANK.assemblyAccession",
        }
        if field not in permitted:
            raise ValueError("NCBI assembly evidence must name the source assembly field")
        if source == "GTDB":
            primary = "ncbi.assembly:" + row["source_id"].split(":", 1)[1][3:]
            if field == "accession" and identifier != primary:
                raise ValueError("GTDB primary assembly must retain its source accession")
            if field == "ncbi_genbank_assembly_accession" and not identifier.startswith("ncbi.assembly:GCA_"):
                raise ValueError("GTDB GenBank assembly evidence must retain a GCA accession")
    elif source == "GTDB":
        _require_pattern(identifier, _GTDB, "GTDB genome identifier")
        if (row.get("source_database") != "gtdb" or identifier != row["source_id"]
                or field != "accession"):
            raise ValueError("GTDB genome/sample evidence must describe its own accession")
    else:
        _require_pattern(identifier, _IMG, "IMG genome identifier")
        if row.get("source_database") != "img" or field != "AP IMG TAXON ID":
            raise ValueError("GOLD genome/sample evidence must come from AP IMG TAXON ID")
    return identifier


def build_evidence(
    sample_rows: Iterable[dict], ncbi_rows: Iterable[dict], genome_rows: Iterable[dict],
) -> tuple[dict[tuple[str, str], list[dict]], dict[tuple[str, str, str], list[dict]]]:
    """Index original assertions by strain/sample and strain/sample/genome.

    The lists contain exact source assertions with only strain_id and empty
    values omitted. Identifier pairs never replace the independent evidence.
    """
    sample_pairs: dict[tuple[str, str], dict[str, dict]] = defaultdict(dict)
    sample_keys: dict[tuple[str, ...], dict[str, tuple[str, dict]]] = defaultdict(dict)
    for row in sample_rows:
        if row.get("record_type") != "BIOSAMPLE":
            continue
        sid, sample_id = _text(row, "strain_id"), _text(row, "record_id")
        _require_pattern(sid, _STRAIN, "strain_id")
        if not sample_id.startswith("biosample:") or not is_sample_accession(sample_id.split(":", 1)[1]):
            raise ValueError(f"invalid BioSample identifier: {sample_id!r}")
        _text(row, "source")
        _require_pattern(_text(row, "source_id"), _SOURCE_ID, "source_id")
        evidence = _evidence(row)
        encoded = _json(evidence)
        sample_pairs[sid, sample_id][encoded] = evidence
        if (key := _evidence_key(row, sample=True)) is not None:
            sample_keys[key][encoded] = (sample_id, evidence)

    genome_pairs: dict[tuple[str, str, str], dict[str, dict]] = defaultdict(dict)
    for rows, ncbi in ((ncbi_rows, True), (genome_rows, False)):
        for row in rows:
            if (key := _evidence_key(row, sample=False)) is None:
                continue
            identifier = _genome_id(row, ncbi=ncbi)
            genome = _evidence(row)
            for sample_id, sample in sample_keys.get(key, {}).values():
                evidence = {"genome": genome, "sample": sample}
                genome_pairs[row["strain_id"], sample_id, identifier][_json(evidence)] = evidence
    return (
        {key: [rows[value] for value in sorted(rows)] for key, rows in sample_pairs.items()},
        {key: [rows[value] for value in sorted(rows)] for key, rows in genome_pairs.items()},
    )


def build_links(
    atb_rows: Iterable[dict], sample_rows: Iterable[dict], ncbi_rows: Iterable[dict],
    genome_rows: Iterable[dict], *, release: str,
) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    """Return strain links, source-supported genome links, and exclusions.

    The caller retains the complete ATB catalog. This view includes only
    available assemblies with usable source sample identity, without an HQ
    requirement. A BioSample shared by multiple strains retains every link.
    """
    release = normalize_release(release)
    sample_evidence, genome_evidence = build_evidence(sample_rows, ncbi_rows, genome_rows)
    strains_by_sample: dict[str, list[str]] = defaultdict(list)
    for sid, sample in sample_evidence:
        strains_by_sample[sample].append(sid)
    genomes_by_sample: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for sid, sample, genome in genome_evidence:
        genomes_by_sample[sample].append((sid, genome))
    strain_links, genome_links, exclusions = [], [], []
    seen = set()
    for row in atb_rows:
        sample = "biosample:" + _text(row, "sample_accession")
        if sample not in strains_by_sample:
            continue
        if sample in seen:
            raise ValueError(f"duplicate ATB sample accession: {sample}")
        seen.add(sample)
        if reason := crosslink_exclusion_reason(row):
            exclusions.append({"sample_id": sample, "reason": reason})
            continue
        atb = assembly_id(release, row["sample_accession"])
        for sid in strains_by_sample[sample]:
            strain_links.append({"strain_id": sid, "atb_id": atb, "sample_id": sample,
                                 "sample_evidence_json": _json(sample_evidence[sid, sample])})
        for sid, genome in genomes_by_sample[sample]:
            genome_links.append({
                "strain_id": sid, "atb_id": atb, "sample_id": sample, "genome_id": genome,
                "relationship": "shares_biosample",
                "source_evidence_json": _json(genome_evidence[sid, sample, genome]),
            })
    return (
        sorted(strain_links, key=lambda row: tuple(row[field] for field in STRAIN_LINK_FIELDS)),
        sorted(genome_links, key=lambda row: tuple(row[field] for field in GENOME_LINK_FIELDS)),
        sorted(exclusions, key=lambda row: tuple(row[field] for field in EXCLUSION_FIELDS)),
    )
