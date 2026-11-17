# YAML Record Review: Thermochaetoides thermophila DSM 1495

- Verdict: pass
- Target: `data/taxa/eukaryota/thermochaetoides_thermophila_dsm_1495.yaml`
- Identifier: `NCBITaxon:759272`

## Target

Reviewed the complete 80-line YAML record for Thermochaetoides thermophila DSM 1495. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thermochaetoides_thermophila_dsm_1495.

## Validation

- `just validate data/taxa/eukaryota/thermochaetoides_thermophila_dsm_1495.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thermochaetoides_thermophila.yaml data/taxa/eukaryota/thermochaetoides_thermophila_dsm_1495.yaml data/taxa/eukaryota/thermomyces_dupontii.yaml data/taxa/eukaryota/thermomyces_ibadanensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:175950` is `NCBITaxon:759272`, label `Thermochaetoides thermophila DSM 1495`, rank `STRAIN`, parent `NCBITaxon:209285`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 0 exact synonyms, 0 broad synonyms, and 0 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:759272` at line 56672.
- All 17 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- No NCBI merged-ID row targeted `NCBITaxon:759272`, and the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:759272` at line 42432 with `organism_count` 18, matching the YAML GOLD source assertion count of 18.
- Native GOLD source tables include 18 organism rows, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has no exact `NCBITaxon:759272` rows.
- The local BacDive exact table has no row for `NCBITaxon:759272`.
- The local StrainInfo exact scan found 0 direct rows and 0 deposit rows for `NCBITaxon:759272`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:759272`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:759272`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:759272`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the strain record's NCBI identity, NCBI lineage, GOLD assertion count, and zero-strain coverage internally consistent with the local generated evidence.
