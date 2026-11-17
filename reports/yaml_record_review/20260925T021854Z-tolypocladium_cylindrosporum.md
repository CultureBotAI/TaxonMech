# YAML Record Review: Tolypocladium cylindrosporum

- Verdict: pass
- Target: `data/taxa/eukaryota/tolypocladium_cylindrosporum.yaml`
- Identifier: `NCBITaxon:38005`

## Target

Reviewed the complete 84-line YAML record for Tolypocladium cylindrosporum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tolypocladium_cylindrosporum.

## Validation

- `just validate data/taxa/eukaryota/tolypocladium_cylindrosporum.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tolypocladium_amazonense.yaml data/taxa/eukaryota/tolypocladium_capitatum.yaml data/taxa/eukaryota/tolypocladium_cylindrosporum.yaml data/taxa/eukaryota/tolypocladium_endophyticum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 4317: `NCBITaxon:38005`, `Tolypocladium cylindrosporum`, rank `SPECIES`, parent `NCBITaxon:29909`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:38005` at line 52383.
- NCBI synonym columns contained 1 exact synonym, 0 broad synonyms, and 1 related synonym, matching the two YAML synonym entries.
- The YAML lineage checked 16 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had one old ID, `NCBITaxon:73500`, redirecting to `NCBITaxon:38005`; the ignored-file-inclusive tab-bounded lookup found it only in `data/raw/ncbi_merged_ids.tsv`, not as a retained active row in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- The generated GOLD aggregate had one row at line 33863 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` had six exact type-material rows for `NCBITaxon:38005`: `ARSEF 2920`, `ARSEF:2920`, `CBS 718.70`, `CBS:718.70`, `LCP 88.3553`, and `LCP:88.3553`.
- BacDive had 0 exact strain rows for `NCBITaxon:38005`.
- StrainInfo JSONL had 36 direct strain rows and 44 exact deposit annotations for `NCBITaxon:38005`; the exact JSONL grep confirmed 36 direct rows and found no non-direct strains carrying exact target deposits.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:38005`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:38005` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:38005` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
