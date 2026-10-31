# Record review: Acidianus hospitalis W1

- Review: 20261019T233304Z-acidianus_hospitalis_w1
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-19T07:24:24Z
- Finished UTC: 2026-10-19T23:33:04Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

NCBITaxon:933801 is correctly identified as the strain Acidianus hospitalis W1, but the seeder promotes the broader GTDB Acidianus hospitalis species cluster to an exact synonym and equivalent xref. This is one confirmed major scope/grounding finding. Source counts and lineage remain intact; historical Madin edge verification is unavailable.

## Scope And Provenance

The entire single resolved generated TaxonRecord and its identity, nomenclature, mapping, strain, source-count and provenance assertions.

Selection: First ten unreviewed corpus paths in lexicographic order at base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; this is record 7. Reviewed means an actual target of a validated bundle from scripts/record_review.py list. Inventory coverage alone does not count.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9b5a8fff5185b38dc5c77bb35235152c81ea7765.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:933801 | data/taxa/archaea/acidianus_hospitalis_w1.yaml | generated | Acidianus hospitalis W1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact NCBI taxon, rank and lineage | passed | True | NCBITaxon:933801 | NCBITaxon:933801 denotes strain W1 below species 563177, with ten carried ancestors and genetic code 11. Pinned and current NCBI agree. The NCBI variants 'str. W1' and 'strain W1' refer to this strain; the unqualified species label does not have the same rank or extension. |
| Imported strain and genome assertion check | not_applicable | False | NCBITaxon:933801 | This target has no imported BacDive strain and no strain-level genome assertion. Exact source inventory/subtree selection was checked; no deposit or assembly is invented from taxon identity. |
| Original aggregate source-edge multiplicities | unavailable | True | NCBITaxon:933801 | Inventories support the record's counts, but the original manifest-pinned MediaDive/GOLD/Madin edge bytes were unavailable in the checked locations; current external files have different hashes. No recount of current data can validate the historical numbers. |
| Initial quality-gate setup attempt | failed | False | NCBITaxon:933801 | Exit 1: missing ruff dependency; environment repaired before the separately recorded full retry. |
| Native strict record validation | passed | True | NCBITaxon:933801 | Actual terminal exit code 0. This exact generated YAML only. |
| Repository history validation | passed | True | NCBITaxon:933801 | Actual terminal exit code 0. All 17 committed standalone history records; generated seed history also inspected in this target. |
| Full-corpus exact reproduction | passed | True | NCBITaxon:933801 | Actual terminal exit code 0. All 625,960 generated taxon YAMLs, not a focused approximation. |
| Native product ID/label gate | passed | True | NCBITaxon:933801 | Actual terminal exit code 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. |
| Authoritative complete quality gate | passed | True | NCBITaxon:933801 | Actual terminal exit code 0. Repository-wide just qc on the isolated checkout; includes corpus-wide checks. Pytest reported 1055 passed, 3 skipped and 5 deselected; the native QC recipe completed successfully. |

## Scientific And Domain Assessments

### Resolved biological taxon and carried lineage

identity: supported. Targets: NCBITaxon:933801.

NCBITaxon:933801 denotes strain W1 below species 563177, with ten carried ancestors and genetic code 11. Pinned and current NCBI agree. The NCBI variants 'str. W1' and 'strain W1' refer to this strain; the unqualified species label does not have the same rank or extension.

### Source-scoped names and nomenclatural standing

nomenclature: concern. Targets: NCBITaxon:933801.

The two NCBI exact synonyms preserve W1. The GTDB exact synonym Acidianus hospitalis drops the strain qualifier and refers to a seven-genome species cluster. That scope inflation is not justified by the local policy allowing normalization of one-to-one species mappings. No LPSN nomenclature is asserted by this strain record.

### Complete imported subtree and source assertion units

completeness: supported. Targets: NCBITaxon:933801.

No BacDive strain is classified under this exact taxon in the complete pinned inventory. Thus strain_count: 0 counts imported BacDive entries, not biological strains. The GTDB attestation's seven GENOMEs are the source-cluster count and Madin's four assertions are direct to W1. The latter cannot be recounted from the original pinned upstream edges.

### GTDB mapping scope and source genome count

grounding: concern. Targets: NCBITaxon:933801.

GTDB:s__Acidianus_hospitalis maps to NCBITaxon:563177, 933801 and 1872104. Among all seven primary cluster rows, only RS_GCF_000213215.1 is classified by NCBI as W1 (933801). RHS.bin.1 and SCGC AC-742_N10 are taxon 563177, while RBS.bin.2, Alice.S.bin.1, Moose.S.bin.11 and SBS.bin.13 are taxon 1872104. A source membership/closeMatch assertion cannot turn the entire species into the W1 strain. The exact synonym and xref are produced by seed.py's unguarded closeMatch identity branch.

### Seed event and scientific status boundary

provenance: supported. Targets: NCBITaxon:933801.

The NCBI identity is grounded EXACT and the record remains SEEDED. Its single seed event is consistent with the latest extraction timestamp across raw, ATB and StrainInfo manifests (2026-09-13T17:54:04Z). This review neither appends history nor promotes native status.

## Findings

### gtdb-strain-scope: GTDB species-cluster identity is promoted to exact equivalence with strain W1

major / open / confirmed; issue key: gtdb-closematch-exact-promotion-933801.

GTDB:s__Acidianus_hospitalis maps to NCBITaxon:563177, 933801 and 1872104. Among all seven primary cluster rows, only RS_GCF_000213215.1 is classified by NCBI as W1 (933801). RHS.bin.1 and SCGC AC-742_N10 are taxon 563177, while RBS.bin.2, Alice.S.bin.1, Moose.S.bin.11 and SBS.bin.13 are taxon 1872104. A source membership/closeMatch assertion cannot turn the entire species into the W1 strain. The exact synonym and xref are produced by seed.py's unguarded closeMatch identity branch. The local policy concerns one-to-one species mappings; a species-to-strain rank mismatch violates the equivalent-xref contract even though it reproduces current seeder code.

## Recommended Actions And Acceptance Checks

### verify-pinned-aggregate-edges

Recover the upstream kg-microbe edge snapshots whose SHA-256 values are pinned in data/raw/MANIFEST.yaml, then recount this exact target using the maintained extractor's source-specific counting rules. This resolves the historical-count limitation without changing generated records.

- Recovered edge files match the manifest SHA-256 values before any comparison.
- Recount only the target's explicit MediaDive METPO:2000517 medium set, GOLD Go subclass assertions and Madin taxon-subject assertions that this record actually attests; preserve their distinct units and direct-taxon boundaries.
- Compare the resulting counts and medium identifiers with the exact inventoried rows cited in this review, and retain any discrepancy as a new observation.

### guard-strain-equivalence

Add an evidence- and rank-aware guard to the maintained seeder so a GTDB species closeMatch does not automatically create an EXACT_SYNONYM or equivalent xref for a narrower strain. Preserve qualified source mapping and its seven-genome cluster count. Clarify the species-versus-strain boundary in the harmonization documentation; regenerate only through guarded repository writers during separately authorized curation.

