# YAML Record Review: Zygosaccharomyces lentus

- Verdict: pass
- Target: `data/taxa/eukaryota/zygosaccharomyces_lentus.yaml`
- Identifier: `NCBITaxon:85125`

## Target

Reviewed the complete 73-line YAML record for Zygosaccharomyces lentus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zygosaccharomyces_lentus.

## Validation

- `just validate data/taxa/eukaryota/zygosaccharomyces_lentus.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zygosaccharomyces_gambellarensis.yaml data/taxa/eukaryota/zygosaccharomyces_kombuchaensis.yaml data/taxa/eukaryota/zygosaccharomyces_lentus.yaml data/taxa/eukaryota/zygosaccharomyces_mellis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:13137` is `NCBITaxon:85125`, `Zygosaccharomyces lentus`, rank `SPECIES`, parent `NCBITaxon:4953`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zygosaccharomyces lentus` entry, at `data/curated/seed_scope.tsv:53416`.
- NCBI synonym counts are 0 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML preserves the related synonym from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:85125`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:43233` reports `organism_count` 1 for `NCBITaxon:85125`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 8 exact culture-from-holotype rows for `NCBITaxon:85125`.
- BacDive has 0 exact local rows for `NCBITaxon:85125`.
- StrainInfo has 14 exact direct strain rows and 30 exact deposit matches for `NCBITaxon:85125`; 29 deposit matches are attached to direct strain rows and 1 deposit match is in 1 deposit-only record.

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
