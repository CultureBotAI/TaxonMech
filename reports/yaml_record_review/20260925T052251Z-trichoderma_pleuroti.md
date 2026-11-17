# YAML Record Review: Trichoderma pleuroti

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_pleuroti.yaml`
- Identifier: `NCBITaxon:500994`

## Target

Reviewed the complete 84-line YAML record for Trichoderma pleuroti. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_pleuroti.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_pleuroti.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_pleuroti.yaml data/taxa/eukaryota/trichoderma_pleuroticola.yaml data/taxa/eukaryota/trichoderma_polysporum.yaml data/taxa/eukaryota/trichoderma_poronioideum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 113625 retains `NCBITaxon:500994` as `Trichoderma pleuroti`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:500994` at line 55853, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 1 related synonym, matching the two synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps retired `NCBITaxon:573365` to retained `NCBITaxon:500994`, and an exact tab-anchored lookup found the old identifier only in `data/raw/ncbi_merged_ids.tsv`, not in the active `data/raw/ncbitaxon_taxa.tsv` row set.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:500994` at line 37313 with `organism_count` 5, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 2 organism rows, and 3 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found seven type-material rows for the target: `CBS 124387`, `CBS:124387`, `G.J.S. 09-02`, `GJS 09-02`, `GJS:09-02`, `CNUMH 501`, and `CNUMH:501`. BacDive and StrainInfo contributed 0 exact direct or deposit rows for `NCBITaxon:500994`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material and native GOLD support, one retired NCBI identifier pointing into the retained target, and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
