# YAML Record Review: Tothia fuscella

- Verdict: pass
- Target: `data/taxa/eukaryota/tothia_fuscella.yaml`
- Identifier: `NCBITaxon:1048955`

## Target
Reviewed the complete 87-line YAML record for Tothia fuscella. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `tothia_fuscella`.

## Validation
- `just validate data/taxa/eukaryota/tothia_fuscella.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/torulaspora_maleeae.yaml data/taxa/eukaryota/torulaspora_microellipsoides.yaml data/taxa/eukaryota/torulaspora_pretoriensis.yaml data/taxa/eukaryota/tothia_fuscella.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 225732 retained `NCBITaxon:1048955` as `Tothia fuscella` at rank `SPECIES`, with parent `NCBITaxon:1048954`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:1048955` on line 57380.
- The NCBI synonym columns supplied 1 exact synonym, 0 broad synonyms, and 2 related synonyms.
- All 16 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- No merged-ID rows were retained for `NCBITaxon:1048955`.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:1048955` on line 816, matching the YAML aggregate with `organism_count` 2.
- Native GOLD carried 1 analysis row, 1 organism row, and 2 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 2 exact rows for `NCBITaxon:1048955`: `WU31396` and `WU:31396`.
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
