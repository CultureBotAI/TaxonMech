# YAML Record Review: Teichospora sp.

- Verdict: pass
- Target: `data/taxa/eukaryota/teichospora_sp.yaml`
- Identifier: `NCBITaxon:2107984`

## Target
- Reviewed the complete 87-line YAML record for Teichospora sp. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for teichospora_sp.

## Validation
- `just validate data/taxa/eukaryota/teichospora_sp.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tardiomyces_blankii.yaml data/taxa/eukaryota/tardiomyces_digboiensis.yaml data/taxa/eukaryota/tausonia_pullulans.yaml data/taxa/eukaryota/teichospora_sp.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:2107984` at `data/raw/ncbitaxon_taxa.tsv:518314`, label `Teichospora sp.`, rank `SPECIES`, parent `NCBITaxon:2639038`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 62359.
- NCBI supplied 2 exact synonyms, 0 broad synonyms, and 0 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 17 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 2 old IDs, `NCBITaxon:3115456` and `NCBITaxon:3445467`, which both resolved to this retained target and had no retained rows in the local NCBI taxa table.

## Evidence
- The GOLD aggregate row at line 20149 matched the YAML source attestation with organism_count 1 for `NCBITaxon:2107984`.
- Native GOLD tables contained 0 organism rows, 0 project rows, and 0 analysis rows for this target.
- Local NCBI type material was absent for this target.
- StrainInfo contained 0 direct records and 0 exact deposit rows for this taxon. BacDive had 0 exact local rows.

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
