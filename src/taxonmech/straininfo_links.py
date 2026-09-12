"""Deposit-specific assertions from StrainInfo's public v2 strain records.

Search results and source strain groups are candidates, not identity proofs.
Only a record's own non-erroneous deposit, matched to a complete registered
culture identifier, can supply a link. Sequences must name that same deposit.
"""

from __future__ import annotations

import gzip
import json
import re
from collections.abc import Iterable, Iterator
from pathlib import Path

from taxonmech.extract import ASSEMBLY_FIELDS, RELATED_RECORD_FIELDS
from taxonmech.genome_sources import index_culture_identifiers, normalize_culture_identifier

STRAIN_FIELDS = (
    "strain_id", "straininfo_strain_id", "straininfo_deposit_id", "matched_strain_id",
    "deposit_designation", "strain_doi", "strain_status", "deposit_status", "source_bacdive_id", "taxon_id",
)
ASSEMBLY_COLUMNS = (*ASSEMBLY_FIELDS, "straininfo_evidence_json")
RELATED_COLUMNS = (*RELATED_RECORD_FIELDS, "straininfo_evidence_json")
EXCLUSION_FIELDS = ("source_strain_id", "source_deposit_id", "accession", "reason", "value")
ASSEMBLY = re.compile(r"GC[AF]_[0-9]{9}(?:\.[1-9][0-9]*)?")
NUCLEOTIDE = re.compile(
    r"(?:[A-Z][0-9]{5}|[A-Z]{2}[0-9]{6}|[A-Z]{2}[0-9]{8}|[A-Z]{4}[0-9]{8,}|"
    r"[A-Z]{6}[0-9]{9,}|[A-Z]{5}[0-9]{7}|(?:AC|NC|NG|NT|NW|NZ|NM|NR|XM|XR)_[0-9]+)"
    r"(?:\.[1-9][0-9]*)?"
)
DOI = re.compile(r"10\.60712/SI-ID([1-9][0-9]*)\.([1-9][0-9]*)")
STRAIN_STATUSES = {"published online", "published offline"}
DEPOSIT_STATUSES = {"private", "dead", "unknown", "available", "erroneous data"}


