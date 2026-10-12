# YAML Record Review: Scheffersomyces xylosifermentans

- Verdict: pass
- Target: `data/taxa/eukaryota/scheffersomyces_xylosifermentans.yaml`
- Identifier: `NCBITaxon:1304137`

## Target

Reviewed the complete 84-line YAML record for Scheffersomyces xylosifermentans. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for scheffersomyces_xylosifermentans.

## Validation

- `just validate data/taxa/eukaryota/scheffersomyces_xylosifermentans.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/scheffersomyces_virginianus.yaml data/taxa/eukaryota/scheffersomyces_xylosifermentans.yaml data/taxa/eukaryota/schizangiella_serpentis.yaml data/taxa/eukaryota/schizochytrium_aggregatum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:308344` has `taxon_id=NCBITaxon:1304137`, `label=Scheffersomyces xylosifermentans`, `rank=SPECIES`, `parent_id=NCBITaxon:766733`, `genetic_code=12`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:1304137` at `data/seed_scope.tsv:59310`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 0 exact synonyms, 0 broad synonyms, and 5 related synonyms, matching the 5 YAML synonym entries.
- All 13 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- NCBI merged-ID rows retire `NCBITaxon:1280836` and `NCBITaxon:979895` into `NCBITaxon:1304137`, but exact old-ID checks found no retained rows in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:7445` reports `organism_count=1` for `NCBITaxon:1304137`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 1 organism row, 34 project rows, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 10 exact type-material rows for `NCBITaxon:1304137`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 0 direct exact rows plus 0 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:1304137`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:1304137`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:1304137`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
