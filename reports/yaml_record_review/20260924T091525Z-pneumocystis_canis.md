# YAML Record Review: Pneumocystis canis

- Verdict: pass
- Target: `data/taxa/eukaryota/pneumocystis_canis.yaml`
- Identifier: `NCBITaxon:2698477`

## Target

Reviewed the complete 75-line YAML record for `Pneumocystis canis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pneumocystis_canis`.

## Validation

- `just validate data/taxa/eukaryota/pneumocystis_canis.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plocamium_pacificum.yaml data/taxa/eukaryota/pluteus_cervinus.yaml data/taxa/eukaryota/pneumocystis_canis.yaml data/taxa/eukaryota/pneumocystis_carinii.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:544779` is the exact retained NCBITaxon row for `NCBITaxon:2698477`: label `Pneumocystis canis`, rank `SPECIES`, parent `NCBITaxon:4753`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:62956` contains the seeded in-scope row for `NCBITaxon:2698477` with the reason `attested rule: Pneumocystis canis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:2736207` to `NCBITaxon:2698477`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:24953` is the aggregate GOLD row for `NCBITaxon:2698477` and reports `organism_count=3`, matching the YAML GOLD source attestation.
- Native GOLD has three exact organism rows, three linked project rows, and three linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:2698477`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2698477`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2698477`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The three exact native GOLD organism rows match the aggregate GOLD `organism_count=3` attestation. No exact BacDive, StrainInfo, or type-material evidence needed to be materialized into the zero-strain YAML.
