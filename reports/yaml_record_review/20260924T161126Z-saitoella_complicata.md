# YAML Record Review: Saitoella complicata

- Verdict: pass
- Target: `data/taxa/eukaryota/saitoella_complicata.yaml`
- Identifier: `NCBITaxon:5606`

## Target

Reviewed the complete 69-line YAML record for Saitoella complicata. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saitoella_complicata.

## Validation

- `just validate data/taxa/eukaryota/saitoella_complicata.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomycopsis_selenospora.yaml data/taxa/eukaryota/saccobolus_dilutellus.yaml data/taxa/eukaryota/saccosoma_farinaceum.yaml data/taxa/eukaryota/saitoella_complicata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:2489` has `taxon_id=NCBITaxon:5606`, `label=Saitoella complicata`, `rank=SPECIES`, `parent_id=NCBITaxon:5605`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:5606` at `data/seed_scope.tsv:52042`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 0 exact synonyms, 0 broad synonyms, and 1 related synonym, matching the 1 YAML synonym entry.
- All 12 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `NCBITaxon:5606` has no retired NCBI IDs merged into it, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:38825` reports `organism_count=1` for `NCBITaxon:5606`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 1 organism row, 4 project rows, and 2 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 12 exact type-material rows for `NCBITaxon:5606`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 2 direct exact rows plus 17 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:5606`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:5606`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:5606`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
