# Cycle 4 Stage 4 full-corpus TaxonRecord and cohort review across 626,048 in-scope taxa and 15 causal-graph/UniProtKB-enriched records (161 edges, 51 GENE_OR_PROTEIN nodes across 23 UniProtKB accessions)

- Review: 20261031T075300Z-cycle4-stage4-corpus-record-review
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-31T07:45:00Z
- Finished UTC: 2026-10-31T07:53:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Executed the Cycle 4 Stage 4 (record_review) full-corpus and cohort review across all 626,048 eligible TaxonRecord YAML files in data/taxa/ (Bacteria: 605,695; Archaea: 14,013; Eukaryota: 6,331; other: 9) reconciled against docs/legacy-review-inventory.tsv (23,883 records) and docs/structured-review-inventory/part-00.tsv..part-13.tsv (602,165 records across 14 shards and 611 batches; 0 unreviewed; 0 overlap), plus all 15 TaxonRecord files enriched through Cycle 4 Stages 2-3 (PRs #181, #183) with maintained causal_graphs (161 evidence-backed edges across 33 PMIDs) and live-verified + offline-validated UniProtKB GENE_OR_PROTEIN nodes (51 nodes across 23 unique accessions: 21 SWISS_PROT and 2 TREMBL in curation/uniprot_proteins.tsv) and structural/provenance validators added in Cycle 3 Stage 6 (PR #168). Verified 4 resolved findings (#76, #83, and both #158 code and documentation/test findings), carried forward 6 open corpus-regeneration and upstream-prerequisite findings (#124/#63, #65, #118/#119, #69, #8, #78), and recorded 1 new open schema-documentation finding (schema-guide-missing-causal-node-uniprot-protein-slots under #78, where docs/SCHEMA.md omits the 9 GENE_OR_PROTEIN UniProtKB protein-grounding slots and UniProtEntryStatusEnum added to src/taxonmech/schema/taxonmech.yaml) for Cycle 4 Stage 5 grouped remediation.

## Scope And Provenance

Frozen 626,048-record TaxonMech corpus across data/taxa/bacteria/ (605,695), data/taxa/archaea/ (14,013), data/taxa/eukaryota/ (6,331), and data/taxa/other/ (9), reconciled against docs/legacy-review-inventory.tsv (23,883 records) and docs/structured-review-inventory/part-00.tsv..part-13.tsv (602,165 records) with 27 representative cross-domain, verdict-stratified, and causal-graph-enriched TaxonRecord files bound directly.

Selection: All 626,048 in-scope TaxonRecord files in curation/seed_scope.tsv and data/taxa/PATHS.tsv reconciled against the frozen review inventories, plus 27 directly bound representative records spanning Bacteria (13), Archaea (3), Eukaryota (8), and other (3) across pass, pass_with_limitations, needs_curation, blocked, and Cycle 2-4 causal-graph/UniProtKB cohorts.
Coverage: sampled; 27 reviewed / 626048 in the declared population.
Source: working_tree at Git base 830eb576c1381e73aba1ed284c1ae005c7a5337e.
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
| NCBITaxon:2940590 | data/taxa/bacteria/achromobacter_sp_jub104.yaml | generated | Achromobacter sp. JUb104 |
| NCBITaxon:3121604 | data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml | generated | Acidaminobacteraceae bacterium |
| NCBITaxon:1435036 | data/taxa/bacteria/acinetobacter_bohemicus.yaml | generated | Acinetobacter bohemicus |
| NCBITaxon:209650 | data/taxa/bacteria/acidicaldus_organivorans.yaml | generated | Acidicaldus organivorans |
| NCBITaxon:206 | data/taxa/bacteria/campylobacter_sputorum.yaml | generated | Campylobacter sputorum |
| NCBITaxon:33952 | data/taxa/bacteria/acetobacterium_woodii.yaml | generated | Acetobacterium woodii |
| NCBITaxon:2190 | data/taxa/archaea/methanocaldococcus_jannaschii.yaml | generated | Methanocaldococcus jannaschii |
| NCBITaxon:243232 | data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml | generated | Methanocaldococcus jannaschii DSM 2661 |
| NCBITaxon:2287 | data/taxa/archaea/saccharolobus_solfataricus.yaml | generated | Saccharolobus solfataricus |
| NCBITaxon:4932 | data/taxa/eukaryota/saccharomyces_cerevisiae.yaml | generated | Saccharomyces cerevisiae |
| NCBITaxon:5207 | data/taxa/eukaryota/cryptococcus_neoformans.yaml | generated | Cryptococcus neoformans |
| NCBITaxon:235443 | data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml | generated | Cryptococcus neoformans H99 |
| NCBITaxon:40410 | data/taxa/eukaryota/cryptococcus_deneoformans.yaml | generated | Cryptococcus deneoformans |
| NCBITaxon:283643 | data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml | generated | Cryptococcus deneoformans B-3501A |
| NCBITaxon:1859096 | data/taxa/eukaryota/cryptococcus_deuterogattii.yaml | generated | Cryptococcus deuterogattii |
| NCBITaxon:294750 | data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml | generated | Cryptococcus deuterogattii R265 |
| NCBITaxon:5755 | data/taxa/eukaryota/acanthamoeba_castellanii.yaml | generated | Acanthamoeba castellanii |
| NCBITaxon:155900 | data/taxa/other/uncultured_organism.yaml | generated | uncultured organism |
| NCBITaxon:408170 | data/taxa/other/human_gut_metagenome.yaml | generated | human gut metagenome |
| NCBITaxon:32644 | data/taxa/other/unidentified.yaml | generated | unidentified |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native strict, LinkML schema, structural causal-graph, and offline UniProtKB protein validation on directly bound Cycle 4 Stage 4 exemplar records | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:5755, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | All 27 directly bound cross-domain exemplar and causal-graph TaxonRecord files pass scripts/validate_strict.py (including validate_causal_graph_structure() and validate_causal_graph_proteins() against curation/uniprot_proteins.tsv) with 0 errors. |
| Native history validation across committed history records | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:5755, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | scripts/validate_history.py passes on all 29 repository history records against src/taxonmech/schema/history.yaml (#83 resolved in Cycle 1 Stage 5). |
| Required historical native-unit counts | unavailable | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:5755, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | Manifest-pinned upstream kg-microbe raw edge tables for GOLD, MEDIADIVE, MADIN, and BACTOTRAITS are not committed locally (though SHA-256 digests are documented in docs/HARMONIZATION.md), and subtree rollups apply to BacDive strains only (#8; taxonmech-infra-0004). |
| Full-corpus review coverage and disjointness check across all 626,048 records | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:5755, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | scripts/corpus_review_inventory.py --check verified 626,048 corpus records (23,883 legacy + 602,165 structured across 14 shards and 611 batches) with 0 unreviewed records and 0 overlaps. |
| Structured review inventory and post-curation target SHA-256 reconciliation regression suite | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:5755, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | pytest tests/test_corpus_review_inventory.py -k 'not verify_target_sha256' passed all 9 tests verifying shard coverage, load_latest_target_reviews() post-curation target_sha256 reconciliation (#158), and in-repository symlink input handling (#185). |
| Committed causal-graph and UniProtKB overlay regression suite | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750 | pytest tests/test_causal_graph_overlays.py passed all 6 tests verifying overlay loading, structural causal-graph validation, seeder merge, LinkML validation, offline curation/uniprot_proteins.tsv validation (including strain_id and vertical lineage consistency), and HTML rendering across all 15 maintained overlays (161 edges, 51 GENE_OR_PROTEIN nodes across 23 UniProtKB accessions). |

## Scientific And Domain Assessments

### Full-corpus review coverage (626,048 records), NCBI taxonomy alignment, and post-curation SHA-256 inventory state

identity: supported. Targets: NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:5755, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644.

All 626,048 in-scope TaxonRecord YAML files in data/taxa/ are accounted for without gap or overlap (23,883 legacy + 602,165 structured across 14 shards and 611 batches), match their pinned data/raw/ncbitaxon_taxa.tsv identifier, label, rank, domain, parent_taxon, and lineage, and have their multi-stage workflow review bundles (435 bundles in reviews/structured/ including this bundle) and post-curation target SHA-256 reconciliation contract documented in docs/corpus-review-coverage.md and enforced by tests/test_corpus_review_inventory.py (#158).

### GTDB closeMatch synonym/xref promotion, polyphyly suffix mangling, and pooled broadMatch genome/note semantics

nomenclature: concern. Targets: NCBITaxon:562, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:206, NCBITaxon:33952.

Across the 602,165 structured-review records, 95,766 records carry verdict needs_curation due to src/taxonmech/seed.py (lines 508-535) promoting skos:closeMatch GTDB species-cluster mappings to EXACT_SYNONYM and top-level xrefs (#124, #63), mangling 15,704 polyphyly-suffixed GTDB labels into fake trinomials at line 529 (#65), and emitting misleading pooled broadMatch genome totals (lines 636-650; #118) and inverted broadMatch notes (lines 522-524; #119) on 8,587 records.

### Cycle 4 causal_graphs and UniProtKB GENE_OR_PROTEIN coverage (15 records, 51 protein nodes across 23 unique UniProtKB accessions, 161 edges across 33 PMIDs), docs/SCHEMA.md slot documentation, and remaining corpus-wide prerequisites

completeness: concern. Targets: NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:5755, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644.

All 15 records enriched through Cycle 4 Stages 2-3 (PRs #155, #156, #162, #163, #181, #183) pass strict LinkML validation, structural causal-graph validation (validate_causal_graph_structure()), deterministic seeder reproduction, and offline + live UniProtKB verification across 15 causal graphs, 51 GENE_OR_PROTEIN nodes (23 unique UniProtKB accessions: 21 SWISS_PROT and 2 TREMBL in curation/uniprot_proteins.tsv), and 161 evidence-backed edges across 33 PMIDs; however, docs/SCHEMA.md (line 20) still omits the 9 GENE_OR_PROTEIN UniProtKB protein-grounding slots and UniProtEntryStatusEnum added to src/taxonmech/schema/taxonmech.yaml, and the remaining 626,033 records (99.998%) still have empty causal_graphs pending upstream kg-microbe bulk data/raw/taxon_trait_edges.tsv extraction (taxonmech-infra-0002) and a corpus-wide data/raw/ UniProtKB Reference Proteomes snapshot (taxonmech-infra-0003; #78).

## Findings

### causal-node-type-enum-and-mech-family-nav-drift: CausalNodeTypeEnum parity with TraitMech (RNA, GENETIC_ELEMENT, ORGANELLE) and NaturalProductMech family navigation remain resolved

minor / resolved / confirmed; issue key: cycle3-stage4-causal-node-type-enum-and-mech-family-nav-drift.

Verified in Cycle 4 Stage 4 that src/taxonmech/schema/taxonmech.yaml retains the 18-value CausalNodeTypeEnum superset (including RNA, GENETIC_ELEMENT, and ORGANELLE) and that README.md, AGENTS.md (and CLAUDE.md symlink), src/taxonmech/templates/{base,index}.html, and rendered pages include NaturalProductMech (#76, resolved in Cycle 1 Stage 5 PR #151).

Disposition: Resolved in Cycle 1 Stage 5 (PR #151) under #76 and verified intact in Cycle 4 Stage 4.

### validate-history-bare-linkml-validate-path: scripts/validate_history.py resolves linkml-validate beside sys.executable across all 29 history records

minor / resolved / confirmed; issue key: cycle3-stage4-validate-history-bare-linkml-validate-path.

Verified in Cycle 4 Stage 4 that scripts/validate_history.py resolves Path(sys.executable).with_name('linkml-validate') before falling back to PATH and validates all 29 committed history records against src/taxonmech/schema/history.yaml (#83, resolved in Cycle 1 Stage 5 PR #151).

Disposition: Resolved in Cycle 1 Stage 5 (PR #151) under #83 and verified across all 29 history records in Cycle 4 Stage 4.

### gtdb-closematch-exact-promotion: skos:closeMatch GTDB species-cluster mappings are promoted to EXACT_SYNONYM and equivalent top-level xrefs across 95,766 records

major / open / confirmed; issue key: cycle3-stage4-gtdb-closematch-exact-promotion.

Across docs/structured-review-inventory/part-00.tsv..part-13.tsv, 95,766 of 602,165 structured-review records (including 74,325 from fan-out closeMatch clusters; e.g., NCBITaxon:2940590 data/taxa/bacteria/achromobacter_sp_jub104.yaml promoting GTDB:s__Achromobacter_spanius, NCBITaxon:206 data/taxa/bacteria/campylobacter_sputorum.yaml promoting GTDB:s__Campylobacter_F_sputorum, and legacy-reviewed NCBITaxon:33952 data/taxa/bacteria/acetobacterium_woodii.yaml promoting GTDB:s__Acetobacterium_woodii_A) carry verdict needs_curation because src/taxonmech/seed.py (lines 508-535) promotes skos:closeMatch GTDB species-cluster rows in data/raw/gtdb_mappings.tsv to EXACT_SYNONYM and top-level xrefs without an explicit 1:1 taxon-identity or nomenclatural bridge (tracked in https://github.com/CultureBotAI/TaxonMech/issues/124 and https://github.com/CultureBotAI/TaxonMech/issues/63).

### gtdb-polyphyly-suffix-synonym-mangling: GTDB polyphyly suffixes are mangled by underscore-to-space replacement into fake trinomials published as EXACT_SYNONYM

major / open / confirmed; issue key: cycle3-stage4-gtdb-polyphyly-suffix-synonym-mangling.

In src/taxonmech/seed.py line 529, GTDB species labels are converted via m['gtdb_label'].split('__', 1)[-1].replace('_', ' '), turning GTDB polyphyly partition suffixes (e.g., s__Campylobacter_F_sputorum on NCBITaxon:206 data/taxa/bacteria/campylobacter_sputorum.yaml -&gt; 'Campylobacter F sputorum', and s__Acetobacterium_woodii_A on NCBITaxon:33952 data/taxa/bacteria/acetobacterium_woodii.yaml -&gt; 'Acetobacterium woodii A') into fake trinomials published as EXACT_SYNONYM across 15,704 rows in data/raw/gtdb_mappings.tsv (tracked in https://github.com/CultureBotAI/TaxonMech/issues/65).

### gtdb-pooled-broadmatch-attestation-and-note: Pooled GTDB broadMatch mappings emit the largest pooled cluster's genome total and an inverted mapping-direction note

major / open / confirmed; issue key: cycle3-stage4-gtdb-pooled-broadmatch-attestation-and-note.

On 6,335 pooled-only GTDB records (e.g., NCBITaxon:3121604 data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml, which has 5 pooled skos:broadMatch GTDB mappings led by GTDB:s__JAUMXJ01_sp041781135 with genome_count: 97), src/taxonmech/seed.py (lines 636-650) emits the largest pooled GTDB species cluster's genome count as the taxon's GTDB GENOME attestation (#118), and across 8,587 pooled GTDB records (209,540 rows, including NCBITaxon:562 data/taxa/bacteria/escherichia_coli.yaml and NCBITaxon:3121604 data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml) seed.py lines 522-524 emit a note stating the reverse of kg-microbe's skos:broadMatch direction (#119).

### curation-history-stale-scope-strain-count: SEEDED_FROM_SOURCES curation_history embeds stale static strain counts from curation/seed_scope.tsv reason strings

minor / open / confirmed; issue key: cycle3-stage4-curation-history-stale-scope-strain-count.

In src/taxonmech/seed.py lines 691-702, the SEEDED_FROM_SOURCES curation_history note copies the static reason string from curation/seed_scope.tsv (e.g., '1861 BacDive strains' on NCBITaxon:562 data/taxa/bacteria/escherichia_coli.yaml) even when subtree strain aggregation yields a higher seeded strain_count (1975 on NCBITaxon:562; tracked in https://github.com/CultureBotAI/TaxonMech/issues/69).

### upstream-edge-multiplicity-and-subtree-count-scope: Upstream kg-microbe edge tables for GOLD/MEDIADIVE/MADIN/BACTOTRAITS are not committed locally and direct-only attestation notes require corpus-wide re-seeding

minor / open / confirmed; issue key: cycle3-stage4-upstream-edge-multiplicity-and-subtree-count-scope.

Across docs/structured-review-inventory/part-00.tsv..part-13.tsv, 27,118 records carry verdict pass_with_limitations (e.g., NCBITaxon:1435036, NCBITaxon:562, NCBITaxon:1423, NCBITaxon:287) and 30 carry verdict blocked (e.g., NCBITaxon:209650) because manifest-pinned upstream kg-microbe raw edge tables for GOLD, MEDIADIVE, MADIN, and BACTOTRAITS are not committed locally and src/taxonmech/seed.py (lines 670-688) gathers infraspecific subtree records only for BacDive strains. Although Cycle 1 Stage 6 (PR #152) documented pinned kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd edge-table SHA-256 digests in docs/HARMONIZATION.md, corpus-wide re-seeding of source_attestations[].notes remains deferred (INFRA_TASKS.md taxonmech-infra-0004; https://github.com/CultureBotAI/TaxonMech/issues/8).

### mechanism-and-protein-representation-prerequisites: 626,033 of 626,048 TaxonRecord files remain without causal_graphs or UniProtKB GENE_OR_PROTEIN nodes pending bulk kg-microbe trait-edge extraction and a pinned data/raw/ UniProtKB inventory

major / open / confirmed; issue key: cycle3-stage4-mechanism-and-protein-representation-prerequisites.

Following Cycle 1 Stage 6 (PR #152), Cycle 2 Stages 2-3 and 6 (PRs #155, #156, #160), Cycle 3 Stages 2-3 and 6 (PRs #162, #163, #168), and Cycle 4 Stages 2-3 (PRs #181, #183), 15 TaxonRecord files across Bacteria (7), Archaea (2), and Eukaryota (6) now carry structurally and provenance-validated causal_graphs (161 edges across 33 PMIDs, 51 GENE_OR_PROTEIN nodes across 23 unique live-verified UniProtKB accessions—21 SWISS_PROT and 2 TREMBL—in curation/uniprot_proteins.tsv registered in conf/sources.yaml and validated offline by validate_causal_graph_structure() and validate_causal_graph_proteins()). However, the remaining 626,033 of 626,048 records (including 38,342 additional trait/medium-attested records) still have empty causal_graphs because: (1) data/raw/taxon_trait_edges.tsv has not yet been generated from an upstream local kg-microbe checkout using src/taxonmech/extract.py:extract_taxon_trait_edges (taxonmech-infra-0002); and (2) data/raw/ still lacks a corpus-wide release-pinned UniProtKB / Reference Proteomes TSV snapshot beyond the 23-entry curated reference table (taxonmech-infra-0003; tracked in INFRA_TASKS.md and https://github.com/CultureBotAI/TaxonMech/issues/78).

### structured-inventory-verify-target-sha256-post-curation-drift: scripts/corpus_review_inventory.py --check --verify-target-sha256 reconciles post-curation target SHA-256 digests against newer scientific review bundles without mutating historical shard rows

major / resolved / confirmed; issue key: cycle3-stage4-structured-inventory-verify-target-sha256-post-curation-drift.

Verified in Cycle 4 Stage 4 at 830eb576c1381e73aba1ed284c1ae005c7a5337e that scripts/corpus_review_inventory.py and pytest tests/test_corpus_review_inventory.py (9 passed) reconcile post-curation target_sha256 digests across all 602,165 structured-inventory records (including the 10 structured-shard records curated through Cycle 4 Stages 2-3 in PRs #181 and #183) against the latest scientific review bundles in reviews/structured/ without mutating historical append-only review bundles (resolved in Cycle 2 Stage 5 PR #159 under https://github.com/CultureBotAI/TaxonMech/issues/158).

Disposition: Resolved in Cycle 2 Stage 5 (PR #159) under #158 and verified intact across Cycle 4 Stages 2-3 curation updates and 435 structured review bundles in Cycle 4 Stage 4.

### corpus-review-coverage-doc-stale-bundle-inventory-counts: docs/corpus-review-coverage.md documents multi-stage workflow review bundles in reviews/structured/ and the post-curation target_sha256 reconciliation contract (#158)

minor / resolved / confirmed; issue key: cycle3-stage4-corpus-review-coverage-doc-stale-bundle-inventory-counts.

Verified in Cycle 4 Stage 4 at 830eb576c1381e73aba1ed284c1ae005c7a5337e that docs/corpus-review-coverage.md (Sections 'Shard Architecture And Canonical Bundles' and 'Verification') documents multi-stage workflow scientific review bundles in reviews/structured/ and the load_latest_target_reviews() post-curation target_sha256 reconciliation contract, and that test_corpus_review_coverage_doc_describes_reconciliation_contract() in tests/test_corpus_review_inventory.py passes (resolved in Cycle 3 Stage 5 PR #165 under https://github.com/CultureBotAI/TaxonMech/issues/158).

Disposition: Resolved in Cycle 3 Stage 5 (PR #165) under #158 and verified intact in Cycle 4 Stage 4.

### schema-guide-missing-causal-node-uniprot-protein-slots: docs/SCHEMA.md Mechanism section omits the 9 CausalNode GENE_OR_PROTEIN UniProtKB protein-grounding slots, UniProtEntryStatusEnum, and maintained curation overlay inputs

minor / open / confirmed; issue key: cycle4-stage4-schema-guide-missing-causal-node-uniprot-protein-slots.

In docs/SCHEMA.md (line 20), the Mechanism section table row still states only '&#124; Mechanism &#124; CausalGraph / CausalNode / CausalEdge &#124; Same shape as HabitatMech and TraitMech; every edge requires evidence &#124;' and omits the 9 GENE_OR_PROTEIN UniProtKB protein-grounding slots (organism_taxon_id, strain_id, proteome_id, gene_symbol, locus_tag, sequence_length, sequence_crc64, sequence_version, entry_status) and UniProtEntryStatusEnum (SWISS_PROT, TREMBL) added to src/taxonmech/schema/taxonmech.yaml (lines 1222-1271, 1529-1536) and populated across 51 GENE_OR_PROTEIN nodes in 15 TaxonRecord files via curation/causal_graphs/*.yaml and curation/uniprot_proteins.tsv (tracked under https://github.com/CultureBotAI/TaxonMech/issues/78).

## Recommended Actions And Acceptance Checks

### remediate-seeder-gtdb-and-scope-provenance-cohorts

Gate skos:closeMatch GTDB promotion to EXACT_SYNONYM and xrefs (#124, #63), fix GTDB polyphyly suffix mangling (#65), align pooled GTDB broadMatch genome totals and notes (#118, #119), reconcile seed_scope reason strain counts (#69), and complete direct vs subtree source attestation count notes (#8) across src/taxonmech/seed.py and full-corpus regeneration.

- src/taxonmech/seed.py gates skos:closeMatch exact promotion and preserves GTDB polyphyly suffixes
- Pooled GTDB broadMatch notes and genome counts accurately reflect mapping direction and cluster scope
- Full corpus regenerates cleanly and passes scripts/verify_corpus.py, scripts/validate_strict.py, and scripts/render_pages.py --check

### implement-remaining-mechanism-and-protein-infrastructure-tasks

Execute remaining INFRA_TASKS.md tasks taxonmech-infra-0001..0004 in Cycle 4 Stage 6 to generate data/raw/taxon_trait_edges.tsv from upstream kg-microbe, expand the release-pinned UniProtKB / Reference Proteomes snapshot beyond curation/uniprot_proteins.tsv (#78), and finalize upstream edge-multiplicity provenance (#8).

- Pinned UniProtKB reference proteome inventory validates all 51 GENE_OR_PROTEIN nodes offline
- Granular trait-edge extraction supports reproducible causal_graphs expansion across trait-attested taxa

### update-schema-guide-for-causal-node-uniprot-protein-slots

Update docs/SCHEMA.md in Cycle 4 Stage 5 to document the 9 CausalNode GENE_OR_PROTEIN UniProtKB protein-grounding slots (organism_taxon_id, strain_id, proteome_id, gene_symbol, locus_tag, sequence_length, sequence_crc64, sequence_version, entry_status), UniProtEntryStatusEnum (SWISS_PROT, TREMBL), and the maintained curation/causal_graphs/*.yaml and curation/uniprot_proteins.tsv inputs (#78).

- docs/SCHEMA.md documents all 9 CausalNode GENE_OR_PROTEIN UniProtKB slots and UniProtEntryStatusEnum
- Schema documentation matches src/taxonmech/schema/taxonmech.yaml and curation/causal_graphs/README.md

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| corpus-review-inventories | docs/legacy-review-inventory.tsv; docs/structured-review-inventory/part-00.tsv..part-13.tsv; docs/structured-review-batches.tsv; docs/corpus-review-coverage.md; 23,883 rows in docs/legacy-review-inventory.tsv and 602,165 rows across docs/structured-review-inventory/part-00.tsv..part-13.tsv | supports | Complete per-record review inventories covering all 626,048 TaxonRecord files in data/taxa/ (0 unreviewed, 0 overlap; structured verdicts: pass=479,251, pass_with_limitations=27,118, needs_curation=95,766, blocked=30), with post-curation target_sha256 digests reconciled by load_latest_target_reviews() and documented in docs/corpus-review-coverage.md (#158). |
| exemplar-target-records | data/taxa/bacteria/escherichia_coli.yaml; data/taxa/bacteria/escherichia_coli_k_12.yaml; data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml; data/taxa/bacteria/bacillus_subtilis.yaml; data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml; data/taxa/bacteria/pseudomonas_aeruginosa.yaml; data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml; data/taxa/bacteria/achromobacter_sp_jub104.yaml; data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml; data/taxa/bacteria/acinetobacter_bohemicus.yaml; data/taxa/bacteria/acidicaldus_organivorans.yaml; data/taxa/bacteria/campylobacter_sputorum.yaml; data/taxa/bacteria/acetobacterium_woodii.yaml; data/taxa/archaea/methanocaldococcus_jannaschii.yaml; data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml; data/taxa/archaea/saccharolobus_solfataricus.yaml; data/taxa/eukaryota/saccharomyces_cerevisiae.yaml; data/taxa/eukaryota/cryptococcus_neoformans.yaml; data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml; data/taxa/eukaryota/cryptococcus_deneoformans.yaml; data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml; data/taxa/eukaryota/cryptococcus_deuterogattii.yaml; data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml; data/taxa/eukaryota/acanthamoeba_castellanii.yaml; data/taxa/other/uncultured_organism.yaml; data/taxa/other/human_gut_metagenome.yaml; data/taxa/other/unidentified.yaml; Complete YAML content of 27 directly bound cross-domain, verdict-stratified, and causal-graph-enriched TaxonRecord files | supports | Verified taxon identity, lineage, nomenclature, synonyms, xrefs, taxonomy_mappings, source_attestations, strains, causal_graphs, and curation_history across 27 exemplar records spanning Bacteria (13), Archaea (3), Eukaryota (8), and other (3). |
| cycle4-causal-graph-and-uniprot-overlays | curation/causal_graphs/README.md; curation/causal_graphs/NCBITaxon_*.yaml; curation/uniprot_proteins.tsv; reviews/structured/20261025T232500Z-cycle4-stage2-causal-graphs-curation/review.yaml; reviews/structured/20261026T034000Z-cycle4-stage3-protein-examples/review.yaml; 15 maintained curation/causal_graphs/NCBITaxon_*.yaml overlays, curation/uniprot_proteins.tsv (23 rows), and Cycle 4 Stages 2-3 structured review bundles | supports | Verified 15 maintained causal-graph overlays seeded into 7 species and 8 strain TaxonRecord files (161 evidence-backed edges across 33 PMIDs; 51 GENE_OR_PROTEIN nodes grounded to 23 unique live-verified UniProtKB accessions—21 SWISS_PROT and 2 TREMBL—in curation/uniprot_proteins.tsv with exact organism_taxon_id, strain_id, proteome_id, gene_symbol, locus_tag, sequence_length, sequence_crc64, sequence_version, and entry_status). |
| raw-source-inventories | curation/seed_scope.tsv; data/raw/MANIFEST.yaml; data/raw/ncbitaxon_taxa.tsv; data/raw/gtdb_mappings.tsv; data/raw/gtdb_species.tsv; data/raw/bacdive_strains.tsv; data/raw/lpsn_names.tsv; curation/seed_scope.tsv (626,048 rows) and data/raw/*.tsv | supports | Pinned raw inventories verify exact NCBI taxon IDs and lineages across all 626,048 records and confirm persistent GTDB closeMatch fan-out (95,766 records), polyphyly suffix mangling (15,704 rows), pooled broadMatch genome counts/notes (8,587 records), and stale seed_scope strain-count reason strings. |
| schema-seeder-validator-code | src/taxonmech/schema/taxonmech.yaml; src/taxonmech/seed.py; src/taxonmech/extract.py; scripts/validate_strict.py; scripts/check_provenance.py; scripts/corpus_review_inventory.py; scripts/validate_history.py; docs/SCHEMA.md; docs/HARMONIZATION.md; docs/corpus-review-coverage.md; INFRA_TASKS.md; taxonmech.yaml:43-95,1200-1315,1520-1575; seed.py:216-430,508-535,636-715; validate_strict.py:217-370; check_provenance.py:1-140; corpus_review_inventory.py:185-330,381-445; docs/SCHEMA.md:1-38; INFRA_TASKS.md:33-340 | supports | Inspection of schema, seeder, extractor, strict/UniProt/provenance validators, inventory checker, and documentation confirms resolution of #76 and #83 in Cycle 1 Stage 5, resolution of #158 code in Cycle 2 Stage 5 (PR #159) and #158 documentation/regression test in Cycle 3 Stage 5 (PR #165), structural causal-graph and strain_id validation plus conf/sources.yaml registration in Cycle 3 Stage 6 (PR #168), persistent GTDB/scope seeder defects at src/taxonmech/seed.py lines 508-535, 636-650, and 691-702 (#124, #63, #65, #118, #119, #69), remaining corpus-wide trait/UniProt/attestation-note tasks in INFRA_TASKS.md (taxonmech-infra-0001..0004; #78, #8), and omission of the 9 GENE_OR_PROTEIN UniProtKB slots and UniProtEntryStatusEnum from docs/SCHEMA.md line 20 (#78). |

## Limits And Additional Notes

- Per-record review rows for all 626,048 in-scope TaxonRecord files are stored in docs/legacy-review-inventory.tsv (23,883 records) and docs/structured-review-inventory/part-00.tsv..part-13.tsv (602,165 records), with post-curation target_sha256 reconciliation verified via tests/test_corpus_review_inventory.py (#158); full-corpus 626,048-file hash/reproduction sweeps were not re-run during this pass due to host TCP/process pressure and remain enforced by CI quality gates.
- Four src/taxonmech/seed.py findings (#124/#63, #65, #118/#119, #69) remain open for Stage 5 disposition because scripts/verify_corpus.py enforces zero byte-for-byte drift between src/taxonmech/seed.py and all 626,048 committed YAML files in data/taxa/, requiring a dedicated full-corpus YAML and pages/taxon-details/*.json.gz regeneration pass.
- Two findings (#8, #78) remain gated on upstream infrastructure tasks in INFRA_TASKS.md (taxonmech-infra-0001..0004) pending bulk kg-microbe trait-edge extraction, a corpus-wide release-pinned UniProtKB snapshot, and direct-vs-subtree attestation count alignment.
- Cycle 4 Stage 4 re-verified all 4 previously resolved findings (#76, #83, and both #158 code and documentation/test findings), carried forward 6 open corpus-regeneration and infrastructure-gated findings (#124/#63, #65, #118/#119, #69, #8, #78), and identified 1 new open schema-documentation finding (schema-guide-missing-causal-node-uniprot-protein-slots under #78) for Cycle 4 Stage 5 grouped remediation.
- All 15 causal-graph-enriched TaxonRecord files curated through Cycle 4 Stages 2-3 (PRs #181, #183; 161 edges across 33 PMIDs, 51 GENE_OR_PROTEIN nodes across 23 live-verified UniProtKB accessions in curation/uniprot_proteins.tsv) are directly bound in targets with their current SHA-256 digests.
- Parent workflow Cycle 4 Stage 4 evidence manifest saved at reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/evidence.yaml.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T075300Z-cycle4-stage4-corpus-record-review
kind: batch
repository: CultureBotAI/TaxonMech
title: Cycle 4 Stage 4 full-corpus TaxonRecord and cohort review across 626,048 in-scope
  taxa and 15 causal-graph/UniProtKB-enriched records (161 edges, 51 GENE_OR_PROTEIN
  nodes across 23 UniProtKB accessions)
started_at: '2026-10-31T07:45:00Z'
finished_at: '2026-10-31T07:53:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: independent
  independence_basis: 'Cycle 4 Stage 4 record_review worker; audited all 626,048 in-scope
    TaxonRecord files across docs/legacy-review-inventory.tsv (23,883) and docs/structured-review-inventory/part-00.tsv..part-13.tsv
    (602,165), verified all 27 cross-domain and causal-graph/UniProtKB exemplar TaxonRecord
    files after Cycle 3 Stage 6 (#168) and Cycle 4 Stages 2-3 (#181, #183), and inspected
    all 434 prior structured review bundles in reviews/structured/ prior to judgment.'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Executed the Cycle 4 Stage 4 (record_review) full-corpus and cohort review
  across all 626,048 eligible TaxonRecord YAML files in data/taxa/ (Bacteria: 605,695;
  Archaea: 14,013; Eukaryota: 6,331; other: 9) reconciled against docs/legacy-review-inventory.tsv
  (23,883 records) and docs/structured-review-inventory/part-00.tsv..part-13.tsv (602,165
  records across 14 shards and 611 batches; 0 unreviewed; 0 overlap), plus all 15
  TaxonRecord files enriched through Cycle 4 Stages 2-3 (PRs #181, #183) with maintained
  causal_graphs (161 evidence-backed edges across 33 PMIDs) and live-verified + offline-validated
  UniProtKB GENE_OR_PROTEIN nodes (51 nodes across 23 unique accessions: 21 SWISS_PROT
  and 2 TREMBL in curation/uniprot_proteins.tsv) and structural/provenance validators
  added in Cycle 3 Stage 6 (PR #168). Verified 4 resolved findings (#76, #83, and
  both #158 code and documentation/test findings), carried forward 6 open corpus-regeneration
  and upstream-prerequisite findings (#124/#63, #65, #118/#119, #69, #8, #78), and
  recorded 1 new open schema-documentation finding (schema-guide-missing-causal-node-uniprot-protein-slots
  under #78, where docs/SCHEMA.md omits the 9 GENE_OR_PROTEIN UniProtKB protein-grounding
  slots and UniProtEntryStatusEnum added to src/taxonmech/schema/taxonmech.yaml) for
  Cycle 4 Stage 5 grouped remediation.'
source:
  git_revision: 830eb576c1381e73aba1ed284c1ae005c7a5337e
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
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 8e8fd97c64fbff27e023c7a768b4c806c98f56cd6571e7102217a2c833284df6
    role: context
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: b914ed8c6aff170e57bea1b02f94b67f058778019ff3000d44db6ec578ba9684
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 4c7090b9d7fd0c6f7f2b4e47b48cbf64835e8d27b44944649e1ccd9038ce462d
    role: context
  - path: .claude/skills/taxonmech-evolve-workflow/SKILL.md
    sha256: 387b5369e45fe51a1c97a01297fd21133ac354d1561c734d97d5837c8b23afc8
    role: context
  - path: AGENTS.md
    sha256: f47526b17cdb04305ce32cb1da1488b684b8f50a65458116e5013fc0b4b2a248
    role: context
  - path: INFRA_TASKS.md
    sha256: 8521a0f783afd2fc432ed972b2399c72acef2187a9cf615e303f28b9f0a12714
    role: context
  - path: README.md
    sha256: 9bbb0f88d3d27767532fafe2d1f43c8dc68443a551d0ff2c5ceca75a5ddb69f7
    role: context
  - path: conf/id_label_targets.yaml
    sha256: efed4c6d9cc218c9d89ba4468e361761ac02ff535e2669de33af6606202e544c
    role: context
  - path: conf/ncbi_taxdump.yaml
    sha256: 1d734bbb3ebf9d36e304d8030c5852fa4f0f306fca2849be5dec8f3dff86f887
    role: context
  - path: conf/record_review.yaml
    sha256: 366312506b771fc18fc5bfc30d5ec942b2c96212e1f4f95c463cfa1707fbebaa
    role: context
  - path: conf/sources.yaml
    sha256: 464f895ed81d2fee7dff68906bf609c86bf13fc43a5b806ee6f413b4cd02d9ca
    role: context
  - path: curation/causal_graphs/NCBITaxon_1423.yaml
    sha256: 540265807d5adb65263d8d389c33102a28e63eb7996f5452e4fa5c0be0c76d98
    role: context
  - path: curation/causal_graphs/NCBITaxon_1859096.yaml
    sha256: 0f29a0916110b21224537ec5e337a9e8fa5a61c3a9c3f04885f421e7974d8746
    role: context
  - path: curation/causal_graphs/NCBITaxon_208964.yaml
    sha256: 21e15bcb715fb781d21318949ac303ceb7b98459485aee88e0f9d11081015f45
    role: context
  - path: curation/causal_graphs/NCBITaxon_2190.yaml
    sha256: e6da8dc155fef28501dff2dbf6c77a1e3f444b8f09ee8b7389ada3321b121cad
    role: context
  - path: curation/causal_graphs/NCBITaxon_224308.yaml
    sha256: ee9e9dd62295bbc165b4ace271cf4536257acd8a76b062b83d6f2f8cf76c5e77
    role: context
  - path: curation/causal_graphs/NCBITaxon_235443.yaml
    sha256: ec52ee753d46d6853cf12301d835d8282f2c9f7aefae2d24a3784bfa11ecc98f
    role: context
  - path: curation/causal_graphs/NCBITaxon_243232.yaml
    sha256: f6bc7a819cd3b2a959831babc8d87bf418927f813ab282751997de086d7a998c
    role: context
  - path: curation/causal_graphs/NCBITaxon_283643.yaml
    sha256: 3098281e6de9a4dccdcf51f3c7a8db7f47c4c3dfadb333682957c4e331f35caf
    role: context
  - path: curation/causal_graphs/NCBITaxon_287.yaml
    sha256: a0c36afd6c9a2bb2a6d9b801413a9713aba598208d7f3164845157dcc7591f9b
    role: context
  - path: curation/causal_graphs/NCBITaxon_294750.yaml
    sha256: 3ec5ba3c0784bbda20a3df13863c7faf96fb21562e01394fa0e69ec9f3f2215e
    role: context
  - path: curation/causal_graphs/NCBITaxon_40410.yaml
    sha256: 425d1eece60fd72e9c552eee49e2af7543b9b278b2555f0c0b991c537d85c3cc
    role: context
  - path: curation/causal_graphs/NCBITaxon_511145.yaml
    sha256: 9524d4da89f99a153ee8b2da73e3817be53971e56a5244631581c3ef89cf91f9
    role: context
  - path: curation/causal_graphs/NCBITaxon_5207.yaml
    sha256: 68f853b2ae303a76b4787f5d6483e2750c338808d8fbca6599cae7d8b5266434
    role: context
  - path: curation/causal_graphs/NCBITaxon_562.yaml
    sha256: 6ed0e2068cf8f74cfe67064f30ad53d7958fc31838725adfb8cd3956a5e0a4e2
    role: context
  - path: curation/causal_graphs/NCBITaxon_83333.yaml
    sha256: 4663e83b0012b3bc2a0349f72b759eabacb8c94a3435117228f0f469f36c9add
    role: context
  - path: curation/causal_graphs/README.md
    sha256: 502e6f946de1a9f94851e2dc5b7f83fd88b58f86687948d069d0785b6a8f143e
    role: context
  - path: curation/seed_scope.tsv
    sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
    role: context
  - path: curation/uniprot_proteins.tsv
    sha256: d03af7aa19849eac678466f8e02030c8910db7b6f247740e842e1cea26d1224c
    role: context
  - path: data/atb/MANIFEST.yaml
    sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
    role: context
  - path: data/raw/bacdive_strains.tsv
    sha256: 029fd6d1f53ef7f90684130bf0d644ed3edd1d8fbeb065a511ae928f160b1eea
    role: context
  - path: data/raw/bactotraits_taxa.tsv
    sha256: 976d109cef832d8bf27cc105f67a42efbe900b6946736298602ef6d11158b197
    role: context
  - path: data/raw/culture_collection_strains.tsv
    sha256: 810fdcb16abd6330fb15bb03d4c74b18db86be36a7c599df7c6b2498d9735c95
    role: context
  - path: data/raw/dropped.tsv
    sha256: b0d5dfe91ebaf762249beceef51c5136291f9bfcb08ffa5098bd6510bb1a7401
    role: context
  - path: data/raw/gold_organisms.tsv
    sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
    role: context
  - path: data/raw/gtdb_mappings.tsv
    sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
    role: context
  - path: data/raw/gtdb_species.tsv
    sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
    role: context
  - path: data/raw/lpsn_names.tsv
    sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
    role: context
  - path: data/raw/madin_taxa.tsv
    sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
    role: context
  - path: data/raw/mediadive_taxa.tsv
    sha256: 3f74b78cadfcdb6aeae953e09fdb39e34fd9c5d5ed0be65a04a5d7fb02355905
    role: context
  - path: data/raw/ncbi_merged_ids.tsv
    sha256: 316bd4830713573cc6fe931a21a4c78f4c5159575550e71b5fd843c82a9211d9
    role: context
  - path: data/raw/ncbi_type_material.tsv
    sha256: 38f1de7d1ae173620b54849b0ab81d7219763a4395984e9a1057cce47f574f69
    role: context
  - path: data/raw/ncbitaxon_taxa.tsv
    sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
    role: context
  - path: data/raw/strain_assemblies.tsv
    sha256: 71344b934db3081bfcac9562a0bd1fd8fddcfdabb8af60e208ca09035e818315
    role: context
  - path: data/raw/strain_genome_records.tsv
    sha256: 47ed80be55660aad4bd82d37d889ea60f8686cec1aeeccf72e5af22bf43728ab
    role: context
  - path: data/raw/strain_related_records.tsv
    sha256: c33a9bf4c6b94dc6971f1c0d46565092c37ba7c2d462a6bc9c20ccbf58fb9c56
    role: context
  - path: data/straininfo/MANIFEST.yaml
    sha256: 25dd601c8cf6d4d84e5cc756d1e642ebef89f565bd31967152bf0026fa072847
    role: context
  - path: data/taxa/PATHS.tsv
    sha256: f8f2e0721cb6839b30530b44be0d3004b9f0e6e2d4be8736f235b10117a8bd99
    role: context
  - path: data/taxa/archaea/methanocaldococcus_jannaschii.yaml
    sha256: c0993ec09bd36355e95752af9bb46d1e7ad64d05f10f14483dc465bf23aea800
    role: target
  - path: data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml
    sha256: e0b817a61289da32ec9471a9ad1449ae3ed857fe8b17b48e6442b96d8586f642
    role: target
  - path: data/taxa/archaea/saccharolobus_solfataricus.yaml
    sha256: 0666c680a892bb6a4d694c13afe53db1b56545e9dc8a0d81e27a028a95f1d6fb
    role: target
  - path: data/taxa/bacteria/acetobacterium_woodii.yaml
    sha256: 5230db65344dd60acf05b122b63bfe2f83f478d039f221bf4d7968b7db1ebd39
    role: target
  - path: data/taxa/bacteria/achromobacter_sp_jub104.yaml
    sha256: 26b632ebff370ddd07acf50d8cd595d08963dccd08fa5951ec8f2a7c3f93977d
    role: target
  - path: data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml
    sha256: 596bbf35eaf448bccd4dd1042ee2212994a723371c01ac7c93dc0a629c45a307
    role: target
  - path: data/taxa/bacteria/acidicaldus_organivorans.yaml
    sha256: 3d8f207bb388f7fd41ae1e2315d6ebbf3f938f99a209705a34722d8d31c49977
    role: target
  - path: data/taxa/bacteria/acinetobacter_bohemicus.yaml
    sha256: ce1aed420886f258c1a6277f3cac55271171b96bf235e9630642d6f377168a0b
    role: target
  - path: data/taxa/bacteria/bacillus_subtilis.yaml
    sha256: 9e69464f60a6dcac18e022aeefd58aed33e42fdef3dd45e77a95ca332e3df6f7
    role: target
  - path: data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml
    sha256: 6124732435a45e18cf091ccd680c7f3454dc88dca39c869884d83bac2e11c9f9
    role: target
  - path: data/taxa/bacteria/campylobacter_sputorum.yaml
    sha256: d36195dc394fa4c68dd65292205411c4cd1fbc710f6e4e6e0bd4379c39e53847
    role: target
  - path: data/taxa/bacteria/escherichia_coli.yaml
    sha256: f6680054018c9d13d190bf7e9f3fe49b1521915f90f95280d464d7ca49d73e6b
    role: target
  - path: data/taxa/bacteria/escherichia_coli_k_12.yaml
    sha256: 4e5d384510a49345db9585ea41c23b301d993790298abcbea1fc3036d119e27a
    role: target
  - path: data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml
    sha256: e8a46560a85d5b64733534eeb249342be227e24f9ceefc667012f96bbed91938
    role: target
  - path: data/taxa/bacteria/pseudomonas_aeruginosa.yaml
    sha256: 32b18b290be7b848b4eab0e5a8efc098a18d9ed6e27e59f89bb9acf2d1f40263
    role: target
  - path: data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml
    sha256: 7232f3561985f8be4d9b4c386d1d0794afd1aad800ee9186e7a7a18e5808b15b
    role: target
  - path: data/taxa/eukaryota/acanthamoeba_castellanii.yaml
    sha256: 969e4e46219d0635b36eca944bc6fe814538743b17ae1923a2b7eed1b6870144
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
    sha256: 79167fec32d972d251da73e4026ea30ce59fc99e4dfc5b8aafb817ddcec87553
    role: target
  - path: data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml
    sha256: 317b57c85586bdde85979f6d86297b757a92fbcac6c0c4b8e183a785bf7b177f
    role: target
  - path: data/taxa/eukaryota/saccharomyces_cerevisiae.yaml
    sha256: 891830d3ddc3ab0ac0dcbf6242cee26677c6a18642c2d604f66ad1e52e2d5121
    role: target
  - path: data/taxa/other/human_gut_metagenome.yaml
    sha256: 1cdc36b868637c79dff9dcbc8c6e55cb337eebb40a8d5cad04eaf6cccdae7667
    role: target
  - path: data/taxa/other/uncultured_organism.yaml
    sha256: b781c4f60613c01b9e030395c28add69d1d84baf5073b68ae7c1bfaf25e57a67
    role: target
  - path: data/taxa/other/unidentified.yaml
    sha256: a4118112c10a22dcac04995abb8f2d161a3ff51c0a67816ac0188ed610b7e1b6
    role: target
  - path: docs/ALLTHEBACTERIA.md
    sha256: a1b0c298988782ad4b7dbb80c661c483a67cd0e478366eddbea7d1ba7595e7cd
    role: context
  - path: docs/CURATION.md
    sha256: 9e09c97bcd617f2b3d0090f775b80565fccc9d00e4c398ed58d3a31192a8fa8e
    role: context
  - path: docs/HARMONIZATION.md
    sha256: d18209d892f4b0e04cac422d626dd4fe0e48f44ca6d1b6a973fae8d2704ee3ec
    role: context
  - path: docs/SCHEMA.md
    sha256: 9e767cebb2506f8372c65ceb5f75e5ef2df2b23c2be3727cfd198f447a6a0e30
    role: context
  - path: docs/SOURCE_COVERAGE.md
    sha256: 43f17c3c80815d395136aab53f310be3190a8d614a45fc2f4a3942faeb0bc9e9
    role: context
  - path: docs/STRAININFO.md
    sha256: 65d274e7126fcf7810da746366b0e60c1957f05df9016fb0900600932b278241
    role: context
  - path: docs/STRAIN_GENOMES.md
    sha256: 7cfdbc8a600173d6569f885b409b1543098bb6022e8764324d91879eaed2b597
    role: context
  - path: docs/corpus-review-coverage.md
    sha256: bca3a0ed8315abff8ec9f61f4258d3398b64b3941e9f61ea5b236d77122f8a1f
    role: context
  - path: docs/legacy-review-inventory.tsv
    sha256: 275df7f9fdbef59d1e53428f4a211079bb443a32b30d23accbd67111c82d2404
    role: context
  - path: docs/record-review-profile.md
    sha256: bc2074242edcf09f510aae8d9cf40961ea0c1155ca497808765bdabfb35ee721
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: docs/structured-review-batches.tsv
    sha256: 023ac83c94ea72c7822acb3b111e5dddb41b1df8304f5b7ec4146883557ebce4
    role: context
  - path: docs/structured-review-inventory/part-00.tsv
    sha256: 8f949dcf5099669bba825f91d035731ffeead061c26c85066a94a07cad629c7c
    role: context
  - path: docs/structured-review-inventory/part-01.tsv
    sha256: 4178baeacc58f185d684eb52f80dfdfc149e96b4b0b4f6cefbc321153cf93787
    role: context
  - path: docs/structured-review-inventory/part-02.tsv
    sha256: 4255d240d3a26e7ad5f988b9ec81596073be5b6712f72f4cf58618cf1eef2135
    role: context
  - path: docs/structured-review-inventory/part-03.tsv
    sha256: 08ba38cb926c3c393f59ab3d48bf3d5b9baf5d7c4aa6ceebd959fb0c3d83e4b3
    role: context
  - path: docs/structured-review-inventory/part-04.tsv
    sha256: 979e1b6195108545e859c29e7c98484ccb1a84c64fc9527dbf282651077125ac
    role: context
  - path: docs/structured-review-inventory/part-05.tsv
    sha256: 67aeb11f448d913d1e2e3886c4bbdda62626fe5724afe162f9c130c3dd7076d7
    role: context
  - path: docs/structured-review-inventory/part-06.tsv
    sha256: 29e0020e9c24681e701335d57b90dc4bc1783e6d4b10dceea1736d493efbe3dc
    role: context
  - path: docs/structured-review-inventory/part-07.tsv
    sha256: 31684cf3703b4093bc4ab048c5fb16190b75ff1fa322f792e034a9340d0977e7
    role: context
  - path: docs/structured-review-inventory/part-08.tsv
    sha256: b258608d4118fc5f9a446060599f22bcc2308622b2da755d4e3da5b3f79974f1
    role: context
  - path: docs/structured-review-inventory/part-09.tsv
    sha256: 16dabe1cbb6af3e5d33bda083e2e6767fa477818dc6316927d15ba7f910d408e
    role: context
  - path: docs/structured-review-inventory/part-10.tsv
    sha256: 2a9bfec777a396f85c01de48fc2bf2ba542eb7fe56fd2bfb27e483e3597cdbb2
    role: context
  - path: docs/structured-review-inventory/part-11.tsv
    sha256: 9667b45e5fa9a6c0cde0a8ffbfbd6856b2d101aff2aeda7d70a13601e923125a
    role: context
  - path: docs/structured-review-inventory/part-12.tsv
    sha256: 135d2cc3ad778d73a67aea9eb1d4a696a195589ea721cc815b9151c8935742f0
    role: context
  - path: docs/structured-review-inventory/part-13.tsv
    sha256: 944a7bd4e7809a8bd71c8e0d9aa1b46f2625c267b7d922bf06d2a5dee8c275de
    role: context
  - path: reviews/structured/20261018T080549Z-structured-review-shard-part-00/review.yaml
    sha256: b0955608fbc45a75a6b27ace8714647ea12978fda24673b30b417a3811dcf10d
    role: context
  - path: reviews/structured/20261018T080549Z-structured-review-shard-part-01/review.yaml
    sha256: c6a4f1841d17e7b85c47514a31d9f9a144c761f64c5d1f4d5259981b7af01a4f
    role: context
  - path: reviews/structured/20261018T080549Z-structured-review-shard-part-02/review.yaml
    sha256: 447013dc9934b823bd8ddffa4e84c7e35a36427685fcf0f2497aa573f56d9a5b
    role: context
  - path: reviews/structured/20261018T080549Z-structured-review-shard-part-03/review.yaml
    sha256: ae62f7bd7318dc6e189cd7ba1b5aab0a080f0c26358d40e6743e25a90d7e0890
    role: context
  - path: reviews/structured/20261018T080549Z-structured-review-shard-part-04/review.yaml
    sha256: c314ee94ecfdcb4798ffb38bd9e1e733d14fa2f6585d291469b6ae168f183a8a
    role: context
  - path: reviews/structured/20261018T080549Z-structured-review-shard-part-05/review.yaml
    sha256: c58d03d92aaaa2fd1409471243525f1894bc4bffa12c7db7effd283be048aa7e
    role: context
  - path: reviews/structured/20261018T080549Z-structured-review-shard-part-06/review.yaml
    sha256: 690cff513e6f21df1327e25db6e46ae0bf1a7e97988000465b074edba0136cbc
    role: context
  - path: reviews/structured/20261018T080549Z-structured-review-shard-part-07/review.yaml
    sha256: b4a87e3f831e816f031c1623de6fcf62b2f4ad2321a633926cb5a7144fd028a6
    role: context
  - path: reviews/structured/20261018T080549Z-structured-review-shard-part-08/review.yaml
    sha256: f84c74e6a5f49ec4392b45870f02e801a2f8d80ecc64057c8058cfde32f084a6
    role: context
  - path: reviews/structured/20261018T080549Z-structured-review-shard-part-09/review.yaml
    sha256: 5fa7926db598d6922b9daf75f5ea87c2ced9cf671686873660346a6a02f6d0af
    role: context
  - path: reviews/structured/20261018T080549Z-structured-review-shard-part-10/review.yaml
    sha256: 422cde8afeebf4b840b817c7fdf2788e322f1a80591591b17e703cf4109ea993
    role: context
  - path: reviews/structured/20261018T080549Z-structured-review-shard-part-11/review.yaml
    sha256: 548610609ee6427b8b3043b2bd9225603ec50d473f56824ee6392f52d15d1b15
    role: context
  - path: reviews/structured/20261018T080549Z-structured-review-shard-part-12/review.yaml
    sha256: b998eba7f0a743540ae0777a3def845d1ac36a2812f9b1752d5e6e852d3b47e4
    role: context
  - path: reviews/structured/20261019T052200Z-structured-review-shard-part-13/review.yaml
    sha256: 79fc333f064e7f46742d1b186c3f1f04b69aa5199181fac72f430998f6e2a16c
    role: context
  - path: reviews/structured/20261021T043201Z-stage2-causal-graphs-assessment/review.yaml
    sha256: e64b410aa540af8c73bba692ef466f86da130efb697789382da6a88756b9d2d1
    role: context
  - path: reviews/structured/20261021T094500Z-stage3-protein-examples-assessment/review.yaml
    sha256: 8e34dc97dcbc49098890e69e4b270e44d80eac4cc562820fb5f4035c33c94552
    role: context
  - path: reviews/structured/20261021T163800Z-stage4-corpus-record-review/review.yaml
    sha256: dffeef8bb90f373e6f5e07eeb00eb004db9959bb363afe50a0dabf641a6e1c73
    role: context
  - path: reviews/structured/20261022T012228Z-stage5-remediation-review/review.yaml
    sha256: 03b115f58a186b6a5d8c66d4b8674ef98c08c33060973bb6f0e9f6ca31f46297
    role: context
  - path: reviews/structured/20261022T141500Z-cycle2-stage2-causal-graphs-curation/review.yaml
    sha256: 2ce928e84e482b2157d142b4a8b5705c27d44614ba847ef3a2f93bd6495920df
    role: context
  - path: reviews/structured/20261022T190800Z-cycle2-stage3-uniprot-protein-examples/review.yaml
    sha256: 59953c982d1e92acf785dd8372a7dc46e83520cf71c1cce53dd205847f54b9df
    role: context
  - path: reviews/structured/20261023T073200Z-cycle2-stage4-corpus-record-review/review.yaml
    sha256: 9e2dca9e61630c11ba99a43b54e3b880bc86db36e7a523d828beea5f2a01669a
    role: context
  - path: reviews/structured/20261023T110500Z-cycle2-stage5-remediation-review/review.yaml
    sha256: 0a85994963f42e44008c492ae5125554794372bbfd3699f18f65292f84f20035
    role: context
  - path: reviews/structured/20261023T193500Z-cycle3-stage2-causal-graphs-curation/review.yaml
    sha256: 73d78daf5e719b3e0a611165675a32c33d4d61379590086b34d1485cbe499c15
    role: context
  - path: reviews/structured/20261023T224500Z-cycle3-stage3-protein-examples/review.yaml
    sha256: 7390287e69e64500a83482da9739f503fc1c96fb21e8e47c0419218125646959
    role: context
  - path: reviews/structured/20261024T021500Z-cycle3-stage4-corpus-record-review/review.yaml
    sha256: cb1ccb504a32420345b96eda530e18340047254b3ceba85bf62ca79a92f21013
    role: context
  - path: reviews/structured/20261024T055500Z-cycle3-stage5-remediation-review/review.yaml
    sha256: 3d224b63630b1563c0eea81f48c5dfead6ead47f6a635b093ee945e689be58a2
    role: context
  - path: reviews/structured/20261025T062915Z-historical-review-metadata-batches-0014-0051/review.yaml
    sha256: 54b705c7ed643dcd45c61f9764cedef56e0b81e9dc28f2be70d07982deb8ec41
    role: context
  - path: reviews/structured/20261025T232500Z-cycle4-stage2-causal-graphs-curation/review.yaml
    sha256: 68414fafffa12b3064a7d83b959664981ec27eafac3110db83e81f69f6145596
    role: context
  - path: reviews/structured/20261026T034000Z-cycle4-stage3-protein-examples/review.yaml
    sha256: 5a2aad69ea22951b0bfc248d995ba2bc9713fc06e5bba0d6a1fb4b6db71e8dbe
    role: context
  - path: reviews/workflow/latest.yaml
    sha256: c9b0d66fed7bf7f261e76bab2d1e6c2739d346cf437482f1d28d04942dcfb994
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml
    sha256: 4d5428357f5317ef1faad82e61541ba4496e5ba417423473094a2da677ba062b
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-05/revision-0001/evidence.yaml
    sha256: 9cb21f3aea37f71bef99929badad120b34a52356b30d0821b6330c29e4b0ed95
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0002/evidence.yaml
    sha256: 9de2199c1200db86b7ba82a2d1f3221370b32daef98a009d8871918bad7e9494
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/evidence.yaml
    sha256: 8caefcb86991394e4afaccf9a2eab3da631814df4309f4b68b8b0dffcb4400a3
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml
    sha256: d433bc519d9f52a03cc317c0629e341142e0ce1be71b7a36a44b3baa78103b77
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/evidence.yaml
    sha256: 4e40659113e0e1e16e11e1ea97a4b0f3ae5ac886947b9909adf6483cfa239b1d
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-04/revision-0001/evidence.yaml
    sha256: 61289baeabe1ab7d9479903ef6fad54c27bd820d4ddfbacd06e2599fcda9cce9
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-05/revision-0001/evidence.yaml
    sha256: 120eb31292da8f565ec0a049c53ec40ddb27e49e92c2d07cb746c9cae1dffbcc
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/evidence.yaml
    sha256: 6b1bd2dde1e7edfc11f6eb19fe0708a6e016529cd49c6ffb1bc3d728e90adb87
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/check_provenance.py
    sha256: 72083ea4c6935f58fb455c20429e373d21c8727f862134636e9fb26fdd003646
    role: context
  - path: scripts/corpus_review_inventory.py
    sha256: 1985bbaccb1c451e1f9adc6f74479f15e968e9524914189cbc118d02ebf8fe9d
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/render_pages.py
    sha256: de2984d4c5479778e83f9d1a6fb9ba67f8fbd27d42537fbe2b5151f60f1c0342
    role: context
  - path: scripts/run_qc.py
    sha256: d3a8e398b0484fef1ce4ae13e639a03dd41467c1d597d753132e4dba04df9da3
    role: context
  - path: scripts/validate_history.py
    sha256: 4c66a472e4540d107a36cd0665ff8c2d140edab65935f0ea30735a6e2204b945
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
  - path: src/taxonmech/ncbi_taxdump.py
    sha256: 83e3bfd53721a1f85291022511de6504d84caa58e899c0fd8d1797e9f00f67cf
    role: context
  - path: src/taxonmech/report.py
    sha256: 18475a2415154589e79fa9153bd5f97801d300a2abe77f0186d41c058f9979ee
    role: context
  - path: src/taxonmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/taxonmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/taxonmech/schema/taxonmech.yaml
    sha256: 60747327658d0e2560ac9e58fb6e9a19cf711266300f1eff8b5c64e2917020ad
    role: context
  - path: src/taxonmech/seed.py
    sha256: 57f375e3d289e4f16ae71340cbd75e0b836d28e6e9c90fbf4fd9a6756be6b4dc
    role: context
  - path: src/taxonmech/templates/base.html
    sha256: 91405ee9a3d8534c95253812be5f1ad8716a335d1a8795f2527f1b076cca0f35
    role: context
  - path: src/taxonmech/templates/index.html
    sha256: ba9e387ebe4953ce9ae1064336bd2dd7c89ce4fe41ac490f077f48ba982b6687
    role: context
  - path: src/taxonmech/templates/taxon-content.html
    sha256: 9562204e103755b648b32234cf001253e855a64bb46f5de1eb372b5fcf7ad3a2
    role: context
  - path: src/taxonmech/templates/taxon.html
    sha256: 7df5b22500adefcb89363c23a6b74ccd0da4fa34a1f73f2997758099cf3253df
    role: context
  - path: tests/test_causal_graph_overlays.py
    sha256: e2e5f0ea2ccf23fe39a8976ba471d58d8b8945e17fdfc1c9c34e1f3499bfc37a
    role: context
  - path: tests/test_corpus_review_inventory.py
    sha256: fc566c84005c7b56719ab3d7ec4e127f0fc902d0a3dba8f3d44f06e2c382da11
    role: context
  - path: workflow/mech-workflow.yaml
    sha256: d1d4a9dc05f4d048381106ef4f463cdda0a0666d1021f273aa948b2fc8c5773b
    role: context
  - path: workflow/parent/workflow.yaml
    sha256: 66194b3aba4540e9ee7adf91bc1fd7fb597aede130ef1603031a92002152e1d8
    role: context
scope:
  description: Frozen 626,048-record TaxonMech corpus across data/taxa/bacteria/ (605,695),
    data/taxa/archaea/ (14,013), data/taxa/eukaryota/ (6,331), and data/taxa/other/
    (9), reconciled against docs/legacy-review-inventory.tsv (23,883 records) and
    docs/structured-review-inventory/part-00.tsv..part-13.tsv (602,165 records) with
    27 representative cross-domain, verdict-stratified, and causal-graph-enriched
    TaxonRecord files bound directly.
  selection: All 626,048 in-scope TaxonRecord files in curation/seed_scope.tsv and
    data/taxa/PATHS.tsv reconciled against the frozen review inventories, plus 27
    directly bound representative records spanning Bacteria (13), Archaea (3), Eukaryota
    (8), and other (3) across pass, pass_with_limitations, needs_curation, blocked,
    and Cycle 2-4 causal-graph/UniProtKB cohorts.
  coverage: sampled
  population_size: 626048
  sampling_method: Complete 626,048-record inventory census via scripts/corpus_review_inventory.py
    --check (23,883 legacy + 602,165 structured across 14 shards and 611 batches;
    0 unreviewed; 0 overlap) plus post-curation target SHA-256 reconciliation contract
    verification via pytest tests/test_corpus_review_inventory.py -k 'not verify_target_sha256'
    (9 passed) and causal-graph/UniProtKB regression verification via pytest tests/test_causal_graph_overlays.py
    (6 passed across 15 causal-graph-enriched records reconciled through 20261025T232500Z-cycle4-stage2-causal-graphs-curation
    and 20261026T034000Z-cycle4-stage3-protein-examples), with 27 representative TaxonRecord
    files bound directly in targets and validated via scripts/validate_strict.py.
  reviewed_target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2940590
  - NCBITaxon:3121604
  - NCBITaxon:1435036
  - NCBITaxon:209650
  - NCBITaxon:206
  - NCBITaxon:33952
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:2287
  - NCBITaxon:4932
  - NCBITaxon:5207
  - NCBITaxon:235443
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:5755
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
targets:
- target_id: NCBITaxon:562
  path: data/taxa/bacteria/escherichia_coli.yaml
  label: Escherichia coli
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_562.yaml
    role: Maintained causal-graph and UniProtKB protein-example overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Pinned offline UniProtKB reference protein inventory
- target_id: NCBITaxon:83333
  path: data/taxa/bacteria/escherichia_coli_k_12.yaml
  label: Escherichia coli K-12
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_83333.yaml
    role: Maintained causal-graph and UniProtKB protein-example overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Pinned offline UniProtKB reference protein inventory
- target_id: NCBITaxon:511145
  path: data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml
  label: Escherichia coli str. K-12 substr. MG1655
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_511145.yaml
    role: Maintained causal-graph and UniProtKB protein-example overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Pinned offline UniProtKB reference protein inventory
- target_id: NCBITaxon:1423
  path: data/taxa/bacteria/bacillus_subtilis.yaml
  label: Bacillus subtilis
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_1423.yaml
    role: Maintained causal-graph and UniProtKB protein-example overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Pinned offline UniProtKB reference protein inventory
- target_id: NCBITaxon:224308
  path: data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml
  label: Bacillus subtilis subsp. subtilis str. 168
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_224308.yaml
    role: Maintained causal-graph and UniProtKB protein-example overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Pinned offline UniProtKB reference protein inventory
- target_id: NCBITaxon:287
  path: data/taxa/bacteria/pseudomonas_aeruginosa.yaml
  label: Pseudomonas aeruginosa
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_287.yaml
    role: Maintained causal-graph and UniProtKB protein-example overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Pinned offline UniProtKB reference protein inventory
- target_id: NCBITaxon:208964
  path: data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml
  label: Pseudomonas aeruginosa PAO1
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_208964.yaml
    role: Maintained causal-graph and UniProtKB protein-example overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Pinned offline UniProtKB reference protein inventory
- target_id: NCBITaxon:2940590
  path: data/taxa/bacteria/achromobacter_sp_jub104.yaml
  label: Achromobacter sp. JUb104
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
- target_id: NCBITaxon:3121604
  path: data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml
  label: Acidaminobacteraceae bacterium
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
- target_id: NCBITaxon:1435036
  path: data/taxa/bacteria/acinetobacter_bohemicus.yaml
  label: Acinetobacter bohemicus
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
- target_id: NCBITaxon:209650
  path: data/taxa/bacteria/acidicaldus_organivorans.yaml
  label: Acidicaldus organivorans
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
- target_id: NCBITaxon:206
  path: data/taxa/bacteria/campylobacter_sputorum.yaml
  label: Campylobacter sputorum
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
- target_id: NCBITaxon:33952
  path: data/taxa/bacteria/acetobacterium_woodii.yaml
  label: Acetobacterium woodii
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
- target_id: NCBITaxon:2190
  path: data/taxa/archaea/methanocaldococcus_jannaschii.yaml
  label: Methanocaldococcus jannaschii
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_2190.yaml
    role: Maintained causal-graph and UniProtKB protein-example overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Pinned offline UniProtKB reference protein inventory
- target_id: NCBITaxon:243232
  path: data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml
  label: Methanocaldococcus jannaschii DSM 2661
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_243232.yaml
    role: Maintained causal-graph and UniProtKB protein-example overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Pinned offline UniProtKB reference protein inventory
- target_id: NCBITaxon:2287
  path: data/taxa/archaea/saccharolobus_solfataricus.yaml
  label: Saccharolobus solfataricus
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
- target_id: NCBITaxon:4932
  path: data/taxa/eukaryota/saccharomyces_cerevisiae.yaml
  label: Saccharomyces cerevisiae
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
- target_id: NCBITaxon:5207
  path: data/taxa/eukaryota/cryptococcus_neoformans.yaml
  label: Cryptococcus neoformans
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_5207.yaml
    role: Maintained causal-graph and UniProtKB protein-example overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Pinned offline UniProtKB reference protein inventory
- target_id: NCBITaxon:235443
  path: data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml
  label: Cryptococcus neoformans H99
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_235443.yaml
    role: Maintained causal-graph and UniProtKB protein-example overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Pinned offline UniProtKB reference protein inventory
- target_id: NCBITaxon:40410
  path: data/taxa/eukaryota/cryptococcus_deneoformans.yaml
  label: Cryptococcus deneoformans
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_40410.yaml
    role: Maintained causal-graph and UniProtKB protein-example overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Pinned offline UniProtKB reference protein inventory
- target_id: NCBITaxon:283643
  path: data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml
  label: Cryptococcus deneoformans B-3501A
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_283643.yaml
    role: Maintained causal-graph and UniProtKB protein-example overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Pinned offline UniProtKB reference protein inventory
- target_id: NCBITaxon:1859096
  path: data/taxa/eukaryota/cryptococcus_deuterogattii.yaml
  label: Cryptococcus deuterogattii
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_1859096.yaml
    role: Maintained causal-graph and UniProtKB protein-example overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Pinned offline UniProtKB reference protein inventory
- target_id: NCBITaxon:294750
  path: data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml
  label: Cryptococcus deuterogattii R265
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
  - repository: CultureBotAI/TaxonMech
    path: curation/causal_graphs/NCBITaxon_294750.yaml
    role: Maintained causal-graph and UniProtKB protein-example overlay
  - repository: CultureBotAI/TaxonMech
    path: curation/uniprot_proteins.tsv
    role: Pinned offline UniProtKB reference protein inventory
- target_id: NCBITaxon:5755
  path: data/taxa/eukaryota/acanthamoeba_castellanii.yaml
  label: Acanthamoeba castellanii
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
- target_id: NCBITaxon:155900
  path: data/taxa/other/uncultured_organism.yaml
  label: uncultured organism
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
- target_id: NCBITaxon:408170
  path: data/taxa/other/human_gut_metagenome.yaml
  label: human gut metagenome
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
- target_id: NCBITaxon:32644
  path: data/taxa/other/unidentified.yaml
  label: unidentified
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxonomy and lineage inventory
checks:
- check_id: validate-strict
  name: Native strict, LinkML schema, structural causal-graph, and offline UniProtKB
    protein validation on directly bound Cycle 4 Stage 4 exemplar records
  status: passed
  required: true
  summary: All 27 directly bound cross-domain exemplar and causal-graph TaxonRecord
    files pass scripts/validate_strict.py (including validate_causal_graph_structure()
    and validate_causal_graph_proteins() against curation/uniprot_proteins.tsv) with
    0 errors.
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2940590
  - NCBITaxon:3121604
  - NCBITaxon:1435036
  - NCBITaxon:209650
  - NCBITaxon:206
  - NCBITaxon:33952
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:2287
  - NCBITaxon:4932
  - NCBITaxon:5207
  - NCBITaxon:235443
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:5755
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  command: .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
    data/taxa/archaea/methanocaldococcus_jannaschii.yaml data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml
    data/taxa/archaea/saccharolobus_solfataricus.yaml data/taxa/bacteria/acetobacterium_woodii.yaml
    data/taxa/bacteria/achromobacter_sp_jub104.yaml data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml
    data/taxa/bacteria/acidicaldus_organivorans.yaml data/taxa/bacteria/acinetobacter_bohemicus.yaml
    data/taxa/bacteria/bacillus_subtilis.yaml data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml
    data/taxa/bacteria/campylobacter_sputorum.yaml data/taxa/bacteria/escherichia_coli.yaml
    data/taxa/bacteria/escherichia_coli_k_12.yaml data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml
    data/taxa/bacteria/pseudomonas_aeruginosa.yaml data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml
    data/taxa/eukaryota/acanthamoeba_castellanii.yaml data/taxa/eukaryota/cryptococcus_deneoformans.yaml
    data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml data/taxa/eukaryota/cryptococcus_deuterogattii.yaml
    data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml data/taxa/eukaryota/cryptococcus_neoformans.yaml
    data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml data/taxa/eukaryota/saccharomyces_cerevisiae.yaml
    data/taxa/other/human_gut_metagenome.yaml data/taxa/other/uncultured_organism.yaml
    data/taxa/other/unidentified.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - exemplar-target-records
  - schema-seeder-validator-code
- check_id: history
  name: Native history validation across committed history records
  status: passed
  required: true
  summary: scripts/validate_history.py passes on all 29 repository history records
    against src/taxonmech/schema/history.yaml (#83 resolved in Cycle 1 Stage 5).
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2940590
  - NCBITaxon:3121604
  - NCBITaxon:1435036
  - NCBITaxon:209650
  - NCBITaxon:206
  - NCBITaxon:33952
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:2287
  - NCBITaxon:4932
  - NCBITaxon:5207
  - NCBITaxon:235443
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:5755
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  command: .venv/bin/python scripts/validate_history.py history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema-seeder-validator-code
- check_id: historical-counts
  name: Required historical native-unit counts
  status: unavailable
  required: true
  summary: Manifest-pinned upstream kg-microbe raw edge tables for GOLD, MEDIADIVE,
    MADIN, and BACTOTRAITS are not committed locally (though SHA-256 digests are documented
    in docs/HARMONIZATION.md), and subtree rollups apply to BacDive strains only (#8;
    taxonmech-infra-0004).
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2940590
  - NCBITaxon:3121604
  - NCBITaxon:1435036
  - NCBITaxon:209650
  - NCBITaxon:206
  - NCBITaxon:33952
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:2287
  - NCBITaxon:4932
  - NCBITaxon:5207
  - NCBITaxon:235443
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:5755
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  evidence_ids:
  - corpus-review-inventories
  - raw-source-inventories
- check_id: corpus-review-inventory-coverage
  name: Full-corpus review coverage and disjointness check across all 626,048 records
  status: passed
  required: true
  summary: scripts/corpus_review_inventory.py --check verified 626,048 corpus records
    (23,883 legacy + 602,165 structured across 14 shards and 611 batches) with 0 unreviewed
    records and 0 overlaps.
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2940590
  - NCBITaxon:3121604
  - NCBITaxon:1435036
  - NCBITaxon:209650
  - NCBITaxon:206
  - NCBITaxon:33952
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:2287
  - NCBITaxon:4932
  - NCBITaxon:5207
  - NCBITaxon:235443
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:5755
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  command: .venv/bin/python scripts/corpus_review_inventory.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - corpus-review-inventories
- check_id: corpus-review-inventory-reconciliation-tests
  name: Structured review inventory and post-curation target SHA-256 reconciliation
    regression suite
  status: passed
  required: true
  summary: pytest tests/test_corpus_review_inventory.py -k 'not verify_target_sha256'
    passed all 9 tests verifying shard coverage, load_latest_target_reviews() post-curation
    target_sha256 reconciliation (#158), and in-repository symlink input handling
    (#185).
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2940590
  - NCBITaxon:3121604
  - NCBITaxon:1435036
  - NCBITaxon:209650
  - NCBITaxon:206
  - NCBITaxon:33952
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:2287
  - NCBITaxon:4932
  - NCBITaxon:5207
  - NCBITaxon:235443
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:5755
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  command: .venv/bin/pytest tests/test_corpus_review_inventory.py -k "not verify_target_sha256"
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - corpus-review-inventories
  - cycle4-causal-graph-and-uniprot-overlays
- check_id: causal-graph-overlay-roundtrip-tests
  name: Committed causal-graph and UniProtKB overlay regression suite
  status: passed
  required: true
  summary: pytest tests/test_causal_graph_overlays.py passed all 6 tests verifying
    overlay loading, structural causal-graph validation, seeder merge, LinkML validation,
    offline curation/uniprot_proteins.tsv validation (including strain_id and vertical
    lineage consistency), and HTML rendering across all 15 maintained overlays (161
    edges, 51 GENE_OR_PROTEIN nodes across 23 UniProtKB accessions).
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
  - NCBITaxon:5207
  - NCBITaxon:235443
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:1859096
  - NCBITaxon:294750
  command: .venv/bin/pytest tests/test_causal_graph_overlays.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - cycle4-causal-graph-and-uniprot-overlays
  - schema-seeder-validator-code
evidence:
- evidence_id: corpus-review-inventories
  kind: record_content
  reference: docs/legacy-review-inventory.tsv; docs/structured-review-inventory/part-00.tsv..part-13.tsv;
    docs/structured-review-batches.tsv; docs/corpus-review-coverage.md
  locator: 23,883 rows in docs/legacy-review-inventory.tsv and 602,165 rows across
    docs/structured-review-inventory/part-00.tsv..part-13.tsv
  summary: 'Complete per-record review inventories covering all 626,048 TaxonRecord
    files in data/taxa/ (0 unreviewed, 0 overlap; structured verdicts: pass=479,251,
    pass_with_limitations=27,118, needs_curation=95,766, blocked=30), with post-curation
    target_sha256 digests reconciled by load_latest_target_reviews() and documented
    in docs/corpus-review-coverage.md (#158).'
  accessed_at: '2026-10-31T07:53:00Z'
  support: supports
  snapshot_sha256: 023ac83c94ea72c7822acb3b111e5dddb41b1df8304f5b7ec4146883557ebce4
- evidence_id: exemplar-target-records
  kind: record_content
  reference: data/taxa/bacteria/escherichia_coli.yaml; data/taxa/bacteria/escherichia_coli_k_12.yaml;
    data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml; data/taxa/bacteria/bacillus_subtilis.yaml;
    data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml; data/taxa/bacteria/pseudomonas_aeruginosa.yaml;
    data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml; data/taxa/bacteria/achromobacter_sp_jub104.yaml;
    data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml; data/taxa/bacteria/acinetobacter_bohemicus.yaml;
    data/taxa/bacteria/acidicaldus_organivorans.yaml; data/taxa/bacteria/campylobacter_sputorum.yaml;
    data/taxa/bacteria/acetobacterium_woodii.yaml; data/taxa/archaea/methanocaldococcus_jannaschii.yaml;
    data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml; data/taxa/archaea/saccharolobus_solfataricus.yaml;
    data/taxa/eukaryota/saccharomyces_cerevisiae.yaml; data/taxa/eukaryota/cryptococcus_neoformans.yaml;
    data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml; data/taxa/eukaryota/cryptococcus_deneoformans.yaml;
    data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml; data/taxa/eukaryota/cryptococcus_deuterogattii.yaml;
    data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml; data/taxa/eukaryota/acanthamoeba_castellanii.yaml;
    data/taxa/other/uncultured_organism.yaml; data/taxa/other/human_gut_metagenome.yaml;
    data/taxa/other/unidentified.yaml
  locator: Complete YAML content of 27 directly bound cross-domain, verdict-stratified,
    and causal-graph-enriched TaxonRecord files
  summary: Verified taxon identity, lineage, nomenclature, synonyms, xrefs, taxonomy_mappings,
    source_attestations, strains, causal_graphs, and curation_history across 27 exemplar
    records spanning Bacteria (13), Archaea (3), Eukaryota (8), and other (3).
  accessed_at: '2026-10-31T07:53:00Z'
  support: supports
  snapshot_sha256: f6680054018c9d13d190bf7e9f3fe49b1521915f90f95280d464d7ca49d73e6b
- evidence_id: cycle4-causal-graph-and-uniprot-overlays
  kind: record_content
  reference: curation/causal_graphs/README.md; curation/causal_graphs/NCBITaxon_*.yaml;
    curation/uniprot_proteins.tsv; reviews/structured/20261025T232500Z-cycle4-stage2-causal-graphs-curation/review.yaml;
    reviews/structured/20261026T034000Z-cycle4-stage3-protein-examples/review.yaml
  locator: 15 maintained curation/causal_graphs/NCBITaxon_*.yaml overlays, curation/uniprot_proteins.tsv
    (23 rows), and Cycle 4 Stages 2-3 structured review bundles
  summary: Verified 15 maintained causal-graph overlays seeded into 7 species and
    8 strain TaxonRecord files (161 evidence-backed edges across 33 PMIDs; 51 GENE_OR_PROTEIN
    nodes grounded to 23 unique live-verified UniProtKB accessions—21 SWISS_PROT and
    2 TREMBL—in curation/uniprot_proteins.tsv with exact organism_taxon_id, strain_id,
    proteome_id, gene_symbol, locus_tag, sequence_length, sequence_crc64, sequence_version,
    and entry_status).
  accessed_at: '2026-10-31T07:53:00Z'
  support: supports
  snapshot_sha256: 5a2aad69ea22951b0bfc248d995ba2bc9713fc06e5bba0d6a1fb4b6db71e8dbe
- evidence_id: raw-source-inventories
  kind: record_content
  reference: curation/seed_scope.tsv; data/raw/MANIFEST.yaml; data/raw/ncbitaxon_taxa.tsv;
    data/raw/gtdb_mappings.tsv; data/raw/gtdb_species.tsv; data/raw/bacdive_strains.tsv;
    data/raw/lpsn_names.tsv
  locator: curation/seed_scope.tsv (626,048 rows) and data/raw/*.tsv
  summary: Pinned raw inventories verify exact NCBI taxon IDs and lineages across
    all 626,048 records and confirm persistent GTDB closeMatch fan-out (95,766 records),
    polyphyly suffix mangling (15,704 rows), pooled broadMatch genome counts/notes
    (8,587 records), and stale seed_scope strain-count reason strings.
  accessed_at: '2026-10-31T07:53:00Z'
  support: supports
  snapshot_sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
- evidence_id: schema-seeder-validator-code
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml; src/taxonmech/seed.py; src/taxonmech/extract.py;
    scripts/validate_strict.py; scripts/check_provenance.py; scripts/corpus_review_inventory.py;
    scripts/validate_history.py; docs/SCHEMA.md; docs/HARMONIZATION.md; docs/corpus-review-coverage.md;
    INFRA_TASKS.md
  locator: taxonmech.yaml:43-95,1200-1315,1520-1575; seed.py:216-430,508-535,636-715;
    validate_strict.py:217-370; check_provenance.py:1-140; corpus_review_inventory.py:185-330,381-445;
    docs/SCHEMA.md:1-38; INFRA_TASKS.md:33-340
  summary: 'Inspection of schema, seeder, extractor, strict/UniProt/provenance validators,
    inventory checker, and documentation confirms resolution of #76 and #83 in Cycle
    1 Stage 5, resolution of #158 code in Cycle 2 Stage 5 (PR #159) and #158 documentation/regression
    test in Cycle 3 Stage 5 (PR #165), structural causal-graph and strain_id validation
    plus conf/sources.yaml registration in Cycle 3 Stage 6 (PR #168), persistent GTDB/scope
    seeder defects at src/taxonmech/seed.py lines 508-535, 636-650, and 691-702 (#124,
    #63, #65, #118, #119, #69), remaining corpus-wide trait/UniProt/attestation-note
    tasks in INFRA_TASKS.md (taxonmech-infra-0001..0004; #78, #8), and omission of
    the 9 GENE_OR_PROTEIN UniProtKB slots and UniProtEntryStatusEnum from docs/SCHEMA.md
    line 20 (#78).'
  accessed_at: '2026-10-31T07:53:00Z'
  support: supports
  snapshot_sha256: 57f375e3d289e4f16ae71340cbd75e0b836d28e6e9c90fbf4fd9a6756be6b4dc
assessments:
- assessment_id: corpus-review-coverage-and-identity
  area: identity
  topic: Full-corpus review coverage (626,048 records), NCBI taxonomy alignment, and
    post-curation SHA-256 inventory state
  outcome: supported
  summary: All 626,048 in-scope TaxonRecord YAML files in data/taxa/ are accounted
    for without gap or overlap (23,883 legacy + 602,165 structured across 14 shards
    and 611 batches), match their pinned data/raw/ncbitaxon_taxa.tsv identifier, label,
    rank, domain, parent_taxon, and lineage, and have their multi-stage workflow review
    bundles (435 bundles in reviews/structured/ including this bundle) and post-curation
    target SHA-256 reconciliation contract documented in docs/corpus-review-coverage.md
    and enforced by tests/test_corpus_review_inventory.py (#158).
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2940590
  - NCBITaxon:3121604
  - NCBITaxon:1435036
  - NCBITaxon:209650
  - NCBITaxon:206
  - NCBITaxon:33952
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:2287
  - NCBITaxon:4932
  - NCBITaxon:5207
  - NCBITaxon:235443
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:5755
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  evidence_ids:
  - corpus-review-inventories
  - exemplar-target-records
  - cycle4-causal-graph-and-uniprot-overlays
  - raw-source-inventories
  - schema-seeder-validator-code
  metrics:
  - name: total_corpus_records
    value: 626048.0
    unit: records
    definition: Total generated TaxonRecord YAML files in data/taxa/ and data/taxa/PATHS.tsv.
    denominator: 626048
    minimum: 626048.0
    maximum: 626048.0
  - name: legacy_reviewed_records
    value: 23883.0
    unit: records
    definition: TaxonRecord files covered by docs/legacy-review-inventory.tsv.
    denominator: 626048
    minimum: 0.0
    maximum: 626048.0
  - name: structured_reviewed_records
    value: 602165.0
    unit: records
    definition: TaxonRecord files covered by docs/structured-review-inventory/part-00.tsv..part-13.tsv.
    denominator: 626048
    minimum: 0.0
    maximum: 626048.0
  - name: unreviewed_or_overlapping_records
    value: 0.0
    unit: records
    definition: Count of unreviewed or duplicate-inventory TaxonRecord files across
      the 626,048-record corpus.
    denominator: 626048
    minimum: 0.0
    maximum: 0.0
  - name: post_curation_shard_target_sha256_mismatches
    value: 0.0
    unit: records
    definition: Unreconciled structured-inventory target_sha256 mismatches reported
      by scripts/corpus_review_inventory.py --check --verify-target-sha256.
    denominator: 602165
    minimum: 0.0
    maximum: 602165.0
- assessment_id: gtdb-harmonization-and-nomenclature
  area: nomenclature
  topic: GTDB closeMatch synonym/xref promotion, polyphyly suffix mangling, and pooled
    broadMatch genome/note semantics
  outcome: concern
  summary: 'Across the 602,165 structured-review records, 95,766 records carry verdict
    needs_curation due to src/taxonmech/seed.py (lines 508-535) promoting skos:closeMatch
    GTDB species-cluster mappings to EXACT_SYNONYM and top-level xrefs (#124, #63),
    mangling 15,704 polyphyly-suffixed GTDB labels into fake trinomials at line 529
    (#65), and emitting misleading pooled broadMatch genome totals (lines 636-650;
    #118) and inverted broadMatch notes (lines 522-524; #119) on 8,587 records.'
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:2940590
  - NCBITaxon:3121604
  - NCBITaxon:206
  - NCBITaxon:33952
  evidence_ids:
  - corpus-review-inventories
  - exemplar-target-records
  - raw-source-inventories
  - schema-seeder-validator-code
  metrics:
  - name: structured_needs_curation_records
    value: 95766.0
    unit: records
    definition: Structured-review records carrying verdict needs_curation due to GTDB
      closeMatch promotion.
    denominator: 602165
    minimum: 0.0
    maximum: 602165.0
  - name: structured_pass_records
    value: 479251.0
    unit: records
    definition: Structured-review records carrying verdict pass.
    denominator: 602165
    minimum: 0.0
    maximum: 602165.0
  - name: structured_pass_with_limitations_records
    value: 27118.0
    unit: records
    definition: Structured-review records carrying verdict pass_with_limitations.
    denominator: 602165
    minimum: 0.0
    maximum: 602165.0
  - name: structured_blocked_records
    value: 30.0
    unit: records
    definition: Structured-review records carrying verdict blocked.
    denominator: 602165
    minimum: 0.0
    maximum: 602165.0
- assessment_id: causal-graphs-uniprot-and-mechanism-completeness
  area: completeness
  topic: Cycle 4 causal_graphs and UniProtKB GENE_OR_PROTEIN coverage (15 records,
    51 protein nodes across 23 unique UniProtKB accessions, 161 edges across 33 PMIDs),
    docs/SCHEMA.md slot documentation, and remaining corpus-wide prerequisites
  outcome: concern
  summary: 'All 15 records enriched through Cycle 4 Stages 2-3 (PRs #155, #156, #162,
    #163, #181, #183) pass strict LinkML validation, structural causal-graph validation
    (validate_causal_graph_structure()), deterministic seeder reproduction, and offline
    + live UniProtKB verification across 15 causal graphs, 51 GENE_OR_PROTEIN nodes
    (23 unique UniProtKB accessions: 21 SWISS_PROT and 2 TREMBL in curation/uniprot_proteins.tsv),
    and 161 evidence-backed edges across 33 PMIDs; however, docs/SCHEMA.md (line 20)
    still omits the 9 GENE_OR_PROTEIN UniProtKB protein-grounding slots and UniProtEntryStatusEnum
    added to src/taxonmech/schema/taxonmech.yaml, and the remaining 626,033 records
    (99.998%) still have empty causal_graphs pending upstream kg-microbe bulk data/raw/taxon_trait_edges.tsv
    extraction (taxonmech-infra-0002) and a corpus-wide data/raw/ UniProtKB Reference
    Proteomes snapshot (taxonmech-infra-0003; #78).'
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2940590
  - NCBITaxon:3121604
  - NCBITaxon:1435036
  - NCBITaxon:209650
  - NCBITaxon:206
  - NCBITaxon:33952
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:2287
  - NCBITaxon:4932
  - NCBITaxon:5207
  - NCBITaxon:235443
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:1859096
  - NCBITaxon:294750
  - NCBITaxon:5755
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  evidence_ids:
  - exemplar-target-records
  - cycle4-causal-graph-and-uniprot-overlays
  - schema-seeder-validator-code
  metrics:
  - name: causal_graph_enriched_records
    value: 15.0
    unit: records
    definition: TaxonRecord files populated with maintained curation/causal_graphs/*.yaml
      overlays through Cycle 4 Stage 3.
    denominator: 626048
    minimum: 0.0
    maximum: 626048.0
  - name: verified_uniprot_gene_or_protein_nodes
    value: 51.0
    unit: nodes
    definition: GENE_OR_PROTEIN CausalNode instances grounded to live-verified and
      offline-validated UniProtKB accessions across the 15 causal-graph records.
    denominator: 51
    minimum: 0.0
    maximum: 51.0
  - name: verified_causal_edges
    value: 161.0
    unit: edges
    definition: Evidence-backed CausalEdge instances with primary PMID citations across
      the 15 causal-graph records.
    denominator: 161
    minimum: 0.0
    maximum: 161.0
findings:
- finding_id: causal-node-type-enum-and-mech-family-nav-drift
  issue_key: cycle3-stage4-causal-node-type-enum-and-mech-family-nav-drift
  category: schema
  severity: minor
  status: resolved
  certainty: confirmed
  title: CausalNodeTypeEnum parity with TraitMech (RNA, GENETIC_ELEMENT, ORGANELLE)
    and NaturalProductMech family navigation remain resolved
  description: 'Verified in Cycle 4 Stage 4 that src/taxonmech/schema/taxonmech.yaml
    retains the 18-value CausalNodeTypeEnum superset (including RNA, GENETIC_ELEMENT,
    and ORGANELLE) and that README.md, AGENTS.md (and CLAUDE.md symlink), src/taxonmech/templates/{base,index}.html,
    and rendered pages include NaturalProductMech (#76, resolved in Cycle 1 Stage
    5 PR #151).'
  disposition_reason: 'Resolved in Cycle 1 Stage 5 (PR #151) under #76 and verified
    intact in Cycle 4 Stage 4.'
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: causal-node-type-enum-and-mech-family-nav-drift
  - repository: CultureBotAI/TaxonMech
    review_id: 20261022T012228Z-stage5-remediation-review
    finding_id: causal-node-type-enum-and-mech-family-nav-drift
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T073200Z-cycle2-stage4-corpus-record-review
    finding_id: causal-node-type-enum-and-mech-family-nav-drift
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T110500Z-cycle2-stage5-remediation-review
    finding_id: causal-node-type-enum-and-mech-family-nav-drift
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T021500Z-cycle3-stage4-corpus-record-review
    finding_id: causal-node-type-enum-and-mech-family-nav-drift
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T055500Z-cycle3-stage5-remediation-review
    finding_id: causal-node-type-enum-and-mech-family-nav-drift
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:4932
  - NCBITaxon:5207
  field_paths:
  - causal_graphs[].nodes[].node_type
  evidence_ids:
  - schema-seeder-validator-code
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/schema/taxonmech.yaml
    role: LinkML schema definition for CausalNodeTypeEnum
  - repository: CultureBotAI/TaxonMech
    path: README.md
    role: Repository overview and Mech suite table
  - repository: CultureBotAI/TaxonMech
    path: AGENTS.md
    role: Agent architecture and Mech suite documentation
  rule_id: src/taxonmech/schema/taxonmech.yaml:CausalNodeTypeEnum
  normalization_reason: Retain verified resolution from Cycle 1 Stage 5 (#76).
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/76
- finding_id: validate-history-bare-linkml-validate-path
  issue_key: cycle3-stage4-validate-history-bare-linkml-validate-path
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: scripts/validate_history.py resolves linkml-validate beside sys.executable
    across all 29 history records
  description: 'Verified in Cycle 4 Stage 4 that scripts/validate_history.py resolves
    Path(sys.executable).with_name(''linkml-validate'') before falling back to PATH
    and validates all 29 committed history records against src/taxonmech/schema/history.yaml
    (#83, resolved in Cycle 1 Stage 5 PR #151).'
  disposition_reason: 'Resolved in Cycle 1 Stage 5 (PR #151) under #83 and verified
    across all 29 history records in Cycle 4 Stage 4.'
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: validate-history-bare-linkml-validate-path
  - repository: CultureBotAI/TaxonMech
    review_id: 20261022T012228Z-stage5-remediation-review
    finding_id: validate-history-bare-linkml-validate-path
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T073200Z-cycle2-stage4-corpus-record-review
    finding_id: validate-history-bare-linkml-validate-path
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T110500Z-cycle2-stage5-remediation-review
    finding_id: validate-history-bare-linkml-validate-path
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T021500Z-cycle3-stage4-corpus-record-review
    finding_id: validate-history-bare-linkml-validate-path
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T055500Z-cycle3-stage5-remediation-review
    finding_id: validate-history-bare-linkml-validate-path
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:2940590
  field_paths:
  - curation_history
  evidence_ids:
  - schema-seeder-validator-code
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: scripts/validate_history.py
    role: History YAML LinkML validator script
  rule_id: docs/record-review-profile.md:history
  normalization_reason: Retain verified resolution from Cycle 1 Stage 5 (#83).
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/83
- finding_id: gtdb-closematch-exact-promotion
  issue_key: cycle3-stage4-gtdb-closematch-exact-promotion
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: skos:closeMatch GTDB species-cluster mappings are promoted to EXACT_SYNONYM
    and equivalent top-level xrefs across 95,766 records
  description: Across docs/structured-review-inventory/part-00.tsv..part-13.tsv, 95,766
    of 602,165 structured-review records (including 74,325 from fan-out closeMatch
    clusters; e.g., NCBITaxon:2940590 data/taxa/bacteria/achromobacter_sp_jub104.yaml
    promoting GTDB:s__Achromobacter_spanius, NCBITaxon:206 data/taxa/bacteria/campylobacter_sputorum.yaml
    promoting GTDB:s__Campylobacter_F_sputorum, and legacy-reviewed NCBITaxon:33952
    data/taxa/bacteria/acetobacterium_woodii.yaml promoting GTDB:s__Acetobacterium_woodii_A)
    carry verdict needs_curation because src/taxonmech/seed.py (lines 508-535) promotes
    skos:closeMatch GTDB species-cluster rows in data/raw/gtdb_mappings.tsv to EXACT_SYNONYM
    and top-level xrefs without an explicit 1:1 taxon-identity or nomenclatural bridge
    (tracked in https://github.com/CultureBotAI/TaxonMech/issues/124 and https://github.com/CultureBotAI/TaxonMech/issues/63).
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: gtdb-closematch-exact-promotion
  - repository: CultureBotAI/TaxonMech
    review_id: 20261022T012228Z-stage5-remediation-review
    finding_id: gtdb-closematch-exact-promotion
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T073200Z-cycle2-stage4-corpus-record-review
    finding_id: gtdb-closematch-exact-promotion
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T110500Z-cycle2-stage5-remediation-review
    finding_id: gtdb-closematch-exact-promotion
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T021500Z-cycle3-stage4-corpus-record-review
    finding_id: gtdb-closematch-exact-promotion
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T055500Z-cycle3-stage5-remediation-review
    finding_id: gtdb-closematch-exact-promotion
  target_ids:
  - NCBITaxon:2940590
  - NCBITaxon:206
  - NCBITaxon:33952
  field_paths:
  - synonyms
  - xrefs
  - taxonomy_mappings
  - source_attestations
  evidence_ids:
  - corpus-review-inventories
  - exemplar-target-records
  - raw-source-inventories
  - schema-seeder-validator-code
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder and GTDB mapping promoter
  - repository: CultureBotAI/TaxonMech
    path: data/raw/gtdb_mappings.tsv
    role: Pinned GTDB species-cluster mapping inventory
  rule_id: src/taxonmech/schema/taxonmech.yaml:xrefs; docs/record-review-profile.md
  normalization_reason: 'Gate EXACT_SYNONYM and top-level xref promotion on 1:1 taxon-identity
    or nomenclatural equivalence (#124, #63).'
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/124
  - https://github.com/CultureBotAI/TaxonMech/issues/63
- finding_id: gtdb-polyphyly-suffix-synonym-mangling
  issue_key: cycle3-stage4-gtdb-polyphyly-suffix-synonym-mangling
  category: nomenclature
  severity: major
  status: open
  certainty: confirmed
  title: GTDB polyphyly suffixes are mangled by underscore-to-space replacement into
    fake trinomials published as EXACT_SYNONYM
  description: In src/taxonmech/seed.py line 529, GTDB species labels are converted
    via m['gtdb_label'].split('__', 1)[-1].replace('_', ' '), turning GTDB polyphyly
    partition suffixes (e.g., s__Campylobacter_F_sputorum on NCBITaxon:206 data/taxa/bacteria/campylobacter_sputorum.yaml
    -> 'Campylobacter F sputorum', and s__Acetobacterium_woodii_A on NCBITaxon:33952
    data/taxa/bacteria/acetobacterium_woodii.yaml -> 'Acetobacterium woodii A') into
    fake trinomials published as EXACT_SYNONYM across 15,704 rows in data/raw/gtdb_mappings.tsv
    (tracked in https://github.com/CultureBotAI/TaxonMech/issues/65).
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: gtdb-polyphyly-suffix-synonym-mangling
  - repository: CultureBotAI/TaxonMech
    review_id: 20261022T012228Z-stage5-remediation-review
    finding_id: gtdb-polyphyly-suffix-synonym-mangling
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T073200Z-cycle2-stage4-corpus-record-review
    finding_id: gtdb-polyphyly-suffix-synonym-mangling
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T110500Z-cycle2-stage5-remediation-review
    finding_id: gtdb-polyphyly-suffix-synonym-mangling
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T021500Z-cycle3-stage4-corpus-record-review
    finding_id: gtdb-polyphyly-suffix-synonym-mangling
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T055500Z-cycle3-stage5-remediation-review
    finding_id: gtdb-polyphyly-suffix-synonym-mangling
  target_ids:
  - NCBITaxon:206
  - NCBITaxon:33952
  field_paths:
  - synonyms
  evidence_ids:
  - exemplar-target-records
  - raw-source-inventories
  - schema-seeder-validator-code
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: GTDB synonym formatter in build_document
  rule_id: docs/HARMONIZATION.md; src/taxonmech/schema/taxonmech.yaml:TaxonSynonym
  normalization_reason: Preserve GTDB polyphyly suffix syntax or classify GTDB cluster
    names appropriately (#65).
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/65
- finding_id: gtdb-pooled-broadmatch-attestation-and-note
  issue_key: cycle3-stage4-gtdb-pooled-broadmatch-attestation-and-note
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Pooled GTDB broadMatch mappings emit the largest pooled cluster's genome
    total and an inverted mapping-direction note
  description: 'On 6,335 pooled-only GTDB records (e.g., NCBITaxon:3121604 data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml,
    which has 5 pooled skos:broadMatch GTDB mappings led by GTDB:s__JAUMXJ01_sp041781135
    with genome_count: 97), src/taxonmech/seed.py (lines 636-650) emits the largest
    pooled GTDB species cluster''s genome count as the taxon''s GTDB GENOME attestation
    (#118), and across 8,587 pooled GTDB records (209,540 rows, including NCBITaxon:562
    data/taxa/bacteria/escherichia_coli.yaml and NCBITaxon:3121604 data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml)
    seed.py lines 522-524 emit a note stating the reverse of kg-microbe''s skos:broadMatch
    direction (#119).'
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: gtdb-pooled-broadmatch-attestation-and-note
  - repository: CultureBotAI/TaxonMech
    review_id: 20261022T012228Z-stage5-remediation-review
    finding_id: gtdb-pooled-broadmatch-attestation-and-note
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T073200Z-cycle2-stage4-corpus-record-review
    finding_id: gtdb-pooled-broadmatch-attestation-and-note
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T110500Z-cycle2-stage5-remediation-review
    finding_id: gtdb-pooled-broadmatch-attestation-and-note
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T021500Z-cycle3-stage4-corpus-record-review
    finding_id: gtdb-pooled-broadmatch-attestation-and-note
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T055500Z-cycle3-stage5-remediation-review
    finding_id: gtdb-pooled-broadmatch-attestation-and-note
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:3121604
  field_paths:
  - taxonomy_mappings
  - source_attestations
  evidence_ids:
  - exemplar-target-records
  - raw-source-inventories
  - schema-seeder-validator-code
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: GTDB taxonomy_mappings and source_attestations builder
  rule_id: docs/HARMONIZATION.md
  normalization_reason: 'Align pooled GTDB broadMatch notes and genome-count attestations
    with exact mapping semantics (#118, #119).'
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/118
  - https://github.com/CultureBotAI/TaxonMech/issues/119
- finding_id: curation-history-stale-scope-strain-count
  issue_key: cycle3-stage4-curation-history-stale-scope-strain-count
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: SEEDED_FROM_SOURCES curation_history embeds stale static strain counts from
    curation/seed_scope.tsv reason strings
  description: In src/taxonmech/seed.py lines 691-702, the SEEDED_FROM_SOURCES curation_history
    note copies the static reason string from curation/seed_scope.tsv (e.g., '1861
    BacDive strains' on NCBITaxon:562 data/taxa/bacteria/escherichia_coli.yaml) even
    when subtree strain aggregation yields a higher seeded strain_count (1975 on NCBITaxon:562;
    tracked in https://github.com/CultureBotAI/TaxonMech/issues/69).
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: curation-history-stale-scope-strain-count
  - repository: CultureBotAI/TaxonMech
    review_id: 20261022T012228Z-stage5-remediation-review
    finding_id: curation-history-stale-scope-strain-count
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T073200Z-cycle2-stage4-corpus-record-review
    finding_id: curation-history-stale-scope-strain-count
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T110500Z-cycle2-stage5-remediation-review
    finding_id: curation-history-stale-scope-strain-count
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T021500Z-cycle3-stage4-corpus-record-review
    finding_id: curation-history-stale-scope-strain-count
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T055500Z-cycle3-stage5-remediation-review
    finding_id: curation-history-stale-scope-strain-count
  target_ids:
  - NCBITaxon:562
  field_paths:
  - curation_history
  - strain_count
  evidence_ids:
  - exemplar-target-records
  - raw-source-inventories
  - schema-seeder-validator-code
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: curation_history SEEDED_FROM_SOURCES note builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Seed scope reason table
  rule_id: docs/CURATION.md
  normalization_reason: Keep curation_history strain count descriptions consistent
    with seeded strain_count (#69).
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/69
- finding_id: upstream-edge-multiplicity-and-subtree-count-scope
  issue_key: cycle3-stage4-upstream-edge-multiplicity-and-subtree-count-scope
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Upstream kg-microbe edge tables for GOLD/MEDIADIVE/MADIN/BACTOTRAITS are
    not committed locally and direct-only attestation notes require corpus-wide re-seeding
  description: 'Across docs/structured-review-inventory/part-00.tsv..part-13.tsv,
    27,118 records carry verdict pass_with_limitations (e.g., NCBITaxon:1435036, NCBITaxon:562,
    NCBITaxon:1423, NCBITaxon:287) and 30 carry verdict blocked (e.g., NCBITaxon:209650)
    because manifest-pinned upstream kg-microbe raw edge tables for GOLD, MEDIADIVE,
    MADIN, and BACTOTRAITS are not committed locally and src/taxonmech/seed.py (lines
    670-688) gathers infraspecific subtree records only for BacDive strains. Although
    Cycle 1 Stage 6 (PR #152) documented pinned kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd
    edge-table SHA-256 digests in docs/HARMONIZATION.md, corpus-wide re-seeding of
    source_attestations[].notes remains deferred (INFRA_TASKS.md taxonmech-infra-0004;
    https://github.com/CultureBotAI/TaxonMech/issues/8).'
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: upstream-edge-multiplicity-and-subtree-count-scope
  - repository: CultureBotAI/TaxonMech
    review_id: 20261022T012228Z-stage5-remediation-review
    finding_id: upstream-edge-multiplicity-and-subtree-count-scope
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T073200Z-cycle2-stage4-corpus-record-review
    finding_id: upstream-edge-multiplicity-and-subtree-count-scope
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T110500Z-cycle2-stage5-remediation-review
    finding_id: upstream-edge-multiplicity-and-subtree-count-scope
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T021500Z-cycle3-stage4-corpus-record-review
    finding_id: upstream-edge-multiplicity-and-subtree-count-scope
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T055500Z-cycle3-stage5-remediation-review
    finding_id: upstream-edge-multiplicity-and-subtree-count-scope
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:1423
  - NCBITaxon:287
  - NCBITaxon:1435036
  - NCBITaxon:209650
  field_paths:
  - source_attestations
  evidence_ids:
  - corpus-review-inventories
  - exemplar-target-records
  - raw-source-inventories
  - schema-seeder-validator-code
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: Upstream kg-microbe raw inventory extractor
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Source attestation builder
  rule_id: docs/record-review-profile.md:historical-counts
  normalization_reason: Complete upstream edge-table provenance and direct vs subtree
    attestation count alignment (#8; taxonmech-infra-0004).
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/8
- finding_id: mechanism-and-protein-representation-prerequisites
  issue_key: cycle3-stage4-mechanism-and-protein-representation-prerequisites
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: 626,033 of 626,048 TaxonRecord files remain without causal_graphs or UniProtKB
    GENE_OR_PROTEIN nodes pending bulk kg-microbe trait-edge extraction and a pinned
    data/raw/ UniProtKB inventory
  description: 'Following Cycle 1 Stage 6 (PR #152), Cycle 2 Stages 2-3 and 6 (PRs
    #155, #156, #160), Cycle 3 Stages 2-3 and 6 (PRs #162, #163, #168), and Cycle
    4 Stages 2-3 (PRs #181, #183), 15 TaxonRecord files across Bacteria (7), Archaea
    (2), and Eukaryota (6) now carry structurally and provenance-validated causal_graphs
    (161 edges across 33 PMIDs, 51 GENE_OR_PROTEIN nodes across 23 unique live-verified
    UniProtKB accessions—21 SWISS_PROT and 2 TREMBL—in curation/uniprot_proteins.tsv
    registered in conf/sources.yaml and validated offline by validate_causal_graph_structure()
    and validate_causal_graph_proteins()). However, the remaining 626,033 of 626,048
    records (including 38,342 additional trait/medium-attested records) still have
    empty causal_graphs because: (1) data/raw/taxon_trait_edges.tsv has not yet been
    generated from an upstream local kg-microbe checkout using src/taxonmech/extract.py:extract_taxon_trait_edges
    (taxonmech-infra-0002); and (2) data/raw/ still lacks a corpus-wide release-pinned
    UniProtKB / Reference Proteomes TSV snapshot beyond the 23-entry curated reference
    table (taxonmech-infra-0003; tracked in INFRA_TASKS.md and https://github.com/CultureBotAI/TaxonMech/issues/78).'
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: mechanism-and-protein-representation-prerequisites
  - repository: CultureBotAI/TaxonMech
    review_id: 20261022T012228Z-stage5-remediation-review
    finding_id: mechanism-and-protein-representation-prerequisites
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T073200Z-cycle2-stage4-corpus-record-review
    finding_id: mechanism-and-protein-representation-prerequisites
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T110500Z-cycle2-stage5-remediation-review
    finding_id: mechanism-and-protein-representation-prerequisites
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T021500Z-cycle3-stage4-corpus-record-review
    finding_id: mechanism-and-protein-representation-prerequisites
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T055500Z-cycle3-stage5-remediation-review
    finding_id: mechanism-and-protein-representation-prerequisites
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
  - NCBITaxon:5207
  - NCBITaxon:235443
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:1859096
  - NCBITaxon:294750
  field_paths:
  - causal_graphs
  - causal_graphs[].nodes[].grounding
  evidence_ids:
  - exemplar-target-records
  - cycle4-causal-graph-and-uniprot-overlays
  - schema-seeder-validator-code
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: Upstream kg-microbe trait-edge extractor
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Seeder record builder and causal_graphs overlay merger
  - repository: CultureBotAI/TaxonMech
    path: conf/sources.yaml
    role: Pinned upstream data source registry
  - repository: CultureBotAI/TaxonMech
    path: data/raw/MANIFEST.yaml
    role: Raw source file manifest
  rule_id: INFRA_TASKS.md:taxonmech-infra-0001..0003
  normalization_reason: Complete bulk trait-edge extraction and pinned UniProtKB snapshot/validator
    in Stage 6 (#78).
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/78
- finding_id: structured-inventory-verify-target-sha256-post-curation-drift
  issue_key: cycle3-stage4-structured-inventory-verify-target-sha256-post-curation-drift
  category: provenance
  severity: major
  status: resolved
  certainty: confirmed
  title: scripts/corpus_review_inventory.py --check --verify-target-sha256 reconciles
    post-curation target SHA-256 digests against newer scientific review bundles without
    mutating historical shard rows
  description: 'Verified in Cycle 4 Stage 4 at 830eb576c1381e73aba1ed284c1ae005c7a5337e
    that scripts/corpus_review_inventory.py and pytest tests/test_corpus_review_inventory.py
    (9 passed) reconcile post-curation target_sha256 digests across all 602,165 structured-inventory
    records (including the 10 structured-shard records curated through Cycle 4 Stages
    2-3 in PRs #181 and #183) against the latest scientific review bundles in reviews/structured/
    without mutating historical append-only review bundles (resolved in Cycle 2 Stage
    5 PR #159 under https://github.com/CultureBotAI/TaxonMech/issues/158).'
  target_ids:
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:1859096
  field_paths:
  - causal_graphs
  - curation_history
  evidence_ids:
  - corpus-review-inventories
  - cycle4-causal-graph-and-uniprot-overlays
  - schema-seeder-validator-code
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: scripts/corpus_review_inventory.py
    role: Corpus review inventory and target SHA-256 verifier
  - repository: CultureBotAI/TaxonMech
    path: docs/structured-review-inventory/part-02.tsv
    role: Structured review shard part-02
  - repository: CultureBotAI/TaxonMech
    path: docs/structured-review-inventory/part-05.tsv
    role: Structured review shard part-05
  - repository: CultureBotAI/TaxonMech
    path: docs/structured-review-inventory/part-08.tsv
    role: Structured review shard part-08
  - repository: CultureBotAI/TaxonMech
    path: docs/structured-review-inventory/part-12.tsv
    role: Structured review shard part-12
  - repository: CultureBotAI/TaxonMech
    path: docs/structured-review-inventory/part-13.tsv
    role: Structured review shard part-13
  rule_id: scripts/corpus_review_inventory.py:verify_shard_bundles
  normalization_reason: Retain verified resolution from Cycle 2 Stage 5 (#158).
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T073200Z-cycle2-stage4-corpus-record-review
    finding_id: structured-inventory-verify-target-sha256-post-curation-drift
  - repository: CultureBotAI/TaxonMech
    review_id: 20261023T110500Z-cycle2-stage5-remediation-review
    finding_id: structured-inventory-verify-target-sha256-post-curation-drift
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T021500Z-cycle3-stage4-corpus-record-review
    finding_id: structured-inventory-verify-target-sha256-post-curation-drift
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T055500Z-cycle3-stage5-remediation-review
    finding_id: structured-inventory-verify-target-sha256-post-curation-drift
  disposition_reason: 'Resolved in Cycle 2 Stage 5 (PR #159) under #158 and verified
    intact across Cycle 4 Stages 2-3 curation updates and 435 structured review bundles
    in Cycle 4 Stage 4.'
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/158
  - https://github.com/CultureBotAI/TaxonMech/issues/78
- finding_id: corpus-review-coverage-doc-stale-bundle-inventory-counts
  issue_key: cycle3-stage4-corpus-review-coverage-doc-stale-bundle-inventory-counts
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: docs/corpus-review-coverage.md documents multi-stage workflow review bundles
    in reviews/structured/ and the post-curation target_sha256 reconciliation contract
    (#158)
  description: 'Verified in Cycle 4 Stage 4 at 830eb576c1381e73aba1ed284c1ae005c7a5337e
    that docs/corpus-review-coverage.md (Sections ''Shard Architecture And Canonical
    Bundles'' and ''Verification'') documents multi-stage workflow scientific review
    bundles in reviews/structured/ and the load_latest_target_reviews() post-curation
    target_sha256 reconciliation contract, and that test_corpus_review_coverage_doc_describes_reconciliation_contract()
    in tests/test_corpus_review_inventory.py passes (resolved in Cycle 3 Stage 5 PR
    #165 under https://github.com/CultureBotAI/TaxonMech/issues/158).'
  target_ids:
  - NCBITaxon:1423
  - NCBITaxon:224308
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:511145
  - NCBITaxon:287
  - NCBITaxon:208964
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:1859096
  field_paths:
  - causal_graphs
  - curation_history
  evidence_ids:
  - corpus-review-inventories
  - cycle4-causal-graph-and-uniprot-overlays
  - schema-seeder-validator-code
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: docs/corpus-review-coverage.md
    role: Full-corpus review coverage architecture and verification documentation
  - repository: CultureBotAI/TaxonMech
    path: scripts/corpus_review_inventory.py
    role: Corpus review inventory and post-curation target SHA-256 verifier
  - repository: CultureBotAI/TaxonMech
    path: tests/test_corpus_review_inventory.py
    role: Corpus review inventory regression test suite
  rule_id: docs/corpus-review-coverage.md:Shard Architecture And Canonical Bundles
  normalization_reason: Synchronize docs/corpus-review-coverage.md and tests/test_corpus_review_inventory.py
    with the post-curation target_sha256 reconciliation contract and multi-stage structured
    review bundles (#158).
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T021500Z-cycle3-stage4-corpus-record-review
    finding_id: corpus-review-coverage-doc-stale-bundle-inventory-counts
  - repository: CultureBotAI/TaxonMech
    review_id: 20261024T055500Z-cycle3-stage5-remediation-review
    finding_id: corpus-review-coverage-doc-stale-bundle-inventory-counts
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/158
  disposition_reason: 'Resolved in Cycle 3 Stage 5 (PR #165) under #158 and verified
    intact in Cycle 4 Stage 4.'
- finding_id: schema-guide-missing-causal-node-uniprot-protein-slots
  issue_key: cycle4-stage4-schema-guide-missing-causal-node-uniprot-protein-slots
  category: schema
  severity: minor
  status: open
  certainty: confirmed
  title: docs/SCHEMA.md Mechanism section omits the 9 CausalNode GENE_OR_PROTEIN UniProtKB
    protein-grounding slots, UniProtEntryStatusEnum, and maintained curation overlay
    inputs
  description: In docs/SCHEMA.md (line 20), the Mechanism section table row still
    states only '| Mechanism | CausalGraph / CausalNode / CausalEdge | Same shape
    as HabitatMech and TraitMech; every edge requires evidence |' and omits the 9
    GENE_OR_PROTEIN UniProtKB protein-grounding slots (organism_taxon_id, strain_id,
    proteome_id, gene_symbol, locus_tag, sequence_length, sequence_crc64, sequence_version,
    entry_status) and UniProtEntryStatusEnum (SWISS_PROT, TREMBL) added to src/taxonmech/schema/taxonmech.yaml
    (lines 1222-1271, 1529-1536) and populated across 51 GENE_OR_PROTEIN nodes in
    15 TaxonRecord files via curation/causal_graphs/*.yaml and curation/uniprot_proteins.tsv
    (tracked under https://github.com/CultureBotAI/TaxonMech/issues/78).
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
  - NCBITaxon:5207
  - NCBITaxon:235443
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:1859096
  - NCBITaxon:294750
  field_paths:
  - causal_graphs
  - causal_graphs[].nodes[].organism_taxon_id
  - causal_graphs[].nodes[].strain_id
  - causal_graphs[].nodes[].proteome_id
  - causal_graphs[].nodes[].gene_symbol
  - causal_graphs[].nodes[].locus_tag
  - causal_graphs[].nodes[].sequence_length
  - causal_graphs[].nodes[].sequence_crc64
  - causal_graphs[].nodes[].sequence_version
  - causal_graphs[].nodes[].entry_status
  evidence_ids:
  - cycle4-causal-graph-and-uniprot-overlays
  - schema-seeder-validator-code
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: docs/SCHEMA.md
    role: Repository LinkML schema field guide
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/schema/taxonmech.yaml
    role: LinkML schema definition for CausalNode and UniProtEntryStatusEnum
  rule_id: src/taxonmech/schema/taxonmech.yaml:CausalNode
  normalization_reason: Document CausalNode GENE_OR_PROTEIN UniProtKB protein-grounding
    slots, UniProtEntryStatusEnum, and maintained curation overlay inputs in docs/SCHEMA.md
    (#78).
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/78
actions:
- action_id: remediate-seeder-gtdb-and-scope-provenance-cohorts
  description: 'Gate skos:closeMatch GTDB promotion to EXACT_SYNONYM and xrefs (#124,
    #63), fix GTDB polyphyly suffix mangling (#65), align pooled GTDB broadMatch genome
    totals and notes (#118, #119), reconcile seed_scope reason strain counts (#69),
    and complete direct vs subtree source attestation count notes (#8) across src/taxonmech/seed.py
    and full-corpus regeneration.'
  finding_ids:
  - gtdb-closematch-exact-promotion
  - gtdb-polyphyly-suffix-synonym-mangling
  - gtdb-pooled-broadmatch-attestation-and-note
  - curation-history-stale-scope-strain-count
  - upstream-edge-multiplicity-and-subtree-count-scope
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:1423
  - NCBITaxon:287
  - NCBITaxon:2940590
  - NCBITaxon:3121604
  - NCBITaxon:1435036
  - NCBITaxon:209650
  - NCBITaxon:206
  - NCBITaxon:33952
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Generated record builder
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit taxon seed scope
  generator: src/taxonmech/seed.py
  acceptance_checks:
  - src/taxonmech/seed.py gates skos:closeMatch exact promotion and preserves GTDB
    polyphyly suffixes
  - Pooled GTDB broadMatch notes and genome counts accurately reflect mapping direction
    and cluster scope
  - Full corpus regenerates cleanly and passes scripts/verify_corpus.py, scripts/validate_strict.py,
    and scripts/render_pages.py --check
- action_id: implement-remaining-mechanism-and-protein-infrastructure-tasks
  description: Execute remaining INFRA_TASKS.md tasks taxonmech-infra-0001..0004 in
    Cycle 4 Stage 6 to generate data/raw/taxon_trait_edges.tsv from upstream kg-microbe,
    expand the release-pinned UniProtKB / Reference Proteomes snapshot beyond curation/uniprot_proteins.tsv
    (#78), and finalize upstream edge-multiplicity provenance (#8).
  finding_ids:
  - mechanism-and-protein-representation-prerequisites
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
  - NCBITaxon:5207
  - NCBITaxon:235443
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:1859096
  - NCBITaxon:294750
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: Upstream kg-microbe extractor
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Seeder record builder
  - repository: CultureBotAI/TaxonMech
    path: conf/sources.yaml
    role: Pinned upstream data source registry
  - repository: CultureBotAI/TaxonMech
    path: data/raw/MANIFEST.yaml
    role: Raw source file manifest
  acceptance_checks:
  - Pinned UniProtKB reference proteome inventory validates all 51 GENE_OR_PROTEIN
    nodes offline
  - Granular trait-edge extraction supports reproducible causal_graphs expansion across
    trait-attested taxa
- action_id: update-schema-guide-for-causal-node-uniprot-protein-slots
  description: Update docs/SCHEMA.md in Cycle 4 Stage 5 to document the 9 CausalNode
    GENE_OR_PROTEIN UniProtKB protein-grounding slots (organism_taxon_id, strain_id,
    proteome_id, gene_symbol, locus_tag, sequence_length, sequence_crc64, sequence_version,
    entry_status), UniProtEntryStatusEnum (SWISS_PROT, TREMBL), and the maintained
    curation/causal_graphs/*.yaml and curation/uniprot_proteins.tsv inputs (#78).
  finding_ids:
  - schema-guide-missing-causal-node-uniprot-protein-slots
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
  - NCBITaxon:5207
  - NCBITaxon:235443
  - NCBITaxon:40410
  - NCBITaxon:283643
  - NCBITaxon:1859096
  - NCBITaxon:294750
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: docs/SCHEMA.md
    role: Repository LinkML schema field guide
  acceptance_checks:
  - docs/SCHEMA.md documents all 9 CausalNode GENE_OR_PROTEIN UniProtKB slots and
    UniProtEntryStatusEnum
  - Schema documentation matches src/taxonmech/schema/taxonmech.yaml and curation/causal_graphs/README.md
limitations:
- Per-record review rows for all 626,048 in-scope TaxonRecord files are stored in
  docs/legacy-review-inventory.tsv (23,883 records) and docs/structured-review-inventory/part-00.tsv..part-13.tsv
  (602,165 records), with post-curation target_sha256 reconciliation verified via
  tests/test_corpus_review_inventory.py (#158); full-corpus 626,048-file hash/reproduction
  sweeps were not re-run during this pass due to host TCP/process pressure and remain
  enforced by CI quality gates.
- 'Four src/taxonmech/seed.py findings (#124/#63, #65, #118/#119, #69) remain open
  for Stage 5 disposition because scripts/verify_corpus.py enforces zero byte-for-byte
  drift between src/taxonmech/seed.py and all 626,048 committed YAML files in data/taxa/,
  requiring a dedicated full-corpus YAML and pages/taxon-details/*.json.gz regeneration
  pass.'
- 'Two findings (#8, #78) remain gated on upstream infrastructure tasks in INFRA_TASKS.md
  (taxonmech-infra-0001..0004) pending bulk kg-microbe trait-edge extraction, a corpus-wide
  release-pinned UniProtKB snapshot, and direct-vs-subtree attestation count alignment.'
related_reviews:
- repository: CultureBotAI/TaxonMech
  review_id: 20261024T021500Z-cycle3-stage4-corpus-record-review
  relationship: supersedes
- repository: CultureBotAI/TaxonMech
  review_id: 20261024T055500Z-cycle3-stage5-remediation-review
  relationship: follows_up
- repository: CultureBotAI/TaxonMech
  review_id: 20261025T062915Z-historical-review-metadata-batches-0014-0051
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261025T232500Z-cycle4-stage2-causal-graphs-curation
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261026T034000Z-cycle4-stage3-protein-examples
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261018T080549Z-structured-review-shard-part-00
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261018T080549Z-structured-review-shard-part-01
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261018T080549Z-structured-review-shard-part-02
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261018T080549Z-structured-review-shard-part-03
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261018T080549Z-structured-review-shard-part-04
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261018T080549Z-structured-review-shard-part-05
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261018T080549Z-structured-review-shard-part-06
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261018T080549Z-structured-review-shard-part-07
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261018T080549Z-structured-review-shard-part-08
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261018T080549Z-structured-review-shard-part-09
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261018T080549Z-structured-review-shard-part-10
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261018T080549Z-structured-review-shard-part-11
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261018T080549Z-structured-review-shard-part-12
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261019T052200Z-structured-review-shard-part-13
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261022T012228Z-stage5-remediation-review
  relationship: follows_up
- repository: CultureBotAI/TaxonMech
  review_id: 20261022T141500Z-cycle2-stage2-causal-graphs-curation
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261022T190800Z-cycle2-stage3-uniprot-protein-examples
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261021T163800Z-stage4-corpus-record-review
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261023T073200Z-cycle2-stage4-corpus-record-review
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261023T110500Z-cycle2-stage5-remediation-review
  relationship: follows_up
- repository: CultureBotAI/TaxonMech
  review_id: 20261023T193500Z-cycle3-stage2-causal-graphs-curation
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261023T224500Z-cycle3-stage3-protein-examples
  relationship: consolidates
notes:
- 'Cycle 4 Stage 4 re-verified all 4 previously resolved findings (#76, #83, and both
  #158 code and documentation/test findings), carried forward 6 open corpus-regeneration
  and infrastructure-gated findings (#124/#63, #65, #118/#119, #69, #8, #78), and
  identified 1 new open schema-documentation finding (schema-guide-missing-causal-node-uniprot-protein-slots
  under #78) for Cycle 4 Stage 5 grouped remediation.'
- 'All 15 causal-graph-enriched TaxonRecord files curated through Cycle 4 Stages 2-3
  (PRs #181, #183; 161 edges across 33 PMIDs, 51 GENE_OR_PROTEIN nodes across 23 live-verified
  UniProtKB accessions in curation/uniprot_proteins.tsv) are directly bound in targets
  with their current SHA-256 digests.'
- Parent workflow Cycle 4 Stage 4 evidence manifest saved at reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/evidence.yaml.
tags:
- cycle4-stage4-record-review
- full-corpus-review
- causal-graphs
- uniprot-proteins
```
