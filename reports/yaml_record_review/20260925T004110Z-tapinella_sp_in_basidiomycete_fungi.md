# YAML Record Review: Tapinella sp. (in: basidiomycete fungi)

- Verdict: pass
- Target: `data/taxa/eukaryota/tapinella_sp_in_basidiomycete_fungi.yaml`
- Identifier: `NCBITaxon:2047543`

## Target
- Reviewed the complete 78-line YAML record for Tapinella sp. (in: basidiomycete fungi). The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tapinella_sp_in_basidiomycete_fungi.

## Validation
- `just validate data/taxa/eukaryota/tapinella_sp_in_basidiomycete_fungi.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/taphrina_antarctica.yaml data/taxa/eukaryota/taphrina_populi_salicis.yaml data/taxa/eukaryota/tapinella_atrotomentosa.yaml data/taxa/eukaryota/tapinella_sp_in_basidiomycete_fungi.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:2047543` at `data/raw/ncbitaxon_taxa.tsv:513631`, label `Tapinella sp. (in: basidiomycete fungi)`, rank `SPECIES`, parent `NCBITaxon:2676631`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 62178.
- NCBI supplied 1 exact synonym, 0 broad synonyms, and 0 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 15 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 19460 matched the YAML source attestation with organism_count 1 for `NCBITaxon:2047543`.
- Native GOLD tables contained 0 organism rows, 0 project rows, and 0 analysis rows for this target.
- Local NCBI type material was absent for this target.
- StrainInfo contained 0 direct records and 0 exact deposit rows for this taxon. BacDive had 0 exact local rows.

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
