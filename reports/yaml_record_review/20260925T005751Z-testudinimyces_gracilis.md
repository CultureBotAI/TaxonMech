# YAML Record Review: Testudinimyces gracilis

- Verdict: pass
- Target: `data/taxa/eukaryota/testudinimyces_gracilis.yaml`
- Identifier: `NCBITaxon:3079312`

## Target

Reviewed the complete 70-line YAML record for Testudinimyces gracilis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for testudinimyces_gracilis.

## Validation

- `just validate data/taxa/eukaryota/testudinimyces_gracilis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/terramyces_sp.yaml data/taxa/eukaryota/testicularia_cyperi.yaml data/taxa/eukaryota/testudinimyces_gracilis.yaml data/taxa/eukaryota/tetrachaetum_elegans.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:595471` is `NCBITaxon:3079312`, label `Testudinimyces gracilis`, rank `SPECIES`, parent `NCBITaxon:3079311`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 0 exact synonyms, 0 broad synonyms, and 2 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:3079312` at line 63542.
- All 11 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps obsolete `NCBITaxon:3025778` to current `NCBITaxon:3079312`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:3079312` at line 31195 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 0 organism rows, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has five exact `NCBITaxon:3079312` culture-from-holotype rows at lines 164808-164812 for OKLA T130A spelling variants and `T130Clone10`.
- The local BacDive exact table has no row for `NCBITaxon:3079312`.
- The local StrainInfo exact scan found 0 direct rows and 0 deposit rows for `NCBITaxon:3079312`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:3079312`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:3079312`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:3079312`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, type-material evidence, and zero-strain coverage internally consistent with the local generated evidence.
