# YAML Record Review: Saccobolus dilutellus

- Verdict: pass
- Target: `data/taxa/eukaryota/saccobolus_dilutellus.yaml`
- Identifier: `NCBITaxon:406764`

## Target

Reviewed the complete 78-line YAML record for Saccobolus dilutellus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccobolus_dilutellus.

## Validation

- `just validate data/taxa/eukaryota/saccobolus_dilutellus.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomycopsis_selenospora.yaml data/taxa/eukaryota/saccobolus_dilutellus.yaml data/taxa/eukaryota/saccosoma_farinaceum.yaml data/taxa/eukaryota/saitoella_complicata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:87833` has `taxon_id=NCBITaxon:406764`, `label=Saccobolus dilutellus`, `rank=SPECIES`, `parent_id=NCBITaxon:47218`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:406764` at `data/seed_scope.tsv:55536`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 1 exact synonym, 0 broad synonyms, and 2 related synonyms, matching the 3 YAML synonym entries.
- All 13 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `NCBITaxon:406764` has no retired NCBI IDs merged into it, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:34633` reports `organism_count=1` for `NCBITaxon:406764`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 0 organism rows, 0 project rows, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 0 exact type-material rows for `NCBITaxon:406764`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 1 direct exact row plus 1 exact deposit cross-reference for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:406764`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:406764`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:406764`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
