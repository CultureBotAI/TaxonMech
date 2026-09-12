"""ATB source integrity, snapshot identity, and atomic catalog publication."""

from __future__ import annotations

import csv
import hashlib
import json
import lzma
import sqlite3

import pytest

from taxonmech import atb_catalog
from taxonmech.atb_catalog import (
    ASSEMBLY_COLUMNS,
    assembly_id,
    build_catalog,
    crosslink_exclusion_reason,
    is_ena_analysis_accession,
    is_sample_accession,
    iter_assemblies,
)


def assembly_row(sample="SAMD00000344", **changes):
    row = dict.fromkeys(ASSEMBLY_COLUMNS, "NA")
    row.update(
        sample_accession=sample, run_accession="DRR024501", assembly_accession="ERZ2821603",
        assembly_seqkit_sum="seqkit.v0.1_DLS_k0_22841afbe77ffd5789a81fb81082f04f",
        asm_pipe_filter="PASS", asm_fasta_on_osf="1", dataset="661k",
        scientific_name="Paucilactobacillus hokkaidonensis JCM 18461",
        sylph_species="Paucilactobacillus hokkaidonensis", hq_filter="PASS", comments="None",
        osf_tarball_filename="atb.assembly.r0.2.batch.127.tar.xz",
        osf_tarball_url="https://osf.io/download/6671719165e1de5eb5893c28/",
        aws_url=f"https://allthebacteria-assemblies.s3.eu-west-2.amazonaws.com/{sample}.fa.gz",
    )
    row.update(changes)
    return row


def metadata_file(tmp_path, rows, *, compressed=False):
    path = tmp_path / ("assembly.tsv.xz" if compressed else "assembly.tsv")
    opener = lzma.open if compressed else type(path).open
    with opener(path, "wt", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=ASSEMBLY_COLUMNS, delimiter="\t",
                                quotechar=None, quoting=csv.QUOTE_NONE)
        writer.writeheader()
        writer.writerows(rows)
    return path


@pytest.mark.parametrize("compressed", [False, True])
def test_stream_preserves_quotes_unknown_runs_and_unprocessed_multi_sample_keys(tmp_path, compressed):
    rows = [
        assembly_row(scientific_name='"Quoted name', comments='literal "quotes"; retained'),
        assembly_row("SAMN1", run_accession="unknown", asm_pipe_filter="NO_RUNS"),
        assembly_row("SAMEA1;SAMEA2", asm_fasta_on_osf="0", asm_pipe_filter="NOT_PROCESSED",
                     run_accession="NA", assembly_accession="NA", aws_url="NA"),
    ]
    path = metadata_file(tmp_path, rows, compressed=compressed)
    assert list(iter_assemblies(path)) == rows


def test_catalog_retains_status_and_source_strings_without_inventing_links(tmp_path):
    rows = [
        assembly_row(),
        assembly_row("SAMN1", asm_pipe_filter="ENA_ASM_SUBMIT_ERR", assembly_accession="NA"),
        assembly_row("SAMEA1;SAMEA2", asm_fasta_on_osf="0", asm_pipe_filter="NOT_PROCESSED",
                     assembly_accession="NA", aws_url="NA"),
    ]
    path = metadata_file(tmp_path, rows, compressed=True)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    destination = tmp_path / "catalog.sqlite"
    stats = build_catalog(path, destination, release="202505", expected_sha256=digest)
    assert stats["rows"] == 3
    assert stats["available_assemblies"] == 2
    assert stats["unavailable_rows"] == stats["non_single_sample_rows"] == 1
    with sqlite3.connect(destination) as conn:
        conn.row_factory = sqlite3.Row
        actual = [dict(row) for row in conn.execute("SELECT * FROM assembly ORDER BY rowid")]
        assert actual == rows
        metadata = dict(conn.execute("SELECT key, value FROM metadata"))
        assert metadata["release"] == "2025-05"
        assert metadata["source_sha256"] == digest
        assert json.loads(metadata["filters"]) == stats["filters"]
        assert {row[1] for row in conn.execute("PRAGMA index_list(assembly)")} >= {
            "assembly_assembly_accession", "assembly_scientific_name", "assembly_sylph_species",
        }


@pytest.mark.parametrize("changes", [
    {"sample_accession": ""}, {"sample_accession": "SAMN1;SAMN2"},
    {"asm_fasta_on_osf": "yes"}, {"assembly_accession": "GCA_000005845.2"},
    {"assembly_accession": "ERZ123.1"},
])
def test_invalid_identity_and_status_values_fail_with_line_context(tmp_path, changes):
    path = metadata_file(tmp_path, [assembly_row(**changes)])
    with pytest.raises(ValueError, match=r"assembly.tsv:2:"):
        list(iter_assemblies(path))


@pytest.mark.parametrize("corruption", ["missing_header", "duplicate_header", "short_row", "long_row"])
def test_structural_corruption_is_not_silently_truncated(tmp_path, corruption):
    path = metadata_file(tmp_path, [assembly_row()])
    lines = path.read_text().splitlines()
    if corruption == "missing_header":
        lines[0] = "\t".join(ASSEMBLY_COLUMNS[:-1])
    elif corruption == "duplicate_header":
        lines[0] = "\t".join([*ASSEMBLY_COLUMNS[:-1], ASSEMBLY_COLUMNS[0]])
    elif corruption == "short_row":
        lines[1] = "\t".join(lines[1].split("\t")[:-1])
    else:
        lines[1] += "\textra"
    path.write_text("\n".join(lines) + "\n")
    with pytest.raises(ValueError, match="columns|malformed TSV"):
        list(iter_assemblies(path))


