# YAML Record Review: Zopfia rosatii

- Verdict: pass
- Target: `data/taxa/eukaryota/zopfia_rosatii.yaml`
- Identifier: `NCBITaxon:160030`

## Target

Reviewed the complete 83-line YAML record for Zopfia rosatii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zopfia_rosatii.

## Validation

- `just validate data/taxa/eukaryota/zopfia_rosatii.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zopfia_rosatii.yaml data/taxa/eukaryota/zopfiella_inermis.yaml data/taxa/eukaryota/zopfiella_leucotricha.yaml data/taxa/eukaryota/zopfiella_macrospora.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:33054` is `NCBITaxon:160030`, `Zopfia rosatii`, rank `SPECIES`, parent `NCBITaxon:160034`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zopfia rosatii` entry, at `data/curated/seed_scope.tsv:54158`.
- NCBI synonym counts are 1 exact synonym, 0 broad synonyms, and 2 related synonyms; the YAML preserves the exact and related synonyms from that row.
- All 15 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:160030`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:12920` reports `organism_count` 2 for `NCBITaxon:160030`, matching the YAML GOLD assertion count of 2.
- Native GOLD organism, project, and analysis snapshot tables have 0 exact rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 4 exact rows for `NCBITaxon:160030`: 2 holotype rows and 2 reference-material rows.
- BacDive has 0 exact local rows for `NCBITaxon:160030`.
- StrainInfo has 9 exact direct strain rows and 15 exact deposit matches for `NCBITaxon:160030`; the deposit matches include one deposit-only record at siID 122298 and 14 deposits attached to direct strain records.

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
