# YAML Record Review: Tieghemiomyces parasiticus

- Verdict: pass
- Target: `data/taxa/eukaryota/tieghemiomyces_parasiticus.yaml`
- Identifier: `NCBITaxon:78921`

## Target

Reviewed the complete 69-line YAML record for Tieghemiomyces parasiticus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tieghemiomyces_parasiticus.

## Validation

- `just validate data/taxa/eukaryota/tieghemiomyces_parasiticus.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/tiarina_fusus.yaml data/taxa/eukaryota/tieghemiomyces_parasiticus.yaml data/taxa/eukaryota/tieghemostelium_lacteum.yaml data/taxa/eukaryota/tilletia_caries.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 11554: `NCBITaxon:78921`, `Tieghemiomyces parasiticus`, rank `SPECIES`, parent `NCBITaxon:78920`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:78921` at line 53333.
- NCBI synonym columns contained 0 exact synonyms, 0 broad synonyms, and 1 related synonym, matching the single YAML synonym entry.
- The YAML lineage checked 12 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had no old IDs redirecting to `NCBITaxon:78921`.

## Evidence

- The generated GOLD aggregate had one row at line 42763 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` had eight exact type-material rows for `NCBITaxon:78921`: `ATCC 14298`, `ATCC:14298`, `CBS 437.61`, `CBS:437.61`, `IMI 087268`, `IMI:087268`, `RSA 861`, and `RSA:861`.
- BacDive had 0 exact strain rows for `NCBITaxon:78921`.
- StrainInfo JSONL had 4 direct strain rows and 7 exact deposit annotations for `NCBITaxon:78921`; the exact JSONL grep confirmed 4 direct rows and found no non-direct strains carrying exact target deposits.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:78921`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:78921` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:78921` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
