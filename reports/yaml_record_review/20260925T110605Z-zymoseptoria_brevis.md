# YAML Record Review: Zymoseptoria brevis

- Verdict: pass
- Target: `data/taxa/eukaryota/zymoseptoria_brevis.yaml`
- Identifier: `NCBITaxon:1047168`

## Target

Reviewed the complete 81-line YAML record for Zymoseptoria brevis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zymoseptoria_brevis.

## Validation

- `just validate data/taxa/eukaryota/zymoseptoria_brevis.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zygotorulaspora_florentina.yaml data/taxa/eukaryota/zygotorulaspora_mrakii.yaml data/taxa/eukaryota/zymoseptoria_ardabiliae.yaml data/taxa/eukaryota/zymoseptoria_brevis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:224865` is `NCBITaxon:1047168`, `Zymoseptoria brevis`, rank `SPECIES`, parent `NCBITaxon:1047167`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zymoseptoria brevis` entry, at `data/curated/seed_scope.tsv:57374`.
- NCBI synonym counts are 0 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML preserves the related synonym from that row.
- All 16 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:1047168`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:790` reports `organism_count` 2 for `NCBITaxon:1047168`, matching the YAML GOLD assertion count of 2.
- Native GOLD evidence has 2 organism rows, 3 project rows, and 2 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 6 exact type-material rows for `NCBITaxon:1047168`.
- BacDive has 0 exact local rows for `NCBITaxon:1047168`.
- StrainInfo has 0 exact direct strain rows and 0 exact deposit matches for `NCBITaxon:1047168`.

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
