# YAML Record Review: Synchroma pusillum

- Verdict: pass
- Target: `data/taxa/eukaryota/synchroma_pusillum.yaml`
- Identifier: `NCBITaxon:1181717`

## Target
- Reviewed the complete 69-line YAML record for Synchroma pusillum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for synchroma_pusillum.

## Validation
- `just validate data/taxa/eukaryota/synchroma_pusillum.yaml` printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/syncephalis_plumigaleata.yaml data/taxa/eukaryota/syncephalis_pseudoplumigaleata.yaml data/taxa/eukaryota/synchroma_pusillum.yaml data/taxa/eukaryota/synchytrium_endobioticum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Retained exact NCBI row: `NCBITaxon:1181717` at `data/raw/ncbitaxon_taxa.tsv:263974`, label `Synchroma pusillum`, rank `SPECIES`, parent `NCBITaxon:1181712`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope inventory had 1 exact row for this taxon at line 58228.
- NCBI supplied 2 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML carried the same NCBITaxon-sourced synonym set.
- All 10 lineage links were checked against the local NCBI table with no missing parents and no label, rank, or identifier mismatches.
- The exact tab-bounded merged-ID lookup, run with ignored files included, found `NCBITaxon:1181716` remapped to `NCBITaxon:1181717` in `data/raw/ncbi_merged_ids.tsv` and no retained `data/raw/ncbitaxon_taxa.tsv` row for that old identifier.

## Evidence
- The GOLD aggregate row at line 3978 matched the YAML source attestation with organism_count 1 for `NCBITaxon:1181717`.
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
