"""Source deposit boundaries survive querying, reporting and browser rendering."""

from __future__ import annotations

import gzip
import json
import shutil
import subprocess
from collections import defaultdict
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from taxonmech import straininfo, straininfo_query
from taxonmech.extract import write_tsv
from taxonmech.report import summarize
from taxonmech.straininfo_links import build_links

SID = "kgmicrobe.strain:bacdive_1"
OTHER = "kgmicrobe.strain:bacdive_3"


def source_record(number, deposits, sequences):
    return {
        "strain": {"siID": number, "doi": f"10.60712/SI-ID{number}.3",
                   "status": "published online", "bdID": 1,
                   "relation": {"deposit": [
                       {"siDP": n, "designation": designation, "ccID": n, "erroneous": False}
                       for n, designation in deposits]}, "sequence": sequences},
        "deposits": [{"siDP": n, "designation": designation, "status": "available",
                      "cultureCollection": {"ccID": n, "deprecated": False}}
                     for n, designation in deposits],
    }


def sequence(accession, depid, designation, kind="genome"):
    return {"accessionNumber": accession, "type": kind, "description": "Original <sequence>",
            "deposit": [{"siDP": depid, "designation": designation}]}


@pytest.fixture
def component(tmp_path, monkeypatch, fixture_renderer):
    raw = tmp_path / "data/raw"
    directory = tmp_path / "data/straininfo"
    raw.mkdir(parents=True)
    directory.mkdir()
    strains = [
        {"strain_id": SID, "bacdive_id": "1", "designation": "Local <strain>",
         "culture_collection_ids": "kgmicrobe.strain:DSM-1|kgmicrobe.strain:ATCC-2"},
        {"strain_id": OTHER, "bacdive_id": "3", "designation": "Unlisted strain",
         "culture_collection_ids": "kgmicrobe.strain:DSM-3"},
    ]
    write_tsv(raw / "bacdive_strains.tsv", list(strains[0]), strains)
    previous = {"strain_id": SID, "assembly_id": "ncbi.assembly:GCA_000000001.1",
                "source": "BACDIVE", "source_id": "bacdive:1"}
    write_tsv(raw / "strain_assemblies.tsv", list(previous), [
        previous, {**previous, "assembly_id": "ncbi.assembly:GCA_000000001"}])
    previous = {"strain_id": SID, "genome_id": "img.taxon:123", "source_database": "img",
                "source": "GOLD", "source_id": "gold:Ga1", "source_project_id": "gold:Gp2",
                "source_organism_id": "gold:Go3", "matched_strain_id": "kgmicrobe.strain:DSM-1"}
    write_tsv(raw / "strain_genome_records.tsv", list(previous), [previous])
    sources = [source_record(1, [(11, "DSM 1"), (12, "ATCC 2"), (19, "DSM 999")], [
        sequence("GCA_000000001", 11, "DSM 1"),
        sequence("GCA_000000002", 12, "ATCC 2"),
        sequence("GCA_000000009", 19, "DSM 999"),
        sequence("X12345", 11, "DSM 1", "gene"),
    ]), source_record(3, [(31, "DSM 3")], [])]
    with gzip.open(directory / "records.jsonl.gz", "wt", encoding="utf-8") as handle:
        handle.writelines(json.dumps(record) + "\n" for record in sources)
    tables = build_links(sources, strains)
    for (name, fields), rows in zip(straininfo.TABLES.items(), tables, strict=True):
        straininfo.write_table(directory / name, fields, rows)
    manifest = {"source": {"snapshot": "2026-09-12", "license": "CC-BY-4.0"}}
    (directory / "MANIFEST.yaml").write_text(yaml.safe_dump(manifest))

    def fixture_links(directory, **_kwargs):
        # Byte pin/replay validation has pipeline tests. UI uses the actual
        # typed converter on bounded primary-source-derived fixture tables.
        output = []
        for name, assembly in (("assemblies.tsv", True), ("related_records.tsv.gz", False)):
            grouped = defaultdict(list)
            for row in straininfo.read_rows(directory / name):
                sid, link = straininfo._link(row, assembly=assembly)
                grouped[sid].append(link)
            output.append(dict(grouped))
        return tuple(output)

    monkeypatch.setattr(straininfo, "record_links", fixture_links)
    monkeypatch.setattr(straininfo_query, "ROOT", tmp_path)
    renderer = fixture_renderer
    monkeypatch.setattr(renderer, "STRAININFO_DIR", directory)
    monkeypatch.setattr(renderer, "STRAINS_TSV", raw / "bacdive_strains.tsv")
    monkeypatch.setattr(renderer, "ATB_DIR", tmp_path / "no-atb")
    doc = {"identifier": "NCBITaxon:1", "label": "Fixture <taxon>", "rank": "SPECIES",
           "taxon_domain": "BACTERIA", "strain_count": 2, "mapping_status": "SEEDED",
           "strains": [{"strain_id": SID, "source_id": "bacdive:1", "designation": "Local <strain>"}]}
    records = [(renderer.TAXA_DIR / "bacteria/fixture.yaml", doc)]
    monkeypatch.setattr(renderer, "load_records", lambda: records)
    return directory, raw, renderer, records


