# YAML Record Review: Protomycocladus faisalabadensis

- Verdict: pass
- Target: `data/taxa/eukaryota/protomycocladus_faisalabadensis.yaml`
- Identifier: `NCBITaxon:101113`

## Target

Reviewed the complete 73-line YAML record for `Protomycocladus faisalabadensis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `protomycocladus_faisalabadensis`.

## Validation

- `just validate data/taxa/eukaryota/protomycocladus_faisalabadensis.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/protocruzia_adhaerens.yaml data/taxa/eukaryota/protomyces_lactucae_debilis.yaml data/taxa/eukaryota/protomycocladus_faisalabadensis.yaml data/taxa/eukaryota/protostelium_mycophagum.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:17429` is the exact retained NCBITaxon row for `NCBITaxon:101113`: label `Protomycocladus faisalabadensis`, rank `SPECIES`, parent `NCBITaxon:101112`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53639` contains the seeded in-scope row for `NCBITaxon:101113` with the reason `attested rule: Protomycocladus faisalabadensis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 1 related synonym, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:250` is the aggregate GOLD row for `NCBITaxon:101113` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, one linked project row, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:101113`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found three direct local JSONL records covering four exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:101113`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:101113`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with the aggregate GOLD row and the native GOLD organism row for `NRRL 22826`; the exact StrainInfo rows are not materialized in BacDive or generated StrainInfo overlays.
