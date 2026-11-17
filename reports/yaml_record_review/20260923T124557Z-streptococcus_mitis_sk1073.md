# YAML Record Review: Streptococcus mitis SK1073

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/streptococcus_mitis_sk1073.yaml
- Started UTC: 2026-09-23T12:44:16Z
- Finished UTC: 2026-09-23T12:45:59Z
- Verdict: needs curation

## Target

- Path: `data/taxa/bacteria/streptococcus_mitis_sk1073.yaml`
- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1008452`
- Label: `Streptococcus mitis SK1073`
- Rank/domain: `STRAIN` in `BACTERIA`
- Parent: `NCBITaxon:28037` (`Streptococcus mitis`)
- Grounding/mapping: `EXACT` / `SEEDED`
- Generated status: generated from committed source inventories under `data/raw/`, `data/atb/`, and `data/straininfo/`; future fixes belong in those maintained inputs or in the seeder, not in `data/taxa/`.

## Validation

- `just validate-strict data/taxa/bacteria/streptococcus_mitis_sk1073.yaml data/taxa/bacteria/streptococcus_mitis_sk1080.yaml data/taxa/bacteria/staphylococcus_epidermidis_fs1.yaml data/taxa/bacteria/acinetobacter_sp_asd01.yaml` passed: 4 files scanned, 0 files with errors, 0 total error rows.
- `just validate data/taxa/bacteria/streptococcus_mitis_sk1073.yaml` passed with `No issues found`.
- `just validate-history` was skipped because this read-only review did not add or modify any `history/` decisions.
- `just validate-products` was skipped because this record has no `causal_graphs` or curator-added graph nodes to check through the product label gate.
- `just verify-corpus` was skipped for this focused review; earlier full-corpus reproduction over 625,960 records was clean.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1008452` with label `Streptococcus mitis SK1073`, rank `STRAIN`, parent `NCBITaxon:28037`, genetic code `11`, and the two NCBI exact synonyms emitted by the YAML.
- The NCBI identity, strain rank, parent species, and NCBI synonyms are exact.
- The GTDB mapping is over-scoped. `data/raw/gtdb_mappings.tsv` maps GTDB species cluster `GTDB:s__Streptococcus_mitis_AP` to this NCBI strain as `skos:closeMatch` with `genome_count` 3, and `src/taxonmech/seed.py` promotes every `skos:closeMatch` to an xref and exact synonym. A GTDB species cluster is broader than `Streptococcus mitis SK1073` and should not be emitted as a strain-level exact-looking identity.

## Evidence

- NCBI supports the strain label and both NCBI synonyms: `Streptococcus mitis str. SK1073` and `Streptococcus mitis strain SK1073`.
- `data/raw/gtdb_mappings.tsv` supports only that GTDB mapped a species cluster with 3 genomes to this NCBI taxon. It does not support the YAML's `Streptococcus mitis AP` `EXACT_SYNONYM` on a single NCBI strain record.
- `data/raw/madin_taxa.tsv` has one direct `NCBITaxon:1008452` assertion, matching the MADIN source attestation.
- Raw genome rows for BacDive, GOLD, and BV-BRC also carry `NCBITaxon:1008452`, but the BacDive strain itself is classed to `NCBITaxon:1303`; no BacDive strain block is expected on this NCBI strain record.

## Completeness

- `strain_count: 0` is schema-consistent for this strain-rank record; strain listings are species-level aggregates.
- No optional causal graph is expected for this generated record.
- The exact ignored-file-aware `find reports/yaml_record_review -maxdepth 1 -type f -name '*-streptococcus_mitis_sk1073.md'` check found no prior report before this one was written.
- Ignored-file-aware exact `rg` checks over `data/raw`, `data/atb`, `data/straininfo`, `data/bacdive`, and `data/gold` found the NCBI, GTDB, MADIN, and raw strain-genome rows discussed above.

## Findings

- **major**: `GTDB:s__Streptococcus_mitis_AP` is a species cluster projected as strain-level identity. The generated record emits `taxonomy_mappings`, `xrefs`, a GTDB source attestation, and the exact synonym `Streptococcus mitis AP` on `NCBITaxon:1008452`, a rank `STRAIN` record. Owner: `data/raw/gtdb_mappings.tsv` generation and the GTDB mapping, xref, and synonym projection in `src/taxonmech/seed.py`.

## Recommended Edits

- Prevent GTDB species clusters from becoming exact-looking mappings, xrefs, and synonyms on NCBI strain records. Fix the upstream GTDB mapping transform that writes `data/raw/gtdb_mappings.tsv`, then guard `src/taxonmech/seed.py` so `skos:closeMatch` does not imply strain-level identity.

## Follow-up Checks

- Rerun `just seed-canary NCBITaxon:1008452` after the mapping fix and verify that `GTDB:s__Streptococcus_mitis_AP`, the `Streptococcus mitis AP` synonym, and the GTDB source attestation no longer appear on the SK1073 strain record.
- Rerun `just validate-strict data/taxa/bacteria/streptococcus_mitis_sk1073.yaml` and `just verify-corpus`.

## Additional Notes

- Live authority pages were not queried during this batch; the checked-in pinned inventories in `data/raw/`, `data/atb`, and `data/straininfo` were treated as the reproducible source of truth.
