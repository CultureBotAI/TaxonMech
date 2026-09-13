"""Smoke tests for the CLI scripts against the committed corpus."""

from __future__ import annotations

import base64
import gzip
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

REPO_ROOT = Path(__file__).resolve().parents[1]


def _run(*args, cwd=REPO_ROOT):
    return subprocess.run([sys.executable, *args], cwd=cwd, capture_output=True, text=True, check=False)


def test_seed_dry_run_writes_nothing(repo_root):
    before = sorted(p.stat().st_mtime for p in (repo_root / "data" / "taxa").rglob("*.yaml"))
    out = _run("scripts/seed_from_sources.py")
    assert out.returncode == 0, out.stderr
    assert "--dry-run" in out.stdout
    after = sorted(p.stat().st_mtime for p in (repo_root / "data" / "taxa").rglob("*.yaml"))
    assert before == after


def test_seed_refuses_an_identifier_outside_scope():
    out = _run("scripts/seed_from_sources.py", "--apply", "--only", "NCBITaxon:999999999")
    assert out.returncode == 2
    assert "not in scope" in out.stderr


def test_validate_strict_passes_on_corpus(tmp_path):
    out = _run("scripts/validate_strict.py", "--quiet", "--out", str(tmp_path / "f.tsv"))
    assert out.returncode == 0, out.stderr


def test_render_check_is_current():
    out = _run("scripts/render_pages.py", "--check")
    assert out.returncode == 0, out.stderr


def test_corpus_report_runs():
    out = _run("scripts/corpus_report.py")
    assert out.returncode == 0, out.stderr
    assert "taxon records" in out.stdout


def test_propose_scope_runs_and_proposes_only_unscoped_taxa():
    from taxonmech.seed import load_scope

    out = _run("scripts/propose_scope.py", "--rule", "core", "--top", "5", "--append")
    assert out.returncode == 0, out.stderr
    in_scope = set(load_scope())
    proposed = [line.split("\t")[0] for line in out.stdout.splitlines() if line.startswith("NCBITaxon:")]
    assert not set(proposed) & in_scope


def test_rendered_site_has_no_broken_local_links(tmp_path):
    """Every relative href/src in the rendered site must resolve to a file in
    the output tree."""
    out = tmp_path / "site"
    res = _run("scripts/render_pages.py", "--out", str(out))
    assert res.returncode == 0, res.stderr
    broken = []
    for html in out.rglob("*.html"):
        text = html.read_text(encoding="utf-8")
        for encoded in re.findall(r'data-gzip-content="([^"]+)"', text):
            text += gzip.decompress(base64.b64decode(encoded)).decode("utf-8")
        for m in re.finditer(r'(?:href|src)="([^"]+)"', text):
            url = urlsplit(m.group(1))
            if url.scheme or url.netloc or not url.path:
                continue
            if not (html.parent / unquote(url.path)).resolve().is_file():
                broken.append(f"{html.relative_to(out)}: {m.group(1)}")
    assert not broken, broken


def test_the_site_root_opts_out_of_jekyll():
    assert (REPO_ROOT / ".nojekyll").exists()
    assert (REPO_ROOT / "pages" / ".nojekyll").exists()