@pytest.mark.parametrize("failure", ["duplicate", "corrupt_later_row", "hash", "truncated_xz", "empty"])
def test_failed_build_preserves_previous_catalog_and_cleans_temporary_files(tmp_path, failure):
    destination = tmp_path / "catalog.sqlite"
    destination.write_bytes(b"previous catalog remains intact")
    rows = [] if failure == "empty" else [assembly_row()]
    if failure == "duplicate":
        rows.append(assembly_row())
    if failure == "corrupt_later_row":
        # Flush a batch before the parser detects the subsequent broken row.
        rows = [assembly_row(f"SAMN{i}") for i in range(2001)]
        rows[-1]["asm_fasta_on_osf"] = "broken"
    path = metadata_file(tmp_path, rows, compressed=failure == "truncated_xz")
    if failure == "truncated_xz":
        path.write_bytes(path.read_bytes()[:-15])
    with pytest.raises((ValueError, EOFError, lzma.LZMAError)):
        build_catalog(path, destination, release="2025-05",
                      expected_sha256="0" * 64 if failure == "hash" else None)
    assert destination.read_bytes() == b"previous catalog remains intact"
    assert not list(tmp_path.glob(".catalog.sqlite.*"))


def test_assembly_keys_are_snapshot_scoped_and_cannot_be_sample_or_ena_ids():
    assert assembly_id("2025-05", "SAMD00000344") == "atb.assembly:202505.SAMD00000344"
    assert assembly_id("202505", "SAMD00000344") == assembly_id("2025-05", "SAMD00000344")
    assert assembly_id("2024-08", "SAMD00000344") != assembly_id("2025-05", "SAMD00000344")
    assert is_ena_analysis_accession("ERZ2821603")
    assert not is_sample_accession("ERZ2821603")
    for sample in ("SAMD00000344;SAMD00000345", "ERZ2821603", "SAMN1 ", "GCA_000005845.2"):
        with pytest.raises(ValueError, match="single ATB sample"):
            assembly_id("2025-05", sample)
    for release in ("latest", "r0.2", "2025-13", "2025-5"):
        with pytest.raises(ValueError, match="aggregate release"):
            assembly_id(release, "SAMN1")


@pytest.mark.parametrize("flag", ["PASS", "ENA_ASM_SUBMIT_ERR", "ASM_LEN"])
def test_available_non_hq_assemblies_without_ena_ids_can_support_sample_crosslinks(flag):
    assert crosslink_exclusion_reason(assembly_row(
        asm_pipe_filter=flag, hq_filter="MAX_CONTIG_NUM", assembly_accession="NA",
    )) == ""


@pytest.mark.parametrize("flag", [
    "NO_RUNS", "RUN_REMOVED", "RMMS", "META_FAIL", "RUN_CHANGE",
    "ENA_ASM_SUBMIT_ERR,NO_RUNS,RUN_REMOVED", "FUTURE_FLAG", "", "PASS,ASM_LEN",
])
def test_available_identity_warnings_and_unknown_filters_remain_unlinked(flag):
    assert crosslink_exclusion_reason(assembly_row(asm_pipe_filter=flag))


@pytest.mark.parametrize("field", ["sylph_filter", "hq_filter"])
def test_identity_warnings_in_any_filter_column_prevent_a_crosslink(field):
    assert crosslink_exclusion_reason(assembly_row(**{field: "MAX_CONTIG_NUM,RMMS"})) == (
        "metadata_identity_flags:RMMS"
    )


@pytest.mark.parametrize("changes,reason", [
    ({"asm_fasta_on_osf": "0"}, "assembly_unavailable"),
    ({"run_accession": "unknown"}, "missing_or_invalid_run_accession"),
    ({"assembly_seqkit_sum": "NA"}, "missing_or_invalid_sequence_digest"),
    ({"aws_url": "https://allthebacteria-assemblies.s3.eu-west-2.amazonaws.com/SAMN2.fa.gz"},
     "missing_or_invalid_assembly_url"),
    ({"osf_tarball_url": "NA"}, "missing_or_invalid_osf_archive"),
])
def test_crosslinks_need_source_supplied_artifact_metadata(changes, reason):
    assert crosslink_exclusion_reason(assembly_row(**changes)) == reason


def test_changed_source_cannot_publish_a_catalog_with_an_outdated_digest(tmp_path, monkeypatch):
    path = metadata_file(tmp_path, [assembly_row()])
    destination = tmp_path / "catalog.sqlite"
    destination.write_bytes(b"previous catalog")
    original_reader = atb_catalog.iter_assemblies

    def changing_source(source_path):
        yield from original_reader(source_path)
        source_path.write_text(source_path.read_text().replace("JCM 18461", "JCM 99999"))

    monkeypatch.setattr(atb_catalog, "iter_assemblies", changing_source)
    with pytest.raises(ValueError, match="changed while building"):
        build_catalog(path, destination, release="2025-05")
    assert destination.read_bytes() == b"previous catalog"
    assert not list(tmp_path.glob(".catalog.sqlite.*"))
