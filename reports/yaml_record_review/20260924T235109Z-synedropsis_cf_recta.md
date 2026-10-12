# YAML Record Review: Synedropsis cf. recta

- Verdict: pass
- Target: `data/taxa/eukaryota/synedropsis_cf_recta.yaml`
- Identifier: `NCBITaxon:265551`

## Target
- Reviewed the complete 65-line YAML record for Synedropsis cf. recta. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for synedropsis_cf_recta.

## Validation
- `just validate data/taxa/eukaryota/synedropsis_cf_recta.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/synedropsis_cf_recta.yaml data/taxa/eukaryota/synura_echinulata.yaml data/taxa/eukaryota/synura_petersenii.yaml data/taxa/eukaryota/synura_rubra.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:265551` at `data/raw/ncbitaxon_taxa.tsv:54359`, label `Synedropsis cf. recta`, rank `SPECIES`, parent `NCBITaxon:186019`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 54883.
- NCBI supplied 0 exact synonyms, 0 broad synonyms, and 0 related synonyms; the YAML correctly had no NCBITaxon synonym block.
- All 12 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 24374 matched the YAML source attestation with organism_count 1 for `NCBITaxon:265551`.
- Native GOLD tables contained 1 organism row, 0 project rows, and 0 analysis rows for this target.
- Local NCBI type material was absent for this target.
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
- No seeded YAML edits are needed; the record is consistent with all checked local NCBI, GOLD, BacDive, and StrainInfo evidence.
