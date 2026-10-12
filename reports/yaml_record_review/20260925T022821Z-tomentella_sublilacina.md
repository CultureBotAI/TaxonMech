# YAML Record Review: Tomentella sublilacina

- Verdict: pass
- Target: `data/taxa/eukaryota/tomentella_sublilacina.yaml`
- Identifier: `NCBITaxon:56497`

## Target

Reviewed the complete 78-line YAML record for Tomentella sublilacina. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tomentella_sublilacina.

## Validation

- `just validate data/taxa/eukaryota/tomentella_sublilacina.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tolypocladium_tundrense.yaml data/taxa/eukaryota/tomentella_sublilacina.yaml data/taxa/eukaryota/tomentellopsis_submollis.yaml data/taxa/eukaryota/torpedospora_radiata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 7123: `NCBITaxon:56497`, `Tomentella sublilacina`, rank `SPECIES`, parent `NCBITaxon:56494`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:56497` at line 52965.
- NCBI synonym columns contained 1 exact synonym, 0 broad synonyms, and 2 related synonyms, matching the three YAML synonym entries.
- The YAML lineage checked 13 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:56497`.

## Evidence

- The generated GOLD aggregate had one row at line 38962 with `organism_count` `2`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 0 organism rows, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` had no type-material rows for `NCBITaxon:56497`.
- BacDive had 0 exact strain rows for `NCBITaxon:56497`.
- StrainInfo JSONL had 0 direct strain rows and 0 exact deposit annotations for `NCBITaxon:56497`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:56497`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:56497` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:56497` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
