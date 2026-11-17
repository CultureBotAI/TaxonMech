# YAML Record Review: Pleurotus opuntiae

- Verdict: pass
- Target: `data/taxa/eukaryota/pleurotus_opuntiae.yaml`
- Identifier: `NCBITaxon:228222`

## Target

Reviewed the complete 81-line YAML record for `Pleurotus opuntiae`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pleurotus_opuntiae`.

## Validation

- `just validate data/taxa/eukaryota/pleurotus_opuntiae.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pleurotus_floridanus.yaml data/taxa/eukaryota/pleurotus_fuscosquamulosus.yaml data/taxa/eukaryota/pleurotus_nebrodensis.yaml data/taxa/eukaryota/pleurotus_opuntiae.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:44710` is the exact retained NCBITaxon row for `NCBITaxon:228222`: label `Pleurotus opuntiae`, rank `SPECIES`, parent `NCBITaxon:5320`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54630` contains the seeded in-scope row for `NCBITaxon:228222` with the reason `attested rule: Pleurotus opuntiae, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 14 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:228222`.

## Evidence

- `data/raw/gold_organisms.tsv:21402` is the aggregate GOLD row for `NCBITaxon:228222` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has no exact organism, project, or analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:228222`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found five exact local JSONL records covering six deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:228222`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:228222`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows, so the generated YAML correctly remains a zero-strain record. The generated GOLD source attestation uses the aggregate GOLD row even though the local native GOLD organism, project, and analysis files have no exact rows for this NCBI taxon.
