# YAML Record Review: Talaromyces funiculosus

- Verdict: pass
- Target: `data/taxa/eukaryota/talaromyces_funiculosus.yaml`
- Identifier: `NCBITaxon:28572`

## Target
- Reviewed the complete 90-line YAML record for Talaromyces funiculosus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for talaromyces_funiculosus.

## Validation
- `just validate data/taxa/eukaryota/talaromyces_funiculosus.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/talaromyces_bacillisporus.yaml data/taxa/eukaryota/talaromyces_diversus.yaml data/taxa/eukaryota/talaromyces_funiculosus.yaml data/taxa/eukaryota/talaromyces_helicus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:28572` at `data/raw/ncbitaxon_taxa.tsv:2973`, label `Talaromyces funiculosus`, rank `SPECIES`, parent `NCBITaxon:2752537`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 52180.
- NCBI supplied 1 exact synonym, 0 broad synonyms, and 3 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 16 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 2 old IDs, `NCBITaxon:1390067` and `NCBITaxon:1541422`, which both resolved to this retained target and had no retained rows in the local NCBI taxa table.

## Evidence
- The GOLD aggregate row at line 27745 matched the YAML source attestation with organism_count 9 for `NCBITaxon:28572`.
- Native GOLD tables contained 9 organism rows, 9 project rows, and 9 analysis rows for this target.
- Local NCBI type material had 4 exact culture-from-neotype rows for this target from `typematerial.dmp`.
- StrainInfo contained 98 direct records and 167 exact deposit rows for this taxon. BacDive had 0 exact local rows.

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
