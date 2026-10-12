# YAML Record Review: Vishniacozyma victoriae

- Verdict: pass
- Target: `data/taxa/eukaryota/vishniacozyma_victoriae.yaml`
- Identifier: `NCBITaxon:1895944`

## Target

Reviewed the complete 78-line YAML record for Vishniacozyma victoriae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for vishniacozyma_victoriae.

## Validation

- `just validate data/taxa/eukaryota/vishniacozyma_victoriae.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/vishniacozyma_victoriae.yaml data/taxa/eukaryota/vitrella_brassicaformis.yaml data/taxa/eukaryota/vuilleminia_comedens.yaml data/taxa/eukaryota/wallemia_hederae.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 491400 retains `NCBITaxon:1895944` as `Vishniacozyma victoriae`, rank `SPECIES`, parent `NCBITaxon:1891946`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1895944` at line 61478, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 2 exact, 0 broad, and 1 related synonym, matching the YAML synonym entries. All 12 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table retains old identifier `NCBITaxon:156168` for this current target at line 20008.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1895944` at line 17098 with `organism_count` 3, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 2 organism rows, and 3 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 7 type-material rows for the target at lines 68562 through 68568. BacDive contributed 0 exact rows; StrainInfo contributed 78 exact direct rows and 85 exact deposit rows for `NCBITaxon:1895944`, with the target deposits all carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI type-material and StrainInfo support, so the YAML accurately reflects the evidence available for the target identifier.
