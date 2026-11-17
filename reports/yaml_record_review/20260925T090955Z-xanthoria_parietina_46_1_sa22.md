# YAML Record Review: Xanthoria parietina 46-1-SA22

- Verdict: pass
- Target: `data/taxa/eukaryota/xanthoria_parietina_46_1_sa22.yaml`
- Identifier: `NCBITaxon:714311`

## Target

Reviewed the complete 86-line YAML record for Xanthoria parietina 46-1-SA22. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for xanthoria_parietina_46_1_sa22.

## Validation

- `just validate data/taxa/eukaryota/xanthoria_parietina_46_1_sa22.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/xanthoria_parietina_46_1_sa22.yaml data/taxa/eukaryota/xerocomellus_chrysenteron.yaml data/taxa/eukaryota/xerocomellus_pruinatus.yaml data/taxa/eukaryota/xerocomus_subtomentosus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 168457 retains `NCBITaxon:714311` as `Xanthoria parietina 46-1-SA22`, rank `STRAIN`, parent `NCBITaxon:107463`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:714311` at line 56542, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 0 related synonyms, matching the empty YAML synonym set. All 19 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:714311` at line 41874 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found no type-material rows for the target. BacDive contributed 0 exact rows, and StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:714311`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon strain and GOLD seed under Xanthoria parietina, with no generated raw strain-table rows pending YAML incorporation.
