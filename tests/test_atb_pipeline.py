"""Atomic publication and provenance checks for the ATB orchestration."""

import json
from pathlib import Path

import pytest
import yaml

from taxonmech import atb
from taxonmech.extract import ASSEMBLY_FIELDS, GENOME_RECORD_FIELDS, RELATED_RECORD_FIELDS, write_tsv
from tests.test_atb_catalog import assembly_row, metadata_file
from tests.test_atb_links import SAMPLE, SID, genome, ncbi, sample


@pytest.fixture
def pipeline(tmp_path):
    raw = tmp_path / "data/raw"
    raw.mkdir(parents=True)
    strain = {"strain_id": SID, "bacdive_id": "5", "culture_collection_ids": "kgmicrobe.strain:DSM-30083"}
    write_tsv(raw / "bacdive_strains.tsv", list(strain), [strain])
    write_tsv(raw / "strain_related_records.tsv", RELATED_RECORD_FIELDS, [sample()])
    write_tsv(raw / "strain_assemblies.tsv", ASSEMBLY_FIELDS, [ncbi()])
    write_tsv(raw / "strain_genome_records.tsv", GENOME_RECORD_FIELDS, [genome()])
    source = metadata_file(tmp_path, [assembly_row(SAMPLE), assembly_row("SAMN999")])
    config = {"release": "2025-05", "url": "https://osf.io/download/4kjh7/",
              "sha256": atb.sha256(source), "metadata_path": str(source),
              "index_path": str(tmp_path / "data/index/catalog.sqlite"),
              "license": "CC-BY-4.0", "citation": "https://doi.org/10.1101/2024.03.08.584059"}
    return source, Path(config["index_path"]), tmp_path / "data/atb", raw, config


def snapshot(index, out):
    return {str(p): p.read_bytes() for p in [index, *(out / n for n in (*atb.OUTPUT_NAMES, "MANIFEST.yaml"))]
            if p.exists()}


def change_row(path, field, value):
    rows = atb.read_rows(path)
    rows[0][field] = value
    write_tsv(path, list(rows[0]), rows)


def test_dry_run_is_read_only_and_replay_is_byte_identical(pipeline):
    source, index, out, raw, config = pipeline
    report = atb.generate(*pipeline)
    assert report["catalog"]["rows"] == 2
    assert report["crosslinks"]["strain_pairs"] == 1
    assert not index.exists() and not out.exists()
    first = atb.generate(*pipeline, apply=True)
    before = snapshot(index, out)
    assert atb.generate(*pipeline, apply=True) == first
    assert snapshot(index, out) == before
    assert atb.genome_records(out)[SID][0]["atb_evidence"]["sample_links"]


@pytest.mark.parametrize("corruption", [
    "unavailable", "identity_warning", "empty_evidence", "different_sample", "wrong_type",
    "empty_source", "missing_deposit", "malformed_taxon", "wrong_sample_prefix", "duplicate_assembly",
])
def test_converter_rejects_unsafe_or_unproven_crosswalk_rows(pipeline, corruption):
    _, _, out, _, _ = pipeline
    atb.generate(*pipeline, apply=True)
    if corruption in {"unavailable", "identity_warning"}:
        change_row(out / "assemblies.tsv", "asm_fasta_on_osf" if corruption == "unavailable" else
                   "hq_filter", "0" if corruption == "unavailable" else "META_FAIL")
    elif corruption == "duplicate_assembly":
        rows = atb.read_rows(out / "assemblies.tsv")
        write_tsv(out / "assemblies.tsv", list(rows[0]), rows + rows)
    elif corruption == "wrong_sample_prefix":
        change_row(out / "strain_links.tsv", "sample_id", "NCBITaxon:" + SAMPLE)
    else:
        path = out / "strain_links.tsv"
        evidence = json.loads(atb.read_rows(path)[0]["sample_evidence_json"])
        if corruption == "empty_evidence":
            evidence = []
        elif corruption == "different_sample":
            evidence[0]["record_id"] = "biosample:SAMN999"
        elif corruption == "wrong_type":
            evidence[0]["record_type"] = "BIOPROJECT"
        elif corruption == "empty_source":
            evidence[0]["source"] = ""
        elif corruption == "missing_deposit":
            evidence[0].pop("matched_strain_id")
        else:
            evidence[0]["taxon_id"] = "NCBITaxon:wrong"
        change_row(path, "sample_evidence_json", json.dumps(evidence))
    # This probe exercises inner invariants even if a rewritten manifest's
    # file hashes agree; artifact integrity alone cannot prove valid evidence.
    manifest = yaml.safe_load((out / "MANIFEST.yaml").read_text())
    manifest["outputs"] = [atb.describe_output(out / name) for name in atb.OUTPUT_NAMES]
    (out / "MANIFEST.yaml").write_text(yaml.safe_dump(manifest, sort_keys=False))
    with pytest.raises(ValueError):
        atb.genome_records(out)


@pytest.mark.parametrize("value", [None, [], {}, {"release": ["2025-05"]}])
def test_non_mapping_or_incomplete_configuration_fails_cleanly(tmp_path, value):
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(value))
    with pytest.raises(ValueError):
        atb.settings(path)


@pytest.mark.parametrize("field,value", [
    ("url", "file:///tmp/source"), ("sha256", "abc"), ("release", "latest"),
    ("license", ["CC-BY-4.0"]), ("citation", ""), ("index_path", 7),
])
def test_invalid_configuration_values_are_rejected_before_fetch_or_build(pipeline, tmp_path, field, value):
    config = {**pipeline[-1], field: value}
    path = tmp_path / "bad.yaml"
    path.write_text(yaml.safe_dump(config))
    with pytest.raises(ValueError):
        atb.settings(path)


