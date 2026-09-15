"""Semantic input contracts run without a model or a complete corpus."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest
import yaml

from taxonmech import text_map_inputs as adapter


def write_record(root: Path, name: str, **extra) -> Path:
    path = root / "data" / adapter.CORPUS / "example" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {"identifier": "NCBITaxon:1", "label": "Test entity", adapter.CATEGORY_FIELD: "OTHER"}
    record.update(extra)
    path.write_text(yaml.safe_dump(record), encoding="utf-8")
    return path


def test_jsonl_contract_and_no_input_mutation(tmp_path):
    path = write_record(tmp_path, "one.yaml")
    before = path.read_bytes()
    preview = adapter.export_inputs(tmp_path, None)
    output = tmp_path / "inputs.jsonl"
    exported = adapter.export_inputs(tmp_path, output)
    row = json.loads(output.read_text())
    assert set(row) == {
        "identifier",
        "label",
        "category",
        "page",
        "source_path",
        "text",
        "text_sha256",
        "adapter_version",
    }
    assert row["text"]
    assert row["text_sha256"] == hashlib.sha256(row["text"].encode()).hexdigest()
    assert row["source_path"] == path.relative_to(tmp_path).as_posix()
    assert preview["scope"] == exported["scope"] == "full"
    assert preview["records"] == exported["records"] == 1
    assert preview["jsonl_sha256"] == exported["jsonl_sha256"]
    assert path.read_bytes() == before


def test_duplicate_identifier_refuses_partial_output(tmp_path):
    write_record(tmp_path, "a.yaml")
    write_record(tmp_path, "b.yaml")
    output = tmp_path / "inputs.jsonl"
    output.write_text("preserve me\n")
    with pytest.raises(ValueError, match="duplicate record identifier"):
        adapter.export_inputs(tmp_path, output)
    assert output.read_text() == "preserve me\n"
    assert not list(tmp_path.glob(".text-map-*"))


def test_selecting_path_outside_corpus_is_refused(tmp_path):
    write_record(tmp_path, "a.yaml")
    elsewhere = tmp_path / "elsewhere.yaml"
    elsewhere.write_text("identifier: NCBITaxon:1\nlabel: elsewhere\n")
    with pytest.raises(ValueError, match="leaves the corpus"):
        list(adapter.iter_inputs(tmp_path, records=["elsewhere.yaml"]))


def test_symlink_records_are_refused(tmp_path):
    real = write_record(tmp_path, "a.yaml")
    (real.parent / "linked.yaml").symlink_to(real)
    with pytest.raises(ValueError, match="symlink"):
        list(adapter.iter_inputs(tmp_path))


def test_subset_is_explicit_and_order_is_stable(tmp_path):
    first = write_record(tmp_path, "a.yaml")
    write_record(tmp_path, "z.yaml", identifier="NCBITaxon:2")
    output = tmp_path / "canary.jsonl"
    receipt = adapter.export_inputs(tmp_path, output, limit=1)
    assert receipt["scope"] == "subset"
    assert receipt["records"] == 1
    assert json.loads(output.read_text())["source_path"] == first.relative_to(tmp_path).as_posix()
    assert (
        adapter.export_inputs(tmp_path, None, records=[first.relative_to(tmp_path).as_posix()])["scope"]
        == "subset"
    )


def test_output_suffix_and_invalid_limit_are_refused(tmp_path):
    source = write_record(tmp_path, "a.yaml")
    with pytest.raises(ValueError, match=".jsonl"):
        adapter.export_inputs(tmp_path, source)
    with pytest.raises(ValueError, match="positive"):
        adapter.export_inputs(tmp_path, None, limit=0)


def test_taxon_canary_selects_before_parsing_unselected_yaml(tmp_path):
    write_record(tmp_path, "a.yaml")
    (tmp_path / "data" / adapter.CORPUS / "example" / "z.yaml").write_text("bad: [unterminated")
    rows = list(adapter.iter_inputs(tmp_path, limit=1))
    assert len(rows) == 1
    with pytest.raises(yaml.YAMLError):
        list(adapter.iter_inputs(tmp_path))


def test_taxon_projection_never_promotes_broad_mapping_to_synonym():
    record = {
        "identifier": "NCBITaxon:562",
        "label": "Escherichia coli",
        "taxon_domain": "BACTERIA",
        "rank": "SPECIES",
        "lineage": [{"taxon_id": "NCBITaxon:561", "taxon_label": "Escherichia"}],
        "synonyms": [{"synonym_text": "Bacterium coli", "source": "LPSN", "synonym_type": "RELATED_SYNONYM"}],
        "taxonomy_mappings": [
            {"source_label": "Klebsiella pneumoniae", "mapping_predicate": "skos:broadMatch"}
        ],
        "strains": [{"genome_assemblies": [{"assembly_id": "GCA_excluded"}]}],
        "curation_history": [{"changes": "excluded curation"}],
        "source_attestations": [{"notes": "excluded notes", "assertion_count": 123}],
    }
    text = adapter.semantic_text(record)
    assert "NCBI lineage: Escherichia" in text
    assert "synonym (LPSN; related synonym): Bacterium coli" in text
    for excluded in ("Klebsiella", "broadMatch", "NCBITaxon:", "excluded", "123"):
        assert excluded not in text
    assert adapter.page_target(record) == "taxon.html?id=NCBITaxon:562"


def test_taxon_page_refuses_non_taxon_or_unsafe_identifier():
    for identifier in ("NCBITaxon:0", "NCBITaxon:562&redirect=evil", "other:1"):
        with pytest.raises(ValueError, match="explicit NCBI"):
            adapter.page_target({"identifier": identifier})
