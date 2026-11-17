# YAML Record Review: Trichoderma amazonicum

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_amazonicum.yaml`
- Identifier: `NCBITaxon:860960`

## Target
Reviewed the complete 77-line YAML record for Trichoderma amazonicum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `trichoderma_amazonicum`.

## Validation
- `just validate data/taxa/eukaryota/trichoderma_amazonicum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_alcalifuscescens.yaml data/taxa/eukaryota/trichoderma_alni.yaml data/taxa/eukaryota/trichoderma_amazonicum.yaml data/taxa/eukaryota/trichoderma_americanum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 180949 retained `NCBITaxon:860960` as `Trichoderma amazonicum` at rank `SPECIES`, with parent `NCBITaxon:5543`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:860960` on line 56789.
- The NCBI synonym columns supplied 0 exact synonyms, 0 broad synonyms, and 0 related synonyms.
- All 16 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- No merged-ID rows were retained for `NCBITaxon:860960`.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:860960` on line 43368, matching the YAML aggregate with `organism_count` 1.
- Native GOLD carried 0 analysis rows, 1 organism row, and 2 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 7 exact rows for `NCBITaxon:860960` across `CBS 126898`, `IB 50`, and `BPI 880413` spellings.
- BacDive and StrainInfo exact scans found 0 matching rows.

## Completeness
- Generated strain tables had 0 target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source tables had 0 target rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlays had 0 target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
No YAML edits were made; this report records the read-only evidence review.
