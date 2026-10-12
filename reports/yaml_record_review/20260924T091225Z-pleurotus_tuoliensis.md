# YAML Record Review: Pleurotus tuoliensis

- Verdict: pass
- Target: `data/taxa/eukaryota/pleurotus_tuoliensis.yaml`
- Identifier: `NCBITaxon:879823`

## Target

Reviewed the complete 84-line YAML record for `Pleurotus tuoliensis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pleurotus_tuoliensis`.

## Validation

- `just validate data/taxa/eukaryota/pleurotus_tuoliensis.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pleurotus_sp.yaml data/taxa/eukaryota/pleurotus_tuber_regium.yaml data/taxa/eukaryota/pleurotus_tuoliensis.yaml data/taxa/eukaryota/plicaturopsis_crispa_fd_325_ss_3.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:187148` is the exact retained NCBITaxon row for `NCBITaxon:879823`: label `Pleurotus tuoliensis`, rank `SPECIES`, parent `NCBITaxon:5320`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:56820` contains the seeded in-scope row for `NCBITaxon:879823` with the reason `attested rule: Pleurotus tuoliensis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 14 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:879823`.

## Evidence

- `data/raw/gold_organisms.tsv:43733` is the aggregate GOLD row for `NCBITaxon:879823` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, one linked project row, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:879823`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:879823`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:879823`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with both the aggregate GOLD row and the native GOLD row for `Pleurotus tuoliensis MG79`. No exact BacDive, StrainInfo, or type-material evidence needed to be materialized into the zero-strain YAML.
