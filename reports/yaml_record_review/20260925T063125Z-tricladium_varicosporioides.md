# YAML Record Review: Tricladium varicosporioides

- Verdict: pass
- Target: `data/taxa/eukaryota/tricladium_varicosporioides.yaml`
- Identifier: `NCBITaxon:2075069`

## Target

Reviewed the complete 81-line YAML record for Tricladium varicosporioides. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tricladium_varicosporioides.

## Validation

- `just validate data/taxa/eukaryota/tricladium_varicosporioides.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/tricladium_splendens.yaml data/taxa/eukaryota/tricladium_varicosporioides.yaml data/taxa/eukaryota/trieres_chinensis.yaml data/taxa/eukaryota/trigonopsis_californica.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 515746 retains `NCBITaxon:2075069` as `Tricladium varicosporioides`, rank `SPECIES`, parent `NCBITaxon:223899`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:2075069` at line 62261, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 2 exact, 0 broad, and 0 related synonyms, matching the two exact synonym entries in YAML. All 15 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps one historical identifier, `NCBITaxon:354079`, into this target; an exact ignored-file-inclusive scan found no retained current row for that old identifier in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:2075069` at line 19816 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 2 organism rows, and 3 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 4 type-material rows for the target at lines 82871 through 82874. BacDive contributed 0 exact rows; StrainInfo contributed 6 exact direct rows and 7 exact deposit rows for `NCBITaxon:2075069`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with exact StrainInfo and NCBI type-material support but no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
