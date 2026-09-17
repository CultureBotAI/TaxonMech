"""Database-specific genome IDs retain direct strain evidence and their syntax."""

from __future__ import annotations

import importlib
import json
from copy import deepcopy
from html.parser import HTMLParser

import pytest

from taxonmech import extract, seed
from taxonmech.report import summarize
from taxonmech.validation.write_validated import validate_taxon
from tests.rendered_taxon import rendered_taxon
from tests.test_seed import _inventory

SID = "kgmicrobe.strain:bacdive_5"
OTHER_SID = "kgmicrobe.strain:bacdive_10"


def _raw_record(bid, genomes):
    return {"General": {"BacDive-ID": bid}, "Sequence information": {"Genome sequences": genomes}}


def _genome(accession="123.10", database="patric", **metadata):
    return {"accession": accession, "database": database, "@ref": 66792,
            "NCBI tax ID": 511145, "description": "Escherichia coli K-12 MG1655",
            "assembly level": "wgs", **metadata}


def _extract(tmp_path, records, strain_ids=(SID,)):
    path = tmp_path / "bacdive.json"
    path.write_text(json.dumps(records), encoding="utf-8")
    return extract.extract_bacdive_genomes(path, set(strain_ids))


def test_database_ids_preserve_suffixes_levels_and_independent_source_taxonomy(tmp_path):
    genomes = [_genome(), _genome("123456789", "img", **{"assembly level": "draft"}),
               _genome("2756170237", "img", **{"assembly level": "complete"}),
               _genome("123.11", **{"assembly level": "plasmid"})]
    assemblies, rows, dropped = _extract(tmp_path, [_raw_record(5, genomes)])
    assert not assemblies and not dropped
    by_id = {row["genome_id"]: row for row in rows}
    assert set(by_id) == {"patric:123.10", "patric:123.11", "img.taxon:123456789",
                          "img.taxon:2756170237"}
    assert by_id["patric:123.10"]["assembly_level"] == "wgs"
    assert by_id["patric:123.11"]["assembly_level"] == "plasmid"
    assert by_id["img.taxon:123456789"]["assembly_level"] == "draft"
    assert by_id["img.taxon:2756170237"]["assembly_level"] == "complete"
    for row in rows:
        assert row["strain_id"] == SID
        assert row["source"] == "BACDIVE"
        assert row["source_id"] == "bacdive:5"
        assert row["source_reference_id"] == "66792"
        # A PATRIC numeric prefix does not override the source's current taxon.
        assert row["taxon_id"] == "NCBITaxon:511145"
        assert row["genome_name"] == genomes[0]["description"]
        assert row["source_database"] == ("patric" if row["genome_id"].startswith("patric:") else "img")


def test_only_identical_assertions_are_deduplicated_and_output_is_deterministic(tmp_path):
    genomes = [_genome(), _genome(), _genome(**{"@ref": 8}),
               _genome(description="Another source description"),
               _genome(**{"NCBI tax ID": 562}), _genome(**{"assembly level": "plasmid"})]
    assemblies, rows, dropped = _extract(tmp_path, [_raw_record(5, genomes)])
    assert not assemblies and not dropped
    assert len(rows) == 5
    assert {row["genome_id"] for row in rows} == {"patric:123.10"}
    assert {row["source_reference_id"] for row in rows} == {"8", "66792"}
    assert {row["taxon_id"] for row in rows} == {"NCBITaxon:511145", "NCBITaxon:562"}
    assert _extract(tmp_path, [_raw_record(5, list(reversed(genomes)))])[1] == rows


