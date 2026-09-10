"""The corpus-reproducibility gate, and proof that it fails on drift."""

from __future__ import annotations

import pytest

from scripts import verify_corpus


@pytest.fixture(scope="module")
def corpus_matches() -> int:
    return verify_corpus.main([])


def test_committed_corpus_reproduces_from_data_raw(corpus_matches):
    assert corpus_matches == 0, (
        "data/taxa/ is not what data/raw/ + curation/seed_scope.tsv produce. Re-seed with "
        "`just seed-apply --force --prune`, or if the change was intended, make it in the seeder."
    )


def test_verifier_fails_on_a_tampered_record(repo_root):
    """Guard against a vacuous pass."""
    taxa = repo_root / "data" / "taxa"
    victim = next(taxa.rglob("*.yaml"))
    original = victim.read_text(encoding="utf-8")
    try:
        victim.write_text(original.replace("label:", "label: TAMPERED", 1), encoding="utf-8")
        assert verify_corpus.main([]) == 1
    finally:
        victim.write_text(original, encoding="utf-8")
    assert verify_corpus.main([]) == 0