def test_exact_query_keeps_genomes_on_their_own_deposit_and_versions(component):
    directory, raw, _, _ = component
    overlap = straininfo_query.load_overlap(directory, raw)
    own = straininfo_query.query_overlap(overlap, strain="SI-ID1", deposit="SI-DP11")
    assert len(own) == 1
    assert [link["assembly_id"] for link in own[0]["assemblies"]] == ["ncbi.assembly:GCA_000000001"]
    assert not straininfo_query.query_overlap(overlap, deposit="11", genome="GCA_000000002")
    assert not straininfo_query.query_overlap(overlap, genome="GCA_000000001.1")
    assert not straininfo_query.query_overlap(overlap, genome="GCA_000000009")
    assert len(straininfo_query.query_overlap(overlap, bacdive="1", genome="GCA_000000002")) == 1
    assert len(straininfo_query.query_overlap(overlap, culture="DSM 1", sequence="X12345")) == 1
    assert not straininfo_query.query_overlap(overlap, culture="DSM-1")
    assert not straininfo_query.query_overlap(overlap, culture="DSM 1", sequence="X12345.1")
    context = own[0]["existing_genome_associations"]
    assert [link["genome_id"] for link in context] == [
        "ncbi.assembly:GCA_000000001", "ncbi.assembly:GCA_000000001.1", "img.taxon:123"]
    assert context[2]["source_evidence"]["source_project_id"] == "gold:Gp2"
    assert {link["relationship"] for link in context} == {"existing_taxonmech_strain_association"}
    assert len(straininfo_query.query_overlap(overlap, existing_genome="img.taxon:123")) == 2
    assert len(straininfo_query.query_overlap(overlap, strain="kgmicrobe.strain:DSM-1")) == 1
    assert len(straininfo_query.query_overlap(overlap, doi="10.60712/SI-ID1.3")) == 2
    assert not straininfo_query.query_overlap(overlap, doi="10.60712/SI-ID1.2")


@pytest.mark.parametrize("selector", [{"deposit": "straininfo.strain:11"}, {"deposit": "0"},
                                      {"strain": "SI-ID1.3"}, {"bacdive": "-1"}])
def test_query_rejects_mistyped_identifiers(component, selector):
    directory, raw, _, _ = component
    with pytest.raises(ValueError):
        straininfo_query.query_overlap(straininfo_query.load_overlap(directory, raw), **selector)


def test_query_cli_checks_current_dependencies_and_outputs(component, monkeypatch, capsys):
    from taxonmech import atb

    calls = []
    monkeypatch.setattr(straininfo, "provenance_problems",
                        lambda root, reproduce: calls.append((root, reproduce)) or ["source pin changed"])
    assert straininfo_query.main(["--deposit", "11"]) == 1
    assert "source pin changed" in capsys.readouterr().err
    assert calls == [(straininfo_query.ROOT, False)]
    monkeypatch.setattr(straininfo, "provenance_problems", lambda root, reproduce: [])
    monkeypatch.setattr(atb, "provenance_problems", lambda root, reproduce: [])
    assert straininfo_query.main(["--deposit", "11", "--evidence"]) == 0
    result = json.loads(capsys.readouterr().out)
    assert result["total_matches"] == 1
    assert result["matches"][0]["assemblies"][0]["straininfo_evidence"]["sequence_deposit_id"] == (
        "straininfo.deposit:11")
    assert straininfo_query.main(["--strain", "1", "--limit", "1", "--offset", "1"]) == 0
    result = json.loads(capsys.readouterr().out)
    assert result["total_matches"] == 2 and len(result["matches"]) == 1
    assert "assembly_ids" in result["matches"][0] and "assemblies" not in result["matches"][0]


