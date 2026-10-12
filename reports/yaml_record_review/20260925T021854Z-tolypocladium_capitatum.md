# YAML Record Review: Tolypocladium capitatum

- Verdict: pass
- Target: `data/taxa/eukaryota/tolypocladium_capitatum.yaml`
- Identifier: `NCBITaxon:45235`

## Target

Reviewed the complete 97-line YAML record for Tolypocladium capitatum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tolypocladium_capitatum.

## Validation

- `just validate data/taxa/eukaryota/tolypocladium_capitatum.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tolypocladium_amazonense.yaml data/taxa/eukaryota/tolypocladium_capitatum.yaml data/taxa/eukaryota/tolypocladium_cylindrosporum.yaml data/taxa/eukaryota/tolypocladium_endophyticum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 5509: `NCBITaxon:45235`, `Tolypocladium capitatum`, rank `SPECIES`, parent `NCBITaxon:29909`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:45235` at line 52608.
- NCBI synonym columns contained 4 exact synonyms, 0 broad synonyms, and 2 related synonyms, matching the six YAML synonym entries.
- The YAML lineage checked 16 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:45235`.

## Evidence

- The generated GOLD aggregate had one row at line 35891 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` had no type-material rows for `NCBITaxon:45235`.
- BacDive had 0 exact strain rows for `NCBITaxon:45235`.
- StrainInfo JSONL had 1 direct strain row and 1 exact deposit annotation for `NCBITaxon:45235`; the exact JSONL grep confirmed 1 direct row.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:45235`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:45235` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:45235` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
