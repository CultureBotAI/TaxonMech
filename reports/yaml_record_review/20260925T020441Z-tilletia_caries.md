# YAML Record Review: Tilletia caries

- Verdict: pass
- Target: `data/taxa/eukaryota/tilletia_caries.yaml`
- Identifier: `NCBITaxon:13290`

## Target

Reviewed the complete 81-line YAML record for Tilletia caries. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tilletia_caries.

## Validation

- `just validate data/taxa/eukaryota/tilletia_caries.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tiarina_fusus.yaml data/taxa/eukaryota/tieghemiomyces_parasiticus.yaml data/taxa/eukaryota/tieghemostelium_lacteum.yaml data/taxa/eukaryota/tilletia_caries.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 2674: `NCBITaxon:13290`, `Tilletia caries`, rank `SPECIES`, parent `NCBITaxon:13289`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:13290` at line 52121.
- NCBI synonym columns contained 2 exact synonyms, 0 broad synonyms, and 3 related synonyms, matching the five YAML synonym entries.
- The YAML lineage checked 12 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had one old ID, `NCBITaxon:61258`, redirecting to `NCBITaxon:13290`; the ignored-file-inclusive tab-bounded lookup found it only in `data/raw/ncbi_merged_ids.tsv`, not as a retained active row in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- The generated GOLD aggregate had one row at line 7994 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` had no type-material rows for `NCBITaxon:13290`.
- BacDive had 0 exact strain rows for `NCBITaxon:13290`.
- StrainInfo JSONL had 20 direct strain rows and 30 exact deposit annotations for `NCBITaxon:13290`; the exact JSONL grep confirmed 20 direct rows and found no non-direct strains carrying exact target deposits.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:13290`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:13290` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:13290` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
