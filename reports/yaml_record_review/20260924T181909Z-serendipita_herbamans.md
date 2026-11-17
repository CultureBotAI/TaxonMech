# YAML Record Review: Serendipita herbamans

- Verdict: pass
- Target: `data/taxa/eukaryota/serendipita_herbamans.yaml`
- Identifier: `NCBITaxon:1505950`

## Target

Reviewed the complete 75-line YAML record for Serendipita herbamans. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for serendipita_herbamans.

## Validation

- `just validate data/taxa/eukaryota/serendipita_herbamans.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/seminavis_robusta.yaml data/taxa/eukaryota/sepedonium_ampullosporum.yaml data/taxa/eukaryota/septobasidium_canescens.yaml data/taxa/eukaryota/serendipita_herbamans.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:386757` has `taxon_id=NCBITaxon:1505950`, `label=Serendipita herbamans`, `rank=SPECIES`, `parent_id=NCBITaxon:358905`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:1505950` at `data/seed_scope.tsv:60352`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 0 exact synonyms, 0 broad synonyms, and 2 related synonyms, matching the 2 YAML synonym entries.
- All 13 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `data/raw/ncbi_merged_ids.tsv:13197` maps old ID `NCBITaxon:1349590` into `NCBITaxon:1505950`, and an ignored-file-inclusive exact scan found no retained old-ID row in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:11824` reports `organism_count=2` for `NCBITaxon:1505950`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 2 organism rows, 0 project rows, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 4 exact type-material rows for `NCBITaxon:1505950`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 1 direct exact row plus 1 exact deposit cross-reference for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:1505950`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:1505950`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:1505950`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
