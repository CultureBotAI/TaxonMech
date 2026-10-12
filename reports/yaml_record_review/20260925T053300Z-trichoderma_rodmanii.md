# YAML Record Review: Trichoderma rodmanii

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_rodmanii.yaml`
- Identifier: `NCBITaxon:1491006`

## Target

Reviewed the complete 85-line YAML record for Trichoderma rodmanii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_rodmanii.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_rodmanii.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_rifaii.yaml data/taxa/eukaryota/trichoderma_rodmanii.yaml data/taxa/eukaryota/trichoderma_rogersonii.yaml data/taxa/eukaryota/trichoderma_rossicum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 381691 retains `NCBITaxon:1491006` as `Trichoderma rodmanii`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1491006` at line 60293, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 2 related synonyms, matching the two related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps retired `NCBITaxon:490625` to retained `NCBITaxon:1491006`, and an exact tab-anchored lookup found the old identifier only in `data/raw/ncbi_merged_ids.tsv`, not in the active `data/raw/ncbitaxon_taxa.tsv` row set.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1491006` at line 11586 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found seven type-material rows for the target: `CBS 120895`, `CBS:120895`, `G.J.S. 91-88`, `GJS 91-88`, `GJS:91-88`, `BPI 1112859`, and `BPI:1112859`. BacDive and StrainInfo contributed 0 exact direct or deposit rows for `NCBITaxon:1491006`.

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
