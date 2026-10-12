# YAML Record Review: Puccinia striiformis

- Verdict: pass
- Target: `data/taxa/eukaryota/puccinia_striiformis.yaml`
- Identifier: `NCBITaxon:27350`

## Target

Reviewed the complete 70-line YAML record for Puccinia striiformis. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `puccinia_striiformis`.

## Validation

- `just validate data/taxa/eukaryota/puccinia_striiformis.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/puccinia_graminis_f_sp_tritici_uvpgt59.yaml data/taxa/eukaryota/puccinia_horiana.yaml data/taxa/eukaryota/puccinia_sorghi.yaml data/taxa/eukaryota/puccinia_striiformis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:2748` retains `NCBITaxon:27350` as `Puccinia striiformis`, rank `SPECIES`, parent `NCBITaxon:5296`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:52162`, with reason `attested rule: Puccinia striiformis, 2 sources incl. NCBI`.
- NCBI lists 0 exact synonyms, 1 related synonym, and 0 broad synonyms for the taxon: `Puccinia striiformis Westend., 1854` as related.
- All 12 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- The NCBI merged-ID table has no rows that retire an old identifier into `NCBITaxon:27350`, and no retained old IDs require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:25501` reports `organism_count: 5` for `NCBITaxon:27350`, matching the YAML source count and its direct-record note.
- The native GOLD tables contain 5 organism rows, 5 project rows, and 5 analysis rows for this taxon.
- NCBI has 0 type-material rows for `NCBITaxon:27350`.
- Local StrainInfo records have 0 direct exact taxon rows and 0 exact deposit rows for `NCBITaxon:27350`.
- BacDive has 0 exact local rows for `NCBITaxon:27350`.

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

The GOLD aggregate includes only records filed directly under this species; descendant forma specialis and strain taxa are intentionally not gathered into the YAML count.
