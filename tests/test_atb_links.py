"""ATB sample links retain source paths and cannot become genome equivalence."""

import json
from copy import deepcopy

import pytest

from taxonmech.atb_links import build_evidence, build_links

SID = "kgmicrobe.strain:bacdive_5"
SAMPLE = "SAMN02604091"
GTDB = "gtdb.genome:RS_GCF_000005845.1"


def atb(sample=SAMPLE, **changes):
    return {
        "sample_accession": sample, "run_accession": "SRR123,ERR456",
        "assembly_accession": "ERZ123", "assembly_seqkit_sum": "seqkit.v0.1_DLS_k0_" + "a" * 32,
        "asm_pipe_filter": "PASS", "asm_fasta_on_osf": "1", "dataset": "661k",
        "scientific_name": "Source organism", "sylph_species_pre_202505": "Source species",
        "in_hq_pre_202505": "T", "sylph_species": "Source species", "sylph_filter": "PASS",
        "hq_filter": "PASS", "osf_tarball_filename": "atb.assembly.r0.2.batch.1.tar.xz",
        "osf_tarball_url": "https://osf.io/download/abc123/",
        "aws_url": f"https://allthebacteria-assemblies.s3.eu-west-2.amazonaws.com/{sample}.fa.gz",
        "comments": "None", **changes,
    }


def base(source="GTDB", **changes):
    row = {
        "strain_id": SID, "source": source, "source_id": GTDB,
        "source_reference_id": "", "taxon_id": "NCBITaxon:511145",
        "matched_strain_id": "kgmicrobe.strain:DSM-30083", "source_strain_identifiers": "DSM 30083",
        "source_strain_field": "ncbi_strain_identifiers", "source_project_id": "", "source_organism_id": "",
    }
    if source == "GOLD":
        row.update(source_id="gold:Ga1", source_project_id="gold:Gp1", source_organism_id="gold:Go1",
                   source_strain_field="ORGANISM CULTURE COLLECTION ID")
    return {**row, **changes}


def sample(sample_id=SAMPLE, source="GTDB", **changes):
    row = base(source)
    row.update(record_id="biosample:" + sample_id, record_type="BIOSAMPLE", record_name="",
               source_field="ncbi_biosample" if source == "GTDB" else "NCBI BIOSAMPLE ACCESSION")
    if source == "GOLD":
        row["source_id"] = row["source_project_id"]
    return {**row, **changes}


def ncbi(identifier="ncbi.assembly:GCF_000005845.1", source="GTDB", **changes):
    return {**base(source), "assembly_id": identifier,
            "source_field": "accession" if source == "GTDB" else "AP GENBANK.assemblyAccession",
            "assembly_name": "Source <assembly>", "assembly_level": "Complete Genome", **changes}


def genome(source="GTDB", **changes):
    return {**base(source), "genome_id": GTDB if source == "GTDB" else "img.taxon:2517572146",
            "source_database": "gtdb" if source == "GTDB" else "img",
            "source_field": "accession" if source == "GTDB" else "AP IMG TAXON ID",
            "genome_name": "Source & genome", **changes}


def links(atb_rows=None, samples=None, assemblies=None, genomes=None, release="2025-05"):
    return build_links(
        [atb()] if atb_rows is None else atb_rows, [sample()] if samples is None else samples,
        [ncbi()] if assemblies is None else assemblies, [genome()] if genomes is None else genomes,
        release=release,
    )


def clean(row):
    return {key: value for key, value in row.items() if key != "strain_id" and value not in (None, "")}


def test_exact_two_source_evidence_is_canonical_deduplicated_and_does_not_mutate_inputs():
    rows = ([atb()], [sample(), sample(source="GOLD"), sample()],
            [ncbi(), ncbi(source="GOLD")], [genome(), genome(source="GOLD")])
    original = deepcopy(rows)
    strain_links, genome_links, exclusions = build_links(*rows, release="2025-05")
    assert rows == original and not exclusions
    assert len(strain_links) == 1
    link = strain_links[0]
    assert link["atb_id"] == "atb.assembly:202505.SAMN02604091"
    assert link["sample_id"] == "biosample:SAMN02604091"
    evidence = json.loads(link["sample_evidence_json"])
    assert {e["source"] for e in evidence} == {"GOLD", "GTDB"}
    assert all("strain_id" not in e and "record_name" not in e for e in evidence)
    assembly = next(r for r in genome_links if r["genome_id"].startswith("ncbi.assembly:"))
    assert assembly["relationship"] == "shares_biosample"
    assert len(json.loads(assembly["source_evidence_json"])) == 2
    assert build_links(*(list(reversed(r)) for r in rows), release="202505") == (
        strain_links, genome_links, exclusions,
    )


