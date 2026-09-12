"""A reproducible local catalog of primary AllTheBacteria assembly metadata.

The table includes unavailable and unprocessed samples. Availability, quality
and suitability for a strain crosslink are separate decisions. All source
columns remain verbatim; this module downloads no sequence files.
"""

from __future__ import annotations

import csv
import hashlib
import json
import lzma
import os
import re
import sqlite3
import tempfile
from collections import Counter
from collections.abc import Iterator
from pathlib import Path

ASSEMBLY_COLUMNS = (
    "sample_accession", "run_accession", "assembly_accession", "assembly_seqkit_sum",
    "asm_pipe_filter", "asm_fasta_on_osf", "dataset", "scientific_name",
    "sylph_species_pre_202505", "in_hq_pre_202505", "sylph_species", "sylph_filter",
    "hq_filter", "osf_tarball_filename", "osf_tarball_url", "aws_url", "comments",
)

_SAMPLE = re.compile(r"SAM[EDN][A-Z]?[0-9]+")
_ENA_ANALYSIS = re.compile(r"ERZ[0-9]+")
IDENTITY_WARNING_FLAGS = frozenset({"NO_RUNS", "RUN_REMOVED", "RMMS", "META_FAIL", "RUN_CHANGE"})
_ASSEMBLY_ONLY_FLAGS = frozenset({"ENA_ASM_SUBMIT_ERR", "ASM_LEN"})


def is_sample_accession(value: str) -> bool:
    """Whether the entire value is one INSDC BioSample accession."""
    return bool(_SAMPLE.fullmatch(value))


def is_ena_analysis_accession(value: str) -> bool:
    """Whether the value is an ENA analysis, distinct from GCA/GCF assemblies."""
    return bool(_ENA_ANALYSIS.fullmatch(value))


def normalize_release(release: str) -> str:
    """Normalize a dated aggregate snapshot to YYYY-MM without guessing a release."""
    match = re.fullmatch(r"([0-9]{4})-?(0[1-9]|1[0-2])", release)
    if not match:
        raise ValueError(f"invalid ATB aggregate release: {release!r}; expected YYYY-MM")
    return f"{match[1]}-{match[2]}"


def assembly_id(release: str, sample: str) -> str:
    """Mint a TaxonMech assembly key scoped to one explicit ATB snapshot.

    ATB names FASTA objects by sample, but a sample is not a timeless assembly
    identity. This locally defined key is neither a BioSample nor an ENA ID.
    Callers must separately establish that the source row has an assembly.
    """
    snapshot = normalize_release(release).replace("-", "")
    if not is_sample_accession(sample):
        raise ValueError(f"not a single ATB sample accession: {sample!r}")
    return f"atb.assembly:{snapshot}.{sample}"


def validate_assembly_row(row: dict[str, str], *, context: str = "ATB metadata") -> None:
    """Reject structural corruption without deleting valid source status rows."""
    if set(row) != set(ASSEMBLY_COLUMNS) or any(not isinstance(value, str) for value in row.values()):
        raise ValueError(f"{context}: malformed TSV row")
    if not row["sample_accession"] or "\x00" in row["sample_accession"]:
        raise ValueError(f"{context}: empty or invalid sample key")
    if row["asm_fasta_on_osf"] not in {"0", "1"}:
        raise ValueError(f"{context}: asm_fasta_on_osf must be 0 or 1")
    if row["asm_fasta_on_osf"] == "1" and not is_sample_accession(row["sample_accession"]):
        raise ValueError(f"{context}: available assembly requires a single sample accession")
    if row["assembly_accession"] not in {"", "NA"} and not is_ena_analysis_accession(
        row["assembly_accession"]
    ):
        raise ValueError(f"{context}: assembly_accession must be an ENA ERZ analysis or NA")


def crosslink_exclusion_reason(row: dict[str, str]) -> str:
    """Return why a catalog row cannot support an exact BioSample crosslink.

    Empty means eligible. This is stricter than catalog inclusion: unknown
    metadata flags fail closed, while assembly-only length/submission errors
    and non-PASS high-quality filters do not establish a sample identity error.
    Required artifact fields must be usable as supplied; URLs are never guessed.
    """
    validate_assembly_row(row)
    if row["asm_fasta_on_osf"] != "1":
        return "assembly_unavailable"
    flags = set(row["asm_pipe_filter"].split(","))
    all_flags = flags | set(row["sylph_filter"].split(",")) | set(row["hq_filter"].split(","))
    if warnings := all_flags & IDENTITY_WARNING_FLAGS:
        return "metadata_identity_flags:" + ",".join(sorted(warnings))
    if flags != {"PASS"} and (not flags or not flags <= _ASSEMBLY_ONLY_FLAGS):
        return "unsupported_assembly_filter:" + row["asm_pipe_filter"]
    if any(not re.fullmatch(r"[EDS]RR[0-9]+", run) for run in row["run_accession"].split(",")):
        return "missing_or_invalid_run_accession"
    if not re.fullmatch(r"seqkit\.v0\.1_DLS_k0_[a-f0-9]{32}", row["assembly_seqkit_sum"]):
        return "missing_or_invalid_sequence_digest"
    expected_url = (
        "https://allthebacteria-assemblies.s3.eu-west-2.amazonaws.com/"
        f"{row['sample_accession']}.fa.gz"
    )
    if row["aws_url"] != expected_url:
        return "missing_or_invalid_assembly_url"
    if not re.fullmatch(r"https://osf\.io/download/[A-Za-z0-9]+/?", row["osf_tarball_url"]) or not (
        row["osf_tarball_filename"].endswith(".tar.xz")
    ):
        return "missing_or_invalid_osf_archive"
    return ""


