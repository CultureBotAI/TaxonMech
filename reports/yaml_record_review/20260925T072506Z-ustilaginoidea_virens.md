# YAML Record Review: Ustilaginoidea virens

- Verdict: pass
- Target: `data/taxa/eukaryota/ustilaginoidea_virens.yaml`
- Identifier: `NCBITaxon:1159556`

## Target

Reviewed the complete 102-line YAML record for Ustilaginoidea virens. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for ustilaginoidea_virens.

## Validation

- `just validate data/taxa/eukaryota/ustilaginoidea_virens.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ustilaginoidea_virens.yaml data/taxa/eukaryota/ustilago_bromivora.yaml data/taxa/eukaryota/ustilago_cynodontis.yaml data/taxa/eukaryota/ustilago_esculenta.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 254799 retains `NCBITaxon:1159556` as `Ustilaginoidea virens`, rank `SPECIES`, parent `NCBITaxon:124426`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1159556` at line 58068, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 3 exact, 0 broad, and 5 related synonyms, matching the YAML synonym entries. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps 1 old identifier into this target at line 9517, with no old identifiers retained as current NCBITaxon rows.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1159556` at line 3422 with `organism_count` 3, matching the YAML GOLD assertion count. The native GOLD tables contained 2 analyses, 3 organism rows, and 3 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 6 type-material rows for the target at lines 10379 through 10384. BacDive contributed 0 exact rows; StrainInfo contributed 8 exact direct rows and 15 exact deposit rows for `NCBITaxon:1159556`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI epitype and StrainInfo support plus one retired NCBI identifier resolved into the current target, so the YAML accurately reflects the evidence available for the target identifier.
