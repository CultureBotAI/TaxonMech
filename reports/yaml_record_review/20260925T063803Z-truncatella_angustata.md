# YAML Record Review: Truncatella angustata

- Verdict: pass
- Target: `data/taxa/eukaryota/truncatella_angustata.yaml`
- Identifier: `NCBITaxon:152316`

## Target

Reviewed the complete 93-line YAML record for Truncatella angustata. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for truncatella_angustata.

## Validation

- `just validate data/taxa/eukaryota/truncatella_angustata.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/triparma_pacifica.yaml data/taxa/eukaryota/tripos_fusus.yaml data/taxa/eukaryota/tritrichomonas_foetus.yaml data/taxa/eukaryota/truncatella_angustata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 31747 retains `NCBITaxon:152316` as `Truncatella angustata`, rank `SPECIES`, parent `NCBITaxon:152317`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:152316` at line 54077, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 2 exact, 0 broad, and 3 related synonyms, matching the YAML synonym entries. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:152316` at line 12044 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 2 analyses, 2 organism rows, and 3 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 6 type-material rows for the target at lines 39229 through 39234. BacDive contributed 0 exact rows; StrainInfo contributed 25 exact direct rows and 29 exact deposit rows for `NCBITaxon:152316`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact StrainInfo and NCBI type-material support but no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
