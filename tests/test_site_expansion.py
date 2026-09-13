"""Large-corpus browsing and publication retain all records and evidence."""

from __future__ import annotations

import gzip
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest
from jinja2 import Environment, FileSystemLoader, select_autoescape

from scripts.build_pages_artifact import stage
from taxonmech.report import summarize

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "src/taxonmech/templates"


def test_static_pagination_reaches_every_record(monkeypatch, tmp_path):
    monkeypatch.syspath_prepend(str(ROOT / "scripts"))
    from scripts.render_pages import write_browse_pages

    env = Environment(loader=FileSystemLoader(str(TEMPLATES)), autoescape=select_autoescape(["html"]))
    records = [{"identifier": f"NCBITaxon:{i}", "label": f"Taxon <{i}>", "rank": "SPECIES",
                "domain": "BACTERIA", "sources": ["NCBITAXON"], "strain_count": 0,
                "genomes": 0, "status": "SEEDED", "page": f"taxa/bacteria/taxon_{i}.html"}
               for i in range(451)]
    write_browse_pages(env, tmp_path, "domain/bacteria", records, root="../", domain="BACTERIA")
    found = []
    for name, count in [("bacteria.html", 200), ("bacteria-2.html", 200), ("bacteria-3.html", 51)]:
        text = (tmp_path / "domain" / name).read_text()
        ids = re.findall(r"<code>(NCBITaxon:\d+)</code>", text)
        assert len(ids) == count
        assert "Taxon <" not in text
        found.extend(ids)
        for link in re.findall(r'href="(../domain/[^"]+)"', text):
            assert (tmp_path / "domain" / link).resolve().is_file()
    assert found == [row["identifier"] for row in records]
    write_browse_pages(env, tmp_path, "empty", [])
    assert "0 records · page 1 of 1" in (tmp_path / "empty.html").read_text()


def test_distinct_strains_are_separate_from_occurrences():
    doc = {"strain_count": 3, "strains": [{"strain_id": "kgmicrobe.strain:bacdive_1"},
                                        {"strain_id": "kgmicrobe.strain:bacdive_2"}]}
    stats = summarize([(Path("species.yaml"), doc), (Path("strain.yaml"), doc)])
    assert stats["strain_total"] == 6
    assert stats["strains_listed"] == 4
    assert stats["distinct_strains_listed"] == 2


@pytest.fixture
def publication(tmp_path):
    root = tmp_path / "repo"
    (root / "pages").mkdir(parents=True)
    (root / "index.html").write_text("pages/index.html")
    (root / ".nojekyll").touch()
    (root / "pages/index.html").write_text("site")
    (root / "private-inventory.tsv").write_text("must not publish")
    return root, tmp_path / "artifact"


def test_publication_retains_urls_and_excludes_non_site_files(publication):
    root, out = publication
    total = stage(None, root=root)
    assert not out.exists()
    assert stage(out, root=root) == total == len("pages/index.htmlsite")
    assert sorted(str(p.relative_to(out)) for p in out.rglob("*") if p.is_file()) == [
        ".nojekyll", "index.html", "pages/index.html"]


def test_oversized_artifact_is_rejected_before_writing(publication):
    root, out = publication
    with pytest.raises(ValueError, match="publication budget"):
        stage(out, root=root, limit=1)
    assert not out.exists()


def test_publication_rejects_links_and_recursive_output(publication):
    root, out = publication
    with pytest.raises(ValueError, match="outside the repository"):
        stage(root / "pages/staging", root=root)
    (root / "pages/leak").symlink_to(root / "private-inventory.tsv")
    with pytest.raises(ValueError, match="symbolic link"):
        stage(out, root=root)
    assert not out.exists()


@pytest.mark.skipif(shutil.which("node") is None, reason="Node is needed for browser execution")
@pytest.mark.parametrize("native", ["native", "missing", "broken"])
def test_gzip_browser_loader_decodes_and_rejects_errors(native):
    script = r"""
const fs = require('fs'), vm = require('vm'), assert = require('assert');
global.window = global;
global.document = {querySelectorAll: () => []};
global.fflate = require(process.argv[1]);
if (process.argv[3] === 'missing') global.DecompressionStream = undefined;
if (process.argv[3] === 'broken') global.DecompressionStream = class {constructor() {throw Error('broken');}};
vm.runInThisContext(fs.readFileSync(process.argv[2], 'utf8'));
const payload = Uint8Array.from(Buffer.from(process.argv[4], 'base64'));
(async () => {
  assert.deepStrictEqual(JSON.parse(await TaxonMechData.decodeGzip(payload)), {evidence: 'DSM 1 → Ω'});
  global.fetch = async () => new Response(payload);
  assert.deepStrictEqual(await TaxonMechData.loadJSON('detail.json.gz'), {evidence: 'DSM 1 → Ω'});
  global.fetch = async () => new Response('missing', {status: 404});
  await assert.rejects(TaxonMechData.loadJSON('detail.json.gz'));
  await assert.rejects(TaxonMechData.decodeGzip(new Uint8Array([1, 2, 3])));
})().catch(error => {console.error(error); process.exitCode = 1;});
"""
    import base64

    payload = base64.b64encode(gzip.compress(json.dumps({"evidence": "DSM 1 → Ω"}).encode())).decode()
    result = subprocess.run(["node", "-e", script, str(TEMPLATES / "vendor/fflate-0.8.2.js"),
                             str(TEMPLATES / "compressed-data.js"), native, payload],
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_vendored_decoder_matches_reviewed_package():
    assert hashlib.sha256((TEMPLATES / "vendor/fflate-0.8.2.js").read_bytes()).hexdigest() == (
        "c3b34f2e9f5e74d4d7d64e01cac7a0c01954c6c406414d42185c7b53d6875ddf")
    assert "MIT License" in (TEMPLATES / "vendor/fflate-LICENSE.txt").read_text()


@pytest.mark.skipif(shutil.which("node") is None, reason="Node is needed for browser execution")
def test_shipped_taxon_browser_searches_beyond_the_first_page():
    result = subprocess.run(["node", str(Path(__file__).with_name("taxon_browser_harness.cjs")),
                             str(TEMPLATES / "taxon-browser.js")], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert "Complete-corpus search and bounded pagination passed" in result.stdout
