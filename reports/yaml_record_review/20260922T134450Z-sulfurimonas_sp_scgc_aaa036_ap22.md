# YAML Record Review: Sulfurimonas sp. SCGC AAA036-AP22

## Target

- Record: `data/taxa/bacteria/sulfurimonas_sp_scgc_aaa036_ap22.yaml`
- Identifier: `NCBITaxon:1001768`
- Slug: `sulfurimonas_sp_scgc_aaa036_ap22`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2623549` (`unclassified Sulfurimonas`)

## Validation

- `just validate data/taxa/bacteria/sulfurimonas_sp_scgc_aaa036_ap22.yaml`: passed.
- `just validate-strict data/taxa/bacteria/sulfurimonas_sp_scgc_aaa036_ap22.yaml data/taxa/bacteria/borrelia_lusitaniae.yaml data/taxa/bacteria/sulfurospirillum_sp_scgc_aaa036_p08.yaml data/taxa/bacteria/sulfurospirillum_sp_scgc_aaa036_n09.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1001768` / `Sulfurimonas sp. SCGC AAA036-AP22`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:2623549` matches the pinned NCBI parent, `unclassified Sulfurimonas`.
- The lineage stays within Bacteria through `Campylobacterota`, `Epsilonproteobacteria`, `Campylobacterales`, `Sulfurimonadaceae`, `Sulfurimonas`, then `unclassified Sulfurimonas`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The NCBI and GOLD attestations are keyed directly to `NCBITaxon:1001768`; their labels and assertion counts match the reviewed raw rows.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI and GOLD rows keyed to `NCBITaxon:1001768`, and no ATB, BacDive, GTDB, LPSN, MADIN, or strain-info rows keyed to this identifier.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `sulfurimonas_sp_scgc_aaa036_ap22` review.
