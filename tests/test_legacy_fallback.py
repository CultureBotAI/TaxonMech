"""Legacy URLs retain usable fallback links and the original anchored redirect."""

from __future__ import annotations

import importlib
import json
from html.parser import HTMLParser

import pytest


class FallbackParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.links = []
        self.in_main = False
        self.in_script = False
        self.script = ""

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        self.tags.append((tag, attributes))
        if tag == "main":
            self.in_main = True
        if tag == "script":
            self.in_script = True
        if tag == "a":
            self.links.append((attributes["href"], self.in_main))

    def handle_endtag(self, tag):
        if tag == "main":
            self.in_main = False
        if tag == "script":
            self.in_script = False

    def handle_data(self, data):
        if self.in_script:
            self.script += data


@pytest.mark.parametrize("domain,route", [
    ("BACTERIA", "taxa/bacteria/fixture.html"),
    ("ARCHAEA", "taxa/archaea/fixture.html"),
    ("EUKARYOTA", "taxa/eukaryota/fixture.html"),
    ("OTHER", "taxa/other/fixture.html"),
    ("BACTERIA", "taxa/bacteria/nested/fixture.html"),
])
def test_legacy_fallback_document_and_exact_targets(tmp_path, repo_root, monkeypatch, domain, route):
    """Exercise the owning full renderer, including nested legacy routes."""
    monkeypatch.syspath_prepend(str(repo_root / "scripts"))
    renderer = importlib.import_module("render_pages")
    identifier = "NCBITaxon:562"
    doc = {"identifier": identifier, "label": "Fixture species", "rank": "SPECIES",
           "taxon_domain": domain, "strain_count": 0, "mapping_status": "SEEDED"}
    monkeypatch.setattr(renderer, "load_records", lambda: [
        (renderer.TAXA_DIR / domain.lower() / "fixture.yaml", doc)])
    monkeypatch.setattr(renderer, "_tsv", lambda path: [{"identifier": identifier, "page": route}])
    output = tmp_path / "site"
    renderer.render(output)
    html = (output / route).read_text(encoding="utf-8")
    parsed = FallbackParser()
    parsed.feed(html)

    assert [(tag, attrs) for tag, attrs in parsed.tags if tag == "html"] == [("html", {"lang": "en"})]
    for structural_tag in ("head", "body", "main"):
        assert sum(tag == structural_tag for tag, _ in parsed.tags) == 1
        assert html.count(f"</{structural_tag}>") == 1
    viewports = [attrs.get("content") for tag, attrs in parsed.tags
                 if tag == "meta" and attrs.get("name") == "viewport"]
    assert viewports == ["width=device-width, initial-scale=1"]
    target = "../" * (len(route.split("/")) - 1) + "taxon.html?id=" + identifier
    source = f"https://github.com/CultureBotAI/TaxonMech/blob/main/data/taxa/{domain.lower()}/fixture.yaml"
    assert parsed.links == [(target, True), (source, True)]
    assert parsed.script == f"location.replace({json.dumps(target)}+location.hash)"
    assert html.endswith("</body></html>\n")


def test_landing_main_contains_primary_content_and_excludes_footer(repo_root):
    from jinja2 import Environment, FileSystemLoader, select_autoescape

    env = Environment(loader=FileSystemLoader(repo_root / "src/taxonmech/templates"),
                      autoescape=select_autoescape(["html"]))
    html = env.get_template("index.html").render(total=1, strains=0, with_type=0, domains=[])
    assert html.count("<main>") == html.count("</main>") == 1
    content = html.split("<main>", 1)[1].split("</main>", 1)[0]
    assert "<h1>TaxonMech</h1>" in content
    assert 'id="domains"' in content
    assert "<footer>" not in content
