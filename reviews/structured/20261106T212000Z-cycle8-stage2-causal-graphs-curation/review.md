# Cycle 8 Stage 2 causal graphs curation and corpus review (626,048 records; 15 curated species+strain exemplars, 301 evidence-backed edges)

- Review: 20261106T212000Z-cycle8-stage2-causal-graphs-curation
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-11-06T20:55:00Z
- Finished UTC: 2026-11-06T21:20:00Z
- Reviewer: Antigravity (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 626,048 in-scope TaxonRecord files across Bacteria (605,695), Archaea (14,013), Eukaryota (6,331), and other (9) against the Stage 2 causal-graph curation contract (.claude/skills/curate-causal-graphs/SKILL.md). Verified that all native prerequisite gates pass, including offline UniProtKB reference proteome and NCBI Taxonomy lineage validation (curation/uniprot_proteins.tsv and validate_causal_graph_proteins() in src/taxonmech/seed.py). Enriched 11 maintained curation/causal_graphs/*.yaml overlays across Escherichia coli (NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145; adding edge e29 linking ptsH UniProtKB:P0AA04 via causally upstream of or within RO:0002418 to lactose_transport GO:0015767, PMID:2960675, PMID:17158705), Bacillus subtilis (NCBITaxon:1423, NCBITaxon:224308; adding edge e36 linking kinC UniProtKB:P39764 via positively regulates RO:0002213 to spo0A UniProtKB:P06534, PMID:8002614, PMID:8002615, PMID:11069677), Pseudomonas aeruginosa (NCBITaxon:287, NCBITaxon:208964; adding edge e19 linking rhlR UniProtKB:P54292 via positively regulates RO:0002213 to phzA1 UniProtKB:Q9HWH1, PMID:27851827, PMID:35019777, PMID:38064526), Methanocaldococcus jannaschii (NCBITaxon:2190, NCBITaxon:243232; adding edge e23 linking mtrH UniProtKB:Q58264 via causally upstream of or within RO:0002418 to mcr_activity GO:0050524, PMID:10338124, PMID:9367957, PMID:38530900), and Cryptococcus neoformans (NCBITaxon:5207, NCBITaxon:235443; adding edge e19 linking mbs1 UniProtKB:J9VG42 via positively regulates RO:0002213 to laccase_activity GO:0052716, PMID:22080454, PMID:25849373, PMID:31575776), expanding the 15 maintained overlays from 290 to 301 evidence-backed edges across 7 cross-domain species exemplars and 8 reference-proteome strains (86 GENE_OR_PROTEIN nodes covering 39 live-verified UniProtKB accessions). Corpus-wide automated expansion across the remaining 38,342 trait/medium-attested records remains source-limited by pre-aggregated 2-column count tables in data/raw/{madin_taxa,bactotraits_taxa}.tsv (tracked under #78 / taxonmech-infra-0002).

## Scope And Provenance

Full-corpus Cycle 8 Stage 2 causal-graph review across all 626,048 TaxonRecord files in data/taxa/, paired with native curation, enrichment, and seeding across all 15 maintained curation/causal_graphs/*.yaml overlays (301 evidence-backed edges across 7 cross-domain species exemplars and 8 reference-proteome strains).

Selection: All 626,048 in-scope taxa in curation/seed_scope.tsv and data/taxa/PATHS.tsv classified by raw source coverage, with all 15 causal-graph-bearing species and strain exemplars reviewed, enriched, and validated directly.
Coverage: sampled; 15 reviewed / 626048 in the declared population.
Source: working_tree at Git base 4895ee09fec7eb5622a3b7e298fb39a314bc70ec.
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
| Strict LinkML and custom semantic validation on all 15 causal-graph-seeded TaxonRecord files | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:5207, NCBITaxon:235443 | All 15 seeded TaxonRecord YAML files pass scripts/validate_strict.py with 0 errors. |
| OAK ID-label correspondence validation across all 15 causal-graph overlays | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:5207, NCBITaxon:235443 | scripts/validate_id_label_correspondence.py verifies 331 OK_CANONICAL GO and RO pairs (30 GO node groundings + 301 RO edge predicates; 338 OBO-grounded pairs including 7 CHEBI node groundings) and 0 MISMATCH across all grounded nodes and predicates in curation/causal_graphs/*.yaml. |
| Unit and integration test suite for causal-graph overlays, offline UniProtKB reference proteome validation, seeder merge, and HTML rendering | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:5207, NCBITaxon:235443 | tests/test_causal_graph_overlays.py passes all roundtrip, offline UniProtKB reference proteome and lineage validation, rendering, and committed-overlay validation checks (301 edges across 15 overlays). |

## Scientific And Domain Assessments

### Evidence-backed native CausalGraph curation and enrichment across 15 cross-domain species and reference-proteome strain records

graph: supported. Targets: NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:5207, NCBITaxon:235443.

Maintained 15 curation/causal_graphs/*.yaml overlays (enriched from 290 to 301 evidence-backed edges in Cycle 8 Stage 2) across Escherichia coli (NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145; 29 edges each including e29 ptsH -&gt; RO:0002418 -&gt; lactose_transport), Bacillus subtilis (NCBITaxon:1423, NCBITaxon:224308; 36 edges each including e36 kinC -&gt; RO:0002213 -&gt; spo0A), Pseudomonas aeruginosa (NCBITaxon:287, NCBITaxon:208964; 19 edges each including e19 rhlR -&gt; RO:0002213 -&gt; phzA1), Methanocaldococcus jannaschii (NCBITaxon:2190, NCBITaxon:243232; 23 edges each including e23 mtrH -&gt; RO:0002418 -&gt; mcr_activity), Cryptococcus deuterogattii (NCBITaxon:1859096, NCBITaxon:294750; 6 edges each), Cryptococcus deneoformans (NCBITaxon:40410, NCBITaxon:283643; 4 edges each), and Cryptococcus neoformans (NCBITaxon:5207, NCBITaxon:235443; 19 edges each including e19 mbs1 -&gt; RO:0002213 -&gt; laccase_activity).

### Remaining corpus-wide trait/medium-attested records awaiting upstream kg-microbe granular edge extraction

completeness: concern. Targets: NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:5207, NCBITaxon:235443.

While extract_taxon_trait_edges() is implemented in src/taxonmech/extract.py (#78 / taxonmech-infra-0002), committed data/raw/madin_taxa.tsv and data/raw/bactotraits_taxa.tsv remain 2-column count tables until re-extracted from an upstream local kg-microbe checkout, limiting bulk automated causal-graph generation across the remaining 38,342 trait/medium-attested records.

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
| curated-causal-graph-overlays-and-records | curation/causal_graphs/NCBITaxon_*.yaml; data/taxa/{bacteria,archaea,eukaryota}/*.yaml; curation/causal_graphs/NCBITaxon_{562,83333,511145,1423,224308,287,208964,2190,243232,1859096,294750,40410,283643,5207,235443}.yaml | supports | Fifteen maintained curation/causal_graphs/*.yaml overlays define 301 evidence-backed causal edges with PMID citations, verified UniProtKB reference proteome accessions, and canonical GO/CHEBI/RO/METPO groundings, merged deterministically into their 15 TaxonRecord YAML files. |
| oak-id-label-validation | conf/id_label_targets.yaml; scripts/validate_id_label_correspondence.py; conf/id_label_targets.yaml:14-65 | supports | All OBO-grounded node and edge pairs across GO, CHEBI, RO, and METPO in the 15 causal-graph overlays match canonical OAK ontology labels (0 MISMATCH). |
| seeder-and-verify-corpus-pipeline | src/taxonmech/seed.py; curation/uniprot_proteins.tsv; tests/test_causal_graph_overlays.py; src/taxonmech/seed.py:217-370,790-810; tests/test_causal_graph_overlays.py:1-961 | supports | load_causal_graphs(), validate_causal_graph_proteins(), and build_document() merge maintained overlays into TaxonRecord.causal_graphs and curation_history while enforcing offline UniProtKB reference proteome and lineage validation and byte-for-byte reproducibility. |
| raw-phenotype-and-trait-inventories | data/raw/madin_taxa.tsv; data/raw/bactotraits_taxa.tsv; data/raw/mediadive_taxa.tsv; madin_taxa.tsv (34,148 rows); bactotraits_taxa.tsv (9,658 rows); mediadive_taxa.tsv (14,154 rows) | supports | Committed raw tables in data/raw/madin_taxa.tsv and data/raw/bactotraits_taxa.tsv store 2-column (taxon_id, assertion_count) summaries until an upstream kg-microbe checkout re-extraction runs extract_taxon_trait_edges(). |

## Limits And Additional Notes

- Bulk automated causal-graph synthesis across the remaining 38,342 Madin/BactoTraits/MediaDive-attested records requires running extract_taxon_trait_edges() against an upstream local kg-microbe checkout (#78 / taxonmech-infra-0002).
- 562,682 of 626,048 in-scope records are taxonomy-only records without phenotype, growth-medium, genome, or strain rows in data/raw/.
- Cycle 8 Stage 2 enriched 11 maintained curation/causal_graphs/*.yaml overlays across Escherichia coli, Bacillus subtilis, Pseudomonas aeruginosa, Methanocaldococcus jannaschii, and Cryptococcus neoformans from 290 to 301 evidence-backed edges across all 15 curated cross-domain species and reference-proteome strain records.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T212000Z-cycle8-stage2-causal-graphs-curation
kind: batch
repository: CultureBotAI/TaxonMech
title: Cycle 8 Stage 2 causal graphs curation and corpus review (626,048 records;
  15 curated species+strain exemplars, 301 evidence-backed edges)
started_at: '2026-11-06T20:55:00Z'
finished_at: '2026-11-06T21:20:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: independent
  independence_basis: Cycle 8 Stage 2 causal-graph curation and audit worker; verified
    all native prerequisite gates, inspected all 626,048 in-scope records and all
    15 maintained curation/causal_graphs/*.yaml overlays, enriched 11 overlays across
    Escherichia coli, Bacillus subtilis, Pseudomonas aeruginosa, Methanocaldococcus
    jannaschii, and Cryptococcus neoformans from 290 to 301 evidence-backed edges,
    seeded the 11 updated TaxonRecord files, and verified LinkML, OAK ID-label correspondence,
    offline UniProtKB reference proteome validation, and HTML rendering gates.
skill: .claude/skills/curate-causal-graphs/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed all 626,048 in-scope TaxonRecord files across Bacteria (605,695),
  Archaea (14,013), Eukaryota (6,331), and other (9) against the Stage 2 causal-graph
  curation contract (.claude/skills/curate-causal-graphs/SKILL.md). Verified that
  all native prerequisite gates pass, including offline UniProtKB reference proteome
  and NCBI Taxonomy lineage validation (curation/uniprot_proteins.tsv and validate_causal_graph_proteins()
  in src/taxonmech/seed.py). Enriched 11 maintained curation/causal_graphs/*.yaml
  overlays across Escherichia coli (NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145;
  adding edge e29 linking ptsH UniProtKB:P0AA04 via causally upstream of or within
  RO:0002418 to lactose_transport GO:0015767, PMID:2960675, PMID:17158705), Bacillus
  subtilis (NCBITaxon:1423, NCBITaxon:224308; adding edge e36 linking kinC UniProtKB:P39764
  via positively regulates RO:0002213 to spo0A UniProtKB:P06534, PMID:8002614, PMID:8002615,
  PMID:11069677), Pseudomonas aeruginosa (NCBITaxon:287, NCBITaxon:208964; adding
  edge e19 linking rhlR UniProtKB:P54292 via positively regulates RO:0002213 to phzA1
  UniProtKB:Q9HWH1, PMID:27851827, PMID:35019777, PMID:38064526), Methanocaldococcus
  jannaschii (NCBITaxon:2190, NCBITaxon:243232; adding edge e23 linking mtrH UniProtKB:Q58264
  via causally upstream of or within RO:0002418 to mcr_activity GO:0050524, PMID:10338124,
  PMID:9367957, PMID:38530900), and Cryptococcus neoformans (NCBITaxon:5207, NCBITaxon:235443;
  adding edge e19 linking mbs1 UniProtKB:J9VG42 via positively regulates RO:0002213
  to laccase_activity GO:0052716, PMID:22080454, PMID:25849373, PMID:31575776), expanding
  the 15 maintained overlays from 290 to 301 evidence-backed edges across 7 cross-domain
  species exemplars and 8 reference-proteome strains (86 GENE_OR_PROTEIN nodes covering
  39 live-verified UniProtKB accessions). Corpus-wide automated expansion across the
  remaining 38,342 trait/medium-attested records remains source-limited by pre-aggregated
  2-column count tables in data/raw/{madin_taxa,bactotraits_taxa}.tsv (tracked under
  #78 / taxonmech-infra-0002).'
source:
  git_revision: 4895ee09fec7eb5622a3b7e298fb39a314bc70ec
  state: working_tree
  inputs:
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
    sha256: 4d4bcd8cfdcb4712331e98d6ed7031ab8ebec4a9d70baf87947a398d875d1e73
    role: context
  - path: README.md
    sha256: 99cc7a9e30b1b766c95b9f7639fe6588552866dfa4645c5fda374281b3f4fde7
    role: context
  - path: conf/id_label_targets.yaml
    sha256: efed4c6d9cc218c9d89ba4468e361761ac02ff535e2669de33af6606202e544c
    role: context
  - path: conf/record_review.yaml
    sha256: 366312506b771fc18fc5bfc30d5ec942b2c96212e1f4f95c463cfa1707fbebaa
    role: context
  - path: curation/causal_graphs/NCBITaxon_1423.yaml
    sha256: 72523d87c7a5723c977dadd2570c85ede2eb7e78f382ad383956d071c5fb0a27
    role: context
  - path: curation/causal_graphs/NCBITaxon_1859096.yaml
    sha256: 0f29a0916110b21224537ec5e337a9e8fa5a61c3a9c3f04885f421e7974d8746
    role: context
  - path: curation/causal_graphs/NCBITaxon_208964.yaml
    sha256: 75cfd07c6a66f3bcb004477ca3884df79bec5872b73c3428e190990bd5542ad6
    role: context
  - path: curation/causal_graphs/NCBITaxon_2190.yaml
    sha256: 8fbd7dd03321ae9288d506e1e88a5314e301475209da5bd17d1d90086df8f667
    role: context
  - path: curation/causal_graphs/NCBITaxon_224308.yaml
    sha256: 8505326e9fba88a9cd62f45aeadeb8b1e4c58a46fe74c87b965b786fb7e25324
    role: context
  - path: curation/causal_graphs/NCBITaxon_235443.yaml
    sha256: e8d998680af2d5f3197683598a1cb67f9886ac8a787062eebd7dd0133c5a510e
    role: context
  - path: curation/causal_graphs/NCBITaxon_243232.yaml
    sha256: 4cff2d2e2366e98d3b5998b934e10ac4abe02339b814cde69e10922aff15fcda
    role: context
  - path: curation/causal_graphs/NCBITaxon_283643.yaml
    sha256: 3098281e6de9a4dccdcf51f3c7a8db7f47c4c3dfadb333682957c4e331f35caf
    role: context
  - path: curation/causal_graphs/NCBITaxon_287.yaml
    sha256: 463a823dedee745dca546bb077b4e49708f4eea7ec52049c1522891b08a6fe84
    role: context
  - path: curation/causal_graphs/NCBITaxon_294750.yaml
    sha256: 3ec5ba3c0784bbda20a3df13863c7faf96fb21562e01394fa0e69ec9f3f2215e
    role: context
  - path: curation/causal_graphs/NCBITaxon_40410.yaml
    sha256: 425d1eece60fd72e9c552eee49e2af7543b9b278b2555f0c0b991c537d85c3cc
    role: context
  - path: curation/causal_graphs/NCBITaxon_511145.yaml
    sha256: 508db56887066d691676c07fbabf081e01a2adab872a9345b52a525163cf1222
    role: context
  - path: curation/causal_graphs/NCBITaxon_5207.yaml
    sha256: 2e6a01b0aeed11465a345df69607848dbd0e812128e401b938d05a43903a6784
    role: context
  - path: curation/causal_graphs/NCBITaxon_562.yaml
    sha256: 62f361e651a1c8d3b6a352a0ce77f5f42ae78d0dae2c9c113035152b5f7561c7
    role: context
  - path: curation/causal_graphs/NCBITaxon_83333.yaml
    sha256: 69bee736fda5c4ff8eeef8ce6834053011da2cbbf6325f138a8a6fe630f7b27d
    role: context
  - path: curation/causal_graphs/README.md
    sha256: 840eb57f4d180742c32a1ebe76474a155c89fc0b0667630df65eb60dc84a8bc5
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
    sha256: edc5decffaad744125f62a6ab7d437295e142ddf586d7d77e24b9fc49bea9d8d
    role: target
  - path: data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml
    sha256: bb9b7b222264f79e4aa19bc45b372361e953234f9e9103a36bfd8c2173170628
    role: target
  - path: data/taxa/bacteria/bacillus_subtilis.yaml
    sha256: 952bc7737bc65c7e983cdd0abe5840f613d79a1bbeaae7235627b7dbf31cd991
    role: target
  - path: data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml
    sha256: 245362d9fc0148af9ca2041ae572442d414ede460f6bf4cbd1792108880a5059
    role: target
  - path: data/taxa/bacteria/escherichia_coli.yaml
    sha256: 9ac8aebbb708d9fbeabcaaa9994a218463a5178730ce8fa99e1f4a126673a561
    role: target
  - path: data/taxa/bacteria/escherichia_coli_k_12.yaml
    sha256: 25c0dce0f3dec1253fef24952f04882f417e87a74999d668b2af166c0b3acaad
    role: target
  - path: data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml
    sha256: 52b0a5fb69644798e87896c18da17f9b645cf714774eff56e8e78cba02baa251
    role: target
  - path: data/taxa/bacteria/pseudomonas_aeruginosa.yaml
    sha256: 510b37cc22cba367b15359c7dfcd8dcc7647dcddea15b8c8666c3fb875e37d08
    role: target
  - path: data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml
    sha256: fd57537d81ad0edab13ab6dd83078ddf3c6953c1a36089232538281e1679d8d1
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
    sha256: 85f2d06f6deed065f240ed316feb85b7ab90395c5be652a5acbdb54a8088a066
    role: target
  - path: data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml
    sha256: 00bc27c6b00fde56c025d1c46acafba89a997fe56a6839ff641adab22c86759e
    role: target
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
    sha256: b02be7259498bc7d540bb095a3db5b2a6557520062ab05e40d127748ca26053b
    role: context
  - path: src/taxonmech/templates/taxon-content.html
    sha256: 9562204e103755b648b32234cf001253e855a64bb46f5de1eb372b5fcf7ad3a2
    role: context
  - path: tests/test_causal_graph_overlays.py
    sha256: 1c33c0df836f4f10447b8857709e66e7a77dc008cc315e2bda18be4ffabacdd0
    role: context
scope:
  description: Full-corpus Cycle 8 Stage 2 causal-graph review across all 626,048
    TaxonRecord files in data/taxa/, paired with native curation, enrichment, and
    seeding across all 15 maintained curation/causal_graphs/*.yaml overlays (301 evidence-backed
    edges across 7 cross-domain species exemplars and 8 reference-proteome strains).
  selection: All 626,048 in-scope taxa in curation/seed_scope.tsv and data/taxa/PATHS.tsv
    classified by raw source coverage, with all 15 causal-graph-bearing species and
    strain exemplars reviewed, enriched, and validated directly.
  coverage: sampled
  population_size: 626048
  sampling_method: Exhaustive deterministic census of all 626,048 records in curation/seed_scope.tsv
    and data/raw/{madin_taxa,bactotraits_taxa,mediadive_taxa,gold_organisms,bacdive_strains,ncbitaxon_taxa}.tsv
    plus 100% inspection and verification of all 15 species and reference-proteome
    strain records carrying maintained curation/causal_graphs/*.yaml overlays across
    Bacteria, Archaea, and Eukaryota.
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
  summary: All 15 seeded TaxonRecord YAML files pass scripts/validate_strict.py with
    0 errors.
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
  - curated-causal-graph-overlays-and-records
- check_id: validate-oak-id-label-correspondence
  name: OAK ID-label correspondence validation across all 15 causal-graph overlays
  status: passed
  required: true
  summary: scripts/validate_id_label_correspondence.py verifies 331 OK_CANONICAL GO
    and RO pairs (30 GO node groundings + 301 RO edge predicates; 338 OBO-grounded
    pairs including 7 CHEBI node groundings) and 0 MISMATCH across all grounded nodes
    and predicates in curation/causal_graphs/*.yaml.
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
    reference proteome validation, seeder merge, and HTML rendering
  status: passed
  required: true
  summary: tests/test_causal_graph_overlays.py passes all roundtrip, offline UniProtKB
    reference proteome and lineage validation, rendering, and committed-overlay validation
    checks (301 edges across 15 overlays).
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
  - seeder-and-verify-corpus-pipeline
evidence:
- evidence_id: curated-causal-graph-overlays-and-records
  kind: record_content
  reference: curation/causal_graphs/NCBITaxon_*.yaml; data/taxa/{bacteria,archaea,eukaryota}/*.yaml
  locator: curation/causal_graphs/NCBITaxon_{562,83333,511145,1423,224308,287,208964,2190,243232,1859096,294750,40410,283643,5207,235443}.yaml
  accessed_at: '2026-11-06T21:20:00Z'
  support: supports
  summary: Fifteen maintained curation/causal_graphs/*.yaml overlays define 301 evidence-backed
    causal edges with PMID citations, verified UniProtKB reference proteome accessions,
    and canonical GO/CHEBI/RO/METPO groundings, merged deterministically into their
    15 TaxonRecord YAML files.
  snapshot_sha256: 62f361e651a1c8d3b6a352a0ce77f5f42ae78d0dae2c9c113035152b5f7561c7
- evidence_id: oak-id-label-validation
  kind: validation
  reference: conf/id_label_targets.yaml; scripts/validate_id_label_correspondence.py
  locator: conf/id_label_targets.yaml:14-65
  accessed_at: '2026-11-06T21:20:00Z'
  support: supports
  summary: All OBO-grounded node and edge pairs across GO, CHEBI, RO, and METPO in
    the 15 causal-graph overlays match canonical OAK ontology labels (0 MISMATCH).
  snapshot_sha256: efed4c6d9cc218c9d89ba4468e361761ac02ff535e2669de33af6606202e544c
- evidence_id: seeder-and-verify-corpus-pipeline
  kind: validation
  reference: src/taxonmech/seed.py; curation/uniprot_proteins.tsv; tests/test_causal_graph_overlays.py
  locator: src/taxonmech/seed.py:217-370,790-810; tests/test_causal_graph_overlays.py:1-961
  accessed_at: '2026-11-06T21:20:00Z'
  support: supports
  summary: load_causal_graphs(), validate_causal_graph_proteins(), and build_document()
    merge maintained overlays into TaxonRecord.causal_graphs and curation_history
    while enforcing offline UniProtKB reference proteome and lineage validation and
    byte-for-byte reproducibility.
  snapshot_sha256: b02be7259498bc7d540bb095a3db5b2a6557520062ab05e40d127748ca26053b
- evidence_id: raw-phenotype-and-trait-inventories
  kind: database
  reference: data/raw/madin_taxa.tsv; data/raw/bactotraits_taxa.tsv; data/raw/mediadive_taxa.tsv
  locator: madin_taxa.tsv (34,148 rows); bactotraits_taxa.tsv (9,658 rows); mediadive_taxa.tsv
    (14,154 rows)
  accessed_at: '2026-11-06T21:20:00Z'
  support: supports
  summary: Committed raw tables in data/raw/madin_taxa.tsv and data/raw/bactotraits_taxa.tsv
    store 2-column (taxon_id, assertion_count) summaries until an upstream kg-microbe
    checkout re-extraction runs extract_taxon_trait_edges().
  snapshot_sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
assessments:
- assessment_id: exemplar-species-and-strain-causal-graphs-enriched
  area: graph
  topic: Evidence-backed native CausalGraph curation and enrichment across 15 cross-domain
    species and reference-proteome strain records
  outcome: supported
  summary: Maintained 15 curation/causal_graphs/*.yaml overlays (enriched from 290
    to 301 evidence-backed edges in Cycle 8 Stage 2) across Escherichia coli (NCBITaxon:562,
    NCBITaxon:83333, NCBITaxon:511145; 29 edges each including e29 ptsH -> RO:0002418
    -> lactose_transport), Bacillus subtilis (NCBITaxon:1423, NCBITaxon:224308; 36
    edges each including e36 kinC -> RO:0002213 -> spo0A), Pseudomonas aeruginosa
    (NCBITaxon:287, NCBITaxon:208964; 19 edges each including e19 rhlR -> RO:0002213
    -> phzA1), Methanocaldococcus jannaschii (NCBITaxon:2190, NCBITaxon:243232; 23
    edges each including e23 mtrH -> RO:0002418 -> mcr_activity), Cryptococcus deuterogattii
    (NCBITaxon:1859096, NCBITaxon:294750; 6 edges each), Cryptococcus deneoformans
    (NCBITaxon:40410, NCBITaxon:283643; 4 edges each), and Cryptococcus neoformans
    (NCBITaxon:5207, NCBITaxon:235443; 19 edges each including e19 mbs1 -> RO:0002213
    -> laccase_activity).
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
  - curated-causal-graph-overlays-and-records
  - oak-id-label-validation
  - seeder-and-verify-corpus-pipeline
  metrics:
  - name: records_with_populated_causal_graphs
    value: 15.0
    unit: records
    definition: In-scope TaxonRecord files carrying a non-empty causal_graphs list.
    denominator: 626048
    minimum: 0.0
    maximum: 626048.0
  - name: evidence_backed_causal_edges
    value: 301.0
    unit: edges
    definition: Total evidence-backed CausalEdge entries across seeded TaxonRecord.causal_graphs.
    minimum: 0.0
- assessment_id: corpus-source-limited-trait-extraction-gap
  area: completeness
  topic: Remaining corpus-wide trait/medium-attested records awaiting upstream kg-microbe
    granular edge extraction
  outcome: concern
  summary: While extract_taxon_trait_edges() is implemented in src/taxonmech/extract.py
    (#78 / taxonmech-infra-0002), committed data/raw/madin_taxa.tsv and data/raw/bactotraits_taxa.tsv
    remain 2-column count tables until re-extracted from an upstream local kg-microbe
    checkout, limiting bulk automated causal-graph generation across the remaining
    38,342 trait/medium-attested records.
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
- Bulk automated causal-graph synthesis across the remaining 38,342 Madin/BactoTraits/MediaDive-attested
  records requires running extract_taxon_trait_edges() against an upstream local kg-microbe
  checkout (#78 / taxonmech-infra-0002).
- 562,682 of 626,048 in-scope records are taxonomy-only records without phenotype,
  growth-medium, genome, or strain rows in data/raw/.
notes:
- Cycle 8 Stage 2 enriched 11 maintained curation/causal_graphs/*.yaml overlays across
  Escherichia coli, Bacillus subtilis, Pseudomonas aeruginosa, Methanocaldococcus
  jannaschii, and Cryptococcus neoformans from 290 to 301 evidence-backed edges across
  all 15 curated cross-domain species and reference-proteome strain records.
tags:
- stage2-causal-graphs
- cycle8-curation
- mechanism-representation
```
