# YAML Record Review: Puccinia striiformis f. sp. tritici

- Verdict: pass
- Target: `data/taxa/eukaryota/puccinia_striiformis_f_sp_tritici.yaml`
- Identifier: `NCBITaxon:168172`

## Target

Reviewed the complete 69-line YAML record for Puccinia striiformis f. sp. tritici. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `puccinia_striiformis_f_sp_tritici`.

## Validation

- `just validate data/taxa/eukaryota/puccinia_striiformis_f_sp_tritici.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/puccinia_striiformis_f_sp_tritici.yaml data/taxa/eukaryota/puccinia_striiformis_f_sp_tritici_pst_78.yaml data/taxa/eukaryota/puccinia_triticina_1_1_bbbd_race_1.yaml data/taxa/eukaryota/puccinia_triticina_race_77.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:34382` retains `NCBITaxon:168172` as `Puccinia striiformis f. sp. tritici`, rank `FORMA_SPECIALIS`, parent `NCBITaxon:27350`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:54242`, with reason `attested rule: Puccinia striiformis f. sp. tritici, 2 sources incl. NCBI`.
- NCBI lists 0 exact synonyms, 0 related synonyms, and 0 broad synonyms for the taxon, matching the absence of a synonym block in the YAML.
- All 13 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- The NCBI merged-ID table has no rows that retire an old identifier into `NCBITaxon:168172`, and no retained old IDs require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:14499` reports `organism_count: 4` for `NCBITaxon:168172`, matching the YAML source count and its direct-record note.
- The native GOLD tables contain 4 organism rows, 4 project rows, and 2 analysis rows for this taxon.
- NCBI has 0 type-material rows for `NCBITaxon:168172`.
- Local StrainInfo records have 0 direct exact taxon rows and 0 exact deposit rows for `NCBITaxon:168172`.
- BacDive has 0 exact local rows for `NCBITaxon:168172`.

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

The aggregate contains only organisms filed directly under this forma specialis; descendant strain rows are intentionally excluded from the YAML count.
