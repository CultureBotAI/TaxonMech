# YAML Record Review: Syracosphaera pulchra

- Verdict: pass
- Target: `data/taxa/eukaryota/syracosphaera_pulchra.yaml`
- Identifier: `NCBITaxon:418946`

## Target
- Reviewed the complete 60-line YAML record for Syracosphaera pulchra. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for syracosphaera_pulchra.

## Validation
- `just validate data/taxa/eukaryota/syracosphaera_pulchra.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/syracosphaera_pulchra.yaml data/taxa/eukaryota/syzygites_megalocarpus.yaml data/taxa/eukaryota/taiozyma_bovis.yaml data/taxa/eukaryota/taiozyma_dajiaensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:418946` at `data/raw/ncbitaxon_taxa.tsv:91790`, label `Syracosphaera pulchra`, rank `SPECIES`, parent `NCBITaxon:74025`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 55592.
- NCBI supplied 0 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML carried the same NCBITaxon-sourced synonym set.
- All 9 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 34998 matched the YAML source attestation with organism_count 1 for `NCBITaxon:418946`.
- Native GOLD tables contained 0 organism rows, 0 project rows, and 0 analysis rows for this target.
- Local NCBI type material was absent for this target.
- StrainInfo contained 8 direct records and 8 exact deposit rows for this taxon. BacDive had 0 exact local rows.

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
