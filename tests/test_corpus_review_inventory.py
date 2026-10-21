"""Full-corpus review coverage is an auditable inventory, not a blanket scientific pass."""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest
import yaml

from scripts import corpus_review_inventory as cri

Dumper = getattr(yaml, "CSafeDumper", yaml.SafeDumper)


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


@pytest.fixture
def sample_repo(tmp_path: Path) -> Path:
    (tmp_path / "data/taxa/bacteria").mkdir(parents=True)
    (tmp_path / "docs/structured-review-inventory").mkdir(parents=True)
    (tmp_path / "reviews/structured/20261018T000000Z-structured-review-shard-part-00").mkdir(
        parents=True
    )

    (tmp_path / "data/taxa/PATHS.tsv").write_text(
        "identifier\tslug\nNCBITaxon:100\tlegacy_taxon\nNCBITaxon:200\tstructured_taxon\n",
        encoding="utf-8",
    )
    legacy_yaml = "identifier: NCBITaxon:100\nlabel: Legacy taxon\n"
    struct_yaml = "identifier: NCBITaxon:200\nlabel: Structured taxon\n"
    (tmp_path / "data/taxa/bacteria/legacy_taxon.yaml").write_text(
        legacy_yaml, encoding="utf-8"
    )
    (tmp_path / "data/taxa/bacteria/structured_taxon.yaml").write_text(
        struct_yaml, encoding="utf-8"
    )

    (tmp_path / "docs/legacy-review-inventory.tsv").write_text(
        "report_path\ttarget_id\ttarget_path\treported_verdict\treported_started_utc\t"
        "reported_finished_utc\tmissing_metadata\tmissing_sections\treport_sha256\n"
        "reports/yaml_record_review/20260101T000000Z-legacy_taxon.md\tNCBITaxon:100\t"
        "data/taxa/bacteria/legacy_taxon.yaml\tpass\t2026-01-01T00:00:00Z\t"
        "2026-01-01T00:01:00Z\t\t\t" + ("a" * 64) + "\n",
        encoding="utf-8",
    )

    struct_sha = _sha256_text(struct_yaml)
    shard_rel = "docs/structured-review-inventory/part-00.tsv"
    shard_text = (
        "\t".join(cri.INVENTORY_COLUMNS)
        + "\n"
        + "\t".join(
            [
                "20261018T000000Z-round25-b01-200",
                "round25-b01",
                "NCBITaxon:200",
                "data/taxa/bacteria/structured_taxon.yaml",
                struct_sha,
                "Structured taxon",
                "needs_curation",
                "completed",
                "true",
                "1",
                "2026-10-18T00:00:00Z",
                "2026-10-18T00:01:00Z",
            ]
        )
        + "\n"
    )
    (tmp_path / shard_rel).write_text(shard_text, encoding="utf-8")

    id_to_slug, existing_paths = cri.load_corpus_targets(tmp_path)
    shard_rows_by_rel, _ = cri.load_structured_shards(
        tmp_path, id_to_slug, existing_paths
    )
    batch_rows = cri.build_batch_rows(shard_rows_by_rel)
    batches_text = cri.render_batches(batch_rows)
    (tmp_path / cri.BATCHES_TSV).write_text(batches_text, encoding="utf-8")

    bundle_doc = {
        "schema_version": "1.0.0",
        "review_id": "20261018T000000Z-structured-review-shard-part-00",
        "kind": "batch",
        "scope": {"population_size": 1},
        "source": {
            "inputs": [
                {"path": shard_rel, "sha256": _sha256_text(shard_text), "role": "context"},
                {
                    "path": cri.BATCHES_TSV.as_posix(),
                    "sha256": _sha256_text(batches_text),
                    "role": "context",
                },
            ]
        },
    }
    (
        tmp_path
        / "reviews/structured/20261018T000000Z-structured-review-shard-part-00/review.yaml"
    ).write_text(yaml.dump(bundle_doc, Dumper=Dumper), encoding="utf-8")
    return tmp_path


def test_synthetic_partition_and_target_sha256_verification(sample_repo: Path) -> None:
    summary = cri.check(sample_repo, verify_target_sha256=True)
    assert summary["corpus_records"] == 2
    assert summary["legacy_records"] == 1
    assert summary["structured_records"] == 1
    assert summary["overlap_records"] == 0
    assert summary["unreviewed_records"] == 0
    assert summary["structured_verdicts_not_promoted"] == {"needs_curation": 1}


def test_overlap_between_legacy_and_structured_is_rejected(sample_repo: Path) -> None:
    (sample_repo / "data/taxa/PATHS.tsv").write_text(
        "identifier\tslug\nNCBITaxon:100\tlegacy_taxon\n",
        encoding="utf-8",
    )
    shard_path = sample_repo / "docs/structured-review-inventory/part-00.tsv"
    shard_path.write_text(
        shard_path.read_text(encoding="utf-8")
        .replace("NCBITaxon:200", "NCBITaxon:100")
        .replace("structured_taxon", "legacy_taxon"),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="overlap between legacy and structured"):
        cri.check(sample_repo)


