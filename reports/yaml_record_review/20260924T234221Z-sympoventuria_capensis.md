# YAML Record Review: Sympoventuria capensis

- Verdict: pass
- Target: `data/taxa/eukaryota/sympoventuria_capensis.yaml`
- Identifier: `NCBITaxon:408669`

## Target
- Reviewed the complete 84-line YAML record for Sympoventuria capensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for sympoventuria_capensis.

## Validation
- `just validate data/taxa/eukaryota/sympoventuria_capensis.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/sympodiomycopsis_kandeliae.yaml data/taxa/eukaryota/sympodiomycopsis_paphiopedili.yaml data/taxa/eukaryota/sympoventuria_capensis.yaml data/taxa/eukaryota/syncephalastrum_monosporum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:408669` at `data/raw/ncbitaxon_taxa.tsv:88399`, label `Sympoventuria capensis`, rank `SPECIES`, parent `NCBITaxon:470111`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 55542.
- NCBI supplied 0 exact synonyms, 0 broad synonyms, and 2 related synonyms; the YAML carried the same NCBITaxon-sourced synonym set.
- All 16 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The local merged-ID table contributed 0 old IDs for this retained target.

## Evidence
- The GOLD aggregate row at line 34677 matched the YAML source attestation with organism_count 1 for `NCBITaxon:408669`.
- Native GOLD tables contained 0 organism rows, 0 project rows, and 0 analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` contained 8 exact NCBI-prefixed culture-from-holotype rows for the target.
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
