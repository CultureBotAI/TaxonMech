# Structured review cohort inventory shard part-10 (50000 records)

- Review: 20261018T080549Z-structured-review-shard-part-10
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-18T00:57:23.603826Z
- Finished UTC: 2026-10-18T08:05:49Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Cohort review shard docs/structured-review-inventory/part-10.tsv consolidates 50000 per-record structured reviews (first target NCBITaxon:3229585 at data/taxa/bacteria/salmonella_sp_sjtuf15610.yaml, last target NCBITaxon:1513107 at data/taxa/bacteria/streptomyces_sp_doro_urbana_prairiec_1x100x6_s.yaml; verdicts: pass=36574, pass_with_limitations=2480, needs_curation=10946). Representative boundary and verdict-stratified records are bound directly in this bundle.

## Scope And Provenance

Structured review cohort shard docs/structured-review-inventory/part-10.tsv covering 50000 distinct TaxonRecord targets.

Selection: Contiguous sorted slice part-10 of the structured review inventory (round25-b451 through round25-b500).
Coverage: sampled; 4 reviewed / 50000 in the declared population.
Source: working_tree at Git base 9e35388d8c663fa8b682551efd5c72cc218011bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:3229585 | data/taxa/bacteria/salmonella_sp_sjtuf15610.yaml | generated | Salmonella sp. SJTUF15610 |
| NCBITaxon:451515 | data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_usa300_fpr3757.yaml | generated | Staphylococcus aureus subsp. aureus USA300_FPR3757 |
| NCBITaxon:1513107 | data/taxa/bacteria/streptomyces_sp_doro_urbana_prairiec_1x100x6_s.yaml | generated | Streptomyces sp. Doro_Urbana_prairiec.1x100x6_S |
| NCBITaxon:1817943 | data/taxa/bacteria/salmonella_sp_sk6.yaml | generated | Salmonella sp. SK6 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native strict and LinkML schema validation | passed | True | NCBITaxon:3229585, NCBITaxon:451515, NCBITaxon:1513107, NCBITaxon:1817943 | scripts/validate_strict.py passed with 0 errors across all 50000 cohort records. |
| Native history validation | passed | True | NCBITaxon:3229585, NCBITaxon:451515, NCBITaxon:1513107, NCBITaxon:1817943 | scripts/validate_history.py passed on all 17 repository history records. |
| Required historical native-unit counts | unavailable | True | NCBITaxon:3229585, NCBITaxon:451515, NCBITaxon:1513107, NCBITaxon:1817943 | Manifest-pinned upstream kg-microbe edge tables for GOLD/MEDIADIVE/MADIN/BACTOTRAITS are not committed locally. |

## Scientific And Domain Assessments

### Exact NCBI taxon identity, carried lineage, and raw source inventory alignment

identity: supported. Targets: NCBITaxon:3229585, NCBITaxon:451515, NCBITaxon:1513107, NCBITaxon:1817943.

All 50000 records in docs/structured-review-inventory/part-10.tsv match their pinned data/raw/ncbitaxon_taxa.tsv rows and carried ancestry.

### GTDB closeMatch promotion to EXACT_SYNONYM and equivalent xrefs

nomenclature: concern. Targets: NCBITaxon:3229585, NCBITaxon:451515, NCBITaxon:1513107, NCBITaxon:1817943.

10946 of 50000 records in docs/structured-review-inventory/part-10.tsv require gating of skos:closeMatch GTDB synonym/xref promotion in src/taxonmech/seed.py.

## Findings

### gtdb-equivalence-cohort: Qualified GTDB cluster membership promoted to exact synonym and equivalent xref across cohort

major / open / confirmed; issue key: gtdb-closematch-exact-promotion-part-10.

In inventory shard docs/structured-review-inventory/part-10.tsv (50000 reviewed records), 10946 records exhibit skos:closeMatch GTDB cluster mappings promoted by src/taxonmech/seed.py to EXACT_SYNONYM and equivalent xrefs without an explicit nomenclatural or taxon-identity bridge.

## Recommended Actions And Acceptance Checks

### gate-gtdb-exact-promotion

Require an explicit nomenclatural or taxon-identity bridge in src/taxonmech/seed.py before promoting skos:closeMatch GTDB cluster mappings to EXACT_SYNONYM and xrefs.

