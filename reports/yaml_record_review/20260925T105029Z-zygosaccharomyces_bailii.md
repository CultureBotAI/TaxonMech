# YAML Record Review: Zygosaccharomyces bailii

- Verdict: pass
- Target: `data/taxa/eukaryota/zygosaccharomyces_bailii.yaml`
- Identifier: `NCBITaxon:4954`

## Target

Reviewed the complete 90-line YAML record for Zygosaccharomyces bailii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zygosaccharomyces_bailii.

## Validation

- `just validate data/taxa/eukaryota/zygosaccharomyces_bailii.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zygoascus_polysorbophilus.yaml data/taxa/eukaryota/zygoascus_sp_pk3305.yaml data/taxa/eukaryota/zygosaccharomyces_bailii.yaml data/taxa/eukaryota/zygosaccharomyces_bisporus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:2161` is `NCBITaxon:4954`, `Zygosaccharomyces bailii`, rank `SPECIES`, parent `NCBITaxon:4953`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zygosaccharomyces bailii` entry, at `data/curated/seed_scope.tsv:51891`.
- NCBI synonym counts are 4 exact synonyms, 0 broad synonyms, and 3 related synonyms; the YAML preserves the exact and related synonyms from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:4954`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:37206` reports `organism_count` 1 for `NCBITaxon:4954`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 22 exact type-material rows for `NCBITaxon:4954`.
- BacDive has 0 exact local rows for `NCBITaxon:4954`.
- StrainInfo has 139 exact direct strain rows and 294 exact deposit matches for `NCBITaxon:4954`; 285 deposit matches are attached to direct strain rows and 9 deposit matches are in 5 deposit-only records.

## Completeness

- Generated raw strain tables all have 0 target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source tables all have 0 rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlay tables have 0 rows in `data/straininfo/assemblies.tsv`, 0 rows in `data/straininfo/exclusions.tsv`, and 2 exact target rows in `data/straininfo/related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
