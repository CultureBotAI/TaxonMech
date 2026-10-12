# YAML Record Review: Trametopsis cervina

- Verdict: pass
- Target: `data/taxa/eukaryota/trametopsis_cervina.yaml`
- Identifier: `NCBITaxon:1111950`

## Target
Reviewed the complete 108-line YAML record for Trametopsis cervina. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `trametopsis_cervina`.

## Validation
- `just validate data/taxa/eukaryota/trametopsis_cervina.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trametopsis_cervina.yaml data/taxa/eukaryota/trematosphaeria_pertusa.yaml data/taxa/eukaryota/tremella_fuciformis.yaml data/taxa/eukaryota/tremella_mesenterica_atcc28783.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 238939 retained `NCBITaxon:1111950` as `Trametopsis cervina` at rank `SPECIES`, with parent `NCBITaxon:1111949`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:1111950` on line 57673.
- The NCBI synonym columns supplied 11 exact synonyms, 0 broad synonyms, and 2 related synonyms.
- All 13 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- `NCBITaxon:295351` occurred only as an old identifier merged into `NCBITaxon:1111950` in `data/raw/ncbi_merged_ids.tsv`, and it was not retained as a live YAML identifier.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:1111950` on line 2017, matching the YAML aggregate with `organism_count` 2.
- Native GOLD carried 0 analysis rows, 1 organism row, and 2 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 0 exact rows for `NCBITaxon:1111950`.
- BacDive and StrainInfo exact scans found 0 matching rows.

## Completeness
- Generated strain tables had 0 target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source tables had 0 target rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlays had 0 target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
No YAML edits were made; this report records the read-only evidence review.
