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
import csv
import filecmp
import gzip
import hashlib
import io
import json
import re
import shutil
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from corpus import REPO_ROOT, TAXA_DIR, load_records
from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATES_DIR = REPO_ROOT / "src" / "taxonmech" / "templates"
PAGES_DIR = REPO_ROOT / "pages"
BROWSE_PAGE_SIZE = 200
# Sources whose licence requires attribution wherever their metadata is
# published. Their data is rendered inline on taxon records rather than on a
# per-source browser, so the notice belongs on the source-catalogue page.
ATTRIBUTION_MANIFESTS = {
    "AllTheBacteria": REPO_ROOT / "data" / "atb" / "MANIFEST.yaml",
    "StrainInfo": REPO_ROOT / "data" / "straininfo" / "MANIFEST.yaml",
}
STRAIN_HTML_THRESHOLD = 32_000


def gzip_bytes(payload: bytes) -> bytes:
    """Deterministic gzip, including its header across supported Python versions."""
    buffer = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buffer, mtime=0) as compressed:
        compressed.write(payload)
    return buffer.getvalue()

DOMAIN_BLURB = {
    "BACTERIA": "Species and infraspecific taxa under NCBITaxon:2, "
                "including uncultured and environmental taxa.",
    "ARCHAEA": "Taxa under NCBITaxon:2157.",
    "EUKARYOTA": "Eukaryotic taxa attested by the sources, including taxa without BacDive strains.",
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
    "ena.analysis": "https://www.ebi.ac.uk/ena/browser/view/",
    "bioproject": "https://www.ncbi.nlm.nih.gov/bioproject/",
    "patric": "https://www.bv-brc.org/view/Genome/",
    "img.taxon": "https://img.jgi.doe.gov/cgi-bin/m/main.cgi?section=TaxonDetail&page=taxonDetail&taxon_oid=",
    "INSDC": "https://www.ncbi.nlm.nih.gov/nuccore/",
    "straininfo.strain": "https://straininfo.dsmz.de/strain/",
    "straininfo.deposit": "https://straininfo.dsmz.de/pass?pass=",
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


def curie_url(curie: str, root: str = "") -> str | None:
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


def source_attributions() -> list[dict]:
    """Licence and citation for every source whose licence requires attribution.

    Read from each source's own committed MANIFEST.yaml rather than restated
    here, so the published notice cannot drift from the snapshot it describes.
    A manifest that is missing the licence is an error, not a silent omission:
    publishing the metadata without its notice is the thing this prevents.
    """
    attributions = []
    for name, manifest in sorted(ATTRIBUTION_MANIFESTS.items()):
        if not manifest.exists():
            raise FileNotFoundError(
                f"{name} manifest is missing: {manifest}. Its metadata is published on taxon "
                "records and its licence requires attribution.")
        source = (yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}).get("source") or {}
        missing = [key for key in ("license", "license_url") if not source.get(key)]
        if missing:
            raise ValueError(f"{manifest} source is missing {', '.join(missing)}")
        attributions.append({
            "name": name,
            "license": source["license"],
            "license_url": source["license_url"],
            "citation": source.get("citation"),
            "version": source.get("release") or source.get("snapshot"),
        })
    return attributions


def page_name(path: Path) -> str:
    rel = path.relative_to(TAXA_DIR).with_suffix("")
    return "/".join(rel.parts)


def deposit_label(identifier: str) -> str:
    """Display the CURIE's source accession without changing its punctuation."""
    return unquote(identifier.removeprefix("kgmicrobe.strain:"), errors="strict")


def external_url(value: str | None) -> str | None:
    """Source metadata may supply download URLs, but never executable schemes."""
    if not value:
        return None
    try:
        parsed = urlsplit(value)
        return value if parsed.scheme in {"http", "https"} and parsed.netloc else None
    except ValueError:
        return None


