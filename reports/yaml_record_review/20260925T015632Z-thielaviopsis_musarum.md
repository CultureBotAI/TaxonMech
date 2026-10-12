# YAML Record Review: Thielaviopsis musarum

- Verdict: pass
- Target: `data/taxa/eukaryota/thielaviopsis_musarum.yaml`
- Identifier: `NCBITaxon:1580842`

## Target

Reviewed the complete 87-line YAML record for Thielaviopsis musarum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thielaviopsis_musarum.

## Validation

- `just validate data/taxa/eukaryota/thielaviopsis_musarum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/therrya_strobi.yaml data/taxa/eukaryota/thielaviopsis_musarum.yaml data/taxa/eukaryota/thielaviopsis_paradoxa.yaml data/taxa/eukaryota/thielaviopsis_punctulata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:407564` is `NCBITaxon:1580842`, label `Thielaviopsis musarum`, rank `SPECIES`, parent `NCBITaxon:60496`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 1 exact synonym, 0 broad synonyms, and 2 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:1580842` at line 60515.
- All 16 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps `NCBITaxon:927673` to `NCBITaxon:1580842`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:1580842` at line 12752 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 1 exact `NCBITaxon:1580842` culture-from-epitype row for ICMP:5789.
- The local BacDive exact table has no row for `NCBITaxon:1580842`.
- The local StrainInfo exact scan found 3 direct rows and 3 deposit rows for `NCBITaxon:1580842`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:1580842`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:1580842`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:1580842`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, NCBI merged-ID handling, GOLD assertion count, type-material row, local StrainInfo matches, and zero-strain coverage internally consistent with the local generated evidence.
