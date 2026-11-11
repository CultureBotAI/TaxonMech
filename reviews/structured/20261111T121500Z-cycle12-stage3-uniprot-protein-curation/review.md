# Cycle 12 Stage 3 UniProtKB protein example curation across 15 maintained causal-graph overlays and 626,048 corpus records

- Review: 20261111T121500Z-cycle12-stage3-uniprot-protein-curation
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-11-11T12:00:00Z
- Finished UTC: 2026-11-11T12:15:00Z
- Reviewer: Antigravity (Cycle 12 Stage 3 add-uniprot-protein-examples) (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Audited all 626,048 in-scope TaxonMech records and the 15 maintained causal-graph overlays for Cycle 12 Stage 3 (protein_examples). Added 5 live-verified reviewed Swiss-Prot proteins across all 5 reference-proteome cohorts in curation/uniprot_proteins.tsv (59 -&gt; 64 rows: 62 SWISS_PROT, 2 TREMBL; UniProt release 2026_02) and 11 reference-proteome overlays (130 -&gt; 141 GENE_OR_PROTEIN nodes, 139 with UP:* proteome_id; 485 -&gt; 518 evidence-backed causal edges): UniProtKB:P0A6T3 (GAL1_ECOLI, galK / b0757, EC:2.7.1.6, 382 aa, 7D886CE6FC48F0A1, v2) on NCBITaxon:562, NCBITaxon:83333, and NCBITaxon:511145; UniProtKB:P08874 (ABRB_BACSU, abrB / BSU00370, 96 aa, 6A964557F5590CFE, v1) on NCBITaxon:1423 and NCBITaxon:224308; UniProtKB:Q9I4X3 (PQSA_PSEAE, pqsA / PA0996, EC:6.2.1.32, 517 aa, 8718FDEC315351F5, v1) on NCBITaxon:287 and NCBITaxon:208964; UniProtKB:Q58257 (MTRE_METJA, mtrE / MJ0847, EC:7.2.1.4, 303 aa, 46BA1BBD80FECCE2, v1) on NCBITaxon:2190 and NCBITaxon:243232; and UniProtKB:J9VX63 (US101_CRYN9, USV101 / CNAG_05420, 647 aa, F87495E33D9AEE07, v1) on NCBITaxon:5207 and NCBITaxon:235443. Documented inapplicability for the 626,033 records without causal_graphs and upstream proteome/review blockers on the 4 remaining Cryptococcus overlays (#78 / taxonmech-infra-0003).

## Scope And Provenance

Full assessment of curation/uniprot_proteins.tsv and all 15 maintained causal-graph overlays (11 updated reference-proteome overlays and 4 upstream-proteome/review-bounded Cryptococcus overlays), with explicit exclusion of the 626,033 seed-only records that lack causal_graphs.

Selection: All 15 maintained causal-graph taxon records plus curation/uniprot_proteins.tsv out of 626,048 corpus records.
Coverage: partial; 16 reviewed / 626049 in the declared population.
Source: working_tree at Git base c6d58b131109c50b231d10fb14687467504a96ac.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| uniprot_proteins_catalog | curation/uniprot_proteins.tsv | maintained | Pinned UniProtKB reference protein catalog (64 accessions across 7 microbial organism taxa) |
| NCBITaxon_562 | data/taxa/bacteria/escherichia_coli.yaml | generated | Escherichia coli (NCBITaxon:562) |
| NCBITaxon_83333 | data/taxa/bacteria/escherichia_coli_k_12.yaml | generated | Escherichia coli K-12 (NCBITaxon:83333) |
| NCBITaxon_511145 | data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml | generated | Escherichia coli str. K-12 substr. MG1655 (NCBITaxon:511145) |
| NCBITaxon_1423 | data/taxa/bacteria/bacillus_subtilis.yaml | generated | Bacillus subtilis (NCBITaxon:1423) |
| NCBITaxon_224308 | data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml | generated | Bacillus subtilis subsp. subtilis str. 168 (NCBITaxon:224308) |
| NCBITaxon_287 | data/taxa/bacteria/pseudomonas_aeruginosa.yaml | generated | Pseudomonas aeruginosa (NCBITaxon:287) |
| NCBITaxon_208964 | data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml | generated | Pseudomonas aeruginosa PAO1 (NCBITaxon:208964) |
| NCBITaxon_2190 | data/taxa/archaea/methanocaldococcus_jannaschii.yaml | generated | Methanocaldococcus jannaschii (NCBITaxon:2190) |
| NCBITaxon_243232 | data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml | generated | Methanocaldococcus jannaschii DSM 2661 (NCBITaxon:243232) |
| NCBITaxon_5207 | data/taxa/eukaryota/cryptococcus_neoformans.yaml | generated | Cryptococcus neoformans (NCBITaxon:5207) |
| NCBITaxon_235443 | data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml | generated | Cryptococcus neoformans H99 (NCBITaxon:235443) |
| NCBITaxon_40410 | data/taxa/eukaryota/cryptococcus_deneoformans.yaml | generated | Cryptococcus deneoformans (NCBITaxon:40410) |
| NCBITaxon_283643 | data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml | generated | Cryptococcus deneoformans B-3501A (NCBITaxon:283643) |
| NCBITaxon_1859096 | data/taxa/eukaryota/cryptococcus_deuterogattii.yaml | generated | Cryptococcus deuterogattii (NCBITaxon:1859096) |
| NCBITaxon_294750 | data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml | generated | Cryptococcus deuterogattii R265 (NCBITaxon:294750) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Causal-graph and UniProtKB catalog provenance gate | passed | True | uniprot_proteins_catalog, NCBITaxon_562, NCBITaxon_83333, NCBITaxon_511145, NCBITaxon_1423, NCBITaxon_224308, NCBITaxon_287, NCBITaxon_208964, NCBITaxon_2190, NCBITaxon_243232, NCBITaxon_5207, NCBITaxon_235443, NCBITaxon_40410, NCBITaxon_283643, NCBITaxon_1859096, NCBITaxon_294750 | scripts/check_provenance.py verified all 16 raw inventories, ATB/StrainInfo snapshots, 64 uniprot_proteins.tsv rows, and 15 causal-graph overlays with 0 problems. |
| Causal-graph and UniProtKB unit and integration test suite | passed | True | uniprot_proteins_catalog, NCBITaxon_562, NCBITaxon_83333, NCBITaxon_511145, NCBITaxon_1423, NCBITaxon_224308, NCBITaxon_287, NCBITaxon_208964, NCBITaxon_2190, NCBITaxon_243232, NCBITaxon_5207, NCBITaxon_235443, NCBITaxon_40410, NCBITaxon_283643, NCBITaxon_1859096, NCBITaxon_294750 | All 20 tests in tests/test_causal_graph_overlays.py passed across 64 UniProtKB rows, 141 GENE_OR_PROTEIN nodes, and 518 edges. |
| Closed-schema LinkML validation of all 15 causal-graph TaxonRecord files | passed | True | NCBITaxon_562, NCBITaxon_83333, NCBITaxon_511145, NCBITaxon_1423, NCBITaxon_224308, NCBITaxon_287, NCBITaxon_208964, NCBITaxon_2190, NCBITaxon_243232, NCBITaxon_5207, NCBITaxon_235443, NCBITaxon_40410, NCBITaxon_283643, NCBITaxon_1859096, NCBITaxon_294750 | scripts/validate_strict.py validated all 15 causal-graph TaxonRecord YAML files with 0 errors. |

## Scientific And Domain Assessments

### Live-verified Swiss-Prot protein curation across the 11 reference-proteome causal-graph overlays

grounding: supported. Targets: uniprot_proteins_catalog, NCBITaxon_562, NCBITaxon_83333, NCBITaxon_511145, NCBITaxon_1423, NCBITaxon_224308, NCBITaxon_287, NCBITaxon_208964, NCBITaxon_2190, NCBITaxon_243232, NCBITaxon_5207, NCBITaxon_235443.

Added 5 live-verified Swiss-Prot proteins (UniProtKB:P0A6T3, UniProtKB:P08874, UniProtKB:Q9I4X3, UniProtKB:Q58257, UniProtKB:J9VX63) to curation/uniprot_proteins.tsv (64 total rows) and 11 GENE_OR_PROTEIN nodes + 33 evidence-backed edges across the 11 reference-proteome overlays (141 total GENE_OR_PROTEIN nodes, 518 total edges).

### Upstream UniProt proteome and Swiss-Prot review limits on C. deneoformans B-3501A and C. deuterogattii R265

completeness: supported. Targets: NCBITaxon_40410, NCBITaxon_283643, NCBITaxon_1859096, NCBITaxon_294750.

Verified that the 4 remaining Cryptococcus overlays (NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750) preserve their existing verified UniProtKB protein nodes (UniProtKB:Q55P57, UniProtKB:Q56R42, UniProtKB:A0A095C6P1, UniProtKB:A0A095CIC4) and documented their upstream UniProtKB proteome/Swiss-Prot coverage bounds.

## Findings

### f_cryptococcus_proteome_and_trembl_limits: 626,033 seed-only records lack causal_graphs and 4 Cryptococcus overlays face upstream UniProt proteome/Swiss-Prot bounds

informational / deferred / confirmed; issue key: taxonmech-uniprot-cryptococcus-proteome-and-corpus-scope-limits.

In TaxonMech, UniProtKB protein groundings live on CausalNode entries (node_type: GENE_OR_PROTEIN) inside curation/causal_graphs/*.yaml overlays validated against curation/uniprot_proteins.tsv. (1) 626,033 of 626,048 in-scope records have no causal_graphs overlay and cannot carry protein groundings without new causal-graph overlays or a top-level protein exemplar slot. (2) C. deneoformans B-3501A (NCBITaxon:283643, host of NCBITaxon:40410 / NCBITaxon:283643) lacks an active UniProt reference proteome (UP:*), and C. deuterogattii R265 (NCBITaxon:294750, UP:UP000029445, host of NCBITaxon:1859096 / NCBITaxon:294750) has zero reviewed Swiss-Prot entries in UniProt 2026_02.

Disposition: Tracked under open issue #78 and INFRA_TASKS.md task taxonmech-infra-0003; existing verified protein nodes remain intact and validated.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_uniprot_api | https://rest.uniprot.org/uniprotkb/{P0A6T3,P08874,Q9I4X3,Q58257,J9VX63}.json; UniProtKB release 2026_02 REST API JSON payloads | supports | Verified canonical accessions, entry names, SWISS_PROT review status, organism_taxon_id, proteome_id (UP:UP000000625, UP:UP000001570, UP:UP000002438, UP:UP000000805, UP:UP000010091), gene_symbol, locus_tag, EC numbers, sequence_length, sequence_crc64, and sequence_version for UniProtKB:P0A6T3 (GAL1_ECOLI), UniProtKB:P08874 (ABRB_BACSU), UniProtKB:Q9I4X3 (PQSA_PSEAE), UniProtKB:Q58257 (MTRE_METJA), and UniProtKB:J9VX63 (US101_CRYN9). |
| ev_primary_literature | PMID:3158881; PMID:1327124; PMID:16524589; PMID:7966338; PMID:2513264; PMID:3096956; PMID:1901914; PMID:12142479; PMID:15066899; PMID:22325716; PMID:9603883; PMID:27668432; PMID:24743168; Europe PMC / PubMed indexed primary experimental and genome literature | supports | Primary literature supporting E. coli GalK galactokinase expression, CRP gal P1 activation, and Leloir galactose phosphorylation (PMID:9278503, PMID:3158881, PMID:16738553, PMID:1327124, PMID:16524589, PMID:7966338); B. subtilis AbrB transition-state repression by Spo0A~P and repression of spo0E/sigH (PMID:9384377, PMID:2513264, PMID:3096956, PMID:3121588, PMID:1901914, PMID:2113474); P. aeruginosa PqsA anthranilate-CoA ligase activation by MvfR/PqsR and PQS signaling to PhzM pyocyanin biosynthesis (PMID:10984043, PMID:12142479, PMID:15066899, PMID:18331462, PMID:16336047, PMID:22325716); M. jannaschii MtrE tetrahydromethanopterin S-methyltransferase subunit E complex formation with MtrA and coupling to McrA methanogenesis (PMID:8688087, PMID:9603883); and C. neoformans H99 Usv101 (CNAG_05420) C2H2 zinc-finger regulation of Rim101/CAP59 polysaccharide capsule assembly (PMID:24743168, PMID:27668432). |
| ev_provenance_gate | scripts/check_provenance.py; causal_graph_provenance_problems() | supports | Offline provenance gate verified 0 errors across 64 UniProtKB rows, 141 GENE_OR_PROTEIN nodes, and 518 causal edges. |
| ev_pytest_overlays | tests/test_causal_graph_overlays.py; 20 test functions in tests/test_causal_graph_overlays.py | supports | 20 passed in tests/test_causal_graph_overlays.py verifying catalog invariants, lineage/strain binding, and HTML rendering. |
| ev_validate_strict | scripts/validate_strict.py; LinkML closed-schema validation of 15 TaxonRecord YAML files | supports | All 15 causal-graph TaxonRecord YAML files passed LinkML closed-schema validation with 0 failures. |

## Limits And Additional Notes

- 626,033 of 626,048 in-scope TaxonMech records do not yet have curation/causal_graphs/*.yaml overlays and therefore cannot carry GENE_OR_PROTEIN nodes without upstream causal-graph curation (#78 / taxonmech-infra-0001 / taxonmech-infra-0003).
- Cryptococcus deneoformans B-3501A (NCBITaxon:283643) has no active UniProt reference proteome (UP:*), and Cryptococcus deuterogattii R265 (NCBITaxon:294750, UP:UP000029445) has 0 reviewed Swiss-Prot entries in UniProt release 2026_02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261111T121500Z-cycle12-stage3-uniprot-protein-curation
kind: batch
repository: CultureBotAI/TaxonMech
title: Cycle 12 Stage 3 UniProtKB protein example curation across 15 maintained causal-graph
  overlays and 626,048 corpus records
started_at: '2026-11-11T12:00:00Z'
finished_at: '2026-11-11T12:15:00Z'
reviewer:
  identity: Antigravity (Cycle 12 Stage 3 add-uniprot-protein-examples)
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Curation-stage self-verification of Cycle 12 Stage 3 UniProtKB
    protein additions prior to independent adversarial PR review.
skill: add-uniprot-protein-examples
completion: completed
verdict: pass_with_limitations
native_verdict: 64_uniprot_proteins_141_nodes_518_edges_verified_with_documented_scope_limits
scientific_review: true
summary: 'Audited all 626,048 in-scope TaxonMech records and the 15 maintained causal-graph
  overlays for Cycle 12 Stage 3 (protein_examples). Added 5 live-verified reviewed
  Swiss-Prot proteins across all 5 reference-proteome cohorts in curation/uniprot_proteins.tsv
  (59 -> 64 rows: 62 SWISS_PROT, 2 TREMBL; UniProt release 2026_02) and 11 reference-proteome
  overlays (130 -> 141 GENE_OR_PROTEIN nodes, 139 with UP:* proteome_id; 485 -> 518
  evidence-backed causal edges): UniProtKB:P0A6T3 (GAL1_ECOLI, galK / b0757, EC:2.7.1.6,
  382 aa, 7D886CE6FC48F0A1, v2) on NCBITaxon:562, NCBITaxon:83333, and NCBITaxon:511145;
  UniProtKB:P08874 (ABRB_BACSU, abrB / BSU00370, 96 aa, 6A964557F5590CFE, v1) on NCBITaxon:1423
  and NCBITaxon:224308; UniProtKB:Q9I4X3 (PQSA_PSEAE, pqsA / PA0996, EC:6.2.1.32,
  517 aa, 8718FDEC315351F5, v1) on NCBITaxon:287 and NCBITaxon:208964; UniProtKB:Q58257
  (MTRE_METJA, mtrE / MJ0847, EC:7.2.1.4, 303 aa, 46BA1BBD80FECCE2, v1) on NCBITaxon:2190
  and NCBITaxon:243232; and UniProtKB:J9VX63 (US101_CRYN9, USV101 / CNAG_05420, 647
  aa, F87495E33D9AEE07, v1) on NCBITaxon:5207 and NCBITaxon:235443. Documented inapplicability
  for the 626,033 records without causal_graphs and upstream proteome/review blockers
  on the 4 remaining Cryptococcus overlays (#78 / taxonmech-infra-0003).'
source:
  git_revision: c6d58b131109c50b231d10fb14687467504a96ac
  state: working_tree
  inputs:
  - path: curation/uniprot_proteins.tsv
    sha256: 9d5d16a068ff410a5e7f5f598614aef3728bd16ac33bbbd32402bb7334688248
    role: maintained_uniprot_protein_catalog
  - path: curation/seed_scope.tsv
    sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
    role: seed_scope
  - path: src/taxonmech/schema/taxonmech.yaml
    sha256: 60747327658d0e2560ac9e58fb6e9a19cf711266300f1eff8b5c64e2917020ad
    role: schema
  - path: curation/causal_graphs/NCBITaxon_562.yaml
    sha256: a7faa8642a83b3a1747ce68a0221245f01e08fc49c1a1a83e6f8fdd38c936ba9
    role: causal_graph_overlay
  - path: data/taxa/bacteria/escherichia_coli.yaml
    sha256: a05ad9777729258374684d392aa8c82c8acd4cc8f5e9d0782e0944c0d83df435
    role: generated_taxon_record
  - path: curation/causal_graphs/NCBITaxon_83333.yaml
    sha256: 89efd811ca0ade11126696bbc7558129098b47d3c4cb454066f545c44b42d87f
    role: causal_graph_overlay
  - path: data/taxa/bacteria/escherichia_coli_k_12.yaml
    sha256: d18e823be5f1107219c8b69018517972ebbee0adf066e100cd01eabf0dfa3428
    role: generated_taxon_record
  - path: curation/causal_graphs/NCBITaxon_511145.yaml
    sha256: 930b7d28a2c3c1afa5e9cbfa876de24e7cc18c5df84f6b83bb93e50a0573c8ba
    role: causal_graph_overlay
  - path: data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml
    sha256: 476768d084ffadd4e0d1dc3fc4c40605d27c3b08ba0eb05e7fb7b8460f584f7b
    role: generated_taxon_record
  - path: curation/causal_graphs/NCBITaxon_1423.yaml
    sha256: e6f90d38bef5b6854ebf72c0e3de61a26f08034b0d8f54b8526a9f45d1b97afd
    role: causal_graph_overlay
  - path: data/taxa/bacteria/bacillus_subtilis.yaml
    sha256: c18a94f3f985be593e7996361963113de427f9aa452be06836045ade160858c5
    role: generated_taxon_record
  - path: curation/causal_graphs/NCBITaxon_224308.yaml
    sha256: 8beb95f12ef1126ce8273f8b76c3739725eb25752171760b0db2247797ecd306
    role: causal_graph_overlay
  - path: data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml
    sha256: 03fe311caf2b5ba40ec9e0dfa267e99f594621fb6977b2dae4beb0a4e2f8215a
    role: generated_taxon_record
  - path: curation/causal_graphs/NCBITaxon_287.yaml
    sha256: eed942b2904f699e103507ae4f632fb62b8e1b3da2c7d6b3a7722d54138c67e7
    role: causal_graph_overlay
  - path: data/taxa/bacteria/pseudomonas_aeruginosa.yaml
    sha256: 0e957c8b22ef46ddc68f9d68090a74030961e6c088ecab7be83cf8200346a4c1
    role: generated_taxon_record
  - path: curation/causal_graphs/NCBITaxon_208964.yaml
    sha256: 31465adb30b4a92afa0d135f4422533e97275fbe7728ef514f44958574e28ec7
    role: causal_graph_overlay
  - path: data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml
    sha256: 653117b4e2cf65bb33f8eae86b62fe751d1f23f269a513333d3be8dcebf9124a
    role: generated_taxon_record
  - path: curation/causal_graphs/NCBITaxon_2190.yaml
    sha256: 2e29a9a765c3a135c206af38d8629d266236633d291f98f69501dfc9d660d7a5
    role: causal_graph_overlay
  - path: data/taxa/archaea/methanocaldococcus_jannaschii.yaml
    sha256: 86c66fe58f0c5d7505c3286c13e7fc5c1b21af40cbf0a1f7c722642aa6728149
    role: generated_taxon_record
  - path: curation/causal_graphs/NCBITaxon_243232.yaml
    sha256: 4d220c3e6dead77114983b1d8c1d8dc1a361a05eefdea9f9f113d012a93c909d
    role: causal_graph_overlay
  - path: data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml
    sha256: df8dbfe5d80d6bd59745915fe3e11ed8522c525028047e9d26562d43dcbabda4
    role: generated_taxon_record
  - path: curation/causal_graphs/NCBITaxon_5207.yaml
    sha256: 2bf92216212a4809f668fac7af14d8ca20e79d88f31fe0598b8df76e1b5a38b2
    role: causal_graph_overlay
  - path: data/taxa/eukaryota/cryptococcus_neoformans.yaml
    sha256: aa39d31f6c99383160190706b492b75611291fd08c5aa1e5376986cc4b802767
    role: generated_taxon_record
  - path: curation/causal_graphs/NCBITaxon_235443.yaml
    sha256: e6c1cb13e35b3a78576a6679289dc09ef9e2fa0af153dd98123c9e034e1128c4
    role: causal_graph_overlay
  - path: data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml
    sha256: 0c8601083669700ac81d724d4935bdb5a0114690fa88c05e74da5c5167e648ba
    role: generated_taxon_record
  - path: curation/causal_graphs/NCBITaxon_40410.yaml
    sha256: 425d1eece60fd72e9c552eee49e2af7543b9b278b2555f0c0b991c537d85c3cc
    role: causal_graph_overlay
  - path: data/taxa/eukaryota/cryptococcus_deneoformans.yaml
    sha256: 90ed37316d8ea747fdcf3ee3c208e7f34cfa96b9d9a504b5ff6f346fe21fefa5
    role: generated_taxon_record
  - path: curation/causal_graphs/NCBITaxon_283643.yaml
    sha256: 3098281e6de9a4dccdcf51f3c7a8db7f47c4c3dfadb333682957c4e331f35caf
    role: causal_graph_overlay
  - path: data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml
    sha256: 28846cf07c1deb3acf5a63cf5470004db24b7eaf227dabb959aa7a24c12a68ce
    role: generated_taxon_record
  - path: curation/causal_graphs/NCBITaxon_1859096.yaml
    sha256: 0f29a0916110b21224537ec5e337a9e8fa5a61c3a9c3f04885f421e7974d8746
    role: causal_graph_overlay
  - path: data/taxa/eukaryota/cryptococcus_deuterogattii.yaml
    sha256: 361df09d787a4889a5a8753f90adf661283f8f555fba9547d4ece43aa4cd8f24
    role: generated_taxon_record
  - path: curation/causal_graphs/NCBITaxon_294750.yaml
    sha256: 3ec5ba3c0784bbda20a3df13863c7faf96fb21562e01394fa0e69ec9f3f2215e
    role: causal_graph_overlay
  - path: data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml
    sha256: c0a7978eae1b0f1abeba6c77112ecbb1831baecafe2ef3cd95f1c7e09c35a955
    role: generated_taxon_record
scope:
  description: Full assessment of curation/uniprot_proteins.tsv and all 15 maintained
    causal-graph overlays (11 updated reference-proteome overlays and 4 upstream-proteome/review-bounded
    Cryptococcus overlays), with explicit exclusion of the 626,033 seed-only records
    that lack causal_graphs.
  selection: All 15 maintained causal-graph taxon records plus curation/uniprot_proteins.tsv
    out of 626,048 corpus records.
  coverage: partial
  population_size: 626049
  reviewed_target_ids:
  - uniprot_proteins_catalog
  - NCBITaxon_562
  - NCBITaxon_83333
  - NCBITaxon_511145
  - NCBITaxon_1423
  - NCBITaxon_224308
  - NCBITaxon_287
  - NCBITaxon_208964
  - NCBITaxon_2190
  - NCBITaxon_243232
  - NCBITaxon_5207
  - NCBITaxon_235443
  - NCBITaxon_40410
  - NCBITaxon_283643
  - NCBITaxon_1859096
  - NCBITaxon_294750
  exclusions:
  - target: data/taxa/{archaea,bacteria,eukaryota,other}/*.yaml (626,033 records without
      curation/causal_graphs/*.yaml overlays)
    reason: Inapplicable for GENE_OR_PROTEIN causal-graph node curation until evidence-backed
      curation/causal_graphs/<NCBITaxon_ID>.yaml overlays or top-level TaxonRecord
      protein exemplar slots exist (#78 / taxonmech-infra-0001 / taxonmech-infra-0003).
targets:
- target_id: uniprot_proteins_catalog
  path: curation/uniprot_proteins.tsv
  label: Pinned UniProtKB reference protein catalog (64 accessions across 7 microbial
    organism taxa)
  record_class: UniProtProteinCatalog
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: maintained_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: validator_and_seeder
- target_id: NCBITaxon_562
  path: data/taxa/bacteria/escherichia_coli.yaml
  label: Escherichia coli (NCBITaxon:562)
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_562.yaml
    role: causal_graph_overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: seeder
- target_id: NCBITaxon_83333
  path: data/taxa/bacteria/escherichia_coli_k_12.yaml
  label: Escherichia coli K-12 (NCBITaxon:83333)
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_83333.yaml
    role: causal_graph_overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: seeder
- target_id: NCBITaxon_511145
  path: data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml
  label: Escherichia coli str. K-12 substr. MG1655 (NCBITaxon:511145)
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_511145.yaml
    role: causal_graph_overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: seeder
- target_id: NCBITaxon_1423
  path: data/taxa/bacteria/bacillus_subtilis.yaml
  label: Bacillus subtilis (NCBITaxon:1423)
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_1423.yaml
    role: causal_graph_overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: seeder
- target_id: NCBITaxon_224308
  path: data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml
  label: Bacillus subtilis subsp. subtilis str. 168 (NCBITaxon:224308)
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_224308.yaml
    role: causal_graph_overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: seeder
- target_id: NCBITaxon_287
  path: data/taxa/bacteria/pseudomonas_aeruginosa.yaml
  label: Pseudomonas aeruginosa (NCBITaxon:287)
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_287.yaml
    role: causal_graph_overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: seeder
- target_id: NCBITaxon_208964
  path: data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml
  label: Pseudomonas aeruginosa PAO1 (NCBITaxon:208964)
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_208964.yaml
    role: causal_graph_overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: seeder
- target_id: NCBITaxon_2190
  path: data/taxa/archaea/methanocaldococcus_jannaschii.yaml
  label: Methanocaldococcus jannaschii (NCBITaxon:2190)
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_2190.yaml
    role: causal_graph_overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: seeder
- target_id: NCBITaxon_243232
  path: data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml
  label: Methanocaldococcus jannaschii DSM 2661 (NCBITaxon:243232)
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_243232.yaml
    role: causal_graph_overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: seeder
- target_id: NCBITaxon_5207
  path: data/taxa/eukaryota/cryptococcus_neoformans.yaml
  label: Cryptococcus neoformans (NCBITaxon:5207)
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_5207.yaml
    role: causal_graph_overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: seeder
- target_id: NCBITaxon_235443
  path: data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml
  label: Cryptococcus neoformans H99 (NCBITaxon:235443)
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_235443.yaml
    role: causal_graph_overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: seeder
- target_id: NCBITaxon_40410
  path: data/taxa/eukaryota/cryptococcus_deneoformans.yaml
  label: Cryptococcus deneoformans (NCBITaxon:40410)
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_40410.yaml
    role: causal_graph_overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: seeder
- target_id: NCBITaxon_283643
  path: data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml
  label: Cryptococcus deneoformans B-3501A (NCBITaxon:283643)
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_283643.yaml
    role: causal_graph_overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: seeder
- target_id: NCBITaxon_1859096
  path: data/taxa/eukaryota/cryptococcus_deuterogattii.yaml
  label: Cryptococcus deuterogattii (NCBITaxon:1859096)
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_1859096.yaml
    role: causal_graph_overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: seeder
- target_id: NCBITaxon_294750
  path: data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml
  label: Cryptococcus deuterogattii R265 (NCBITaxon:294750)
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_294750.yaml
    role: causal_graph_overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: seeder
checks:
- check_id: check_provenance
  name: Causal-graph and UniProtKB catalog provenance gate
  status: passed
  required: true
  summary: scripts/check_provenance.py verified all 16 raw inventories, ATB/StrainInfo
    snapshots, 64 uniprot_proteins.tsv rows, and 15 causal-graph overlays with 0 problems.
  target_ids:
  - uniprot_proteins_catalog
  - NCBITaxon_562
  - NCBITaxon_83333
  - NCBITaxon_511145
  - NCBITaxon_1423
  - NCBITaxon_224308
  - NCBITaxon_287
  - NCBITaxon_208964
  - NCBITaxon_2190
  - NCBITaxon_243232
  - NCBITaxon_5207
  - NCBITaxon_235443
  - NCBITaxon_40410
  - NCBITaxon_283643
  - NCBITaxon_1859096
  - NCBITaxon_294750
  command: .venv/bin/python scripts/check_provenance.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_uniprot_api
  - ev_provenance_gate
- check_id: pytest_causal_graph_overlays
  name: Causal-graph and UniProtKB unit and integration test suite
  status: passed
  required: true
  summary: All 20 tests in tests/test_causal_graph_overlays.py passed across 64 UniProtKB
    rows, 141 GENE_OR_PROTEIN nodes, and 518 edges.
  target_ids:
  - uniprot_proteins_catalog
  - NCBITaxon_562
  - NCBITaxon_83333
  - NCBITaxon_511145
  - NCBITaxon_1423
  - NCBITaxon_224308
  - NCBITaxon_287
  - NCBITaxon_208964
  - NCBITaxon_2190
  - NCBITaxon_243232
  - NCBITaxon_5207
  - NCBITaxon_235443
  - NCBITaxon_40410
  - NCBITaxon_283643
  - NCBITaxon_1859096
  - NCBITaxon_294750
  command: .venv/bin/pytest -q tests/test_causal_graph_overlays.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_pytest_overlays
- check_id: validate_strict_15_records
  name: Closed-schema LinkML validation of all 15 causal-graph TaxonRecord files
  status: passed
  required: true
  summary: scripts/validate_strict.py validated all 15 causal-graph TaxonRecord YAML
    files with 0 errors.
  target_ids:
  - NCBITaxon_562
  - NCBITaxon_83333
  - NCBITaxon_511145
  - NCBITaxon_1423
  - NCBITaxon_224308
  - NCBITaxon_287
  - NCBITaxon_208964
  - NCBITaxon_2190
  - NCBITaxon_243232
  - NCBITaxon_5207
  - NCBITaxon_235443
  - NCBITaxon_40410
  - NCBITaxon_283643
  - NCBITaxon_1859096
  - NCBITaxon_294750
  command: .venv/bin/python scripts/validate_strict.py --out .temp/instance_validation_failures.tsv
    ...
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_validate_strict
evidence:
- evidence_id: ev_uniprot_api
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/{P0A6T3,P08874,Q9I4X3,Q58257,J9VX63}.json
  locator: UniProtKB release 2026_02 REST API JSON payloads
  accessed_at: '2026-11-11T12:05:00Z'
  support: supports
  summary: Verified canonical accessions, entry names, SWISS_PROT review status, organism_taxon_id,
    proteome_id (UP:UP000000625, UP:UP000001570, UP:UP000002438, UP:UP000000805, UP:UP000010091),
    gene_symbol, locus_tag, EC numbers, sequence_length, sequence_crc64, and sequence_version
    for UniProtKB:P0A6T3 (GAL1_ECOLI), UniProtKB:P08874 (ABRB_BACSU), UniProtKB:Q9I4X3
    (PQSA_PSEAE), UniProtKB:Q58257 (MTRE_METJA), and UniProtKB:J9VX63 (US101_CRYN9).
- evidence_id: ev_primary_literature
  kind: primary_source
  reference: PMID:3158881; PMID:1327124; PMID:16524589; PMID:7966338; PMID:2513264;
    PMID:3096956; PMID:1901914; PMID:12142479; PMID:15066899; PMID:22325716; PMID:9603883;
    PMID:27668432; PMID:24743168
  locator: Europe PMC / PubMed indexed primary experimental and genome literature
  accessed_at: '2026-11-11T12:08:00Z'
  support: supports
  summary: Primary literature supporting E. coli GalK galactokinase expression, CRP
    gal P1 activation, and Leloir galactose phosphorylation (PMID:9278503, PMID:3158881,
    PMID:16738553, PMID:1327124, PMID:16524589, PMID:7966338); B. subtilis AbrB transition-state
    repression by Spo0A~P and repression of spo0E/sigH (PMID:9384377, PMID:2513264,
    PMID:3096956, PMID:3121588, PMID:1901914, PMID:2113474); P. aeruginosa PqsA anthranilate-CoA
    ligase activation by MvfR/PqsR and PQS signaling to PhzM pyocyanin biosynthesis
    (PMID:10984043, PMID:12142479, PMID:15066899, PMID:18331462, PMID:16336047, PMID:22325716);
    M. jannaschii MtrE tetrahydromethanopterin S-methyltransferase subunit E complex
    formation with MtrA and coupling to McrA methanogenesis (PMID:8688087, PMID:9603883);
    and C. neoformans H99 Usv101 (CNAG_05420) C2H2 zinc-finger regulation of Rim101/CAP59
    polysaccharide capsule assembly (PMID:24743168, PMID:27668432).
- evidence_id: ev_provenance_gate
  kind: validation
  reference: scripts/check_provenance.py
  locator: causal_graph_provenance_problems()
  accessed_at: '2026-11-11T12:12:00Z'
  support: supports
  summary: Offline provenance gate verified 0 errors across 64 UniProtKB rows, 141
    GENE_OR_PROTEIN nodes, and 518 causal edges.
- evidence_id: ev_pytest_overlays
  kind: validation
  reference: tests/test_causal_graph_overlays.py
  locator: 20 test functions in tests/test_causal_graph_overlays.py
  accessed_at: '2026-11-11T12:13:00Z'
  support: supports
  summary: 20 passed in tests/test_causal_graph_overlays.py verifying catalog invariants,
    lineage/strain binding, and HTML rendering.
- evidence_id: ev_validate_strict
  kind: validation
  reference: scripts/validate_strict.py
  locator: LinkML closed-schema validation of 15 TaxonRecord YAML files
  accessed_at: '2026-11-11T12:14:00Z'
  support: supports
  summary: All 15 causal-graph TaxonRecord YAML files passed LinkML closed-schema
    validation with 0 failures.
assessments:
- assessment_id: assess_updated_proteome_cohorts
  area: grounding
  topic: Live-verified Swiss-Prot protein curation across the 11 reference-proteome
    causal-graph overlays
  outcome: supported
  summary: Added 5 live-verified Swiss-Prot proteins (UniProtKB:P0A6T3, UniProtKB:P08874,
    UniProtKB:Q9I4X3, UniProtKB:Q58257, UniProtKB:J9VX63) to curation/uniprot_proteins.tsv
    (64 total rows) and 11 GENE_OR_PROTEIN nodes + 33 evidence-backed edges across
    the 11 reference-proteome overlays (141 total GENE_OR_PROTEIN nodes, 518 total
    edges).
  target_ids:
  - uniprot_proteins_catalog
  - NCBITaxon_562
  - NCBITaxon_83333
  - NCBITaxon_511145
  - NCBITaxon_1423
  - NCBITaxon_224308
  - NCBITaxon_287
  - NCBITaxon_208964
  - NCBITaxon_2190
  - NCBITaxon_243232
  - NCBITaxon_5207
  - NCBITaxon_235443
  evidence_ids:
  - ev_uniprot_api
  - ev_primary_literature
  - ev_provenance_gate
  - ev_pytest_overlays
  - ev_validate_strict
  metrics:
  - name: pinned_uniprot_accessions
    value: 64.0
    unit: accessions
    definition: Total live-verified UniProtKB accessions pinned in curation/uniprot_proteins.tsv.
    minimum: 0.0
  - name: gene_or_protein_nodes
    value: 141.0
    unit: nodes
    definition: Total GENE_OR_PROTEIN nodes across the 15 maintained causal-graph
      overlays.
    minimum: 0.0
  - name: causal_graph_edges
    value: 518.0
    unit: edges
    definition: Total evidence-backed causal edges across the 15 maintained causal-graph
      overlays.
    minimum: 0.0
- assessment_id: assess_cryptococcus_upstream_proteome_limits
  area: completeness
  topic: Upstream UniProt proteome and Swiss-Prot review limits on C. deneoformans
    B-3501A and C. deuterogattii R265
  outcome: supported
  summary: Verified that the 4 remaining Cryptococcus overlays (NCBITaxon:40410, NCBITaxon:283643,
    NCBITaxon:1859096, NCBITaxon:294750) preserve their existing verified UniProtKB
    protein nodes (UniProtKB:Q55P57, UniProtKB:Q56R42, UniProtKB:A0A095C6P1, UniProtKB:A0A095CIC4)
    and documented their upstream UniProtKB proteome/Swiss-Prot coverage bounds.
  target_ids:
  - NCBITaxon_40410
  - NCBITaxon_283643
  - NCBITaxon_1859096
  - NCBITaxon_294750
  evidence_ids:
  - ev_provenance_gate
  - ev_pytest_overlays
  - ev_validate_strict
findings:
- finding_id: f_cryptococcus_proteome_and_trembl_limits
  issue_key: taxonmech-uniprot-cryptococcus-proteome-and-corpus-scope-limits
  category: representation
  severity: informational
  status: deferred
  certainty: confirmed
  title: 626,033 seed-only records lack causal_graphs and 4 Cryptococcus overlays
    face upstream UniProt proteome/Swiss-Prot bounds
  description: 'In TaxonMech, UniProtKB protein groundings live on CausalNode entries
    (node_type: GENE_OR_PROTEIN) inside curation/causal_graphs/*.yaml overlays validated
    against curation/uniprot_proteins.tsv. (1) 626,033 of 626,048 in-scope records
    have no causal_graphs overlay and cannot carry protein groundings without new
    causal-graph overlays or a top-level protein exemplar slot. (2) C. deneoformans
    B-3501A (NCBITaxon:283643, host of NCBITaxon:40410 / NCBITaxon:283643) lacks an
    active UniProt reference proteome (UP:*), and C. deuterogattii R265 (NCBITaxon:294750,
    UP:UP000029445, host of NCBITaxon:1859096 / NCBITaxon:294750) has zero reviewed
    Swiss-Prot entries in UniProt 2026_02.'
  target_ids:
  - uniprot_proteins_catalog
  - NCBITaxon_40410
  - NCBITaxon_283643
  - NCBITaxon_1859096
  - NCBITaxon_294750
  field_paths:
  - causal_graphs[].nodes[].grounding
  - causal_graphs[].nodes[].proteome_id
  evidence_ids:
  - ev_uniprot_api
  - ev_provenance_gate
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: uniprot_protein_catalog
  - repository: CultureBotAI/TaxonMech
    path: INFRA_TASKS.md
    role: infrastructure_backlog
  disposition_reason: 'Tracked under open issue #78 and INFRA_TASKS.md task taxonmech-infra-0003;
    existing verified protein nodes remain intact and validated.'
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/78
actions: []
limitations:
- 626,033 of 626,048 in-scope TaxonMech records do not yet have curation/causal_graphs/*.yaml
  overlays and therefore cannot carry GENE_OR_PROTEIN nodes without upstream causal-graph
  curation (#78 / taxonmech-infra-0001 / taxonmech-infra-0003).
- Cryptococcus deneoformans B-3501A (NCBITaxon:283643) has no active UniProt reference
  proteome (UP:*), and Cryptococcus deuterogattii R265 (NCBITaxon:294750, UP:UP000029445)
  has 0 reviewed Swiss-Prot entries in UniProt release 2026_02.
links:
- https://github.com/CultureBotAI/TaxonMech/issues/78
tags:
- cycle12
- stage3
- protein_examples
- uniprot
```