def test_gtdb_record_keys_prevent_a_same_strain_genome_sample_cartesian_product():
    other_sample, other_source = "SAMN123", "gtdb.genome:RS_GCF_000005845.2"
    strains, genomes, drops = links(
        atb_rows=[atb(), atb(other_sample)],
        samples=[sample(), sample(other_sample, source_id=other_source)],
        assemblies=[ncbi(), ncbi("ncbi.assembly:GCF_000005845.2", source_id=other_source)], genomes=[],
    )
    assert len(strains) == 2 and not drops
    assert {(row["sample_id"], row["genome_id"]) for row in genomes} == {
        ("biosample:" + SAMPLE, "ncbi.assembly:GCF_000005845.1"),
        ("biosample:" + other_sample, "ncbi.assembly:GCF_000005845.2"),
    }


def test_gold_matches_both_project_and_organism_and_retains_analysis_evidence():
    other = "SAMN123"
    samples = [sample(source="GOLD"), sample(other, source="GOLD", source_id="gold:Gp2",
                                            source_project_id="gold:Gp2")]
    native = [genome(source="GOLD"),
              genome(source="GOLD", genome_id="img.taxon:9", source_id="gold:Ga2",
                     source_project_id="gold:Gp2"),
              genome(source="GOLD", genome_id="img.taxon:10", source_organism_id="gold:Go2"),
              genome(source="GOLD", genome_id="img.taxon:11", source_project_id="")]
    _, rows, drops = links(atb_rows=[atb(), atb(other)], samples=samples, assemblies=[], genomes=native)
    assert not drops
    assert {(r["sample_id"], r["genome_id"]) for r in rows} == {
        ("biosample:" + SAMPLE, "img.taxon:2517572146"), ("biosample:" + other, "img.taxon:9"),
    }
    evidence = json.loads(rows[0]["source_evidence_json"])[0]
    assert evidence["genome"]["source_id"].startswith("gold:Ga")
    assert evidence["sample"]["source_id"] == evidence["genome"]["source_project_id"]
    assert evidence["sample"]["source_organism_id"] == evidence["genome"]["source_organism_id"]


@pytest.mark.parametrize("field,value", [
    ("matched_strain_id", "kgmicrobe.strain:ATCC-11775"),
    ("source_strain_identifiers", "DSM 30083; ATCC 11775"),
    ("source_reference_id", "another-reference"), ("taxon_id", "NCBITaxon:562"),
])
def test_distinct_assertion_context_cannot_borrow_another_sample_path(field, value):
    strain_links, genome_links, _ = links(assemblies=[ncbi(**{field: value})], genomes=[])
    assert strain_links and genome_links == []


def test_bacdive_genomes_cannot_borrow_gtdb_or_gold_samples_from_the_same_strain():
    b = {"strain_id": SID, "source": "BACDIVE", "source_id": "bacdive:5"}
    _, rows, _ = links(assemblies=[{**b, "assembly_id": "ncbi.assembly:GCA_000005845.1"}],
                       genomes=[{**b, "genome_id": "patric:562.10", "source_database": "patric"},
                                {**b, "genome_id": "img.taxon:123", "source_database": "img"}])
    assert rows == []


def test_shared_sample_preserves_multiple_strain_records_and_exact_identifier_versions():
    other = "kgmicrobe.strain:bacdive_10"
    versions = ["ncbi.assembly:GCA_000005845", "ncbi.assembly:GCA_000005845.1",
                "ncbi.assembly:GCA_000005845.10"]
    assemblies = [ncbi(identifier, strain_id=sid, source_field="ncbi_genbank_assembly_accession")
                  for sid in [SID, other] for identifier in versions]
    strains, genomes, _ = links(
        samples=[sample(), sample(strain_id=other)], assemblies=assemblies, genomes=[],
    )
    assert len(strains) == 2 and len(genomes) == 6
    assert {r["genome_id"] for r in genomes} == set(versions)
    assert {r["strain_id"] for r in genomes} == {SID, other}


def test_same_pair_keeps_each_original_assertion_and_each_source_field():
    first = ncbi()
    second = ncbi(assembly_name="Conflicting source name")
    third = ncbi(source_reference_id="2")
    _, rows, _ = links(samples=[sample(), sample(source_reference_id="2")],
                       assemblies=[first, deepcopy(first), second, third], genomes=[])
    assert len(rows) == 1
    assertions = json.loads(rows[0]["source_evidence_json"])
    assert len(assertions) == 3
    assert {json.dumps(p["genome"], sort_keys=True) for p in assertions} == {
        json.dumps(clean(r), sort_keys=True) for r in [first, second, third]
    }
    assert all(p["sample"].get("source_reference_id", "") == p["genome"].get("source_reference_id", "")
               for p in assertions)


