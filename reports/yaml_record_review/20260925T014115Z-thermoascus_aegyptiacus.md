# YAML Record Review: Thermoascus aegyptiacus

- Verdict: pass
- Target: `data/taxa/eukaryota/thermoascus_aegyptiacus.yaml`
- Identifier: `NCBITaxon:1394850`

## Target

Reviewed the complete 81-line YAML record for Thermoascus aegyptiacus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thermoascus_aegyptiacus.

## Validation

- `just validate data/taxa/eukaryota/thermoascus_aegyptiacus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thelephora_ganbajun.yaml data/taxa/eukaryota/thelephora_terrestris.yaml data/taxa/eukaryota/thelonectria_olida.yaml data/taxa/eukaryota/thermoascus_aegyptiacus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:342844` is `NCBITaxon:1394850`, label `Thermoascus aegyptiacus`, rank `SPECIES`, parent `NCBITaxon:5086`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 1 exact synonym, 0 broad synonyms, and 1 related synonym.
- The seed-scope table has exactly one row for `NCBITaxon:1394850` at line 59838.
- All 15 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- No NCBI merged-ID row targeted `NCBITaxon:1394850`, and the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:1394850` at line 9315 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has no exact `NCBITaxon:1394850` rows.
- The local BacDive exact table has no row for `NCBITaxon:1394850`.
- The local StrainInfo exact scan found 1 direct row and 1 deposit row for `NCBITaxon:1394850`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:1394850`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:1394850`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:1394850`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, local StrainInfo matches, and zero-strain coverage internally consistent with the local generated evidence.
