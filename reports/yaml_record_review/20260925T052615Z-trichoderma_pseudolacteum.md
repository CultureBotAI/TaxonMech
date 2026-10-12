# YAML Record Review: Trichoderma pseudolacteum

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_pseudolacteum.yaml`
- Identifier: `NCBITaxon:1227968`

## Target

Reviewed the complete 96-line YAML record for Trichoderma pseudolacteum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_pseudolacteum.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_pseudolacteum.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_protopulvinatum.yaml data/taxa/eukaryota/trichoderma_pseudokoningii.yaml data/taxa/eukaryota/trichoderma_pseudolacteum.yaml data/taxa/eukaryota/trichoderma_pubescens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 280273 retains `NCBITaxon:1227968` as `Trichoderma pseudolacteum`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1227968` at line 58505, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 6 related synonyms, matching the six related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps retired `NCBITaxon:1227969`, `NCBITaxon:1227970`, `NCBITaxon:1227971`, and `NCBITaxon:1227972` to retained `NCBITaxon:1227968`, and an exact tab-anchored lookup found all four old identifiers only in `data/raw/ncbi_merged_ids.tsv`, not in the active `data/raw/ncbitaxon_taxa.tsv` row set.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1227968` at line 5453 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found six type-material rows for the target: `CBS 133191`, `CBS:133191`, `TUFC 61490`, `TUFC:61490`, `TMI 8484`, and `TMI:8484`. BacDive and StrainInfo contributed 0 exact direct or deposit rows for `NCBITaxon:1227968`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material support, four retired NCBI identifiers pointing into the retained target, and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
