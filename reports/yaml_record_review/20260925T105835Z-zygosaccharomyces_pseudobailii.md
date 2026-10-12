# YAML Record Review: Zygosaccharomyces pseudobailii

- Verdict: pass
- Target: `data/taxa/eukaryota/zygosaccharomyces_pseudobailii.yaml`
- Identifier: `NCBITaxon:1365887`

## Target

Reviewed the complete 79-line YAML record for Zygosaccharomyces pseudobailii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zygosaccharomyces_pseudobailii.

## Validation

- `just validate data/taxa/eukaryota/zygosaccharomyces_pseudobailii.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zygosaccharomyces_parabailii.yaml data/taxa/eukaryota/zygosaccharomyces_pseudobailii.yaml data/taxa/eukaryota/zygosaccharomyces_pseudorouxii_nom_inval.yaml data/taxa/eukaryota/zygosaccharomyces_rouxii.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:334758` is `NCBITaxon:1365887`, `Zygosaccharomyces pseudobailii`, rank `SPECIES`, parent `NCBITaxon:4953`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zygosaccharomyces pseudobailii` entry, at `data/curated/seed_scope.tsv:59689`.
- NCBI synonym counts are 0 exact synonyms, 0 broad synonyms, and 3 related synonyms; the YAML preserves the related synonyms from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 2 redirects into `NCBITaxon:1365887`, from old IDs `NCBITaxon:1302347` and `NCBITaxon:3016118`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:8811` reports `organism_count` 2 for `NCBITaxon:1365887`, matching the YAML GOLD assertion count of 2.
- Native GOLD evidence has 2 organism rows, 2 project rows, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 8 exact rows for `NCBITaxon:1365887`: 4 culture-from-holotype rows and 4 holotype rows.
- BacDive has 0 exact local rows for `NCBITaxon:1365887`.
- StrainInfo has 0 exact direct strain rows and 0 exact deposit matches for `NCBITaxon:1365887`.

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
