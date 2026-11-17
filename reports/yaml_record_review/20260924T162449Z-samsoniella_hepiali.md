# YAML Record Review: Samsoniella hepiali

- Verdict: pass
- Target: `data/taxa/eukaryota/samsoniella_hepiali.yaml`
- Identifier: `NCBITaxon:797268`

## Target

Reviewed the complete 92-line YAML record for Samsoniella hepiali. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for samsoniella_hepiali.

## Validation

- `just validate data/taxa/eukaryota/samsoniella_hepiali.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sampaiozyma_vanillica.yaml data/taxa/eukaryota/samsoniella_hepiali.yaml data/taxa/eukaryota/sanghuangporus_baumii.yaml data/taxa/eukaryota/sanghuangporus_sanghuang.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:179879` has `taxon_id=NCBITaxon:797268`, `label=Samsoniella hepiali`, `rank=SPECIES`, `parent_id=NCBITaxon:2591471`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:797268` at `data/seed_scope.tsv:56717`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 1 exact synonym, 0 broad synonyms, and 3 related synonyms, matching the 4 YAML synonym entries.
- All 16 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `data/raw/ncbi_merged_ids.tsv` contains 1 retired ID that merges into `NCBITaxon:797268`: `NCBITaxon:491086` at line 81748. An exact old-ID check found no retained row for it in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:42838` reports `organism_count=1` for `NCBITaxon:797268`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 1 organism row, 1 project row, and 1 analysis row.
- `data/raw/ncbi_type_material.tsv` contains 4 exact type-material rows for `NCBITaxon:797268`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 5 direct exact rows plus 5 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:797268`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:797268`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:797268`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
