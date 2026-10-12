# YAML Record Review: Thoracosphaera heimii

- Verdict: pass
- Target: `data/taxa/eukaryota/thoracosphaera_heimii.yaml`
- Identifier: `NCBITaxon:2923`

## Target

Reviewed the complete 63-line YAML record for Thoracosphaera heimii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thoracosphaera_heimii.

## Validation

- `just validate data/taxa/eukaryota/thoracosphaera_heimii.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/thoracosphaera_heimii.yaml data/taxa/eukaryota/thraustochytrium_sp.yaml data/taxa/eukaryota/thraustotheca_clavata.yaml data/taxa/eukaryota/thyridium_curvatum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 1991: `NCBITaxon:2923`, `Thoracosphaera heimii`, rank `SPECIES`, parent `NCBITaxon:2922`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:2923` at line 51819.
- NCBI synonym columns contained 1 exact synonym, 0 broad synonyms, and 1 related synonym, matching the two YAML synonym entries.
- The YAML lineage checked 9 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:2923`.

## Evidence

- The generated GOLD aggregate had one row at line 28741 with `organism_count` `2`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` had no type-material rows for `NCBITaxon:2923`.
- BacDive had 0 exact strain rows for `NCBITaxon:2923`.
- StrainInfo JSONL had 8 direct strain rows and 8 exact deposit annotations for `NCBITaxon:2923`; the exact JSONL grep confirmed 8 direct rows.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:2923`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:2923` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:2923` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
