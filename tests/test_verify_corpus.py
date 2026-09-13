"""The corpus-reproducibility gate, and proof that it fails on drift."""

from __future__ import annotations

import pytest

from scripts import verify_corpus
from taxonmech import seed
from taxonmech.validation.write_validated import write_validated_taxon
from tests.test_seed import _inventory


@pytest.fixture(scope="module")
def corpus_matches() -> int:
    return verify_corpus.main([])


def test_committed_corpus_reproduces_from_data_raw(corpus_matches):
    assert corpus_matches == 0, (
        "data/taxa/ is not what data/raw/ + curation/seed_scope.tsv produce. Re-seed with "
        "`just seed-apply --force --prune`, or if the change was intended, make it in the seeder."
    )


@pytest.mark.parametrize("mutation", ["tampered", "missing", "extra"])
def test_verifier_rejects_drift_without_mutating_the_real_corpus(tmp_path, monkeypatch, mutation):
    """Exercise failure paths on real generated records in an isolated tiny corpus."""
    taxa = tmp_path / "data/taxa"
    inv = _inventory()
    corpus = seed.Corpus(seed.build_concepts(inv, ["NCBITaxon:562", "NCBITaxon:83333"]), inv, {})
    monkeypatch.setattr(seed, "TAXA_DIR", taxa)
    monkeypatch.setattr(verify_corpus, "TAXA_DIR", taxa)
    monkeypatch.setattr(verify_corpus, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(verify_corpus, "build_corpus", lambda: corpus)
    monkeypatch.setattr(verify_corpus, "load_lockfile", dict)
    paths, _ = seed.assign_paths(corpus.concepts)
    for concept in corpus.concepts:
        write_validated_taxon(seed.build_document(concept, inv), paths[concept.identifier])
    assert verify_corpus.main([]) == 0
    victim = paths["NCBITaxon:562"]
    original = victim.read_text(encoding="utf-8")
    if mutation == "tampered":
        victim.write_text(original.replace("label:", "label: TAMPERED", 1), encoding="utf-8")
    elif mutation == "missing":
        victim.unlink()
    else:
        (victim.parent / "extra.yaml").write_text(original, encoding="utf-8")
    assert verify_corpus.main([]) == 1
