# YAML Record Review: Escherichia coli PA47
- Repository: TaxonMech
- Record: data/taxa/bacteria/escherichia_coli_pa47.yaml
- Started UTC: 2026-09-23T00:48:37Z
- Finished UTC: 2026-09-23T00:48:37Z
- Verdict: needs curation

## Target

- YAML record: `data/taxa/bacteria/escherichia_coli_pa47.yaml`
- Identifier: `NCBITaxon:1005512`
- Label: `Escherichia coli PA47`
- Rank: `STRAIN`
- Parent: `NCBITaxon:562`
- Registry row: `data/taxa/PATHS.tsv:1746`
- Scope row: `curation/seed_scope.tsv:35995`
- A pre-write `find reports/yaml_record_review ... -name '*-escherichia_coli_pa47.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/escherichia_coli_pa45.yaml data/taxa/bacteria/escherichia_coli_pa47.yaml data/taxa/bacteria/escherichia_coli_pa48.yaml data/taxa/bacteria/escherichia_coli_pa49.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/escherichia_coli_pa47.yaml` passed with no LinkML issues.

## Identity and Grounding

- The record's identifier, label, strain rank, bacterial domain, parent, and genetic code agree with the pinned NCBI row at `data/raw/ncbitaxon_taxa.tsv:210408`.
- The stored lineage correctly places the strain under species `NCBITaxon:562` / `Escherichia coli`.
- The NCBI taxon grounding is exact for `NCBITaxon:1005512`.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210408` attests `NCBITaxon:1005512` as strain `Escherichia coli PA47`, parent `NCBITaxon:562`, genetic code `11`, and NCBI snapshot `2026-09-13`.
- `data/raw/madin_taxa.tsv:280` contributes one Madin trait assertion for `NCBITaxon:1005512`.
- `data/raw/gtdb_mappings.tsv:952` maps `GTDB:s__Escherichia_coli` to `NCBITaxon:1005512` with `skos:closeMatch` and genome count `36408`.
- `data/raw/gtdb_species.tsv:59219` identifies `GTDB:s__Escherichia_coli` as a GTDB species cluster with `36408` genomes.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` found no rows for `NCBITaxon:1005512`, `Escherichia coli PA47`, or `escherichia_coli_pa47`.

## Completeness

- The generated record includes the expected NCBI, GTDB, and Madin attestations for a three-source seed.
- It is not semantically complete as a strain record because the GTDB species cluster has been promoted into strain-level equivalence slots.

## Findings

- **Major:** `GTDB:s__Escherichia_coli` is projected as a `skos:closeMatch`, xref, GTDB attestation, and `EXACT_SYNONYM` of `Escherichia coli` on NCBI strain `Escherichia coli PA47`. That GTDB ID denotes the species cluster `s__Escherichia_coli`, so it should not be asserted as an equivalent identifier for a single PA47 strain node.

## Recommended Edits

- Change the GTDB mapping generation and `src/taxonmech/seed.py` synonym projection so species-cluster GTDB rows do not become exact or close strain mappings.
- Regenerate the YAML after removing `GTDB:s__Escherichia_coli` from this strain's `taxonomy_mappings`, `source_attestations`, `xrefs`, and exact synonyms unless strain-specific GTDB evidence exists.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/escherichia_coli_pa47.yaml` after regeneration.
- Confirm that `Escherichia coli` is not emitted as a GTDB exact synonym on this narrower PA47 record.

## Additional Notes

- The pinned local NCBI, GTDB, Madin, ATB, and StrainInfo rows were the review source of truth; live upstream lookup was not used.
- `just validate-history` was skipped because this read-only review added no `history/` curation decision.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