- A W1 canary retains NCBITaxon:933801, STRAIN rank, parent 563177, carried lineage and the two NCBI W1 synonyms.
- GTDB:s__Acidianus_hospitalis remains a qualified source mapping with genome_count 7, without exact species-to-strain synonym/xref promotion absent an explicit appropriate identity bridge.
- A positive species control preserves supported species normalization, including LPSN-backed mappings; the guard does not discard source assertions or genome links.
- After authorized guarded regeneration, run just validate-strict for the affected record, just validate-history, just verify-corpus and just qc.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/taxa/archaea/acidianus_hospitalis_w1.yaml; entire TaxonRecord; identifier=NCBITaxon:933801 | supports | Read the entire generated YAML, including identity, all synonyms, mappings, source attestations, every strain assertion and seed history. |
| taxonomy-inventory | data/raw/ncbitaxon_taxa.tsv; line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""}; line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"}; line 1798: {"taxon_id":"NCBITaxon:2281","label":"Sulfolobales","rank":"ORDER","parent_id":"NCBITaxon:183924"}; line 2648: {"taxon_id":"NCBITaxon:12914","label":"Acidianus","rank":"GENUS","parent_id":"NCBITaxon:118883"}; line 2980: {"taxon_id":"NCBITaxon:28889","label":"Thermoproteota","rank":"PHYLUM","parent_id":"NCBITaxon:1783275"}; line 22254: {"taxon_id":"NCBITaxon:118883","label":"Sulfolobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2281"}; line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"}; line 36612: {"taxon_id":"NCBITaxon:183924","label":"Thermoprotei","rank":"CLASS","parent_id":"NCBITaxon:28889"}; line 132206: {"taxon_id":"NCBITaxon:563177","label":"Acidianus hospitalis","rank":"SPECIES","parent_id":"NCBITaxon:12914"}; line 197221: {"taxon_id":"NCBITaxon:933801","label":"Acidianus hospitalis W1","rank":"STRAIN","parent_id":"NCBITaxon:563177","genetic_code":"11","exact_synonyms":"Acidianus hospitalis str. W1&#124;Acidianus hospitalis strain W1","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb&#124;madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"}; line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"} | supports | Inspected the exact target row and every carried ancestor. Rank, label, parent, genetic code and typed source names were compared with the complete record. |
| scope-row | curation/seed_scope.tsv; line 35257: {"identifier":"NCBITaxon:933801","added":"2026-09-12","reason":"attested rule: Acidianus hospitalis W1, 3 sources incl. NCBI"} | supports | The exact target is explicitly included in the seed scope. |
| path-row | data/taxa/PATHS.tsv; line 612764: {"identifier":"NCBITaxon:933801","slug":"acidianus_hospitalis_w1"} | supports | The indexed path resolves to the same NCBI taxon and generated target. |
| ncbi-live | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=933801; TaxaSet/Taxon[TaxId='933801']; captured together with the other nine explicitly selected batch taxa | supports | Inspected the official current taxonomy response for this exact taxon: scientific name, rank, parent, source name classes, lineage identifiers and genetic code. Compared it with the separately pinned September taxonomy. |
| lpsn-inventory | data/raw/lpsn_names.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Inspected all exact taxon/name mappings and linked synonymous LPSN names, retaining statuses and type-designation scope. |
| gtdb-mappings | data/raw/gtdb_mappings.tsv; line 70969: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","gtdb_label":"s__Acidianus_hospitalis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:1872104","predicate":"skos:broadMatch","genome_count":"7"}; line 296668: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","gtdb_label":"s__Acidianus_hospitalis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:563177","predicate":"skos:closeMatch","genome_count":"7"}; line 320834: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","gtdb_label":"s__Acidianus_hospitalis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:933801","predicate":"skos:closeMatch","genome_count":"7"} | supports | Inspected this taxon's GTDB mappings and every reverse mapping of the same selected source cluster; predicates and counts remain source-scoped. |
| gtdb-species | data/raw/gtdb_species.tsv; line 3494: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","label":"s__Acidianus_hospitalis","parent":"GTDB:g__Acidianus","genome_count":"7"} | supports | Inspected source species identifiers, labels, parent cluster and genome counts. |
| bacdive-inventory | data/raw/bacdive_strains.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Full BacDive inventory selection used the exact taxon plus every descendant from the complete NCBI parent graph. Deposits, type status and classified_as remain separate from taxon identity. |
| culture-inventory | data/raw/culture_collection_strains.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Inspected exact culture identifiers associated with the target; source aliases do not independently authorize genome joins. |
| gold-organisms | data/raw/gold_organisms.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Inspected the exact GOLD organism count row, or its bounded absence, without converting counts to phenotypes. |
| mediadive-taxa | data/raw/mediadive_taxa.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Inspected the exact MediaDive medium count row, or its bounded absence, without converting counts to phenotypes. |
| madin-taxa | data/raw/madin_taxa.tsv; line 33029: {"taxon_id":"NCBITaxon:933801","assertion_count":"4"} | supports | Inspected the exact Madin trait-assertion count row, or its bounded absence, without converting counts to phenotypes. |
| bactotraits-taxa | data/raw/bactotraits_taxa.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Inspected the exact BactoTraits trait-assertion count row, or its bounded absence, without converting counts to phenotypes. |
| mapping-policy | docs/HARMONIZATION.md; Mapping predicates and Scope and lineage sections | supports | The local mapping policy permits one-to-one species closeMatch mappings and LPSN-linked species to supply xrefs/synonyms, retains pooled broadMatch entries separately, and carries NCBI lineage unchanged. |
| equivalence-contract | src/taxonmech/schema/taxonmech.yaml; TaxonRecord.xrefs (lines 180–187); TaxonomyMapping (lines 417–439) | supports | TaxonRecord.xrefs denotes true equivalence, while broader/narrower relationships belong in taxonomy_mappings; TaxonomyMapping.genome_count counts genomes under the source taxon. |
| seed-owner | src/taxonmech/seed.py; GTDB mapping construction and identity promotion, lines 440–472 | supports | The identity branch accepts an LPSN GTDB bridge or any skos:closeMatch, then emits an equivalent xref and, if the text differs, an EXACT_SYNONYM. It does not guard against a strain-rank target. |
| manifest | data/raw/MANIFEST.yaml; kg_microbe_source, inputs, extracted_at | supports | The source manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd and hashes individual upstream inputs; extraction time is 2026-09-13T17:50:44Z. |
| overlay-manifests | data/atb/MANIFEST.yaml; extracted_at, together with data/straininfo/MANIFEST.yaml | supports | Compared raw, ATB and StrainInfo extraction timestamps. Their maximum, 2026-09-13T17:54:04Z, matches the sole generated seed event. The StrainInfo manifest is separately captured in source.inputs. |
| genome-catalog-manifest | data/catalog/MANIFEST.json; coverage.sources[name=GTDB] | supports | The complete native GTDB genome catalog is the RS232 snapshot. Species clusters and MAGs remain distinct from physical strain deposits. |
| genome-catalog-1 | data/catalog/gtdb_genomes-0017.jsonl.gz; line 32156: {"accession":"GB_GCA_032249015.1","ncbi_taxid":"1872104","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus hospitalis","ncbi_strain_identifiers":"RBS.bin.2"}; line 37598: {"accession":"RS_GCF_046537415.1","ncbi_taxid":"1872104","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus hospitalis","ncbi_strain_identifiers":"Alice.S.bin.1"}; line 37916: {"accession":"GB_GCA_046533895.1","ncbi_taxid":"563177","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus hospitalis","ncbi_strain_identifiers":"RHS.bin.1"}; line 46762: {"accession":"GB_GCA_003086435.1","ncbi_taxid":"563177","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus hospitalis","ncbi_strain_identifiers":"SCGC AC-742_N10"}; line 47899: {"accession":"RS_GCF_046534395.1","ncbi_taxid":"1872104","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus hospitalis","ncbi_strain_identifiers":"Moose.S.bin.11"}; line 49253: {"accession":"RS_GCF_000213215.1","ncbi_taxid":"933801","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus hospitalis","ncbi_strain_identifiers":"W1"} | supports | Inspected the complete selected genome catalog rows. Source genome identity, taxonomic assignment, deposit fields and accession versions were assessed separately. |
| genome-catalog-2 | data/catalog/gtdb_genomes-0018.jsonl.gz; line 1150: {"accession":"GB_GCA_046533515.1","ncbi_taxid":"1872104","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus hospitalis","ncbi_strain_identifiers":"SBS.bin.13"} | supports | Inspected the complete selected genome catalog rows. Source genome identity, taxonomic assignment, deposit fields and accession versions were assessed separately. |
| historical-edge-availability | data/raw/MANIFEST.yaml; data/transformed/mediadive/edges.tsv: expected=78ea275a59d4e2de09a9cf72652ec64454c6a111d2defa1ae0a44bac8a72e523, present=4e933d1e2412fb1aad74e60719a6a64dfa34862ff0a6b84e93d78da5ce13dd8b; data/transformed/gold/edges.tsv: expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12, present=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d; data/transformed/madin_etal/edges.tsv: expected=3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f, present=c19bfc848e1b410548614c54a2b99e2c58452d58aeb61f972c99fcb3039a1d24 | partial | The exact configured external paths were checked including ignored files. They exist, but each current SHA-256 differs from the manifest-pinned snapshot; none was treated as the original extraction input. |
| qc-setup-receipt | just qc; initial setup attempt, 2026-10-19T07:17:01Z through 2026-10-19T07:17:01Z | context_only | Initial actual invocation exited 1 because the isolated environment lacked ruff. Locked ruff 0.16.7 was then installed in that environment and the full command retried; qc below records the retry result. |
| strict-receipt | just validate-strict data/taxa/archaea/acidianus_hospitalis_w1.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/strict-07.tsv; This exact generated YAML only. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:24:25Z, finished 2026-10-19T07:24:26Z, exit 0.<br>Validating 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/strict-07.tsv |
| history-receipt | just validate-history; All 17 committed standalone history records; generated seed history also inspected in this target. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:01Z, finished 2026-10-19T07:17:03Z, exit 0.<br>history links: 17 record(s), 0 invalid<br>No issues found<br>17 history record(s) valid against src/taxonmech/schema/history.yaml |
| corpus-receipt | just verify-corpus; All 625,960 generated taxon YAMLs, not a focused approximation. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:18:23Z, finished 2026-10-19T07:24:12Z, exit 0.<br>uv run python scripts/verify_corpus.py <br>expected 625960 records, found 625960 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ and curation/seed_scope.tsv |
| products-receipt | just validate-products; Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:01Z, finished 2026-10-19T07:55:11Z, exit 0.<br>uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml<br><br>id↔label correspondence summary:<br><br>✅ All id↔label pairs correspond. |
| qc-receipt | just qc; Repository-wide just qc on the isolated checkout; includes corpus-wide checks. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:41Z, finished 2026-10-19T08:07:39Z, exit 0.<br>1055 passed, 3 skipped, 5 deselected in 1634.00s (0:27:13)<br>Validating 625960 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml<br>  files scanned:      625960<br>expected 625960 records, found 625960 on disk<br>pages/ is current<br>Site publication: 530,864,122 bytes (budget 950,000,000)<br>625960 taxon records<br>  NCBITAXON        625960<br>All TaxonMech quality gates passed.<br>  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890 strains (not genome counts)<br>  Related STRAININFO_DEPOSIT: 107277 strain-record pairs, 106843 identifiers, 53890 strains (not genome counts)<br>  Related NUCLEOTIDE_SEQUENCE: 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)<br>LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809 records mapped, 324404579 genomes summed across record attestations (not deduplicated)<br>Causal graphs: 0 records (0 evidence-backed edges)<br><br>All TaxonMech quality gates passed. |

