# YAML Record Review: Trichoderma brevicompactum

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_brevicompactum.yaml`
- Identifier: `NCBITaxon:247546`

## Target
Reviewed the complete 81-line YAML record for Trichoderma brevicompactum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `trichoderma_brevicompactum`.

## Validation
- `just validate data/taxa/eukaryota/trichoderma_brevicompactum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_brevicompactum.yaml data/taxa/eukaryota/trichoderma_britannicum.yaml data/taxa/eukaryota/trichoderma_caerulescens.yaml data/taxa/eukaryota/trichoderma_caesareum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 48600 retained `NCBITaxon:247546` as `Trichoderma brevicompactum` at rank `SPECIES`, with parent `NCBITaxon:5543`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:247546` on line 54749.
- The NCBI synonym columns supplied 0 exact synonyms, 0 broad synonyms, and 1 related synonym.
- All 16 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- No merged-ID rows were retained for `NCBITaxon:247546`.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:247546` on line 22188, matching the YAML aggregate with `organism_count` 2.
- Native GOLD carried 1 analysis row, 2 organism rows, and 3 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 9 exact rows for `NCBITaxon:247546` across `CBS 109720`, `DAOM 231232`, `TUB F-1076`, `MA 3296`, and `Prillinger MA 3296` spellings.
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
