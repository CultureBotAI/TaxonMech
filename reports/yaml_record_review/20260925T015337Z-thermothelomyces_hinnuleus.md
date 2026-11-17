# YAML Record Review: Thermothelomyces hinnuleus

- Verdict: pass
- Target: `data/taxa/eukaryota/thermothelomyces_hinnuleus.yaml`
- Identifier: `NCBITaxon:225406`

## Target

Reviewed the complete 88-line YAML record for Thermothelomyces hinnuleus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thermothelomyces_hinnuleus.

## Validation

- `just validate data/taxa/eukaryota/thermothelomyces_hinnuleus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thermothelomyces_hinnuleus.yaml data/taxa/eukaryota/thermothelomyces_myriococcoides.yaml data/taxa/eukaryota/thermothelomyces_thermophilus.yaml data/taxa/eukaryota/thermothielavioides_terrestris.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:44210` is `NCBITaxon:225406`, label `Thermothelomyces hinnuleus`, rank `SPECIES`, parent `NCBITaxon:1920207`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 2 exact synonyms, 0 broad synonyms, and 1 related synonym.
- The seed-scope table has exactly one row for `NCBITaxon:225406` at line 54622.
- All 16 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- No NCBI merged-ID row targeted `NCBITaxon:225406`, and the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:225406` at line 21247 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 8 exact `NCBITaxon:225406` rows for AJ 6773, ATCC 52474, CBS 597.83, and NHL 2909, each present in both plain and colon-delimited forms.
- The local BacDive exact table has no row for `NCBITaxon:225406`.
- The local StrainInfo exact scan found 7 direct rows and 10 deposit rows for `NCBITaxon:225406`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:225406`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:225406`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:225406`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, type-material rows, local StrainInfo matches, and zero-strain coverage internally consistent with the local generated evidence.
