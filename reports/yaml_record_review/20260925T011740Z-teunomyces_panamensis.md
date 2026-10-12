# YAML Record Review: Teunomyces panamensis

- Verdict: pass
- Target: `data/taxa/eukaryota/teunomyces_panamensis.yaml`
- Identifier: `NCBITaxon:297651`

## Target

Reviewed the complete 97-line YAML record for Teunomyces panamensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for teunomyces_panamensis.

## Validation

- `just validate data/taxa/eukaryota/teunomyces_panamensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/teunomyces_panamensis.yaml data/taxa/eukaryota/teunomyces_stri.yaml data/taxa/eukaryota/teunomyces_tritomae.yaml data/taxa/eukaryota/thalassionema_frauenfeldii.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:60692` is `NCBITaxon:297651`, label `Teunomyces panamensis`, rank `SPECIES`, parent `NCBITaxon:1539665`, genetic code `12`, taxonomy snapshot `2026-09-13`, with 1 exact synonym, 0 broad synonyms, and 8 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:297651` at line 55055.
- All 13 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps obsolete `NCBITaxon:271304`, `NCBITaxon:271338`, `NCBITaxon:271362`, `NCBITaxon:297649`, and `NCBITaxon:297650` to current `NCBITaxon:297651`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:297651` at line 29722 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has six exact `NCBITaxon:297651` Candida panamensis rows at lines 150560-150565 for NRRL Y-27657 culture-from-holotype variants and CBS 9849 type-material variants.
- The local BacDive exact table has no row for `NCBITaxon:297651`.
- The local StrainInfo exact scan found 0 direct rows and 0 deposit rows for `NCBITaxon:297651`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:297651`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:297651`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:297651`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, type-material evidence, and zero-strain coverage internally consistent with the local generated evidence.
