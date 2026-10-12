# YAML Record Review: Taiozyma yuanshanica

- Verdict: pass
- Target: `data/taxa/eukaryota/taiozyma_yuanshanica.yaml`
- Identifier: `NCBITaxon:639368`

## Target
- Reviewed the complete 79-line YAML record for Taiozyma yuanshanica. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for taiozyma_yuanshanica.

## Validation
- `just validate data/taxa/eukaryota/taiozyma_yuanshanica.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/taiozyma_sp_m8010.yaml data/taxa/eukaryota/taiozyma_sp_pg4208.yaml data/taxa/eukaryota/taiozyma_sp_yhql14.yaml data/taxa/eukaryota/taiozyma_yuanshanica.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:639368` at `data/raw/ncbitaxon_taxa.tsv:147339`, label `Taiozyma yuanshanica`, rank `SPECIES`, parent `NCBITaxon:3712561`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 56199.
- NCBI supplied 1 exact synonym, 0 broad synonyms, and 2 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 13 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 1 old ID, `NCBITaxon:432113`, which resolved to this retained target and had no retained row in the local NCBI taxa table.

## Evidence
- The GOLD aggregate row at line 40185 matched the YAML source attestation with organism_count 1 for `NCBITaxon:639368`.
- Native GOLD tables contained 1 organism row, 1 project row, and 0 analysis rows for this target.
- Local NCBI type material had 9 exact rows for this target, spanning culture-from-holotype and holotype rows from `typematerial.dmp`.
- StrainInfo contained 2 direct records and 4 exact deposit rows for this taxon. BacDive had 0 exact local rows.

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