def _tsv(path: Path) -> list[dict]:
    csv.field_size_limit(min(sys.maxsize, 2**31 - 1))
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def render(out_dir: Path) -> None:
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)), autoescape=select_autoescape(["html"]),
                      trim_blocks=True, lstrip_blocks=True)
    env.filters["curie_url"] = curie_url
    env.filters["external_url"] = external_url
    env.filters["deposit_label"] = deposit_label
    env.globals["script_version"] = hashlib.sha256(b"".join(
        path.read_bytes() for path in sorted(TEMPLATES_DIR.glob("*.js")))).hexdigest()[:16]

    records = load_records()
    by_domain: dict[str, list[dict]] = defaultdict(list)
    index = []
    for _path, doc in records:
        sources = sorted({a["source"] for a in doc.get("source_attestations") or []})
        entry = {
            "identifier": doc["identifier"],
            "label": doc["label"],
            "rank": doc.get("rank"),
            "domain": doc.get("taxon_domain"),
            "status": doc.get("mapping_status"),
            "page": f"taxon.html?id={doc['identifier']}",
            "sources": sources,
            "strain_count": doc.get("strain_count") or 0,
            "has_type_strain": any(s.get("is_type_strain") for s in doc.get("strains") or []),
            "genomes": sum(a.get("assertion_count") or 0 for a in doc.get("source_attestations") or []
                           if a.get("source") == "GTDB"),
        }
        by_domain[entry["domain"]].append(entry)
        index.append(entry)

    out_dir.mkdir(parents=True, exist_ok=True)
    from taxonmech.source_catalog import load_manifest
    (out_dir / "sources.html").write_text(env.get_template("sources.html").render(
        catalog=load_manifest(), attributions=source_attributions(), root=""), encoding="utf-8")
    (out_dir / ".nojekyll").write_text("")
    shutil.copy(TEMPLATES_DIR / "style.css", out_dir / "style.css")
    # Vendored byte-identical across the Mech sites: reads localStorage
    # "mech-theme", sets data-theme before paint, injects the toggle button.
    shutil.copy(TEMPLATES_DIR / "theme-toggle.js", out_dir / "theme-toggle.js")
    shutil.copy(TEMPLATES_DIR / "compressed-data.js", out_dir / "compressed-data.js")
    shutil.copy(TEMPLATES_DIR / "taxon-browser.js", out_dir / "taxon-browser.js")
    shutil.copy(TEMPLATES_DIR / "taxon-viewer.js", out_dir / "taxon-viewer.js")
    shutil.copytree(TEMPLATES_DIR / "vendor", out_dir / "vendor", dirs_exist_ok=True)

    domains = [
        {"name": d, "count": len(v), "blurb": DOMAIN_BLURB.get(d, ""), "page": f"domain/{d.lower()}.html"}
        for d, v in sorted(by_domain.items())
    ]
    strains = len({s["strain_id"] for _p, d in records for s in d.get("strains") or []})
    typed = [e for e in index if e["has_type_strain"]]
    with_type = len(typed)
    (out_dir / "index.html").write_text(
        env.get_template("index.html").render(domains=domains, total=len(index), strains=strains,
                                              with_type=with_type, root=""),
        encoding="utf-8")
    write_browse_pages(env, out_dir, "browse", index)
    write_browse_pages(env, out_dir, "type-strains", typed, typed=True,
                       page_title="Taxa with a type strain", heading="Taxa with a type strain",
                       lede=f"{len(typed)} records list a BacDive strain whose deposit "
                            "LPSN names as the type strain.")
    write_search_index(out_dir, index)

    for dom in domains:
        write_browse_pages(env, out_dir, f"domain/{dom['name'].lower()}", by_domain[dom["name"]],
                           root="../", domain=dom["name"], page_title=dom["name"].capitalize(),
                           heading=dom["name"].capitalize(), lede=dom["blurb"])

    write_taxon_data(env, out_dir, records)
    (out_dir / "taxon.html").write_text(
        env.get_template("taxon-viewer.html").render(root=""), encoding="utf-8")
    # Preserve every previously published taxon URL, including its strain anchor.
    active = {entry["identifier"]: entry["domain"] for entry in index}
    for row in _tsv(REPO_ROOT / "curation/legacy_page_paths.tsv"):
        if row["identifier"] not in active:
            continue
        relative = Path(row["page"])
        if relative.is_absolute() or ".." in relative.parts or relative.parts[0] != "taxa":
            raise ValueError("legacy taxon route leaves the generated taxa directory")
        target = "../" * (len(relative.parts) - 1) + "taxon.html?id=" + row["identifier"]
        source = f"data/taxa/{active[row['identifier']].lower()}/{relative.stem}.yaml"
        path = out_dir / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text('<!doctype html><meta charset="utf-8"><title>TaxonMech</title>'
                        f'<a href="{target}">Open the taxon record</a>'
                        '<p><a href="https://github.com/CultureBotAI/TaxonMech/blob/main/'
                        f'{source}">Read the source YAML</a></p>'
                        f'<script>location.replace({json.dumps(target)}+location.hash)</script>\n')
    if hasattr(records, "close"):
        records.close()