@pytest.mark.parametrize("target", ["source", "raw_input", "raw_manifest", "config", "output"])
def test_catalog_destination_cannot_overwrite_source_or_another_output(pipeline, target):
    source, index, out, raw, config = pipeline
    destination = {"source": source, "raw_input": raw / "strain_assemblies.tsv",
                   "raw_manifest": raw / "MANIFEST.yaml", "config": atb.CONFIG,
                   "output": out / "strain_links.tsv"}[target]
    before = source.read_bytes(), (raw / "strain_assemblies.tsv").read_bytes()
    with pytest.raises(ValueError):
        atb.generate(source, destination, out, raw, config, apply=True)
    assert (source.read_bytes(), (raw / "strain_assemblies.tsv").read_bytes()) == before


def test_custom_config_path_is_protected_by_cli(pipeline, monkeypatch, tmp_path):
    source, _, out, raw, config = pipeline
    custom = tmp_path / "custom-source.yaml"
    custom.write_text(yaml.safe_dump(config))
    before = custom.read_bytes()
    monkeypatch.setattr(atb, "ROOT", tmp_path)
    monkeypatch.setattr(atb, "ATB_DIR", out)
    with pytest.raises(SystemExit) as error:
        atb.main(["index", "--config", str(custom), "--metadata", str(source),
                  "--index", str(custom), "--apply"])
    assert error.value.code == 1 and custom.read_bytes() == before


def test_refresh_between_input_read_and_hash_cannot_mislabel_old_evidence(pipeline, monkeypatch):
    source, index, out, raw, config = pipeline
    original = atb.load_inputs

    def changed_after_read(path):
        result = original(path)
        change_row(path / "strain_assemblies.tsv", "assembly_name", "New source evidence")
        return result

    monkeypatch.setattr(atb, "load_inputs", changed_after_read)
    with pytest.raises(ValueError, match="changed"):
        atb.generate(*pipeline, apply=True)
    assert not index.exists() and not out.exists()


def test_late_publish_failure_rolls_back_both_index_and_crosswalk(pipeline, monkeypatch):
    source, index, out, raw, config = pipeline
    atb.generate(*pipeline, apply=True)
    before = snapshot(index, out)
    source.write_text(source.read_text().replace("JCM 18461", "JCM 99999"))
    config["sha256"] = atb.sha256(source)
    replace = atb.os.replace
    failed = False

    def fail_final_index_once(src, dst):
        nonlocal failed
        if Path(dst) == index and not failed:
            failed = True
            raise OSError("simulated final index publication failure")
        return replace(src, dst)

    monkeypatch.setattr(atb.os, "replace", fail_final_index_once)
    with pytest.raises(OSError, match="simulated"):
        atb.generate(*pipeline, apply=True)
    assert snapshot(index, out) == before


@pytest.mark.parametrize("name", atb.INPUT_NAMES)
def test_empty_source_inventories_cannot_publish_a_silently_empty_crosswalk(pipeline, name):
    source, index, out, raw, config = pipeline
    path = raw / name
    path.write_text(path.read_text().splitlines()[0] + "\n")
    with pytest.raises(ValueError):
        atb.generate(*pipeline, apply=True)
    assert not index.exists() and not out.exists()


@pytest.mark.parametrize("field,value", [("source", {}), ("inputs", []), ("outputs", []),
                                         ("extracted_at", "yesterday")])
def test_missing_or_malformed_committed_provenance_is_not_accepted(pipeline, field, value):
    _, _, out, _, _ = pipeline
    atb.generate(*pipeline, apply=True)
    path = out / "MANIFEST.yaml"
    manifest = yaml.safe_load(path.read_text())
    manifest[field] = value
    path.write_text(yaml.safe_dump(manifest, sort_keys=False))
    with pytest.raises(ValueError):
        atb.genome_records(out)


@pytest.mark.parametrize("corruption", ["summary", "missing_summary", "catalog_total", "catalog_datasets",
                                         "catalog_filters", "catalog_non_single"])
def test_provenance_checks_summaries_and_catalog_count_consistency(pipeline, monkeypatch, corruption):
    _, _, out, raw, config = pipeline
    root = raw.parent.parent
    (root / "conf").mkdir()
    (root / "conf/allthebacteria.yaml").write_text(yaml.safe_dump(config))
    monkeypatch.setattr(atb.subprocess, "check_output", lambda *a, **k:
                        "\n".join("data/atb/" + name for name in atb.OUTPUT_NAMES))
    atb.generate(*pipeline, apply=True)
    assert atb.provenance_problems(root) == []
    path = out / "MANIFEST.yaml"
    manifest = yaml.safe_load(path.read_text())
    if corruption == "summary":
        manifest["crosslinks"]["strains"] = 0
    elif corruption == "missing_summary":
        manifest.pop("crosslinks")
    elif corruption == "catalog_total":
        manifest["catalog"]["rows"] += 1
    elif corruption == "catalog_non_single":
        manifest["catalog"]["non_single_sample_rows"] = manifest["catalog"]["rows"] + 1
    else:
        manifest["catalog"][corruption.removeprefix("catalog_")] = {"incorrect": 1}
    path.write_text(yaml.safe_dump(manifest, sort_keys=False))
    assert atb.provenance_problems(root)
