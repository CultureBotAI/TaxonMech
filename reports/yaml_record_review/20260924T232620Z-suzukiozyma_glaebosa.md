# YAML Record Review: Suzukiozyma glaebosa

- Verdict: pass
- Target: `data/taxa/eukaryota/suzukiozyma_glaebosa.yaml`
- Identifier: `NCBITaxon:45554`

## Target
- Reviewed the complete 79-line YAML record for Suzukiozyma glaebosa. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for suzukiozyma_glaebosa.

## Validation
- `just validate data/taxa/eukaryota/suzukiozyma_glaebosa.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/suzukiozyma_candida.yaml data/taxa/eukaryota/suzukiozyma_fluviatilis.yaml data/taxa/eukaryota/suzukiozyma_glaebosa.yaml data/taxa/eukaryota/suzukiozyma_manassasensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:45554` at `data/raw/ncbitaxon_taxa.tsv:5608`, label `Suzukiozyma glaebosa`, rank `SPECIES`, parent `NCBITaxon:3712560`, genetic code `12`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 52654.
- NCBI supplied 1 exact synonym, 0 broad synonyms, and 2 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 13 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 36063 matched the YAML source attestation with organism_count 1 for `NCBITaxon:45554`.
- Native GOLD tables contained 1 organism row and 1 project row, with 0 analysis rows, for this target.
- `data/raw/ncbi_type_material.tsv` contained 24 exact NCBI-prefixed rows for the target's holotype and culture-from-holotype accessions.
- StrainInfo contained 9 direct records and 28 exact deposit rows for this taxon, plus 1 non-direct `Candida pseudoglaebosa` record carrying 3 exact deposits for `NCBITaxon:45554`. BacDive had 0 exact local rows.

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
