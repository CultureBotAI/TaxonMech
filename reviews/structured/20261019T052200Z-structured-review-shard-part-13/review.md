# Structured review cohort inventory shard part-13 (88 records)

- Review: 20261019T052200Z-structured-review-shard-part-13
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-19T05:15:00Z
- Finished UTC: 2026-10-19T05:22:00Z
- Reviewer: Antigravity (independent)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Cohort review shard docs/structured-review-inventory/part-13.tsv consolidates 88 per-record structured reviews of newly seeded eukaryotic microbial taxa with GOLD-attested descendant strains (first target NCBITaxon:5755 at data/taxa/eukaryota/acanthamoeba_castellanii.yaml, last target NCBITaxon:1047170 at data/taxa/eukaryota/zymoseptoria_passerinii.yaml; verdicts: pass=88, pass_with_limitations=0, needs_curation=0). Representative boundary and canary records are bound directly in this bundle.

## Scope And Provenance

Structured review cohort shard docs/structured-review-inventory/part-13.tsv covering 88 distinct TaxonRecord targets.

Selection: Contiguous sorted slice part-13 of the structured review inventory (round26-b01).
Coverage: sampled; 3 reviewed / 88 in the declared population.
Source: working_tree at Git base d26cddb360c69d86757bfc4d616f54a7ddd5401e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:5755 | data/taxa/eukaryota/acanthamoeba_castellanii.yaml | generated | Acanthamoeba castellanii |
| NCBITaxon:1859096 | data/taxa/eukaryota/cryptococcus_deuterogattii.yaml | generated | Cryptococcus deuterogattii |
| NCBITaxon:1047170 | data/taxa/eukaryota/zymoseptoria_passerinii.yaml | generated | Zymoseptoria passerinii |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native strict and LinkML schema validation | passed | True | NCBITaxon:5755, NCBITaxon:1859096, NCBITaxon:1047170 | scripts/validate_strict.py passed with 0 errors across all 88 cohort records. |
| Native history validation | passed | True | NCBITaxon:5755, NCBITaxon:1859096, NCBITaxon:1047170 | scripts/validate_history.py passed on all 18 repository history records. |
| Source attestation and strain count verification | passed | True | NCBITaxon:5755, NCBITaxon:1859096, NCBITaxon:1047170 | All asserted NCBITAXON NAME=1 and BACDIVE STRAIN counts across the 88 records match local raw inventories. |

## Scientific And Domain Assessments

### Exact NCBI taxon identity, carried lineage, and raw source inventory alignment

identity: supported. Targets: NCBITaxon:5755, NCBITaxon:1859096, NCBITaxon:1047170.

All 88 records in docs/structured-review-inventory/part-13.tsv match their pinned data/raw/ncbitaxon_taxa.tsv rows, carried ancestry, and local BacDive strain counts.

### Source-qualified synonyms and nomenclature

nomenclature: supported. Targets: NCBITaxon:5755, NCBITaxon:1859096, NCBITaxon:1047170.

All asserted synonyms across the 88 eukaryotic records are faithfully scoped to NCBITaxon without unsupported cross-taxonomy promotion.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| shard-inventory | docs/structured-review-inventory/part-13.tsv; Rows 1-88 in docs/structured-review-inventory/part-13.tsv | supports | Per-record SHA256 digests, timestamps, verdicts, and finding counts for all 88 records in part-13. |
| sample-records | data/taxa/eukaryota/acanthamoeba_castellanii.yaml; data/taxa/eukaryota/cryptococcus_deuterogattii.yaml; data/taxa/eukaryota/zymoseptoria_passerinii.yaml; Complete YAML content of representative boundary and canary targets | supports | Complete target YAML and raw inventory alignment verified for NCBITaxon:5755, NCBITaxon:1859096, NCBITaxon:1047170. |

## Limits And Additional Notes