def encoded(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def positive_id(value: object, context: str) -> int:
    if type(value) is not int or value <= 0:
        raise ValueError(f"StrainInfo {context} must be a positive integer")
    return value


def objects(value: object, context: str) -> list[dict]:
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        raise ValueError(f"StrainInfo {context} must be a list of objects")
    return value


def nonempty(value: object, context: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"StrainInfo {context} must be a nonempty string")
    return value


def project_record(record: dict) -> dict:
    """Keep original identity/sequence fields, omitting unrelated phenotype data.

    No values within these fields are normalized or inferred. The original
    response hashes and request URLs are recorded separately in SOURCE.json.
    """
    if not isinstance(record, dict) or not isinstance(record.get("strain"), dict):
        raise ValueError("StrainInfo response must contain a strain object")
    strain = record["strain"]
    positive_id(strain.get("siID"), "strain.siID")
    keys = ("siID", "doi", "status", "bdID", "taxon", "relation", "sequence",
            "alternative", "merged", "archive")
    dep_keys = ("siDP", "designation", "status", "typeStrain", "lastUpdate", "cultureCollection", "taxon")
    return {"strain": {key: strain[key] for key in keys if key in strain},
            "deposits": [{key: dep[key] for key in dep_keys if key in dep}
                         for dep in objects(record.get("deposits"), "deposits")]}


def read_records(path: Path) -> Iterator[dict]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            try:
                record = json.loads(line)
                if project_record(record) != record:
                    raise ValueError("unexpected fields outside the source projection")
                yield record
            except (TypeError, ValueError) as exc:
                raise ValueError(f"{path}:{number}: {exc}") from exc


def candidate_ids(search_rows: Iterable[list], strains: list[dict]) -> list[int]:
    """Use the complete search table only to select rich source records."""
    deposits = index_culture_identifiers(strains)
    result, seen = set(), set()
    for row in search_rows:
        if not isinstance(row, list) or len(row) != 6 or not isinstance(row[1], list):
            raise ValueError("StrainInfo search rows must have six columns and a designation list")
        si_id = positive_id(row[0], "search SI-ID")
        if si_id in seen:
            raise ValueError("StrainInfo search contains duplicate SI-IDs")
        seen.add(si_id)
        if any(normalize_culture_identifier(nonempty(des, "search designation")) in deposits
               for des in row[1]):
            result.add(si_id)
    return sorted(result)


def _unique(rows: list[dict], fields: tuple | list) -> list[dict[str, str]]:
    values = {tuple(str(row.get(key, "")) for key in fields) for row in rows}
    return [dict(zip(fields, value, strict=True)) for value in sorted(values)]


def build_links(records: Iterable[dict], strains: list[dict]) -> tuple[list, list, list, list]:
    deposits = index_culture_identifiers(strains)
    known = {row["strain_id"]: row for row in strains}
    if len(known) != len(strains) or not known:
        raise ValueError("StrainInfo requires a nonempty inventory with unique strain identifiers")
    if any(not re.fullmatch(r"[1-9][0-9]*", row.get("bacdive_id", ""))
           or row["strain_id"] != "kgmicrobe.strain:bacdive_" + row["bacdive_id"] for row in strains):
        raise ValueError("StrainInfo strain inventory must preserve matching BacDive identifiers")
    strain_links, assemblies, related, exclusions = [], [], [], []
    seen = set()

    def excluded(siid, sidp, accession, reason, value=""):
        exclusions.append(dict(zip(EXCLUSION_FIELDS, (siid, sidp, accession, reason, value), strict=True)))

    for record in records:
        strain = record["strain"]
        number = positive_id(strain.get("siID"), "strain.siID")
        siid = f"straininfo.strain:{number}"
        if number in seen:
            raise ValueError(f"Duplicate StrainInfo record: {siid}")
        seen.add(number)
        status = nonempty(strain.get("status"), "strain.status")
        if status not in STRAIN_STATUSES:
            excluded(siid, "", "", "ineligible_strain_status", status)
            continue
        doi = strain.get("doi", "")
        if doi and (not isinstance(doi, str) or not (match := DOI.fullmatch(doi))
                    or int(match[1]) != number):
            raise ValueError(f"{siid}: DOI does not identify the same strain record")
        source_bacdive = (f"bacdive:{positive_id(strain['bdID'], 'strain.bdID')}"
                          if "bdID" in strain else "")
        relation = strain.get("relation")
        if not isinstance(relation, dict):
            raise ValueError(f"{siid}: missing strain.relation object")
        relations = {}
        for item in objects(relation.get("deposit"), "strain.relation.deposit"):
            depid = positive_id(item.get("siDP"), "relation deposit.siDP")
            if depid in relations or type(item.get("erroneous")) is not bool:
                raise ValueError(f"{siid}: duplicate deposit relation or missing erroneous flag")
            relations[depid] = item
            if "ccID" in item:
                positive_id(item["ccID"], "relation deposit.ccID")
        dep_records = {}
        matches = {}
        for dep in objects(record.get("deposits"), "deposits"):
            depid = positive_id(dep.get("siDP"), "deposit.siDP")
            sidp = f"straininfo.deposit:{depid}"
            if depid in dep_records:
                raise ValueError(f"{siid}: duplicate deposit detail {sidp}")
            dep_records[depid] = dep
            designation = nonempty(dep.get("designation"), "deposit.designation")
            rel = relations.get(depid)
            if rel is None or rel.get("designation") != designation:
                raise ValueError(f"{siid}/{sidp}: deposit detail disagrees with its parent relation")
            collection = dep.get("cultureCollection")
            # Registered private isolates can have no collection yet. Keep
            # their source record, but do not promote the designation to a
            # culture-deposit match without collection metadata.
            if collection is None and "ccID" not in rel:
                if normalize_culture_identifier(designation) in deposits:
                    excluded(siid, sidp, "", "missing_culture_collection", designation)
                continue
            if (not isinstance(collection, dict) or collection.get("ccID") != rel.get("ccID")
                    or type(collection.get("deprecated")) is not bool):
                raise ValueError(f"{siid}/{sidp}: culture collection disagrees with its parent relation")
            positive_id(collection.get("ccID"), "deposit cultureCollection.ccID")
            dep_status = nonempty(dep.get("status"), "deposit.status")
            if dep_status not in DEPOSIT_STATUSES:
                raise ValueError(f"{siid}/{sidp}: unknown deposit status {dep_status!r}")
            if rel["erroneous"] or dep_status == "erroneous data" or collection["deprecated"]:
                excluded(siid, sidp, "", "erroneous_deposit", designation)
                continue
            key = normalize_culture_identifier(designation)
            own_matches = sorted(deposits.get(key, ()))
            if not own_matches:
                continue
            if not isinstance(dep.get("taxon", {}), dict):
                raise ValueError(f"{siid}/{sidp}: deposit taxon must be an object")
            taxon = dep.get("taxon", {}).get("ncbi")
            taxon_id = f"NCBITaxon:{positive_id(taxon, 'deposit taxon.ncbi')}" if taxon is not None else ""
            matches[depid] = []
            for local_id, matched_id in own_matches:
                evidence = {"strain_id": siid, "deposit_id": sidp, "deposit_designation": designation,
                            "strain_status": status, "deposit_status": dep_status,
                            "match_method": "culture_identifier"}
                if doi:
                    evidence["strain_doi"] = "DOI:" + doi
                if source_bacdive:
                    evidence["source_bacdive_id"] = source_bacdive
                    if source_bacdive != f"bacdive:{known[local_id]['bacdive_id']}":
                        evidence["bacdive_reference_conflict"] = True
                        excluded(siid, sidp, "", "conflicting_bacdive_reference_not_used",
                                 f"{source_bacdive}; deposit matches {local_id}")
                base = {"strain_id": local_id, "source": "STRAININFO", "source_id": siid,
                        "matched_strain_id": matched_id, "source_strain_identifiers": designation,
                        "source_strain_field": "deposits.designation", "taxon_id": taxon_id}
                matches[depid].append((base, evidence))
                strain_links.append({"strain_id": local_id, "straininfo_strain_id": siid,
                                     "straininfo_deposit_id": sidp, "matched_strain_id": matched_id,
                                     "deposit_designation": designation,
                                     "strain_doi": "DOI:" + doi if doi else "",
                                     "strain_status": status, "deposit_status": dep_status,
                                     "source_bacdive_id": source_bacdive, "taxon_id": taxon_id})
                for target, record_type, field in ((siid, "STRAININFO_STRAIN", "strain.siID"),
                                                   (sidp, "STRAININFO_DEPOSIT", "deposits.siDP")):
                    related.append({**base, "record_id": target, "record_type": record_type,
                                    "source_field": field, "record_name": designation,
                                    "straininfo_evidence_json": encoded(evidence)})
        if set(relations) != set(dep_records):
            raise ValueError(f"{siid}: rich response is missing deposit details")
        if not matches:
            excluded(siid, "", "", "no_eligible_own_deposit_match")
        for seq in objects(strain.get("sequence", []), "strain.sequence"):
            accession = nonempty(seq.get("accessionNumber"), "sequence.accessionNumber")
            seq_type = nonempty(seq.get("type"), "sequence.type")
            for field in ("description", "assemblyLevel"):
                if field in seq:
                    nonempty(seq[field], f"sequence.{field}")
            seq_deposits = objects(seq.get("deposit"), "sequence.deposit")
            if not seq_deposits:
                raise ValueError(f"{siid}/{accession}: sequence must name a deposit")
            for seq_dep in seq_deposits:
                depid = positive_id(seq_dep.get("siDP"), "sequence deposit.siDP")
                sidp = f"straininfo.deposit:{depid}"
                own = dep_records.get(depid)
                if own is None or own["designation"] != seq_dep.get("designation"):
                    raise ValueError(f"{siid}/{accession}: sequence deposit is outside the source record")
                if depid not in matches:
                    continue
                if seq_type == "genome":
                    valid = ASSEMBLY.fullmatch(accession)
                else:
                    valid = seq_type in {"gene", "rrnaop", "patent"} and NUCLEOTIDE.fullmatch(accession)
                if not valid:
                    excluded(siid, sidp, accession, "unsupported_sequence_type_or_accession", seq_type)
                    continue
                for base, evidence in matches[depid]:
                    row = {**base, "source_field": "strain.sequence.accessionNumber",
                           "straininfo_evidence_json": encoded({**evidence, "sequence_type": seq_type,
                                                                 "sequence_deposit_id": sidp})}
                    if seq_type == "genome":
                        assemblies.append({**row, "assembly_id": "ncbi.assembly:" + accession,
                                           "assembly_name": seq.get("description", ""),
                                           "assembly_level": seq.get("assemblyLevel", "")})
                    else:
                        related.append({**row, "record_id": "INSDC:" + accession,
                                        "record_type": "NUCLEOTIDE_SEQUENCE",
                                        "record_name": seq.get("description", "")})
    return (_unique(strain_links, STRAIN_FIELDS), _unique(assemblies, ASSEMBLY_COLUMNS),
            _unique(related, RELATED_COLUMNS), _unique(exclusions, EXCLUSION_FIELDS))
