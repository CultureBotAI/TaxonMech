# YAML Record Review: Schizothecium curvisporum

- Verdict: pass
- Target: `data/taxa/eukaryota/schizothecium_curvisporum.yaml`
- Identifier: `NCBITaxon:179326`

## Target

Reviewed the complete 99-line YAML record for Schizothecium curvisporum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for schizothecium_curvisporum.

## Validation

- `just validate data/taxa/eukaryota/schizothecium_curvisporum.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/schizothecium_carpinicola.yaml data/taxa/eukaryota/schizothecium_curvisporum.yaml data/taxa/eukaryota/schizothecium_vesticola.yaml data/taxa/eukaryota/schmidingerella_arcuata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:35930` has `taxon_id=NCBITaxon:179326`, `label=Schizothecium curvisporum`, `rank=SPECIES`, `parent_id=NCBITaxon:252155`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:179326` at `data/seed_scope.tsv:54325`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 3 exact synonyms, 0 broad synonyms, and 4 related synonyms, matching the 7 YAML synonym entries.
- All 16 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `NCBITaxon:179326` has no retired NCBI IDs merged into it, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:15667` reports `organism_count=1` for `NCBITaxon:179326`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 1 organism row, 2 project rows, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 4 exact type-material rows for `NCBITaxon:179326`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 4 direct exact rows plus 5 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:179326`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:179326`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:179326`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
