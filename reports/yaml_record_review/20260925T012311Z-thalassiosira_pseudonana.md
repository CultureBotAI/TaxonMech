# YAML Record Review: Thalassiosira pseudonana

- Verdict: pass
- Target: `data/taxa/eukaryota/thalassiosira_pseudonana.yaml`
- Identifier: `NCBITaxon:35128`

## Target

Reviewed the complete 69-line YAML record for Thalassiosira pseudonana. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thalassiosira_pseudonana.

## Validation

- `just validate data/taxa/eukaryota/thalassiosira_pseudonana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thalassiosira_oceanica.yaml data/taxa/eukaryota/thalassiosira_oceanica_ccmp1005.yaml data/taxa/eukaryota/thalassiosira_pseudonana.yaml data/taxa/eukaryota/thalassiosira_punctigera.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:3892` is `NCBITaxon:35128`, label `Thalassiosira pseudonana`, rank `SPECIES`, parent `NCBITaxon:35127`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 0 exact synonyms, 0 broad synonyms, and 1 related synonym.
- The seed-scope table has exactly one row for `NCBITaxon:35128` at line 52288.
- All 12 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- No NCBI merged-ID row targeted `NCBITaxon:35128`, and the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:35128` at line 33010 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 2 organism rows, 30 project rows, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has no exact `NCBITaxon:35128` rows.
- The local BacDive exact table has no row for `NCBITaxon:35128`.
- The local StrainInfo exact scan found 10 direct rows carrying 11 exact deposit rows for `NCBITaxon:35128`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:35128`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:35128`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:35128`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, StrainInfo exact matches, and zero generated-strain coverage internally consistent with the local generated evidence.
