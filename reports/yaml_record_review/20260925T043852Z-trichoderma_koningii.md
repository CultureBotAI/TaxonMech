# YAML Record Review: Trichoderma koningii

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_koningii.yaml`
- Identifier: `NCBITaxon:97093`

## Target

Reviewed the complete 84-line YAML record for Trichoderma koningii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_koningii.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_koningii.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_italicum.yaml data/taxa/eukaryota/trichoderma_ivoriense.yaml data/taxa/eukaryota/trichoderma_konilangbra.yaml data/taxa/eukaryota/trichoderma_koningii.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 16377 retains `NCBITaxon:97093` as `Trichoderma koningii`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:97093` at line 53573, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 1 related synonym, matching the two synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps retired `NCBITaxon:114618` and `NCBITaxon:2050754` to retained `NCBITaxon:97093`, and an exact tab-anchored lookup found both old identifiers only in `data/raw/ncbi_merged_ids.tsv`, not in the active `data/raw/ncbitaxon_taxa.tsv` row set.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:97093` at line 45133 with `organism_count` 3, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 2 organism rows, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 14 type-material rows for the target: `CBS 989.97`, `CBS:989.97`, `G.J.S. 89-122`, `GJS 89-122`, `GJS:89-122`, `BPI 745885`, `BPI:745885`, `CBS 457.96`, `CBS:457.96`, `G.J.S. 96-117`, `GJS 96-117`, `GJS:96-117`, `ATCC 64262`, and `ATCC:64262`. The raw StrainInfo JSONL contains 127 exact direct records and 170 exact deposit rows for `NCBITaxon:97093`, including four non-direct records carrying four exact deposits for the target; BacDive contributed 0 exact rows.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target, so the exact raw StrainInfo side inventory has not been materialized as local child strain records.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material support, two retired NCBI identifiers pointing into the retained target, raw StrainInfo side evidence, and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
