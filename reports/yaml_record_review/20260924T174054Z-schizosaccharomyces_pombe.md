# YAML Record Review: Schizosaccharomyces pombe

- Verdict: pass
- Target: `data/taxa/eukaryota/schizosaccharomyces_pombe.yaml`
- Identifier: `NCBITaxon:4896`

## Target

Reviewed the complete 75-line YAML record for Schizosaccharomyces pombe. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for schizosaccharomyces_pombe.

## Validation

- `just validate data/taxa/eukaryota/schizosaccharomyces_pombe.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/schizopora_paradoxa.yaml data/taxa/eukaryota/schizosaccharomyces_japonicus_nbrc_1609.yaml data/taxa/eukaryota/schizosaccharomyces_kambucha_nom_inval.yaml data/taxa/eukaryota/schizosaccharomyces_pombe.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:2131` has `taxon_id=NCBITaxon:4896`, `label=Schizosaccharomyces pombe`, `rank=SPECIES`, `parent_id=NCBITaxon:4895`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:4896` at `data/seed_scope.tsv:51870`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 1 exact synonym, 0 broad synonyms, and 2 related synonyms, matching the 3 YAML synonym entries.
- All 12 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `data/raw/ncbi_merged_ids.tsv:78655` maps old ID `NCBITaxon:45042` into `NCBITaxon:4896`, and an ignored-file-inclusive exact scan found no retained old-ID row in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:37042` reports `organism_count=1` for `NCBITaxon:4896`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 5 organism rows, 5 project rows, and 1 analysis row.
- `data/raw/ncbi_type_material.tsv` contains 14 exact type-material rows for `NCBITaxon:4896`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 1053 direct exact rows plus 1165 exact deposit cross-references for this taxon. The exact JSONL scan also found 1 non-direct record, `SI-ID 155148` for `Cladosporium allii-porri`, carrying a deposit cross-reference to `NCBITaxon:4896`.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:4896`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:4896`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:4896`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
