# YAML Record Review: Suzukiozyma palmioleophila

- Verdict: pass
- Target: `data/taxa/eukaryota/suzukiozyma_palmioleophila.yaml`
- Identifier: `NCBITaxon:45574`

## Target
- Reviewed the complete 79-line YAML record for Suzukiozyma palmioleophila. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for suzukiozyma_palmioleophila.

## Validation
- `just validate data/taxa/eukaryota/suzukiozyma_palmioleophila.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/suzukiozyma_palmioleophila.yaml data/taxa/eukaryota/suzukiozyma_pseudoglaebosa.yaml data/taxa/eukaryota/suzukiozyma_sphagnicola.yaml data/taxa/eukaryota/symbiodinium_kawagutii.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:45574` at `data/raw/ncbitaxon_taxa.tsv:5621`, label `Suzukiozyma palmioleophila`, rank `SPECIES`, parent `NCBITaxon:3712560`, genetic code `12`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 52667.
- NCBI supplied 1 exact synonym, 0 broad synonyms, and 2 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 13 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 36076 matched the YAML source attestation with organism_count 1 for `NCBITaxon:45574`.
- Native GOLD tables contained 1 organism row and 1 project row, with 0 analysis rows, for this target.
- `data/raw/ncbi_type_material.tsv` contained 9 exact NCBI-prefixed rows for the target's holotype and culture-from-holotype accessions.
- StrainInfo contained 16 direct records and 30 exact deposit rows for this taxon, plus 1 non-direct `Candida` record carrying 1 exact deposit for `NCBITaxon:45574`. BacDive had 0 exact local rows.

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
