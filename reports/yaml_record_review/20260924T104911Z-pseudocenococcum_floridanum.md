# YAML Record Review: Pseudocenococcum floridanum

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudocenococcum_floridanum.yaml`
- Identifier: `NCBITaxon:2022479`

## Target

Reviewed the complete 106-line YAML record for `Pseudocenococcum floridanum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudocenococcum_floridanum`.

## Validation

- `just validate data/taxa/eukaryota/pseudocenococcum_floridanum.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudo_nitzschia_multiseries.yaml data/taxa/eukaryota/pseudo_nitzschia_multistriata.yaml data/taxa/eukaryota/pseudo_nitzschia_pungens.yaml data/taxa/eukaryota/pseudocenococcum_floridanum.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:511405` is the exact retained NCBITaxon row for `NCBITaxon:2022479`: label `Pseudocenococcum floridanum`, rank `SPECIES`, parent `NCBITaxon:2022478`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:61959` contains the seeded in-scope row for `NCBITaxon:2022479` with the reason `attested rule: Pseudocenococcum floridanum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 9 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old IDs `NCBITaxon:1751036`, `NCBITaxon:1751037`, `NCBITaxon:1751038`, `NCBITaxon:1751039`, `NCBITaxon:1751040`, `NCBITaxon:1751041`, `NCBITaxon:1751042`, and `NCBITaxon:1751043` to `NCBITaxon:2022479`, and exact retained NCBITaxon scans found no retained rows for those old IDs.

## Evidence

- `data/raw/gold_organisms.tsv:18853` is the aggregate GOLD row for `NCBITaxon:2022479` and reports `organism_count=3`, matching the YAML GOLD source attestation.
- Native GOLD has no exact organism rows, linked project rows, or linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:78408` through `data/raw/ncbi_type_material.tsv:78415` provide eight exact type-material aliases, split between four `culture from holotype` rows, two `culture from isotype` rows, and two `holotype` rows.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2022479`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2022479`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

All eight merged old IDs appear only in `data/raw/ncbi_merged_ids.tsv` and not as retained rows in `data/raw/ncbitaxon_taxa.tsv`, matching the absence of generated `replaces` values. The generated GOLD source attestation is backed by the aggregate GOLD row, with no exact native GOLD rows in the local scan.
