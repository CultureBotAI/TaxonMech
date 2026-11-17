# YAML Record Review: Trichoderma rogersonii

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_rogersonii.yaml`
- Identifier: `NCBITaxon:362042`

## Target

Reviewed the complete 90-line YAML record for Trichoderma rogersonii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_rogersonii.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_rogersonii.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_rifaii.yaml data/taxa/eukaryota/trichoderma_rodmanii.yaml data/taxa/eukaryota/trichoderma_rogersonii.yaml data/taxa/eukaryota/trichoderma_rossicum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 75362 retains `NCBITaxon:362042` as `Trichoderma rogersonii`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:362042` at line 55358, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 3 related synonyms, matching the four synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps retired `NCBITaxon:255610` to retained `NCBITaxon:362042`, and an exact tab-anchored lookup found the old identifier only in `data/raw/ncbi_merged_ids.tsv`, not in the active `data/raw/ncbitaxon_taxa.tsv` row set.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:362042` at line 33310 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found nine type-material rows for the target: `CBS 119233`, `CBS:119233`, `G.J.S. 04-158`, `GJS 04-158`, `GJS:04-158`, `BPI 870964A`, `BPI:870964A`, `BPI 870964B`, and `BPI:870964B`. BacDive and StrainInfo contributed 0 exact direct or deposit rows for `NCBITaxon:362042`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material support, one retired NCBI identifier pointing into the retained target, and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
