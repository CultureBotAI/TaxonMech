"""Committed raw inventories have complete, byte-checked provenance."""

from __future__ import annotations

from copy import deepcopy

import yaml

from scripts import check_provenance


def test_every_committed_raw_tsv_has_valid_provenance():
    assert not check_provenance.problems()


def _manifest():
    return yaml.safe_load(check_provenance.MANIFEST.read_text(encoding="utf-8"))


def test_source_commit_is_required():
    manifest = _manifest()
    manifest["kg_microbe_source"] = "kg-microbe@unknown"
    assert any("kg_microbe_source" in f for f in check_provenance.manifest_contract_problems(manifest))


def test_output_integrity_fields_are_required():
    for field in ("rows", "bytes", "sha256"):
        broken = deepcopy(_manifest())
        del broken["outputs"][0][field]
        assert any(f"missing {field}" in f for f in check_provenance.manifest_contract_problems(broken))
