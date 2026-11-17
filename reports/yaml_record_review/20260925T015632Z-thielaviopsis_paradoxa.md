# YAML Record Review: Thielaviopsis paradoxa

- Verdict: pass
- Target: `data/taxa/eukaryota/thielaviopsis_paradoxa.yaml`
- Identifier: `NCBITaxon:13001`

## Target

Reviewed the complete 103-line YAML record for Thielaviopsis paradoxa. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thielaviopsis_paradoxa.

## Validation

- `just validate data/taxa/eukaryota/thielaviopsis_paradoxa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/therrya_strobi.yaml data/taxa/eukaryota/thielaviopsis_musarum.yaml data/taxa/eukaryota/thielaviopsis_paradoxa.yaml data/taxa/eukaryota/thielaviopsis_punctulata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:2656` is `NCBITaxon:13001`, label `Thielaviopsis paradoxa`, rank `SPECIES`, parent `NCBITaxon:60496`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 6 exact synonyms, 0 broad synonyms, and 2 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:13001` at line 52119.
- All 16 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps `NCBITaxon:54188` to `NCBITaxon:13001`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:13001` at line 7356 with `organism_count` 2, matching the YAML GOLD source assertion count of 2.
- Native GOLD source tables include 2 organism rows, 2 project rows, and 2 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has no exact `NCBITaxon:13001` rows.
- The local BacDive exact table has no row for `NCBITaxon:13001`.
- The local StrainInfo exact scan found 47 direct rows and 61 deposit rows for `NCBITaxon:13001`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:13001`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:13001`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:13001`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, NCBI merged-ID handling, GOLD assertion count, local StrainInfo matches, and zero-strain coverage internally consistent with the local generated evidence.
