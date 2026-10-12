# YAML Record Review: Venturia carpophila

- Verdict: pass
- Target: `data/taxa/eukaryota/venturia_carpophila.yaml`
- Identifier: `NCBITaxon:86257`

## Target

Reviewed the complete 87-line YAML record for Venturia carpophila. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for venturia_carpophila.

## Validation

- `just validate data/taxa/eukaryota/venturia_carpophila.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/veluticeps_abietina.yaml data/taxa/eukaryota/venturia_carpophila.yaml data/taxa/eukaryota/venturia_effusa.yaml data/taxa/eukaryota/venturia_inaequalis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 13345 retains `NCBITaxon:86257` as `Venturia carpophila`, rank `SPECIES`, parent `NCBITaxon:5024`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:86257` at line 53438, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 2 exact, 0 broad, and 1 related synonym, matching the YAML synonym entries. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps 1 old identifier into this target at line 80196, with no old identifiers retained as current NCBITaxon rows.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:86257` at line 43425 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 2 type-material rows for the target at lines 269062 and 269063. BacDive contributed 0 exact rows; StrainInfo contributed 12 exact direct rows and 16 exact deposit rows for `NCBITaxon:86257`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI type-material and StrainInfo support plus one retired NCBI identifier resolved into the current target, so the YAML accurately reflects the evidence available for the target identifier.
