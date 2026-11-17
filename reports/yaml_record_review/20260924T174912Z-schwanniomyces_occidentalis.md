# YAML Record Review: Schwanniomyces occidentalis

- Verdict: pass
- Target: `data/taxa/eukaryota/schwanniomyces_occidentalis.yaml`
- Identifier: `NCBITaxon:27300`

## Target

Reviewed the complete 88-line YAML record for Schwanniomyces occidentalis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for schwanniomyces_occidentalis.

## Validation

- `just validate data/taxa/eukaryota/schwanniomyces_occidentalis.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/schmidingerella_taraikaensis.yaml data/taxa/eukaryota/schwanniomyces_capriottii.yaml data/taxa/eukaryota/schwanniomyces_etchellsii.yaml data/taxa/eukaryota/schwanniomyces_occidentalis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:2716` has `taxon_id=NCBITaxon:27300`, `label=Schwanniomyces occidentalis`, `rank=SPECIES`, `parent_id=NCBITaxon:766758`, `genetic_code=12`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:27300` at `data/seed_scope.tsv:52140`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 2 exact synonyms, 0 broad synonyms, and 4 related synonyms, matching the 6 YAML synonym entries.
- All 13 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `data/raw/ncbi_merged_ids.tsv:81922` maps old ID `NCBITaxon:4946` into `NCBITaxon:27300`, and an ignored-file-inclusive exact scan found no retained old-ID row in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:25418` reports `organism_count=9` for `NCBITaxon:27300`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 9 organism rows, 1 project row, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 19 exact type-material rows for `NCBITaxon:27300`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 33 direct exact rows plus 81 exact deposit cross-references for this taxon. The exact JSONL scan also found 8 non-direct records carrying 17 deposit cross-references to `NCBITaxon:27300`.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:27300`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:27300`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:27300`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
