# YAML Record Review: Sungouiella tsuchiyae

- Verdict: pass
- Target: `data/taxa/eukaryota/sungouiella_tsuchiyae.yaml`
- Identifier: `NCBITaxon:46168`

## Target
- Reviewed the complete 79-line YAML record for Sungouiella tsuchiyae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for sungouiella_tsuchiyae.

## Validation
- `just validate data/taxa/eukaryota/sungouiella_tsuchiyae.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/sungouiella_thailandica.yaml data/taxa/eukaryota/sungouiella_tsuchiyae.yaml data/taxa/eukaryota/sungouiozyma_ichnusensis.yaml data/taxa/eukaryota/sungouiozyma_intestinalis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:46168` at `data/raw/ncbitaxon_taxa.tsv:5784`, label `Sungouiella tsuchiyae`, rank `SPECIES`, parent `NCBITaxon:3315605`, genetic code `12`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 52700.
- NCBI supplied 1 exact synonym, 0 broad synonyms, and 2 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 13 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 36230 matched the YAML source attestation with organism_count 1 for `NCBITaxon:46168`.
- Native GOLD tables contained 1 organism row and 1 project row, with 0 analysis rows, for this target.
- `data/raw/ncbi_type_material.tsv` contained 14 exact NCBI-prefixed type-material rows for the target.
- StrainInfo contained 2 direct records and 14 exact deposit rows for this taxon; the parsed non-direct deposit lookup returned no additional rows. BacDive had 0 exact local rows.

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
- No seeded YAML edits are needed; the record is consistent with all checked local NCBI, GOLD, type-material, BacDive, and StrainInfo evidence.
