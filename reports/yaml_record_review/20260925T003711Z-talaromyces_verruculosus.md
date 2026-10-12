# YAML Record Review: Talaromyces verruculosus

- Verdict: pass
- Target: `data/taxa/eukaryota/talaromyces_verruculosus.yaml`
- Identifier: `NCBITaxon:198730`

## Target
- Reviewed the complete 94-line YAML record for Talaromyces verruculosus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for talaromyces_verruculosus.

## Validation
- `just validate data/taxa/eukaryota/talaromyces_verruculosus.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/talaromyces_thailandensis.yaml data/taxa/eukaryota/talaromyces_verruculosus.yaml data/taxa/eukaryota/talaromyces_wortmannii.yaml data/taxa/eukaryota/tanozyma_kutaoensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:198730` at `data/raw/ncbitaxon_taxa.tsv:39459`, label `Talaromyces verruculosus`, rank `SPECIES`, parent `NCBITaxon:2752537`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 54444.
- NCBI supplied 1 exact synonym, 0 broad synonyms, and 4 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 16 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 2 old IDs, `NCBITaxon:1390059` and `NCBITaxon:3134886`, which both resolved to this retained target and had no retained rows in the local NCBI taxa table.

## Evidence
- The GOLD aggregate row at line 18404 matched the YAML source attestation with organism_count 1 for `NCBITaxon:198730`.
- Native GOLD tables contained 1 organism row, 1 project row, and 1 analysis row for this target.
- Local NCBI type material had 10 exact culture-from-neotype rows for this target from `typematerial.dmp`.
- StrainInfo contained 60 direct records and 103 exact deposit rows for this taxon, plus 4 non-direct records carrying 7 exact deposits for `NCBITaxon:198730`. BacDive had 0 exact local rows.

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
