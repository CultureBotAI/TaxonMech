# YAML Record Review: Thioreductor sp. SCGC AAA036-M21

## Target

- Record: `data/taxa/bacteria/thioreductor_sp_scgc_aaa036_m21.yaml`
- Identifier: `NCBITaxon:1001766`
- Slug: `thioreductor_sp_scgc_aaa036_m21`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2625334` (`unclassified Thioreductor`)

## Validation

- `just validate data/taxa/bacteria/thioreductor_sp_scgc_aaa036_m21.yaml`: passed.
- `just validate-strict data/taxa/bacteria/sulfurovum_sp_scgc_aaa036_o23.yaml data/taxa/bacteria/thioreductor_sp_scgc_aaa036_k21.yaml data/taxa/bacteria/thioreductor_sp_scgc_aaa036_m21.yaml data/taxa/bacteria/sulfurimonas_sp_scgc_aaa036_a04.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1001766` / `Thioreductor sp. SCGC AAA036-M21`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:2625334` matches the pinned NCBI parent, `unclassified Thioreductor`.
- The lineage stays within Bacteria through `Campylobacterota`, `Campylobacterota incertae sedis`, `Thioreductoraceae`, `Thioreductor`, then `unclassified Thioreductor`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1001766`; its label and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row keyed to `NCBITaxon:1001766`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, or strain-info rows keyed to this identifier.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `thioreductor_sp_scgc_aaa036_m21` review.
