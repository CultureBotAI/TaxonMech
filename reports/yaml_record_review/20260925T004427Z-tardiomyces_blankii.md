# YAML Record Review: Tardiomyces blankii

- Verdict: pass
- Target: `data/taxa/eukaryota/tardiomyces_blankii.yaml`
- Identifier: `NCBITaxon:45524`

## Target
- Reviewed the complete 83-line YAML record for Tardiomyces blankii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tardiomyces_blankii.

## Validation
- `just validate data/taxa/eukaryota/tardiomyces_blankii.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tardiomyces_blankii.yaml data/taxa/eukaryota/tardiomyces_digboiensis.yaml data/taxa/eukaryota/tausonia_pullulans.yaml data/taxa/eukaryota/teichospora_sp.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:45524` at `data/raw/ncbitaxon_taxa.tsv:5589`, label `Tardiomyces blankii`, rank `SPECIES`, parent `NCBITaxon:3712562`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 52635.
- NCBI supplied 1 exact synonym, 0 broad synonyms, and 3 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 13 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 36034 matched the YAML source attestation with organism_count 1 for `NCBITaxon:45524`.
- Native GOLD tables contained 1 organism row, 1 project row, and 0 analysis rows for this target.
- Local NCBI type material had 29 exact rows for this target, spanning culture-from-holotype and holotype rows from `typematerial.dmp`.
- StrainInfo contained 13 direct records and 40 exact deposit rows for this taxon. BacDive had 0 exact local rows.

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
