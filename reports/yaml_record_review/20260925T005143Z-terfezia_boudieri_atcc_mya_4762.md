# YAML Record Review: Terfezia boudieri ATCC MYA-4762

- Verdict: pass
- Target: `data/taxa/eukaryota/terfezia_boudieri_atcc_mya_4762.yaml`
- Identifier: `NCBITaxon:1051890`

## Target
- Reviewed the complete 75-line YAML record for Terfezia boudieri ATCC MYA-4762. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for terfezia_boudieri_atcc_mya_4762.

## Validation
- `just validate data/taxa/eukaryota/terfezia_boudieri_atcc_mya_4762.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/teratosphaeria_destructans.yaml data/taxa/eukaryota/teratosphaeria_nubilosa.yaml data/taxa/eukaryota/terfezia_boudieri.yaml data/taxa/eukaryota/terfezia_boudieri_atcc_mya_4762.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:1051890` at `data/raw/ncbitaxon_taxa.tsv:226883`, label `Terfezia boudieri ATCC MYA-4762`, rank `STRAIN`, parent `NCBITaxon:82571`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 57395.
- NCBI supplied 1 exact synonym, 0 broad synonyms, and 0 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 14 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 955 matched the YAML source attestation with organism_count 1 for `NCBITaxon:1051890`.
- Native GOLD tables contained 0 organism rows, 0 project rows, and 0 analysis rows for this target.
- Local NCBI type material was absent for this target strain.
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
