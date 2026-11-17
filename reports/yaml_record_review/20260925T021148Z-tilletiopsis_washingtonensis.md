# YAML Record Review: Tilletiopsis washingtonensis

- Verdict: pass
- Target: `data/taxa/eukaryota/tilletiopsis_washingtonensis.yaml`
- Identifier: `NCBITaxon:58919`

## Target

Reviewed the complete 69-line YAML record for Tilletiopsis washingtonensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tilletiopsis_washingtonensis.

## Validation

- `just validate data/taxa/eukaryota/tilletiopsis_washingtonensis.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tilletia_maclaganii.yaml data/taxa/eukaryota/tilletia_walkeri.yaml data/taxa/eukaryota/tilletiaria_anomala.yaml data/taxa/eukaryota/tilletiopsis_washingtonensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 7445: `NCBITaxon:58919`, `Tilletiopsis washingtonensis`, rank `SPECIES`, parent `NCBITaxon:1500560`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:58919` at line 53001.
- NCBI synonym columns contained 0 exact synonyms, 0 broad synonyms, and 1 related synonym, matching the single YAML synonym entry.
- The YAML lineage checked 12 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had two old IDs, `NCBITaxon:84743` and `NCBITaxon:84744`, redirecting to `NCBITaxon:58919`; the ignored-file-inclusive tab-bounded lookup found both only in `data/raw/ncbi_merged_ids.tsv`, not as retained active rows in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- The generated GOLD aggregate had one row at line 39578 with `organism_count` `8`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 7 organism rows, 2 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` had six exact type-material rows for `NCBITaxon:58919`: `ATCC 36489`, `ATCC:36489`, `CBS 544.50`, `CBS:544.50`, `JCM 8362`, and `JCM:8362`.
- BacDive had 0 exact strain rows for `NCBITaxon:58919`.
- StrainInfo JSONL had 24 direct strain rows and 39 exact deposit annotations for `NCBITaxon:58919`; the exact JSONL grep found 27 records, including three non-direct rows carrying exact target deposits under `NCBITaxon:58915` and `NCBITaxon:88838`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:58919`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:58919` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:58919` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
