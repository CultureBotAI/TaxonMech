#!/usr/bin/env python3
"""Render the browsable site under pages/ from data/taxa/.

Generated, committed, and served from `main`, matching the sibling Mech
repos. Regenerate with `just render`; `--check` fails when the committed
output is out of step with the corpus.

Usage:
    python scripts/render_pages.py
    python scripts/render_pages.py --out /tmp/site --check
"""

from __future__ import annotations

import argparse
import filecmp
import json
import shutil
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

from corpus import REPO_ROOT, TAXA_DIR, load_records
from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATES_DIR = REPO_ROOT / "src" / "taxonmech" / "templates"
PAGES_DIR = REPO_ROOT / "pages"

DOMAIN_BLURB = {
    "BACTERIA": "Taxa under NCBITaxon:2 — the bulk of the cultured, named prokaryotes.",
    "ARCHAEA": "Taxa under NCBITaxon:2157.",
    "EUKARYOTA": "Microbial eukaryotes with strain or name records in the sources.",
    "VIRUSES": "Viral taxa the sources attest.",
    "OTHER": "Taxa whose lineage places them under none of the four domains.",
}

PREFIX_URL = {
    "NCBITaxon": "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=",
    "GTDB": "https://gtdb.ecogenomic.org/taxon?name=",
    "lpsn": "https://lpsn.dsmz.de/",
    "bacdive": "https://bacdive.dsmz.de/strain/",
    "mediadive.medium": "https://mediadive.dsmz.de/medium/",
    "ncbi.assembly": "https://www.ncbi.nlm.nih.gov/datasets/genome/",
    "gtdb.genome": "https://gtdb.ecogenomic.org/genome?gid=",
    "biosample": "https://www.ncbi.nlm.nih.gov/biosample/",
    "bioproject": "https://www.ncbi.nlm.nih.gov/bioproject/",
    "patric": "https://www.bv-brc.org/view/Genome/",
    "img.taxon": "https://img.jgi.doe.gov/cgi-bin/m/main.cgi?section=TaxonDetail&page=taxonDetail&taxon_oid=",
    "INSDC": "https://www.ncbi.nlm.nih.gov/nuccore/",
    "PMID": "https://pubmed.ncbi.nlm.nih.gov/",
    "DOI": "https://doi.org/",
    "GO": "http://purl.obolibrary.org/obo/GO_",
    "CHEBI": "http://purl.obolibrary.org/obo/CHEBI_",
    "ENVO": "http://purl.obolibrary.org/obo/ENVO_",
    "UBERON": "http://purl.obolibrary.org/obo/UBERON_",
    "METPO": "https://w3id.org/metpo/",
    "traitmech": "https://w3id.org/traitmech/",
    "habitatmech": "https://w3id.org/habitatmech/",
}


def curie_url(curie: str) -> str | None:
    if not isinstance(curie, str) or ":" not in curie:
        return None
    prefix, local = curie.split(":", 1)
    base = PREFIX_URL.get(prefix)
    if prefix == "gtdb.genome" and local.startswith(("RS_", "GB_")):
        local = local[3:]
    if prefix == "gold":
        if local.startswith("Go"):
            base = "https://gold.jgi.doe.gov/organism?id="
        elif local.startswith("Gp"):
            base = "https://gold.jgi.doe.gov/project?id="
        elif local.startswith("Ga"):
            base = "https://gold.jgi.doe.gov/analysis_project?id="
    if prefix == "lpsn":
        # LPSN name ids resolve through the search page; the record's own url is preferred.
        return None
    return f"{base}{local}" if base else None


def page_name(path: Path) -> str:
    rel = path.relative_to(TAXA_DIR).with_suffix("")
    return "/".join(rel.parts)


