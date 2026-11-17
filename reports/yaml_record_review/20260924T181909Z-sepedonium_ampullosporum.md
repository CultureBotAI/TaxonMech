# YAML Record Review: Sepedonium ampullosporum

- Verdict: pass
- Target: `data/taxa/eukaryota/sepedonium_ampullosporum.yaml`
- Identifier: `NCBITaxon:74838`

## Target

Reviewed the complete 81-line YAML record for Sepedonium ampullosporum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for sepedonium_ampullosporum.

## Validation

- `just validate data/taxa/eukaryota/sepedonium_ampullosporum.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/seminavis_robusta.yaml data/taxa/eukaryota/sepedonium_ampullosporum.yaml data/taxa/eukaryota/septobasidium_canescens.yaml data/taxa/eukaryota/serendipita_herbamans.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:10647` has `taxon_id=NCBITaxon:74838`, `label=Sepedonium ampullosporum`, `rank=SPECIES`, `parent_id=NCBITaxon:74837`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:74838` at `data/seed_scope.tsv:53272`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 0 exact synonyms, 0 broad synonyms, and 1 related synonym, matching the 1 YAML synonym entry.
- All 16 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `NCBITaxon:74838` has no retired NCBI IDs merged into it, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:42253` reports `organism_count=2` for `NCBITaxon:74838`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 0 organism rows, 0 project rows, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 8 exact type-material rows for `NCBITaxon:74838`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 15 direct exact rows plus 20 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:74838`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:74838`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:74838`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
