# YAML Record Review: Protostelium mycophagum

- Verdict: pass
- Target: `data/taxa/eukaryota/protostelium_mycophagum.yaml`
- Identifier: `NCBITaxon:472931`

## Target

Reviewed the complete 63-line YAML record for `Protostelium mycophagum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `protostelium_mycophagum`.

## Validation

- `just validate data/taxa/eukaryota/protostelium_mycophagum.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/protocruzia_adhaerens.yaml data/taxa/eukaryota/protomyces_lactucae_debilis.yaml data/taxa/eukaryota/protomycocladus_faisalabadensis.yaml data/taxa/eukaryota/protostelium_mycophagum.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:105602` is the exact retained NCBITaxon row for `NCBITaxon:472931`: label `Protostelium mycophagum`, rank `SPECIES`, parent `NCBITaxon:472930`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:55769` contains the seeded in-scope row for `NCBITaxon:472931` with the reason `attested rule: Protostelium mycophagum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 1 related synonym, and 0 broad synonyms.
- All 9 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:36493` is the aggregate GOLD row for `NCBITaxon:472931` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, one linked project row, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:472931`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has one direct local JSONL record covering one exact deposit, `CCAP 1562/1`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:472931`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:472931`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with the aggregate GOLD row and the native GOLD organism row for `ATCC PRA-154`. No type-material, BacDive, or generated StrainInfo overlay rows were present for this zero-strain record.
