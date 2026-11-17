# YAML Record Review: Tortispora caseinolytica

- Verdict: pass
- Target: `data/taxa/eukaryota/tortispora_caseinolytica.yaml`
- Identifier: `NCBITaxon:51930`

## Target

Reviewed the complete 87-line YAML record for Tortispora caseinolytica. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tortispora_caseinolytica.

## Validation

- `just validate data/taxa/eukaryota/tortispora_caseinolytica.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/torrubiella_hemipterigena.yaml data/taxa/eukaryota/tortispora_agaves.yaml data/taxa/eukaryota/tortispora_caseinolytica.yaml data/taxa/eukaryota/tortispora_ganteri.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 6536: `NCBITaxon:51930`, `Tortispora caseinolytica`, rank `SPECIES`, parent `NCBITaxon:1540147`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:51930` at line 52853.
- NCBI synonym columns contained 1 exact synonym, 0 broad synonyms, and 5 related synonyms, matching the six YAML synonym entries.
- The YAML lineage checked 13 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had three old IDs, `NCBITaxon:1326885`, `NCBITaxon:1326886`, and `NCBITaxon:1326891`, redirecting to `NCBITaxon:51930`; the ignored-file-inclusive tab-bounded lookup found all three only in `data/raw/ncbi_merged_ids.tsv`, not as retained active rows in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- The generated GOLD aggregate had one row at line 37695 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 2 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` had 13 exact type-material rows for `NCBITaxon:51930`: `ATCC 90546`, `ATCC:90546`, `CBS 7781`, `CBS:7781`, `NCYC 2634`, `NCYC:2634`, `NRRL Y-17796`, `NRRL:Y-17796`, `NRRL:Y:17796`, `UCD 83-438.3`, `UCD-FST 83-438.3`, `UCD-FST:83-438.3`, and `UCD:83-438.3`.
- BacDive had 0 exact strain rows for `NCBITaxon:51930`.
- StrainInfo JSONL had 7 direct strain rows and 14 exact deposit annotations for `NCBITaxon:51930`; the exact JSONL grep confirmed 7 direct rows and found no non-direct strains carrying exact target deposits.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:51930`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:51930` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:51930` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
