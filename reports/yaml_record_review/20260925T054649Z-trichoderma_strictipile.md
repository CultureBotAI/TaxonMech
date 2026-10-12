# YAML Record Review: Trichoderma strictipile

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_strictipile.yaml`
- Identifier: `NCBITaxon:63589`

## Target

Reviewed the complete 96-line YAML record for Trichoderma strictipile. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_strictipile.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_strictipile.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_stercorarium.yaml data/taxa/eukaryota/trichoderma_stilbohypoxyli.yaml data/taxa/eukaryota/trichoderma_strictipile.yaml data/taxa/eukaryota/trichoderma_strigosellum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 7996 retains `NCBITaxon:63589` as `Trichoderma strictipile`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:63589` at line 53064, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 4 exact, 0 broad, and 2 related synonyms, matching the four exact and two related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps five historical identifiers, `NCBITaxon:134831`, `NCBITaxon:173938`, `NCBITaxon:257807`, `NCBITaxon:320498`, and `NCBITaxon:63580`, into this target; an exact ignored-file-inclusive scan found no retained current rows for those old identifiers in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:63589` at line 40138 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 17 type-material rows for the target: `TNS-F 191611`, `TNS-F:191611`, `TNS.D-148`, `DAOM 167646`, `DAOM:167646`, `CBS 118.72`, `CBS 338.93`, `CBS:118.72`, `CBS:338.93`, `DAOM 167646; CBS 118.72`, `DAOM:167646; CBS 118.72`, `CBS 347.93`, `CBS:347.93`, `DAOM 172827`, `DAOM:172827`, `DAOM 172827; CBS 347.93`, and `DAOM:172827; CBS 347.93`. BacDive contributed 0 exact rows; StrainInfo contributed 6 exact direct rows and 12 exact deposit rows for `NCBITaxon:63589`.

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
