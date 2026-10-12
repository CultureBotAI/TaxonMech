# YAML Record Review: Gaiella occulta

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/gaiella_occulta.yaml`
- Started UTC: 2026-09-22T16:11:10Z
- Finished UTC: 2026-09-22T16:12:08Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/gaiella_occulta.yaml`
- Identifier: `NCBITaxon:1002870`
- Slug: `gaiella_occulta`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1154586` (`Gaiella`)

## Validation

- `just validate data/taxa/bacteria/gaiella_occulta.yaml`: passed.
- `just validate-strict data/taxa/bacteria/tolypothrix_sp_lcrnk_3.yaml data/taxa/bacteria/tolypothrix_sp_lcrnk_5.yaml data/taxa/bacteria/tolypothrix_sp_lcrnk_8.yaml data/taxa/bacteria/gaiella_occulta.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002870` / `Gaiella occulta`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:1154586` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Bacillati`, `Actinomycetota`, `Thermoleophilia`, `Gaiellales`, `Gaiellaceae`, and `Gaiella`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.
- The LPSN row `lpsn:789667` names `Gaiella occulta`, marks it legitimate, validly published, and the correct name, links it to `NCBITaxon:1002870` and `GTDB:s__Gaiella_occulta`, and identifies `kgmicrobe.strain:LMG-26412` as type material.
- The GTDB mapping is a species-level `skos:closeMatch` for `GTDB:s__Gaiella_occulta` with `genome_count: 1`.

## Evidence

The reviewed source rows support the generated record:

- NCBI supports the exact taxon, the two related synonyms, and the type-material designations for F2-233, CECT 7815, and LMG 26412.
- LPSN supports the nomenclature entry, type strain, publication identifiers, and `INSDC:JF423906`.
- BacDive supports one strain, `kgmicrobe.strain:bacdive_168557` / `bacdive:168557`, with designation `F2-233`, culture collection IDs `CECT-7815` and `LMG-26412`, and the linked NCBI assembly, IMG genome, and BV-BRC genome.
- GOLD and StrainInfo related-record rows match the `LMG-26412` and `CECT-7815` aliases to the same BacDive strain.
- `source_attestations` match the inspected NCBI, LPSN, GTDB, BacDive, GOLD, and MADIN source rows and counts.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the maintained source rows listed above and no same-taxon ATB or MediaDive rows keyed to `NCBITaxon:1002870` / `Gaiella occulta`.

## Completeness

The record has no `comments`, `equivalent_identifiers`, or product-level sections. None are required by the reviewed local evidence. The available LPSN, GTDB, BacDive, GOLD, MADIN, culture-collection, and StrainInfo evidence is represented in the generated taxonomy, nomenclature, mapping, xref, source-attestation, and strain slots.

## Findings

No findings.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- `just validate-history` was not run because this read-only review did not add a `history/` decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `gaiella_occulta` review.
