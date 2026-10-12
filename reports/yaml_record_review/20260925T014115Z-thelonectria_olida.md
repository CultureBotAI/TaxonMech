# YAML Record Review: Thelonectria olida

- Verdict: pass
- Target: `data/taxa/eukaryota/thelonectria_olida.yaml`
- Identifier: `NCBITaxon:1576542`

## Target

Reviewed the complete 102-line YAML record for Thelonectria olida. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thelonectria_olida.

## Validation

- `just validate data/taxa/eukaryota/thelonectria_olida.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thelephora_ganbajun.yaml data/taxa/eukaryota/thelephora_terrestris.yaml data/taxa/eukaryota/thelonectria_olida.yaml data/taxa/eukaryota/thermoascus_aegyptiacus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:405839` is `NCBITaxon:1576542`, label `Thelonectria olida`, rank `SPECIES`, parent `NCBITaxon:1053258`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 4 exact synonyms, 0 broad synonyms, and 4 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:1576542` at line 60502.
- All 16 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps `NCBITaxon:303675` to `NCBITaxon:1576542`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:1576542` at line 12692 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 2 project rows, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 12 exact `NCBITaxon:1576542` culture-from-neotype rows for ATCC 16548, CBS 215.67, and DSM 62520 across plain, hyphenated, compact, and colon-delimited forms.
- The local BacDive exact table has no row for `NCBITaxon:1576542`.
- The local StrainInfo exact scan found 9 direct rows and 18 deposit rows for `NCBITaxon:1576542`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:1576542`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:1576542`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:1576542`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, NCBI merged-ID handling, GOLD assertion count, type-material rows, local StrainInfo matches, and zero-strain coverage internally consistent with the local generated evidence.
