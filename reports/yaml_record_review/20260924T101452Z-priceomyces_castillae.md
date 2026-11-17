# YAML Record Review: Priceomyces castillae

- Verdict: pass
- Target: `data/taxa/eukaryota/priceomyces_castillae.yaml`
- Identifier: `NCBITaxon:45501`

## Target

Reviewed the complete 82-line YAML record for `Priceomyces castillae`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `priceomyces_castillae`.

## Validation

- `just validate data/taxa/eukaryota/priceomyces_castillae.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/powellomyces_hirtus.yaml data/taxa/eukaryota/preussia_procaviae.yaml data/taxa/eukaryota/priceomyces_carsonii.yaml data/taxa/eukaryota/priceomyces_castillae.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:5573` is the exact retained NCBITaxon row for `NCBITaxon:45501`: label `Priceomyces castillae`, rank `SPECIES`, parent `NCBITaxon:766759`, genetic code `12`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52619` contains the seeded in-scope row for `NCBITaxon:45501` with the reason `attested rule: Priceomyces castillae, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:36016` is the aggregate GOLD row for `NCBITaxon:45501` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, two linked project rows, and two linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:214541` through `data/raw/ncbi_type_material.tsv:214554` provide 14 exact type-material aliases, split between seven `culture from type material` rows and seven `type material` rows.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found two direct local JSONL records covering 12 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:45501`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:45501`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with the aggregate GOLD row and the single native GOLD organism row for `NRRL Y-7501`; GOLD then links that one organism row to two native project rows and two native analysis rows.
