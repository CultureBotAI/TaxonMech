"""Required checks must evaluate both PRs and native merge-group commits."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_WORKFLOWS = {"main.yaml": ["qc (3.10)", "qc (3.12)"], "vendored-sync.yaml": ["vendored-sync"]}


@pytest.mark.parametrize("filename", REQUIRED_WORKFLOWS)
def test_required_workflow_reports_for_every_pr_and_merge_group(filename):
    document = yaml.safe_load((ROOT / ".github/workflows" / filename).read_text())
    events = document.get("on", document.get(True))
    assert "pull_request" in events
    assert not events["pull_request"], "workflow filters can leave a required PR check pending"
    assert events["merge_group"] == {"types": ["checks_requested"]}
    assert document["permissions"] == {"contents": "read"}
    concurrency = document["concurrency"]
    assert concurrency["cancel-in-progress"] == "${{ github.event_name == 'pull_request' }}"
    assert "github.run_id" in concurrency["group"]
    for job in document["jobs"].values():
        assert "if" not in job, "a required job must not skip the queue commit"
        for step in job.get("steps", []):
            if step.get("uses", "").startswith("actions/checkout@"):
                assert "ref" not in step.get("with", {}), "checkout must evaluate the event's combined commit"


def test_required_job_contexts_remain_stable():
    for filename, expected in REQUIRED_WORKFLOWS.items():
        document = yaml.safe_load((ROOT / ".github/workflows" / filename).read_text())
        observed = []
        for job_id, job in document["jobs"].items():
            versions = job.get("strategy", {}).get("matrix", {}).get("python-version")
            if "uses" in job:
                observed.append(f"{job_id} / {job_id}")
            elif versions:
                for version in versions:
                    name = job.get("name")
                    observed.append(
                        name.replace("${{ matrix.python-version }}", version)
                        if name
                        else f"{job_id} ({version})"
                    )
            else:
                observed.append(job.get("name", job_id))
        assert sorted(observed) == sorted(expected)
