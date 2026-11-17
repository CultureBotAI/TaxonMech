# YAML Record Review: Zopfochytrium polystomum

- Verdict: pass
- Target: `data/taxa/eukaryota/zopfochytrium_polystomum.yaml`
- Identifier: `NCBITaxon:2211651`

## Target

Reviewed the complete 81-line YAML record for Zopfochytrium polystomum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zopfochytrium_polystomum.

## Validation

- `just validate data/taxa/eukaryota/zopfochytrium_polystomum.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zopfiella_pleuropora.yaml data/taxa/eukaryota/zopfochytrium_polystomum.yaml data/taxa/eukaryota/zychaea_mexicana.yaml data/taxa/eukaryota/zygoascus_biomembranicola.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:521597` is `NCBITaxon:2211651`, `Zopfochytrium polystomum`, rank `SPECIES`, parent `NCBITaxon:2709238`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zopfochytrium polystomum` entry, at `data/curated/seed_scope.tsv:62485`.
- NCBI synonym counts are 1 exact synonym, 0 broad synonyms, and 3 related synonyms; the YAML preserves the exact and related synonyms from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 1 redirect into `NCBITaxon:2211651`, from old ID `NCBITaxon:1437435`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:21007` reports `organism_count` 3 for `NCBITaxon:2211651`, matching the YAML GOLD assertion count of 3.
- Native GOLD evidence has 1 organism row, 2 project rows, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 5 exact epitype rows for `NCBITaxon:2211651`.
- BacDive has 0 exact local rows for `NCBITaxon:2211651`.
- StrainInfo has 0 exact direct strain rows and 0 exact deposit matches for `NCBITaxon:2211651`.

## Completeness

- Generated raw strain tables all have 0 target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source tables all have 0 rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlay tables all have 0 target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
