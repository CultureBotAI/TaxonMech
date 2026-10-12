# YAML Record Review: Thamnostylum lucknowense

- Verdict: pass
- Target: `data/taxa/eukaryota/thamnostylum_lucknowense.yaml`
- Identifier: `NCBITaxon:1162313`

## Target

Reviewed the complete 76-line YAML record for Thamnostylum lucknowense. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thamnostylum_lucknowense.

## Validation

- `just validate data/taxa/eukaryota/thamnostylum_lucknowense.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thamnostylum_lucknowense.yaml data/taxa/eukaryota/thamnostylum_nigricans.yaml data/taxa/eukaryota/thamnostylum_piriforme.yaml data/taxa/eukaryota/thamnostylum_repens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:255517` is `NCBITaxon:1162313`, label `Thamnostylum lucknowense`, rank `SPECIES`, parent `NCBITaxon:64650`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 1 exact synonym, 0 broad synonyms, and 2 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:1162313` at line 58080.
- All 12 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- No NCBI merged-ID row targeted `NCBITaxon:1162313`, and the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:1162313` at line 3485 with `organism_count` 6, matching the YAML GOLD source assertion count of 6.
- Native GOLD source tables include 4 organism rows, 4 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 10 exact `NCBITaxon:1162313` rows for ATCC 14746, CBS 576.69, IMI 086838, NRRL 2892, and RSA 1015, each present in both plain and colon-delimited forms.
- The local BacDive exact table has no row for `NCBITaxon:1162313`.
- The local StrainInfo exact scan found 4 direct rows and 9 deposit rows for `NCBITaxon:1162313`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:1162313`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:1162313`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:1162313`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, type-material rows, local StrainInfo matches, and zero-strain coverage internally consistent with the local generated evidence.
