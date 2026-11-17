# YAML Record Review: Synchytrium endobioticum

- Verdict: pass
- Target: `data/taxa/eukaryota/synchytrium_endobioticum.yaml`
- Identifier: `NCBITaxon:286115`

## Target
- Reviewed the complete 75-line YAML record for Synchytrium endobioticum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for synchytrium_endobioticum.

## Validation
- `just validate data/taxa/eukaryota/synchytrium_endobioticum.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/syncephalis_plumigaleata.yaml data/taxa/eukaryota/syncephalis_pseudoplumigaleata.yaml data/taxa/eukaryota/synchroma_pusillum.yaml data/taxa/eukaryota/synchytrium_endobioticum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:286115` at `data/raw/ncbitaxon_taxa.tsv:58493`, label `Synchytrium endobioticum`, rank `SPECIES`, parent `NCBITaxon:286114`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 54997.
- NCBI supplied 1 exact synonym, 0 broad synonyms, and 1 related synonym; the YAML carried the same NCBITaxon-sourced synonym set.
- All 13 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 27789 matched the YAML source attestation with organism_count 3 for `NCBITaxon:286115`.
- Native GOLD tables contained 3 organism rows, 3 project rows, and 3 analysis rows for this target.
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
