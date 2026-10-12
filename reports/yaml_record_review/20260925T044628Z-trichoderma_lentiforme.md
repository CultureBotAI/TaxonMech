# YAML Record Review: Trichoderma lentiforme

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_lentiforme.yaml`
- Identifier: `NCBITaxon:1567552`

## Target

Reviewed the complete 90-line YAML record for Trichoderma lentiforme. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_lentiforme.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_lentiforme.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_lentiforme.yaml data/taxa/eukaryota/trichoderma_lieckfeldtiae.yaml data/taxa/eukaryota/trichoderma_longibrachiatum.yaml data/taxa/eukaryota/trichoderma_longibrachiatum_smf2.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 403716 retains `NCBITaxon:1567552` as `Trichoderma lentiforme`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1567552` at line 60484, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 3 related synonyms, matching the four synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table reported no retired identifiers mapping to this taxon, and no retained old identifiers were present in the active NCBI row.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1567552` at line 12603 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found seven type-material rows for the target: `CBS 100542`, `CBS:100542`, `G.J.S. 98-6`, `GJS 98-6`, `GJS:98-6`, `BPI 744709`, and `BPI:744709`. The raw StrainInfo JSONL contains 1 exact direct record and 1 exact deposit row for `NCBITaxon:1567552`; BacDive contributed 0 exact rows.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target, so the exact raw StrainInfo side inventory has not been materialized as local child strain records.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material support, raw StrainInfo side evidence, and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
