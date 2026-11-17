# YAML Record Review: uncultured fungus

- Verdict: pass
- Target: `data/taxa/eukaryota/uncultured_fungus.yaml`
- Identifier: `NCBITaxon:175245`

## Target

Reviewed the complete 90-line YAML record for uncultured fungus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for uncultured_fungus.

## Validation

- `just validate data/taxa/eukaryota/uncultured_fungus.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/umbilicaria_muhlenbergii.yaml data/taxa/eukaryota/uncultured_chytridiomycetes.yaml data/taxa/eukaryota/uncultured_fungus.yaml data/taxa/eukaryota/undaria_pinnatifida.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 35538 retains `NCBITaxon:175245` as `uncultured fungus`, rank `SPECIES`, parent `NCBITaxon:57731`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:175245` at line 54285, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 3 exact, 0 broad, and 11 related synonyms, matching the YAML synonym entries. All 6 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps 11 old identifiers into this target at lines 21805, 23963, 39560, 40157, 42969, 64269, 73057, 77162, 80606, 81082, and 81348, with no old identifiers retained as current NCBITaxon rows.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:175245` at line 15237 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 0 type-material rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:175245`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed for a high-level environmental-sample fungal target with 11 retired NCBI identifiers resolved into the current target, so the YAML accurately reflects the evidence available for the target identifier.
