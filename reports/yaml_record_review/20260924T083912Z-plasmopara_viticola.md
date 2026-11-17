# YAML Record Review: Plasmopara viticola

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmopara_viticola.yaml`
- Identifier: `NCBITaxon:143451`

## Target

Reviewed the complete 59-line YAML record for `Plasmopara viticola`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmopara_viticola`.

## Validation

- `just validate data/taxa/eukaryota/plasmopara_viticola.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plasmopara_muralis.yaml data/taxa/eukaryota/plasmopara_obducens.yaml data/taxa/eukaryota/plasmopara_viticola.yaml data/taxa/eukaryota/platygloea_disciformis.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:29047` is the exact retained NCBITaxon row for `NCBITaxon:143451`: label `Plasmopara viticola`, rank `SPECIES`, parent `NCBITaxon:4780`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54020` contains the seeded in-scope row for `NCBITaxon:143451` with the reason `attested rule: Plasmopara viticola, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 0 related synonyms, and 0 broad synonyms.
- All 10 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:143451`.

## Evidence

- `data/raw/gold_organisms.tsv:10358` is the aggregate GOLD row for `NCBITaxon:143451` and reports `organism_count=3`, matching the YAML GOLD source attestation.
- Native GOLD has four exact organism rows, four linked project rows, and three linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:143451`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:143451`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:143451`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The aggregate GOLD inventory reports 3 organisms, while the local native GOLD organism JSONL has 4 exact rows for this NCBI taxon; generated GOLD source attestations use the aggregate row.
