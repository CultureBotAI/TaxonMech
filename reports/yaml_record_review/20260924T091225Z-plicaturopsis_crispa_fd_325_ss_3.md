# YAML Record Review: Plicaturopsis crispa FD-325 SS-3

- Verdict: pass
- Target: `data/taxa/eukaryota/plicaturopsis_crispa_fd_325_ss_3.yaml`
- Identifier: `NCBITaxon:944288`

## Target

Reviewed the complete 75-line YAML record for `Plicaturopsis crispa FD-325 SS-3`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plicaturopsis_crispa_fd_325_ss_3`.

## Validation

- `just validate data/taxa/eukaryota/plicaturopsis_crispa_fd_325_ss_3.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pleurotus_sp.yaml data/taxa/eukaryota/pleurotus_tuber_regium.yaml data/taxa/eukaryota/pleurotus_tuoliensis.yaml data/taxa/eukaryota/plicaturopsis_crispa_fd_325_ss_3.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:201677` is the exact retained NCBITaxon row for `NCBITaxon:944288`: label `Plicaturopsis crispa FD-325 SS-3`, rank `STRAIN`, parent `NCBITaxon:2831993`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:57016` contains the seeded in-scope row for `NCBITaxon:944288` with the reason `attested rule: Plicaturopsis crispa FD-325 SS-3, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 0 related synonyms, and 0 broad synonyms.
- All 14 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:944288`.

## Evidence

- `data/raw/gold_organisms.tsv:44988` is the aggregate GOLD row for `NCBITaxon:944288` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, three linked project rows, and two linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:944288`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:944288`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:944288`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

Although this is a strain-rank NCBITaxon record, no BacDive or StrainInfo rows materialized into the generated strain tables. The generated GOLD source attestation uses the aggregate GOLD row even though the local native GOLD files carry two exact organism rows for this NCBI taxon.