def iter_assemblies(path: Path) -> Iterator[dict[str, str]]:
    """Stream the complete 17-column TSV or TSV.xz, preserving source values.

    ATB explicitly requires QUOTE_NONE for ENA-derived TSV. Its status table
    also contains unprocessed semicolon-separated sample keys; these remain
    one raw row and never become assembly identifiers. Available assemblies
    require a single valid sample accession.
    """
    path = Path(path)
    opener = lzma.open if path.suffix == ".xz" else Path.open
    with opener(path, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t", quotechar=None, quoting=csv.QUOTE_NONE)
        headers = reader.fieldnames or []
        if len(headers) != len(ASSEMBLY_COLUMNS) or set(headers) != set(ASSEMBLY_COLUMNS):
            raise ValueError(f"ATB metadata {path}: expected exactly the 17 assembly columns")
        for row in reader:
            context = f"ATB metadata {path}:{reader.line_num}"
            validate_assembly_row(row, context=context)
            yield row


def sha256_file(path: Path) -> str:
    """Hash the exact source bytes, including compression when supplied."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_catalog(
    metadata_path: Path,
    index_path: Path,
    *,
    release: str,
    expected_sha256: str | None = None,
) -> dict:
    """Atomically replace a local SQLite catalog after complete validation.

    ``assembly`` stores every source column as TEXT with the raw sample key as
    its primary key. ``metadata(key, value)`` stores scalar strings and JSON
    objects for the count dictionaries. No source row is excluded by quality
    or availability. A failed build leaves the previous catalog intact.
    """
    metadata_path, index_path = Path(metadata_path), Path(index_path)
    release = normalize_release(release)
    if metadata_path.resolve() == index_path.resolve():
        raise ValueError("ATB source metadata and catalog must be different paths")
    source_sha256 = sha256_file(metadata_path)
    if expected_sha256 is not None:
        if not re.fullmatch(r"[a-fA-F0-9]{64}", expected_sha256):
            raise ValueError("expected_sha256 must be a 64-character SHA256 digest")
        if source_sha256 != expected_sha256.lower():
            raise ValueError(f"ATB source SHA256 mismatch: expected {expected_sha256}, got {source_sha256}")

    index_path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(prefix=f".{index_path.name}.", suffix=".tmp", dir=index_path.parent)
    os.close(fd)
    temporary_path = Path(temporary_name)
    connection = None
    counts: Counter = Counter()
    datasets: Counter = Counter()
    filters: Counter = Counter()
    try:
        connection = sqlite3.connect(temporary_path)
        with connection:
            declarations = ", ".join(
                f'"{column}" TEXT NOT NULL' + (" PRIMARY KEY" if column == "sample_accession" else "")
                for column in ASSEMBLY_COLUMNS
            )
            connection.execute(f"CREATE TABLE assembly ({declarations})")
            insert = f"INSERT INTO assembly VALUES ({','.join('?' for _ in ASSEMBLY_COLUMNS)})"
            batch = []
            for row in iter_assemblies(metadata_path):
                counts["rows"] += 1
                counts["available_assemblies"] += row["asm_fasta_on_osf"] == "1"
                counts["unavailable_rows"] += row["asm_fasta_on_osf"] == "0"
                counts["non_single_sample_rows"] += not is_sample_accession(row["sample_accession"])
                datasets[row["dataset"]] += 1
                filters[row["asm_pipe_filter"]] += 1
                batch.append(tuple(row[column] for column in ASSEMBLY_COLUMNS))
                if len(batch) == 2000:
                    connection.executemany(insert, batch)
                    batch.clear()
            connection.executemany(insert, batch)
            if not counts["rows"]:
                raise ValueError("ATB source metadata contains no sample rows")
            if sha256_file(metadata_path) != source_sha256:
                raise ValueError("ATB source metadata changed while building the catalog")
            for column in ("assembly_accession", "scientific_name", "sylph_species"):
                connection.execute(f'CREATE INDEX "assembly_{column}" ON assembly ("{column}")')
            stats = {
                "release": release,
                "source_sha256": source_sha256,
                **dict(counts),
                "datasets": dict(sorted(datasets.items())),
                "filters": dict(sorted(filters.items())),
            }
            connection.execute("CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
            connection.executemany(
                "INSERT INTO metadata VALUES (?, ?)",
                [(key, json.dumps(value, sort_keys=True) if isinstance(value, dict) else str(value))
                 for key, value in stats.items()],
            )
        connection.close()
        connection = None
        temporary_path.replace(index_path)
        return stats
    except sqlite3.IntegrityError as exc:
        raise ValueError("ATB metadata contains a duplicate sample accession") from exc
    finally:
        if connection is not None:
            connection.close()
        temporary_path.unlink(missing_ok=True)
