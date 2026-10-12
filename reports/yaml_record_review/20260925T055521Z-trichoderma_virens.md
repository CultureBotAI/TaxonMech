# YAML Record Review: Trichoderma virens

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_virens.yaml`
- Identifier: `NCBITaxon:29875`

## Target

Reviewed the complete 96-line YAML record for Trichoderma virens. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_virens.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_virens.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_velutinum.yaml data/taxa/eukaryota/trichoderma_vermipilum.yaml data/taxa/eukaryota/trichoderma_victoriense.yaml data/taxa/eukaryota/trichoderma_virens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 3288 retains `NCBITaxon:29875` as `Trichoderma virens`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:29875` at line 52218, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 4 exact, 0 broad, and 2 related synonyms, matching the four exact and two related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps two historical identifiers, `NCBITaxon:63582` and `NCBITaxon:64490`, into this target; an exact ignored-file-inclusive scan found no retained current rows for those old identifiers in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:29875` at line 29905 with `organism_count` 13, matching the YAML GOLD assertion count. The native GOLD tables contained 2 analyses, 13 organism rows, and 52 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 26 type-material rows for the target: `ATCC 13308`, `ATCC:13308`, `CBS 248.59`, `CBS:248.59`, `DAOM 167652`, `DAOM:167652`, `ATCC MYA-1298`, `ATCC:MYA-1298`, `ATCC:MYA:1298`, `BPI 737768`, `BPI:737768`, `CBS 109339`, `CBS:109339`, `G.J. Samuels 95-194`, `G.J.S. 95-194`, `personal:G.J. Samuels:95-194`, `CBS 249.59`, `CBS:249.59`, `ATCC 13213`, `ATCC:13213`, `CBS 249.59; DCDSL 139/01`, `CBS:249.59; DCDSL 139/01`, `DAOM 167651; CBS 249.59`, `DAOM:167651; CBS 249.59`, `MUCL 7585`, and `MUCL:7585`. BacDive contributed 0 exact rows; StrainInfo contributed 94 exact direct rows and 158 exact deposit rows for `NCBITaxon:29875`.

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
