# YAML Record Review: Schwanniomyces polymorphus var. polymorphus

- Verdict: pass
- Target: `data/taxa/eukaryota/schwanniomyces_polymorphus_var_polymorphus.yaml`
- Identifier: `NCBITaxon:251372`

## Target

Reviewed the complete 83-line YAML record for Schwanniomyces polymorphus var. polymorphus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for schwanniomyces_polymorphus_var_polymorphus.

## Validation

- `just validate data/taxa/eukaryota/schwanniomyces_polymorphus_var_polymorphus.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/schwanniomyces_occidentalis_var_persoonii.yaml data/taxa/eukaryota/schwanniomyces_polymorphus_var_africanus.yaml data/taxa/eukaryota/schwanniomyces_polymorphus_var_polymorphus.yaml data/taxa/eukaryota/schwanniomyces_pseudopolymorphus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:50712` has `taxon_id=NCBITaxon:251372`, `label=Schwanniomyces polymorphus var. polymorphus`, `rank=VARIETAS`, `parent_id=NCBITaxon:27301`, `genetic_code=12`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:251372` at `data/seed_scope.tsv:54759`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 1 exact synonym, 0 broad synonyms, and 2 related synonyms, matching the 3 YAML synonym entries.
- All 14 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `NCBITaxon:251372` has no retired NCBI IDs merged into it, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:22884` reports `organism_count=1` for `NCBITaxon:251372`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 1 organism row, 1 project row, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 16 exact type-material rows for `NCBITaxon:251372`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 11 direct exact rows plus 48 exact deposit cross-references for this taxon. The exact JSONL scan also found 6 non-direct `Schwanniomyces polymorphus` records carrying 20 deposit cross-references to `NCBITaxon:251372`.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:251372`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:251372`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:251372`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
