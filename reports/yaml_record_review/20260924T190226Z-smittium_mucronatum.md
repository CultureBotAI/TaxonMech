# YAML Record Review: Smittium mucronatum

- Verdict: pass
- Target: `data/taxa/eukaryota/smittium_mucronatum.yaml`
- Identifier: `NCBITaxon:133383`

## Target

Reviewed the complete 69-line YAML record for Smittium mucronatum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for smittium_mucronatum.

## Validation

- `just validate data/taxa/eukaryota/smittium_mucronatum.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/smittium_mucronatum.yaml data/taxa/eukaryota/sodiomyces_alcalophilus_jcm_7366.yaml data/taxa/eukaryota/sodiomyces_alkalinus.yaml data/taxa/eukaryota/solicoccozyma_phenolica.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:25936` has `taxon_id=NCBITaxon:133383`, `label=Smittium mucronatum`, `rank=SPECIES`, `parent_id=NCBITaxon:4888`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:133383` at `data/seed_scope.tsv:53952`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 0 exact synonyms, 0 broad synonyms, and 1 related synonym, matching the 1 YAML synonym entry.
- All 12 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `data/raw/ncbi_merged_ids.tsv` contains 0 retired IDs that map into `NCBITaxon:133383`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:8100` reports `organism_count=1` for `NCBITaxon:133383`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 1 organism row, 1 project row, and 1 analysis row.
- `data/raw/ncbi_type_material.tsv` contains 0 exact type-material rows for `NCBITaxon:133383`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 1 direct exact row plus 1 exact deposit cross-reference for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:133383`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:133383`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:133383`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
