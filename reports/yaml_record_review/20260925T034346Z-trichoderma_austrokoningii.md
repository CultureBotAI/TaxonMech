# YAML Record Review: Trichoderma austrokoningii

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_austrokoningii.yaml`
- Identifier: `NCBITaxon:362043`

## Target
Reviewed the complete 87-line YAML record for Trichoderma austrokoningii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `trichoderma_austrokoningii`.

## Validation
- `just validate data/taxa/eukaryota/trichoderma_austrokoningii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_austrokoningii.yaml data/taxa/eukaryota/trichoderma_avellaneum.yaml data/taxa/eukaryota/trichoderma_balearicum.yaml data/taxa/eukaryota/trichoderma_bavaricum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 75363 retained `NCBITaxon:362043` as `Trichoderma austrokoningii` at rank `SPECIES`, with parent `NCBITaxon:5543`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:362043` on line 55359.
- The NCBI synonym columns supplied 1 exact synonym, 0 broad synonyms, and 2 related synonyms.
- All 16 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- No merged-ID rows were retained for `NCBITaxon:362043`.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:362043` on line 33311, matching the YAML aggregate with `organism_count` 1.
- Native GOLD carried 0 analysis rows, 1 organism row, and 2 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 11 exact rows for `NCBITaxon:362043` across `ICMP 16281`, `BPI 870962A`, `CBS 119092`, `GJS 99-146`, and `BPI 870962B` spellings.
- BacDive found 0 exact rows. StrainInfo found 4 direct strain rows and 4 deposit rows under `NCBITaxon:362043`, with all 4 compressed JSONL rows assigned directly to the target taxon.

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
