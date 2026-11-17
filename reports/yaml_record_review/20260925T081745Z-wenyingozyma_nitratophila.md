# YAML Record Review: Wenyingozyma nitratophila

- Verdict: pass
- Target: `data/taxa/eukaryota/wenyingozyma_nitratophila.yaml`
- Identifier: `NCBITaxon:5495`

## Target

Reviewed the complete 85-line YAML record for Wenyingozyma nitratophila. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for wenyingozyma_nitratophila.

## Validation

- `just validate data/taxa/eukaryota/wenyingozyma_nitratophila.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/wenyingozyma_nanaspora.yaml data/taxa/eukaryota/wenyingozyma_nitratophila.yaml data/taxa/eukaryota/wenyingozyma_ramenticola.yaml data/taxa/eukaryota/wenyingozyma_succiphila.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 2440 retains `NCBITaxon:5495` as `Wenyingozyma nitratophila`, rank `SPECIES`, parent `NCBITaxon:3712563`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:5495` at line 52017, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 2 exact, 0 broad, and 3 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:5495` at line 38521 with `organism_count` 8, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 8 organism rows, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 20 type-material rows for the target at lines 233314 through 233333. BacDive contributed 0 exact rows; StrainInfo contributed 11 exact direct rows and 30 exact deposit rows for `NCBITaxon:5495`, with the target deposits all carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI type-material and StrainInfo support, so the YAML accurately reflects the evidence available for the target identifier.
