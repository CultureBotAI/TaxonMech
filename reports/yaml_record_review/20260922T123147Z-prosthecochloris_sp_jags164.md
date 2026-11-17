# YAML Record Review: Prosthecochloris sp. JAGS164

## Target

- Record: `data/taxa/bacteria/prosthecochloris_sp_jags164.yaml`
- Identifier: `NCBITaxon:1001379`
- Slug: `prosthecochloris_sp_jags164`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2632826` (`unclassified Prosthecochloris`)

## Validation

- `just validate data/taxa/bacteria/prosthecochloris_sp_jags164.yaml`: passed.
- `just validate-strict data/taxa/bacteria/chlorobaculum_sp_jags162.yaml data/taxa/bacteria/chlorobaculum_sp_jags163.yaml data/taxa/bacteria/prosthecochloris_sp_jags164.yaml data/taxa/bacteria/pseudomonas_sp_fg_2.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The record is an exact, seeded NCBI Taxonomy concept for `NCBITaxon:1001379` / `Prosthecochloris sp. JAGS164`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for an in-scope, direct NCBI seed record.
- `parent_taxon: NCBITaxon:2632826` matches the pinned NCBI parent, `unclassified Prosthecochloris`.
- The lineage stays within Bacteria through `Chlorobiota`, `Chlorobiia`, `Chlorobiales`, `Chlorobiaceae`, `Prosthecochloris`, then the unclassified genus bin.

## Evidence

The lone `source_attestations` entry is internally consistent:

- `source: NCBITAXON`
- `source_id: NCBITaxon:1001379`
- `source_label: Prosthecochloris sp. JAGS164`
- `assertion_count: 1`
- `assertion_unit: NAME`

An exact `rg --no-ignore --hidden` search for `NCBITaxon:1001379` over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, and `data/straininfo` found the expected `PATHS.tsv`, `seed_scope.tsv`, and `data/raw/ncbitaxon_taxa.tsv` rows, and no extra ATB, BacDive, or strain-info rows keyed to the reviewed identifier.

## Completeness

The record has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections. That is consistent with an NCBI-only source footprint and `strain_count: 0`.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None urgent. Re-check only if a future source refresh adds ATB, BacDive, or strain-info rows for `NCBITaxon:1001379`.

## Additional Notes

- The NCBI evidence comes from the pinned local `data/raw/ncbitaxon_taxa.tsv` snapshot rather than a live NCBI lookup.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `prosthecochloris_sp_jags164` review.
