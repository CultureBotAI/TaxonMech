# YAML Record Review: Trichoderma velutinum

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_velutinum.yaml`
- Identifier: `NCBITaxon:202918`

## Target

Reviewed the complete 84-line YAML record for Trichoderma velutinum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_velutinum.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_velutinum.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_velutinum.yaml data/taxa/eukaryota/trichoderma_vermipilum.yaml data/taxa/eukaryota/trichoderma_victoriense.yaml data/taxa/eukaryota/trichoderma_virens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 40045 retains `NCBITaxon:202918` as `Trichoderma velutinum`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:202918` at line 54474, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 2 related synonyms, matching the two related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps one historical identifier, `NCBITaxon:127027`, into this target; an exact ignored-file-inclusive scan found no retained current row for that old identifier in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:202918` at line 19118 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 2 organism rows, and 4 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found ten type-material rows for the target: `ATCC MYA-4841`, `ATCC:MYA-4841`, `ATCC:MYA:4841`, `DAOM 230013`, `DAOM:230013`, `C.P.K. 298`, `DAOM 230013; TUB F-784`, `DAOM 230013; TUB F-784; CPK298`, `DAOM:230013; TUB F-784`, and `DAOM:230013; TUB F-784; CPK298`. BacDive and StrainInfo contributed 0 exact direct or deposit rows for `NCBITaxon:202918`.

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
