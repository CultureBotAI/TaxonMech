# YAML Record Review: Syncephalastrum racemosum

- Verdict: pass
- Target: `data/taxa/eukaryota/syncephalastrum_racemosum.yaml`
- Identifier: `NCBITaxon:13706`

## Target
- Reviewed the complete 72-line YAML record for Syncephalastrum racemosum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for syncephalastrum_racemosum.

## Validation
- `just validate data/taxa/eukaryota/syncephalastrum_racemosum.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/syncephalastrum_racemosum.yaml data/taxa/eukaryota/syncephalastrum_verruculosum.yaml data/taxa/eukaryota/syncephalis_cornu.yaml data/taxa/eukaryota/syncephalis_fuscata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:13706` at `data/raw/ncbitaxon_taxa.tsv:2696`, label `Syncephalastrum racemosum`, rank `SPECIES`, parent `NCBITaxon:13705`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 52128.
- NCBI supplied 1 exact synonym, 0 broad synonyms, and 1 related synonym; the YAML carried the same NCBITaxon-sourced synonym set.
- All 12 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The exact tab-bounded merged-ID lookup, run with ignored files included, found `NCBITaxon:1618010` and `NCBITaxon:862185` remapped to `NCBITaxon:13706` in `data/raw/ncbi_merged_ids.tsv` and no retained `data/raw/ncbitaxon_taxa.tsv` rows for those old identifiers.

## Evidence
- The GOLD aggregate row at line 8865 matched the YAML source attestation with organism_count 10 for `NCBITaxon:13706`.
- Native GOLD tables contained 10 organism rows, 12 project rows, and 2 analysis rows for this target.
- Local NCBI type material was absent for this target.
- StrainInfo contained 93 direct records and 126 exact deposit rows for this taxon. BacDive had 0 exact local rows.

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
