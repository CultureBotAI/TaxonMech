# YAML Record Review: Pochonia chlamydosporia

- Verdict: pass
- Target: `data/taxa/eukaryota/pochonia_chlamydosporia.yaml`
- Identifier: `NCBITaxon:280754`

## Target

Reviewed the complete 125-line YAML record for `Pochonia chlamydosporia`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pochonia_chlamydosporia`.

## Validation

- `just validate data/taxa/eukaryota/pochonia_chlamydosporia.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/poaceascoma_sp.yaml data/taxa/eukaryota/pochonia_chlamydosporia.yaml data/taxa/eukaryota/podila_clonocystis.yaml data/taxa/eukaryota/podila_epicladia.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:57116` is the exact retained NCBITaxon row for `NCBITaxon:280754`: label `Pochonia chlamydosporia`, rank `SPECIES`, parent `NCBITaxon:243023`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54960` contains the seeded in-scope row for `NCBITaxon:280754` with the reason `attested rule: Pochonia chlamydosporia, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 9 exact synonyms, 6 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old IDs `NCBITaxon:132163`, `NCBITaxon:280753`, `NCBITaxon:282303`, and `NCBITaxon:40265` to `NCBITaxon:280754`, and exact retained NCBITaxon scans found no retained rows for those old IDs.

## Evidence

- `data/raw/gold_organisms.tsv:26914` is the aggregate GOLD row for `NCBITaxon:280754` and reports `organism_count=4`, matching the YAML GOLD source attestation.
- Native GOLD has three exact organism rows, five linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:280754`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has 51 exact strain records covering 67 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:280754`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:280754`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

One additional StrainInfo JSONL row has a `Pochonia chlamydosporia var. catenulata` strain with a `Verticillium catenulatum` deposit; it was counted only in the exact-deposit total. The generated GOLD source attestation uses the aggregate GOLD row rather than the smaller local native GOLD organism row count.
