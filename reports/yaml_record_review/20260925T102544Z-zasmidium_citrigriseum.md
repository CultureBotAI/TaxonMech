# YAML Record Review: Zasmidium citrigriseum

- Verdict: pass
- Target: `data/taxa/eukaryota/zasmidium_citrigriseum.yaml`
- Identifier: `NCBITaxon:1629917`

## Target

Reviewed the complete 99-line YAML record for Zasmidium citrigriseum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zasmidium_citrigriseum.

## Validation

- `just validate data/taxa/eukaryota/zasmidium_citrigriseum.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zasmidium_cellare.yaml data/taxa/eukaryota/zasmidium_citrigriseum.yaml data/taxa/eukaryota/zasmidium_sp.yaml data/taxa/eukaryota/zhuliangomyces_illinitus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:423477` is `NCBITaxon:1629917`, `Zasmidium citrigriseum`, rank `SPECIES`, parent `NCBITaxon:395590`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zasmidium citrigriseum` entry, at `data/curated/seed_scope.tsv:60930`.
- NCBI synonym counts are 5 exact synonyms, 0 broad synonyms, and 2 related synonyms; the YAML preserves all 7 synonym entries from that row.
- All 16 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` retains 2 redirects into `NCBITaxon:1629917`: `NCBITaxon:113225` and `NCBITaxon:513420`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:13938` reports `organism_count` 1 for `NCBITaxon:1629917`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 4 exact `culture from epitype` rows for `NCBITaxon:1629917`, covering `CBS 139467` and `CPC 15296` designation variants.
- BacDive has 0 exact local rows for `NCBITaxon:1629917`.
- StrainInfo has 2 exact direct strain rows and 2 exact deposit matches for `NCBITaxon:1629917`, covering siIDs 204790 and 259981.

## Completeness

- Generated raw strain tables all have 0 target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source tables all have 0 rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlay tables all have 0 target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
