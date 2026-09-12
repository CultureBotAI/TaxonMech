"""Strain-to-genome assertions from primary database metadata.

GTDB's metadata associates an assembly with explicit strain identifiers. Only
whole culture-collection identifiers already present in the strain inventory
are join keys; taxonomy, organism names and accession stems are not evidence.
"""

from __future__ import annotations

import csv
import gzip
import json
import re
from collections import defaultdict
from collections.abc import Iterator
from functools import lru_cache
from pathlib import Path

GTDB_METADATA_FIELDS = (
    "accession", "ncbi_strain_identifiers", "ncbi_genbank_assembly_accession",
    "ncbi_taxid", "ncbi_assembly_level", "ncbi_assembly_name", "ncbi_organism_name",
    "ncbi_biosample", "ncbi_bioproject",
)

STRAIN_EVIDENCE_FIELDS = [
    "source_field", "matched_strain_id", "source_strain_identifiers", "source_strain_field",
    "source_organism_id", "source_project_id",
]
RELATED_RECORD_FIELDS = [
    "strain_id", "record_id", "record_type", "source", "source_id", "source_reference_id",
    "taxon_id", *STRAIN_EVIDENCE_FIELDS,
]

_GTDB_ACCESSION = re.compile(r"(?:RS_GCF_|GB_GCA_)[0-9]{9}\.[1-9][0-9]*")
_GENBANK_ACCESSION = re.compile(r"GCA_[0-9]{9}(?:\.[1-9][0-9]*)?")
CAFI_REGISTRY_PATH = Path(__file__).resolve().parent / "data" / "cafi_acronyms.json"
_MISSING = {"", "none", "na", "n/a"}
# ENA specifies SAM(E|D|N)[A-Z]?[0-9]+, including SAMEA accessions.
_BIOSAMPLE = re.compile(r"SAM[EDN][A-Z]?[0-9]+")
# NCBI documents the legacy PRJDA/PRJEA prefixes alongside current prefixes.
_BIOPROJECT = re.compile(r"PRJ(?:NA|DB|DA|EB|EA)[0-9]+")


@lru_cache(maxsize=1)
def _culture_identifier_patterns() -> tuple[re.Pattern[str], dict[str, re.Pattern[str]]]:
    """Load authority names and accession templates from the DSMZ CAFI snapshot.

    Inventory fields can also contain bare laboratory strain names. Their
    presence in ``culture_collection_ids`` does not give them global scope.
    CAFI synonyms are recognized, but never mapped onto another acronym. An
    acronym alone is insufficient: AS-8 is a lab alias, whereas the registered
    historical AS collection requires a numeric.numeric accession.
    """
    registry = json.loads(CAFI_REGISTRY_PATH.read_text(encoding="utf-8"))
    templates: dict[str, str] = {}
    for entry in registry.values():
        template = entry.get("regex_id", {}).get("full")
        if not isinstance(template, str) or not template:
            raise ValueError(f"missing accession template in CAFI snapshot: {entry.get('acr')!r}")
        for acronym in [entry["acr"], *entry.get("acr_synonym", [])]:
            if not re.fullmatch(r"[A-Z]+(?::[A-Z]+)*", acronym):
                raise ValueError(f"invalid culture authority in CAFI snapshot: {acronym!r}")
            # CAFI uses a colon for compound acronyms whose printed form can
            # contain a hyphen (e.g. ACA:DC / ACA-DC). Recognize both spellings,
            # but retain the spelling as part of the identity matching key.
            for authority in {acronym, acronym.replace(":", "-")}:
                if authority in templates and templates[authority] != template:
                    raise ValueError(f"conflicting accession templates in CAFI snapshot: {authority!r}")
                templates[authority] = template
    if not templates:
        raise ValueError("CAFI culture authority snapshot is empty")
    ordered = sorted(templates, key=lambda authority: (-len(authority), authority))
    alternatives = "|".join(re.escape(authority) for authority in ordered)
    authority_pattern = re.compile(rf"(?P<authority>(?i:{alternatives}))[ :_-]+(?P<accession>.+)")
    try:
        accession_patterns = {authority: re.compile(template) for authority, template in templates.items()}
    except re.error as exc:
        raise ValueError(f"invalid accession template in CAFI snapshot: {exc}") from exc
    return authority_pattern, accession_patterns


def normalize_culture_identifier(identifier: str) -> str:
    """Return a registered deposit key, or empty for an unsupported identifier.

    Only the recognized authority's case and its following separator are
    normalized. Accession case, leading zeros, internal punctuation and strain
    markers remain significant. Neither substring searches nor historical
    acronym rewriting can establish an identity. The accession must match the
    authority's case-sensitive CAFI template; unmodeled formats are excluded.
    """
    authority_pattern, accession_patterns = _culture_identifier_patterns()
    match = authority_pattern.fullmatch(identifier.strip())
    if not match:
        return ""
    authority, accession = match["authority"].upper(), match["accession"]
    if not accession_patterns[authority].fullmatch(accession):
        return ""
    return f"{authority}-{accession}"


