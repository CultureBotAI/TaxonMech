# YAML Record Review: Escherichia coli PA38
- Repository: TaxonMech
- Record: data/taxa/bacteria/escherichia_coli_pa38.yaml
- Started UTC: 2026-09-23T00:44:18Z
- Finished UTC: 2026-09-23T00:44:18Z
- Verdict: needs curation

## Target

- YAML record: `data/taxa/bacteria/escherichia_coli_pa38.yaml`
- Identifier: `NCBITaxon:1005506`
- Label: `Escherichia coli PA38`
- Rank: `STRAIN`
- Parent: `NCBITaxon:562`
- Registry row: `data/taxa/PATHS.tsv:1740`
- Scope row: `curation/seed_scope.tsv:35989`
- A pre-write `find reports/yaml_record_review ... -name '*-escherichia_coli_pa38.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/escherichia_coli_pa32.yaml data/taxa/bacteria/escherichia_coli_pa33.yaml data/taxa/bacteria/escherichia_coli_pa34.yaml data/taxa/bacteria/escherichia_coli_pa38.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/escherichia_coli_pa38.yaml` passed with no LinkML issues.

## Identity and Grounding

- The record's identifier, label, rank, bacterial domain, parent taxon, and genetic code agree with `data/raw/ncbitaxon_taxa.tsv:210402`.
- The lineage terminates at `NCBITaxon:562` / `Escherichia coli`, matching the asserted parent species for this NCBI strain.
- `grounding_status: EXACT` is appropriate for the NCBI taxon identity itself.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210402` attests `NCBITaxon:1005506` as strain `Escherichia coli PA38`, parent `NCBITaxon:562`, genetic code `11`, and a `2026-09-13` NCBI snapshot.
- `data/raw/madin_taxa.tsv:274` contributes two Madin trait assertions for `NCBITaxon:1005506`.
- `data/raw/gtdb_mappings.tsv:946` maps `GTDB:s__Escherichia_coli` to `NCBITaxon:1005506` with `skos:closeMatch` and genome count `36408`.
- `data/raw/gtdb_species.tsv:59219` identifies `GTDB:s__Escherichia_coli` as the GTDB species cluster `s__Escherichia_coli` under `GTDB:g__Escherichia`, with `36408` genomes.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` for `NCBITaxon:1005506`, `Escherichia coli PA38`, and `escherichia_coli_pa38` found no same-taxon auxiliary rows.

## Completeness

- The YAML includes the expected NCBI source attestation, Madin source attestation, lineage, generated curation history, GTDB mapping, GTDB xref, and GTDB synonym for the seeded three-source row.
- It is semantically over-complete because the GTDB species cluster is represented on a narrower strain record.

## Findings

- **Major:** `GTDB:s__Escherichia_coli` is a species-cluster ID, but this strain-level record stores it as a `skos:closeMatch`, xref, GTDB source attestation, and `EXACT_SYNONYM` of `Escherichia coli`. That conflates `Escherichia coli PA38` with the full GTDB `Escherichia coli` species cluster.

## Recommended Edits

- Fix `data/raw/gtdb_mappings.tsv` generation and the taxonomy mapping and synonym projection in `src/taxonmech/seed.py` so GTDB species clusters are not attached to NCBI strain records as exact or close equivalents.
- Regenerate the record so `GTDB:s__Escherichia_coli` is removed from `taxonomy_mappings`, `source_attestations`, `synonyms`, and `xrefs` unless a strain-specific GTDB record is available.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/escherichia_coli_pa38.yaml` after regeneration.
- Re-check that the regenerated YAML has no exact synonym equating this PA38 strain node with species-level text `Escherichia coli`.

## Additional Notes

- Live NCBI and GTDB lookups were not used; this review treats the pinned local rows in `data/raw/`, `data/atb/`, and `data/straininfo/` as source of truth.
- `just validate-history` was not run because the read-only review creates no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.

