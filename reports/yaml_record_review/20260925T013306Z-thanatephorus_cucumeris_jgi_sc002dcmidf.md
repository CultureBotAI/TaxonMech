# YAML Record Review: Thanatephorus cucumeris JGI SC002DCMIDF

- Verdict: pass
- Target: `data/taxa/eukaryota/thanatephorus_cucumeris_jgi_sc002dcmidf.yaml`
- Identifier: `NCBITaxon:1379297`

## Target

Reviewed the complete 71-line YAML record for Thanatephorus cucumeris JGI SC002DCMIDF. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thanatephorus_cucumeris_jgi_sc002dcmidf.

## Validation

- `just validate data/taxa/eukaryota/thanatephorus_cucumeris_jgi_sc002dcmidf.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/thanatephorus_cucumeris.yaml data/taxa/eukaryota/thanatephorus_cucumeris_jgi_sc002dcmidf.yaml data/taxa/eukaryota/thanatephorus_sp.yaml data/taxa/eukaryota/thaxterogaster_aff_campbellae.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:336760` is `NCBITaxon:1379297`, label `Thanatephorus cucumeris JGI SC002DCMIDF`, rank `STRAIN`, parent `NCBITaxon:107832`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 0 exact synonyms, 0 broad synonyms, and 0 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:1379297` at line 59707.
- All 14 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- No NCBI merged-ID row targeted `NCBITaxon:1379297`, and the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:1379297` at line 8910 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 0 organism rows, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has no exact `NCBITaxon:1379297` rows.
- The local BacDive exact table has no row for `NCBITaxon:1379297`.
- The local StrainInfo exact scan found 0 direct rows and 0 deposit rows for `NCBITaxon:1379297`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:1379297`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:1379297`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:1379297`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the strain record's NCBI identity, NCBI lineage, GOLD assertion count, and zero-strain coverage internally consistent with the local generated evidence.