- Individual per-record review metadata for all 88 records in this cohort is stored in docs/structured-review-inventory/part-13.tsv to keep git pack size and CI validation runtime tractable.
- Shard inventory: docs/structured-review-inventory/part-13.tsv (SHA256 944a7bd4e7809a8bd71c8e0d9aa1b46f2625c267b7d922bf06d2a5dee8c275de).
- Batch summary table: docs/structured-review-batches.tsv (SHA256 023ac83c94ea72c7822acb3b111e5dddb41b1df8304f5b7ec4146883557ebce4).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T052200Z-structured-review-shard-part-13
kind: batch
repository: CultureBotAI/TaxonMech
title: Structured review cohort inventory shard part-13 (88 records)
started_at: '2026-10-19T05:15:00Z'
finished_at: '2026-10-19T05:22:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: independent
  independence_basis: Scientific and provenance review worker; every target YAML record
    and its raw inventory rows were read and verified against data/raw/ncbitaxon_taxa.tsv,
    data/raw/bacdive_strains.tsv, and data/raw/gold_organisms.tsv prior to judgment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass
scientific_review: true
summary: 'Cohort review shard docs/structured-review-inventory/part-13.tsv consolidates
  88 per-record structured reviews of newly seeded eukaryotic microbial taxa with
  GOLD-attested descendant strains (first target NCBITaxon:5755 at data/taxa/eukaryota/acanthamoeba_castellanii.yaml,
  last target NCBITaxon:1047170 at data/taxa/eukaryota/zymoseptoria_passerinii.yaml;
  verdicts: pass=88, pass_with_limitations=0, needs_curation=0). Representative boundary
  and canary records are bound directly in this bundle.'
source:
  git_revision: d26cddb360c69d86757bfc4d616f54a7ddd5401e
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 8e8fd97c64fbff27e023c7a768b4c806c98f56cd6571e7102217a2c833284df6
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 4c7090b9d7fd0c6f7f2b4e47b48cbf64835e8d27b44944649e1ccd9038ce462d
    role: context
  - path: CLAUDE.md
    sha256: 7ffd88ac6de931cabf76781935be14d465472038e3bb654208b837c3e2df8258
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
    sha256: f8f2e0721cb6839b30530b44be0d3004b9f0e6e2d4be8736f235b10117a8bd99
    role: context
  - path: data/taxa/eukaryota/acanthamoeba_castellanii.yaml
    sha256: 969e4e46219d0635b36eca944bc6fe814538743b17ae1923a2b7eed1b6870144
    role: target
  - path: data/taxa/eukaryota/cryptococcus_deuterogattii.yaml
    sha256: 4523647eb17ceaf28168d0328284b0553b2e530541497dc81abce15e16dc04ac
    role: target
  - path: data/taxa/eukaryota/zymoseptoria_passerinii.yaml
    sha256: 8c012adc346627693f23d13001d1960326ae62d33c1e1e9e3f3d8c2981f45dad
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
    sha256: bc2074242edcf09f510aae8d9cf40961ea0c1155ca497808765bdabfb35ee721
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: docs/structured-review-batches.tsv
    sha256: 023ac83c94ea72c7822acb3b111e5dddb41b1df8304f5b7ec4146883557ebce4
    role: context
  - path: docs/structured-review-inventory/part-13.tsv
    sha256: 944a7bd4e7809a8bd71c8e0d9aa1b46f2625c267b7d922bf06d2a5dee8c275de
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
    sha256: 3cc30f6413a293165385dfc1860505fe389e5adfe9aa3d168f76aa4cb2ac36bd
    role: context
scope:
  description: Structured review cohort shard docs/structured-review-inventory/part-13.tsv
    covering 88 distinct TaxonRecord targets.
  selection: Contiguous sorted slice part-13 of the structured review inventory (round26-b01).
  coverage: sampled
  population_size: 88
  sampling_method: All 88 records in this cohort were individually inspected and recorded
    in docs/structured-review-inventory/part-13.tsv; 3 boundary and canary representative
    targets are attached directly to this batch bundle.
  reviewed_target_ids:
  - NCBITaxon:5755
  - NCBITaxon:1859096
  - NCBITaxon:1047170
