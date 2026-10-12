# YAML Record Review: Tolypocladium paradoxum

- Verdict: pass
- Target: `data/taxa/eukaryota/tolypocladium_paradoxum.yaml`
- Identifier: `NCBITaxon:94208`

## Target

Reviewed the complete 90-line YAML record for Tolypocladium paradoxum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tolypocladium_paradoxum.

## Validation

- `just validate data/taxa/eukaryota/tolypocladium_paradoxum.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tolypocladium_ovalisporum.yaml data/taxa/eukaryota/tolypocladium_paradoxum.yaml data/taxa/eukaryota/tolypocladium_pustulatum.yaml data/taxa/eukaryota/tolypocladium_tropicale.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 15613: `NCBITaxon:94208`, `Tolypocladium paradoxum`, rank `SPECIES`, parent `NCBITaxon:29909`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:94208` at line 53551.
- NCBI synonym columns contained 2 exact synonyms, 0 broad synonyms, and 2 related synonyms, matching the four YAML synonym entries.
- The YAML lineage checked 16 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:94208`.

## Evidence

- The generated GOLD aggregate had one row at line 44965 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` had no type-material rows for `NCBITaxon:94208`.
- BacDive had 0 exact strain rows for `NCBITaxon:94208`.
- StrainInfo JSONL had 1 direct strain row and 1 exact deposit annotation for `NCBITaxon:94208`; the exact JSONL grep confirmed 1 direct row.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:94208`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:94208` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:94208` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
