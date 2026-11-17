# YAML Record Review: Streptococcus mitis SK1080

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/streptococcus_mitis_sk1080.yaml
- Started UTC: 2026-09-23T12:44:16Z
- Finished UTC: 2026-09-23T12:45:59Z
- Verdict: needs curation

## Target

- Path: `data/taxa/bacteria/streptococcus_mitis_sk1080.yaml`
- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1008453`
- Label: `Streptococcus mitis SK1080`
- Rank/domain: `STRAIN` in `BACTERIA`
- Parent: `NCBITaxon:28037` (`Streptococcus mitis`)
- Grounding/mapping: `EXACT` / `SEEDED`
- Generated status: generated from committed source inventories under `data/raw/`, `data/atb/`, and `data/straininfo/`; future fixes belong in those maintained inputs or in the seeder, not in `data/taxa/`.

## Validation

- `just validate-strict data/taxa/bacteria/streptococcus_mitis_sk1073.yaml data/taxa/bacteria/streptococcus_mitis_sk1080.yaml data/taxa/bacteria/staphylococcus_epidermidis_fs1.yaml data/taxa/bacteria/acinetobacter_sp_asd01.yaml` passed: 4 files scanned, 0 files with errors, 0 total error rows.
- `just validate data/taxa/bacteria/streptococcus_mitis_sk1080.yaml` passed with `No issues found`.
- `just validate-history` was skipped because this read-only review did not add or modify any `history/` decisions.
- `just validate-products` was skipped because this record has no `causal_graphs` or curator-added graph nodes to check through the product label gate.
- `just verify-corpus` was skipped for this focused review; earlier full-corpus reproduction over 625,960 records was clean.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1008453` with label `Streptococcus mitis SK1080`, rank `STRAIN`, parent `NCBITaxon:28037`, genetic code `11`, and the two NCBI exact synonyms emitted by the YAML.
- The NCBI identity, strain rank, parent species, and NCBI synonyms are exact.
- The GTDB mapping is over-scoped. `data/raw/gtdb_mappings.tsv` maps GTDB species cluster `GTDB:s__Streptococcus_mitis_K` to this NCBI strain as `skos:closeMatch`; even with `genome_count` 1, the GTDB species cluster is broader than the NCBI strain and should not be emitted as a strain-level exact-looking identity.

## Evidence

- NCBI supports the strain label and both NCBI synonyms: `Streptococcus mitis str. SK1080` and `Streptococcus mitis strain SK1080`.
- `data/raw/gtdb_mappings.tsv` supports only that GTDB mapped a species cluster to this NCBI taxon. It does not support the YAML's `Streptococcus mitis K` `EXACT_SYNONYM` on a single NCBI strain record.
- `data/raw/madin_taxa.tsv` has one direct `NCBITaxon:1008453` assertion, matching the MADIN source attestation.
- Raw genome rows for GOLD also carry `NCBITaxon:1008453`, but the BacDive strain itself is classed to `NCBITaxon:1313`; no BacDive strain block is expected on this NCBI strain record.

## Completeness

- `strain_count: 0` is schema-consistent for this strain-rank record; strain listings are species-level aggregates.
- No optional causal graph is expected for this generated record.
- The exact ignored-file-aware `find reports/yaml_record_review -maxdepth 1 -type f -name '*-streptococcus_mitis_sk1080.md'` check found no prior report before this one was written.
- Ignored-file-aware exact `rg` checks over `data/raw`, `data/atb`, `data/straininfo`, `data/bacdive`, and `data/gold` found the NCBI, GTDB, MADIN, and raw strain-genome rows discussed above.

## Findings

- **major**: `GTDB:s__Streptococcus_mitis_K` is a species cluster projected as strain-level identity. The generated record emits `taxonomy_mappings`, `xrefs`, a GTDB source attestation, and the exact synonym `Streptococcus mitis K` on `NCBITaxon:1008453`, a rank `STRAIN` record. Owner: `data/raw/gtdb_mappings.tsv` generation and the GTDB mapping, xref, and synonym projection in `src/taxonmech/seed.py`.

## Recommended Edits

- Prevent GTDB species clusters from becoming exact-looking mappings, xrefs, and synonyms on NCBI strain records. Fix the upstream GTDB mapping transform that writes `data/raw/gtdb_mappings.tsv`, then guard `src/taxonmech/seed.py` so `skos:closeMatch` does not imply strain-level identity.

## Follow-up Checks

- Rerun `just seed-canary NCBITaxon:1008453` after the mapping fix and verify that `GTDB:s__Streptococcus_mitis_K`, the `Streptococcus mitis K` synonym, and the GTDB source attestation no longer appear on the SK1080 strain record.
- Rerun `just validate-strict data/taxa/bacteria/streptococcus_mitis_sk1080.yaml` and `just verify-corpus`.

## Additional Notes

- Live authority pages were not queried during this batch; the checked-in pinned inventories in `data/raw/`, `data/atb`, and `data/straininfo` were treated as the reproducible source of truth.
