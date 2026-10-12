# YAML Record Review: Pseudo-nitzschia pungens

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudo_nitzschia_pungens.yaml`
- Identifier: `NCBITaxon:37318`

## Target

Reviewed the complete 81-line YAML record for `Pseudo-nitzschia pungens`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudo_nitzschia_pungens`.

## Validation

- `just validate data/taxa/eukaryota/pseudo_nitzschia_pungens.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudo_nitzschia_multiseries.yaml data/taxa/eukaryota/pseudo_nitzschia_multistriata.yaml data/taxa/eukaryota/pseudo_nitzschia_pungens.yaml data/taxa/eukaryota/pseudocenococcum_floridanum.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4207` is the exact retained NCBITaxon row for `NCBITaxon:37318`: label `Pseudo-nitzschia pungens`, rank `SPECIES`, parent `NCBITaxon:41953`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52369` contains the seeded in-scope row for `NCBITaxon:37318` with the reason `attested rule: Pseudo-nitzschia pungens, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 3 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:37317` to `NCBITaxon:37318`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:33635` is the aggregate GOLD row for `NCBITaxon:37318` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, no linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:37318`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has one direct local JSONL record covering one exact deposit, `CCAP 1061/30`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:37318`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:37318`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

`NCBITaxon:37317` appears only as a retired old ID in `data/raw/ncbi_merged_ids.tsv` and not as a retained row in `data/raw/ncbitaxon_taxa.tsv`, matching the absence of a generated `replaces` value.
