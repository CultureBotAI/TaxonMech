# YAML Record Review: Tolypocladium ovalisporum

- Verdict: pass
- Target: `data/taxa/eukaryota/tolypocladium_ovalisporum.yaml`
- Identifier: `NCBITaxon:557785`

## Target

Reviewed the complete 88-line YAML record for Tolypocladium ovalisporum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tolypocladium_ovalisporum.

## Validation

- `just validate data/taxa/eukaryota/tolypocladium_ovalisporum.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tolypocladium_ovalisporum.yaml data/taxa/eukaryota/tolypocladium_paradoxum.yaml data/taxa/eukaryota/tolypocladium_pustulatum.yaml data/taxa/eukaryota/tolypocladium_tropicale.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 130889: `NCBITaxon:557785`, `Tolypocladium ovalisporum`, rank `SPECIES`, parent `NCBITaxon:29909`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:557785` at line 56029.
- NCBI synonym columns contained 1 exact synonym, 0 broad synonyms, and 2 related synonyms, matching the three YAML synonym entries.
- The YAML lineage checked 16 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:557785`.

## Evidence

- The generated GOLD aggregate had one row at line 38771 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` had two exact type-material rows for `NCBITaxon:557785`: `CBS 700.92` and `CBS:700.92`.
- BacDive had 0 exact strain rows for `NCBITaxon:557785`.
- StrainInfo JSONL had 2 direct strain rows and 3 exact deposit annotations for `NCBITaxon:557785`; the exact JSONL grep confirmed 2 direct rows and found no non-direct strains carrying exact target deposits.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:557785`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:557785` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:557785` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
