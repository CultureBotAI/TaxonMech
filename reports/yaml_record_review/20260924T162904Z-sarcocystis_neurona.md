# YAML Record Review: Sarcocystis neurona

- Verdict: pass
- Target: `data/taxa/eukaryota/sarcocystis_neurona.yaml`
- Identifier: `NCBITaxon:42890`

## Target

Reviewed the complete 65-line YAML record for Sarcocystis neurona. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for sarcocystis_neurona.

## Validation

- `just validate data/taxa/eukaryota/sarcocystis_neurona.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sarcocystis_neurona.yaml data/taxa/eukaryota/sarcodon_aspratus.yaml data/taxa/eukaryota/sarcoleotia_globosa.yaml data/taxa/eukaryota/sarcopodium_sp_kn_2018.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:5057` has `taxon_id=NCBITaxon:42890`, `label=Sarcocystis neurona`, `rank=SPECIES`, `parent_id=NCBITaxon:5812`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:42890` at `data/seed_scope.tsv:52533`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 0 exact synonyms, 0 broad synonyms, and 0 related synonyms, matching the absent YAML synonym list.
- All 12 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `NCBITaxon:42890` has no retired NCBI IDs merged into it, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:35254` reports `organism_count=2` for `NCBITaxon:42890`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 3 organism rows, 4 project rows, and 2 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 0 exact type-material rows for `NCBITaxon:42890`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 0 direct exact rows plus 0 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:42890`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:42890`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:42890`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