def test_cooccurring_database_records_are_not_merged_as_equivalent(tmp_path):
    genomes = [_genome("GCA_000005845.2", "ncbi"), _genome("GCF_000005845.1", "ncbi"),
               _genome(), _genome("2756170237", "img")]
    assemblies, rows, dropped = _extract(tmp_path, [_raw_record(5, genomes)])
    assert not dropped
    assert {row["assembly_id"] for row in assemblies} == {
        "ncbi.assembly:GCA_000005845.2", "ncbi.assembly:GCF_000005845.1",
    }
    assert {row["genome_id"] for row in rows} == {"patric:123.10", "img.taxon:2756170237"}
    assert len(assemblies) == len(rows) == 2


def test_same_genome_identifier_can_have_assertions_for_several_strains(tmp_path):
    assemblies, rows, dropped = _extract(
        tmp_path, [_raw_record(5, _genome()), _raw_record(10, _genome())], (SID, OTHER_SID),
    )
    assert not assemblies and not dropped
    assert len(rows) == 2
    assert {row["genome_id"] for row in rows} == {"patric:123.10"}
    assert {row["strain_id"] for row in rows} == {SID, OTHER_SID}
    assert {row["source_id"] for row in rows} == {"bacdive:5", "bacdive:10"}


@pytest.mark.parametrize(("database", "accession"), [
    ("patric", "GCA_000005845.2"), ("img", "GCA_000005845.2"),
    ("img", "123.10"), ("patric", "123456789"),
    ("patric", "123.10.1"), ("patric", "123.10extra"), ("img", "123456789extra"),
    ("patric", 123.1), ("patric", 123), ("patric", None),
])
def test_known_database_invalid_ids_are_quarantined_without_retyping(tmp_path, database, accession):
    assemblies, rows, dropped = _extract(tmp_path, [_raw_record(5, _genome(accession, database))])
    assert assemblies == rows == []
    assert len(dropped) == 1
    assert dropped[0]["kind"] == "bacdive_genome_record"
    assert dropped[0]["reason"]


def test_database_discriminator_and_source_section_are_required_evidence(tmp_path):
    record = _raw_record(5, [_genome(database="ncbi"), _genome("123456789", "ncbi"),
                             _genome(database="another_database")])
    record["Sequence information"]["16S sequences"] = _genome()
    assemblies, rows, _ = _extract(tmp_path, [record])
    assert assemblies == rows == []


def test_unknown_strain_genome_links_are_auditable(tmp_path):
    assemblies, rows, dropped = _extract(tmp_path, [_raw_record(99, _genome())])
    assert assemblies == rows == []
    assert len(dropped) == 1
    assert dropped[0]["kind"] == "bacdive_genome_record"
    assert "absent from bacdive_strains.tsv" in dropped[0]["reason"]


def test_ncbi_only_api_retains_its_rows_and_drop_scope(tmp_path):
    payload = [_raw_record(5, [_genome("GCA_000005845.2", "ncbi"),
                              _genome("GCA_000005845.3", "ncbi"),
                              _genome("GCA_000005845.0", "ncbi"),
                              _genome(), _genome("bad", "img")])]
    assemblies, rows, dropped = _extract(tmp_path, payload)
    ncbi_rows, ncbi_dropped = extract.extract_bacdive_assemblies(tmp_path / "bacdive.json", {SID})
    assert len(assemblies) == 2 and len(rows) == 1
    assert ncbi_rows == assemblies
    assert ncbi_dropped == [row for row in dropped if row["kind"] == "bacdive_assembly"]
    assert len(ncbi_dropped) == 1


def _document(tmp_path, include_other_only=False):
    inv = _inventory()
    raw = [_raw_record(5, [_genome("GCA_000005845.2", "ncbi"),
                          _genome("GCA_000005845.3", "ncbi"), _genome(),
                          _genome("123456789", "img", description="")])]
    if include_other_only:
        raw.append(_raw_record(10, _genome("562.10")))
    assemblies, rows, dropped = _extract(tmp_path, raw, (SID, OTHER_SID))
    assert not dropped
    inv.strain_assemblies = {SID: assemblies}
    inv.strain_genome_records = {
        sid: [row for row in rows if row["strain_id"] == sid]
        for sid in {row["strain_id"] for row in rows}
    }
    return seed.build_document(seed.build_concepts(inv, ["NCBITaxon:562"])[0], inv), inv


