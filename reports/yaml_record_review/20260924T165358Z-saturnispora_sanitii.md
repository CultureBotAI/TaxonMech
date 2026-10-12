# YAML Record Review: Saturnispora sanitii

- Verdict: pass
- Target: `data/taxa/eukaryota/saturnispora_sanitii.yaml`
- Identifier: `NCBITaxon:714657`

## Target

Reviewed the complete 95-line YAML record for Saturnispora sanitii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saturnispora_sanitii.

## Validation

- `just validate data/taxa/eukaryota/saturnispora_sanitii.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saturnispora_mendoncae.yaml data/taxa/eukaryota/saturnispora_quitensis.yaml data/taxa/eukaryota/saturnispora_saitoi.yaml data/taxa/eukaryota/saturnispora_sanitii.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:168486` has `taxon_id=NCBITaxon:714657`, `label=Saturnispora sanitii`, `rank=SPECIES`, `parent_id=NCBITaxon:29834`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:714657` at `data/seed_scope.tsv:56545`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 1 exact synonym, 0 broad synonyms, and 7 related synonyms, matching the 8 YAML synonym entries.
- All 13 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- NCBI merged-ID rows retire `NCBITaxon:455148`, `NCBITaxon:455150`, `NCBITaxon:455152`, `NCBITaxon:455153`, and `NCBITaxon:455154` into `NCBITaxon:714657`, but exact old-ID checks found no retained rows in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:41885` reports `organism_count=1` for `NCBITaxon:714657`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 1 organism row, 1 project row, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 4 exact type-material rows for `NCBITaxon:714657`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 0 direct exact rows plus 0 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:714657`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:714657`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:714657`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
