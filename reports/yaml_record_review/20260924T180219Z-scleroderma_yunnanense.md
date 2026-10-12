# YAML Record Review: Scleroderma yunnanense

- Verdict: pass
- Target: `data/taxa/eukaryota/scleroderma_yunnanense.yaml`
- Identifier: `NCBITaxon:1163567`

## Target

Reviewed the complete 78-line YAML record for Scleroderma yunnanense. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for scleroderma_yunnanense.

## Validation

- `just validate data/taxa/eukaryota/scleroderma_yunnanense.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/scleroderma_citrinum.yaml data/taxa/eukaryota/scleroderma_sp.yaml data/taxa/eukaryota/scleroderma_yunnanense.yaml data/taxa/eukaryota/sclerogaster_hysterangioides.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:256056` has `taxon_id=NCBITaxon:1163567`, `label=Scleroderma yunnanense`, `rank=SPECIES`, `parent_id=NCBITaxon:68787`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:1163567` at `data/seed_scope.tsv:58083`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 0 exact synonyms, 0 broad synonyms, and 2 related synonyms, matching the 2 YAML synonym entries.
- All 14 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `NCBITaxon:1163567` has no retired NCBI IDs merged into it, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:3500` reports `organism_count=1` for `NCBITaxon:1163567`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 1 organism row, 2 project rows, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 10 exact type-material rows for `NCBITaxon:1163567`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 0 direct exact rows plus 0 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:1163567`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:1163567`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:1163567`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