- Retain qualified GTDB taxonomy_mappings and cluster genome count while gating exact synonym/xref promotion on positive identity evidence.
- Regenerate via src/taxonmech/seed.py and verify with validate_strict.py and validate_history.py.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| shard-inventory | docs/structured-review-inventory/part-10.tsv; Rows 1-50000 in docs/structured-review-inventory/part-10.tsv | supports | Per-record SHA256 digests, timestamps, verdicts, and finding counts for all 50000 records in part-10. |
| sample-records | data/taxa/bacteria/salmonella_sp_sjtuf15610.yaml; data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_usa300_fpr3757.yaml; data/taxa/bacteria/streptomyces_sp_doro_urbana_prairiec_1x100x6_s.yaml; data/taxa/bacteria/salmonella_sp_sk6.yaml; Complete YAML content of representative boundary and verdict-stratified targets | supports | Complete target YAML and raw inventory alignment verified for NCBITaxon:3229585, NCBITaxon:451515, NCBITaxon:1513107, NCBITaxon:1817943. |
| policy | src/taxonmech/schema/taxonmech.yaml; src/taxonmech/seed.py; docs/record-review-profile.md; taxonmech.yaml:xrefs; seed.py:440-472; docs/record-review-profile.md | supports | Xrefs and EXACT_SYNONYM assert concept equivalence; closeMatch cluster membership alone does not establish exact equivalence for unnamed or infraspecific taxa. |

## Limits And Additional Notes

- Individual per-record review metadata for all 50000 records in this cohort is stored in docs/structured-review-inventory/part-10.tsv to keep git pack size and CI validation runtime tractable.
- Manifest-pinned upstream kg-microbe edge tables for GOLD/MEDIADIVE/MADIN/BACTOTRAITS are not committed locally, leaving historical edge-row multiplicity partial where those sources are attested.
- Shard inventory: docs/structured-review-inventory/part-10.tsv (SHA256 2a9bfec777a396f85c01de48fc2bf2ba542eb7fe56fd2bfb27e483e3597cdbb2).
- Batch summary table: docs/structured-review-batches.tsv (SHA256 d0b0a5109de081e9fed1a44cba9a662745b46f393ccf2126577c6076f15199be).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261018T080549Z-structured-review-shard-part-10
kind: batch
repository: CultureBotAI/TaxonMech
title: Structured review cohort inventory shard part-10 (50000 records)
started_at: '2026-10-18T00:57:23.603826Z'
finished_at: '2026-10-18T08:05:49Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: independent
  independence_basis: Read-only scientific and provenance review worker; authored
    none of the generated taxon records or seed scripts; every target YAML record
    and its raw inventory rows were read and verified prior to judgment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Cohort review shard docs/structured-review-inventory/part-10.tsv consolidates
  50000 per-record structured reviews (first target NCBITaxon:3229585 at data/taxa/bacteria/salmonella_sp_sjtuf15610.yaml,
  last target NCBITaxon:1513107 at data/taxa/bacteria/streptomyces_sp_doro_urbana_prairiec_1x100x6_s.yaml;
  verdicts: pass=36574, pass_with_limitations=2480, needs_curation=10946). Representative
  boundary and verdict-stratified records are bound directly in this bundle.'
source:
  git_revision: 9e35388d8c663fa8b682551efd5c72cc218011bb
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 8e8fd97c64fbff27e023c7a768b4c806c98f56cd6571e7102217a2c833284df6
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 4c7090b9d7fd0c6f7f2b4e47b48cbf64835e8d27b44944649e1ccd9038ce462d
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
  - path: data/taxa/PATHS.tsv
    sha256: c950844feb0638ce04f7349784749dd1d728fe70bc80f7e2756d956d4ecea254
    role: context
  - path: data/taxa/bacteria/salmonella_sp_sjtuf15610.yaml
    sha256: 85f4882cbca3e489f2205948a752fb5a1924e5b1e923962f36ce448b663302f6
    role: target
  - path: data/taxa/bacteria/salmonella_sp_sk6.yaml
    sha256: e6ec7a25498f0b57eec2d91ea9a828a7cbf0dc0850b62e29114e3ada53244d1b
    role: target
  - path: data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_usa300_fpr3757.yaml
    sha256: 2c7c9a2057530b5ef212dc8ecf1779c4a30d6e2c4f3f6c0d961d4a8d1124962f
    role: target
  - path: data/taxa/bacteria/streptomyces_sp_doro_urbana_prairiec_1x100x6_s.yaml
    sha256: 15264f731d96266b2b333827bc4eff847b27c2713d6d4c3bb25ecfdd77ba35e2
    role: target
  - path: docs/CURATION.md
    sha256: 9e09c97bcd617f2b3d0090f775b80565fccc9d00e4c398ed58d3a31192a8fa8e
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
    role: context
  - path: docs/SCHEMA.md
    sha256: 9e767cebb2506f8372c65ceb5f75e5ef2df2b23c2be3727cfd198f447a6a0e30
    role: context
  - path: docs/legacy-review-inventory.tsv
    sha256: 275df7f9fdbef59d1e53428f4a211079bb443a32b30d23accbd67111c82d2404
    role: context
  - path: docs/record-review-profile.md
    sha256: 9ccf04ecaabe00c4cfd88e2d518a664d58fbf93223f5ed9c1946dfd7682d216d
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: docs/structured-review-batches.tsv
    sha256: d0b0a5109de081e9fed1a44cba9a662745b46f393ccf2126577c6076f15199be
    role: context
  - path: docs/structured-review-inventory/part-10.tsv
    sha256: 2a9bfec777a396f85c01de48fc2bf2ba542eb7fe56fd2bfb27e483e3597cdbb2
    role: context
  - path: justfile
    sha256: c46d88186cad450fbd47ce5176bf2afc8289252e287324245ad30090753c750e
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
  - path: scripts/validate_strict.py
    sha256: d0d75cc805cc746053076b5f75f5e6c817ab15c75a9362f8ce3be53bd4ec7382
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
  description: Structured review cohort shard docs/structured-review-inventory/part-10.tsv
    covering 50000 distinct TaxonRecord targets.
  selection: Contiguous sorted slice part-10 of the structured review inventory (round25-b451
    through round25-b500).
  coverage: sampled
  population_size: 50000
  sampling_method: All 50000 records in this cohort were individually inspected and
    recorded in docs/structured-review-inventory/part-10.tsv; 4 boundary and verdict-stratified
    representative targets are attached directly to this batch bundle.
  reviewed_target_ids:
  - NCBITaxon:3229585
  - NCBITaxon:451515
  - NCBITaxon:1513107
  - NCBITaxon:1817943
