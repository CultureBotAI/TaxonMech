# YAML Record Review: Sarocladium strictum

- Verdict: pass
- Target: `data/taxa/eukaryota/sarocladium_strictum.yaml`
- Identifier: `NCBITaxon:5046`

## Target

Reviewed the complete 90-line YAML record for Sarocladium strictum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for sarocladium_strictum.

## Validation

- `just validate data/taxa/eukaryota/sarocladium_strictum.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sarocladium_strictum.yaml data/taxa/eukaryota/sarocladium_zeae.yaml data/taxa/eukaryota/saturnispora_ahearnii.yaml data/taxa/eukaryota/saturnispora_besseyi.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:2203` has `taxon_id=NCBITaxon:5046`, `label=Sarocladium strictum`, `rank=SPECIES`, `parent_id=NCBITaxon:284134`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:5046` at `data/seed_scope.tsv:51914`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 2 exact synonyms, 0 broad synonyms, and 2 related synonyms, matching the 4 YAML synonym entries.
- All 16 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `data/raw/ncbi_merged_ids.tsv` contains 1 retired ID that merges into `NCBITaxon:5046`: `NCBITaxon:1452525` at line 16401. An exact old-ID check found no retained row for it in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:37391` reports `organism_count=6` for `NCBITaxon:5046`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 4 organism rows, 2 project rows, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 13 exact type-material rows for `NCBITaxon:5046`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 131 direct exact rows plus 159 exact deposit cross-references for this taxon; a parsed JSONL check accounted for the 2 non-direct rows that also carry exact `NCBITaxon:5046` deposits.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:5046`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:5046`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:5046`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
