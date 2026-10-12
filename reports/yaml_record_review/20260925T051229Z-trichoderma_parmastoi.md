# YAML Record Review: Trichoderma parmastoi

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_parmastoi.yaml`
- Identifier: `NCBITaxon:1491000`

## Target

Reviewed the complete 87-line YAML record for Trichoderma parmastoi. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_parmastoi.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_parmastoi.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_pararogersonii.yaml data/taxa/eukaryota/trichoderma_paraviridescens.yaml data/taxa/eukaryota/trichoderma_parepimyces.yaml data/taxa/eukaryota/trichoderma_parmastoi.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 381685 retains `NCBITaxon:1491000` as `Trichoderma parmastoi`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1491000` at line 60287, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the three synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps retired `NCBITaxon:396889` to retained `NCBITaxon:1491000`, and an exact tab-anchored lookup found the old identifier only in `data/raw/ncbi_merged_ids.tsv`, not in the active `data/raw/ncbitaxon_taxa.tsv` row set.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1491000` at line 11580 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. `data/raw/ncbi_type_material.tsv` contains five type-material rows for the target: `TFC 97-143`, `TFC:97-143`, `BPI 843639`, `BPI:843639`, and `TAA(M) 169055`. BacDive and StrainInfo contributed 0 exact direct or deposit rows for `NCBITaxon:1491000`.

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