## Limits And Additional Notes

- This review is limited to the entire generated record and the specified source evidence. It does not independently re-estimate phylogenetic species boundaries or establish experimental mechanisms from database annotations.
- The NCBI taxonomy snapshot is dated 2026-09-13. Current authority checks are distinguished from pinned source assertions; source coverage and zero imported strains are not worldwide absence claims.
- Historical source counts match the committed inventories, but the locally configured kg-microbe MediaDive, GOLD and Madin edge files have hashes different from data/raw/MANIFEST.yaml. They cannot reproduce the original counts. Required historical edge verification is unavailable; completion remains partial.
- No generated record, page or curation history was edited. Findings and actions are proposed work, not completed fixes or native scientific-status promotion.
- The initial just qc attempt failed because ruff was absent. The locked ruff 0.16.7 dependency was installed only in this isolated environment, and the complete command was retried; the final retry result is recorded above.
- The initial whole-corpus listing found 52 existing actual record targets among 625,960 corpus records. Historical TSV inventories are not substituted for one-record structured bundles.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T233304Z-acidianus_hospitalis_w1
kind: record
repository: CultureBotAI/TaxonMech
title: 'Record review: Acidianus hospitalis W1'
started_at: '2026-10-19T07:24:24Z'
finished_at: '2026-10-19T23:33:04Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: The reviewer did not author or curate the target records. This
    pass only inspects existing data and authors new review bundles in an isolated
    clone.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: NCBITaxon:933801 is correctly identified as the strain Acidianus hospitalis
  W1, but the seeder promotes the broader GTDB Acidianus hospitalis species cluster
  to an exact synonym and equivalent xref. This is one confirmed major scope/grounding
  finding. Source counts and lineage remain intact; historical Madin edge verification
  is unavailable.
