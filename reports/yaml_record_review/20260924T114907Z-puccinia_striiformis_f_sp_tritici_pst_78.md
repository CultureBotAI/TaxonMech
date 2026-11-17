# YAML Record Review: Puccinia striiformis f. sp. tritici PST-78

- Verdict: pass
- Target: `data/taxa/eukaryota/puccinia_striiformis_f_sp_tritici_pst_78.yaml`
- Identifier: `NCBITaxon:1165861`

## Target

Reviewed the complete 78-line YAML record for Puccinia striiformis f. sp. tritici PST-78. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `puccinia_striiformis_f_sp_tritici_pst_78`.

## Validation

- `just validate data/taxa/eukaryota/puccinia_striiformis_f_sp_tritici_pst_78.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/puccinia_striiformis_f_sp_tritici.yaml data/taxa/eukaryota/puccinia_striiformis_f_sp_tritici_pst_78.yaml data/taxa/eukaryota/puccinia_triticina_1_1_bbbd_race_1.yaml data/taxa/eukaryota/puccinia_triticina_race_77.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:257242` retains `NCBITaxon:1165861` as `Puccinia striiformis f. sp. tritici PST-78`, rank `STRAIN`, parent `NCBITaxon:168172`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:58089`, with reason `attested rule: Puccinia striiformis f. sp. tritici PST-78, 2 sources incl. NCBI`.
- NCBI lists 2 exact synonyms, 0 related synonyms, and 0 broad synonyms for the taxon, matching the 2 synonym assertions in the YAML.
- All 14 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- `data/raw/ncbi_merged_ids.tsv:92124` retires `NCBITaxon:683838` into `NCBITaxon:1165861`, but that old ID is absent from retained NCBI taxon rows and does not require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:3519` reports `organism_count: 1` for `NCBITaxon:1165861`, matching the YAML source count.
- The native GOLD tables contain 2 organism rows, 2 project rows, and 1 analysis row for this taxon.
- NCBI has 0 type-material rows for `NCBITaxon:1165861`.
- Local StrainInfo records have 0 direct exact taxon rows and 0 exact deposit rows for `NCBITaxon:1165861`.
- BacDive has 0 exact local rows for `NCBITaxon:1165861`.

## Completeness

- Generated raw strain tables contain 0 target rows across `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary generated sources contain 0 target rows across BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive.
- Generated StrainInfo overlays contain 0 rows across `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- The YAML correctly carries `strain_count: 0`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The retired `NCBITaxon:683838` identifier is not retained as a live NCBI taxon row, so it does not alter the generated YAML.
