# YAML Record Review: Talaromyces islandicus

- Verdict: pass
- Target: `data/taxa/eukaryota/talaromyces_islandicus.yaml`
- Identifier: `NCBITaxon:28573`

## Target
- Reviewed the complete 87-line YAML record for Talaromyces islandicus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for talaromyces_islandicus.

## Validation
- `just validate data/taxa/eukaryota/talaromyces_islandicus.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/talaromyces_islandicus.yaml data/taxa/eukaryota/talaromyces_marneffei.yaml data/taxa/eukaryota/talaromyces_piceae.yaml data/taxa/eukaryota/talaromyces_pinophilus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:28573` at `data/raw/ncbitaxon_taxa.tsv:2974`, label `Talaromyces islandicus`, rank `SPECIES`, parent `NCBITaxon:2752542`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 52181.
- NCBI supplied 2 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML carried the same NCBITaxon-sourced synonym set.
- All 16 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 27747 matched the YAML source attestation with organism_count 1 for `NCBITaxon:28573`.
- Native GOLD tables contained 1 organism row, 1 project row, and 1 analysis row for this target.
- Local NCBI type material had 10 exact culture-from-neotype rows for this target from `typematerial.dmp`.
- StrainInfo contained 91 direct records and 153 exact deposit rows for this taxon. BacDive had 0 exact local rows.

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