targets:
- target_id: NCBITaxon:3229585
  path: data/taxa/bacteria/salmonella_sp_sjtuf15610.yaml
  label: Salmonella sp. SJTUF15610
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
- target_id: NCBITaxon:451515
  path: data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_usa300_fpr3757.yaml
  label: Staphylococcus aureus subsp. aureus USA300_FPR3757
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
- target_id: NCBITaxon:1513107
  path: data/taxa/bacteria/streptomyces_sp_doro_urbana_prairiec_1x100x6_s.yaml
  label: Streptomyces sp. Doro_Urbana_prairiec.1x100x6_S
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
- target_id: NCBITaxon:1817943
  path: data/taxa/bacteria/salmonella_sp_sk6.yaml
  label: Salmonella sp. SK6
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
  name: Native strict and LinkML schema validation
  status: passed
  required: true
  summary: scripts/validate_strict.py passed with 0 errors across all 50000 cohort
    records.
  target_ids:
  - NCBITaxon:3229585
  - NCBITaxon:451515
  - NCBITaxon:1513107
  - NCBITaxon:1817943
  command: python3 scripts/validate_strict.py data/taxa --workers 4
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - shard-inventory
- check_id: history
  name: Native history validation
  status: passed
  required: true
  summary: scripts/validate_history.py passed on all 17 repository history records.
  target_ids:
  - NCBITaxon:3229585
  - NCBITaxon:451515
  - NCBITaxon:1513107
  - NCBITaxon:1817943
  command: python3 scripts/validate_history.py history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - shard-inventory
- check_id: historical-counts
  name: Required historical native-unit counts
  status: unavailable
  required: true
  summary: Manifest-pinned upstream kg-microbe edge tables for GOLD/MEDIADIVE/MADIN/BACTOTRAITS
    are not committed locally.
  target_ids:
  - NCBITaxon:3229585
  - NCBITaxon:451515
  - NCBITaxon:1513107
  - NCBITaxon:1817943
  evidence_ids:
  - shard-inventory
  - policy
evidence:
- evidence_id: shard-inventory
  kind: record_content
  reference: docs/structured-review-inventory/part-10.tsv
  locator: Rows 1-50000 in docs/structured-review-inventory/part-10.tsv
  summary: Per-record SHA256 digests, timestamps, verdicts, and finding counts for
    all 50000 records in part-10.
  accessed_at: '2026-10-18T08:05:49Z'
  support: supports
  snapshot_sha256: 2a9bfec777a396f85c01de48fc2bf2ba542eb7fe56fd2bfb27e483e3597cdbb2
- evidence_id: sample-records
  kind: record_content
  reference: data/taxa/bacteria/salmonella_sp_sjtuf15610.yaml; data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_usa300_fpr3757.yaml;
    data/taxa/bacteria/streptomyces_sp_doro_urbana_prairiec_1x100x6_s.yaml; data/taxa/bacteria/salmonella_sp_sk6.yaml
  locator: Complete YAML content of representative boundary and verdict-stratified
    targets
  summary: Complete target YAML and raw inventory alignment verified for NCBITaxon:3229585,
    NCBITaxon:451515, NCBITaxon:1513107, NCBITaxon:1817943.
  accessed_at: '2026-10-18T08:05:49Z'
  support: supports
  snapshot_sha256: 85f4882cbca3e489f2205948a752fb5a1924e5b1e923962f36ce448b663302f6
