# YAML Record Review: Zygosaccharomyces pseudorouxii (nom. inval.)

- Verdict: pass
- Target: `data/taxa/eukaryota/zygosaccharomyces_pseudorouxii_nom_inval.yaml`
- Identifier: `NCBITaxon:227369`

## Target

Reviewed the complete 75-line YAML record for Zygosaccharomyces pseudorouxii (nom. inval.). The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zygosaccharomyces_pseudorouxii_nom_inval.

## Validation

- `just validate data/taxa/eukaryota/zygosaccharomyces_pseudorouxii_nom_inval.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zygosaccharomyces_parabailii.yaml data/taxa/eukaryota/zygosaccharomyces_pseudobailii.yaml data/taxa/eukaryota/zygosaccharomyces_pseudorouxii_nom_inval.yaml data/taxa/eukaryota/zygosaccharomyces_rouxii.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:44556` is `NCBITaxon:227369`, `Zygosaccharomyces pseudorouxii (nom. inval.)`, rank `SPECIES`, parent `NCBITaxon:2618685`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zygosaccharomyces pseudorouxii (nom. inval.)` entry, at `data/curated/seed_scope.tsv:54628`.
- NCBI synonym counts are 1 exact synonym, 0 broad synonyms, and 0 related synonyms; the YAML preserves the exact synonym from that row.
- All 14 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:227369`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:21366` reports `organism_count` 1 for `NCBITaxon:227369`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 0 exact rows for `NCBITaxon:227369`.
- BacDive has 0 exact local rows for `NCBITaxon:227369`.
- StrainInfo has 0 exact direct strain rows and 0 exact deposit matches for `NCBITaxon:227369`.

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
