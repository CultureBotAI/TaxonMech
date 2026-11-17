# YAML Record Review: Trichoderma attinorum

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_attinorum.yaml`
- Identifier: `NCBITaxon:1684291`

## Target
Reviewed the complete 85-line YAML record for Trichoderma attinorum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `trichoderma_attinorum`.

## Validation
- `just validate data/taxa/eukaryota/trichoderma_attinorum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_atrobrunneum.yaml data/taxa/eukaryota/trichoderma_atroviride.yaml data/taxa/eukaryota/trichoderma_attinorum.yaml data/taxa/eukaryota/trichoderma_aureoviride.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 439934 retained `NCBITaxon:1684291` as `Trichoderma attinorum` at rank `SPECIES`, with parent `NCBITaxon:5543`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:1684291` on line 61020.
- The NCBI synonym columns supplied 0 exact synonyms, 0 broad synonyms, and 2 related synonyms.
- All 16 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- No merged-ID rows were retained for `NCBITaxon:1684291`.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:1684291` on line 14522, matching the YAML aggregate with `organism_count` 1.
- Native GOLD carried 0 analysis rows, 0 organism rows, and 0 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 6 exact rows for `NCBITaxon:1684291` across `CBMAI 1826`, `CBS 139783`, and `LESF 236` spellings.
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
