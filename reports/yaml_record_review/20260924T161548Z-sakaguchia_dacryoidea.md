# YAML Record Review: Sakaguchia dacryoidea

- Verdict: pass
- Target: `data/taxa/eukaryota/sakaguchia_dacryoidea.yaml`
- Identifier: `NCBITaxon:106023`

## Target

Reviewed the complete 73-line YAML record for Sakaguchia dacryoidea. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for sakaguchia_dacryoidea.

## Validation

- `just validate data/taxa/eukaryota/sakaguchia_dacryoidea.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saitozyma_podzolica.yaml data/taxa/eukaryota/saitozyma_sp_jcm_24511.yaml data/taxa/eukaryota/sakaguchia_dacryoidea.yaml data/taxa/eukaryota/sakaguchia_lamellibrachiae.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:19052` has `taxon_id=NCBITaxon:106023`, `label=Sakaguchia dacryoidea`, `rank=SPECIES`, `parent_id=NCBITaxon:106022`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:106023` at `data/seed_scope.tsv:53721`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 2 exact synonyms, 0 broad synonyms, and 0 related synonyms, matching the 2 YAML synonym entries.
- All 12 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `data/raw/ncbi_merged_ids.tsv` contains 1 retired ID that merges into `NCBITaxon:106023`: `NCBITaxon:5287` at line 84786. An exact old-ID check found no retained row for it in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:1104` reports `organism_count=8` for `NCBITaxon:106023`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 7 organism rows, 0 project rows, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 12 exact type-material rows for `NCBITaxon:106023`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 14 direct exact rows plus 42 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:106023`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:106023`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:106023`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
