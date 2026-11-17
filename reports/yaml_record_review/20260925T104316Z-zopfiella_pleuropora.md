# YAML Record Review: Zopfiella pleuropora

- Verdict: pass
- Target: `data/taxa/eukaryota/zopfiella_pleuropora.yaml`
- Identifier: `NCBITaxon:1646530`

## Target

Reviewed the complete 81-line YAML record for Zopfiella pleuropora. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zopfiella_pleuropora.

## Validation

- `just validate data/taxa/eukaryota/zopfiella_pleuropora.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zopfiella_pleuropora.yaml data/taxa/eukaryota/zopfochytrium_polystomum.yaml data/taxa/eukaryota/zychaea_mexicana.yaml data/taxa/eukaryota/zygoascus_biomembranicola.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:430476` is `NCBITaxon:1646530`, `Zopfiella pleuropora`, rank `SPECIES`, parent `NCBITaxon:252180`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zopfiella pleuropora` entry, at `data/curated/seed_scope.tsv:60951`.
- NCBI synonym counts are 0 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML preserves the related synonym from that row.
- All 16 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:1646530`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:14132` reports `organism_count` 1 for `NCBITaxon:1646530`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 2 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 2 exact rows for `NCBITaxon:1646530`, both isotype rows for `CBS 518.70`.
- BacDive has 0 exact local rows for `NCBITaxon:1646530`.
- StrainInfo has 4 exact direct strain rows and 9 exact deposit matches for `NCBITaxon:1646530`, all attached to the direct StrainInfo rows.

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
