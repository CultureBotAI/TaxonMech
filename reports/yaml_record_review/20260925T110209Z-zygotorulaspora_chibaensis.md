# YAML Record Review: Zygotorulaspora chibaensis

- Verdict: pass
- Target: `data/taxa/eukaryota/zygotorulaspora_chibaensis.yaml`
- Identifier: `NCBITaxon:2116648`

## Target

Reviewed the complete 75-line YAML record for Zygotorulaspora chibaensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zygotorulaspora_chibaensis.

## Validation

- `just validate data/taxa/eukaryota/zygotorulaspora_chibaensis.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zygosaccharomyces_sapae.yaml data/taxa/eukaryota/zygosaccharomyces_siamensis.yaml data/taxa/eukaryota/zygotorulaspora_chibaensis.yaml data/taxa/eukaryota/zygotorulaspora_danielsina.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:518511` is `NCBITaxon:2116648`, `Zygotorulaspora chibaensis`, rank `SPECIES`, parent `NCBITaxon:1196389`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zygotorulaspora chibaensis` entry, at `data/curated/seed_scope.tsv:62364`.
- NCBI synonym counts are 0 exact synonyms, 0 broad synonyms, and 2 related synonyms; the YAML preserves the related synonyms from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:2116648`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:20195` reports `organism_count` 1 for `NCBITaxon:2116648`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 4 exact rows for `NCBITaxon:2116648`: 2 culture-from-holotype rows and 2 holotype rows.
- BacDive has 0 exact local rows for `NCBITaxon:2116648`.
- StrainInfo has 0 exact direct strain rows and 0 exact deposit matches for `NCBITaxon:2116648`.

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
