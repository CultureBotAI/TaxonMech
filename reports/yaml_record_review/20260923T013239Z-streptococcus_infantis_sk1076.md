# YAML Record Review: Streptococcus infantis SK1076
- Repository: TaxonMech
- Record: data/taxa/bacteria/streptococcus_infantis_sk1076.yaml
- Started UTC: 2026-09-23T01:32:39Z
- Finished UTC: 2026-09-23T01:32:39Z
- Verdict: needs curation

## Target

- YAML record: `data/taxa/bacteria/streptococcus_infantis_sk1076.yaml`
- Identifier: `NCBITaxon:1005705`
- Label: `Streptococcus infantis SK1076`
- Rank: `STRAIN`
- Parent: `NCBITaxon:68892`
- Registry row: `data/taxa/PATHS.tsv:1820`
- Scope row: `curation/seed_scope.tsv:36051`
- A pre-write `find reports/yaml_record_review ... -name '*-streptococcus_infantis_sk1076.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/kosakonia_oryziphila.yaml data/taxa/bacteria/propionibacterium_sp_cc003_hc2.yaml data/taxa/bacteria/streptococcus_oralis_sk255.yaml data/taxa/bacteria/streptococcus_infantis_sk1076.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/streptococcus_infantis_sk1076.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, genetic code, and NCBI strain synonyms agree with `data/raw/ncbitaxon_taxa.tsv:210482`.
- The stored lineage terminates at the asserted parent species `NCBITaxon:68892` / `Streptococcus infantis`.
- `grounding_status: EXACT` is appropriate for the NCBI strain taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210482` attests `NCBITaxon:1005705` as `Streptococcus infantis SK1076`, rank `STRAIN`, parent `NCBITaxon:68892`, genetic code `11`, NCBI aliases, and NCBI snapshot `2026-09-13`.
- `data/raw/madin_taxa.tsv:337` contributes one Madin trait assertion for `NCBITaxon:1005705`.
- `data/raw/gtdb_mappings.tsv:1011` maps `GTDB:s__Streptococcus_infantis_B` to `NCBITaxon:1005705` as `skos:closeMatch`.
- `data/raw/gtdb_species.tsv:168813` identifies `GTDB:s__Streptococcus_infantis_B` as a 7-genome GTDB species cluster.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` found no same-taxon rows for `NCBITaxon:1005705`, `Streptococcus infantis SK1076`, or `streptococcus_infantis_sk1076`.

## Completeness

- The generated NCBI identity, lineage, NCBI synonyms, Madin attestation, source attestations, and seed history are complete for the local source rows.
- The GTDB mapping and synonym material are present but belong to the broader species cluster, not this strain.

## Findings

- **Major:** the record represents `GTDB:s__Streptococcus_infantis_B`, a GTDB species-cluster ID, as a close match, xref, exact synonym source, and genome-count attestation for NCBI strain `Streptococcus infantis SK1076`. A species cluster with 7 genomes should not be attached as equivalent to this single strain.

## Recommended Edits

- Repair the GTDB mapping source or the `src/taxonmech/seed.py` projection so species clusters are not emitted onto strain records.
- Regenerate `data/taxa/bacteria/streptococcus_infantis_sk1076.yaml` after the shared fix and confirm that `GTDB:s__Streptococcus_infantis_B` is gone from `taxonomy_mappings`, `source_attestations`, `synonyms`, and `xrefs`.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/streptococcus_infantis_sk1076.yaml` after regeneration.
- Re-run an exact source scan for `NCBITaxon:1005705` to confirm no strain-specific GTDB source row has replaced the species-cluster row.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
