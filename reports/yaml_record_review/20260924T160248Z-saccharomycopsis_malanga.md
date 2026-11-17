# YAML Record Review: Saccharomycopsis malanga

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomycopsis_malanga.yaml`
- Identifier: `NCBITaxon:44092`

## Target

Reviewed the complete 79-line YAML record for Saccharomycopsis malanga. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomycopsis_malanga.

## Validation

- `just validate data/taxa/eukaryota/saccharomycopsis_malanga.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomycopsis_guyanensis.yaml data/taxa/eukaryota/saccharomycopsis_javanensis.yaml data/taxa/eukaryota/saccharomycopsis_lassenensis.yaml data/taxa/eukaryota/saccharomycopsis_malanga.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:5340` has `taxon_id=NCBITaxon:44092`, `label=Saccharomycopsis malanga`, `rank=SPECIES`, `parent_id=NCBITaxon:4943`, `genetic_code=12`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:44092` at `data/seed_scope.tsv:52579`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 1 exact synonym, 0 broad synonyms, and 2 related synonyms, matching the 3 YAML synonym entries.
- All 13 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `NCBITaxon:44092` has no retired NCBI IDs merged into it, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:35583` reports `organism_count=3` for `NCBITaxon:44092`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 3 organism rows, 3 project rows, and 2 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 11 exact type-material rows for `NCBITaxon:44092`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 4 direct exact rows plus 22 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:44092`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:44092`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:44092`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
