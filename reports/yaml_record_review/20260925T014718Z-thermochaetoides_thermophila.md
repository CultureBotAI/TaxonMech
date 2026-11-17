# YAML Record Review: Thermochaetoides thermophila

- Verdict: pass
- Target: `data/taxa/eukaryota/thermochaetoides_thermophila.yaml`
- Identifier: `NCBITaxon:209285`

## Target

Reviewed the complete 97-line YAML record for Thermochaetoides thermophila. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thermochaetoides_thermophila.

## Validation

- `just validate data/taxa/eukaryota/thermochaetoides_thermophila.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thermochaetoides_thermophila.yaml data/taxa/eukaryota/thermochaetoides_thermophila_dsm_1495.yaml data/taxa/eukaryota/thermomyces_dupontii.yaml data/taxa/eukaryota/thermomyces_ibadanensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:41309` is `NCBITaxon:209285`, label `Thermochaetoides thermophila`, rank `SPECIES`, parent `NCBITaxon:2944547`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 3 exact synonyms, 0 broad synonyms, and 3 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:209285` at line 54509.
- All 16 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps `NCBITaxon:1485947`, `NCBITaxon:2588330`, and `NCBITaxon:285224` to `NCBITaxon:209285`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:209285` at line 19994 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 18 exact `NCBITaxon:209285` rows covering paired CBS, DAOM, DSM, IMI, UC, and ATCC designations filed under `Chaetomium thermophilum` and `Chaetomium thermophilum var. coprophilum`.
- The local BacDive exact table has no row for `NCBITaxon:209285`.
- The local StrainInfo exact scan found 20 direct rows and 31 deposit rows for `NCBITaxon:209285`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:209285`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:209285`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:209285`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, NCBI merged-ID handling, GOLD assertion count, type-material rows, local StrainInfo matches, and zero-strain coverage internally consistent with the local generated evidence.
