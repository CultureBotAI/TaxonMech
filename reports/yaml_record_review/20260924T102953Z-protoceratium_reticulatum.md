# YAML Record Review: Protoceratium reticulatum

- Verdict: pass
- Target: `data/taxa/eukaryota/protoceratium_reticulatum.yaml`
- Identifier: `NCBITaxon:133427`

## Target

Reviewed the complete 63-line YAML record for `Protoceratium reticulatum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `protoceratium_reticulatum`.

## Validation

- `just validate data/taxa/eukaryota/protoceratium_reticulatum.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/proteomonas_sulcata.yaml data/taxa/eukaryota/protoceratium_reticulatum.yaml data/taxa/eukaryota/protocrea_farinosa.yaml data/taxa/eukaryota/protocrea_pallida.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:25945` is the exact retained NCBITaxon row for `NCBITaxon:133427`: label `Protoceratium reticulatum`, rank `SPECIES`, parent `NCBITaxon:133426`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53955` contains the seeded in-scope row for `NCBITaxon:133427` with the reason `attested rule: Protoceratium reticulatum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 1 related synonym, and 0 broad synonyms.
- All 9 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:8117` is the aggregate GOLD row for `NCBITaxon:133427` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, no linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:133427`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found five direct local JSONL records covering five exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:133427`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:133427`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with the aggregate GOLD row and the single native GOLD organism row for `CCCM 535`. Exact StrainInfo evidence is present for five rows, but none were materialized into generated StrainInfo overlays.
