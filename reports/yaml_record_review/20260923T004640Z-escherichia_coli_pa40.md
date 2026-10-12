# YAML Record Review: Escherichia coli PA40
- Repository: TaxonMech
- Record: data/taxa/bacteria/escherichia_coli_pa40.yaml
- Started UTC: 2026-09-23T00:46:40Z
- Finished UTC: 2026-09-23T00:46:40Z
- Verdict: needs curation

## Target

- YAML record: `data/taxa/bacteria/escherichia_coli_pa40.yaml`
- Identifier: `NCBITaxon:1005508`
- Label: `Escherichia coli PA40`
- Rank: `STRAIN`
- Parent: `NCBITaxon:562`
- Registry row: `data/taxa/PATHS.tsv:1742`
- Scope row: `curation/seed_scope.tsv:35991`
- A pre-write `find reports/yaml_record_review ... -name '*-escherichia_coli_pa40.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/escherichia_coli_pa39.yaml data/taxa/bacteria/escherichia_coli_pa40.yaml data/taxa/bacteria/escherichia_coli_pa41.yaml data/taxa/bacteria/escherichia_coli_pa42.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/escherichia_coli_pa40.yaml` passed with no LinkML issues.

## Identity and Grounding

- The YAML identifier, label, `STRAIN` rank, `BACTERIA` domain, parent `NCBITaxon:562`, and genetic code `11` match `data/raw/ncbitaxon_taxa.tsv:210404`.
- The lineage is internally coherent and ends at the asserted parent species `Escherichia coli`.
- `grounding_status: EXACT` is appropriate for the NCBI strain taxon itself.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210404` attests `NCBITaxon:1005508` as strain `Escherichia coli PA40`, parent `NCBITaxon:562`, genetic code `11`, and NCBI snapshot `2026-09-13`.
- `data/raw/madin_taxa.tsv:276` contributes one Madin trait assertion for `NCBITaxon:1005508`.
- `data/raw/gtdb_mappings.tsv:948` maps `GTDB:s__Escherichia_coli` to `NCBITaxon:1005508` with `skos:closeMatch` and genome count `36408`.
- `data/raw/gtdb_species.tsv:59219` confirms that `GTDB:s__Escherichia_coli` is the GTDB `s__Escherichia_coli` species cluster, not a PA40 strain identifier.
- An exact `rg --no-ignore --hidden` scan over `data/atb` and `data/straininfo` for the NCBI ID, label, and slug found no same-taxon auxiliary rows.

## Completeness

- The record contains all generated sections expected from the NCBI, GTDB, and Madin seed inputs.
- The generated GTDB mapping, xref, and exact synonym make the record too broad by projecting a species-cluster assertion onto a narrower strain node.

## Findings

- **Major:** `GTDB:s__Escherichia_coli` represents the GTDB species cluster `s__Escherichia_coli`, but this record attaches it to NCBI strain `Escherichia coli PA40` as a close match, xref, GTDB genome attestation, and exact synonym text `Escherichia coli`. A species cluster should not be modeled as an equivalent identifier or exact synonym for a single strain.

## Recommended Edits

- Fix the GTDB mapping generation and `src/taxonmech/seed.py` projection path so a species-cluster row in `data/raw/gtdb_mappings.tsv` does not emit strain-level `taxonomy_mappings`, `xrefs`, `source_attestations`, or `EXACT_SYNONYM` entries.
- Regenerate `data/taxa/bacteria/escherichia_coli_pa40.yaml` after that upstream fix.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/escherichia_coli_pa40.yaml` after regeneration.
- Verify that no regenerated synonym equates `Escherichia coli PA40` with species-level text `Escherichia coli`.

## Additional Notes

- Live taxonomy lookups were unavailable earlier in this review stream; pinned rows in `data/raw/`, `data/atb/`, and `data/straininfo/` were the source of truth.
- `just validate-history` was not needed for this read-only report because no `history/` file was added.
- `just validate-products` was not applicable because there are no `causal_graphs`.

