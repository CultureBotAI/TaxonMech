# YAML Record Review: Polychytrium aggregatum

- Verdict: pass
- Target: `data/taxa/eukaryota/polychytrium_aggregatum.yaml`
- Identifier: `NCBITaxon:110093`

## Target

Reviewed the complete 72-line YAML record for `Polychytrium aggregatum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `polychytrium_aggregatum`.

## Validation

- `just validate data/taxa/eukaryota/polychytrium_aggregatum.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/polychaeton_citri.yaml data/taxa/eukaryota/polychytrium_aggregatum.yaml data/taxa/eukaryota/polymyxa_betae.yaml data/taxa/eukaryota/polyphilus_sieberi.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:19754` is the exact retained NCBITaxon row for `NCBITaxon:110093`: label `Polychytrium aggregatum`, rank `SPECIES`, parent `NCBITaxon:110092`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53757` contains the seeded in-scope row for `NCBITaxon:110093` with the reason `attested rule: Polychytrium aggregatum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:1854` is the aggregate GOLD row for `NCBITaxon:110093` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, two linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has four exact reference-material rows for `NCBITaxon:110093`, filed under `Polychytrium aggregatum`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:110093`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:110093`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact type-material rows cover NCBI reference-material designations for `AFTOL-ID 24`, `AFTOL-ID:24`, `JEL 109`, and `JEL:109`, and no BacDive or StrainInfo evidence needed to be materialized into the zero-strain YAML.
