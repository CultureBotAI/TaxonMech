# YAML Record Review: Symbiodinium microadriaticum

- Verdict: pass
- Target: `data/taxa/eukaryota/symbiodinium_microadriaticum.yaml`
- Identifier: `NCBITaxon:2951`

## Target
- Reviewed the complete 60-line YAML record for Symbiodinium microadriaticum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for symbiodinium_microadriaticum.

## Validation
- `just validate data/taxa/eukaryota/symbiodinium_microadriaticum.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/symbiodinium_microadriaticum.yaml data/taxa/eukaryota/symbiodinium_natans.yaml data/taxa/eukaryota/symbiodinium_necroappetens.yaml data/taxa/eukaryota/symbiodinium_pilosum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:2951` at `data/raw/ncbitaxon_taxa.tsv:2002`, label `Symbiodinium microadriaticum`, rank `SPECIES`, parent `NCBITaxon:2949`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 51825.
- NCBI supplied 0 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML carried the same NCBITaxon-sourced synonym set.
- All 9 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 29342 matched the YAML source attestation with organism_count 3 for `NCBITaxon:2951`.
- Native GOLD tables contained 3 organism rows, 3 project rows, and 3 analysis rows for this target.
- Local NCBI type material was absent for this target.
- StrainInfo contained 10 direct records and 10 exact deposit rows for this taxon. BacDive had 0 exact local rows.

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
