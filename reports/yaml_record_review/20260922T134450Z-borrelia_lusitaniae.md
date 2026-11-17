# YAML Record Review: [Borrelia] lusitaniae

## Target

- Record: `data/taxa/bacteria/borrelia_lusitaniae.yaml`
- Identifier: `NCBITaxon:100177`
- Slug: `borrelia_lusitaniae`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:64895` (`Borreliella`)

## Validation

- `just validate data/taxa/bacteria/borrelia_lusitaniae.yaml`: passed.
- `just validate-strict data/taxa/bacteria/sulfurimonas_sp_scgc_aaa036_ap22.yaml data/taxa/bacteria/borrelia_lusitaniae.yaml data/taxa/bacteria/sulfurospirillum_sp_scgc_aaa036_p08.yaml data/taxa/bacteria/sulfurospirillum_sp_scgc_aaa036_n09.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:100177` / `[Borrelia] lusitaniae`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:64895` matches the pinned NCBI parent, `Borreliella`.
- The lineage stays within Bacteria through `Spirochaetota`, `Spirochaetia`, `Spirochaetales`, `Borreliaceae`, then `Borreliella`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The NCBI, BacDive, MediaDive, GOLD, MADIN, and GTDB attestations are keyed directly to `NCBITaxon:100177`; their labels and assertion counts match the reviewed raw rows. The GTDB `GTDB:s__Borreliella_lusitaniae` species cluster maps with `skos:closeMatch` and a 4-genome count.

The BacDive-derived type strain `bacdive:158095` preserves the `PotiB2` designation and the `CIP 105366` / `DSM 107168` culture collection identifiers. The two GOLD related records point to the same `gold:Go0621735` organism through different DSM 107168 fields, and the four StrainInfo related records preserve the expected CIP and DSM deposits and strain IDs for `NCBITaxon:100177`.

Exact `rg --no-ignore --hidden` searches over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI, BacDive, MediaDive, GOLD, MADIN, GTDB, culture-collection, StrainInfo, NCBI merged-ID, NCBI type-material, and strain-related rows keyed to `NCBITaxon:100177`, and no same-taxon ATB rows.

## Completeness

The NCBI-derived synonyms preserve `Borrelia genospecies PotiB2`, `Borrelia lusitaniae`, `Borreliella lusitaniae`, and both authority-bearing related synonyms. The GTDB xref and exact synonym agree with the Borreliella placement.

The record has no `equivalent_identifiers`, `comments`, or product-level sections. The missing LPSN nomenclature block described below is the only questionable omission in the reviewed local evidence.

## Findings

### Major: Indirect LPSN nomenclature evidence is omitted

The direct BacDive row for `kgmicrobe.strain:bacdive_158095` is keyed to `NCBITaxon:100177` and cites `lpsn:783530`; `data/raw/lpsn_names.tsv` contains that same LPSN name with the expected `Borrelia lusitaniae` species label, Le Fleche et al. 1997 authority, valid-publication flags, `CIP 105366` / `DSM 107168` type-strain designations, publications, and `INSDC:X98228` accession. Because the LPSN row itself does not carry `NCBITaxon:100177`, the generated record drops `lpsn:783530` from `nomenclature`, `xrefs`, and `source_attestations`, even though the BacDive-to-LPSN edge locally ties the same type strain back to this species.

## Recommended Edits

- Teach LPSN ingestion to accept high-confidence BacDive-mediated LPSN links when the BacDive row is already keyed to the current NCBI taxon and the LPSN row shares the same type-strain identifiers.
- Add the `lpsn:783530` nomenclature block, xref, and LPSN source attestation to `NCBITaxon:100177` after the indirect LPSN crosswalk is represented explicitly.
- Add a regression check for BacDive rows whose `lpsn_ids` point to otherwise unlinked LPSN names with matching type-strain designations.

## Follow-up Checks

- Re-check other BacDive-backed species whose `data/raw/lpsn_names.tsv` row has an empty NCBI column after the LPSN crosswalk is expanded.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `borrelia_lusitaniae` review.
