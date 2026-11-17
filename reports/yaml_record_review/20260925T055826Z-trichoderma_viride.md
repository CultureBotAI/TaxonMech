# YAML Record Review: Trichoderma viride

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_viride.yaml`
- Identifier: `NCBITaxon:5547`

## Target

Reviewed the complete 108-line YAML record for Trichoderma viride. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_viride.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_viride.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_viridarium.yaml data/taxa/eukaryota/trichoderma_viride.yaml data/taxa/eukaryota/trichoderma_viridescens.yaml data/taxa/eukaryota/trichoderma_viridialbum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 2466 retains `NCBITaxon:5547` as `Trichoderma viride`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:5547` at line 52032, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 3 exact, 0 broad, and 7 related synonyms, matching the three exact and seven related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps six historical identifiers, `NCBITaxon:303616`, `NCBITaxon:362035`, `NCBITaxon:482421`, `NCBITaxon:65470`, `NCBITaxon:79661`, and `NCBITaxon:79662`, into this target; an exact ignored-file-inclusive scan found no retained current rows for those old identifiers in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:5547` at line 38689 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 11 type-material rows for the target: `WU 24093`, `WU:24093`, `C.P.K. 1997`, `CBS 119325`, `CBS:119325`, `GJS 04-372`, `GJS:04-372`, `Hypo 292`, `WU 24013a`, `WU:24013a`, and `personal:Hypo:292`. BacDive contributed 0 exact rows; StrainInfo contributed 212 exact direct rows and 271 exact deposit rows for `NCBITaxon:5547`.

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
