# YAML Record Review: Trichoderma paucisporum

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_paucisporum.yaml`
- Identifier: `NCBITaxon:552828`

## Target

Reviewed the complete 87-line YAML record for Trichoderma paucisporum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_paucisporum.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_paucisporum.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_patella.yaml data/taxa/eukaryota/trichoderma_paucisporum.yaml data/taxa/eukaryota/trichoderma_peltatum.yaml data/taxa/eukaryota/trichoderma_petersenii.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 129408 retains `NCBITaxon:552828` as `Trichoderma paucisporum`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:552828` at line 55984, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 3 related synonyms, matching the three related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps retired `NCBITaxon:336768`, `NCBITaxon:336772`, and `NCBITaxon:336773` to retained `NCBITaxon:552828`, and an exact tab-anchored lookup found all three old identifiers only in `data/raw/ncbi_merged_ids.tsv`, not in the active `data/raw/ncbitaxon_taxa.tsv` row set.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:552828` at line 38613 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found nine type-material rows for the target: `ATCC MYA-3641`, `ATCC:MYA-3641`, `ATCC:MYA:3641`, `CBS 118645`, `CBS:118645`, `GJS 01-13`, `GJS:01-13`, `BPI 870953`, and `BPI:870953`. The raw StrainInfo JSONL contains 2 exact direct records and 2 exact deposit rows for `NCBITaxon:552828`; BacDive contributed 0 exact rows.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target, so the exact raw StrainInfo side inventory has not been materialized as local child strain records.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material support, three retired NCBI identifiers pointing into the retained target, raw StrainInfo side evidence, and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
