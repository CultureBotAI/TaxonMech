# YAML Record Review: Trametes maxima

- Verdict: pass
- Target: `data/taxa/eukaryota/trametes_maxima.yaml`
- Identifier: `NCBITaxon:259368`

## Target
Reviewed the complete 90-line YAML record for Trametes maxima. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `trametes_maxima`.

## Validation
- `just validate data/taxa/eukaryota/trametes_maxima.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trametes_maxima.yaml data/taxa/eukaryota/trametes_meyenii.yaml data/taxa/eukaryota/trametes_polyzona.yaml data/taxa/eukaryota/trametes_pubescens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 52971 retained `NCBITaxon:259368` as `Trametes maxima` at rank `SPECIES`, with parent `NCBITaxon:5324`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:259368` on line 54828.
- The NCBI synonym columns supplied 4 exact synonyms, 0 broad synonyms, and 3 related synonyms.
- All 13 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- `NCBITaxon:888995` occurred only as an old identifier merged into `NCBITaxon:259368` in `data/raw/ncbi_merged_ids.tsv`, and it was not retained as a live YAML identifier.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:259368` on line 23790, matching the YAML aggregate with `organism_count` 2.
- Native GOLD carried 1 analysis row, 1 organism row, and 2 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 0 exact rows for `NCBITaxon:259368`.
- BacDive found 0 exact rows. StrainInfo found 23 direct strain rows and 23 deposit rows under `NCBITaxon:259368`, with all 23 compressed JSONL rows assigned directly to the target taxon.

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