@pytest.mark.parametrize("sample_id", ["SAMD00046889", "SAMN02198985", "SAMN15052191"])
def test_three_real_available_atb_samples_without_erz_still_link(sample_id):
    row = atb(sample_id, assembly_accession="NA", asm_pipe_filter="ENA_ASM_SUBMIT_ERR")
    strains, genomes, drops = links(atb_rows=[row], samples=[sample(sample_id)])
    assert strains and genomes and not drops
    assert strains[0]["atb_id"] == "atb.assembly:202505." + sample_id
    assert all(not r["genome_id"].startswith("ERZ") for r in genomes)


def test_quality_failure_does_not_hide_an_available_assembly_with_valid_identity():
    row = atb(hq_filter="CHECKM2_MAX_CONTAM,SYLPH_RESULTS_FAIL", sylph_filter="SYLPH_RESULTS_FAIL")
    strains, genomes, drops = links(atb_rows=[row])
    assert strains and genomes and not drops


def test_source_assembly_length_warning_does_not_hide_available_artifact():
    strains, genomes, drops = links(atb_rows=[atb(asm_pipe_filter="ASM_LEN")])
    assert strains and genomes and not drops


@pytest.mark.parametrize("changes,reason", [
    ({"asm_fasta_on_osf": "0"}, "assembly_unavailable"),
    ({"asm_pipe_filter": "META_FAIL"}, "metadata_identity_flags:META_FAIL"),
    ({"asm_pipe_filter": "NO_RUNS,RMMS"}, "metadata_identity_flags:NO_RUNS,RMMS"),
    ({"asm_pipe_filter": "RUN_CHANGE"}, "metadata_identity_flags:RUN_CHANGE"),
    ({"hq_filter": "META_FAIL"}, "metadata_identity_flags:META_FAIL"),
    ({"sylph_filter": "RUN_REMOVED"}, "metadata_identity_flags:RUN_REMOVED"),
    ({"asm_pipe_filter": "FUTURE_CHECK"}, "unsupported_assembly_filter:FUTURE_CHECK"),
    ({"assembly_seqkit_sum": "NA"}, "missing_or_invalid_sequence_digest"),
    ({"aws_url": "https://example.org/unrelated.fa.gz"}, "missing_or_invalid_assembly_url"),
])
def test_unavailable_unsafe_unknown_or_missing_artifact_rows_are_auditable(changes, reason):
    strains, genomes, drops = links(atb_rows=[atb(**changes), atb("SAMN999", **changes)])
    assert strains == genomes == []
    assert drops == [{"sample_id": "biosample:" + SAMPLE, "reason": reason}]


def test_sample_ids_are_exact_and_composite_metadata_keys_are_never_split():
    assert links(atb_rows=[atb("SAMN026040910"), atb(SAMPLE + ";SAMN123", asm_fasta_on_osf="0")]) == (
        [], [], [],
    )
    assert links(samples=[sample(source="GOLD", record_type="BIOPROJECT")]) == ([], [], [])


@pytest.mark.parametrize("changes", [
    {"record_id": "NCBITaxon:562"}, {"source_id": ""}, {"matched_strain_id": ""},
    {"source_field": "ncbi_bioproject"},
])
def test_incomplete_or_malformed_existing_biosample_evidence_fails_closed(changes):
    with pytest.raises(ValueError):
        links(samples=[sample(**changes)])


def test_gold_sample_must_be_asserted_by_its_stated_project():
    with pytest.raises(ValueError, match="stated Gp project"):
        links(samples=[sample(source="GOLD", source_id="gold:Gp999")])


@pytest.mark.parametrize("assembly,field", [
    ("ncbi.assembly:GCF_000005845.2", "accession"),
    ("ncbi.assembly:GCF_000005845.1", "ncbi_genbank_assembly_accession"),
])
def test_native_assembly_fields_cannot_be_retyped_or_borrow_another_gtdb_accession(assembly, field):
    with pytest.raises(ValueError, match="GTDB"):
        links(assemblies=[ncbi(assembly, source_field=field)])


def test_duplicate_matching_source_sample_or_invalid_release_fails_before_returning_links():
    with pytest.raises(ValueError, match="duplicate ATB"):
        links(atb_rows=[atb(), atb()])
    with pytest.raises(ValueError, match="release"):
        links(release="latest")


def test_evidence_builder_does_not_require_atb_rows_to_expose_original_sample_paths():
    sample_map, genome_map = build_evidence([sample()], [ncbi()], [genome()])
    assert sample_map[SID, "biosample:" + SAMPLE] == [clean(sample())]
    assert genome_map[SID, "biosample:" + SAMPLE, GTDB] == [
        {"genome": clean(genome()), "sample": clean(sample())},
    ]
