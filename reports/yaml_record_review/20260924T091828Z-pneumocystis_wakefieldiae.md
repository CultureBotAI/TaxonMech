# YAML Record Review: Pneumocystis wakefieldiae

- Verdict: pass
- Target: `data/taxa/eukaryota/pneumocystis_wakefieldiae.yaml`
- Identifier: `NCBITaxon:38082`

## Target

Reviewed the complete 69-line YAML record for `Pneumocystis wakefieldiae`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pneumocystis_wakefieldiae`.

## Validation

- `just validate data/taxa/eukaryota/pneumocystis_wakefieldiae.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pneumocystis_jirovecii.yaml data/taxa/eukaryota/pneumocystis_oryctolagi.yaml data/taxa/eukaryota/pneumocystis_sp_macacae.yaml data/taxa/eukaryota/pneumocystis_wakefieldiae.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4333` is the exact retained NCBITaxon row for `NCBITaxon:38082`: label `Pneumocystis wakefieldiae`, rank `SPECIES`, parent `NCBITaxon:4753`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52387` contains the seeded in-scope row for `NCBITaxon:38082` with the reason `attested rule: Pneumocystis wakefieldiae, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:38082`.

## Evidence

- `data/raw/gold_organisms.tsv:33896` is the aggregate GOLD row for `NCBITaxon:38082` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, one linked project row, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has two exact holotype rows for `NCBITaxon:38082`, both filed under `Pneumocystis wakefieldiae`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:38082`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:38082`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact holotype rows are NCBI designations that do not appear as generated strain rows. The generated GOLD source attestation is consistent with both the aggregate GOLD row and the native GOLD row for `Pneumocystis wakefieldiae 2A`.
