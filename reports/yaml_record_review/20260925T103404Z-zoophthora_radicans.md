# YAML Record Review: Zoophthora radicans

- Verdict: pass
- Target: `data/taxa/eukaryota/zoophthora_radicans.yaml`
- Identifier: `NCBITaxon:42210`

## Target

Reviewed the complete 82-line YAML record for Zoophthora radicans. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zoophthora_radicans.

## Validation

- `just validate data/taxa/eukaryota/zoophthora_radicans.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zoophthora_radicans.yaml data/taxa/eukaryota/zoophthora_radicans_arsef_4784.yaml data/taxa/eukaryota/zooxanthella_nutricula.yaml data/taxa/eukaryota/zopfia_rhizophila.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:4959` is `NCBITaxon:42210`, `Zoophthora radicans`, rank `SPECIES`, parent `NCBITaxon:34482`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zoophthora radicans` entry, at `data/curated/seed_scope.tsv:52511`.
- NCBI synonym counts are 2 exact synonyms, 0 broad synonyms, and 3 related synonyms; the YAML preserves all 5 synonym entries from that row.
- All 12 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` retains 1 redirect into `NCBITaxon:42210`: `NCBITaxon:1117328`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:35093` reports `organism_count` 1 for `NCBITaxon:42210`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 4 project rows, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 2 exact `reference material` rows for `NCBITaxon:42210`: `ARSEF 6003` and `ARSEF:6003`.
- BacDive has 0 exact local rows for `NCBITaxon:42210`.
- StrainInfo has 12 exact direct strain rows and 15 exact deposit matches for `NCBITaxon:42210`; all deposit matches are on direct records.

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
