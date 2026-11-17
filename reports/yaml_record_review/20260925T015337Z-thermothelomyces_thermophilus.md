# YAML Record Review: Thermothelomyces thermophilus

- Verdict: pass
- Target: `data/taxa/eukaryota/thermothelomyces_thermophilus.yaml`
- Identifier: `NCBITaxon:78579`

## Target

Reviewed the complete 100-line YAML record for Thermothelomyces thermophilus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thermothelomyces_thermophilus.

## Validation

- `just validate data/taxa/eukaryota/thermothelomyces_thermophilus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thermothelomyces_hinnuleus.yaml data/taxa/eukaryota/thermothelomyces_myriococcoides.yaml data/taxa/eukaryota/thermothelomyces_thermophilus.yaml data/taxa/eukaryota/thermothielavioides_terrestris.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:11494` is `NCBITaxon:78579`, label `Thermothelomyces thermophilus`, rank `SPECIES`, parent `NCBITaxon:1920207`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 4 exact synonyms, 0 broad synonyms, and 3 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:78579` at line 53325.
- All 16 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps `NCBITaxon:109386`, `NCBITaxon:49010`, `NCBITaxon:573728`, and `NCBITaxon:911416` to `NCBITaxon:78579`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:78579` at line 42748 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 2 exact `NCBITaxon:78579` rows for CBS 117.65 in both plain and colon-delimited forms.
- The local BacDive exact table has no row for `NCBITaxon:78579`.
- The local StrainInfo exact scan found 49 direct rows and 66 deposit rows for `NCBITaxon:78579`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:78579`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:78579`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:78579`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, NCBI merged-ID handling, GOLD assertion count, type-material rows, local StrainInfo matches, and zero-strain coverage internally consistent with the local generated evidence.
