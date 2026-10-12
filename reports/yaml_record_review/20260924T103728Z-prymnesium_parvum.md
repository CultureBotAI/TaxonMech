# YAML Record Review: Prymnesium parvum

- Verdict: pass
- Target: `data/taxa/eukaryota/prymnesium_parvum.yaml`
- Identifier: `NCBITaxon:97485`

## Target

Reviewed the complete 63-line YAML record for `Prymnesium parvum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `prymnesium_parvum`.

## Validation

- `just validate data/taxa/eukaryota/prymnesium_parvum.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/prymnesium_kappa.yaml data/taxa/eukaryota/prymnesium_neolepis.yaml data/taxa/eukaryota/prymnesium_parvum.yaml data/taxa/eukaryota/prymnesium_polylepis.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:16456` is the exact retained NCBITaxon row for `NCBITaxon:97485`: label `Prymnesium parvum`, rank `SPECIES`, parent `NCBITaxon:3688006`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53587` contains the seeded in-scope row for `NCBITaxon:97485` with the reason `attested rule: Prymnesium parvum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 10 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:45158` is the aggregate GOLD row for `NCBITaxon:97485` and reports `organism_count=3`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, no linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:97485`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found 11 direct local JSONL records covering 15 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:97485`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:97485`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The YAML parent is the retained NCBI `Prymnesium parvum species complex` species-group row. The generated GOLD source attestation matches the aggregate GOLD row even though the exact native GOLD scan found one organism row, `Prymnesium parvum Texoma1`.
