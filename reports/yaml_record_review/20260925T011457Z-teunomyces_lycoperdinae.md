# YAML Record Review: Teunomyces lycoperdinae

- Verdict: pass
- Target: `data/taxa/eukaryota/teunomyces_lycoperdinae.yaml`
- Identifier: `NCBITaxon:297653`

## Target

Reviewed the complete 91-line YAML record for Teunomyces lycoperdinae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for teunomyces_lycoperdinae.

## Validation

- `just validate data/taxa/eukaryota/teunomyces_lycoperdinae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/teunomyces_gatunensis.yaml data/taxa/eukaryota/teunomyces_kruisii.yaml data/taxa/eukaryota/teunomyces_lycoperdinae.yaml data/taxa/eukaryota/teunomyces_pallodes.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:60693` is `NCBITaxon:297653`, label `Teunomyces lycoperdinae`, rank `SPECIES`, parent `NCBITaxon:1539665`, genetic code `12`, taxonomy snapshot `2026-09-13`, with 1 exact synonym, 0 broad synonyms, and 6 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:297653` at line 55056.
- All 13 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps obsolete `NCBITaxon:234549`, `NCBITaxon:271265`, and `NCBITaxon:297652` to current `NCBITaxon:297653`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:297653` at line 29723 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has eight exact `NCBITaxon:297653` Candida lycoperdinae rows at lines 150566-150573 for ATCC MYA-4350 culture-from-type-material variants plus CBS 9850 and NRRL Y-27658 type-material variants.
- The local BacDive exact table has no row for `NCBITaxon:297653`.
- The local StrainInfo exact scan found 0 direct rows and 0 deposit rows for `NCBITaxon:297653`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:297653`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:297653`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:297653`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, type-material evidence, and zero-strain coverage internally consistent with the local generated evidence.
