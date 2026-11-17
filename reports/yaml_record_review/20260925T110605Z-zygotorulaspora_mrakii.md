# YAML Record Review: Zygotorulaspora mrakii

- Verdict: pass
- Target: `data/taxa/eukaryota/zygotorulaspora_mrakii.yaml`
- Identifier: `NCBITaxon:42260`

## Target

Reviewed the complete 78-line YAML record for Zygotorulaspora mrakii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zygotorulaspora_mrakii.

## Validation

- `just validate data/taxa/eukaryota/zygotorulaspora_mrakii.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zygotorulaspora_florentina.yaml data/taxa/eukaryota/zygotorulaspora_mrakii.yaml data/taxa/eukaryota/zymoseptoria_ardabiliae.yaml data/taxa/eukaryota/zymoseptoria_brevis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:4977` is `NCBITaxon:42260`, `Zygotorulaspora mrakii`, rank `SPECIES`, parent `NCBITaxon:1196389`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zygotorulaspora mrakii` entry, at `data/curated/seed_scope.tsv:52515`.
- NCBI synonym counts are 1 exact synonym, 0 broad synonyms, and 2 related synonyms; the YAML preserves the exact and related synonyms from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:42260`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:35113` reports `organism_count` 1 for `NCBITaxon:42260`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 2 project rows, and 2 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 16 exact rows for `NCBITaxon:42260`: 5 culture-from-type-material rows and 11 type-material rows.
- BacDive has 0 exact local rows for `NCBITaxon:42260`.
- StrainInfo has 10 exact direct strain rows and 26 exact deposit matches for `NCBITaxon:42260`, all attached to direct StrainInfo rows.

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
