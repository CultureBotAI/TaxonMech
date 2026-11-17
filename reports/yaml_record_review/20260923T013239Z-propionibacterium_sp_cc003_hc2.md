# YAML Record Review: Propionibacterium sp. CC003-HC2
- Repository: TaxonMech
- Record: data/taxa/bacteria/propionibacterium_sp_cc003_hc2.yaml
- Started UTC: 2026-09-23T01:32:39Z
- Finished UTC: 2026-09-23T01:32:39Z
- Verdict: needs curation

## Target

- YAML record: `data/taxa/bacteria/propionibacterium_sp_cc003_hc2.yaml`
- Identifier: `NCBITaxon:1005703`
- Label: `Propionibacterium sp. CC003-HC2`
- Rank: `SPECIES`
- Parent: `NCBITaxon:2608905`
- Registry row: `data/taxa/PATHS.tsv:1818`
- Scope row: `curation/seed_scope.tsv:36049`
- A pre-write `find reports/yaml_record_review ... -name '*-propionibacterium_sp_cc003_hc2.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/kosakonia_oryziphila.yaml data/taxa/bacteria/propionibacterium_sp_cc003_hc2.yaml data/taxa/bacteria/streptococcus_oralis_sk255.yaml data/taxa/bacteria/streptococcus_infantis_sk1076.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/propionibacterium_sp_cc003_hc2.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, and genetic code agree with `data/raw/ncbitaxon_taxa.tsv:210480`.
- The stored lineage terminates at the asserted parent `NCBITaxon:2608905` / `unclassified Propionibacterium`.
- `grounding_status: EXACT` is appropriate for the NCBI species taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210480` attests `NCBITaxon:1005703` as `Propionibacterium sp. CC003-HC2`, rank `SPECIES`, parent `NCBITaxon:2608905`, genetic code `11`, and NCBI snapshot `2026-09-13`.
- `data/raw/madin_taxa.tsv:335` contributes six Madin trait assertions for `NCBITaxon:1005703`.
- `data/raw/gtdb_mappings.tsv:1009` maps `GTDB:s__Cutibacterium_acnes` to `NCBITaxon:1005703` as `skos:closeMatch`.
- `data/raw/gtdb_species.tsv:47767` identifies `GTDB:s__Cutibacterium_acnes` as a 544-genome GTDB species cluster.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` found no same-taxon rows for `NCBITaxon:1005703`, `Propionibacterium sp. CC003-HC2`, or `propionibacterium_sp_cc003_hc2`.

## Completeness

- The generated NCBI identity, lineage, Madin attestation, source attestations, and seed history are complete for the local source rows.
- The GTDB mapping and synonym material are present but belong to named species `Cutibacterium acnes`, not this unclassified `Propionibacterium` isolate.

## Findings

- **Major:** the record represents `GTDB:s__Cutibacterium_acnes`, a 544-genome GTDB `Cutibacterium acnes` species-cluster ID, as a close match, xref, exact synonym source, and genome-count attestation for NCBI species placeholder `Propionibacterium sp. CC003-HC2`. That named GTDB species should not be attached as equivalent to this unclassified NCBI species record.

## Recommended Edits

- Repair the GTDB mapping source or the `src/taxonmech/seed.py` projection so named GTDB species clusters are not emitted as exact synonym material on unclassified isolate records.
- Regenerate `data/taxa/bacteria/propionibacterium_sp_cc003_hc2.yaml` after the shared fix and confirm that `GTDB:s__Cutibacterium_acnes` is gone from `taxonomy_mappings`, `source_attestations`, `synonyms`, and `xrefs`.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/propionibacterium_sp_cc003_hc2.yaml` after regeneration.
- Re-run an exact source scan for `NCBITaxon:1005703` to confirm no strain-specific GTDB source row has replaced the named-species row.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
