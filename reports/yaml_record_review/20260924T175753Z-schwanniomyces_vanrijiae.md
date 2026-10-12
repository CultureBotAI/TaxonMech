# YAML Record Review: Schwanniomyces vanrijiae

- Verdict: pass
- Target: `data/taxa/eukaryota/schwanniomyces_vanrijiae.yaml`
- Identifier: `NCBITaxon:27305`

## Target

Reviewed the complete 86-line YAML record for Schwanniomyces vanrijiae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for schwanniomyces_vanrijiae.

## Validation

- `just validate data/taxa/eukaryota/schwanniomyces_vanrijiae.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/schwanniomyces_vanrijiae.yaml data/taxa/eukaryota/schwanniomyces_vanrijiae_var_yarrowii.yaml data/taxa/eukaryota/schwanniomyces_yamadae.yaml data/taxa/eukaryota/sclerococcum_haliotrephum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:2720` has `taxon_id=NCBITaxon:27305`, `label=Schwanniomyces vanrijiae`, `rank=SPECIES`, `parent_id=NCBITaxon:766758`, `genetic_code=12`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:27305` at `data/seed_scope.tsv:52143`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 3 exact synonyms, 0 broad synonyms, and 2 related synonyms, matching the 5 YAML synonym entries.
- All 13 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `NCBITaxon:27305` has no retired NCBI IDs merged into it, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:25431` reports `organism_count=6` for `NCBITaxon:27305`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 6 organism rows, 1 project row, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 18 exact type-material rows for `NCBITaxon:27305`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 9 direct exact rows plus 29 exact deposit cross-references for this taxon. The exact JSONL scan also found 7 non-direct variety records carrying 20 deposit cross-references to `NCBITaxon:27305`.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:27305`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:27305`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:27305`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