def test_reader_does_not_silently_drop_missing_existing_genome_inventory(component):
    directory, raw, _, _ = component
    (raw / "strain_assemblies.tsv").unlink()
    with pytest.raises(FileNotFoundError):
        straininfo_query.load_overlap(directory, raw)


def test_renderer_rejects_missing_straininfo_component_with_linked_taxa(component, tmp_path):
    directory, _, renderer, records = component
    _, related = straininfo.record_links(directory)
    records[0][1]["strains"][0]["related_records"] = related[SID]
    directory.rename(directory.with_name("hidden-straininfo"))
    with pytest.raises(FileNotFoundError, match="MANIFEST.yaml"):
        renderer.render(tmp_path / "site")


def test_query_cli_checks_atb_context_before_using_it(component, monkeypatch, capsys):
    from taxonmech import atb

    (straininfo_query.ROOT / "data/atb").mkdir()
    monkeypatch.setattr(straininfo, "provenance_problems", lambda root, reproduce: [])
    monkeypatch.setattr(atb, "provenance_problems", lambda root, reproduce: ["raw input changed"])
    assert straininfo_query.main(["--existing-genome", "img.taxon:123"]) == 1
    assert "raw input changed" in capsys.readouterr().err


def test_browser_is_uncapped_and_keeps_source_sequences_separate(component, tmp_path):
    directory, raw, renderer, records = component
    overlap = renderer.build_straininfo_index(records, directory, raw / "bacdive_strains.tsv")
    first, other = overlap["records"]
    assert first["url"] == "https://straininfo.dsmz.de/strain/1"
    assert first["doi_url"] == "https://doi.org/10.60712/SI-ID1.3"
    assert first["matches"][0]["url"] == "https://straininfo.dsmz.de/strain/1?SI-DP11"
    assert len(first["source_metadata"]["matched_deposits"]) == 2
    assert other["strains"][0]["taxon_pages"] == []
    assert other["strains"][0]["source_id"] == "bacdive:3"
    assert first["strains"][0]["taxon_pages"][0]["page"].endswith("#strains-kgmicrobe.strain-bacdive_1")
    renderer.write_straininfo_browser_data(overlap, tmp_path)
    index = json.loads((tmp_path / "straininfo-index.json").read_text())
    assert "source_metadata" not in index["records"][0]
    assert index["records"][0]["assembly_ids"] == [
        "ncbi.assembly:GCA_000000001", "ncbi.assembly:GCA_000000002"]
    assert "GCA_000000009" not in json.dumps(index)
    detail = json.loads(gzip.decompress((tmp_path / index["records"][0]["detail_path"]).read_bytes()))
    assert detail == overlap["records"]
    assert gzip.decompress((tmp_path / "straininfo-index.json.gz").read_bytes()) == (
        tmp_path / "straininfo-index.json").read_bytes()
    compressed_before = (tmp_path / "straininfo-index.json.gz").read_bytes()
    renderer.write_straininfo_browser_data(overlap, tmp_path)
    assert (tmp_path / "straininfo-index.json.gz").read_bytes() == compressed_before


def test_browser_detail_batches_respect_byte_limit(component, tmp_path):
    directory, raw, renderer, records = component
    overlap = renderer.build_straininfo_index(records, directory, raw / "bacdive_strains.tsv")
    for group in overlap["records"]:
        group["source_metadata"]["large_description"] = "x" * 600_000
    renderer.write_straininfo_browser_data(overlap, tmp_path)
    files = sorted((tmp_path / "straininfo-details").glob("*.json.gz"))
    assert len(files) == 2 and all(len(gzip.decompress(path.read_bytes())) <= 1_000_000 for path in files)


def test_compressed_taxon_table_retains_anchors_and_escapes_source_text(component, tmp_path, monkeypatch):
    from tests.rendered_taxon import rendered_taxon

    _, _, renderer, records = component
    records[0][1]["strains"][0]["designation"] = "<script>alert(1)</script> Ω"
    renderer.render(tmp_path / "site")
    page = rendered_taxon(tmp_path / "site", records[0][1]["identifier"])
    table = page
    assert 'id="strains-kgmicrobe.strain-bacdive_1"' in table
    assert "https://bacdive.dsmz.de/strain/1" in table
    assert "&lt;script&gt;alert(1)&lt;/script&gt; Ω" in table
    assert "<script>" not in table
    assert ('href="https://github.com/CultureBotAI/TaxonMech/blob/main/'
            'data/taxa/bacteria/fixture.yaml"') in page


