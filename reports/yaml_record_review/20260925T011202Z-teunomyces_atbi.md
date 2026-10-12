# YAML Record Review: Teunomyces atbi

- Verdict: pass
- Target: `data/taxa/eukaryota/teunomyces_atbi.yaml`
- Identifier: `NCBITaxon:348314`

## Target

Reviewed the complete 88-line YAML record for Teunomyces atbi. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for teunomyces_atbi.

## Validation

- `just validate data/taxa/eukaryota/teunomyces_atbi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/teunomyces_atbi.yaml data/taxa/eukaryota/teunomyces_barrocoloradensis.yaml data/taxa/eukaryota/teunomyces_cretensis.yaml data/taxa/eukaryota/teunomyces_funiuensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:71946` is `NCBITaxon:348314`, label `Teunomyces atbi`, rank `SPECIES`, parent `NCBITaxon:1539665`, genetic code `12`, taxonomy snapshot `2026-09-13`, with 1 exact synonym, 0 broad synonyms, and 5 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:348314` at line 55300.
- All 13 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps obsolete `NCBITaxon:297644` and `NCBITaxon:297645` to current `NCBITaxon:348314`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:348314` at line 32953 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has eight exact `NCBITaxon:348314` Candida atbi rows at lines 191245-191252 for ATCC MYA-4351 culture-from-type-material variants plus CBS 9852 and NRRL Y-27651 type-material variants.
- The local BacDive exact table has no row for `NCBITaxon:348314`.
- The local StrainInfo exact scan found 0 direct rows and 0 deposit rows for `NCBITaxon:348314`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:348314`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:348314`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:348314`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, type-material evidence, and zero-strain coverage internally consistent with the local generated evidence.
