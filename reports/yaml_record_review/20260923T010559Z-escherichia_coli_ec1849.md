# YAML Record Review: Escherichia coli EC1849
- Repository: TaxonMech
- Record: data/taxa/bacteria/escherichia_coli_ec1849.yaml
- Started UTC: 2026-09-23T01:05:59Z
- Finished UTC: 2026-09-23T01:05:59Z
- Verdict: needs curation

## Target

- YAML record: `data/taxa/bacteria/escherichia_coli_ec1849.yaml`
- Identifier: `NCBITaxon:1005544`
- Label: `Escherichia coli EC1849`
- Rank: `STRAIN`
- Parent: `NCBITaxon:562`
- Registry row: `data/taxa/PATHS.tsv:1777`
- Scope row: `curation/seed_scope.tsv:36026`
- A pre-write `find reports/yaml_record_review ... -name '*-escherichia_coli_ec1849.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/escherichia_coli_ec1849.yaml data/taxa/bacteria/escherichia_coli_ec1850.yaml data/taxa/bacteria/escherichia_coli_ec1856.yaml data/taxa/bacteria/escherichia_coli_ec1862.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/escherichia_coli_ec1849.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, and genetic code agree with `data/raw/ncbitaxon_taxa.tsv:210439`.
- The stored lineage terminates at the asserted parent species `NCBITaxon:562` / `Escherichia coli`.
- `grounding_status: EXACT` is appropriate for the NCBI strain taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210439` attests `NCBITaxon:1005544` as `Escherichia coli EC1849`, rank `STRAIN`, parent `NCBITaxon:562`, genetic code `11`, and NCBI snapshot `2026-09-13`.
- `data/raw/madin_taxa.tsv:311` contributes two Madin trait assertions for `NCBITaxon:1005544`.
- `data/raw/gtdb_mappings.tsv:983` maps `GTDB:s__Escherichia_coli` to `NCBITaxon:1005544` as `skos:closeMatch`.
- `data/raw/gtdb_species.tsv:59219` identifies `GTDB:s__Escherichia_coli` as a 36408-genome GTDB species cluster.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` found no same-taxon rows for `NCBITaxon:1005544`, `Escherichia coli EC1849`, or `escherichia_coli_ec1849`.

## Completeness

- The generated NCBI identity, lineage, Madin attestation, source attestations, and seed history are complete for the local source rows.
- The GTDB mapping and synonym material are present but belong to the broader species cluster, not this strain.

## Findings

- **Major:** the record represents `GTDB:s__Escherichia_coli`, a GTDB species-cluster ID, as a close match, xref, exact synonym source, and genome-count attestation for NCBI strain `Escherichia coli EC1849`. A species cluster with 36408 genomes should not be attached as equivalent to this single strain.

## Recommended Edits

- Repair the GTDB mapping source or the `src/taxonmech/seed.py` projection so species clusters are not emitted onto strain records.
- Regenerate `data/taxa/bacteria/escherichia_coli_ec1849.yaml` after the shared fix and confirm that `GTDB:s__Escherichia_coli` is gone from `taxonomy_mappings`, `source_attestations`, `synonyms`, and `xrefs`.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/escherichia_coli_ec1849.yaml` after regeneration.
- Re-run an exact source scan for `NCBITaxon:1005544` to confirm no strain-specific GTDB source row has replaced the species-cluster row.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
