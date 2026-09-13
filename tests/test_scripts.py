"""Smoke tests for the CLI scripts against the committed corpus."""

from __future__ import annotations

import base64
import gzip
import html as html_module
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

import pytest

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


@pytest.mark.qc_gate
def test_validate_strict_passes_on_corpus(tmp_path):
    out = _run("scripts/validate_strict.py", "--quiet", "--out", str(tmp_path / "f.tsv"))
    assert out.returncode == 0, out.stderr


@pytest.mark.qc_gate
def test_render_check_is_current():
    out = _run("scripts/render_pages.py", "--check")
    assert out.returncode == 0, out.stderr


@pytest.mark.qc_gate
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


def test_rendered_site_has_no_broken_local_links():
    """Every relative href/src in the rendered site must resolve to a file in
    the output tree."""
    # The render-reproduction test verifies generation separately. Audit the
    # published bytes, including every deferred record and strain page.
    from taxonmech.seed import load_scope

    out = REPO_ROOT / "pages"
    scope = set(load_scope())
    broken, checked, seen = [], set(), set()

    def check_links(html, text):
        for encoded in re.findall(r'data-gzip-content="([^"]+)"', text):
            text += gzip.decompress(base64.b64decode(encoded)).decode("utf-8")
        for m in re.finditer(r'(?:href|src)="([^"]+)"', text):
            url = urlsplit(html_module.unescape(m.group(1)))
            if url.scheme or url.netloc or not url.path:
                continue
            key = (html.parent, url.path)
            if key not in checked and not (html.parent / unquote(url.path)).resolve().is_file():
                broken.append(f"{html.relative_to(out)}: {m.group(1)}")
            checked.add(key)
            if url.path.endswith("taxon.html"):
                identifier = parse_qs(url.query).get("id", [None])[0]
                if identifier not in scope:
                    broken.append(f"unpublished taxon target: {m.group(1)}")

    for html in out.rglob("*.html"):
        check_links(html, html.read_text(encoding="utf-8"))
    for shard in sorted((out / "taxon-details").glob("*.json.gz")):
        data = json.loads(gzip.decompress(shard.read_bytes()))
        assert not seen.intersection(data), f"duplicate published taxon in {shard}"
        for identifier, row in data.items():
            assert int(identifier.split(":")[1]) // 1000 == int(shard.name.split(".")[0])
            check_links(out / "taxon.html", row["html"])
            for page in row["strain_pages"]:
                check_links(out / "taxon.html", page["html"])
        seen.update(data)
    assert seen == scope, "published detail shards must cover the entire explicit scope"
    assert not broken, broken


def test_the_site_root_opts_out_of_jekyll():
    assert (REPO_ROOT / ".nojekyll").exists()
    assert (REPO_ROOT / "pages" / ".nojekyll").exists()
