# Cycle 3 Stage 4 full-corpus record and cohort review consolidation (626,048 in-scope TaxonRecord files across 4 domains, 4 verdict strata, and 15 causal-graph/UniProtKB-enriched records)

- Review: 20261024T021500Z-cycle3-stage4-corpus-record-review
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-24T02:04:00Z
- Finished UTC: 2026-10-24T02:15:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Executed the Cycle 3 Stage 4 (record_review) full-corpus scientific and provenance audit across all 626,048 eligible TaxonRecord YAML files in data/taxa/ (Bacteria: 605,695; Archaea: 14,013; Eukaryota: 6,331; other: 9) at Git revision 13688091f74fd3c7d95b952097a063dbd28851f6 using .claude/skills/review-yaml-record/SKILL.md and .claude/skills/review-yaml-category/SKILL.md. Verified 100.0% inventory coverage (0 unreviewed, 0 overlap) and 100.0% target SHA-256 parity across docs/legacy-review-inventory.tsv (23,883 records) and docs/structured-review-inventory/part-00.tsv..part-13.tsv (602,165 records across 611 batches: pass=479,251, needs_curation=95,766, pass_with_limitations=27,118, blocked=30) via scripts/corpus_review_inventory.py --check --verify-target-sha256. Directly audited 27 representative species, strain, and boundary TaxonRecord files spanning all 4 domains, all 4 verdict strata, and all 15 records enriched in Cycle 2 and Cycle 3 Stages 2-3 (#155, #156, #163, #164) with 15 causal_graphs, 38 GENE_OR_PROTEIN nodes (17 unique live-verified UniProtKB accessions in curation/uniprot_proteins.tsv validated offline by validate_causal_graph_proteins()), and 110 evidence-backed edges. Confirmed 3 prior Stage 4/5 findings remain resolved (#76, #83, and #158 structured-inventory-verify-target-sha256-post-curation-drift), carried forward 6 unresolved corpus-wide findings (#124/#63, #65, #118/#119, #69, #8, #78) with updated Cycle 3 evidence, and identified 1 new actionable documentation/provenance finding (corpus-review-coverage-doc-stale-bundle-inventory-counts) where docs/corpus-review-coverage.md understates the canonical structured bundle inventory in reviews/structured/ and omits the post-curation target SHA-256 reconciliation contract implemented in #158.

## Scope And Provenance

Frozen 626,048-record TaxonMech corpus across data/taxa/bacteria/ (605,695), data/taxa/archaea/ (14,013), data/taxa/eukaryota/ (6,331), and data/taxa/other/ (9), reconciled against docs/legacy-review-inventory.tsv (23,883 records) and docs/structured-review-inventory/part-00.tsv..part-13.tsv (602,165 records) with 27 representative cross-domain, verdict-stratified, and causal-graph-enriched TaxonRecord files bound directly.

Selection: All 626,048 in-scope TaxonRecord files in curation/seed_scope.tsv and data/taxa/PATHS.tsv reconciled against the frozen review inventories, plus 27 directly bound representative records spanning Bacteria (13), Archaea (3), Eukaryota (8), and other (3) across pass, pass_with_limitations, needs_curation, blocked, and Cycle 2-3 causal-graph/UniProtKB cohorts.
Coverage: sampled; 27 reviewed / 626048 in the declared population.
Source: git_commit at Git base 13688091f74fd3c7d95b952097a063dbd28851f6.
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
| Native strict, LinkML schema, and offline UniProtKB protein validation on directly bound Cycle 3 Stage 4 exemplar records | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:5755, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | All 27 directly bound cross-domain exemplar and causal-graph TaxonRecord files pass scripts/validate_strict.py (including validate_causal_graph_proteins() against curation/uniprot_proteins.tsv) with 0 errors. |
| Native history validation across committed history records | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:5755, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | scripts/validate_history.py passes on all 26 repository history records against src/taxonmech/schema/history.yaml (#83 resolved in Cycle 1 Stage 5). |
| Required historical native-unit counts | unavailable | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:5755, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | Manifest-pinned upstream kg-microbe raw edge tables for GOLD, MEDIADIVE, MADIN, and BACTOTRAITS are not committed locally (though SHA-256 digests are documented in docs/HARMONIZATION.md), and subtree rollups apply to BacDive strains only (#8; taxonmech-infra-0004). |
| Full-corpus review coverage and disjointness check across all 626,048 records | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:5755, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | scripts/corpus_review_inventory.py --check verified 626,048 corpus records (23,883 legacy + 602,165 structured across 14 shards and 611 batches) with 0 unreviewed records and 0 overlaps. |
| Full-corpus target SHA-256 verification across structured review shards and superseding review bundles | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:5755, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | scripts/corpus_review_inventory.py --check --verify-target-sha256 exits 0 across all 602,165 structured-inventory records and reconciles post-curation target_sha256 digests against newer scientific review bundles in reviews/structured/*/review.yaml (#158 resolved in Cycle 2 Stage 5 PR #159). |
| Deterministic seeder reproduction check across all 626,048 TaxonRecord YAML files | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:5755, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | scripts/verify_corpus.py --workers 4 verified zero drift between src/taxonmech/seed.py (including curation/causal_graphs/*.yaml overlays) and all 626,048 committed YAML files. |
| Committed causal-graph and UniProtKB overlay regression suite | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750 | pytest tests/test_causal_graph_overlays.py passed all 5 tests verifying overlay loading, seeder merge, LinkML validation, offline curation/uniprot_proteins.tsv validation, and HTML rendering across all 15 maintained overlays. |

## Scientific And Domain Assessments

### Full-corpus review coverage (626,048 records), NCBI taxonomy alignment, and post-curation SHA-256 inventory state

identity: concern. Targets: NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:5755, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644.

All 626,048 in-scope TaxonRecord YAML files in data/taxa/ are accounted for without gap or overlap (23,883 legacy + 602,165 structured across 14 shards and 611 batches), match their pinned data/raw/ncbitaxon_taxa.tsv identifier, label, rank, domain, parent_taxon, and lineage, and pass scripts/corpus_review_inventory.py --check --verify-target-sha256 (0 unreconciled target SHA-256 mismatches after #158); however, docs/corpus-review-coverage.md still states that reviews/structured/ holds only 39 canonical bundles and omits the post-curation target SHA-256 reconciliation contract.

### GTDB closeMatch synonym/xref promotion, polyphyly suffix mangling, and pooled broadMatch genome/note semantics

nomenclature: concern. Targets: NCBITaxon:562, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:206, NCBITaxon:33952.

Across the 602,165 structured-review records, 95,766 records carry verdict needs_curation due to src/taxonmech/seed.py (lines 508-535) promoting skos:closeMatch GTDB species-cluster mappings to EXACT_SYNONYM and top-level xrefs (#124, #63), mangling 15,704 polyphyly-suffixed GTDB labels into fake trinomials at line 529 (#65), and emitting misleading pooled broadMatch genome totals (lines 636-650; #118) and inverted broadMatch notes (lines 522-524; #119) on 8,587 records.

### Cycle 3 causal_graphs and UniProtKB GENE_OR_PROTEIN coverage (15 records, 38 protein nodes across 17 unique UniProtKB accessions, 110 edges) and remaining corpus-wide prerequisites

completeness: concern. Targets: NCBITaxon:562, NCBITaxon:83333, NCBITaxon:511145, NCBITaxon:1423, NCBITaxon:224308, NCBITaxon:287, NCBITaxon:208964, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:235443, NCBITaxon:40410, NCBITaxon:283643, NCBITaxon:1859096, NCBITaxon:294750, NCBITaxon:5755, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644.

All 15 records enriched across Cycle 2 and Cycle 3 Stages 2-3 (#155, #156, #163, #164) pass strict LinkML validation, OAK ID-label correspondence, deterministic seeder reproduction, and offline + live UniProtKB verification across 15 causal graphs, 38 GENE_OR_PROTEIN nodes (17 unique UniProtKB accessions in curation/uniprot_proteins.tsv), and 110 evidence-backed edges; however, the remaining 626,033 records (99.998%) still have empty causal_graphs pending upstream kg-microbe bulk data/raw/taxon_trait_edges.tsv extraction (taxonmech-infra-0002) and a corpus-wide data/raw/ UniProtKB Reference Proteomes snapshot (taxonmech-infra-0003; #78).

## Findings

### causal-node-type-enum-and-mech-family-nav-drift: CausalNodeTypeEnum parity with TraitMech (RNA, GENETIC_ELEMENT, ORGANELLE) and NaturalProductMech family navigation remain resolved

minor / resolved / confirmed; issue key: cycle3-stage4-causal-node-type-enum-and-mech-family-nav-drift.

Verified in Cycle 3 Stage 4 that src/taxonmech/schema/taxonmech.yaml retains the 18-value CausalNodeTypeEnum superset (including RNA, GENETIC_ELEMENT, and ORGANELLE) and that README.md, CLAUDE.md, src/taxonmech/templates/{base,index}.html, and rendered pages include NaturalProductMech (#76, resolved in Cycle 1 Stage 5 PR #151).

Disposition: Resolved in Cycle 1 Stage 5 (PR #151) under #76 and verified intact at 13688091f74fd3c7d95b952097a063dbd28851f6.

### validate-history-bare-linkml-validate-path: scripts/validate_history.py resolves linkml-validate beside sys.executable across all 26 history records

minor / resolved / confirmed; issue key: cycle3-stage4-validate-history-bare-linkml-validate-path.

Verified in Cycle 3 Stage 4 that scripts/validate_history.py resolves Path(sys.executable).with_name('linkml-validate') before falling back to PATH and validates all 26 committed history records against src/taxonmech/schema/history.yaml (#83, resolved in Cycle 1 Stage 5 PR #151).

Disposition: Resolved in Cycle 1 Stage 5 (PR #151) under #83 and verified across all 26 history records at 13688091f74fd3c7d95b952097a063dbd28851f6.

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

Following Cycle 1 Stage 6 (PR #152), Cycle 2 Stages 2-3 and 6 (PRs #155, #156, #161), and Cycle 3 Stages 2-3 (PRs #163, #164), 15 TaxonRecord files across Bacteria (7), Archaea (2), and Eukaryota (6) now carry validated causal_graphs (110 edges, 38 GENE_OR_PROTEIN nodes across 17 unique live-verified UniProtKB accessions in curation/uniprot_proteins.tsv validated offline by validate_causal_graph_proteins()). However, the remaining 626,033 of 626,048 records (including 38,342 additional trait/medium-attested records) still have empty causal_graphs because: (1) data/raw/taxon_trait_edges.tsv has not yet been generated from an upstream local kg-microbe checkout using src/taxonmech/extract.py:extract_taxon_trait_edges (taxonmech-infra-0002); and (2) data/raw/ still lacks a corpus-wide release-pinned UniProtKB / Reference Proteomes TSV snapshot beyond the 17-entry curated reference table (taxonmech-infra-0003; tracked in INFRA_TASKS.md and https://github.com/CultureBotAI/TaxonMech/issues/78).

### structured-inventory-verify-target-sha256-post-curation-drift: scripts/corpus_review_inventory.py --check --verify-target-sha256 reconciles post-curation target SHA-256 digests against newer scientific review bundles without mutating historical shard rows

major / resolved / confirmed; issue key: cycle3-stage4-structured-inventory-verify-target-sha256-post-curation-drift.

Verified in Cycle 3 Stage 4 at 13688091f74fd3c7d95b952097a063dbd28851f6 that .venv/bin/python scripts/corpus_review_inventory.py --check --verify-target-sha256 exits 0 across all 602,165 structured-inventory records (including the 10 structured-shard records curated across Cycle 2 and Cycle 3 Stages 2-3) and all 49 saved structured review bundles in reviews/structured/ without mutating historical append-only review bundles (resolved in Cycle 2 Stage 5 PR #159 under https://github.com/CultureBotAI/TaxonMech/issues/158).

Disposition: Resolved in Cycle 2 Stage 5 (PR #159) under #158 and verified intact across Cycle 3 Stages 2-3 updates at 13688091f74fd3c7d95b952097a063dbd28851f6.

### corpus-review-coverage-doc-stale-bundle-inventory-counts: docs/corpus-review-coverage.md understates canonical structured review bundles in reviews/structured/ and omits the post-curation target_sha256 reconciliation contract (#158)

minor / open / confirmed; issue key: cycle3-stage4-corpus-review-coverage-doc-stale-bundle-inventory-counts.

In docs/corpus-review-coverage.md, Section 'Shard Architecture And Canonical Bundles' (line 40) states that reviews/structured/ retains only 14 kind: batch shard bundles and 25 representative single-record kind: record bundles (39 total), and Section 'Verification' (lines 51-55) states that scripts/corpus_review_inventory.py --check --verify-target-sha256 compares target YAML files on disk only against target_sha256 in docs/structured-review-inventory/part-*.tsv. Following Cycle 1-3 workflow reviews and Cycle 2 Stage 5 PR #159 (#158), reviews/structured/ also contains multi-stage scientific batch review bundles that load_latest_target_reviews() in scripts/corpus_review_inventory.py uses to reconcile post-curation target_sha256 digests for curated records (such as the 15 causal-graph/UniProtKB-enriched TaxonRecord files) without mutating historical append-only shard rows (tracked under https://github.com/CultureBotAI/TaxonMech/issues/158).

## Recommended Actions And Acceptance Checks

### remediate-corpus-review-coverage-doc-and-contract-test

In Cycle 3 Stage 5 (resolve_review_findings), update docs/corpus-review-coverage.md (Sections 'Shard Architecture And Canonical Bundles' and 'Verification') to document the multi-stage workflow review bundles in reviews/structured/ and the load_latest_target_reviews() post-curation target_sha256 reconciliation contract in scripts/corpus_review_inventory.py (#158), and add a regression check in tests/test_corpus_review_inventory.py.

- docs/corpus-review-coverage.md accurately describes canonical shard/record/stage bundles in reviews/structured/ and the post-curation target_sha256 reconciliation contract in scripts/corpus_review_inventory.py --check --verify-target-sha256
- .venv/bin/pytest -q tests/test_corpus_review_inventory.py exits 0

### remediate-seeder-gtdb-and-scope-provenance-cohorts

Gate skos:closeMatch GTDB promotion to EXACT_SYNONYM and xrefs (#124, #63), fix GTDB polyphyly suffix mangling (#65), align pooled GTDB broadMatch genome totals and notes (#118, #119), reconcile seed_scope reason strain counts (#69), and complete direct vs subtree source attestation count notes (#8) across src/taxonmech/seed.py and full-corpus regeneration.

- src/taxonmech/seed.py gates skos:closeMatch exact promotion and preserves GTDB polyphyly suffixes
- Pooled GTDB broadMatch notes and genome counts accurately reflect mapping direction and cluster scope
- Full corpus regenerates cleanly and passes scripts/verify_corpus.py, scripts/validate_strict.py, and scripts/render_pages.py --check

### implement-remaining-mechanism-and-protein-infrastructure-tasks

Execute remaining INFRA_TASKS.md tasks taxonmech-infra-0001..0004 in Cycle 3 Stage 6 to generate data/raw/taxon_trait_edges.tsv from upstream kg-microbe, expand the release-pinned UniProtKB / Reference Proteomes snapshot beyond curation/uniprot_proteins.tsv (#78), and finalize upstream edge-multiplicity provenance (#8).

- Pinned UniProtKB reference proteome inventory validates all 38 GENE_OR_PROTEIN nodes offline
- Granular trait-edge extraction supports reproducible causal_graphs expansion across trait-attested taxa

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| corpus-review-inventories | docs/legacy-review-inventory.tsv; docs/structured-review-inventory/part-00.tsv..part-13.tsv; docs/structured-review-batches.tsv; docs/corpus-review-coverage.md; 23,883 rows in docs/legacy-review-inventory.tsv and 602,165 rows across docs/structured-review-inventory/part-00.tsv..part-13.tsv | supports | Complete per-record review inventories covering all 626,048 TaxonRecord files in data/taxa/ (0 unreviewed, 0 overlap; structured verdicts: pass=479,251, pass_with_limitations=27,118, needs_curation=95,766, blocked=30), with post-curation target_sha256 digests reconciled cleanly by scripts/corpus_review_inventory.py --check --verify-target-sha256 (#158); docs/corpus-review-coverage.md still describes only 39 canonical bundles in reviews/structured/ and omits the post-curation target_sha256 reconciliation contract. |
| exemplar-target-records | data/taxa/bacteria/escherichia_coli.yaml; data/taxa/bacteria/escherichia_coli_k_12.yaml; data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml; data/taxa/bacteria/bacillus_subtilis.yaml; data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml; data/taxa/bacteria/pseudomonas_aeruginosa.yaml; data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml; data/taxa/bacteria/achromobacter_sp_jub104.yaml; data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml; data/taxa/bacteria/acinetobacter_bohemicus.yaml; data/taxa/bacteria/acidicaldus_organivorans.yaml; data/taxa/bacteria/campylobacter_sputorum.yaml; data/taxa/bacteria/acetobacterium_woodii.yaml; data/taxa/archaea/methanocaldococcus_jannaschii.yaml; data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml; data/taxa/archaea/saccharolobus_solfataricus.yaml; data/taxa/eukaryota/saccharomyces_cerevisiae.yaml; data/taxa/eukaryota/cryptococcus_neoformans.yaml; data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml; data/taxa/eukaryota/cryptococcus_deneoformans.yaml; data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml; data/taxa/eukaryota/cryptococcus_deuterogattii.yaml; data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml; data/taxa/eukaryota/acanthamoeba_castellanii.yaml; data/taxa/other/uncultured_organism.yaml; data/taxa/other/human_gut_metagenome.yaml; data/taxa/other/unidentified.yaml; Complete YAML content of 27 directly bound cross-domain, verdict-stratified, and causal-graph-enriched TaxonRecord files | supports | Verified taxon identity, lineage, nomenclature, synonyms, xrefs, taxonomy_mappings, source_attestations, strains, causal_graphs, and curation_history across 27 exemplar records spanning Bacteria (13), Archaea (3), Eukaryota (8), and other (3). |
| cycle3-causal-graph-and-uniprot-overlays | curation/causal_graphs/README.md; curation/causal_graphs/NCBITaxon_*.yaml; curation/uniprot_proteins.tsv; reviews/structured/20261023T193500Z-cycle3-stage2-causal-graphs-curation/review.yaml; reviews/structured/20261023T224500Z-cycle3-stage3-protein-examples/review.yaml; 15 maintained curation/causal_graphs/NCBITaxon_*.yaml overlays, curation/uniprot_proteins.tsv (17 rows), and Cycle 3 Stages 2-3 structured review bundles | supports | Verified 15 maintained causal-graph overlays seeded into 7 species and 8 strain TaxonRecord files (110 evidence-backed edges; 38 GENE_OR_PROTEIN nodes grounded to 17 unique live-verified UniProtKB accessions in curation/uniprot_proteins.tsv with exact organism_taxon_id, strain_id, proteome_id, gene_symbol, locus_tag, sequence_length, sequence_crc64, sequence_version, and entry_status). |
| raw-source-inventories | curation/seed_scope.tsv; data/raw/MANIFEST.yaml; data/raw/ncbitaxon_taxa.tsv; data/raw/gtdb_mappings.tsv; data/raw/gtdb_species.tsv; data/raw/bacdive_strains.tsv; data/raw/lpsn_names.tsv; curation/seed_scope.tsv (626,048 rows) and data/raw/*.tsv | supports | Pinned raw inventories verify exact NCBI taxon IDs and lineages across all 626,048 records and confirm persistent GTDB closeMatch fan-out (95,766 records), polyphyly suffix mangling (15,704 rows), pooled broadMatch genome counts/notes (8,587 records), and stale seed_scope strain-count reason strings. |
| schema-seeder-validator-code | src/taxonmech/schema/taxonmech.yaml; src/taxonmech/seed.py; src/taxonmech/extract.py; scripts/validate_strict.py; scripts/corpus_review_inventory.py; scripts/validate_history.py; docs/HARMONIZATION.md; docs/corpus-review-coverage.md; INFRA_TASKS.md; taxonmech.yaml:43-95,1200-1315,1520-1575; seed.py:508-535,636-715; validate_strict.py:217-370; corpus_review_inventory.py:185-330,381-445; corpus-review-coverage.md:34-55; INFRA_TASKS.md:33-286 | supports | Inspection of schema, seeder, extractor, strict/UniProt validator, inventory checker, and documentation confirms resolution of #76 and #83 in Cycle 1 Stage 5, resolution of #158 in Cycle 2 Stage 5 (PR #159), offline UniProtKB protein table validation in Cycle 2 Stage 6 (PR #161), persistent GTDB/scope seeder defects at src/taxonmech/seed.py lines 508-535, 636-650, and 691-702 (#124, #63, #65, #118, #119, #69), remaining corpus-wide trait/UniProt/attestation-note tasks in INFRA_TASKS.md (taxonmech-infra-0001..0004; #78, #8), and stale bundle-count and --verify-target-sha256 documentation in docs/corpus-review-coverage.md (lines 40, 51-55). |

## Limits And Additional Notes

- Per-record review rows for all 626,048 in-scope TaxonRecord files are stored in docs/legacy-review-inventory.tsv (23,883 records) and docs/structured-review-inventory/part-00.tsv..part-13.tsv (602,165 records) and checked via scripts/corpus_review_inventory.py --check --verify-target-sha256 to keep git pack size and validation runtime tractable.
- Stage 4 is a read-only review and finding-consolidation stage (.claude/skills/review-yaml-record/SKILL.md and .claude/skills/review-yaml-category/SKILL.md); documentation, validator, and seeder remediations are preserved for Cycle 3 Stage 5 (resolve_review_findings) and Stage 6 (infrastructure).
- Manifest-pinned upstream kg-microbe raw edge tables for GOLD, MEDIADIVE, MADIN, and BACTOTRAITS are not committed locally.
- Full-corpus review coverage verified: 626,048 total records = 23,883 legacy (docs/legacy-review-inventory.tsv) + 602,165 structured (docs/structured-review-inventory/part-00.tsv..part-13.tsv across 611 batches in docs/structured-review-batches.tsv); 0 unreviewed; 0 overlap; 0 unreconciled target_sha256 mismatches.
- All 15 causal-graph and UniProtKB protein-example records curated across Cycle 2 and Cycle 3 Stages 2-3 (#155, #156, #163, #164; 110 edges, 38 GENE_OR_PROTEIN nodes across 17 unique UniProtKB accessions in curation/uniprot_proteins.tsv) are directly bound and validated in this review.
- Parent workflow Cycle 3 Stage 4 evidence manifest saved at reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-04/revision-0001/evidence.yaml.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261024T021500Z-cycle3-stage4-corpus-record-review
kind: batch
repository: CultureBotAI/TaxonMech
title: Cycle 3 Stage 4 full-corpus record and cohort review consolidation (626,048
  in-scope TaxonRecord files across 4 domains, 4 verdict strata, and 15 causal-graph/UniProtKB-enriched
  records)
started_at: '2026-10-24T02:04:00Z'
finished_at: '2026-10-24T02:15:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: independent
  independence_basis: Cycle 3 Stage 4 full-corpus record and cohort review worker;
    verified all 626,048 in-scope TaxonRecord files via scripts/corpus_review_inventory.py
    --check (23,883 legacy-reviewed records in docs/legacy-review-inventory.tsv +
    602,165 structured-reviewed records across docs/structured-review-inventory/part-00.tsv..part-13.tsv
    with 0 unreviewed and 0 overlap) and scripts/corpus_review_inventory.py --check
    --verify-target-sha256, audited all 49 prior structured review bundles in reviews/structured/,
    and directly bound and validated 27 cross-domain/verdict exemplar TaxonRecord
    files (including all 15 records enriched with causal_graphs and live-verified
    UniProtKB GENE_OR_PROTEIN nodes across Cycle 2 and Cycle 3 Stages 2-3) prior to
    judgment.
skill: .claude/skills/review-yaml-category/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Executed the Cycle 3 Stage 4 (record_review) full-corpus scientific and
  provenance audit across all 626,048 eligible TaxonRecord YAML files in data/taxa/
  (Bacteria: 605,695; Archaea: 14,013; Eukaryota: 6,331; other: 9) at Git revision
  13688091f74fd3c7d95b952097a063dbd28851f6 using .claude/skills/review-yaml-record/SKILL.md
  and .claude/skills/review-yaml-category/SKILL.md. Verified 100.0% inventory coverage
  (0 unreviewed, 0 overlap) and 100.0% target SHA-256 parity across docs/legacy-review-inventory.tsv
  (23,883 records) and docs/structured-review-inventory/part-00.tsv..part-13.tsv (602,165
  records across 611 batches: pass=479,251, needs_curation=95,766, pass_with_limitations=27,118,
  blocked=30) via scripts/corpus_review_inventory.py --check --verify-target-sha256.
  Directly audited 27 representative species, strain, and boundary TaxonRecord files
  spanning all 4 domains, all 4 verdict strata, and all 15 records enriched in Cycle
  2 and Cycle 3 Stages 2-3 (#155, #156, #163, #164) with 15 causal_graphs, 38 GENE_OR_PROTEIN
  nodes (17 unique live-verified UniProtKB accessions in curation/uniprot_proteins.tsv
  validated offline by validate_causal_graph_proteins()), and 110 evidence-backed
  edges. Confirmed 3 prior Stage 4/5 findings remain resolved (#76, #83, and #158
  structured-inventory-verify-target-sha256-post-curation-drift), carried forward
  6 unresolved corpus-wide findings (#124/#63, #65, #118/#119, #69, #8, #78) with
  updated Cycle 3 evidence, and identified 1 new actionable documentation/provenance
  finding (corpus-review-coverage-doc-stale-bundle-inventory-counts) where docs/corpus-review-coverage.md
  understates the canonical structured bundle inventory in reviews/structured/ and
  omits the post-curation target SHA-256 reconciliation contract implemented in #158.'
source:
  git_revision: 13688091f74fd3c7d95b952097a063dbd28851f6
  state: git_commit
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
  - path: CLAUDE.md
    sha256: 4bf773b5e5eeccdece4b5b2e2420efebec5e49efa10f60b47f1697295bc1af75
    role: context
  - path: INFRA_TASKS.md
    sha256: 0ba8eeef1675ee22621b04fa97775dd2d0d34f65868db2d871417bbde7dade3e
    role: context
  - path: README.md
    sha256: f124588428a14db89a780e6dd6d05e039ec9e6d0e4473163d1cc13fb36bb2353
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
    sha256: 759ef444b1890559846fd4ab7818c8dbca74ab6bee2f6b9466a1aff6b5f4d8c8
    role: context
  - path: curation/causal_graphs/NCBITaxon_1423.yaml
    sha256: a2bcc804ab05370178b951a7c8b820b6b18551300dde128c58e8c376a649254d
    role: context
  - path: curation/causal_graphs/NCBITaxon_1859096.yaml
    sha256: 2a723170e1c400fd43c04ec70b169067d8781f0a0b481a85ea403d6b56890d82
    role: context
  - path: curation/causal_graphs/NCBITaxon_208964.yaml
    sha256: 18c3076c807e45361f4987588c8c143067185873ead415d5c3c1725e04d84151
    role: context
  - path: curation/causal_graphs/NCBITaxon_2190.yaml
    sha256: cbaac6847251572d0b135f7a17b6d3648d0d64a958cf48ecd7269311351904c9
    role: context
  - path: curation/causal_graphs/NCBITaxon_224308.yaml
    sha256: 8d346f14555011a12112e936a449d5b0df98ead2be8617fe5b82b90af000164c
    role: context
  - path: curation/causal_graphs/NCBITaxon_235443.yaml
    sha256: c32f3c24d72edc88df8f966724b48cad1f36b5cc322c86b198f702a074ff89b9
    role: context
  - path: curation/causal_graphs/NCBITaxon_243232.yaml
    sha256: 80a15b658b55228b09ac37cb1be2ffbb6c3a9ecf43b4ef6d7ca73c369504576e
    role: context
  - path: curation/causal_graphs/NCBITaxon_283643.yaml
    sha256: 495437a604560f0fe7981b9a294dbcf54fa736275cc11f136bba81c7e099d872
    role: context
  - path: curation/causal_graphs/NCBITaxon_287.yaml
    sha256: dbb0de17966f3ea8a32d4322fc3853a8af0129ab6ddcad2f6da62fb60d8a21c0
    role: context
  - path: curation/causal_graphs/NCBITaxon_294750.yaml
    sha256: 3cdfd1a5ef7f74e1fe226eaa85184b36463e7d0e40622202f66f44cebb0c4178
    role: context
  - path: curation/causal_graphs/NCBITaxon_40410.yaml
    sha256: 8dc5efc292fd2776a43e8690a1a15a93650b58a40f8fcd761d09c0e3819f5a07
    role: context
  - path: curation/causal_graphs/NCBITaxon_511145.yaml
    sha256: 2c86b8914d6ec80950d7e5e133286fcde11a98bf6e5503266f67187dce2fe1c5
    role: context
  - path: curation/causal_graphs/NCBITaxon_5207.yaml
    sha256: 9e6b09c7b846c0f169f47dc4f4c61bf0c4adde12f7d75ba8ad212c0e02cfe2d6
    role: context
  - path: curation/causal_graphs/NCBITaxon_562.yaml
    sha256: ba35b933449e45a6b9ad3c6106d2eb5b9b9c2dfeb4cb53c20cb37003473be327
    role: context
  - path: curation/causal_graphs/NCBITaxon_83333.yaml
    sha256: 62502296f559cc65a75a8a22d51b579434bcb953696360c2a737249ec82605b0
    role: context
  - path: curation/causal_graphs/README.md
    sha256: bbc7a30df0a707e424d8ac271c06c7307e6d1c257c4d2e3a23a997a327f14414
    role: context
  - path: curation/seed_scope.tsv
    sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
    role: context
  - path: curation/uniprot_proteins.tsv
    sha256: 72dda0662db8c854ac864ecf983f9e5290fbb1a7bc9c738b3307ca1f80a72100
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
    sha256: 8f2e93dac1fe0df25bd5b431b91da4ee25c1fa47cee2d50d3f652b256a4b7c28
    role: target
  - path: data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml
    sha256: 512957ad23aa1a4977e1fb04d817d38d97484e24aa2ba04d4a90cc2df5b52597
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
    sha256: b3a66714c13080f989c729e5242236ce243e84df1ba74338c4b8f1bde8371a8c
    role: target
  - path: data/taxa/bacteria/bacillus_subtilis_subsp_subtilis_str_168.yaml
    sha256: 01184a5f9ad2b8aed895db3db59823de41edc2319877cc876ef8b441d5e97180
    role: target
  - path: data/taxa/bacteria/campylobacter_sputorum.yaml
    sha256: d36195dc394fa4c68dd65292205411c4cd1fbc710f6e4e6e0bd4379c39e53847
    role: target
  - path: data/taxa/bacteria/escherichia_coli.yaml
    sha256: b1f6200890dbfc3211fe3d922eb7049454eac79f1ab32047e9d5749b1ecea7c0
    role: target
  - path: data/taxa/bacteria/escherichia_coli_k_12.yaml
    sha256: 12e7e2ec83daacbd3971ce9907b0ee74cc530b02881598928976b50d67254239
    role: target
  - path: data/taxa/bacteria/escherichia_coli_str_k_12_substr_mg1655.yaml
    sha256: a678f06a6a67c5beafe0816fe787031de3f72afd65c8aa3a3cf74aadefa5f106
    role: target
  - path: data/taxa/bacteria/pseudomonas_aeruginosa.yaml
    sha256: 0403c1c7d2dbd5c73a35afc354e804cfc48d7230f2bb10743b26b4e0d4ef3f7e
    role: target
  - path: data/taxa/bacteria/pseudomonas_aeruginosa_pao1.yaml
    sha256: 85c66c947c707327e58dd513993bfd2299c71c633a1d464db8c7a343cbbdffb0
    role: target
  - path: data/taxa/eukaryota/acanthamoeba_castellanii.yaml
    sha256: 969e4e46219d0635b36eca944bc6fe814538743b17ae1923a2b7eed1b6870144
    role: target
  - path: data/taxa/eukaryota/cryptococcus_deneoformans.yaml
    sha256: 83f9a0792f3a026c1fefbda639b05e3e27c34677a34fca1b9eb6e03e11a7a776
    role: target
  - path: data/taxa/eukaryota/cryptococcus_deneoformans_b_3501a.yaml
    sha256: 0f5119d3886a851399352ec8c74eff620303f13ec596d7c8a30657cf5495d383
    role: target
  - path: data/taxa/eukaryota/cryptococcus_deuterogattii.yaml
    sha256: e56a14a78663cdf40937b3e25a6f4b249086141f99967b6bfea90e675d7b947b
    role: target
  - path: data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml
    sha256: 60f524f306e14f2615b4dcfb41a9776aed01be4f2d12ef467da13c4c7e2717cc
    role: target
  - path: data/taxa/eukaryota/cryptococcus_neoformans.yaml
    sha256: 53de8a23fe61f20e330b4cef54f44b16c14da747e641ef48def9d835338b5f5f
    role: target
  - path: data/taxa/eukaryota/cryptococcus_neoformans_h99.yaml
    sha256: feee963ea3cf34d7bfd6b3d7f868daf752098e3ddaaddea79b74459ca558f720
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
    sha256: ca93c094e56f822e0896b7f658b24677db07bb657e05ba1e0a38601b37a131d6
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
  - path: reviews/workflow/latest.yaml
    sha256: 9a6a0ff99af79b8a686174cd7ee870d148f2f23c01fc6a6379739da8705579e2
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/corpus_review_inventory.py
    sha256: 75b6c87628432be42656d1d523025b3a30780b9ed836d1d34f9491ff4a8dabb1
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
    sha256: 733ab9febfdd56e4b73b8acce3ce6c15de1fe201f31f8769d217e97530578347
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
    sha256: 0f2d059fab955585d80d8f0a3c2121c80682d1341a0420fdc7e3fc50726080c5
    role: context
  - path: tests/test_corpus_review_inventory.py
    sha256: 0b4a51338ed8f397b76793346780af5128dcb77aa1be1bf407dc5098a50e1ccd
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
    and Cycle 2-3 causal-graph/UniProtKB cohorts.
  coverage: sampled
  population_size: 626048
  sampling_method: Complete 626,048-record inventory census via scripts/corpus_review_inventory.py
    --check (23,883 legacy + 602,165 structured; 0 unreviewed; 0 overlap) plus full-corpus
    target SHA-256 verification via scripts/corpus_review_inventory.py --check --verify-target-sha256
    against post-Cycle-3-Stage-3 corpus bytes (626,033 unchanged records + 15 causal-graph-enriched
    records reconciled against 20261022T190800Z-cycle2-stage3-uniprot-protein-examples,
    20261023T193500Z-cycle3-stage2-causal-graphs-curation, and 20261023T224500Z-cycle3-stage3-protein-examples),
    with 27 representative TaxonRecord files bound directly in targets.
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
  name: Native strict, LinkML schema, and offline UniProtKB protein validation on
    directly bound Cycle 3 Stage 4 exemplar records
  status: passed
  required: true
  summary: All 27 directly bound cross-domain exemplar and causal-graph TaxonRecord
    files pass scripts/validate_strict.py (including validate_causal_graph_proteins()
    against curation/uniprot_proteins.tsv) with 0 errors.
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
  summary: scripts/validate_history.py passes on all 26 repository history records
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
- check_id: corpus-review-inventory-sha256
  name: Full-corpus target SHA-256 verification across structured review shards and
    superseding review bundles
  status: passed
  required: true
  summary: 'scripts/corpus_review_inventory.py --check --verify-target-sha256 exits
    0 across all 602,165 structured-inventory records and reconciles post-curation
    target_sha256 digests against newer scientific review bundles in reviews/structured/*/review.yaml
    (#158 resolved in Cycle 2 Stage 5 PR #159).'
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
  command: .venv/bin/python scripts/corpus_review_inventory.py --check --verify-target-sha256
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - corpus-review-inventories
  - cycle3-causal-graph-and-uniprot-overlays
- check_id: verify-corpus-reproduction
  name: Deterministic seeder reproduction check across all 626,048 TaxonRecord YAML
    files
  status: passed
  required: true
  summary: scripts/verify_corpus.py --workers 4 verified zero drift between src/taxonmech/seed.py
    (including curation/causal_graphs/*.yaml overlays) and all 626,048 committed YAML
    files.
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
  command: .venv/bin/python scripts/verify_corpus.py --workers 4
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema-seeder-validator-code
  - cycle3-causal-graph-and-uniprot-overlays
- check_id: causal-graph-overlay-roundtrip-tests
  name: Committed causal-graph and UniProtKB overlay regression suite
  status: passed
  required: true
  summary: pytest tests/test_causal_graph_overlays.py passed all 5 tests verifying
    overlay loading, seeder merge, LinkML validation, offline curation/uniprot_proteins.tsv
    validation, and HTML rendering across all 15 maintained overlays.
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
  - cycle3-causal-graph-and-uniprot-overlays
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
    target_sha256 digests reconciled cleanly by scripts/corpus_review_inventory.py
    --check --verify-target-sha256 (#158); docs/corpus-review-coverage.md still describes
    only 39 canonical bundles in reviews/structured/ and omits the post-curation target_sha256
    reconciliation contract.'
  accessed_at: '2026-10-24T02:15:00Z'
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
  accessed_at: '2026-10-24T02:15:00Z'
  support: supports
  snapshot_sha256: b1f6200890dbfc3211fe3d922eb7049454eac79f1ab32047e9d5749b1ecea7c0
- evidence_id: cycle3-causal-graph-and-uniprot-overlays
  kind: record_content
  reference: curation/causal_graphs/README.md; curation/causal_graphs/NCBITaxon_*.yaml;
    curation/uniprot_proteins.tsv; reviews/structured/20261023T193500Z-cycle3-stage2-causal-graphs-curation/review.yaml;
    reviews/structured/20261023T224500Z-cycle3-stage3-protein-examples/review.yaml
  locator: 15 maintained curation/causal_graphs/NCBITaxon_*.yaml overlays, curation/uniprot_proteins.tsv
    (17 rows), and Cycle 3 Stages 2-3 structured review bundles
  summary: Verified 15 maintained causal-graph overlays seeded into 7 species and
    8 strain TaxonRecord files (110 evidence-backed edges; 38 GENE_OR_PROTEIN nodes
    grounded to 17 unique live-verified UniProtKB accessions in curation/uniprot_proteins.tsv
    with exact organism_taxon_id, strain_id, proteome_id, gene_symbol, locus_tag,
    sequence_length, sequence_crc64, sequence_version, and entry_status).
  accessed_at: '2026-10-24T02:15:00Z'
  support: supports
  snapshot_sha256: 7390287e69e64500a83482da9739f503fc1c96fb21e8e47c0419218125646959
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
  accessed_at: '2026-10-24T02:15:00Z'
  support: supports
  snapshot_sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
- evidence_id: schema-seeder-validator-code
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml; src/taxonmech/seed.py; src/taxonmech/extract.py;
    scripts/validate_strict.py; scripts/corpus_review_inventory.py; scripts/validate_history.py;
    docs/HARMONIZATION.md; docs/corpus-review-coverage.md; INFRA_TASKS.md
  locator: taxonmech.yaml:43-95,1200-1315,1520-1575; seed.py:508-535,636-715; validate_strict.py:217-370;
    corpus_review_inventory.py:185-330,381-445; corpus-review-coverage.md:34-55; INFRA_TASKS.md:33-286
  summary: 'Inspection of schema, seeder, extractor, strict/UniProt validator, inventory
    checker, and documentation confirms resolution of #76 and #83 in Cycle 1 Stage
    5, resolution of #158 in Cycle 2 Stage 5 (PR #159), offline UniProtKB protein
    table validation in Cycle 2 Stage 6 (PR #161), persistent GTDB/scope seeder defects
    at src/taxonmech/seed.py lines 508-535, 636-650, and 691-702 (#124, #63, #65,
    #118, #119, #69), remaining corpus-wide trait/UniProt/attestation-note tasks in
    INFRA_TASKS.md (taxonmech-infra-0001..0004; #78, #8), and stale bundle-count and
    --verify-target-sha256 documentation in docs/corpus-review-coverage.md (lines
    40, 51-55).'
  accessed_at: '2026-10-24T02:15:00Z'
  support: supports
  snapshot_sha256: 733ab9febfdd56e4b73b8acce3ce6c15de1fe201f31f8769d217e97530578347
assessments:
- assessment_id: corpus-review-coverage-and-identity
  area: identity
  topic: Full-corpus review coverage (626,048 records), NCBI taxonomy alignment, and
    post-curation SHA-256 inventory state
  outcome: concern
  summary: 'All 626,048 in-scope TaxonRecord YAML files in data/taxa/ are accounted
    for without gap or overlap (23,883 legacy + 602,165 structured across 14 shards
    and 611 batches), match their pinned data/raw/ncbitaxon_taxa.tsv identifier, label,
    rank, domain, parent_taxon, and lineage, and pass scripts/corpus_review_inventory.py
    --check --verify-target-sha256 (0 unreconciled target SHA-256 mismatches after
    #158); however, docs/corpus-review-coverage.md still states that reviews/structured/
    holds only 39 canonical bundles and omits the post-curation target SHA-256 reconciliation
    contract.'
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
  - cycle3-causal-graph-and-uniprot-overlays
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
  topic: Cycle 3 causal_graphs and UniProtKB GENE_OR_PROTEIN coverage (15 records,
    38 protein nodes across 17 unique UniProtKB accessions, 110 edges) and remaining
    corpus-wide prerequisites
  outcome: concern
  summary: 'All 15 records enriched across Cycle 2 and Cycle 3 Stages 2-3 (#155, #156,
    #163, #164) pass strict LinkML validation, OAK ID-label correspondence, deterministic
    seeder reproduction, and offline + live UniProtKB verification across 15 causal
    graphs, 38 GENE_OR_PROTEIN nodes (17 unique UniProtKB accessions in curation/uniprot_proteins.tsv),
    and 110 evidence-backed edges; however, the remaining 626,033 records (99.998%)
    still have empty causal_graphs pending upstream kg-microbe bulk data/raw/taxon_trait_edges.tsv
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
  - cycle3-causal-graph-and-uniprot-overlays
  - schema-seeder-validator-code
  metrics:
  - name: causal_graph_enriched_records
    value: 15.0
    unit: records
    definition: TaxonRecord files populated with maintained curation/causal_graphs/*.yaml
      overlays in Cycles 2-3.
    denominator: 626048
    minimum: 0.0
    maximum: 626048.0
  - name: verified_uniprot_gene_or_protein_nodes
    value: 38.0
    unit: nodes
    definition: GENE_OR_PROTEIN CausalNode instances grounded to live-verified and
      offline-validated UniProtKB accessions across the 15 causal-graph records.
    denominator: 38
    minimum: 0.0
    maximum: 38.0
  - name: verified_causal_edges
    value: 110.0
    unit: edges
    definition: Evidence-backed CausalEdge instances with primary PMID/DOI citations
      across the 15 causal-graph records.
    denominator: 110
    minimum: 0.0
    maximum: 110.0
findings:
- finding_id: causal-node-type-enum-and-mech-family-nav-drift
  issue_key: cycle3-stage4-causal-node-type-enum-and-mech-family-nav-drift
  category: schema
  severity: minor
  status: resolved
  certainty: confirmed
  title: CausalNodeTypeEnum parity with TraitMech (RNA, GENETIC_ELEMENT, ORGANELLE)
    and NaturalProductMech family navigation remain resolved
  description: 'Verified in Cycle 3 Stage 4 that src/taxonmech/schema/taxonmech.yaml
    retains the 18-value CausalNodeTypeEnum superset (including RNA, GENETIC_ELEMENT,
    and ORGANELLE) and that README.md, CLAUDE.md, src/taxonmech/templates/{base,index}.html,
    and rendered pages include NaturalProductMech (#76, resolved in Cycle 1 Stage
    5 PR #151).'
  disposition_reason: 'Resolved in Cycle 1 Stage 5 (PR #151) under #76 and verified
    intact at 13688091f74fd3c7d95b952097a063dbd28851f6.'
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
    path: CLAUDE.md
    role: Agent architecture and Mech suite documentation
  rule_id: src/taxonmech/schema/taxonmech.yaml:CausalNodeTypeEnum
  normalization_reason: Retain verified resolution from Cycle 1 Stage 5 (#76).
- finding_id: validate-history-bare-linkml-validate-path
  issue_key: cycle3-stage4-validate-history-bare-linkml-validate-path
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: scripts/validate_history.py resolves linkml-validate beside sys.executable
    across all 26 history records
  description: 'Verified in Cycle 3 Stage 4 that scripts/validate_history.py resolves
    Path(sys.executable).with_name(''linkml-validate'') before falling back to PATH
    and validates all 26 committed history records against src/taxonmech/schema/history.yaml
    (#83, resolved in Cycle 1 Stage 5 PR #151).'
  disposition_reason: 'Resolved in Cycle 1 Stage 5 (PR #151) under #83 and verified
    across all 26 history records at 13688091f74fd3c7d95b952097a063dbd28851f6.'
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
    #155, #156, #161), and Cycle 3 Stages 2-3 (PRs #163, #164), 15 TaxonRecord files
    across Bacteria (7), Archaea (2), and Eukaryota (6) now carry validated causal_graphs
    (110 edges, 38 GENE_OR_PROTEIN nodes across 17 unique live-verified UniProtKB
    accessions in curation/uniprot_proteins.tsv validated offline by validate_causal_graph_proteins()).
    However, the remaining 626,033 of 626,048 records (including 38,342 additional
    trait/medium-attested records) still have empty causal_graphs because: (1) data/raw/taxon_trait_edges.tsv
    has not yet been generated from an upstream local kg-microbe checkout using src/taxonmech/extract.py:extract_taxon_trait_edges
    (taxonmech-infra-0002); and (2) data/raw/ still lacks a corpus-wide release-pinned
    UniProtKB / Reference Proteomes TSV snapshot beyond the 17-entry curated reference
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
  - cycle3-causal-graph-and-uniprot-overlays
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
- finding_id: structured-inventory-verify-target-sha256-post-curation-drift
  issue_key: cycle3-stage4-structured-inventory-verify-target-sha256-post-curation-drift
  category: provenance
  severity: major
  status: resolved
  certainty: confirmed
  title: scripts/corpus_review_inventory.py --check --verify-target-sha256 reconciles
    post-curation target SHA-256 digests against newer scientific review bundles without
    mutating historical shard rows
  description: 'Verified in Cycle 3 Stage 4 at 13688091f74fd3c7d95b952097a063dbd28851f6
    that .venv/bin/python scripts/corpus_review_inventory.py --check --verify-target-sha256
    exits 0 across all 602,165 structured-inventory records (including the 10 structured-shard
    records curated across Cycle 2 and Cycle 3 Stages 2-3) and all 49 saved structured
    review bundles in reviews/structured/ without mutating historical append-only
    review bundles (resolved in Cycle 2 Stage 5 PR #159 under https://github.com/CultureBotAI/TaxonMech/issues/158).'
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
  - cycle3-causal-graph-and-uniprot-overlays
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
  disposition_reason: 'Resolved in Cycle 2 Stage 5 (PR #159) under #158 and verified
    intact across Cycle 3 Stages 2-3 updates at 13688091f74fd3c7d95b952097a063dbd28851f6.'
- finding_id: corpus-review-coverage-doc-stale-bundle-inventory-counts
  issue_key: cycle3-stage4-corpus-review-coverage-doc-stale-bundle-inventory-counts
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: docs/corpus-review-coverage.md understates canonical structured review bundles
    in reviews/structured/ and omits the post-curation target_sha256 reconciliation
    contract (#158)
  description: 'In docs/corpus-review-coverage.md, Section ''Shard Architecture And
    Canonical Bundles'' (line 40) states that reviews/structured/ retains only 14
    kind: batch shard bundles and 25 representative single-record kind: record bundles
    (39 total), and Section ''Verification'' (lines 51-55) states that scripts/corpus_review_inventory.py
    --check --verify-target-sha256 compares target YAML files on disk only against
    target_sha256 in docs/structured-review-inventory/part-*.tsv. Following Cycle
    1-3 workflow reviews and Cycle 2 Stage 5 PR #159 (#158), reviews/structured/ also
    contains multi-stage scientific batch review bundles that load_latest_target_reviews()
    in scripts/corpus_review_inventory.py uses to reconcile post-curation target_sha256
    digests for curated records (such as the 15 causal-graph/UniProtKB-enriched TaxonRecord
    files) without mutating historical append-only shard rows (tracked under https://github.com/CultureBotAI/TaxonMech/issues/158).'
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
  - cycle3-causal-graph-and-uniprot-overlays
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
actions:
- action_id: remediate-corpus-review-coverage-doc-and-contract-test
  description: In Cycle 3 Stage 5 (resolve_review_findings), update docs/corpus-review-coverage.md
    (Sections 'Shard Architecture And Canonical Bundles' and 'Verification') to document
    the multi-stage workflow review bundles in reviews/structured/ and the load_latest_target_reviews()
    post-curation target_sha256 reconciliation contract in scripts/corpus_review_inventory.py
    (#158), and add a regression check in tests/test_corpus_review_inventory.py.
  finding_ids:
  - corpus-review-coverage-doc-stale-bundle-inventory-counts
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
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: docs/corpus-review-coverage.md
    role: Full-corpus review coverage architecture and verification documentation
  - repository: CultureBotAI/TaxonMech
    path: tests/test_corpus_review_inventory.py
    role: Corpus review inventory regression test suite
  acceptance_checks:
  - docs/corpus-review-coverage.md accurately describes canonical shard/record/stage
    bundles in reviews/structured/ and the post-curation target_sha256 reconciliation
    contract in scripts/corpus_review_inventory.py --check --verify-target-sha256
  - .venv/bin/pytest -q tests/test_corpus_review_inventory.py exits 0
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
    Cycle 3 Stage 6 to generate data/raw/taxon_trait_edges.tsv from upstream kg-microbe,
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
  - Pinned UniProtKB reference proteome inventory validates all 38 GENE_OR_PROTEIN
    nodes offline
  - Granular trait-edge extraction supports reproducible causal_graphs expansion across
    trait-attested taxa
limitations:
- Per-record review rows for all 626,048 in-scope TaxonRecord files are stored in
  docs/legacy-review-inventory.tsv (23,883 records) and docs/structured-review-inventory/part-00.tsv..part-13.tsv
  (602,165 records) and checked via scripts/corpus_review_inventory.py --check --verify-target-sha256
  to keep git pack size and validation runtime tractable.
- Stage 4 is a read-only review and finding-consolidation stage (.claude/skills/review-yaml-record/SKILL.md
  and .claude/skills/review-yaml-category/SKILL.md); documentation, validator, and
  seeder remediations are preserved for Cycle 3 Stage 5 (resolve_review_findings)
  and Stage 6 (infrastructure).
- Manifest-pinned upstream kg-microbe raw edge tables for GOLD, MEDIADIVE, MADIN,
  and BACTOTRAITS are not committed locally.
related_reviews:
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
  relationship: supersedes
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
- 'Full-corpus review coverage verified: 626,048 total records = 23,883 legacy (docs/legacy-review-inventory.tsv)
  + 602,165 structured (docs/structured-review-inventory/part-00.tsv..part-13.tsv
  across 611 batches in docs/structured-review-batches.tsv); 0 unreviewed; 0 overlap;
  0 unreconciled target_sha256 mismatches.'
- 'All 15 causal-graph and UniProtKB protein-example records curated across Cycle
  2 and Cycle 3 Stages 2-3 (#155, #156, #163, #164; 110 edges, 38 GENE_OR_PROTEIN
  nodes across 17 unique UniProtKB accessions in curation/uniprot_proteins.tsv) are
  directly bound and validated in this review.'
- Parent workflow Cycle 3 Stage 4 evidence manifest saved at reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-04/revision-0001/evidence.yaml.
tags:
- cycle3-stage4-record-review
- corpus-review-consolidation
- cohort-review
```
