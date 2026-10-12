# YAML Record Review: Tolypocladium guangdongense

- Verdict: pass
- Target: `data/taxa/eukaryota/tolypocladium_guangdongense.yaml`
- Identifier: `NCBITaxon:2730933`

## Target

Reviewed the complete 91-line YAML record for Tolypocladium guangdongense. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tolypocladium_guangdongense.

## Validation

- `just validate data/taxa/eukaryota/tolypocladium_guangdongense.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tolypocladium_geodes.yaml data/taxa/eukaryota/tolypocladium_guangdongense.yaml data/taxa/eukaryota/tolypocladium_inflatum_nrrl8044.yaml data/taxa/eukaryota/tolypocladium_nubicola.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 548293: `NCBITaxon:2730933`, `Tolypocladium guangdongense`, rank `SPECIES`, parent `NCBITaxon:29909`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:2730933` at line 63002.
- NCBI synonym columns contained 1 exact synonym, 0 broad synonyms, and 3 related synonyms, matching the four YAML synonym entries.
- The YAML lineage checked 16 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had one old ID, `NCBITaxon:475933`, redirecting to `NCBITaxon:2730933`; the ignored-file-inclusive tab-bounded lookup found it only in `data/raw/ncbi_merged_ids.tsv`, not as a retained active row in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- The generated GOLD aggregate had one row at line 25440 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` had four exact type-material rows for `NCBITaxon:2730933`: `GDGM 24020`, `GDGM-24020`, `GDGM24020`, and `GDGM:24020`.
- BacDive had 0 exact strain rows for `NCBITaxon:2730933`.
- StrainInfo JSONL had 0 direct strain rows and 0 exact deposit annotations for `NCBITaxon:2730933`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:2730933`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:2730933` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:2730933` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
