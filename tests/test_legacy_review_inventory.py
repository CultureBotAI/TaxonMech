"""Historical file coverage is not a scientific or structured-review verdict."""

import os
import subprocess
from pathlib import Path

import pytest

from scripts import legacy_review_inventory as archive


@pytest.fixture
def sample(tmp_path):
    (tmp_path / "data/taxa/bacteria").mkdir(parents=True)
    (tmp_path / "data/taxa/PATHS.tsv").write_text("identifier\tslug\nNCBITaxon:123\tfixture\n")
    (tmp_path / "data/taxa/bacteria/fixture.yaml").write_text("identifier: NCBITaxon:123\n")
    (tmp_path / archive.REPORTS).mkdir(parents=True)
    report = tmp_path / archive.REPORTS / "20260101T000000Z-fixture.md"
    report.write_text(
        "# Historical observation\n\n- Target: `data/taxa/bacteria/fixture.yaml`\n"
        "- Taxon: `NCBITaxon:123`\n\n## Target\n\n## Findings\n\nNone found.\n"
    )
    return tmp_path, report


def test_missing_metadata_is_not_inferred_from_filename_or_findings(sample):
    root, _ = sample
    row, = archive.inventory(root)
    assert row["reported_verdict"] == ""
    assert row["reported_started_utc"] == row["reported_finished_utc"] == ""
    assert row["missing_metadata"] == "Repository;Started UTC;Finished UTC;Verdict"
    assert "Validation" in row["missing_sections"]
    assert archive.summary([row])["reported_verdicts_not_reassessed"] == {"NOT_RECORDED": 1}


def test_preserve_nonpass_metadata_and_content_hash(sample):
    root, report = sample
    original = archive.inventory(root)[0]
    report.write_text(report.read_text() + "\n- Verdict: needs curation\n")
    current = archive.inventory(root)[0]
    assert current["reported_verdict"] == "needs curation"
    assert current["report_sha256"] != original["report_sha256"]
    assert archive.render([current]) == archive.render(archive.inventory(root))


def test_duplicate_ignored_report_is_not_hidden(sample):
    root, report = sample
    hidden = report.parent / ".hidden"
    hidden.mkdir()
    (root / ".gitignore").write_text("reports/\n")
    (hidden / report.name).write_bytes(report.read_bytes())
    with pytest.raises(ValueError, match="duplicate report target"):
        archive.inventory(root)


@pytest.mark.parametrize("change", ["wrong_id", "id_suffix", "wrong_path", "missing_target", "symlink"])
def test_bad_target_is_rejected(sample, change):
    root, report = sample
    if change == "wrong_id":
        report.write_text(report.read_text().replace("NCBITaxon:123", "NCBITaxon:1234"))
    elif change == "id_suffix":
        report.write_text(report.read_text().replace("NCBITaxon:123", "NCBITaxon:123A"))
    elif change == "wrong_path":
        report.write_text(report.read_text().replace("bacteria/fixture", "bacteria/not_fixture"))
    elif change == "missing_target":
        (root / "data/taxa/bacteria/fixture.yaml").unlink()
    else:
        (report.parent / "alias.md").symlink_to(report)
    with pytest.raises(ValueError):
        archive.inventory(root)


def test_duplicate_metadata_is_rejected(sample):
    root, report = sample
    report.write_text(report.read_text() + "\n- Verdict: pass\n- Verdict: needs curation\n")
    with pytest.raises(ValueError, match="duplicate metadata"):
        archive.inventory(root)


def test_index_drift_and_historical_rewrite_are_rejected(sample):
    root, report = sample
    (root / "docs").mkdir()
    index = root / archive.INDEX
    index.write_text(archive.render(archive.inventory(root)))
    for args in (
        ("init", "-q"), ("config", "user.name", "Archive fixture"),
        ("config", "user.email", "fixture@example.invalid"), ("add", "."),
        ("-c", "commit.gpgsign=false", "commit", "-qm", "fixture"),
    ):
        subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)
    archive.check(root, "HEAD")
    index.write_text("wrong inventory\n")
    with pytest.raises(ValueError, match="inventory drift"):
        archive.check(root, "HEAD")
    report.write_text(report.read_text() + "\n- Verdict: pass\n")
    index.write_text(archive.render(archive.inventory(root)))
    with pytest.raises(ValueError, match="historical report changed"):
        archive.check(root, "HEAD")
    with pytest.raises(subprocess.CalledProcessError):
        archive.assert_preserved(root, "nonexistent-base")


def test_committed_archive_matches_inventory():
    root = Path(__file__).resolve().parents[1]
    archive.check(root, os.environ.get("RECORD_REVIEW_BASE") or "HEAD")
