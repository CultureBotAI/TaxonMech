# YAML Record Review: Symbiodinium sp. clade A Y106

- Verdict: pass
- Target: `data/taxa/eukaryota/symbiodinium_sp_clade_a_y106.yaml`
- Identifier: `NCBITaxon:1563115`

## Target
- Reviewed the complete 65-line YAML record for Symbiodinium sp. clade A Y106. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for symbiodinium_sp_clade_a_y106.

## Validation
- `just validate data/taxa/eukaryota/symbiodinium_sp_clade_a_y106.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/symbiodinium_sp.yaml data/taxa/eukaryota/symbiodinium_sp_clade_a_y106.yaml data/taxa/eukaryota/symbiodinium_sp_clade_c_y103.yaml data/taxa/eukaryota/symbiodinium_sp_kb8.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:1563115` at `data/raw/ncbitaxon_taxa.tsv:401798`, label `Symbiodinium sp. clade A Y106`, rank `STRAIN`, parent `NCBITaxon:765179`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 60470.
- NCBI supplied 0 exact synonyms, 0 broad synonyms, and 0 related synonyms; the YAML correctly had no NCBITaxon synonym block.
- All 12 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 12528 matched the YAML source attestation with organism_count 1 for `NCBITaxon:1563115`.
- Native GOLD tables contained 1 organism row, 1 project row, and 1 analysis row for this target.
- Local NCBI type material was absent for this target.
- Local exact rows were absent from BacDive and StrainInfo direct/deposit scans.

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