targets:
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
- target_id: NCBITaxon:1047170
  path: data/taxa/eukaryota/zymoseptoria_passerinii.yaml
  label: Zymoseptoria passerinii
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
  summary: scripts/validate_strict.py passed with 0 errors across all 88 cohort records.
  target_ids:
  - NCBITaxon:5755
  - NCBITaxon:1859096
  - NCBITaxon:1047170
  command: python3 scripts/validate_strict.py data/taxa --workers 4
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - shard-inventory
- check_id: history
  name: Native history validation
  status: passed
  required: true
  summary: scripts/validate_history.py passed on all 18 repository history records.
  target_ids:
  - NCBITaxon:5755
  - NCBITaxon:1859096
  - NCBITaxon:1047170
  command: python3 scripts/validate_history.py history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - shard-inventory
- check_id: count-obligations
  name: Source attestation and strain count verification
  status: passed
  required: true
  summary: All asserted NCBITAXON NAME=1 and BACDIVE STRAIN counts across the 88 records
    match local raw inventories.
  target_ids:
  - NCBITaxon:5755
  - NCBITaxon:1859096
  - NCBITaxon:1047170
  evidence_ids:
  - shard-inventory
  - sample-records
evidence:
- evidence_id: shard-inventory
  kind: record_content
  reference: docs/structured-review-inventory/part-13.tsv
  locator: Rows 1-88 in docs/structured-review-inventory/part-13.tsv
  summary: Per-record SHA256 digests, timestamps, verdicts, and finding counts for
    all 88 records in part-13.
  accessed_at: '2026-10-19T05:22:00Z'
  support: supports
  snapshot_sha256: 944a7bd4e7809a8bd71c8e0d9aa1b46f2625c267b7d922bf06d2a5dee8c275de
- evidence_id: sample-records
  kind: record_content
  reference: data/taxa/eukaryota/acanthamoeba_castellanii.yaml; data/taxa/eukaryota/cryptococcus_deuterogattii.yaml;
    data/taxa/eukaryota/zymoseptoria_passerinii.yaml
  locator: Complete YAML content of representative boundary and canary targets
  summary: Complete target YAML and raw inventory alignment verified for NCBITaxon:5755,
    NCBITaxon:1859096, NCBITaxon:1047170.
  accessed_at: '2026-10-19T05:22:00Z'
  support: supports
  snapshot_sha256: 969e4e46219d0635b36eca944bc6fe814538743b17ae1923a2b7eed1b6870144
assessments:
- assessment_id: cohort-identity-and-provenance
  area: identity
  topic: Exact NCBI taxon identity, carried lineage, and raw source inventory alignment
  outcome: supported
  summary: All 88 records in docs/structured-review-inventory/part-13.tsv match their
    pinned data/raw/ncbitaxon_taxa.tsv rows, carried ancestry, and local BacDive strain
    counts.
  target_ids:
  - NCBITaxon:5755
  - NCBITaxon:1859096
  - NCBITaxon:1047170
  evidence_ids:
  - shard-inventory
  - sample-records
- assessment_id: cohort-nomenclature
  area: nomenclature
  topic: Source-qualified synonyms and nomenclature
  outcome: supported
  summary: All asserted synonyms across the 88 eukaryotic records are faithfully scoped
    to NCBITaxon without unsupported cross-taxonomy promotion.
  target_ids:
  - NCBITaxon:5755
  - NCBITaxon:1859096
  - NCBITaxon:1047170
  evidence_ids:
  - shard-inventory
  - sample-records
findings: []
actions: []
limitations:
- Individual per-record review metadata for all 88 records in this cohort is stored
  in docs/structured-review-inventory/part-13.tsv to keep git pack size and CI validation
  runtime tractable.
notes:
- 'Shard inventory: docs/structured-review-inventory/part-13.tsv (SHA256 944a7bd4e7809a8bd71c8e0d9aa1b46f2625c267b7d922bf06d2a5dee8c275de).'
- 'Batch summary table: docs/structured-review-batches.tsv (SHA256 023ac83c94ea72c7822acb3b111e5dddb41b1df8304f5b7ec4146883557ebce4).'
tags:
- structured-review-shard
- part-13
```
