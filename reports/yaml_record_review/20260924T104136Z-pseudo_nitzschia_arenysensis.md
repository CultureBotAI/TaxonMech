# YAML Record Review: Pseudo-nitzschia arenysensis

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudo_nitzschia_arenysensis.yaml`
- Identifier: `NCBITaxon:697910`

## Target

Reviewed the complete 69-line YAML record for `Pseudo-nitzschia arenysensis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudo_nitzschia_arenysensis`.

## Validation

- `just validate data/taxa/eukaryota/pseudo_nitzschia_arenysensis.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudauliscus_ralfsianus.yaml data/taxa/eukaryota/pseudevernia_furfuracea.yaml data/taxa/eukaryota/pseudictyota_dubia.yaml data/taxa/eukaryota/pseudo_nitzschia_arenysensis.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:163752` is the exact retained NCBITaxon row for `NCBITaxon:697910`: label `Pseudo-nitzschia arenysensis`, rank `SPECIES`, parent `NCBITaxon:41953`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:56460` contains the seeded in-scope row for `NCBITaxon:697910` with the reason `attested rule: Pseudo-nitzschia arenysensis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:41550` is the aggregate GOLD row for `NCBITaxon:697910` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, no linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:697910`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:697910`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:697910`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with the aggregate GOLD row and the single native GOLD organism row for `Pseudo-nitzschia arenysensis B593`. No exact BacDive, StrainInfo, or type-material evidence needed to be materialized into the zero-strain YAML.
