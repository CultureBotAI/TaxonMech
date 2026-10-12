# YAML Record Review: Trichoderma parepimyces

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_parepimyces.yaml`
- Identifier: `NCBITaxon:692672`

## Target

Reviewed the complete 87-line YAML record for Trichoderma parepimyces. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_parepimyces.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_parepimyces.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_pararogersonii.yaml data/taxa/eukaryota/trichoderma_paraviridescens.yaml data/taxa/eukaryota/trichoderma_parepimyces.yaml data/taxa/eukaryota/trichoderma_parmastoi.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 162582 retains `NCBITaxon:692672` as `Trichoderma parepimyces`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:692672` at line 56410, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the three synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:692672` at line 41427 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 2 projects for this identifier. `data/raw/ncbi_type_material.tsv` contains four type-material rows for the target: `CBS 122769`, `CBS:122769`, `WU 29107a`, and `WU:29107a`. BacDive and StrainInfo contributed 0 exact direct or deposit rows for `NCBITaxon:692672`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material and native GOLD support and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
