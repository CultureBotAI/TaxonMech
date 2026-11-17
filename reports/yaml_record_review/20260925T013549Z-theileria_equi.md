# YAML Record Review: Theileria equi

- Verdict: pass
- Target: `data/taxa/eukaryota/theileria_equi.yaml`
- Identifier: `NCBITaxon:5872`

## Target

Reviewed the complete 68-line YAML record for Theileria equi. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for theileria_equi.

## Validation

- `just validate data/taxa/eukaryota/theileria_equi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thecaphora_thlaspeos.yaml data/taxa/eukaryota/theileria_annulata_strain_ankara.yaml data/taxa/eukaryota/theileria_equi.yaml data/taxa/eukaryota/theileria_orientalis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:2606` is `NCBITaxon:5872`, label `Theileria equi`, rank `SPECIES`, parent `NCBITaxon:5873`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 1 exact synonym, 0 broad synonyms, and 2 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:5872` at line 52106.
- All 10 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps `NCBITaxon:288690` to `NCBITaxon:5872`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:5872` at line 39528 with `organism_count` 2, matching the YAML GOLD source assertion count of 2.
- Native GOLD source tables include 2 organism rows, 2 project rows, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has no exact `NCBITaxon:5872` rows.
- The local BacDive exact table has no row for `NCBITaxon:5872`.
- The local StrainInfo exact scan found 0 direct rows and 0 deposit rows for `NCBITaxon:5872`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:5872`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:5872`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:5872`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, NCBI merged-ID handling, GOLD assertion count, and zero-strain coverage internally consistent with the local generated evidence.
