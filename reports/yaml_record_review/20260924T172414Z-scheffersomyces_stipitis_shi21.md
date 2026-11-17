# YAML Record Review: Scheffersomyces stipitis Shi21

- Verdict: pass
- Target: `data/taxa/eukaryota/scheffersomyces_stipitis_shi21.yaml`
- Identifier: `NCBITaxon:564619`

## Target

Reviewed the complete 75-line YAML record for Scheffersomyces stipitis Shi21. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for scheffersomyces_stipitis_shi21.

## Validation

- `just validate data/taxa/eukaryota/scheffersomyces_stipitis_shi21.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/scheffersomyces_stambukii.yaml data/taxa/eukaryota/scheffersomyces_stipitis.yaml data/taxa/eukaryota/scheffersomyces_stipitis_shi21.yaml data/taxa/eukaryota/scheffersomyces_titani.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:133065` has `taxon_id=NCBITaxon:564619`, `label=Scheffersomyces stipitis Shi21`, `rank=STRAIN`, `parent_id=NCBITaxon:4924`, `genetic_code=12`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:564619` at `data/seed_scope.tsv:56051`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 1 exact synonym, 0 broad synonyms, and 0 related synonyms, matching the 1 YAML synonym entry.
- All 14 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `NCBITaxon:564619` has no retired NCBI IDs merged into it, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:38950` reports `organism_count=1` for `NCBITaxon:564619`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 1 organism row, 1 project row, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 0 exact type-material rows for `NCBITaxon:564619`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 0 direct exact rows plus 0 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:564619`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:564619`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:564619`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
