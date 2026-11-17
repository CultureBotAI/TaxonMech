# YAML Record Review: Xylaria cubensis

- Verdict: pass
- Target: `data/taxa/eukaryota/xylaria_cubensis.yaml`
- Identifier: `NCBITaxon:114814`

## Target

Reviewed the complete 123-line YAML record for Xylaria cubensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for xylaria_cubensis.

## Validation

- `just validate data/taxa/eukaryota/xylaria_cubensis.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/xylaria_crozonensis.yaml data/taxa/eukaryota/xylaria_cubensis.yaml data/taxa/eukaryota/xylaria_curta.yaml data/taxa/eukaryota/xylaria_digitata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 20882 retains `NCBITaxon:114814` as `Xylaria cubensis`, rank `SPECIES`, parent `NCBITaxon:37991`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:114814` at line 53810, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 14 related synonyms, matching the YAML synonym entries. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps 12 old identifiers, `NCBITaxon:1180845`, `NCBITaxon:1180900`, `NCBITaxon:1180911`, `NCBITaxon:1180912`, `NCBITaxon:1180913`, `NCBITaxon:1180957`, `NCBITaxon:1180969`, `NCBITaxon:1181017`, `NCBITaxon:1181059`, `NCBITaxon:1181121`, `NCBITaxon:1181122`, and `NCBITaxon:757798`, into this retained target, and the YAML keeps only `NCBITaxon:114814`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:114814` at line 3014 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 18 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found no type-material rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 13 exact direct rows and 17 exact deposit rows for `NCBITaxon:114814`, with all target deposits carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a retained NCBITaxon and GOLD seed with exact StrainInfo support, and the 12 old NCBI identifiers correctly remain out of the YAML identifier set.
