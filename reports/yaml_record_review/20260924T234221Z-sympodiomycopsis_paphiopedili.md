# YAML Record Review: Sympodiomycopsis paphiopedili

- Verdict: pass
- Target: `data/taxa/eukaryota/sympodiomycopsis_paphiopedili.yaml`
- Identifier: `NCBITaxon:37782`

## Target
- Reviewed the complete 69-line YAML record for Sympodiomycopsis paphiopedili. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for sympodiomycopsis_paphiopedili.

## Validation
- `just validate data/taxa/eukaryota/sympodiomycopsis_paphiopedili.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/sympodiomycopsis_kandeliae.yaml data/taxa/eukaryota/sympodiomycopsis_paphiopedili.yaml data/taxa/eukaryota/sympoventuria_capensis.yaml data/taxa/eukaryota/syncephalastrum_monosporum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:37782` at `data/raw/ncbitaxon_taxa.tsv:4285`, label `Sympodiomycopsis paphiopedili`, rank `SPECIES`, parent `NCBITaxon:37842`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 52377.
- NCBI supplied 0 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML carried the same NCBITaxon-sourced synonym set.
- All 12 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 33794 matched the YAML source attestation with organism_count 4 for `NCBITaxon:37782`.
- Native GOLD tables contained 4 organism rows, 0 project rows, and 0 analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` contained 7 exact NCBI-prefixed type-material and culture-from-type-material rows for the target.
- StrainInfo contained 2 direct records and 16 exact deposit rows for this taxon. BacDive had 0 exact local rows.

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
