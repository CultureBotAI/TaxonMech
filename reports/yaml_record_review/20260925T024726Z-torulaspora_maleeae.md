# YAML Record Review: Torulaspora maleeae

- Verdict: pass
- Target: `data/taxa/eukaryota/torulaspora_maleeae.yaml`
- Identifier: `NCBITaxon:200334`

## Target
Reviewed the complete 103-line YAML record for Torulaspora maleeae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `torulaspora_maleeae`.

## Validation
- `just validate data/taxa/eukaryota/torulaspora_maleeae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/torulaspora_maleeae.yaml data/taxa/eukaryota/torulaspora_microellipsoides.yaml data/taxa/eukaryota/torulaspora_pretoriensis.yaml data/taxa/eukaryota/tothia_fuscella.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 39585 retained `NCBITaxon:200334` as `Torulaspora maleeae` at rank `SPECIES`, with parent `NCBITaxon:4948`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:200334` on line 54449.
- The NCBI synonym columns supplied 0 exact synonyms, 0 broad synonyms, and 11 related synonyms.
- All 13 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- `NCBITaxon:443857` through `NCBITaxon:443864`, plus `NCBITaxon:444775`, occurred only as old identifiers merged into `NCBITaxon:200334` in `data/raw/ncbi_merged_ids.tsv`, and none were retained as live YAML identifiers.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:200334` on line 18469, matching the YAML aggregate with `organism_count` 1.
- Native GOLD carried 1 analysis row, 1 organism row, and 1 project row for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 7 exact rows for `NCBITaxon:200334` across `BCC 25515`, `BCC:25515`, `BCC<THA>:25515`, `CBS 10694`, `CBS:10694`, `NBRC 11061`, and `NBRC:11061`.
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