def test_unreviewed_corpus_record_is_rejected(sample_repo: Path) -> None:
    (sample_repo / "data/taxa/PATHS.tsv").write_text(
        (sample_repo / "data/taxa/PATHS.tsv").read_text(encoding="utf-8")
        + "NCBITaxon:300\tunreviewed_taxon\n",
        encoding="utf-8",
    )
    (sample_repo / "data/taxa/bacteria/unreviewed_taxon.yaml").write_text(
        "identifier: NCBITaxon:300\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="unreviewed corpus records remaining"):
        cri.check(sample_repo)


def test_tampered_target_yaml_sha256_is_rejected(sample_repo: Path) -> None:
    (sample_repo / "data/taxa/bacteria/structured_taxon.yaml").write_text(
        "identifier: NCBITaxon:200\nlabel: Tampered\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="target_sha256 mismatch"):
        cri.check(sample_repo, verify_target_sha256=True)


def test_batch_summary_drift_is_rejected(sample_repo: Path) -> None:
    (sample_repo / cri.BATCHES_TSV).write_text("drifted\n", encoding="utf-8")
    with pytest.raises(ValueError, match="structured-review-batches.tsv drift"):
        cri.check(sample_repo)


def test_multi_shard_append_requires_latest_shard_context_hashes(sample_repo: Path) -> None:
    (sample_repo / "data/taxa/PATHS.tsv").write_text(
        (sample_repo / "data/taxa/PATHS.tsv").read_text(encoding="utf-8")
        + "NCBITaxon:300\tsecond_taxon\n",
        encoding="utf-8",
    )
    second_yaml = "identifier: NCBITaxon:300\nlabel: Second taxon\n"
    (sample_repo / "data/taxa/bacteria/second_taxon.yaml").write_text(
        second_yaml, encoding="utf-8"
    )
    second_sha = _sha256_text(second_yaml)
    shard1_rel = "docs/structured-review-inventory/part-01.tsv"
    shard1_text = (
        "\t".join(cri.INVENTORY_COLUMNS)
        + "\n"
        + "\t".join(
            [
                "20261019T000000Z-round26-b01-300",
                "round26-b01",
                "NCBITaxon:300",
                "data/taxa/bacteria/second_taxon.yaml",
                second_sha,
                "Second taxon",
                "pass",
                "completed",
                "true",
                "0",
                "2026-10-19T00:00:00Z",
                "2026-10-19T00:01:00Z",
            ]
        )
        + "\n"
    )
    (sample_repo / shard1_rel).write_text(shard1_text, encoding="utf-8")
    id_to_slug, existing_paths = cri.load_corpus_targets(sample_repo)
    shard_rows_by_rel, _ = cri.load_structured_shards(
        sample_repo, id_to_slug, existing_paths
    )
    batches_text = cri.render_batches(cri.build_batch_rows(shard_rows_by_rel))
    (sample_repo / cri.BATCHES_TSV).write_text(batches_text, encoding="utf-8")
    paths_sha = _sha256_text(
        (sample_repo / "data/taxa/PATHS.tsv").read_text(encoding="utf-8")
    )

    bundle1_dir = (
        sample_repo
        / "reviews/structured/20261019T000000Z-structured-review-shard-part-01"
    )
    bundle1_dir.mkdir(parents=True)
    bundle1_doc = {
        "schema_version": "1.0.0",
        "review_id": "20261019T000000Z-structured-review-shard-part-01",
        "kind": "batch",
        "scope": {"population_size": 1},
        "source": {
            "inputs": [
                {"path": shard1_rel, "sha256": _sha256_text(shard1_text), "role": "context"},
                {
                    "path": cri.BATCHES_TSV.as_posix(),
                    "sha256": _sha256_text(batches_text),
                    "role": "context",
                },
                {
                    "path": "data/taxa/PATHS.tsv",
                    "sha256": paths_sha,
                    "role": "context",
                },
            ]
        },
    }
    (bundle1_dir / "review.yaml").write_text(
        yaml.dump(bundle1_doc, Dumper=Dumper), encoding="utf-8"
    )
    summary = cri.check(sample_repo, verify_target_sha256=True)
    assert summary["structured_shards"] == 2
    assert summary["structured_records"] == 2

    bundle1_doc["source"]["inputs"][2]["sha256"] = "0" * 64
    (bundle1_dir / "review.yaml").write_text(
        yaml.dump(bundle1_doc, Dumper=Dumper), encoding="utf-8"
    )
    with pytest.raises(ValueError, match="stale SHA256 for data/taxa/PATHS.tsv"):
        cri.check(sample_repo, verify_target_sha256=True)


def test_committed_corpus_review_inventory_is_complete_and_valid() -> None:
    summary = cri.check(cri.ROOT, verify_target_sha256=False)
    assert summary["corpus_records"] == 626048
    assert summary["legacy_records"] == 23883
    assert summary["structured_records"] == 602165
    assert summary["overlap_records"] == 0
    assert summary["unreviewed_records"] == 0
    assert summary["structured_shards"] == 14
    assert summary["structured_batches"] == 611
    assert sum(summary["structured_verdicts_not_promoted"].values()) == 602165
