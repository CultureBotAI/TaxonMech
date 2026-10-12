# YAML Record Review: Talaromyces adpressus

- Verdict: pass
- Target: `data/taxa/eukaryota/talaromyces_adpressus.yaml`
- Identifier: `NCBITaxon:1974180`

## Target
- Reviewed the complete 84-line YAML record for Talaromyces adpressus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for talaromyces_adpressus.

## Validation
- `just validate data/taxa/eukaryota/talaromyces_adpressus.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/talaromyces_aculeatus_atcc_10409.yaml data/taxa/eukaryota/talaromyces_adpressus.yaml data/taxa/eukaryota/talaromyces_amestolkiae.yaml data/taxa/eukaryota/talaromyces_atroroseus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:1974180` at `data/raw/ncbitaxon_taxa.tsv:506591`, label `Talaromyces adpressus`, rank `SPECIES`, parent `NCBITaxon:2752537`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 61785.
- NCBI supplied 0 exact synonyms, 0 broad synonyms, and 2 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 16 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 1 old ID, `NCBITaxon:1810896`, which resolved to this retained target and had no retained row in the local NCBI taxa table.

## Evidence
- The GOLD aggregate row at line 18237 matched the YAML source attestation with organism_count 1 for `NCBITaxon:1974180`.
- Native GOLD tables contained 1 organism row, 1 project row, and 1 analysis row for this target.
- Local NCBI type material had 9 exact rows for this target, spanning culture-from-type-material and holotype rows from `typematerial.dmp`.
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
