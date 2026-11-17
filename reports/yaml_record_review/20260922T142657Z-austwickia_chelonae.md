# YAML Record Review: Austwickia chelonae

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/austwickia_chelonae.yaml`
- Started UTC: 2026-09-22T14:25:04Z
- Finished UTC: 2026-09-22T14:26:57Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/austwickia_chelonae.yaml`
- Identifier: `NCBITaxon:100225`
- Slug: `austwickia_chelonae`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1184606` (`Austwickia`)

## Validation

- `just validate data/taxa/bacteria/austwickia_chelonae.yaml`: passed.
- `just validate-strict data/taxa/bacteria/serratia_sp_pt19.yaml data/taxa/bacteria/austwickia_chelonae.yaml data/taxa/bacteria/streptomyces_coelicolor_a3_2.yaml data/taxa/bacteria/bradyrhizobium_sp_pe2_6.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:100225` / `Austwickia chelonae`.

- `identifier`, `label`, `rank`, and `parent_taxon: NCBITaxon:1184606` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Actinomycetota`, `Actinomycetes`, `Micrococcales`, `Dermatophilaceae`, then `Austwickia`.
- The LPSN entry, two GTDB broad-match mappings, `Dermatophilus chelonae` synonyms from NCBI and LPSN, and xrefs are represented.
- The BacDive type strain `bacdive:3942` is filed under descendant strain `NCBITaxon:1184607` and is preserved with `classified_as: NCBITaxon:1184607`.
- `grounding_status: EXACT` is correct for the species seed.

## Evidence

The exact `rg --no-ignore --hidden` scan over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI, LPSN, GTDB, GOLD, and MADIN rows keyed to `NCBITaxon:100225`, and a follow-up gitignore-independent scan over `bacdive:3942`, `kgmicrobe.strain:bacdive_3942`, and `NCBITaxon:1184607` found the expected descendant BacDive and NBRC 105200 rows.

The reviewed YAML carries the LPSN type strain designations, all six BacDive culture collection IDs, NBRC 105200 and DSM 44178 assembly/genome rows, GOLD organism/project evidence for ATCC, CCUG, CIP, DSM, JCM, and NBRC collection deposits, 16S sequence related records, and StrainInfo deposit records for the type-strain aliases.

## Completeness

The record includes the expected nomenclature, GTDB mappings, synonyms, xrefs, type-strain entry, assembly/genome links, related records, StrainInfo evidence, and direct plus descendant source attestations present in the pinned local evidence. No missing same-taxon evidence was found.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `austwickia_chelonae` review.