def test_seeding_keeps_ncbi_links_and_adds_only_explicit_genome_record_assertions(tmp_path):
    doc, inv = _document(tmp_path)
    assert validate_taxon(doc) == []
    strain = doc["strains"][0]
    assert strain["strain_id"] == SID
    assert strain["classified_as"] == "NCBITaxon:83333"
    assert len(strain["genome_assemblies"]) == len(strain["genome_records"]) == 2
    assert {row["genome_id"] for row in strain["genome_records"]} == {
        "patric:123.10", "img.taxon:123456789",
    }
    assert all(row["taxon_id"] == "NCBITaxon:511145" for row in strain["genome_records"])
    assert all("strain_id" not in row and "" not in row.values() for row in strain["genome_records"])
    assert "genome_records" not in doc["strains"][1]
    assert not any(x.startswith(("patric:", "img.taxon:")) for x in doc["xrefs"])
    child = seed.build_document(seed.build_concepts(inv, ["NCBITaxon:83333"])[0], inv)
    assert child["strains"][0]["genome_records"] == strain["genome_records"]


def test_strains_without_ncbi_assemblies_still_keep_other_database_links(tmp_path):
    doc, _ = _document(tmp_path, include_other_only=True)
    assert validate_taxon(doc) == []
    strain = next(row for row in doc["strains"] if row["strain_id"] == OTHER_SID)
    assert "genome_assemblies" not in strain
    assert [row["genome_id"] for row in strain["genome_records"]] == ["patric:562.10"]


def test_listing_cap_does_not_truncate_the_genome_record_inventory(tmp_path, monkeypatch):
    doc, inv = _document(tmp_path, include_other_only=True)
    before = deepcopy(inv.strain_genome_records)
    monkeypatch.setattr(seed, "STRAIN_LISTING_CAP", 0)
    capped = seed.build_document(seed.build_concepts(inv, ["NCBITaxon:562"])[0], inv)
    assert capped["strains"] == [] and capped["strain_count"] == doc["strain_count"]
    assert inv.strain_genome_records == before


@pytest.mark.parametrize("field", ["genome_id", "source_database", "source", "source_id"])
def test_schema_requires_genome_identity_and_provenance(tmp_path, field):
    doc, _ = _document(tmp_path)
    del doc["strains"][0]["genome_records"][0][field]
    assert validate_taxon(doc)


@pytest.mark.parametrize("genome_id", [
    "ncbi.assembly:GCA_000005845.2", "NCBITaxon:562", "INSDC:AB681728", "IMG:123456789",
    "patric:123", "patric:123.10.1", "patric:123.10extra", "img.taxon:123.10",
])
def test_schema_rejects_ids_from_other_entity_types_or_with_invalid_syntax(tmp_path, genome_id):
    doc, _ = _document(tmp_path)
    doc["strains"][0]["genome_records"][0]["genome_id"] = genome_id
    assert validate_taxon(doc)


