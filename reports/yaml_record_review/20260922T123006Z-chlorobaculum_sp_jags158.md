# YAML Record Review: Chlorobaculum sp. JAGS158

## Target

- Record: `data/taxa/bacteria/chlorobaculum_sp_jags158.yaml`
- Identifier: `NCBITaxon:1001373`
- Slug: `chlorobaculum_sp_jags158`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2685250` (`unclassified Chlorobaculum`)

## Validation

- `just validate data/taxa/bacteria/chlorobaculum_sp_jags158.yaml`: passed.
- `just validate-strict data/taxa/bacteria/chlorobaculum_sp_jags158.yaml data/taxa/bacteria/chlorobaculum_sp_jags159.yaml data/taxa/bacteria/prosthecochloris_sp_jags160.yaml data/taxa/bacteria/prosthecochloris_sp_jags161.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The record is an exact, seeded NCBI Taxonomy concept for `NCBITaxon:1001373` / `Chlorobaculum sp. JAGS158`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for an in-scope, direct NCBI seed record.
- `parent_taxon: NCBITaxon:2685250` matches the pinned NCBI parent, `unclassified Chlorobaculum`.
- The lineage stays within Bacteria through `Chlorobiota`, `Chlorobiia`, `Chlorobiales`, `Chlorobiaceae`, `Chlorobaculum`, then the unclassified genus bin.

## Evidence

The lone `source_attestations` entry is internally consistent:

- `source: NCBITAXON`
- `source_id: NCBITaxon:1001373`
- `source_label: Chlorobaculum sp. JAGS158`
- `assertion_count: 1`
- `assertion_unit: NAME`

An exact `rg --no-ignore --hidden` search for `NCBITaxon:1001373` over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, and `data/straininfo` found the expected `PATHS.tsv`, `seed_scope.tsv`, and `data/raw/ncbitaxon_taxa.tsv` rows, and no extra ATB, BacDive, or strain-info rows keyed to the reviewed identifier.

## Completeness

The record has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections. That is consistent with an NCBI-only source footprint and `strain_count: 0`.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None urgent. Re-check only if a future source refresh adds ATB, BacDive, or strain-info rows for `NCBITaxon:1001373`.

## Additional Notes

- The NCBI evidence comes from the pinned local `data/raw/ncbitaxon_taxa.tsv` snapshot rather than a live NCBI lookup.
- Before this report was written, exact `find reports/yaml_record_review -maxdepth 1 ...` checks over ignored report files found no prior `chlorobaculum_sp_jags158` review.
