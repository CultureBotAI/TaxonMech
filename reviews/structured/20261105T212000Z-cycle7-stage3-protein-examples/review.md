# Cycle 7 Stage 3 UniProtKB protein examples curation and corpus review (626,048 records; 15 causal-graph records, 86 GENE_OR_PROTEIN nodes, 39 live-verified UniProtKB accessions, 290 evidence-backed edges)

- Review: 20261105T212000Z-cycle7-stage3-protein-examples
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-11-05T18:10:00Z
- Finished UTC: 2026-11-05T21:20:00Z
- Reviewer: Antigravity (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 626,048 in-scope TaxonRecord files across Bacteria (605,695), Archaea (14,013), Eukaryota (6,331), and other (9) against the Stage 3 UniProtKB protein-examples contract (.claude/skills/add-uniprot-protein-examples/SKILL.md). Expanded curation/uniprot_proteins.tsv from 34 to 39 live-verified UniProtKB accessions (UniProt release 2026_02), adding reviewed Swiss-Prot proteins UniProtKB:P0AA04 (PTHP_ECOLI, ptsH/b2415, NCBITaxon:83333, UP:UP000000625, 85 aa, CRC64 E5C8879C0A95AD41, v1), UniProtKB:P39764 (KINC_BACSU, kinC/BSU14490, EC:2.7.13.3, NCBITaxon:224308, UP:UP000001570, 428 aa, CRC64 18B78E68FD933297, v1), UniProtKB:P54292 (RHLR_PSEAE, rhlR/PA3477, NCBITaxon:208964, UP:UP000002438, 241 aa, CRC64 70C0AEA8C1DE0D4B, v1), UniProtKB:Q58264 (MTRH_METJA, mtrH/MJ0854, EC:7.2.1.4, NCBITaxon:243232, UP:UP000000805, 319 aa, CRC64 370E20B41F5CDA00, v2), and UniProtKB:J9VG42 (MBS1_CRYN9, MBS1/CNAG_07464, NCBITaxon:235443, UP:UP000010091, 774 aa, CRC64 86EAB6D3B95FF04A, v2). Enriched 11 maintained overlays in curation/causal_graphs/ (NCBITaxon_562, NCBITaxon_83333, NCBITaxon_511145, NCBITaxon_1423, NCBITaxon_224308, NCBITaxon_287, NCBITaxon_208964, NCBITaxon_2190, NCBITaxon_243232, NCBITaxon_5207, NCBITaxon_235443), bringing the 15 maintained overlays from 75 to 86 GENE_OR_PROTEIN nodes (84 carrying UP:* reference proteome_id; 2 on Cryptococcus deneoformans B-3501A NCBITaxon:283643 &amp; species NCBITaxon:40410 omitting proteome_id because strain B-3501A has no UP:UP... proteome cross-reference in UniProtKB 2026_02 whereas sibling strain JEC21 NCBITaxon:214684 has UP:UP000001247) and from 257 to 290 evidence-backed edges. Corpus-wide protein example attachment outside the 15 causal-graph records remains inapplicable because TaxonRecord has no top-level protein slot and the remaining 626,033 records carry causal_graphs: [].

## Scope And Provenance

Full-corpus Cycle 7 Stage 3 UniProtKB protein-example review across all 626,048 TaxonRecord files in data/taxa/, paired with live UniProt REST + NCBI PubMed verification, catalog expansion (34 -&gt; 39 UniProtKB accessions in curation/uniprot_proteins.tsv), and causal-graph overlay enrichment across 11 of the 15 causal-graph-bearing species and reference-proteome strain records (86 GENE_OR_PROTEIN nodes, 290 evidence-backed edges).

Selection: All 626,048 in-scope taxa in curation/seed_scope.tsv and data/taxa/PATHS.tsv classified by causal_graphs presence, with 100% direct inspection, live UniProtKB/PubMed verification, and validation of all 15 causal-graph-bearing species and strain records.
Coverage: sampled; 15 reviewed / 626048 in the declared population.
Source: working_tree at Git base ce681803275fa1e308df38efcd7e188a9a4813e5.
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
| Strict LinkML and custom semantic validation on all 15 causal-graph-seeded TaxonRecord files | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:5207, NCBITaxon:235443 | All 15 seeded TaxonRecord YAML files (including the 11 records updated in Cycle 7 Stage 3) pass scripts/validate_strict.py with 0 errors. |
| OAK ID-label correspondence validation across all 15 causal-graph overlays and seeded records | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:5207, NCBITaxon:235443 | scripts/validate_id_label_correspondence.py verifies 320 OK_CANONICAL GO and RO pairs (30 GO node groundings + 290 RO edge predicates; 327 OBO-grounded pairs including 7 CHEBI node groundings), 108 SKIPPED_NO_ADAPTER, and 0 MISMATCH across all grounded nodes and predicates in curation/causal_graphs/*.yaml. |
| Unit and integration test suite for causal-graph overlays, offline UniProtKB reference proteome validation, structural referential integrity, seeder merge, and HTML rendering | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:5207, NCBITaxon:235443 | tests/test_causal_graph_overlays.py passes all 12 tests covering roundtrip seeding, offline UniProtKB reference proteome/lineage/strain validation (39 proteins, 86 GENE_OR_PROTEIN nodes, 290 edges), structural validation, and HTML rendering. |

## Scientific And Domain Assessments

### Live-verified UniProtKB protein examples and reference proteome metadata across all 15 causal-graph-bearing species and strain records

grounding: supported. Targets: NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:5207, NCBITaxon:235443.

Expanded curation/uniprot_proteins.tsv from 34 to 39 live-verified UniProtKB accessions (37 SWISS_PROT, 2 TREMBL) and enriched 11 maintained causal-graph overlays across Escherichia coli (NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145; adding HPr UniProtKB:P0AA04 ptsH/b2415 alongside Crr UniProtKB:P69783, CyaA UniProtKB:P00936, CRP UniProtKB:P0ACJ8, LacZ UniProtKB:P00722, LacY UniProtKB:P02920, LacI UniProtKB:P03023, and LacA UniProtKB:P07464 on UP:UP000000625, with edges e26, e27, e28 supported by PMID:9278503, PMID:2411636, PMID:2960675, and PMID:17158705), Bacillus subtilis (NCBITaxon:1423, NCBITaxon:224308; adding KinC UniProtKB:P39764 kinC/BSU14490 alongside PhrA UniProtKB:Q00829, RapA UniProtKB:Q00828, KinA UniProtKB:P16497, KinB UniProtKB:Q08430, Spo0F UniProtKB:P06628, Spo0B UniProtKB:P06535, Spo0A UniProtKB:P06534, and Spo0E UniProtKB:P05043 on UP:UP000001570, with edges e33, e34, e35 supported by PMID:9384377, PMID:8002614, PMID:8002615, and PMID:11069677), Pseudomonas aeruginosa (NCBITaxon:287, NCBITaxon:208964; adding RhlR UniProtKB:P54292 rhlR/PA3477 alongside PqsE UniProtKB:P20581, PhzA1 UniProtKB:Q9HWH1, PhzB1 UniProtKB:O69753, PhzD1 UniProtKB:P0DPB9, PhzM UniProtKB:Q9HWH2, and PhzS UniProtKB:Q9HWG9 on UP:UP000002438, with edges e16, e17, e18 supported by PMID:10984043, PMID:8144472, PMID:8522523, PMID:35019777, PMID:36379213, PMID:36456567, PMID:27851827, and PMID:38064526), Methanocaldococcus jannaschii (NCBITaxon:2190, NCBITaxon:243232; adding MtrH UniProtKB:Q58264 mtrH/MJ0854 alongside MtrA UniProtKB:Q58261, FwdB UniProtKB:P61154, Mer UniProtKB:Q58929, McrA UniProtKB:Q58256, McrB UniProtKB:Q58252, and McrG UniProtKB:Q58255 on UP:UP000000805, with edges e20, e21, e22 supported by PMID:8688087, PMID:10338124, PMID:27342374, and PMID:38530900), and Cryptococcus neoformans (NCBITaxon:5207, NCBITaxon:235443; adding MBS1 UniProtKB:J9VG42 MBS1/CNAG_07464 alongside CUF1 UniProtKB:J9VT33, BZP4 UniProtKB:J9VQ26, LAC1 UniProtKB:J9VY90, and LAC2 UniProtKB:J9VQZ4 on UP:UP000010091, with edges e16, e17, e18 supported by PMID:24743168, PMID:22080454, PMID:25849373, and PMID:31575776), bringing all 15 overlays to 86 GENE_OR_PROTEIN nodes and 290 evidence-backed edges.

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
| curated-uniprot-catalog-and-overlays | curation/uniprot_proteins.tsv; curation/causal_graphs/NCBITaxon_*.yaml; data/taxa/{bacteria,archaea,eukaryota}/*.yaml; curation/uniprot_proteins.tsv (39 rows); curation/causal_graphs/NCBITaxon_{562,83333,511145,1423,224308,287,208964,2190,243232,1859096,294750,40410,283643,5207,235443}.yaml | supports | Thirty-nine live-verified UniProtKB accessions in curation/uniprot_proteins.tsv ground 86 GENE_OR_PROTEIN nodes (84 with UP:* proteome_id, 2 without on C. deneoformans B-3501A) and 290 evidence-backed causal edges across the 15 maintained overlays and seeded TaxonRecord YAML files. |
| oak-id-label-validation | conf/id_label_targets.yaml; scripts/validate_id_label_correspondence.py; conf/id_label_targets.yaml:18-65 | supports | All OBO-grounded node and edge pairs across GO, CHEBI, and RO in the 15 causal-graph overlays and seeded records match canonical OAK ontology labels (320 OK_CANONICAL GO/RO pairs, 7 CHEBI pairs, 108 SKIPPED_NO_ADAPTER, 0 MISMATCH). |
| seeder-and-uniprot-catalog-validation | src/taxonmech/seed.py; curation/uniprot_proteins.tsv; tests/test_causal_graph_overlays.py; src/taxonmech/seed.py:217-460,790-810; tests/test_causal_graph_overlays.py:1-225 | supports | load_uniprot_proteins(), validate_causal_graph_proteins(), and validate_causal_graph_structure() enforce exact organism lineage compatibility, UP:* reference proteome membership, review_status, gene_symbol, locus_tag, ec_number, length, sequence_crc64, sequence_version, and BacDive strain_id consistency across all 86 GENE_OR_PROTEIN nodes and 290 causal edges. |
| raw-phenotype-and-trait-inventories | data/raw/madin_taxa.tsv; data/raw/bactotraits_taxa.tsv; data/raw/mediadive_taxa.tsv; madin_taxa.tsv (34,148 rows); bactotraits_taxa.tsv (9,658 rows); mediadive_taxa.tsv (14,154 rows) | supports | Committed raw tables in data/raw/madin_taxa.tsv and data/raw/bactotraits_taxa.tsv store 2-column (taxon_id, assertion_count) summaries until an upstream kg-microbe checkout re-extraction runs extract_taxon_trait_edges(), leaving 626,033 in-scope records with causal_graphs: []. |

## Limits And Additional Notes

- 626,033 of 626,048 in-scope records carry causal_graphs: [] and have no top-level protein slot on TaxonRecord; bulk causal-graph expansion awaits upstream kg-microbe re-extraction (#78 / taxonmech-infra-0002).
- Cryptococcus deneoformans B-3501A (NCBITaxon:283643) and its parent species C. deneoformans (NCBITaxon:40410) intentionally omit UP:* proteome_id on LAC1 (UniProtKB:Q55P57) because strain B-3501A has no UP:UP... proteome cross-reference in UniProtKB 2026_02 (whereas sibling strain JEC21 NCBITaxon:214684 has UP:UP000001247).
- Cryptococcus deuterogattii R265 (NCBITaxon:294750, reference proteome UP:UP000029445) has 0 reviewed Swiss-Prot entries for CAP59 and LAC1 in UniProtKB 2026_02; CAP59 (UniProtKB:A0A095C6P1) and LAC1 (UniProtKB:A0A095CIC4) are reference-proteome TrEMBL entries with explicit review_status: TREMBL in curation/uniprot_proteins.tsv.
- Cycle 7 Stage 3 expanded curation/uniprot_proteins.tsv from 34 to 39 live-verified UniProtKB accessions (37 SWISS_PROT, 2 TREMBL) and enriched 11 maintained causal-graph overlays from 75 to 86 GENE_OR_PROTEIN nodes and from 257 to 290 evidence-backed edges across all 15 causal-graph records.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T212000Z-cycle7-stage3-protein-examples
kind: batch
repository: CultureBotAI/TaxonMech
title: Cycle 7 Stage 3 UniProtKB protein examples curation and corpus review (626,048
  records; 15 causal-graph records, 86 GENE_OR_PROTEIN nodes, 39 live-verified UniProtKB
  accessions, 290 evidence-backed edges)
started_at: '2026-11-05T18:10:00Z'
finished_at: '2026-11-05T21:20:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: independent
  independence_basis: Cycle 7 Stage 3 UniProtKB protein-example curation and audit
    worker; verified all native prerequisite gates (.claude/skills/add-uniprot-protein-examples/SKILL.md),
    live-verified 5 additional Swiss-Prot UniProtKB accessions (release 2026_02) and
    their primary PubMed citations against live UniProt REST and NCBI E-utilities,
    expanded curation/uniprot_proteins.tsv from 34 to 39 entries (37 SWISS_PROT, 2
    TREMBL), enriched 11 maintained curation/causal_graphs/*.yaml overlays to bring
    the 15 curated overlays from 75 to 86 GENE_OR_PROTEIN nodes (84 with UP:* proteome_id,
    2 without on Cryptococcus deneoformans B-3501A) and from 257 to 290 evidence-backed
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
  Expanded curation/uniprot_proteins.tsv from 34 to 39 live-verified UniProtKB accessions
  (UniProt release 2026_02), adding reviewed Swiss-Prot proteins UniProtKB:P0AA04
  (PTHP_ECOLI, ptsH/b2415, NCBITaxon:83333, UP:UP000000625, 85 aa, CRC64 E5C8879C0A95AD41,
  v1), UniProtKB:P39764 (KINC_BACSU, kinC/BSU14490, EC:2.7.13.3, NCBITaxon:224308,
  UP:UP000001570, 428 aa, CRC64 18B78E68FD933297, v1), UniProtKB:P54292 (RHLR_PSEAE,
  rhlR/PA3477, NCBITaxon:208964, UP:UP000002438, 241 aa, CRC64 70C0AEA8C1DE0D4B, v1),
  UniProtKB:Q58264 (MTRH_METJA, mtrH/MJ0854, EC:7.2.1.4, NCBITaxon:243232, UP:UP000000805,
  319 aa, CRC64 370E20B41F5CDA00, v2), and UniProtKB:J9VG42 (MBS1_CRYN9, MBS1/CNAG_07464,
  NCBITaxon:235443, UP:UP000010091, 774 aa, CRC64 86EAB6D3B95FF04A, v2). Enriched
  11 maintained overlays in curation/causal_graphs/ (NCBITaxon_562, NCBITaxon_83333,
  NCBITaxon_511145, NCBITaxon_1423, NCBITaxon_224308, NCBITaxon_287, NCBITaxon_208964,
  NCBITaxon_2190, NCBITaxon_243232, NCBITaxon_5207, NCBITaxon_235443), bringing the
  15 maintained overlays from 75 to 86 GENE_OR_PROTEIN nodes (84 carrying UP:* reference
  proteome_id; 2 on Cryptococcus deneoformans B-3501A NCBITaxon:283643 & species NCBITaxon:40410
  omitting proteome_id because strain B-3501A has no UP:UP... proteome cross-reference
  in UniProtKB 2026_02 whereas sibling strain JEC21 NCBITaxon:214684 has UP:UP000001247)
  and from 257 to 290 evidence-backed edges. Corpus-wide protein example attachment
  outside the 15 causal-graph records remains inapplicable because TaxonRecord has
  no top-level protein slot and the remaining 626,033 records carry causal_graphs:
  [].'
source:
  git_revision: ce681803275fa1e308df38efcd7e188a9a4813e5
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
    sha256: e11e92a2fd18f7789d079a1415f8516cef9c1bf7bdc4435ed7797776120c4ec3
    role: context
  - path: README.md
    sha256: 7a6fcfdfb115278603dccca5692ff9dfa2cc83a725b919f53a9dcb90a41c11e8
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
    sha256: 89cd985c85f91c60d939db8d628994be20b5a78420e18bd324799c6391499f75
    role: context
  - path: curation/causal_graphs/NCBITaxon_1859096.yaml
    sha256: 0f29a0916110b21224537ec5e337a9e8fa5a61c3a9c3f04885f421e7974d8746
    role: context
  - path: curation/causal_graphs/NCBITaxon_208964.yaml
    sha256: ed26b411e5a15bfc1fbe76f44d915697b3e690d6a9208bd74914fff3f1242c3f
    role: context
  - path: curation/causal_graphs/NCBITaxon_2190.yaml
    sha256: 9a65623b567b95a1a3e9966fc184a86d4e9b56a986ad7227152e61a7e602878e
    role: context
  - path: curation/causal_graphs/NCBITaxon_224308.yaml
    sha256: ccf929f8e8b8638c2475008baaa6a52219c35cc84e7a71de35350b5cd1e36037
    role: context
  - path: curation/causal_graphs/NCBITaxon_235443.yaml
    sha256: a11f8393a35bf832f670781697490b46b0cefdd69845c7de5b8826ede491aa74
    role: context
  - path: curation/causal_graphs/NCBITaxon_243232.yaml
    sha256: 83a58bb4a665b7c09daf6e9f52874e6164289506869b12b412136d27d74955bc
    role: context
  - path: curation/causal_graphs/NCBITaxon_283643.yaml
    sha256: 3098281e6de9a4dccdcf51f3c7a8db7f47c4c3dfadb333682957c4e331f35caf
    role: context
  - path: curation/causal_graphs/NCBITaxon_287.yaml
    sha256: 758828c37feb6af36037a01dfbdc427d026c192f133324b3240699cfa3ab638d
    role: context
  - path: curation/causal_graphs/NCBITaxon_294750.yaml
    sha256: 3ec5ba3c0784bbda20a3df13863c7faf96fb21562e01394fa0e69ec9f3f2215e
    role: context
  - path: curation/causal_graphs/NCBITaxon_40410.yaml
    sha256: 425d1eece60fd72e9c552eee49e2af7543b9b278b2555f0c0b991c537d85c3cc
    role: context
  - path: curation/causal_graphs/NCBITaxon_511145.yaml
    sha256: 818af4bef441b3827b30fcc6e8376e3b05acc1f49b90513b738daa85a35ff677
    role: context
  - path: curation/causal_graphs/NCBITaxon_5207.yaml
    sha256: 03b29827539e0b1f480c3886887b412856783d8fc6503d950a65988445bbad20
    role: context
  - path: curation/causal_graphs/NCBITaxon_562.yaml
    sha256: a0e6e85be027827ac12571aac91a87423fcd6c67dc748736f65c77e0ad58a513
    role: context
  - path: curation/causal_graphs/NCBITaxon_83333.yaml
    sha256: 612bfc84c3202aa7db71e14ea40e2cbfc305207af6efe62ab12f9e3680be57cc
    role: context
  - path: curation/causal_graphs/README.md
    sha256: e05ae1769883360b65701e961c02db0e5aac6b194fe6b156e3d791d8c08c9911
    role: context
  - path: curation/seed_scope.tsv
    sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
    role: context
  - path: curation/uniprot_proteins.tsv
    sha256: fd0731942afc031f0e9a3d04e159a4a8de752b36f9c101a5aecfb98511f2eb3f
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
    sha256: 1a662d63976cbfbe0676b3a7155901da7cfa4b8f9a45c5dacb2ed0eb9a523beb
    role: target
  - path: data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml
    sha256: bce1f92edb9b31720ee636c3cd7b506e4b661d3d312197cc5ed266e5c06dea78
    role: target
  - path: data/taxa/bacteria/bacillus_subtilis.yaml
    sha256: 89c92d353b94580499de8a97a29f6af5a3152e233ef2a1715b92326db2d1067f
    role: target
  - path: data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml
    sha256: 08a3f3ca1220a268c50cd770806cf7d2d066cef453884cdeb8c18813076e6371
    role: target
  - path: data/taxa/bacteria/escherichia_coli.yaml
    sha256: c84dca488c607760f3e28997a78cc096f178b42e804990f0cb833ef155dda4b7
    role: target
  - path: data/taxa/bacteria/escherichia_coli_k_12.yaml
    sha256: 3195d65694ec3b8ec397203edb235da95b93ce31cecdf5c23979d38e70ed3f2d
    role: target
  - path: data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml
    sha256: 35c40233f7aa484ea2009e60f8b99a1d35953b9ace05f69d666b842c890e2bc6
    role: target
  - path: data/taxa/bacteria/pseudomonas_aeruginosa.yaml
    sha256: bdde8e345d0f00a32c4b29d02d31742a0756c77932d86dc87bbc3bf275c1309e
    role: target
  - path: data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml
    sha256: 62e616e696d69b577dbc149a42f16af53771e406168bc3b1c6fc1d536714e4bb
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
    sha256: 10c405c1d065926a63dc043faa33542ac88d34984cfd1cc80ce65537d1ea7ea5
    role: target
  - path: data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml
    sha256: 90ee98cfc705a9dc3b265ccf8cbd46d840a88f00c8fe1b7d7652482c5f892a0c
    role: target
  - path: scripts/check_provenance.py
    sha256: d9f9139ee475da3fd7bd9da4af3b7d02f74e5ffc98bae375d35625b40bade965
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
    sha256: 72319123f9533c9076de6b207c629757aa502cfd1c04b172965a5739abea676f
    role: context
  - path: src/taxonmech/templates/taxon-content.html
    sha256: 9562204e103755b648b32234cf001253e855a64bb46f5de1eb372b5fcf7ad3a2
    role: context
  - path: tests/test_causal_graph_overlays.py
    sha256: 977d75c0d4da22b4223077dd553d8d92f58c7edb93539e368d178298573389c1
    role: context
scope:
  description: Full-corpus Cycle 7 Stage 3 UniProtKB protein-example review across
    all 626,048 TaxonRecord files in data/taxa/, paired with live UniProt REST + NCBI
    PubMed verification, catalog expansion (34 -> 39 UniProtKB accessions in curation/uniprot_proteins.tsv),
    and causal-graph overlay enrichment across 11 of the 15 causal-graph-bearing species
    and reference-proteome strain records (86 GENE_OR_PROTEIN nodes, 290 evidence-backed
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
    of all 15 causal-graph records and their 86 GENE_OR_PROTEIN nodes across 39 unique
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
    in Cycle 7 Stage 3) pass scripts/validate_strict.py with 0 errors.
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
  summary: scripts/validate_id_label_correspondence.py verifies 320 OK_CANONICAL GO
    and RO pairs (30 GO node groundings + 290 RO edge predicates; 327 OBO-grounded
    pairs including 7 CHEBI node groundings), 108 SKIPPED_NO_ADAPTER, and 0 MISMATCH
    across all grounded nodes and predicates in curation/causal_graphs/*.yaml.
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
  summary: tests/test_causal_graph_overlays.py passes all 12 tests covering roundtrip
    seeding, offline UniProtKB reference proteome/lineage/strain validation (39 proteins,
    86 GENE_OR_PROTEIN nodes, 290 edges), structural validation, and HTML rendering.
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
  locator: curation/uniprot_proteins.tsv (39 rows); curation/causal_graphs/NCBITaxon_{562,83333,511145,1423,224308,287,208964,2190,243232,1859096,294750,40410,283643,5207,235443}.yaml
  accessed_at: '2026-11-05T21:20:00Z'
  support: supports
  summary: Thirty-nine live-verified UniProtKB accessions in curation/uniprot_proteins.tsv
    ground 86 GENE_OR_PROTEIN nodes (84 with UP:* proteome_id, 2 without on C. deneoformans
    B-3501A) and 290 evidence-backed causal edges across the 15 maintained overlays
    and seeded TaxonRecord YAML files.
  snapshot_sha256: fd0731942afc031f0e9a3d04e159a4a8de752b36f9c101a5aecfb98511f2eb3f
- evidence_id: oak-id-label-validation
  kind: validation
  reference: conf/id_label_targets.yaml; scripts/validate_id_label_correspondence.py
  locator: conf/id_label_targets.yaml:18-65
  accessed_at: '2026-11-05T21:20:00Z'
  support: supports
  summary: All OBO-grounded node and edge pairs across GO, CHEBI, and RO in the 15
    causal-graph overlays and seeded records match canonical OAK ontology labels (320
    OK_CANONICAL GO/RO pairs, 7 CHEBI pairs, 108 SKIPPED_NO_ADAPTER, 0 MISMATCH).
  snapshot_sha256: efed4c6d9cc218c9d89ba4468e361761ac02ff535e2669de33af6606202e544c
- evidence_id: seeder-and-uniprot-catalog-validation
  kind: validation
  reference: src/taxonmech/seed.py; curation/uniprot_proteins.tsv; tests/test_causal_graph_overlays.py
  locator: src/taxonmech/seed.py:217-460,790-810; tests/test_causal_graph_overlays.py:1-225
  accessed_at: '2026-11-05T21:20:00Z'
  support: supports
  summary: load_uniprot_proteins(), validate_causal_graph_proteins(), and validate_causal_graph_structure()
    enforce exact organism lineage compatibility, UP:* reference proteome membership,
    review_status, gene_symbol, locus_tag, ec_number, length, sequence_crc64, sequence_version,
    and BacDive strain_id consistency across all 86 GENE_OR_PROTEIN nodes and 290
    causal edges.
  snapshot_sha256: 72319123f9533c9076de6b207c629757aa502cfd1c04b172965a5739abea676f
- evidence_id: raw-phenotype-and-trait-inventories
  kind: database
  reference: data/raw/madin_taxa.tsv; data/raw/bactotraits_taxa.tsv; data/raw/mediadive_taxa.tsv
  locator: madin_taxa.tsv (34,148 rows); bactotraits_taxa.tsv (9,658 rows); mediadive_taxa.tsv
    (14,154 rows)
  accessed_at: '2026-11-05T21:20:00Z'
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
  summary: Expanded curation/uniprot_proteins.tsv from 34 to 39 live-verified UniProtKB
    accessions (37 SWISS_PROT, 2 TREMBL) and enriched 11 maintained causal-graph overlays
    across Escherichia coli (NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145; adding
    HPr UniProtKB:P0AA04 ptsH/b2415 alongside Crr UniProtKB:P69783, CyaA UniProtKB:P00936,
    CRP UniProtKB:P0ACJ8, LacZ UniProtKB:P00722, LacY UniProtKB:P02920, LacI UniProtKB:P03023,
    and LacA UniProtKB:P07464 on UP:UP000000625, with edges e26, e27, e28 supported
    by PMID:9278503, PMID:2411636, PMID:2960675, and PMID:17158705), Bacillus subtilis
    (NCBITaxon:1423, NCBITaxon:224308; adding KinC UniProtKB:P39764 kinC/BSU14490
    alongside PhrA UniProtKB:Q00829, RapA UniProtKB:Q00828, KinA UniProtKB:P16497,
    KinB UniProtKB:Q08430, Spo0F UniProtKB:P06628, Spo0B UniProtKB:P06535, Spo0A UniProtKB:P06534,
    and Spo0E UniProtKB:P05043 on UP:UP000001570, with edges e33, e34, e35 supported
    by PMID:9384377, PMID:8002614, PMID:8002615, and PMID:11069677), Pseudomonas aeruginosa
    (NCBITaxon:287, NCBITaxon:208964; adding RhlR UniProtKB:P54292 rhlR/PA3477 alongside
    PqsE UniProtKB:P20581, PhzA1 UniProtKB:Q9HWH1, PhzB1 UniProtKB:O69753, PhzD1 UniProtKB:P0DPB9,
    PhzM UniProtKB:Q9HWH2, and PhzS UniProtKB:Q9HWG9 on UP:UP000002438, with edges
    e16, e17, e18 supported by PMID:10984043, PMID:8144472, PMID:8522523, PMID:35019777,
    PMID:36379213, PMID:36456567, PMID:27851827, and PMID:38064526), Methanocaldococcus
    jannaschii (NCBITaxon:2190, NCBITaxon:243232; adding MtrH UniProtKB:Q58264 mtrH/MJ0854
    alongside MtrA UniProtKB:Q58261, FwdB UniProtKB:P61154, Mer UniProtKB:Q58929,
    McrA UniProtKB:Q58256, McrB UniProtKB:Q58252, and McrG UniProtKB:Q58255 on UP:UP000000805,
    with edges e20, e21, e22 supported by PMID:8688087, PMID:10338124, PMID:27342374,
    and PMID:38530900), and Cryptococcus neoformans (NCBITaxon:5207, NCBITaxon:235443;
    adding MBS1 UniProtKB:J9VG42 MBS1/CNAG_07464 alongside CUF1 UniProtKB:J9VT33,
    BZP4 UniProtKB:J9VQ26, LAC1 UniProtKB:J9VY90, and LAC2 UniProtKB:J9VQZ4 on UP:UP000010091,
    with edges e16, e17, e18 supported by PMID:24743168, PMID:22080454, PMID:25849373,
    and PMID:31575776), bringing all 15 overlays to 86 GENE_OR_PROTEIN nodes and 290
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
    value: 39.0
    unit: accessions
    definition: Unique live-verified UniProtKB accessions in curation/uniprot_proteins.tsv.
    minimum: 0.0
  - name: causal_graph_gene_or_protein_nodes
    value: 86.0
    unit: nodes
    definition: Total GENE_OR_PROTEIN CausalNode instances across the 15 seeded records.
    minimum: 0.0
  - name: evidence_backed_causal_edges
    value: 290.0
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
- Cycle 7 Stage 3 expanded curation/uniprot_proteins.tsv from 34 to 39 live-verified
  UniProtKB accessions (37 SWISS_PROT, 2 TREMBL) and enriched 11 maintained causal-graph
  overlays from 75 to 86 GENE_OR_PROTEIN nodes and from 257 to 290 evidence-backed
  edges across all 15 causal-graph records.
tags:
- stage3-protein-examples
- cycle7-curation
- uniprot-reference-proteomes
```
