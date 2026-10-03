"""Browse tables retain semantic context and scroll independently of the page."""
from html.parser import HTMLParser
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]


class Elements(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


def test_browse_template_provides_named_keyboard_region_and_column_scopes():
    env = Environment(loader=FileSystemLoader(ROOT / "src/taxonmech/templates"),
                      autoescape=select_autoescape(["html"]))
    page = env.get_template("browse.html").render(root="", records=[], pagination={
        "domain": "", "typed": False, "page": 1, "size": 200, "total": 0, "pages": 1})
    parsed = Elements()
    parsed.feed(page)
    region = next(attrs for _, attrs in parsed.elements if attrs.get("class") == "table-scroll")
    assert region["role"] == "region" and region["tabindex"] == "0"
    assert region["aria-label"] == "Taxon records"
    headers = [attrs for tag, attrs in parsed.elements if tag == "th"]
    assert len(headers) == 8 and all(attrs.get("scope") == "col" for attrs in headers)
    assert '<caption>All records</caption>' in page
    assert 'id="taxon-static-pages"' in page and 'id="taxon-dynamic-pages"' in page


def test_both_public_shells_link_the_maintained_project_directory():
    for path in [ROOT / "pages/index.html", ROOT / "pages/browse.html", ROOT / "pages/taxon.html"]:
        assert 'href="https://culturebotai.github.io/mechs/"' in path.read_text(), path
