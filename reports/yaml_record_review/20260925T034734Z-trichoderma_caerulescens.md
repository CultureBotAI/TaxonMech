# YAML Record Review: Trichoderma caerulescens

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_caerulescens.yaml`
- Identifier: `NCBITaxon:1490980`

## Target
Reviewed the complete 87-line YAML record for Trichoderma caerulescens. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `trichoderma_caerulescens`.

## Validation
- `just validate data/taxa/eukaryota/trichoderma_caerulescens.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_brevicompactum.yaml data/taxa/eukaryota/trichoderma_britannicum.yaml data/taxa/eukaryota/trichoderma_caerulescens.yaml data/taxa/eukaryota/trichoderma_caesareum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 381669 retained `NCBITaxon:1490980` as `Trichoderma caerulescens` at rank `SPECIES`, with parent `NCBITaxon:5543`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:1490980` on line 60271.
- The NCBI synonym columns supplied 1 exact synonym, 0 broad synonyms, and 2 related synonyms.
- All 16 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- `NCBITaxon:1169868` occurred only as an old identifier merged into `NCBITaxon:1490980` in `data/raw/ncbi_merged_ids.tsv`, and it was not retained as a live YAML identifier.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:1490980` on line 11563, matching the YAML aggregate with `organism_count` 1.
- Native GOLD carried 0 analysis rows, 0 organism rows, and 0 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 6 exact rows for `NCBITaxon:1490980` across `CBS 130011`, `S195`, and `WU 31600` spellings.
- BacDive found 0 exact rows. StrainInfo found 4 direct strain rows and 4 deposit rows under `NCBITaxon:1490980`, with all 4 compressed JSONL rows assigned directly to the target taxon.

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
