# YAML Record Review: Trichoderma koningiopsis

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_koningiopsis.yaml`
- Identifier: `NCBITaxon:337941`

## Target

Reviewed the complete 96-line YAML record for Trichoderma koningiopsis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_koningiopsis.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_koningiopsis.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_koningiopsis.yaml data/taxa/eukaryota/trichoderma_kunmingense.yaml data/taxa/eukaryota/trichoderma_lanuginosum.yaml data/taxa/eukaryota/trichoderma_leguminosarum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 69302 retains `NCBITaxon:337941` as `Trichoderma koningiopsis`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:337941` at line 55278, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 5 related synonyms, matching the six synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps retired `NCBITaxon:1909264`, `NCBITaxon:255607`, `NCBITaxon:255608`, `NCBITaxon:255609`, and `NCBITaxon:336771` to retained `NCBITaxon:337941`, and an exact tab-anchored lookup found those old identifiers only in `data/raw/ncbi_merged_ids.tsv`, not in the active `data/raw/ncbitaxon_taxa.tsv` row set.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:337941` at line 32536 with `organism_count` 3, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 2 organism rows, and 3 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found nine type-material rows for the target: `BPI 802571`, `BPI:802571`, `CBS 119075`, `CBS:119075`, `G.J.S. 93-20`, `GJS 93-20`, `GJS:93-20`, `BPI 802571B`, and `BPI:802571B`. The raw StrainInfo JSONL contains 7 exact direct records and 8 exact deposit rows for `NCBITaxon:337941`, including one non-direct `Trichoderma koningii` record carrying one exact deposit for the target; BacDive contributed 0 exact rows.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target, so the exact raw StrainInfo side inventory has not been materialized as local child strain records.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material support, five retired NCBI identifiers pointing into the retained target, raw StrainInfo side evidence, and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