def render(out_dir: Path) -> None:
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)), autoescape=select_autoescape(["html"]),
                      trim_blocks=True, lstrip_blocks=True)
    env.filters["curie_url"] = curie_url

    records = load_records()
    by_domain: dict[str, list[dict]] = defaultdict(list)
    index = []
    for path, doc in records:
        name = page_name(path)
        sources = sorted({a["source"] for a in doc.get("source_attestations") or []})
        entry = {
            "identifier": doc["identifier"],
            "label": doc["label"],
            "rank": doc.get("rank"),
            "domain": doc.get("taxon_domain"),
            "status": doc.get("mapping_status"),
            "page": f"taxa/{name}.html",
            "sources": sources,
            "strain_count": doc.get("strain_count") or 0,
            "genomes": sum(a.get("assertion_count") or 0 for a in doc.get("source_attestations") or []
                           if a.get("source") == "GTDB"),
        }
        by_domain[entry["domain"]].append(entry)
        index.append(entry)

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / ".nojekyll").write_text("")
    shutil.copy(TEMPLATES_DIR / "style.css", out_dir / "style.css")
    # Vendored byte-identical across the Mech sites: reads localStorage
    # "mech-theme", sets data-theme before paint, injects the toggle button.
    shutil.copy(TEMPLATES_DIR / "theme-toggle.js", out_dir / "theme-toggle.js")

    domains = [
        {"name": d, "count": len(v), "blurb": DOMAIN_BLURB.get(d, ""), "page": f"domain/{d.lower()}.html"}
        for d, v in sorted(by_domain.items())
    ]
    strains = sum(e["strain_count"] for e in index)
    with_type = sum(1 for _p, d in records if any(s.get("is_type_strain") for s in d.get("strains") or []))
    (out_dir / "index.html").write_text(
        env.get_template("index.html").render(domains=domains, total=len(index), strains=strains,
                                              with_type=with_type, root=""),
        encoding="utf-8")
    (out_dir / "browse.html").write_text(env.get_template("browse.html").render(records=index, root=""),
                                         encoding="utf-8")
    typed = [e for e in index if any(s.get("is_type_strain") for _p, d in records
                                     if d["identifier"] == e["identifier"] for s in d.get("strains") or [])]
    (out_dir / "type-strains.html").write_text(
        env.get_template("browse.html").render(
            records=typed, root="", page_title="Taxa with a type strain", heading="Taxa with a type strain",
            lede=f"{len(typed)} records list a BacDive strain whose deposit LPSN names as the type strain."),
        encoding="utf-8")
    (out_dir / "index.json").write_text(json.dumps(index, indent=1, ensure_ascii=False) + "\n",
                                        encoding="utf-8")

    for dom in domains:
        p = out_dir / dom["page"]
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(
            env.get_template("domain.html").render(domain=dom, records=by_domain[dom["name"]], root="../"),
            encoding="utf-8")

    for path, doc in records:
        name = page_name(path)
        p = out_dir / "taxa" / f"{name}.html"
        p.parent.mkdir(parents=True, exist_ok=True)
        # The page sits at taxa/<domain>/<slug>.html; the directories below
        # pages/ are taxa/ plus every part of `name` except the file itself.
        depth = len(Path(name).parts)
        p.write_text(
            env.get_template("taxon.html").render(r=doc, root="../" * depth,
                                                  source_path=str(path.relative_to(REPO_ROOT))),
            encoding="utf-8")


def _tree_differs(a: Path, b: Path) -> list[str]:
    diffs: list[str] = []

    def walk(cmp: filecmp.dircmp, prefix: str) -> None:
        diffs.extend(f"{prefix}{n}" for n in cmp.left_only + cmp.right_only + cmp.diff_files)
        for name, sub in cmp.subdirs.items():
            walk(sub, f"{prefix}{name}/")

    walk(filecmp.dircmp(a, b), "")
    return diffs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=PAGES_DIR)
    parser.add_argument("--check", action="store_true", help="Render to a temp dir and diff against --out.")
    args = parser.parse_args()

    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            render(Path(tmp))
            if not args.out.exists():
                print(f"{args.out} does not exist; run `just render`", file=sys.stderr)
                return 1
            diffs = _tree_differs(Path(tmp), args.out)
        if diffs:
            print(f"pages/ is stale ({len(diffs)} file(s) differ), e.g. {diffs[:5]}; run `just render`",
                  file=sys.stderr)
            return 1
        print("pages/ is current")
        return 0

    if args.out.exists():
        shutil.rmtree(args.out)
    render(args.out)
    print(f"rendered site under {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