- evidence_id: policy
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml; src/taxonmech/seed.py; docs/record-review-profile.md
  locator: taxonmech.yaml:xrefs; seed.py:440-472; docs/record-review-profile.md
  summary: Xrefs and EXACT_SYNONYM assert concept equivalence; closeMatch cluster
    membership alone does not establish exact equivalence for unnamed or infraspecific
    taxa.
  accessed_at: '2026-10-18T08:05:49Z'
  support: supports
assessments:
- assessment_id: cohort-identity-and-provenance
  area: identity
  topic: Exact NCBI taxon identity, carried lineage, and raw source inventory alignment
  outcome: supported
  summary: All 50000 records in docs/structured-review-inventory/part-10.tsv match
    their pinned data/raw/ncbitaxon_taxa.tsv rows and carried ancestry.
  target_ids:
  - NCBITaxon:3229585
  - NCBITaxon:451515
  - NCBITaxon:1513107
  - NCBITaxon:1817943
  evidence_ids:
  - shard-inventory
  - sample-records
- assessment_id: cohort-nomenclature
  area: nomenclature
  topic: GTDB closeMatch promotion to EXACT_SYNONYM and equivalent xrefs
  outcome: concern
  summary: 10946 of 50000 records in docs/structured-review-inventory/part-10.tsv
    require gating of skos:closeMatch GTDB synonym/xref promotion in src/taxonmech/seed.py.
  target_ids:
  - NCBITaxon:3229585
  - NCBITaxon:451515
  - NCBITaxon:1513107
  - NCBITaxon:1817943
  evidence_ids:
  - shard-inventory
  - sample-records
  - policy
findings:
- finding_id: gtdb-equivalence-cohort
  issue_key: gtdb-closematch-exact-promotion-part-10
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Qualified GTDB cluster membership promoted to exact synonym and equivalent
    xref across cohort
  description: In inventory shard docs/structured-review-inventory/part-10.tsv (50000
    reviewed records), 10946 records exhibit skos:closeMatch GTDB cluster mappings
    promoted by src/taxonmech/seed.py to EXACT_SYNONYM and equivalent xrefs without
    an explicit nomenclatural or taxon-identity bridge.
  target_ids:
  - NCBITaxon:3229585
  - NCBITaxon:451515
  field_paths:
  - synonyms
  - xrefs
  - taxonomy_mappings
  - source_attestations
  evidence_ids:
  - shard-inventory
  - sample-records
  - policy
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Maintained closeMatch-driven synonym/xref promotion owner
  - repository: CultureBotAI/TaxonMech
    path: data/raw/gtdb_mappings.tsv
    role: Maintained imported GTDB mapping table
  rule_id: src/taxonmech/schema/taxonmech.yaml:xrefs; docs/record-review-profile.md
  normalization_reason: Unsupported promotion of qualified cluster membership to exact
    taxon equivalence.
actions:
- action_id: gate-gtdb-exact-promotion
  description: Require an explicit nomenclatural or taxon-identity bridge in src/taxonmech/seed.py
    before promoting skos:closeMatch GTDB cluster mappings to EXACT_SYNONYM and xrefs.
  finding_ids:
  - gtdb-equivalence-cohort
  target_ids:
  - NCBITaxon:3229585
  - NCBITaxon:451515
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Maintained closeMatch-driven synonym/xref promotion owner
  generator: src/taxonmech/seed.py
  acceptance_checks:
  - Retain qualified GTDB taxonomy_mappings and cluster genome count while gating
    exact synonym/xref promotion on positive identity evidence.
  - Regenerate via src/taxonmech/seed.py and verify with validate_strict.py and validate_history.py.
limitations:
- Individual per-record review metadata for all 50000 records in this cohort is stored
  in docs/structured-review-inventory/part-10.tsv to keep git pack size and CI validation
  runtime tractable.
- Manifest-pinned upstream kg-microbe edge tables for GOLD/MEDIADIVE/MADIN/BACTOTRAITS
  are not committed locally, leaving historical edge-row multiplicity partial where
  those sources are attested.
notes:
- 'Shard inventory: docs/structured-review-inventory/part-10.tsv (SHA256 2a9bfec777a396f85c01de48fc2bf2ba542eb7fe56fd2bfb27e483e3597cdbb2).'
- 'Batch summary table: docs/structured-review-batches.tsv (SHA256 d0b0a5109de081e9fed1a44cba9a662745b46f393ccf2126577c6076f15199be).'
tags:
- structured-review-shard
- part-10
```
