# YAML Record Review: Zhuliangozyma parablackwelliae

- Verdict: pass
- Target: `data/taxa/eukaryota/zhuliangozyma_parablackwelliae.yaml`
- Identifier: `NCBITaxon:2126718`

## Target

Reviewed the complete 82-line YAML record for Zhuliangozyma parablackwelliae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zhuliangozyma_parablackwelliae.

## Validation

- `just validate data/taxa/eukaryota/zhuliangozyma_parablackwelliae.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zhuliangozyma_blackwelliae.yaml data/taxa/eukaryota/zhuliangozyma_boniae.yaml data/taxa/eukaryota/zhuliangozyma_parablackwelliae.yaml data/taxa/eukaryota/zonaria_farlowii.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:518617` is `NCBITaxon:2126718`, `Zhuliangozyma parablackwelliae`, rank `SPECIES`, parent `NCBITaxon:3712567`, genetic code `12`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zhuliangozyma parablackwelliae` entry, at `data/curated/seed_scope.tsv:62367`.
- NCBI synonym counts are 1 exact synonym, 0 broad synonyms, and 3 related synonyms; the YAML preserves all 4 synonym entries from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:2126718`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:20244` reports `organism_count` 1 for `NCBITaxon:2126718`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 6 exact rows for `NCBITaxon:2126718`: four `culture from holotype` variants for `CBS 15228` and two `holotype` variants for `NYNU 17763`.
- BacDive has 0 exact local rows for `NCBITaxon:2126718`.
- StrainInfo has 0 exact direct strain rows and 0 exact deposit matches for `NCBITaxon:2126718`.

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
