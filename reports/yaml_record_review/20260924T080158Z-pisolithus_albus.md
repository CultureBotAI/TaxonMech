# YAML Record Review: Pisolithus albus

- Verdict: pass
- Target: `data/taxa/eukaryota/pisolithus_albus.yaml`
- Identifier: `NCBITaxon:178870`

## Target

Reviewed the complete 81-line YAML record for `Pisolithus albus`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pisolithus_albus`.

## Validation

- `just validate data/taxa/eukaryota/pisolithus_albus.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/piskurozyma_tuonelana.yaml data/taxa/eukaryota/piskurozyma_yama.yaml data/taxa/eukaryota/pisolithus_albus.yaml data/taxa/eukaryota/pisolithus_calongei.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:35849` is the exact retained NCBITaxon row for `NCBITaxon:178870`: label `Pisolithus albus`, rank `SPECIES`, parent `NCBITaxon:37467`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54315` contains the seeded in-scope row for `NCBITaxon:178870` with the reason `attested rule: Pisolithus albus, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 14 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:178870`.

## Evidence

- `data/raw/gold_organisms.tsv:15624` is the aggregate GOLD row for `NCBITaxon:178870` and reports `organism_count=19`, matching the YAML GOLD source attestation.
- Native GOLD has 18 exact organism rows, 35 linked project rows, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv:59594` through `data/raw/ncbi_type_material.tsv:59595` contain the 2 exact NCBI type-material rows for `NCBITaxon:178870`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:178870`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:178870`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The aggregate GOLD inventory reports 19 organisms, while the local native GOLD organism JSONL has 18 exact rows for this NCBI taxon; generated GOLD source attestations use the aggregate row.
