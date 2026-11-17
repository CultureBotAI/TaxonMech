# YAML Record Review: Xylaria bambusicola

- Verdict: pass
- Target: `data/taxa/eukaryota/xylaria_bambusicola.yaml`
- Identifier: `NCBITaxon:326684`

## Target

Reviewed the complete 81-line YAML record for Xylaria bambusicola. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for xylaria_bambusicola.

## Validation

- `just validate data/taxa/eukaryota/xylaria_bambusicola.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/xiuguozyma_silvatica.yaml data/taxa/eukaryota/xylaria_acuta.yaml data/taxa/eukaryota/xylaria_arbuscula.yaml data/taxa/eukaryota/xylaria_bambusicola.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 66815 retains `NCBITaxon:326684` as `Xylaria bambusicola`, rank `SPECIES`, parent `NCBITaxon:37991`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:326684` at line 55227, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 1 related synonym, matching the YAML synonym entries. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:326684` at line 32180 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 2 type-material rows for the target at lines 177660 through 177661. BacDive contributed 0 exact rows; StrainInfo contributed 1 exact direct row and 2 exact deposit rows for `NCBITaxon:326684`, with all target deposits carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI type-material and StrainInfo support, and no generated raw strain-table rows pending YAML incorporation.
