# YAML Record Review: Thraustochytrium sp.

- Verdict: pass
- Target: `data/taxa/eukaryota/thraustochytrium_sp.yaml`
- Identifier: `NCBITaxon:145168`

## Target

Reviewed the complete 66-line YAML record for Thraustochytrium sp. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thraustochytrium_sp.

## Validation

- `just validate data/taxa/eukaryota/thraustochytrium_sp.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/thoracosphaera_heimii.yaml data/taxa/eukaryota/thraustochytrium_sp.yaml data/taxa/eukaryota/thraustotheca_clavata.yaml data/taxa/eukaryota/thyridium_curvatum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 29462: `NCBITaxon:145168`, `Thraustochytrium sp.`, rank `SPECIES`, parent `NCBITaxon:1299920`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:145168` at line 54028.
- NCBI synonym columns contained 0 exact synonyms, 0 broad synonyms, and 1 related synonym, matching the single YAML synonym entry.
- The YAML lineage checked 11 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:145168`.

## Evidence

- The generated GOLD aggregate had one row at line 10979 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` had no type-material rows for `NCBITaxon:145168`.
- BacDive had 0 exact strain rows for `NCBITaxon:145168`.
- StrainInfo JSONL had 0 direct strain rows and 0 exact deposit annotations for `NCBITaxon:145168`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:145168`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:145168` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:145168` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
