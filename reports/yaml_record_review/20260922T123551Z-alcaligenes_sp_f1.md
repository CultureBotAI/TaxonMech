# YAML Record Review: Alcaligenes sp. F1

## Target

- Record: `data/taxa/bacteria/alcaligenes_sp_f1.yaml`
- Identifier: `NCBITaxon:1001544`
- Slug: `alcaligenes_sp_f1`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:259357` (`unclassified Alcaligenes`)

## Validation

- `just validate data/taxa/bacteria/alcaligenes_sp_f1.yaml`: passed.
- `just validate-strict data/taxa/bacteria/francisella_tularensis_subsp_tularensis_tigb03.yaml data/taxa/bacteria/alcaligenes_sp_f1.yaml data/taxa/bacteria/pseudomonas_sp_cm1_a2.yaml data/taxa/bacteria/pseudomonas_sp_v6.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The record is an exact, seeded NCBI Taxonomy concept for `NCBITaxon:1001544` / `Alcaligenes sp. F1`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for an in-scope, direct NCBI seed record.
- `parent_taxon: NCBITaxon:259357` matches the pinned NCBI parent, `unclassified Alcaligenes`.
- The lineage stays within Bacteria through `Pseudomonadota`, `Betaproteobacteria`, `Burkholderiales`, `Alcaligenaceae`, `Alcaligenes`, then the unclassified genus bin.

## Evidence

The lone `source_attestations` entry is internally consistent:

- `source: NCBITAXON`
- `source_id: NCBITaxon:1001544`
- `source_label: Alcaligenes sp. F1`
- `assertion_count: 1`
- `assertion_unit: NAME`

An exact `rg --no-ignore --hidden` search for `NCBITaxon:1001544` over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, and `data/straininfo` found the expected `PATHS.tsv`, `seed_scope.tsv`, and `data/raw/ncbitaxon_taxa.tsv` rows, and no extra ATB, BacDive, GTDB, GOLD, MADIN, or strain-info rows keyed to the reviewed identifier.

## Completeness

The record has no `strains`, `equivalent_identifiers`, `comments`, `synonyms`, `xrefs`, or product-level sections. That is consistent with an NCBI-only source footprint and `strain_count: 0`.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None urgent. Re-check only if a future source refresh adds ATB, BacDive, GTDB, GOLD, MADIN, or strain-info rows for `NCBITaxon:1001544`.

## Additional Notes

- The NCBI evidence comes from the pinned local `data/raw/ncbitaxon_taxa.tsv` snapshot rather than a live NCBI lookup.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `alcaligenes_sp_f1` review.
