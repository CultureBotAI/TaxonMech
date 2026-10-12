# YAML Record Review: Spiromyces aspiralis

- Verdict: pass
- Target: `data/taxa/eukaryota/spiromyces_aspiralis.yaml`
- Identifier: `NCBITaxon:68401`

## Target

Reviewed the complete 75-line YAML record for Spiromyces aspiralis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for spiromyces_aspiralis.

## Validation

- `just validate data/taxa/eukaryota/spiromyces_aspiralis.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/spiromyces_aspiralis.yaml data/taxa/eukaryota/spironucleus_salmonicida.yaml data/taxa/eukaryota/spironucleus_vortens.yaml data/taxa/eukaryota/spizellomyces_sp.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:9372` has `taxon_id=NCBITaxon:68401`, `label=Spiromyces aspiralis`, `rank=SPECIES`, `parent_id=NCBITaxon:61417`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:68401` at `data/seed_scope.tsv:53166`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 0 exact synonyms, 0 broad synonyms, and 3 related synonyms, matching the 3 YAML synonym entries.
- All 12 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `data/raw/ncbi_merged_ids.tsv` contains 1 retired ID that maps into `NCBITaxon:68401`: `NCBITaxon:61419`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:41300` reports `organism_count=1` for `NCBITaxon:68401`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 1 organism row, 2 project rows, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 7 exact type-material rows for `NCBITaxon:68401`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 0 direct exact rows plus 0 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:68401`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:68401`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:68401`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
