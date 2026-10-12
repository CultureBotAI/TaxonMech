# YAML Record Review: Tolypocladium inflatum NRRL8044

- Verdict: pass
- Target: `data/taxa/eukaryota/tolypocladium_inflatum_nrrl8044.yaml`
- Identifier: `NCBITaxon:1086729`

## Target

Reviewed the complete 80-line YAML record for Tolypocladium inflatum NRRL8044. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tolypocladium_inflatum_nrrl8044.

## Validation

- `just validate data/taxa/eukaryota/tolypocladium_inflatum_nrrl8044.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tolypocladium_geodes.yaml data/taxa/eukaryota/tolypocladium_guangdongense.yaml data/taxa/eukaryota/tolypocladium_inflatum_nrrl8044.yaml data/taxa/eukaryota/tolypocladium_nubicola.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 233755: `NCBITaxon:1086729`, `Tolypocladium inflatum NRRL8044`, rank `STRAIN`, parent `NCBITaxon:29910`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:1086729` at line 57570.
- NCBI synonym columns contained 0 exact synonyms, 0 broad synonyms, and 0 related synonyms, matching the YAML record's absence of a `synonyms` block.
- The YAML lineage checked 17 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:1086729`.

## Evidence

- The generated GOLD aggregate had one row at line 1594 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 2 project rows, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` had no type-material rows for `NCBITaxon:1086729`.
- BacDive had 0 exact strain rows for `NCBITaxon:1086729`.
- StrainInfo JSONL had 0 direct strain rows and 0 exact deposit annotations for `NCBITaxon:1086729`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1086729`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:1086729` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:1086729` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
