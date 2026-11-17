# YAML Record Review: Zygosaccharomyces rouxii

- Verdict: pass
- Target: `data/taxa/eukaryota/zygosaccharomyces_rouxii.yaml`
- Identifier: `NCBITaxon:4956`

## Target

Reviewed the complete 81-line YAML record for Zygosaccharomyces rouxii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zygosaccharomyces_rouxii.

## Validation

- `just validate data/taxa/eukaryota/zygosaccharomyces_rouxii.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zygosaccharomyces_parabailii.yaml data/taxa/eukaryota/zygosaccharomyces_pseudobailii.yaml data/taxa/eukaryota/zygosaccharomyces_pseudorouxii_nom_inval.yaml data/taxa/eukaryota/zygosaccharomyces_rouxii.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:2163` is `NCBITaxon:4956`, `Zygosaccharomyces rouxii`, rank `SPECIES`, parent `NCBITaxon:4953`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zygosaccharomyces rouxii` entry, at `data/curated/seed_scope.tsv:51893`.
- NCBI synonym counts are 1 exact synonym, 0 broad synonyms, and 3 related synonyms; the YAML preserves the exact and related synonyms from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 1 redirect into `NCBITaxon:4956`, from old ID `NCBITaxon:559307`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:37210` reports `organism_count` 6 for `NCBITaxon:4956`, matching the YAML GOLD assertion count of 6.
- Native GOLD evidence has 4 organism rows, 5 project rows, and 2 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 20 exact rows for `NCBITaxon:4956`: 5 culture-from-type-material rows and 15 type-material rows.
- BacDive has 0 exact local rows for `NCBITaxon:4956`.
- StrainInfo has 329 exact direct strain rows and 647 exact deposit matches for `NCBITaxon:4956`; 634 deposit matches are attached to direct strain rows and 13 deposit matches are in 8 deposit-only records.

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
