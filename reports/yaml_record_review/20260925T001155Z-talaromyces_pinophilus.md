# YAML Record Review: Talaromyces pinophilus

- Verdict: pass
- Target: `data/taxa/eukaryota/talaromyces_pinophilus.yaml`
- Identifier: `NCBITaxon:128442`

## Target
- Reviewed the complete 106-line YAML record for Talaromyces pinophilus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for talaromyces_pinophilus.

## Validation
- `just validate data/taxa/eukaryota/talaromyces_pinophilus.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/talaromyces_islandicus.yaml data/taxa/eukaryota/talaromyces_marneffei.yaml data/taxa/eukaryota/talaromyces_piceae.yaml data/taxa/eukaryota/talaromyces_pinophilus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:128442` at `data/raw/ncbitaxon_taxa.tsv:24598`, label `Talaromyces pinophilus`, rank `SPECIES`, parent `NCBITaxon:2752537`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 53915.
- NCBI supplied 5 exact synonyms, 0 broad synonyms, and 4 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 16 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 5 old IDs, `NCBITaxon:1257279`, `NCBITaxon:1414448`, `NCBITaxon:1472165`, `NCBITaxon:627224`, and `NCBITaxon:87064`, which all resolved to this retained target and had no retained rows in the local NCBI taxa table.

## Evidence
- The GOLD aggregate row at line 6605 matched the YAML source attestation with organism_count 7 for `NCBITaxon:128442`.
- Native GOLD tables contained 5 organism rows, 5 project rows, and 5 analysis rows for this target.
- Local NCBI type material had 20 exact rows for this target, spanning culture-from-holotype, culture-from-neotype, holotype, and type-material rows from `typematerial.dmp`.
- StrainInfo contained 65 direct records and 145 exact deposit rows for this taxon. BacDive had 0 exact local rows.

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
