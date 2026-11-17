# YAML Record Review: Tribonema aequale

- Verdict: pass
- Target: `data/taxa/eukaryota/tribonema_aequale.yaml`
- Identifier: `NCBITaxon:2981`

## Target
Reviewed the complete 66-line YAML record for Tribonema aequale. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `tribonema_aequale`.

## Validation
- `just validate data/taxa/eukaryota/tribonema_aequale.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/triangularia_tetraspora.yaml data/taxa/eukaryota/triangularia_verruculosa.yaml data/taxa/eukaryota/tribonema_aequale.yaml data/taxa/eukaryota/tribonema_minus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 2018 retained `NCBITaxon:2981` as `Tribonema aequale` at rank `SPECIES`, with parent `NCBITaxon:2980`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:2981` on line 51830.
- The NCBI synonym columns supplied 0 exact synonyms, 0 broad synonyms, and 1 related synonym.
- All 11 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- No merged-ID rows were retained for `NCBITaxon:2981`.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:2981` on line 29775, matching the YAML aggregate with `organism_count` 1.
- Native GOLD carried 0 analysis rows, 1 organism row, and 1 project row for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 0 exact rows for `NCBITaxon:2981`.
- BacDive found 0 exact rows. StrainInfo found 2 direct strain rows and 6 deposit rows under `NCBITaxon:2981`, with both compressed JSONL rows assigned directly to the target taxon.

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
