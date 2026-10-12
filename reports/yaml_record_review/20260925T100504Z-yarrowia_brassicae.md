# YAML Record Review: Yarrowia brassicae

- Verdict: pass
- Target: `data/taxa/eukaryota/yarrowia_brassicae.yaml`
- Identifier: `NCBITaxon:2860395`

## Target

Reviewed the complete 79-line YAML record for Yarrowia brassicae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yarrowia_brassicae.

## Validation

- `just validate data/taxa/eukaryota/yarrowia_brassicae.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/yarrowia_alimentaria.yaml data/taxa/eukaryota/yarrowia_brassicae.yaml data/taxa/eukaryota/yarrowia_bubula.yaml data/taxa/eukaryota/yarrowia_deformans.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:565509` is `NCBITaxon:2860395`, `Yarrowia brassicae`, rank `SPECIES`, parent `NCBITaxon:4951`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Yarrowia brassicae` entry, at `data/curated/seed_scope.tsv:63321`.
- NCBI synonym counts are 0 exact synonyms, 0 broad synonyms, and 3 related synonyms; the YAML preserves all 3 synonym entries from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` retains 1 redirect into `NCBITaxon:2860395`: `NCBITaxon:2083061`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:27782` reports `organism_count` 1 for `NCBITaxon:2860395`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 8 exact rows for `NCBITaxon:2860395`: four `culture from holotype` designation variants for `CBS 15225` and four `holotype` designation variants for `CICC 33263`.
- BacDive has 0 exact local rows for `NCBITaxon:2860395`.
- StrainInfo has 0 exact direct strain rows and 0 exact deposit matches for `NCBITaxon:2860395`.

## Completeness

- Generated raw strain tables all have 0 target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source tables all have 0 rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlay tables all have 0 target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
