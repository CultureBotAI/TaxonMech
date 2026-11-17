# YAML Record Review: Teleaulax acuta

- Verdict: pass
- Target: `data/taxa/eukaryota/teleaulax_acuta.yaml`
- Identifier: `NCBITaxon:195071`

## Target
- Reviewed the complete 66-line YAML record for Teleaulax acuta. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for teleaulax_acuta.

## Validation
- `just validate data/taxa/eukaryota/teleaulax_acuta.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/teleaulax_acuta.yaml data/taxa/eukaryota/teleaulax_amphioxeia.yaml data/taxa/eukaryota/teleaulax_sp_rcc4857.yaml data/taxa/eukaryota/tephrocybe_sp_nhm501043.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:195071` at `data/raw/ncbitaxon_taxa.tsv:38765`, label `Teleaulax acuta`, rank `SPECIES`, parent `NCBITaxon:77930`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 54426.
- NCBI supplied 2 exact synonyms, 0 broad synonyms, and 3 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 7 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 2 old IDs, `NCBITaxon:254932` and `NCBITaxon:356654`, which both resolved to this retained target and had no retained rows in the local NCBI taxa table.

## Evidence
- The GOLD aggregate row at line 17924 matched the YAML source attestation with organism_count 1 for `NCBITaxon:195071`.
- Native GOLD tables contained 0 organism rows, 0 project rows, and 0 analysis rows for this target.
- Local NCBI type material was absent for this target.
- StrainInfo contained 2 direct records and 3 exact deposit rows for this taxon. BacDive had 0 exact local rows.

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
