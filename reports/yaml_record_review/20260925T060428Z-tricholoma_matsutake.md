# YAML Record Review: Tricholoma matsutake

- Verdict: pass
- Target: `data/taxa/eukaryota/tricholoma_matsutake.yaml`
- Identifier: `NCBITaxon:40145`

## Target

Reviewed the complete 99-line YAML record for Tricholoma matsutake. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tricholoma_matsutake.

## Validation

- `just validate data/taxa/eukaryota/tricholoma_matsutake.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/tricholoma_flavovirens.yaml data/taxa/eukaryota/tricholoma_furcatifolium.yaml data/taxa/eukaryota/tricholoma_matsutake.yaml data/taxa/eukaryota/tricholoma_populinum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 4562 retains `NCBITaxon:40145` as `Tricholoma matsutake`, rank `SPECIES`, parent `NCBITaxon:40144`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:40145` at line 52418, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 3 exact, 0 broad, and 6 related synonyms, matching the three exact and six related synonym entries in YAML. All 14 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps one historical identifier, `NCBITaxon:1095628`, into this target; an exact ignored-file-inclusive scan found no retained current row for that old identifier in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:40145` at line 34464 with `organism_count` 7, matching the YAML GOLD assertion count. The native GOLD tables contained 3 analyses, 5 organism rows, and 13 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found six type-material rows for the target: `AY-2041007-002`, `TNS F82226`, `TNS-F 82226`, `TNS-F82226`, `TNS:F82226`, and `TNSF82226`. BacDive contributed 0 exact rows; StrainInfo contributed 44 exact direct rows and 91 exact deposit rows for `NCBITaxon:40145`.

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
