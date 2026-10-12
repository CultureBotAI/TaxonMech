# YAML Record Review: Sphaerodes sp. 'pseudofimicola'

- Verdict: pass
- Target: `data/taxa/eukaryota/sphaerodes_sp_pseudofimicola.yaml`
- Identifier: `NCBITaxon:1200297`

## Target

Reviewed the complete 87-line YAML record for Sphaerodes sp. 'pseudofimicola'. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for sphaerodes_sp_pseudofimicola.

## Validation

- `just validate data/taxa/eukaryota/sphaerodes_sp_pseudofimicola.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sphaerodes_sp_pseudofimicola.yaml data/taxa/eukaryota/sphaeroforma_sirkka.yaml data/taxa/eukaryota/sphaerosporella_brunnea.yaml data/taxa/eukaryota/sphaerostilbella_broomeana.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:270988` has `taxon_id=NCBITaxon:1200297`, `label=Sphaerodes sp. 'pseudofimicola'`, `rank=SPECIES`, `parent_id=NCBITaxon:2649391`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:1200297` at `data/seed_scope.tsv:58321`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 1 exact synonym, 0 broad synonyms, and 1 related synonym, matching the 2 YAML synonym entries.
- All 17 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `data/raw/ncbi_merged_ids.tsv` contains 0 retired IDs that map into `NCBITaxon:1200297`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:4821` reports `organism_count=1` for `NCBITaxon:1200297`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 0 organism rows, 0 project rows, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 0 exact type-material rows for `NCBITaxon:1200297`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 2 direct exact rows plus 2 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:1200297`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:1200297`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:1200297`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
