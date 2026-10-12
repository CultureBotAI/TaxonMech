# YAML Record Review: Puccinia triticina 1-1 BBBD Race 1

- Verdict: pass
- Target: `data/taxa/eukaryota/puccinia_triticina_1_1_bbbd_race_1.yaml`
- Identifier: `NCBITaxon:630390`

## Target

Reviewed the complete 68-line YAML record for Puccinia triticina 1-1 BBBD Race 1. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `puccinia_triticina_1_1_bbbd_race_1`.

## Validation

- `just validate data/taxa/eukaryota/puccinia_triticina_1_1_bbbd_race_1.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/puccinia_striiformis_f_sp_tritici.yaml data/taxa/eukaryota/puccinia_striiformis_f_sp_tritici_pst_78.yaml data/taxa/eukaryota/puccinia_triticina_1_1_bbbd_race_1.yaml data/taxa/eukaryota/puccinia_triticina_race_77.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:145167` retains `NCBITaxon:630390` as `Puccinia triticina 1-1 BBBD Race 1`, rank `STRAIN`, parent `NCBITaxon:208348`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:56179`, with reason `attested rule: Puccinia triticina 1-1 BBBD Race 1, 2 sources incl. NCBI`.
- NCBI lists 0 exact synonyms, 0 related synonyms, and 0 broad synonyms for the taxon, matching the absence of a synonym block in the YAML.
- All 13 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- The NCBI merged-ID table has no rows that retire an old identifier into `NCBITaxon:630390`, and no retained old IDs require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:40042` reports `organism_count: 1` for `NCBITaxon:630390`, matching the YAML source count.
- The native GOLD tables contain 2 organism rows, 2 project rows, and 1 analysis row for this taxon.
- NCBI has 0 type-material rows for `NCBITaxon:630390`.
- Local StrainInfo records have 0 direct exact taxon rows and 0 exact deposit rows for `NCBITaxon:630390`.
- BacDive has 0 exact local rows for `NCBITaxon:630390`.

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

No type-material, StrainInfo, BacDive, auxiliary, or merged-ID rows surfaced for this Puccinia triticina strain.
