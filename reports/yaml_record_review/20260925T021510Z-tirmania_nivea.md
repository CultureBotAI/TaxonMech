# YAML Record Review: Tirmania nivea

- Verdict: pass
- Target: `data/taxa/eukaryota/tirmania_nivea.yaml`
- Identifier: `NCBITaxon:160517`

## Target

Reviewed the complete 80-line YAML record for Tirmania nivea. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tirmania_nivea.

## Validation

- `just validate data/taxa/eukaryota/tirmania_nivea.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/timspurckia_oligopyrenoides.yaml data/taxa/eukaryota/tirmania_nivea.yaml data/taxa/eukaryota/togula_jolla.yaml data/taxa/eukaryota/tolypocladium_album.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 33115: `NCBITaxon:160517`, `Tirmania nivea`, rank `SPECIES`, parent `NCBITaxon:160516`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:160517` at line 54177.
- NCBI synonym columns contained 1 exact synonym, 0 broad synonyms, and 3 related synonyms, matching the four YAML synonym entries.
- The YAML lineage checked 13 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had one old ID, `NCBITaxon:1968060`, redirecting to `NCBITaxon:160517`; the ignored-file-inclusive tab-bounded lookup found it only in `data/raw/ncbi_merged_ids.tsv`, not as a retained active row in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- The generated GOLD aggregate had one row at line 12982 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 2 project rows, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` had no type-material rows for `NCBITaxon:160517`.
- BacDive had 0 exact strain rows for `NCBITaxon:160517`.
- StrainInfo JSONL had 0 direct strain rows and 0 exact deposit annotations for `NCBITaxon:160517`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:160517`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:160517` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:160517` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
