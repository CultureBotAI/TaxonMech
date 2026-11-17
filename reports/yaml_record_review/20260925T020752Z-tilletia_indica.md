# YAML Record Review: Tilletia indica

- Verdict: pass
- Target: `data/taxa/eukaryota/tilletia_indica.yaml`
- Identifier: `NCBITaxon:43049`

## Target

Reviewed the complete 78-line YAML record for Tilletia indica. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tilletia_indica.

## Validation

- `just validate data/taxa/eukaryota/tilletia_indica.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tilletia_controversa.yaml data/taxa/eukaryota/tilletia_horrida.yaml data/taxa/eukaryota/tilletia_indica.yaml data/taxa/eukaryota/tilletia_laevis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 5195: `NCBITaxon:43049`, `Tilletia indica`, rank `SPECIES`, parent `NCBITaxon:13289`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:43049` at line 52534.
- NCBI synonym columns contained 1 exact synonym, 0 broad synonyms, and 3 related synonyms, matching the four YAML synonym entries.
- The YAML lineage checked 12 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:43049`.

## Evidence

- The generated GOLD aggregate had one row at line 35281 with `organism_count` `7`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 7 organism rows, 7 project rows, and 7 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` had no type-material rows for `NCBITaxon:43049`.
- BacDive had 0 exact strain rows for `NCBITaxon:43049`.
- StrainInfo JSONL had 1 direct strain row and 1 exact deposit annotation for `NCBITaxon:43049`; the exact JSONL grep confirmed 1 direct row.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:43049`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:43049` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:43049` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
