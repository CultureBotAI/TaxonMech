# YAML Record Review: Trichoderma asperellum

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_asperellum.yaml`
- Identifier: `NCBITaxon:101201`

## Target
Reviewed the complete 84-line YAML record for Trichoderma asperellum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `trichoderma_asperellum`.

## Validation
- `just validate data/taxa/eukaryota/trichoderma_asperellum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_appalachiense.yaml data/taxa/eukaryota/trichoderma_arundinaceum.yaml data/taxa/eukaryota/trichoderma_asperelloides.yaml data/taxa/eukaryota/trichoderma_asperellum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 17470 retained `NCBITaxon:101201` as `Trichoderma asperellum` at rank `SPECIES`, with parent `NCBITaxon:5543`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:101201` on line 53657.
- The NCBI synonym columns supplied 0 exact synonyms, 0 broad synonyms, and 2 related synonyms.
- All 16 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- No merged-ID rows were retained for `NCBITaxon:101201`.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:101201` on line 270, matching the YAML aggregate with `organism_count` 6.
- Native GOLD carried 3 analysis rows, 4 organism rows, and 5 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 4 exact rows for `NCBITaxon:101201` across `CBS 433.97` and `BPI 746504` spellings.
- BacDive found 0 exact rows. StrainInfo found 21 direct strain rows and 25 deposit rows under `NCBITaxon:101201`, with all 21 compressed JSONL rows assigned directly to the target taxon.

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
