# YAML Record Review: Symbiodinium sp.

- Verdict: pass
- Target: `data/taxa/eukaryota/symbiodinium_sp.yaml`
- Identifier: `NCBITaxon:2950`

## Target
- Reviewed the complete 59-line YAML record for Symbiodinium sp. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for symbiodinium_sp.

## Validation
- `just validate data/taxa/eukaryota/symbiodinium_sp.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/symbiodinium_sp.yaml data/taxa/eukaryota/symbiodinium_sp_clade_a_y106.yaml data/taxa/eukaryota/symbiodinium_sp_clade_c_y103.yaml data/taxa/eukaryota/symbiodinium_sp_kb8.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:2950` at `data/raw/ncbitaxon_taxa.tsv:2001`, label `Symbiodinium sp.`, rank `SPECIES`, parent `NCBITaxon:279888`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 51824.
- NCBI supplied 0 exact synonyms, 0 broad synonyms, and 0 related synonyms; the YAML correctly had no NCBITaxon synonym block.
- All 10 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 29305 matched the YAML source attestation with organism_count 7 for `NCBITaxon:2950`.
- Native GOLD tables contained 8 organism rows and 1 project row, with 0 analysis rows, for this target.
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
