# YAML Record Review: Tilletia controversa

- Verdict: pass
- Target: `data/taxa/eukaryota/tilletia_controversa.yaml`
- Identifier: `NCBITaxon:13291`

## Target

Reviewed the complete 72-line YAML record for Tilletia controversa. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tilletia_controversa.

## Validation

- `just validate data/taxa/eukaryota/tilletia_controversa.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tilletia_controversa.yaml data/taxa/eukaryota/tilletia_horrida.yaml data/taxa/eukaryota/tilletia_indica.yaml data/taxa/eukaryota/tilletia_laevis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 2675: `NCBITaxon:13291`, `Tilletia controversa`, rank `SPECIES`, parent `NCBITaxon:13289`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:13291` at line 52122.
- NCBI synonym columns contained 1 exact synonym, 0 broad synonyms, and 1 related synonym, matching the two YAML synonym entries.
- The YAML lineage checked 12 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:13291`.

## Evidence

- The generated GOLD aggregate had one row at line 7995 with `organism_count` `2`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 2 organism rows, 2 project rows, and 2 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` had no type-material rows for `NCBITaxon:13291`.
- BacDive had 0 exact strain rows for `NCBITaxon:13291`.
- StrainInfo JSONL had 1 direct strain row and 1 exact deposit annotation for `NCBITaxon:13291`; the exact JSONL grep confirmed 1 direct row.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:13291`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:13291` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:13291` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
