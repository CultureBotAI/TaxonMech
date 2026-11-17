# YAML Record Review: Theileria orientalis

- Verdict: pass
- Target: `data/taxa/eukaryota/theileria_orientalis.yaml`
- Identifier: `NCBITaxon:68886`

## Target

Reviewed the complete 225-line YAML record for Theileria orientalis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for theileria_orientalis.

## Validation

- `just validate data/taxa/eukaryota/theileria_orientalis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thecaphora_thlaspeos.yaml data/taxa/eukaryota/theileria_annulata_strain_ankara.yaml data/taxa/eukaryota/theileria_equi.yaml data/taxa/eukaryota/theileria_orientalis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:9430` is `NCBITaxon:68886`, label `Theileria orientalis`, rank `SPECIES`, parent `NCBITaxon:5873`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 0 exact synonyms, 0 broad synonyms, and 55 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:68886` at line 53174.
- All 10 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps the 54 old identifiers from `NCBITaxon:1417866` through `NCBITaxon:1417919` to `NCBITaxon:68886`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:68886` at line 41374 with `organism_count` 4, matching the YAML GOLD source assertion count of 4.
- Native GOLD source tables include 4 organism rows, 4 project rows, and 4 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has no exact `NCBITaxon:68886` rows.
- The local BacDive exact table has no row for `NCBITaxon:68886`.
- The local StrainInfo exact scan found 0 direct rows and 0 deposit rows for `NCBITaxon:68886`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:68886`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:68886`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:68886`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, NCBI merged-ID handling, GOLD assertion count, and zero-strain coverage internally consistent with the local generated evidence.
