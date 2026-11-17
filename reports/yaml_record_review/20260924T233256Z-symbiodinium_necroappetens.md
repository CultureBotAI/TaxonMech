# YAML Record Review: Symbiodinium necroappetens

- Verdict: pass
- Target: `data/taxa/eukaryota/symbiodinium_necroappetens.yaml`
- Identifier: `NCBITaxon:1628268`

## Target
- Reviewed the complete 64-line YAML record for Symbiodinium necroappetens. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for symbiodinium_necroappetens.

## Validation
- `just validate data/taxa/eukaryota/symbiodinium_necroappetens.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/symbiodinium_microadriaticum.yaml data/taxa/eukaryota/symbiodinium_natans.yaml data/taxa/eukaryota/symbiodinium_necroappetens.yaml data/taxa/eukaryota/symbiodinium_pilosum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:1628268` at `data/raw/ncbitaxon_taxa.tsv:423245`, label `Symbiodinium necroappetens`, rank `SPECIES`, parent `NCBITaxon:2949`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 60926.
- NCBI supplied 0 exact synonyms, 0 broad synonyms, and 2 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 9 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 13923 matched the YAML source attestation with organism_count 1 for `NCBITaxon:1628268`.
- Native GOLD tables contained 1 organism row, 1 project row, and 1 analysis row for this target.
- `data/raw/ncbi_type_material.tsv` contained 2 exact NCBI-prefixed type-material rows for the target.
- Local exact rows were absent from BacDive and StrainInfo direct/deposit scans.

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
