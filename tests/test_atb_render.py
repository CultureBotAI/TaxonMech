"""AllTheBacteria evidence as it is published: inline on the taxon record.

AllTheBacteria has no per-source browser page. Its assemblies, sample evidence
and source chains are rendered on the strain row of the taxon that classifies
the strain, which makes this the only surface that publishes them — so the
escaping and link-safety checks here are load-bearing rather than incidental.
"""

from __future__ import annotations

import importlib
from copy import deepcopy

import pytest

from taxonmech.report import summarize

SID = "kgmicrobe.strain:bacdive_1"
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


@pytest.fixture
def site(tmp_path, repo_root, monkeypatch):
    """A renderer over one fixture record. Rendering reads only the records;
    the ATB inventories are a seeding input, not a rendering input."""
    monkeypatch.syspath_prepend(str(repo_root / "scripts"))
    renderer = importlib.import_module("render_pages")
    doc = {"identifier": "NCBITaxon:1", "label": "Fixture species", "rank": "SPECIES",
           "taxon_domain": "BACTERIA", "strain_count": 1, "mapping_status": "SEEDED",
           "strains": [{"strain_id": SID, "source_id": "bacdive:1", "designation": "Culture 1"}]}
    records = [(renderer.TAXA_DIR / "bacteria/fixture.yaml", doc)]
    monkeypatch.setattr(renderer, "load_records", lambda: records)
    return renderer, records


def test_taxon_page_exposes_safe_native_links_and_original_sample_evidence(site, tmp_path):
    from tests.rendered_taxon import rendered_taxon
    from tests.test_genome_records import _StrainTableParser

    renderer, records = site
    doc = records[0][1]
    doc["strains"][0]["genome_records"] = [atb_record()]
    evidence = doc["strains"][0]["genome_records"][0]["atb_evidence"]
    evidence["archive_url"] = 'javascript:alert("archive")'
    output = tmp_path / "site"
    renderer.render(output)

    html = rendered_taxon(output, doc["identifier"])
    parsed = _StrainTableParser(SID)
    parsed.feed(html)
    ncbi, other, _related = parsed.cells[-3:]
    assert parsed.headers.index("NCBI genome assemblies") < parsed.headers.index("Other genome records")
    assert "No NCBI assembly link imported" in ncbi["text"]
    # The assembly identifier is published as text: it has no resolvable page
    # of its own now that the browser is gone, and inventing one would be a
    # link to nothing.
    assert ATB in other["text"]
    assert not [href for href in other["hrefs"] if "atb.html" in href]
    assert "https://example.org/1.fa.gz" in other["hrefs"]
    assert "https://www.ebi.ac.uk/ena/browser/view/ERZ1" in other["hrefs"]
    assert "https://gold.jgi.doe.gov/project?id=Gp1" in other["hrefs"]
    assert "DSM 1 <original>" in other["text"]
    assert "SeqKit sum" in other["text"] and "not MD5" in other["text"]
    assert "javascript:" not in html
    assert "&lt;script&gt;" in html and '<script>alert("name")' not in html


def test_the_site_publishes_no_per_source_browser(site, tmp_path):
    """The sources are integrated into the records, so the standalone browsers
    and their indexes must not be published at all — a stale copy left behind
    would keep serving a second, divergent view of the same data."""
    renderer, records = site
    records[0][1]["strains"][0]["genome_records"] = [atb_record()]
    output = tmp_path / "site"
    renderer.render(output)

    for name in ("atb.html", "atb-browser.js", "atb-index.json",
                 "straininfo.html", "straininfo-browser.js", "straininfo-index.json",
                 "straininfo-index.json.gz"):
        assert not (output / name).exists(), f"{name} should no longer be published"
    for directory in ("atb-details", "straininfo-details"):
        assert not (output / directory).exists(), f"{directory}/ should no longer be published"
    landing = (output / "index.html").read_text()
    assert "atb.html" not in landing and "straininfo.html" not in landing


def test_attribution_for_the_integrated_sources_is_published(site, tmp_path):
    """Removing the browsers removed the only page that carried the CC-BY
    notice for these sources. Their metadata is still published on every taxon
    record, so the notice moved to the source catalogue rather than vanishing."""
    renderer, _records = site
    output = tmp_path / "site"
    renderer.render(output)
    sources = (output / "sources.html").read_text()
    assert "Attribution" in sources
    for name in ("AllTheBacteria", "StrainInfo"):
        assert name in sources
    assert "CC-BY-4.0" in sources
    assert "https://creativecommons.org/licenses/by/4.0/" in sources


def test_attribution_refuses_to_publish_without_a_licence(site, monkeypatch, tmp_path):
    """Guard the guard: a manifest that loses its licence must fail the render,
    not publish the metadata silently."""
    renderer, _records = site
    monkeypatch.setitem(renderer.ATTRIBUTION_MANIFESTS, "AllTheBacteria", tmp_path / "absent.yaml")
    with pytest.raises(FileNotFoundError, match="AllTheBacteria"):
        renderer.source_attributions()

    manifest = tmp_path / "no-licence.yaml"
    manifest.write_text("source:\n  release: '2025-05'\n")
    monkeypatch.setitem(renderer.ATTRIBUTION_MANIFESTS, "AllTheBacteria", manifest)
    with pytest.raises(ValueError, match="license"):
        renderer.source_attributions()


def test_atb_report_deduplicates_genome_identifiers_without_promoting_samples(site):
    _renderer, records = site
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
