# Stage 5 grouped remediation verification and carry-forward disposition review (2 findings resolved under #76 and #83; 6 corpus-regeneration and Stage 6 infrastructure findings deferred with linked issues)

- Review: 20261022T012228Z-stage5-remediation-review
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-22T01:14:28Z
- Finished UTC: 2026-10-22T01:22:28Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Executed Cycle 1 Stage 5 (resolve_review_findings) grouped remediation and post-remediation verification against Stage 4 review 20261021T163800Z-stage4-corpus-record-review. Grouped all 8 Stage 4 findings by root cause and repair ownership, deduplicated against open GitHub issues in CultureBotAI/TaxonMech, and resolved 2 directly actionable repository findings: (1) causal-node-type-enum-and-mech-family-nav-drift (#76) by adding RNA, GENETIC_ELEMENT, and ORGANELLE to CausalNodeTypeEnum in src/taxonmech/schema/taxonmech.yaml (completing the 18-value superset of TraitMech and HabitatMech) and adding NaturalProductMech to README.md, CLAUDE.md, src/taxonmech/templates/{base,index}.html, and all 6,372 rendered HTML pages in pages/; and (2) validate-history-bare-linkml-validate-path (#83) by resolving Path(sys.executable).with_name('linkml-validate') in scripts/validate_history.py before falling back to PATH. Recorded explicit deferred dispositions and canonical open GitHub issue links (#124, #65, #118, #69, #8, #78) for the 4 src/taxonmech/seed.py findings that require a 626,048-record full-corpus regeneration under scripts/verify_corpus.py and the 2 findings gated on Stage 6 infrastructure tasks (INFRA_TASKS.md taxonmech-infra-0001..0004).

## Scope And Provenance

Frozen 626,048-record TaxonMech corpus across data/taxa/bacteria/ (605,695), data/taxa/archaea/ (14,013), data/taxa/eukaryota/ (6,331), and data/taxa/other/ (9), reconciled against docs/legacy-review-inventory.tsv (23,883 records) and docs/structured-review-inventory/part-00.tsv..part-13.tsv (602,165 records) with 20 representative cross-domain and verdict-stratified TaxonRecord files bound directly.

Selection: All 626,048 in-scope TaxonRecord files in curation/seed_scope.tsv and data/taxa/PATHS.tsv verified by SHA-256 digest in the frozen review inventories, plus 20 directly bound representative records spanning Bacteria (10), Archaea (3), Eukaryota (4), and other (3) across pass, pass_with_limitations, needs_curation, and blocked cohorts.
Coverage: sampled; 20 reviewed / 626048 in the declared population.
Source: working_tree at Git base 5bab842c1acde531640142f784b013af168b9a0f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:562 | data/taxa/bacteria/escherichia_coli.yaml | generated | Escherichia coli |
| NCBITaxon:83333 | data/taxa/bacteria/escherichia_coli_k_12.yaml | generated | Escherichia coli K-12 |
| NCBITaxon:1423 | data/taxa/bacteria/bacillus_subtilis.yaml | generated | Bacillus subtilis |
| NCBITaxon:287 | data/taxa/bacteria/pseudomonas_aeruginosa.yaml | generated | Pseudomonas aeruginosa |
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
| NCBITaxon:5755 | data/taxa/eukaryota/acanthamoeba_castellanii.yaml | generated | Acanthamoeba castellanii |
| NCBITaxon:1859096 | data/taxa/eukaryota/cryptococcus_deuterogattii.yaml | generated | Cryptococcus deuterogattii |
| NCBITaxon:155900 | data/taxa/other/uncultured_organism.yaml | generated | uncultured organism |
| NCBITaxon:408170 | data/taxa/other/human_gut_metagenome.yaml | generated | human gut metagenome |
| NCBITaxon:32644 | data/taxa/other/unidentified.yaml | generated | unidentified |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native strict and LinkML schema validation on directly bound Stage 4 exemplar records | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:1423, NCBITaxon:287, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:5755, NCBITaxon:1859096, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | All 20 directly bound cross-domain exemplar TaxonRecord files pass scripts/validate_strict.py with 0 errors. |
| Native history validation across committed history records | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:1423, NCBITaxon:287, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:5755, NCBITaxon:1859096, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | scripts/validate_history.py resolves linkml-validate beside sys.executable and passes on all 17 repository history records even when .venv/bin is stripped from PATH (#83 resolved). |
| Required historical native-unit counts | unavailable | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:1423, NCBITaxon:287, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:5755, NCBITaxon:1859096, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | Manifest-pinned upstream kg-microbe raw edge tables for GOLD, MEDIADIVE, MADIN, and BACTOTRAITS are not committed locally, and subtree rollups apply to BacDive strains only (#8). |
| Full-corpus review coverage and target SHA-256 verification across all 626,048 records | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:1423, NCBITaxon:287, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:5755, NCBITaxon:1859096, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | scripts/corpus_review_inventory.py --check --verify-target-sha256 verified 626,048 corpus records (23,883 legacy + 602,165 structured across 14 shards and 611 batches) with 0 unreviewed records, 0 overlaps, and 0 SHA-256 mismatches. |
| Deterministic seeder reproduction check across all 626,048 TaxonRecord YAML files | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:1423, NCBITaxon:287, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:5755, NCBITaxon:1859096, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | scripts/verify_corpus.py --workers 4 verified zero drift between src/taxonmech/seed.py and all 626,048 committed YAML files. |
| Stage 5 regression tests for CausalNodeTypeEnum parity, Mech family navigation, and validate_history executable resolution | passed | True | NCBITaxon:562, NCBITaxon:83333, NCBITaxon:1423, NCBITaxon:287, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:5755, NCBITaxon:1859096, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644 | pytest tests/test_schema.py tests/test_html_navigation.py tests/test_new_history_record.py and template/page parity verification across all 6,372 HTML files in pages/ passed with 0 errors. |

## Scientific And Domain Assessments

### Full-corpus review coverage (626,048 records), SHA-256 inventory reconciliation, and NCBI taxonomy alignment

identity: supported. Targets: NCBITaxon:562, NCBITaxon:83333, NCBITaxon:1423, NCBITaxon:287, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:5755, NCBITaxon:1859096, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644.

All 626,048 in-scope TaxonRecord YAML files in data/taxa/ are accounted for without gap or overlap (23,883 legacy + 602,165 structured across 14 shards and 611 batches) and match their pinned data/raw/ncbitaxon_taxa.tsv identifier, label, rank, domain, parent_taxon, and lineage.

### Stage 5 remediation of CausalNodeTypeEnum parity, Mech suite NaturalProductMech navigation (#76), and validate_history executable resolution (#83)

schema: supported. Targets: NCBITaxon:562, NCBITaxon:83333, NCBITaxon:1423, NCBITaxon:287, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:5755, NCBITaxon:1859096, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644.

Both directly actionable repository findings from Stage 4 are resolved and verified by regression tests: CausalNodeTypeEnum in src/taxonmech/schema/taxonmech.yaml now includes RNA, GENETIC_ELEMENT, and ORGANELLE (18 values total), NaturalProductMech is included in README.md, CLAUDE.md, src/taxonmech/templates/{base,index}.html, and all 6,372 rendered HTML pages (#76), and scripts/validate_history.py resolves linkml-validate beside sys.executable before falling back to PATH (#83).

### GTDB closeMatch synonym/xref promotion, polyphyly suffix mangling, and pooled broadMatch genome/note semantics

nomenclature: concern. Targets: NCBITaxon:562, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:206, NCBITaxon:33952.

Across the 602,165 structured-review records, 95,766 records carry verdict needs_curation due to src/taxonmech/seed.py (lines 443-478) promoting skos:closeMatch GTDB species-cluster mappings to EXACT_SYNONYM and top-level xrefs (#124, #63), mangling 15,704 polyphyly-suffixed GTDB labels into fake trinomials at lines 470-473 (#65), and emitting misleading pooled broadMatch genome totals (lines 579-593; #118) and inverted broadMatch notes (lines 465-467; #119) on 8,587 records.

### Stage 6 infrastructure prerequisites for causal_graphs, UniProtKB protein references (#78), and upstream edge-table provenance (#8)

completeness: concern. Targets: NCBITaxon:562, NCBITaxon:83333, NCBITaxon:1423, NCBITaxon:287, NCBITaxon:2940590, NCBITaxon:3121604, NCBITaxon:1435036, NCBITaxon:209650, NCBITaxon:206, NCBITaxon:33952, NCBITaxon:2190, NCBITaxon:243232, NCBITaxon:2287, NCBITaxon:4932, NCBITaxon:5207, NCBITaxon:5755, NCBITaxon:1859096, NCBITaxon:155900, NCBITaxon:408170, NCBITaxon:32644.

Two Stage 4 findings remain deferred to Stage 6 (implement_infra_tasks) under INFRA_TASKS.md (taxonmech-infra-0001..0004) and open GitHub issues #8 and #78: upstream kg-microbe edge-table provenance and subtree count rollup alignment (#8), and maintained causal_graphs overlay merging, granular trait/pathway extraction, and pinned UniProtKB snapshot/prefix/scope validation (#78).

## Findings

### causal-node-type-enum-and-mech-family-nav-drift: CausalNodeTypeEnum omits GENETIC_ELEMENT, ORGANELLE, and RNA relative to TraitMech, and Mech family navigation omits NaturalProductMech

minor / resolved / confirmed; issue key: stage4-causal-node-type-enum-and-mech-family-nav-drift.

In src/taxonmech/schema/taxonmech.yaml (lines 1467-1504), CausalNodeTypeEnum claims to be a superset of TraitMech's CausalNodeTypeEnum so TraitMech MechanismTemplate graphs can be instantiated without lossy remapping, but omits GENETIC_ELEMENT, ORGANELLE, and RNA. Additionally, the Mech suite family navigation in README.md, CLAUDE.md, src/taxonmech/templates/index.html, and src/taxonmech/templates/taxon.html omits NaturalProductMech (tracked in https://github.com/CultureBotAI/TaxonMech/issues/76).

Disposition: Resolved in Stage 5 under #76: added RNA, GENETIC_ELEMENT, and ORGANELLE to CausalNodeTypeEnum in src/taxonmech/schema/taxonmech.yaml, added NaturalProductMech to README.md, CLAUDE.md, src/taxonmech/templates/{base,index}.html, and all 6,372 rendered HTML pages in pages/, and added regression tests in tests/test_schema.py and tests/test_html_navigation.py.

### validate-history-bare-linkml-validate-path: scripts/validate_history.py invokes linkml-validate by bare name instead of resolving the active Python environment's bin directory

minor / resolved / confirmed; issue key: stage4-validate-history-bare-linkml-validate-path.

In scripts/validate_history.py lines 47-51, main() calls subprocess.run(['linkml-validate', '--schema', str(SCHEMA), '--target-class', TARGET_CLASS, *[str(p) for p in paths]], cwd=REPO_ROOT, check=False) using a bare executable name. When invoked via .venv/bin/python scripts/validate_history.py history in shells or CI steps where .venv/bin is not prepended to PATH, subprocess.run raises FileNotFoundError even though linkml-validate is installed alongside sys.executable (tracked in https://github.com/CultureBotAI/TaxonMech/issues/83).

Disposition: Resolved in Stage 5 under #83: added linkml_validate() helper in scripts/validate_history.py resolving Path(sys.executable).with_name('linkml-validate') when present on disk and falling back to 'linkml-validate' on PATH, verified by test_validate_history_resolves_linkml_validate_beside_interpreter in tests/test_new_history_record.py.

### gtdb-closematch-exact-promotion: skos:closeMatch GTDB species-cluster mappings are promoted to EXACT_SYNONYM and equivalent top-level xrefs across 95,766 records

major / deferred / confirmed; issue key: stage4-gtdb-closematch-exact-promotion.

Across docs/structured-review-inventory/part-00.tsv..part-13.tsv, 95,766 of 602,165 structured-review records (including 74,325 from fan-out closeMatch clusters; e.g., NCBITaxon:2940590 data/taxa/bacteria/achromobacter_sp_jub104.yaml promoting GTDB:s__Achromobacter_spanius, NCBITaxon:206 data/taxa/bacteria/campylobacter_sputorum.yaml promoting GTDB:s__Campylobacter_F_sputorum, and legacy-reviewed NCBITaxon:33952 data/taxa/bacteria/acetobacterium_woodii.yaml promoting GTDB:s__Acetobacterium_woodii_A) carry verdict needs_curation because src/taxonmech/seed.py (lines 443-478) promotes skos:closeMatch GTDB species-cluster rows in data/raw/gtdb_mappings.tsv to EXACT_SYNONYM and top-level xrefs without an explicit 1:1 taxon-identity or nomenclatural bridge (tracked in https://github.com/CultureBotAI/TaxonMech/issues/124 and https://github.com/CultureBotAI/TaxonMech/issues/63).

Disposition: Deferred under #124 and #63: scripts/verify_corpus.py enforces byte-for-byte identity between src/taxonmech/seed.py and all 626,048 committed YAML files in data/taxa/, so gating skos:closeMatch promotion requires a dedicated full-corpus regeneration (95,766 YAML files and 2,909 pages/taxon-details/*.json.gz shards).

### gtdb-polyphyly-suffix-synonym-mangling: GTDB polyphyly suffixes are mangled by underscore-to-space replacement into fake trinomials published as EXACT_SYNONYM

major / deferred / confirmed; issue key: stage4-gtdb-polyphyly-suffix-synonym-mangling.

In src/taxonmech/seed.py lines 470-473, GTDB species labels are converted via m['gtdb_label'].split('__', 1)[-1].replace('_', ' '), turning GTDB polyphyly partition suffixes (e.g., s__Campylobacter_F_sputorum on NCBITaxon:206 data/taxa/bacteria/campylobacter_sputorum.yaml -&gt; 'Campylobacter F sputorum', and s__Acetobacterium_woodii_A on NCBITaxon:33952 data/taxa/bacteria/acetobacterium_woodii.yaml -&gt; 'Acetobacterium woodii A') into fake trinomials published as EXACT_SYNONYM across 15,704 rows in data/raw/gtdb_mappings.tsv (tracked in https://github.com/CultureBotAI/TaxonMech/issues/65).

Disposition: Deferred under #65: fixing GTDB polyphyly suffix formatting in src/taxonmech/seed.py requires regenerating all affected TaxonRecord YAML files (15,704 GTDB mapping rows) and rendered page shards to satisfy scripts/verify_corpus.py and scripts/render_pages.py --check.

### gtdb-pooled-broadmatch-attestation-and-note: Pooled GTDB broadMatch mappings emit the largest pooled cluster's genome total and an inverted mapping-direction note

major / deferred / confirmed; issue key: stage4-gtdb-pooled-broadmatch-attestation-and-note.

On 6,335 pooled-only GTDB records (e.g., NCBITaxon:3121604 data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml, which has 5 pooled skos:broadMatch GTDB mappings led by GTDB:s__JAUMXJ01_sp041781135 with genome_count: 97), src/taxonmech/seed.py (lines 579-593) emits the largest pooled GTDB species cluster's genome count as the taxon's GTDB GENOME attestation (#118), and across 8,587 pooled GTDB records (209,540 rows, including NCBITaxon:562 data/taxa/bacteria/escherichia_coli.yaml and NCBITaxon:3121604 data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml) seed.py lines 465-467 emit a note stating the reverse of kg-microbe's skos:broadMatch direction (#119).

Disposition: Deferred under #118 and #119: updating pooled GTDB skos:broadMatch genome-count attestations and mapping-direction notes in src/taxonmech/seed.py requires regenerating 8,587 TaxonRecord YAML files and rendered page shards in a dedicated corpus-regeneration batch.

### curation-history-stale-scope-strain-count: SEEDED_FROM_SOURCES curation_history embeds stale static strain counts from curation/seed_scope.tsv reason strings

minor / deferred / confirmed; issue key: stage4-curation-history-stale-scope-strain-count.

In src/taxonmech/seed.py lines 635-645, the SEEDED_FROM_SOURCES curation_history note copies the static reason string from curation/seed_scope.tsv (e.g., '1861 BacDive strains' on NCBITaxon:562 data/taxa/bacteria/escherichia_coli.yaml) even when subtree strain aggregation yields a higher seeded strain_count (1975 on NCBITaxon:562; tracked in https://github.com/CultureBotAI/TaxonMech/issues/69).

Disposition: Deferred under #69: updating SEEDED_FROM_SOURCES curation_history reason strings in src/taxonmech/seed.py and curation/seed_scope.tsv requires regenerating affected TaxonRecord YAML files across the corpus to pass scripts/verify_corpus.py.

### upstream-edge-multiplicity-and-subtree-count-scope: Upstream kg-microbe edge tables for GOLD/MEDIADIVE/MADIN/BACTOTRAITS are not committed locally and subtree rollups apply only to BacDive strains

minor / deferred / confirmed; issue key: stage4-upstream-edge-multiplicity-and-subtree-count-scope.

Across docs/structured-review-inventory/part-00.tsv..part-13.tsv, 27,118 records carry verdict pass_with_limitations (e.g., 8-source record NCBITaxon:1435036 data/taxa/bacteria/acinetobacter_bohemicus.yaml as well as NCBITaxon:562, NCBITaxon:1423, and NCBITaxon:287) and 30 carry verdict blocked (e.g., 8-source record NCBITaxon:209650 data/taxa/bacteria/acidicaldus_organivorans.yaml) because manifest-pinned upstream kg-microbe raw edge tables for GOLD, MEDIADIVE, MADIN, and BACTOTRAITS are not committed locally, and src/taxonmech/seed.py gathers infraspecific subtree records only for BacDive strains while reporting direct-only taxon counts for GOLD, MediaDive, Madin, and BactoTraits (tracked in INFRA_TASKS.md taxonmech-infra-0004 and https://github.com/CultureBotAI/TaxonMech/issues/8).

Disposition: Deferred to Stage 6 (implement_infra_tasks) under INFRA_TASKS.md taxonmech-infra-0004 and #8: requires upstream kg-microbe edge-table provenance or subtree count rollup alignment in src/taxonmech/extract.py and src/taxonmech/seed.py.

### mechanism-and-protein-representation-prerequisites: 0 of 626,048 TaxonRecord files populate causal_graphs or UniProtKB GENE_OR_PROTEIN nodes pending seeder overlay, granular extraction, and UniProtKB validation infrastructure

major / deferred / confirmed; issue key: stage4-mechanism-and-protein-representation-prerequisites.

As established in Cycle 1 Stages 2 and 3 (reviews/structured/20261021T043201Z-stage2-causal-graphs-assessment and reviews/structured/20261021T094500Z-stage3-protein-examples-assessment), 0 of 626,048 records currently populate causal_graphs or GENE_OR_PROTEIN UniProtKB references because: (1) src/taxonmech/seed.py has no maintained overlay input and scripts/verify_corpus.py rejects manual YAML edits (taxonmech-infra-0001); (2) src/taxonmech/extract.py collapses upstream kg-microbe trait/pathway edges to integer counts (taxonmech-infra-0002); and (3) data/raw/ lacks a pinned UniProtKB snapshot while src/taxonmech/schema/taxonmech.yaml and conf/id_label_targets.yaml omit UniProtKB and EC prefixes and structured organism/strain/proteome/locus/checksum scope slots (taxonmech-infra-0003; tracked in INFRA_TASKS.md and https://github.com/CultureBotAI/TaxonMech/issues/78).

Disposition: Deferred to Stage 6 (implement_infra_tasks) under INFRA_TASKS.md (taxonmech-infra-0001, taxonmech-infra-0002, taxonmech-infra-0003) and #78: requires maintained causal_graphs overlay merging in src/taxonmech/seed.py, granular trait/pathway extraction in src/taxonmech/extract.py, and a pinned UniProtKB snapshot plus UniProtKB/EC prefix and organism/strain/proteome scope validation.

## Recommended Actions And Acceptance Checks

### remediate-seeder-gtdb-and-scope-provenance-cohorts

Gate skos:closeMatch GTDB promotion to EXACT_SYNONYM and xrefs (#124, #63), fix GTDB polyphyly suffix mangling (#65), align pooled GTDB broadMatch genome totals and notes (#118, #119), reconcile seed_scope reason strain counts (#69), and document direct vs subtree source attestation counts (#8) across src/taxonmech/seed.py and full-corpus regeneration.

- src/taxonmech/seed.py gates skos:closeMatch exact promotion and preserves GTDB polyphyly suffixes
- Pooled GTDB broadMatch notes and genome counts accurately reflect mapping direction and cluster scope
- Full corpus regenerates cleanly and passes scripts/verify_corpus.py, scripts/validate_strict.py, and scripts/render_pages.py --check

### implement-mechanism-and-protein-infrastructure-prerequisites

Execute INFRA_TASKS.md tasks taxonmech-infra-0001, taxonmech-infra-0002, taxonmech-infra-0003, and taxonmech-infra-0004 in Stage 6 to add maintained causal_graphs overlay merging in src/taxonmech/seed.py, granular trait/pathway extraction in src/taxonmech/extract.py, a pinned UniProtKB raw snapshot + prefix/scope validation (#78), and reproducible upstream edge-multiplicity provenance (#8).

- Maintained causal_graphs and UniProtKB GENE_OR_PROTEIN overlays round-trip through src/taxonmech/seed.py and scripts/verify_corpus.py
- scripts/validate_id_label_correspondence.py and scripts/validate_strict.py validate UniProtKB and EC CURIEs and organism/strain/proteome scope

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| corpus-review-inventories | docs/legacy-review-inventory.tsv; docs/structured-review-inventory/part-00.tsv..part-13.tsv; docs/structured-review-batches.tsv; 23,883 rows in docs/legacy-review-inventory.tsv and 602,165 rows across docs/structured-review-inventory/part-00.tsv..part-13.tsv | supports | Complete SHA-256-verified per-record review inventories covering all 626,048 TaxonRecord files in data/taxa/ (0 unreviewed, 0 overlap; structured verdicts: pass=479,251, pass_with_limitations=27,118, needs_curation=95,766, blocked=30). |
| exemplar-target-records | data/taxa/bacteria/escherichia_coli.yaml; data/taxa/bacteria/escherichia_coli_k_12.yaml; data/taxa/bacteria/bacillus_subtilis.yaml; data/taxa/bacteria/pseudomonas_aeruginosa.yaml; data/taxa/bacteria/achromobacter_sp_jub104.yaml; data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml; data/taxa/bacteria/acinetobacter_bohemicus.yaml; data/taxa/bacteria/acidicaldus_organivorans.yaml; data/taxa/bacteria/campylobacter_sputorum.yaml; data/taxa/bacteria/acetobacterium_woodii.yaml; data/taxa/archaea/methanocaldococcus_jannaschii.yaml; data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml; data/taxa/archaea/saccharolobus_solfataricus.yaml; data/taxa/eukaryota/saccharomyces_cerevisiae.yaml; data/taxa/eukaryota/cryptococcus_neoformans.yaml; data/taxa/eukaryota/acanthamoeba_castellanii.yaml; data/taxa/eukaryota/cryptococcus_deuterogattii.yaml; data/taxa/other/uncultured_organism.yaml; data/taxa/other/human_gut_metagenome.yaml; data/taxa/other/unidentified.yaml; Complete YAML content of 20 directly bound cross-domain and verdict-stratified TaxonRecord files | supports | Verified taxon identity, lineage, nomenclature, synonyms, xrefs, taxonomy_mappings, source_attestations, strains, and curation_history across 20 exemplar records spanning Bacteria (10), Archaea (3), Eukaryota (4), and other (3). |
| raw-source-inventories | curation/seed_scope.tsv; data/raw/MANIFEST.yaml; data/raw/ncbitaxon_taxa.tsv; data/raw/gtdb_mappings.tsv; data/raw/gtdb_species.tsv; data/raw/bacdive_strains.tsv; data/raw/lpsn_names.tsv; curation/seed_scope.tsv (626,048 rows) and data/raw/*.tsv | supports | Pinned raw inventories verify exact NCBI taxon IDs and lineages across all 626,048 records and expose systematic GTDB closeMatch fan-out (74,325 records), polyphyly suffix mangling (15,704 rows), pooled broadMatch genome counts/notes (8,587 records), and stale seed_scope strain-count reason strings. |
| schema-seeder-validator-code | src/taxonmech/schema/taxonmech.yaml; scripts/validate_history.py; README.md; CLAUDE.md; src/taxonmech/templates/base.html; src/taxonmech/templates/index.html; src/taxonmech/seed.py; src/taxonmech/extract.py; taxonmech.yaml:1467-1522; validate_history.py:25-60; base.html:32-44; index.html:244; README.md:216; CLAUDE.md:258 | supports | Post-remediation inspection confirms CausalNodeTypeEnum now includes RNA, GENETIC_ELEMENT, and ORGANELLE (18 permissible values matching TraitMech/HabitatMech) and NaturalProductMech is linked across README.md, CLAUDE.md, base.html, index.html, and all 6,372 rendered HTML pages (#76 resolved), and scripts/validate_history.py resolves linkml-validate via Path(sys.executable).with_name('linkml-validate') before falling back to PATH (#83 resolved). |
| stage1-stage2-stage3-reviews | reviews/structured/20261019T052200Z-structured-review-shard-part-13/review.yaml; reviews/structured/20261021T043201Z-stage2-causal-graphs-assessment/review.yaml; reviews/structured/20261021T094500Z-stage3-protein-examples-assessment/review.yaml; Cycle 1 Stages 1-3 structured review bundles and INFRA_TASKS.md | supports | Prior Cycle 1 structured review bundles verify the 88 newly added microbial eukaryote records in part-13 and document the mechanism causal_graphs and UniProtKB protein-example representation/writer prerequisites. |
| stage5-remediation-verification | tests/test_schema.py; tests/test_html_navigation.py; tests/test_new_history_record.py; pages/index.html; pages/browse.html; test_causal_node_type_enum_is_superset_of_traitmech_and_habitatmech; test_mech_family_navigation_and_docs_include_naturalproductmech; test_validate_history_resolves_linkml_validate_beside_interpreter | supports | Regression tests and template-to-page rendering verification across all 6,372 HTML pages confirm complete resolution of #76 and #83 with zero corpus drift. |

## Limits And Additional Notes

- Per-record review rows for all 626,048 in-scope TaxonRecord files are stored in docs/legacy-review-inventory.tsv (23,883 records) and docs/structured-review-inventory/part-00.tsv..part-13.tsv (602,165 records) and verified by SHA-256 digest via scripts/corpus_review_inventory.py --check --verify-target-sha256.
- Four src/taxonmech/seed.py findings (#124, #65, #118, #69) remain deferred because scripts/verify_corpus.py enforces zero byte-for-byte drift between src/taxonmech/seed.py and all 626,048 committed YAML files in data/taxa/, requiring a dedicated full-corpus YAML and pages/taxon-details/*.json.gz regeneration pass.
- Two findings (#8, #78) are gated on Stage 6 infrastructure tasks (INFRA_TASKS.md taxonmech-infra-0001..0004) and uncommitted upstream kg-microbe raw edge tables.
- Stage 5 resolved 2 of 8 Stage 4 findings (#76 and #83) and verified all 6,372 rendered HTML pages and 17 history records.
- Six findings (#124, #65, #118, #69, #8, #78) are carried forward with explicit deferred dispositions and open GitHub issue links.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T012228Z-stage5-remediation-review
kind: batch
repository: CultureBotAI/TaxonMech
title: 'Stage 5 grouped remediation verification and carry-forward disposition review
  (2 findings resolved under #76 and #83; 6 corpus-regeneration and Stage 6 infrastructure
  findings deferred with linked issues)'
started_at: '2026-10-22T01:14:28Z'
finished_at: '2026-10-22T01:22:28Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: independent
  independence_basis: Stage 5 post-remediation review worker; re-verified all 20 cross-domain
    exemplar TaxonRecord files, the 626,048-record review inventories, and the remediated
    LinkML schema, Mech suite navigation templates/pages, and history validator against
    Stage 4 review 20261021T163800Z-stage4-corpus-record-review.
skill: .claude/skills/review-yaml-category/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Executed Cycle 1 Stage 5 (resolve_review_findings) grouped remediation and
  post-remediation verification against Stage 4 review 20261021T163800Z-stage4-corpus-record-review.
  Grouped all 8 Stage 4 findings by root cause and repair ownership, deduplicated
  against open GitHub issues in CultureBotAI/TaxonMech, and resolved 2 directly actionable
  repository findings: (1) causal-node-type-enum-and-mech-family-nav-drift (#76) by
  adding RNA, GENETIC_ELEMENT, and ORGANELLE to CausalNodeTypeEnum in src/taxonmech/schema/taxonmech.yaml
  (completing the 18-value superset of TraitMech and HabitatMech) and adding NaturalProductMech
  to README.md, CLAUDE.md, src/taxonmech/templates/{base,index}.html, and all 6,372
  rendered HTML pages in pages/; and (2) validate-history-bare-linkml-validate-path
  (#83) by resolving Path(sys.executable).with_name(''linkml-validate'') in scripts/validate_history.py
  before falling back to PATH. Recorded explicit deferred dispositions and canonical
  open GitHub issue links (#124, #65, #118, #69, #8, #78) for the 4 src/taxonmech/seed.py
  findings that require a 626,048-record full-corpus regeneration under scripts/verify_corpus.py
  and the 2 findings gated on Stage 6 infrastructure tasks (INFRA_TASKS.md taxonmech-infra-0001..0004).'
source:
  git_revision: 5bab842c1acde531640142f784b013af168b9a0f
  state: working_tree
  inputs:
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
  - path: README.md
    sha256: c94a83ef428aa033d93a0522d3f03bd25ef39d85fab77d765b3a626f10bbe5cc
    role: context
  - path: conf/id_label_targets.yaml
    sha256: bfd1b248f7b189cd054e15b7ad0171042a30980d2ebdbdd8e7d85cea68dde9c8
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
  - path: curation/seed_scope.tsv
    sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
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
    sha256: 39d9441864565158e65948cd0ad7dd7ce79fc872fdac550ce411dcf30c663595
    role: target
  - path: data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml
    sha256: 5e50479780e050f263cddbe5634e8b602c3c46b217b0069a62384f6b474dd4b4
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
    sha256: dcf2b6af885121fd3165a0a8e1c738ab3ad7c5a27c63a95d2e816379ccb2d05c
    role: target
  - path: data/taxa/bacteria/campylobacter_sputorum.yaml
    sha256: d36195dc394fa4c68dd65292205411c4cd1fbc710f6e4e6e0bd4379c39e53847
    role: target
  - path: data/taxa/bacteria/escherichia_coli.yaml
    sha256: c656a8e47ba5dc7606507095912a35ed9bd919188dd944cb35d8693694be2acd
    role: target
  - path: data/taxa/bacteria/escherichia_coli_k_12.yaml
    sha256: b46fc7cfa796b192339be22ce127941b252db3b381b47d35e6191b012fd556da
    role: target
  - path: data/taxa/bacteria/pseudomonas_aeruginosa.yaml
    sha256: 5d94e066b274fb31533477c16b41c2345660cdd38f4dc62b53bdf075ea43de6d
    role: target
  - path: data/taxa/eukaryota/acanthamoeba_castellanii.yaml
    sha256: 969e4e46219d0635b36eca944bc6fe814538743b17ae1923a2b7eed1b6870144
    role: target
  - path: data/taxa/eukaryota/cryptococcus_deuterogattii.yaml
    sha256: 4523647eb17ceaf28168d0328284b0553b2e530541497dc81abce15e16dc04ac
    role: target
  - path: data/taxa/eukaryota/cryptococcus_neoformans.yaml
    sha256: 321562b0e9aa2a104c4763f8b5c1c9c4b4871204cf92ecc76b0b1229e2482d03
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
    sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
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
  - path: pages/browse.html
    sha256: 480cb95aa2c05d8cce75e65e5d5cc1e13080d12069851a7eec236974c590df2e
    role: context
  - path: pages/index.html
    sha256: 8d885cb08054dce5b4e96d7dbb8cc027c7dc5355f9e1c8105f17151ec3b41855
    role: context
  - path: reviews/structured/20261018T080549Z-structured-review-shard-part-00/review.yaml
    sha256: b0955608fbc45a75a6b27ace8714647ea12978fda24673b30b417a3811dcf10d
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
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml
    sha256: 4d5428357f5317ef1faad82e61541ba4496e5ba417423473094a2da677ba062b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/corpus_review_inventory.py
    sha256: f1631d3b1eecfc376c69ee15c9481fb1e49d2e43d3c49891409ceee2ba2c5b9e
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
    sha256: 48c4ef707543d1b836052013e8991d530d14559f9b58aa3ff9faf02c4e1ffc2e
    role: context
  - path: src/taxonmech/extract.py
    sha256: 7c5b5bf385e0c060f1cb3dbac304d05ddb941e4c83c900017a04133efd6d1822
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
    sha256: cbbe1fe7f3e738eb853ac8872ebe234ee1d4eb95a2ffe7adb590615bd64985e4
    role: context
  - path: src/taxonmech/seed.py
    sha256: 3cc30f6413a293165385dfc1860505fe389e5adfe9aa3d168f76aa4cb2ac36bd
    role: context
  - path: src/taxonmech/templates/base.html
    sha256: 91405ee9a3d8534c95253812be5f1ad8716a335d1a8795f2527f1b076cca0f35
    role: context
  - path: src/taxonmech/templates/index.html
    sha256: ba9e387ebe4953ce9ae1064336bd2dd7c89ce4fe41ac490f077f48ba982b6687
    role: context
  - path: src/taxonmech/templates/taxon.html
    sha256: 7df5b22500adefcb89363c23a6b74ccd0da4fa34a1f73f2997758099cf3253df
    role: context
  - path: tests/test_html_navigation.py
    sha256: cdba4274272a4eac5197651faaf1157e3a4745eba46394830fdd325424c279c8
    role: context
  - path: tests/test_new_history_record.py
    sha256: 0a630c546ef3f3891b6efa2d036989414726d936fe08e8fb5572388da6a31b5c
    role: context
  - path: tests/test_schema.py
    sha256: e8e08a66cb6439fa9c47c307ba0ec5af749d1fe4e7853c5d5e01c5da83e8bca4
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
    20 representative cross-domain and verdict-stratified TaxonRecord files bound
    directly.
  selection: All 626,048 in-scope TaxonRecord files in curation/seed_scope.tsv and
    data/taxa/PATHS.tsv verified by SHA-256 digest in the frozen review inventories,
    plus 20 directly bound representative records spanning Bacteria (10), Archaea
    (3), Eukaryota (4), and other (3) across pass, pass_with_limitations, needs_curation,
    and blocked cohorts.
  coverage: sampled
  population_size: 626048
  sampling_method: Complete SHA-256-verified census of all 626,048 corpus records
    via scripts/corpus_review_inventory.py --check --verify-target-sha256 (23,883
    legacy + 602,165 structured; 0 unreviewed; 0 overlap), stratified by domain, rank,
    source attestation, and review verdict, with 20 representative TaxonRecord files
    bound directly in targets.
  reviewed_target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:1423
  - NCBITaxon:287
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
  - NCBITaxon:5755
  - NCBITaxon:1859096
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
  name: Native strict and LinkML schema validation on directly bound Stage 4 exemplar
    records
  status: passed
  required: true
  summary: All 20 directly bound cross-domain exemplar TaxonRecord files pass scripts/validate_strict.py
    with 0 errors.
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:1423
  - NCBITaxon:287
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
  - NCBITaxon:5755
  - NCBITaxon:1859096
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  command: python3 scripts/validate_strict.py data/taxa/bacteria/escherichia_coli.yaml
    data/taxa/bacteria/escherichia_coli_k_12.yaml data/taxa/bacteria/bacillus_subtilis.yaml
    data/taxa/bacteria/pseudomonas_aeruginosa.yaml data/taxa/bacteria/achromobacter_sp_jub104.yaml
    data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml data/taxa/bacteria/acinetobacter_bohemicus.yaml
    data/taxa/bacteria/acidicaldus_organivorans.yaml data/taxa/bacteria/campylobacter_sputorum.yaml
    data/taxa/bacteria/acetobacterium_woodii.yaml data/taxa/archaea/methanocaldococcus_jannaschii.yaml
    data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml data/taxa/archaea/saccharolobus_solfataricus.yaml
    data/taxa/eukaryota/saccharomyces_cerevisiae.yaml data/taxa/eukaryota/cryptococcus_neoformans.yaml
    data/taxa/eukaryota/acanthamoeba_castellanii.yaml data/taxa/eukaryota/cryptococcus_deuterogattii.yaml
    data/taxa/other/uncultured_organism.yaml data/taxa/other/human_gut_metagenome.yaml
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
  summary: scripts/validate_history.py resolves linkml-validate beside sys.executable
    and passes on all 17 repository history records even when .venv/bin is stripped
    from PATH (#83 resolved).
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:1423
  - NCBITaxon:287
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
  - NCBITaxon:5755
  - NCBITaxon:1859096
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  command: env PATH=/usr/bin:/bin .venv/bin/python scripts/validate_history.py history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema-seeder-validator-code
- check_id: historical-counts
  name: Required historical native-unit counts
  status: unavailable
  required: true
  summary: Manifest-pinned upstream kg-microbe raw edge tables for GOLD, MEDIADIVE,
    MADIN, and BACTOTRAITS are not committed locally, and subtree rollups apply to
    BacDive strains only (#8).
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:1423
  - NCBITaxon:287
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
  - NCBITaxon:5755
  - NCBITaxon:1859096
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  evidence_ids:
  - corpus-review-inventories
  - raw-source-inventories
- check_id: corpus-review-inventory-sha256
  name: Full-corpus review coverage and target SHA-256 verification across all 626,048
    records
  status: passed
  required: true
  summary: scripts/corpus_review_inventory.py --check --verify-target-sha256 verified
    626,048 corpus records (23,883 legacy + 602,165 structured across 14 shards and
    611 batches) with 0 unreviewed records, 0 overlaps, and 0 SHA-256 mismatches.
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:1423
  - NCBITaxon:287
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
  - NCBITaxon:5755
  - NCBITaxon:1859096
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  command: .venv/bin/python scripts/corpus_review_inventory.py --check --verify-target-sha256
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - corpus-review-inventories
- check_id: verify-corpus-reproduction
  name: Deterministic seeder reproduction check across all 626,048 TaxonRecord YAML
    files
  status: passed
  required: true
  summary: scripts/verify_corpus.py --workers 4 verified zero drift between src/taxonmech/seed.py
    and all 626,048 committed YAML files.
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:1423
  - NCBITaxon:287
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
  - NCBITaxon:5755
  - NCBITaxon:1859096
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  command: .venv/bin/python scripts/verify_corpus.py --workers 4
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema-seeder-validator-code
- check_id: stage5-remediation-unit-and-page-gates
  name: Stage 5 regression tests for CausalNodeTypeEnum parity, Mech family navigation,
    and validate_history executable resolution
  status: passed
  required: true
  summary: pytest tests/test_schema.py tests/test_html_navigation.py tests/test_new_history_record.py
    and template/page parity verification across all 6,372 HTML files in pages/ passed
    with 0 errors.
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:1423
  - NCBITaxon:287
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
  - NCBITaxon:5755
  - NCBITaxon:1859096
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  command: .venv/bin/python -m pytest -q tests/test_schema.py tests/test_html_navigation.py
    tests/test_new_history_record.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema-seeder-validator-code
  - stage5-remediation-verification
evidence:
- evidence_id: corpus-review-inventories
  kind: record_content
  reference: docs/legacy-review-inventory.tsv; docs/structured-review-inventory/part-00.tsv..part-13.tsv;
    docs/structured-review-batches.tsv
  locator: 23,883 rows in docs/legacy-review-inventory.tsv and 602,165 rows across
    docs/structured-review-inventory/part-00.tsv..part-13.tsv
  summary: 'Complete SHA-256-verified per-record review inventories covering all 626,048
    TaxonRecord files in data/taxa/ (0 unreviewed, 0 overlap; structured verdicts:
    pass=479,251, pass_with_limitations=27,118, needs_curation=95,766, blocked=30).'
  accessed_at: '2026-10-22T01:22:28Z'
  support: supports
  snapshot_sha256: 023ac83c94ea72c7822acb3b111e5dddb41b1df8304f5b7ec4146883557ebce4
- evidence_id: exemplar-target-records
  kind: record_content
  reference: data/taxa/bacteria/escherichia_coli.yaml; data/taxa/bacteria/escherichia_coli_k_12.yaml;
    data/taxa/bacteria/bacillus_subtilis.yaml; data/taxa/bacteria/pseudomonas_aeruginosa.yaml;
    data/taxa/bacteria/achromobacter_sp_jub104.yaml; data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml;
    data/taxa/bacteria/acinetobacter_bohemicus.yaml; data/taxa/bacteria/acidicaldus_organivorans.yaml;
    data/taxa/bacteria/campylobacter_sputorum.yaml; data/taxa/bacteria/acetobacterium_woodii.yaml;
    data/taxa/archaea/methanocaldococcus_jannaschii.yaml; data/taxa/archaea/methanocaldococcus_jannaschii_dsm_2661.yaml;
    data/taxa/archaea/saccharolobus_solfataricus.yaml; data/taxa/eukaryota/saccharomyces_cerevisiae.yaml;
    data/taxa/eukaryota/cryptococcus_neoformans.yaml; data/taxa/eukaryota/acanthamoeba_castellanii.yaml;
    data/taxa/eukaryota/cryptococcus_deuterogattii.yaml; data/taxa/other/uncultured_organism.yaml;
    data/taxa/other/human_gut_metagenome.yaml; data/taxa/other/unidentified.yaml
  locator: Complete YAML content of 20 directly bound cross-domain and verdict-stratified
    TaxonRecord files
  summary: Verified taxon identity, lineage, nomenclature, synonyms, xrefs, taxonomy_mappings,
    source_attestations, strains, and curation_history across 20 exemplar records
    spanning Bacteria (10), Archaea (3), Eukaryota (4), and other (3).
  accessed_at: '2026-10-22T01:22:28Z'
  support: supports
  snapshot_sha256: c656a8e47ba5dc7606507095912a35ed9bd919188dd944cb35d8693694be2acd
- evidence_id: raw-source-inventories
  kind: record_content
  reference: curation/seed_scope.tsv; data/raw/MANIFEST.yaml; data/raw/ncbitaxon_taxa.tsv;
    data/raw/gtdb_mappings.tsv; data/raw/gtdb_species.tsv; data/raw/bacdive_strains.tsv;
    data/raw/lpsn_names.tsv
  locator: curation/seed_scope.tsv (626,048 rows) and data/raw/*.tsv
  summary: Pinned raw inventories verify exact NCBI taxon IDs and lineages across
    all 626,048 records and expose systematic GTDB closeMatch fan-out (74,325 records),
    polyphyly suffix mangling (15,704 rows), pooled broadMatch genome counts/notes
    (8,587 records), and stale seed_scope strain-count reason strings.
  accessed_at: '2026-10-22T01:22:28Z'
  support: supports
  snapshot_sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
- evidence_id: schema-seeder-validator-code
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml; scripts/validate_history.py; README.md;
    CLAUDE.md; src/taxonmech/templates/base.html; src/taxonmech/templates/index.html;
    src/taxonmech/seed.py; src/taxonmech/extract.py
  locator: taxonmech.yaml:1467-1522; validate_history.py:25-60; base.html:32-44; index.html:244;
    README.md:216; CLAUDE.md:258
  summary: Post-remediation inspection confirms CausalNodeTypeEnum now includes RNA,
    GENETIC_ELEMENT, and ORGANELLE (18 permissible values matching TraitMech/HabitatMech)
    and NaturalProductMech is linked across README.md, CLAUDE.md, base.html, index.html,
    and all 6,372 rendered HTML pages (#76 resolved), and scripts/validate_history.py
    resolves linkml-validate via Path(sys.executable).with_name('linkml-validate')
    before falling back to PATH (#83 resolved).
  accessed_at: '2026-10-22T01:22:28Z'
  support: supports
  snapshot_sha256: cbbe1fe7f3e738eb853ac8872ebe234ee1d4eb95a2ffe7adb590615bd64985e4
- evidence_id: stage1-stage2-stage3-reviews
  kind: record_content
  reference: reviews/structured/20261019T052200Z-structured-review-shard-part-13/review.yaml;
    reviews/structured/20261021T043201Z-stage2-causal-graphs-assessment/review.yaml;
    reviews/structured/20261021T094500Z-stage3-protein-examples-assessment/review.yaml
  locator: Cycle 1 Stages 1-3 structured review bundles and INFRA_TASKS.md
  summary: Prior Cycle 1 structured review bundles verify the 88 newly added microbial
    eukaryote records in part-13 and document the mechanism causal_graphs and UniProtKB
    protein-example representation/writer prerequisites.
  accessed_at: '2026-10-22T01:22:28Z'
  support: supports
  snapshot_sha256: 8e34dc97dcbc49098890e69e4b270e44d80eac4cc562820fb5f4035c33c94552
- evidence_id: stage5-remediation-verification
  kind: validation
  reference: tests/test_schema.py; tests/test_html_navigation.py; tests/test_new_history_record.py;
    pages/index.html; pages/browse.html
  locator: test_causal_node_type_enum_is_superset_of_traitmech_and_habitatmech; test_mech_family_navigation_and_docs_include_naturalproductmech;
    test_validate_history_resolves_linkml_validate_beside_interpreter
  accessed_at: '2026-10-22T01:22:28Z'
  support: supports
  summary: 'Regression tests and template-to-page rendering verification across all
    6,372 HTML pages confirm complete resolution of #76 and #83 with zero corpus drift.'
  snapshot_sha256: bf772269023c092be353dc0fc58e5131ef21aa07c0d6c96152749b84d605d0fc
assessments:
- assessment_id: corpus-review-coverage-and-identity
  area: identity
  topic: Full-corpus review coverage (626,048 records), SHA-256 inventory reconciliation,
    and NCBI taxonomy alignment
  outcome: supported
  summary: All 626,048 in-scope TaxonRecord YAML files in data/taxa/ are accounted
    for without gap or overlap (23,883 legacy + 602,165 structured across 14 shards
    and 611 batches) and match their pinned data/raw/ncbitaxon_taxa.tsv identifier,
    label, rank, domain, parent_taxon, and lineage.
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:1423
  - NCBITaxon:287
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
  - NCBITaxon:5755
  - NCBITaxon:1859096
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  evidence_ids:
  - corpus-review-inventories
  - exemplar-target-records
  - raw-source-inventories
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
    definition: TaxonRecord files covered by SHA-256-verified docs/legacy-review-inventory.tsv.
    denominator: 626048
    minimum: 0.0
    maximum: 626048.0
  - name: structured_reviewed_records
    value: 602165.0
    unit: records
    definition: TaxonRecord files covered by SHA-256-verified docs/structured-review-inventory/part-00.tsv..part-13.tsv.
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
- assessment_id: schema-enum-nav-and-history-validator-remediation
  area: schema
  topic: Stage 5 remediation of CausalNodeTypeEnum parity, Mech suite NaturalProductMech
    navigation (#76), and validate_history executable resolution (#83)
  outcome: supported
  summary: 'Both directly actionable repository findings from Stage 4 are resolved
    and verified by regression tests: CausalNodeTypeEnum in src/taxonmech/schema/taxonmech.yaml
    now includes RNA, GENETIC_ELEMENT, and ORGANELLE (18 values total), NaturalProductMech
    is included in README.md, CLAUDE.md, src/taxonmech/templates/{base,index}.html,
    and all 6,372 rendered HTML pages (#76), and scripts/validate_history.py resolves
    linkml-validate beside sys.executable before falling back to PATH (#83).'
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:1423
  - NCBITaxon:287
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
  - NCBITaxon:5755
  - NCBITaxon:1859096
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  evidence_ids:
  - schema-seeder-validator-code
  - stage5-remediation-verification
  metrics:
  - name: stage4_findings_resolved_in_stage5
    value: 2.0
    unit: findings
    definition: 'Stage 4 review findings resolved and verified in Stage 5 (#76, #83).'
    denominator: 8
    minimum: 0.0
    maximum: 8.0
  - name: causal_node_type_enum_permissible_values
    value: 18.0
    unit: enum_values
    definition: Count of permissible values in CausalNodeTypeEnum after adding RNA,
      GENETIC_ELEMENT, and ORGANELLE.
    denominator: 18
    minimum: 18.0
    maximum: 18.0
- assessment_id: gtdb-harmonization-and-nomenclature
  area: nomenclature
  topic: GTDB closeMatch synonym/xref promotion, polyphyly suffix mangling, and pooled
    broadMatch genome/note semantics
  outcome: concern
  summary: 'Across the 602,165 structured-review records, 95,766 records carry verdict
    needs_curation due to src/taxonmech/seed.py (lines 443-478) promoting skos:closeMatch
    GTDB species-cluster mappings to EXACT_SYNONYM and top-level xrefs (#124, #63),
    mangling 15,704 polyphyly-suffixed GTDB labels into fake trinomials at lines 470-473
    (#65), and emitting misleading pooled broadMatch genome totals (lines 579-593;
    #118) and inverted broadMatch notes (lines 465-467; #119) on 8,587 records.'
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
- assessment_id: deferred-mechanism-and-upstream-edge-infrastructure
  area: completeness
  topic: Stage 6 infrastructure prerequisites for causal_graphs, UniProtKB protein
    references (#78), and upstream edge-table provenance (#8)
  outcome: concern
  summary: 'Two Stage 4 findings remain deferred to Stage 6 (implement_infra_tasks)
    under INFRA_TASKS.md (taxonmech-infra-0001..0004) and open GitHub issues #8 and
    #78: upstream kg-microbe edge-table provenance and subtree count rollup alignment
    (#8), and maintained causal_graphs overlay merging, granular trait/pathway extraction,
    and pinned UniProtKB snapshot/prefix/scope validation (#78).'
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:1423
  - NCBITaxon:287
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
  - NCBITaxon:5755
  - NCBITaxon:1859096
  - NCBITaxon:155900
  - NCBITaxon:408170
  - NCBITaxon:32644
  evidence_ids:
  - schema-seeder-validator-code
  - stage1-stage2-stage3-reviews
  metrics:
  - name: stage4_findings_deferred_with_linked_issues
    value: 6.0
    unit: findings
    definition: 'Stage 4 review findings deferred with explicit disposition and open
      GitHub issues (#124, #65, #118, #69, #8, #78).'
    denominator: 8
    minimum: 0.0
    maximum: 8.0
findings:
- finding_id: causal-node-type-enum-and-mech-family-nav-drift
  issue_key: stage4-causal-node-type-enum-and-mech-family-nav-drift
  category: schema
  severity: minor
  status: resolved
  certainty: confirmed
  title: CausalNodeTypeEnum omits GENETIC_ELEMENT, ORGANELLE, and RNA relative to
    TraitMech, and Mech family navigation omits NaturalProductMech
  description: In src/taxonmech/schema/taxonmech.yaml (lines 1467-1504), CausalNodeTypeEnum
    claims to be a superset of TraitMech's CausalNodeTypeEnum so TraitMech MechanismTemplate
    graphs can be instantiated without lossy remapping, but omits GENETIC_ELEMENT,
    ORGANELLE, and RNA. Additionally, the Mech suite family navigation in README.md,
    CLAUDE.md, src/taxonmech/templates/index.html, and src/taxonmech/templates/taxon.html
    omits NaturalProductMech (tracked in https://github.com/CultureBotAI/TaxonMech/issues/76).
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:4932
  - NCBITaxon:5207
  field_paths:
  - causal_graphs[].nodes[].node_type
  evidence_ids:
  - schema-seeder-validator-code
  - stage5-remediation-verification
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
  normalization_reason: Restore lossless CausalNodeTypeEnum parity with TraitMech
    and complete Mech family navigation links (#76).
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/76
  disposition_reason: 'Resolved in Stage 5 under #76: added RNA, GENETIC_ELEMENT,
    and ORGANELLE to CausalNodeTypeEnum in src/taxonmech/schema/taxonmech.yaml, added
    NaturalProductMech to README.md, CLAUDE.md, src/taxonmech/templates/{base,index}.html,
    and all 6,372 rendered HTML pages in pages/, and added regression tests in tests/test_schema.py
    and tests/test_html_navigation.py.'
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: causal-node-type-enum-and-mech-family-nav-drift
- finding_id: validate-history-bare-linkml-validate-path
  issue_key: stage4-validate-history-bare-linkml-validate-path
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: scripts/validate_history.py invokes linkml-validate by bare name instead
    of resolving the active Python environment's bin directory
  description: In scripts/validate_history.py lines 47-51, main() calls subprocess.run(['linkml-validate',
    '--schema', str(SCHEMA), '--target-class', TARGET_CLASS, *[str(p) for p in paths]],
    cwd=REPO_ROOT, check=False) using a bare executable name. When invoked via .venv/bin/python
    scripts/validate_history.py history in shells or CI steps where .venv/bin is not
    prepended to PATH, subprocess.run raises FileNotFoundError even though linkml-validate
    is installed alongside sys.executable (tracked in https://github.com/CultureBotAI/TaxonMech/issues/83).
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:2940590
  field_paths:
  - curation_history
  evidence_ids:
  - schema-seeder-validator-code
  - stage5-remediation-verification
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: scripts/validate_history.py
    role: History YAML LinkML validator script
  rule_id: docs/record-review-profile.md:history
  normalization_reason: Resolve linkml-validate relative to sys.executable before
    falling back to PATH (#83).
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/83
  disposition_reason: 'Resolved in Stage 5 under #83: added linkml_validate() helper
    in scripts/validate_history.py resolving Path(sys.executable).with_name(''linkml-validate'')
    when present on disk and falling back to ''linkml-validate'' on PATH, verified
    by test_validate_history_resolves_linkml_validate_beside_interpreter in tests/test_new_history_record.py.'
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: validate-history-bare-linkml-validate-path
- finding_id: gtdb-closematch-exact-promotion
  issue_key: stage4-gtdb-closematch-exact-promotion
  category: grounding
  severity: major
  status: deferred
  certainty: confirmed
  title: skos:closeMatch GTDB species-cluster mappings are promoted to EXACT_SYNONYM
    and equivalent top-level xrefs across 95,766 records
  description: Across docs/structured-review-inventory/part-00.tsv..part-13.tsv, 95,766
    of 602,165 structured-review records (including 74,325 from fan-out closeMatch
    clusters; e.g., NCBITaxon:2940590 data/taxa/bacteria/achromobacter_sp_jub104.yaml
    promoting GTDB:s__Achromobacter_spanius, NCBITaxon:206 data/taxa/bacteria/campylobacter_sputorum.yaml
    promoting GTDB:s__Campylobacter_F_sputorum, and legacy-reviewed NCBITaxon:33952
    data/taxa/bacteria/acetobacterium_woodii.yaml promoting GTDB:s__Acetobacterium_woodii_A)
    carry verdict needs_curation because src/taxonmech/seed.py (lines 443-478) promotes
    skos:closeMatch GTDB species-cluster rows in data/raw/gtdb_mappings.tsv to EXACT_SYNONYM
    and top-level xrefs without an explicit 1:1 taxon-identity or nomenclatural bridge
    (tracked in https://github.com/CultureBotAI/TaxonMech/issues/124 and https://github.com/CultureBotAI/TaxonMech/issues/63).
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
  disposition_reason: 'Deferred under #124 and #63: scripts/verify_corpus.py enforces
    byte-for-byte identity between src/taxonmech/seed.py and all 626,048 committed
    YAML files in data/taxa/, so gating skos:closeMatch promotion requires a dedicated
    full-corpus regeneration (95,766 YAML files and 2,909 pages/taxon-details/*.json.gz
    shards).'
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: gtdb-closematch-exact-promotion
- finding_id: gtdb-polyphyly-suffix-synonym-mangling
  issue_key: stage4-gtdb-polyphyly-suffix-synonym-mangling
  category: nomenclature
  severity: major
  status: deferred
  certainty: confirmed
  title: GTDB polyphyly suffixes are mangled by underscore-to-space replacement into
    fake trinomials published as EXACT_SYNONYM
  description: In src/taxonmech/seed.py lines 470-473, GTDB species labels are converted
    via m['gtdb_label'].split('__', 1)[-1].replace('_', ' '), turning GTDB polyphyly
    partition suffixes (e.g., s__Campylobacter_F_sputorum on NCBITaxon:206 data/taxa/bacteria/campylobacter_sputorum.yaml
    -> 'Campylobacter F sputorum', and s__Acetobacterium_woodii_A on NCBITaxon:33952
    data/taxa/bacteria/acetobacterium_woodii.yaml -> 'Acetobacterium woodii A') into
    fake trinomials published as EXACT_SYNONYM across 15,704 rows in data/raw/gtdb_mappings.tsv
    (tracked in https://github.com/CultureBotAI/TaxonMech/issues/65).
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
  disposition_reason: 'Deferred under #65: fixing GTDB polyphyly suffix formatting
    in src/taxonmech/seed.py requires regenerating all affected TaxonRecord YAML files
    (15,704 GTDB mapping rows) and rendered page shards to satisfy scripts/verify_corpus.py
    and scripts/render_pages.py --check.'
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: gtdb-polyphyly-suffix-synonym-mangling
- finding_id: gtdb-pooled-broadmatch-attestation-and-note
  issue_key: stage4-gtdb-pooled-broadmatch-attestation-and-note
  category: evidence
  severity: major
  status: deferred
  certainty: confirmed
  title: Pooled GTDB broadMatch mappings emit the largest pooled cluster's genome
    total and an inverted mapping-direction note
  description: 'On 6,335 pooled-only GTDB records (e.g., NCBITaxon:3121604 data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml,
    which has 5 pooled skos:broadMatch GTDB mappings led by GTDB:s__JAUMXJ01_sp041781135
    with genome_count: 97), src/taxonmech/seed.py (lines 579-593) emits the largest
    pooled GTDB species cluster''s genome count as the taxon''s GTDB GENOME attestation
    (#118), and across 8,587 pooled GTDB records (209,540 rows, including NCBITaxon:562
    data/taxa/bacteria/escherichia_coli.yaml and NCBITaxon:3121604 data/taxa/bacteria/acidaminobacteraceae_bacterium.yaml)
    seed.py lines 465-467 emit a note stating the reverse of kg-microbe''s skos:broadMatch
    direction (#119).'
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
  disposition_reason: 'Deferred under #118 and #119: updating pooled GTDB skos:broadMatch
    genome-count attestations and mapping-direction notes in src/taxonmech/seed.py
    requires regenerating 8,587 TaxonRecord YAML files and rendered page shards in
    a dedicated corpus-regeneration batch.'
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: gtdb-pooled-broadmatch-attestation-and-note
- finding_id: curation-history-stale-scope-strain-count
  issue_key: stage4-curation-history-stale-scope-strain-count
  category: provenance
  severity: minor
  status: deferred
  certainty: confirmed
  title: SEEDED_FROM_SOURCES curation_history embeds stale static strain counts from
    curation/seed_scope.tsv reason strings
  description: In src/taxonmech/seed.py lines 635-645, the SEEDED_FROM_SOURCES curation_history
    note copies the static reason string from curation/seed_scope.tsv (e.g., '1861
    BacDive strains' on NCBITaxon:562 data/taxa/bacteria/escherichia_coli.yaml) even
    when subtree strain aggregation yields a higher seeded strain_count (1975 on NCBITaxon:562;
    tracked in https://github.com/CultureBotAI/TaxonMech/issues/69).
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
  disposition_reason: 'Deferred under #69: updating SEEDED_FROM_SOURCES curation_history
    reason strings in src/taxonmech/seed.py and curation/seed_scope.tsv requires regenerating
    affected TaxonRecord YAML files across the corpus to pass scripts/verify_corpus.py.'
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: curation-history-stale-scope-strain-count
- finding_id: upstream-edge-multiplicity-and-subtree-count-scope
  issue_key: stage4-upstream-edge-multiplicity-and-subtree-count-scope
  category: completeness
  severity: minor
  status: deferred
  certainty: confirmed
  title: Upstream kg-microbe edge tables for GOLD/MEDIADIVE/MADIN/BACTOTRAITS are
    not committed locally and subtree rollups apply only to BacDive strains
  description: Across docs/structured-review-inventory/part-00.tsv..part-13.tsv, 27,118
    records carry verdict pass_with_limitations (e.g., 8-source record NCBITaxon:1435036
    data/taxa/bacteria/acinetobacter_bohemicus.yaml as well as NCBITaxon:562, NCBITaxon:1423,
    and NCBITaxon:287) and 30 carry verdict blocked (e.g., 8-source record NCBITaxon:209650
    data/taxa/bacteria/acidicaldus_organivorans.yaml) because manifest-pinned upstream
    kg-microbe raw edge tables for GOLD, MEDIADIVE, MADIN, and BACTOTRAITS are not
    committed locally, and src/taxonmech/seed.py gathers infraspecific subtree records
    only for BacDive strains while reporting direct-only taxon counts for GOLD, MediaDive,
    Madin, and BactoTraits (tracked in INFRA_TASKS.md taxonmech-infra-0004 and https://github.com/CultureBotAI/TaxonMech/issues/8).
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
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: Upstream kg-microbe raw inventory extractor
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Source attestation builder
  rule_id: docs/record-review-profile.md:historical-counts
  normalization_reason: Document and reconcile direct vs subtree attestation counts
    and upstream edge-table provenance (#8; taxonmech-infra-0004).
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/8
  disposition_reason: 'Deferred to Stage 6 (implement_infra_tasks) under INFRA_TASKS.md
    taxonmech-infra-0004 and #8: requires upstream kg-microbe edge-table provenance
    or subtree count rollup alignment in src/taxonmech/extract.py and src/taxonmech/seed.py.'
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: upstream-edge-multiplicity-and-subtree-count-scope
- finding_id: mechanism-and-protein-representation-prerequisites
  issue_key: stage4-mechanism-and-protein-representation-prerequisites
  category: completeness
  severity: major
  status: deferred
  certainty: confirmed
  title: 0 of 626,048 TaxonRecord files populate causal_graphs or UniProtKB GENE_OR_PROTEIN
    nodes pending seeder overlay, granular extraction, and UniProtKB validation infrastructure
  description: 'As established in Cycle 1 Stages 2 and 3 (reviews/structured/20261021T043201Z-stage2-causal-graphs-assessment
    and reviews/structured/20261021T094500Z-stage3-protein-examples-assessment), 0
    of 626,048 records currently populate causal_graphs or GENE_OR_PROTEIN UniProtKB
    references because: (1) src/taxonmech/seed.py has no maintained overlay input
    and scripts/verify_corpus.py rejects manual YAML edits (taxonmech-infra-0001);
    (2) src/taxonmech/extract.py collapses upstream kg-microbe trait/pathway edges
    to integer counts (taxonmech-infra-0002); and (3) data/raw/ lacks a pinned UniProtKB
    snapshot while src/taxonmech/schema/taxonmech.yaml and conf/id_label_targets.yaml
    omit UniProtKB and EC prefixes and structured organism/strain/proteome/locus/checksum
    scope slots (taxonmech-infra-0003; tracked in INFRA_TASKS.md and https://github.com/CultureBotAI/TaxonMech/issues/78).'
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:1423
  - NCBITaxon:287
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:5207
  field_paths:
  - causal_graphs
  - causal_graphs[].nodes[].grounding
  evidence_ids:
  - schema-seeder-validator-code
  - stage1-stage2-stage3-reviews
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Seeder record builder
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: Upstream kg-microbe extractor
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/schema/taxonmech.yaml
    role: LinkML schema definition
  - repository: CultureBotAI/TaxonMech
    path: conf/id_label_targets.yaml
    role: OAK ID-label target configuration
  rule_id: INFRA_TASKS.md:taxonmech-infra-0001..0003
  normalization_reason: Implement maintained overlay merge, granular trait/pathway
    extraction, and pinned UniProtKB validation in Stage 6 (#78).
  external_issues:
  - https://github.com/CultureBotAI/TaxonMech/issues/78
  disposition_reason: 'Deferred to Stage 6 (implement_infra_tasks) under INFRA_TASKS.md
    (taxonmech-infra-0001, taxonmech-infra-0002, taxonmech-infra-0003) and #78: requires
    maintained causal_graphs overlay merging in src/taxonmech/seed.py, granular trait/pathway
    extraction in src/taxonmech/extract.py, and a pinned UniProtKB snapshot plus UniProtKB/EC
    prefix and organism/strain/proteome scope validation.'
  previous_occurrences:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261021T163800Z-stage4-corpus-record-review
    finding_id: mechanism-and-protein-representation-prerequisites
actions:
- action_id: remediate-seeder-gtdb-and-scope-provenance-cohorts
  description: 'Gate skos:closeMatch GTDB promotion to EXACT_SYNONYM and xrefs (#124,
    #63), fix GTDB polyphyly suffix mangling (#65), align pooled GTDB broadMatch genome
    totals and notes (#118, #119), reconcile seed_scope reason strain counts (#69),
    and document direct vs subtree source attestation counts (#8) across src/taxonmech/seed.py
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
- action_id: implement-mechanism-and-protein-infrastructure-prerequisites
  description: Execute INFRA_TASKS.md tasks taxonmech-infra-0001, taxonmech-infra-0002,
    taxonmech-infra-0003, and taxonmech-infra-0004 in Stage 6 to add maintained causal_graphs
    overlay merging in src/taxonmech/seed.py, granular trait/pathway extraction in
    src/taxonmech/extract.py, a pinned UniProtKB raw snapshot + prefix/scope validation
    (#78), and reproducible upstream edge-multiplicity provenance (#8).
  finding_ids:
  - mechanism-and-protein-representation-prerequisites
  target_ids:
  - NCBITaxon:562
  - NCBITaxon:83333
  - NCBITaxon:1423
  - NCBITaxon:287
  - NCBITaxon:2190
  - NCBITaxon:243232
  - NCBITaxon:5207
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Seeder record builder
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: Upstream kg-microbe extractor
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/schema/taxonmech.yaml
    role: LinkML schema definition
  - repository: CultureBotAI/TaxonMech
    path: conf/id_label_targets.yaml
    role: OAK ID-label target configuration
  acceptance_checks:
  - Maintained causal_graphs and UniProtKB GENE_OR_PROTEIN overlays round-trip through
    src/taxonmech/seed.py and scripts/verify_corpus.py
  - scripts/validate_id_label_correspondence.py and scripts/validate_strict.py validate
    UniProtKB and EC CURIEs and organism/strain/proteome scope
limitations:
- Per-record review rows for all 626,048 in-scope TaxonRecord files are stored in
  docs/legacy-review-inventory.tsv (23,883 records) and docs/structured-review-inventory/part-00.tsv..part-13.tsv
  (602,165 records) and verified by SHA-256 digest via scripts/corpus_review_inventory.py
  --check --verify-target-sha256.
- 'Four src/taxonmech/seed.py findings (#124, #65, #118, #69) remain deferred because
  scripts/verify_corpus.py enforces zero byte-for-byte drift between src/taxonmech/seed.py
  and all 626,048 committed YAML files in data/taxa/, requiring a dedicated full-corpus
  YAML and pages/taxon-details/*.json.gz regeneration pass.'
- 'Two findings (#8, #78) are gated on Stage 6 infrastructure tasks (INFRA_TASKS.md
  taxonmech-infra-0001..0004) and uncommitted upstream kg-microbe raw edge tables.'
related_reviews:
- repository: CultureBotAI/TaxonMech
  review_id: 20261021T163800Z-stage4-corpus-record-review
  relationship: follows_up
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
  review_id: 20261021T043201Z-stage2-causal-graphs-assessment
  relationship: consolidates
- repository: CultureBotAI/TaxonMech
  review_id: 20261021T094500Z-stage3-protein-examples-assessment
  relationship: consolidates
notes:
- 'Stage 5 resolved 2 of 8 Stage 4 findings (#76 and #83) and verified all 6,372 rendered
  HTML pages and 17 history records.'
- 'Six findings (#124, #65, #118, #69, #8, #78) are carried forward with explicit
  deferred dispositions and open GitHub issue links.'
tags:
- stage5-remediation-review
- resolve-review-findings
- post-remediation-verification
```
