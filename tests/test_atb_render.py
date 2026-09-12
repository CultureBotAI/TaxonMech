"""ATB browser eligibility, evidence, links and separate coverage counts."""

from __future__ import annotations

import csv
import importlib
import json
import shutil
import subprocess
from copy import deepcopy
from pathlib import Path

import pytest

from taxonmech.atb_catalog import ASSEMBLY_COLUMNS
from taxonmech.report import summarize

SID = "kgmicrobe.strain:bacdive_1"
OTHER = "kgmicrobe.strain:bacdive_2"
ATB = "atb.assembly:202505.SAMN1"
SAMPLE = {"record_id": "biosample:SAMN1", "record_type": "BIOSAMPLE", "source": "GOLD",
          "source_id": "gold:Gp1", "source_field": "PROJECT NCBI BIOSAMPLE ID",
          "source_organism_id": "gold:Go1", "source_project_id": "gold:Gp1",
          "matched_strain_id": "kgmicrobe.strain:DSM-1",
          "source_strain_field": "ORGANISM CULTURE COLLECTION ID",
          "source_strain_identifiers": "DSM 1 <original>"}


def atb_record():
    return {"genome_id": ATB, "source_id": ATB, "source": "ALLTHEBACTERIA",
            "source_database": "allthebacteria", "genome_name": 'Species <script>alert("name")</script>',
            "atb_evidence": {
                "release": "2025-05", "sample_id": "biosample:SAMN1", "ena_analysis_id": "ena.analysis:ERZ1",
                "run_accessions": "ERR1,ERR2", "assembly_seqkit_sum": "seqkit.v0.1_DLS_k0_" + "a" * 32,
                "dataset": "2024-08", "assembly_filter": "PASS", "hq_filter": "FALSE",
                "download_url": "https://example.org/1.fa.gz", "archive_url": "https://osf.io/example",
                "archive_filename": "part001.tar", "sample_links": [deepcopy(SAMPLE)],
            }}


