# YAML Record Review: Saccosoma farinaceum

- Verdict: pass
- Target: `data/taxa/eukaryota/saccosoma_farinaceum.yaml`
- Identifier: `NCBITaxon:2650717`

## Target

Reviewed the complete 84-line YAML record for Saccosoma farinaceum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccosoma_farinaceum.

## Validation

- `just validate data/taxa/eukaryota/saccosoma_farinaceum.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomycopsis_selenospora.yaml data/taxa/eukaryota/saccobolus_dilutellus.yaml data/taxa/eukaryota/saccosoma_farinaceum.yaml data/taxa/eukaryota/saitoella_complicata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:540354` has `taxon_id=NCBITaxon:2650717`, `label=Saccosoma farinaceum`, `rank=SPECIES`, `parent_id=NCBITaxon:2485767`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:2650717` at `data/seed_scope.tsv:62917`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 3 exact synonyms, 0 broad synonyms, and 3 related synonyms, matching the 6 YAML synonym entries.
- All 12 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `data/raw/ncbi_merged_ids.tsv` contains 1 retired ID that merges into `NCBITaxon:2650717`: `NCBITaxon:2184202` at line 38734. An exact old-ID check found no retained row for it in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:24279` reports `organism_count=1` for `NCBITaxon:2650717`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 1 organism row, 2 project rows, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 1 exact type-material row for `NCBITaxon:2650717`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 1 direct exact row plus 1 exact deposit cross-reference for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:2650717`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:2650717`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:2650717`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
