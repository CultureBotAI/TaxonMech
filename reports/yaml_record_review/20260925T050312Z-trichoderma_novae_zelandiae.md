# YAML Record Review: Trichoderma novae-zelandiae

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_novae_zelandiae.yaml`
- Identifier: `NCBITaxon:173947`

## Target

Reviewed the complete 97-line YAML record for Trichoderma novae-zelandiae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_novae_zelandiae.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_novae_zelandiae.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_novae_zelandiae.yaml data/taxa/eukaryota/trichoderma_nybergianum.yaml data/taxa/eukaryota/trichoderma_oblongisporum.yaml data/taxa/eukaryota/trichoderma_olivascens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 35335 retains `NCBITaxon:173947` as `Trichoderma novae-zelandiae`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:173947` at line 54275, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 3 exact, 0 broad, and 3 related synonyms, matching the six synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps retired `NCBITaxon:1117148` and `NCBITaxon:1352079` to retained `NCBITaxon:173947`, and an exact tab-anchored lookup found both old identifiers only in `data/raw/ncbi_merged_ids.tsv`, not in the active `data/raw/ncbitaxon_taxa.tsv` row set.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:173947` at line 15111 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 11 type-material rows for the target: `CBS 496.97`, `CBS:496.97`, `G.J.S. 81-265`, `ATCC 208856`, `ATCC:208856`, `CBS 639.92`, `CBS:639.92`, `GJS 81-265`, `GJS:81-265`, `PDD 46792`, and `PDD:46792`. The raw StrainInfo JSONL contains 1 exact direct record and 1 exact deposit row for `NCBITaxon:173947`; BacDive contributed 0 exact rows.

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
