"""Regressions for the independently reported website defects (#96–104)."""

import gzip
import importlib
import json
import re
from copy import deepcopy

import pytest

from tests.rendered_taxon import rendered_taxon


@pytest.fixture
def audited_site(repo_root, tmp_path, monkeypatch):
    monkeypatch.syspath_prepend(str(repo_root / "scripts"))
    renderer = importlib.import_module("render_pages")
    parent = {
        "identifier": "NCBITaxon:2173", "label": "Methanobrevibacter smithii", "rank": "SPECIES",
        "taxon_domain": "ARCHAEA", "mapping_status": "SEEDED", "strain_count": 1,
        "source_attestations": [{"source": "GTDB", "assertion_count": 514,
                                 "assertion_unit": "GENOMES", "mapping_predicate": "skos:broadMatch"}],
        "taxonomy_mappings": [
            {"source": "GTDB", "source_id": "GTDB:s__Gemmiger_qucibialis",
             "genome_count": 514, "mapping_predicate": "skos:broadMatch"},
            {"source": "GTDB", "source_id": "GTDB:s__Methanocatella_smithii",
             "genome_count": 194, "mapping_predicate": "skos:closeMatch"},
        ],
        "xrefs": ["lpsn:777826"],
    }
    child = {
        "identifier": "NCBITaxon:9999", "label": "Fixture strain", "rank": "STRAIN",
        "taxon_domain": "ARCHAEA", "mapping_status": "SEEDED", "parent_taxon": "NCBITaxon:2173",
        "lineage": [
            {"taxon_id": "NCBITaxon:2157", "taxon_label": "Archaea", "rank": "SUPERKINGDOM"},
            {"taxon_id": "NCBITaxon:2173", "taxon_label": parent["label"], "rank": "SPECIES"},
        ],
    }
    records = [(renderer.TAXA_DIR / "archaea" / f"fixture_{i}.yaml", doc)
               for i, doc in enumerate([parent, child])]
    unchanged = deepcopy(records)
    monkeypatch.setattr(renderer, "load_records", lambda: records)
    output = tmp_path / "site"
    renderer.render(output)
    assert records == unchanged, "Publishing must not rewrite scientific records"
    return renderer, output


def test_pooled_mappings_are_not_taxon_genome_totals(audited_site):
    _, output = audited_site
    index = json.loads(gzip.decompress((output / "index.json.gz").read_bytes()))
    record = next(row for row in index if row["identifier"] == "NCBITaxon:2173")
    assert "genomes" not in record
    assert record["gtdb_mapping_count"] == 2
    assert record["gtdb_pooled_mapping_count"] == 1
    browse = (output / "browse.html").read_text()
    assert "GTDB mappings" in browse and "1 pooled" in browse
    assert "514" not in browse
    detail = rendered_taxon(output, "NCBITaxon:2173")
    for retained in ("514", "194", "skos:broadMatch", "skos:closeMatch"):
        assert retained in detail


def test_sources_are_visible_discoverable_and_scrollable(audited_site):
    _, output = audited_site
    html = (output / "sources.html").read_text()
    title = re.search(r"<title>(.*?)</title>", html, re.DOTALL).group(1)
    assert title == "Source coverage · TaxonMech"
    assert "<h2>Attribution</h2>" in html.split("</head>", 1)[1]
    assert html.count('class="table-scroll" role="region" tabindex="0"') == html.count("<table") == 3
    assert 'href="sources.html"' in (output / "index.html").read_text()


def test_local_lineage_links_require_actual_records(audited_site):
    _, output = audited_site
    child = rendered_taxon(output, "NCBITaxon:9999")
    parent = rendered_taxon(output, "NCBITaxon:2173")
    assert 'href="taxon.html?id=NCBITaxon:2173"' in child
    assert 'href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2173"' in child
    assert 'href="taxon.html?id=NCBITaxon:2157"' not in child
    assert 'href="taxon.html?id=NCBITaxon:9999"' in parent
    assert "1 child taxon records" in parent
    assert "inventory,," not in parent
    assert json.loads((output / "taxon-details/index.json").read_text()) == {"buckets": ["0002", "0009"]}


