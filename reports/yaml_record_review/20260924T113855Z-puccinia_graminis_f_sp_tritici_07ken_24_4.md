# YAML Record Review: Puccinia graminis f. sp. tritici 07KEN 24-4

- Verdict: pass
- Target: `data/taxa/eukaryota/puccinia_graminis_f_sp_tritici_07ken_24_4.yaml`
- Identifier: `NCBITaxon:626361`

## Target

Reviewed the complete 75-line YAML record for Puccinia graminis f. sp. tritici 07KEN 24-4. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `puccinia_graminis_f_sp_tritici_07ken_24_4`.

## Validation

- `just validate data/taxa/eukaryota/puccinia_graminis_f_sp_tritici_07ken_24_4.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/puccinia_graminis_f_sp_tritici_07ken_24_4.yaml data/taxa/eukaryota/puccinia_graminis_f_sp_tritici_126_6711.yaml data/taxa/eukaryota/puccinia_graminis_f_sp_tritici_194_12356.yaml data/taxa/eukaryota/puccinia_graminis_f_sp_tritici_21_0.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:144449` retains `NCBITaxon:626361` as `Puccinia graminis f. sp. tritici 07KEN 24-4`, rank `STRAIN`, parent `NCBITaxon:56615`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:56172`, with reason `attested rule: Puccinia graminis f. sp. tritici 07KEN 24-4, 2 sources incl. NCBI`.
- NCBI lists 1 exact synonym, 0 related synonyms, and 0 broad synonyms for the taxon: `Puccinia graminis f. sp. tritici 07KEN24-4` as exact.
- All 14 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- `data/raw/ncbi_merged_ids.tsv:6726` retires `NCBITaxon:1183175` into `NCBITaxon:626361`, but that old ID is absent from retained NCBI taxon rows and does not require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:39976` reports `organism_count: 1` for `NCBITaxon:626361`, matching the YAML source count.
- The native GOLD tables contain 2 organism rows, 2 project rows, and 0 analysis rows for this taxon.
- NCBI has 0 type-material rows for `NCBITaxon:626361`.
- Local StrainInfo records have 0 direct exact taxon rows and 0 exact deposit rows for `NCBITaxon:626361`.
- BacDive has 0 exact local rows for `NCBITaxon:626361`.

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

The single retired NCBI ID is not retained as a live taxon row, so no historical replacement assertion is generated for this strain.
