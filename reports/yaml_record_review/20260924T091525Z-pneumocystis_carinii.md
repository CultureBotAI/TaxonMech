# YAML Record Review: Pneumocystis carinii

- Verdict: pass
- Target: `data/taxa/eukaryota/pneumocystis_carinii.yaml`
- Identifier: `NCBITaxon:4754`

## Target

Reviewed the complete 75-line YAML record for `Pneumocystis carinii`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pneumocystis_carinii`.

## Validation

- `just validate data/taxa/eukaryota/pneumocystis_carinii.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plocamium_pacificum.yaml data/taxa/eukaryota/pluteus_cervinus.yaml data/taxa/eukaryota/pneumocystis_canis.yaml data/taxa/eukaryota/pneumocystis_carinii.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2040` is the exact retained NCBITaxon row for `NCBITaxon:4754`: label `Pneumocystis carinii`, rank `SPECIES`, parent `NCBITaxon:4753`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:51837` contains the seeded in-scope row for `NCBITaxon:4754` with the reason `attested rule: Pneumocystis carinii, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:38081` to `NCBITaxon:4754`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:36554` is the aggregate GOLD row for `NCBITaxon:4754` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has three exact organism rows, three linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:4754`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has one exact strain record covering one exact deposit.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:4754`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:4754`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hit has no corresponding BacDive or generated StrainInfo overlay row, so the generated YAML correctly remains a zero-strain record. The generated GOLD source attestation uses the aggregate GOLD row even though the local native GOLD organism count is three for this NCBI taxon.
