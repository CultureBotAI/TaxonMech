# YAML Record Review: Symbiodinium kawagutii

- Verdict: pass
- Target: `data/taxa/eukaryota/symbiodinium_kawagutii.yaml`
- Identifier: `NCBITaxon:104179`

## Target
- Reviewed the complete 60-line YAML record for Symbiodinium kawagutii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for symbiodinium_kawagutii.

## Validation
- `just validate data/taxa/eukaryota/symbiodinium_kawagutii.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/suzukiozyma_palmioleophila.yaml data/taxa/eukaryota/suzukiozyma_pseudoglaebosa.yaml data/taxa/eukaryota/suzukiozyma_sphagnicola.yaml data/taxa/eukaryota/symbiodinium_kawagutii.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:104179` at `data/raw/ncbitaxon_taxa.tsv:18617`, label `Symbiodinium kawagutii`, rank `SPECIES`, parent `NCBITaxon:2949`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 53672.
- NCBI supplied 0 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML carried the same NCBITaxon-sourced synonym set.
- All 9 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 598 matched the YAML source attestation with organism_count 2 for `NCBITaxon:104179`.
- Native GOLD tables contained 2 organism rows, 1 project row, and 1 analysis row for this target.
- Local NCBI type material was absent for this target.
- StrainInfo contained 1 direct record and 1 exact deposit row for this taxon. BacDive had 0 exact local rows.

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
