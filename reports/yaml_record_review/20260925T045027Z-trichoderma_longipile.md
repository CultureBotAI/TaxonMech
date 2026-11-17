# YAML Record Review: Trichoderma longipile

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_longipile.yaml`
- Identifier: `NCBITaxon:692670`

## Target

Reviewed the complete 99-line YAML record for Trichoderma longipile. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_longipile.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_longipile.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_longifialidicum.yaml data/taxa/eukaryota/trichoderma_longipile.yaml data/taxa/eukaryota/trichoderma_lycogaloides.yaml data/taxa/eukaryota/trichoderma_margaretense.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 162581 retains `NCBITaxon:692670` as `Trichoderma longipile`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:692670` at line 56409, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 4 exact, 0 broad, and 3 related synonyms, matching the seven synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps retired `NCBITaxon:212373`, `NCBITaxon:504484`, `NCBITaxon:63583`, and `NCBITaxon:63584` to retained `NCBITaxon:692670`, and an exact tab-anchored lookup found those old identifiers only in `data/raw/ncbi_merged_ids.tsv`, not in the active `data/raw/ncbitaxon_taxa.tsv` row set.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:692670` at line 41426 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 16 type-material rows for the target: `BPI 1112864`, `BPI:1112864`, `CBS 111148`, `CBS:111148`, `CBS 120953`, `CBS:120953`, `BPI 843660`, `BPI:843660`, `CBS 340.93`, `CBS:340.93`, `DAOM 177227`, `DAOM:177227`, `DAOM 177227-1a`, `DAOM:177227-1a`, `DAOM 177227; CBS 340.93`, and `DAOM:177227; CBS 340.93`. The raw StrainInfo JSONL contains 5 exact direct records and 8 exact deposit rows for `NCBITaxon:692670`; BacDive contributed 0 exact rows.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target, so the exact raw StrainInfo side inventory has not been materialized as local child strain records.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material support, four retired NCBI identifiers pointing into the retained target, raw StrainInfo side evidence, and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
