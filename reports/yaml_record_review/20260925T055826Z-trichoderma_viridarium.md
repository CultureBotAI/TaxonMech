# YAML Record Review: Trichoderma viridarium

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_viridarium.yaml`
- Identifier: `NCBITaxon:1383394`

## Target

Reviewed the complete 84-line YAML record for Trichoderma viridarium. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_viridarium.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_viridarium.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_viridarium.yaml data/taxa/eukaryota/trichoderma_viride.yaml data/taxa/eukaryota/trichoderma_viridescens.yaml data/taxa/eukaryota/trichoderma_viridialbum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 338070 retains `NCBITaxon:1383394` as `Trichoderma viridarium`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1383394` at line 59747, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 2 related synonyms, matching the two related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1383394` at line 9018 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found eight type-material rows for the target: `CBS 132568`, `CBS:132568`, `S136`, `S:136`, `WU 31627`, `WU:31627`, `GJS 89-142`, and `GJS:89-142`. BacDive contributed 0 exact rows; StrainInfo contributed 4 exact direct rows and 4 exact deposit rows for `NCBITaxon:1383394`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material and exact StrainInfo support but no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
