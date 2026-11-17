# YAML Record Review: Triangularia setosa

- Verdict: pass
- Target: `data/taxa/eukaryota/triangularia_setosa.yaml`
- Identifier: `NCBITaxon:2587417`

## Target
Reviewed the complete 96-line YAML record for Triangularia setosa. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `triangularia_setosa`.

## Validation
- `just validate data/taxa/eukaryota/triangularia_setosa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/tremella_yokohamensis.yaml data/taxa/eukaryota/triangularia_allahabadensis.yaml data/taxa/eukaryota/triangularia_phialophoroides.yaml data/taxa/eukaryota/triangularia_setosa.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 534332 retained `NCBITaxon:2587417` as `Triangularia setosa` at rank `SPECIES`, with parent `NCBITaxon:252192`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:2587417` on line 62865.
- The NCBI synonym columns supplied 2 exact synonyms, 0 broad synonyms, and 4 related synonyms.
- All 16 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- `NCBITaxon:179329` occurred only as an old identifier merged into `NCBITaxon:2587417` in `data/raw/ncbi_merged_ids.tsv`, and it was not retained as a live YAML identifier.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:2587417` on line 23681, matching the YAML aggregate with `organism_count` 1.
- Native GOLD carried 0 analysis rows, 1 organism row, and 2 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 0 exact rows for `NCBITaxon:2587417`.
- BacDive found 0 exact rows. StrainInfo found 20 direct strain rows and 25 deposit rows under `NCBITaxon:2587417`, with all 20 compressed JSONL rows assigned directly to the target taxon.

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
