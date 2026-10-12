# YAML Record Review: Timspurckia oligopyrenoides

- Verdict: pass
- Target: `data/taxa/eukaryota/timspurckia_oligopyrenoides.yaml`
- Identifier: `NCBITaxon:708627`

## Target

Reviewed the complete 60-line YAML record for Timspurckia oligopyrenoides. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for timspurckia_oligopyrenoides.

## Validation

- `just validate data/taxa/eukaryota/timspurckia_oligopyrenoides.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/timspurckia_oligopyrenoides.yaml data/taxa/eukaryota/tirmania_nivea.yaml data/taxa/eukaryota/togula_jolla.yaml data/taxa/eukaryota/tolypocladium_album.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 165697: `NCBITaxon:708627`, `Timspurckia oligopyrenoides`, rank `SPECIES`, parent `NCBITaxon:983317`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:708627` at line 56518.
- NCBI synonym columns contained 0 exact synonyms, 0 broad synonyms, and 2 related synonyms, matching the two YAML synonym entries.
- The YAML lineage checked 8 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:708627`.

## Evidence

- The generated GOLD aggregate had one row at line 41759 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` had no type-material rows for `NCBITaxon:708627`.
- BacDive had 0 exact strain rows for `NCBITaxon:708627`.
- StrainInfo JSONL had 0 direct strain rows and 0 exact deposit annotations for `NCBITaxon:708627`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:708627`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:708627` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:708627` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
