# YAML Record Review: Prymnesium kappa

- Verdict: pass
- Target: `data/taxa/eukaryota/prymnesium_kappa.yaml`
- Identifier: `NCBITaxon:97486`

## Target

Reviewed the complete 66-line YAML record for `Prymnesium kappa`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `prymnesium_kappa`.

## Validation

- `just validate data/taxa/eukaryota/prymnesium_kappa.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/prymnesium_kappa.yaml data/taxa/eukaryota/prymnesium_neolepis.yaml data/taxa/eukaryota/prymnesium_parvum.yaml data/taxa/eukaryota/prymnesium_polylepis.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:16457` is the exact retained NCBITaxon row for `NCBITaxon:97486`: label `Prymnesium kappa`, rank `SPECIES`, parent `NCBITaxon:35143`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53588` contains the seeded in-scope row for `NCBITaxon:97486` with the reason `attested rule: Prymnesium kappa, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 9 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:45159` is the aggregate GOLD row for `NCBITaxon:97486` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has no exact organism rows, linked project rows, or linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:97486`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found two direct local JSONL records covering three exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:97486`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:97486`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is backed by the aggregate GOLD row; exact native GOLD organism, project, and analysis scans returned 0 rows for `NCBITaxon:97486`. Exact StrainInfo JSONL rows are present but have no generated overlay rows.
