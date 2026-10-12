# YAML Record Review: Polyphilus sieberi

- Verdict: pass
- Target: `data/taxa/eukaryota/polyphilus_sieberi.yaml`
- Identifier: `NCBITaxon:2137868`

## Target

Reviewed the complete 81-line YAML record for `Polyphilus sieberi`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `polyphilus_sieberi`.

## Validation

- `just validate data/taxa/eukaryota/polyphilus_sieberi.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/polychaeton_citri.yaml data/taxa/eukaryota/polychytrium_aggregatum.yaml data/taxa/eukaryota/polymyxa_betae.yaml data/taxa/eukaryota/polyphilus_sieberi.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:519003` is the exact retained NCBITaxon row for `NCBITaxon:2137868`: label `Polyphilus sieberi`, rank `SPECIES`, parent `NCBITaxon:2316363`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:62378` contains the seeded in-scope row for `NCBITaxon:2137868` with the reason `attested rule: Polyphilus sieberi, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 15 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:20324` is the aggregate GOLD row for `NCBITaxon:2137868` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, two linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has three exact type-material rows for `NCBITaxon:2137868`, filed under `Polyphilus sieberi`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2137868`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2137868`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact type-material rows are two culture-from-holotype designations for `DSM 106515` and `DSM:106515`, plus the `BP:109051` holotype designation. No exact BacDive or StrainInfo evidence needed to be materialized into the zero-strain YAML.
