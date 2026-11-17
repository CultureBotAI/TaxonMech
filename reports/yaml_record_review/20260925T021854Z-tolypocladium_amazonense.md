# YAML Record Review: Tolypocladium amazonense

- Verdict: pass
- Target: `data/taxa/eukaryota/tolypocladium_amazonense.yaml`
- Identifier: `NCBITaxon:1436175`

## Target

Reviewed the complete 84-line YAML record for Tolypocladium amazonense. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tolypocladium_amazonense.

## Validation

- `just validate data/taxa/eukaryota/tolypocladium_amazonense.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tolypocladium_amazonense.yaml data/taxa/eukaryota/tolypocladium_capitatum.yaml data/taxa/eukaryota/tolypocladium_cylindrosporum.yaml data/taxa/eukaryota/tolypocladium_endophyticum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 359248: `NCBITaxon:1436175`, `Tolypocladium amazonense`, rank `SPECIES`, parent `NCBITaxon:29909`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:1436175` at line 60117.
- NCBI synonym columns contained 0 exact synonyms, 0 broad synonyms, and 2 related synonyms, matching the two YAML synonym entries.
- The YAML lineage checked 16 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:1436175`.

## Evidence

- The generated GOLD aggregate had one row at line 10397 with `organism_count` `2`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 2 organism rows, 2 project rows, and 2 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` had six exact type-material rows for `NCBITaxon:1436175`: `CBS 136895`, `CBS:136895`, `MS308`, `MS:308`, `BPI 892889`, and `BPI:892889`.
- BacDive had 0 exact strain rows for `NCBITaxon:1436175`.
- StrainInfo JSONL had 0 direct strain rows and 0 exact deposit annotations for `NCBITaxon:1436175`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1436175`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:1436175` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:1436175` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