def write_search_index(out_dir: Path, index: list[dict]) -> None:
    """Publish the complete search data without an oversized plain JSON blob."""
    payload = (json.dumps(index, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")
    compressed = gzip_bytes(payload)
    (out_dir / "index.json.gz").write_bytes(compressed)
    (out_dir / "index.json").write_text(json.dumps({
        "format_version": 1, "format": "json.gz", "path": "index.json.gz", "records": len(index),
        "bytes": len(compressed), "sha256": hashlib.sha256(compressed).hexdigest(),
    }, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def taxon_payload(env: Environment, path: Path, doc: dict) -> dict:
    env.filters.setdefault("deposit_label", deposit_label)
    pages = []
    strains = doc.get("strains") or []
    for offset in range(0, len(strains), 200):
        part = strains[offset:offset + 200]
        pages.append({"html": env.get_template("taxon-strains.html").render(
            r={**doc, "strains": part}, root=""),
                      "anchors": ["strains-" + strain["strain_id"].replace(":", "-") for strain in part]})
    return {"label": doc["label"], "html": env.get_template("taxon-content.html").render(
        r=doc, root="", strain_page_count=len(pages), source_path=str(path.relative_to(REPO_ROOT))),
        "strain_pages": pages}


def write_taxon_data(env: Environment, out_dir: Path, records) -> None:
    """Shard numerically, keeping at most 1,000 taxon records in memory."""
    directory = out_dir / "taxon-details"
    directory.mkdir(exist_ok=True)
    ordered = records.by_identifier() if hasattr(records, "by_identifier") else sorted(
        records, key=lambda item: int(item[1]["identifier"].split(":")[1]))
    bucket, payload = None, {}

    def flush():
        if payload:
            raw = (json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
            (directory / f"{bucket:04}.json.gz").write_bytes(gzip_bytes(raw))

    for path, doc in ordered:
        identifier = doc["identifier"]
        if not re.fullmatch(r"NCBITaxon:[1-9][0-9]*", identifier):
            raise ValueError("taxon viewer requires an explicit NCBI taxonomy identifier")
        current = int(identifier.split(":")[1]) // 1000
        if current != bucket:
            flush()
            bucket, payload = current, {}
        if identifier in payload:
            raise ValueError("duplicate taxon in publication shard")
        payload[identifier] = taxon_payload(env, path, doc)
    flush()


def write_browse_pages(env: Environment, out_dir: Path, stem: str, entries: list[dict],
                       *, root: str = "", domain: str = "", typed: bool = False, **context) -> None:
    """Bound static tables and retain a complete browse route without JavaScript."""
    count = max(1, (len(entries) + BROWSE_PAGE_SIZE - 1) // BROWSE_PAGE_SIZE)

    def name(number: int) -> str:
        return f"{stem}{'-' + str(number) if number > 1 else ''}.html"

    for number in range(1, count + 1):
        path = out_dir / name(number)
        path.parent.mkdir(parents=True, exist_ok=True)
        pagination = {"page": number, "pages": count, "total": len(entries),
                      "previous": root + name(number - 1) if number > 1 else "",
                      "next": root + name(number + 1) if number < count else "",
                      "domain": domain, "typed": typed, "size": BROWSE_PAGE_SIZE}
        path.write_text(env.get_template("browse.html").render(
            records=entries[(number - 1) * BROWSE_PAGE_SIZE:number * BROWSE_PAGE_SIZE], root=root,
            pagination=pagination, **context), encoding="utf-8")


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
