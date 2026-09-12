"""Read and query the committed StrainInfo overlap without a separate database.

Source genomes belong to the explicitly asserting SI-DP. Other TaxonMech
genome associations are context on the local strain, not StrainInfo claims.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


def _identifier(value: object, kind: str) -> str:
    text = str(value)
    for prefix in (f"straininfo.{kind}:", "SI-ID" if kind == "strain" else "SI-DP"):
        if text.startswith(prefix):
            text = text[len(prefix):]
            break
    if not re.fullmatch(r"[1-9][0-9]*", text):
        raise ValueError(f"Invalid StrainInfo {kind} identifier: {value}")
    return f"straininfo.{kind}:{text}"


def _existing_genomes(raw: Path, atb: Path | None, wanted: set[str]) -> dict[str, list[dict]]:
    from taxonmech.atb import genome_records, read_rows

    result: dict[str, list[dict]] = defaultdict(list)
    for filename, field in (("strain_assemblies.tsv", "assembly_id"),
                            ("strain_genome_records.tsv", "genome_id")):
        path = raw / filename
        for row in read_rows(path):
            if row["strain_id"] in wanted:
                result[row["strain_id"]].append({
                    "genome_id": row[field], "relationship": "existing_taxonmech_strain_association",
                    "source_evidence": {key: value for key, value in row.items()
                                        if key != "strain_id" and value != ""},
                })
    if atb is not None and atb.exists():
        for sid, links in genome_records(atb).items():
            if sid in wanted:
                result[sid].extend({"genome_id": link["genome_id"],
                                    "relationship": "existing_taxonmech_strain_association",
                                    "source_evidence": link} for link in links)
    for links in result.values():
        links.sort(key=lambda link: (not link["genome_id"].startswith("ncbi.assembly:"),
                                     link["genome_id"], json.dumps(link, sort_keys=True)))
    return dict(result)


def load_overlap(directory: Path, raw: Path, atb: Path | None = None) -> dict:
    """Build linked SI-ID groups, retaining every own-deposit assertion path.

    Callers serving current data validate component provenance separately.
    This reader also supports isolated fixtures and explicit historical files.
    """
    from taxonmech.straininfo import read_records, read_rows, record_links

    manifest = yaml.safe_load((directory / "MANIFEST.yaml").read_text(encoding="utf-8"))
    links = read_rows(directory / "strain_links.tsv")
    wanted = {row["strain_id"] for row in links}
    source_strains = {row["strain_id"]: row for row in read_rows(raw / "bacdive_strains.tsv")
                      if row["strain_id"] in wanted}
    existing = _existing_genomes(raw, atb, wanted)
    assemblies, related = record_links(directory, root=raw.parent.parent)
    assertions: dict[tuple[str, str, str, str], dict[str, list]] = defaultdict(
        lambda: {"assemblies": [], "related_records": []})
    for field, inventory in (("assemblies", assemblies), ("related_records", related)):
        for sid, values in inventory.items():
            for value in values:
                evidence = value["straininfo_evidence"]
                key = sid, evidence["strain_id"], evidence["deposit_id"], value["matched_strain_id"]
                if ((field == "assemblies" or value.get("record_type") == "NUCLEOTIDE_SEQUENCE")
                        and evidence.get("sequence_deposit_id") != evidence["deposit_id"]):
                    raise ValueError("StrainInfo sequence does not assert the matched deposit")
                assertions[key][field].append(value)
    groups: dict[str, dict] = {}
    for row in links:
        si_id = _identifier(row["straininfo_strain_id"], "strain")
        deposit_id = _identifier(row["straininfo_deposit_id"], "deposit")
        group = groups.setdefault(si_id, {
            "straininfo_strain_id": si_id, "strain_doi": row["strain_doi"],
            "strain_status": row["strain_status"], "source_metadata": {},
            "matches": [], "strains": [],
        })
        if (row["strain_doi"], row["strain_status"]) != (group["strain_doi"], group["strain_status"]):
            raise ValueError(f"Inconsistent StrainInfo record metadata: {si_id}")
        key = row["strain_id"], si_id, deposit_id, row["matched_strain_id"]
        evidence = assertions.pop(key, {"assemblies": [], "related_records": []})
        group["matches"].append({**row, "straininfo_strain_id": si_id,
                                  "straininfo_deposit_id": deposit_id, **evidence})
    if assertions:
        raise ValueError("StrainInfo assertions have no corresponding matched deposit")
    for source in read_records(directory / "records.jsonl.gz"):
        si_id = _identifier(source["strain"]["siID"], "strain")
        if si_id in groups:
            group = groups[si_id]
            matched = {match["straininfo_deposit_id"] for match in group["matches"]}
            # Unmatched deposits and their sequences must not look like imported links.
            group["source_metadata"] = {
                "strain": {key: value for key, value in source["strain"].items() if key != "sequence"},
                "matched_deposits": [deposit for deposit in source.get("deposits", [])
                                     if _identifier(deposit["siDP"], "deposit") in matched],
            }
    for group in groups.values():
        if not group["source_metadata"]:
            raise ValueError("StrainInfo match has no source record projection")
        for sid in sorted({match["strain_id"] for match in group["matches"]}):
            strain = source_strains[sid]
            group["strains"].append({
                "strain_id": sid, "source_id": f"bacdive:{strain['bacdive_id']}",
                "designation": strain["designation"],
                "culture_collection_ids": strain["culture_collection_ids"].split("|")
                                          if strain["culture_collection_ids"] else [],
                "existing_genome_associations": existing.get(sid, []),
            })
        group["matches"].sort(key=lambda match: (
            match["strain_id"], match["straininfo_deposit_id"], match["matched_strain_id"]))
    return {"manifest": manifest, "records": [groups[key] for key in sorted(
        groups, key=lambda key: int(key.split(":")[1]))]}


def query_overlap(overlap: dict, *, strain: str | None = None, deposit: str | None = None,
                  culture: str | None = None, bacdive: str | None = None,
                  doi: str | None = None, genome: str | None = None,
                  sequence: str | None = None, existing_genome: str | None = None) -> list[dict]:
    """Exact selectors are ANDed on one matched deposit; no accession version inference."""
    si_strain = None
    if strain and (strain.isdecimal() or strain.startswith(("SI-ID", "straininfo.strain:"))):
        si_strain = _identifier(strain, "strain")
    if deposit:
        deposit = _identifier(deposit, "deposit")
    if bacdive:
        value = bacdive.removeprefix("bacdive:").removeprefix("kgmicrobe.strain:bacdive_")
        if not re.fullmatch(r"[1-9][0-9]*", value):
            raise ValueError("--bacdive expects a positive BacDive identifier")
        bacdive = "kgmicrobe.strain:bacdive_" + value
    if genome and genome.startswith(("GCA_", "GCF_")):
        genome = "ncbi.assembly:" + genome
    if sequence and not sequence.startswith("INSDC:"):
        sequence = "INSDC:" + sequence
    results = []
    for group in overlap["records"]:
        if si_strain and group["straininfo_strain_id"] != si_strain:
            continue
        if doi and group["strain_doi"].removeprefix("DOI:") != doi.removeprefix("DOI:"):
            continue
        local = {item["strain_id"]: item for item in group["strains"]}
        for match in group["matches"]:
            if strain and not si_strain and strain not in {
                match["strain_id"], match["matched_strain_id"]}:
                continue
            if deposit and match["straininfo_deposit_id"] != deposit:
                continue
            if culture and culture not in {match["matched_strain_id"], match["deposit_designation"]}:
                continue
            if bacdive and match["strain_id"] != bacdive:
                continue
            if genome and not any(link["assembly_id"] == genome for link in match["assemblies"]):
                continue
            if sequence and not any(link["record_type"] == "NUCLEOTIDE_SEQUENCE"
                                    and link["record_id"] == sequence for link in match["related_records"]):
                continue
            context = local[match["strain_id"]]["existing_genome_associations"]
            if existing_genome and not any(link["genome_id"] == existing_genome for link in context):
                continue
            results.append({**match, "existing_genome_associations": context})
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strain", help="SI-ID, local BacDive strain CURIE or matched culture CURIE")
    parser.add_argument("--deposit", help="SI-DP number, SI-DP… or straininfo.deposit:…")
    parser.add_argument("--culture", help="Exact source deposit designation or matched culture CURIE")
    parser.add_argument("--bacdive", help="Local BacDive ID (not the source's cross-reference field)")
    parser.add_argument("--doi", help="Exact StrainInfo record-version DOI")
    parser.add_argument("--genome", help="Exact StrainInfo NCBI assembly accession, version as supplied")
    parser.add_argument("--sequence", help="Exact StrainInfo-asserted nucleotide accession")
    parser.add_argument("--existing-genome",
                        help="Prior TaxonMech strain association, retaining its original provenance")
    parser.add_argument("--info", action="store_true", help="Show committed source and overlap summary")
    parser.add_argument("--evidence", action="store_true", help="Include complete original source assertions")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--format", choices=("json", "tsv"), default="json")
    args = parser.parse_args(argv)
    selectors = {key: getattr(args, key) for key in (
        "strain", "deposit", "culture", "bacdive", "doi", "genome", "sequence", "existing_genome")}
    if not 1 <= args.limit <= 1000 or args.offset < 0:
        parser.error("--limit must be 1..1000 and --offset must be nonnegative")
    if not args.info and not any(selectors.values()):
        parser.error("Supply an exact selector or --info")
    try:
        from taxonmech.straininfo import provenance_problems

        problems = provenance_problems(ROOT, reproduce=False)
        if problems:
            raise ValueError("StrainInfo snapshot is stale or invalid: " + "; ".join(problems))
        directory = ROOT / "data" / "straininfo"
        manifest_before = (directory / "MANIFEST.yaml").read_bytes()
        if args.info:
            print(json.dumps(yaml.safe_load(manifest_before), indent=2, ensure_ascii=False))
            return 0
        from taxonmech.atb import provenance_problems as atb_provenance_problems

        if problems := atb_provenance_problems(ROOT, reproduce=False):
            raise ValueError("Existing ATB/strain associations are stale or invalid: "
                             + "; ".join(problems))
        overlap = load_overlap(directory, ROOT / "data" / "raw", ROOT / "data" / "atb")
        matches = query_overlap(overlap, **selectors)
        if manifest_before != (directory / "MANIFEST.yaml").read_bytes():
            raise ValueError("StrainInfo snapshot changed during the query; retry")
        selected = matches[args.offset:args.offset + args.limit]
        if not args.evidence:
            selected = [{key: value for key, value in match.items()
                         if key not in {"assemblies", "related_records", "existing_genome_associations"}}
                        | {"assembly_ids": sorted({link["assembly_id"] for link in match["assemblies"]}),
                           "related_record_ids": sorted({link["record_id"]
                                                         for link in match["related_records"]}),
                           "existing_taxonmech_genome_ids": list(dict.fromkeys(
                               link["genome_id"] for link in match["existing_genome_associations"]))}
                        for match in selected]
        if args.format == "json":
            print(json.dumps({"total_matches": len(matches), "offset": args.offset,
                              "matches": selected}, indent=2, ensure_ascii=False))
        elif selected:
            writer = csv.DictWriter(sys.stdout, fieldnames=list(selected[0]), delimiter="\t",
                                    lineterminator="\n")
            writer.writeheader()
            writer.writerows({key: json.dumps(value, ensure_ascii=False) if isinstance(value, (list, dict))
                              else value for key, value in row.items()} for row in selected)
        return 0
    except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as error:
        print(f"straininfo-query: {error}", file=sys.stderr)
        return 1
