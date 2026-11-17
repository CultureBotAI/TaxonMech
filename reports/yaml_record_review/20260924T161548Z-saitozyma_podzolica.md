# YAML Record Review: Saitozyma podzolica

- Verdict: pass
- Target: `data/taxa/eukaryota/saitozyma_podzolica.yaml`
- Identifier: `NCBITaxon:1890683`

## Target

Reviewed the complete 88-line YAML record for Saitozyma podzolica. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saitozyma_podzolica.

## Validation

- `just validate data/taxa/eukaryota/saitozyma_podzolica.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saitozyma_podzolica.yaml data/taxa/eukaryota/saitozyma_sp_jcm_24511.yaml data/taxa/eukaryota/sakaguchia_dacryoidea.yaml data/taxa/eukaryota/sakaguchia_lamellibrachiae.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:490925` has `taxon_id=NCBITaxon:1890683`, `label=Saitozyma podzolica`, `rank=SPECIES`, `parent_id=NCBITaxon:1890244`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:1890683` at `data/seed_scope.tsv:61461`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 2 exact synonyms, 0 broad synonyms, and 5 related synonyms, matching the 7 YAML synonym entries.
- All 12 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `data/raw/ncbi_merged_ids.tsv` contains 3 retired IDs that merge into `NCBITaxon:1890683`: `NCBITaxon:2898221` at line 56679, `NCBITaxon:2932453` at line 57884, and `NCBITaxon:89927` at line 98285. Exact old-ID checks found no retained rows for these IDs in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:17027` reports `organism_count=1` for `NCBITaxon:1890683`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 1 organism row, 1 project row, and 1 analysis row.
- `data/raw/ncbi_type_material.tsv` contains 21 exact type-material rows for `NCBITaxon:1890683`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 42 direct exact rows plus 60 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:1890683`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:1890683`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:1890683`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
