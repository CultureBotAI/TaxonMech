# YAML Record Review: Thelebolus globosus

- Verdict: pass
- Target: `data/taxa/eukaryota/thelebolus_globosus.yaml`
- Identifier: `NCBITaxon:319062`

## Target

Reviewed the complete 78-line YAML record for Thelebolus globosus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thelebolus_globosus.

## Validation

- `just validate data/taxa/eukaryota/thelebolus_globosus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/theileria_parva_strain_muguga.yaml data/taxa/eukaryota/thelebolus_globosus.yaml data/taxa/eukaryota/thelebolus_microsporus.yaml data/taxa/eukaryota/thelephora_aurantiotincta.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:65346` is `NCBITaxon:319062`, label `Thelebolus globosus`, rank `SPECIES`, parent `NCBITaxon:46452`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 0 exact synonyms, 0 broad synonyms, and 1 related synonym.
- The seed-scope table has exactly one row for `NCBITaxon:319062` at line 55178.
- All 15 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- No NCBI merged-ID row targeted `NCBITaxon:319062`, and the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:319062` at line 31889 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 2 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 2 exact `NCBITaxon:319062` culture-from-holotype rows for CBS 113940 in both plain and colon-delimited forms.
- The local BacDive exact table has no row for `NCBITaxon:319062`.
- The local StrainInfo exact scan found 2 direct rows and 2 deposit rows for `NCBITaxon:319062`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:319062`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:319062`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:319062`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, type-material rows, local StrainInfo matches, and zero-strain coverage internally consistent with the local generated evidence.