def index_culture_identifiers(strain_rows: list[dict]) -> dict[str, set[tuple[str, str]]]:
    """Index normalized deposits to strain IDs and their exact source CURIEs."""
    deposits: dict[str, set[tuple[str, str]]] = defaultdict(set)
    for strain in strain_rows:
        for deposit in strain.get("culture_collection_ids", "").split("|"):
            if not deposit:
                continue
            if not deposit.startswith("kgmicrobe.strain:") or not deposit.split(":", 1)[1]:
                raise ValueError(f"invalid culture-collection CURIE in strain inventory: {deposit!r}")
            local = deposit.split(":", 1)[1]
            if key := normalize_culture_identifier(local):
                deposits[key].add((strain["strain_id"], deposit))
    return dict(deposits)


def _metadata_rows(path: Path) -> Iterator[dict[str, str]]:
    """Read a structurally complete metadata table, including ignored files."""
    opener = gzip.open if path.suffix == ".gz" else Path.open
    with opener(path, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        headers = reader.fieldnames or []
        missing = set(GTDB_METADATA_FIELDS) - set(headers)
        if missing or len(headers) != len(set(headers)):
            raise ValueError(f"GTDB metadata {path}: missing or duplicate headers: {sorted(missing)}")
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"GTDB metadata {path}:{reader.line_num}: malformed TSV row")
            yield row


def _value(row: dict[str, str], field: str) -> str:
    value = row[field].strip()
    return "" if value.lower() in _MISSING else value


def _unique_sorted(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    unique = {tuple(sorted(row.items())): row for row in rows}
    return [unique[key] for key in sorted(unique)]


def extract_gtdb_strain_genomes(
    metadata_paths: list[Path], strain_rows: list[dict],
) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    """Return NCBI assemblies, GTDB records, related records and rejected IDs.

    Each match retains the exact inventoried culture CURIE and the verbatim
    GTDB strain field. Multiple deposits, source assertions and matching strain
    records remain separate. Only identical assertions are deduplicated.
    """
    deposits = index_culture_identifiers(strain_rows)

    assemblies: list[dict[str, str]] = []
    genomes: list[dict[str, str]] = []
    related: list[dict[str, str]] = []
    drops: list[dict[str, str]] = []

    for path in metadata_paths:
        for row in _metadata_rows(path):
            raw_strains = row["ncbi_strain_identifiers"]
            matches = set()
            # This field's delimiter is semicolon. A comma, '=' or descriptive
            # phrase is not permission to select a substring as a deposit ID.
            for token in raw_strains.split(";"):
                matches.update(deposits.get(normalize_culture_identifier(token), ()))
            if not matches:
                continue

            accession = _value(row, "accession")
            source_id = f"gtdb.genome:{accession}"
            if not _GTDB_ACCESSION.fullmatch(accession):
                drops.append({"kind": "gtdb_genome_record", "id": source_id,
                              "reason": "malformed GTDB genome accession"})
                continue
            taxon = _value(row, "ncbi_taxid")
            if taxon and not re.fullmatch(r"[0-9]+", taxon):
                drops.append({"kind": "gtdb_genome_record", "id": source_id,
                              "reason": f"malformed NCBI taxon identifier: {taxon!r}"})
                continue

            genbank = _value(row, "ncbi_genbank_assembly_accession")
            if genbank and not _GENBANK_ACCESSION.fullmatch(genbank):
                drops.append({"kind": "gtdb_assembly", "id": f"{source_id}/{genbank}",
                              "reason": "malformed ncbi_genbank_assembly_accession"})
                genbank = ""

            related_targets = []
            for field, prefix, record_type, pattern in (
                ("ncbi_biosample", "biosample", "BIOSAMPLE", _BIOSAMPLE),
                ("ncbi_bioproject", "bioproject", "BIOPROJECT", _BIOPROJECT),
            ):
                target = _value(row, field)
                if not target:
                    continue
                if not pattern.fullmatch(target):
                    drops.append({"kind": "gtdb_related_record", "id": f"{source_id}/{target}",
                                  "reason": f"malformed {field}"})
                    continue
                related_targets.append((field, f"{prefix}:{target}", record_type))

            for strain_id, deposit in sorted(matches):
                provenance = {
                    "strain_id": strain_id, "source": "GTDB", "source_id": source_id,
                    "source_reference_id": "", "taxon_id": f"NCBITaxon:{taxon}" if taxon else "",
                    "matched_strain_id": deposit, "source_strain_identifiers": raw_strains,
                    "source_strain_field": "ncbi_strain_identifiers",
                }
                # The GTDB record and its NCBI accession describe distinct
                # database identifiers, retained with their own source fields.
                genomes.append({
                    **provenance, "genome_id": source_id, "source_database": "gtdb",
                    "source_field": "accession", "assembly_level": _value(row, "ncbi_assembly_level"),
                    "genome_name": _value(row, "ncbi_organism_name"),
                })
                assembly_targets = [("accession", accession[3:])]
                if genbank:
                    assembly_targets.append(("ncbi_genbank_assembly_accession", genbank))
                for field, target in assembly_targets:
                    assemblies.append({
                        **provenance, "assembly_id": f"ncbi.assembly:{target}", "source_field": field,
                        "assembly_level": _value(row, "ncbi_assembly_level"),
                        "assembly_name": _value(row, "ncbi_assembly_name"),
                    })
                for field, target, record_type in related_targets:
                    related.append({**provenance, "record_id": target, "record_type": record_type,
                                    "source_field": field})

    return (_unique_sorted(assemblies), _unique_sorted(genomes),
            _unique_sorted(related), _unique_sorted(drops))
