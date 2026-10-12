# YAML Record Review: Trichoderma polysporum

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_polysporum.yaml`
- Identifier: `NCBITaxon:40695`

## Target

Reviewed the complete 115-line YAML record for Trichoderma polysporum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_polysporum.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_polysporum.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_pleuroti.yaml data/taxa/eukaryota/trichoderma_pleuroticola.yaml data/taxa/eukaryota/trichoderma_polysporum.yaml data/taxa/eukaryota/trichoderma_poronioideum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 4673 retains `NCBITaxon:40695` as `Trichoderma polysporum`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:40695` at line 52451, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 6 exact, 0 broad, and 6 related synonyms, matching the 12 synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps retired `NCBITaxon:1491021`, `NCBITaxon:1676178`, `NCBITaxon:234717`, `NCBITaxon:317022`, and `NCBITaxon:63579` to retained `NCBITaxon:40695`, and an exact tab-anchored lookup found all five old identifiers only in `data/raw/ncbi_merged_ids.tsv`, not in the active `data/raw/ncbitaxon_taxa.tsv` row set.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:40695` at line 34638 with `organism_count` 3, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 15 type-material rows for the target: `CBS 112265`, `CBS:112265`, `G.J.S. 99-122`, `GJS 99-222`, `GJS:99-222`, `PDD 77488`, `PDD:77488`, `CBS 820.68`, `CBS:820.68`, `TNS-F-190528`, `TNS-F:190528`, `CBS 337.93`, `CBS:337.93`, `DAOM 167068`, and `DAOM:167068`. The raw StrainInfo JSONL contains 68 exact direct records and 87 exact deposit rows for `NCBITaxon:40695`; one non-direct row, StrainInfo 147104, also carries an exact target deposit. BacDive contributed 0 exact rows.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target, so the exact raw StrainInfo side inventory has not been materialized as local child strain records.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with extensive type-material support, five retired NCBI identifiers pointing into the retained target, raw StrainInfo side evidence, and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
