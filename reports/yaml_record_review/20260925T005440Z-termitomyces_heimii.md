# YAML Record Review: Termitomyces heimii

- Verdict: pass
- Target: `data/taxa/eukaryota/termitomyces_heimii.yaml`
- Identifier: `NCBITaxon:71929`

## Target
- Reviewed the complete 75-line YAML record for Termitomyces heimii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for termitomyces_heimii.

## Validation
- `just validate data/taxa/eukaryota/termitomyces_heimii.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/terfezia_claveryi.yaml data/taxa/eukaryota/termitomyces_eurrhizus.yaml data/taxa/eukaryota/termitomyces_heimii.yaml data/taxa/eukaryota/termitomyces_sp_cryptogamus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:71929` at `data/raw/ncbitaxon_taxa.tsv:10061`, label `Termitomyces heimii`, rank `SPECIES`, parent `NCBITaxon:71927`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 53226.
- NCBI supplied 0 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML carried the same NCBITaxon-sourced synonym set.
- All 14 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 41951 matched the YAML source attestation with organism_count 1 for `NCBITaxon:71929`.
- Native GOLD tables contained 1 organism row, 1 project row, and 1 analysis row for this target.
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
