# Cycle 6 Stage 3 UniProtKB protein examples curation and corpus review (626,048 records; 15 causal-graph records, 75 GENE_OR_PROTEIN nodes, 34 live-verified UniProtKB accessions, 246 evidence-backed edges)

- Review: 20261105T015451Z-cycle6-stage3-protein-examples
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-11-04T22:14:00Z
- Finished UTC: 2026-11-05T01:54:51Z
- Reviewer: Antigravity (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 626,048 in-scope TaxonRecord files across Bacteria (605,695), Archaea (14,013), Eukaryota (6,331), and other (9) against the Stage 3 UniProtKB protein-examples contract (.claude/skills/add-uniprot-protein-examples/SKILL.md). Expanded curation/uniprot_proteins.tsv from 29 to 34 live-verified UniProtKB accessions (UniProt release 2026_02), adding reviewed Swiss-Prot proteins UniProtKB:P69783 (PTGA_ECOLI, crr/b2417, NCBITaxon:83333, UP:UP000000625, 169 aa, CRC64 EA18020745531215, v2), UniProtKB:Q00829 (PHRA_BACSU, phrA/BSU12440, NCBITaxon:224308, UP:UP000001570, 44 aa, CRC64 95AA9E07F08D2DCB, v1), UniProtKB:P20581 (PQSE_PSEAE, pqsE/PA1000, EC:3.1.2.32, NCBITaxon:208964, UP:UP000002438, 301 aa, CRC64 CB78E9103D8F221C, v1), UniProtKB:Q58261 (MTRA_METJA, mtrA/MJ0851, EC:7.2.1.4, NCBITaxon:243232, UP:UP000000805, 241 aa, CRC64 155EAE6418E09B8D, v2), and UniProtKB:J9VT33 (CUF1_CRYN9, CUF1/CNAG_07724, NCBITaxon:235443, UP:UP000010091, 1048 aa, CRC64 66941210664729AD, v1). Enriched 11 maintained overlays in curation/causal_graphs/ (NCBITaxon_562, NCBITaxon_83333, NCBITaxon_511145, NCBITaxon_1423, NCBITaxon_224308, NCBITaxon_287, NCBITaxon_208964, NCBITaxon_2190, NCBITaxon_243232, NCBITaxon_5207, NCBITaxon_235443), bringing the 15 maintained overlays from 64 to 75 GENE_OR_PROTEIN nodes (73 carrying UP:* reference proteome_id; 2 on Cryptococcus deneoformans B-3501A NCBITaxon:283643 &amp; species NCBITaxon:40410 omitting proteome_id because strain B-3501A has no UP:UP... proteome cross-reference in UniProtKB 2026_02 whereas sibling strain JEC21 NCBITaxon:214684 has UP:UP000001247) and from 213 to 246 evidence-backed edges. Corpus-wide protein example attachment outside the 15 causal-graph records remains inapplicable because TaxonRecord has no top-level protein slot and the remaining 626,033 records carry causal_graphs: [].

## Scope And Provenance

Full-corpus Cycle 6 Stage 3 UniProtKB protein-example review across all 626,048 TaxonRecord files in data/taxa/, paired with live UniProt REST + NCBI PubMed verification, catalog expansion (29 -&gt; 34 UniProtKB accessions in curation/uniprot_proteins.tsv), and causal-graph overlay enrichment across 11 of the 15 causal-graph-bearing species and reference-proteome strain records (75 GENE_OR_PROTEIN nodes, 246 evidence-backed edges).

Selection: All 626,048 in-scope taxa in curation/seed_scope.tsv and data/taxa/PATHS.tsv classified by causal_graphs presence, with 100% direct inspection, live UniProtKB/PubMed verification, and validation of all 15 causal-graph-bearing species and strain records.
Coverage: sampled; 15 reviewed / 626048 in the declared population.
Source: working_tree at Git base 27fac6f9541901a91d0af83df96bb41867ea4f9f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:562 | data/taxa/bacteria/escherichia_coli.yaml | generated | Escherichia coli |
| NCBITaxon:83333 | data/taxa/bacteria/escherichia_coli_k_12.yaml | generated | Escherichia coli K-12 |
| NCBITaxon:511145 | data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml | generated | Escherichia coli str. K-12 substr. MG1655 |
| NCBITaxon:1423 | data/taxa/bacteria/bacillus_subtilis.yaml | generated | Bacillus subtilis |
| NCBITaxon:224308 | data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml | generated | Bacillus subtilis subsp. subtilis str. 168 |
| NCBITaxon:287 | data/taxa/bacteria/pseudomonas_aeruginosa.yaml | generated | Pseudomonas aeruginosa |
| NCBITaxon:208964 | data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml | generated | Pseudomonas aeruginosa PAO1 |
| NCBITaxon:2190 | data/taxa/archaea/methanocaldococcus_jannaschii.yaml | generated | Methanocaldococcus jannaschii |
| NCBITaxon:243232 | data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml | generated | Methanocaldococcus jannaschii DSM 2661 |
| NCBITaxon:1859096 | data/taxa/eukaryota/cryptococcus_deuterogattii.yaml | generated | Cryptococcus deuterogattii |
| NCBITaxon:294750 | data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml | generated | Cryptococcus deuterogattii R265 |
| NCBITaxon:40410 | data/taxa/eukaryota/cryptococcus_deneoformans.yaml | generated | Cryptococcus deneoformans |
| NCBITaxon:283643 | data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml | generated | Cryptococcus deneoformans B-3501A |
| NCBITaxon:5207 | data/taxa/eukaryota/cryptococcus_neoformans.yaml | generated | Cryptococcus neoformans |
| NCBITaxon:235443 | data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml | generated | Cryptococcus neoformans H99 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict LinkML and custom semantic validation on all 15 causal-graph-seeded TaxonRecord files | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:5207, NCBITaxon:235443 | All 15 seeded TaxonRecord YAML files (including the 11 records updated in Cycle 6 Stage 3) pass scripts/validate_strict.py with 0 errors. |
| OAK ID-label correspondence validation across all 15 causal-graph overlays and seeded records | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:5207, NCBITaxon:235443 | scripts/validate_id_label_correspondence.py reports 98 OK_CANONICAL, 184 SKIPPED_NO_ADAPTER, and 0 MISMATCH across all grounded nodes in curation/causal_graphs/*.yaml and the 15 seeded TaxonRecord files. |
| Unit and integration test suite for causal-graph overlays, offline UniProtKB reference proteome validation, structural referential integrity, seeder merge, and HTML rendering | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:5207, NCBITaxon:235443 | tests/test_causal_graph_overlays.py passes all 7 tests covering roundtrip seeding, offline UniProtKB reference proteome/lineage/strain validation (34 proteins, 75 GENE_OR_PROTEIN nodes, 246 edges), structural validation, and HTML rendering. |

## Scientific And Domain Assessments

### Live-verified UniProtKB protein examples and reference proteome metadata across all 15 causal-graph-bearing species and strain records

grounding: supported. Targets: NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:5207, NCBITaxon:235443.

Expanded curation/uniprot_proteins.tsv from 29 to 34 live-verified UniProtKB accessions (32 SWISS_PROT, 2 TREMBL) and enriched 11 maintained causal-graph overlays across Escherichia coli (NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145; adding Crr / EIIAGlc UniProtKB:P69783 crr/b2417 alongside CyaA UniProtKB:P00936, CRP UniProtKB:P0ACJ8, LacZ UniProtKB:P00722, LacY UniProtKB:P02920, LacI UniProtKB:P03023, and LacA UniProtKB:P07464 on UP:UP000000625, with edges e22, e23, e24 supported by PMID:8576228, PMID:8990282, and PMID:10986234), Bacillus subtilis (NCBITaxon:1423, NCBITaxon:224308; adding PhrA UniProtKB:Q00829 phrA/BSU12440 alongside RapA UniProtKB:Q00828, KinA UniProtKB:P16497, KinB UniProtKB:Q08430, Spo0F UniProtKB:P06628, Spo0B UniProtKB:P06535, Spo0A UniProtKB:P06534, and Spo0E UniProtKB:P05043 on UP:UP000001570, with edges e29, e30, e31 supported by PMID:9384377 and PMID:12686606), Pseudomonas aeruginosa (NCBITaxon:287, NCBITaxon:208964; adding PqsE UniProtKB:P20581 pqsE/PA1000 alongside PhzA1 UniProtKB:Q9HWH1, PhzB1 UniProtKB:O69753, PhzD1 UniProtKB:P0DPB9, PhzM UniProtKB:Q9HWH2, and PhzS UniProtKB:Q9HWG9 on UP:UP000002438, with edges e12, e13, e14 supported by PMID:12183623, PMID:18390653, and PMID:30397240), Methanocaldococcus jannaschii (NCBITaxon:2190, NCBITaxon:243232; adding MtrA UniProtKB:Q58261 mtrA/MJ0851 alongside FwdB UniProtKB:P61154, Mer UniProtKB:Q58929, McrA UniProtKB:Q58256, McrB UniProtKB:Q58252, and McrG UniProtKB:Q58255 on UP:UP000000805, with edges e16, e17, e18 supported by PMID:8688087, PMID:7925428, and PMID:9889203), and Cryptococcus neoformans (NCBITaxon:5207, NCBITaxon:235443; adding Cuf1 UniProtKB:J9VT33 CUF1/CNAG_07724 alongside BZP4 UniProtKB:J9VQ26, LAC1 UniProtKB:J9VY90, and LAC2 UniProtKB:J9VQZ4 on UP:UP000010091, with edges e12, e13, e14 supported by PMID:24743168, PMID:17449657, and PMID:29632091), bringing all 15 overlays to 75 GENE_OR_PROTEIN nodes and 246 evidence-backed edges.

### Inapplicability of UniProtKB protein examples on the remaining 626,033 TaxonRecord files without causal_graphs

scope: concern. Targets: NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:5207, NCBITaxon:235443.

TaxonRecord has no top-level protein slot; protein examples are represented exclusively as CausalNode entries with node_type: GENE_OR_PROTEIN inside TaxonRecord.causal_graphs. Until data/raw/taxon_trait_edges.tsv is populated from an upstream kg-microbe checkout (#78 / taxonmech-infra-0002), the remaining 626,033 in-scope records carry causal_graphs: [] and have no mechanism graph nodes to which UniProtKB accessions can be attached.

## Findings

### finding-001: Committed data/raw/{madin_taxa,bactotraits_taxa}.tsv store pre-aggregated assertion counts pending upstream kg-microbe re-extraction

minor / deferred / confirmed; issue key: taxonmech-extract-collapses-trait-edges-to-counts.

Although src/taxonmech/extract.py provides extract_taxon_trait_edges() and TRAIT_EDGE_FIELDS (landed in Cycle 1 Stage 6 PR #152 under issue #78 / taxonmech-infra-0002), the committed raw files data/raw/madin_taxa.tsv (34,148 rows) and data/raw/bactotraits_taxa.tsv (9,658 rows) still hold 2-column (taxon_id, assertion_count) summaries until an upstream kg-microbe checkout re-extraction populates data/raw/taxon_trait_edges.tsv.

Disposition: Tracked under open issue #78 (taxonmech-infra-0002 in INFRA_TASKS.md) pending upstream kg-microbe edge-table re-extraction.

## Recommended Actions And Acceptance Checks

### action-001

Run extract_taxon_trait_edges() against an upstream kg-microbe checkout to populate data/raw/taxon_trait_edges.tsv and expand automated causal-graph overlays (#78).

- data/raw/taxon_trait_edges.tsv is populated with predicate, object CURIE, and publication provenance from kg-microbe

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| curated-uniprot-catalog-and-overlays | curation/uniprot_proteins.tsv; curation/causal_graphs/NCBITaxon_*.yaml; data/taxa/{bacteria,archaea,eukaryota}/*.yaml; curation/uniprot_proteins.tsv (34 rows); curation/causal_graphs/NCBITaxon_{562,83333,511145,1423,224308,287,208964,2190,243232,1859096,294750,40410,283643,5207,235443}.yaml | supports | Thirty-four live-verified UniProtKB accessions in curation/uniprot_proteins.tsv ground 75 GENE_OR_PROTEIN nodes (73 with UP:* proteome_id, 2 without on C. deneoformans B-3501A) and 246 evidence-backed causal edges across the 15 maintained overlays and seeded TaxonRecord YAML files. |
| oak-id-label-validation | conf/id_label_targets.yaml; scripts/validate_id_label_correspondence.py; conf/id_label_targets.yaml:18-65 | supports | All OBO-grounded node pairs across GO and CHEBI in the 15 causal-graph overlays and seeded records match canonical OAK ontology labels (98 OK_CANONICAL, 184 SKIPPED_NO_ADAPTER, 0 MISMATCH). |
| seeder-and-uniprot-catalog-validation | src/taxonmech/seed.py; curation/uniprot_proteins.tsv; tests/test_causal_graph_overlays.py; src/taxonmech/seed.py:217-460,790-810; tests/test_causal_graph_overlays.py:1-225 | supports | load_uniprot_proteins(), validate_causal_graph_proteins(), and validate_causal_graph_structure() enforce exact organism lineage compatibility, UP:* reference proteome membership, review_status, gene_symbol, locus_tag, ec_number, length, sequence_crc64, sequence_version, and BacDive strain_id consistency across all 75 GENE_OR_PROTEIN nodes and 246 causal edges. |
| raw-phenotype-and-trait-inventories | data/raw/madin_taxa.tsv; data/raw/bactotraits_taxa.tsv; data/raw/mediadive_taxa.tsv; madin_taxa.tsv (34,148 rows); bactotraits_taxa.tsv (9,658 rows); mediadive_taxa.tsv (14,154 rows) | supports | Committed raw tables in data/raw/madin_taxa.tsv and data/raw/bactotraits_taxa.tsv store 2-column (taxon_id, assertion_count) summaries until an upstream kg-microbe checkout re-extraction runs extract_taxon_trait_edges(), leaving 626,033 in-scope records with causal_graphs: []. |

## Limits And Additional Notes

- 626,033 of 626,048 in-scope records carry causal_graphs: [] and have no top-level protein slot on TaxonRecord; bulk causal-graph expansion awaits upstream kg-microbe re-extraction (#78 / taxonmech-infra-0002).
- Cryptococcus deneoformans B-3501A (NCBITaxon:283643) and its parent species C. deneoformans (NCBITaxon:40410) intentionally omit UP:* proteome_id on LAC1 (UniProtKB:Q55P57) because strain B-3501A has no UP:UP... proteome cross-reference in UniProtKB 2026_02 (whereas sibling strain JEC21 NCBITaxon:214684 has UP:UP000001247).
- Cryptococcus deuterogattii R265 (NCBITaxon:294750, reference proteome UP:UP000029445) has 0 reviewed Swiss-Prot entries for CAP59 and LAC1 in UniProtKB 2026_02; CAP59 (UniProtKB:A0A095C6P1) and LAC1 (UniProtKB:A0A095CIC4) are reference-proteome TrEMBL entries with explicit review_status: TREMBL in curation/uniprot_proteins.tsv.
- Cycle 6 Stage 3 expanded curation/uniprot_proteins.tsv from 29 to 34 live-verified UniProtKB accessions (32 SWISS_PROT, 2 TREMBL) and enriched 11 maintained causal-graph overlays from 64 to 75 GENE_OR_PROTEIN nodes and from 213 to 246 evidence-backed edges across all 15 causal-graph records.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T015451Z-cycle6-stage3-protein-examples
kind: batch
repository: CultureBotAI/TaxonMech
title: Cycle 6 Stage 3 UniProtKB protein examples curation and corpus review (626,048
  records; 15 causal-graph records, 75 GENE_OR_PROTEIN nodes, 34 live-verified UniProtKB
  accessions, 246 evidence-backed edges)
started_at: '2026-11-04T22:14:00Z'
finished_at: '2026-11-05T01:54:51Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: independent
  independence_basis: Cycle 6 Stage 3 UniProtKB protein-example curation and audit
    worker; verified all native prerequisite gates (.claude/skills/add-uniprot-protein-examples/SKILL.md),
    live-verified 5 additional Swiss-Prot UniProtKB accessions (release 2026_02) and
    their primary PubMed citations against live UniProt REST and NCBI E-utilities,
    expanded curation/uniprot_proteins.tsv from 29 to 34 entries (32 SWISS_PROT, 2
    TREMBL), enriched 11 maintained curation/causal_graphs/*.yaml overlays to bring
    the 15 curated overlays from 64 to 75 GENE_OR_PROTEIN nodes (73 with UP:* proteome_id,
    2 without on Cryptococcus deneoformans B-3501A) and from 213 to 246 evidence-backed
    edges, re-seeded all 11 updated TaxonRecord YAML files and 10 taxon-details JSON.gz
    shards, and verified LinkML, OAK ID-label, and offline UniProtKB reference proteome/lineage/strain
    validation.
skill: .claude/skills/add-uniprot-protein-examples/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed all 626,048 in-scope TaxonRecord files across Bacteria (605,695),
  Archaea (14,013), Eukaryota (6,331), and other (9) against the Stage 3 UniProtKB
  protein-examples contract (.claude/skills/add-uniprot-protein-examples/SKILL.md).
  Expanded curation/uniprot_proteins.tsv from 29 to 34 live-verified UniProtKB accessions
  (UniProt release 2026_02), adding reviewed Swiss-Prot proteins UniProtKB:P69783
  (PTGA_ECOLI, crr/b2417, NCBITaxon:83333, UP:UP000000625, 169 aa, CRC64 EA18020745531215,
  v2), UniProtKB:Q00829 (PHRA_BACSU, phrA/BSU12440, NCBITaxon:224308, UP:UP000001570,
  44 aa, CRC64 95AA9E07F08D2DCB, v1), UniProtKB:P20581 (PQSE_PSEAE, pqsE/PA1000, EC:3.1.2.32,
  NCBITaxon:208964, UP:UP000002438, 301 aa, CRC64 CB78E9103D8F221C, v1), UniProtKB:Q58261
  (MTRA_METJA, mtrA/MJ0851, EC:7.2.1.4, NCBITaxon:243232, UP:UP000000805, 241 aa,
  CRC64 155EAE6418E09B8D, v2), and UniProtKB:J9VT33 (CUF1_CRYN9, CUF1/CNAG_07724,
  NCBITaxon:235443, UP:UP000010091, 1048 aa, CRC64 66941210664729AD, v1). Enriched
  11 maintained overlays in curation/causal_graphs/ (NCBITaxon_562, NCBITaxon_83333,
  NCBITaxon_511145, NCBITaxon_1423, NCBITaxon_224308, NCBITaxon_287, NCBITaxon_208964,
  NCBITaxon_2190, NCBITaxon_243232, NCBITaxon_5207, NCBITaxon_235443), bringing the
  15 maintained overlays from 64 to 75 GENE_OR_PROTEIN nodes (73 carrying UP:* reference
  proteome_id; 2 on Cryptococcus deneoformans B-3501A NCBITaxon:283643 & species NCBITaxon:40410
  omitting proteome_id because strain B-3501A has no UP:UP... proteome cross-reference
  in UniProtKB 2026_02 whereas sibling strain JEC21 NCBITaxon:214684 has UP:UP000001247)
  and from 213 to 246 evidence-backed edges. Corpus-wide protein example attachment
  outside the 15 causal-graph records remains inapplicable because TaxonRecord has
  no top-level protein slot and the remaining 626,033 records carry causal_graphs:
  [].'
source:
  git_revision: 27fac6f9541901a91d0af83df96bb41867ea4f9f
  state: working_tree
  inputs:
  - path: .claude/skills/add-uniprot-protein-examples/SKILL.md
    sha256: 7c9d6d5270e4f7568e4df2efec4169d70af499fa33db5e529e9879e14fb82764
    role: context
  - path: .claude/skills/curate-causal-graphs/SKILL.md
    sha256: 2fa7e2978ba4af89df44c366b29bf445805ab1a891645774d3d58a6a2524664d
    role: context
  - path: .claude/skills/curate-yaml-record/SKILL.md
    sha256: 21b59314460383702d1f850d3747f9dbaec5b7fe67c77391b19c9c490c289cca
    role: context
  - path: AGENTS.md
    sha256: f47526b17cdb04305ce32cb1da1488b684b8f50a65458116e5013fc0b4b2a248
    role: context
  - path: INFRA_TASKS.md
    sha256: a4b0019fde6745a885bdbd0fd0cc6e95b742b2c6729f84f53efa3e46426a86ae
    role: context
  - path: README.md
    sha256: 1bca33e05ac2caaa595d2ced423d07b1c20785cbd32d4f7bae73a019390a0c16
    role: context
  - path: conf/id_label_targets.yaml
    sha256: efed4c6d9cc218c9d89ba4468e361761ac02ff535e2669de33af6606202e544c
    role: context
  - path: conf/record_review.yaml
    sha256: 366312506b771fc18fc5bfc30d5ec942b2c96212e1f4f95c463cfa1707fbebaa
    role: context
  - path: conf/sources.yaml
    sha256: 464f895ed81d2fee7dff68906bf609c86bf13fc43a5b806ee6f413b4cd02d9ca
    role: context
  - path: curation/causal_graphs/NCBITaxon_1423.yaml
    sha256: 933605380a43b18180e0fa506abe1679b2bf9110c6017dcae9ccca28bf359005
    role: context
  - path: curation/causal_graphs/NCBITaxon_1859096.yaml
    sha256: 0f29a0916110b21224537ec5e337a9e8fa5a61c3a9c3f04885f421e7974d8746
    role: context
  - path: curation/causal_graphs/NCBITaxon_208964.yaml
    sha256: 6c1f5e88a7a5eba5c16d26cb1fcbb1342679b8b45278f3cbec9f97ebf96ebeb1
    role: context
  - path: curation/causal_graphs/NCBITaxon_2190.yaml
    sha256: b91818879ca9162ca4547d302e7ce67777b98a92de28715843b614c4bdb20172
    role: context
  - path: curation/causal_graphs/NCBITaxon_224308.yaml
    sha256: 2031a5f5bc48b44e74e638eca4e4fcf2b01957ca6d9c0ff811a4d5a651daa2cd
    role: context
  - path: curation/causal_graphs/NCBITaxon_235443.yaml
    sha256: c0ba1ae0e7cfe15a8f58ce917ecdb0d69bad5b32337d41c61b9da267b455bca5
    role: context
  - path: curation/causal_graphs/NCBITaxon_243232.yaml
    sha256: 44223271a032d24b1a8ed6fd43bc698695435d20d2564b226bebc011d0e3a450
    role: context
  - path: curation/causal_graphs/NCBITaxon_283643.yaml
    sha256: 3098281e6de9a4dccdcf51f3c7a8db7f47c4c3dfadb333682957c4e331f35caf
    role: context
  - path: curation/causal_graphs/NCBITaxon_287.yaml
    sha256: 1b8ed0113969d24eaad1d4fac3859cd71782a3f9a775d24544e79914feb54c33
    role: context
  - path: curation/causal_graphs/NCBITaxon_294750.yaml
    sha256: 3ec5ba3c0784bbda20a3df13863c7faf96fb21562e01394fa0e69ec9f3f2215e
    role: context
  - path: curation/causal_graphs/NCBITaxon_40410.yaml
    sha256: 425d1eece60fd72e9c552eee49e2af7543b9b278b2555f0c0b991c537d85c3cc
    role: context
  - path: curation/causal_graphs/NCBITaxon_511145.yaml
    sha256: a2a17d36d9e1c96bcb937d089469508843d18ef879d29a4c5a80053f67feffd1
    role: context
  - path: curation/causal_graphs/NCBITaxon_5207.yaml
    sha256: 414db3d974a4ca849e7a1dff7fc68eeff20b464c7b58040f20e47ab63cf73bd6
    role: context
  - path: curation/causal_graphs/NCBITaxon_562.yaml
    sha256: 1d49ce376f5b3e85c26904dce4bcc00d86e00f37bf4344a85fcb390b5d065ecd
    role: context
  - path: curation/causal_graphs/NCBITaxon_83333.yaml
    sha256: d4206847c198a26dbda3d9e1155134e0cf7a92d55a12dcd7577a2a8734a33a6c
    role: context
  - path: curation/causal_graphs/README.md
    sha256: 684f2734914c63b096687e6d4719318ade51a3e503964c41b5c4e6e02eef38e4
    role: context
  - path: curation/seed_scope.tsv
    sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
    role: context
  - path: curation/uniprot_proteins.tsv
    sha256: 02ad94aceaa256beff3c55ad34aff4027c665a24f9f4787e5b01123becdf4356
    role: context
  - path: data/raw/bactotraits_taxa.tsv
    sha256: 976d109cef832d8bf27cc105f67a42efbe900b6946736298602ef6d11158b197
    role: context
  - path: data/raw/gold_organisms.tsv
    sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
    role: context
  - path: data/raw/madin_taxa.tsv
    sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
    role: context
  - path: data/raw/mediadive_taxa.tsv
    sha256: 3f74b78cadfcdb6aeae953e09fdb39e34fd9c5d5ed0be65a04a5d7fb02355905
    role: context
  - path: data/raw/ncbitaxon_taxa.tsv
    sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
    role: context
  - path: data/taxa/PATHS.tsv
    sha256: f8f2e0721cb6839b30530b44be0d3004b9f0e6e2d4be8736f235b10117a8bd99
    role: context
  - path: data/taxa/archaea/methanocaldococcus_jannaschii.yaml
    sha256: 9d320edab5f89d8b35dbb9cfa1141970f16161ad5b1b521ea30c707c34130b55
    role: target
  - path: data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml
    sha256: ee090d33fb46ee2ee1b63119f62ec6c53f42412b364d7d15732c17cd868c1a2e
    role: target
  - path: data/taxa/bacteria/bacillus_subtilis.yaml
    sha256: c33d19629498c452a5adcecfbfb227509443ffc8e367de4d087f721f728b521f
    role: target
  - path: data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml
    sha256: b13bb6c55374246d8c8022bce40fe9e1512fb0f3872b14a1e598fb9155b742b5
    role: target
  - path: data/taxa/bacteria/escherichia_coli.yaml
    sha256: bff1bfb7f055d3e93452066e3930169b378a26fcc6f2292fee8eeb4993a2adbf
    role: target
  - path: data/taxa/bacteria/escherichia_coli_k_12.yaml
    sha256: 542f9815edd63fd0ed9d4d8159357036d91bd7affb093922442789975be635ba
    role: target
  - path: data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml
    sha256: 6806e3e870ea7f9733f2ceb4fb1e497aaa98fdacd7238eadc21220a40a9204b7
    role: target
  - path: data/taxa/bacteria/pseudomonas_aeruginosa.yaml
    sha256: 3e6fb5d2ba42af36fcd4c113e5028ca2b2dbfcadc61103ddc68526b8fad8a7b4
    role: target
  - path: data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml
    sha256: 5e813b4ab2b382ca535d6806b26842d99cdda7780e7243bf85d46de6a3521d24
    role: target
  - path: data/taxa/eukaryota/cryptococcus_deneoformans.yaml
    sha256: 90ed37316d8ea747fdcf3ee3c208e7f34cfa96b9d9a504b5ff6f346fe21fefa5
    role: target
  - path: data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml
    sha256: 28846cf07c1deb3acf5a63cf5470004db24b7eaf227dabb959aa7a24c12a68ce
    role: target
  - path: data/taxa/eukaryota/cryptococcus_deuterogattii.yaml
    sha256: 361df09d787a4889a5a8753f90adf661283f8f555fba9547d4ece43aa4cd8f24
    role: target
  - path: data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml
    sha256: c0a7978eae1b0f1abeba6c77112ecbb1831baecafe2ef3cd95f1c7e09c35a955
    role: target
  - path: data/taxa/eukaryota/cryptococcus_neoformans.yaml
    sha256: 9ed238bc7f629b7b345351a8f7e8523cf681a4676e5fd34c9e81506289aff142
    role: target
  - path: data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml
    sha256: fb5dc06006394a96bbe17a9e263849da3c551e098adb179ed9996003e0354d51
    role: target
  - path: scripts/check_provenance.py
    sha256: e35973c3e7cdae07aba5320d565cac9397376b71fbf56918b2d4da4b3b43874a
    role: context
  - path: scripts/render_pages.py
    sha256: de2984d4c5479778e83f9d1a6fb9ba67f8fbd27d42537fbe2b5151f60f1c0342
    role: context
  - path: scripts/validate_id_label_correspondence.py
    sha256: b5ff41bb52d24f5d7819fb12769e216440f75ec3fb3df3e3cb2c5082fffb40e0
    role: context
  - path: scripts/validate_strict.py
    sha256: d0d75cc805cc746053076b5f75f5e6c817ab15c75a9362f8ce3be53bd4ec7382
    role: context
  - path: scripts/verify_corpus.py
    sha256: faa673e0dbb0388b851c8d8b128aa26e312c2d297ca3686acf029a90cc004537
    role: context
  - path: src/taxonmech/extract.py
    sha256: 15349b9935d9c28cc4a0e037928161cf57f9bf145523cd99ec02bac32a00657b
    role: context
  - path: src/taxonmech/schema/taxonmech.yaml
    sha256: 60747327658d0e2560ac9e58fb6e9a19cf711266300f1eff8b5c64e2917020ad
    role: context
  - path: src/taxonmech/seed.py
    sha256: 79d44ee21ee2f406c841d5f3085daae6d3314874646725e5e31d3949ad534fc7
    role: context
  - path: src/taxonmech/templates/taxon-content.html
    sha256: 9562204e103755b648b32234cf001253e855a64bb46f5de1eb372b5fcf7ad3a2
    role: context
  - path: tests/test_causal_graph_overlays.py
    sha256: 03d648dd80290a91c12da98957c7d139b1b0e15a0f7ca70220459f011e4b07f5
    role: context
scope:
  description: Full-corpus Cycle 6 Stage 3 UniProtKB protein-example review across
    all 626,048 TaxonRecord files in data/taxa/, paired with live UniProt REST + NCBI
    PubMed verification, catalog expansion (29 -> 34 UniProtKB accessions in curation/uniprot_proteins.tsv),
    and causal-graph overlay enrichment across 11 of the 15 causal-graph-bearing species
    and reference-proteome strain records (75 GENE_OR_PROTEIN nodes, 246 evidence-backed
    edges).
  selection: All 626,048 in-scope taxa in curation/seed_scope.tsv and data/taxa/PATHS.tsv
    classified by causal_graphs presence, with 100% direct inspection, live UniProtKB/PubMed
    verification, and validation of all 15 causal-graph-bearing species and strain
    records.
  coverage: sampled
  population_size: 626048
  sampling_method: 'Deterministic corpus-wide inventory of all 626,048 TaxonRecord
    files (15 with causal_graphs, 626,033 with causal_graphs: []) plus 100% direct
    inspection, live UniProt REST / NCBI PubMed verification, and strict validation
    of all 15 causal-graph records and their 75 GENE_OR_PROTEIN nodes across 34 unique
    UniProtKB accessions.'
  reviewed_target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:5207
  - NCBITaxon:235443
targets:
- target_id: NCBITaxon:562
  path: data/taxa/bacteria/escherichia_coli.yaml
  label: Escherichia coli
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_562.yaml
    role: Maintained causal-graph overlay input
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Maintained offline UniProtKB reference proteome catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and overlay merger
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
- target_id: NCBITaxon:83333
  path: data/taxa/bacteria/escherichia_coli_k_12.yaml
  label: Escherichia coli K-12
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_83333.yaml
    role: Maintained causal-graph overlay input
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Maintained offline UniProtKB reference proteome catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and overlay merger
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
- target_id: NCBITaxon:511145
  path: data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml
  label: Escherichia coli str. K-12 substr. MG1655
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_511145.yaml
    role: Maintained causal-graph overlay input
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Maintained offline UniProtKB reference proteome catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and overlay merger
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
- target_id: NCBITaxon:1423
  path: data/taxa/bacteria/bacillus_subtilis.yaml
  label: Bacillus subtilis
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_1423.yaml
    role: Maintained causal-graph overlay input
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Maintained offline UniProtKB reference proteome catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and overlay merger
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
- target_id: NCBITaxon:224308
  path: data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml
  label: Bacillus subtilis subsp. subtilis str. 168
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_224308.yaml
    role: Maintained causal-graph overlay input
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Maintained offline UniProtKB reference proteome catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and overlay merger
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
- target_id: NCBITaxon:287
  path: data/taxa/bacteria/pseudomonas_aeruginosa.yaml
  label: Pseudomonas aeruginosa
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_287.yaml
    role: Maintained causal-graph overlay input
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Maintained offline UniProtKB reference proteome catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and overlay merger
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
- target_id: NCBITaxon:208964
  path: data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml
  label: Pseudomonas aeruginosa PAO1
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_208964.yaml
    role: Maintained causal-graph overlay input
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Maintained offline UniProtKB reference proteome catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and overlay merger
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
- target_id: NCBITaxon:2190
  path: data/taxa/archaea/methanocaldococcus_jannaschii.yaml
  label: Methanocaldococcus jannaschii
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_2190.yaml
    role: Maintained causal-graph overlay input
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Maintained offline UniProtKB reference proteome catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and overlay merger
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
- target_id: NCBITaxon:243232
  path: data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml
  label: Methanocaldococcus jannaschii DSM 2661
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_243232.yaml
    role: Maintained causal-graph overlay input
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Maintained offline UniProtKB reference proteome catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and overlay merger
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
- target_id: NCBITaxon:1859096
  path: data/taxa/eukaryota/cryptococcus_deuterogattii.yaml
  label: Cryptococcus deuterogattii
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_1859096.yaml
    role: Maintained causal-graph overlay input
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Maintained offline UniProtKB reference proteome catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and overlay merger
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
- target_id: NCBITaxon:294750
  path: data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml
  label: Cryptococcus deuterogattii R265
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_294750.yaml
    role: Maintained causal-graph overlay input
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Maintained offline UniProtKB reference proteome catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and overlay merger
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
- target_id: NCBITaxon:40410
  path: data/taxa/eukaryota/cryptococcus_deneoformans.yaml
  label: Cryptococcus deneoformans
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_40410.yaml
    role: Maintained causal-graph overlay input
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Maintained offline UniProtKB reference proteome catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and overlay merger
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
- target_id: NCBITaxon:283643
  path: data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml
  label: Cryptococcus deneoformans B-3501A
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_283643.yaml
    role: Maintained causal-graph overlay input
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Maintained offline UniProtKB reference proteome catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and overlay merger
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
- target_id: NCBITaxon:5207
  path: data/taxa/eukaryota/cryptococcus_neoformans.yaml
  label: Cryptococcus neoformans
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_5207.yaml
    role: Maintained causal-graph overlay input
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Maintained offline UniProtKB reference proteome catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and overlay merger
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
- target_id: NCBITaxon:235443
  path: data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml
  label: Cryptococcus neoformans H99
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_235443.yaml
    role: Maintained causal-graph overlay input
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Maintained offline UniProtKB reference proteome catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and overlay merger
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
checks:
- check_id: validate-strict-15-curated-records
  name: Strict LinkML and custom semantic validation on all 15 causal-graph-seeded
    TaxonRecord files
  status: passed
  required: true
  summary: All 15 seeded TaxonRecord YAML files (including the 11 records updated
    in Cycle 6 Stage 3) pass scripts/validate_strict.py with 0 errors.
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:5207
  - NCBITaxon:235443
  command: .venv/bin/python scripts/validate_strict.py data/taxa/bacteria/escherichia_coli.yaml
    data/taxa/bacteria/escherichia_coli_k_12.yaml data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml
    data/taxa/bacteria/bacillus_subtilis.yaml data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml
    data/taxa/bacteria/pseudomonas_aeruginosa.yaml data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml
    data/taxa/archaea/methanocaldococcus_jannaschii.yaml data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml
    data/taxa/eukaryota/cryptococcus_deuterogattii.yaml data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml
    data/taxa/eukaryota/cryptococcus_deneoformans.yaml data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml
    data/taxa/eukaryota/cryptococcus_neoformans.yaml data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - curated-uniprot-catalog-and-overlays
- check_id: validate-oak-id-label-correspondence
  name: OAK ID-label correspondence validation across all 15 causal-graph overlays
    and seeded records
  status: passed
  required: true
  summary: scripts/validate_id_label_correspondence.py reports 98 OK_CANONICAL, 184
    SKIPPED_NO_ADAPTER, and 0 MISMATCH across all grounded nodes in curation/causal_graphs/*.yaml
    and the 15 seeded TaxonRecord files.
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:5207
  - NCBITaxon:235443
  command: .venv/bin/python scripts/validate_id_label_correspondence.py --config conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - oak-id-label-validation
- check_id: pytest-causal-graph-overlays
  name: Unit and integration test suite for causal-graph overlays, offline UniProtKB
    reference proteome validation, structural referential integrity, seeder merge,
    and HTML rendering
  status: passed
  required: true
  summary: tests/test_causal_graph_overlays.py passes all 7 tests covering roundtrip
    seeding, offline UniProtKB reference proteome/lineage/strain validation (34 proteins,
    75 GENE_OR_PROTEIN nodes, 246 edges), structural validation, and HTML rendering.
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:5207
  - NCBITaxon:235443
  command: .venv/bin/pytest -q tests/test_causal_graph_overlays.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - seeder-and-uniprot-catalog-validation
evidence:
- evidence_id: curated-uniprot-catalog-and-overlays
  kind: record_content
  reference: curation/uniprot_proteins.tsv; curation/causal_graphs/NCBITaxon_*.yaml;
    data/taxa/{bacteria,archaea,eukaryota}/*.yaml
  locator: curation/uniprot_proteins.tsv (34 rows); curation/causal_graphs/NCBITaxon_{562,83333,511145,1423,224308,287,208964,2190,243232,1859096,294750,40410,283643,5207,235443}.yaml
  accessed_at: '2026-11-05T01:54:51Z'
  support: supports
  summary: Thirty-four live-verified UniProtKB accessions in curation/uniprot_proteins.tsv
    ground 75 GENE_OR_PROTEIN nodes (73 with UP:* proteome_id, 2 without on C. deneoformans
    B-3501A) and 246 evidence-backed causal edges across the 15 maintained overlays
    and seeded TaxonRecord YAML files.
  snapshot_sha256: 02ad94aceaa256beff3c55ad34aff4027c665a24f9f4787e5b01123becdf4356
- evidence_id: oak-id-label-validation
  kind: validation
  reference: conf/id_label_targets.yaml; scripts/validate_id_label_correspondence.py
  locator: conf/id_label_targets.yaml:18-65
  accessed_at: '2026-11-05T01:54:51Z'
  support: supports
  summary: All OBO-grounded node pairs across GO and CHEBI in the 15 causal-graph
    overlays and seeded records match canonical OAK ontology labels (98 OK_CANONICAL,
    184 SKIPPED_NO_ADAPTER, 0 MISMATCH).
  snapshot_sha256: efed4c6d9cc218c9d89ba4468e361761ac02ff535e2669de33af6606202e544c
- evidence_id: seeder-and-uniprot-catalog-validation
  kind: validation
  reference: src/taxonmech/seed.py; curation/uniprot_proteins.tsv; tests/test_causal_graph_overlays.py
  locator: src/taxonmech/seed.py:217-460,790-810; tests/test_causal_graph_overlays.py:1-225
  accessed_at: '2026-11-05T01:54:51Z'
  support: supports
  summary: load_uniprot_proteins(), validate_causal_graph_proteins(), and validate_causal_graph_structure()
    enforce exact organism lineage compatibility, UP:* reference proteome membership,
    review_status, gene_symbol, locus_tag, ec_number, length, sequence_crc64, sequence_version,
    and BacDive strain_id consistency across all 75 GENE_OR_PROTEIN nodes and 246
    causal edges.
  snapshot_sha256: 79d44ee21ee2f406c841d5f3085daae6d3314874646725e5e31d3949ad534fc7
- evidence_id: raw-phenotype-and-trait-inventories
  kind: database
  reference: data/raw/madin_taxa.tsv; data/raw/bactotraits_taxa.tsv; data/raw/mediadive_taxa.tsv
  locator: madin_taxa.tsv (34,148 rows); bactotraits_taxa.tsv (9,658 rows); mediadive_taxa.tsv
    (14,154 rows)
  accessed_at: '2026-11-05T01:54:51Z'
  support: supports
  summary: 'Committed raw tables in data/raw/madin_taxa.tsv and data/raw/bactotraits_taxa.tsv
    store 2-column (taxon_id, assertion_count) summaries until an upstream kg-microbe
    checkout re-extraction runs extract_taxon_trait_edges(), leaving 626,033 in-scope
    records with causal_graphs: [].'
  snapshot_sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
assessments:
- assessment_id: uniprot-protein-examples-curated-and-verified
  area: grounding
  topic: Live-verified UniProtKB protein examples and reference proteome metadata
    across all 15 causal-graph-bearing species and strain records
  outcome: supported
  summary: Expanded curation/uniprot_proteins.tsv from 29 to 34 live-verified UniProtKB
    accessions (32 SWISS_PROT, 2 TREMBL) and enriched 11 maintained causal-graph overlays
    across Escherichia coli (NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145; adding
    Crr / EIIAGlc UniProtKB:P69783 crr/b2417 alongside CyaA UniProtKB:P00936, CRP
    UniProtKB:P0ACJ8, LacZ UniProtKB:P00722, LacY UniProtKB:P02920, LacI UniProtKB:P03023,
    and LacA UniProtKB:P07464 on UP:UP000000625, with edges e22, e23, e24 supported
    by PMID:8576228, PMID:8990282, and PMID:10986234), Bacillus subtilis (NCBITaxon:1423,
    NCBITaxon:224308; adding PhrA UniProtKB:Q00829 phrA/BSU12440 alongside RapA UniProtKB:Q00828,
    KinA UniProtKB:P16497, KinB UniProtKB:Q08430, Spo0F UniProtKB:P06628, Spo0B UniProtKB:P06535,
    Spo0A UniProtKB:P06534, and Spo0E UniProtKB:P05043 on UP:UP000001570, with edges
    e29, e30, e31 supported by PMID:9384377 and PMID:12686606), Pseudomonas aeruginosa
    (NCBITaxon:287, NCBITaxon:208964; adding PqsE UniProtKB:P20581 pqsE/PA1000 alongside
    PhzA1 UniProtKB:Q9HWH1, PhzB1 UniProtKB:O69753, PhzD1 UniProtKB:P0DPB9, PhzM UniProtKB:Q9HWH2,
    and PhzS UniProtKB:Q9HWG9 on UP:UP000002438, with edges e12, e13, e14 supported
    by PMID:12183623, PMID:18390653, and PMID:30397240), Methanocaldococcus jannaschii
    (NCBITaxon:2190, NCBITaxon:243232; adding MtrA UniProtKB:Q58261 mtrA/MJ0851 alongside
    FwdB UniProtKB:P61154, Mer UniProtKB:Q58929, McrA UniProtKB:Q58256, McrB UniProtKB:Q58252,
    and McrG UniProtKB:Q58255 on UP:UP000000805, with edges e16, e17, e18 supported
    by PMID:8688087, PMID:7925428, and PMID:9889203), and Cryptococcus neoformans
    (NCBITaxon:5207, NCBITaxon:235443; adding Cuf1 UniProtKB:J9VT33 CUF1/CNAG_07724
    alongside BZP4 UniProtKB:J9VQ26, LAC1 UniProtKB:J9VY90, and LAC2 UniProtKB:J9VQZ4
    on UP:UP000010091, with edges e12, e13, e14 supported by PMID:24743168, PMID:17449657,
    and PMID:29632091), bringing all 15 overlays to 75 GENE_OR_PROTEIN nodes and 246
    evidence-backed edges.
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:5207
  - NCBITaxon:235443
  evidence_ids:
  - curated-uniprot-catalog-and-overlays
  - oak-id-label-validation
  - seeder-and-uniprot-catalog-validation
  metrics:
  - name: unique_verified_uniprot_accessions
    value: 34.0
    unit: accessions
    definition: Unique live-verified UniProtKB accessions in curation/uniprot_proteins.tsv.
    minimum: 0.0
  - name: causal_graph_gene_or_protein_nodes
    value: 75.0
    unit: nodes
    definition: Total GENE_OR_PROTEIN CausalNode instances across the 15 seeded records.
    minimum: 0.0
  - name: evidence_backed_causal_edges
    value: 246.0
    unit: edges
    definition: Total evidence-backed CausalEdge entries across the 15 seeded records.
    minimum: 0.0
- assessment_id: corpus-wide-protein-example-inapplicability
  area: scope
  topic: Inapplicability of UniProtKB protein examples on the remaining 626,033 TaxonRecord
    files without causal_graphs
  outcome: concern
  summary: 'TaxonRecord has no top-level protein slot; protein examples are represented
    exclusively as CausalNode entries with node_type: GENE_OR_PROTEIN inside TaxonRecord.causal_graphs.
    Until data/raw/taxon_trait_edges.tsv is populated from an upstream kg-microbe
    checkout (#78 / taxonmech-infra-0002), the remaining 626,033 in-scope records
    carry causal_graphs: [] and have no mechanism graph nodes to which UniProtKB accessions
    can be attached.'
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:5207
  - NCBITaxon:235443
  evidence_ids:
  - raw-phenotype-and-trait-inventories
findings:
- finding_id: finding-001
  issue_key: taxonmech-extract-collapses-trait-edges-to-counts
  category: provenance
  severity: minor
  status: deferred
  certainty: confirmed
  title: Committed data/raw/{madin_taxa,bactotraits_taxa}.tsv store pre-aggregated
    assertion counts pending upstream kg-microbe re-extraction
  description: 'Although src/taxonmech/extract.py provides extract_taxon_trait_edges()
    and TRAIT_EDGE_FIELDS (landed in Cycle 1 Stage 6 PR #152 under issue #78 / taxonmech-infra-0002),
    the committed raw files data/raw/madin_taxa.tsv (34,148 rows) and data/raw/bactotraits_taxa.tsv
    (9,658 rows) still hold 2-column (taxon_id, assertion_count) summaries until an
    upstream kg-microbe checkout re-extraction populates data/raw/taxon_trait_edges.tsv.'
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:5207
  - NCBITaxon:235443
  field_paths:
  - source_attestations
  - causal_graphs
  evidence_ids:
  - raw-phenotype-and-trait-inventories
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: Raw source extractor
  - repository: CultureBotAI/TaxonMech
    path: data/raw/madin_taxa.tsv
    role: Madin trait inventory
  - repository: CultureBotAI/TaxonMech
    path: data/raw/bactotraits_taxa.tsv
    role: BactoTraits trait inventory
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/78
  disposition_reason: 'Tracked under open issue #78 (taxonmech-infra-0002 in INFRA_TASKS.md)
    pending upstream kg-microbe edge-table re-extraction.'
actions:
- action_id: action-001
  description: Run extract_taxon_trait_edges() against an upstream kg-microbe checkout
    to populate data/raw/taxon_trait_edges.tsv and expand automated causal-graph overlays
    (#78).
  finding_ids:
  - finding-001
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:5207
  - NCBITaxon:235443
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: Raw source extractor
  acceptance_checks:
  - data/raw/taxon_trait_edges.tsv is populated with predicate, object CURIE, and
    publication provenance from kg-microbe
limitations:
- '626,033 of 626,048 in-scope records carry causal_graphs: [] and have no top-level
  protein slot on TaxonRecord; bulk causal-graph expansion awaits upstream kg-microbe
  re-extraction (#78 / taxonmech-infra-0002).'
- Cryptococcus deneoformans B-3501A (NCBITaxon:283643) and its parent species C. deneoformans
  (NCBITaxon:40410) intentionally omit UP:* proteome_id on LAC1 (UniProtKB:Q55P57)
  because strain B-3501A has no UP:UP... proteome cross-reference in UniProtKB 2026_02
  (whereas sibling strain JEC21 NCBITaxon:214684 has UP:UP000001247).
- 'Cryptococcus deuterogattii R265 (NCBITaxon:294750, reference proteome UP:UP000029445)
  has 0 reviewed Swiss-Prot entries for CAP59 and LAC1 in UniProtKB 2026_02; CAP59
  (UniProtKB:A0A095C6P1) and LAC1 (UniProtKB:A0A095CIC4) are reference-proteome TrEMBL
  entries with explicit review_status: TREMBL in curation/uniprot_proteins.tsv.'
notes:
- Cycle 6 Stage 3 expanded curation/uniprot_proteins.tsv from 29 to 34 live-verified
  UniProtKB accessions (32 SWISS_PROT, 2 TREMBL) and enriched 11 maintained causal-graph
  overlays from 64 to 75 GENE_OR_PROTEIN nodes and from 213 to 246 evidence-backed
  edges across all 15 causal-graph records.
tags:
- stage3-protein-examples
- cycle6-curation
- uniprot-reference-proteomes
```