source:
  git_revision: 9b5a8fff5185b38dc5c77bb35235152c81ea7765
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 8e8fd97c64fbff27e023c7a768b4c806c98f56cd6571e7102217a2c833284df6
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 4c7090b9d7fd0c6f7f2b4e47b48cbf64835e8d27b44944649e1ccd9038ce462d
    role: context
  - path: AGENTS.md
    sha256: bde64bd1943c4fc64b332cdbc76b89c1460294d9b1042beeedbfa91160a70331
    role: context
  - path: CLAUDE.md
    sha256: 8ae749dbc22700080dcf5e1a0b7ed75710dee6a27f5c7f9e7c6790c26176e5c8
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
    sha256: 5fdc0f7111b64e02439d95c6f2b51fcff1d2154c34b2d957422dd9b297e94d4b
    role: context
  - path: data/atb/MANIFEST.yaml
    sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
    role: context
  - path: data/catalog/MANIFEST.json
    sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
    role: context
  - path: data/catalog/gtdb_genomes-0017.jsonl.gz
    sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
    role: context
  - path: data/catalog/gtdb_genomes-0018.jsonl.gz
    sha256: 8baa314877815777abcdf600079c6ee42f2ea5340398df9f2e18de9c18fd4347
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
  - path: data/raw/ncbitaxon_taxa.tsv
    sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
    role: context
  - path: data/straininfo/MANIFEST.yaml
    sha256: 25dd601c8cf6d4d84e5cc756d1e642ebef89f565bd31967152bf0026fa072847
    role: context
  - path: data/taxa/PATHS.tsv
    sha256: c950844feb0638ce04f7349784749dd1d728fe70bc80f7e2756d956d4ecea254
    role: context
  - path: data/taxa/archaea/acidianus_hospitalis_w1.yaml
    sha256: 732662f934ac729ede67d95ccf42f94aeee0f968754f4ba4b9cbd04dd828d41a
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
  - path: docs/record-review-profile.md
    sha256: d98d6944810090bf9c344ab218d82f8927d73eaad432322b94a876fe9e891334
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: c46d88186cad450fbd47ce5176bf2afc8289252e287324245ad30090753c750e
    role: context
  - path: reviews/structured/20261018T080710Z-round25-sample-3077755/review.yaml
    sha256: be0dc0ef4ecdcb25886de15f6a42266cd34529c3eb5f9417bdd4f35e77bae0a0
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/run_qc.py
    sha256: d3a8e398b0484fef1ce4ae13e639a03dd41467c1d597d753132e4dba04df9da3
    role: context
  - path: scripts/validate_history.py
    sha256: aa8fd8528a28cf56a92768c05d57aea7ff48745510796126f144856b8fd7ae8b
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
  - path: src/taxonmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/taxonmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/taxonmech/schema/taxonmech.yaml
    sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
    role: context
  - path: src/taxonmech/seed.py
    sha256: 6b5b065f4ae7aea022af736a22c0f63dc58a2425c7ee453259e567ab030f8257
    role: context
scope:
  description: The entire single resolved generated TaxonRecord and its identity,
    nomenclature, mapping, strain, source-count and provenance assertions.
  selection: First ten unreviewed corpus paths in lexicographic order at base 9b5a8fff5185b38dc5c77bb35235152c81ea7765;
    this is record 7. Reviewed means an actual target of a validated bundle from scripts/record_review.py
    list. Inventory coverage alone does not count.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - NCBITaxon:933801
targets:
- target_id: NCBITaxon:933801
  path: data/taxa/archaea/acidianus_hospitalis_w1.yaml
  label: Acidianus hospitalis W1
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Maintained generated-record builder
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: Maintained source inventory extractor
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/ncbi_taxdump.py
    role: Maintained NCBI primary-taxonomy projection
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxon identity, name classes and carried ancestry
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit species-or-below scope
checks:
- check_id: identity-authority
  name: Exact NCBI taxon, rank and lineage
  status: passed
  required: true
  summary: NCBITaxon:933801 denotes strain W1 below species 563177, with ten carried
    ancestors and genetic code 11. Pinned and current NCBI agree. The NCBI variants
    'str. W1' and 'strain W1' refer to this strain; the unqualified species label
    does not have the same rank or extension.
  target_ids:
  - NCBITaxon:933801
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - scope-row
  - path-row
- check_id: strain-genome-evidence
  name: Imported strain and genome assertion check
  status: not_applicable
  required: false
  summary: This target has no imported BacDive strain and no strain-level genome assertion.
    Exact source inventory/subtree selection was checked; no deposit or assembly is
    invented from taxon identity.
  target_ids:
  - NCBITaxon:933801
  evidence_ids:
  - record
  - bacdive-inventory
- check_id: historical-source-counts
  name: Original aggregate source-edge multiplicities
  status: unavailable
  required: true
  summary: Inventories support the record's counts, but the original manifest-pinned
    MediaDive/GOLD/Madin edge bytes were unavailable in the checked locations; current
    external files have different hashes. No recount of current data can validate
    the historical numbers.
  target_ids:
  - NCBITaxon:933801
  evidence_ids:
  - manifest
  - historical-edge-availability
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
- check_id: qc-setup-attempt
  name: Initial quality-gate setup attempt
  status: failed
  required: false
  summary: 'Exit 1: missing ruff dependency; environment repaired before the separately
    recorded full retry.'
  target_ids:
  - NCBITaxon:933801
  evidence_ids:
  - qc-setup-receipt
  command: just qc
  exit_code: 1
  expected_exit_code: 0
  scope_note: Superseded environment setup attempt, not the final native QC result.
- check_id: strict
  name: Native strict record validation
  status: passed
  required: true
  summary: Actual terminal exit code 0. This exact generated YAML only.
  target_ids:
  - NCBITaxon:933801
  evidence_ids:
  - strict-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/uv-cache
    just validate-strict data/taxa/archaea/acidianus_hospitalis_w1.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/strict-07.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: This exact generated YAML only.
- check_id: history
  name: Repository history validation
  status: passed
  required: true
  summary: Actual terminal exit code 0. All 17 committed standalone history records;
    generated seed history also inspected in this target.
  target_ids:
  - NCBITaxon:933801
  evidence_ids:
  - history-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/uv-cache
    just validate-history
  exit_code: 0
  expected_exit_code: 0
  scope_note: All 17 committed standalone history records; generated seed history
    also inspected in this target.
- check_id: corpus
  name: Full-corpus exact reproduction
  status: passed
  required: true
  summary: Actual terminal exit code 0. All 625,960 generated taxon YAMLs, not a focused
    approximation.
  target_ids:
  - NCBITaxon:933801
  evidence_ids:
  - corpus-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/uv-cache
    just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  scope_note: All 625,960 generated taxon YAMLs, not a focused approximation.
- check_id: products
  name: Native product ID/label gate
  status: passed
  required: true
  summary: Actual terminal exit code 0. Full configured corpus scan for curator-added
    graph nodes; this target contains no causal graph.
  target_ids:
  - NCBITaxon:933801
  evidence_ids:
  - products-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/uv-cache
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: Full configured corpus scan for curator-added graph nodes; this target
    contains no causal graph.
