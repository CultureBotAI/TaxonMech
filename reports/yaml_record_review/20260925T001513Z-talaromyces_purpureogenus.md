# YAML Record Review: Talaromyces purpureogenus

- Verdict: pass
- Target: `data/taxa/eukaryota/talaromyces_purpureogenus.yaml`
- Identifier: `NCBITaxon:1266744`

## Target
- Reviewed the complete 112-line YAML record for Talaromyces purpureogenus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for talaromyces_purpureogenus.

## Validation
- `just validate data/taxa/eukaryota/talaromyces_purpureogenus.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/talaromyces_proteolyticus.yaml data/taxa/eukaryota/talaromyces_purpureogenus.yaml data/taxa/eukaryota/talaromyces_sp_b14p1.yaml data/taxa/eukaryota/talaromyces_sp_f3606.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:1266744` at `data/raw/ncbitaxon_taxa.tsv:293778`, label `Talaromyces purpureogenus`, rank `SPECIES`, parent `NCBITaxon:2752537`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 58810.
- NCBI supplied 4 exact synonyms, 0 broad synonyms, and 7 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 16 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 9 old IDs, all of which resolved to this retained target and had no retained rows in the local NCBI taxa table.

## Evidence
- The GOLD aggregate row at line 6333 matched the YAML source attestation with organism_count 1 for `NCBITaxon:1266744`.
- Native GOLD tables contained 1 organism row, 2 project rows, and 1 analysis row for this target.
- Local NCBI type material had 4 exact culture-from-neotype rows for this target from `typematerial.dmp`.
- StrainInfo contained 7 direct records and 8 exact deposit rows for this taxon. BacDive had 0 exact local rows.

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