def test_official_resolvers_preserve_identifier_suffixes(audited_site):
    renderer, output = audited_site
    for name in ("Gemmiger_qucibialis", "Methanocatella_smithii", "Escherichia_coli"):
        assert renderer.curie_url("GTDB:s__" + name) == (
            "https://gtdb.ecogenomic.org/tree?r=s__" + name.replace("_", "%20"))
    assert renderer.curie_url("GTDB:s__Escherichia_A_coli_A") == (
        "https://gtdb.ecogenomic.org/tree?r=s__Escherichia_A%20coli_A")
    assert renderer.curie_url("GTDB:g__Escherichia_A") == (
        "https://gtdb.ecogenomic.org/tree?r=g__Escherichia_A")
    assert renderer.curie_url("GTDB:s__Escherichia coli") == (
        "https://gtdb.ecogenomic.org/tree?r=s__Escherichia%20coli")
    assert renderer.curie_url("gtdb.genome:RS_GCF_000005845.2") == (
        "https://gtdb.ecogenomic.org/genome?gid=GCF_000005845.2")
    assert renderer.curie_url("lpsn:777826") == "https://lpsn.dsmz.de/taxon/777826"
    assert renderer.curie_url("lpsn:unresolved") is None
    assert 'href="https://lpsn.dsmz.de/taxon/777826"' in rendered_taxon(output, "NCBITaxon:2173")


def test_embedding_map_waits_for_deferred_gzip_loader(audited_site):
    import shutil
    import subprocess

    if shutil.which("node") is None:
        pytest.skip("Node is needed for browser execution")
    _, output = audited_site
    html = (output / "map.html").read_text()
    inline_script = re.search(r"<script>\s*(\(\(\)\s*=>[\s\S]*?)\s*</script>", html).group(1)
    harness = r"""
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const siteDir = process.argv[1];
const inlineScript = process.argv[2];
class Node {
  constructor(tag = "DIV") {
    this.tagName = tag; this.children = []; this.events = {}; this.value = "";
    this.style = {}; this.dataset = {}; this.width = 820; this.height = 580;
  }
  append(...items) { this.children.push(...items); }
  replaceChildren(...items) { this.children = items; }
  addEventListener(name, fn) { this.events[name] = fn; }
  getContext() {
    return {clearRect() {}, beginPath() {}, arc() {}, fill() {}, stroke() {}};
  }
}
const nodes = new Map();
const get = id => {
  if (!nodes.has(id)) nodes.set(id, new Node(id === "map-search" ? "INPUT" : "DIV"));
  return nodes.get(id);
};
get("map-color").value = "domain";
const winEvents = {};
global.document = {
  getElementById: get,
  querySelectorAll: () => [],
  createElement: tag => new Node(tag.toUpperCase())
};
global.window = global;
global.location = {search: "", pathname: "/TaxonMech/pages/map.html"};
global.history = {replaceState() {}};
global.addEventListener = (name, fn) => { winEvents[name] = fn; };
global.fetch = async rel => new Response(fs.readFileSync(path.join(siteDir, rel)));

// 1. Inline script in <body> runs synchronously BEFORE deferred <head> scripts execute
vm.runInThisContext(inlineScript);
assert.equal(typeof winEvents.DOMContentLoaded, "function");
assert.equal(global.TaxonMechData, undefined);

// 2. Deferred <head> scripts run after HTML parsing completes, before DOMContentLoaded
global.fflate = require(path.join(siteDir, "vendor/fflate-0.8.2.js"));
vm.runInThisContext(fs.readFileSync(path.join(siteDir, "compressed-data.js"), "utf8"));
assert.equal(typeof global.TaxonMechData.loadJSON, "function");

// 3. DOMContentLoaded fires and loads corpus_map.json.gz
winEvents.DOMContentLoaded();
(async () => {
  for (let i = 0; i < 20 && !get("map-status").textContent; i++) {
    await new Promise(resolve => setTimeout(resolve, 10));
  }
  assert.equal(get("map-status").textContent, "2 of 2 embedded taxa shown.");
})().catch(err => { console.error(err); process.exitCode = 1; });
"""
    result = subprocess.run(
        ["node", "-e", harness, str(output), inline_script], capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr
