#!/usr/bin/env python3
"""Retain complete primary catalogs and publish an auditable source census.

--project captures local pinned primary files into compact committed catalogs.
Run without it after inventory/StrainInfo regeneration to refresh the manifest.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import shutil
import tarfile
from collections import Counter
from pathlib import Path

import yaml

from taxonmech.extract import resolve_kg_microbe
from taxonmech.ncbi_assemblies import read_summary
from taxonmech.ncbi_assemblies import settings as assembly_settings
from taxonmech.ncbi_taxdump import fields, load_taxdump, prokaryote_taxa
from taxonmech.ncbi_taxdump import settings as taxdump_settings
from taxonmech.source_catalog import ROOT, sha256, write_chunks

DIRECTORY = ROOT / "data/catalog"


def info(path: Path, rows: int | None = None) -> dict:
    item = {"path": str(path.relative_to(ROOT)), "bytes": path.stat().st_size, "sha256": sha256(path)}
    if rows is not None:
        item["rows"] = rows
    return item


def project():
    DIRECTORY.mkdir(parents=True, exist_ok=True)
    config = taxdump_settings()
    nodes, parents, _ranks, _synonyms, _redirects, _material = load_taxdump(
        ROOT / config["path"], expected_sha256=config["sha256"]
    )
    prokaryotes = prokaryote_taxa(parents, nodes)
    del parents, _ranks, _synonyms, _redirects, _material
    inputs = [info(ROOT / "conf/ncbi_taxdump.yaml"), info(ROOT / "conf/ncbi_assemblies.yaml")]
    outputs = {}

    def save(name, rows, *, source, scope, url, extra=None):
        files = write_chunks(DIRECTORY, name, rows)
        for item in files:
            item["path"] = "data/catalog/" + item["path"]
        outputs[name] = {
            "id": name,
            "name": source,
            "scope": scope,
            "url": url,
            "format": "jsonl.gz",
            "rows": sum(f["rows"] for f in files),
            "files": files,
            **(extra or {}),
        }
        print(name, outputs[name]["rows"], "source records", flush=True)

    for item in assembly_settings(ROOT / "conf/ncbi_assemblies.yaml", ROOT)["sources"]:
        counts = Counter()

        def selected(item=item, counts=counts):
            for row in read_summary(ROOT / item["path"]):
                counts["input_rows"] += 1
                taxid, species = "NCBITaxon:" + row["taxid"], "NCBITaxon:" + row["species_taxid"]
                if taxid in prokaryotes or species in prokaryotes:
                    counts["prokaryote_rows"] += 1
                    yield row
                elif taxid not in nodes and species not in nodes:
                    counts["unresolved_taxonomy_rows_retained"] += 1
                    yield row
                else:
                    counts["non_prokaryote_rows"] += 1

        name = "ncbi_" + item["name"]
        save(
            name,
            selected(),
            source="NCBI Assembly " + item["name"].replace("_", " "),
            scope="All bacterial/archaeal rows and unresolved taxon IDs; all original columns and statuses",
            url=item["url"],
        )
        outputs[name]["selection_counts"] = dict(counts)
        outputs[name]["snapshot"] = "2026-09-13"

    def names():
        with tarfile.open(ROOT / config["path"], "r|gz") as archive:
            for member in archive:
                if member.name == "names.dmp":
                    for row in fields(archive.extractfile(member), "names.dmp"):
                        tid = "NCBITaxon:" + row[0]
                        if tid in prokaryotes:
                            yield {
                                "taxon_id": tid,
                                "name": row[1],
                                "unique_name": row[2],
                                "name_class": row[3],
                            }

    save(
        "ncbi_names",
        names(),
        source="NCBI Taxonomy names",
        scope="Every bacterial/archaeal name class",
        url=config["url"],
        extra={"snapshot": config["snapshot"]},
    )
    nodes.clear()
    prokaryotes.clear()
    kgm = resolve_kg_microbe(None)
    gtdb_inputs = [kgm / f"data/raw/gtdb/{domain}_metadata.tsv.gz" for domain in ("bac120", "ar53")]

    def genomes():
        seen = set()
        for path in gtdb_inputs:
            with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle, delimiter="\t")
                for row in reader:
                    if None in row or None in row.values() or row["accession"] in seen:
                        raise ValueError("malformed or duplicate GTDB primary genome")
                    seen.add(row["accession"])
                    yield {
                        key: value
                        for key, value in row.items()
                        if key.startswith("ncbi_")
                        or key
                        in {
                            "accession",
                            "gtdb_taxonomy",
                            "gtdb_representative",
                            "gtdb_type_designation",
                            "gtdb_type_species_of_genus",
                        }
                    }

    save(
        "gtdb_genomes",
        genomes(),
        source="GTDB genomes",
        scope="Every bacterial and archaeal genome in RS232",
        url="https://data.gtdb.ecogenomic.org/releases/release232/232.0/",
        extra={"snapshot": "RS232"},
    )
    outputs["gtdb_genomes"]["primary_inputs"] = [
        {"path": str(path.relative_to(kgm)), "bytes": path.stat().st_size, "sha256": sha256(path)}
        for path in gtdb_inputs
    ]
    atb = yaml.safe_load((ROOT / "conf/allthebacteria.yaml").read_text())
    path = ROOT / atb["metadata_path"]
    if sha256(path) != atb["sha256"]:
        raise ValueError("AllTheBacteria full metadata differs from its configured pin")
    target = DIRECTORY / "allthebacteria.tsv.xz"
    shutil.copyfile(path, target)
    from taxonmech.atb_catalog import iter_assemblies

    count = sum(1 for _ in iter_assemblies(target))
    outputs["allthebacteria"] = {
        "id": "allthebacteria",
        "name": "AllTheBacteria full catalog",
        "scope": "Every source sample/assembly row, including all unavailable statuses",
        "snapshot": atb["release"],
        "url": atb["url"],
        "format": "atb.tsv.xz",
        "rows": count,
        "files": [info(target, count)],
    }
    inputs.append(info(ROOT / "conf/allthebacteria.yaml"))
    (DIRECTORY / "PRIMARY.json").write_text(
        json.dumps({"inputs": inputs, "sources": list(outputs.values())}, sort_keys=True, indent=2) + "\n"
    )


def manifest():
    primary = json.loads((DIRECTORY / "PRIMARY.json").read_text())
    sources = list(primary["sources"])
    inputs = [*primary["inputs"], info(DIRECTORY / "PRIMARY.json"), info(ROOT / "conf/source_coverage.yaml")]

    def add(identifier, name, path, rows, *, format="jsonl.gz", scope, url, snapshot=""):
        sources.append(
            {
                "id": identifier,
                "name": name,
                "scope": scope,
                "url": url,
                "snapshot": snapshot,
                "format": format,
                "rows": rows,
                "files": [info(path, rows)],
            }
        )

    raw = yaml.safe_load((ROOT / "data/raw/MANIFEST.yaml").read_text())
    inputs.append(info(ROOT / "data/raw/MANIFEST.yaml"))
    for filename, identifier, name, scope, url in (
        (
            "ncbitaxon_taxa.tsv",
            "ncbi_taxa",
            "NCBI Taxonomy",
            "Complete prokaryote backbone plus other attested taxa and ancestors",
            "https://www.ncbi.nlm.nih.gov/taxonomy",
        ),
        (
            "ncbi_type_material.tsv",
            "ncbi_type_material",
            "NCBI type material",
            "Type and excluded-from-type assertions; no inferred equivalence",
            "https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/new_taxdump/",
        ),
        (
            "ncbi_merged_ids.tsv",
            "ncbi_merged_ids",
            "NCBI merged taxon IDs",
            "Every source merged-ID assertion",
            "https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/new_taxdump/",
        ),
        (
            "gtdb_species.tsv",
            "gtdb_species",
            "GTDB species",
            "Every species cluster, including unmapped clusters",
            "https://gtdb.ecogenomic.org/",
        ),
        (
            "gtdb_mappings.tsv",
            "gtdb_mappings",
            "GTDB NCBI mappings",
            "Every supplied species-to-NCBI mapping",
            "https://gtdb.ecogenomic.org/",
        ),
        (
            "lpsn_names.tsv",
            "lpsn",
            "LPSN names",
            "Every name in the pinned kg-microbe transform, including unmapped names",
            "https://lpsn.dsmz.de/",
        ),
        (
            "bacdive_strains.tsv",
            "bacdive_deposits",
            "BacDive deposit crosswalk",
            "Every current strain and its reported culture-collection identifiers",
            "https://bacdive.dsmz.de/",
        ),
    ):
        entry = next(item for item in raw["outputs"] if item["path"] == filename)
        add(
            identifier,
            name,
            ROOT / "data/raw" / filename,
            entry["rows"],
            format="tsv",
            scope=scope,
            url=url,
            snapshot=raw["extracted_at"],
        )
    for folder, source_name, source_file in (
        ("bacdive", "BacDive", "SOURCE.json"),
        ("straininfo", "StrainInfo", "SOURCE.json"),
    ):
        path = ROOT / "data" / folder
        metadata = json.loads((path / source_file).read_text())
        inputs.append(info(path / source_file))
        add(
            folder,
            source_name,
            path / "records.jsonl.gz",
            metadata["records"]["rows"],
            scope="Every strain in the captured public census; original identity and sequence projection",
            url="https://" + ("bacdive.dsmz.de/" if folder == "bacdive" else "straininfo.dsmz.de/"),
            snapshot=metadata["captured_at"],
        )
    path = ROOT / "data/seqcode"
    seqcode = json.loads((path / "SOURCE.json").read_text())
    inputs.append(info(path / "SOURCE.json"))
    for key, item in seqcode["outputs"].items():
        add(
            "seqcode_" + key.replace("-", "_"),
            "SeqCode " + key,
            path / item["path"],
            item["rows"],
            scope="Every public name (discovery census)"
            if key == "names"
            else "Every returned type-genome name, preserving rank, status and classification",
            url="https://registry.seqco.de/",
            snapshot=seqcode["captured_at"],
        )
    path = ROOT / "data/bvbrc"
    bvbrc = json.loads((path / "SOURCE.json").read_text())
    inputs.append(info(path / "SOURCE.json"))
    sources.append({"id": "bvbrc", "name": "BV-BRC / PATRIC", "format": "jsonl.gz",
                    "rows": bvbrc["census_count"], "snapshot": bvbrc["captured_at"],
                    "scope": "Complete public bacterial and archaeal genome census and identity metadata",
                    "url": "https://www.bv-brc.org/", "files": [
                        info(path / item["path"], item["rows"]) for item in bvbrc["files"]]})
    path = ROOT / "data/gold"
    gold = json.loads((path / "SOURCE.json").read_text())
    inputs.append(info(path / "SOURCE.json"))
    for name, item in gold["outputs"].items():
        add(
            "gold_" + name.lower().replace(" ", "_"),
            "GOLD " + name,
            path / item["path"],
            item["rows"],
            scope="Every public workbook row; original identity, strain and genome/project fields",
            url=gold["url"],
            snapshot=gold["workbook_sha256"],
        )
    coverage = yaml.safe_load((ROOT / "conf/source_coverage.yaml").read_text())
    value = {
        "format_version": 1,
        "inputs": inputs,
        "sources": sorted(sources, key=lambda item: item["id"]),
        "coverage": coverage,
        "interpretation": "Catalog inclusion preserves source assertions and does not establish equivalence."
        " Complete refers to each named pinned snapshot, not every organism or database on the Internet.",
    }
    (DIRECTORY / "MANIFEST.json").write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")
    print({item["id"]: item["rows"] for item in sources})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", action="store_true")
    args = parser.parse_args()
    project() if args.project else manifest()


if __name__ == "__main__":
    main()
