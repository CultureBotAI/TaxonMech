# YAML Record Review: Pectinatus sottacetonis

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/pectinatus_sottacetonis.yaml`
- Started UTC: 2026-09-22T15:48:04Z
- Finished UTC: 2026-09-22T15:49:06Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/pectinatus_sottacetonis.yaml`
- Identifier: `NCBITaxon:1002795`
- Slug: `pectinatus_sottacetonis`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:864` (`Pectinatus`)

## Validation

- `just validate data/taxa/bacteria/pectinatus_sottacetonis.yaml`: passed.
- `just validate-strict data/taxa/eukaryota/uncultured_eukaryote.yaml data/taxa/bacteria/novosphingobium_sp_hme6881.yaml data/taxa/bacteria/pectinatus_sottacetonis.yaml data/taxa/bacteria/helicobacter_bizzozeronii_ciii_1.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002795` / `Pectinatus sottacetonis`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:864` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Bacillati`, `Bacillota`, `Negativicutes`, `Selenomonadales`, `Selenomonadaceae`, then `Pectinatus`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The exact same-taxon source rows cover the six source families named in `source_attestations`: NCBI, LPSN, GTDB, BacDive, GOLD, and MADIN.

- The NCBI row supplies two related synonyms and type-material rows for the `ATCC BAA-2501`, `VTT E-113163`, and `FSRU B0405` designations; the related synonyms and type-strain flag on `kgmicrobe.strain:bacdive_133950` are present in the YAML.
- The LPSN row for `lpsn:791186` is a correct species name, links `NCBITaxon:1002795` to `GTDB:s__Pectinatus_sottacetonis`, designates `kgmicrobe.strain:ATCC-BAA-2501`, and supplies the two DOIs, one PMID, and `INSDC:JF280084`; the `nomenclature` entry carries those values.
- The GTDB row maps `GTDB:s__Pectinatus_sottacetonis` to this taxon with `skos:closeMatch` and 1 genome, matching the YAML `taxonomy_mappings`, GTDB xref, and GTDB source attestation.
- The BacDive row supplies one strain, matching `strain_count: 1`; the BacDive, BV-BRC, and GOLD assembly, genome, and related records are represented under that strain.
- The GOLD and MADIN rows report assertion counts of 1 organism and 21 trait assertions, matching the corresponding `source_attestations`.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected same-taxon rows and no ATB, MediaDive, BactoTraits, or strain-info rows keyed to `NCBITaxon:1002795`.

## Completeness

The record carries the expected LPSN `nomenclature`, GTDB `taxonomy_mappings`, NCBI `synonyms`, GTDB and LPSN `xrefs`, BacDive `strains`, and source attestations for all six local source families. There are no `comments` or product-level sections. None are required by the reviewed local evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `pectinatus_sottacetonis` review.
