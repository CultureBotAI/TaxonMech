# YAML Record Review: Thermothielavioides terrestris

- Verdict: pass
- Target: `data/taxa/eukaryota/thermothielavioides_terrestris.yaml`
- Identifier: `NCBITaxon:2587410`

## Target

Reviewed the complete 96-line YAML record for Thermothielavioides terrestris. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thermothielavioides_terrestris.

## Validation

- `just validate data/taxa/eukaryota/thermothielavioides_terrestris.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thermothelomyces_hinnuleus.yaml data/taxa/eukaryota/thermothelomyces_myriococcoides.yaml data/taxa/eukaryota/thermothelomyces_thermophilus.yaml data/taxa/eukaryota/thermothielavioides_terrestris.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:534328` is `NCBITaxon:2587410`, label `Thermothielavioides terrestris`, rank `SPECIES`, parent `NCBITaxon:2609811`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 3 exact synonyms, 0 broad synonyms, and 3 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:2587410` at line 62861.
- All 16 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps `NCBITaxon:35720` and `NCBITaxon:45274` to `NCBITaxon:2587410`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:2587410` at line 23677 with `organism_count` 7, matching the YAML GOLD source assertion count of 7.
- Native GOLD source tables include 7 organism rows, 7 project rows, and 2 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 4 exact `NCBITaxon:2587410` culture-from-holotype rows for CBS 117535 and CBS 355.66 in both plain and colon-delimited forms.
- The local BacDive exact table has no row for `NCBITaxon:2587410`.
- The local StrainInfo exact scan found 29 direct rows and 46 deposit rows for `NCBITaxon:2587410`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:2587410`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:2587410`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:2587410`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, NCBI merged-ID handling, GOLD assertion count, type-material rows, local StrainInfo matches, and zero-strain coverage internally consistent with the local generated evidence.
