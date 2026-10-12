# YAML Record Review: Tilletia walkeri

- Verdict: pass
- Target: `data/taxa/eukaryota/tilletia_walkeri.yaml`
- Identifier: `NCBITaxon:117179`

## Target

Reviewed the complete 69-line YAML record for Tilletia walkeri. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tilletia_walkeri.

## Validation

- `just validate data/taxa/eukaryota/tilletia_walkeri.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tilletia_maclaganii.yaml data/taxa/eukaryota/tilletia_walkeri.yaml data/taxa/eukaryota/tilletiaria_anomala.yaml data/taxa/eukaryota/tilletiopsis_washingtonensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 21680: `NCBITaxon:117179`, `Tilletia walkeri`, rank `SPECIES`, parent `NCBITaxon:13289`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:117179` at line 53834.
- NCBI synonym columns contained 0 exact synonyms, 0 broad synonyms, and 1 related synonym, matching the single YAML synonym entry.
- The YAML lineage checked 12 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:117179`.

## Evidence

- The generated GOLD aggregate had one row at line 3695 with `organism_count` `2`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 2 organism rows, 2 project rows, and 2 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` had no type-material rows for `NCBITaxon:117179`.
- BacDive had 0 exact strain rows for `NCBITaxon:117179`.
- StrainInfo JSONL had 0 direct strain rows and 0 exact deposit annotations for `NCBITaxon:117179`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:117179`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:117179` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:117179` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
