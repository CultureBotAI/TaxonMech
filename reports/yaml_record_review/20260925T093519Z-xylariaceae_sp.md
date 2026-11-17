# YAML Record Review: Xylariaceae sp.

- Verdict: pass
- Target: `data/taxa/eukaryota/xylariaceae_sp.yaml`
- Identifier: `NCBITaxon:1881983`

## Target

Reviewed the complete 77-line YAML record for Xylariaceae sp. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for xylariaceae_sp.

## Validation

- `just validate data/taxa/eukaryota/xylariaceae_sp.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/xylaria_telfairii.yaml data/taxa/eukaryota/xylaria_venustula.yaml data/taxa/eukaryota/xylariaceae_sp.yaml data/taxa/eukaryota/xylariales_sp_no_14919.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 490163 retains `NCBITaxon:1881983` as `Xylariaceae sp.`, rank `SPECIES`, parent `NCBITaxon:246490`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1881983` at line 61422, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 0 related synonyms, matching the absent YAML synonym section. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1881983` at line 16897 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found no type-material rows for the target. BacDive contributed 0 exact rows, and StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:1881983`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed under unclassified Xylariaceae with no generated raw strain-table rows pending YAML incorporation.
