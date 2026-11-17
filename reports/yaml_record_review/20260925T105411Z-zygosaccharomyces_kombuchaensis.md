# YAML Record Review: Zygosaccharomyces kombuchaensis

- Verdict: pass
- Target: `data/taxa/eukaryota/zygosaccharomyces_kombuchaensis.yaml`
- Identifier: `NCBITaxon:166050`

## Target

Reviewed the complete 73-line YAML record for Zygosaccharomyces kombuchaensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zygosaccharomyces_kombuchaensis.

## Validation

- `just validate data/taxa/eukaryota/zygosaccharomyces_kombuchaensis.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zygosaccharomyces_gambellarensis.yaml data/taxa/eukaryota/zygosaccharomyces_kombuchaensis.yaml data/taxa/eukaryota/zygosaccharomyces_lentus.yaml data/taxa/eukaryota/zygosaccharomyces_mellis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:34123` is `NCBITaxon:166050`, `Zygosaccharomyces kombuchaensis`, rank `SPECIES`, parent `NCBITaxon:4953`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zygosaccharomyces kombuchaensis` entry, at `data/curated/seed_scope.tsv:54227`.
- NCBI synonym counts are 0 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML preserves the related synonym from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:166050`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:14306` reports `organism_count` 2 for `NCBITaxon:166050`, matching the YAML GOLD assertion count of 2.
- Native GOLD evidence has 2 organism rows, 2 project rows, and 2 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 6 exact rows for `NCBITaxon:166050`: 4 culture-from-holotype rows and 2 type-material rows.
- BacDive has 0 exact local rows for `NCBITaxon:166050`.
- StrainInfo has 5 exact direct strain rows and 16 exact deposit matches for `NCBITaxon:166050`, all attached to direct StrainInfo rows.

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
