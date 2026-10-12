# YAML Record Review: Thalassionema nitzschioides

- Verdict: pass
- Target: `data/taxa/eukaryota/thalassionema_nitzschioides.yaml`
- Identifier: `NCBITaxon:33649`

## Target

Reviewed the complete 75-line YAML record for Thalassionema nitzschioides. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thalassionema_nitzschioides.

## Validation

- `just validate data/taxa/eukaryota/thalassionema_nitzschioides.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thalassionema_nitzschioides.yaml data/taxa/eukaryota/thalassiosira_antarctica.yaml data/taxa/eukaryota/thalassiosira_gravida.yaml data/taxa/eukaryota/thalassiosira_minuscula.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:3567` is `NCBITaxon:33649`, label `Thalassionema nitzschioides`, rank `SPECIES`, parent `NCBITaxon:33648`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 1 exact synonym, 0 broad synonyms, and 2 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:33649` at line 52259.
- All 12 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- No NCBI merged-ID row targeted `NCBITaxon:33649`, and the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:33649` at line 32467 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 2 organism rows, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has no exact `NCBITaxon:33649` rows.
- The local BacDive exact table has no row for `NCBITaxon:33649`.
- The local StrainInfo exact scan found 4 direct rows carrying 4 exact deposit rows for `NCBITaxon:33649`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:33649`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:33649`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:33649`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, StrainInfo exact matches, and zero generated-strain coverage internally consistent with the local generated evidence.
