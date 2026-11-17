# YAML Record Review: Arcobacter sp. SCGC AAA036-D18

## Target

- Record: `data/taxa/bacteria/arcobacter_sp_scgc_aaa036_d18.yaml`
- Identifier: `NCBITaxon:1001760`
- Slug: `arcobacter_sp_scgc_aaa036_d18`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2593671` (`unclassified Arcobacter`)

## Validation

- `just validate data/taxa/bacteria/arcobacter_sp_scgc_aaa036_d18.yaml`: passed.
- `just validate-strict data/taxa/bacteria/arcobacter_sp_scgc_aaa036_d18.yaml data/taxa/bacteria/arcobacter_sp_scgc_aaa036_f23.yaml data/taxa/bacteria/sulfurovum_sp_scgc_aaa036_b05.yaml data/taxa/bacteria/sulfurovum_sp_scgc_aaa036_g05.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1001760` / `Arcobacter sp. SCGC AAA036-D18`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:2593671` matches the pinned NCBI parent, `unclassified Arcobacter`.
- The lineage stays within Bacteria through `Campylobacterota`, `Epsilonproteobacteria`, `Campylobacterales`, `Arcobacteraceae`, `Arcobacter`, then `unclassified Arcobacter`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The NCBI and GOLD attestations are keyed directly to `NCBITaxon:1001760`; their labels and assertion counts match the reviewed raw rows.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI and GOLD rows keyed to `NCBITaxon:1001760`, and no ATB, BacDive, GTDB, LPSN, MADIN, or strain-info rows keyed to this identifier.

## Completeness

The record has no `taxonomy_mappings`, `synonyms`, `xrefs`, `strains`, `equivalent_identifiers`, `comments`, or product-level sections. None are required by the reviewed local evidence.

## Findings

No findings.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `arcobacter_sp_scgc_aaa036_d18` review.
