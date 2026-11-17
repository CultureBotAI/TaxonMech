# YAML Record Review: Sordaria araneosa

- Verdict: pass
- Target: `data/taxa/eukaryota/sordaria_araneosa.yaml`
- Identifier: `NCBITaxon:573841`

## Target

Reviewed the complete 87-line YAML record for Sordaria araneosa. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for sordaria_araneosa.

## Validation

- `just validate data/taxa/eukaryota/sordaria_araneosa.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/solicoccozyma_terrea.yaml data/taxa/eukaryota/solicoccozyma_terricola.yaml data/taxa/eukaryota/sonoraphlyctis_ranzonii.yaml data/taxa/eukaryota/sordaria_araneosa.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:135394` has `taxon_id=NCBITaxon:573841`, `label=Sordaria araneosa`, `rank=SPECIES`, `parent_id=NCBITaxon:5146`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:573841` at `data/seed_scope.tsv:56080`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 1 exact synonym, 0 broad synonyms, and 2 related synonyms, matching the 3 YAML synonym entries.
- All 16 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `data/raw/ncbi_merged_ids.tsv` contains 1 retired ID that maps into `NCBITaxon:573841`: `NCBITaxon:438772`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:39212` reports `organism_count=1` for `NCBITaxon:573841`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 0 organism rows, 0 project rows, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 0 exact type-material rows for `NCBITaxon:573841`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 1 direct exact row plus 2 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:573841`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:573841`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:573841`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
