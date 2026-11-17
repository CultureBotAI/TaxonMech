# YAML Record Review: Scedosporium boydii

- Verdict: pass
- Target: `data/taxa/eukaryota/scedosporium_boydii.yaml`
- Identifier: `NCBITaxon:5597`

## Target

Reviewed the complete 102-line YAML record for Scedosporium boydii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for scedosporium_boydii.

## Validation

- `just validate data/taxa/eukaryota/scedosporium_boydii.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/scedosporium_boydii.yaml data/taxa/eukaryota/scedosporium_dehoogii.yaml data/taxa/eukaryota/scheffersomyces_amazonensis.yaml data/taxa/eukaryota/scheffersomyces_broadrunensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:2483` has `taxon_id=NCBITaxon:5597`, `label=Scedosporium boydii`, `rank=SPECIES`, `parent_id=NCBITaxon:41687`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:5597` at `data/seed_scope.tsv:52039`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 3 exact synonyms, 0 broad synonyms, and 5 related synonyms, matching the 8 YAML synonym entries.
- All 16 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `NCBITaxon:5597` has no retired NCBI IDs merged into it, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:38807` reports `organism_count=4` for `NCBITaxon:5597`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 4 organism rows, 1 project row, and 1 analysis row.
- `data/raw/ncbi_type_material.tsv` contains 10 exact type-material rows for `NCBITaxon:5597`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 266 direct exact rows plus 317 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:5597`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:5597`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:5597`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
