# YAML Record Review: Plasmopara halstedii

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmopara_halstedii.yaml`
- Identifier: `NCBITaxon:4781`

## Target

Reviewed the complete 69-line YAML record for `Plasmopara halstedii`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmopara_halstedii`.

## Validation

- `just validate data/taxa/eukaryota/plasmopara_halstedii.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plasmodium_yoelii.yaml data/taxa/eukaryota/plasmodium_yoelii_killicki.yaml data/taxa/eukaryota/plasmodium_yoelii_nigeriensis.yaml data/taxa/eukaryota/plasmopara_halstedii.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2056` is the exact retained NCBITaxon row for `NCBITaxon:4781`: label `Plasmopara halstedii`, rank `SPECIES`, parent `NCBITaxon:4780`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:51842` contains the seeded in-scope row for `NCBITaxon:4781` with the reason `attested rule: Plasmopara halstedii, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 10 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:4781`.

## Evidence

- `data/raw/gold_organisms.tsv:36625` is the aggregate GOLD row for `NCBITaxon:4781` and reports `organism_count=6`, matching the YAML GOLD source attestation.
- Native GOLD has five exact organism rows, five linked project rows, and five linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:4781`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:4781`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:4781`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The aggregate GOLD inventory reports 6 organisms, while the local native GOLD organism JSONL has 5 exact rows for this NCBI taxon; generated GOLD source attestations use the aggregate row.
