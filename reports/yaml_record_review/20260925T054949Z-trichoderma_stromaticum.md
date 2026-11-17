# YAML Record Review: Trichoderma stromaticum

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_stromaticum.yaml`
- Identifier: `NCBITaxon:96910`

## Target

Reviewed the complete 90-line YAML record for Trichoderma stromaticum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_stromaticum.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_stromaticum.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_strigosum.yaml data/taxa/eukaryota/trichoderma_stromaticum.yaml data/taxa/eukaryota/trichoderma_subeffusum.yaml data/taxa/eukaryota/trichoderma_sulphureum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 16336 retains `NCBITaxon:96910` as `Trichoderma stromaticum`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:96910` at line 53572, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 3 related synonyms, matching the exact and three related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps one historical identifier, `NCBITaxon:212379`, into this target; an exact ignored-file-inclusive scan found no retained current row for that old identifier in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:96910` at line 45125 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found ten type-material rows for the target: `ATCC 204426`, `ATCC:204426`, `CBS 101875`, `CBS:101875`, `GJS 97-183`, `GJS:97-183`, `BPI 746496`, `BPI:746496`, `DAOM 231100`, and `DAOM:231100`. BacDive contributed 0 exact rows; StrainInfo contributed 6 exact direct rows and 11 exact deposit rows for `NCBITaxon:96910`.

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
