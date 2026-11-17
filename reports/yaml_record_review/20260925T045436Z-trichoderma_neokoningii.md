# YAML Record Review: Trichoderma neokoningii

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_neokoningii.yaml`
- Identifier: `NCBITaxon:398675`

## Target

Reviewed the complete 81-line YAML record for Trichoderma neokoningii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_neokoningii.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_neokoningii.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_mienum.yaml data/taxa/eukaryota/trichoderma_minutisporum.yaml data/taxa/eukaryota/trichoderma_neocrassum.yaml data/taxa/eukaryota/trichoderma_neokoningii.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 85065 retains `NCBITaxon:398675` as `Trichoderma neokoningii`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:398675` at line 55513, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 1 related synonym, matching the single related synonym entry in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table reported no retired identifiers mapping to this taxon, and no retained old identifiers were present in the active NCBI row.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:398675` at line 34396 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found five type-material rows for the target: `CBS 120070`, `CBS:120070`, `G.J.S. 04-216`, `GJS 04-216`, and `GJS:04-216`. BacDive and StrainInfo contributed 0 exact direct or deposit rows for `NCBITaxon:398675`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material support and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