def write_tsv(path, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


@pytest.fixture
def browser(tmp_path, repo_root, monkeypatch):
    monkeypatch.syspath_prepend(str(repo_root / "scripts"))
    renderer = importlib.import_module("render_pages")
    directory = tmp_path / "atb"
    directory.mkdir()
    (directory / "MANIFEST.yaml").write_text("source:\n  release: '2025-05'\n  license: CC-BY-4.0\n")
    rows = []
    for n in range(1, 4):
        row = dict.fromkeys(ASSEMBLY_COLUMNS, "NA")
        row.update(sample_accession=f"SAMN{n}", assembly_accession=f"ERZ{n}",
                   scientific_name='Species <script>alert("name")</script>',
                   run_accession="ERR1,ERR2", assembly_seqkit_sum="seqkit:source-sum",
                   asm_pipe_filter="PASS", asm_fasta_on_osf="1", hq_filter="FALSE",
                   dataset="2024-08", aws_url=f"https://example.org/{n}.fa.gz",
                   osf_tarball_url="https://osf.io/example", osf_tarball_filename="part001.tar")
        rows.append(row)
    rows[1]["assembly_accession"] = "NA"  # Available FASTA without an ENA analysis.
    rows[2]["asm_fasta_on_osf"] = "0"  # Metadata overlap alone cannot become a browser result.
    write_tsv(directory / "assemblies.tsv", rows)
    strain_links = [
        {"strain_id": sid, "atb_id": f"atb.assembly:202505.SAMN{n}", "sample_id": f"biosample:SAMN{n}",
         "sample_evidence_json": json.dumps([{**SAMPLE, "record_id": f"biosample:SAMN{n}"}])}
        for n, sid in [(1, SID), (2, OTHER)]
    ]
    write_tsv(directory / "strain_links.tsv", strain_links)
    genome_links = [
        {"strain_id": SID, "atb_id": ATB, "sample_id": "biosample:SAMN1", "genome_id": gid,
         "relationship": "shares_biosample", "source_evidence_json": json.dumps([
             {"genome": {"source": "GOLD", "source_id": "gold:Ga1", "source_project_id": "gold:Gp1",
                         "source_organism_id": "gold:Go1"}, "sample": SAMPLE}])}
        for gid in ["img.taxon:1", "ncbi.assembly:GCA_000000001.2"]
    ]
    write_tsv(directory / "genome_links.tsv", genome_links)
    strains = tmp_path / "bacdive_strains.tsv"
    write_tsv(strains, [
        {"strain_id": sid, "bacdive_id": str(n), "designation": f"Culture {n}",
         "culture_collection_ids": f"kgmicrobe.strain:DSM-{n}"}
        for n, sid in [(1, SID), (2, OTHER)]
    ])
    doc = {"identifier": "NCBITaxon:1", "label": "Fixture species", "rank": "SPECIES",
           "taxon_domain": "BACTERIA", "strain_count": 2, "mapping_status": "SEEDED",
           "strains": [{"strain_id": SID, "source_id": "bacdive:1", "designation": "Culture 1"}]}
    records = [(renderer.TAXA_DIR / "bacteria/fixture.yaml", doc)]
    monkeypatch.setattr(renderer, "ATB_DIR", directory)
    monkeypatch.setattr(renderer, "STRAINS_TSV", strains)
    monkeypatch.setattr(renderer, "load_records", lambda: records)
    return renderer, records, directory, strains


def test_browser_retains_eligible_unlisted_strains_exact_metadata_and_source_chains(browser):
    renderer, records, directory, strains = browser
    index = renderer.build_atb_index(records, directory, strains)
    first, other = index["assemblies"]
    assert index["release"] == "2025-05"
    assert [row["atb_id"] for row in index["assemblies"]] == [ATB, "atb.assembly:202505.SAMN2"]
    assert set(first["metadata"]) == set(ASSEMBLY_COLUMNS)
    assert first["strains"][0]["sample_evidence"] == [SAMPLE]
    assert first["strains"][0]["taxon_pages"][0]["page"] == (
        "taxa/bacteria/fixture.html#strains-kgmicrobe.strain-bacdive_1")
    assert other["strains"][0]["taxon_pages"] == []
    assert other["strains"][0]["source_id"] == "bacdive:2"
    assert other["metadata"]["assembly_accession"] == "NA"
    assert first["metadata"]["hq_filter"] == "FALSE"
    assert first["genome_links"][0]["genome_id"] == "ncbi.assembly:GCA_000000001.2"
    assert first["genome_links"][0]["source_evidence"][0]["sample"] == SAMPLE
    assert {link["relationship"] for link in first["genome_links"]} == {"shares_biosample"}
    assert other["genome_links"] == []


@pytest.mark.parametrize("change", ["sample", "strain", "relationship", "missing_metadata"])
def test_browser_rejects_inconsistent_committed_crosslinks(browser, change):
    renderer, records, directory, strains = browser
    if change == "missing_metadata":
        rows = renderer._tsv(directory / "assemblies.tsv")
        write_tsv(directory / "assemblies.tsv", rows[1:])
    else:
        rows = renderer._tsv(directory / "genome_links.tsv")
        key, value = {"sample": ("sample_id", "biosample:SAMN999"),
                      "strain": ("strain_id", OTHER), "relationship": ("relationship", "sameAs")}[change]
        rows[0][key] = value
        write_tsv(directory / "genome_links.tsv", rows)
    with pytest.raises(ValueError):
        renderer.build_atb_index(records, directory, strains)


def test_taxon_and_atb_pages_expose_safe_native_links_and_original_sample_evidence(browser, tmp_path):
    from tests.test_genome_records import _StrainTableParser

    renderer, records, directory, _strains = browser
    doc = records[0][1]
    doc["strains"][0]["genome_records"] = [atb_record()]
    evidence = doc["strains"][0]["genome_records"][0]["atb_evidence"]
    evidence["archive_url"] = 'javascript:alert("archive")'
    output = tmp_path / "site"
    renderer.render(output)
    html = (output / "taxa/bacteria/fixture.html").read_text()
    parsed = _StrainTableParser(SID)
    parsed.feed(html)
    ncbi, other, _related = parsed.cells[-3:]
    assert parsed.headers.index("NCBI genome assemblies") < parsed.headers.index("Other genome records")
    assert "No NCBI assembly link imported" in ncbi["text"]
    assert "../../atb.html#" + ATB in other["hrefs"]
    assert "https://example.org/1.fa.gz" in other["hrefs"]
    assert "https://www.ebi.ac.uk/ena/browser/view/ERZ1" in other["hrefs"]
    assert "https://gold.jgi.doe.gov/project?id=Gp1" in other["hrefs"]
    assert "DSM 1 <original>" in other["text"]
    assert "SeqKit sum" in other["text"] and "not MD5" in other["text"]
    assert "javascript:" not in html
    assert "&lt;script&gt;" in html and '<script>alert("name")' not in html
    browser_html = (output / "atb.html").read_text()
    assert 'id="atb-query"' in browser_html and 'role="status"' in browser_html
    assert "CC-BY-4.0" in browser_html and "not genome equivalence" in browser_html
    assert "SAMN3" not in (output / "atb-index.json").read_text()
    light_index = json.loads((output / "atb-index.json").read_text())
    assert "sample_evidence" not in light_index["assemblies"][0]["strains"][0]
    full_details = json.loads((output / light_index["assemblies"][0]["detail_path"]).read_text())
    assert full_details[0]["strains"][0]["sample_evidence"] == [SAMPLE]
    assert 'href="atb.html"' in (output / "index.html").read_text()
    assert (output / "atb-browser.js").exists()


def test_atb_report_deduplicates_genome_identifiers_without_promoting_samples(browser):
    _renderer, records, directory, _strains = browser
    doc = records[0][1]
    doc["strains"][0]["genome_records"] = [atb_record()]
    doc["strains"][0]["related_records"] = [SAMPLE]
    doc["strains"][0]["genome_records"] *= 2
    stats = summarize(records + [(records[0][0], deepcopy(doc))])
    coverage = stats["listed_genome_links_by_database"]
    assert list(coverage)[0] == "NCBI"
    assert coverage["AllTheBacteria"] == {"strain_links": 1, "strains": 1, "identifiers": 1}
    assert stats["listed_genome_records"] == 1
    assert stats["listed_related_records_by_type"]["BIOSAMPLE"]["identifiers"] == 1


def test_shipped_browser_script_searches_and_follows_evidence(browser, tmp_path):
    node = shutil.which("node")
    if not node:
        pytest.skip("Node is needed to execute the browser interaction test")
    renderer, records, directory, strains = browser
    index = tmp_path / "atb-index.json"
    renderer.write_atb_browser_data(renderer.build_atb_index(records, directory, strains), tmp_path)
    result = subprocess.run([
        node, str(Path(__file__).with_name("atb_browser_harness.cjs")),
        str(renderer.TEMPLATES_DIR / "atb-browser.js"), str(index),
    ], text=True, capture_output=True, check=False)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "URL safety passed" in result.stdout
