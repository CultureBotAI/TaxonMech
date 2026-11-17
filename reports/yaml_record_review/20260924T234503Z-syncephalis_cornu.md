# YAML Record Review: Syncephalis cornu

- Verdict: pass
- Target: `data/taxa/eukaryota/syncephalis_cornu.yaml`
- Identifier: `NCBITaxon:1029783`

## Target
- Reviewed the complete 69-line YAML record for Syncephalis cornu. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for syncephalis_cornu.

## Validation
- `just validate data/taxa/eukaryota/syncephalis_cornu.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/syncephalastrum_racemosum.yaml data/taxa/eukaryota/syncephalastrum_verruculosum.yaml data/taxa/eukaryota/syncephalis_cornu.yaml data/taxa/eukaryota/syncephalis_fuscata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:1029783` at `data/raw/ncbitaxon_taxa.tsv:220063`, label `Syncephalis cornu`, rank `SPECIES`, parent `NCBITaxon:78910`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 57229.
- NCBI supplied 0 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML carried the same NCBITaxon-sourced synonym set.
- All 12 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 357 matched the YAML source attestation with organism_count 2 for `NCBITaxon:1029783`.
- Native GOLD tables contained 2 organism rows and 2 project rows, with 0 analysis rows, for this target.
- Local NCBI type material was absent for this target.
- StrainInfo contained 9 direct records and 11 exact deposit rows for this taxon. BacDive had 0 exact local rows.

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
