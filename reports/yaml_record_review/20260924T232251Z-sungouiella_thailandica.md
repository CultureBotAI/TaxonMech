# YAML Record Review: Sungouiella thailandica

- Verdict: pass
- Target: `data/taxa/eukaryota/sungouiella_thailandica.yaml`
- Identifier: `NCBITaxon:1323753`

## Target
- Reviewed the complete 83-line YAML record for Sungouiella thailandica. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for sungouiella_thailandica.

## Validation
- `just validate data/taxa/eukaryota/sungouiella_thailandica.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/sungouiella_thailandica.yaml data/taxa/eukaryota/sungouiella_tsuchiyae.yaml data/taxa/eukaryota/sungouiozyma_ichnusensis.yaml data/taxa/eukaryota/sungouiozyma_intestinalis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:1323753` at `data/raw/ncbitaxon_taxa.tsv:315399`, label `Sungouiella thailandica`, rank `SPECIES`, parent `NCBITaxon:3315605`, genetic code `12`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 59459.
- NCBI supplied 1 exact synonym, 0 broad synonyms, and 3 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 13 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The exact tab-bounded merged-ID lookup, run with ignored files included, found `NCBITaxon:225543` remapped to `NCBITaxon:1323753` in `data/raw/ncbi_merged_ids.tsv` and no retained `data/raw/ncbitaxon_taxa.tsv` row for that old identifier.

## Evidence
- The GOLD aggregate row at line 7866 matched the YAML source attestation with organism_count 1 for `NCBITaxon:1323753`.
- Native GOLD tables contained 1 organism row and 1 project row, with 0 analysis rows, for this target.
- `data/raw/ncbi_type_material.tsv` contained 13 exact NCBI-prefixed rows for the target's holotype and culture-from-holotype accessions.
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
