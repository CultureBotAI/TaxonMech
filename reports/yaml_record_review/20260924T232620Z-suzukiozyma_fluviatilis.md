# YAML Record Review: Suzukiozyma fluviatilis

- Verdict: pass
- Target: `data/taxa/eukaryota/suzukiozyma_fluviatilis.yaml`
- Identifier: `NCBITaxon:45551`

## Target
- Reviewed the complete 79-line YAML record for Suzukiozyma fluviatilis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for suzukiozyma_fluviatilis.

## Validation
- `just validate data/taxa/eukaryota/suzukiozyma_fluviatilis.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/suzukiozyma_candida.yaml data/taxa/eukaryota/suzukiozyma_fluviatilis.yaml data/taxa/eukaryota/suzukiozyma_glaebosa.yaml data/taxa/eukaryota/suzukiozyma_manassasensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:45551` at `data/raw/ncbitaxon_taxa.tsv:5605`, label `Suzukiozyma fluviatilis`, rank `SPECIES`, parent `NCBITaxon:3712560`, genetic code `12`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 52651.
- NCBI supplied 1 exact synonym, 0 broad synonyms, and 2 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 13 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 36060 matched the YAML source attestation with organism_count 1 for `NCBITaxon:45551`.
- Native GOLD tables contained 1 organism row and 1 project row, with 0 analysis rows, for this target.
- `data/raw/ncbi_type_material.tsv` contained 19 exact NCBI-prefixed rows for the target's holotype and culture-from-holotype accessions.
- StrainInfo contained 3 direct records and 18 exact deposit rows for this taxon; the parsed non-direct deposit lookup returned no additional rows. BacDive had 0 exact local rows.

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
