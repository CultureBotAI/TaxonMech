# YAML Record Review: Xylaria arbuscula

- Verdict: pass
- Target: `data/taxa/eukaryota/xylaria_arbuscula.yaml`
- Identifier: `NCBITaxon:114810`

## Target

Reviewed the complete 93-line YAML record for Xylaria arbuscula. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for xylaria_arbuscula.

## Validation

- `just validate data/taxa/eukaryota/xylaria_arbuscula.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/xiuguozyma_silvatica.yaml data/taxa/eukaryota/xylaria_acuta.yaml data/taxa/eukaryota/xylaria_arbuscula.yaml data/taxa/eukaryota/xylaria_bambusicola.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 20879 retains `NCBITaxon:114810` as `Xylaria arbuscula`, rank `SPECIES`, parent `NCBITaxon:37991`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:114810` at line 53808, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 5 related synonyms, matching the YAML synonym entries. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps four old identifiers, `NCBITaxon:1180987`, `NCBITaxon:1181012`, `NCBITaxon:1181041`, and `NCBITaxon:1181053`, into this retained target, and the YAML keeps only `NCBITaxon:114810`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:114810` at line 3012 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 2 organism rows, and 24 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found no type-material rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 11 exact direct rows and 20 exact deposit rows for `NCBITaxon:114810`, with all target deposits carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a retained NCBITaxon and GOLD seed with exact StrainInfo support, and the four old NCBI identifiers correctly remain out of the YAML identifier set.