def test_report_counts_database_identifiers_strain_pairs_and_evidence_separately(tmp_path):
    doc, _ = _document(tmp_path, include_other_only=True)
    first, second = doc["strains"]
    patric = next(row for row in first["genome_records"] if row["source_database"] == "patric")
    first["genome_records"].extend([deepcopy(patric), {**patric, "source_reference_id": "8"}])
    # The same identifier on a different strain is another link, not another identifier.
    second["genome_records"].append({**patric, "source_id": "bacdive:10"})
    stats = summarize([(tmp_path / "species.yaml", doc), (tmp_path / "child.yaml", deepcopy(doc))])
    assert stats["listed_strain_assembly_links"] == 2
    assert stats["listed_assemblies"] == 2
    assert stats["listed_strains_with_assemblies"] == 1
    assert stats["listed_genome_record_links"] == 4
    assert stats["listed_genome_records"] == 3
    assert stats["listed_strains_with_genome_records"] == 2
    assert stats["listed_strains_with_any_genome"] == 2
    coverage = stats["listed_genome_links_by_database"]
    assert list(coverage) == ["NCBI", "GTDB", "PATRIC", "IMG", "AllTheBacteria"]
    assert coverage == {
        "NCBI": {"strain_links": 2, "strains": 1, "identifiers": 2},
        "GTDB": {"strain_links": 0, "strains": 0, "identifiers": 0},
        "PATRIC": {"strain_links": 3, "strains": 2, "identifiers": 2},
        "IMG": {"strain_links": 1, "strains": 1, "identifiers": 1},
        "AllTheBacteria": {"strain_links": 0, "strains": 0, "identifiers": 0},
    }


class _StrainTableParser(HTMLParser):
    """Collect table headings and the requested strain's cells without layout matching."""

    def __init__(self, strain_id):
        super().__init__()
        self.row_id = f"strains-{strain_id.replace(':', '-')}"
        self.headers = []
        self.cells = []
        self.in_header = self.in_row = self.in_cell = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "th":
            self.in_header = True
            self.headers.append("")
        if tag == "tr" and attrs.get("id") == self.row_id:
            self.in_row = True
        if self.in_row and tag == "td":
            self.in_cell = True
            self.cells.append({"text": "", "hrefs": []})
        if self.in_cell and tag == "a":
            self.cells[-1]["hrefs"].append(attrs.get("href"))

    def handle_endtag(self, tag):
        if tag == "th":
            self.in_header = False
        if tag == "td":
            self.in_cell = False
        if tag == "tr":
            self.in_row = False

    def handle_data(self, data):
        if self.in_header:
            self.headers[-1] += data
        if self.in_cell:
            self.cells[-1]["text"] += data


def test_rendered_strain_links_prioritize_ncbi_and_preserve_other_database_ids(
    tmp_path, repo_root, monkeypatch,
):
    monkeypatch.syspath_prepend(str(repo_root / "scripts"))
    renderer = importlib.import_module("render_pages")
    doc, _ = _document(tmp_path)
    patric = next(row for row in doc["strains"][0]["genome_records"] if row["source_database"] == "patric")
    patric["assembly_level"] = "plasmid"
    patric["genome_name"] = "Plasmid <annotated> & retained"
    path = renderer.TAXA_DIR / "bacteria" / "fixture.yaml"
    monkeypatch.setattr(renderer, "load_records", lambda: [(path, doc)])
    output = tmp_path / "site"
    renderer.render(output)
    html = rendered_taxon(output, doc["identifier"])
    parsed = _StrainTableParser(SID)
    parsed.feed(html)
    assert parsed.headers.index("NCBI genome assemblies") < parsed.headers.index("Other genome records")
    ncbi, other, related = parsed.cells[-3:]
    assert "No related record link imported" in related["text"]
    assert {
        "https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000005845.2",
        "https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000005845.3",
    } <= set(ncbi["hrefs"])
    assert "https://www.bv-brc.org/view/Genome/123.10" in other["hrefs"]
    img_url = ("https://img.jgi.doe.gov/cgi-bin/m/main.cgi?section=TaxonDetail"
               "&page=taxonDetail&taxon_oid=123456789")
    assert img_url in other["hrefs"]
    assert img_url.replace("&", "&amp;") in html
    assert "patric:123.10" in other["text"] and "img.taxon:123456789" in other["text"]
    assert "plasmid" in other["text"]
    assert "Plasmid &lt;annotated&gt; &amp; retained" in html
    # The LPSN marker gene elsewhere on the page is never promoted into a genome column.
    assert "AB681728" not in ncbi["text"] + other["text"]
    assert not any("/nuccore/" in url for url in ncbi["hrefs"] + other["hrefs"])
