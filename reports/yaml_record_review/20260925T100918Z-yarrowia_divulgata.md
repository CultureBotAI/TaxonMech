# YAML Record Review: Yarrowia divulgata

- Verdict: pass
- Target: `data/taxa/eukaryota/yarrowia_divulgata.yaml`
- Identifier: `NCBITaxon:479095`

## Target

Reviewed the complete 80-line YAML record for Yarrowia divulgata. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yarrowia_divulgata.

## Validation

- `just validate data/taxa/eukaryota/yarrowia_divulgata.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/yarrowia_divulgata.yaml data/taxa/eukaryota/yarrowia_galli.yaml data/taxa/eukaryota/yarrowia_hollandica.yaml data/taxa/eukaryota/yarrowia_keelungensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:107042` is `NCBITaxon:479095`, `Yarrowia divulgata`, rank `SPECIES`, parent `NCBITaxon:4951`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Yarrowia divulgata` entry, at `data/curated/seed_scope.tsv:55785`.
- NCBI synonym counts are 0 exact synonyms, 0 broad synonyms, and 3 related synonyms; the YAML preserves all 3 synonym entries from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:479095`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:36692` reports `organism_count` 1 for `NCBITaxon:479095`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 13 exact rows for `NCBITaxon:479095`: four `culture from holotype` variants for `CCUG 56725`, four `culture from holotype` variants for `NRRL Y-63741`, four `holotype` variants for `CBS 11013`, and one `holotype` row for `F6-17`.
- BacDive has 0 exact local rows for `NCBITaxon:479095`.
- StrainInfo has 1 exact direct strain row and 1 exact deposit match for `NCBITaxon:479095`, both at siID 408447.

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
