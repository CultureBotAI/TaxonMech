# YAML Record Review: Nocardiopsis sp. AE46

## Target

- Record: `data/taxa/bacteria/nocardiopsis_sp_ae46.yaml`
- Identifier: `NCBITaxon:1001645`
- Slug: `nocardiopsis_sp_ae46`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2649073` (`unclassified Nocardiopsis`)

## Validation

- `just validate data/taxa/bacteria/nocardiopsis_sp_ae46.yaml`: passed.
- `just validate-strict data/taxa/bacteria/nocardiopsis_sp_ae46.yaml data/taxa/bacteria/streptomyces_sp_ae41.yaml data/taxa/bacteria/aeromonas_sp_fars89d1.yaml data/taxa/bacteria/aeromonas_sp_fars89d2.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The record is an exact, seeded NCBI Taxonomy concept for `NCBITaxon:1001645` / `Nocardiopsis sp. AE46`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for an in-scope, direct NCBI seed record.
- `parent_taxon: NCBITaxon:2649073` matches the pinned NCBI parent, `unclassified Nocardiopsis`.
- The lineage stays within Bacteria through `Actinomycetota`, `Actinomycetes`, `Streptosporangiales`, `Nocardiopsidaceae`, `Nocardiopsis`, then the unclassified genus bin.

## Evidence

The lone `source_attestations` entry is internally consistent:

- `source: NCBITAXON`
- `source_id: NCBITaxon:1001645`
- `source_label: Nocardiopsis sp. AE46`
- `assertion_count: 1`
- `assertion_unit: NAME`

An exact `rg --no-ignore --hidden` search for `NCBITaxon:1001645` over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, and `data/straininfo` found the expected `PATHS.tsv`, `seed_scope.tsv`, and `data/raw/ncbitaxon_taxa.tsv` rows, and no extra ATB, BacDive, GTDB, GOLD, MADIN, or strain-info rows keyed to the reviewed identifier.

## Completeness

The record has no `strains`, `equivalent_identifiers`, `comments`, `synonyms`, `xrefs`, or product-level sections. That is consistent with an NCBI-only source footprint and `strain_count: 0`.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None urgent. Re-check only if a future source refresh adds ATB, BacDive, GTDB, GOLD, MADIN, or strain-info rows for `NCBITaxon:1001645`.

## Additional Notes

- The NCBI evidence comes from the pinned local `data/raw/ncbitaxon_taxa.tsv` snapshot rather than a live NCBI lookup.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `nocardiopsis_sp_ae46` review.
