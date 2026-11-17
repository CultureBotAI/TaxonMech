# YAML Record Review: Thraustotheca clavata

- Verdict: pass
- Target: `data/taxa/eukaryota/thraustotheca_clavata.yaml`
- Identifier: `NCBITaxon:74557`

## Target

Reviewed the complete 59-line YAML record for Thraustotheca clavata. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thraustotheca_clavata.

## Validation

- `just validate data/taxa/eukaryota/thraustotheca_clavata.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/thoracosphaera_heimii.yaml data/taxa/eukaryota/thraustochytrium_sp.yaml data/taxa/eukaryota/thraustotheca_clavata.yaml data/taxa/eukaryota/thyridium_curvatum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 10589: `NCBITaxon:74557`, `Thraustotheca clavata`, rank `SPECIES`, parent `NCBITaxon:74556`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:74557` at line 53267.
- NCBI synonym columns contained 0 exact synonyms, 0 broad synonyms, and 0 related synonyms, matching the YAML record's absence of a `synonyms` block.
- The YAML lineage checked 10 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:74557`.

## Evidence

- The generated GOLD aggregate had one row at line 42206 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 2 organism rows, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` had no type-material rows for `NCBITaxon:74557`.
- BacDive had 0 exact strain rows for `NCBITaxon:74557`.
- StrainInfo JSONL had 9 direct strain rows and 11 exact deposit annotations for `NCBITaxon:74557`; the exact JSONL grep confirmed 9 direct rows and found no non-direct strains carrying exact target deposits.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:74557`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:74557` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:74557` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
