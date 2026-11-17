# YAML Record Review: Papillibacter cinnamivorans

## Target

- Record: `data/taxa/bacteria/papillibacter_cinnamivorans.yaml`
- Identifier: `NCBITaxon:100176`
- Slug: `papillibacter_cinnamivorans`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:100175` (`Papillibacter`)

## Validation

- `just validate data/taxa/bacteria/papillibacter_cinnamivorans.yaml`: passed.
- `just validate-strict data/taxa/bacteria/streptococcus_pneumoniae_07ar0125.yaml data/taxa/bacteria/streptococcus_pneumoniae_br1064.yaml data/taxa/bacteria/streptococcus_pneumoniae_nd6012.yaml data/taxa/bacteria/papillibacter_cinnamivorans.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:100176` / `Papillibacter cinnamivorans`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:100175` matches the pinned NCBI parent, `Papillibacter`.
- The lineage stays within Bacteria through `Bacillota`, `Clostridia`, `Eubacteriales`, `Oscillospiraceae`, then `Papillibacter`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The NCBI and LPSN entries are keyed directly to `NCBITaxon:100176`. The `lpsn:779146` row preserves the expected species name, authority, valid-publication flags, type-strain designations for `ATCC 700879` and `DSM 12816`, publications, and `INSDC:AF167711` sequence accession.

The one BacDive-derived strain `bacdive:17681` is filed under the descendant NCBI strain `NCBITaxon:1122930` / `Papillibacter cinnamivorans DSM 12816`; the valid DSM 12816-linked assembly, genome, BioSample, BioProject, GOLD, GTDB, NCBI Assembly, StrainInfo, and AllTheBacteria rows in the YAML match the reviewed raw rows.

Exact `rg --no-ignore --hidden` searches over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected direct NCBI and LPSN rows keyed to `NCBITaxon:100176`, expected BacDive and assembly-overlay rows for descendant `NCBITaxon:1122930`, and cross-taxon GOLD and StrainInfo rows keyed to `NCBITaxon:82541` through the shared `ATCC 700879` culture-collection identifier.

## Completeness

`strain_count: 1` matches the single BacDive-derived strain under the descendant strain taxon, and the LPSN type-strain identifiers are preserved as `kgmicrobe.strain:ATCC-700879` and `kgmicrobe.strain:DSM-12816`.

The record has no `equivalent_identifiers`, `comments`, or product-level sections. The only questionable related records are the cross-taxon `ATCC 700879` matches described below.

## Findings

### Major: Cross-taxon ATCC 700879 evidence is projected into the Papillibacter type strain

The `kgmicrobe.strain:bacdive_17681` strain is classified as descendant `NCBITaxon:1122930` (`Papillibacter cinnamivorans DSM 12816`), but four of its related records point at `NCBITaxon:82541`, a different species, `Cupriavidus gilardii`. Two of those records are `gold:Go0260178` / `Cupriavidus gilardii ATCC 700879`, and two are StrainInfo records for the `ATCC 700879` deposit. They appear to have been pulled into this `Papillibacter` strain through the `kgmicrobe.strain:ATCC-700879` culture-collection alias without requiring the source record's taxon to match the BacDive strain taxon or a descendant of this reviewed species.

## Recommended Edits

- Suppress related records for `bacdive:17681` when the source taxon is neither `NCBITaxon:1122930` nor a compatible descendant of `NCBITaxon:100176`.
- Drop the two `gold:Go0260178` `GOLD_ORGANISM` entries and the two `NCBITaxon:82541` StrainInfo entries that are currently matched through `kgmicrobe.strain:ATCC-700879`.
- Add a regression check that culture-collection identifier joins cannot import GOLD or StrainInfo records whose `taxon_id` belongs to an unrelated species.

## Follow-up Checks

- Re-check other type strains with ATCC aliases for cross-taxon related records after the culture-collection join is tightened.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `papillibacter_cinnamivorans` review.
