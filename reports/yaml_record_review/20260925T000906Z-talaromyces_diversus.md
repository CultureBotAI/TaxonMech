# YAML Record Review: Talaromyces diversus

- Verdict: pass
- Target: `data/taxa/eukaryota/talaromyces_diversus.yaml`
- Identifier: `NCBITaxon:128434`

## Target
- Reviewed the complete 87-line YAML record for Talaromyces diversus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for talaromyces_diversus.

## Validation
- `just validate data/taxa/eukaryota/talaromyces_diversus.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/talaromyces_bacillisporus.yaml data/taxa/eukaryota/talaromyces_diversus.yaml data/taxa/eukaryota/talaromyces_funiculosus.yaml data/taxa/eukaryota/talaromyces_helicus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:128434` at `data/raw/ncbitaxon_taxa.tsv:24597`, label `Talaromyces diversus`, rank `SPECIES`, parent `NCBITaxon:2752540`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 53914.
- NCBI supplied 1 exact synonym, 0 broad synonyms, and 2 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 16 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 6601 matched the YAML source attestation with organism_count 9 for `NCBITaxon:128434`.
- Native GOLD tables contained 9 organism rows, 0 project rows, and 0 analysis rows for this target.
- Local NCBI type material had 10 exact rows for this target, spanning culture-from-holotype and culture-from-neotype rows from `typematerial.dmp`.
- StrainInfo contained 20 direct records and 38 exact deposit rows for this taxon. BacDive had 0 exact local rows.

## Completeness
- Generated raw strain tables had 0 exact target rows in BacDive strains, culture collection strains, strain assemblies, strain genome records, and strain-related records.
- Auxiliary sources had 0 exact target rows in BactoTraits, GTDB mappings, GTDB species, LPSN, MADIN, and MediaDive.
- Generated StrainInfo overlay tables had 0 exact target rows in assemblies, exclusions, and related_records.

## Findings
- No findings.

## Recommended Edits
- No edits are recommended.

## Follow-up Checks
- No follow-up checks are required.

## Additional Notes
- No seeded YAML edits are needed; the record is consistent with all checked local NCBI, GOLD, BacDive, and StrainInfo evidence.
