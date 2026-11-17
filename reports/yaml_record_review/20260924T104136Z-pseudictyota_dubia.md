# YAML Record Review: Pseudictyota dubia

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudictyota_dubia.yaml`
- Identifier: `NCBITaxon:2749911`

## Target

Reviewed the complete 81-line YAML record for `Pseudictyota dubia`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudictyota_dubia`.

## Validation

- `just validate data/taxa/eukaryota/pseudictyota_dubia.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudauliscus_ralfsianus.yaml data/taxa/eukaryota/pseudevernia_furfuracea.yaml data/taxa/eukaryota/pseudictyota_dubia.yaml data/taxa/eukaryota/pseudo_nitzschia_arenysensis.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:550675` is the exact retained NCBITaxon row for `NCBITaxon:2749911`: label `Pseudictyota dubia`, rank `SPECIES`, parent `NCBITaxon:2749910`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:63191` contains the seeded in-scope row for `NCBITaxon:2749911` with the reason `attested rule: Pseudictyota dubia, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:1003142` to `NCBITaxon:2749911`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:25905` is the aggregate GOLD row for `NCBITaxon:2749911` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has no exact organism rows, linked project rows, or linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:2749911`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has one direct local JSONL record covering one exact deposit, `NIES-556`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2749911`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2749911`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

`NCBITaxon:1003142` appears only as a retired old ID in `data/raw/ncbi_merged_ids.tsv` and not as a retained row in `data/raw/ncbitaxon_taxa.tsv`, matching the absence of a generated `replaces` value. The generated GOLD source attestation is backed by the aggregate GOLD row, with no exact native GOLD rows in the local scan.
