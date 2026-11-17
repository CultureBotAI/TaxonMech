# YAML Record Review: Clostridium peptidivorans

## Target

- Record: `data/taxa/bacteria/clostridium_peptidivorans.yaml`
- Identifier: `NCBITaxon:100174`
- Slug: `clostridium_peptidivorans`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1485` (`Clostridium`)

## Validation

- `just validate data/taxa/bacteria/clostridium_peptidivorans.yaml`: passed.
- `just validate-strict data/taxa/bacteria/clostridium_peptidivorans.yaml data/taxa/bacteria/mycobacteroides_abscessus_6g_0125_r.yaml data/taxa/bacteria/mycobacteroides_abscessus_6g_0125_s.yaml data/taxa/bacteria/streptococcus_pneumoniae_pt8114.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:100174` / `Clostridium peptidivorans`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:1485` matches the pinned NCBI parent, `Clostridium`.
- The lineage stays within Bacteria through `Bacillota`, `Clostridia`, `Eubacteriales`, `Clostridiaceae`, then `Clostridium`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The NCBI, MADIN, GOLD, and BacDive rows are keyed directly to `NCBITaxon:100174`; the LPSN row `lpsn:774949` also points to `NCBITaxon:100174` and preserves the expected species name, authority, valid-publication flags, type-strain designation, publications, and `INSDC:AF156796` sequence accession. The one-genome GTDB `GTDB:s__Clostridium_AK_peptidivorans` mapping is a species-level `skos:closeMatch` to this species and is attached at the correct rank.

The BacDive-derived strain `bacdive:2801` carries the expected `kgmicrobe.strain:DSM-12505` and `kgmicrobe.strain:TMC%204` culture collection identifiers. Its related records preserve the GOLD organism `gold:Go0028489`, StrainInfo strain `straininfo.strain:49308`, deposit `straininfo.deposit:163228`, and the `INSDC:AF156796` sequence record matched through the DSM 12505 deposit.

Exact `rg --no-ignore --hidden` searches over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected rows keyed to `NCBITaxon:100174` in the NCBI, MADIN, GOLD, BacDive, culture-collection, GTDB, LPSN, strain-related, and NCBI type-material raw tables; the exact `data/atb` scan found no same-taxon ATB rows.

## Completeness

The record preserves the NCBI nomenclatural authority as a related synonym and keeps the GTDB species label as a GTDB-derived exact synonym. `strain_count: 1` matches the one BacDive-derived local strain, and the StrainInfo overlay under that strain is consistent with the DSM 12505 BacDive link.

The record has no `equivalent_identifiers`, `comments`, or product-level sections. None are required by the reviewed local evidence.

## Findings

No findings.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- The review used pinned local `data/raw/*.tsv` and `data/straininfo/*.tsv` snapshots rather than live source lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `clostridium_peptidivorans` review.
