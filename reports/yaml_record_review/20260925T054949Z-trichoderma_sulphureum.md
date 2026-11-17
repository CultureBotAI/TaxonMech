# YAML Record Review: Trichoderma sulphureum

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_sulphureum.yaml`
- Identifier: `NCBITaxon:1491022`

## Target

Reviewed the complete 93-line YAML record for Trichoderma sulphureum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_sulphureum.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_sulphureum.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_strigosum.yaml data/taxa/eukaryota/trichoderma_stromaticum.yaml data/taxa/eukaryota/trichoderma_subeffusum.yaml data/taxa/eukaryota/trichoderma_sulphureum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 381694 retains `NCBITaxon:1491022` as `Trichoderma sulphureum`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1491022` at line 60296, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 2 exact, 0 broad, and 3 related synonyms, matching the two exact and three related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps one historical identifier, `NCBITaxon:202960`, into this target; an exact ignored-file-inclusive scan found no retained current row for that old identifier in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1491022` at line 11589 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 16 type-material rows for the target: `C.P.K. 1598`, `CBS 119929`, `CBS:119929`, `CPK 1598`, `CPK:1598`, `WU 29493`, `WU:29493`, `BPI 801107`, `BPI:801107`, `BPI 737752`, `BPI:737752`, `G.J.S. 95-176`, `GJS 95-176`, `GJS:95-176`, `WJ 2320`, and `WJ:2320`. BacDive contributed 0 exact rows; StrainInfo contributed 4 exact direct rows and 8 exact deposit rows for `NCBITaxon:1491022`.

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
