# YAML Record Review: Terfezia claveryi

- Verdict: pass
- Target: `data/taxa/eukaryota/terfezia_claveryi.yaml`
- Identifier: `NCBITaxon:139407`

## Target
- Reviewed the complete 72-line YAML record for Terfezia claveryi. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for terfezia_claveryi.

## Validation
- `just validate data/taxa/eukaryota/terfezia_claveryi.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/terfezia_claveryi.yaml data/taxa/eukaryota/termitomyces_eurrhizus.yaml data/taxa/eukaryota/termitomyces_heimii.yaml data/taxa/eukaryota/termitomyces_sp_cryptogamus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:139407` at `data/raw/ncbitaxon_taxa.tsv:28167`, label `Terfezia claveryi`, rank `SPECIES`, parent `NCBITaxon:74855`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 54005.
- NCBI supplied 0 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML carried the same NCBITaxon-sourced synonym set.
- All 13 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 9311 matched the YAML source attestation with organism_count 2 for `NCBITaxon:139407`.
- Native GOLD tables contained 2 organism rows, 3 project rows, and 0 analysis rows for this target.
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
