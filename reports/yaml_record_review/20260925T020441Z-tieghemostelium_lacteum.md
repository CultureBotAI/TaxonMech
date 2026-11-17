# YAML Record Review: Tieghemostelium lacteum

- Verdict: pass
- Target: `data/taxa/eukaryota/tieghemostelium_lacteum.yaml`
- Identifier: `NCBITaxon:361077`

## Target

Reviewed the complete 69-line YAML record for Tieghemostelium lacteum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tieghemostelium_lacteum.

## Validation

- `just validate data/taxa/eukaryota/tieghemostelium_lacteum.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tiarina_fusus.yaml data/taxa/eukaryota/tieghemiomyces_parasiticus.yaml data/taxa/eukaryota/tieghemostelium_lacteum.yaml data/taxa/eukaryota/tilletia_caries.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 75085: `NCBITaxon:361077`, `Tieghemostelium lacteum`, rank `SPECIES`, parent `NCBITaxon:2058951`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:361077` at line 55355.
- NCBI synonym columns contained 1 exact synonym, 0 broad synonyms, and 2 related synonyms, matching the three YAML synonym entries.
- The YAML lineage checked 10 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:361077`.

## Evidence

- The generated GOLD aggregate had one row at line 33290 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` had no type-material rows for `NCBITaxon:361077`.
- BacDive had 0 exact strain rows for `NCBITaxon:361077`.
- StrainInfo JSONL had 1 direct strain row and 1 exact deposit annotation for `NCBITaxon:361077`; the exact JSONL grep confirmed 1 direct row.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:361077`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:361077` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:361077` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
