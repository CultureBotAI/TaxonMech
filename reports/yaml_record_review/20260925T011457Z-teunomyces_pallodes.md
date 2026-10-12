# YAML Record Review: Teunomyces pallodes

- Verdict: pass
- Target: `data/taxa/eukaryota/teunomyces_pallodes.yaml`
- Identifier: `NCBITaxon:348313`

## Target

Reviewed the complete 100-line YAML record for Teunomyces pallodes. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for teunomyces_pallodes.

## Validation

- `just validate data/taxa/eukaryota/teunomyces_pallodes.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/teunomyces_gatunensis.yaml data/taxa/eukaryota/teunomyces_kruisii.yaml data/taxa/eukaryota/teunomyces_lycoperdinae.yaml data/taxa/eukaryota/teunomyces_pallodes.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:71945` is `NCBITaxon:348313`, label `Teunomyces pallodes`, rank `SPECIES`, parent `NCBITaxon:1539665`, genetic code `12`, taxonomy snapshot `2026-09-13`, with 1 exact synonym, 0 broad synonyms, and 9 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:348313` at line 55299.
- All 13 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps obsolete `NCBITaxon:234570`, `NCBITaxon:297641`, `NCBITaxon:297642`, `NCBITaxon:297643`, `NCBITaxon:297647`, and `NCBITaxon:297648` to current `NCBITaxon:348313`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:348313` at line 32952 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has six exact `NCBITaxon:348313` Candida pallodes rows at lines 191239-191244 for NRRL Y-27653 culture-from-holotype variants and CBS 9845 type-material variants.
- The local BacDive exact table has no row for `NCBITaxon:348313`.
- The local StrainInfo exact scan found 0 direct rows and 0 deposit rows for `NCBITaxon:348313`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:348313`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:348313`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:348313`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, type-material evidence, and zero-strain coverage internally consistent with the local generated evidence.