- check_id: qc
  name: Authoritative complete quality gate
  status: passed
  required: true
  summary: Actual terminal exit code 0. Repository-wide just qc on the isolated checkout;
    includes corpus-wide checks. Pytest reported 1055 passed, 3 skipped and 5 deselected;
    the native QC recipe completed successfully.
  target_ids:
  - NCBITaxon:933801
  evidence_ids:
  - qc-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/uv-cache
    just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: Repository-wide just qc on the isolated checkout; includes corpus-wide
    checks.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/taxa/archaea/acidianus_hospitalis_w1.yaml
  accessed_at: '2026-10-19T23:33:04Z'
  support: supports
  summary: Read the entire generated YAML, including identity, all synonyms, mappings,
    source attestations, every strain assertion and seed history.
  locator: entire TaxonRecord; identifier=NCBITaxon:933801
  snapshot_sha256: 732662f934ac729ede67d95ccf42f94aeee0f968754f4ba4b9cbd04dd828d41a
- evidence_id: taxonomy-inventory
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-19T07:24:26Z'
  support: supports
  summary: Inspected the exact target row and every carried ancestor. Rank, label,
    parent, genetic code and typed source names were compared with the complete record.
  locator: 'line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""};
    line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"};
    line 1798: {"taxon_id":"NCBITaxon:2281","label":"Sulfolobales","rank":"ORDER","parent_id":"NCBITaxon:183924"};
    line 2648: {"taxon_id":"NCBITaxon:12914","label":"Acidianus","rank":"GENUS","parent_id":"NCBITaxon:118883"};
    line 2980: {"taxon_id":"NCBITaxon:28889","label":"Thermoproteota","rank":"PHYLUM","parent_id":"NCBITaxon:1783275"};
    line 22254: {"taxon_id":"NCBITaxon:118883","label":"Sulfolobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2281"};
    line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"};
    line 36612: {"taxon_id":"NCBITaxon:183924","label":"Thermoprotei","rank":"CLASS","parent_id":"NCBITaxon:28889"};
    line 132206: {"taxon_id":"NCBITaxon:563177","label":"Acidianus hospitalis","rank":"SPECIES","parent_id":"NCBITaxon:12914"};
    line 197221: {"taxon_id":"NCBITaxon:933801","label":"Acidianus hospitalis W1","rank":"STRAIN","parent_id":"NCBITaxon:563177","genetic_code":"11","exact_synonyms":"Acidianus
    hospitalis str. W1|Acidianus hospitalis strain W1","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon|gtdb|madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"};
    line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
- evidence_id: scope-row
  kind: database
  reference: curation/seed_scope.tsv
  accessed_at: '2026-10-19T07:24:26Z'
  support: supports
  summary: The exact target is explicitly included in the seed scope.
  locator: 'line 35257: {"identifier":"NCBITaxon:933801","added":"2026-09-12","reason":"attested
    rule: Acidianus hospitalis W1, 3 sources incl. NCBI"}'
  snapshot_sha256: 5fdc0f7111b64e02439d95c6f2b51fcff1d2154c34b2d957422dd9b297e94d4b
- evidence_id: path-row
  kind: database
  reference: data/taxa/PATHS.tsv
  accessed_at: '2026-10-19T07:24:26Z'
  support: supports
  summary: The indexed path resolves to the same NCBI taxon and generated target.
  locator: 'line 612764: {"identifier":"NCBITaxon:933801","slug":"acidianus_hospitalis_w1"}'
  snapshot_sha256: c950844feb0638ce04f7349784749dd1d728fe70bc80f7e2756d956d4ecea254
- evidence_id: ncbi-live
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=933801
  accessed_at: '2026-10-19T07:21:19Z'
  support: supports
  summary: 'Inspected the official current taxonomy response for this exact taxon:
    scientific name, rank, parent, source name classes, lineage identifiers and genetic
    code. Compared it with the separately pinned September taxonomy.'
  locator: TaxaSet/Taxon[TaxId='933801']; captured together with the other nine explicitly
    selected batch taxa
  snapshot_sha256: 520faf6a04c00bf6a23ceda7be536ac20f87f878e83936a21df23f283c23db51
- evidence_id: lpsn-inventory
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-19T07:24:26Z'
  support: supports
  summary: Inspected all exact taxon/name mappings and linked synonymous LPSN names,
    retaining statuses and type-designation scope.
  locator: complete table; exact target/subtree/source-identifier search had no matching
    row
  snapshot_sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: gtdb-mappings
  kind: database
  reference: data/raw/gtdb_mappings.tsv
  accessed_at: '2026-10-19T07:24:26Z'
  support: supports
  summary: Inspected this taxon's GTDB mappings and every reverse mapping of the same
    selected source cluster; predicates and counts remain source-scoped.
  locator: 'line 70969: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","gtdb_label":"s__Acidianus_hospitalis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:1872104","predicate":"skos:broadMatch","genome_count":"7"};
    line 296668: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","gtdb_label":"s__Acidianus_hospitalis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:563177","predicate":"skos:closeMatch","genome_count":"7"};
    line 320834: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","gtdb_label":"s__Acidianus_hospitalis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:933801","predicate":"skos:closeMatch","genome_count":"7"}'
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
- evidence_id: gtdb-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-19T07:24:26Z'
  support: supports
  summary: Inspected source species identifiers, labels, parent cluster and genome
    counts.
  locator: 'line 3494: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","label":"s__Acidianus_hospitalis","parent":"GTDB:g__Acidianus","genome_count":"7"}'
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
- evidence_id: bacdive-inventory
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-19T07:24:26Z'
  support: supports
  summary: Full BacDive inventory selection used the exact taxon plus every descendant
    from the complete NCBI parent graph. Deposits, type status and classified_as remain
    separate from taxon identity.
  locator: complete table; exact target/subtree/source-identifier search had no matching
    row
  snapshot_sha256: 029fd6d1f53ef7f90684130bf0d644ed3edd1d8fbeb065a511ae928f160b1eea
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: culture-inventory
  kind: database
  reference: data/raw/culture_collection_strains.tsv
  accessed_at: '2026-10-19T07:24:26Z'
  support: supports
  summary: Inspected exact culture identifiers associated with the target; source
    aliases do not independently authorize genome joins.
  locator: complete table; exact target/subtree/source-identifier search had no matching
    row
  snapshot_sha256: 810fdcb16abd6330fb15bb03d4c74b18db86be36a7c599df7c6b2498d9735c95
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: gold-organisms
  kind: database
  reference: data/raw/gold_organisms.tsv
  accessed_at: '2026-10-19T07:24:26Z'
  support: supports
  summary: Inspected the exact GOLD organism count row, or its bounded absence, without
    converting counts to phenotypes.
  locator: complete table; exact target/subtree/source-identifier search had no matching
    row
  snapshot_sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: mediadive-taxa
  kind: database
  reference: data/raw/mediadive_taxa.tsv
  accessed_at: '2026-10-19T07:24:26Z'
  support: supports
  summary: Inspected the exact MediaDive medium count row, or its bounded absence,
    without converting counts to phenotypes.
  locator: complete table; exact target/subtree/source-identifier search had no matching
    row
  snapshot_sha256: 3f74b78cadfcdb6aeae953e09fdb39e34fd9c5d5ed0be65a04a5d7fb02355905
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: madin-taxa
  kind: database
  reference: data/raw/madin_taxa.tsv
  accessed_at: '2026-10-19T07:24:26Z'
  support: supports
  summary: Inspected the exact Madin trait-assertion count row, or its bounded absence,
    without converting counts to phenotypes.
  locator: 'line 33029: {"taxon_id":"NCBITaxon:933801","assertion_count":"4"}'
  snapshot_sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
- evidence_id: bactotraits-taxa
  kind: database
  reference: data/raw/bactotraits_taxa.tsv
  accessed_at: '2026-10-19T07:24:26Z'
  support: supports
  summary: Inspected the exact BactoTraits trait-assertion count row, or its bounded
    absence, without converting counts to phenotypes.
  locator: complete table; exact target/subtree/source-identifier search had no matching
    row
  snapshot_sha256: 976d109cef832d8bf27cc105f67a42efbe900b6946736298602ef6d11158b197
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: mapping-policy
  kind: record_content
  reference: docs/HARMONIZATION.md
  accessed_at: '2026-10-19T23:33:04Z'
  support: supports
  summary: The local mapping policy permits one-to-one species closeMatch mappings
    and LPSN-linked species to supply xrefs/synonyms, retains pooled broadMatch entries
    separately, and carries NCBI lineage unchanged.
  locator: Mapping predicates and Scope and lineage sections
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
- evidence_id: equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-19T23:33:04Z'
  support: supports
  summary: TaxonRecord.xrefs denotes true equivalence, while broader/narrower relationships
    belong in taxonomy_mappings; TaxonomyMapping.genome_count counts genomes under
    the source taxon.
  locator: TaxonRecord.xrefs (lines 180–187); TaxonomyMapping (lines 417–439)
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
- evidence_id: seed-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-19T23:33:04Z'
  support: supports
  summary: The identity branch accepts an LPSN GTDB bridge or any skos:closeMatch,
    then emits an equivalent xref and, if the text differs, an EXACT_SYNONYM. It does
    not guard against a strain-rank target.
  locator: GTDB mapping construction and identity promotion, lines 440–472
  snapshot_sha256: 6b5b065f4ae7aea022af736a22c0f63dc58a2425c7ee453259e567ab030f8257
- evidence_id: manifest
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T23:33:04Z'
  support: supports
  summary: The source manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd
    and hashes individual upstream inputs; extraction time is 2026-09-13T17:50:44Z.
  locator: kg_microbe_source, inputs, extracted_at
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
- evidence_id: overlay-manifests
  kind: record_content
  reference: data/atb/MANIFEST.yaml
  accessed_at: '2026-10-19T23:33:04Z'
  support: supports
  summary: Compared raw, ATB and StrainInfo extraction timestamps. Their maximum,
    2026-09-13T17:54:04Z, matches the sole generated seed event. The StrainInfo manifest
    is separately captured in source.inputs.
  locator: extracted_at, together with data/straininfo/MANIFEST.yaml
  snapshot_sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
- evidence_id: genome-catalog-manifest
  kind: record_content
  reference: data/catalog/MANIFEST.json
  accessed_at: '2026-10-19T23:33:04Z'
  support: supports
  summary: The complete native GTDB genome catalog is the RS232 snapshot. Species
    clusters and MAGs remain distinct from physical strain deposits.
  locator: coverage.sources[name=GTDB]
  snapshot_sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
- evidence_id: genome-catalog-1
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0017.jsonl.gz
  accessed_at: '2026-10-19T07:25:21Z'
  support: supports
  summary: Inspected the complete selected genome catalog rows. Source genome identity,
    taxonomic assignment, deposit fields and accession versions were assessed separately.
  locator: 'line 32156: {"accession":"GB_GCA_032249015.1","ncbi_taxid":"1872104","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    hospitalis","ncbi_strain_identifiers":"RBS.bin.2"}; line 37598: {"accession":"RS_GCF_046537415.1","ncbi_taxid":"1872104","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    hospitalis","ncbi_strain_identifiers":"Alice.S.bin.1"}; line 37916: {"accession":"GB_GCA_046533895.1","ncbi_taxid":"563177","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    hospitalis","ncbi_strain_identifiers":"RHS.bin.1"}; line 46762: {"accession":"GB_GCA_003086435.1","ncbi_taxid":"563177","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    hospitalis","ncbi_strain_identifiers":"SCGC AC-742_N10"}; line 47899: {"accession":"RS_GCF_046534395.1","ncbi_taxid":"1872104","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    hospitalis","ncbi_strain_identifiers":"Moose.S.bin.11"}; line 49253: {"accession":"RS_GCF_000213215.1","ncbi_taxid":"933801","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    hospitalis","ncbi_strain_identifiers":"W1"}'
  snapshot_sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
- evidence_id: genome-catalog-2
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0018.jsonl.gz
  accessed_at: '2026-10-19T07:25:21Z'
  support: supports
  summary: Inspected the complete selected genome catalog rows. Source genome identity,
    taxonomic assignment, deposit fields and accession versions were assessed separately.
  locator: 'line 1150: {"accession":"GB_GCA_046533515.1","ncbi_taxid":"1872104","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    hospitalis","ncbi_strain_identifiers":"SBS.bin.13"}'
  snapshot_sha256: 8baa314877815777abcdf600079c6ee42f2ea5340398df9f2e18de9c18fd4347
- evidence_id: historical-edge-availability
  kind: search
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T07:30:22Z'
  support: partial
  summary: The exact configured external paths were checked including ignored files.
    They exist, but each current SHA-256 differs from the manifest-pinned snapshot;
    none was treated as the original extraction input.
  locator: 'data/transformed/mediadive/edges.tsv: expected=78ea275a59d4e2de09a9cf72652ec64454c6a111d2defa1ae0a44bac8a72e523,
    present=4e933d1e2412fb1aad74e60719a6a64dfa34862ff0a6b84e93d78da5ce13dd8b; data/transformed/gold/edges.tsv:
    expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12, present=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d;
    data/transformed/madin_etal/edges.tsv: expected=3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f,
    present=c19bfc848e1b410548614c54a2b99e2c58452d58aeb61f972c99fcb3039a1d24'
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
  search_scope: Exact files beneath the kg_microbe_root in conf/sources.yaml, plus
    an ignored-inclusive search of this isolated clone. No claim that the historical
    snapshots are absent from all storage.
- evidence_id: qc-setup-receipt
  kind: validation
  reference: just qc
  accessed_at: '2026-10-19T07:17:01Z'
  support: context_only
  summary: Initial actual invocation exited 1 because the isolated environment lacked
    ruff. Locked ruff 0.16.7 was then installed in that environment and the full command
    retried; qc below records the retry result.
  locator: initial setup attempt, 2026-10-19T07:17:01Z through 2026-10-19T07:17:01Z
  snapshot_sha256: 1d189beecc64b369096499a7ce4adf71897235e4c1190c69e7d0ed3a77b6a3f9
- evidence_id: strict-receipt
  kind: validation
  reference: just validate-strict data/taxa/archaea/acidianus_hospitalis_w1.yaml --out
    /private/tmp/taxonmech-record-reviews-k0MubV/strict-07.tsv
  accessed_at: '2026-10-19T07:24:26Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo;\
    \ started 2026-10-19T07:24:25Z, finished 2026-10-19T07:24:26Z, exit 0.\nValidating\
    \ 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/strict-07.tsv"
  locator: This exact generated YAML only.
  snapshot_sha256: e324cea3258dbec05aa8c809e5fb656e84451638ff6f8e070f68cb85399a2951
- evidence_id: history-receipt
  kind: validation
  reference: just validate-history
  accessed_at: '2026-10-19T07:17:03Z'
  support: supports
  summary: 'Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo;
    started 2026-10-19T07:17:01Z, finished 2026-10-19T07:17:03Z, exit 0.

    history links: 17 record(s), 0 invalid

    No issues found

    17 history record(s) valid against src/taxonmech/schema/history.yaml'
  locator: All 17 committed standalone history records; generated seed history also
    inspected in this target.
  snapshot_sha256: 3fc63ae7bb58034c180e5dcebec02f98c487038ba74793b9f43462ddaacdcbf4
- evidence_id: corpus-receipt
  kind: validation
  reference: just verify-corpus
  accessed_at: '2026-10-19T07:24:12Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo;\
    \ started 2026-10-19T07:18:23Z, finished 2026-10-19T07:24:12Z, exit 0.\nuv run\
    \ python scripts/verify_corpus.py \nexpected 625960 records, found 625960 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/ and curation/seed_scope.tsv"
  locator: All 625,960 generated taxon YAMLs, not a focused approximation.
  snapshot_sha256: 6bcd0e5b423155259cb8f8dbecb3e4af467b5dba232906734156e9a99fb5a459
- evidence_id: products-receipt
  kind: validation
  reference: just validate-products
  accessed_at: '2026-10-19T07:55:11Z'
  support: supports
  summary: 'Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo;
    started 2026-10-19T07:17:01Z, finished 2026-10-19T07:55:11Z, exit 0.

    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml


    id↔label correspondence summary:


    ✅ All id↔label pairs correspond.'
  locator: Full configured corpus scan for curator-added graph nodes; this target
    contains no causal graph.
  snapshot_sha256: 48dd07515706dc62199fc2205c4b0bfdd5750028037d9b800179f254d2f1eb07
- evidence_id: qc-receipt
  kind: validation
  reference: just qc
  accessed_at: '2026-10-19T08:07:39Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo;\
    \ started 2026-10-19T07:17:41Z, finished 2026-10-19T08:07:39Z, exit 0.\n1055 passed,\
    \ 3 skipped, 5 deselected in 1634.00s (0:27:13)\nValidating 625960 files with\
    \ 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml\n\
    \  files scanned:      625960\nexpected 625960 records, found 625960 on disk\n\
    pages/ is current\nSite publication: 530,864,122 bytes (budget 950,000,000)\n\
    625960 taxon records\n  NCBITAXON        625960\nAll TaxonMech quality gates passed.\n\
    \  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890\
    \ strains (not genome counts)\n  Related STRAININFO_DEPOSIT: 107277 strain-record\
    \ pairs, 106843 identifiers, 53890 strains (not genome counts)\n  Related NUCLEOTIDE_SEQUENCE:\
    \ 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)\n\
    LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809\
    \ records mapped, 324404579 genomes summed across record attestations (not deduplicated)\n\
    Causal graphs: 0 records (0 evidence-backed edges)\n\nAll TaxonMech quality gates\
    \ passed."
  locator: Repository-wide just qc on the isolated checkout; includes corpus-wide
    checks.
  snapshot_sha256: b86a9cc6f529c3b822140f60179e9bc4046e2e6abef3ee0e67fa1035ffb1a76d
assessments:
- assessment_id: identity
  area: identity
  topic: Resolved biological taxon and carried lineage
  outcome: supported
  summary: NCBITaxon:933801 denotes strain W1 below species 563177, with ten carried
    ancestors and genetic code 11. Pinned and current NCBI agree. The NCBI variants
    'str. W1' and 'strain W1' refer to this strain; the unqualified species label
    does not have the same rank or extension.
  target_ids:
  - NCBITaxon:933801
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - scope-row
  - path-row
  dimensions:
  - name: taxon-rank
    value: STRAIN
    definition: NCBI rank of the reviewed target, distinct from strain/deposit/genome
      identity.
    evidence_ids:
    - record
    - taxonomy-inventory
    - ncbi-live
  - name: taxonomy-snapshot
    value: '2026-09-13'
    definition: Pinned NCBI snapshot; current authority is separately identified.
    evidence_ids:
    - taxonomy-inventory
    - manifest
- assessment_id: nomenclature
  area: nomenclature
  topic: Source-scoped names and nomenclatural standing
  outcome: concern
  summary: The two NCBI exact synonyms preserve W1. The GTDB exact synonym Acidianus
    hospitalis drops the strain qualifier and refers to a seven-genome species cluster.
    That scope inflation is not justified by the local policy allowing normalization
    of one-to-one species mappings. No LPSN nomenclature is asserted by this strain
    record.
  target_ids:
  - NCBITaxon:933801
  evidence_ids:
  - record
  - taxonomy-inventory
  - lpsn-inventory
  - gtdb-mappings
  - mapping-policy
- assessment_id: completeness
  area: completeness
  topic: Complete imported subtree and source assertion units
  outcome: supported
  summary: 'No BacDive strain is classified under this exact taxon in the complete
    pinned inventory. Thus strain_count: 0 counts imported BacDive entries, not biological
    strains. The GTDB attestation''s seven GENOMEs are the source-cluster count and
    Madin''s four assertions are direct to W1. The latter cannot be recounted from
    the original pinned upstream edges.'
  target_ids:
  - NCBITaxon:933801
  evidence_ids:
  - record
  - taxonomy-inventory
  - bacdive-inventory
  - culture-inventory
  - gtdb-species
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
  dimensions:
  - name: assertion-units
    value: 'NCBITAXON: 1 NAME; GTDB: 7 GENOME; MADIN: 4 TRAIT_ASSERTION'
    definition: Native source-specific counts; not interchangeable biological measurements.
    evidence_ids:
    - record
    - gold-organisms
    - mediadive-taxa
    - madin-taxa
    - bactotraits-taxa
- assessment_id: taxonomy-mapping
  area: grounding
  topic: GTDB mapping scope and source genome count
  outcome: concern
  summary: GTDB:s__Acidianus_hospitalis maps to NCBITaxon:563177, 933801 and 1872104.
    Among all seven primary cluster rows, only RS_GCF_000213215.1 is classified by
    NCBI as W1 (933801). RHS.bin.1 and SCGC AC-742_N10 are taxon 563177, while RBS.bin.2,
    Alice.S.bin.1, Moose.S.bin.11 and SBS.bin.13 are taxon 1872104. A source membership/closeMatch
    assertion cannot turn the entire species into the W1 strain. The exact synonym
    and xref are produced by seed.py's unguarded closeMatch identity branch.
  target_ids:
  - NCBITaxon:933801
  evidence_ids:
  - record
  - gtdb-mappings
  - gtdb-species
  - mapping-policy
  - equivalence-contract
  - seed-owner
  - genome-catalog-1
  - genome-catalog-2
  dimensions:
  - name: gtdb-release
    value: RS232
    definition: GTDB metadata release recorded in the pinned native catalog manifest;
      not NCBI taxon rank.
    evidence_ids:
    - genome-catalog-manifest
    - genome-catalog-1
    - genome-catalog-2
- assessment_id: native-status
  area: provenance
  topic: Seed event and scientific status boundary
  outcome: supported
  summary: The NCBI identity is grounded EXACT and the record remains SEEDED. Its
    single seed event is consistent with the latest extraction timestamp across raw,
    ATB and StrainInfo manifests (2026-09-13T17:54:04Z). This review neither appends
    history nor promotes native status.
  target_ids:
  - NCBITaxon:933801
  evidence_ids:
  - record
  - manifest
  - overlay-manifests
findings:
- finding_id: gtdb-strain-scope
  issue_key: gtdb-closematch-exact-promotion-933801
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: GTDB species-cluster identity is promoted to exact equivalence with strain
    W1
  description: GTDB:s__Acidianus_hospitalis maps to NCBITaxon:563177, 933801 and 1872104.
    Among all seven primary cluster rows, only RS_GCF_000213215.1 is classified by
    NCBI as W1 (933801). RHS.bin.1 and SCGC AC-742_N10 are taxon 563177, while RBS.bin.2,
    Alice.S.bin.1, Moose.S.bin.11 and SBS.bin.13 are taxon 1872104. A source membership/closeMatch
    assertion cannot turn the entire species into the W1 strain. The exact synonym
    and xref are produced by seed.py's unguarded closeMatch identity branch. The local
    policy concerns one-to-one species mappings; a species-to-strain rank mismatch
    violates the equivalent-xref contract even though it reproduces current seeder
    code.
  target_ids:
  - NCBITaxon:933801
  field_paths:
  - synonyms[source=GTDB].synonym_type
  - xrefs
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - gtdb-mappings
  - gtdb-species
  - equivalence-contract
  - seed-owner
  - mapping-policy
  - genome-catalog-1
  - genome-catalog-2
  rule_id: src/taxonmech/schema/taxonmech.yaml:TaxonRecord.xrefs; docs/record-review-profile.md:strain/taxon/genome
    identity boundary
  native_severity: major
  normalization_reason: Confirmed scope inflation and unsupported exact grounding;
    the target's underlying NCBI identity remains correct.
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Maintained GTDB synonym/xref promotion logic
  - repository: CultureBotAI/TaxonMech
    path: data/raw/gtdb_mappings.tsv
    role: Pinned qualified source mapping; preserve original assertion
  - repository: CultureBotAI/TaxonMech
    path: docs/HARMONIZATION.md
    role: Document the rank boundary for species identity normalization
  related_findings:
  - repository: CultureBotAI/TaxonMech
    review_id: 20261018T080710Z-round25-sample-3077755
    finding_id: gtdb-equivalence
actions:
- action_id: verify-pinned-aggregate-edges
  description: Recover the upstream kg-microbe edge snapshots whose SHA-256 values
    are pinned in data/raw/MANIFEST.yaml, then recount this exact target using the
    maintained extractor's source-specific counting rules. This resolves the historical-count
    limitation without changing generated records.
  finding_ids: []
  target_ids:
  - NCBITaxon:933801
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: data/raw/MANIFEST.yaml
    role: Exact historical input identifiers and hashes
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: MediaDive, GOLD and trait assertion counting rules
  acceptance_checks:
  - Recovered edge files match the manifest SHA-256 values before any comparison.
  - Recount only the target's explicit MediaDive METPO:2000517 medium set, GOLD Go
    subclass assertions and Madin taxon-subject assertions that this record actually
    attests; preserve their distinct units and direct-taxon boundaries.
  - Compare the resulting counts and medium identifiers with the exact inventoried
    rows cited in this review, and retain any discrepancy as a new observation.
- action_id: guard-strain-equivalence
  description: Add an evidence- and rank-aware guard to the maintained seeder so a
    GTDB species closeMatch does not automatically create an EXACT_SYNONYM or equivalent
    xref for a narrower strain. Preserve qualified source mapping and its seven-genome
    cluster count. Clarify the species-versus-strain boundary in the harmonization
    documentation; regenerate only through guarded repository writers during separately
    authorized curation.
  finding_ids:
  - gtdb-strain-scope
  target_ids:
  - NCBITaxon:933801
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Maintained GTDB synonym/xref promotion logic
  - repository: CultureBotAI/TaxonMech
    path: data/raw/gtdb_mappings.tsv
    role: Pinned qualified source mapping; preserve original assertion
  - repository: CultureBotAI/TaxonMech
    path: docs/HARMONIZATION.md
    role: Document the rank boundary for species identity normalization
  generator: src/taxonmech/seed.py
  acceptance_checks:
  - A W1 canary retains NCBITaxon:933801, STRAIN rank, parent 563177, carried lineage
    and the two NCBI W1 synonyms.
  - GTDB:s__Acidianus_hospitalis remains a qualified source mapping with genome_count
    7, without exact species-to-strain synonym/xref promotion absent an explicit appropriate
    identity bridge.
  - A positive species control preserves supported species normalization, including
    LPSN-backed mappings; the guard does not discard source assertions or genome links.
  - After authorized guarded regeneration, run just validate-strict for the affected
    record, just validate-history, just verify-corpus and just qc.
limitations:
- This review is limited to the entire generated record and the specified source evidence.
  It does not independently re-estimate phylogenetic species boundaries or establish
  experimental mechanisms from database annotations.
- The NCBI taxonomy snapshot is dated 2026-09-13. Current authority checks are distinguished
  from pinned source assertions; source coverage and zero imported strains are not
  worldwide absence claims.
- Historical source counts match the committed inventories, but the locally configured
  kg-microbe MediaDive, GOLD and Madin edge files have hashes different from data/raw/MANIFEST.yaml.
  They cannot reproduce the original counts. Required historical edge verification
  is unavailable; completion remains partial.
notes:
- No generated record, page or curation history was edited. Findings and actions are
  proposed work, not completed fixes or native scientific-status promotion.
- The initial just qc attempt failed because ruff was absent. The locked ruff 0.16.7
  dependency was installed only in this isolated environment, and the complete command
  was retried; the final retry result is recorded above.
- The initial whole-corpus listing found 52 existing actual record targets among 625,960
  corpus records. Historical TSV inventories are not substituted for one-record structured
  bundles.
tags:
- record-review
- batch-0001
- archaea
- generated
- source-checked
```
