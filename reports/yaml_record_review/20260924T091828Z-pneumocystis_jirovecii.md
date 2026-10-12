# YAML Record Review: Pneumocystis jirovecii

- Verdict: pass
- Target: `data/taxa/eukaryota/pneumocystis_jirovecii.yaml`
- Identifier: `NCBITaxon:42068`

## Target

Reviewed the complete 72-line YAML record for `Pneumocystis jirovecii`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pneumocystis_jirovecii`.

## Validation

- `just validate data/taxa/eukaryota/pneumocystis_jirovecii.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pneumocystis_jirovecii.yaml data/taxa/eukaryota/pneumocystis_oryctolagi.yaml data/taxa/eukaryota/pneumocystis_sp_macacae.yaml data/taxa/eukaryota/pneumocystis_wakefieldiae.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4916` is the exact retained NCBITaxon row for `NCBITaxon:42068`: label `Pneumocystis jirovecii`, rank `SPECIES`, parent `NCBITaxon:4753`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52508` contains the seeded in-scope row for `NCBITaxon:42068` with the reason `attested rule: Pneumocystis jirovecii, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:42068`.

## Evidence

- `data/raw/gold_organisms.tsv:35059` is the aggregate GOLD row for `NCBITaxon:42068` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row and no linked project or analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:42068`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:42068`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:42068`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with both the aggregate GOLD row and the single native GOLD organism row. No exact BacDive, StrainInfo, or type-material evidence needed to be materialized into the zero-strain YAML.
