# YAML Record Review: Torulaspora gathmanii

- Verdict: pass
- Target: `data/taxa/eukaryota/torulaspora_gathmanii.yaml`
- Identifier: `NCBITaxon:3680291`

## Target
Reviewed the complete 79-line YAML record for Torulaspora gathmanii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `torulaspora_gathmanii`.

## Validation
- `just validate data/taxa/eukaryota/torulaspora_gathmanii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/torulaspora_delbrueckii.yaml data/taxa/eukaryota/torulaspora_franciscae.yaml data/taxa/eukaryota/torulaspora_gathmanii.yaml data/taxa/eukaryota/torulaspora_globosa.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 639750 retained `NCBITaxon:3680291` as `Torulaspora gathmanii` at rank `SPECIES`, with parent `NCBITaxon:4948`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:3680291` on line 63689.
- The NCBI synonym columns supplied 0 exact synonyms, 0 broad synonyms, and 3 related synonyms.
- All 13 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- `NCBITaxon:2866360` and `NCBITaxon:3342731` occurred only as old identifiers merged into `NCBITaxon:3680291` in `data/raw/ncbi_merged_ids.tsv`, and neither was retained as a live YAML identifier.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:3680291` on line 33482, matching the YAML aggregate with `organism_count` 1.
- Native GOLD carried 0 analysis rows, 0 organism rows, and 0 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 12 exact rows for `NCBITaxon:3680291` across `CBS 18642`, `CBS-18642`, `CBS18642`, `CBS:18642`, `PYCC 9889`, `PYCC-9889`, `PYCC9889`, `PYCC:9889`, `PYCC 9889H`, `PYCC-9889H`, `PYCC9889H`, and `PYCC:9889H`.
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
