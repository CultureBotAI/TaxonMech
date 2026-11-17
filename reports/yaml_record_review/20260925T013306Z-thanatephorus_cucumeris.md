# YAML Record Review: Thanatephorus cucumeris

- Verdict: pass
- Target: `data/taxa/eukaryota/thanatephorus_cucumeris.yaml`
- Identifier: `NCBITaxon:107832`

## Target

Reviewed the complete 94-line YAML record for Thanatephorus cucumeris. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thanatephorus_cucumeris.

## Validation

- `just validate data/taxa/eukaryota/thanatephorus_cucumeris.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thanatephorus_cucumeris.yaml data/taxa/eukaryota/thanatephorus_cucumeris_jgi_sc002dcmidf.yaml data/taxa/eukaryota/thanatephorus_sp.yaml data/taxa/eukaryota/thaxterogaster_aff_campbellae.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:19506` is `NCBITaxon:107832`, label `Thanatephorus cucumeris`, rank `SPECIES`, parent `NCBITaxon:5238`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 3 exact synonyms, 0 broad synonyms, and 5 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:107832` at line 53726.
- All 13 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps `NCBITaxon:118239`, `NCBITaxon:29906`, `NCBITaxon:46530`, and `NCBITaxon:5239` to `NCBITaxon:107832`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:107832` at line 1437 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has no exact `NCBITaxon:107832` rows.
- The local BacDive exact table has no row for `NCBITaxon:107832`.
- The local StrainInfo exact scan found 176 direct rows and 287 deposit rows for `NCBITaxon:107832`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:107832`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:107832`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:107832`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, NCBI merged-ID handling, GOLD assertion count, local StrainInfo matches, and zero-strain coverage internally consistent with the local generated evidence.
