# YAML Record Review: Taphrina antarctica

- Verdict: pass
- Target: `data/taxa/eukaryota/taphrina_antarctica.yaml`
- Identifier: `NCBITaxon:1221547`

## Target
- Reviewed the complete 75-line YAML record for Taphrina antarctica. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for taphrina_antarctica.

## Validation
- `just validate data/taxa/eukaryota/taphrina_antarctica.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/taphrina_antarctica.yaml data/taxa/eukaryota/taphrina_populi_salicis.yaml data/taxa/eukaryota/tapinella_atrotomentosa.yaml data/taxa/eukaryota/tapinella_sp_in_basidiomycete_fungi.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:1221547` at `data/raw/ncbitaxon_taxa.tsv:277221`, label `Taphrina antarctica`, rank `SPECIES`, parent `NCBITaxon:5010`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 58481.
- NCBI supplied 0 exact synonyms, 0 broad synonyms, and 3 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 12 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 1 old ID, `NCBITaxon:1221548`, which resolved to this retained target and had no retained row in the local NCBI taxa table.

## Evidence
- The GOLD aggregate row at line 5320 matched the YAML source attestation with organism_count 4 for `NCBITaxon:1221547`.
- Native GOLD tables contained 4 organism rows, 0 project rows, and 0 analysis rows for this target.
- Local NCBI type material had 2 exact culture-from-holotype rows for this target from `typematerial.dmp`.
- StrainInfo contained 1 direct record and 1 exact deposit row for this taxon. BacDive had 0 exact local rows.

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
