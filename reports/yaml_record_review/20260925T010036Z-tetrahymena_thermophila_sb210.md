# YAML Record Review: Tetrahymena thermophila SB210

- Verdict: pass
- Target: `data/taxa/eukaryota/tetrahymena_thermophila_sb210.yaml`
- Identifier: `NCBITaxon:312017`

## Target

Reviewed the complete 68-line YAML record for Tetrahymena thermophila SB210. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tetrahymena_thermophila_sb210.

## Validation

- `just validate data/taxa/eukaryota/tetrahymena_thermophila_sb210.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/tetracladium_marchalianum.yaml data/taxa/eukaryota/tetrahymena_elliotti_4ea.yaml data/taxa/eukaryota/tetrahymena_thermophila.yaml data/taxa/eukaryota/tetrahymena_thermophila_sb210.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:63822` is `NCBITaxon:312017`, label `Tetrahymena thermophila SB210`, rank `STRAIN`, parent `NCBITaxon:5911`, genetic code `6`, taxonomy snapshot `2026-09-13`, with 0 exact synonyms, 0 broad synonyms, and 0 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:312017` at line 55138.
- All 13 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- No NCBI merged-ID row targeted `NCBITaxon:312017`, and the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:312017` at line 31495 with `organism_count` 2, matching the YAML GOLD source assertion count of 2.
- Native GOLD source tables include 2 organism rows, 2 project rows, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has no exact `NCBITaxon:312017` rows.
- The local BacDive exact table has no row for `NCBITaxon:312017`.
- The local StrainInfo exact scan found 0 direct rows and 0 deposit rows for `NCBITaxon:312017`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:312017`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:312017`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:312017`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, and zero-strain coverage internally consistent with the local generated evidence.
