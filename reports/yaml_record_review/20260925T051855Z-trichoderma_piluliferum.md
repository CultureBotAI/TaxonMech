# YAML Record Review: Trichoderma piluliferum

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_piluliferum.yaml`
- Identifier: `NCBITaxon:509242`

## Target

Reviewed the complete 87-line YAML record for Trichoderma piluliferum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_piluliferum.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_piluliferum.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_pezizoides.yaml data/taxa/eukaryota/trichoderma_piluliferum.yaml data/taxa/eukaryota/trichoderma_pinnatum.yaml data/taxa/eukaryota/trichoderma_placentula.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 115707 retains `NCBITaxon:509242` as `Trichoderma piluliferum`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:509242` at line 55864, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the three synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps retired `NCBITaxon:63575` to retained `NCBITaxon:509242`, and an exact tab-anchored lookup found the old identifier only in `data/raw/ncbi_merged_ids.tsv`, not in the active `data/raw/ncbitaxon_taxa.tsv` row set.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:509242` at line 37481 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found six type-material rows for the target: `CBS 814.68`, `CBS:814.68`, `CBS 120927`, `CBS:120927`, `SHD-M 2638`, and `SHD-M:2638`. The raw StrainInfo JSONL contains 9 exact direct records and 17 exact deposit rows for `NCBITaxon:509242`; two non-direct rows, StrainInfo 147105 and 147106, also carry exact target deposits. BacDive contributed 0 exact rows.

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
