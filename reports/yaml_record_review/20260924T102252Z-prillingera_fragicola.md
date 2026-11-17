# YAML Record Review: Prillingera fragicola

- Verdict: pass
- Target: `data/taxa/eukaryota/prillingera_fragicola.yaml`
- Identifier: `NCBITaxon:181175`

## Target

Reviewed the complete 83-line YAML record for `Prillingera fragicola`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `prillingera_fragicola`.

## Validation

- `just validate data/taxa/eukaryota/prillingera_fragicola.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/prillingera_fragicola.yaml data/taxa/eukaryota/proboscia_alata.yaml data/taxa/eukaryota/proboscia_inermis.yaml data/taxa/eukaryota/proliferodiscus_dingleyae.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:36364` is the exact retained NCBITaxon row for `NCBITaxon:181175`: label `Prillingera fragicola`, rank `SPECIES`, parent `NCBITaxon:2576017`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54352` contains the seeded in-scope row for `NCBITaxon:181175` with the reason `attested rule: Prillingera fragicola, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:16031` is the aggregate GOLD row for `NCBITaxon:181175` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, one linked project row, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv:61543` through `data/raw/ncbi_type_material.tsv:61548` provide six exact `culture from holotype` aliases under `Cryptococcus fragicola`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found one direct local JSONL record covering three exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:181175`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:181175`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The native GOLD organism row, NCBI type-material aliases, and direct StrainInfo row all carry `JCM 1530` as an exact local designation, but no generated raw strain or StrainInfo overlay rows exist for the zero-strain YAML.
