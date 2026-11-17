# YAML Record Review: Thalassiosira oceanica

- Verdict: pass
- Target: `data/taxa/eukaryota/thalassiosira_oceanica.yaml`
- Identifier: `NCBITaxon:159749`

## Target

Reviewed the complete 70-line YAML record for Thalassiosira oceanica. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thalassiosira_oceanica.

## Validation

- `just validate data/taxa/eukaryota/thalassiosira_oceanica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thalassiosira_oceanica.yaml data/taxa/eukaryota/thalassiosira_oceanica_ccmp1005.yaml data/taxa/eukaryota/thalassiosira_pseudonana.yaml data/taxa/eukaryota/thalassiosira_punctigera.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:32999` is `NCBITaxon:159749`, label `Thalassiosira oceanica`, rank `SPECIES`, parent `NCBITaxon:35127`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 0 exact synonyms, 0 broad synonyms, and 1 related synonym.
- The seed-scope table has exactly one row for `NCBITaxon:159749` at line 54157.
- All 12 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- No NCBI merged-ID row targeted `NCBITaxon:159749`, and the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:159749` at line 12908 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has no exact `NCBITaxon:159749` rows.
- The local BacDive exact table has no row for `NCBITaxon:159749`.
- The local StrainInfo exact scan found 10 direct rows carrying 10 exact deposit rows for `NCBITaxon:159749`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:159749`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:159749`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:159749`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, StrainInfo exact matches, and zero generated-strain coverage internally consistent with the local generated evidence.
