# YAML Record Review: Trichoderma atroviride

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_atroviride.yaml`
- Identifier: `NCBITaxon:63577`

## Target
Reviewed the complete 87-line YAML record for Trichoderma atroviride. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `trichoderma_atroviride`.

## Validation
- `just validate data/taxa/eukaryota/trichoderma_atroviride.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_atrobrunneum.yaml data/taxa/eukaryota/trichoderma_atroviride.yaml data/taxa/eukaryota/trichoderma_attinorum.yaml data/taxa/eukaryota/trichoderma_aureoviride.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 7989 retained `NCBITaxon:63577` as `Trichoderma atroviride` at rank `SPECIES`, with parent `NCBITaxon:5543`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:63577` on line 53057.
- The NCBI synonym columns supplied 1 exact synonym, 0 broad synonyms, and 2 related synonyms.
- All 16 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- `NCBITaxon:1641640`, `NCBITaxon:197014`, and `NCBITaxon:58857` occurred only as old identifiers merged into `NCBITaxon:63577` in `data/raw/ncbi_merged_ids.tsv`, and none was retained as a live YAML identifier.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:63577` on line 40131, matching the YAML aggregate with `organism_count` 7.
- Native GOLD carried 5 analysis rows, 6 organism rows, and 81 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 15 exact rows for `NCBITaxon:63577` across `GJS 98-134`, `NBRC 101776`, `BPI 748312`, `ATCC MYA- 2687`, `CBS 110086`, `NBRC 10177`, `CBS 142.95`, and `K(M) 161972` spellings.
- BacDive found 0 exact rows. StrainInfo found 64 direct strain rows and 82 deposit rows under `NCBITaxon:63577`; 64 of 69 compressed JSONL rows were assigned directly to the target, and the five remaining exact deposits occurred on SI 63457, SI 106200, SI 166050, SI 166055, and SI 183019 under non-target taxa.

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
