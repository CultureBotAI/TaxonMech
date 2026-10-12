# YAML Record Review: Tremella yokohamensis

- Verdict: pass
- Target: `data/taxa/eukaryota/tremella_yokohamensis.yaml`
- Identifier: `NCBITaxon:1758741`

## Target
Reviewed the complete 81-line YAML record for Tremella yokohamensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `tremella_yokohamensis`.

## Validation
- `just validate data/taxa/eukaryota/tremella_yokohamensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/tremella_yokohamensis.yaml data/taxa/eukaryota/triangularia_allahabadensis.yaml data/taxa/eukaryota/triangularia_phialophoroides.yaml data/taxa/eukaryota/triangularia_setosa.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 459209 retained `NCBITaxon:1758741` as `Tremella yokohamensis` at rank `SPECIES`, with parent `NCBITaxon:105767`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:1758741` on line 61225.
- The NCBI synonym columns supplied 1 exact synonym, 0 broad synonyms, and 4 related synonyms.
- All 12 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- `NCBITaxon:1762056` and `NCBITaxon:859626` occurred only as old identifiers merged into `NCBITaxon:1758741` in `data/raw/ncbi_merged_ids.tsv`, and neither was retained as a live YAML identifier.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:1758741` on line 15310, matching the YAML aggregate with `organism_count` 5.
- Native GOLD carried 0 analysis rows, 5 organism rows, and 0 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 10 exact rows for `NCBITaxon:1758741` across `VLA M-11700`, `CBS 11776`, `DSM 23671`, `JCM 16989`, and `TIMM 10001` spellings.
- BacDive found 0 exact rows. StrainInfo found 1 direct strain row and 1 deposit row under `NCBITaxon:1758741`, with the compressed JSONL row assigned directly to the target taxon.

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
