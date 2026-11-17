# YAML Record Review: Thermothelomyces heterothallicus CBS 202.75

- Verdict: pass
- Target: `data/taxa/eukaryota/thermothelomyces_heterothallicus_cbs_202_75.yaml`
- Identifier: `NCBITaxon:1149848`

## Target

Reviewed the complete 84-line YAML record for Thermothelomyces heterothallicus CBS 202.75. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thermothelomyces_heterothallicus_cbs_202_75.

## Validation

- `just validate data/taxa/eukaryota/thermothelomyces_heterothallicus_cbs_202_75.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thermomyces_lanuginosus.yaml data/taxa/eukaryota/thermothelomyces_fergusii.yaml data/taxa/eukaryota/thermothelomyces_heterothallicus.yaml data/taxa/eukaryota/thermothelomyces_heterothallicus_cbs_202_75.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:251464` is `NCBITaxon:1149848`, label `Thermothelomyces heterothallicus CBS 202.75`, rank `STRAIN`, parent `NCBITaxon:1149786`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 1 exact synonym, 0 broad synonyms, and 0 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:1149848` at line 57998.
- All 17 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- No NCBI merged-ID row targeted `NCBITaxon:1149848`, and the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:1149848` at line 3034 with `organism_count` 2, matching the YAML GOLD source assertion count of 2.
- Native GOLD source tables include 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has no exact `NCBITaxon:1149848` rows.
- The local BacDive exact table has no row for `NCBITaxon:1149848`.
- The local StrainInfo exact scan found 0 direct rows and 0 deposit rows for `NCBITaxon:1149848`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:1149848`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:1149848`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:1149848`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the strain record's NCBI identity, NCBI lineage, GOLD assertion count, and zero-strain coverage internally consistent with the local generated evidence.
