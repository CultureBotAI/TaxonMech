# YAML Record Review: Trichoderma pezizoides

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_pezizoides.yaml`
- Identifier: `NCBITaxon:1491002`

## Target

Reviewed the complete 88-line YAML record for Trichoderma pezizoides. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_pezizoides.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_pezizoides.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_pezizoides.yaml data/taxa/eukaryota/trichoderma_piluliferum.yaml data/taxa/eukaryota/trichoderma_pinnatum.yaml data/taxa/eukaryota/trichoderma_placentula.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 381687 retains `NCBITaxon:1491002` as `Trichoderma pezizoides`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1491002` at line 60289, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the three synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps retired `NCBITaxon:213985` to retained `NCBITaxon:1491002`, and an exact tab-anchored lookup found the old identifier only in `data/raw/ncbi_merged_ids.tsv`, not in the active `data/raw/ncbitaxon_taxa.tsv` row set.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1491002` at line 11582 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. `data/raw/ncbi_type_material.tsv` contains two type-material rows for the target: `GJS 01-257` and `GJS:01-257`. The raw StrainInfo JSONL contains 3 exact direct records and 4 exact deposit rows for `NCBITaxon:1491002`; BacDive contributed 0 exact rows.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target, so the exact raw StrainInfo side inventory has not been materialized as local child strain records.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material support, one retired NCBI identifier pointing into the retained target, raw StrainInfo side evidence, and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
