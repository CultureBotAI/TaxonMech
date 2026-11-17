# YAML Record Review: Saccharomycopsis guyanensis

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomycopsis_guyanensis.yaml`
- Identifier: `NCBITaxon:1379279`

## Target

Reviewed the complete 78-line YAML record for Saccharomycopsis guyanensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomycopsis_guyanensis.

## Validation

- `just validate data/taxa/eukaryota/saccharomycopsis_guyanensis.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomycopsis_guyanensis.yaml data/taxa/eukaryota/saccharomycopsis_javanensis.yaml data/taxa/eukaryota/saccharomycopsis_lassenensis.yaml data/taxa/eukaryota/saccharomycopsis_malanga.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:336756` has `taxon_id=NCBITaxon:1379279`, `label=Saccharomycopsis guyanensis`, `rank=SPECIES`, `parent_id=NCBITaxon:4943`, `genetic_code=12`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:1379279` at `data/seed_scope.tsv:59704`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 0 exact synonyms, 0 broad synonyms, and 3 related synonyms, matching the 3 YAML synonym entries.
- All 13 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `data/raw/ncbi_merged_ids.tsv` contains 2 retired IDs that merge into `NCBITaxon:1379279`: `NCBITaxon:1379282` at line 13919 and `NCBITaxon:1421527` at line 15482. Exact old-ID checks found no retained rows for either ID in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:8907` reports `organism_count=1` for `NCBITaxon:1379279`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 1 organism row, 1 project row, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 4 exact type-material rows for `NCBITaxon:1379279`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 0 direct exact rows plus 0 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:1379279`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:1379279`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:1379279`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
