# YAML Record Review: Teratosphaeria nubilosa

- Verdict: pass
- Target: `data/taxa/eukaryota/teratosphaeria_nubilosa.yaml`
- Identifier: `NCBITaxon:161662`

## Target
- Reviewed the complete 96-line YAML record for Teratosphaeria nubilosa. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for teratosphaeria_nubilosa.

## Validation
- `just validate data/taxa/eukaryota/teratosphaeria_nubilosa.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/teratosphaeria_destructans.yaml data/taxa/eukaryota/teratosphaeria_nubilosa.yaml data/taxa/eukaryota/terfezia_boudieri.yaml data/taxa/eukaryota/terfezia_boudieri_atcc_mya_4762.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:161662` at `data/raw/ncbitaxon_taxa.tsv:33302`, label `Teratosphaeria nubilosa`, rank `SPECIES`, parent `NCBITaxon:237584`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 54187.
- NCBI supplied 4 exact synonyms, 0 broad synonyms, and 2 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 16 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 2 old IDs, `NCBITaxon:112485` and `NCBITaxon:112487`, which both resolved to this retained target and had no retained rows in the local NCBI taxa table.

## Evidence
- The GOLD aggregate row at line 13118 matched the YAML source attestation with organism_count 2 for `NCBITaxon:161662`.
- Native GOLD tables contained 1 organism row, 2 project rows, and 1 analysis row for this target.
- Local NCBI type material had 6 exact rows for this target, spanning culture-from-epitype and type-material rows from `typematerial.dmp`.
- StrainInfo contained 5 direct records and 5 exact deposit rows for this taxon. BacDive had 0 exact local rows.

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
