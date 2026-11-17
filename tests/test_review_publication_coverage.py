"""Publication eligibility must include inventory rows, not just sampled bundles."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import subprocess
from pathlib import Path

import pytest
import yaml

from scripts.review_publication_coverage import CoverageError, audit, main, render

ROOT = Path(__file__).resolve().parents[1]
BASE = "a050e29c140f7ca7e74432e364b10d732e2922f1"
PUBLICATION = "bc4f9b4c1cb44a87acd830dd96e7b8ba2f36f6b5"
LEDGER = ROOT / "docs/review-publication-corrections/pr-169.json"


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()


def write(repo: Path, path: str, content: str) -> None:
    destination = repo / path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content)


def commit(repo: Path) -> str:
    git(repo, "add", "--force", ".")
    git(
        repo,
        "-c",
        "user.name=Coverage test",
        "-c",
        "user.email=coverage@example.invalid",
        "commit",
        "--quiet",
        "-m",
        "Fixture snapshot",
    )
    return git(repo, "rev-parse", "HEAD")


def table(columns: list[str], rows: list[dict[str, str]]) -> str:
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=columns, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def review(identifier: str, target: int, source: str, target_hash: str, *, scientific: bool = True) -> dict:
    path = f"data/taxa/archaea/record-{target}.yaml"
    return {
        "review_id": identifier,
        "kind": "record",
        "scientific_review": scientific,
        "completion": "completed",
        "verdict": "pass_with_limitations",
        "scope": {
            "reviewed_target_ids": [f"NCBITaxon:{target}"] if scientific else [],
            "coverage": "full",
            "population_size": 1,
        },
        "targets": [{"target_id": f"NCBITaxon:{target}", "path": path, "label": f"Record {target}"}],
        "source": {
            "git_revision": source,
            "state": "git_commit",
            "inputs": [{"path": path, "sha256": target_hash}],
        },
    }


def save_review(repo: Path, document: dict) -> None:
    directory = f"reviews/structured/{document['review_id']}"
    write(repo, directory + "/review.yaml", yaml.safe_dump(document, sort_keys=False))
    write(repo, directory + "/review.md", "# Preserved review rendering fixture\n")


@pytest.fixture
def history(tmp_path: Path) -> dict:
    git(tmp_path, "init", "--quiet")
    hashes = {}
    for number in range(1, 5):
        content = f"identifier: NCBITaxon:{number}\nname: Record {number}\n"
        write(tmp_path, f"data/taxa/archaea/record-{number}.yaml", content)
        hashes[number] = hashlib.sha256(content.encode()).hexdigest()
    source = commit(tmp_path)
    # Ignore rules must not remove tracked coverage inputs from enumeration.
    write(tmp_path, ".gitignore", "docs/\nreviews/\nreports/\n")
    save_review(tmp_path, review("prior-canonical", 3, source, hashes[3]))
    columns = [
        "review_id",
        "round_id",
        "target_id",
        "target_path",
        "target_sha256",
        "verdict",
        "completion",
        "scientific_review",
    ]
    write(
        tmp_path,
        "docs/structured-review-inventory/part-00.tsv",
        table(
            columns,
            [
                {
                    "review_id": "different-older-review-id",
                    "round_id": "round1",
                    "target_id": "NCBITaxon:1",
                    "target_path": "data/taxa/archaea/record-1.yaml",
                    "target_sha256": hashes[1],
                    "verdict": "needs_curation",
                    "completion": "completed",
                    "scientific_review": "true",
                }
            ],
        ),
    )
    report_path = "reports/yaml_record_review/old-record-2.md"
    report = "# Historical observation\nNCBITaxon:2\n"
    write(tmp_path, report_path, report)
    legacy_columns = ["report_path", "target_id", "target_path", "reported_verdict", "report_sha256"]
    write(
        tmp_path,
        "docs/legacy-review-inventory.tsv",
        table(
            legacy_columns,
            [
                {
                    "report_path": report_path,
                    "target_id": "NCBITaxon:2",
                    "target_path": "data/taxa/archaea/record-2.yaml",
                    "reported_verdict": "",
                    "report_sha256": hashlib.sha256(report.encode()).hexdigest(),
                }
            ],
        ),
    )
    base = commit(tmp_path)
    for number in range(1, 5):
        save_review(tmp_path, review(f"incoming-{number}", number, source, hashes[number]))
    save_review(tmp_path, review("metadata-only", 1, source, hashes[1], scientific=False))
    publication = commit(tmp_path)
    return {"repo": tmp_path, "base": base, "publication": publication, "source": source, "hashes": hashes}


def run(history: dict) -> dict:
    return audit(history["repo"], history["base"], history["publication"])


def amend_incoming(history: dict, change) -> None:
    path = history["repo"] / "reviews/structured/incoming-1/review.yaml"
    document = yaml.safe_load(path.read_text())
    change(document)
    path.write_text(yaml.safe_dump(document, sort_keys=False))
    # Keep the baseline fixed; the publication endpoint remains additions-only.
    history["publication"] = commit(history["repo"])


def test_inventory_only_coverage_excludes_target_with_different_review_id(history):
    result = run(history)
    first = result["targets"][0]
    assert first["review_id"] == "incoming-1"
    assert first["prior_canonical"] is False
    assert first["prior_structured"] is True
    assert first["eligible"] is False
    evidence = first["prior_records"][0]
    assert evidence["record_id"] == "different-older-review-id"
    assert evidence["line"] == 2
    assert evidence["verdict"] == "needs_curation"
    assert evidence["target_hash_matches_incoming_capture"] is True
    assert result["policy"]["hash_equality_is_scientific_equivalence"] is False


def test_legacy_excludes_without_promoting_unknown_scientific_status(history):
    second = run(history)["targets"][1]
    assert second["prior_legacy"] is True and second["eligible"] is False
    assert second["structured_only_eligible_informative"] is True
    evidence = second["prior_records"][0]
    assert evidence["scientific_review"] is None
    assert evidence["completion"] is None and evidence["verdict"] is None
    assert evidence["target_sha256"] is None
    assert evidence["report"]["sha256"] == evidence["row"]["report_sha256"]


def test_canonical_and_no_prior_coverage_and_metadata_exclusion(history):
    result = run(history)
    assert result["targets"][2]["prior_canonical"] is True
    assert result["targets"][2]["eligible"] is False
    assert result["targets"][3]["eligible"] is True
    assert result["summary"]["incoming_targets"] == 4
    assert result["summary"]["excluded_prior_coverage"] == 3
    assert result["excluded_incoming_bundles"][0]["review_id"] == "metadata-only"
    assert result["excluded_incoming_bundles"][0]["reason"].startswith("scientific_review_false")


def test_tracked_git_inputs_ignore_dirty_checkout_and_output_is_deterministic(history):
    before = render(run(history))
    write(history["repo"], "docs/structured-review-inventory/part-00.tsv", "broken checkout\n")
    write(history["repo"], "reviews/structured/incoming-1/review.yaml", "broken checkout\n")
    assert render(run(history)) == before


@pytest.mark.parametrize(
    "path", ["docs/legacy-review-inventory.tsv", "docs/structured-review-inventory/part-00.tsv"]
)
def test_missing_inventory_fails_closed(history, path):
    git(history["repo"], "checkout", "--quiet", history["base"])
    (history["repo"] / path).unlink()
    history["base"] = commit(history["repo"])
    save_review(history["repo"], review("new", 4, history["source"], history["hashes"][4]))
    history["publication"] = commit(history["repo"])
    with pytest.raises(CoverageError, match="Missing required"):
        run(history)


@pytest.mark.parametrize("bad_hash", ["wrong", "0" * 64])
def test_invalid_or_mismatched_git_commit_capture_fails(history, bad_hash):
    amend_incoming(history, lambda document: document["source"]["inputs"][0].update(sha256=bad_hash))
    with pytest.raises(CoverageError, match="SHA256|hash mismatch"):
        run(history)


def test_missing_target_capture_fails(history):
    amend_incoming(history, lambda document: document["source"].update(inputs=[]))
    with pytest.raises(CoverageError, match="captured target hash"):
        run(history)


def test_missing_source_commit_fails_even_for_working_tree(history):
    amend_incoming(
        history,
        lambda document: document["source"].update(
            state="working_tree",
            git_revision="f" * 40,
        ),
    )
    with pytest.raises(CoverageError, match="Git rev-parse"):
        run(history)


def test_scientific_batch_additions_do_not_silently_reduce_to_representatives(history):
    amend_incoming(history, lambda document: document.update(kind="batch"))
    with pytest.raises(CoverageError, match="one fully reviewed record"):
        run(history)


def test_baseline_metadata_observation_is_not_native_target_coverage(history):
    git(history["repo"], "checkout", "--quiet", history["base"])
    document = review("prior-metadata", 1, history["source"], history["hashes"][1], scientific=False)
    document["scope"]["reviewed_target_ids"] = ["NCBITaxon:1"]
    document["targets"][0]["path"] = "reviews/structured/prior-canonical/review.yaml"
    save_review(history["repo"], document)
    history["base"] = commit(history["repo"])
    save_review(history["repo"], review("new", 1, history["source"], history["hashes"][1]))
    history["publication"] = commit(history["repo"])
    result = run(history)
    assert result["excluded_baseline_bundles"][0]["review_id"] == "prior-metadata"
    assert result["excluded_baseline_targets"][0]["target_path"] == document["targets"][0]["path"]
    assert result["targets"][0]["prior_canonical"] is False
    assert result["targets"][0]["prior_structured"] is True


def test_non_scientific_canonical_native_record_still_excludes_publication(history):
    git(history["repo"], "checkout", "--quiet", history["base"])
    document = review("prior-deterministic", 4, history["source"], history["hashes"][4], scientific=False)
    document["scope"]["reviewed_target_ids"] = ["NCBITaxon:4"]
    save_review(history["repo"], document)
    history["base"] = commit(history["repo"])
    save_review(history["repo"], review("new", 4, history["source"], history["hashes"][4]))
    history["publication"] = commit(history["repo"])
    result = run(history)
    row = result["targets"][0]
    assert row["prior_canonical"] is True and row["eligible"] is False
    assert row["prior_structured"] is False and row["prior_legacy"] is False
    assert row["prior_records"][0]["scientific_review"] is False
    assert row["prior_records"][0]["record_id"] == "prior-deterministic"
    assert result["excluded_baseline_bundles"] == []


def test_mixed_baseline_artifact_and_native_scope_retains_native_coverage(history):
    git(history["repo"], "checkout", "--quiet", history["base"])
    document = review("prior-mixed", 4, history["source"], history["hashes"][4], scientific=False)
    document["scope"]["reviewed_target_ids"] = ["NCBITaxon:1", "NCBITaxon:4"]
    document["targets"].append(
        {"target_id": "NCBITaxon:1", "path": "reviews/structured/prior-canonical/review.yaml"}
    )
    save_review(history["repo"], document)
    history["base"] = commit(history["repo"])
    for number in [1, 4]:
        save_review(
            history["repo"], review(f"new-{number}", number, history["source"], history["hashes"][number])
        )
    history["publication"] = commit(history["repo"])
    result = run(history)
    assert result["targets"][0]["prior_canonical"] is False
    assert result["targets"][1]["prior_canonical"] is True
    assert result["targets"][1]["prior_records"][0]["scientific_review"] is False
    assert result["excluded_baseline_bundles"] == []
    assert len(result["excluded_baseline_targets"]) == 1


def test_working_tree_capture_difference_is_not_a_commit_integrity_failure(history):
    def change(document):
        document["source"]["state"] = "working_tree"
        document["source"]["inputs"][0]["sha256"] = "0" * 64

    amend_incoming(history, change)
    row = run(history)["targets"][0]
    assert row["captured_hash_matches_source_commit"] is False
    assert row["working_tree_limitation"]
    assert row["eligible"] is False
    assert row["prior_records"][0]["target_hash_matches_incoming_capture"] is False


def test_conflicting_prior_target_path_fails(history):
    git(history["repo"], "checkout", "--quiet", history["base"])
    path = history["repo"] / "docs/structured-review-inventory/part-00.tsv"
    path.write_text(path.read_text().replace("record-1.yaml", "record-4.yaml"))
    history["base"] = commit(history["repo"])
    save_review(history["repo"], review("new", 1, history["source"], history["hashes"][1]))
    history["publication"] = commit(history["repo"])
    with pytest.raises(CoverageError, match="Ambiguous prior target identity"):
        run(history)


def test_legacy_report_hash_mismatch_fails(history):
    git(history["repo"], "checkout", "--quiet", history["base"])
    write(history["repo"], "reports/yaml_record_review/old-record-2.md", "changed report\n")
    history["base"] = commit(history["repo"])
    save_review(history["repo"], review("new", 2, history["source"], history["hashes"][2]))
    history["publication"] = commit(history["repo"])
    with pytest.raises(CoverageError, match="Legacy report hash mismatch"):
        run(history)


def test_check_rejects_stale_ledger_without_rewriting_it(history, capsys):
    path = history["repo"] / "ledger.json"
    args = [
        "--repo",
        str(history["repo"]),
        "--base",
        history["base"],
        "--publication",
        history["publication"],
    ]
    assert main([*args, "--output", str(path)]) == 0
    assert main([*args, "--check", str(path)]) == 0
    assert main(["--repo", str(history["repo"]), "--check", str(path)]) == 0
    content = json.loads(path.read_text())
    content["summary"]["eligible"] += 1
    path.write_text(json.dumps(content))
    stale = path.read_bytes()
    assert main([*args, "--check", str(path)]) == 1
    assert path.read_bytes() == stale
    assert "ledger drift" in capsys.readouterr().err


def test_committed_pr_169_ledger_reproduces_from_public_history():
    # This is mandatory in this repository and CI's full-history checkout.
    # Tiny fixture repositories may deliberately omit the publication history.
    tracked = git(ROOT, "ls-files", "--", "scripts/review_publication_coverage.py")
    for revision in (BASE, PUBLICATION):
        result = subprocess.run(
            ["git", "cat-file", "-e", revision + "^{commit}"], cwd=ROOT, capture_output=True, check=False
        )
        if result.returncode:
            if not tracked:
                pytest.skip("Synthetic fixture lacks publication history")
            pytest.fail(f"Required public-history commit is unavailable: {revision}")
    result = audit(ROOT, BASE, PUBLICATION)
    assert LEDGER.read_text() == render(result)
    assert result["summary"] == {
        "incoming_scientific_reviews": 380,
        "incoming_targets": 380,
        "excluded_metadata_bundles": 1,
        "eligible": 0,
        "excluded_prior_coverage": 380,
        "prior_structured": 149,
        "prior_legacy": 231,
        "prior_canonical": 0,
        "structured_only_eligible_informative": 231,
    }
