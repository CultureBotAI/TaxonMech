# YAML Record Review: Torpedospora radiata

- Verdict: pass
- Target: `data/taxa/eukaryota/torpedospora_radiata.yaml`
- Identifier: `NCBITaxon:311114`

## Target

Reviewed the complete 81-line YAML record for Torpedospora radiata. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for torpedospora_radiata.

## Validation

- `just validate data/taxa/eukaryota/torpedospora_radiata.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tolypocladium_tundrense.yaml data/taxa/eukaryota/tomentella_sublilacina.yaml data/taxa/eukaryota/tomentellopsis_submollis.yaml data/taxa/eukaryota/torpedospora_radiata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 63702: `NCBITaxon:311114`, `Torpedospora radiata`, rank `SPECIES`, parent `NCBITaxon:311111`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:311114` at line 55131.
- NCBI synonym columns contained 0 exact synonyms, 0 broad synonyms, and 1 related synonym, matching the single YAML synonym entry.
- The YAML lineage checked 16 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:311114`.

## Evidence

- The generated GOLD aggregate had one row at line 31392 with `organism_count` `2`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 16 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` had no type-material rows for `NCBITaxon:311114`.
- BacDive had 0 exact strain rows for `NCBITaxon:311114`.
- StrainInfo JSONL had 9 direct strain rows and 12 exact deposit annotations for `NCBITaxon:311114`; the exact JSONL grep confirmed 9 direct rows and found no non-direct strains carrying exact target deposits.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:311114`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:311114` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:311114` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