def test_generated_script_urls_change_when_browser_code_changes(component, tmp_path, monkeypatch):
    import re

    _, _, renderer, _ = component
    templates = tmp_path / "templates"
    shutil.copytree(renderer.TEMPLATES_DIR, templates)
    monkeypatch.setattr(renderer, "TEMPLATES_DIR", templates)
    renderer.render(tmp_path / "first")
    script = templates / "compressed-data.js"
    script.write_text(script.read_text() + "\n// Updated browser code.\n")
    renderer.render(tmp_path / "second")
    versions = [re.search(r'compressed-data.js\?v=([a-f0-9]{16})',
                          (tmp_path / output / "taxon.html").read_text()).group(1)
                for output in ("first", "second")]
    assert versions[0] != versions[1]


def test_taxon_links_and_report_keep_record_types_separate(component, tmp_path):
    from tests.test_genome_records import _StrainTableParser

    directory, _, renderer, records = component
    assemblies, related = straininfo.record_links(directory)
    strain = records[0][1]["strains"][0]
    strain["genome_assemblies"], strain["related_records"] = assemblies[SID], related[SID]
    renderer.render(tmp_path / "site")
    from tests.rendered_taxon import rendered_taxon
    html = rendered_taxon(tmp_path / "site", records[0][1]["identifier"])
    parsed = _StrainTableParser(SID)
    parsed.feed(html)
    ncbi, _, references = parsed.cells[-3:]
    assert "https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000000001" in ncbi["hrefs"]
    assert "straininfo.html#straininfo.strain:1" in ncbi["hrefs"]
    assert "https://straininfo.dsmz.de/strain/1?SI-DP11" in references["hrefs"]
    assert "https://doi.org/10.60712/SI-ID1.3" in references["hrefs"]
    assert "Strain record-version DOI" in references["text"]
    assert "Nucleotide sequence reference" in references["text"]
    assert "Original &lt;sequence&gt;" in html and "Original <sequence>" not in html
    stats = summarize(records + [(records[0][0], deepcopy(records[0][1]))])
    assert list(stats["listed_genome_links_by_database"])[0] == "NCBI"
    assert "StrainInfo" not in stats["listed_genome_links_by_database"]
    assert stats["listed_assemblies"] == 2
    assert stats["listed_related_records_by_type"]["STRAININFO_STRAIN"]["identifiers"] == 1
    assert stats["listed_related_records_by_type"]["STRAININFO_DEPOSIT"]["identifiers"] == 2
    assert stats["listed_related_records_by_type"]["NUCLEOTIDE_SEQUENCE"]["identifiers"] == 1


def test_atb_context_never_changes_existing_sample_or_genome_evidence(component):
    directory, raw, renderer, records = component
    atb = {"assemblies": [{"strains": [{"strain_id": SID, "sample_evidence": [{"source": "GOLD"}]}],
                           "genome_links": [{"genome_id": "img.taxon:123",
                                             "relationship": "shares_biosample"}]}]}
    before = deepcopy(atb)
    renderer.add_straininfo_context(atb, renderer.build_straininfo_index(
        records, directory, raw / "bacdive_strains.tsv"))
    assert atb["assemblies"][0]["genome_links"] == before["assemblies"][0]["genome_links"]
    strain = atb["assemblies"][0]["strains"][0]
    assert strain.pop("straininfo_context") == [{"straininfo_strain_id": "straininfo.strain:1",
                                                "url": "straininfo.html#straininfo.strain:1"}]
    assert atb == before


@pytest.mark.parametrize("compression", ["json", "gzip", "broken_gzip"])
def test_shipped_straininfo_browser_search_and_native_links(component, tmp_path, compression):
    node = shutil.which("node")
    if not node:
        pytest.skip("Node is needed for the shipped browser interaction test")
    directory, raw, renderer, records = component
    renderer.write_straininfo_browser_data(renderer.build_straininfo_index(
        records, directory, raw / "bacdive_strains.tsv"), tmp_path)
    result = subprocess.run([
        node, str(Path(__file__).with_name("straininfo_browser_harness.cjs")),
        str(renderer.TEMPLATES_DIR / "straininfo-browser.js"), str(tmp_path / "straininfo-index.json"),
        compression,
    ], text=True, capture_output=True, check=False)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "deposit boundaries passed" in result.stdout
