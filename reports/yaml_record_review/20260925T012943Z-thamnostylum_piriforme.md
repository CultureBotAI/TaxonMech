# YAML Record Review: Thamnostylum piriforme

- Verdict: pass
- Target: `data/taxa/eukaryota/thamnostylum_piriforme.yaml`
- Identifier: `NCBITaxon:101143`

## Target

Reviewed the complete 78-line YAML record for Thamnostylum piriforme. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thamnostylum_piriforme.

## Validation

- `just validate data/taxa/eukaryota/thamnostylum_piriforme.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thamnostylum_lucknowense.yaml data/taxa/eukaryota/thamnostylum_nigricans.yaml data/taxa/eukaryota/thamnostylum_piriforme.yaml data/taxa/eukaryota/thamnostylum_repens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:17455` is `NCBITaxon:101143`, label `Thamnostylum piriforme`, rank `SPECIES`, parent `NCBITaxon:64650`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 2 exact synonyms, 0 broad synonyms, and 2 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:101143` at line 53654.
- All 12 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps `NCBITaxon:1896171` and `NCBITaxon:64655` to `NCBITaxon:101143`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:101143` at line 265 with `organism_count` 4, matching the YAML GOLD source assertion count of 4.
- Native GOLD source tables include 4 organism rows, 4 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 4 exact `NCBITaxon:101143` rows for CBS 316.66 and IMI 211275, each present in both plain and colon-delimited forms.
- The local BacDive exact table has no row for `NCBITaxon:101143`.
- The local StrainInfo exact scan found 44 direct rows and 58 deposit rows for `NCBITaxon:101143`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:101143`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:101143`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:101143`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, NCBI merged-ID handling, GOLD assertion count, type-material rows, local StrainInfo matches, and zero-strain coverage internally consistent with the local generated evidence.
