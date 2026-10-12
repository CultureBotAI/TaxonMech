# YAML Record Review: Tolypocladium geodes

- Verdict: pass
- Target: `data/taxa/eukaryota/tolypocladium_geodes.yaml`
- Identifier: `NCBITaxon:38000`

## Target

Reviewed the complete 84-line YAML record for Tolypocladium geodes. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tolypocladium_geodes.

## Validation

- `just validate data/taxa/eukaryota/tolypocladium_geodes.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tolypocladium_geodes.yaml data/taxa/eukaryota/tolypocladium_guangdongense.yaml data/taxa/eukaryota/tolypocladium_inflatum_nrrl8044.yaml data/taxa/eukaryota/tolypocladium_nubicola.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 4314: `NCBITaxon:38000`, `Tolypocladium geodes`, rank `SPECIES`, parent `NCBITaxon:29909`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:38000` at line 52380.
- NCBI synonym columns contained 1 exact synonym, 0 broad synonyms, and 1 related synonym, matching the two YAML synonym entries.
- The YAML lineage checked 16 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:38000`.

## Evidence

- The generated GOLD aggregate had one row at line 33856 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` had two exact type-material rows for `NCBITaxon:38000`: `CBS 723.70` and `CBS:723.70`.
- BacDive had 0 exact strain rows for `NCBITaxon:38000`.
- StrainInfo JSONL had 13 direct strain rows and 16 exact deposit annotations for `NCBITaxon:38000`; the exact JSONL grep confirmed 13 direct rows and found no non-direct strains carrying exact target deposits.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:38000`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:38000` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:38000` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
