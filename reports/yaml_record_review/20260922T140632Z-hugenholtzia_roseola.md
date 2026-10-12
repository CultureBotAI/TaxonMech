# YAML Record Review: Hugenholtzia roseola

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/hugenholtzia_roseola.yaml`
- Started UTC: 2026-09-22T14:04:58Z
- Finished UTC: 2026-09-22T14:06:32Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/hugenholtzia_roseola.yaml`
- Identifier: `NCBITaxon:1002`
- Slug: `hugenholtzia_roseola`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1937999` (`Hugenholtzia`)

## Validation

- `just validate data/taxa/bacteria/hugenholtzia_roseola.yaml`: passed.
- `just validate-strict data/taxa/bacteria/hugenholtzia_roseola.yaml data/taxa/bacteria/alcaligenes_sp_cob4.yaml data/taxa/bacteria/bacillus_sp_cob.yaml data/taxa/bacteria/chromobacterium_sp_cob6.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002` / `Hugenholtzia roseola`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:1937999` matches the pinned NCBI parent, `Hugenholtzia`.
- The lineage stays within Bacteria through `Bacteroidota`, `Cytophagia`, `Cytophagales`, `Bernardetiaceae`, then `Hugenholtzia`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The NCBI, LPSN, BacDive, GOLD, MADIN, StrainInfo, and strain-overlay rows are internally consistent for the reviewed record.

- `lpsn:795344` maps to `NCBITaxon:1002`, preserves the correct name `Hugenholtzia roseola`, the authority `(Lewin 1969) Hahnke et al. 2017`, valid-publication and legitimacy flags, the type-strain designations, the publications, `INSDC:AB078063`, and the LPSN-provided `GTDB:s__Hugenholtzia_roseola` xref.
- `kgmicrobe.strain:bacdive_3792` / `CR-155` is classified as descendant strain `NCBITaxon:1121903` and is marked as the type strain through the LPSN type-strain culture-collection identifiers.
- `kgmicrobe.strain:bacdive_136522` / `CR-141` carries same-species GOLD and StrainInfo related records for `ATCC 23087`, `CIP 106407`, `LMG 13167`, and `NCIMB 1370`.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected direct NCBI, LPSN, BacDive, GOLD, and MADIN rows keyed to `NCBITaxon:1002`, StrainInfo and GOLD related records for both BacDive strains, and no ATB rows keyed to this identifier.

## Completeness

`strain_count: 2` matches the two BacDive strains keyed to the species in `data/raw/bacdive_strains.tsv`, and the listed type strain matches the LPSN type-strain designations through the shared culture-collection identifiers. The record correctly omits a direct `taxonomy_mappings` section because the inspected rows did not include a same-taxon `data/raw/gtdb_mappings.tsv` row for `NCBITaxon:1002`.

The record has no `equivalent_identifiers`, `comments`, or product-level sections. None are required by the reviewed local evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `hugenholtzia_roseola` review.
